"""E2 round 2: pots, mounded shrubs, flowering cascades (sill-pivot frame, metres).

Shrubs are built as real geometry: a few main stems, twigs out to the surface of a mound
(ellipsoid sized to the crop), and clusters of cupped, rounded leaves in overlapping layers.
Every leaf sits on a twig and every twig on a stem, so nothing floats.
"""
import math

from mathutils import Matrix, Vector

from e2_lib import rng

LEAF_ROWS = [0.0, 0.14, 0.32, 0.52, 0.72, 0.88, 1.0]
LEAF_COLS = [-1.0, -0.5, 0.0, 0.5, 1.0]
PALETTE = [(0.10, 0.22, 0.030), (0.06, 0.15, 0.020), (0.17, 0.31, 0.045),
           (0.04, 0.10, 0.015), (0.13, 0.26, 0.035), (0.21, 0.36, 0.06)]


# --------------------------------------------------------------------------------------
# pots
# --------------------------------------------------------------------------------------
def pot2(mb, c, rt, h, rb, mat="terracotta", bulge=0.0, seg=36):
    """Classic tapered flower pot: straight taper, rolled rim bead, inner wall, soil.
    rt = radius at the top of the rim, h = overall height, rb = foot radius."""
    x, y, z = c
    rim_h = h * 0.17
    bead = rim_h * 0.5
    body_top = h - rim_h
    r_bt = rt - bead * 0.55            # body radius where the rim starts
    prof = [(0.0, 0.0), (rb, 0.0), (rb + 0.004, 0.006)]
    for i in range(1, 7):
        t = i / 7
        r = rb + (r_bt - rb) * t + bulge * rt * math.sin(math.pi * t)
        prof.append((r, 0.006 + (body_top - 0.006) * t))
    # rolled rim: a half-round bead standing proud of the body
    cz = body_top + rim_h * 0.5
    for i in range(9):
        a = -math.pi / 2 + math.pi * i / 8
        prof.append((r_bt + bead * 0.55 + bead * 0.45 * math.cos(a) + (rim_h * 0.12 if 2 < i < 6 else 0.0) * 0,
                     cz + rim_h * 0.5 * math.sin(a)))
    th = max(0.007, rt * 0.07)
    prof += [(rt - th, h - 0.002), (rt - th * 1.3, h - rim_h * 0.6), (r_bt - th * 1.4, h * 0.9), (0.0, h * 0.9)]
    mb.lathe(prof, seg, mat, center=(x, y, z), cap_bottom=True, cap_top=False)
    r_s = r_bt - th * 1.4
    mb.lathe([(r_s + 0.002, 0.0), (r_s * 0.85, 0.008), (r_s * 0.4, 0.016), (0.0, 0.018)], 24, "soil",
             center=(x, y, z + h * 0.9 - 0.004), cap_bottom=True)
    return Vector((x, y, z + h * 0.9 + 0.01)), r_s


# --------------------------------------------------------------------------------------
# leaves
# --------------------------------------------------------------------------------------
def leaf2(base, axis, side, size, width=0.62, cup=0.22, curl=0.18, twist=0.0):
    """Rounded, cupped ovate leaf: one base vertex, one tip vertex, 5 rows x 5 columns between."""
    axis = axis.normalized()
    side = (side - axis * side.dot(axis)).normalized()
    nrm = axis.cross(side).normalized()
    verts, uvv = [base.copy()], [(0.5, 0.0)]
    for t in LEAF_ROWS[1:-1]:
        w = size * width * 0.5 * (math.sin(math.pi * t) ** 0.65) * (1.0 - 0.22 * t)
        c = base + axis * (size * t) + nrm * (curl * size * t * t)
        rot = Matrix.Rotation(twist * t, 3, axis)
        for col in LEAF_COLS:
            off = rot @ (side * (w * col)) + nrm * (cup * w * col * col)
            verts.append(c + off)
            uvv.append((0.5 + 0.5 * col, t))
    verts.append(base + axis * size + nrm * (curl * size))
    uvv.append((0.5, 1.0))
    nc = len(LEAF_COLS)
    nr = len(LEAF_ROWS) - 2
    tip = len(verts) - 1
    faces = [(0, 1 + j + 1, 1 + j) for j in range(nc - 1)]
    for r in range(nr - 1):
        a = 1 + r * nc
        b = 1 + (r + 1) * nc
        for j in range(nc - 1):
            faces.append((a + j, a + j + 1, b + j + 1, b + j))
    last = 1 + (nr - 1) * nc
    faces += [(last + j, last + j + 1, tip) for j in range(nc - 1)]
    uvs = [[uvv[k] for k in f] for f in faces]
    return verts, faces, uvs


def _add_leaf(leaves, tints, R, p, axis, size, palette, cup=0.22, width=0.62):
    side = axis.orthogonal()
    side = Matrix.Rotation(R.uniform(0, 2 * math.pi), 3, axis) @ side
    v, f, uv = leaf2(p, axis, side, size, width=width * R.uniform(0.85, 1.15), cup=cup * R.uniform(0.6, 1.3),
                     curl=R.uniform(-0.05, 0.3), twist=R.uniform(-0.6, 0.6))
    leaves.add([tuple(x) for x in v], f, "leaf", uvs=uv)
    col = palette[R.randrange(len(palette))]
    j = R.uniform(0.8, 1.25)
    tints.extend([(col[0] * j, col[1] * j, col[2] * j)] * len(f))


def flower2(mb, p, nrm, r, mat, R):
    """Five-petal flower: cupped petal disc + centre boss; centre touches the twig point."""
    nrm = nrm.normalized()
    u = nrm.orthogonal().normalized()
    v = nrm.cross(u)
    n = 20
    ring1, ring2 = [], []
    for i in range(n):
        a = 2 * math.pi * i / n
        pet = 0.62 + 0.38 * abs(math.cos(5 * a / 2)) ** 0.7
        d = (u * math.cos(a) + v * math.sin(a))
        ring1.append(p + d * r * 0.45 * pet + nrm * r * 0.12)
        ring2.append(p + d * r * pet + nrm * r * 0.32 * pet)
    c = p + nrm * 0.002
    vs = [c] + ring1 + ring2
    fs = [(0, 1 + i, 1 + (i + 1) % n) for i in range(n)]
    fs += [(1 + i, 1 + n + i, 1 + n + (i + 1) % n, 1 + (i + 1) % n) for i in range(n)]
    mb.add([tuple(x) for x in vs], fs, mat)
    from e2_parts import _centre_dome
    _centre_dome(mb, c + nrm * r * 0.1, nrm, r * 0.18)


# --------------------------------------------------------------------------------------
# shrubs
# --------------------------------------------------------------------------------------
def bush(leaves, stems, tints, base, rx, ry, rz, n_leaves, leaf_size, seed, lift=0.0, palette=None,
         flowers=None, droop=0.25, leaf_width=0.62, n_main=6, lean=(0.0, 0.0, 0.0)):
    """Mounded shrub filling an ellipsoid (rx, ry, rz) whose centre sits rz*0.8 + lift above `base`."""
    R = rng(seed)
    palette = palette or PALETTE
    base = Vector(base)
    c = base + Vector((lean[0], lean[1], rz * 0.8 + lift))
    tips = []
    for i in range(n_main):
        t = Vector((R.uniform(-1, 1) * rx * 0.45, R.uniform(-1, 1) * ry * 0.45, R.uniform(-0.3, 0.4) * rz)) + c
        p0 = base + Vector((R.uniform(-1, 1) * 0.02, R.uniform(-1, 1) * 0.02, -0.012))
        mid = p0.lerp(t, 0.5) + Vector((R.uniform(-1, 1) * 0.02, R.uniform(-1, 1) * 0.02, 0.0))
        pts = [p0.lerp(mid, k / 3) for k in range(3)] + [mid.lerp(t, k / 3) for k in range(1, 4)]
        stems.tube(pts, 0.0032, "stem", sides=5, r_end=0.002, roll=R.uniform(0, 6.283))
        tips.append(t)
    n_cl = max(4, n_leaves // 7)
    for k in range(n_cl):
        d = Vector((R.gauss(0, 1), R.gauss(0, 1), R.gauss(0, 1)))
        d.z = abs(d.z) * 1.1 - droop * abs(R.gauss(0, 1))
        d.normalize()
        s = c + Vector((d.x * rx, d.y * ry, d.z * rz)) * R.uniform(0.62, 1.0)
        t0 = min(tips, key=lambda q: (q - s).length)
        bend = t0.lerp(s, 0.55) + Vector((0, 0, R.uniform(0.0, 0.03)))
        twig = [t0, t0.lerp(bend, 0.5), bend, bend.lerp(s, 0.5), s]
        stems.tube(twig, 0.0018, "stem", sides=5, r_end=0.0011, roll=R.uniform(0, 6.283))
        nl = int(R.uniform(5, 9))
        for i in range(nl):
            f = 0.45 + 0.55 * (i + R.random()) / nl
            seg = min(int(f * 4), 3)
            p = twig[seg].lerp(twig[seg + 1], f * 4 - seg)
            out = (d * 0.85 + Vector((R.gauss(0, 0.45), R.gauss(0, 0.45), R.gauss(0.25, 0.35)))).normalized()
            _add_leaf(leaves, tints, R, p, out, leaf_size * R.uniform(0.65, 1.25), palette, width=leaf_width)
        if flowers and R.random() < flowers[2]:
            fr, fmats = flowers[0], flowers[1]
            fm = fmats if isinstance(fmats, str) else fmats[R.randrange(len(fmats))]
            flower2(stems, s, d + Vector((0, -0.4, 0.3)), fr * R.uniform(0.8, 1.2), fm, R)


def cascade(leaves, stems, tints, start, length, n, seed, side=-1, fmats=("petal_pink",), flower_p=0.45,
            leaf_size=0.042, spread=0.18, palette=None):
    """Dense flowering cascade: a crown of stems arching over the ledge edge and hanging down,
    leafy all the way, flowers clustered in the upper two thirds."""
    R = rng(seed)
    palette = palette or PALETTE
    sx, sy, sz = start
    for s in range(n):
        L = length * R.uniform(0.55, 1.0)
        out = R.uniform(0.02, spread)
        ox, oy = R.uniform(-0.04, 0.04), R.uniform(-0.03, 0.03)
        fy = R.uniform(0.10, 0.22)
        pts = []
        for i in range(16):
            t = i / 15
            arch = math.sin(math.pi / 2 * min(t * 3.0, 1.0))
            x = sx + ox + side * (out * arch + 0.03 * t + R.uniform(-0.01, 0.01) * t)
            y = sy + oy - fy * arch - 0.02 * t
            z = sz + 0.05 * math.sin(math.pi * min(t * 3.0, 1.0)) - L * max(0.0, t - 0.2) / 0.8
            pts.append(Vector((x, y, z)))
        stems.tube(pts, 0.0026, "stem", sides=5, r_end=0.0012, roll=R.uniform(0, 6.283))
        for i in range(1, 15):
            for _ in range(2):
                f = R.random()
                p = pts[i].lerp(pts[i + 1], f)
                tang = (pts[i + 1] - pts[i]).normalized()
                out_v = (tang.orthogonal().normalized())
                out_v = Matrix.Rotation(R.uniform(0, 6.283), 3, tang) @ out_v
                axis = (out_v + Vector((side * 0.3, -0.8, 0.35))).normalized()
                _add_leaf(leaves, tints, R, p, axis, leaf_size * R.uniform(0.7, 1.2) * (1.0 - 0.3 * i / 15), palette)
            if i < 12 and R.random() < flower_p * (1.3 - i / 13):
                for _ in range(R.randint(1, 3)):
                    p = pts[i].lerp(pts[i + 1], R.random())
                    nrm = Vector((side * R.uniform(0, 0.6), -1.0, R.uniform(-0.2, 0.7)))
                    flower2(stems, p, nrm, 0.022 * R.uniform(0.8, 1.25), fmats[R.randrange(len(fmats))], R)


def wall_cascade(leaves, stems, tints, root, ledge_end_x, ledge_front_y, ledge_top_z, drop, n, seed, side=-1,
                 fmats=("petal_pink",), flower_p=0.6, leaf_size=0.045, spread=(-0.28, 0.12), palette=None):
    """Flowering vine rooted in a pot at the ledge end: stems run out over the ledge's end and front
    corner, then drape down hugging the wall (y -> -0.03), fanning sideways; leafy throughout, flowers
    densest in the upper half (crop w3)."""
    R = rng(seed)
    palette = palette or PALETTE
    rx, ry, rz = root
    for k in range(n):
        L = drop * R.uniform(0.5, 1.0)
        fan = R.uniform(*spread)
        lip_x = ledge_end_x + side * R.uniform(-0.06, 0.05)
        lip_y = ledge_front_y - R.uniform(0.0, 0.04)
        hug_y = -R.uniform(0.025, 0.09)
        p0 = Vector((rx + R.uniform(-0.03, 0.03), ry + R.uniform(-0.03, 0.03), rz))
        p1 = Vector((lip_x, lip_y * 0.5, ledge_top_z + R.uniform(0.02, 0.07)))
        p2 = Vector((lip_x + side * 0.02, lip_y, ledge_top_z - 0.02))
        pts = [p0, p0.lerp(p1, 0.5) + Vector((0, 0, 0.03)), p1, p2]
        for i in range(1, 11):
            t = i / 10
            x = p2.x + side * fan * (t ** 0.8) + R.uniform(-0.012, 0.012)
            y = p2.y + (hug_y - p2.y) * min(1.0, t * 2.5)
            z = p2.z - L * t
            pts.append(Vector((x, y, z)))
        stems.tube(pts, 0.0026, "stem", sides=5, r_end=0.0012, roll=R.uniform(0, 6.283))
        for i in range(1, len(pts) - 1):
            for _ in range(3):
                p = pts[i].lerp(pts[i + 1], R.random())
                tang = (pts[i + 1] - pts[i]).normalized()
                out_v = Matrix.Rotation(R.uniform(0, 6.283), 3, tang) @ tang.orthogonal().normalized()
                axis = (out_v + Vector((0, -1.0, 0.25))).normalized()
                _add_leaf(leaves, tints, R, p, axis, leaf_size * R.uniform(0.7, 1.2), palette)
            if i < 9 and R.random() < flower_p * (1.25 - i / 12):
                for _ in range(R.randint(1, 3)):
                    p = pts[i].lerp(pts[i + 1], R.random())
                    flower2(stems, p, Vector((side * R.uniform(-0.3, 0.5), -1.0, R.uniform(-0.1, 0.6))),
                            0.023 * R.uniform(0.8, 1.25), fmats[R.randrange(len(fmats))], R)
