"""Electrical retrofit hardware for the Absinthe Arcade, per the production reference.

Rebuilds aa_prop_conduit_set (purple and green conduit runs, mismatched clamps
drilled into the stone, sealed junction boxes with cable glands) and adds
aa_arch_hero_neon_extrados (green neon tube tracing the archivolt on LED/acrylic
brackets) to the arch hero. Reference: "5. Electrical / mounting detail" and
"11. Electrical / mounting details" on the daytime sheets.

Blender space: facade on y=0 facing -Y. Safe to re-run.
"""

import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

PURPLE_R = 0.034
GREEN_R = 0.03
CLAMP_STEP = 0.42
BOX = (0.30, 0.12, 0.36)          # junction box w, depth, h

# Runs as (x, z) polylines on the wall, read off the daytime reference.
PURPLE_RUNS = [
    [(-6.95, 6.3), (-3.35, 6.3), (-3.35, 3.05), (-2.78, 3.05)],        # left: over cornice, down the arch
    [(-3.35, 6.3), (-3.35, 7.55), (-2.35, 7.55), (-2.35, 8.3)],        # left: up into the mural
    [(2.72, 6.3), (3.9, 6.3), (3.9, 7.45)],                            # right: shoulder to window box
    [(3.9, 6.3), (3.9, 4.65), (3.32, 4.65), (3.32, 4.42)],             # right: down to the offer board
    [(-6.95, 5.2), (-6.1, 5.2), (-6.1, 4.1)],                          # left corner feed to the lantern
]
GREEN_RUNS = [
    [(4.32, 6.75), (4.32, 1.0)],                                       # right riser to the ground box
    [(2.72, 6.55), (3.55, 6.55), (3.55, 7.3)],
]
BOXES = [(-5.55, 6.3), (-3.35, 6.3), (3.9, 6.3), (3.9, 7.45), (4.32, 1.0), (-6.1, 5.2)]
END_GLANDS = [(-2.78, 3.05), (-2.35, 8.3), (3.32, 4.42), (3.55, 7.3)]
# Ground-floor cornice: vertical runs crossing it jog out over the ledge.
CORNICE_Z = (5.5, 6.06)
CORNICE_DEPTH = 0.40


def route(run, radius):
    """(x, z) wall polyline -> 3D points, jogging over the cornice where needed."""
    wall_y = -(radius + 0.012)
    out_y = -(CORNICE_DEPTH + radius + 0.01)
    lo, hi = CORNICE_Z
    pts = [(run[0][0], wall_y, run[0][1])]
    for (x0, z0), (x1, z1) in zip(run, run[1:]):
        if abs(x1 - x0) < 1e-6 and min(z0, z1) < lo and max(z0, z1) > hi:
            first, second = (hi + 0.02, lo - 0.02) if z1 < z0 else (lo - 0.02, hi + 0.02)
            step = 0.12 if z1 < z0 else -0.12
            pts += [(x0, wall_y, first + step), (x0, out_y, first),
                    (x0, out_y, second), (x0, wall_y, second - step)]
        pts.append((x1, wall_y, z1))
    return pts


def mat(name):
    m = bpy.data.materials.get(name)
    if m is None:
        raise KeyError(f"material {name} missing; run the arch build first")
    return m


def tube_mesh(bm, pts3, radius, mat_index, segments=16, corner=0.12):
    """Sweep a circle along a polyline with rounded corners."""
    path = [Vector(p) for p in pts3]
    smooth = [path[0]]
    for a, b, c in zip(path, path[1:], path[2:]):
        d1 = (b - a).normalized()
        d2 = (c - b).normalized()
        r = min(corner, (b - a).length / 2, (c - b).length / 2)
        p0, p1 = b - d1 * r, b + d2 * r
        for t in [i / 6 for i in range(7)]:
            smooth.append((1 - t) ** 2 * p0 + 2 * (1 - t) * t * b + t ** 2 * p1)
    smooth.append(path[-1])
    rings = []
    prev_n = None
    for i, p in enumerate(smooth):
        tan = (smooth[min(i + 1, len(smooth) - 1)] - smooth[max(i - 1, 0)]).normalized()
        n = prev_n if prev_n is not None else Vector((0, -1, 0))
        n = (n - tan * n.dot(tan)).normalized()
        if n.length < 1e-6:
            n = tan.orthogonal().normalized()
        prev_n = n
        bnorm = tan.cross(n)
        ring = []
        for k in range(segments):
            a = 2 * math.pi * k / segments
            ring.append(bm.verts.new(p + (n * math.cos(a) + bnorm * math.sin(a)) * radius))
        rings.append(ring)
    for r0, r1 in zip(rings, rings[1:]):
        for k in range(segments):
            f = bm.faces.new((r0[k], r0[(k + 1) % segments], r1[(k + 1) % segments], r1[k]))
            f.material_index = mat_index
            f.smooth = True
    for ring in (rings[0], rings[-1][::-1]):
        f = bm.faces.new(ring)
        f.material_index = mat_index
    return smooth


def add_box(bm, center, size, mat_index, rot=Matrix.Identity(3)):
    res = bmesh.ops.create_cube(bm, size=1.0)
    for v in res["verts"]:
        v.co = Vector(center) + rot @ Vector((v.co.x * size[0], v.co.y * size[1], v.co.z * size[2]))
    for f in {f for v in res["verts"] for f in v.link_faces}:
        f.material_index = mat_index
    return res["verts"]


def add_cyl(bm, center, axis, radius, depth, mat_index, segments=12):
    res = bmesh.ops.create_cone(bm, cap_ends=True, segments=segments, radius1=radius,
                                radius2=radius, depth=depth)
    rot = Vector((0, 0, 1)).rotation_difference(Vector(axis).normalized()).to_matrix()
    for v in res["verts"]:
        v.co = Vector(center) + rot @ v.co
    for f in {f for v in res["verts"] for f in v.link_faces}:
        f.material_index = mat_index
        f.smooth = True


def clamps_along(bm, path, radius, steel, black, seed):
    """Mismatched clips: saddle clamps, P-clips and the odd cable tie."""
    total = sum((b - a).length for a, b in zip(path, path[1:]))
    s, i = CLAMP_STEP * 0.5, 0
    segs = list(zip(path, path[1:]))
    while s < total:
        acc = 0.0
        for a, b in segs:
            L = (b - a).length
            if acc + L >= s:
                t = (s - acc) / L
                p = a.lerp(b, t)
                tan = (b - a).normalized()
                break
            acc += L
        kind = (seed + i) % 5
        if p.y < -0.1 or CORNICE_Z[0] - 0.2 < p.z < CORNICE_Z[1] + 0.2:
            s += CLAMP_STEP * 0.5        # no clamps on the jog over the cornice
            i += 1
            continue
        side = tan.cross(Vector((0, -1, 0))).normalized()
        wall_y = 0.0
        if kind in (0, 1, 3):          # saddle clamp: strap over the tube, two screws
            add_box(bm, (p.x, p.y - radius * 0.2, p.z), (radius * 2.6 + 0.05, 0.022, radius * 1.15),
                    steel, Matrix((side, Vector((0, 1, 0)), tan)).transposed())
            for sgn in (-1, 1):
                q = p + side * sgn * (radius + 0.03)
                add_cyl(bm, (q.x, wall_y - 0.006, q.z), (0, 1, 0), 0.009, 0.012, steel, 8)
        elif kind == 2:                 # P-clip: darker, one screw, offset
            add_box(bm, (p.x, p.y, p.z), (radius * 2.4, 0.03, radius * 2.6), black,
                    Matrix((side, Vector((0, 1, 0)), tan)).transposed())
            q = p + side * (radius + 0.035)
            add_cyl(bm, (q.x, wall_y - 0.008, q.z), (0, 1, 0), 0.011, 0.016, steel, 8)
        else:                           # cable tie
            add_cyl(bm, (p.x, p.y, p.z), tan, radius * 1.18, 0.012, black, 12)
        s += CLAMP_STEP * (0.85 + 0.3 * ((seed * 7 + i * 3) % 5) / 4)
        i += 1


def junction_box(bm, x, z, metal, steel, black):
    w, d, h = BOX
    y = -d / 2
    add_box(bm, (x, y, z), (w, d, h), metal)
    add_box(bm, (x, -d - 0.006, z), (w - 0.02, 0.012, h - 0.02), metal)          # lid
    for sx in (-1, 1):
        for sz in (-1, 1):
            add_cyl(bm, (x + sx * (w / 2 - 0.025), -d - 0.014, z + sz * (h / 2 - 0.025)),
                    (0, 1, 0), 0.008, 0.008, steel, 8)
    # Cable glands top and bottom, each with a sealant collar.
    for sz in (-1, 1):
        add_cyl(bm, (x, y, z + sz * (h / 2 + 0.02)), (0, 0, 1), 0.024, 0.04, steel, 12)
        add_cyl(bm, (x, y, z + sz * (h / 2 + 0.004)), (0, 0, 1), 0.034, 0.012, black, 12)
    # Mounting tabs screwed into the stone.
    for sz in (-1, 1):
        add_box(bm, (x, -0.004, z + sz * (h / 2 + 0.05)), (0.05, 0.006, 0.04), steel)


def build_conduit_set():
    coll = aa.kit_collection("aa_prop_conduit_set")
    obj = next(o for o in coll.objects if o.type == "MESH")
    me = obj.data
    me.materials.clear()
    names = ["aa_tmp_conduit_green", "aa_tmp_conduit_purple", "aa_tmp_junction_metal",
             "aa_tmp_clip_steel", "aa_tmp_clip_black"]
    if bpy.data.materials.get("aa_tmp_clip_black") is None:
        m = bpy.data.materials.new("aa_tmp_clip_black")
        m.use_nodes = True
        b = m.node_tree.nodes["Principled BSDF"]
        b.inputs["Base Color"].default_value = (0.02, 0.02, 0.022, 1)
        b.inputs["Roughness"].default_value = 0.5
    for n in names:
        me.materials.append(mat(n))
    GREEN, PURPLE, METAL, STEEL, BLACK = range(5)
    bm = bmesh.new()
    for i, run in enumerate(PURPLE_RUNS):
        pts = route(run, PURPLE_R)
        tube_mesh(bm, pts, PURPLE_R, PURPLE)
        clamps_along(bm, [Vector(p) for p in pts], PURPLE_R, STEEL, BLACK, i)
    for i, run in enumerate(GREEN_RUNS):
        pts = route(run, GREEN_R)
        tube_mesh(bm, pts, GREEN_R, GREEN)
        clamps_along(bm, [Vector(p) for p in pts], GREEN_R, STEEL, BLACK, i + 2)
    metal = mat("aa_tmp_junction_metal").node_tree.nodes["Principled BSDF"]
    metal.inputs["Base Color"].default_value = (0.36, 0.37, 0.38, 1)   # galvanised grey
    metal.inputs["Metallic"].default_value = 0.85
    metal.inputs["Roughness"].default_value = 0.42
    for x, z in BOXES:
        junction_box(bm, x, z, METAL, STEEL, BLACK)
    for x, z in END_GLANDS:
        add_cyl(bm, (x, -0.046, z), (1, 0, 0), 0.042, 0.05, BLACK, 12)
    bm.to_mesh(me)
    bm.free()
    if "uv_material" not in me.uv_layers:
        me.uv_layers.new(name="uv_material")
    me.update()
    return len(me.vertices)


def archivolt_outline(offset):
    """Outer edge of the archivolt (from its mesh), pushed out by `offset` metres."""
    arch = bpy.data.objects["aa_arch_hero_archivolt"]
    co = [v.co for v in arch.data.vertices]
    prof = []
    z = 2.0
    while z <= 5.3:
        xs = [c.x for c in co if z - 0.05 <= c.z < z + 0.05]
        if xs:
            prof.append((max(xs), z))
        z += 0.1
    top = max(c.z for c in co)
    # Offset the right half outward along its 2D normal, mirror for the left.
    right = []
    for (x0, z0), (x1, z1) in zip(prof, prof[1:]):
        t = Vector((x1 - x0, z1 - z0)).normalized()
        n = Vector((t.y, -t.x))
        right.append((x0 + n.x * offset, z0 + n.y * offset))
    right.append((0.0, top + offset))
    # Left foot up to the crown, then down to the right foot.
    return [(-x, z) for x, z in right] + list(reversed(right[:-1]))


def build_neon_extrados():
    coll = aa.kit_collection("aa_arch_hero")
    name = "aa_arch_hero_neon_extrados"
    obj = bpy.data.objects.get(name)
    if obj is None:
        obj = bpy.data.objects.new(name, bpy.data.meshes.new(name))
        coll.objects.link(obj)
    me = obj.data
    me.materials.clear()
    for n in ("aa_tmp_conduit_green", "aa_tmp_clip_steel", "m_aa_glass_acrylic"):
        me.materials.append(mat(n))
    bm = bmesh.new()
    pts = [(x, -0.25, z) for x, z in archivolt_outline(0.11)]
    path = tube_mesh(bm, pts, 0.026, 0, corner=0.0)
    # LED/acrylic brackets: acrylic standoff + steel foot every ~0.35 m.
    acc = 0.0
    for a, b in zip(path, path[1:]):
        acc += (b - a).length
        if acc < 0.35:
            continue
        acc = 0.0
        add_box(bm, (b.x, -0.225, b.z), (0.035, 0.05, 0.05), 2)
        add_box(bm, (b.x, -0.205, b.z), (0.07, 0.01, 0.07), 1)
    bm.to_mesh(me)
    bm.free()
    if "uv_material" not in me.uv_layers:
        me.uv_layers.new(name="uv_material")
    me.update()
    return len(me.vertices)


def main():
    return {"conduit_verts": build_conduit_set(), "extrados_verts": build_neon_extrados()}


result = main()
print(result)
