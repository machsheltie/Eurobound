"""E2 review renders: places the kits on a stand-in facade at mason's interface positions and renders

  * bible_<view>: through aa_bible_cam (dev/aa_team/interfaces.json), border-cropped to the exact
    pixel box of the reference crop, so the compare is pixel-registered with the bible;
  * front_<view>: a straight-on view of the same window (for R2 and the dormer, against the sheet).

  blender -b <wip>/E2_windows.blend --python review_e2.py -- [--views l2 l1 ...] [--clay] [--long 1800]

The script never saves: wall, layout empties, cat placement and cameras exist only for the render.
"""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Euler, Matrix, Vector

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from e2_lib import MB, get_coll, mat_basic, to_object  # noqa: E402

REPO = HERE.parents[4]
OUT = REPO / "dev/aa_team/renders/E2"
IFACE = json.loads((REPO / "dev/aa_team/interfaces.json").read_text(encoding="utf-8"))

K = 5248 / 1600  # 1600-px bible view -> full-res bible pixels


def box(b):
    return tuple(int(v * K) for v in b)


# reference crops: full-res bible pixel boxes (x0, y0, x1, y1) or sheet crops for front-only views
VIEWS = {
    "l2": dict(kit="aa_window_l2_cat", bible=box((540, 130, 720, 560)), ref="ref/bible_w2.png"),
    "l1": dict(kit="aa_window_l1_arched", bible=box((520, 590, 720, 900)), ref="ref/bible_w1.png"),
    "l3": dict(kit="aa_window_l3_balcony", bible=box((500, 0, 720, 240)), ref="ref/bible_w3.png"),
    "r1": dict(kit="aa_window_r1", bible=box((1180, 0, 1420, 430)), ref="ref/bible_r1.png"),
    "r2": dict(kit="aa_window_r2", bible=None, ref="ref/sheet_r2.png"),
    "dormer_l": dict(kit="aa_window_dormer_l", bible=None, ref="ref/sheet_dormer_l.png"),
    "dormer_r": dict(kit="aa_window_dormer_r", bible=None, ref="ref/sheet_dormer_r.png"),
    "side_w0": dict(kit="aa_window_side_w0", bible=None, ref="ref/sheet_side_w0.png"),
    "side_w1": dict(kit="aa_window_side_w1", bible=None, ref="ref/sheet_side_w1.png"),
    "side_w2": dict(kit="aa_window_side_w2", bible=None, ref="ref/sheet_side_w2.png"),
    "dormer_side": dict(kit="aa_window_dormer_side", bible=None, ref="ref/sheet_dormer_side.png"),
}
DORMER_POS = (8.0, 14.0)  # stand-in roof patch, away from the facade (dormer openings arrive in v2)


def args():
    a = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = {"views": list(VIEWS), "clay": False, "out": str(OUT), "long": 1800, "samples": 64, "modes": ["bible", "front"]}
    i = 0
    while i < len(a):
        if a[i] in ("--views", "--modes"):
            k = a[i][2:]
            out[k] = []
            i += 1
            while i < len(a) and not a[i].startswith("--"):
                out[k].append(a[i])
                i += 1
            continue
        if a[i] == "--clay":
            out["clay"] = True
        elif a[i] in ("--out", "--long", "--samples"):
            out[a[i][2:]] = a[i + 1] if a[i] == "--out" else int(a[i + 1])
            i += 1
        i += 1
    return out


SIDE_X0 = 7.0   # review only: the side kits are laid out unrotated on a stand-in wall to the right


def place(aid):
    c = bpy.data.collections[aid]
    if "e2_side_place" in c:
        sp = json.loads(c["e2_side_place"])
        return (SIDE_X0 + sp["u_center"] * (2.4 if "dormer" not in aid else 1.0) + (3.0 if "dormer" in aid else 0.0),
                sp["sill_z"])
    return tuple(c["e2_place"])


def instance(coll_name, loc, parent):
    e = bpy.data.objects.new(f"rv_{coll_name}", None)
    e.instance_type = "COLLECTION"
    e.instance_collection = bpy.data.collections[coll_name]
    e.location = loc
    parent.objects.link(e)
    return e


def wall_with_holes(rv):
    """Stand-in facade (mason's plane, extents and openings) - flat stone, no mural."""
    stone = bpy.data.materials["m_aa_trim_stone"]
    f = IFACE["facade"]
    mb = MB()
    mb.box((f["x_left_corner"], 0.0, 0.0), (f["x_right_seam"], 0.6, IFACE["storeys"]["eave_z_provisional"]), "stone")
    wall = to_object(mb, "rv_wall", rv, {"stone": stone}, bake_uv="norm")
    cut = get_coll("rv_cutters", rv)
    for key, e in IFACE["windows"].items():
        x, z, W, H = e["center_x"], e["sill_z"], e["width"], e["height"]
        c = MB()
        arched = e.get("head_shape") in ("semicircular", "elliptical")
        top = e.get("springing_z", z + H) if arched else z + H
        c.box((x - W / 2, -0.2, z - 0.002), (x + W / 2, 0.9, top), "stone")
        if arched:
            ez = (e.get("head_rise", W / 2)) / (W / 2)
            n0 = len(c.v)
            c.lathe([(0.0, -0.2), (W / 2, -0.2), (W / 2, 0.9), (0.0, 0.9)], 48, "stone")
            c.v[n0:] = [(x + vx, vz, top + vy * ez) for vx, vy, vz in c.v[n0:]]
        ob = to_object(c, f"rv_cut_{key}", cut, {"stone": stone}, bake_uv="norm")
        ob.hide_render = True
        ob.display_type = "WIRE"
    # stand-in side wall (review only: side kits laid out unrotated to the right of the facade)
    side = (IFACE.get("side_right") or {}).get("windows", {})
    if side:
        sb = MB()
        sb.box((SIDE_X0, 0.0, 0.0), (SIDE_X0 + 6.0, 0.6, IFACE["storeys"]["eave_z_provisional"]), "stone")
        to_object(sb, "rv_side_wall_src", rv, {"stone": stone}, bake_uv="norm")
        sw = bpy.data.objects["rv_side_wall_src"]
        for key, e in side.items():
            aid = {"side_w0_ground": "aa_window_side_w0", "side_w1": "aa_window_side_w1", "side_w2": "aa_window_side_w2"}[key]
            x, _ = place(aid)
            c = MB()
            c.box((x - e["width"] / 2, -0.2, e["sill_z"] - 0.002), (x + e["width"] / 2, 0.9, e["head_z"]), "stone")
            ob = to_object(c, f"rv_cut_{key}", cut, {"stone": stone}, bake_uv="norm")
            ob.hide_render = True
        m2 = sw.modifiers.new("holes", "BOOLEAN")
        m2.operation = "DIFFERENCE"
        m2.operand_type = "COLLECTION"
        m2.collection = cut
        m2.solver = "EXACT"
    m = wall.modifiers.new("holes", "BOOLEAN")
    m.operation = "DIFFERENCE"
    m.operand_type = "COLLECTION"
    m.collection = cut
    m.solver = "EXACT"
    return wall


def roof_patch(rv):
    """Stand-in mansard slope above the eave (mason's roof is the real one)."""
    slate = bpy.data.materials["m_aa_roof_slate"]
    f = IFACE["facade"]
    ze = IFACE["storeys"]["eave_z_provisional"]
    x0, x1 = f["x_left_corner"], f["x_right_seam"]
    mb = MB()
    x1 = max(x1, SIDE_X0 + 6.0)
    mb.add([(x0, 0.35, ze + 0.45), (x1, 0.35, ze + 0.45), (x1, 1.4, ze + 3.4), (x0, 1.4, ze + 3.4)], [(0, 1, 2, 3)], "slate")
    to_object(mb, "rv_roof", rv, {"slate": slate}, bake_uv="norm")
    mb = MB()
    mb.box((x0, -0.35, ze), (x1, 0.6, ze + 0.45), "stone")   # eave band (spans the side stand-in too)
    to_object(mb, "rv_eave", rv, {"stone": bpy.data.materials["m_aa_trim_stone"]}, bake_uv="norm")


def place_cat(rv):
    src = bpy.data.objects.get("aa_prop_window_cat")
    if src is None:
        return None
    c = bpy.data.collections["aa_window_l2_cat"]
    k = c.get("e2_scale_k", 1.0)
    x, z = place("aa_window_l2_cat")
    cat = src.copy()
    cat.name = "rv_window_cat"
    cat.hide_render = False
    cat.hide_set(False)
    rv.objects.link(cat)
    rot = src.matrix_basis.to_3x3().normalized().to_4x4()
    cat.matrix_world = Matrix.Translation((x + 0.13 * k, -0.075 * k, z)) @ rot
    bpy.context.view_layer.update()
    ws = [cat.matrix_world @ v.co for v in cat.data.vertices]
    cat.location.z += z - min(p.z for p in ws)
    cat.location.y += (-0.075 * k) - (max(p.y for p in ws) + min(p.y for p in ws)) / 2
    return cat


def lights(scene):
    """Soft warm overcast: Blender's bundled courtyard HDRI (diffuse sky + bounce) plus a soft warm sun."""
    w = bpy.data.worlds.new("rv_world")
    scene.world = w
    nt = w.node_tree
    bg = next(n for n in nt.nodes if n.type == "BACKGROUND")
    hdr = Path(bpy.utils.system_resource("DATAFILES")) / "studiolights/world/courtyard.exr"
    if hdr.exists():
        env = nt.nodes.new("ShaderNodeTexEnvironment")
        env.image = bpy.data.images.load(str(hdr), check_existing=True)
        mp = nt.nodes.new("ShaderNodeMapping")
        mp.inputs["Rotation"].default_value = (0, 0, math.radians(200))
        tc = nt.nodes.new("ShaderNodeTexCoord")
        nt.links.new(tc.outputs["Generated"], mp.inputs[0])
        nt.links.new(mp.outputs[0], env.inputs[0])
        hs = nt.nodes.new("ShaderNodeHueSaturation")
        hs.inputs["Saturation"].default_value = 0.55
        nt.links.new(env.outputs[0], hs.inputs["Color"])
        nt.links.new(hs.outputs[0], bg.inputs["Color"])
        bg.inputs["Strength"].default_value = 0.85
    else:
        bg.inputs["Color"].default_value = (0.58, 0.62, 0.68, 1)
        bg.inputs["Strength"].default_value = 1.35
    sun_d = bpy.data.lights.new("rv_sun", "SUN")
    sun_d.energy = 3.6
    sun_d.color = (1.0, 0.88, 0.72)
    sun_d.angle = math.radians(12)
    sun = bpy.data.objects.new("rv_sun", sun_d)
    sun.rotation_euler = Euler((math.radians(48), 0, math.radians(-32)))
    scene.collection.objects.link(sun)


# ---- per-view camera solve (PnP) against points measured on each crop ---------------------
# Image points are in crop pixels (full-res bible scale); see the report for how they were read.
IMG_PTS = {
    "l2": {"frame_tl": (154, 419), "frame_tr": (455, 390), "frame_br": (422, 1036), "cap_fr": (524, 1031)},
    "l1": {"arch_top": (300, 301), "spring_l": (129, 466), "spring_r": (491, 460), "cap_fr": (481, 932)},
    "r1": {"frame_tl": (161, 471), "frame_tr": (510, 405), "cap_fr": (688, 1146)},
    "l3": {"finial_l": (263, 230), "finial_r": (620, 147), "cap_fl": (243, 427), "cap_fr": (677, 363)},
}


def world_pts(v):
    aid = VIEWS[v]["kit"]
    c = bpy.data.collections[aid]
    P = json.loads(c["e2_params"])
    k = c.get("e2_scale_k", 1.0)
    cx0, sz = place(aid)
    W, H, R = P["W"] * k, P["H"] * k, P["sash"]["reveal"] * k
    cx = cx0 + P.get("frame_dx", 0.0)
    rise = P["sash"].get("rise_frac", 1.0) * W / 2
    out = {"frame_tl": (cx - W / 2, R, sz + H), "frame_tr": (cx + W / 2, R, sz + H),
           "frame_bl": (cx - W / 2, R, sz), "frame_br": (cx + W / 2, R, sz),
           "arch_top": (cx, R, sz + H), "spring_l": (cx - W / 2, R, sz + H - rise),
           "spring_r": (cx + W / 2, R, sz + H - rise)}
    sl = P.get("sill") or P.get("slab")
    if sl:
        out["cap_fr"] = (cx0 + (sl["w"] / 2 + 0.012) * k, -sl["proj"] * k, sz)
        out["cap_fl"] = (cx0 - (sl["w"] / 2 + 0.012) * k, -sl["proj"] * k, sz)
    rl = P.get("rail")
    if rl:
        out["finial_l"] = (cx0 - rl["half"] * k, rl["y"] * k, sz + (rl["h"] + 0.088) * k)
        out["finial_r"] = (cx0 + rl["half"] * k, rl["y"] * k, sz + (rl["h"] + 0.088) * k)
    return out


def _project(loc, rot, f, cxp, cyp, X):
    q = rot.to_matrix().transposed() @ (Vector(X) - loc)
    return (cxp + f * q.x / -q.z, cyp - f * q.y / -q.z)


def solve_view_cam(v):
    """Gauss-Newton PnP from aa_bible_cam: 6 pose params, intrinsics fixed, soft priors on the pose."""
    import numpy as np
    c = IFACE["camera"]
    Wr, Hr = c["resolution"]
    f = c["lens_mm"] / c["sensor_width_mm"] * Wr
    cxp, cyp = Wr / 2, Hr / 2
    x0, y0 = VIEWS[v]["bible"][:2]
    wp = world_pts(v)
    pairs = [(wp[n], (x0 + u, y0 + w)) for n, (u, w) in IMG_PTS[v].items() if n in wp]
    loc0 = Vector(c["location"])
    rot0 = Euler([math.radians(a) for a in c["rotation_euler_xyz_deg"]], "XYZ")
    p = np.zeros(6)
    base_err = []
    for X, (u, w) in pairs:
        pu, pw = _project(loc0, rot0, f, cxp, cyp, X)
        base_err.append(math.hypot(pu - u, pw - w))

    def pose(p):
        loc = loc0 + Vector(p[3:6])
        rot = (rot0.to_matrix() @ Euler(p[0:3], "XYZ").to_matrix()).to_euler("XYZ")
        return loc, rot

    def resid(p):
        loc, rot = pose(p)
        r = []
        for X, (u, w) in pairs:
            pu, pw = _project(loc, rot, f, cxp, cyp, X)
            r += [pu - u, pw - w]
        # priors: 4 deg on rotation, 2 m on position, expressed in pixels (~f*angle)
        r += list(p[0:3] / math.radians(4.0) * 4.0) + list(p[3:6] / 2.0 * 4.0)
        return np.array(r)
    for it in range(30):
        r = resid(p)
        J = np.zeros((len(r), 6))
        for j in range(6):
            d = np.zeros(6)
            d[j] = 1e-4 if j < 3 else 1e-3
            J[:, j] = (resid(p + d) - r) / d[j]
        step = np.linalg.lstsq(J.T @ J + 1e-3 * np.eye(6), -J.T @ r, rcond=None)[0]
        p = p + step
        if np.linalg.norm(step) < 1e-7:
            break
    loc, rot = pose(p)
    errs = []
    for X, (u, w) in pairs:
        pu, pw = _project(loc, rot, f, cxp, cyp, X)
        errs.append(math.hypot(pu - u, pw - w))
    return loc, rot, errs, base_err


def kit_bbox(aid, origin):
    lo = Vector((1e9, 1e9, 1e9))
    hi = -lo
    obs = list(bpy.data.collections[aid].objects)
    if bpy.data.collections.get(f"{aid}_body"):
        obs += list(bpy.data.collections[f"{aid}_body"].objects)
    for o in obs:
        if o.type != "MESH" or "interior" in o.name:
            continue
        for v in o.data.vertices:
            p = o.matrix_world @ v.co + Vector(origin)
            lo = Vector(map(min, lo, p))
            hi = Vector(map(max, hi, p))
    return lo, hi


def frame_front(cam, lo, hi, aspect=None, margin=0.06):
    x0, x1, z0, z1 = lo.x - margin, hi.x + margin, lo.z - margin, hi.z + margin
    cx, cz = (x0 + x1) / 2, (z0 + z1) / 2
    cam.location = Vector((cx, -14.0, cz))
    cam.rotation_euler = Euler((math.radians(90), 0, 0))
    cd = cam.data
    cd.sensor_fit = "HORIZONTAL"
    cd.sensor_width = 36.0
    a = aspect or (x1 - x0) / (z1 - z0)
    w = max(x1 - x0, (z1 - z0) * a)
    cd.lens = 36.0 * 14.0 / w
    cd.shift_x = cd.shift_y = 0.0
    return a


def bible_cam(cam):
    c = IFACE["camera"]
    cam.location = Vector(c["location"])
    cam.rotation_euler = Euler([math.radians(v) for v in c["rotation_euler_xyz_deg"]], "XYZ")
    cd = cam.data
    cd.lens = c["lens_mm"]
    cd.sensor_width = c["sensor_width_mm"]
    cd.sensor_fit = c["sensor_fit"]
    cd.shift_x, cd.shift_y = c["shift"]


def main():
    A = args()
    scene = bpy.context.scene
    rv = get_coll("rv_review")
    vl = bpy.context.view_layer
    for lc in vl.layer_collection.children:
        if lc.name in ("aa_kit", "e2_external"):
            lc.exclude = True
    for aid in ["aa_window_l1_arched", "aa_window_l2_cat", "aa_window_l3_balcony", "aa_window_r1", "aa_window_r2", "aa_window_dormer_l", "aa_window_dormer_r",
                "aa_window_side_w0", "aa_window_side_w1", "aa_window_side_w2", "aa_window_dormer_side"]:
        x, z = place(aid)
        fy = json.loads(bpy.data.collections[aid]["e2_params"]).get("face_y", 0.0)
        instance(aid, (x, fy, z), rv)
        if "dormer" in aid:
            instance(f"{aid}_body", (x, fy, z), rv)
    for lc in vl.layer_collection.children:
        if lc.name == "e2_dormer_body_standin":
            lc.exclude = True
    wall_with_holes(rv)
    # faint room backlight behind the sheer curtains (review only; the room isn't part of the kits)
    for aid in ("aa_window_l1_arched", "aa_window_l2_cat", "aa_window_r1", "aa_window_r2"):
        x, z = place(aid)
        k_ = bpy.data.collections[aid].get("e2_scale_k", 1.0)
        ld = bpy.data.lights.new(f"rv_room_{aid}", "AREA")
        ld.energy = 18.0
        ld.size = 0.7
        ld.color = (1.0, 0.9, 0.78)
        lo = bpy.data.objects.new(f"rv_room_{aid}", ld)
        lo.location = (x, 0.95 * k_, z + 0.9 * k_)
        lo.rotation_euler = Euler((math.radians(-90), 0, 0))   # facing -Y, toward the street
        rv.objects.link(lo)
    roof_patch(rv)
    place_cat(rv)
    lights(scene)
    scene.render.engine = "BLENDER_EEVEE"
    ee = scene.eevee
    ee.taa_render_samples = A["samples"]
    for attr, val in (("use_raytracing", True), ("use_shadows", True), ("use_fast_gi", True),
                      ("shadow_ray_count", 3), ("shadow_step_count", 12), ("use_shadow_jitter_viewport", True)):
        try:
            setattr(ee, attr, val)
        except Exception:
            pass
    scene.view_settings.view_transform = "AgX"
    try:
        scene.view_settings.look = "AgX - Base Contrast"
    except TypeError:
        pass
    scene.view_settings.exposure = 0.1
    try:
        ee.fast_gi_method = "GLOBAL_ILLUMINATION"
        ee.fast_gi_distance = 0.6
        ee.ray_tracing_options.use_denoise = True
    except Exception:
        pass
    if A["clay"]:
        vl.material_override = mat_basic("rv_clay", (170, 166, 160), rough=0.6)
    cam = bpy.data.objects.new("rv_cam", bpy.data.cameras.new("rv_cam"))
    rv.objects.link(cam)
    scene.camera = cam
    cam.data.clip_start = 0.05
    cam.data.clip_end = 300
    out = Path(A["out"])
    if not out.is_absolute():
        out = (REPO / out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    tag = "clay" if A["clay"] else "final"
    done = []
    global SOLVE
    SOLVE = {}
    r = scene.render
    for v in A["views"]:
        V = VIEWS[v]
        for mode in A["modes"]:
            if mode == "bible":
                if not V["bible"]:
                    continue
                bible_cam(cam)
                x0, y0, x1, y1 = V["bible"]
                W, H = IFACE["camera"]["resolution"]
                rg = None
                if v in IMG_PTS:
                    loc, rot, errs, berr = solve_view_cam(v)
                    cam.location, cam.rotation_euler = loc, rot
                    long_side = max(x1 - x0, y1 - y0)
                    SOLVE[v] = {"residual_px": [round(e, 1) for e in errs], "max_pct_of_crop": round(100 * max(errs) / long_side, 2),
                                "aa_bible_cam_residual_px": [round(e, 1) for e in berr],
                                "aa_bible_cam_max_pct": round(100 * max(berr) / long_side, 2)}
                if rg:  # framing fit to the crop (register_e2.py): zoom about the principal point + shift
                    sc, tx, ty = rg["s"], rg["tx"], rg["ty"]
                    cam.data.lens = IFACE["camera"]["lens_mm"] * sc
                    spx = (1 - sc) * (x0 - W / 2) + tx
                    spy = (1 - sc) * (y0 - H / 2) + ty
                    cam.data.shift_x = -spx / max(W, H) * rg.get("sign", 1)
                    cam.data.shift_y = spy / max(W, H) * rg.get("sign", 1)
                r.resolution_x, r.resolution_y = W, H
                r.resolution_percentage = max(1, int(round(A["long"] / max(x1 - x0, y1 - y0) * 100)))
                r.use_border = True
                r.use_crop_to_border = True
                r.border_min_x, r.border_max_x = x0 / W, x1 / W
                r.border_min_y, r.border_max_y = 1 - y1 / H, 1 - y0 / H
            else:
                r.use_border = False
                px, pz = place(V["kit"])
                lo, hi = kit_bbox(V["kit"], (px, 0.0, pz))
                a = frame_front(cam, lo, hi)
                if a >= 1:
                    r.resolution_x, r.resolution_y = A["long"], int(round(A["long"] / a))
                else:
                    r.resolution_x, r.resolution_y = int(round(A["long"] * a)), A["long"]
                r.resolution_percentage = 100
            fp = out / f"{tag}_{mode}_{v}.png"
            r.filepath = str(fp)
            bpy.ops.render.render(write_still=True)
            done.append(str(fp))
    print("@@JSON@@" + json.dumps({"rendered": done, "camera_solve": SOLVE}))


if __name__ == "__main__":
    main()
