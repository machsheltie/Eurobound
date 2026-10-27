"""Electrical retrofit hardware for the Absinthe Arcade, per the production reference.

Rebuilds aa_prop_conduit_set (purple and green conduit runs, mismatched clamps
drilled into the stone, sealed junction boxes with cable glands), and on the arch
hero aa_arch_hero_neon_extrados (green neon tube on the outer arch order, on
acrylic standoffs) and aa_arch_hero_marquee_mounts (the steel that hangs the
marquee lightbox in front of the arch). Reference: "5. Electrical / mounting
detail" and "11. Electrical / mounting details" on the daytime sheets.

Everything sits on the real masonry: the facade has depth planes, cornices and
surrounds (build_shell.py), so conduit runs are raycast against the stone and
jog out over whatever they cross, and boxes, clamps and brackets land on the
face they are screwed to. Run build_shell.py first. Safe to re-run.

Blender space: street toward -Y, z up.
"""

import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402
import build_shell as shell  # noqa: E402

PURPLE_R = 0.034
GREEN_R = 0.03
CLAMP_STEP = 0.42
BOX = (0.30, 0.12, 0.36)          # junction box w, depth, h
STANDOFF = 0.012                  # gap between conduit and stone

# Runs read off the daytime reference. (x, z) points run on the wall; (x, y, z) points
# are free-hanging (flexible conduit into a sign).
PURPLE_RUNS = [
    # left: over the cornice, down beside the arch, flexible tail into the marquee's underside
    [(-6.95, 6.3), (-3.45, 6.3), (-3.45, 3.15), (-2.62, -0.66, 3.1), (-2.1, -0.66, 3.3)],
    [(-3.45, 6.3), (-3.45, 7.55), (-2.35, 7.55), (-2.35, 8.3)],        # left: up into the mural
    [(2.72, 6.3), (3.9, 6.3), (3.9, 7.45)],                            # right: shoulder to window box
    [(3.9, 6.3), (3.9, 4.65), (3.22, 4.65), (3.22, 3.1)],              # right: down into the offer board
    [(-6.95, 5.2), (-6.1, 5.2), (-6.1, 4.1)],                          # left corner feed to the lantern
]
GREEN_RUNS = [
    [(4.32, 6.75), (4.32, 1.0)],                                       # right riser to the ground box
    [(2.72, 6.55), (3.55, 6.55), (3.55, 7.3)],
]
BOXES = [(-5.55, 6.3), (-3.45, 6.3), (3.9, 6.3), (3.9, 7.45), (4.32, 1.0), (-6.1, 5.2)]

# The masonry everything is fixed to.
STONE = ("aa_shell_facade_walls", "aa_shell_facade_mouldings", "aa_shell_facade_quoins",
         "aa_shell_facade_window_surrounds", "aa_arch_hero_archivolt", "aa_arch_hero_plinths",
         "aa_arch_hero_cartouche")


class Facade:
    """Raycasts against the stone. surf(x, z) is the y of the face a fixing would hit."""

    def __init__(self, names=STONE):
        dg = bpy.context.evaluated_depsgraph_get()
        self.trees = []
        for n in names:
            o = bpy.data.objects[n]
            bm = bmesh.new()
            bm.from_object(o, dg)
            bm.transform(o.matrix_world)
            self.trees.append((n, BVHTree.FromBMesh(bm)))
            bm.free()

    def ray(self, origin, direction=(0, 1, 0), dist=8.0):
        best = (None, None, dist)
        for n, t in self.trees:
            loc, _, _, d = t.ray_cast(Vector(origin), Vector(direction), dist)
            if loc is not None and d < best[2]:
                best = (loc, n, d)
        return best[0], best[1]

    def surf(self, x, z):
        loc, _ = self.ray((x, -4.0, z))
        return loc.y if loc is not None else 0.0

    def proud(self, x, z, rx, rz, n=3):
        """Most-proud face over an rx by rz half-extent footprint."""
        return min(self.surf(x + rx * (2 * i / (n - 1) - 1), z + rz * (2 * j / (n - 1) - 1))
                   for i in range(n) for j in range(n))


def route(face, run, radius, ramp=0.08, step=0.03):
    """Run -> 3D points hugging the stone, offsetting out over anything proud it crosses."""
    pts = []
    for a, b in zip(run, run[1:]):
        if len(b) == 3:
            if len(a) == 2 and not pts:
                pts.append(Vector((a[0], face.surf(*a) - radius - STANDOFF, a[1])))
            pts.append(Vector(b))
            continue
        if len(a) == 3:
            raise ValueError("a free-hanging point must end its run")
        A, B = Vector((a[0], a[1])), Vector((b[0], b[1]))
        L = (B - A).length
        d = (B - A) / L
        q = Vector((-d.y, d.x)) * (radius + 0.01)
        n = max(2, int(L / step) + 1)
        ss = [L * i / (n - 1) for i in range(n)]
        raw = []
        for s in ss:
            p = A + d * s
            raw.append(min(face.surf(p.x + o.x, p.y + o.y) for o in (Vector((0, 0)), q, -q)))
        win = ramp + radius
        ys = [min(r for s2, r in zip(ss, raw) if abs(s2 - s) <= win) - radius - STANDOFF for s in ss]

        def at(s, y):
            p = A + d * s
            return Vector((p.x, y, p.y))

        seg = [at(0.0, ys[0])]
        last_s = 0.0
        for i in range(1, n):
            dy = ys[i] - ys[i - 1]
            if abs(dy) < 0.004:
                continue
            if dy < 0:          # stepping out: ramp before the step, over free wall
                s0 = max(last_s, ss[i] - ramp)
                seg += [at(s0, ys[i - 1]), at(ss[i], ys[i])]
                last_s = ss[i]
            else:               # stepping back in: ramp after leaving the obstacle
                s1 = min(L, ss[i - 1] + ramp)
                seg += [at(ss[i - 1], ys[i - 1]), at(s1, ys[i])]
                last_s = s1
        seg.append(at(L, ys[-1]))
        clean = [seg[0]]
        for p in seg[1:]:
            if (p - clean[-1]).length > 1e-4:
                clean.append(p)
        pts += clean if not pts else clean[1:] if (clean[0] - pts[-1]).length < 1e-4 else clean
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


def plate(bm, x, z, wall_y, w, h, steel, bolts=4):
    """Steel mounting plate screwed to the stone face at wall_y, with bolt heads."""
    add_box(bm, (x, wall_y - 0.005, z), (w, 0.01, h), steel)
    corners = [(-1, -1), (1, 1), (-1, 1), (1, -1)][:bolts]
    for sx, sz in corners:
        add_cyl(bm, (x + sx * (w / 2 - 0.022), wall_y - 0.013, z + sz * (h / 2 - 0.022)), (0, 1, 0),
                0.009, 0.008, steel, 8)


def clamps_along(bm, face, path, radius, steel, black, seed):
    """Mismatched clips where the tube lies on the stone: saddle clamps, P-clips, cable ties."""
    total = sum((b - a).length for a, b in zip(path, path[1:]))
    s, i = CLAMP_STEP * 0.5, 0
    segs = list(zip(path, path[1:]))
    while s < total:
        acc = 0.0
        for a, b in segs:
            L = (b - a).length
            if acc + L >= s:
                t = (s - acc) / max(L, 1e-9)
                p = a.lerp(b, t)
                tan = (b - a).normalized()
                break
            acc += L
        wall_y = face.surf(p.x, p.z)
        if wall_y - (p.y + radius) > 0.03 or abs(tan.y) > 0.2:
            s += CLAMP_STEP * 0.5        # off the stone (jogging over a ledge, or hanging free)
            i += 1
            continue
        kind = (seed + i) % 5
        side = tan.cross(Vector((0, -1, 0))).normalized()
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


def junction_box(bm, face, x, z, metal, steel, black):
    w, d, h = BOX
    wall = face.proud(x, z, w / 2, h / 2)
    y = wall - d / 2
    add_box(bm, (x, y, z), (w, d, h), metal)
    add_box(bm, (x, wall - d - 0.006, z), (w - 0.02, 0.012, h - 0.02), metal)          # lid
    for sx in (-1, 1):
        for sz in (-1, 1):
            add_cyl(bm, (x + sx * (w / 2 - 0.025), wall - d - 0.014, z + sz * (h / 2 - 0.025)),
                    (0, 1, 0), 0.008, 0.008, steel, 8)
    # Cable glands top and bottom, each with a sealant collar.
    for sz in (-1, 1):
        add_cyl(bm, (x, y, z + sz * (h / 2 + 0.02)), (0, 0, 1), 0.024, 0.04, steel, 12)
        add_cyl(bm, (x, y, z + sz * (h / 2 + 0.004)), (0, 0, 1), 0.034, 0.012, black, 12)
    # Mounting tabs screwed into the stone.
    for sz in (-1, 1):
        add_box(bm, (x, wall - 0.004, z + sz * (h / 2 + 0.05)), (0.05, 0.006, 0.04), steel)


def gland(bm, path, radius, black, end=True):
    """Sealing gland where a run dives into the stone or a sign."""
    a, b = (path[-2], path[-1]) if end else (path[1], path[0])
    add_cyl(bm, b, (b - a).normalized(), radius * 1.25, 0.05, black, 12)


def build_conduit_set(face):
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
    for runs, radius, m_idx, seed0 in ((PURPLE_RUNS, PURPLE_R, PURPLE, 0), (GREEN_RUNS, GREEN_R, GREEN, 2)):
        for i, run in enumerate(runs):
            pts = route(face, run, radius)
            tube_mesh(bm, pts, radius, m_idx, corner=0.06)
            clamps_along(bm, face, pts, radius, STEEL, BLACK, seed0 + i)
            if run[-1] not in [r[0] for r in runs] and run[-1] not in BOXES:
                gland(bm, pts, radius, BLACK)
            if run[0] not in BOXES and not any(run[0] in r[1:] for r in runs):
                gland(bm, pts, radius, BLACK, end=False)
    metal = mat("aa_tmp_junction_metal").node_tree.nodes["Principled BSDF"]
    metal.inputs["Base Color"].default_value = (0.36, 0.37, 0.38, 1)   # galvanised grey
    metal.inputs["Metallic"].default_value = 0.85
    metal.inputs["Roughness"].default_value = 0.42
    for x, z in BOXES:
        junction_box(bm, face, x, z, METAL, STEEL, BLACK)
    bm.to_mesh(me)
    bm.free()
    if "uv_material" not in me.uv_layers:
        me.uv_layers.new(name="uv_material")
    me.update()
    return len(me.vertices)


def hero_object(name, mats):
    obj = bpy.data.objects.get(name)
    if obj is None:
        obj = bpy.data.objects.new(name, bpy.data.meshes.new(name))
        aa.kit_collection("aa_arch_hero").objects.link(obj)
    obj.data.materials.clear()
    for n in mats:
        obj.data.materials.append(mat(n))
    return obj


def build_neon_extrados(face):
    """Green neon on the outer arch order, up both jambs, ending in glands behind the scrolls."""
    obj = hero_object("aa_arch_hero_neon_extrados",
                      ("aa_tmp_conduit_green", "aa_tmp_clip_steel", "m_aa_glass_acrylic"))
    r = 0.026
    off = shell.ORDERS[-1][0] - 0.11                       # along the outer order's face
    y_face = -shell.RUST_P - shell.ORDERS[-1][1]
    y = y_face - 0.045 - r
    H, S, R = shell.ARCH_HALF, shell.ARCH_SPRING, shell.ARCH_RISE
    bm = bmesh.new()
    for sx in (-1, 1):
        pts = [Vector((sx * (H + off), y, 1.15))]
        for i in range(0, 61):
            t = math.pi / 2 * i / 60
            p = shell.arch_point(H, S, R, t, off)
            if p.x < 1.08:                                 # the bust's scrolls hide the end
                break
            pts.append(Vector((sx * p.x, y, p.y)))
        path = tube_mesh(bm, pts, r, 0, corner=0.0)
        gland(bm, [Vector(p) for p in pts], r, 1)
        gland(bm, [Vector(p) for p in pts], r, 1, end=False)
        acc = 0.0
        for a, b in zip(path, path[1:]):
            acc += (b - a).length
            if acc < 0.35:
                continue
            acc = 0.0
            wall = face.surf(b.x, b.z)
            add_box(bm, (b.x, (wall + b.y) / 2, b.z), (0.035, wall - b.y, 0.05), 2)   # acrylic
            add_box(bm, (b.x, wall - 0.005, b.z), (0.07, 0.01, 0.07), 1)            # steel foot
    me = obj.data
    bm.to_mesh(me)
    bm.free()
    if "uv_material" not in me.uv_layers:
        me.uv_layers.new(name="uv_material")
    me.update()
    return len(me.vertices)


def build_marquee_mounts(face):
    """Square-tube standoffs from the marquee back to the arch orders, plates and bolts on the
    stone, and two stay rods with turnbuckles tying the lightbox's top back to the voussoirs."""
    obj = hero_object("aa_arch_hero_marquee_mounts", ("aa_tmp_clip_steel", "aa_tmp_clip_black"))
    STEEL, BLACK = 0, 1
    mq = bpy.data.objects["aa_arch_hero_marquee"]
    dg = bpy.context.evaluated_depsgraph_get()
    tmp = bmesh.new()
    tmp.from_object(mq, dg)
    tmp.transform(mq.matrix_world)
    mq_tree = BVHTree.FromBMesh(tmp)
    tmp.free()
    back = shell.MARQUEE_BACK
    bm = bmesh.new()
    made = {"standoffs": 0, "plates": 0}
    for sx in (-1, 1):
        for z in (3.72, 4.25, 4.75):
            for x in (2.4, 2.3, 2.2, 2.08, 1.95, 1.8):
                hit, _, _, _ = mq_tree.ray_cast(Vector((sx * x, -4.0, z)), Vector((0, 1, 0)), 8.0)
                if hit is None:
                    continue
                loc, name = face.ray((sx * x, back + 0.005, z))
                if loc is None or name != "aa_arch_hero_archivolt" or loc.y - back > 0.6:
                    continue
                L = loc.y - back
                if L > 0.04:
                    add_box(bm, (sx * x, back + L / 2, z), (0.045, L, 0.045), STEEL)
                    add_box(bm, (sx * x, back + 0.006, z), (0.09, 0.012, 0.09), STEEL)
                    made["standoffs"] += 1
                plate(bm, sx * x, z, loc.y, 0.13, 0.13, STEEL)
                made["plates"] += 1
                break
        # Stay rod: eye plate on the outer order, turnbuckle, lug on the lightbox's crown.
        p = shell.arch_point(shell.ARCH_HALF, shell.ARCH_SPRING, shell.ARCH_RISE, math.pi * 0.27,
                             shell.ORDERS[-1][0] - 0.11)
        ax, az = sx * p.x, p.y
        wall = face.surf(ax, az)
        plate(bm, ax, az, wall, 0.1, 0.12, STEEL, bolts=2)
        mx = sx * p.x * 0.78
        top, _, _, _ = mq_tree.ray_cast(Vector((mx, back - 0.15, 7.0)), Vector((0, 0, -1)), 8.0)
        if top is None:
            continue
        front, _, _, _ = mq_tree.ray_cast(Vector((mx, -4.0, top.z - 0.08)), Vector((0, 1, 0)), 8.0)
        fy = front.y if front is not None else back - 0.3
        lug = Vector((mx, fy + 0.06, top.z + 0.03))
        eye = Vector((ax, wall - 0.04, az))
        add_box(bm, (mx, fy + 0.06, top.z + 0.012), (0.08, 0.05, 0.024), STEEL)
        add_box(bm, (ax, wall - 0.025, az), (0.03, 0.04, 0.03), STEEL)
        tube_mesh(bm, [eye, lug], 0.008, STEEL, segments=8)
        mid = (eye + lug) / 2
        add_cyl(bm, mid, lug - eye, 0.017, 0.13, BLACK, 10)
    me = obj.data
    bm.to_mesh(me)
    bm.free()
    if "uv_material" not in me.uv_layers:
        me.uv_layers.new(name="uv_material")
    me.update()
    made["verts"] = len(me.vertices)
    return made


def main():
    face = Facade()
    return {"conduit_verts": build_conduit_set(face), "extrados_verts": build_neon_extrados(face),
            "marquee_mounts": build_marquee_mounts(face)}


if __name__ == "__main__" or "AA_RUN" in globals():
    result = main()
    print(result)
