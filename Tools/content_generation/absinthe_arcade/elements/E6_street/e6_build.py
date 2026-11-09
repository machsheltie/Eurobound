"""Build E6 (street kit) into wip/E6_street.blend. Re-runnable.

  blender -b --factory-startup --python e6_build.py -- [--no-save]

Kept Tripo props (judged against the bible through aa_bible_cam; appended read-only from aa_exterior.blend):
cabinet, chalkboard, awning, wall lantern (x2), bollard (x6), planter. Each is decimated to a game budget and
fitted through aa_bible_cam to its bible-pixel footprint (uniform scale), ground props standing on z=0.
Built here: the two corner wall signs (TOKENS / REGRETS plaque; TOKENS / DRINKS / GAMES / REGRETS board with a
gold coupe), the metal bucket, the string lights and tangled cables under the awning, the CLOCKTOWER / PLAZA
bracket sign with its hanging lantern (Q-006, corner mounting zone from interfaces.json), the low stone post
beside the shrub, the wet cobble ground (frontage only) with puddles.
Context (not kit): mason's shell + E5 mural (from E5_surface.blend), E3 (E3_entrance.blend), E4 (E4 wip).
"""
import json
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from e6_cam import BibleCam, to_plane_z  # noqa: E402

REPO = HERE.parents[4]
ASSET = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade"
MAIN = ASSET / "blender/aa_exterior.blend"
E3WIP, E4WIP, E5WIP = (ASSET / "blender/wip" / n for n in ("E3_entrance.blend", "E4_keystone_conduits.blend",
                                                           "E5_surface.blend"))
WIP = ASSET / "blender/wip/E6_street.blend"
IFACE = json.loads((REPO / "dev/aa_team/interfaces.json").read_text(encoding="utf-8"))
FONTS = Path("C:/Windows/Fonts")
CAM = BibleCam()
PI = math.pi
STONE = ["aa_shell_facade_walls", "aa_shell_facade_mouldings", "aa_shell_facade_window_surrounds",
         "aa_shell_facade_corner_bay", "aa_arch_hero_archivolt", "aa_arch_hero_plinths"]

# bible-pixel footprints (u0, v0, u1, v1) of the kept / built props, and their front planes (y)
FIT = {
    "cabinet": ((1522, 3317, 2189, 4361), -0.80),
    "chalkboard": ((2211, 3634, 2560, 4394), -0.95),
    "awning": ((1444, 2990, 2262, 3243), -1.05),
    "lantern_l": ((1055, 2794, 1227, 3094), -0.62),
    "lantern_r": ((4875, 2250, 5000, 2500), -0.55),
    "planter": ((4330, 3825, 4580, 4388), -0.55),
}
BUCKET_PX = (2093, 4190, 2204, 4354)
STONE_POST_PX = (4650, 4250, 4838, 4538)
TALL_SIGN_PX = (1244, 3034, 1500, 3706)
SMALL_SIGN_PX = (1311, 2688, 1493, 3028)
BOLLARD_FEET = [(85, 4095), (270, 4280), (778, 4217), (888, 4233), (1055, 4710), (1300, 4350)]
BOLLARD_H = 1.0
BOLLARD_FIT = {4: (911, 3928, 1200, 4716), 5: (1222, 3805, 1378, 4350)}
TRIS = {"cabinet": 290000, "chalkboard": 120000, "awning": 150000, "lantern": 90000, "bollard": 60000,
        "planter": 160000}


def coll(name, parent=None):
    c = bpy.data.collections.get(name) or bpy.data.collections.new(name)
    p = parent or bpy.context.scene.collection
    if c.name not in [x.name for x in p.children]:
        p.children.link(c)
    return c


def lin(r, g, b):
    c = lambda v: (v / 255) / 12.92 if v / 255 <= 0.04045 else (((v / 255) + 0.055) / 1.055) ** 2.4
    return (c(r), c(g), c(b))


MATS = {}


def mat(name, base, rough=0.5, metal=0.0, emit=None, estr=0.0, coat=0.0, alpha=1.0, trans=0.0):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (*base, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    b.inputs["Coat Weight"].default_value = coat
    b.inputs["Transmission Weight"].default_value = trans
    if alpha < 1:
        b.inputs["Alpha"].default_value = alpha
        m.surface_render_method = "BLENDED"
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = estr
    MATS[name] = m
    return m


def uv_box(me):
    while me.uv_layers:
        me.uv_layers.remove(me.uv_layers[0])
    a = me.uv_layers.new(name="uv_material")
    me.uv_layers.new(name="uv_bake")
    for p in me.polygons:
        n = p.normal
        for li in p.loop_indices:
            c = me.vertices[me.loops[li].vertex_index].co
            a.data[li].uv = (c.x, c.z) if abs(n.y) >= max(abs(n.x), abs(n.z)) else \
                ((c.y, c.z) if abs(n.x) >= abs(n.z) else (c.x, c.y))


def new_obj(name, bm, mats, C, smooth=True):
    me = bpy.data.meshes.new(name)
    bad = [f for f in bm.faces if f.calc_area() < 1e-8]            # closed-ring caps, sweep-seam slivers
    if bad:
        bmesh.ops.delete(bm, geom=bad, context="FACES")
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    split_same_direction(bm)
    for f in bm.faces:
        f.smooth = smooth
    bm.to_mesh(me)
    bm.free()
    for m in mats:
        me.materials.append(m)
    uv_box(me)
    ob = bpy.data.objects.new(name, me)
    C.objects.link(ob)
    return ob


def sweep(bm, pts, r, mi=0, seg=10):
    pts = [Vector(p) for p in pts]
    rings = []
    ref = Vector((0, 0, 1))
    for i, p in enumerate(pts):
        t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        a = t.cross(ref if abs(t.dot(ref)) < 0.9 else Vector((1, 0, 0))).normalized()
        b = t.cross(a)
        rings.append([bm.verts.new(p + (a * math.cos(2 * PI * k / seg) + b * math.sin(2 * PI * k / seg)) * r)
                      for k in range(seg)])
    for i in range(len(rings) - 1):
        for k in range(seg):
            bm.faces.new((rings[i][k], rings[i][(k + 1) % seg], rings[i + 1][(k + 1) % seg],
                          rings[i + 1][k])).material_index = mi
    bm.faces.new(rings[0][::-1]).material_index = mi
    bm.faces.new(rings[-1]).material_index = mi


def box(bm, c, size, mi, rot=None):
    m = Matrix.Translation(c) @ (rot or Matrix.Identity(4)) @ Matrix.Diagonal((*size, 1))
    r = bmesh.ops.create_cube(bm, size=1.0, matrix=m)
    for v in r["verts"]:
        for f in v.link_faces:
            f.material_index = mi


def cyl(bm, c, axis, r1, r2, depth, mi, seg=24, caps=True):
    q = Vector((0, 0, 1)).rotation_difference(Vector(axis).normalized()).to_matrix().to_4x4()
    res = bmesh.ops.create_cone(bm, cap_ends=caps, segments=seg, radius1=r1, radius2=r2, depth=depth,
                                matrix=Matrix.Translation(c) @ q)
    for v in res["verts"]:
        for f in v.link_faces:
            f.material_index = mi


def text_mesh(name, body, font, m, x0, x1, z_top, z_bot, y_front, depth, C, rot_z=0.0, pivot=None):
    cu = bpy.data.curves.new(name, "FONT")
    cu.body = body
    cu.font = bpy.data.fonts.load(str(font), check_existing=True)
    cu.extrude = 0.5
    cu.align_x = "CENTER"
    tmp = bpy.data.objects.new(name + "_tmp", cu)
    C.objects.link(tmp)
    me = bpy.data.meshes.new_from_object(tmp.evaluated_get(bpy.context.evaluated_depsgraph_get()))
    bpy.data.objects.remove(tmp)
    bpy.data.curves.remove(cu)
    xs = [v.co.x for v in me.vertices]
    ys = [v.co.y for v in me.vertices]
    zs = [v.co.z for v in me.vertices]
    sz = (z_top - z_bot) / (max(ys) - min(ys))
    sx = min(sz, (x1 - x0) / (max(xs) - min(xs)))
    cx = (min(xs) + max(xs)) / 2
    for v in me.vertices:
        a, b, c = v.co
        v.co = ((x0 + x1) / 2 + (a - cx) * sx, y_front + (max(zs) - c) / (max(zs) - min(zs)) * depth,
                z_bot + (b - min(ys)) * sz)
    me.materials.append(m)
    uv_box(me)
    ob = bpy.data.objects.new(name, me)
    C.objects.link(ob)
    return ob


# =========================================================================================
# context
# =========================================================================================
def load_context():
    ctx = coll("e6_context")
    with bpy.data.libraries.load(str(E5WIP), link=False) as (src, dst):
        dst.collections = [n for n in ("e5_context_mason_shell", "aa_e5_mural") if n in src.collections]
    for c in dst.collections:
        ctx.children.link(c)
    for path, names in ((E3WIP, ("aa_e3_marquee", "aa_e3_doorway", "aa_e3_interior_set")),
                        (E4WIP, ("aa_e4_keystone", "aa_e4_conduits", "aa_e4_pipes", "aa_e4_plaque"))):
        if path.exists():
            with bpy.data.libraries.load(str(path), link=False) as (src, dst):
                dst.collections = [n for n in names if n in src.collections]
            for c in dst.collections:
                ctx.children.link(c)
    for im in bpy.data.images:
        if im.source == "FILE" and not im.packed_file:
            im.filepath = bpy.path.abspath(im.filepath, library=im.library)


class Facade:
    def __init__(self):
        dg = bpy.context.evaluated_depsgraph_get()
        self.trees = []
        for n in STONE:
            o = bpy.data.objects.get(n)
            if o is None:
                continue
            bm = bmesh.new()
            bm.from_object(o, dg)
            bm.transform(o.matrix_world)
            self.trees.append(BVHTree.FromBMesh(bm))
            bm.free()

    def cam_hit(self, u, v):
        best = None
        for t in self.trees:
            loc, nrm, _, d = t.ray_cast(Vector(CAM.loc), Vector(CAM.ray(u, v)).normalized(), 60)
            if loc is not None and (best is None or d < best[2]):
                best = (loc, nrm, d)
        return best


# =========================================================================================
# kept Tripo props
# =========================================================================================
def append_props():
    names = ["aa_prop_arcade_cabinet", "aa_prop_chalkboard", "aa_prop_awning", "aa_prop_wall_lantern",
             "aa_prop_bollard", "aa_prop_planter"]
    with bpy.data.libraries.load(str(MAIN), link=False) as (src, dst):
        dst.objects = [n for n in names if n in src.objects]
    for im in bpy.data.images:
        if im.source == "FILE" and not im.packed_file:
            im.filepath = bpy.path.abspath(im.filepath, library=im.library)
    return {o.name: o for o in dst.objects}


def decimate(ob, target):
    tmp = None
    if not ob.users_collection:
        tmp = coll("e6_tmp_eval")
        tmp.objects.link(ob)
    tris = sum(len(p.vertices) - 2 for p in ob.data.polygons)
    if tris > target:
        md = ob.modifiers.new("Decimate", "DECIMATE")
        md.ratio = target / tris
        md.use_collapse_triangulate = True
        me = bpy.data.meshes.new_from_object(ob.evaluated_get(bpy.context.evaluated_depsgraph_get()))
        old = ob.data
        ob.modifiers.clear()
        ob.data = me
        bpy.data.meshes.remove(old)
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-5)
    bad = [f for f in bm.faces if f.calc_area() < 1e-10]
    if bad:
        bmesh.ops.delete(bm, geom=bad, context="FACES")
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    split_same_direction(bm)
    bm.to_mesh(ob.data)
    bm.free()
    snap_islands(ob)
    if tmp is not None:
        tmp.objects.unlink(ob)


def snap_islands(ob, max_gap=0.06):
    """Detached Tripo islands (bracket scrolls, a leaf clump) hovering < max_gap off the main part: move each so
    it just touches (they are attached in the source art; decimation opened the hairline gap)."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.verts.ensure_lookup_table()
    seen, isl = set(), []
    for v in bm.verts:
        if v.index in seen:
            continue
        st, cur = [v], []
        seen.add(v.index)
        while st:
            x = st.pop()
            cur.append(x)
            for e in x.link_edges:
                y = e.other_vert(x)
                if y.index not in seen:
                    seen.add(y.index)
                    st.append(y)
        isl.append(cur)
    isl.sort(key=len, reverse=True)
    if len(isl) > 1:
        main = isl[0]
        mset = set(main)
        faces = [f for f in bm.faces if f.verts[0] in mset]
        tree = BVHTree.FromPolygons([v.co for v in bm.verts], [[v.index for v in f.verts] for f in faces])
        for part in isl[1:]:
            best = None
            for v in part:
                loc, nrm, _, d = tree.find_nearest(v.co)
                if loc is not None and (best is None or d < best[0]):
                    best = (d, loc - v.co)
            if best and 0.0015 < best[0] < max_gap:
                off = best[1] * (1 - 0.0005 / best[0])
                for v in part:
                    v.co += off
    # duplicate faces (same vertex set) -> keep one
    keys = {}
    dup = []
    for f in bm.faces:
        k = frozenset(v.index for v in f.verts)
        if k in keys:
            dup.append(f)
        else:
            keys[k] = f
    if dup:
        bmesh.ops.delete(bm, geom=dup, context="FACES_ONLY")
    bm.to_mesh(ob.data)
    bm.free()


def zfight_clean(ob, eps=0.001):
    """Drop the smaller face of each coplanar overlapping pair (decimation leftovers), as qa_check finds them."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.triangulate(bm, faces=bm.faces[:])
    bm.faces.ensure_lookup_table()
    tree = BVHTree.FromBMesh(bm)
    kill = set()
    for f in bm.faces:
        if f.index in kill:
            continue
        c = f.calc_center_median()
        for (loc, nrm, idx, d) in tree.find_nearest_range(c, eps):
            if idx is None or idx == f.index or idx in kill:
                continue
            g = bm.faces[idx]
            if abs(g.normal.dot(f.normal)) > 0.999 and not (set(g.verts) & set(f.verts)):
                kill.add(idx if g.calc_area() < f.calc_area() else f.index)
                break
        if f.index in kill:
            continue
        a, b, c_ = (v.co for v in f.verts)                  # qa also samples toward the corners
        for p in (c.lerp(a, .6), c.lerp(b, .6), c.lerp(c_, .6)):
            for (loc, nrm, idx, d) in tree.find_nearest_range(p, eps):
                if idx is None or idx == f.index or idx in kill:
                    continue
                g = bm.faces[idx]
                if abs(g.normal.dot(f.normal)) > 0.999 and not (set(g.verts) & set(f.verts)):
                    kill.add(idx if g.calc_area() < f.calc_area() else f.index)
                    break
    if kill:
        bmesh.ops.delete(bm, geom=[bm.faces[i] for i in kill], context="FACES_ONLY")
    bm.to_mesh(ob.data)
    bm.free()


def split_same_direction(bm):
    """Edges used twice in the same direction (decimation folds, mirrored tube joins): split them open, so
    no face pair is wound against its neighbour (qa: inconsistent winding)."""
    for _ in range(3):
        bad = []
        for e in bm.edges:
            starts = [l.vert for l in e.link_loops]
            if len(starts) != len(set(starts)):
                bad.append(e)
        if not bad:
            return
        bmesh.ops.split_edges(bm, edges=bad)
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)


def unit(ob):
    """Bake the transform, then normalise: 1 m tall, centred in x/y, bottom z=0, front (min y) at y=0."""
    me = ob.data
    me.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)
    vs = [v.co for v in me.vertices]
    lo = Vector([min(v[i] for v in vs) for i in range(3)])
    hi = Vector([max(v[i] for v in vs) for i in range(3)])
    me.transform(Matrix.Scale(1.0 / (hi.z - lo.z), 4) @ Matrix.Translation((-(lo.x + hi.x) / 2, -lo.y, -lo.z)))
    me.update()


def fit_params(co, box_px, y_front, ground=False, iters=14):
    """(s, x, z) placing unit-mesh samples co so their projection fills box_px (by height), front on y_front."""
    u0, v0, u1, v1 = box_px
    a = CAM.to_plane_y(u0, v1, y_front)
    b = CAM.to_plane_y(u0, v0, y_front)
    s = b[1] - a[1]
    x, z = CAM.to_plane_y((u0 + u1) / 2, v1, y_front)
    for _ in range(iters):
        pr = [CAM.project((x + c.x * s, y_front + c.y * s, z + c.z * s)) for c in co]
        pu0, pu1 = min(p[0] for p in pr), max(p[0] for p in pr)
        pv0, pv1 = min(p[1] for p in pr), max(p[1] for p in pr)
        s *= (v1 - v0) / (pv1 - pv0)
        uc, vc = (u0 + u1) / 2, (v0 + v1) / 2
        a1 = CAM.to_plane_y(uc, vc, y_front)
        a2 = CAM.to_plane_y(uc + 1, vc, y_front)
        mpp = abs(a2[0] - a1[0])
        x += ((u0 + u1) - (pu0 + pu1)) / 2 * mpp * 0.8
        z -= ((v0 + v1) - (pv0 + pv1)) / 2 * mpp * 0.8
        if ground:
            z = 0.0
    return s, x, z


def fit(ob, box_px, y_front, ground=False, iters=14, stretch_x=False):
    """Uniform scale + x/z so the aa_bible_cam projection fills box_px (by height), front on y_front."""
    me = ob.data
    n = len(me.vertices)
    co = [me.vertices[i].co.copy() for i in range(0, n, max(1, n // 3000))]
    u0, v0, u1, v1 = box_px
    a = CAM.to_plane_y(u0, v1, y_front)
    b = CAM.to_plane_y(u0, v0, y_front)
    s = b[1] - a[1]
    x, z = CAM.to_plane_y((u0 + u1) / 2, v1, y_front)
    for _ in range(iters):
        pr = [CAM.project((x + c.x * s, y_front + c.y * s, z + c.z * s)) for c in co]
        pu0, pu1 = min(p[0] for p in pr), max(p[0] for p in pr)
        pv0, pv1 = min(p[1] for p in pr), max(p[1] for p in pr)
        s *= (v1 - v0) / (pv1 - pv0)
        uc, vc = (u0 + u1) / 2, (v0 + v1) / 2
        a1 = CAM.to_plane_y(uc, vc, y_front)
        a2 = CAM.to_plane_y(uc + 1, vc, y_front)
        mpp = abs(a2[0] - a1[0])                       # metres per bible px at the target, front plane
        x += ((u0 + u1) - (pu0 + pu1)) / 2 * mpp * 0.8
        z -= ((v0 + v1) - (pv0 + pv1)) / 2 * mpp * 0.8
        if ground:
            z = 0.0
    me.transform(Matrix.Translation((x, y_front, z)) @ Matrix.Scale(s, 4))
    me.update()
    if stretch_x:                                           # parametric pieces (awning): also match the width
        for _ in range(4):
            vs = [me.vertices[i].co for i in range(0, n, max(1, n // 3000))]
            pr = [CAM.project(v) for v in vs]
            pu0, pu1 = min(p[0] for p in pr), max(p[0] for p in pr)
            cx = sum(v.x for v in vs) / len(vs)
            k = (u1 - u0) / (pu1 - pu0)
            me.transform(Matrix.Translation((cx, 0, 0)) @ Matrix.Diagonal((k, 1, 1, 1)) @ Matrix.Translation((-cx, 0, 0)))
            vs = [me.vertices[i].co for i in range(0, n, max(1, n // 3000))]
            pr = [CAM.project(v) for v in vs]
            pu0, pu1 = min(p[0] for p in pr), max(p[0] for p in pr)
            a1 = CAM.to_plane_y((u0 + u1) / 2, (v0 + v1) / 2, y_front)
            a2 = CAM.to_plane_y((u0 + u1) / 2 + 1, (v0 + v1) / 2, y_front)
            me.transform(Matrix.Translation((((u0 + u1) - (pu0 + pu1)) / 2 * abs(a2[0] - a1[0]), 0, 0)))
        me.update()
    return s


def place_props(P, kit, F):
    out = {}
    C = coll("aa_e6_cabinet", kit)
    o = P["aa_prop_arcade_cabinet"]
    C.objects.link(o)
    decimate(o, TRIS["cabinet"])
    unit(o)
    out["cabinet"] = fit(o, *FIT["cabinet"], ground=True)
    C = coll("aa_e6_chalkboard", kit)
    o = P["aa_prop_chalkboard"]
    C.objects.link(o)
    decimate(o, TRIS["chalkboard"])
    o.data.transform(Matrix.Rotation(math.radians(27), 4, "Z"))    # board faces the street camera (bible)
    unit(o)
    out["chalkboard"] = fit(o, *FIT["chalkboard"], ground=True)
    C = coll("aa_e6_awning", kit)
    o = P["aa_prop_awning"]
    C.objects.link(o)
    decimate(o, TRIS["awning"])
    unit(o)
    out["awning"] = fit(o, *FIT["awning"], stretch_x=True)
    seat_on_wall(o, F)
    vs = [v.co for v in o.data.vertices]
    AWN.update(x0=min(v.x for v in vs), x1=max(v.x for v in vs), y0=min(v.y for v in vs), y1=max(v.y for v in vs),
               z0=min(v.z for v in vs), z1=max(v.z for v in vs))
    bpy.data.objects.remove(o)                            # replaced: the Tripo sheet read as a soft blur
    build_awning(C)
    o = P["aa_prop_wall_lantern"]
    decimate(o, TRIS["lantern"])
    glow_bright(o)
    unit(o)
    for side in ("l", "r"):
        lo_ = o.copy()
        lo_.data = o.data.copy()
        lo_.name = lo_.data.name = f"aa_e6_wall_lantern_{side}"
        coll(f"aa_e6_lantern_{side}", kit).objects.link(lo_)
        out["lantern_" + side] = fit(lo_, *FIT["lantern_" + side])
        if side == "r":
            vs = [v.co for v in lo_.data.vertices]
            xmax = max(v.x for v in vs)
            if xmax > 3.0:                               # keep its wall plate on the Arcade, not the cafe
                lo_.data.transform(Matrix.Translation((2.98 - xmax, 0, 0)))
        seat_on_wall(lo_, F)
        zfight_clean(lo_)
    bpy.data.objects.remove(o)
    C = coll("aa_e6_shrub", kit)
    o = P["aa_prop_planter"]
    C.objects.link(o)
    decimate(o, TRIS["planter"])
    unit(o)
    out["planter"] = fit(o, *FIT["planter"], ground=True)
    # bollards: kerb line fitted through the four consistent feet, each bollard where its u meets the line
    C = coll("aa_e6_bollards", kit)
    o = P["aa_prop_bollard"]
    o.data = bollard_mesh()                                # clean lathed cast iron replaces the lumpy scan
    o.matrix_world = Matrix.Identity(4)
    unit(o)
    feet = [to_plane_z(CAM, u, v, 0.0) for (u, v) in BOLLARD_FEET]
    pts = [feet[i] for i in (2, 3, 4, 5)]
    mx_ = sum(p[0] for p in pts) / 4
    my_ = sum(p[1] for p in pts) / 4
    sxx = sum((p[0] - mx_) ** 2 for p in pts)
    sxy = sum((p[0] - mx_) * (p[1] - my_) for p in pts)
    k = sxy / sxx
    glossy = mat("m_e6_cast_iron_gloss", lin(2, 2, 3), rough=0.3, coat=0.7)
    glossy.node_tree.nodes["Principled BSDF"].inputs["Coat Roughness"].default_value = 0.02
    glossy.node_tree.nodes["Principled BSDF"].inputs["Specular IOR Level"].default_value = 0.15
    o.data.materials.clear()
    o.data.materials.append(glossy)
    co = [v.co.copy() for i, v in enumerate(o.data.vertices) if i % 20 == 0]
    for i, (u, v) in enumerate(BOLLARD_FEET):
        best = None
        if i in (0, 1, 4):                           # off the kerb line (plaza pair, big near one): ground hit
            x, y = to_plane_z(CAM, u, v, 0.0)
            best = (0, x, y)
        for j in ([] if best else range(-3000, -300)):
            x = j * 0.01
            y = my_ + k * (x - mx_)
            pu, _ = CAM.project((x, y, 0.0))
            if best is None or abs(pu - u) < best[0]:
                best = (abs(pu - u), x, y)
        _, x, y = best
        b = o.copy()
        b.data = o.data
        b.name = f"aa_e6_bollard_{i}"
        C.objects.link(b)
        b.matrix_world = Matrix.Translation((x, y, 0.0)) @ Matrix.Scale(BOLLARD_H, 4) @ Matrix.Translation((0, -0.16, 0))
        if i in BOLLARD_FIT:                          # the two the crop shows large: fitted to their footprints
            s_, x_, z_ = fit_params(co, BOLLARD_FIT[i], y - 0.16, ground=True)
            b.data = o.data.copy()                    # own mesh, scale applied (no unapplied transforms)
            b.data.name = f"aa_e6_bollard_{i}"
            b.data.transform(Matrix.Scale(s_, 4))
            b.matrix_world = Matrix.Translation((x_, y - 0.16, 0.0))
    bpy.data.objects.remove(o)
    out["kerb"] = (mx_, my_, k)
    return out


BOLLARD_PROFILE = [  # (radius, z) for a 1 m bollard: flared plinth, tapered shaft, two collars, bulb, domed cap
    (0.0, 0.0), (0.21, 0.0), (0.21, 0.035), (0.195, 0.05), (0.19, 0.065), (0.17, 0.08), (0.15, 0.11),
    (0.135, 0.15), (0.128, 0.2), (0.12, 0.45), (0.114, 0.62),
    (0.14, 0.63), (0.148, 0.65), (0.148, 0.675), (0.135, 0.69), (0.112, 0.70), (0.105, 0.72),
    (0.13, 0.73), (0.135, 0.745), (0.135, 0.765), (0.122, 0.78), (0.1, 0.79),
    (0.112, 0.81), (0.12, 0.84), (0.118, 0.865), (0.105, 0.88),
    (0.125, 0.885), (0.128, 0.9), (0.115, 0.91),
    (0.105, 0.915), (0.09, 0.94), (0.065, 0.962), (0.035, 0.978), (0.03, 0.983), (0.036, 0.99),
    (0.02, 0.998), (0.0, 1.0)]


def bollard_mesh(seg=72):
    """Lathe BOLLARD_PROFILE around z; hard rings keep crisp edges, the round faces shade smooth."""
    bm = bmesh.new()
    rings = []
    for r, z in BOLLARD_PROFILE:
        if r == 0.0:
            rings.append([bm.verts.new((0.0, 0.0, z))])
            continue
        rings.append([bm.verts.new((r * math.cos(2 * PI * k / seg), r * math.sin(2 * PI * k / seg), z))
                      for k in range(seg)])
    for ra, rb in zip(rings, rings[1:]):
        for k in range(seg):
            k2 = (k + 1) % seg
            if len(ra) == 1:
                bm.faces.new((ra[0], rb[k], rb[k2])[::-1])
            elif len(rb) == 1:
                bm.faces.new((ra[k], ra[k2], rb[0])[::-1])
            else:
                bm.faces.new((ra[k], ra[k2], rb[k2], rb[k])[::-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("aa_e6_bollard")
    bm.to_mesh(me)
    bm.free()
    me.shade_smooth()
    me.set_sharp_from_angle(angle=math.radians(38))
    uv_box(me)
    return me


AWN = {}


def build_awning(C):
    """Clear corrugated polycarbonate arched sheet (crisp ribs) on two wrought-iron scroll brackets and a wall rail,
    sized to the fitted Tripo awning's footprint."""
    a = AWN
    x0, x1, yf, yw, zb, zt = a["x0"], a["x1"], a["y0"], a["y1"], a["z0"], a["z1"]
    depth = yw - yf
    ztop = zt
    drop = (zt - zb) * 0.42
    nu, nv, pitch, amp = 160, 28, 0.065, 0.011
    bm = bmesh.new()
    grid = []
    for j in range(nv + 1):
        t = j / nv
        ang = t * PI / 2
        yy = yw - depth * math.sin(ang)                  # quarter arch from the wall out to the front edge
        zz = ztop - drop + drop * math.cos(ang)
        ny, nz = -math.sin(ang), math.cos(ang)           # arch normal
        row = []
        for i in range(nu + 1):
            x = x0 + (x1 - x0) * i / nu
            w = amp * math.sin(2 * PI * (x - x0) / pitch)
            row.append(bm.verts.new((x, yy + ny * w, zz + nz * w)))
        grid.append(row)
    for j in range(nv):
        for i in range(nu):
            bm.faces.new((grid[j][i], grid[j][i + 1], grid[j + 1][i + 1], grid[j + 1][i]))
    sheet_m = mat("m_e6_polycarbonate_clear", (0.95, 0.97, 1.0), rough=0.04, trans=1.0)
    sheet_m.node_tree.nodes["Principled BSDF"].inputs["IOR"].default_value = 1.58
    ob = new_obj("aa_e6_awning_sheet", bm, [sheet_m], C)
    sol = ob.modifiers.new("Solidify", "SOLIDIFY")
    sol.thickness = 0.003
    iron = mat("m_e6_wrought_iron", lin(14, 14, 15), rough=0.35, coat=0.4)
    bm = bmesh.new()
    sweep(bm, [Vector((x0, yw - 0.01, ztop + 0.01)), Vector((x1, yw - 0.01, ztop + 0.01))], 0.014, 0)   # wall rail
    sweep(bm, [Vector((x0, yf, ztop - drop)), Vector((x1, yf, ztop - drop))], 0.008, 0)                  # front edge bar
    for xb in (x0 + 0.04, x1 - 0.04):
        arch = [Vector((xb, yw - depth * math.sin(t * PI / 2), ztop - drop + drop * math.cos(t * PI / 2) - 0.012))
                for t in [0.03 + 0.97 * k / 16 for k in range(17)]]       # stops short of the wall rim
        sweep(bm, arch, 0.01, 0)                                                     # rafter under the sheet
        foot = Vector((xb, yw - 0.01, zb + 0.05))
        sweep(bm, [foot, Vector((xb, yw - 0.01, ztop))], 0.012, 0)                   # wall leg
        sweep(bm, [foot, Vector((xb, yf + depth * 0.25, ztop - drop * 0.85))], 0.01, 0)   # diagonal strut
        for k, (t, rr) in enumerate(((0.35, 0.09), (0.62, 0.07))):                  # C-scrolls in the bracket
            c = Vector((xb, yw - depth * t, zb + (ztop - zb) * (0.45 + 0.2 * k)))
            pts = [c + Vector((0, -math.cos(q), math.sin(q))) * rr * (q / (3.5 * PI))
                   for q in [3.5 * PI * m / 40 for m in range(41)]]
            sweep(bm, pts, 0.006, 0, seg=6)
    new_obj("aa_e6_awning_brackets", bm, [iron], C)


def glow_bright(ob):
    """Lantern glass glows warm: emission from the texture where it is bright (the lit panes)."""
    for m in ob.data.materials:
        nt = m.node_tree
        b = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
        t = next((n for n in nt.nodes if n.type == "TEX_IMAGE" and n.image and
                  n.image.colorspace_settings.name == "sRGB"), None)
        if b is None or t is None:
            continue
        bw = nt.nodes.new("ShaderNodeRGBToBW")
        nt.links.new(t.outputs["Color"], bw.inputs["Color"])
        mr = nt.nodes.new("ShaderNodeMapRange")
        mr.inputs["From Min"].default_value = 0.35
        mr.inputs["From Max"].default_value = 0.7
        mr.inputs["To Max"].default_value = 6.0
        nt.links.new(bw.outputs["Val"], mr.inputs["Value"])
        b.inputs["Emission Color"].default_value = (1.0, 0.62, 0.28, 1)
        nt.links.new(mr.outputs["Result"], b.inputs["Emission Strength"])


def seat_on_wall(ob, F):
    """Slide a wall-mounted prop along y until its back touches the stone (raycast at the back centre)."""
    vs = [v.co for v in ob.data.vertices]
    cx = (min(v.x for v in vs) + max(v.x for v in vs)) / 2
    cz = (min(v.z for v in vs) + max(v.z for v in vs)) / 2
    ymax = max(v.y for v in vs)
    wall = None
    for t in F.trees:
        loc, _, _, d = t.ray_cast(Vector((cx, -5, cz)), Vector((0, 1, 0)), 10)
        if loc is not None and (wall is None or loc.y < wall):
            wall = loc.y
    if wall is not None:
        ob.data.transform(Matrix.Translation((0, wall - ymax - 0.002, 0)))


# =========================================================================================
# built pieces
# =========================================================================================
def wall_y_at(F, u, v, box=None):
    """Stone face y under a bible pixel; with box, the most proud face over the box (so nothing occludes it)."""
    pts = [(u, v)] if box is None else [(box[0] + (box[2] - box[0]) * i / 6, box[1] + (box[3] - box[1]) * j / 6)
                                         for i in range(7) for j in range(7)]
    ys = []
    for (pu, pv) in pts:
        hit = F.cam_hit(pu, pv)
        if hit:
            ys.append(hit[0].y)
    return min(ys) if ys else 0.0


def build_signs(kit, F):
    C = coll("aa_e6_wall_signs", kit)
    black = mat("m_e6_sign_black", lin(16, 16, 18), rough=0.7)
    frame = mat("m_e6_sign_frame_black", lin(10, 10, 11), rough=0.35, coat=0.4)
    gold = mat("m_e6_gold", (0.78, 0.6, 0.3), rough=0.3, metal=1.0)
    cream = mat("m_e6_sign_cream_gold", lin(232, 214, 160), rough=0.45, emit=lin(232, 214, 160), estr=0.12)
    white = mat("m_e6_goblet_white", lin(240, 238, 232), rough=0.35, emit=lin(240, 238, 232), estr=0.15)
    wine = mat("m_e6_goblet_gold_liquid", lin(214, 168, 70), rough=0.15, emit=lin(214, 168, 70), estr=0.35, coat=0.8)
    steel = mat("m_e6_screw_steel", (0.7, 0.7, 0.72), rough=0.3, metal=1.0)
    silver = mat("m_e6_plaque_aluminium", lin(178, 180, 178), rough=0.38, metal=1.0)
    blue = mat("m_e6_badge_blue", lin(60, 130, 210), rough=0.4)
    # ---- tall board: black board in a raised frame with corner screws
    u0, v0, u1, v1 = TALL_SIGN_PX
    yw = wall_y_at(F, 0, 0, TALL_SIGN_PX)
    yf = yw - 0.035
    x0, z1 = CAM.to_plane_y(u0, v0, yf)
    x1, z0 = CAM.to_plane_y(u1, v1, yf)
    W, H = x1 - x0, z1 - z0
    bm = bmesh.new()
    box(bm, Vector(((x0 + x1) / 2, (yf + yw) / 2, (z0 + z1) / 2)), (W, yw - yf, H), 0)
    fw = 0.028
    for (cx, cz, sx, sz) in (((x0 + x1) / 2, z1 - fw / 2, W, fw), ((x0 + x1) / 2, z0 + fw / 2, W, fw),
                             (x0 + fw / 2, (z0 + z1) / 2, fw, H - 2 * fw), (x1 - fw / 2, (z0 + z1) / 2, fw, H - 2 * fw)):
        box(bm, Vector((cx, yf - 0.006, cz)), (sx, 0.012, sz), 1)
    for xx, zz in ((x0 + fw / 2, z0 + fw / 2), (x1 - fw / 2, z0 + fw / 2), (x0 + fw / 2, z1 - fw / 2), (x1 - fw / 2, z1 - fw / 2)):
        cyl(bm, Vector((xx, yf - 0.0135, zz)), (0, 1, 0), 0.006, 0.006, 0.004, 2, seg=10)
    inset = fw + 0.012
    for li, w_ in enumerate((0.006, 0.0035)):
        a0, a1, b0, b1 = x0 + inset + li * 0.012, x1 - inset - li * 0.012, z0 + inset + li * 0.012, z1 - inset - li * 0.012
        yb = yf - 0.0015 - 0.0012 * li
        for zz in (b0, b1):
            box(bm, Vector(((a0 + a1) / 2, yb, zz)), (a1 - a0 + w_, 0.003, w_), 3)
        for xx in (a0, a1):
            box(bm, Vector((xx, yb - 0.0006, (b0 + b1) / 2)), (w_, 0.003, b1 - b0 - w_ * 1.02), 3)
    new_obj("aa_e6_sign_tokens_board", bm, [black, frame, steel, gold], C, smooth=False)
    for i, t in enumerate(["TOKENS", "DRINKS", "GAMES", "REGRETS"]):
        zt = z1 - H * (0.09 + i * 0.125)
        text_mesh(f"aa_e6_sign_tokens_text_{i}", t, FONTS / "ARIALN.TTF", cream, x0 + W * 0.14, x1 - W * 0.14,
                  zt, zt - H * 0.085, yf - 0.006, 0.003, C)
    # goblet: rounded bowl, gold liquid, white outline, stem and foot, a highlight
    cx = (x0 + x1) / 2
    zr = z0 + H * 0.36
    r = W * 0.2
    yg = yf - 0.0045
    bowl = [Vector((cx + r * math.sin(a), yg, zr - r * 0.95 * math.cos(a))) for a in
            [-PI / 2 + PI * k / 24 for k in range(25)]]
    bm = bmesh.new()
    sweep(bm, bowl, 0.004, 0)
    sweep(bm, [Vector((cx - r, yg, zr)), Vector((cx + r, yg, zr))], 0.004, 0)
    zb_ = zr - r * 0.95
    # thick stem + filled foot (bible): one gold-filled silhouette with a white edge
    zf = z0 + H * 0.115
    zs = zf + r * 0.22
    half = [(0.1, zb_ + 0.002), (0.075, (zb_ + zs) / 2 + r * 0.05), (0.08, zs + r * 0.12), (0.16, zs + r * 0.03),
            (0.4, zs - r * 0.01), (0.6, zf + r * 0.09), (0.62, zf)]
    sil = [(cx + r * hx, z_) for hx, z_ in half] + [(cx - r * hx, z_) for hx, z_ in reversed(half)]
    sweep(bm, [Vector((x_, yg, z_)) for x_, z_ in sil] + [Vector((sil[0][0], yg, sil[0][1]))], 0.004, 0)
    sweep(bm, [Vector((cx + r * 0.55, yg - 0.001, zr - r * 0.2)), Vector((cx + r * 0.75, yg - 0.001, zr - r * 0.5))],
          0.0025, 0)                                                               # highlight stroke
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=2e-5)          # the closed silhouette's seam
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=2e-5)
    new_obj("aa_e6_sign_tokens_goblet", bm, [white], C)
    bm = bmesh.new()
    bm.faces.new([bm.verts.new((x_, yf - 0.0032, z_)) for x_, z_ in sil])    # 1.2 mm off the liquid layer
    new_obj("aa_e6_sign_tokens_goblet_stem", bm, [wine], C)
    bm = bmesh.new()
    liq = [Vector((cx + r * 0.9 * math.sin(a), yf - 0.002, zr - 0.02 - r * 0.86 * math.cos(a)))
           for a in [-PI / 2 + PI * k / 24 for k in range(25)]]
    vs_ = [bm.verts.new(p) for p in liq]
    bm.faces.new(vs_)
    new_obj("aa_e6_sign_tokens_goblet_liquid", bm, [wine], C)
    # ---- small plaque: aluminium plate with screws, coin badge + blue icon, black bands with light stencil text
    u0, v0, u1, v1 = SMALL_SIGN_PX
    yw = wall_y_at(F, 0, 0, SMALL_SIGN_PX)
    yf = yw - 0.02
    x0, z1 = CAM.to_plane_y(u0, v0, yf)
    x1, z0 = CAM.to_plane_y(u1, v1, yf)
    W, H = x1 - x0, z1 - z0
    bm = bmesh.new()
    box(bm, Vector(((x0 + x1) / 2, (yf + yw) / 2, (z0 + z1) / 2)), (W, yw - yf, H), 0)
    for xx, zz in ((x0 + 0.02, z0 + 0.02), (x1 - 0.02, z0 + 0.02), (x0 + 0.02, z1 - 0.02), (x1 - 0.02, z1 - 0.02)):
        cyl(bm, Vector((xx, yf - 0.002, zz)), (0, 1, 0), 0.007, 0.007, 0.004, 3, seg=10)
    bands = ((z1 - H * 0.42, z1 - H * 0.66), (z1 - H * 0.7, z1 - H * 0.94))
    for (bt, bb) in bands:
        box(bm, Vector(((x0 + x1) / 2, yf - 0.002, (bt + bb) / 2)), (W * 0.86, 0.004, bt - bb), 1)
    cyl(bm, Vector((x0 + W * 0.42, yf - 0.004, z1 - H * 0.2)), (0, 1, 0), W * 0.085, W * 0.085, 0.008, 2, seg=24)
    box(bm, Vector((x0 + W * 0.78, yf - 0.003, z1 - H * 0.2)), (W * 0.11, 0.006, W * 0.11), 4)
    new_obj("aa_e6_sign_regrets_plaque", bm, [silver, black, gold, steel, blue], C, smooth=False)
    stencil = mat("m_e6_plaque_stencil_light", lin(214, 210, 196), rough=0.6)
    for k, (t, (bt, bb)) in enumerate(zip(("TOKENS", "REGRETS"), bands)):
        h_ = bt - bb
        text_mesh(f"aa_e6_sign_regrets_text_{k}", t, FONTS / "ARIALNB.TTF", stencil, x0 + W * 0.13, x1 - W * 0.13,
                  bt - h_ * 0.16, bb + h_ * 0.16, yf - 0.0052, 0.0015, C)


CRT_PX = (1727, 3527, 1993, 3783)
SIDE_PANEL_PX = (2080, 3340, 2160, 3420)


def build_cabinet_screen(kit):
    """Pink/purple horizontal bands behind a green crab invader on the CRT (bible), and the glowing green panel near
    the top of the cabinet's right side. Emissive decals on the Tripo cabinet's faces (raycast)."""
    import numpy as np
    C = coll("aa_e6_cabinet", kit)
    cab = bpy.data.objects["aa_prop_arcade_cabinet"]
    dg = bpy.context.evaluated_depsgraph_get()
    bmc = bmesh.new()
    bmc.from_object(cab, dg)
    tree = BVHTree.FromBMesh(bmc)
    bmc.free()

    def hit(u, v):
        loc, nrm, _, _ = tree.ray_cast(Vector(CAM.loc), Vector(CAM.ray(u, v)).normalized(), 60)
        return loc, nrm
    # screen texture
    w, h = 256, 200
    a = np.zeros((h, w, 4), np.float32)
    a[..., :3] = (0.03, 0.02, 0.08)
    a[..., 3] = 1
    for k, col in enumerate([(0.95, 0.35, 0.75), (0.6, 0.25, 0.9), (0.9, 0.3, 0.6), (0.55, 0.2, 0.85)]):
        y0 = 110 + k * 22
        a[y0:y0 + 12, :, :3] = col
    crab = ["..#.....#..", "...#...#...", "..#######..", ".##.###.##.", "###########", "#.#######.#", "#.#.....#.#",
            "...##.##..."]
    cs = 9
    ox, oy = (w - 11 * cs) // 2, 22
    for r_, row in enumerate(crab):
        for c_, ch in enumerate(row):
            if ch == "#":
                a[oy + r_ * cs:oy + (r_ + 1) * cs, ox + c_ * cs:ox + (c_ + 1) * cs, :3] = (0.4, 0.95, 0.3)
    img = bpy.data.images.new("e6_crt_screen", w, h)
    img.pixels.foreach_set(a[::-1].ravel())
    img.filepath_raw = str(ASSET / "textures/e6_street/e6_crt_screen.png")
    (ASSET / "textures/e6_street").mkdir(parents=True, exist_ok=True)
    img.file_format = "PNG"
    img.save()
    m = bpy.data.materials.new("m_e6_crt_screen")
    nt = m.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    t = nt.nodes.new("ShaderNodeTexImage")
    t.image = img
    t.interpolation = "Closest"
    nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
    nt.links.new(t.outputs["Color"], b.inputs["Emission Color"])
    b.inputs["Emission Strength"].default_value = 1.6
    b.inputs["Roughness"].default_value = 0.08
    u0, v0, u1, v1 = CRT_PX
    corners = [hit(u0, v1), hit(u1, v1), hit(u1, v0), hit(u0, v0)]
    if all(c[0] is not None for c in corners):
        bm = bmesh.new()
        uvl = bm.loops.layers.uv.new("uv_material")
        vs = [bm.verts.new(c[0] - c[1] * -0.002 + c[1] * 0.003) for c in corners]
        f = bm.faces.new(vs)
        for l_, uv in zip(f.loops, ((0, 0), (1, 0), (1, 1), (0, 1))):
            l_[uvl].uv = uv
        me = bpy.data.meshes.new("aa_e6_cabinet_crt")
        bm.to_mesh(me)
        bm.free()
        me.uv_layers.new(name="uv_bake")
        me.materials.append(m)
        crt = bpy.data.objects.new("aa_e6_cabinet_crt", me)
        C.objects.link(crt)
        hide_behind(cab, crt)
    # side panel on the cabinet's right (+x) face near the top (bible)
    gm = mat("m_e6_cabinet_side_green", lin(120, 230, 70), rough=0.3, emit=lin(120, 230, 70), estr=1.1)
    vs = [cab.matrix_world @ v.co for v in cab.data.vertices]
    xmax = max(v.x for v in vs)
    ymin, ymax = min(v.y for v in vs), max(v.y for v in vs)
    zmax = max(v.z for v in vs)
    d_ = ymax - ymin
    bm = bmesh.new()
    ya, yb, za, zb_ = ymin + d_ * 0.5, ymin + d_ * 0.85, zmax - 0.42, zmax - 0.16   # back half of the side, top
    q = [Vector((xmax + 0.004, ya, za)), Vector((xmax + 0.004, ya, zb_)),
         Vector((xmax + 0.004, yb, zb_)), Vector((xmax + 0.004, yb, za))]
    cbvh = BVHTree.FromPolygons(vs, [p_.vertices for p_ in cab.data.polygons])
    for p_ in q:                                           # seat each corner on the side face (1.5 mm proud)
        h_ = cbvh.ray_cast(Vector((xmax + 0.2, p_.y, p_.z)), Vector((-1, 0, 0)))
        if h_[0] is not None:
            p_.x = h_[0].x + 0.0015
        else:
            print("E6 SIDE_PANEL corner missed the cabinet", tuple(p_))
    bm.faces.new([bm.verts.new(p_) for p_ in q])
    new_obj("aa_e6_cabinet_side_panel", bm, [gm], C)


def hide_behind(base, decal, eps=0.0012):
    """Delete base faces lying flush behind an opaque decal (never visible; qa would read them as z-fighting)."""
    from mathutils import geometry as _g
    mw = decal.matrix_world
    dtris = []
    for p_ in decal.data.polygons:
        co = [mw @ decal.data.vertices[i].co for i in p_.vertices]
        dtris += [(co[0], co[k], co[k + 1]) for k in range(1, len(co) - 1)]
    dv = [v for t in dtris for v in t]
    tree = BVHTree.FromPolygons(dv, [[3 * i, 3 * i + 1, 3 * i + 2] for i in range(len(dtris))])
    bm = bmesh.new()
    bm.from_mesh(base.data)
    bm.transform(base.matrix_world)
    kill = []
    for f in bm.faces:
        c = f.calc_center_median()
        pts = [c] + [c.lerp(v.co, 0.6) for v in f.verts]
        if any(abs(f.normal.dot(n)) > 0.998 for p in pts for (_, n, _, _) in tree.find_nearest_range(p, eps)):
            kill.append(f)
    if kill:
        bmesh.ops.delete(bm, geom=kill, context="FACES")
        bm.transform(base.matrix_world.inverted())
        bm.to_mesh(base.data)
    bm.free()
    print("E6 HIDE_BEHIND", base.name, len(kill))


def build_bucket(kit):
    C = coll("aa_e6_bucket", kit)
    galv = mat("m_e6_galvanised_pail", lin(188, 190, 188), rough=0.4, metal=0.6)     # light grey galvanised
    u0, v0, u1, v1 = BUCKET_PX
    # stands on the street where its bible foot is (in front of the cabinet's side, beside the A-frame)
    _, y = to_plane_z(CAM, (u0 + u1) / 2, v1, 0.0)
    y = min(y, -0.74)            # the bible's foot ray lands behind the cabinet side; bring it out in front
    x0, zt = CAM.to_plane_y(u0, v0, y)
    x1, zb = CAM.to_plane_y(u1, v1, y)
    _cv = [bpy.data.objects["aa_prop_arcade_cabinet"].matrix_world @ v.co for v in list(bpy.data.objects["aa_prop_arcade_cabinet"].data.vertices)[::40]]
    print("E6 BUCKET front y", round(y, 3), "x", round(x0, 3), round(x1, 3), "h", round(zt - max(zb, 0.0), 3),
          "cabinet x", round(min(v.x for v in _cv), 3), round(max(v.x for v in _cv), 3), "y", round(min(v.y for v in _cv), 3), round(max(v.y for v in _cv), 3))
    h = max(zt - zb, 0.36)       # knee-high pail; stands on the street (z = 0)
    r = (x1 - x0) / 2
    cx = (x0 + x1) / 2 - 0.07     # clear of the A-frame's near leg (bible: in front of it, beside the cabinet)
    bm = bmesh.new()
    cyl(bm, Vector((cx, y + r, h / 2)), (0, 0, 1), r * 0.85, r, h, 0, seg=32)               # pail (closed)
    for zz in (h * 0.3, h * 0.65, h * 0.985):                                              # rolled bands
        rr = r * (0.85 + 0.15 * zz / h) + 0.002
        ring = [Vector((cx + rr * math.cos(a), y + r + rr * math.sin(a), zz)) for a in
                [2 * PI * k / 32 for k in range(33)]]
        sweep(bm, ring, 0.004, 0, seg=6)
    sweep(bm, [Vector((cx - r - 0.004, y + r, h * 0.9)), Vector((cx - r * 0.7, y + r, h * 1.35)),
               Vector((cx + r * 0.7, y + r, h * 1.35)), Vector((cx + r + 0.004, y + r, h * 0.9))], 0.003, 0)
    new_obj("aa_e6_bucket", bm, [galv], C)


def build_awning_lights(kit, F):
    """Tangled black cables and small warm string lights under the awning (bible)."""
    C = coll("aa_e6_awning", kit)
    aw = bpy.data.objects["aa_e6_awning_sheet"]
    vs = [v.co for v in aw.data.vertices]
    x0, x1 = min(v.x for v in vs), max(v.x for v in vs)
    y0, y1 = min(v.y for v in vs), max(v.y for v in vs)
    zb = min(v.z for v in vs)
    cable = mat("m_e6_cable_black", lin(12, 12, 13), rough=0.45)
    bulb = mat("m_e6_string_bulb", (1.0, 0.75, 0.4), emit=(1.0, 0.68, 0.32), estr=18)
    from mathutils.kdtree import KDTree
    kd = KDTree(len(aw.data.vertices))
    for i, v in enumerate(aw.data.vertices):
        kd.insert(v.co, i)
    kd.balance()
    snap = lambda p: kd.find(p)[0] + Vector((0, 0, 0.006))  # cable ends pass through the awning sheet (tied on)
    bm = bmesh.new()
    bb = bmesh.new()
    n = 9
    for strand, (yy, sag) in enumerate(((y0 + 0.08, 0.12), (y0 + 0.25, 0.18), (y0 + 0.45, 0.1))):
        pts = []
        for k in range(n + 1):
            t = k / n
            x = x0 + 0.06 + (x1 - x0 - 0.12) * t
            z = zb + 0.02 - sag * math.sin(PI * t) * (0.7 + 0.3 * math.sin(7 * t + strand))
            pts.append(Vector((x, yy + 0.04 * math.sin(5 * t + strand * 2), z)))
            if 0 < k < n and (k + strand) % 2 == 0:
                bmesh.ops.create_uvsphere(bb, u_segments=10, v_segments=6, radius=0.018,
                                          matrix=Matrix.Translation(pts[-1] - Vector((0, 0, 0.03))))
                sweep(bm, [pts[-1], pts[-1] - Vector((0, 0, 0.02))], 0.004, 0, seg=6)
        pts[0], pts[-1] = snap(pts[0]), snap(pts[-1])
        sweep(bm, pts, 0.005, 0, seg=8)
    # loose drops down to the cabinet and along the wall (tangled look)
    for k in range(4):
        x = x0 + (x1 - x0) * (0.15 + 0.22 * k)
        sweep(bm, [snap(Vector((x, y1 - 0.05, zb))), Vector((x + 0.05, y1 - 0.12, zb - 0.25 - 0.1 * k)),
                   Vector((x - 0.03, y1 - 0.08, zb - 0.45 - 0.08 * k))], 0.005, 0, seg=8)
    new_obj("aa_e6_awning_cables", bm, [cable], C)
    new_obj("aa_e6_awning_string_bulbs", bb, [bulb], C)


def build_clocktower_sign(kit):
    """CLOCKTOWER / PLAZA bracket sign (Q-006) on the Arcade's left corner, interfaces corner mounting zone."""
    C = coll("aa_e6_clocktower_sign", kit)
    cb = IFACE["corner_bay"]
    zone = cb["clocktower_plaza_sign_mount_zone"]
    ax = zone["at_arris_x"]
    z0, z1 = zone["at_arris_z"]
    iron = mat("m_e6_wrought_iron", lin(14, 14, 15), rough=0.35, coat=0.4)
    gold = mat("m_e6_gold", (0.78, 0.6, 0.3), rough=0.3, metal=1.0)
    board = mat("m_e6_shield_black", lin(18, 20, 24), rough=0.55)
    glass = mat("m_e6_lantern_glass", (1.0, 0.8, 0.5), rough=0.1, emit=(1.0, 0.65, 0.3), estr=8)
    # arm out from the arris along the bisector of the facade and the cant (both readable from the street)
    d = Vector((-0.38, -0.92, 0)).normalized()
    base = Vector((ax, 0.0, z1 - 0.02))
    L = 1.05
    bm = bmesh.new()
    box(bm, base + Vector((0, 0, -0.35)), (0.05, 0.05, 0.8), 0)                       # wall plate
    sweep(bm, [base, base + d * L], 0.018, 0)                                         # top arm
    sweep(bm, [base + Vector((0, 0, -0.6)), base + d * (L * 0.65)], 0.012, 0)          # diagonal strut
    for k, (t, rr) in enumerate(((0.3, 0.1), (0.55, 0.08), (0.8, 0.06))):            # scrolls
        c = base + d * (L * t) + Vector((0, 0, -0.13))
        pts = [c + (d * math.cos(a) + Vector((0, 0, 1)) * math.sin(a)) * rr * (a / (4 * PI))
               for a in [4 * PI * j / 40 for j in range(41)]]
        sweep(bm, pts, 0.006, 0, seg=6)
        sweep(bm, [pts[-1], pts[-1] + Vector((0, 0, 0.13))], 0.006, 0, seg=6)       # collar tie up to the arm
    for t in (0.25, 0.9):                                                             # hanging rings
        c = base + d * (L * t)
        sweep(bm, [c, c + Vector((0, 0, -0.1))], 0.006, 0, seg=6)
    new_obj("aa_e6_clocktower_bracket", bm, [iron], C)
    # scalloped shield in the plane of the arm
    side = d.cross(Vector((0, 0, 1))).normalized()
    sc = base + d * (L * 0.575) + Vector((0, 0, -0.1 - 0.42))
    w, h = 0.3, 0.3
    outline = []
    for k in range(9):                                                                # scalloped top
        t = k / 8
        outline.append((-w + 2 * w * t, h + 0.03 * math.cos(t * 8 * PI)))
    for k in range(1, 13):                                                            # curved shield base
        a = PI * k / 12
        outline.append((w * math.cos(a), -h * 0.15 - h * 0.85 * math.sin(a) ** 0.8))
    def to3(p, off):
        return sc + d * p[0] + Vector((0, 0, p[1])) + side * off
    bm = bmesh.new()
    for off in (-0.012, 0.012):
        pass
    f_ = [bm.verts.new(to3(p, -0.012)) for p in outline]
    b_ = [bm.verts.new(to3(p, 0.012)) for p in outline]
    bm.faces.new(f_)
    bm.faces.new(b_[::-1])
    n = len(outline)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((f_[i], f_[j], b_[j], b_[i]))
    new_obj("aa_e6_clocktower_shield", bm, [board], C, smooth=False)
    # gold border (both faces), text, compass rose
    for sgn in (-1, 1):
        bm = bmesh.new()
        pts = [to3((p[0] * 0.92, p[1] * 0.92 + 0.0), sgn * 0.015) for p in outline] + \
              [to3((outline[0][0] * 0.92, outline[0][1] * 0.92), sgn * 0.015)]
        sweep(bm, pts, 0.006, 0, seg=6)
        rc = to3((0, -h * 0.35), sgn * 0.016)
        for a in range(8):                                                            # compass rose
            ang = a * PI / 4
            rr = 0.1 if a % 2 == 0 else 0.055
            tip = rc + (d * math.cos(ang) + Vector((0, 0, 1)) * math.sin(ang)) * rr
            sweep(bm, [rc, tip], 0.006 if a % 2 == 0 else 0.004, 0, seg=6)
        circ = [rc + (d * math.cos(t) + Vector((0, 0, 1)) * math.sin(t)) * 0.065 for t in
                [2 * PI * j / 32 for j in range(33)]]
        sweep(bm, circ, 0.003, 0, seg=6)
        new_obj(f"aa_e6_clocktower_gold_{'a' if sgn < 0 else 'b'}", bm, [gold], C)
        for i, t in enumerate(("CLOCKTOWER", "PLAZA")):
            zt = h * (0.72 - i * 0.27)
            ob = text_mesh(f"aa_e6_clocktower_text_{'a' if sgn < 0 else 'b'}_{i}", t, FONTS / "cambriab.ttf", gold,
                           -w * 0.78, w * 0.78, zt, zt - h * 0.17, 0.0, 0.003, C)
            # text_mesh builds in the XZ plane facing -Y: rotate it into the shield plane, facing out
            R = Matrix.Translation(sc) @ Matrix((d, -side * sgn * -1, Vector((0, 0, 1)))).transposed().to_4x4()
            M_ = Matrix.Translation(side * sgn * 0.0165) @ Matrix.Translation(sc) @ \
                Matrix((d * (1 if sgn < 0 else -1), side * (-1 if sgn < 0 else 1), Vector((0, 0, 1)))).transposed().to_4x4()
            ob.data.transform(M_)
    # hanging lantern below
    lc = sc + Vector((0, 0, -h - 0.16))
    bm = bmesh.new()
    sweep(bm, [sc + Vector((0, 0, -h - 0.02)), lc + Vector((0, 0, 0.13))], 0.005, 0, seg=6)
    cyl(bm, lc + Vector((0, 0, 0.1)), (0, 0, 1), 0.07, 0.015, 0.06, 0, seg=6)
    cyl(bm, lc + Vector((0, 0, -0.08)), (0, 0, 1), 0.04, 0.065, 0.035, 0, seg=6)
    new_obj("aa_e6_clocktower_lantern", bm, [iron], C)
    bm = bmesh.new()
    cyl(bm, lc, (0, 0, 1), 0.058, 0.058, 0.13, 0, seg=6)
    new_obj("aa_e6_clocktower_lantern_glass_glow", bm, [glass], C)


def build_stone_post(kit):
    C = coll("aa_e6_stone_post", kit)
    stone = mat("m_e6_stone_post", lin(170, 160, 145), rough=0.85)
    u0, v0, u1, v1 = STONE_POST_PX
    y = -0.35
    x0, zt = CAM.to_plane_y(u0, v0, y)
    x1, zb = CAM.to_plane_y(u1, v1, y)
    x0, x1 = min(x0, 2.95), min(x1, 3.04)
    bm = bmesh.new()
    box(bm, Vector(((x0 + x1) / 2, y + 0.15, (zt) / 2)), (x1 - x0, 0.3, zt), 0)
    ob = new_obj("aa_e6_stone_post", bm, [stone], C, smooth=False)
    bv = ob.modifiers.new("Bevel", "BEVEL")
    bv.width, bv.segments = 0.015, 2


def build_ground(kit, kerb):
    """Wet rounded cobbles (facade to kerb, and on past the kerb to the bollards), dark wet grout bed, streaky
    puddles, leaf litter piled at the cabinet foot and along the wall, a thin dark wet stone kerb edge and the
    pale stone step at the wall foot."""
    import random
    from mathutils import geometry as _g
    rnd = random.Random(11)
    C = coll("aa_e6_ground", kit)
    mx_, my_, k = kerb
    X0, X1 = -7.2, 3.04
    KW = 0.04                                                     # kerb half-width (thin edge, bible)
    ROAD = 2.0                                                    # cobbles continue this far past the kerb
    YMIN = -10.4

    def kerb_y(x):
        return max(my_ + k * (x - mx_), -8.0)

    def inside(x, y, gap=0.0):
        if not (X0 <= x <= X1) or y < YMIN:
            return False
        yk = kerb_y(x)
        if abs(y - yk) < KW + gap:                                # the kerb itself
            return False
        if y < yk:                                                # street side of the kerb
            return y > yk - ROAD
        if x > -5.4:
            if y > -0.02:
                return False
            if -2.3 <= x <= 2.8 and y > -0.37:                   # E3's threshold step
                return False
            if -5.4 <= x <= -3.92 and y > -0.3:                    # wall-foot step
                return False
        elif y > (-5.4 - x) - 0.02:                                # corner-bay cant
            return False
        return True
    xs = [X0 + 0.25 * i_ for i_ in range(int((X1 - X0) / 0.25) + 1)]
    bm = bmesh.new()
    top = [bm.verts.new((x, 0.0 if x > -5.4 else min(1.41, -5.4 - x), 0.0)) for x in xs]
    kin = [bm.verts.new((x, kerb_y(x) + KW, 0.0)) for x in xs]
    kout = [bm.verts.new((x, kerb_y(x) - KW, 0.0)) for x in xs]
    far = [bm.verts.new((x, max(kerb_y(x) - ROAD, YMIN), 0.0)) for x in xs]
    for i_ in range(len(xs) - 1):
        bm.faces.new((kin[i_], kin[i_ + 1], top[i_ + 1], top[i_]))
        bm.faces.new((far[i_], far[i_ + 1], kout[i_ + 1], kout[i_]))
    bed = mat("m_e6_cobble_bed_wet", lin(22, 21, 20), rough=0.15, coat=0.5)
    new_obj("aa_e6_ground_bed", bm, [bed], C, smooth=False)
    # cobbles: varied size / height / rotation / tilt, tops slightly flattened, a per-stone tone value
    bm = bmesh.new()
    tone = bm.faces.layers.float.new("cobble_tone")
    n = 0
    dy, dx = 0.118, 0.132          # bible setts read ~11-13 cm
    y = -0.02
    row = 0
    PUD = 0.016
    while y > YMIN:
        x = X0 + (dx / 2 if row % 2 else 0) + rnd.uniform(-0.02, 0.02)
        while x < X1:
            px, py = x + rnd.uniform(-0.015, 0.015), y + rnd.uniform(-0.012, 0.012)
            if inside(px, py, gap=0.045):
                sx, sy = rnd.uniform(0.046, 0.074), rnd.uniform(0.04, 0.064)
                sz = rnd.uniform(0.014, 0.026)
                cz = sz * rnd.uniform(0.3, 0.62)
                if abs(cz + sz * 0.71 - PUD) < 0.002:              # top never flush with the puddle sheet
                    cz += 0.004
                M_ = (Matrix.Translation((px, py, cz)) @ Matrix.Rotation(rnd.uniform(0, PI), 4, "Z")
                      @ Matrix.Rotation(rnd.uniform(-0.16, 0.16), 4, "X")
                      @ Matrix.Rotation(rnd.uniform(-0.16, 0.16), 4, "Y") @ Matrix.Diagonal((sx, sy, sz, 1)))
                r_ = bmesh.ops.create_icosphere(bm, subdivisions=2, radius=1.0)
                for v in r_["verts"]:
                    co = v.co.copy()
                    co.x = math.copysign(abs(co.x) ** 0.55, co.x)  # squarer plan: a dressed sett, not a pebble
                    co.y = math.copysign(abs(co.y) ** 0.55, co.y)
                    if co.z > 0.35:
                        co.z = 0.35 + (co.z - 0.35) * 0.25         # worn, flattened top
                    v.co = M_ @ co
                tv = rnd.random()
                for f in {f for v in r_["verts"] for f in v.link_faces}:
                    f[tone] = tv
                n += 1
            x += dx * rnd.uniform(0.9, 1.1)
        y -= dy
        row += 1
    cob = cobble_material()
    ob = new_obj("aa_e6_ground_cobbles", bm, [cob], C)
    outward_islands(ob.data)
    # puddle sheet between the stones
    bm = bmesh.new()
    nx, ny_ = 82, 92
    gv = {}
    for a_ in range(nx + 1):
        for b_ in range(ny_ + 1):
            gv[(a_, b_)] = bm.verts.new((X0 + (X1 - X0) * a_ / nx, YMIN * b_ / ny_, PUD))
    for a_ in range(nx):
        for b_ in range(ny_):
            qd = [gv[(a_, b_)], gv[(a_ + 1, b_)], gv[(a_ + 1, b_ + 1)], gv[(a_, b_ + 1)]]
            cx = sum(v.co.x for v in qd) / 4
            cy = sum(v.co.y for v in qd) / 4
            if inside(cx, cy, gap=0.06):
                bm.faces.new(qd)
    loose = [v for v in bm.verts if not v.link_faces]
    bmesh.ops.delete(bm, geom=loose, context="VERTS")
    new_obj("aa_e6_ground_puddles", bm, [puddle_material()], C, smooth=False)
    surf = [o_.data for o_ in (ob, bpy.data.objects["aa_e6_ground_bed"], bpy.data.objects["aa_e6_ground_puddles"])]
    sv, sf = [], []
    for me_ in surf:                                       # leaves rest ON the cobbles: raycast target
        base = len(sv)
        sv += [v.co.copy() for v in me_.vertices]
        sf += [[base + i_ for i_ in p_.vertices] for p_ in me_.polygons]
    ground_bvh = BVHTree.FromPolygons(sv, sf)
    # leaf litter: piled at the cabinet foot and along the wall (bible), lighter elsewhere
    cab = bpy.data.objects.get("aa_prop_arcade_cabinet")
    if cab:
        cv = [cab.matrix_world @ v.co for v in list(cab.data.vertices)[::50]]
        cx0, cx1 = min(v.x for v in cv), max(v.x for v in cv)
        cy0, cy1 = min(v.y for v in cv), max(v.y for v in cv)
    else:
        cx0, cx1, cy0, cy1 = -3.8, -2.8, -0.8, -0.05

    def leaf_spot():
        r = rnd.random()
        if r < 0.6:                                        # cabinet foot: front and right side
            if rnd.random() < 0.7:
                return rnd.uniform(cx0 - 0.25, cx1 + 0.35), cy0 - 0.03 - (rnd.random() ** 1.6) * 0.5
            return cx1 + 0.03 + (rnd.random() ** 1.6) * 0.35, rnd.uniform(cy0 - 0.2, cy1 - 0.05)
        if r < 0.95:                                       # along the wall foot
            x = rnd.uniform(-5.4, X1)
            return x, (-0.39 if -2.3 <= x <= 2.8 else -0.32) - (rnd.random() ** 2) * 0.45
        x = rnd.uniform(X0, X1)
        yk = kerb_y(x)
        tt = rnd.random() ** 2
        return x, ((-0.35 - tt * 1.4) if rnd.random() < 0.5 else (yk + 0.12 + tt * 1.2))
    taken = {}
    bm = bmesh.new()
    nl = 0
    for _ in range(60000):
        x, yy = leaf_spot()
        if not inside(x, yy, gap=0.03) or (cx0 - 0.01 < x < cx1 + 0.01 and cy0 - 0.01 < yy < cy1 + 0.01):
            continue
        s_ = rnd.uniform(0.014, 0.028)
        cell = (round(x / 0.03), round(yy / 0.03))
        lay = sum(taken.get((cell[0] + a_, cell[1] + b_), 0) for a_ in (-1, 0, 1) for b_ in (-1, 0, 1))
        if lay >= 4:
            continue                                       # overlapping neighbours stack 1.3 mm apart, max 4
        M_ = Matrix.Translation((x, yy, 0.0)) @ Matrix.Rotation(rnd.uniform(0, 2 * PI), 4, "Z")
        pts_ = []
        for p_ in ((-s_, -s_ * 0.6, 0), (s_, -s_ * 0.5, 0), (s_ * 0.8, s_ * 0.6, 0), (-s_ * 0.9, s_ * 0.5, 0)):
            q_ = M_ @ Vector(p_)
            hit = ground_bvh.ray_cast(Vector((q_.x, q_.y, 0.2)), Vector((0, 0, -1)))
            if hit[0] is None:
                break
            q_.z = hit[0].z + 0.0015 + 0.0013 * lay        # stacked leaves clear each other (> z-fight eps)
            pts_.append(q_)
        if len(pts_) < 4:
            continue                                       # off the paving: no leaf
        nl_ = _g.normal(pts_[0], pts_[1], pts_[2])
        cen_ = sum(pts_, Vector()) / 4
        if any(abs(nl_.dot(hn)) > 0.998 for pp in [cen_] + [cen_.lerp(q, 0.6) for q in pts_]
               for (_, hn, _, _) in ground_bvh.find_nearest_range(pp, 0.0012)):
            continue                                       # would lie flush on a cobble facet (z-fight)
        taken[cell] = taken.get(cell, 0) + 1
        vs = [bm.verts.new(q_) for q_ in pts_]
        f = bm.faces.new(vs)
        f.material_index = nl % 2
        nl += 1
        if nl >= 5000:
            break
    new_obj("aa_e6_ground_leaves", bm, [mat("m_e6_leaf_orange", lin(210, 110, 30), rough=0.5),
                                        mat("m_e6_leaf_gold", lin(220, 160, 40), rough=0.5)], C, smooth=False)
    # thin dark wet stone kerb edge + the pale stone step at the wall foot
    kerb_m = mat("m_e6_kerb_wet_stone", lin(38, 37, 37), rough=0.3, coat=0.35)
    pale = mat("m_e6_kerb_pale_stone", lin(196, 186, 170), rough=0.55)
    kb = bmesh.new()
    rows_ = []
    for x in xs:
        yk = kerb_y(x)
        rows_.append([kb.verts.new((x, yk + dy_, z_)) for dy_, z_ in ((-KW, -0.03), (-KW, 0.018), (KW, 0.018),
                                                                       (KW, -0.03))])
    for a_ in range(len(rows_) - 1):
        for k_ in range(4):
            kb.faces.new((rows_[a_][k_], rows_[a_][(k_ + 1) % 4], rows_[a_ + 1][(k_ + 1) % 4], rows_[a_ + 1][k_]))
    kb.faces.new(rows_[0][::-1])
    kb.faces.new(rows_[-1])
    box(kb, Vector(((-5.4 - 3.92) / 2, -0.15, 0.04)), (5.4 - 3.92, 0.3, 0.08), 1)
    new_obj("aa_e6_ground_kerb", kb, [kerb_m, pale], C, smooth=False)
    print("E6 GROUND cobbles", n, "leaves", nl)
    return ob


def outward_islands(me):
    """Flip any closed island whose signed volume is negative (a stone whose normals point inward)."""
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    seen = set()
    for f in bm.faces:
        if f.index in seen:
            continue
        isl, st = [], [f]
        seen.add(f.index)
        while st:
            g = st.pop()
            isl.append(g)
            for e in g.edges:
                for h in e.link_faces:
                    if h.index not in seen:
                        seen.add(h.index)
                        st.append(h)
        vol = 0.0
        for g in isl:
            vs = [v.co for v in g.verts]
            for i in range(1, len(vs) - 1):
                vol += vs[0].dot(vs[i].cross(vs[i + 1]))
        if vol < 0:
            bmesh.ops.reverse_faces(bm, faces=isl)
    bm.to_mesh(me)
    bm.free()


def puddle_material():
    """Wet puddle film between the cobbles: near-black mirror water in noise-shaped pools, with a ripple bump
    stretched along the view (y) so lantern / neon reflections smear into vertical streaks, as in the bible."""
    m = bpy.data.materials.new("m_e6_puddle_water")
    m.surface_render_method = "DITHERED"
    nt = m.node_tree
    L = nt.links.new
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (0.012, 0.012, 0.014, 1)
    b.inputs["Roughness"].default_value = 0.02
    b.inputs["Specular IOR Level"].default_value = 0.8
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    nz = nt.nodes.new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = 0.55
    nz.inputs["Detail"].default_value = 5
    L(geo.outputs["Position"], nz.inputs["Vector"])
    mr = nt.nodes.new("ShaderNodeMapRange")
    mr.inputs["From Min"].default_value = 0.44                 # wider pools than before
    mr.inputs["From Max"].default_value = 0.47
    L(nz.outputs["Fac"], mr.inputs["Value"])
    L(mr.outputs["Result"], b.inputs["Alpha"])
    # streaks: noise squashed along y (toward the camera) -> long thin ripples -> stretched reflections
    sq = nt.nodes.new("ShaderNodeVectorMath")
    sq.operation = "MULTIPLY"
    sq.inputs[1].default_value = (55.0, 1.6, 1.0)
    L(geo.outputs["Position"], sq.inputs[0])
    rn = nt.nodes.new("ShaderNodeTexNoise")
    rn.inputs["Scale"].default_value = 1.0
    rn.inputs["Detail"].default_value = 3
    L(sq.outputs["Vector"], rn.inputs["Vector"])
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.6
    bump.inputs["Distance"].default_value = 0.002
    L(rn.outputs["Fac"], bump.inputs["Height"])
    L(bump.outputs["Normal"], b.inputs["Normal"])
    return m


def cobble_material():
    """Wet rounded cobble: per-stone tone (cobble_tone attribute) ramped across dark basalt, mid grey and warm
    grey, slight in-stone mottling, strong wet clear coat."""
    m = bpy.data.materials.new("m_e6_wet_cobbles")
    nt = m.node_tree
    L = nt.links.new
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    at = nt.nodes.new("ShaderNodeAttribute")
    at.attribute_type = "GEOMETRY"
    at.attribute_name = "cobble_tone"
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    els = ramp.color_ramp.elements
    els[0].position, els[0].color = 0.0, (*lin(34, 31, 29), 1)          # dark wet basalt
    els[1].position, els[1].color = 1.0, (*lin(150, 128, 104), 1)      # warm grey-brown
    e = els.new(0.35)
    e.color = (*lin(70, 64, 60), 1)
    e = els.new(0.7)
    e.color = (*lin(112, 100, 88), 1)
    L(at.outputs["Fac"], ramp.inputs["Fac"])
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    mot = nt.nodes.new("ShaderNodeTexNoise")
    mot.inputs["Scale"].default_value = 60.0
    L(geo.outputs["Position"], mot.inputs["Vector"])
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.blend_type = "MULTIPLY"
    mix.inputs["Factor"].default_value = 0.35
    L(ramp.outputs["Color"], mix.inputs["A"])
    L(mot.outputs["Color"], mix.inputs["B"])
    L(mix.outputs["Result"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.2
    b.inputs["Coat Weight"].default_value = 0.6
    b.inputs["Coat Roughness"].default_value = 0.04
    return m


def unwrap_bake(kit):
    for c in kit.children:
        seen = set()
        obs = []
        for o in c.all_objects:                                  # one object per shared mesh (bollards)
            if o.type == "MESH" and o.data.name not in seen:
                seen.add(o.data.name)
                obs.append(o)
        if not obs:
            continue
        for o in bpy.context.scene.objects:
            o.select_set(o in obs)
        bpy.context.view_layer.objects.active = obs[0]
        with bpy.context.temp_override(active_object=obs[0], object=obs[0], selected_objects=obs,
                                       selected_editable_objects=obs):
            for o in obs:
                o.data.uv_layers.active = o.data.uv_layers["uv_bake"]
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.002)
            bpy.ops.object.mode_set(mode="OBJECT")
            for o in obs:
                o.data.uv_layers.active = o.data.uv_layers["uv_material"]
                o.select_set(False)


def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)
    load_context()
    F = Facade()
    kit = coll("aa_kit")
    P = append_props()
    out = place_props(P, kit, F)
    build_signs(kit, F)
    build_bucket(kit)
    build_cabinet_screen(kit)
    build_awning_lights(kit, F)
    build_clocktower_sign(kit)
    build_stone_post(kit)
    build_ground(kit, out["kerb"])
    unwrap_bake(kit)
    print("E6 BUILD fits", {k: (round(v, 3) if isinstance(v, float) else v) for k, v in out.items()},
          "objects", len(bpy.data.objects))
    if "--no-save" not in args:
        bpy.ops.wm.save_as_mainfile(filepath=str(WIP))
        print("saved", WIP)


main()
