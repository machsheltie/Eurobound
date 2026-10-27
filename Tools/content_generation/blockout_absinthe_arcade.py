"""Absinthe Arcade exterior blockout generator (Step 1: architectural base).

Writes two self-contained glTF 2.0 files (no external deps):
  arcade_building_base.gltf  - building hull, facade openings, structural trim,
                               and empty anchor nodes where later art attaches
  street_ground_tile.gltf    - 2 m wide tileable sidewalk/curb/gutter/street strip

Conventions: meters, Y-up, facade front plane at z=0 facing +Z (street side),
building centered on x=0, sidewalk top at y=0. UVs are planar-projected in
meters (1 UV unit = 1 m) so tiling textures line up across parts and tiles.

Dimensions are derived from the reference scale panel (human 180 cm, cabinet
165 cm, awning top ~210 cm) and the straight-on entrance reference. Every
number lives in the DIMENSIONS block below; edit and re-run to adjust.

Usage: python tools/content_generation/blockout_absinthe_arcade.py [--preview]
"""

import base64
import json
import math
import struct
import sys
from pathlib import Path

OUT_DIR = (
    Path(__file__).resolve().parents[2]
    / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blockout"
)

# --- DIMENSIONS (meters) -----------------------------------------------------
W = 14.0                 # facade width
D = 12.0                 # building depth
GROUND_FLOOR = 6.0       # ground floor height (holds arch + sign + gentleman)
FLOOR_H = 3.6            # upper floor height
UPPER_FLOORS = 3
EAVE_H = GROUND_FLOOR + FLOOR_H * UPPER_FLOORS   # 16.8
ROOF_RISE = 3.2
SIDE_BAY_X = 4.6         # window column centers at +/- this

# Entrance: rectangular jambs, then a semi-elliptical (basket) arch.
ARCH_HALF_SPAN = 2.2     # clear opening 4.4 m
ARCH_SPRING = 3.4        # jamb height where the curve begins
ARCH_RISE = 1.4          # apex at 4.8 m
ARCH_DEPTH = 1.6         # recess depth to the interior void plane
ARCHIVOLT_W = 0.35       # carved surround band width
ARCH_SEGMENTS = 24

# Ground-floor left window (round-headed, balcony below)
GF_WIN = dict(cx=-SIDE_BAY_X, half_w=0.8, sill=3.0, spring=4.4, rise=0.8)

# Upper-floor windows
UP_WIN_HALF_W = 0.7
UP_WIN_SILL = 0.9        # above floor line
UP_WIN_H = 2.2
WIN_DEPTH = 0.3

# --- MATERIALS ----------------------------------------------------------------
MATERIALS = {
    "wall_stone": (0.72, 0.67, 0.58),
    "trim_stone": (0.86, 0.82, 0.74),
    "recess": (0.30, 0.29, 0.28),
    "interior_void": (0.03, 0.03, 0.03),
    "roof": (0.36, 0.30, 0.29),
    "ironwork": (0.14, 0.14, 0.15),
    "sidewalk": (0.56, 0.55, 0.53),
    "curb": (0.76, 0.74, 0.70),
    "gutter": (0.30, 0.30, 0.30),
    "street_cobble": (0.42, 0.41, 0.40),
}


# --- geometry helpers ----------------------------------------------------------
def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def normalize(v):
    n = math.sqrt(dot(v, v)) or 1.0
    return (v[0] / n, v[1] / n, v[2] / n)


def planar_uv(p, n):
    ax = max(range(3), key=lambda i: abs(n[i]))
    if ax == 0:
        return (p[2] * (1 if n[0] < 0 else -1), -p[1])
    if ax == 1:
        return (p[0], p[2])
    return (p[0] * (1 if n[2] > 0 else -1), -p[1])


class Part:
    """One glTF node: a mesh with one primitive per material."""

    def __init__(self, name):
        self.name = name
        self.prims = {}

    def poly(self, pts, mat, facing=None):
        """Flat-shaded convex polygon. `facing` flips winding to match a hint."""
        n = normalize(cross(sub(pts[1], pts[0]), sub(pts[2], pts[0])))
        if facing is not None and dot(n, facing) < 0:
            pts = pts[::-1]
            n = (-n[0], -n[1], -n[2])
        prim = self.prims.setdefault(mat, {"pos": [], "nrm": [], "uv": [], "idx": []})
        base = len(prim["pos"])
        for p in pts:
            prim["pos"].append(p)
            prim["nrm"].append(n)
            prim["uv"].append(planar_uv(p, n))
        for i in range(1, len(pts) - 1):
            prim["idx"] += [base, base + i, base + i + 1]

    def box(self, x0, x1, y0, y1, z0, z1, mat, skip=()):
        c = ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)
        faces = {
            "+x": [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)],
            "-x": [(x0, y0, z0), (x0, y0, z1), (x0, y1, z1), (x0, y1, z0)],
            "+y": [(x0, y1, z0), (x0, y1, z1), (x1, y1, z1), (x1, y1, z0)],
            "-y": [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)],
            "+z": [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],
            "-z": [(x0, y0, z0), (x0, y1, z0), (x1, y1, z0), (x1, y0, z0)],
        }
        for key, pts in faces.items():
            if key in skip:
                continue
            fc = tuple(sum(p[i] for p in pts) / 4 for i in range(3))
            self.poly(pts, mat, facing=sub(fc, c))


def ellipse_pts(cx, spring, a, b, n):
    """Arch curve from left springing point to right, as (x, y)."""
    return [
        (cx + a * math.cos(math.pi - math.pi * i / n), spring + b * math.sin(math.pi - math.pi * i / n))
        for i in range(n + 1)
    ]


class Opening:
    """Facade opening: rectangle x0..x1, y0..y_top, optional arched cap."""

    def __init__(self, x0, x1, y0, y1, rise=0.0, depth=WIN_DEPTH, back_mat="recess", segs=12):
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1
        self.rise, self.depth, self.back_mat, self.segs = rise, depth, back_mat, segs

    @property
    def top(self):
        return self.y1 + self.rise

    def curve(self):
        cx, a = (self.x0 + self.x1) / 2, (self.x1 - self.x0) / 2
        return ellipse_pts(cx, self.y1, a, self.rise, self.segs)

    def outline(self):
        """Closed outline (x, y), counter-clockwise from bottom-left."""
        pts = [(self.x0, self.y0), (self.x1, self.y0)]
        if self.rise > 0:
            pts += list(reversed(self.curve()))
        else:
            pts += [(self.x1, self.y1), (self.x0, self.y1)]
        return pts


def build_facade_face(part, openings, x_min, x_max, y_min, y_max, mat):
    """Front face at z=0 with openings cut out (grid cut + arch-cap strips)."""
    xs = sorted({x_min, x_max} | {v for o in openings for v in (o.x0, o.x1)})
    ys = sorted({y_min, y_max} | {v for o in openings for v in (o.y0, o.y1, o.top)})
    fwd = (0, 0, 1)
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            cx, cy = (xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2
            if any(o.x0 < cx < o.x1 and o.y0 < cy < o.top for o in openings):
                continue
            x0, x1, y0, y1 = xs[i], xs[i + 1], ys[j], ys[j + 1]
            part.poly([(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)], mat, fwd)
    # Fill between each arch curve and its bounding-box top.
    for o in openings:
        if o.rise <= 0:
            continue
        c = o.curve()
        for (xa, ya), (xb, yb) in zip(c, c[1:]):
            part.poly([(xa, ya, 0), (xb, yb, 0), (xb, o.top, 0), (xa, o.top, 0)], mat, fwd)


def build_recess(part, o, wall_mat):
    """Reveals (jambs, sill, head or arch soffit) and the back plane."""
    d = -o.depth
    outline = o.outline()
    cx, cy = (o.x0 + o.x1) / 2, (o.y0 + o.y1) / 2
    for (xa, ya), (xb, yb) in zip(outline, outline[1:] + outline[:1]):
        mid = ((xa + xb) / 2, (ya + yb) / 2)
        inward = (cx - mid[0], cy - mid[1], 0)
        part.poly([(xa, ya, 0), (xb, yb, 0), (xb, yb, d), (xa, ya, d)], wall_mat, inward)
    part.poly([(x, y, d) for x, y in outline], o.back_mat, (0, 0, 1))


def build_arch_ring(part, cx, spring, a, b, width, proud, segs, mat, jamb_bottom):
    """Protruding archivolt band following the arch curve, down both jambs."""
    inner = ellipse_pts(cx, spring, a, b, segs)
    outer = ellipse_pts(cx, spring, a + width, b + width, segs)
    z = proud
    for (ia, oa), (ib, ob) in zip(zip(inner, outer), zip(inner[1:], outer[1:])):
        part.poly([(ia[0], ia[1], z), (ib[0], ib[1], z), (ob[0], ob[1], z), (oa[0], oa[1], z)], mat, (0, 0, 1))
        part.poly([(oa[0], oa[1], 0), (oa[0], oa[1], z), (ob[0], ob[1], z), (ob[0], ob[1], 0)], mat,
                  (oa[0] - cx, oa[1] - spring, 0))
        part.poly([(ia[0], ia[1], 0), (ib[0], ib[1], 0), (ib[0], ib[1], z), (ia[0], ia[1], z)], mat,
                  (cx - ia[0], spring - ia[1], 0))
    for side in (-1, 1):
        xi = cx + side * a
        xo = cx + side * (a + width)
        part.box(min(xi, xo), max(xi, xo), jamb_bottom, spring, 0, proud, mat, skip=("-z",))


# --- building ----------------------------------------------------------------
def build_building():
    parts = []
    hx = W / 2

    # Openings
    arch = Opening(-ARCH_HALF_SPAN, ARCH_HALF_SPAN, 0.0, ARCH_SPRING, ARCH_RISE,
                   depth=ARCH_DEPTH, back_mat="interior_void", segs=ARCH_SEGMENTS)
    gf = GF_WIN
    gf_win = Opening(gf["cx"] - gf["half_w"], gf["cx"] + gf["half_w"], gf["sill"], gf["spring"], gf["rise"])
    upper = []
    for f in range(UPPER_FLOORS):
        floor_y = GROUND_FLOOR + f * FLOOR_H
        for cx in (-SIDE_BAY_X, SIDE_BAY_X):
            upper.append(Opening(cx - UP_WIN_HALF_W, cx + UP_WIN_HALF_W,
                                 floor_y + UP_WIN_SILL, floor_y + UP_WIN_SILL + UP_WIN_H))
    windows = [gf_win] + upper

    # Hull: facade face with holes + the other five box faces.
    facade = Part("facade_front")
    build_facade_face(facade, [arch] + windows, -hx, hx, 0.0, EAVE_H, "wall_stone")
    parts.append(facade)

    hull = Part("hull_walls")
    hull.box(-hx, hx, 0.0, EAVE_H, -D, 0.0, "wall_stone", skip=("+z", "-y"))
    parts.append(hull)

    entrance = Part("entrance_recess")
    build_recess(entrance, arch, "wall_stone")
    entrance.box(-ARCH_HALF_SPAN, ARCH_HALF_SPAN, 0.0, 0.12, -ARCH_DEPTH, 0.35, "trim_stone", skip=("-y",))
    parts.append(entrance)

    win_part = Part("window_recesses")
    for o in windows:
        build_recess(win_part, o, "wall_stone")
    parts.append(win_part)

    # Roof: pitched, ridge along X, small overhang front/back and gable ends.
    roof = Part("roof")
    ov = 0.5
    ridge_y, ridge_z = EAVE_H + ROOF_RISE, -D / 2
    fz, bz = ov, -D - ov
    drop = ROOF_RISE * ov / (D / 2)
    ey = EAVE_H - drop
    roof.poly([(-hx, ey, fz), (hx, ey, fz), (hx, ridge_y, ridge_z), (-hx, ridge_y, ridge_z)], "roof", (0, 1, 1))
    roof.poly([(-hx, ey, bz), (-hx, ridge_y, ridge_z), (hx, ridge_y, ridge_z), (hx, ey, bz)], "roof", (0, 1, -1))
    for sx in (-hx, hx):
        roof.poly([(sx, EAVE_H, 0.0), (sx, EAVE_H, -D), (sx, ridge_y, ridge_z)], "wall_stone", (sx, 0, 0))
    parts.append(roof)

    # Structural trim
    trim = Part("trim_bands")
    trim.box(-hx - 0.1, -ARCH_HALF_SPAN - ARCHIVOLT_W, 0.0, 0.7, 0.0, 0.1, "trim_stone", skip=("-z", "-y"))
    trim.box(ARCH_HALF_SPAN + ARCHIVOLT_W, hx + 0.1, 0.0, 0.7, 0.0, 0.1, "trim_stone", skip=("-z", "-y"))
    trim.box(-hx - 0.18, hx + 0.18, GROUND_FLOOR - 0.35, GROUND_FLOOR, 0.0, 0.18, "trim_stone", skip=("-z",))
    for f in range(1, UPPER_FLOORS):
        y = GROUND_FLOOR + f * FLOOR_H
        trim.box(-hx - 0.1, hx + 0.1, y - 0.2, y, 0.0, 0.1, "trim_stone", skip=("-z",))
    trim.box(-hx - 0.3, hx + 0.3, EAVE_H - 0.6, EAVE_H - 0.25, 0.0, 0.25, "trim_stone", skip=("-z",))
    trim.box(-hx - 0.5, hx + 0.5, EAVE_H - 0.25, EAVE_H, 0.0, 0.45, "trim_stone", skip=("-z",))
    parts.append(trim)

    quoins = Part("corner_pilasters")
    for sx in (-1, 1):
        x_in, x_out = sx * (hx - 0.7), sx * (hx + 0.12)
        quoins.box(min(x_in, x_out), max(x_in, x_out), 0.7, GROUND_FLOOR - 0.35, 0.0, 0.12, "trim_stone", skip=("-z",))
        for f in range(UPPER_FLOORS):
            y0 = GROUND_FLOOR + f * FLOOR_H
            y1 = y0 + FLOOR_H - 0.2 if f < UPPER_FLOORS - 1 else EAVE_H - 0.6
            quoins.box(min(x_in, x_out), max(x_in, x_out), y0, y1, 0.0, 0.12, "trim_stone", skip=("-z",))
    parts.append(quoins)

    archivolt = Part("entrance_archivolt")
    build_arch_ring(archivolt, 0.0, ARCH_SPRING, ARCH_HALF_SPAN, ARCH_RISE, ARCHIVOLT_W, 0.15,
                    ARCH_SEGMENTS, "trim_stone", jamb_bottom=0.0)
    # Keystone corbel: the mass the Headphone Gentleman carving is cut from.
    apex = ARCH_SPRING + ARCH_RISE
    archivolt.box(-0.6, 0.6, apex - 0.1, GROUND_FLOOR + 0.6, 0.0, 0.55, "trim_stone", skip=("-z",))
    parts.append(archivolt)

    surrounds = Part("window_surrounds")
    for o in upper:
        fw = 0.16
        surrounds.box(o.x0 - fw, o.x0, o.y0, o.y1, 0.0, 0.08, "trim_stone", skip=("-z",))
        surrounds.box(o.x1, o.x1 + fw, o.y0, o.y1, 0.0, 0.08, "trim_stone", skip=("-z",))
        surrounds.box(o.x0 - 0.25, o.x1 + 0.25, o.y0 - 0.14, o.y0, 0.0, 0.2, "trim_stone", skip=("-z",))
        surrounds.box(o.x0 - 0.3, o.x1 + 0.3, o.y1, o.y1 + 0.22, 0.0, 0.22, "trim_stone", skip=("-z",))
    build_arch_ring(surrounds, gf["cx"], gf["spring"], gf["half_w"], gf["rise"], 0.16, 0.08, 12,
                    "trim_stone", jamb_bottom=gf["sill"])
    parts.append(surrounds)

    balcony = Part("balcony_gf_left")
    bx0, bx1 = gf_win.x0 - 0.35, gf_win.x1 + 0.35
    balcony.box(bx0, bx1, gf["sill"] - 0.15, gf["sill"], 0.0, 0.7, "trim_stone", skip=("-z",))
    rail_h = gf["sill"] + 0.95
    balcony.box(bx0, bx1, rail_h - 0.05, rail_h, 0.62, 0.7, "ironwork", skip=("-z",))
    for x in (bx0, bx1 - 0.05):
        balcony.box(x, x + 0.05, gf["sill"], rail_h, 0.0, 0.7, "ironwork")
    balcony.box(bx0, bx1, gf["sill"], rail_h, 0.66, 0.67, "ironwork")
    parts.append(balcony)

    # Anchors: empty nodes marking where later-step art attaches.
    # Positions follow the straight-on entrance reference.
    anchors = {
        "anchor_arch_sign": (0.0, ARCH_SPRING + ARCH_RISE * 0.5, 0.2),
        "anchor_headphone_gentleman": (0.0, GROUND_FLOOR - 0.1, 0.55),
        "anchor_green_fairy_mural": (0.0, GROUND_FLOOR + 1.5 * FLOOR_H, 0.01),
        "anchor_awning_left": (gf["cx"], 2.2, 0.0),
        "anchor_street_cabinet": (gf["cx"] + 0.4, 0.0, 0.45),
        "anchor_chalkboard": (-ARCH_HALF_SPAN - 0.8, 0.0, 0.6),
        "anchor_doorframe_sign_right": (ARCH_HALF_SPAN + 0.75, 1.9, 0.05),
        "anchor_house_number": (ARCH_HALF_SPAN + 1.3, 3.4, 0.02),
        "anchor_hanging_sign_left": (-hx + 0.4, 3.6, 0.3),
        "anchor_bollard_left": (-hx + 0.7, 0.0, 2.4),
        "anchor_bollard_right": (ARCH_HALF_SPAN + 1.6, 0.0, 2.4),
        "anchor_drainpipe_left": (-hx + 0.35, 0.0, 0.15),
        "anchor_drainpipe_right": (hx - 0.35, 0.0, 0.15),
    }
    return parts, anchors


# --- ground tile -------------------------------------------------------------
SIDEWALK_DEPTH = 3.0
CURB_W = 0.25
CURB_DROP = 0.15
GUTTER_W = 0.4
STREET_DEPTH = 6.0
TILE_W = 2.0  # W / TILE_W = 7 tiles across the building


def build_ground():
    hx = TILE_W / 2
    up = (0, 1, 0)
    z_curb = SIDEWALK_DEPTH
    z_gutter = z_curb + CURB_W
    z_street = z_gutter + GUTTER_W
    z_end = z_street + STREET_DEPTH
    sy = -CURB_DROP

    sidewalk = Part("sidewalk")
    sidewalk.poly([(-hx, 0, 0), (-hx, 0, z_curb), (hx, 0, z_curb), (hx, 0, 0)], "sidewalk", up)
    curb = Part("curb")
    curb.poly([(-hx, 0, z_curb), (-hx, 0, z_gutter), (hx, 0, z_gutter), (hx, 0, z_curb)], "curb", up)
    curb.poly([(-hx, 0, z_gutter), (-hx, sy, z_gutter), (hx, sy, z_gutter), (hx, 0, z_gutter)], "curb", (0, 0, 1))
    gutter = Part("gutter")
    gutter.poly([(-hx, sy, z_gutter), (-hx, sy - 0.03, z_street - GUTTER_W / 2), (hx, sy - 0.03, z_street - GUTTER_W / 2),
                 (hx, sy, z_gutter)], "gutter", up)
    gutter.poly([(-hx, sy - 0.03, z_street - GUTTER_W / 2), (-hx, sy, z_street), (hx, sy, z_street),
                 (hx, sy - 0.03, z_street - GUTTER_W / 2)], "gutter", up)
    street = Part("street")
    street.poly([(-hx, sy, z_street), (-hx, sy, z_end), (hx, sy, z_end), (hx, sy, z_street)], "street_cobble", up)
    return [sidewalk, curb, gutter, street], {}


# --- glTF writer -------------------------------------------------------------
def write_gltf(path, root_name, parts, anchors):
    mat_names = sorted({m for p in parts for m in p.prims})
    blob = bytearray()
    views, accessors, meshes, nodes = [], [], [], []

    def add_view(data, target):
        while len(blob) % 4:
            blob.append(0)
        views.append({"buffer": 0, "byteOffset": len(blob), "byteLength": len(data), "target": target})
        blob.extend(data)
        return len(views) - 1

    def add_accessor(values, comps, ctype, target, minmax=False):
        flat = [c for v in values for c in (v if comps > 1 else (v,))]
        fmt = "<%d%s" % (len(flat), "f" if ctype == 5126 else "I")
        acc = {"bufferView": add_view(struct.pack(fmt, *flat), target), "componentType": ctype,
               "count": len(values), "type": {1: "SCALAR", 2: "VEC2", 3: "VEC3"}[comps]}
        if minmax:
            acc["min"] = [min(v[i] for v in values) for i in range(comps)]
            acc["max"] = [max(v[i] for v in values) for i in range(comps)]
        accessors.append(acc)
        return len(accessors) - 1

    child_ids = []
    for part in parts:
        prims = []
        for mat, d in part.prims.items():
            prims.append({
                "attributes": {
                    "POSITION": add_accessor(d["pos"], 3, 5126, 34962, minmax=True),
                    "NORMAL": add_accessor(d["nrm"], 3, 5126, 34962),
                    "TEXCOORD_0": add_accessor(d["uv"], 2, 5126, 34962),
                },
                "indices": add_accessor(d["idx"], 1, 5125, 34963),
                "material": mat_names.index(mat),
            })
        meshes.append({"name": part.name, "primitives": prims})
        nodes.append({"name": part.name, "mesh": len(meshes) - 1})
        child_ids.append(len(nodes) - 1)

    if anchors:
        anchor_ids = []
        for name, pos in anchors.items():
            nodes.append({"name": name, "translation": list(pos)})
            anchor_ids.append(len(nodes) - 1)
        nodes.append({"name": "anchors", "children": anchor_ids})
        child_ids.append(len(nodes) - 1)

    nodes.append({"name": root_name, "children": child_ids})
    gltf = {
        "asset": {"version": "2.0", "generator": "Eurobound blockout_absinthe_arcade.py"},
        "scene": 0,
        "scenes": [{"name": root_name, "nodes": [len(nodes) - 1]}],
        "nodes": nodes,
        "meshes": meshes,
        "materials": [{"name": m, "pbrMetallicRoughness": {
            "baseColorFactor": list(MATERIALS[m]) + [1.0], "metallicFactor": 0.0, "roughnessFactor": 0.9}}
            for m in mat_names],
        "accessors": accessors,
        "bufferViews": views,
        "buffers": [{"byteLength": len(blob),
                     "uri": "data:application/octet-stream;base64," + base64.b64encode(bytes(blob)).decode()}],
    }
    path.write_text(json.dumps(gltf, separators=(",", ":")))
    tris = sum(len(d["idx"]) // 3 for p in parts for d in p.prims.values())
    print(f"wrote {path.name}: {len(parts)} meshes, {len(anchors)} anchors, {tris} tris")


# --- preview renderer (Pillow, flat shading, painter's sort) ------------------
def subdivide(tri, max_edge):
    """Split a triangle until every edge is short, so painter's sort holds up."""
    a, b, c = tri
    edges = [(math.dist(a, b), 0), (math.dist(b, c), 1), (math.dist(c, a), 2)]
    length, i = max(edges)
    if length <= max_edge:
        return [tri]
    p, q, r = [(a, b, c), (b, c, a), (c, a, b)][i]
    m = tuple((p[k] + q[k]) / 2 for k in range(3))
    return subdivide((p, m, r), max_edge) + subdivide((m, q, r), max_edge)


def render_preview(path, scenes, cam_yaw_deg, cam_pitch_deg, size=(1200, 1400), extra=()):
    from PIL import Image, ImageDraw

    ss = 2
    w, h = size[0] * ss, size[1] * ss
    yaw, pitch = math.radians(cam_yaw_deg), math.radians(cam_pitch_deg)
    light = normalize((-0.4, 0.7, 0.6))

    def view(p):
        x = p[0] * math.cos(yaw) - p[2] * math.sin(yaw)
        z = p[0] * math.sin(yaw) + p[2] * math.cos(yaw)
        y = p[1] * math.cos(pitch) - z * math.sin(pitch)
        z2 = p[1] * math.sin(pitch) + z * math.cos(pitch)
        return (x, y, z2)

    tris = []
    for parts, offset in scenes:
        for part in parts:
            for mat, d in part.prims.items():
                col = MATERIALS[mat]
                for i in range(0, len(d["idx"]), 3):
                    pts = [tuple(d["pos"][d["idx"][i + k]][c] + offset[c] for c in range(3)) for k in range(3)]
                    n = d["nrm"][d["idx"][i]]
                    shade = 0.45 + 0.55 * max(0.0, dot(n, light))
                    rgb = tuple(int(255 * min(1, c * shade)) for c in col)
                    tris += [([view(p) for p in t], rgb) for t in subdivide(pts, 0.6)]
    tris += [([view(p) for p in t], c) for t, c in extra]

    xs = [p[0] for t, _ in tris for p in t]
    ys = [p[1] for t, _ in tris for p in t]
    scale = min(w / (max(xs) - min(xs)), h / (max(ys) - min(ys))) * 0.92
    ox, oy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2

    img = Image.new("RGB", (w, h), (24, 26, 30))
    draw = ImageDraw.Draw(img)
    for t, col in sorted(tris, key=lambda tc: sum(p[2] for p in tc[0]) / 3):
        draw.polygon([(w / 2 + (p[0] - ox) * scale, h / 2 - (p[1] - oy) * scale) for p in t], fill=col)
    img.resize(size, Image.LANCZOS).save(path)
    print(f"wrote {path.name}")


def human_marker(x, z):
    """1.8 m tall magenta scale slab (preview only)."""
    c = (230, 40, 200)
    a, b, cc, d = (x - 0.25, 0, z), (x + 0.25, 0, z), (x + 0.25, 1.8, z), (x - 0.25, 1.8, z)
    return [((a, b, cc), c), ((a, cc, d), c)]


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    b_parts, b_anchors = build_building()
    g_parts, _ = build_ground()
    write_gltf(OUT_DIR / "arcade_building_base.gltf", "arcade_building_base", b_parts, b_anchors)
    write_gltf(OUT_DIR / "street_ground_tile.gltf", "street_ground_tile", g_parts, {})

    if "--preview" in sys.argv:
        n_tiles = int(round(W / TILE_W)) + 2
        start = -(n_tiles - 1) * TILE_W / 2
        ground = [(g_parts, (start + i * TILE_W, 0, 0)) for i in range(n_tiles)]
        scenes = ground + [(b_parts, (0, 0, 0))]
        marker = human_marker(-3.4, 1.2) + human_marker(0.0, 0.5)
        render_preview(OUT_DIR / "preview_front.png", scenes, 0, 0, extra=marker)
        render_preview(OUT_DIR / "preview_three_quarter.png", scenes, -35, 18, size=(1400, 1400), extra=marker)


if __name__ == "__main__":
    main()
