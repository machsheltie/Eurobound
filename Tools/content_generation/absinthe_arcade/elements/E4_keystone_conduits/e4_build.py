"""Build E4 (keystone headphones, green hoses, purple conduits, junction boxes, pipes, "13" plaque)
into wip/E4_keystone_conduits.blend. Re-runnable.

  blender -b --factory-startup --python e4_build.py -- [--no-save]

Every traced bible pixel (e4_trace.py) is cast through aa_bible_cam onto mason's stone (appended from
aa_exterior.blend as context) or onto a named plane; runs then follow the stone relief between their
vertices (straight on the facade, jogging out over cornices and mouldings), stand off it by a few mm
and are clamped back to it. Kit: aa_kit/aa_e4_* collections, facade pivot (arch axis, facade plane
y=0, street z=0). Context (not kit): e4_context.
"""
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import e4_trace as T  # noqa: E402
from e4_cam import BibleCam  # noqa: E402

REPO = HERE.parents[4]
MAIN = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/aa_exterior.blend"
HEAD_BLEND = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/E4_head_ingest.blend"
E3WIP = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/E3_entrance.blend"
WIP = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/E4_keystone_conduits.blend"
STONE = ["aa_shell_facade_walls", "aa_shell_facade_mouldings", "aa_shell_facade_window_surrounds",
         "aa_shell_facade_corner_bay", "aa_arch_hero_archivolt", "aa_arch_hero_cartouche", "aa_arch_hero_plinths"]
CONTEXT_EXTRA = ["aa_shell_facade_sash_windows", "aa_decal_mural"]
FONT_SERIF = Path("C:/Windows/Fonts/cambriab.ttf")
STANDOFF = 0.008
PI = math.pi
CAM = BibleCam()


# =========================================================================================
# context + raycasting
# =========================================================================================
def coll(name, parent=None):
    c = bpy.data.collections.get(name) or bpy.data.collections.new(name)
    p = parent or bpy.context.scene.collection
    if c.name not in [x.name for x in p.children]:
        p.children.link(c)
    return c


def load_context():
    ctx = coll("e4_context")
    with bpy.data.libraries.load(str(MAIN), link=False) as (src, dst):
        dst.objects = [n for n in STONE + CONTEXT_EXTRA if n in src.objects]
    for o in dst.objects:
        ctx.objects.link(o)
    if E3WIP.exists():
        with bpy.data.libraries.load(str(E3WIP), link=False) as (src, dst):
            dst.collections = [n for n in ("aa_e3_marquee",) if n in src.collections]
        for c in dst.collections:
            ctx.children.link(c)
    return ctx


class Facade:
    def __init__(self, names):
        dg = bpy.context.evaluated_depsgraph_get()
        self.trees = []
        for n in names:
            o = bpy.data.objects.get(n)
            if o is None or o.type != "MESH":
                continue
            bm = bmesh.new()
            bm.from_object(o, dg)
            bm.transform(o.matrix_world)
            self.trees.append(BVHTree.FromBMesh(bm))
            bm.free()

    def ray(self, origin, d, dist=60.0):
        best = (None, None, dist)
        for t in self.trees:
            loc, nrm, _, dd = t.ray_cast(Vector(origin), Vector(d).normalized(), dist)
            if loc is not None and dd < best[2]:
                best = (loc, nrm, dd)
        return best[0], best[1]

    def cam_hit(self, u, v):
        return self.ray(CAM.loc, CAM.ray(u, v))

    def surf(self, x, z):
        loc, _ = self.ray((x, -6.0, z), (0, 1, 0), 12.0)
        return loc.y if loc is not None else 0.0


def recess_keystone_context():
    """Context only, pending mason's recess (interfaces v2): drop the archivolt's keystone voussoir and the
    cartouche behind the head, so the head and volutes read in front of the archivolt as in the bible."""
    c = bpy.data.objects.get("aa_arch_hero_cartouche")
    if c:
        bpy.data.objects.remove(c)
    o = bpy.data.objects.get("aa_arch_hero_archivolt")
    if o is None:
        return
    bm = bmesh.new()
    bm.from_mesh(o.data)
    mw = o.matrix_world
    kill = [f for f in bm.faces if abs((mw @ f.calc_center_median()).x) < 0.42 and (mw @ f.calc_center_median()).z > 4.55]
    bmesh.ops.delete(bm, geom=kill, context="FACES")
    bm.to_mesh(o.data)
    bm.free()


def conform_mural(F):
    """Context only: the appended mural decal floats up to 0.17 m off mason's stone and hides anything
    fixed to the wall. Paint lies on the stone, so drop each decal vertex onto it (3 mm proud)."""
    o = bpy.data.objects.get("aa_decal_mural")
    if o is None:
        return
    mw, mi = o.matrix_world, o.matrix_world.inverted()
    for v in o.data.vertices:
        p = mw @ v.co
        p.y = F.surf(p.x, p.z) - 0.003
        v.co = mi @ p
    o.data.update()


def px_scale(u, v, y):
    """metres per bible pixel at depth plane y."""
    a = CAM.to_plane_y(u, v, y)
    b = CAM.to_plane_y(u + 1, v, y)
    return abs(b[0] - a[0])


# =========================================================================================
# materials
# =========================================================================================
MATS = {}


def lin(r, g, b):
    c = lambda v: (v / 255) / 12.92 if v / 255 <= 0.04045 else (((v / 255) + 0.055) / 1.055) ** 2.4
    return (c(r), c(g), c(b))


def mat(name, base, rough=0.5, metal=0.0, emit=None, estr=0.0, coat=0.0):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (*base, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    b.inputs["Coat Weight"].default_value = coat
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = estr
    m.diffuse_color = (*base, 1)
    MATS[name] = m
    return m


def materials():
    M = {}
    M["purple"] = mat("m_e4_conduit_purple", lin(140, 55, 185), rough=0.2, coat=0.7, emit=lin(160, 70, 215), estr=0.3)
    M["green"] = mat("m_e4_hose_green", lin(95, 170, 25), rough=0.18, coat=0.8, emit=lin(120, 200, 30), estr=0.28)
    M["steel"] = mat("m_e4_steel", (0.62, 0.62, 0.64), rough=0.3, metal=1.0)
    M["galv"] = mat("m_e4_galvanised", (0.55, 0.56, 0.57), rough=0.45, metal=1.0)
    M["box"] = mat("m_e4_box_grey", lin(168, 170, 168), rough=0.45, metal=0.0, coat=0.2)
    M["cup"] = mat("m_e4_earcup_grey_paint", lin(160, 162, 162), rough=0.5)              # matte painted grey metal
    M["dark"] = mat("m_e4_recess_dark", lin(20, 20, 22), rough=0.6)
    M["black"] = mat("m_e4_black_plastic", lin(18, 18, 20), rough=0.45)
    M["iron"] = mat("m_e4_cast_iron_black", lin(16, 17, 19), rough=0.38, coat=0.25)
    M["brass"] = mat("m_e4_brass", (0.70, 0.52, 0.25), rough=0.3, metal=1.0)
    M["yellow"] = mat("m_e4_decal_yellow", lin(235, 190, 30), rough=0.5)
    M["amber"] = mat("m_e4_indicator_amber", lin(200, 140, 40), rough=0.3, emit=lin(230, 150, 40), estr=0.6)
    M["blue_led"] = mat("m_e4_led_blue", lin(60, 90, 255), rough=0.2, emit=lin(80, 110, 255), estr=4.0)
    M["label_blue"] = mat("m_e4_label_blue", lin(40, 110, 200), rough=0.6)
    M["label_white"] = mat("m_e4_label_white", lin(230, 230, 225), rough=0.6)
    M["plaque"] = mat("m_e4_plaque_navy_black", lin(14, 18, 30), rough=0.35, coat=0.4)
    M["white"] = mat("m_e4_plaque_white", lin(240, 240, 238), rough=0.4)
    M["stone"] = mat("m_e4_carved_sandstone", lin(212, 178, 136), rough=0.85)
    M["cup_rim"] = mat("m_e4_earcup_rim_dark", lin(88, 90, 92), rough=0.55)
    M["tube"] = mat("m_e4_crown_tube_green_gloss", lin(110, 190, 35), rough=0.1, metal=0.65, coat=1.0,
                    emit=lin(120, 200, 30), estr=0.15)
    M["stone_shadow"] = mat("m_e4_carved_sandstone_recess", lin(40, 31, 24), rough=0.95)   # carved-back ground (in shadow)
    M["curl"] = mat("m_e4_curl_sandstone", lin(194, 152, 110), rough=0.9)      # matches the head's toned sandstone
    nt_ = M["curl"].node_tree
    if not any(n.type == "BUMP" for n in nt_.nodes):
        bsdf_ = next(n for n in nt_.nodes if n.type == "BSDF_PRINCIPLED")
        nz_ = nt_.nodes.new("ShaderNodeTexNoise")
        nz_.inputs["Scale"].default_value = 180.0
        nz_.inputs["Detail"].default_value = 6
        bp_ = nt_.nodes.new("ShaderNodeBump")
        bp_.inputs["Strength"].default_value = 0.25
        bp_.inputs["Distance"].default_value = 0.002
        nt_.links.new(nz_.outputs["Fac"], bp_.inputs["Height"])
        nt_.links.new(bp_.outputs["Normal"], bsdf_.inputs["Normal"])
    M["neon"] = mat("m_e4_marquee_neon_green", lin(120, 215, 40), rough=0.06, coat=1.0,
                    emit=lin(130, 230, 45), estr=2.2)                                      # smooth glowing tube
    M["moustache"] = mat("m_e4_moustache_black", lin(12, 12, 13), rough=0.35, coat=0.3)
    return M


# =========================================================================================
# mesh helpers
# =========================================================================================
def new_obj(name, bm, mats, collection, smooth=True):
    me = bpy.data.meshes.new(name)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    for f in bm.faces:                              # smooth by angle: sharp rims, smooth tubes
        f.smooth = True
    for e in bm.edges:
        e.smooth = (not e.is_manifold) or e.calc_face_angle(0.0) < math.radians(35)
    bm.to_mesh(me)
    bm.free()
    for m in mats:
        me.materials.append(m)
    uv_box(me)
    ob = bpy.data.objects.get(name)
    if ob:
        bpy.data.objects.remove(ob)
    ob = bpy.data.objects.new(name, me)
    collection.objects.link(ob)
    ob.modifiers.new("WeightedNormal", "WEIGHTED_NORMAL").keep_sharp = True
    return ob


def uv_box(me):
    """uv_material: metric box projection; uv_bake: placeholder (replaced by the smart-project unwrap)."""
    while me.uv_layers:
        me.uv_layers.remove(me.uv_layers[0])
    a = me.uv_layers.new(name="uv_material")
    me.uv_layers.new(name="uv_bake")
    for p in me.polygons:
        n = p.normal
        for li in p.loop_indices:
            c = me.vertices[me.loops[li].vertex_index].co
            if abs(n.y) >= max(abs(n.x), abs(n.z)):
                a.data[li].uv = (c.x, c.z)
            elif abs(n.x) >= abs(n.z):
                a.data[li].uv = (c.y, c.z)
            else:
                a.data[li].uv = (c.x, c.y)


def frames(pts):
    """Parallel-transport frames along a polyline: list of (tangent, normal, binormal)."""
    out = []
    t0 = (pts[1] - pts[0]).normalized()
    ref = Vector((0, 1, 0)) if abs(t0.y) < 0.9 else Vector((1, 0, 0))
    n = t0.cross(ref).normalized()
    for i in range(len(pts)):
        if i == 0:
            t = t0
        elif i == len(pts) - 1:
            t = (pts[i] - pts[i - 1]).normalized()
        else:
            t = ((pts[i + 1] - pts[i]).normalized() + (pts[i] - pts[i - 1]).normalized())
            t = t.normalized() if t.length > 1e-6 else (pts[i] - pts[i - 1]).normalized()
        n = (n - t * n.dot(t))
        n = n.normalized() if n.length > 1e-6 else t.cross(ref).normalized()
        out.append((t, n, t.cross(n)))
    return out


def sweep(bm, pts, radius, mat_index=0, seg=16, caps=True, rad_fn=None):
    """Tube along pts; rad_fn(s) -> radius multiplier (corrugation)."""
    pts = [Vector(p) for p in pts]
    fr = frames(pts)
    rings = []
    s = 0.0
    for i, (p, (t, n, b)) in enumerate(zip(pts, fr)):
        if i:
            s += (p - pts[i - 1]).length
        r = radius * (rad_fn(s) if rad_fn else 1.0)
        rings.append([bm.verts.new(p + (n * math.cos(2 * PI * k / seg) + b * math.sin(2 * PI * k / seg)) * r)
                      for k in range(seg)])
    faces = []
    for i in range(len(rings) - 1):
        for k in range(seg):
            faces.append(bm.faces.new((rings[i][k], rings[i][(k + 1) % seg], rings[i + 1][(k + 1) % seg],
                                       rings[i + 1][k])))
    if caps:
        faces.append(bm.faces.new(rings[0][::-1]))
        faces.append(bm.faces.new(rings[-1]))
    for f in faces:
        f.material_index = mat_index
        f.smooth = True
    return faces


def fillet(pts, rad, n=8):
    """Round the polyline's interior corners with circular-ish (quadratic bezier) fillets."""
    pts = [Vector(p) for p in pts]
    if len(pts) < 3:
        return pts
    out = [pts[0]]
    for i in range(1, len(pts) - 1):
        a, b, c = pts[i - 1], pts[i], pts[i + 1]
        d1, d2 = (b - a), (c - b)
        r = min(rad, d1.length * 0.45, d2.length * 0.45)
        if r < 1e-4 or d1.normalized().dot(d2.normalized()) > 0.9995:
            out.append(b)
            continue
        p0 = b - d1.normalized() * r
        p2 = b + d2.normalized() * r
        for k in range(n + 1):
            t = k / n
            out.append(p0 * (1 - t) ** 2 + b * 2 * t * (1 - t) + p2 * t * t)
    out.append(pts[-1])
    return out


def densify(pts, step):
    out = [Vector(pts[0])]
    for a, b in zip(pts, pts[1:]):
        a, b = Vector(a), Vector(b)
        n = max(1, int((b - a).length / step))
        for k in range(1, n + 1):
            out.append(a.lerp(b, k / n))
    return out


def box(bm, c, size, mat_index, rot=None):
    m = Matrix.Translation(c)
    if rot is not None:
        m = m @ rot
    m = m @ Matrix.Diagonal((*size, 1))
    r = bmesh.ops.create_cube(bm, size=1.0, matrix=m)
    for v in r["verts"]:
        for f in v.link_faces:
            f.material_index = mat_index
    return r


def cyl(bm, c, axis, r, depth, mat_index, seg=16):
    q = Vector((0, 0, 1)).rotation_difference(Vector(axis).normalized()).to_matrix().to_4x4()
    res = bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r, radius2=r, depth=depth,
                                matrix=Matrix.Translation(c) @ q)
    for v in res["verts"]:
        for f in v.link_faces:
            f.material_index = mat_index
            f.smooth = True
    return res


# =========================================================================================
# routing on the stone
# =========================================================================================
def route_on_stone(F, verts_px, r, step=0.02):
    """Bible-px vertices -> 3D centreline that sits r + STANDOFF off the most proud stone under it."""
    anchors = []
    for (u, v) in verts_px:
        loc, _ = F.cam_hit(u, v)
        if loc is None:
            x, z = CAM.to_plane_y(u, v, 0.0)
            loc = Vector((x, 0.0, z))
        anchors.append(Vector((loc.x, 0.0, loc.z)))
    dense = densify(anchors, step)
    ys = [F.surf(p.x, p.z) for p in dense]
    # most proud within the tube's footprint, then 45-degree ramps
    w = max(1, int((r * 2 + 0.03) / step))
    yp = [min(ys[max(0, i - w):i + w + 1]) for i in range(len(ys))]
    for i in range(1, len(yp)):
        yp[i] = min(yp[i], yp[i - 1] + step)
    for i in range(len(yp) - 2, -1, -1):
        yp[i] = min(yp[i], yp[i + 1] + step)
    pts = [Vector((p.x, y - r - STANDOFF, p.z)) for p, y in zip(dense, yp)]
    # keep the elbows crisp: re-insert the anchor corners
    return simplify(pts, 0.0015), ys


def simplify(pts, tol):
    """Drop points collinear within tol (keeps corners and ramps)."""
    out = [pts[0]]
    for i in range(1, len(pts) - 1):
        a, b, c = out[-1], pts[i], pts[i + 1]
        d = (c - a)
        if d.length < 1e-6:
            continue
        dist = (b - a).cross(d.normalized()).length
        if dist > tol:
            out.append(b)
    out.append(pts[-1])
    return out


CLAMP_SPOTS = []


def clamps_along(bm_clamp, F, pts, r, every, mi_strap, mi_screw, kind="saddle", seed=0):
    """Saddle straps (or black clips) at intervals, feet screwed to the stone."""
    length = sum((b - a).length for a, b in zip(pts, pts[1:]))
    s_targets = [every * (k + 0.5) for k in range(int(length / every))]
    acc, i = 0.0, 0
    for st in s_targets:
        while i < len(pts) - 2 and acc + (pts[i + 1] - pts[i]).length < st:
            acc += (pts[i + 1] - pts[i]).length
            i += 1
        a, b = pts[i], pts[i + 1]
        seg = (b - a)
        if seg.length < 1e-6:
            continue
        p = a + seg.normalized() * (st - acc)
        t = seg.normalized()
        if abs(t.y) > 0.5:                  # ramp: no clamp on a jog
            continue
        if any((p - q).length < 0.09 for q in CLAMP_SPOTS):     # parallel runs: one clamp per spot
            continue
        CLAMP_SPOTS.append(p.copy())
        wall = F.surf(p.x, p.z)
        side = Vector((0, 0, 1)).cross(t) if abs(t.z) < 0.9 else Vector((1, 0, 0))
        side = Vector((side.x, 0, side.z)).normalized()
        k = (seed + len(s_targets)) % 3 if kind == "mixed" else 0
        if kind == "black" or k == 2:
            # black plastic clip: a block over the tube
            if side.cross(Vector((0, 1, 0))).dot(t) < 0:
                side = -side
            rot = Matrix((side, Vector((0, 1, 0)), t)).transposed().to_4x4()
            box(bm_clamp, Vector((p.x, (wall + p.y - r) / 2, p.z)), (r * 2.6, abs(wall - (p.y - r)) + 0.004, 0.022),
                mi_screw, rot)
            seed += 1
            continue
        # saddle: U strap round the tube + two feet
        prof = []
        for j in range(13):
            ang = PI * j / 12
            prof.append(p + side * (math.cos(ang) * (r + 0.0012)) + Vector((0, -1, 0)) * (math.sin(ang) * (r + 0.0012)))
        foot_y = wall - 0.0035
        strap = [Vector((prof[0].x, foot_y, prof[0].z))] + prof + [Vector((prof[-1].x, foot_y, prof[-1].z))]
        sweep_rect(bm_clamp, strap, t, 0.016, 0.0025, mi_strap)
        for sgn in (1, -1):                                       # foot pads + screws, separate from the strap
            fp = Vector((p.x, wall - 0.0014, p.z)) + side * sgn * (r + 0.014)
            box(bm_clamp, fp, (0.024, 0.0028, 0.018), mi_strap,
                Matrix((Vector((side.x, 0, side.z)), Vector((0, 1, 0)), t)).transposed().to_4x4()
                if side.cross(Vector((0, 1, 0))).dot(t) > 0 else
                Matrix((-Vector((side.x, 0, side.z)), Vector((0, 1, 0)), t)).transposed().to_4x4())
            cyl(bm_clamp, fp + Vector((0, -0.0026, 0)), (0, 1, 0), 0.0045, 0.003, mi_screw, seg=8)
        seed += 1


def sweep_rect(bm, pts, axis, w, h, mi):
    """Flat strap (w along `axis`, thickness h) along pts lying in the plane normal to axis."""
    axis = Vector(axis).normalized()
    pts = [Vector(p) for p in pts]
    rings = []
    for i, p in enumerate(pts):
        t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        nrm = axis.cross(t).normalized()
        rings.append([bm.verts.new(p + axis * sa * w / 2 + nrm * sb * h / 2)
                      for sa, sb in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
    for i in range(len(rings) - 1):
        for k in range(4):
            f = bm.faces.new((rings[i][k], rings[i][(k + 1) % 4], rings[i + 1][(k + 1) % 4], rings[i + 1][k]))
            f.material_index = mi
    made = []
    for i in range(len(rings) - 1):
        pass
    for ring in (rings[0][::-1], rings[-1]):
        f = bm.faces.new(ring)
        f.material_index = mi
    # orient the closed strap outward (a strap swept against its own tangent winds inside out)
    vs = {v for r_ in rings for v in r_}
    fs = {f for v in vs for f in v.link_faces}
    vol = 0.0
    for f in fs:
        co = [v.co for v in f.verts]
        for k in range(1, len(co) - 1):
            vol += co[0].dot(co[k].cross(co[k + 1]))
    if vol < 0:
        bmesh.ops.reverse_faces(bm, faces=list(fs))


# =========================================================================================
# builders
# =========================================================================================
BOX_GEOM = {}


SCREWS = None


def build_boxes(F, M, C):
    """Boxes are bevelled; their screw heads go to one unbevelled object (the bevel collapsed them)."""
    global SCREWS
    SCREWS = bmesh.new()
    _build_boxes(F, M, C)
    new_obj("aa_e4_box_screws", SCREWS, [M["galv"], M["galv"]], C, smooth=False)


def _build_boxes(F, M, C):
    for name, (u, v), wpx, hpx, depth, feat in T.BOXES:
        loc, _ = F.cam_hit(u, v)
        wall = F.surf(loc.x, loc.z) if loc is not None else 0.0
        if name == "L_big":
            wall -= 0.13                    # bolted to a steel frame in front of the left downpipe (bible)
        sc = px_scale(u, v, wall - depth)
        w, h = wpx * sc, hpx * sc
        cx, cz = (loc.x, loc.z) if loc is not None else CAM.to_plane_y(u, v, 0.0)
        # re-project the centre on the box front plane so the front face lands where the bible shows it
        cx, cz = CAM.to_plane_y(u, v, wall - depth)
        BOX_GEOM[name] = (cx, cz, w, h, wall, depth)
        bm = bmesh.new()
        mats = [M["box"], M["galv"], M["dark"], M["yellow"], M["amber"], M["label_blue"], M["label_white"],
                M["blue_led"], M["black"], M["brass"]]
        yb, yf = wall, wall - depth
        box(bm, Vector((cx, (yb + yf + 0.012) / 2, cz)), (w, depth - 0.012, h), 0)                 # body
        box(bm, Vector((cx, yf + 0.006, cz)), (w + 0.006, 0.012, h + 0.006), 0)                     # lid
        for sx in (-1, 1):                                                                           # lid screws
            for sz in (-1, 1):
                cyl(SCREWS, Vector((cx + sx * (w / 2 - 0.018), yf - 0.002, cz + sz * (h / 2 - 0.018))), (0, 1, 0),
                    0.006, 0.003, 1, seg=10)          # screw heads seated on the lid (not sunk into its bevel)
        for sx in (-1, 1):                                                                           # wall lugs
            box(bm, Vector((cx + sx * (w / 2 + 0.012), yb - 0.004, cz)), (0.024, 0.008, 0.04), 1)
            cyl(SCREWS, Vector((cx + sx * (w / 2 + 0.012), yb - 0.009, cz)), (0, 1, 0), 0.005, 0.004, 1, seg=8)
        if feat.get("hinge"):
            hx = cx + (-1 if feat["hinge"] == "left" else 1) * (w / 2 + 0.004)
            for dz in (-0.3, 0.3):
                cyl(bm, Vector((hx, yf + 0.006, cz + dz * h)), (0, 0, 1), 0.006, 0.05, 1, seg=10)
        yd = yf - 0.0022
        if feat.get("triangle"):
            s = min(w, h) * 0.32
            tc = Vector((cx, yd, cz + h * 0.05))
            tri = [tc + Vector((-s / 2, 0, -s * 0.43)), tc + Vector((s / 2, 0, -s * 0.43)), tc + Vector((0, 0, s * 0.43))]
            decal_poly(bm, tri, 3, 0.0035)
            inner = [tc + (p - tc) * 0.62 for p in tri]
            decal_poly(bm, [p + Vector((0, -0.003, 0)) for p in inner], 2, 0.0018, ring=0.006)   # thick enough to orient
            cyl(bm, tc + Vector((0, -0.0045, -s * 0.02)), (0, 1, 0), s * 0.06, 0.001, 2, seg=12)
        if feat.get("knob"):                       # brass lock ring with a dark keyhole (bible)
            kc = Vector((cx, yf, cz + h * 0.3))
            cyl(bm, kc + Vector((0, -0.006, 0)), (0, 1, 0), min(w, h) * 0.1, 0.012, 9, seg=24)
            cyl(bm, kc + Vector((0, -0.0125, 0)), (0, 1, 0), min(w, h) * 0.065, 0.002, 2, seg=20)
            box(bm, kc + Vector((0, -0.0145, -min(w, h) * 0.02)), (min(w, h) * 0.02, 0.002, min(w, h) * 0.05), 9)
        if feat.get("round_sticker"):
            sc_ = Vector((cx - w * 0.04, yd, cz + h * 0.3))
            cyl(bm, sc_, (0, 1, 0), min(w, h) * 0.11, 0.0035, 4, seg=24)
            cyl(bm, sc_ + Vector((0, -0.0022, 0)), (0, 1, 0), min(w, h) * 0.055, 0.0018, 2, seg=20)
        if name == "L_big":                         # steel frame it is bolted to, spanning the downpipe
            for dz in (-0.32, 0.32):
                box(bm, Vector((cx, yb + 0.0625, cz + dz * h)), (w * 1.25, 0.123, 0.03), 1)
                for sx in (-1, 1):
                    box(bm, Vector((cx + sx * w * 0.6, yb + 0.1265, cz + dz * h)), (0.05, 0.007, 0.08), 1)
        if feat.get("label"):
            mi = 5 if feat["label"] == "blue" else 6
            box(bm, Vector((cx - w * 0.06, yd, cz - h * 0.12 if feat["label"] == "blue" else cz)),
                (w * 0.5, 0.0035, h * 0.16), mi)
        if feat.get("blue_led"):
            cyl(bm, Vector((cx, yf - 0.008, cz - h * 0.1)), (0, 1, 0), min(w, h) * 0.16, 0.016, 7, seg=16)
        if feat.get("fitting"):
            for dz in (-1, 1):                                                                       # threaded hubs
                cyl(bm, Vector((cx, (yb + yf) / 2, cz + dz * (h / 2 + 0.012))), (0, 0, 1), 0.026, 0.024, 1, seg=16)
        ob = new_obj(f"aa_e4_box_{name}", bm, mats, C, smooth=False)
        bv = ob.modifiers.new("Bevel", "BEVEL")
        bv.width, bv.segments, bv.limit_method = 0.0012, 2, "ANGLE"     # small enough not to collapse 6 mm screws
        bv.use_clamp_overlap = True
        bv.angle_limit = math.radians(50)   # skip the 36-degree side edges of 10-segment screws (they collapsed)
        ob.modifiers.move(1, 0)


def decal_poly(bm, pts, mi, thick, ring=None):
    """Thin decal prism proud of the box lid (front at pts' y, back `thick` behind). ring: outline width."""
    if ring:                                         # one closed band (no shared coplanar sides)
        c = sum(pts, Vector()) / len(pts)
        inner = [c + (p - c) * (1 - ring / max((p - c).length, 1e-6)) for p in pts]
        n = len(pts)
        of = [bm.verts.new(p) for p in pts]
        inf = [bm.verts.new(p) for p in inner]
        ob = [bm.verts.new(p + Vector((0, thick, 0))) for p in pts]
        ib = [bm.verts.new(p + Vector((0, thick, 0))) for p in inner]
        made = []
        for k in range(n):
            j = (k + 1) % n
            for q in ((of[k], of[j], inf[j], inf[k]), (ob[j], ob[k], ib[k], ib[j]),
                      (of[j], of[k], ob[k], ob[j]), (inf[k], inf[j], ib[j], ib[k])):
                f = bm.faces.new(q)
                f.material_index = mi
                made.append(f)
        vol = sum(f.verts[0].co.dot(f.verts[i].co.cross(f.verts[i + 1].co))
                  for f in made for i in range(1, len(f.verts) - 1))
        if vol < 0:                                  # wind the band outward whatever the input order
            bmesh.ops.reverse_faces(bm, faces=made)
        return
    vf = [bm.verts.new(p) for p in pts]
    vb = [bm.verts.new(p + Vector((0, thick, 0))) for p in pts]
    fs = [bm.faces.new(vf), bm.faces.new(vb[::-1])]
    for k in range(len(pts)):
        j = (k + 1) % len(pts)
        fs.append(bm.faces.new((vf[k], vb[k], vb[j], vf[j])))
    for f in fs:
        f.material_index = mi


def build_conduits(F, M, C):
    bm_c = bmesh.new()
    bm_k = bmesh.new()
    for name, verts, wpx, couplers in T.PURPLE:
        u, v = verts[0]
        r = max(0.014, wpx * px_scale(u, v, -0.03) / 2)
        pts, _ = route_on_stone(F, verts, r)
        path = fillet(pts, r * 3.0, 8)
        sweep(bm_c, densify(path, 0.03), r, 0, seg=18)
        clamps_along(bm_k, F, pts, r, 0.36, 0, 1, kind="mixed", seed=len(name))
        for ci in couplers:
            loc, _ = F.cam_hit(*verts[ci])
            if loc is None:
                continue
            q = min(pts, key=lambda p: (Vector((p.x, 0, p.z)) - Vector((loc.x, 0, loc.z))).length)
            i = pts.index(q)
            t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
            cyl(bm_k, q, t, r * 1.45, 0.07, 0, seg=20)
            cyl(bm_k, q, t, r * 1.6, 0.012, 0, seg=6)
    new_obj("aa_e4_conduits_purple", bm_c, [M["purple"]], C)
    new_obj("aa_e4_conduit_clamps", bm_k, [M["galv"], M["black"]], C, smooth=False)
    # black flex cables
    bm_b = bmesh.new()
    bm_bk = bmesh.new()
    for name, verts, wpx in T.BLACK:
        r = 0.009
        pts, _ = route_on_stone(F, verts, r)
        sweep(bm_b, densify(fillet(pts, 0.06, 8), 0.03), r, 0, seg=10)
        clamps_along(bm_bk, F, pts, r, 0.3, 0, 0, kind="black")
    # thin black pipe beside the downspout
    pts, _ = route_on_stone(F, T.BLACK_PIPE_R, 0.025)
    sweep(bm_b, densify(pts, 0.05), 0.025, 0, seg=14)
    clamps_along(bm_bk, F, pts, 0.025, 0.5, 0, 0)
    new_obj("aa_e4_cables_black", bm_b, [M["black"]], C)
    new_obj("aa_e4_cable_clips", bm_bk, [M["black"]], C, smooth=False)


def corrugate(pitch=0.028, depth=0.13):
    return lambda s: 1.0 + depth * (0.5 + 0.5 * math.cos(2 * PI * s / pitch))


def build_green(F, M, C, marquee_tree):
    bm = bmesh.new()
    bm_s = bmesh.new()                                  # smooth glossy runs (the cup hose)
    bm_k = bmesh.new()
    for name, verts, wpx, target, collars in T.GREEN:
        if name == "marquee_top":
            continue                                    # built by build_marquee_neon (smooth, on the housing)
        u, v = verts[0]
        if target == "stone":
            r = wpx * px_scale(u, v, -0.05) / 2
            pts, _ = route_on_stone(F, verts, r)
            pts = fillet(pts, 0.25, 10)
        elif target == "marquee":
            r = wpx * px_scale(u, v, -0.4) / 2
            pts = []
            for (uu, vv) in verts:
                loc, nrm, _, _ = marquee_tree.ray_cast(Vector(CAM.loc), Vector(CAM.ray(uu, vv)).normalized(), 60)
                if loc is None:
                    x, z = CAM.to_plane_y(uu, vv, -0.36)
                    loc = Vector((x, -0.36, z))
                pts.append(Vector((loc.x, loc.y - r, loc.z)))
            pts = fillet(pts, 0.08, 8)
        else:   # free: from the cup outlet down to the marquee, on a plane easing back to the board
            n = len(verts)
            pts = []
            for k, (uu, vv) in enumerate(verts):
                y = T.HEAD_PLANE_Y + (-0.36 - T.HEAD_PLANE_Y) * (k / (n - 1))
                x, z = CAM.to_plane_y(uu, vv, y)
                pts.append(Vector((x, y, z)))
            r = wpx * px_scale(u, v, T.HEAD_PLANE_Y) / 2
            if name == "cup_R_hose" and "R" in PORT:     # starts in the right cup's threaded side port
                p0, dirp, rp = PORT["R"]
                r = rp
                pts = [p0, p0 + dirp * 0.06] + pts[1:]
                cyl(bm_k, p0 + dirp * 0.03, dirp, r * 1.3, 0.05, 0, seg=24)      # chrome collar
            pts = fillet(pts, 0.2, 10)
        smooth_hose = (name == "cup_R_hose")
        sweep(bm_s if smooth_hose else bm, densify(pts, 0.006), r, 0, seg=20,
              rad_fn=None if smooth_hose else corrugate(pitch=max(0.02, r * 0.9)))
        for ci in collars:
            uu, vv = verts[ci]
            q = min(pts, key=lambda p: (Vector(CAM.project(p)) - Vector((uu, vv))).length)
            i = pts.index(q)
            t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
            cyl(bm_k, q, t, r * 1.35, 0.06, 0, seg=20)
            cyl(bm_k, q, t, r * 1.5, 0.014, 0, seg=6)
        if target == "stone":
            clamps_along(bm_k, F, [p for p in densify(pts, 0.02)][::3], r, 0.45, 0, 0)
    new_obj("aa_e4_hoses_green", bm, [M["green"]], C)
    new_obj("aa_e4_hose_cup_smooth", bm_s, [M["tube"]], C)
    new_obj("aa_e4_hose_collars", bm_k, [M["steel"]], C, smooth=False)


# ear cups: pose fitted so the projected face rim and the whole cup silhouette overlay the bible
# (scratchpad cupfit.py, least squares through aa_bible_cam; residuals <= 6 px). F = face centre,
# yaw / pitch turn the cup axis (face -> back), r = cup radius.
CUP_POSE = {
    "L": (Vector((-0.4689, -0.3777, 5.2166)), -11.9, -6.7, 0.1588),
    "R": (Vector((0.6823, -0.3885, 5.1637)), -14.3, 8.73, 0.1690),
}
CUP_TRACE = {"L": (3001, 3123, 1820, 1954), "R": (3500, 3642, 1756, 1914)}   # traced face-rim boxes (bible px)
CUP_OVERLAP_PX = {"L": 40, "R": 42}         # cup face over the head's edge (bible ~28 / 42; L pushed further in so its rim hides the edge)
TUBE_Y = -0.06                          # crown tube runs behind the crown curls
PORT = {}                               # right cup's side-port outlet (world): the hose starts there


def _cup_matrix(F, yaw, pitch, d):
    R = Matrix.Rotation(math.radians(yaw), 4, "Z") @ Matrix.Rotation(math.radians(pitch), 4, "X")
    a = (R @ Vector((0, 1, 0, 0))).to_3d().normalized()
    return Matrix.Translation(F + a * (d / 2)) @ R, a


def build_headphones(M, C):
    head = bpy.data.objects.get("aa_e4_keystone_head")
    htree = None
    if head:
        hb = bmesh.new()
        hb.from_mesh(head.data)
        hb.transform(head.matrix_world)
        htree = BVHTree.FromBMesh(hb)
        hb.free()
    cups = {}
    bm_all = bmesh.new()

    camv = Vector(CAM.loc)
    for side, (F, yaw, pitch, r) in CUP_POSE.items():
        d = r * 0.9
        if htree:
            hcen = sum((head.matrix_world @ Vector(b_) for b_ in head.bound_box), Vector()) / 8
            inward = Vector((1.0 if hcen.x > F.x else -1.0, 0, 0))
            hv = [head.matrix_world @ v.co for v in list(head.data.vertices)[::7]]
            pv = [CAM.project(q) for q in hv]
            Mt, _ = _cup_matrix(F, yaw, pitch, d)
            vc = CAM.project(Mt @ Vector((0, -d / 2, 0)))[1]
            # visible head edge on the cup's row: first camera ray (from the cup toward the head) that hits it
            uc0 = CAM.project(Mt @ Vector((0, -d / 2, 0)))[0]
            hair_edge = None
            for k in range(0, 400):
                uu = uc0 + (k if side == "L" else -k)
                if htree.ray_cast(camv, Vector(CAM.ray(uu, vc)).normalized(), 80)[0] is not None:
                    hair_edge = uu
                    break
            if hair_edge is None:
                hair_edge = uc0 + (400 if side == "L" else -400)
            shift = 0.0
            for k in range(0, 81):
                s_ = k * 0.0025
                Mt, _ = _cup_matrix(F + inward * s_, yaw, pitch, d)
                rimu = [CAM.project(Mt @ Vector((r * math.cos(2 * PI * j / 48), -d / 2, r * math.sin(2 * PI * j / 48))))[0]
                        for j in range(48)]
                inner = max(rimu) if side == "L" else min(rimu)
                over = (inner - hair_edge) if side == "L" else (hair_edge - inner)
                if over >= CUP_OVERLAP_PX[side]:
                    shift = s_
                    break
            F = F + inward * shift
            FIT["cup_shift_" + side] = shift
            FIT["cup_hair_edge_u_" + side] = hair_edge
            FIT["cup_inner_u_" + side] = inner
            # back along the camera ray (projection kept, scaled with distance) until the back plate meets the head
            for k_ in [1.0 + 0.001 * i for i in range(0, 21)]:          # <= ~0.23 m back along the ray
                Fk = camv + (F - camv) * k_
                Mt, _ = _cup_matrix(Fk, yaw, pitch, r * k_ * 0.9)
                rim = [Mt @ Vector((r * k_ * math.cos(2 * PI * j / 24), r * k_ * 0.45 + 0.012,
                                    r * k_ * math.sin(2 * PI * j / 24))) for j in range(24)]
                if min(htree.find_nearest(q)[3] for q in rim) < 0.012:
                    break
            F, r = Fk, r * k_
            d = r * 0.9
            FIT["cup_k_" + side] = k_
        Mw, a = _cup_matrix(F, yaw, pitch, d)
        bm = bmesh.new()
        # local cup: axis along +Y (face toward the street at y = -d/2), centre at origin
        cyl(bm, Vector((0, 0, 0)), (0, 1, 0), r, d, 0, seg=64)
        bmesh.ops.bevel(bm, geom=[e for e in bm.edges if e.calc_face_angle(0) > 1.0], offset=r * 0.06,
                        segments=3, affect="EDGES", clamp_overlap=True)
        cyl(bm, Vector((0, d / 2 + 0.012, 0)), (0, 1, 0), r * 0.9, 0.024, 4, seg=64)        # back plate, dark rim
        rim_faces = [f for f in bm.faces if abs(f.normal.y) < 0.2 and (f.calc_center_median().y < -d / 2 + d * 0.23)]
        for f in rim_faces:
            f.material_index = 4                                                        # darker rim band
        yf = -d / 2 - 0.0002
        for ang in (45, 135, 225, 315):                                                    # 4 bolts
            p = Vector((r * 0.74 * math.cos(math.radians(ang)), yf, r * 0.74 * math.sin(math.radians(ang))))
            cyl(bm, p, (0, 1, 0), r * 0.05, 0.003, 1, seg=10)
        for sgn in (-1, 1):                                                                # 2 radial slots
            box(bm, Vector((sgn * r * 0.84, yf, 0)), (r * 0.16, 0.002, r * 0.022), 1)
        # connector collar on top: the crown tube enters it
        cyl(bm, Vector((0, 0, r * 1.05)), (0, 0, 1), r * 0.2, r * 0.26, 2, seg=24)
        cyl(bm, Vector((0, 0, r * 1.2)), (0, 0, 1), r * 0.235, r * 0.05, 2, seg=6)          # hex nut
        if side == "R":
            # side port (bottom right) with a short threaded fitting where the hose leaves
            pa = Vector((math.cos(math.radians(-35)), 0, math.sin(math.radians(-35))))
            base = Vector((0, -d * 0.12, 0)) + pa * r * 0.98
            cyl(bm, base + pa * r * 0.08, pa, r * 0.2, r * 0.18, 2, seg=24)
            for k in range(5):                                                             # threads
                cyl(bm, base + pa * (r * 0.2 + k * r * 0.045), pa, r * 0.15, r * 0.025, 2, seg=20)
            cyl(bm, base + pa * r * 0.44, pa, r * 0.19, r * 0.07, 2, seg=6)               # nut
            PORT["R"] = (Mw @ (base + pa * r * 0.48), (Mw.to_3x3() @ pa).normalized(), r * 0.15)
            # small fitting below the cup
            cyl(bm, Vector((-r * 0.15, -d * 0.1, -r * 1.06)), (0, 0, 1), r * 0.15, r * 0.24, 3, seg=16)
            cyl(bm, Vector((-r * 0.15, -d * 0.1, -r * 1.22)), (0, 0, 1), r * 0.1, r * 0.12, 2, seg=16)
        cyl(bm, Vector((0, d / 2 + 0.036, 0)), (0, 1, 0), r * 0.8, 0.03, 4, seg=48)      # thin pad on the head
        bmesh.ops.transform(bm, matrix=Mw, verts=bm.verts)
        tmp = bpy.data.meshes.new("tmp")
        bm.to_mesh(tmp)
        bm.free()
        bm_all.from_mesh(tmp)
        bpy.data.meshes.remove(tmp)
        cups[side] = (Mw @ Vector((0, 0, r * 1.23)), Mw.to_3x3() @ Vector((0, 0, 1)), r)
        rimf = [CAM.project(Mw @ Vector((r * math.cos(2 * PI * j / 48), -d / 2, r * math.sin(2 * PI * j / 48))))
                for j in range(48)]
        tb = CUP_TRACE[side]
        got = (min(p_[0] for p_ in rimf), max(p_[0] for p_ in rimf), min(p_[1] for p_ in rimf), max(p_[1] for p_ in rimf))
        FIT["cup_resid_px_" + side] = max(abs(g - t) for g, t in zip(got, tb))
        FIT["cup_centre_dx_px_" + side] = (got[0] + got[1] - tb[0] - tb[1]) / 2
    new_obj("aa_e4_headphone_cups", bm_all, [M["cup"], M["dark"], M["steel"], M["brass"], M["cup_rim"]], C,
            smooth=False)
    # crown tube: rises out of each cup's top collar and runs over the crown behind the curls
    (tl, nl, rl), (tr, nr, rr) = cups["L"], cups["R"]
    mid = []
    for (u, v) in T.CROWN[2:-2]:
        x, z = CAM.to_plane_y(u, v, TUBE_Y)
        mid.append(Vector((x, TUBE_Y, z)))
    pts = [tl - nl * 0.02, tl + nl * 0.07, tl + nl * 0.16 + Vector((0, (TUBE_Y - tl.y) * 0.5, 0))] + mid + \
        [tr + nr * 0.16 + Vector((0, (TUBE_Y - tr.y) * 0.5, 0)), tr + nr * 0.07, tr - nr * 0.02]
    r = T.CROWN_W * px_scale(*T.CROWN[5], -0.3) / 2
    bm = bmesh.new()
    sweep(bm, densify(fillet(pts, 0.08, 6), 0.01), r, 0, seg=24)
    new_obj("aa_e4_headphone_crown_tube", bm, [M["tube"]], C)
    FIT["cup_collar_L_z"] = tl.z
    FIT["cup_collar_R_z"] = tr.z


# =========================================================================================
# marquee neon bar: smooth glowing tube along the stepped top of the E3 marquee housing
# =========================================================================================
NEON_OFF = 0.035            # standoff above / outside the bezel outline
NEON_BOTTOM_Z = 3.15        # the side runs end here
NEON_W_PX = 16


def marquee_outline():
    rim = bpy.data.objects.get("aa_e3_marquee_rim")
    if rim is None:
        return None, None
    dg = bpy.context.evaluated_depsgraph_get()
    me = rim.evaluated_get(dg).to_mesh()
    vs = [rim.matrix_world @ v.co for v in me.vertices]
    rim.evaluated_get(dg).to_mesh_clear()
    yfront = min(v.y for v in vs)
    front = [v for v in vs if v.y < yfront + 0.06]
    step = 0.02
    x0, x1 = min(v.x for v in front), max(v.x for v in front)
    n = int((x1 - x0) / step) + 1
    top = [-9.0] * n
    for v in front:
        i = min(n - 1, max(0, int((v.x - x0) / step)))
        top[i] = max(top[i], v.z)
    for i in range(n):                                   # fill empty bins
        if top[i] < -8:
            top[i] = top[i - 1] if i else max(top)
    k = int(NEON_OFF / step) + 1                         # square Minkowski offset of the envelope
    off = [max(top[max(0, i - k):i + k + 1]) + NEON_OFF for i in range(n)]
    pts2 = [(x0 + (i + 0.5) * step, off[i]) for i in range(n)]
    return pts2, yfront


def build_marquee_neon(M, C):
    pts2, yfront = marquee_outline()
    if not pts2:
        return
    r = NEON_W_PX * px_scale(3330, 2185, yfront) / 2
    y = yfront - NEON_OFF * 0.6 - r
    xl, xr = pts2[0][0] - NEON_OFF, pts2[-1][0] + NEON_OFF
    path = [Vector((xl, y, NEON_BOTTOM_Z)), Vector((xl, y, pts2[0][1]))]
    path += [Vector((x, y, z)) for x, z in pts2]
    path += [Vector((xr, y, pts2[-1][1])), Vector((xr, y, NEON_BOTTOM_Z))]
    path = simplify(path, 0.004)
    path = densify(fillet(path, 0.035, 6), 0.01)
    bm = bmesh.new()
    sweep(bm, path, r, 0, seg=24)
    new_obj("aa_e4_marquee_neon_tube", bm, [M["neon"]], C)
    # small clamps: saddle band over the tube + a foot back to the bezel, every ~0.4 m, plus the couplings
    bmk = bmesh.new()
    s = 0.0
    nxt = 0.15
    for a_, b_ in zip(path, path[1:]):
        s += (b_ - a_).length
        if s >= nxt:
            t = (b_ - a_).normalized()
            cyl(bmk, b_, t, r * 1.3, 0.014, 0, seg=20)
            box(bmk, b_ + Vector((0, (yfront - b_.y) / 2 + r * 0.6, 0)), (0.008, max(0.01, yfront - b_.y - r * 1.2), 0.008), 0)
            nxt += 0.4
    new_obj("aa_e4_marquee_neon_clamps", bmk, [M["steel"]], C, smooth=False)
    FIT["neon_r"] = round(r, 4)
    FIT["neon_top_z"] = round(max(z for _, z in pts2), 3)


# =========================================================================================
# lower carving: clean modelled S / C scrolls traced off the bible (2980-3740 x 1940-2235)
# =========================================================================================
SCROLL_BED_Y = -0.27       # dark carved-back ground behind the curls
CURL_Y = -0.325            # plane of the curl centrelines (traced in bible px, cast through aa_bible_cam)
CURL_W = 1.4              # traced centreline half-widths -> the bible's fat rolled ribbons
CURL_BACK_Y = -0.262       # every curl's back face is flattened onto the bed
# explicitly modelled curls, traced off the bible crop 2985-3720 x 1945-2172 (form read from mural reference
# panel 9): name, centreline px (from the spiral eye / leaf root outward), half-width px, start factor, end
# factor, start cap ("eye" = rolled eye, "tip" = leaf tip, "" = plain round), end cap
CURLS = [
    # ---- right cluster
    ("R_big_s", [(3518, 2036), (3500, 2008), (3490, 1982), (3500, 1962), (3525, 1964), (3555, 1985), (3585, 2015),
                 (3598, 2050), (3585, 2083), (3555, 2100), (3515, 2102), (3482, 2092), (3463, 2080)], 18, 0.42, 0.55,
     "eye", ""),
    ("R_back_c", [(3622, 2042), (3606, 2052), (3618, 2068), (3650, 2068), (3680, 2048), (3690, 2014), (3674, 1985),
                  (3640, 1972), (3602, 1977), (3578, 1992)], 16, 0.42, 0.6, "eye", ""),
    ("R_tip", [(3694, 1988), (3705, 1972), (3696, 1958), (3676, 1955), (3655, 1965)], 10, 0.5, 0.65, "eye", ""),
    ("R_jaw_leaf", [(3446, 1992), (3442, 2040), (3433, 2090), (3420, 2135), (3402, 2168)], 15, 0.7, 0.3, "", "tip"),
    ("R_low_hook", [(3480, 2136), (3458, 2142), (3440, 2128), (3434, 2106), (3446, 2090)], 11, 0.6, 0.6, "", "eye"),
    ("R_low_lobe_a", [(3470, 2168), (3490, 2163), (3502, 2143), (3494, 2118)], 10, 0.45, 0.8, "tip", ""),
    ("R_low_lobe_b", [(3534, 2160), (3547, 2135), (3534, 2108)], 10, 0.45, 0.8, "tip", ""),
    # ---- under the goatee: a little carving, leaf tongues ending at the archivolt line
    ("C_leaf_l", [(3212, 2070), (3220, 2108), (3230, 2142), (3240, 2168)], 17, 0.8, 0.4, "", "tip"),
    ("C_leaf_l2", [(3258, 2116), (3266, 2144), (3276, 2168)], 11, 0.8, 0.4, "", "tip"),
    ("C_hook", [(3292, 2110), (3304, 2138), (3324, 2157), (3342, 2150), (3346, 2130)], 12, 0.8, 0.5, "", "eye"),
    ("C_leaf_r", [(3400, 2094), (3388, 2124), (3380, 2150), (3373, 2170)], 16, 0.8, 0.4, "", "tip"),
    # ---- left cluster (mirrored arrangement, varied)
    ("L_big_c", [(3138, 2096), (3152, 2092), (3165, 2108), (3158, 2128), (3130, 2140), (3094, 2133), (3068, 2110),
                 (3062, 2078), (3075, 2048), (3100, 2033), (3132, 2034), (3152, 2050)], 20, 0.42, 0.6, "eye", ""),
    ("L_top_hook", [(3150, 2046), (3157, 2024), (3146, 2004), (3124, 1997), (3108, 2010)], 13, 0.8, 0.55, "", "eye"),
    ("L_low_s", [(3168, 2128), (3152, 2140), (3157, 2158), (3178, 2164), (3202, 2150), (3213, 2125), (3200, 2104),
                 (3176, 2098), (3152, 2108)], 14, 0.42, 0.6, "eye", ""),
    ("L_outer_eye", [(3040, 2078), (3025, 2075), (3012, 2090), (3025, 2108), (3050, 2105), (3062, 2085),
                     (3055, 2060), (3030, 2045), (3000, 2048)], 15, 0.42, 0.6, "eye", ""),
    ("L_jaw_leaf", [(3205, 1995), (3203, 2035), (3196, 2075)], 12, 0.7, 0.45, "", "tip"),
]


def _smooth_px(pts, n=6):
    """Open Catmull-Rom through the traced px points (ends clamped)."""
    P = [Vector((u, v, 0)) for u, v in pts]
    P = [P[0]] + P + [P[-1]]
    out = []
    for k in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[k - 1], P[k], P[k + 1], P[k + 2]
        for t in [i / n for i in range(n)]:
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 +
                              (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(P[-2])
    return [(p.x, p.y) for p in out]


def _ss(e0, e1, x):
    t = min(1.0, max(0.0, (x - e0) / (e1 - e0)))
    return t * t * (3 - 2 * t)


def sweep_curl(bm, pts, wfn, seg=28):
    """One carved curl: a rounded teardrop section swept along the centreline. The fat rolled lip is on the
    outside of the curve, a soft channel runs along the inner side, the back is flattened onto the bed."""
    Y = Vector((0, 1, 0))
    n_ = len(pts)
    tans = []
    for i in range(n_):
        t = pts[min(i + 1, n_ - 1)] - pts[max(i - 1, 0)]
        tans.append(Vector((t.x, 0, t.z)).normalized())
    outs = []
    for i in range(n_):
        dt = tans[min(i + 1, n_ - 1)] - tans[max(i - 1, 0)]
        nrm = tans[i].cross(Y).normalized()
        outs.append(-max(-1.0, min(1.0, dt.dot(nrm) * 6.0)))
    outs = [sum(outs[max(0, i - 3):i + 4]) / len(outs[max(0, i - 3):i + 4]) for i in range(n_)]
    rings = []
    for i, p in enumerate(pts):
        nrm = tans[i].cross(Y).normalized()
        w = wfn(i / (n_ - 1))
        o = outs[i]
        d = w * 0.78
        ring = []
        for k in range(seg):
            th = 2 * PI * k / seg
            c, s_ = math.cos(th), math.sin(th)
            if s_ >= 0:                                            # front: rolled, lip fat on the outer side
                lip = 1.0 + 0.45 * c * o
                groove = (1.0 - 0.32 * math.exp(-((c + 0.42 * o) / 0.13) ** 2)
                          - 0.18 * math.exp(-((c - 0.55 * o) / 0.1) ** 2))      # carved channels along the band
                lat = w * c * (1.0 + 0.08 * o * c)
                dy = -d * (s_ ** 0.45) * lip * groove                           # flat-faced band, rolled shoulders
            else:                                                  # back: flattened onto the bed
                lat = w * c * (0.9 + 0.1 * (1 + s_))
                dy = (-s_) * (CURL_BACK_Y - p.y)
            ring.append(bm.verts.new(p + nrm * lat + Y * dy))
        rings.append(ring)
    for i in range(n_ - 1):
        for k in range(seg):
            bm.faces.new((rings[i][k], rings[i][(k + 1) % seg], rings[i + 1][(k + 1) % seg], rings[i + 1][k]))
    for ring, endp in ((rings[0], 0), (rings[-1], 1)):                   # domed caps
        c = sum((v.co for v in ring), Vector()) / len(ring)
        t = tans[0] if endp == 0 else tans[-1]
        tip = bm.verts.new(c + t * (-1 if endp == 0 else 1) * wfn(float(endp)) * 0.4)
        rr = ring if endp == 1 else ring[::-1]
        for k in range(len(rr)):
            bm.faces.new((rr[k], rr[(k + 1) % len(rr)], tip))
    return outs


# left temple hair locks (bible: the head's hair reaches out under the left cup; the Tripo head's left side is
# cheek at that depth, so the hair is modelled): wavy locks from the head's edge flowing down-left behind the cup
HAIR_LOCKS_L = [   # roots tucked under the head's left edge (u ~3195-3205), tips behind the cup
    [(3196, 1770), (3168, 1784), (3146, 1808), (3150, 1836), (3124, 1858)],
    [(3200, 1800), (3172, 1818), (3154, 1846), (3160, 1876), (3132, 1902)],
    [(3204, 1840), (3178, 1862), (3164, 1892), (3170, 1922), (3142, 1950)],
    [(3208, 1880), (3186, 1906), (3176, 1936), (3182, 1962), (3160, 1986)],
]
HAIR_LOCK_Y = -0.27


def build_hair_locks(M, C):
    head = bpy.data.objects.get("aa_e4_keystone_head")
    bm = bmesh.new()
    sc = px_scale(3160, 1860, HAIR_LOCK_Y)
    for tr in HAIR_LOCKS_L:
        pts = []
        for (u, v) in _smooth_px(tr, 8):
            x, z = CAM.to_plane_y(u, v, HAIR_LOCK_Y)
            pts.append(Vector((x, HAIR_LOCK_Y, z)))
        w = 12 * sc

        def wfn(s, w=w):
            return w * (0.85 + 0.15 * _ss(0.0, 0.3, s)) * (0.35 + 0.65 * _ss(1.0, 0.6, s))
        sweep_curl(bm, pts, wfn)
    ob = new_obj("aa_e4_keystone_hair_locks_l", bm, [M["curl"]], C)
    sub = ob.modifiers.new("Subdivision", "SUBSURF")
    sub.levels = sub.render_levels = 1
    ob.modifiers.move(len(ob.modifiers) - 1, 0)
    return ob


CURLS_BLEND = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/E4_curls_ingest.blend"
# bible footprints (px) of each scroll cluster, packed against the jaw from mouth level down to the archivolt
# line; anchor = the edge that meets the jaw (the other edge follows the cluster's own proportions)
CURL_FIT = {
    "aa_e4_keystone_curls_r": ((3432, 1948, 3716, 2172), "left"),
    "aa_e4_keystone_curls_l": ((2994, 1990, 3218, 2172), "right"),
}
CURL_FRONT_Y = -0.42


def append_curls(C):
    """glazier's two Tripo scroll clusters (e4_ingest_curls.py): each fitted through aa_bible_cam to its side's
    footprint (uniform scale), its jaw-side edge and its bottom (the archivolt line) pinned, back cut flat."""
    if not CURLS_BLEND.exists():
        return []
    with bpy.data.libraries.load(str(CURLS_BLEND), link=False) as (src, dst):
        dst.objects = [n for n in CURL_FIT if n in src.objects]
    out = []
    for o in dst.objects:
        C.objects.link(o)
        box, anchor = CURL_FIT[o.name]
        FIT[o.name + "_scale"] = fit_to_px(o, box, CURL_FRONT_Y, by="mean")
        me = o.data
        co = [v.co for v in list(me.vertices)[::max(1, len(me.vertices) // 4000)]]
        pr = [CAM.project(c) for c in co]
        pu0, pu1 = min(p[0] for p in pr), max(p[0] for p in pr)
        pv1 = max(p[1] for p in pr)
        du = (box[0] - pu0) if anchor == "left" else (box[2] - pu1)
        dv = box[3] - pv1
        sc = px_scale((box[0] + box[2]) / 2, (box[1] + box[3]) / 2, CURL_FRONT_Y)
        me.transform(Matrix.Translation((du * sc, 0, -dv * sc)))
        me.update()
        cut_back(o)
        pr = [CAM.project(v.co) for v in list(me.vertices)[::max(1, len(me.vertices) // 4000)]]
        FIT[o.name + "_px"] = round(min(p[0] for p in pr)), round(max(p[0] for p in pr)),             round(min(p[1] for p in pr)), round(max(p[1] for p in pr))
        out.append(o)
    return out


def build_scrolls(M, C):
    """aa_e4_keystone_scrolls: explicitly modelled curls (teardrop sections swept along traced spiral
    centrelines, tapering into their rolled eyes, leaf tongues tapering to tips), subdivided and smooth, on a
    dark carved-back bed."""
    import numpy as np
    bm = bmesh.new()
    sc = px_scale(3360, 2080, CURL_Y)
    for name, tr, wpx, f0, f1, cap0, cap1 in CURLS:
        sm = _smooth_px(tr, 8)
        pts = []
        for (u, v) in sm:
            x, z = CAM.to_plane_y(u, v, CURL_Y)
            pts.append(Vector((x, CURL_Y, z)))
        w = wpx * sc * CURL_W

        def wfn(s, w=w, f0=f0, f1=f1):
            return w * (f0 + (1 - f0) * _ss(0.0, 0.35, s)) * (f1 + (1 - f1) * _ss(1.0, 0.7, s))
        sweep_curl(bm, pts, wfn)
        for cap, endp in ((cap0, 0), (cap1, 1)):
            if cap != "eye":
                continue
            p = pts[0] if endp == 0 else pts[-1]
            we = wfn(float(endp))
            bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=14, radius=1.0,
                                      matrix=Matrix.Translation(p + Vector((0, -we * 0.45, 0))) @
                                      Matrix.Diagonal((we * 1.25, we * 1.1, we * 1.25, 1)))    # rolled eye
    ob = new_obj("aa_e4_keystone_scrolls", bm, [M["curl"]], C)
    sub = ob.modifiers.new("Subdivision", "SUBSURF")
    sub.levels = sub.render_levels = 1
    ob.modifiers.move(len(ob.modifiers) - 1, 0)
    # dark carved-back bed: the closed carving silhouette from the bible (scroll_relief.npz), flat, in shadow
    d = np.load(HERE / "scroll_relief.npz")
    bed, u0, v0 = d["bed"], int(d["u0"]), int(d["v0"])
    H, W = bed.shape
    bm = bmesh.new()
    bv = {}
    st = 2
    for j in range(0, H, st):
        for i in range(0, W, st):
            if bed[j, i]:
                x, z = CAM.to_plane_y(u0 + i + 0.5, v0 + j + 0.5, SCROLL_BED_Y)
                bv[(i, j)] = bm.verts.new((x, SCROLL_BED_Y, z))
    for (i, j) in list(bv):
        q = [(i, j), (i, j + st), (i + st, j + st), (i + st, j)]
        if all(k in bv for k in q):
            bm.faces.new([bv[k] for k in q])
    loose = [v for v in bm.verts if not v.link_faces]
    bmesh.ops.delete(bm, geom=loose, context="VERTS")
    new_obj("aa_e4_keystone_scroll_bed", bm, [M["stone_shadow"]], C, smooth=False)
    FIT["curls"] = len(CURLS)
    return ob


def build_pipes(F, M, C):
    # left smooth black pipe: upper run, swan neck, lower run through (behind) the big box
    LP = T.LEFT_PIPE
    u0, v0 = LP["neck"][0]
    r = LP["w_px"] * px_scale(u0, v0, -0.1) / 2
    top, _ = F.cam_hit(*LP["neck"][0])
    bot, _ = F.cam_hit(*LP["neck"][1])
    gap = 0.03
    y_up = F.surf(top.x, top.z) - r - gap
    y_lo = F.surf(bot.x, bot.z + 0.4) - r - gap
    pts = [Vector((top.x, y_up, 13.0)), Vector((top.x, y_up, top.z)), Vector((bot.x, y_lo, bot.z)), Vector((bot.x, y_lo, 0.0))]
    bm = bmesh.new()
    sweep(bm, densify(fillet(pts, 0.25, 10), 0.04), r, 0, seg=24)
    for vy in LP["collars_px_y"]:
        p, _ = F.cam_hit(LP["lower_x_px"], vy)
        if p is not None:
            cyl(bm, Vector((bot.x, y_lo, p.z)), (0, 0, 1), r * 1.18, 0.05, 0, seg=24)
            box(bm, Vector((bot.x, (y_lo + F.surf(bot.x, p.z)) / 2, p.z)), (0.03, abs(F.surf(bot.x, p.z) - y_lo), 0.03), 1)
    new_obj("aa_e4_pipe_left", bm, [M["iron"], M["galv"]], C)
    # right cast-iron downspout: 1.8 m socketed lengths, flared bells, ribbed bracket bands
    DS = T.DOWNSPOUT
    p, _ = F.cam_hit(DS["x_px_top"], 1900)
    R = DS["w_px"] * px_scale(DS["x_px_top"], 1900, -0.15) / 2
    x = p.x
    wall = min(F.surf(x + dx, z) for dx in (-R * 0.5, 0, R * 0.5) for z in (2.0, 5.0, 8.0))
    y = wall - R - 0.02
    bm = bmesh.new()
    sweep(bm, [Vector((x, y, 0.05)), Vector((x, y, 13.2))], R, 0, seg=32)
    bells = [CAM_hit_z(F, DS["x_px_top"], vy) for vy in DS["bells_px_y"]]
    raw = sorted([b for b in bells if b] + [bells[0] + k * 1.8 for k in range(-3, 6)] if bells and bells[0] else [])
    zs = []
    for zb in raw:                                   # one socket per 1.8 m length; drop near-duplicates
        if not zs or zb - zs[-1] > 0.5:
            zs.append(zb)
    for zb in zs:
        if 0.3 < zb < 13.0:
            bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=R * 1.06, radius2=R * 1.3, depth=0.12,
                                  matrix=Matrix.Translation((x, y, zb - 0.06)))
            cyl(bm, Vector((x, y, zb + 0.021)), (0, 0, 1), R * 1.3, 0.04, 0, seg=32)
            # bracket band just below the bell, ears bolted to the wall
            zc = zb - 0.22
            cyl(bm, Vector((x, y, zc)), (0, 0, 1), R * 1.1, 0.05, 1, seg=32)
            for rib in (-0.0155, 0.0155):
                cyl(bm, Vector((x, y, zc + rib)), (0, 0, 1), R * 1.16, 0.0075, 1, seg=32)
            for sgn in (-1, 1):
                box(bm, Vector((x + sgn * (R * 1.1 + 0.02), (y + wall) / 2, zc)), (0.012, wall - y, 0.05), 1)
                cyl(bm, Vector((x + sgn * (R * 1.1 + 0.02), wall - 0.006, zc)), (0, 1, 0), 0.008, 0.008, 1, seg=8)
    bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=R * 1.35, radius2=R, depth=0.12,
                          matrix=Matrix.Translation((x, y, 0.1)))                       # shoe
    new_obj("aa_e4_downspout_right", bm, [M["iron"], M["galv"]], C)
    return x, wall


def CAM_hit_z(F, u, v):
    loc, _ = F.cam_hit(u, v)
    return loc.z if loc is not None else None


def build_plaque(F, M, C):
    u, v = T.PLAQUE["centre"]
    loc, _ = F.cam_hit(u, v)
    wall = F.surf(loc.x, loc.z)
    y = wall - 0.012
    sc = px_scale(u, v, y)
    w, h = T.PLAQUE["w_px"] * sc, T.PLAQUE["h_px"] * sc
    x, z = CAM.to_plane_y(u, v, y)
    bm = bmesh.new()
    box(bm, Vector((x, (wall + y) / 2, z)), (w, wall - y, h), 0)
    rr, hw, hh = 0.012, w * 0.42, h * 0.42            # rounded corners (bible)
    rect_o = []
    for cxs, czs, a0 in ((1, 1, 0), (-1, 1, 90), (-1, -1, 180), (1, -1, 270)):
        for k in range(7):
            a = math.radians(a0 + 15 * k)
            rect_o.append(Vector((x + cxs * (hw - rr) + rr * math.cos(a), y - 0.0015,
                                  z + czs * (hh - rr) + rr * math.sin(a))))
    rect_o = rect_o[::-1]
    decal_poly(bm, rect_o, 1, 0.002, ring=0.005)
    for sx in (-1, 1):
        for sz in (-1, 1):
            cyl(bm, Vector((x + sx * w * 0.47, y - 0.001, z + sz * h * 0.47)), (0, 1, 0), 0.004, 0.003, 1, seg=8)
    new_obj("aa_e4_plaque_13", bm, [M["plaque"], M["white"]], C, smooth=False)
    # the "13" (white serif)
    cu = bpy.data.curves.new("e4_13", "FONT")
    cu.body = "13"
    cu.font = bpy.data.fonts.load(str(FONT_SERIF), check_existing=True)
    cu.extrude = 0.5
    tmp = bpy.data.objects.new("e4_13_tmp", cu)
    C.objects.link(tmp)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(tmp.evaluated_get(dg))
    bpy.data.objects.remove(tmp)
    bpy.data.curves.remove(cu)
    xs = [vv.co.x for vv in me.vertices]
    ys = [vv.co.y for vv in me.vertices]
    zs = [vv.co.z for vv in me.vertices]
    th = h * 0.56
    s = th / (max(ys) - min(ys))
    cxm, cym = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    for vv in me.vertices:
        a, b, c = vv.co
        vv.co = (x + (a - cxm) * s, y - 0.0015 - (c - min(zs)) / (max(zs) - min(zs)) * 0.002, z + (b - cym) * s)
    me.materials.append(M["white"])
    uv_box(me)
    ob = bpy.data.objects.new("aa_e4_plaque_13_numerals", me)
    C.objects.link(ob)


def build_head_seat(C):
    """Clean seat for the Tripo v2 head: an empty marking keystone_head_bible and the proud range."""
    hs = T.HEAD_SEAT
    e = bpy.data.objects.get("aa_e4_head_seat") or bpy.data.objects.new("aa_e4_head_seat", None)
    if e.name not in C.objects:
        C.objects.link(e)
    e.empty_display_type = "CUBE"
    e.location = (hs["x"], -sum(hs["proud"]) / 4, (hs["z0"] + hs["z1"]) / 2)
    e.scale = (0.55, sum(hs["proud"]) / 4, (hs["z1"] - hs["z0"]) / 2)
    e["z_range"] = (hs["z0"], hs["z1"])
    e["proud_m"] = hs["proud"]
    e["note"] = "aa_keystone_head_v2.glb (Tripo, glazier) seats here; moustache as separate black geometry"


HEAD_PX = (3130, 1525, 3525, 2090)            # crown top .. goatee tip, hair to hair (bible px)
VOLUTE_R_PX = (3470, 1980, 3730, 2205)        # right cluster: inner edge on the jawline, top at mouth level
VOLUTE_L_PX = (2995, 1985, 3228, 2210)        # left cluster (mirrored + varied copy), same rule
HEAD_FRONT_Y, VOLUTE_FRONT_Y = -0.50, -0.42


def fit_to_px(ob, box_px, y_front, iters=5, by="mean"):
    """Uniform scale + x/z placement so the object's projection through aa_bible_cam fills box_px,
    front face on the plane y_front."""
    me = ob.data
    n = len(me.vertices)
    step = max(1, n // 4000)
    co = [me.vertices[i].co.copy() for i in range(0, n, step)]
    u0, v0, u1, v1 = box_px
    s = (v1 - v0) * px_scale((u0 + u1) / 2, (v0 + v1) / 2, y_front)       # unit-height mesh
    x, z = CAM.to_plane_y((u0 + u1) / 2, v1, y_front)
    for _ in range(iters):
        pts = [Vector((x + c.x * s, y_front + c.y * s, z + c.z * s)) for c in co]
        pr = [CAM.project(p) for p in pts]
        pu0, pu1 = min(p[0] for p in pr), max(p[0] for p in pr)
        pv0, pv1 = min(p[1] for p in pr), max(p[1] for p in pr)
        kw, kh = (u1 - u0) / (pu1 - pu0), (v1 - v0) / (pv1 - pv0)
        k = kh if by == "height" else 0.5 * (kw + kh)
        s *= k
        sc = px_scale((u0 + u1) / 2, (v0 + v1) / 2, y_front)
        x += (((u0 + u1) - (pu0 + pu1)) / 2) * sc
        z -= (((v0 + v1) - (pv0 + pv1)) / 2) * sc
    me.transform(Matrix.Translation((x, y_front, z)) @ Matrix.Scale(s, 4))
    me.update()
    return s


def cut_back(ob, y=0.0):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    r = bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], dist=1e-5,
                               plane_co=(0, y, 0), plane_no=(0, 1, 0), clear_outer=True)
    cut = [e for e in r["geom_cut"] if isinstance(e, bmesh.types.BMEdge)]
    if cut:
        bmesh.ops.holes_fill(bm, edges=cut, sides=0)
    bm.to_mesh(ob.data)
    bm.free()


LOWER_PX = (2980, 1940, 3740, 2235)     # glazier's crop: scroll clusters + pendant, the head removed
LOWER_FRONT_Y = -0.40
# bible outline of the jaw + goatee (bible px): the carving starts outside it, as in the bible
JAW_PX = [(3205, 1860), (3215, 1930), (3232, 1995), (3258, 2050), (3290, 2088), (3315, 2098), (3342, 2086), (3372, 2048),
          (3410, 1995), (3440, 1955), (3462, 1860)]     # up past the moustache tips
HEAD_EYE_WIDTH_RATIO = 280 / 565.0      # bible: face width at eye level / crown-to-goatee height
HEAD_EYE_LEVEL = 0.49                   # eye line, fraction of the head height from the goatee tip
LEAF_PX = [(3262, 2078), (3358, 2078), (3366, 2120), (3346, 2165), (3312, 2205), (3278, 2165), (3256, 2120)]
LEAF_Y = -0.36                           # carved tongue hanging under the goatee (bible), proud of the archivolt


def _catmull(pts, n=8):
    out = []
    m = len(pts)
    for k in range(m):
        p0, p1, p2, p3 = pts[k - 1], pts[k], pts[(k + 1) % m], pts[(k + 2) % m]
        for t in [i / n for i in range(n)]:
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 +
                              (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    return out


def build_underchin_leaf(M, C):
    """Simple carved leaf / drapery tongue hanging under the goatee: a smooth cushioned lens with a soft
    centre rib, its top tucked under the goatee tip."""
    outline = [Vector(CAM.to_plane_y(u, v, LEAF_Y)) for (u, v) in LEAF_PX]
    outline = _catmull(outline, 8)
    c = sum(outline, Vector((0.0, 0.0))) / len(outline)
    bm = bmesh.new()
    rings = []
    steps = 7
    for k in range(steps + 1):
        a = (PI / 2) * k / steps
        sc = math.cos(a) ** 0.8 if k < steps else 0.0
        dy = -0.055 * math.sin(a)
        rings.append([bm.verts.new(Vector((c.x + (p.x - c.x) * sc, LEAF_Y + 0.055 + dy, c.y + (p.y - c.y) * sc)))
                      for p in outline] if k < steps else [bm.verts.new(Vector((c.x, LEAF_Y + 0.055 + dy, c.y)))])
    n = len(outline)
    for k in range(steps - 1):
        for i_ in range(n):
            j_ = (i_ + 1) % n
            bm.faces.new((rings[k][i_], rings[k][j_], rings[k + 1][j_], rings[k + 1][i_]))
    for i_ in range(n):
        bm.faces.new((rings[steps - 1][i_], rings[steps - 1][(i_ + 1) % n], rings[steps][0]))
    back = [bm.verts.new(Vector((p.x, 0.0, p.y))) for p in outline]
    for i_ in range(n):
        j_ = (i_ + 1) % n
        bm.faces.new((back[i_], back[j_], rings[0][j_], rings[0][i_]))
    bm.faces.new(back[::-1])
    ob = new_obj("aa_e4_keystone_underchin_leaf", bm, [M["stone"]], C)
    rib = [Vector((c.x, LEAF_Y - 0.002, z)) for z in (c.y + 0.07, c.y, c.y - 0.08)]
    bm2 = bmesh.new()
    sweep(bm2, densify(fillet(rib, 0.03, 6), 0.01), 0.008, 0, seg=12)
    new_obj("aa_e4_keystone_underchin_rib", bm2, [M["stone"]], C)
    return ob


def unit_normalize(me):
    vs = [v.co for v in me.vertices]
    lo = Vector([min(v[i] for v in vs) for i in range(3)])
    hi = Vector([max(v[i] for v in vs) for i in range(3)])
    me.transform(Matrix.Scale(1.0 / (hi.z - lo.z), 4) @ Matrix.Translation((-(lo.x + hi.x) / 2, -lo.y, -lo.z)))
    me.update()


def face_camera(me, centre_world):
    """Turn the relief so its front looks at aa_bible_cam: the bible draws the head frontal although the
    camera is low and to the right, so a frontal carving read through the camera looks warped."""
    d = (Vector(CAM.loc) - Vector(centre_world)).normalized()
    q = Vector((0, -1, 0)).rotation_difference(d)
    c = Vector((0, 0.3, 0.5))
    me.transform(Matrix.Translation(c) @ q.to_matrix().to_4x4() @ Matrix.Translation(-c))
    me.update()
    return q


def narrow_to_bible(me):
    """x-scale so the face width at eye level / height matches the bible (unit mesh, front at y=0)."""
    band = [v.co for v in me.vertices if abs(v.co.z - HEAD_EYE_LEVEL) < 0.02 and v.co.y < 0.25]
    if not band:
        return 1.0
    w = max(v.x for v in band) - min(v.x for v in band)
    k = min(1.0, HEAD_EYE_WIDTH_RATIO / w)
    me.transform(Matrix.Diagonal((k, 1, 1, 1)))
    me.update()
    return k


def clean_and_decimate(ob, target_tris):
    """Collapse-decimate to the game budget (full mesh stays in tripo_raw), dissolve degenerates, recalc normals."""
    tris = sum(len(p.vertices) - 2 for p in ob.data.polygons)
    if tris > target_tris:
        md = ob.modifiers.new("Decimate", "DECIMATE")
        md.ratio = target_tris / tris
        md.use_collapse_triangulate = True
        dg = bpy.context.evaluated_depsgraph_get()
        me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
        old = ob.data
        ob.modifiers.clear()
        ob.data = me
        bpy.data.meshes.remove(old)
        me.name = ob.name
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    for _ in range(2):
        bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-5)
        bad = [f for f in bm.faces if f.calc_area() < 1e-10]
        if bad:
            bmesh.ops.delete(bm, geom=bad, context="FACES")
    loose = [v for v in bm.verts if not v.link_faces]
    if loose:
        bmesh.ops.delete(bm, geom=loose, context="VERTS")
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(ob.data)
    bm.free()
    ob.data.update()
    return sum(len(p.vertices) - 2 for p in ob.data.polygons)


def mirror_vary(src, name, C, roll, kx, kz):
    o = src.copy()
    o.data = src.data.copy()
    C.objects.link(o)
    o.name = o.data.name = name
    o.data.transform(Matrix.Rotation(math.radians(roll), 4, "Y") @ Matrix.Diagonal((-kx, 1, kz, 1)))
    bm = bmesh.new()
    bm.from_mesh(o.data)
    bmesh.ops.reverse_faces(bm, faces=bm.faces)
    bm.to_mesh(o.data)
    bm.free()
    unit_normalize(o.data)
    return o


def _in_poly(u, v, poly):
    inside = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > v) != (y2 > v) and u < x1 + (v - y1) * (x2 - x1) / (y2 - y1):
            inside = not inside
    return inside


def trim_inside_px(ob, poly):
    """Delete the geometry whose aa_bible_cam projection falls inside poly (bible px): the carving must
    meet the jaw and goatee, never run over the face."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    kill = [v for v in bm.verts if _in_poly(*CAM.project(v.co), poly)]
    bmesh.ops.delete(bm, geom=kill, context="VERTS")
    bm.to_mesh(ob.data)
    bm.free()
    return len(kill)


TEMPLE_PUSH = {"L": 0.0, "R": 0.10}   # m. L: the Tripo head's left cheek and temple are one surface at the same depth (pushing smears the face), so the L cup slides in instead


def widen_temples(head):
    """Push the side hair outward around each cup's height so the head reaches the bible's width at the
    temples and the cups can sit on the hair. Measured in bible px: each vertex's offset from the head's
    projected centre line at its own row, so only the outer hair moves (smooth falloff in height and width)."""
    me = head.data
    mw = head.matrix_world
    vs = [mw @ v.co for v in me.vertices]
    pr = [CAM.project(v) for v in vs]
    inv = mw.inverted()
    moved = {}
    for side, (F, yaw, pitch, r) in CUP_POSE.items():
        sg = -1.0 if side == "L" else 1.0
        vc = CAM.project(F)[1]
        row = [pu for (pu, pv) in pr if abs(pv - vc) < 15]
        uc = (min(row) + max(row)) / 2
        hw = (max(row) - min(row)) / 2
        n = 0
        nm = mw.to_3x3().inverted().transposed()
        for v, wv, (pu, pv) in zip(me.vertices, vs, pr):
            t = sg * (pu - uc) / hw
            if t < 0.55:
                continue
            side_w = max(0.0, sg * (nm @ v.normal).normalized().x)      # only surfaces facing outward (hair at
            if side_w < 0.15 or wv.y < -0.34:                         # the sides), never the frontal face or
                continue                                                # the cheeks (side hair lies deeper)
            fz = math.exp(-((pv - vc) / 110.0) ** 2)
            fx = min(1.0, (t - 0.55) / 0.35)
            fx = fx * fx * (3 - 2 * fx)
            push = TEMPLE_PUSH[side] * fz * fx * min(1.0, side_w * 1.6)
            if push > 1e-4:
                v.co = inv @ (wv + Vector((sg * push, 0, 0)))
                n += 1
        moved[side] = n
    me.update()
    FIT["temple_verts_L"], FIT["temple_verts_R"] = moved.get("L", 0), moved.get("R", 0)


def append_head(C):
    """Tripo v3 head + right volute (ingested by e4_ingest_head.py): decimated to the game budget, head
    narrowed to the bible's face proportion and turned to face aa_bible_cam, all fitted to their bible
    footprints; left volute = mirrored, varied copy; a third, turned-down copy is the leaf under the chin."""
    if not HEAD_BLEND.exists():
        return None, []
    with bpy.data.libraries.load(str(HEAD_BLEND), link=False) as (src, dst):
        dst.objects = [n for n in ("aa_e4_keystone_head",) if n in src.objects]
    head = vol = None
    for o in dst.objects:
        C.objects.link(o)
        if o.name.startswith("aa_e4_keystone_head"):
            head = o
        else:
            vol = o
    FIT.clear()
    if head:
        FIT["head_tris"] = clean_and_decimate(head, 420000)
        FIT["head_xscale"] = narrow_to_bible(head.data)
        x, z = CAM.to_plane_y((HEAD_PX[0] + HEAD_PX[2]) / 2, (HEAD_PX[1] + HEAD_PX[3]) / 2, HEAD_FRONT_Y)
        face_camera(head.data, (x, HEAD_FRONT_Y + 0.25, z))
        unit_normalize(head.data)
        FIT["head_scale"] = fit_to_px(head, HEAD_PX, HEAD_FRONT_Y, by="height")
        widen_temples(head)
        cut_back(head)
        clean_and_decimate(head, 10 ** 9)
    vols = []
    if vol:
        # the whole lower carving (both scroll clusters + the pendant under the goatee) as ONE piece,
        # fitted to its bible footprint so it meets the jaw and goatee
        FIT["lower_tris"] = clean_and_decimate(vol, 320000)
        vol.name = vol.data.name = "aa_e4_keystone_lower_carving"
        FIT["lower_scale"] = fit_to_px(vol, LOWER_PX, LOWER_FRONT_Y)
        FIT["lower_trimmed_verts"] = trim_inside_px(vol, JAW_PX)
        cut_back(vol)
        clean_and_decimate(vol, 10 ** 9)
        vols.append(vol)
    return head, vols


FIT = {}


MOUSTACHE_R = [(3290, 1952), (3320, 1955), (3345, 1964), (3362, 1961), (3371, 1946), (3364, 1934), (3354, 1937)]
GOATEE_PX = (3265, 2030, 3345, 2090)            # the goatee tip carries the faint green


def retone_head(head, M):
    """Even warm sandstone from the Tripo atlas's luminance (kills its baked dark mottling), normal map kept,
    faint green on the goatee as the bible shows."""
    old = head.data.materials[0]
    if old.name.startswith("m_e4_keystone_head_sandstone"):
        return
    imgs = [n.image for n in old.node_tree.nodes if n.type == "TEX_IMAGE" and n.image]
    base = next((i for i in imgs if i.colorspace_settings.name == "sRGB"), None)
    nrm = next((i for i in imgs if "normal" in i.name.lower()), None)
    m = bpy.data.materials.new("m_e4_keystone_head_sandstone" if "head" in head.name else
                               "m_e4_keystone_volute_sandstone")
    nt = m.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Roughness"].default_value = 0.78
    uv = nt.nodes.new("ShaderNodeUVMap")
    uv.uv_map = head.data.uv_layers[0].name
    t = nt.nodes.new("ShaderNodeTexImage")
    t.image = base
    nt.links.new(uv.outputs["UV"], t.inputs["Vector"])
    bw = nt.nodes.new("ShaderNodeRGBToBW")
    nt.links.new(t.outputs["Color"], bw.inputs["Color"])
    mr = nt.nodes.new("ShaderNodeMapRange")
    mr.inputs["From Min"].default_value = 0.12
    mr.inputs["From Max"].default_value = 0.62
    mr.inputs["To Min"].default_value = 0.45            # compress the baked shadows: the renderer shades it
    nt.links.new(bw.outputs["Val"], mr.inputs["Value"])
    tone = nt.nodes.new("ShaderNodeMix")
    tone.data_type = "RGBA"
    tone.inputs["A"].default_value = (*lin(150, 108, 70), 1)
    tone.inputs["B"].default_value = (*lin(226, 190, 146), 1)
    if "head" in head.name:
        # head: grade Tripo's own texture (keeps the painted black moustache), warm and lifted
        tone.blend_type = "MULTIPLY"
        tone.inputs["Factor"].default_value = 1.0
        nt.links.new(t.outputs["Color"], tone.inputs["A"])
        tone.inputs["B"].default_value = (1.25, 1.12, 1.0, 1)
    else:
        # volutes: their atlas bakes dark mottling, so tone from luminance into the bible's sandstone
        nt.links.new(mr.outputs["Result"], tone.inputs["Factor"])
    # goatee tint mask (world position box from the bible's goatee pixels on the face plane)
    x0, z1 = CAM.to_plane_y(GOATEE_PX[0], GOATEE_PX[1], -0.42)
    x1, z0 = CAM.to_plane_y(GOATEE_PX[2], GOATEE_PX[3], -0.42)
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(geo.outputs["Position"], sep.inputs[0])
    masks = []
    for comp, lo, hi in (("X", x0, x1), ("Z", z0, z1)):
        c, h = (lo + hi) / 2, abs(hi - lo) / 2
        sub = nt.nodes.new("ShaderNodeMath")
        sub.operation = "SUBTRACT"
        sub.inputs[1].default_value = c
        nt.links.new(sep.outputs[comp], sub.inputs[0])
        ab = nt.nodes.new("ShaderNodeMath")
        ab.operation = "ABSOLUTE"
        nt.links.new(sub.outputs[0], ab.inputs[0])
        r = nt.nodes.new("ShaderNodeMapRange")
        r.interpolation_type = "SMOOTHSTEP"
        r.inputs["From Min"].default_value = h
        r.inputs["From Max"].default_value = h * 0.55
        nt.links.new(ab.outputs[0], r.inputs["Value"])
        masks.append(r)
    mm = nt.nodes.new("ShaderNodeMath")
    mm.operation = "MULTIPLY"
    nt.links.new(masks[0].outputs["Result"], mm.inputs[0])
    nt.links.new(masks[1].outputs["Result"], mm.inputs[1])
    k = nt.nodes.new("ShaderNodeMath")
    k.operation = "MULTIPLY"
    k.inputs[1].default_value = 0.4
    nt.links.new(mm.outputs[0], k.inputs[0])
    tint = nt.nodes.new("ShaderNodeMix")
    tint.data_type = "RGBA"
    tint.blend_type = "MULTIPLY"
    tint.inputs["B"].default_value = (*lin(205, 222, 160), 1)
    nt.links.new(k.outputs[0], tint.inputs["Factor"])
    nt.links.new(tone.outputs["Result"], tint.inputs["A"])
    nt.links.new(tint.outputs["Result"], b.inputs["Base Color"])
    if nrm:
        tn = nt.nodes.new("ShaderNodeTexImage")
        tn.image = nrm
        nt.links.new(uv.outputs["UV"], tn.inputs["Vector"])
        nm = nt.nodes.new("ShaderNodeNormalMap")
        nm.uv_map = uv.uv_map
        nt.links.new(tn.outputs["Color"], nm.inputs["Color"])
        nt.links.new(nm.outputs["Normal"], b.inputs["Normal"])
    head.data.materials[0] = m


def build_moustache(head, M, C):
    """Black handlebar moustache as its own geometry, laid on the face along the bible's outline."""
    dg = bpy.context.evaluated_depsgraph_get()
    bm = bmesh.new()
    bm.from_object(head, dg)
    bm.transform(head.matrix_world)
    tree = BVHTree.FromBMesh(bm)
    bm.free()
    out = bmesh.new()
    for sgn in (1, -1):
        pts = []
        for (u, v) in MOUSTACHE_R:
            uu = 3290 + sgn * (u - 3290)
            loc, nrm, _, _ = tree.ray_cast(Vector(CAM.loc), Vector(CAM.ray(uu, v)).normalized(), 60)
            if loc is None:
                x, z = CAM.to_plane_y(uu, v, -0.45)
                loc, nrm = Vector((x, -0.45, z)), Vector((0, -1, 0))
            pts.append(loc - Vector(CAM.ray(uu, v)).normalized() * 0.012)
        r0 = 40 * px_scale(3290, 1952, -0.45) / 2        # bible: ~40 px thick at the philtrum
        L = sum((b - a).length for a, b in zip(pts, pts[1:]))
        sweep(out, densify(fillet(pts, 0.02, 6), 0.004), r0, 0, seg=14,
              rad_fn=lambda s, L=L: max(0.22, 1.0 - 0.8 * s / L))
    return new_obj("aa_e4_keystone_moustache", out, [M["moustache"]], C)


def orient_islands(bm):
    """Closed islands with negative signed volume are wound inside out (recalc misjudges tiny bevelled parts):
    reverse them."""
    bm.faces.index_update()
    seen = set()
    for f0 in list(bm.faces):
        if not f0.is_valid:
            continue
        if f0.index in seen:
            continue
        stack, isl = [f0], []
        seen.add(f0.index)
        while stack:
            f = stack.pop()
            isl.append(f)
            for e in f.edges:
                for g in e.link_faces:
                    if g.index not in seen:
                        seen.add(g.index)
                        stack.append(g)
        if not all(len(e.link_faces) == 2 for f in isl for e in f.edges):
            continue
        vol = sum(f.verts[0].co.dot(f.verts[i].co.cross(f.verts[i + 1].co))
                  for f in isl for i in range(1, len(f.verts) - 1)) / 6.0
        vs = {v for f in isl for v in f.verts}
        lo = Vector([min(v.co[i] for v in vs) for i in range(3)])
        hi = Vector([max(v.co[i] for v in vs) for i in range(3)])
        ext = hi - lo
        if max(ext) < 0.02 and abs(vol) < 0.15 * ext.x * ext.y * ext.z:     # only tiny screw heads
            # collapsed bevel output (a 6 mm screw head): replace with a clean cylinder of the same footprint
            mi = isl[0].material_index
            bmesh.ops.delete(bm, geom=list(vs), context="VERTS")
            r = bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=min(ext.x, ext.z) / 2,
                                      radius2=min(ext.x, ext.z) / 2, depth=ext.y,
                                      matrix=Matrix.Translation((lo + hi) / 2) @ Matrix.Rotation(PI / 2, 4, "X"))
            for f in {f for v in r["verts"] for f in v.link_faces}:
                f.material_index = mi
            bm.faces.index_update()
        elif vol < 0:
            bmesh.ops.reverse_faces(bm, faces=isl)


def finalize(cnames, skip=("aa_e4_keystone_head", "aa_e4_keystone_volute_r", "aa_e4_keystone_volute_l",
                           "aa_e4_keystone_volute_chin", "aa_e4_keystone_underchin_leaf",
                           "aa_e4_keystone_lower_carving", "aa_e4_keystone_curls_r", "aa_e4_keystone_curls_l")):
    """Apply modifiers, weld, dissolve degenerate bevel output, recalc normals (no visual change)."""
    dg = bpy.context.evaluated_depsgraph_get()
    for cname in cnames:
        for o in list(bpy.data.collections[cname].all_objects):
            if o.type != "MESH" or o.name in skip:
                continue
            if o.modifiers:
                me = bpy.data.meshes.new_from_object(o.evaluated_get(dg))
                old = o.data
                o.modifiers.clear()
                o.data = me
                if old.users == 0:
                    bpy.data.meshes.remove(old)
            bm = bmesh.new()
            bm.from_mesh(o.data)
            bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
            bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-6)
            loose = [v for v in bm.verts if not v.link_faces]
            if loose:
                bmesh.ops.delete(bm, geom=loose, context="VERTS")
            bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
            bm.to_mesh(o.data)
            bm.free()
            o.modifiers.new("WeightedNormal", "WEIGHTED_NORMAL").keep_sharp = True


def unwrap_bake_objs(obs):
    tmp = coll("e4_tmp_unwrap")
    for o in obs:
        tmp.objects.link(o)
    unwrap_bake(["e4_tmp_unwrap"])
    for o in obs:
        tmp.objects.unlink(o)
    bpy.data.collections.remove(tmp)


def unwrap_bake(cnames):
    for cname in cnames:
        obs = [o for o in bpy.data.collections[cname].all_objects if o.type == "MESH"]
        if not obs:
            continue
        for o in obs:
            o.data.uv_layers.active = o.data.uv_layers["uv_bake"]
            o.select_set(True)
        bpy.context.view_layer.objects.active = obs[0]
        with bpy.context.temp_override(active_object=obs[0], object=obs[0], selected_objects=obs,
                                       selected_editable_objects=obs):
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.002, scale_to_bounds=False)
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
    recess_keystone_context()
    F = Facade(STONE)
    conform_mural(F)
    mq = [o for o in bpy.data.objects if o.name.startswith("aa_e3_marquee_rim") or o.name == "aa_e3_marquee_board"]
    dg = bpy.context.evaluated_depsgraph_get()
    bm = bmesh.new()
    for o in mq:
        b2 = bmesh.new()
        b2.from_object(o, dg)
        b2.transform(o.matrix_world)
        tmp = bpy.data.meshes.new("tmp")
        b2.to_mesh(tmp)
        b2.free()
        bm.from_mesh(tmp)
        bpy.data.meshes.remove(tmp)
    mtree = BVHTree.FromBMesh(bm)
    bm.free()
    kit = coll("aa_kit")
    c_key = coll("aa_e4_keystone", kit)
    c_con = coll("aa_e4_conduits", kit)
    c_pip = coll("aa_e4_pipes", kit)
    c_plq = coll("aa_e4_plaque", kit)
    M = materials()
    build_head_seat(c_key)
    head, vols = append_head(c_key)
    for o in ([head] if head else []) + vols:
        retone_head(o, M)
    # (the simple under-chin leaf is superseded by the Tripo lower carving's own pendant)
    # the v3 head's own painted moustache reads solid black once the texture keeps it: no extra geometry
    curls = append_curls(c_key)                 # Tripo clusters replace the modelled scrolls and their bed
    for o in curls:
        retone_head(o, M)
    # (left hair locks dropped, coordinator round 3: the left cup's inner rim overlaps the head's edge instead)
    build_headphones(M, c_key)
    build_boxes(F, M, c_con)
    build_conduits(F, M, c_con)
    build_green(F, M, c_con, mtree)
    build_marquee_neon(M, c_con)
    xr, wr = build_pipes(F, M, c_pip)
    build_plaque(F, M, c_plq)
    finalize(["aa_e4_keystone", "aa_e4_conduits", "aa_e4_pipes", "aa_e4_plaque"])
    unwrap_bake(["aa_e4_conduits", "aa_e4_pipes", "aa_e4_plaque"])
    unwrap_bake_objs([o for o in c_key.objects if o.type == "MESH"])   # fresh uv_bake incl. decimated Tripo pieces
    print("E4 FIT", {k: (round(v, 4) if isinstance(v, (int, float)) else v) for k, v in FIT.items()})
    print("E4 BUILD objects", len(bpy.data.objects), "downspout x", round(xr, 3), "wall", round(wr, 3),
          "boxes", {k: tuple(round(a, 3) for a in v) for k, v in BOX_GEOM.items()})
    if "--no-save" not in args:
        WIP.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(WIP))
        print("saved", WIP)


main()
