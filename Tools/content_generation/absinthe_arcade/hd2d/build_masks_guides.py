"""Build the Absinthe Arcade technical masks and guides from the code's own geometry (bead Eurobound-zx7u).

Everything is derived from the .gd constants (parsed with regexes, so a code change flows through on
re-run) and the approved plates; nothing is generated art. World geometry is projected to plate pixels
with each room's paint camera (the inverse of paint_px_to_floor.px_to_floor).

Outputs (hall plate and north wing plate are separate images, so each interior mask has _hall and
_north_wing files; each PNG has a .json legend beside it):
  masks:   game/assets/worlds/debaucheryville/absinthe_arcade/interior/masks/
             aa_mask_interior_collision_{hall,north_wing}   white = blocked, black = walkable
             aa_mask_interior_interaction_{hall,north_wing} one flat colour per interaction id
             aa_mask_interior_occlusion_{hall,north_wing}   white = an occluder draws in front
             (+ aa_mask_interior_occlusion_hall_ids.png: one flat colour per occluder)
  guides:  Assets/Graphics/worlds/debaucheryville/absinthearcade/guides/
             aa_guide_node_overlay_{hall,north_wing}.png, aa_guide_scale_camera.png (hall)
           aa_mask_interior_interaction_mirror_corridor   the three shadow switches + exits (Desk zx7u-q2)
  exterior (Desk zx7u-q1: a top-down plan of the street, real metres, no plate):
           game/assets/worlds/debaucheryville/absinthe_arcade/exterior/masks/
             aa_mask_exterior_collision     white = blocked, black = walkable
             aa_mask_exterior_occlusion     grey = how much of a bro standing there the follow camera
                                            cannot see (0 visible .. 255 fully hidden)
             (+ aa_mask_exterior_occlusion_ids.png: each occluder's footprint and its hide zone)
  review:  dev/asset_team/reviews/zx7u_<id>_overlay.jpg (each mask at 50% over its plate) and
           zx7u_aa_mask_exterior_plan_labels.jpg (labelled plan of the exterior).

Usage (from anywhere):  python -I Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py
Needs Pillow and numpy. Reads only; writes only the files above.
"""
import colorsys
import importlib.util
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
HD2D = Path(__file__).resolve().parent
GAME = ROOT / "game"
WORLDS = GAME / "worlds/debaucheryville"
INT = GAME / "assets/worlds/debaucheryville/absinthe_arcade/interior"
MASK_DIR = INT / "masks"
GUIDE_DIR = ROOT / "Assets/Graphics/worlds/debaucheryville/absinthearcade/guides"
REVIEW_DIR = ROOT / "dev/asset_team/reviews"
W, H = 2752, 1536


# ---------------------------------------------------------------- GDScript constant parsing
def _scan_expr(text, i):
    """Return the cleaned expression text starting at i (comments dropped) up to the end of the line
    at bracket depth 0."""
    out, depth = [], 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "#":
            while i < n and text[i] != "\n":
                i += 1
            continue
        if c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            out.append(text[i:j + 1])
            i = j + 1
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == "\n" and depth <= 0:
            break
        out.append(c)
        i += 1
    return "".join(out)


def parse_consts(path):
    """All `const NAME := expr` of a .gd file that evaluate as plain data (Vector2 -> tuple)."""
    text = Path(path).read_text(encoding="utf-8")
    ns = {"V": lambda x, y: (float(x), float(y)), "V3": lambda x, y, z: (float(x), float(y), float(z)),
          "true": True, "false": False, "PI": math.pi}
    for m in re.finditer(r"^const\s+(\w+)\s*:=\s*", text, re.M):
        expr = _scan_expr(text, m.end())
        expr = re.sub(r"\bVector2i?\(", "V(", expr)
        expr = re.sub(r"\bVector3i?\(", "V3(", expr)
        try:  # eval on this repo's own .gd constants only, with builtins removed
            ns[m.group(1)] = eval(expr, {"__builtins__": {}}, ns)
        except Exception:
            pass
    return {k: v for k, v in ns.items() if k not in ("V", "V3", "true", "false", "PI")}


def gd_number(path, pattern):
    m = re.search(pattern, Path(path).read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"constant not found in {path}: {pattern}")
    return float(m.group(1))


# ---------------------------------------------------------------- paint camera
class Cam:
    def __init__(self, focal, pitch_deg, cam_h, cam_z, w=W, h=H):
        self.f, self.h0, self.cz, self.w, self.h = focal, cam_h, cam_z, w, h
        self.a = -math.radians(pitch_deg)

    def px_to_floor(self, u, v):
        """Same maths as paint_px_to_floor.px_to_floor, vectorised."""
        dx = (np.asarray(u, np.float64) - self.w / 2) / self.f
        dy = -(np.asarray(v, np.float64) - self.h / 2) / self.f
        wy = dy * math.cos(self.a) + math.sin(self.a)
        wz = dy * math.sin(self.a) - math.cos(self.a)
        t = self.h0 / -wy
        return dx * t, self.cz + wz * t

    def project(self, x, y, z):
        """World (x, y up, z) in painting units to plate pixels (u, v)."""
        rx, ry, rz = x, y - self.h0, z - self.cz
        c, s = math.cos(self.a), math.sin(self.a)
        yc = ry * c + rz * s
        zc = -ry * s + rz * c
        return self.w / 2 + self.f * rx / -zc, self.h / 2 - self.f * yc / -zc

    def floor_px(self, x, z):
        return self.project(x, 0.0, z)


def round_trip(cam, ref_fn=None):
    """Max pixel error of project(px_to_floor(p)) over a grid, and the max floor-position gap to the
    reference px_to_floor of paint_px_to_floor.py (hall only)."""
    us, vs = np.meshgrid(np.linspace(0, W, 23), np.linspace(H * 0.2, H, 17))
    fx, fz = cam.px_to_floor(us, vs)
    err = 0.0
    for u, v, x, z in zip(us.ravel(), vs.ravel(), fx.ravel(), fz.ravel()):
        pu, pv = cam.floor_px(x, z)
        err = max(err, math.hypot(pu - u, pv - v))
    ref_gap = None
    if ref_fn:
        ref_gap = 0.0
        for u, v in zip(us.ravel()[::7], vs.ravel()[::7]):
            rx, rz = ref_fn(float(u), float(v))
            x, z = cam.px_to_floor(u, v)
            ref_gap = max(ref_gap, abs(rx - float(x)), abs(rz - float(z)))
    return err, ref_gap


# ---------------------------------------------------------------- rooms
class Room:
    pass


def build_hall():
    gd = WORLDS / "absinthe_arcade_interior_hd2d.gd"
    c = parse_consts(gd)
    r = Room()
    r.key, r.c, r.gd = "hall", c, gd.relative_to(ROOT).as_posix()
    r.scale = c["WORLD_SCALE"]
    r.cam = Cam(c["PAINT_FOCAL_PX"], c["PAINT_PITCH_DEG"], c["PAINT_CAM_HEIGHT"], c["PAINT_CAM_Z"])
    r.plate = INT / "hall/aa_int_hall_night.png"
    r.interact = c["INTERACT_POINTS"]
    r.stand_off = c["STAND_OFF"]
    r.unit = "painting units (metres at painted-patron scale; real metres = units * WORLD_SCALE)"

    def xat(line, z):
        (x0, z0), (x1, z1) = line
        return x0 + (x1 - x0) * (z - z0) / (z1 - z0)

    bz, fe, fd = c["BACK_WALL_Z"], c["FRONT_EDGE_Z"], c["FRONT_DOOR_X"]
    arch = c["NORTH_ARCH"]
    ax0, ax1 = (arch["x0"], bz), (arch["x1"], bz)
    deep = bz - arch["depth"]
    lb, rb = (xat(c["LEFT_WALL"], bz), bz), (xat(c["RIGHT_WALL"], bz), bz)
    lf, rf = (xat(c["LEFT_WALL"], c["FRONT_Z"]), c["FRONT_Z"]), (xat(c["RIGHT_WALL"], c["FRONT_Z"]), c["FRONT_Z"])
    fl, fr = (xat(c["LEFT_WALL"], fe), fe + 0.15), (xat(c["RIGHT_WALL"], fe), fe + 0.15)
    # Walkable outline: the room to the front-edge wall line, the arch corridor, and the gap between
    # the door leaves out to the wall behind the exit (code: _build_room).
    zf = fe + 0.15
    r.walkable = [
        [lb, ax0, (ax0[0], deep), (ax1[0], deep), ax1, rb, (xat(c["RIGHT_WALL"], zf), zf), (xat(c["LEFT_WALL"], zf), zf)],
        [(-fd, zf), (fd, zf), (fd, fe + 0.6), (-fd, fe + 0.6)],
    ]
    segs = [(lb, ax0), (ax1, rb), (lf, lb), (rb, rf), (ax0, (ax0[0], deep)), ((ax1[0], deep), ax1),
            ((ax0[0], deep), (ax1[0], deep)), (fl, (-fd, fe + 0.15)), ((fd, fe + 0.15), fr),
            ((-fd, fe + 0.6), (fd, fe + 0.6))]
    r.blocked = []  # (id, polygon, source)
    for i, (a, b) in enumerate(segs):
        r.blocked.append((f"wall_{i}", wall_strip(a, b), "_build_room _wall_collider"))
    for i, (ctr, sz) in enumerate(c["FLOOR_BLOCKERS"]):
        r.blocked.append((f"blocker_{i}", box_poly(ctr, sz), "FLOOR_BLOCKERS"))
    r.prisms = {}
    for lid, spec in c["OCCLUDERS"].items():
        r.prisms[lid] = spec
        if not spec.get("collide", True):  # painted mesh only (code: _build_occluders)
            continue
        r.blocked.append((lid, spec["footprint"], "OCCLUDERS footprint collider"))
        if "also" in spec:
            r.blocked.append((lid + "_also", spec["also"], "OCCLUDERS also collider"))
    r.exits = {
        "exit_north_arch": box_poly(((arch["x0"] + arch["x1"]) / 2, c["NORTH_EXIT_Z"] - 0.3),
                                    (arch["x1"] - arch["x0"], 0.6)),
        "exit_front_doors": box_poly((0.0, fe - 0.4), (fd * 2, 0.8)),
    }
    # aa_node_* positions from the code (see the source string on each).
    ip = r.interact
    r.nodes = {
        "aa_node_entry_vestibule": (c["SPAWNS"]["from_street"][0], "SPAWNS.from_street"),
        "aa_node_token_exchange": (c["BARK_NODE_POS"]["aa_node_token_exchange"], "BARK_NODE_POS"),
        "aa_node_bottle_bar": (c["BARK_NODE_POS"]["aa_node_bottle_bar"], "BARK_NODE_POS"),
        "aa_node_main_cabinet_loop": (c["BARK_NODE_POS"]["aa_node_main_cabinet_loop"], "BARK_NODE_POS"),
        "aa_node_claw_alcove": (ip["rigged_absinthe_claw_machine"][0], "INTERACT_POINTS.rigged_absinthe_claw_machine"),
        "aa_node_mirror_corridor": (((arch["x0"] + arch["x1"]) / 2, c["NORTH_EXIT_Z"]), "NORTH_ARCH centre at NORTH_EXIT_Z"),
    }
    r.landmarks = {k: ip[k][0] for k in ("token_machine", "cabinet_frogger", "cabinet_street_fighter",
                                         "ddr_dance_off", "rigged_absinthe_claw_machine")}
    r.landmarks["aa_node_bottle_bar"] = c["BARK_NODE_POS"]["aa_node_bottle_bar"]
    # The north arch's exit trigger; label = its code name (author, Desk zx7u-q3).
    r.landmarks["exit_north_arch"] = r.nodes["aa_node_mirror_corridor"][0]
    r.landmarks["exit_front_doors"] = (0.0, fe)
    return r


def build_north_wing():
    gd = WORLDS / "absinthe_arcade_north_wing_hd2d.gd"
    c = parse_consts(gd)
    r = Room()
    r.key, r.c, r.gd = "north_wing", c, gd.relative_to(ROOT).as_posix()
    r.scale = gd_number(gd, r"world_scale\s*=\s*([\d.]+)")
    r.cam = Cam(gd_number(gd, r"focal_px\s*=\s*([\d.]+)"), gd_number(gd, r"pitch_deg\s*=\s*([\d.]+)"),
                gd_number(gd, r"cam_height\s*=\s*([\d.]+)"), gd_number(gd, r"cam_z\s*=\s*([\d.]+)"))
    r.plate = INT / "north_wing/aa_int_north_wing_night.png"
    r.interact = {k: [v[0], 0.0, v[1]] for k, v in c["INTERACT_POINTS"].items()}
    r.stand_off = 1.0
    r.unit = "tiles (a tile is 0.67 m; real metres = tiles * world_scale)"
    bz, ff = c["BACK_Z"], c["FRONT_Z"]
    lb, lf = c["LEFT_WALL"]
    rb, rf = c["RIGHT_WALL"]
    zs = ff + 1.4
    xl = lambda z: lb[0] + (lf[0] - lb[0]) * (z - lb[1]) / (lf[1] - lb[1])
    xr = lambda z: rb[0] + (rf[0] - rb[0]) * (z - rb[1]) / (rf[1] - rb[1])
    r.walkable = [[(xl(bz), bz), (xr(bz), bz), (xr(zs), zs), (xl(zs), zs)]]
    segs = [(lb, rb), (lf, lb), (rb, rf), ((-8.5, zs), (8.0, zs))]
    r.blocked = []
    for i, (a, b) in enumerate(segs):
        r.blocked.append((f"wall_{i}", wall_strip(a, b), "_build_room _wall_collider"))
    for i, fp in enumerate(c["FLOOR_BLOCKERS"]):
        r.blocked.append((f"blocker_{i}", fp, "FLOOR_BLOCKERS"))
    r.prisms = {}
    r.exits = {"exit_south_to_corridor": box_poly((0.0, ff + 0.5), (16.0, 0.8))}
    sp = c["SPAWNS"]
    r.nodes = {
        "aa_node_north_wing": (sp["from_mirror_corridor"][0], "SPAWNS.from_mirror_corridor"),
        "aa_node_mirror_corridor": ((0.0, ff + 0.5), "exit_south_to_corridor centre"),
        "aa_node_taproom_curtain": (c["INTERACT_POINTS"]["taproom_curtain"][0], "INTERACT_POINTS.taproom_curtain"),
        "aa_node_broken_ddr": (c["INTERACT_POINTS"]["broken_ddr"][0], "INTERACT_POINTS.broken_ddr"),
        "aa_node_maintenance_door": (c["INTERACT_POINTS"]["maintenance_door"][0], "INTERACT_POINTS.maintenance_door"),
    }
    return r


def build_mirror_corridor():
    """Interaction only (author, Desk zx7u-q2: "Yes, make a mirror-corridor interaction mask too, the
    same way"): the three shadow switches and the two exits, through the corridor's paint camera."""
    gd = WORLDS / "absinthe_arcade_mirror_corridor_hd2d.gd"
    c = parse_consts(gd)
    r = Room()
    r.key, r.c, r.gd = "mirror_corridor", c, gd.relative_to(ROOT).as_posix()
    r.scale = gd_number(gd, r"world_scale\s*=\s*([\d.]+)")
    r.cam = Cam(c["PAINT_FOCAL_PX"], c["PAINT_PITCH_DEG"], c["PAINT_CAM_HEIGHT"], c["PAINT_CAM_Z"])
    r.plate = INT / "mirror_corridor/aa_int_corridor_night.png"
    # Ids as the code names them: switch_id(i) = "shadow_switch_%d" % (i + 1); [anchor, yaw, stand].
    r.interact = {f"shadow_switch_{i + 1}": [at, None, stand] for i, (at, stand) in enumerate(c["SWITCHES"])}
    r.stand_off = 1.0
    r.unit = "tiles (a tile is 0.55 m; real metres = tiles * world_scale)"
    a, fz, wx = c["ARCH"], c["FRONT_Z"], c["WALL_X"]
    r.exits = {
        "exit_south_to_hall": box_poly((0.0, fz + 0.4), (wx * 2.0, 0.8)),
        "exit_north_arch": box_poly(((a["x0"] + a["x1"]) / 2, -0.6), (a["x1"] - a["x0"], 0.8)),
    }
    return r


# ---------------------------------------------------------------- exterior (top-down plan)
EXT_DIR = GAME / "assets/worlds/debaucheryville/absinthe_arcade/exterior"
EXT_MASK_DIR = EXT_DIR / "masks"
PLAN_PPM = 100            # plan pixels per real metre
PLAN_HALF = 12.5          # the plan covers x, z in [-12.5, 12.5] m (street edge walls reach 12.2)
PLAN_N = int(PLAN_HALF * 2 * PLAN_PPM)


def plan_px(x, z):
    """Real metres to plan pixels: +X to the right, -Z (behind the building) up, so the camera side
    of the street (+Z) is at the bottom, as in the game view."""
    return (x + PLAN_HALF) * PLAN_PPM, (z + PLAN_HALF) * PLAN_PPM


def rect(centre, u, v):
    """A flat rectangle: centre and two half-axis vectors (3D, real metres)."""
    return {"c": np.array(centre, float), "u": np.array(u, float), "v": np.array(v, float)}


def build_exterior():
    gd = WORLDS / "absinthe_arcade_exterior_hd2d.gd"
    c = parse_consts(gd)
    ps = c["PAINT_SCALE"]
    faces = json.loads((EXT_DIR / "faces/faces.json").read_text(encoding="utf-8"))["faces"]
    pj = json.loads((EXT_DIR / "props/props.json").read_text(encoding="utf-8"))
    pppm = float(pj["ppm"])

    def size(pid):  # props.json texture px -> real metres (px / ppm * PAINT_SCALE painting units / PAINT_SCALE)
        tx, ty = pj["props"][pid]["texture_px"]
        return tx / pppm, ty / pppm

    r = Room()
    r.key, r.c, r.gd = "exterior", c, gd.relative_to(ROOT).as_posix()
    w = faces["aa_face_front"]["wall_width_m"] / ps
    d = c["DEPTH_M"] / ps
    roof = c["ROOF_DECK_M"] / ps
    e = c["STREET_HALF_EXTENT"]
    r.walkable = [box_poly((0.0, 0.0), (e * 2.0, e * 2.0))]
    r.blocked = [("building", box_poly((0.0, -d / 2), (w, d)), "_build_walkable building box")]
    for i, (ctr, sz) in enumerate(c["SOLID_PROPS"]):
        r.blocked.append((f"solid_prop_{i}", box_poly(ctr, sz), "SOLID_PROPS"))
    for name, ctr, sz in (("edge_east", (e, 0), (0.4, e * 2)), ("edge_west", (-e, 0), (0.4, e * 2)),
                          ("edge_south", (0, e), (e * 2, 0.4)), ("edge_north", (0, -e), (e * 2, 0.4))):
        r.blocked.append((name, box_poly(ctr, sz), "_build_walkable street edge"))
    for i, fp in enumerate(c.get("FLOOR_BLOCKERS", [])):  # convex prisms (code: _footprint)
        r.blocked.append((f"blocker_{i}", list(fp), "FLOOR_BLOCKERS"))
    door_w = c["DOOR_HALF_WIDTH_M"] * 2.0 - 0.4
    r.exits = {"exit_front_door": box_poly((0.0, 0.2), (door_w, 0.5))}
    r.spawns = {"start": (0.5, 5.0), "from_arcade": (0.0, 1.4)}

    # Follow camera: fixed offset from the focus (leader + CAM_FOCUS_HEIGHT), so the ray from a bro
    # to the camera has the same direction wherever the leader stands.
    pitch, yaw = math.radians(c["CAM_PITCH_DEG"]), math.radians(c["CAM_YAW_DEG"])
    dist = c["CAM_DISTANCE_M"]
    r.cam_offset = np.array([math.sin(yaw) * math.cos(pitch), math.sin(pitch), math.cos(yaw) * math.cos(pitch)]) * dist
    r.focus_h = np.array(c["CAM_FOCUS_HEIGHT"], float)
    face = np.array([math.sin(yaw), 0.0, math.cos(yaw)])   # billboards turn to the camera (FIXED_Y)
    side = np.array([face[2], 0.0, -face[0]])

    lay = {}
    for ent in c["PROP_LAYOUT"]:
        lay.setdefault(ent["id"], []).append(ent)
    occ = []  # (id, kind, boxes [(min xyz, max xyz)], rects, source)

    def P(v3):
        return np.array(v3, float) / ps

    occ.append(("building", "box", [((-w / 2, 0, -d), (w / 2, roof, 0))], [],
                f"{r.gd} _build_building (faces.json wall_width_m / PAINT_SCALE, DEPTH_M, ROOF_DECK_M); "
                "relief recesses, roof cresting and chimneys are not modelled"))
    cab = P(lay["aa_prop_cabinet"][0]["pos"])
    fw, fh = size("aa_prop_cabinet_front")
    dep = c["CABINET_DEPTH_REAL_M"]
    occ.append(("aa_prop_cabinet", "box", [((cab[0] - fw / 2, 0, cab[2]), (cab[0] + fw / 2, fh, cab[2] + dep))], [],
                f"{r.gd} PROP_LAYOUT + _build_cabinet (front card at CABINET_DEPTH_REAL_M)"))
    aw = P(lay["aa_prop_awning"][0]["pos"])
    a_w, reach, drop = c["AWNING_WIDTH_REAL_M"], c["AWNING_REACH_REAL_M"], c["AWNING_DROP_REAL_M"]
    with Image.open(EXT_DIR / "props/aa_prop_awning_day.png") as im:
        tw, th = im.size
    vh = a_w * (1.0 - c["AWNING_VALANCE_V"]) * th / tw          # valance card height (code: vh)
    bx, by = size("aa_prop_awning_bracket")
    bh = by * reach / bx                                        # bracket scaled so its width = reach
    tube = 0.018                                                # iron tube radius r (0.018 * PAINT_SCALE painting units)
    brk = [rect((aw[0] + s * (a_w / 2 - tube), aw[1] - drop - bh / 2 + tube, aw[2] + reach / 2), (0, 0, reach / 2), (0, bh / 2, 0))
           for s in (-1, 1)]
    occ.append(("aa_prop_awning", "box+cards", [((aw[0] - a_w / 2, aw[1] - drop - vh + tube, aw[2]), (aw[0] + a_w / 2, aw[1], aw[2] + reach))],
                brk, f"{r.gd} _build_awning (canopy + valance as one box; the two brackets as side-profile cards)"))
    ch = P(lay["aa_prop_chalkboard"][0]["pos"])
    cw, chh = size("aa_prop_chalkboard")
    tilt = math.radians(lay["aa_prop_chalkboard"][0].get("tilt", 12.0))
    up_f = np.array([0, math.cos(tilt), -math.sin(tilt)]) * chh    # front board leans back (-Z)
    back_z = ch[2] - 2.0 * chh * math.sin(tilt)
    up_b = np.array([0, math.cos(tilt), math.sin(tilt)]) * chh     # back board leans forward (+Z)
    occ.append(("aa_prop_chalkboard", "cards", [], [
        rect(np.array([ch[0], 0, ch[2]]) + up_f / 2, (cw / 2, 0, 0), up_f / 2),
        rect(np.array([ch[0], 0, back_z]) + up_b / 2, (cw / 2, 0, 0), up_b / 2)],
        f"{r.gd} PROP_LAYOUT + _build_aframe (two boards, tilt {math.degrees(tilt):g} deg)"))
    for pid in ("aa_prop_metal_bucket", "aa_prop_potted_shrub", "aa_prop_bollard"):
        bw, bhh = size(pid)
        for k, ent in enumerate(lay[pid]):
            p = P(ent["pos"])
            oid = pid if len(lay[pid]) == 1 else f"{pid}_{k + 1}"
            occ.append((oid, "billboard", [], [rect((p[0], p[1] + bhh / 2, p[2]), side * bw / 2, (0, bhh / 2, 0))],
                        f"{r.gd} PROP_LAYOUT (billboard, turned to the camera yaw)"))
    for pid in ("aa_prop_wall_sign_tokens", "aa_prop_wall_lantern_side", "aa_prop_wall_lantern_front"):
        ent = lay[pid][0]
        p = P(ent["pos"])
        sw, sh = size(pid)
        ry = math.radians(float(ent.get("rot_y", 0.0)))
        across = np.array([math.cos(ry), 0.0, -math.sin(ry)])  # a card's local +X after rot_y
        occ.append((pid, "card", [], [rect((p[0], p[1] + sh / 2, p[2]), across * sw / 2, (0, sh / 2, 0))],
                    f"{r.gd} PROP_LAYOUT (card, rot_y {math.degrees(ry):g})"))
    r.occluders = occ
    r.not_modelled = {
        "door leaves": "no door-leaf geometry in the exterior code (the doorway is a relief recess on aa_face_front; doors are bead d4i6)",
        "flyer panel": "flat overlay cards 0.06 painting units off the front face: they cannot stand between a bro and the camera",
        "wifi hotspot / examine points": "markers and a hidden Label3D only, no visible mesh",
        "night lights": "lights only, no geometry",
    }
    return r


def _hidden(r, xs, zs, heights):
    """For each floor point, how many of the bro's sample heights the camera cannot see, and which
    occluder hides the most of them. xs, zs: flat arrays (real metres)."""
    n = xs.size
    count = np.zeros(n, np.int16)
    per = np.zeros((len(r.occluders), n), np.int16)
    for hy in heights:
        dvec = r.focus_h + r.cam_offset - np.array([0.0, hy, 0.0])   # same for every floor point
        o = np.stack([xs, np.full(n, hy), zs], axis=1)
        any_hit = np.zeros(n, bool)
        for k, (_oid, _kind, boxes, rects, _src) in enumerate(r.occluders):
            hit = np.zeros(n, bool)
            for lo, hi in boxes:
                t0, t1 = np.zeros(n), np.ones(n)
                inside = np.ones(n, bool)
                for ax in range(3):
                    if abs(dvec[ax]) < 1e-12:
                        inside &= (o[:, ax] >= lo[ax]) & (o[:, ax] <= hi[ax])
                        continue
                    a = (lo[ax] - o[:, ax]) / dvec[ax]
                    b = (hi[ax] - o[:, ax]) / dvec[ax]
                    t0 = np.maximum(t0, np.minimum(a, b))
                    t1 = np.minimum(t1, np.maximum(a, b))
                hit |= inside & (t0 <= t1) & (t1 > 1e-6)
            for rc in rects:
                nrm = np.cross(rc["u"], rc["v"])
                den = float(dvec @ nrm)
                if abs(den) < 1e-12:
                    continue
                t = ((rc["c"] - o) @ nrm) / den
                q = o + np.outer(t, dvec) - rc["c"]
                su = (q @ rc["u"]) / float(rc["u"] @ rc["u"])
                sv = (q @ rc["v"]) / float(rc["v"] @ rc["v"])
                hit |= (t > 1e-6) & (t < 1.0) & (np.abs(su) <= 1) & (np.abs(sv) <= 1)
            per[k] += hit
            any_hit |= hit
        count += any_hit
    return count, per


def exterior_images(r):
    """Collision, occlusion (hidden fraction) and occlusion ids, all PLAN_N x PLAN_N."""
    to_px = lambda poly: [plan_px(x, z) for x, z in poly]
    col = Image.new("L", (PLAN_N, PLAN_N), 255)
    dc = ImageDraw.Draw(col)
    for poly in r.walkable:
        dc.polygon(to_px(poly), fill=0)
    for _i, poly, _s in r.blocked:
        dc.polygon(to_px(poly), fill=255)
    walk = np.asarray(col) < 128
    h_m = gd_number(GAME / "characters/party/party_sprite_3d.gd", r"var height_m := ([\d.]+)")
    heights = [h_m * (i + 0.5) / 5 for i in range(5)]
    hid = np.zeros((PLAN_N, PLAN_N), np.uint8)
    who = np.full((PLAN_N, PLAN_N), -1, np.int16)
    for y0 in range(0, PLAN_N, 125):
        vv, uu = np.mgrid[y0:min(y0 + 125, PLAN_N), 0:PLAN_N]
        xs = (uu + 0.5) / PLAN_PPM - PLAN_HALF
        zs = (vv + 0.5) / PLAN_PPM - PLAN_HALF
        m = walk[vv, uu]
        cnt, per = _hidden(r, xs[m], zs[m], heights)
        blk = hid[y0:y0 + vv.shape[0]]
        blk[m] = np.round(cnt * 255 / len(heights)).astype(np.uint8)
        wb = who[y0:y0 + vv.shape[0]]
        top = np.where(per.max(axis=0) > 0, per.argmax(axis=0), -1)
        wb[m] = top
    occ = Image.fromarray(hid, "L")
    cols = palette(len(r.occluders), 0.07)
    rgb = np.zeros((PLAN_N, PLAN_N, 3), np.uint8)
    for k, cc in enumerate(cols):
        rgb[who == k] = (np.array(cc) * 0.55).astype(np.uint8)
    ids = Image.fromarray(rgb, "RGB")
    di = ImageDraw.Draw(ids)
    legend, footprints = {}, {}
    for k, ((oid, kind, boxes, rects, src), cc) in enumerate(zip(r.occluders, cols)):
        polys = [[(lo[0], lo[2]), (hi[0], lo[2]), (hi[0], hi[2]), (lo[0], hi[2])] for lo, hi in boxes]
        for rc in rects:  # floor footprint of a card: its extent along x/z, at least 4 cm thick
            cxz = rc["c"][[0, 2]]
            ext = np.abs(rc["u"][[0, 2]]) + np.abs(rc["v"][[0, 2]])
            ext = np.maximum(ext, 0.02)
            polys.append([(cxz[0] - ext[0], cxz[1] - ext[1]), (cxz[0] + ext[0], cxz[1] - ext[1]),
                          (cxz[0] + ext[0], cxz[1] + ext[1]), (cxz[0] - ext[0], cxz[1] + ext[1])])
        for poly in polys:
            di.polygon(to_px(poly), fill=tuple(cc), outline=(255, 255, 255))
        footprints[oid] = polys
        ys = [lo[1] for lo, _ in boxes] + [hi[1] for _, hi in boxes]
        for rc in rects:
            ys += [rc["c"][1] - abs(rc["v"][1]) - abs(rc["u"][1]), rc["c"][1] + abs(rc["v"][1]) + abs(rc["u"][1])]
        zone = int((who == k).sum())
        legend[oid] = {"kind": kind, "color": hexc(cc), "rgb": list(cc), "hide_zone_color": hexc((np.array(cc) * 0.55).astype(int)),
                       "height_range_m": [round(min(ys), 3), round(max(ys), 3)],
                       "footprint_xz_m": [[[round(p[0], 3), round(p[1], 3)] for p in poly] for poly in polys],
                       "hide_zone_m2": round(zone / PLAN_PPM ** 2, 2), "source": src}
    return col, occ, ids, legend, footprints, heights, h_m


def exterior(r):
    col, occ, ids, oleg, footprints, heights, h_m = exterior_images(r)
    off = [round(float(t), 3) for t in r.cam_offset]
    notes = {"size_px": [PLAN_N, PLAN_N], "view": "top-down plan of the street (author, Desk zx7u-q1)",
             "units": "real metres (the exterior world is in real metres; the diorama is scaled by 1/PAINT_SCALE)",
             "pixel_per_m": PLAN_PPM,
             "transform": f"px = (x + {PLAN_HALF}) * {PLAN_PPM}, py = (z + {PLAN_HALF}) * {PLAN_PPM}; +X right, -Z (behind the building) up, so the camera side of the street is at the bottom",
             "origin": "centre of the front wall base (x 0, z 0)",
             "source": r.gd, "generator": "Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py"}
    EXT_MASK_DIR.mkdir(parents=True, exist_ok=True)

    def save(im, name, legend):
        im.save(EXT_MASK_DIR / f"{name}.png", optimize=True)
        doc = dict(notes, file=f"{name}.png")
        doc.update(legend)
        (EXT_MASK_DIR / f"{name}.json").write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")

    save(col, "aa_mask_exterior_collision", {
        "classes": {"255": "blocked", "0": "walkable"},
        "meaning": "floor footprint of the street's colliders: the ground box (STREET_HALF_EXTENT), its four 0.4 m edge walls, the building box, SOLID_PROPS and FLOOR_BLOCKERS. Raw geometry: the 0.25 m player capsule is not added.",
        "elements": [{"id": i, "source": f"{r.gd} {s}", "polygon_xz_m": [[round(p[0], 4), round(p[1], 4)] for p in poly]} for i, poly, s in r.blocked],
        "triggers_not_blocking": {"exit_front_door": {"polygon_xz_m": [[round(p[0], 4), round(p[1], 4)] for p in r.exits["exit_front_door"]],
                                                      "target": "absinthe_arcade_interior / from_street"}},
        "spawns_xz_m": r.spawns})
    save(occ, "aa_mask_exterior_occlusion", {
        "classes": {"0": "a bro standing here is fully visible", "51/102/153/204": "1-4 of 5 body sample heights hidden", "255": "fully hidden"},
        "meaning": "Seen from above: for every walkable floor point, how much of a bro standing there the follow camera cannot see. Rays go from the bro's centre line at 5 heights to the camera; anything solid in between hides that height. Blocked floor is 0 (no bro stands there). The footprints of the things that hide the bros are in aa_mask_exterior_occlusion_ids.png.",
        "camera": {"pitch_deg": r.c["CAM_PITCH_DEG"], "yaw_deg": r.c["CAM_YAW_DEG"], "distance_m": r.c["CAM_DISTANCE_M"],
                   "fov_deg": r.c["CAM_FOV"], "focus_height_m": list(r.c["CAM_FOCUS_HEIGHT"]), "offset_m": off,
                   "rule": "the Phantom Camera follows the leader at a fixed offset (_build_camera), so the ray from the leader to the camera has one direction everywhere. Computed for the leader; the two followers stand a step behind and use the leader's camera. Follow damping is ignored."},
        "bro": {"height_m": h_m, "sample_heights_m": [round(h, 3) for h in heights], "width": "centre line only (sprite width not added)"},
        "companion": "aa_mask_exterior_occlusion_ids.png",
        "not_modelled": r.not_modelled})
    ids.save(EXT_MASK_DIR / "aa_mask_exterior_occlusion_ids.png", optimize=True)
    (EXT_MASK_DIR / "aa_mask_exterior_occlusion_ids.json").write_text(json.dumps(dict(notes, file="aa_mask_exterior_occlusion_ids.png",
        classes="black = nothing; full colour = an occluder's floor footprint (white outline); the same colour at 55% = the floor where it hides the most of a bro",
        occluders=oleg), indent=1) + "\n", encoding="utf-8")
    plan_review(r, col, occ, footprints, oleg)
    hidden_any = int((np.asarray(occ) > 0).sum())
    print(f"exterior: walkable {int((np.asarray(col) < 128).sum()) / PLAN_PPM ** 2:.1f} m2, "
          f"some bro hidden on {hidden_any / PLAN_PPM ** 2:.1f} m2, fully hidden on {int((np.asarray(occ) == 255).sum()) / PLAN_PPM ** 2:.1f} m2")


def plan_review(r, col, occ, footprints, oleg):
    """Labelled plan for the reviewer and the author: blocked grey, hide zones red by depth, every
    occluder footprint named, the exit, the spawns, the camera direction and a metre scale."""
    base = np.zeros((PLAN_N, PLAN_N, 3), np.uint8)
    base[np.asarray(col) > 127] = (70, 70, 78)
    base[np.asarray(col) <= 127] = (26, 30, 34)
    h = np.asarray(occ).astype(np.float32) / 255
    m = h > 0
    base[m] = (np.array([40, 30, 40]) * (1 - h[m, None]) + np.array([235, 60, 70]) * h[m, None]).astype(np.uint8)
    im = Image.fromarray(base, "RGB")
    d = ImageDraw.Draw(im)
    for x in range(-12, 13):  # 1 m grid
        u, _ = plan_px(x, 0)
        d.line((u, 0, u, PLAN_N), fill=(50, 54, 60) if x else (90, 96, 104), width=1)
        _, v = plan_px(0, x)
        d.line((0, v, PLAN_N, v), fill=(50, 54, 60) if x else (90, 96, 104), width=1)
    to_px = lambda poly: [plan_px(x, z) for x, z in poly]
    for oid, polys in footprints.items():
        for poly in polys:
            d.polygon(to_px(poly), fill=tuple(oleg[oid]["rgb"]), outline=(255, 255, 255))
    d.polygon(to_px(r.exits["exit_front_door"]), outline=(90, 230, 255), width=5)
    f, fb = font(30), font(34, True)
    # Labels keep clear of every footprint, the exit box, the spawns and each other.
    boxes = []
    for polys in list(footprints.values()) + [[r.exits["exit_front_door"]]]:
        for poly in polys:
            pp = to_px(poly)
            boxes.append((min(p[0] for p in pp) - 4, min(p[1] for p in pp) - 4, max(p[0] for p in pp) + 4, max(p[1] for p in pp) + 4))
    for x, z in r.spawns.values():
        u, v = plan_px(x, z)
        boxes.append((u - 16, v - 16, u + 16, v + 16))
    for name, (x, z) in r.spawns.items():
        u, v = plan_px(x, z)
        d.ellipse((u - 12, v - 12, u + 12, v + 12), fill=(120, 255, 140), outline=(0, 0, 0), width=3)
        boxes.append(label(d, (u + 20, v), f"spawn {name}", f, fill=(160, 255, 170), anchor="lm"))
    u, v = plan_px(0, 0.45)
    boxes.append(label(d, (u - 30, v + 60), "exit_front_door", f, fill=(140, 235, 255), anchor="ra"))
    for oid, polys in footprints.items():
        xs = [p[0] for poly in polys for p in poly]
        zs = [p[1] for poly in polys for p in poly]
        tx, ty = plan_px((min(xs) + max(xs)) / 2, (min(zs) + max(zs)) / 2)
        text = oid.replace("aa_prop_", "")
        tw = d.textlength(text, font=f)
        big = (max(xs) - min(xs)) * PLAN_PPM > tw + 40
        for rr in ((0,) if big else ()) + (90, 150, 220, 300, 390, 480, 580):
            done = False
            for ang in (270, 90, 0, 180, 315, 225, 45, 135, 300, 240, 60, 120):
                cx, cy = tx + rr * math.cos(math.radians(ang)), ty - rr * math.sin(math.radians(ang))
                box = (cx - tw / 2 - 6, cy - 22, cx + tw / 2 + 6, cy + 22)
                if box[0] < 4 or box[2] > PLAN_N - 4 or box[1] < 180 or box[3] > PLAN_N - 4:
                    continue
                roomy = (box[0] - 10, box[1] - 10, box[2] + 10, box[3] + 10)
                if any(overlaps(roomy, b) for b in boxes if not (rr == 0 and b[0] <= box[0] and b[2] >= box[2] and b[1] <= box[1] and b[3] >= box[3])):
                    continue
                if rr:
                    d.line((tx, ty, cx, cy), fill=(255, 255, 255), width=2)
                d.rectangle(box, fill=(0, 0, 0), outline=tuple(oleg[oid]["rgb"]), width=2)
                d.text((cx, cy), text, font=f, fill=(255, 255, 255), anchor="mm")
                boxes.append(box)
                done = True
                break
            if done:
                break
    # camera direction (from a bro toward the camera, horizontal part)
    ox, oz = r.cam_offset[0], r.cam_offset[2]
    sx, sy = plan_px(8.5, 6.0)
    k = 2.6 / math.hypot(ox, oz)
    ex, ey = plan_px(8.5 + ox * k, 6.0 + oz * k)
    d.line((sx, sy, ex, ey), fill=(255, 230, 90), width=8)
    d.polygon([(ex, ey), (ex - 26 * ox * k / 2.6 + 14, ey - 26 * oz * k / 2.6), (ex - 26 * ox * k / 2.6 - 14, ey - 26 * oz * k / 2.6)], fill=(255, 230, 90))
    label(d, (sx, sy - 20), "toward camera", fb, fill=(255, 230, 90), anchor="md")
    # scale bar
    x0, y0 = plan_px(-11.5, 11.2)
    d.rectangle((x0, y0, x0 + 5 * PLAN_PPM, y0 + 14), fill=(255, 255, 255))
    label(d, (x0, y0 - 10), "5 m", fb, anchor="ld")
    head = ["EXTERIOR, top-down plan (real metres). Grey: blocked. Dark: walkable.",
            "Red: floor where the follow camera loses a bro (bright = fully hidden).",
            "Coloured boxes: the things that hide bros, by their floor footprint."]
    hy = 14
    for t in head:
        label(d, (20, hy), t, fb, anchor="la")
        hy += 56
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    im.save(REVIEW_DIR / "zx7u_aa_mask_exterior_plan_labels.jpg", quality=88)


def wall_strip(a, b, thick=0.3):
    dx, dz = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dz) or 1.0
    px, pz = -dz / n * thick / 2, dx / n * thick / 2
    return [(a[0] + px, a[1] + pz), (b[0] + px, b[1] + pz), (b[0] - px, b[1] - pz), (a[0] - px, a[1] - pz)]


def box_poly(ctr, size):
    cx, cz = ctr
    sx, sz = size[0] / 2, size[1] / 2
    return [(cx - sx, cz - sz), (cx + sx, cz - sz), (cx + sx, cz + sz), (cx - sx, cz + sz)]


# ---------------------------------------------------------------- raster helpers
def poly_px(room, poly):
    return [tuple(round(t) for t in room.cam.floor_px(x, z)) for x, z in poly]


def collision_image(room):
    im = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(im)
    for poly in room.walkable:
        d.polygon(poly_px(room, poly), fill=0)
    for _id, poly, _src in room.blocked:
        d.polygon(poly_px(room, poly), fill=255)
    return im


def palette(n, offset=0.0):
    cols = []
    for i in range(n):
        h = (offset + i * 0.381966) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.85 if i % 2 else 0.6, 0.95)
        cols.append((round(r * 255), round(g * 255), round(b * 255)))
    return cols


def hexc(c):
    return "#%02x%02x%02x" % tuple(c)


def interaction_image(room):
    pts = room.interact
    ids = list(pts.keys())
    cols = palette(len(ids) + len(room.exits))
    rng = 1.0 / room.scale  # INTERACT_RANGE 1.0 m in painting units
    best = np.full((H, W), np.inf, np.float32)
    which = np.full((H, W), -1, np.int16)
    for y0 in range(0, H, 256):
        vv, uu = np.mgrid[y0:min(y0 + 256, H), 0:W]
        fx, fz = room.cam.px_to_floor(uu, vv)
        for k, i in enumerate(ids):
            ax, az = pts[i][0]
            d = np.hypot(fx - ax, fz - az).astype(np.float32)
            sl = slice(y0, y0 + d.shape[0])
            upd = (d <= rng) & (d < best[sl])
            best[sl][upd] = d[upd]
            which[sl][upd] = k
    palette_arr = np.array(cols[:len(ids)], np.uint8)
    rgb = np.zeros((H, W, 3), np.uint8)
    m = which >= 0
    rgb[m] = palette_arr[which[m]]
    im = Image.fromarray(rgb, "RGB")
    d = ImageDraw.Draw(im)
    legend = {}
    for k, i in enumerate(ids):
        spec = pts[i]
        stand = spec[2] if len(spec) > 2 else None
        if stand is None:
            # the way the machine faces: Vector2(0, 1).rotated(-yaw) = (-sin(a), cos(a)) with a = -yaw
            a = -math.radians(float(spec[1]))
            ox, oz = -math.sin(a), math.cos(a)
            stand = (spec[0][0] + ox * room.stand_off, spec[0][1] + oz * room.stand_off)
        legend[i] = {"kind": "interact", "color": hexc(cols[k]), "rgb": list(cols[k]),
                     "anchor_xz": list(spec[0]), "anchor_px": [round(t, 1) for t in room.cam.floor_px(*spec[0])],
                     "stand_xz": [round(t, 3) for t in stand],
                     "facing_yaw_deg": spec[1], "radius_units": round(rng, 4), "radius_m": 1.0,
                     "source": f"{room.gd} INTERACT_POINTS.{i}"}
    for j, (eid, poly) in enumerate(room.exits.items()):
        col = cols[len(ids) + j]
        d.polygon(poly_px(room, poly), fill=col)
        legend[eid] = {"kind": "exit", "color": hexc(col), "rgb": list(col),
                       "polygon_xz": [list(p) for p in poly], "source": f"{room.gd} _build_markers {eid}"}
        pp = [room.cam.floor_px(x, z) for x, z in poly]
        if all(v >= H for _u, v in pp) or all(v < 0 for _u, v in pp):
            legend[eid]["off_plate"] = "the trigger lies outside the plate (below the screen's bottom edge), so it does not appear in the image"
    return im, legend


# ---------------------------------------------------------------- occlusion
def occlusion_images(room):
    """Hall only: the depth-layer outlines (JSON, plate pixels) plus the prop cut-outs, each with its
    sort depth from the code."""
    polys = json.loads((HD2D / "interior_layer_polys.json").read_text(encoding="utf-8"))["layers"]
    items = []  # (id, sort_z or None, [pixel polygons] | alpha ndarray placed, meta)
    for lid, spec in polys.items():
        pr = room.prisms.get(lid)
        meta = {"kind": "depth_layer", "source": "interior_layer_polys.json (pixels)"}
        if pr:
            fp = pr["footprint"] + pr.get("also", [])
            meta.update({"sort_depth_z": max(p[1] for p in fp), "footprint_z_range": [min(p[1] for p in fp), max(p[1] for p in fp)],
                         "prism_height_units": pr["height"],
                         "sort_note": "prism front face z (painting units, -Z = toward the back wall); bros nearer than this draw in front",
                         "prism_source": f"{room.gd} OCCLUDERS.{lid}"})
            if "sort_z" in pr:  # a prism along the side walls: its z range is not its depth (see the code comment)
                meta.update({"sort_depth_z": pr["sort_z"],
                             "sort_note": f"explicit OCCLUDERS.{lid}.sort_z: the prisms are strips along the side walls, behind every walkable spot, so every bro draws in front"})
            if not pr.get("collide", True):
                meta["collider"] = "none (painted mesh only)"
        else:
            meta.update({"sort_depth_z": None,
                         "sort_note": "no prism in code for this layer: the outline is in the cut-out JSON only, no sort depth is defined"})
        items.append((lid, meta.get("sort_depth_z"), [[tuple(p) for p in poly] for poly in spec["polys"]], None, meta))
    props = room.c["PROPS"]
    pdir = INT / "hall/props"
    for pid, (jfile, prefix, z, state) in props.items():
        js = json.loads((pdir / jfile).read_text(encoding="utf-8"))["sprites"]
        key = next((k for k in js if k.startswith(f"{prefix}_{state}_night") or k == f"{prefix}.png"), None)
        if key is None:
            key = next((k for k in js if k.startswith(prefix) and k.endswith("_night.png")), None)
        if key is None:
            continue
        s = js[key]
        a = np.array(Image.open(pdir / key).convert("RGBA"))[..., 3] > 127
        meta = {"kind": "prop_cutout", "sort_depth_z": z, "state_file": key, "rect_px": [s["x"], s["y"], s["w"], s["h"]],
                "sort_note": "quad depth z (painting units); source " + f"{room.gd} PROPS.{pid}"}
        items.append((pid, z, None, (s["x"], s["y"], a), meta))
    # farthest first so the nearest occluder is on top in the id image; unknown depth goes first
    items.sort(key=lambda t: (t[1] is not None, t[1] if t[1] is not None else 0))
    cols = palette(len(items), 0.13)
    white = Image.new("L", (W, H), 0)
    ids_im = Image.new("RGB", (W, H), (0, 0, 0))
    dw, di = ImageDraw.Draw(white), ImageDraw.Draw(ids_im)
    legend = {}
    for (oid, z, polys_px, alpha, meta), col in zip(items, cols):
        if polys_px:
            for poly in polys_px:
                dw.polygon(poly, fill=255)
                di.polygon(poly, fill=col)
        else:
            x0, y0, a = alpha
            m = Image.fromarray((a * 255).astype(np.uint8), "L")
            white.paste(255, (x0, y0), m)
            ids_im.paste(col, (x0, y0), m)
        legend[oid] = dict(meta, color=hexc(col), rgb=list(col))
    return white, ids_im, legend


# ---------------------------------------------------------------- IO helpers
def save_mask(im, name, legend, notes):
    MASK_DIR.mkdir(parents=True, exist_ok=True)
    im.save(MASK_DIR / f"{name}.png", optimize=True)
    doc = dict(notes)
    doc["file"] = f"{name}.png"
    doc["generator"] = "Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py"
    doc.update(legend)
    (MASK_DIR / f"{name}.json").write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")


def review(mask, plate, name, tint):
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    base = Image.open(plate).convert("RGB")
    m = mask.convert("RGB")
    if tint is not None:  # single-channel masks: white -> tint colour
        arr = np.asarray(mask.convert("L")) > 127
        t = np.zeros((H, W, 3), np.uint8)
        t[arr] = tint
        m = Image.fromarray(t, "RGB")
        cover = Image.fromarray((arr * 128).astype(np.uint8), "L")
    else:
        cover = Image.fromarray((np.asarray(mask.convert("RGB")).any(axis=2) * 128).astype(np.uint8), "L")
    base.paste(m, (0, 0), cover)
    base.save(REVIEW_DIR / f"zx7u_{name}_overlay.jpg", quality=86)


def font(size, bold=False):
    for f in ("arialbd.ttf" if bold else "arial.ttf", "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            pass
    return ImageFont.load_default(size)


def common_notes(room):
    cam = room.cam
    return {"plate": room.plate.relative_to(ROOT).as_posix(), "size_px": [W, H],
            "units": room.unit, "world_scale": room.scale,
            "camera": {"focal_px": cam.f, "pitch_deg": round(-math.degrees(cam.a), 3), "cam_height": cam.h0, "cam_z": cam.cz,
                       "source": room.gd, "method": "world (x, 0, z) -> pixel through the paint camera (inverse of paint_px_to_floor.px_to_floor)"},
            "naming": "interior spans two plates: *_hall.png is the main hall plate, *_north_wing.png the north wing plate"}


# ---------------------------------------------------------------- guides
def label(d, xy, text, f, fill=(255, 255, 255), bg=(0, 0, 0, 190), anchor="la", pad=6):
    bbox = d.textbbox(xy, text, font=f, anchor=anchor)
    box = (bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad)
    d.rectangle(box, fill=bg)
    d.text(xy, text, font=f, fill=fill, anchor=anchor)
    return box


def overlaps(a, b):
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])


def node_overlay(room, out_name):
    plate = Image.open(room.plate).convert("RGBA")
    plate = Image.blend(plate, Image.new("RGBA", plate.size, (0, 0, 0, 255)), 0.28)
    layer = Image.new("RGBA", plate.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f = font(40, True)
    boxes, out = [], {}
    for nid, ((x, z), src) in room.nodes.items():
        u, v = room.cam.floor_px(x, z)
        out[nid] = {"anchor_xz": [x, z], "anchor_px": [round(u, 1), round(v, 1)], "source": f"{room.gd} {src}"}
        if not (0 <= u < W and 0 <= v < H):
            out[nid]["off_plate"] = "anchor is outside the plate; the dot is clamped to the edge"
        u, v = clamp(u, 40, W - 40), clamp(v, 40, H - 40)
        d.ellipse((u - 18, v - 18, u + 18, v + 18), fill=(255, 220, 40, 255), outline=(0, 0, 0, 255), width=5)
        w = d.textlength(nid, font=f)
        lx = clamp(u, w / 2 + 12, W - w / 2 - 12)
        ty = min(v - 70, H - 140)
        while True:
            box = (lx - w / 2 - 6, ty - 6, lx + w / 2 + 6, ty + 46)
            if not any(overlaps(box, b) for b in boxes) or ty < 40:
                break
            ty -= 58
        d.line((u, v - 18, lx, ty + 46), fill=(255, 220, 40, 255), width=4)
        label(d, (lx, ty), nid, f, fill=(255, 240, 120), anchor="ma")
        boxes.append(box)
    im = Image.alpha_composite(plate, layer).convert("RGB")
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    im.quantize(256, Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(GUIDE_DIR / f"{out_name}.png", optimize=True)
    notes = {"file": f"{out_name}.png", "plate": room.plate.relative_to(ROOT).as_posix(),
             "nodes": out,
             "not_placed": {"aa_node_exterior_approach": "exterior, no interior plate",
                            "aa_node_taproom_transition": "non-walkable, behind the curtain, other room",
                            "aa_node_restroom_transition": "non-walkable, behind the maintenance door, other room"},
             "note": "Positions are the code's (see each source). Nodes with no INTERACT_POINTS entry use the nearest code anchor named in source.",
             "generator": "Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py"}
    (GUIDE_DIR / f"{out_name}.json").write_text(json.dumps(notes, indent=1) + "\n", encoding="utf-8")
    return im


def floor_grid(room, cell=0.04, erode_units=0.0):
    pts = [p for poly in room.walkable for p in poly]
    x0, x1 = min(p[0] for p in pts) - 1, max(p[0] for p in pts) + 1
    z0, z1 = min(p[1] for p in pts) - 1, max(p[1] for p in pts) + 1
    nx, nz = int((x1 - x0) / cell), int((z1 - z0) / cell)
    to = lambda poly: [((x - x0) / cell, (z - z0) / cell) for x, z in poly]
    im = Image.new("L", (nx, nz), 255)
    d = ImageDraw.Draw(im)
    for poly in room.walkable:
        d.polygon(to(poly), fill=0)
    for _i, poly, _s in room.blocked:
        d.polygon(to(poly), fill=255)
    blocked = np.asarray(im) > 127
    if erode_units > 0:
        r = int(math.ceil(erode_units / cell))
        out = blocked.copy()
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                if dx * dx + dy * dy <= r * r:
                    out |= np.roll(np.roll(blocked, dy, 0), dx, 1)
        blocked = out
    return blocked, (x0, z0, cell)


def scale_camera(room, out_name):
    c = room.c
    cam = room.cam
    cap_r = gd_number(GAME / "characters/player/player_controller.gd", r"capsule\.radius\s*=\s*([\d.]+)")
    reach = gd_number(GAME / "characters/player/player_controller.gd", r"const INTERACT_RANGE\s*:=\s*([\d.]+)")
    h_m = gd_number(GAME / "characters/party/party_sprite_3d.gd", r"var height_m := ([\d.]+)")
    blocked, (gx0, gz0, cell) = floor_grid(room, erode_units=cap_r / room.scale)
    plate = Image.open(room.plate).convert("RGBA")
    plate = Image.blend(plate, Image.new("RGBA", plate.size, (0, 0, 0, 255)), 0.35)
    # walkable lanes: pixels whose floor point is reachable by a bro's centre
    tint = np.zeros((H, W, 4), np.uint8)
    for y0 in range(0, H, 256):
        vv, uu = np.mgrid[y0:min(y0 + 256, H), 0:W]
        fx, fz = cam.px_to_floor(uu, vv)
        ix, iz = ((fx - gx0) / cell).astype(int), ((fz - gz0) / cell).astype(int)
        ok = (ix >= 0) & (ix < blocked.shape[1]) & (iz >= 0) & (iz < blocked.shape[0])
        free = np.zeros(ok.shape, bool)
        free[ok] = ~blocked[iz[ok], ix[ok]]
        sl = tint[y0:y0 + ok.shape[0]]
        sl[free] = (60, 220, 90, 95)
    layer = Image.alpha_composite(plate, Image.fromarray(tint, "RGBA"))
    d = ImageDraw.Draw(layer)
    f, fb = font(38), font(40, True)
    fl = font(48, True)
    legend = {}

    # camera crops (KEEP_HEIGHT: a narrower window crops the sides)
    crops = {"16:9 (project window 1920x1080): the whole plate": 16 / 9, "16:10": 16 / 10, "4:3": 4 / 3}
    for (name, ar), col in zip(crops.items(), [(255, 255, 255, 255), (255, 200, 60, 255), (255, 110, 60, 255)]):
        w = min(W, H * ar)
        x0 = (W - w) / 2
        inset = 4 if ar > 1.7 else 0
        d.rectangle((x0 + inset, inset, x0 + w - inset - 1, H - inset - 1), outline=col, width=6)
        legend[name] = {"crop_px": [round(x0), 0, round(x0 + w), H]}
    # Header legend panel (drawn first so labels avoid it).
    fh = font(56, True)
    head = ["WHITE/AMBER/ORANGE frames: camera crop 16:9 (whole plate), 16:10, 4:3",
            "PINK: 1.8 m bro, shrinks to x0.68 at the back wall (full size at z 2.0)",
            "GREEN: where a bro's centre can walk (0.25 m capsule)  BLUE: sightlines",
            f"Interact reach {reach:g} m. Camera foot is off plate at z {cam.cz:g}"]
    hy, hw = 16, 0
    for t in head:
        hw = max(hw, d.textlength(t, font=fh))
    panel = (14, 8, 14 + hw + 40, 8 + len(head) * 72 + 16)
    d.rectangle(panel, fill=(0, 0, 0, 215))
    for i, t in enumerate(head):
        d.text((34, 16 + i * 72), t, font=fh, fill=(255, 255, 255, 255), anchor="la")
    obstacles = [panel]
    labels = []  # (text, target (x, y), colour)

    # sightlines from the camera's foot on the floor to the key landmarks
    foot = cam.floor_px(0.0, cam.cz)
    for k, (x, z) in room.landmarks.items():
        u, v = cam.floor_px(x, z)
        d.line((foot[0], foot[1], u, v), fill=(120, 200, 255, 215), width=4)
        d.ellipse((u - 14, v - 14, u + 14, v + 14), fill=(120, 200, 255, 255), outline=(0, 0, 0, 255), width=4)
        obstacles.append((u - 16, v - 16, u + 16, v + 16))
        labels.append((k, (u, v), (190, 230, 255)))
        legend[f"sightline_{k}"] = {"landmark_xz": [x, z], "landmark_px": [round(u, 1), round(v, 1)]}

    # bro silhouettes at a few depths, centred on the widest walkable run at that depth
    depth = lambda z: lerp(1.0, c["DEPTH_BACK_SCALE"], clamp((c["DEPTH_FULL_Z"] - z) / (c["DEPTH_FULL_Z"] - c["BACK_WALL_Z"]), 0, 1))
    for z in (4.6, 2.0, -0.6, -2.8):
        iz = int((z - gz0) / cell)
        row = ~blocked[iz]
        if z < 1.0:  # west lane: the open aisle between the DDR/foosball side and the bar
            row = row.copy()
            row[int((-0.4 - gx0) / cell):] = False
        best, run0, run = (0, 0), None, 0
        for i, ok in enumerate(list(row) + [False]):
            if ok and run0 is None:
                run0 = i
            if not ok and run0 is not None:
                if i - run0 > best[1] - best[0]:
                    best = (run0, i)
                run0 = None
        xc = gx0 + (best[0] + best[1]) / 2 * cell
        sc = depth(z)
        hu = h_m / room.scale * sc
        fu, fv = cam.floor_px(xc, z)
        _hu, hv = cam.project(xc, hu, z)
        u2, _v2 = cam.floor_px(xc + 1.0, z)
        ppu = u2 - fu  # horizontal pixels per painting unit here
        sh = 0.55 / room.scale * sc * ppu / 2  # shoulder half width: 0.55 m
        hr = (fv - hv) * 0.11
        col = (255, 90, 190, 150)
        d.polygon([(fu - sh * 0.8, fv), (fu + sh * 0.8, fv), (fu + sh, hv + (fv - hv) * 0.22),
                   (fu - sh, hv + (fv - hv) * 0.22)], fill=col, outline=(255, 255, 255, 255))
        d.ellipse((fu - hr, hv, fu + hr, hv + 2 * hr), fill=col, outline=(255, 255, 255, 255), width=3)
        d.ellipse((fu - 10, fv - 10, fu + 10, fv + 10), fill=(255, 255, 255, 255))
        obstacles.append((fu - sh - 4, hv - 4, fu + sh + 4, fv + 12))
        labels.append((f"{h_m:g} m  z {z:g}  x{sc:.2f}", (fu + sh * 0.6, (fv + hv) / 2), (255, 255, 255)))
        legend[f"bro_z{z:g}"] = {"feet_px": [round(fu, 1), round(fv, 1)], "head_px": [round(fu, 1), round(hv, 1)],
                                 "height_px": round(fv - hv, 1), "depth_scale": round(sc, 3), "x_units": round(xc, 2)}

    # Labels last, each on the first free spot, with a leader line back to its target. A label keeps
    # at least `gap` px clear of every other label, marker and silhouette (author, Desk zx7u-q3:
    # "space out the crowded labels").
    pad, gap = 8, 34
    for text, (tx, ty), colr in labels:
        w = d.textlength(text, font=fl)
        hgt = 52
        spot = None
        for r in (30, 60, 100, 150, 210, 280, 360, 450, 550):
            for ang in (0, 180, 90, 270, 45, 315, 135, 225, 20, 160, 200, 340):
                cx, cy = tx + r * math.cos(math.radians(ang)), ty - r * math.sin(math.radians(ang))
                box = (cx - w / 2 - pad, cy - hgt / 2 - pad, cx + w / 2 + pad, cy + hgt / 2 + pad)
                if box[0] < 6 or box[2] > W - 6 or box[1] < 6 or box[3] > H - 6:
                    continue
                roomy = (box[0] - gap, box[1] - gap, box[2] + gap, box[3] + gap)
                if any(overlaps(roomy, o) for o in obstacles):
                    continue
                spot = (cx, cy, box)
                break
            if spot:
                break
        if spot is None:
            sys.exit(f"no free label spot for {text}")
        cx, cy, box = spot
        d.line((tx, ty, cx, cy), fill=(255, 255, 255, 230), width=3)
        d.rectangle(box, fill=(0, 0, 0, 225), outline=colr + (255,), width=2)
        d.text((cx, cy), text, font=fl, fill=colr + (255,), anchor="mm")
        obstacles.append(box)
    im = layer.convert("RGB")
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    im.quantize(256, Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(GUIDE_DIR / f"{out_name}.png", optimize=True)
    doc = {"file": f"{out_name}.png", "plate": room.plate.relative_to(ROOT).as_posix(),
           "character_height_m": h_m, "capsule_radius_m": cap_r, "interact_range_m": reach,
           "depth_curve": {"full_z": c["DEPTH_FULL_Z"], "back_scale": c["DEPTH_BACK_SCALE"], "back_wall_z": c["BACK_WALL_Z"],
                           "source": f"{room.gd} depth_scale_at"},
           "camera": common_notes(room)["camera"],
           "crop_note": "Camera is KEEP_HEIGHT; project viewport is 1920x1080 stretch aspect expand, so 16:9 shows the whole plate and narrower windows crop the sides.",
           "items": legend, "generator": "Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py"}
    (GUIDE_DIR / f"{out_name}.json").write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")


def lerp(a, b, t):
    return a + (b - a) * t


def clamp(x, a, b):
    return max(a, min(b, x))


# ---------------------------------------------------------------- main
def main():
    spec = importlib.util.spec_from_file_location("paint_px_to_floor", HD2D / "paint_px_to_floor.py")
    ppf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ppf)
    hall, nw, mc = build_hall(), build_north_wing(), build_mirror_corridor()
    for room in (hall, nw, mc):
        ref = ppf.px_to_floor if room is hall else None
        err, gap = round_trip(room.cam, ref)
        print(f"{room.key}: round-trip max {err:.6f} px" + (f", vs paint_px_to_floor max {gap:.2e} units" if gap is not None else ""))
        if err >= 1.0:
            sys.exit("projection round trip over 1 px")

    for room in (hall, nw):
        k = room.key
        notes = common_notes(room)
        # collision
        col = collision_image(room)
        legend = {"classes": {"255": "blocked", "0": "walkable"},
                  "meaning": "floor-plane footprint of the code's colliders: room walls (0.3 thick strips), FLOOR_BLOCKERS and the occluder-prism colliders; everything outside the room outline is blocked. Raw geometry: the 0.25 m player capsule is not added.",
                  "elements": [{"id": i, "source": s, "polygon_xz": [list(p) for p in poly]} for i, poly, s in room.blocked],
                  "not_included": "arch_unbuilt_stop (only exists while the mirror-corridor scene is missing; it exists now)" if k == "hall" else ""}
        save_mask(col, f"aa_mask_interior_collision_{k}", legend, notes)
        review(col, room.plate, f"aa_mask_interior_collision_{k}", (255, 40, 40))
        # interaction
        im, leg = interaction_image(room)
        save_mask(im, f"aa_mask_interior_interaction_{k}",
                  {"classes": "black = no interaction; every other colour is one id below",
                   "meaning": "the disc (1.0 m INTERACT_RANGE = radius_units on the floor) around each INTERACT_POINTS anchor, nearest anchor wins on overlaps, plus the scene-exit trigger boxes. The 60 degree facing cone is not drawn. Anchors can be reached only where collision allows.",
                   "ids": leg}, notes)
        review(im, room.plate, f"aa_mask_interior_interaction_{k}", None)
        # occlusion
        if k == "hall":
            white, ids_im, oleg = occlusion_images(room)
            save_mask(white, "aa_mask_interior_occlusion_hall",
                      {"classes": {"255": "an occluder draws in front of bros behind its sort depth", "0": "nothing"},
                       "companion": "aa_mask_interior_occlusion_hall_ids.png (one flat colour per occluder; nearest on top)",
                       "occluders": oleg}, notes)
            ids_im.save(MASK_DIR / "aa_mask_interior_occlusion_hall_ids.png", optimize=True)
            review(white, room.plate, "aa_mask_interior_occlusion_hall", (255, 200, 0))
        else:
            white = Image.new("L", (W, H), 0)
            save_mask(white, "aa_mask_interior_occlusion_north_wing",
                      {"classes": {"255": "occluder", "0": "nothing"}, "occluders": {},
                       "meaning": "EMPTY: the north wing has no occluder prisms, depth layers or cut-out props in code (the bros are never drawn behind anything). Re-run after the north wing rework (59b9) if occluders are added."},
                      notes)
            review(white, room.plate, "aa_mask_interior_occlusion_north_wing", (255, 200, 0))
        # node overlay
        node_overlay(room, f"aa_guide_node_overlay_{k}")
    scale_camera(hall, "aa_guide_scale_camera")
    # mirror corridor: interaction only (Desk zx7u-q2)
    im, leg = interaction_image(mc)
    dirs = ["south", "south_east", "east", "north_east", "north", "north_west", "west", "south_west"]  # PartySprite3D.DIRECTIONS
    for k, (at, stand) in enumerate(mc.c["SWITCHES"]):
        tx, tz = at[0] - stand[0], at[1] - stand[1]   # code: _add_switches, toward = (at - stand), then _facing
        best = max(range(8), key=lambda i: (math.sin(i * math.pi / 4) * tx + math.cos(i * math.pi / 4) * tz) / math.hypot(tx, tz))
        leg[f"shadow_switch_{k + 1}"]["stand_facing"] = dirs[best]
        leg[f"shadow_switch_{k + 1}"]["stand_facing_source"] = f"{mc.gd} _add_switches spawn at_shadow_switch_{k + 1} (_facing of anchor - stand)"
    save_mask(im, "aa_mask_interior_interaction_mirror_corridor",
              {"classes": "black = no interaction; every other colour is one id below",
               "meaning": "the disc (1.0 m INTERACT_RANGE = radius_units on the floor) around each SWITCHES anchor (interact id shadow_switch_N, N = switch index + 1 as in switch_id), nearest anchor wins on overlaps, plus the scene-exit trigger boxes. The 60 degree facing cone is not drawn. stand_xz is the code's stand point (spawn at_shadow_switch_N). Anchors can be reached only where collision allows.",
               "naming": "the mirror corridor is its own plate: *_mirror_corridor.png",
               "ids": leg}, dict(common_notes(mc), naming="mirror corridor plate"))
    review(im, mc.plate, "aa_mask_interior_interaction_mirror_corridor", None)
    # exterior: top-down plan (Desk zx7u-q1)
    exterior(build_exterior())
    print("wrote masks, legends, guides and review overlays")


if __name__ == "__main__":
    main()
