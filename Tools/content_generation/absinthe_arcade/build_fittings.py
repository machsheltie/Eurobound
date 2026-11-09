"""Electrical retrofit hardware for the Absinthe Arcade, per the production reference.

Rebuilds aa_prop_conduit_set (purple and green conduit runs, mismatched clamps
drilled into the stone, sealed junction boxes with cable glands), and on the arch
hero aa_arch_hero_neon_extrados (green neon tube on the outer arch order, on
acrylic standoffs) and aa_arch_hero_marquee_mounts (the steel that hangs the
marquee lightbox in front of the arch). Also the two cast-iron downpipes
(aa_prop_drainpipe): outlet through the eave soffit, rainwater head, socketed
lengths on eared brackets, a swan neck out over the ground cornice, an offset over
the plinth and a gully at the pavement, with later repairs in newer steel. Reference: "5. Electrical / mounting
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

# Runs traced off the daytime bible on its rectified facade plane (E1 re-seat, 2026-10-28;
# temporary until E4 rebuilds the retrofit). Arch-axis coordinates, metres.
# (x, z) points run on the wall; (x, y, z) points are free-hanging (flex into a sign).
PURPLE_RUNS = [
    # left: from the coupling under the cat window's apron, along the ledge, into the box
    [(-4.07, 6.14), (-2.48, 6.14)],
    # left: down from that box beside the arch, a jog round the arch ring, down the jamb
    [(-2.48, 6.14), (-2.48, 4.62), (-2.72, 4.50), (-2.72, 3.95), (-2.47, 3.72), (-2.47, 2.0)],
    # right: from the small box beside the mural, across and down into the big box
    [(1.84, 6.02), (2.20, 6.02), (2.27, 5.50), (2.55, 5.22), (2.58, 4.97)],
    # right: big box down to the lower box, and a second feed beside it
    [(2.58, 4.97), (2.58, 3.95)],
    [(2.76, 4.85), (2.76, 4.05)],
]
# The green on the facade is the arch neon (build_neon_extrados) fed from the earcups.
GREEN_RUNS = []
# Black flex cables (power for the corner lantern, along the ledge), as in the bible.
BLACK_RUNS = [
    [(-5.30, 4.95), (-4.75, 4.62)],                             # corner lantern into the big box
    [(-4.30, 5.98), (-2.62, 5.98)],                             # along the ground-floor cornice
]
BLACK_R = 0.011
BOXES = [(-2.48, 6.14), (2.58, 4.97), (2.58, 3.95)]
# The big box beside the arched window is bolted to a steel frame in front of the left
# downpipe, as in the bible (somebody needed the spot and the pipe was in the way).
BIG_BOX = (-4.48, 4.50, (0.42, 0.14, 0.48))

# Downpipes: cast iron, 110 mm, in 1.8 m socketed lengths.
PIPE_R = 0.055
PIPE_GAP = 0.06                   # clearance behind the pipe left by the bracket ears
SOCKET_STEP = 1.8

# The masonry everything is fixed to.
STONE = ("aa_shell_facade_walls", "aa_shell_facade_mouldings", "aa_shell_facade_corner_bay",
         "aa_shell_facade_window_surrounds", "aa_arch_hero_archivolt", "aa_arch_hero_plinths",
         "aa_arch_hero_cartouche")


class Facade:
    """Raycasts against the stone. surf(x, z) is the y of the face a fixing would hit."""

    def __init__(self, names=STONE):
        dg = bpy.context.evaluated_depsgraph_get()
        self.trees = []
        for n in names:
            o = bpy.data.objects.get(n)
            if o is None:                 # e.g. aa_arch_hero_cartouche, removed in interfaces v2
                continue
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


def box_over_pipe(bm, face, metal, steel, black):
    """The big box on a channel frame standing off the wall, clear of the downpipe behind."""
    x, z, (w, d, h) = BIG_BOX
    pipe_x = shell.DRAIN["left"]["x_lower"]
    pipe_front = min(face.surf(pipe_x, z + dz) for dz in (-0.2, 0.0, 0.2)) - PIPE_GAP - 2 * PIPE_R - 0.04
    back = pipe_front - 0.015
    add_box(bm, (x, back - d / 2, z), (w, d, h), metal)
    add_box(bm, (x, back - d - 0.006, z), (w - 0.02, 0.012, h - 0.02), metal)          # lid
    for sx in (-1, 1):
        for sz in (-1, 1):
            add_cyl(bm, (x + sx * (w / 2 - 0.03), back - d - 0.014, z + sz * (h / 2 - 0.03)),
                    (0, 1, 0), 0.009, 0.008, steel, 8)
    for sz in (-1, 1):                                                                  # glands
        add_cyl(bm, (x + 0.07, back - d / 2, z + sz * (h / 2 + 0.02)), (0, 0, 1), 0.024, 0.04, steel, 12)
        add_cyl(bm, (x + 0.07, back - d / 2, z + sz * (h / 2 + 0.004)), (0, 0, 1), 0.034, 0.012, black, 12)
    # Two channel rails across the back, each on two legs into the stone either side of the pipe.
    legs = (pipe_x - PIPE_R - 0.08, x + w / 2 - 0.05)
    for zr in (z - h / 2 + 0.08, z + h / 2 - 0.08):
        add_box(bm, ((legs[0] + legs[1]) / 2, back + 0.02, zr), (legs[1] - legs[0] + 0.06, 0.04, 0.04), steel)
        for lx in legs:
            wall = face.surf(lx, zr)
            add_box(bm, (lx, (back + 0.04 + wall) / 2, zr), (0.035, wall - back - 0.04, 0.035), steel)
            plate(bm, lx, zr, wall, 0.08, 0.08, steel, bolts=2)


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
    for runs, radius, m_idx, seed0 in ((PURPLE_RUNS, PURPLE_R, PURPLE, 0), (GREEN_RUNS, GREEN_R, GREEN, 2),
                                       (BLACK_RUNS, BLACK_R, BLACK, 4)):
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
    box_over_pipe(bm, face, METAL, STEEL, BLACK)
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


# Side gland on each earcup box (x mirrored); measured with the bust's base at 5.42, so it
# follows the bust when build_shell re-seats it.
EARCUP_OUTLET = (0.79, -0.775, 6.11 + shell.GENTLEMAN_BASE - 5.42)


def trim_side_runs():
    """Drop the gentleman's old green side runs that dived into the wall behind his scrolls;
    the arch neon now runs from those earcup outlets instead, as in the reference."""
    obj = bpy.data.objects["aa_arch_hero_gentleman_hardware"]
    names = [m.name for m in obj.data.materials]
    if "aa_tmp_conduit_green" not in names:
        return 0
    gi = names.index("aa_tmp_conduit_green")
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    green = {f for f in bm.faces if f.material_index == gi}
    doomed, seen = [], set()
    for f in green:
        if f in seen:
            continue
        stack, island = [f], []
        seen.add(f)
        while stack:
            g = stack.pop()
            island.append(g)
            for e in g.edges:
                for h in e.link_faces:
                    if h in green and h not in seen:
                        seen.add(h)
                        stack.append(h)
        if min(abs(v.co.x) for g in island for v in g.verts) > 0.75:
            doomed += island
    if doomed:
        bmesh.ops.delete(bm, geom=doomed, context="FACES")
        bm.to_mesh(obj.data)
        obj.data.update()
    bm.free()
    return len(doomed)


def build_neon_extrados(face):
    """Green neon from each earcup outlet down onto the outer arch order and down the jambs."""
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
            if p.x < 1.08:                                 # leave the arch under the scrolls
                break
            pts.append(Vector((sx * p.x, y, p.y)))
        # Rise off the arch over the scrolls into the earcup's side outlet.
        ex, ey, ez = EARCUP_OUTLET
        top = pts[-1]
        pts += [Vector((sx * 1.0, (y + ey) / 2, top.z + 0.14)), Vector((sx * (ex + 0.06), ey, ez - 0.01)),
                Vector((sx * ex, ey, ez))]
        path = tube_mesh(bm, pts, r, 0, corner=0.06)
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
        for z in (3.1, 3.75, 4.35):
            for x in (2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.6, 1.4):
                hit, _, _, _ = mq_tree.ray_cast(Vector((sx * x, -4.0, z)), Vector((0, 1, 0)), 8.0)
                if hit is None:
                    continue
                loc, name = face.ray((sx * x, back + 0.005, z))
                if loc is None or name not in ("aa_arch_hero_archivolt", "aa_shell_facade_walls")                         or loc.y - back > 0.6:
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


def frustum(bm, center, bottom, top, h, mat_index):
    """Box tapering from bottom (w, d) to top (w, d), back face kept flat against the wall."""
    cx, cy, cz = center
    yb = cy + bottom[1] / 2                         # shared back plane
    rings = []
    for (w, d), z in ((bottom, cz), (top, cz + h)):
        rings.append([bm.verts.new((cx + sx * w / 2, y, z))
                      for sx, y in ((-1, yb - d), (1, yb - d), (1, yb), (-1, yb))])
    lo, hi = rings
    faces = [bm.faces.new(lo[::-1]), bm.faces.new(hi)]
    for i in range(4):
        j = (i + 1) % 4
        faces.append(bm.faces.new((lo[i], lo[j], hi[j], hi[i])))
    for f in faces:
        f.material_index = mat_index
    bmesh.ops.recalc_face_normals(bm, faces=faces)


def ear_bracket(bm, x, z, y, wall, iron, steel):
    """Original fixing: cast ears either side of the socket, nailed through spacer bobbins."""
    ty = y + PIPE_R * 0.4
    for sx in (-1, 1):
        ex = x + sx * (PIPE_R + 0.04)
        add_box(bm, (ex, ty, z), (0.06, 0.014, 0.075), iron)
        add_cyl(bm, (ex, (ty + wall) / 2, z), (0, 1, 0), 0.014, wall - ty, iron, 8)
        add_cyl(bm, (ex, ty - 0.011, z), (0, 1, 0), 0.01, 0.01, steel, 8)


def band_clamp(bm, x, z, y, wall, steel):
    """Later fixing: galvanised two-part band on a threaded rod into a wall plate."""
    add_cyl(bm, (x, y, z), (0, 0, 1), PIPE_R + 0.008, 0.03, steel, 16)
    for sx in (-1, 1):
        add_box(bm, (x + sx * (PIPE_R + 0.02), y, z), (0.03, 0.02, 0.03), steel)
        add_cyl(bm, (x + sx * (PIPE_R + 0.02), y, z), (0, 1, 0), 0.006, 0.05, steel, 6)
    add_cyl(bm, (x, (y + PIPE_R + wall) / 2, z), (0, 1, 0), 0.007, wall - y - PIPE_R, steel, 8)
    plate(bm, x, z, wall, 0.07, 0.07, steel, bolts=2)


def coupler(bm, x, y, z, black, steel, h=0.14):
    """Rubber repair coupler with two worm-drive bands."""
    add_cyl(bm, (x, y, z), (0, 0, 1), PIPE_R + 0.012, h, black, 16)
    for dz in (-h * 0.32, h * 0.32):
        add_cyl(bm, (x, y, z + dz), (0, 0, 1), PIPE_R + 0.016, 0.018, steel, 16)


def build_drainpipes(face):
    """Both downpipes, as the bible has them. Left: cast iron down the main wall beside the
    corner, a swan neck out over the ground-floor cornice that also steps right, then down
    through the big junction box's frame to the pavement (one cracked length wrapped in a
    coupler, the ground floor re-fixed with band clamps beside the old ears). Right: down the
    seam with the neighbour, over the right cornice; its ground-floor length replaced in steel."""
    coll = aa.kit_collection("aa_prop_drainpipe")
    obj = next(o for o in coll.objects if o.type == "MESH")
    me = obj.data
    me.materials.clear()
    for n in ("m_aa_iron", "aa_tmp_clip_steel", "aa_tmp_clip_black"):
        me.materials.append(mat(n))
    IRON, STEEL, BLACK = range(3)
    FA = shell.FA
    e0 = shell.EAVE0
    corona = FA["eave_cornice_z"]
    head = (e0 - 0.52, e0 - 0.14)                   # rainwater head, under the eave cornice
    y_out = -0.5                                    # outlet through the cornice soffit
    g = FA["gf_cornice"]
    dp = FA["drainpipes"]
    pipes = [(dp["left"]["x_upper"], dp["left"]["x_lower"], g["left"], False),
             (dp["right"]["x"], dp["right"]["x"], g["right"], True)]
    bm = bmesh.new()
    made = {}
    for k, (xu, xl, cor_spec, replaced) in enumerate(pipes):
        cz0, cz1 = cor_spec["z"]
        cproud = cor_spec["proud"]
        upper_wall = min(face.surf(xu, z) for z in (cz1 + 0.6, cz1 + 1.5, cz1 + 3.0, e0 - 1.0))
        ground_wall = min(face.surf(xl, z) for z in (1.4, 2.6, cz0 - 0.6))
        y_up = upper_wall - PIPE_GAP - PIPE_R
        y_gf = ground_wall - PIPE_GAP - PIPE_R
        y_neck = -cproud - 0.03 - PIPE_R            # just clear of the cornice
        y_foot = -shell.PLINTH_P - 0.03 - PIPE_R
        tube_mesh(bm, [Vector((xu, y_out, corona[0] - 0.02)), Vector((xu, y_out, e0 - 0.02)),
                       Vector((xu, y_up - 0.01, head[1] + 0.05)), Vector((xu, y_up, head[1] - 0.06))],
                  PIPE_R * 0.85, IRON, corner=0.08)
        frustum(bm, (xu, upper_wall - 0.11, head[0]), (0.2, 0.2), (0.36, 0.24), head[1] - head[0], IRON)
        add_box(bm, (xu, upper_wall - 0.125, head[1] + 0.02), (0.4, 0.27, 0.04), IRON)
        for sx in (-1, 1):
            add_box(bm, (xu + sx * 0.2, upper_wall - 0.006, head[0] + 0.12), (0.06, 0.012, 0.09), IRON)
        n_top, n_bot = cz1 + 0.45, cz0 - 0.4
        path = [Vector((xu, y_up, head[0])), Vector((xu, y_up, n_top)),
                Vector(((xu + xl) / 2, y_neck, cz1 + 0.05)), Vector((xl, y_neck, cz0 - 0.05)),
                Vector((xl, y_gf, n_bot)), Vector((xl, y_gf, 0.55)),
                Vector((xl, y_foot, 0.38)), Vector((xl, y_foot, 0.12))]
        if replaced:
            joint = Vector((xl, y_gf, n_bot - 0.4))
            tube_mesh(bm, path[:5] + [joint], PIPE_R, IRON)
            tube_mesh(bm, [joint] + path[5:], PIPE_R * 0.93, STEEL)
            coupler(bm, xl, y_gf, joint.z, BLACK, STEEL)
        else:
            tube_mesh(bm, path, PIPE_R, IRON)
            coupler(bm, xu, y_up, (head[0] + n_top) / 2, BLACK, STEEL, h=0.16)
        sockets = 0
        for (top, bottom), x, gen in (((head[0], n_top), xu, "ears"),
                                      ((n_bot, 0.55), xl, "steel" if replaced else "refixed")):
            y = y_up if gen == "ears" else y_gf
            z = top - 0.15
            while z > bottom + 0.2:
                if not (replaced and z < n_bot - 0.4):
                    add_cyl(bm, (x, y, z), (0, 0, 1), PIPE_R * 1.22, 0.1, IRON, 16)
                    add_cyl(bm, (x, y, z - 0.055), (0, 0, 1), PIPE_R * 1.12, 0.012, IRON, 16)
                wall = face.surf(x, z)
                if gen == "steel":
                    band_clamp(bm, x, z, y, wall, STEEL)
                else:
                    ear_bracket(bm, x, z, y, wall, IRON, STEEL)
                    if gen == "refixed":
                        band_clamp(bm, x, z - 0.45, y, face.surf(x, z - 0.45), STEEL)
                z -= SOCKET_STEP
                sockets += 1
        cz = (cz0 + cz1) / 2
        cor = face.surf(xl, cz)
        add_cyl(bm, (xl, y_neck, cz), (0, 0, 1), PIPE_R + 0.008, 0.03, STEEL, 16)
        if cor - y_neck - PIPE_R > 0.01:
            add_box(bm, (xl, (y_neck + PIPE_R + cor) / 2, cz), (0.03, cor - y_neck - PIPE_R, 0.025), STEEL)
        plate(bm, xl, cz, cor, 0.06, 0.05, STEEL, bolts=2)
        gy = y_foot - 0.02
        add_box(bm, (xl, gy, 0.06), (0.3, 0.26, 0.12), IRON)
        for i in range(5):
            add_box(bm, (xl - 0.1 + 0.05 * i, gy, 0.125), (0.018, 0.22, 0.012), IRON)
        made[f"pipe_{k}"] = {"y_up": round(y_up, 3), "y_gf": round(y_gf, 3), "sockets": sockets}
    # Back-corner downpipe on the right side elevation (asset sheet), straight down the side
    # wall from a rainwater head under the eave cornice to a gully. Temporary until E4.
    sr = FA["side_right"]
    yb = sr["back_downpipe"]["u"]
    xs = shell.X_RIGHT + PIPE_GAP + PIPE_R
    tube_mesh(bm, [Vector((xs + 0.45, yb, corona[0] - 0.02)), Vector((xs + 0.45, yb, e0 - 0.02)),
                   Vector((xs + 0.01, yb, head[1] + 0.05)), Vector((xs, yb, head[1] - 0.06))],
              PIPE_R * 0.85, IRON, corner=0.08)
    add_box(bm, (shell.X_RIGHT + 0.13, yb, (head[0] + head[1]) / 2), (0.24, 0.32, head[1] - head[0]), IRON)
    tube_mesh(bm, [Vector((xs, yb, head[0])), Vector((xs, yb, 0.55)),
                   Vector((xs + shell.PLINTH_P, yb, 0.38)), Vector((xs + shell.PLINTH_P, yb, 0.12))], PIPE_R, IRON)
    z = head[0] - 0.15
    while z > 0.75:
        add_cyl(bm, (xs, yb, z), (0, 0, 1), PIPE_R * 1.22, 0.1, IRON, 16)
        for sy in (-1, 1):
            ey = yb + sy * (PIPE_R + 0.04)
            add_box(bm, (xs - PIPE_R * 0.4, ey, z), (0.014, 0.06, 0.075), IRON)
            add_cyl(bm, ((xs + shell.X_RIGHT) / 2, ey, z), (1, 0, 0), 0.014, xs - shell.X_RIGHT, IRON, 8)
        z -= SOCKET_STEP
    add_box(bm, (xs + shell.PLINTH_P + 0.02, yb, 0.06), (0.26, 0.3, 0.12), IRON)
    bm.to_mesh(me)
    bm.free()
    if "uv_material" not in me.uv_layers:
        me.uv_layers.new(name="uv_material")
    me.update()
    made["verts"] = len(me.vertices)
    return made


def main():
    face = Facade()
    made = {"side_runs_removed": trim_side_runs(), "conduit_verts": build_conduit_set(face),
            "extrados_verts": build_neon_extrados(face),
            "marquee_mounts": build_marquee_mounts(face), "drainpipes": build_drainpipes(face)}
    # Manufactured edges on the boxes, plates and clamps (applied on export).
    for name in ("aa_prop_conduit_set", "aa_arch_hero_neon_extrados", "aa_arch_hero_marquee_mounts",
                 "aa_prop_drainpipe"):
        shell.soften(bpy.data.objects[name], 0.003, angle=40)
    return made


if __name__ == "__main__" or "AA_RUN" in globals():
    result = main()
    print(result)
