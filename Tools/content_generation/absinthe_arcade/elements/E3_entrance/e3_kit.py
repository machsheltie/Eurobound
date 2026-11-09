"""E3 shared kit: depth planes, material factories, the bmesh builder and mesh helpers.

Imported by e3_build.py, e3_doorway.py, e3_interior.py and e3_marquee2.py (runs inside Blender).
"""
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
import e3_layout as L  # noqa: E402

FONT_DIR = Path("C:/Windows/Fonts")
F_SLOGAN = FONT_DIR / "segoeui.ttf"      # bahnschrift is a variable font: overlapping contours
F_SIGN = FONT_DIR / "ARIALN.TTF"
F_GAME = FONT_DIR / "ARIALNB.TTF"

# ---- depth planes (Blender Y, metres; negative = toward the street) -----------------------
Y_BOARD_F, Y_BOARD_B = -0.30, -0.20          # marquee board
Y_RIM_F = -0.355                             # raised rim tube
Y_LET_F = -0.52                              # letter fronts (letters run back to the board)
Y_STUD = 0.035                               # pixel studs stand proud of the board
Y_BANNER_F, Y_BANNER_B = -0.43, -0.31
Y_TYMP_F, Y_TYMP_B = 0.03, 0.09             # arched casing filling the arch head, inside the opening
Y_FRAME_F, Y_FRAME_B = 0.03, 0.30            # fixed outer frames, inside the masonry opening
Y_HINGE = 0.20                               # door hinge line
Y_INT0 = 0.34                                # interior starts
Y_LEDGE_F = -0.36

L.use("door", 0.0)
STEP_Z = L.mz(2215)                          # top of the threshold step
ARCH = L.ARCH


# =========================================================================================
# helpers
# =========================================================================================
def coll(name, parent=None):
    c = bpy.data.collections.get(name) or bpy.data.collections.new(name)
    p = parent or bpy.context.scene.collection
    if c.name not in [x.name for x in p.children]:
        p.children.link(c)
    return c


MATS = {}


def lin(r, g, b):
    """sRGB 0-255 (sampled off the bible crop) -> linear."""
    def c(v):
        v /= 255.0
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return (c(r), c(g), c(b))


def glow(name, srgb, estr=0.9, base_k=0.25, rough=0.35):
    """Self-lit colour: emission carries the bible colour, a dim base takes the daylight."""
    col = lin(*srgb)
    return mat(name, tuple(x * base_k for x in col), rough=rough, emit=col, estr=estr)


def _principled(m):
    return next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")


def mat(name, base=(0.05, 0.05, 0.05), rough=0.5, metal=0.0, emit=None, estr=0.0, coat=0.0):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        if n.type not in ("BSDF_PRINCIPLED", "OUTPUT_MATERIAL"):
            nt.nodes.remove(n)
    b = _principled(m)
    b.inputs["Base Color"].default_value = (*base, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if coat:
        b.inputs["Coat Weight"].default_value = coat
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = estr
    m.diffuse_color = (*base, 1)
    MATS[name] = m
    return m


def img(path, noncolor=False):
    im = bpy.data.images.load(str(path), check_existing=True)
    if noncolor:
        im.colorspace_settings.name = "Non-Color"
    return im


def tex_node(m, image, uv="uv_material", scale=None, interp="Linear"):
    nt = m.node_tree
    t = nt.nodes.new("ShaderNodeTexImage")
    t.image = image
    t.interpolation = interp
    u = nt.nodes.new("ShaderNodeUVMap")
    u.uv_map = uv
    if scale:
        mp = nt.nodes.new("ShaderNodeMapping")
        mp.inputs["Scale"].default_value = (scale, scale, 1)
        nt.links.new(u.outputs["UV"], mp.inputs["Vector"])
        nt.links.new(mp.outputs["Vector"], t.inputs["Vector"])
    else:
        nt.links.new(u.outputs["UV"], t.inputs["Vector"])
    return t


def mat_led(name, base, emit, estr, side_note=""):
    """Letter face: emissive colour broken up by a square-LED grid (normal + brightness)."""
    if name in MATS:
        return MATS[name]
    m = mat(name, base, rough=0.35, emit=emit, estr=estr)
    nt = m.node_tree
    b = _principled(m)
    led_scale = 1.0 / (16 * 0.0246)               # 16 LEDs per tile, 24.6 mm pitch
    tn = tex_node(m, img(L.TEX / "e3_led_normal.png", True), scale=led_scale)
    nm = nt.nodes.new("ShaderNodeNormalMap")
    nm.uv_map = "uv_material"
    nm.inputs["Strength"].default_value = 1.0
    nt.links.new(tn.outputs["Color"], nm.inputs["Color"])
    nt.links.new(nm.outputs["Normal"], b.inputs["Normal"])
    th = tex_node(m, img(L.TEX / "e3_led_height.png", True), scale=led_scale)
    ramp = nt.nodes.new("ShaderNodeMapRange")
    ramp.inputs["To Min"].default_value = 0.35
    ramp.inputs["To Max"].default_value = 1.0
    nt.links.new(th.outputs["Color"], ramp.inputs["Value"])
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    mul.inputs[1].default_value = estr
    nt.links.new(ramp.outputs["Result"], mul.inputs[0])
    nt.links.new(mul.outputs["Value"], b.inputs["Emission Strength"])
    return m


def mat_image(name, path, rough=0.4, estr=0.0, mask=None, base_mult=1.0, alpha_from=None):
    """Image base colour; optional emission = image * strength (masked)."""
    if name in MATS:
        return MATS[name]
    m = mat(name, rough=rough)
    nt = m.node_tree
    b = _principled(m)
    t = tex_node(m, img(path))
    if base_mult != 1.0:
        mm = nt.nodes.new("ShaderNodeMix")
        mm.data_type = "RGBA"
        mm.blend_type = "MULTIPLY"
        mm.inputs["Factor"].default_value = 1.0
        nt.links.new(t.outputs["Color"], mm.inputs["A"])
        mm.inputs["B"].default_value = (base_mult, base_mult, base_mult, 1)
        nt.links.new(mm.outputs["Result"], b.inputs["Base Color"])
    else:
        nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
    if estr:
        nt.links.new(t.outputs["Color"], b.inputs["Emission Color"])
        if mask:
            mt = tex_node(m, img(mask, True))
            mul = nt.nodes.new("ShaderNodeMath")
            mul.operation = "MULTIPLY"
            mul.inputs[1].default_value = estr
            nt.links.new(mt.outputs["Color"], mul.inputs[0])
            nt.links.new(mul.outputs["Value"], b.inputs["Emission Strength"])
        else:
            b.inputs["Emission Strength"].default_value = estr
    return m


def mat_mask_emit(name, mask_path, dark=(0.02, 0.02, 0.02), col=(0.5, 0.85, 0.2), estr=3.0, invert=False):
    """Emissive line art from a mask: col where mask is white, dark elsewhere."""
    if name in MATS:
        return MATS[name]
    m = mat(name, dark, rough=0.4)
    nt = m.node_tree
    b = _principled(m)
    t = tex_node(m, img(mask_path, True))
    src = t.outputs["Color"]
    if invert:
        inv = nt.nodes.new("ShaderNodeInvert")
        nt.links.new(src, inv.inputs["Color"])
        src = inv.outputs["Color"]
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    nt.links.new(src, mix.inputs["Factor"])
    mix.inputs["A"].default_value = (*dark, 1)
    mix.inputs["B"].default_value = (*col, 1)
    nt.links.new(mix.outputs["Result"], b.inputs["Base Color"])
    b.inputs["Emission Color"].default_value = (*col, 1)
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    mul.inputs[1].default_value = estr
    nt.links.new(src, mul.inputs[0])
    nt.links.new(mul.outputs["Value"], b.inputs["Emission Strength"])
    return m


class MB:
    """bmesh accumulator -> one object, multi-material, box-projected uv_material + uv_bake."""

    def __init__(self, jitter=True):
        self.jitter = jitter
        self.nbox = 0
        self.bm = bmesh.new()
        self.mats = []
        self.uvbox = {}          # material index -> (x0, x1, z0, z1): front faces get 0..1 UVs

    def mi(self, m):
        if m not in self.mats:
            self.mats.append(m)
        return self.mats.index(m)

    def _faces(self, faces, m):
        i = self.mi(m)
        for f in faces:
            f.material_index = i
        return faces

    def box(self, x0, x1, y0, y1, z0, z1, m):
        bm = self.bm
        x0, x1 = sorted((x0, x1))
        y0, y1 = sorted((y0, y1))
        z0, z1 = sorted((z0, z1))
        if self.jitter:                       # 0..4.8 mm, never visible, keeps boxes off each other's planes
            j = 0.0011 * (self.nbox % 7)
            x0, x1, y0, y1, z0, z1 = x0 - j, x1 + j, y0 - j * 0.5, y1 + j, z0 - j, z1 + j
        self.nbox += 1
        v = [bm.verts.new(p) for p in [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
                                        (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]]
        idx = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
        return self._faces([bm.faces.new([v[a] for a in q]) for q in idx], m)

    def prism(self, pts, y0, y1, m, m_side=None):
        """Polygon in XZ (any winding) extruded from y0 (front) to y1 (back)."""
        bm = self.bm
        if _area(pts) > 0:      # make the front face point -Y
            pts = pts[::-1]
        vf = [bm.verts.new((x, y0, z)) for x, z in pts]
        vb = [bm.verts.new((x, y1, z)) for x, z in pts]
        f = bm.faces.new(vf)
        b = bm.faces.new(vb[::-1])
        n = len(pts)
        sides = [bm.faces.new((vf[(k + 1) % n], vf[k], vb[k], vb[(k + 1) % n])) for k in range(n)]
        self._faces([f], m)
        self._faces([b], m_side or m)
        self._faces(sides, m_side or m)
        return f

    def ring(self, outer, inner, y0, y1, m):
        """Closed band between two polygons with matching vertex counts (XZ), extruded in Y."""
        bm = self.bm
        if _area(outer) > 0:
            outer, inner = outer[::-1], inner[::-1]
        n = len(outer)
        of = [bm.verts.new((x, y0, z)) for x, z in outer]
        inf = [bm.verts.new((x, y0, z)) for x, z in inner]
        ob = [bm.verts.new((x, y1, z)) for x, z in outer]
        ib = [bm.verts.new((x, y1, z)) for x, z in inner]
        fs = []
        for k in range(n):
            j = (k + 1) % n
            fs.append(bm.faces.new((of[k], of[j], inf[j], inf[k])))      # front
            fs.append(bm.faces.new((ob[j], ob[k], ib[k], ib[j])))        # back
            fs.append(bm.faces.new((of[j], of[k], ob[k], ob[j])))        # outer side
            fs.append(bm.faces.new((inf[k], inf[j], ib[j], ib[k])))      # inner side
        self._faces(fs, m)
        bmesh.ops.recalc_face_normals(bm, faces=fs)

    def seg(self, p0, p1, w, y0, y1, m):
        """Thin bar along an XZ segment."""
        (x0, z0), (x1, z1) = p0, p1
        dx, dz = x1 - x0, z1 - z0
        ln = math.hypot(dx, dz) or 1e-6
        nx, nz = -dz / ln * w / 2, dx / ln * w / 2
        ex, ez = dx / ln * w / 2, dz / ln * w / 2      # extend so joints overlap
        pts = [(x0 - ex + nx, z0 - ez + nz), (x1 + ex + nx, z1 + ez + nz),
               (x1 + ex - nx, z1 + ez - nz), (x0 - ex - nx, z0 - ez - nz)]
        self.prism(pts, y0, y1, m)

    def cells(self, cells, y0, y1, m_front, m_side):
        """Union of axis-aligned XZ squares (x0, x1, z0, z1) -> one extruded solid."""
        bm = self.bm
        key = {}

        def V(x, z):
            k = (round(x, 5), round(z, 5))
            if k not in key:
                key[k] = bm.verts.new((x, y0, z))
            return key[k]
        faces = []
        for (x0, x1, z0, z1) in cells:
            faces.append(bm.faces.new((V(x0, z0), V(x0, z1), V(x1, z1), V(x1, z0))))
        self._faces(faces, m_front)
        ret = bmesh.ops.extrude_face_region(bm, geom=faces)
        newv = [e for e in ret["geom"] if isinstance(e, bmesh.types.BMVert)]
        bmesh.ops.translate(bm, verts=newv, vec=(0, y1 - y0, 0))
        side = self.mi(m_side)
        newf = [e for e in ret["geom"] if isinstance(e, bmesh.types.BMFace)]
        for f in bm.faces:
            if f not in faces:
                f.material_index = side if f.material_index == self.mi(m_front) and f in newf else f.material_index
        for f in newf:
            f.material_index = side
        # side walls created by the extrude
        for f in bm.faces:
            if f not in faces and abs(f.normal.y) < 0.5:
                f.material_index = side
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        return faces

    def transform(self, mtx, verts=None):
        bmesh.ops.transform(self.bm, matrix=mtx, verts=list(verts or self.bm.verts))

    def finish(self, name, collection, bevel=0.0, smooth=False, uv_scale=1.0, segments=2, weld=True):
        me = bpy.data.meshes.new(name)
        if weld:
            bmesh.ops.remove_doubles(self.bm, verts=self.bm.verts, dist=1e-5)
        bmesh.ops.recalc_face_normals(self.bm, faces=self.bm.faces)
        self.bm.to_mesh(me)
        self.bm.free()
        for m in self.mats:
            me.materials.append(m)
        _uv(me, self.uvbox, uv_scale)
        ob = bpy.data.objects.get(name)
        if ob:
            bpy.data.objects.remove(ob)
        ob = bpy.data.objects.new(name, me)
        collection.objects.link(ob)
        if bevel:
            md = ob.modifiers.new("Bevel", "BEVEL")
            md.width = bevel
            md.segments = segments
            md.limit_method = "ANGLE"
            md.angle_limit = math.radians(30)
            md.use_clamp_overlap = True
            md.harden_normals = True
            smooth = True
        if smooth:
            me.shade_smooth()
        return ob


def _area(pts):
    return 0.5 * sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
                     for i in range(len(pts)))


def _uv(me, uvbox, scale):
    """uv_material: metric box projection (or 0..1 over uvbox for -Y faces of listed materials);
    uv_bake: the same, normalised into 0..1 over the mesh bounds (non-overlap not guaranteed)."""
    while me.uv_layers:
        me.uv_layers.remove(me.uv_layers[0])
    uvm = me.uv_layers.new(name="uv_material")
    uvb = me.uv_layers.new(name="uv_bake")
    co = [v.co for v in me.vertices]
    if not co:
        return
    lo = Vector((min(c.x for c in co), min(c.y for c in co), min(c.z for c in co)))
    hi = Vector((max(c.x for c in co), max(c.y for c in co), max(c.z for c in co)))
    span = hi - lo
    s = max(span.x, span.y, span.z, 1e-6)
    for p in me.polygons:
        n = p.normal
        box = uvbox.get(p.material_index)
        for li in p.loop_indices:
            c = me.vertices[me.loops[li].vertex_index].co
            if box and n.y < -0.5:
                x0, x1, z0, z1 = box
                uvm.data[li].uv = ((c.x - x0) / (x1 - x0), (c.z - z0) / (z1 - z0))
            elif abs(n.y) >= max(abs(n.x), abs(n.z)):
                uvm.data[li].uv = (c.x * scale, c.z * scale)
            elif abs(n.x) >= abs(n.z):
                uvm.data[li].uv = (c.y * scale, c.z * scale)
            else:
                uvm.data[li].uv = (c.x * scale, c.y * scale)
            if abs(n.y) >= max(abs(n.x), abs(n.z)):
                a, b = c.x - lo.x, c.z - lo.z
            elif abs(n.x) >= abs(n.z):
                a, b = c.y - lo.y, c.z - lo.z
            else:
                a, b = c.x - lo.x, c.y - lo.y
            uvb.data[li].uv = (min(max(a / s, 0), 1), min(max(b / s, 0), 1))


def plane(name, collection, x0, x1, z0, z1, y, m, rot=None, pivot=None):
    """Vertical quad facing -Y with 0..1 UVs (textures map exactly)."""
    mb = MB()
    mb.uvbox[mb.mi(m)] = (min(x0, x1), max(x0, x1), min(z0, z1), max(z0, z1))
    bm = mb.bm
    v = [bm.verts.new(p) for p in [(x0, y, z0), (x1, y, z0), (x1, y, z1), (x0, y, z1)]]
    f = bm.faces.new(v)
    f.material_index = 0
    f.normal_update()
    if f.normal.y > 0:
        f.normal_flip()
    ob = mb.finish(name, collection)
    return ob


def text_obj(name, collection, body, font, m, x0, x1, ztop, zbot, y_front, depth, fit=True, spacing=1.0,
             uniform=False):
    """Text mesh facing -Y, scaled to fill the traced box (x0..x1, zbot..ztop)."""
    cu = bpy.data.curves.new(name + "_crv", "FONT")
    cu.body = body
    cu.font = bpy.data.fonts.load(str(font), check_existing=True)
    cu.size = 1.0
    cu.extrude = 0.5
    cu.align_x = "LEFT"
    cu.space_character = spacing
    tmp = bpy.data.objects.new(name + "_tmp", cu)
    collection.objects.link(tmp)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(tmp.evaluated_get(dg))
    bpy.data.objects.remove(tmp)
    bpy.data.curves.remove(cu)
    # text lies in XY with depth in Z: map to XZ facing -Y
    xs = [v.co.x for v in me.vertices]
    ys = [v.co.y for v in me.vertices]
    zs = [v.co.z for v in me.vertices]
    bx0, bx1, by0, by1, bz0, bz1 = min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)
    sx = (x1 - x0) / (bx1 - bx0)
    sz = (ztop - zbot) / (by1 - by0)
    if uniform:                      # keep the glyph's proportions, centre it in x0..x1
        sx = sz
        x0 = (x0 + x1) / 2 - (bx1 - bx0) * sx / 2
    for v in me.vertices:
        x, yv, zv = v.co
        nx = x0 + (x - bx0) * sx
        nz = zbot + (yv - by0) * sz
        ny = y_front + (bz1 - zv) / (bz1 - bz0) * depth
        v.co = (nx, ny, nz)
    me.update()
    me.materials.append(m)
    _uv(me, {}, 1.0)
    ob = bpy.data.objects.get(name)
    if ob:
        bpy.data.objects.remove(ob)
    ob = bpy.data.objects.new(name, me)
    collection.objects.link(ob)
    # flip check (mirror in mapping can invert winding)
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()
    return ob


def join_objects(obs, name):
    """Merge mesh objects (same collection) into one object called name."""
    bm = bmesh.new()
    mats = []
    for o in obs:
        me = o.data
        for mt in me.materials:
            if mt not in mats:
                mats.append(mt)
        remap = [mats.index(mt) for mt in me.materials]
        tmp = bmesh.new()
        tmp.from_mesh(me)
        for f in tmp.faces:
            f.material_index = remap[f.material_index] if remap else 0
        tmp.to_mesh(me)
        tmp.free()
        bm.from_mesh(me)
    coll_ = obs[0].users_collection[0]
    for o in obs:
        me = o.data
        bpy.data.objects.remove(o)
        bpy.data.meshes.remove(me)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    for mt in mats:
        me.materials.append(mt)
    _uv(me, {}, 1.0)
    ob = bpy.data.objects.new(name, me)
    coll_.objects.link(ob)
    return ob


def tube(name, collection, pts, radius, m, cyclic=False, res=6):
    """Curve tube through 3D points -> mesh."""
    cu = bpy.data.curves.new(name + "_crv", "CURVE")
    cu.dimensions = "3D"
    cu.bevel_depth = radius
    cu.bevel_resolution = 2
    sp = cu.splines.new("POLY")
    sp.points.add(len(pts) - 1)
    for p, c in zip(sp.points, pts):
        p.co = (*c, 1)
    sp.use_cyclic_u = cyclic
    cu.use_fill_caps = True
    tmp = bpy.data.objects.new(name + "_tmp", cu)
    collection.objects.link(tmp)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(tmp.evaluated_get(dg))
    bpy.data.objects.remove(tmp)
    bpy.data.curves.remove(cu)
    me.materials.append(m)
    _uv(me, {}, 1.0)
    ob = bpy.data.objects.get(name)
    if ob:
        bpy.data.objects.remove(ob)
    ob = bpy.data.objects.new(name, me)
    collection.objects.link(ob)
    me.shade_smooth()
    return ob


def polyline_outline(pts, w):
    """Open polyline -> closed outline polygon of width w (mitred joints, square ends)."""
    def nrm(a, b):
        d = (Vector(b) - Vector(a)).normalized()
        return d, Vector((-d.y, d.x))
    left, right = [], []
    n = len(pts)
    for i in range(n):
        p = Vector(pts[i])
        if i == 0:
            d, nn = nrm(pts[0], pts[1])
            p = p - d * w / 2
            off = nn * w / 2
        elif i == n - 1:
            d, nn = nrm(pts[-2], pts[-1])
            p = p + d * w / 2
            off = nn * w / 2
        else:
            _, n0 = nrm(pts[i - 1], pts[i])
            _, n1 = nrm(pts[i], pts[i + 1])
            b = (n0 + n1).normalized()
            off = b * (w / 2) / max(b.dot(n0), 0.3)
        left.append(tuple(p + off))
        right.append(tuple(p - off))
    return left + right[::-1]


def offset_poly(pts, d):
    """Miter offset of a closed polygon; positive d moves edges inward."""
    n = len(pts)
    sgn = 1 if _area(pts) > 0 else -1
    out = []
    for i in range(n):
        p0, p1, p2 = Vector(pts[i - 1]), Vector(pts[i]), Vector(pts[(i + 1) % n])
        e0, e1 = (p1 - p0).normalized(), (p2 - p1).normalized()
        n0 = Vector((-e0.y, e0.x)) * sgn
        n1 = Vector((-e1.y, e1.x)) * sgn
        bis = (n0 + n1)
        if bis.length < 1e-6:
            bis = n0
        bis.normalize()
        cosh = max(bis.dot(n0), 0.3)
        q = p1 + bis * (d / cosh)
        out.append((q.x, q.y))
    return out


def arc_pts(cx, cz, r, a0, a1, n):
    return [(cx + r * math.cos(a0 + (a1 - a0) * k / n), cz + r * math.sin(a0 + (a1 - a0) * k / n))
            for k in range(n + 1)]


def spiral(cx, cz, r, turns, n=40, a0=0.0, sign=1):
    return [(cx + r * (k / n) * math.cos(a0 + sign * 2 * math.pi * turns * k / n),
             cz + r * (k / n) * math.sin(a0 + sign * 2 * math.pi * turns * k / n)) for k in range(n + 1)]


# =========================================================================================
# materials
# =========================================================================================
