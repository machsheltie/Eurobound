"""E2 window set: mesh-building helpers and materials (runs inside Blender 5.2).

Space: Blender metres, Z up, street side -Y, facade front plane y = 0.
Every kit asset is authored at the origin with the `sill` pivot:
bottom centre of the window opening, on the facade front plane.
"""
import math
import random

import bmesh
import bpy
import numpy as np
from mathutils import Matrix, Vector

TEX_DIR = None  # set by build script (Path to absinthearcade/textures)


# --------------------------------------------------------------------------------------
# Mesh builder
# --------------------------------------------------------------------------------------
class MB:
    """Accumulates verts/faces with a material slot name per face."""

    def __init__(self):
        self.v = []
        self.f = []
        self.m = []
        self.leaf_uv = {}  # face index -> list of (u, v) per corner (explicit UVs)
        self.parts = []    # (first_vert, end_vert) per add() call: welding stays inside a part

    def add(self, verts, faces, mat, uvs=None):
        o = len(self.v)
        self.v.extend([tuple(map(float, p)) for p in verts])
        self.parts.append((o, len(self.v)))
        for i, fc in enumerate(faces):
            self.f.append([o + k for k in fc])
            self.m.append(mat)
            if uvs is not None:
                self.leaf_uv[len(self.f) - 1] = uvs[i]
        return o

    def merge(self, other, mat_map=None, xform=None):
        o = len(self.v)
        vs = other.v
        if xform is not None:
            vs = [tuple(xform @ Vector(p)) for p in vs]
        self.v.extend(vs)
        base = len(self.f)
        for fc, mm in zip(other.f, other.m):
            self.f.append([o + k for k in fc])
            self.m.append(mat_map.get(mm, mm) if mat_map else mm)
        for k, uv in other.leaf_uv.items():
            self.leaf_uv[base + k] = uv
        self.parts.extend([(a + o, b + o) for a, b in other.parts])

    def transform(self, mat):
        self.v = [tuple(mat @ Vector(p)) for p in self.v]
        return self

    # ---- primitives ------------------------------------------------------------------
    def box(self, lo, hi, mat):
        x0, y0, z0 = lo
        x1, y1, z1 = hi
        vs = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
              (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
        fs = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
        return self.add(vs, fs, mat)

    def prism_x(self, prof, x0, x1, mat, cap=True):
        """Closed 2D profile [(y, z)...] extruded along X from x0 to x1."""
        n = len(prof)
        vs = [(x0, y, z) for y, z in prof] + [(x1, y, z) for y, z in prof]
        fs = [(i, (i + 1) % n, n + (i + 1) % n, n + i) for i in range(n)]
        if cap:
            fs.append(tuple(reversed(range(n))))
            fs.append(tuple(range(n, 2 * n)))
        return self.add(vs, fs, mat)

    def prism_y(self, prof, y0, y1, mat, cap=True):
        """Closed 2D profile [(x, z)...] extruded along Y (a flat cut-out shape)."""
        n = len(prof)
        vs = [(x, y0, z) for x, z in prof] + [(x, y1, z) for x, z in prof]
        fs = [(i, (i + 1) % n, n + (i + 1) % n, n + i) for i in range(n)]
        if cap:
            fs.append(tuple(reversed(range(n))))
            fs.append(tuple(range(n, 2 * n)))
        return self.add(vs, fs, mat)

    def sweep(self, path, prof, mat, normal=(0, -1, 0), closed=False, cap=True):
        """Sweep a closed profile [(d, p)] along a planar polyline `path` (Vectors).

        d = in-plane offset to the LEFT of travel direction (mitred), p = offset along `normal`.
        """
        N = Vector(normal).normalized()
        P = [Vector(p) for p in path]
        n = len(P)
        segs = n if closed else n - 1
        dirs = [(P[(i + 1) % n] - P[i]).normalized() for i in range(segs)]
        lefts = [N.cross(d).normalized() for d in dirs]
        rings = []
        for i in range(n):
            if closed:
                a, b = lefts[i - 1], lefts[i % segs]
            else:
                a = lefts[max(i - 1, 0)]
                b = lefts[min(i, segs - 1)]
            m = (a + b)
            m = m.normalized() if m.length > 1e-9 else a
            k = 1.0 / max(m.dot(a), 0.2)
            rings.append([P[i] + m * (d * k) + N * pp for d, pp in prof])
        np_ = len(prof)
        vs = [tuple(v) for r in rings for v in r]
        fs = []
        rn = n if closed else n - 1
        for i in range(rn):
            i2 = (i + 1) % n
            for j in range(np_):
                j2 = (j + 1) % np_
                fs.append((i * np_ + j, i * np_ + j2, i2 * np_ + j2, i2 * np_ + j))
        if cap and not closed:
            fs.append(tuple(range(np_)))
            fs.append(tuple(reversed(range((n - 1) * np_, n * np_))))
        return self.add(vs, fs, mat)

    def lathe(self, prof, seg, mat, center=(0, 0, 0), cap_bottom=True, cap_top=False, sx=1.0, sy=1.0):
        """Revolve [(r, z)] about Z. Profile runs bottom -> top along the outside."""
        cx, cy, cz = center
        n = len(prof)
        vs = []
        for s in range(seg):
            a = 2 * math.pi * s / seg
            ca, sa = math.cos(a), math.sin(a)
            for r, z in prof:
                vs.append((cx + r * ca * sx, cy + r * sa * sy, cz + z))
        fs = []
        for s in range(seg):
            s2 = (s + 1) % seg
            for j in range(n - 1):
                fs.append((s * n + j, s2 * n + j, s2 * n + j + 1, s * n + j + 1))
        if cap_bottom:
            fs.append(tuple(reversed([s * n for s in range(seg)])))
        if cap_top:
            fs.append(tuple(s * n + n - 1 for s in range(seg)))
        return self.add(vs, fs, mat)

    def tube(self, pts, r, mat, sides=6, cap=True, r_end=None, closed=False, roll=0.37):
        # roll default 0.37 rad: no tube face is axis-aligned, so crossing bars never share a plane
        """Tube along a 3D polyline, parallel-transported frames."""
        P = [Vector(p) for p in pts]
        n = len(P)
        if n < 2:
            return
        tans = []
        for i in range(n):
            if closed:
                t = P[(i + 1) % n] - P[i - 1]
            elif i == 0:
                t = P[1] - P[0]
            elif i == n - 1:
                t = P[-1] - P[-2]
            else:
                t = P[i + 1] - P[i - 1]
            tans.append(t.normalized() if t.length > 1e-9 else Vector((0, 0, 1)))
        up = Vector((0, 0, 1)) if abs(tans[0].z) < 0.9 else Vector((1, 0, 0))
        nrm = tans[0].cross(up).normalized()
        if roll:
            nrm = Matrix.Rotation(roll, 3, tans[0]) @ nrm
        frames = []
        for i in range(n):
            if i > 0:
                nrm = nrm - tans[i] * nrm.dot(tans[i])
                if nrm.length < 1e-9:
                    nrm = tans[i].orthogonal()
                nrm.normalize()
            frames.append((nrm.copy(), tans[i].cross(nrm).normalized()))
        vs = []
        for i in range(n):
            rr = r if r_end is None else r + (r_end - r) * i / (n - 1)
            a_, b_ = frames[i]
            for s in range(sides):
                ang = 2 * math.pi * (s + 0.5) / sides
                vs.append(tuple(P[i] + (a_ * math.cos(ang) + b_ * math.sin(ang)) * rr))
        fs = []
        rn = n if closed else n - 1
        for i in range(rn):
            i2 = (i + 1) % n
            for s in range(sides):
                s2 = (s + 1) % sides
                fs.append((i * sides + s, i * sides + s2, i2 * sides + s2, i2 * sides + s))
        if cap and not closed:
            fs.append(tuple(reversed(range(sides))))
            fs.append(tuple(range((n - 1) * sides, n * sides)))
        return self.add(vs, fs, mat)

    def sphere(self, c, r, mat, seg=12, rings=8, sz=1.0):
        prof = []
        for k in range(rings + 1):
            a = -math.pi / 2 + math.pi * k / rings
            prof.append((max(r * math.cos(a), 1e-5 if 0 < k < rings else 0.0), r * math.sin(a) * sz))
        prof[0] = (1e-4, prof[0][1])
        prof[-1] = (1e-4, prof[-1][1])
        return self.lathe(prof, seg, mat, center=c, cap_bottom=True, cap_top=True)

    def grid(self, fn, nu, nv, mat, uv=True):
        """Parametric sheet: fn(u, v) -> (x, y, z), u, v in [0, 1]."""
        vs = [fn(i / nu, j / nv) for j in range(nv + 1) for i in range(nu + 1)]
        fs, uvs = [], []
        for j in range(nv):
            for i in range(nu):
                a = j * (nu + 1) + i
                fs.append((a, a + 1, a + nu + 2, a + nu + 1))
                uvs.append([(i / nu, j / nv), ((i + 1) / nu, j / nv), ((i + 1) / nu, (j + 1) / nv), (i / nu, (j + 1) / nv)])
        return self.add(vs, fs, mat, uvs=uvs if uv else None)


# --------------------------------------------------------------------------------------
# Profiles
# --------------------------------------------------------------------------------------
def arc_pts(cx, cy, r, a0, a1, n):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]


def cyma(x0, y0, x1, y1, n=6, reverse=False):
    """S-curve from (x0,y0) to (x1,y1)."""
    out = []
    for i in range(n + 1):
        t = i / n
        s = 0.5 - 0.5 * math.cos(math.pi * t)
        if reverse:
            s = t + (t - s)
            s = min(max(s, 0), 1)
        out.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * s))
    return out


def ovolo(x0, y0, x1, y1, n=5):
    """Quarter-round from (x0,y0) to (x1,y1), bulging outward."""
    return [(x0 + (x1 - x0) * math.sin(math.pi / 2 * i / n), y0 + (y1 - y0) * (1 - math.cos(math.pi / 2 * i / n))) for i in range(n + 1)]


def dedupe(pts, eps=1e-6):
    out = []
    for p in pts:
        if not out or (abs(out[-1][0] - p[0]) > eps or abs(out[-1][1] - p[1]) > eps):
            out.append(p)
    if len(out) > 2 and abs(out[0][0] - out[-1][0]) < eps and abs(out[0][1] - out[-1][1]) < eps:
        out.pop()
    return out


# --------------------------------------------------------------------------------------
# Objects
# --------------------------------------------------------------------------------------
def get_coll(name, parent=None):
    c = bpy.data.collections.get(name) or bpy.data.collections.new(name)
    parent = parent or bpy.context.scene.collection
    if c.name not in [x.name for x in parent.children]:
        parent.children.link(c)
    return c


def box_uv(me, scale=1.0):
    """Planar projection per face by dominant normal axis (metres * scale), vectorised."""
    uvl = me.uv_layers.get("uv_material") or me.uv_layers.new(name="uv_material")
    nv, np_, nl = len(me.vertices), len(me.polygons), len(me.loops)
    co = np.empty(nv * 3)
    me.vertices.foreach_get("co", co)
    co = co.reshape(-1, 3)
    pn = np.empty(np_ * 3)
    me.polygons.foreach_get("normal", pn)
    pn = pn.reshape(-1, 3)
    tot = np.empty(np_, dtype=np.int64)
    me.polygons.foreach_get("loop_total", tot)
    lv = np.empty(nl, dtype=np.int64)
    me.loops.foreach_get("vertex_index", lv)
    ln = np.repeat(pn, tot, axis=0)
    v = co[lv]
    ax = np.abs(ln).argmax(1)
    sg = np.where(ln[np.arange(nl), ax] >= 0, 1.0, -1.0)
    out = np.zeros((nl, 2))
    m0, m1, m2 = ax == 0, ax == 1, ax == 2
    out[m0] = np.stack([v[m0, 1] * sg[m0], v[m0, 2]], 1)
    out[m1] = np.stack([-v[m1, 0] * sg[m1], v[m1, 2]], 1)
    out[m2] = np.stack([v[m2, 0], v[m2, 1] * sg[m2]], 1)
    uvl.data.foreach_set("uv", (out * scale).ravel())
    return uvl


def _outward_closed_islands(bm):
    """Flip any closed (manifold) island whose signed volume is negative (normals pointing inward)."""
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
        if any(e.is_boundary for g in isl for e in g.edges):
            continue
        vol = 0.0
        for g in isl:
            vs = [v.co for v in g.verts]
            for i in range(1, len(vs) - 1):
                vol += vs[0].dot(vs[i].cross(vs[i + 1]))
        if vol < 0:
            bmesh.ops.reverse_faces(bm, faces=isl)


def to_object(mb, name, coll, mats, smooth_angle=35.0, uv_scale=1.0, recalc=True, bake_uv="smart"):
    me = bpy.data.meshes.new(name)
    me.from_pydata(mb.v, [], mb.f)
    me.validate(clean_customdata=False)
    names = []
    for mname in mb.m:
        if mname not in names:
            names.append(mname)
    for mname in names:
        me.materials.append(mats[mname])
    idx = np.array([names.index(m) for m in mb.m], dtype=np.int32)
    if len(idx) == len(me.polygons):
        me.polygons.foreach_set("material_index", idx)
    if recalc:
        bm = bmesh.new()
        bm.from_mesh(me)
        bm.verts.ensure_lookup_table()
        # weld only inside each primitive (lathe poles, sweep seams); separate parts that merely
        # touch (frame members, glazing bars) stay separate closed shells
        groups = [[bm.verts[i] for i in range(a, b)] for a, b in mb.parts] or [list(bm.verts)]
        for g in groups:
            bmesh.ops.remove_doubles(bm, verts=[v for v in g if v.is_valid], dist=1e-5)
        bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-6)
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        _outward_closed_islands(bm)
        bm.to_mesh(me)
        bm.free()
    ob = bpy.data.objects.new(name, me)
    coll.objects.link(ob)
    # shading
    me.shade_smooth()
    try:
        me.set_sharp_from_angle(angle=math.radians(smooth_angle))
    except Exception:
        pass
    # UVs
    if mb.leaf_uv and not recalc:
        uvl = me.uv_layers.new(name="uv_material")
        arr = np.zeros((len(me.loops), 2))
        for p in me.polygons:
            uv = mb.leaf_uv.get(p.index)
            if uv:
                for k, li in enumerate(p.loop_indices):
                    arr[li] = uv[k % len(uv)]
        uvl.data.foreach_set("uv", arr.ravel())
        b = me.uv_layers.new(name="uv_bake")
        b.data.foreach_set("uv", np.clip(arr, 0, 1).ravel())
    else:
        box_uv(me, uv_scale)
        bake = me.uv_layers.new(name="uv_bake")
        me.uv_layers.active = bake
        ok = False
        if bake_uv == "smart" and len(me.polygons) < 60000:
            ok = smart_uv(ob)
        if not ok:
            a = np.empty(len(me.loops) * 2)
            me.uv_layers["uv_material"].data.foreach_get("uv", a)
            a = a.reshape(-1, 2)
            lo, hi = a.min(0), a.max(0)
            a = (a - lo) / max((hi - lo).max(), 1e-6)
            bake.data.foreach_set("uv", a.ravel())
        me.uv_layers["uv_material"].active_render = True
        me.uv_layers.active = me.uv_layers["uv_bake"]
    return ob


def smart_uv(ob):
    try:
        vl = bpy.context.view_layer
        for o in vl.objects:
            o.select_set(False)
        vl.objects.active = ob
        ob.select_set(True)
        with bpy.context.temp_override(active_object=ob, object=ob, selected_objects=[ob], selected_editable_objects=[ob]):
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.004)
            bpy.ops.object.mode_set(mode="OBJECT")
        ob.select_set(False)
        return True
    except Exception as e:  # noqa
        print("smart_uv failed", ob.name, e)
        try:
            bpy.ops.object.mode_set(mode="OBJECT")
        except Exception:
            pass
        return False


# --------------------------------------------------------------------------------------
# Materials
# --------------------------------------------------------------------------------------
def srgb(c):
    def f(x):
        x = x / 255.0
        return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4
    return (f(c[0]), f(c[1]), f(c[2]), 1.0)


def _bsdf(mat):
    return next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")


def mat_basic(name, rgb, rough=0.5, metal=0.0, alpha=None, emit=None, emit_strength=0.0,
              tint_attr=None, translucent=0.0, backface=True):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    nt = mat.node_tree
    b = _bsdf(mat)
    b.inputs["Base Color"].default_value = srgb(rgb)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    mat.diffuse_color = srgb(rgb)
    if alpha is not None:
        b.inputs["Alpha"].default_value = alpha
        mat.surface_render_method = "BLENDED"
        try:
            mat.use_transparency_overlap = True
        except Exception:
            pass
    if emit:
        b.inputs["Emission Color"].default_value = srgb(emit)
        b.inputs["Emission Strength"].default_value = emit_strength
    if tint_attr:
        at = nt.nodes.new("ShaderNodeAttribute")
        at.attribute_name = tint_attr
        mul = nt.nodes.new("ShaderNodeMix")
        mul.data_type = "RGBA"
        mul.blend_type = "MULTIPLY"
        mul.inputs["Factor"].default_value = 1.0
        mul.inputs[6].default_value = srgb(rgb)
        nt.links.new(at.outputs["Color"], mul.inputs[7])
        nt.links.new(mul.outputs[2], b.inputs["Base Color"])
    if translucent > 0:
        try:
            b.inputs["Subsurface Weight"].default_value = 0.0
            b.inputs["Transmission Weight"].default_value = 0.0
        except Exception:
            pass
        # mix with a translucent BSDF
        out = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
        tr = nt.nodes.new("ShaderNodeBsdfTranslucent")
        tr.inputs["Color"].default_value = srgb(rgb)
        if tint_attr:  # translucency takes the per-leaf tint too (else leaves glow white)
            tl = next(n for n in nt.nodes if n.type == "MIX" and n.blend_type == "MULTIPLY")
            nt.links.new(tl.outputs[2], tr.inputs["Color"])
        mix = nt.nodes.new("ShaderNodeMixShader")
        mix.inputs["Fac"].default_value = translucent
        nt.links.new(b.outputs[0], mix.inputs[1])
        nt.links.new(tr.outputs[0], mix.inputs[2])
        nt.links.new(mix.outputs[0], out.inputs["Surface"])
    mat.use_backface_culling = not backface
    return mat


def mat_stone(name, tex_dir, tile_m=1.6, cavity=0.06, power=1.6, value=0.84):
    """Clean limestone base: tiled author swatch, projected by face direction (uv_material)."""
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    nt = mat.node_tree
    b = _bsdf(mat)
    uv = nt.nodes.new("ShaderNodeUVMap")
    uv.uv_map = "uv_material"
    mp = nt.nodes.new("ShaderNodeMapping")
    s = 1.0 / tile_m
    mp.inputs["Scale"].default_value = (s, s, s)
    nt.links.new(uv.outputs[0], mp.inputs[0])

    def img(fn, cs):
        p = tex_dir / fn
        im = bpy.data.images.get(fn) or bpy.data.images.load(str(p), check_existing=True)
        im.colorspace_settings.name = cs
        n = nt.nodes.new("ShaderNodeTexImage")
        n.image = im
        nt.links.new(mp.outputs[0], n.inputs[0])
        return n
    bc = img("m_aa_limestone_tile_basecolor.png", "sRGB")
    # restrained underpainting: pull the swatch toward the bible's warm cream
    hsv = nt.nodes.new("ShaderNodeHueSaturation")
    hsv.inputs["Saturation"].default_value = 1.45
    hsv.inputs["Value"].default_value = value
    nt.links.new(bc.outputs[0], hsv.inputs["Color"])
    # warm the underpainting toward the bible's ochre cream
    warm = nt.nodes.new("ShaderNodeMix")
    warm.data_type = "RGBA"
    warm.blend_type = "MULTIPLY"
    warm.inputs["Factor"].default_value = 1.0
    warm.inputs[7].default_value = (1.0, 0.9, 0.74, 1.0)
    nt.links.new(hsv.outputs[0], warm.inputs[6])
    # cavity darkening for carved and moulded work (review look; bake for the engine)
    ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
    ao.inputs["Distance"].default_value = cavity
    ao.samples = 16
    pw = nt.nodes.new("ShaderNodeMath")
    pw.operation = "POWER"
    pw.inputs[1].default_value = power
    nt.links.new(ao.outputs["AO"], pw.inputs[0])
    cav = nt.nodes.new("ShaderNodeMix")
    cav.data_type = "RGBA"
    cav.blend_type = "MULTIPLY"
    cav.inputs["Factor"].default_value = 1.0
    nt.links.new(warm.outputs[2], cav.inputs[6])
    nt.links.new(pw.outputs[0], cav.inputs[7])
    nt.links.new(cav.outputs[2], b.inputs["Base Color"])
    rg = img("m_aa_limestone_tile_roughness.png", "Non-Color")
    nt.links.new(rg.outputs[0], b.inputs["Roughness"])
    nm = img("m_aa_limestone_tile_normal.png", "Non-Color")
    nmap = nt.nodes.new("ShaderNodeNormalMap")
    nmap.uv_map = "uv_material"
    nmap.inputs["Strength"].default_value = 0.6
    nt.links.new(nm.outputs[0], nmap.inputs["Color"])
    nt.links.new(nmap.outputs[0], b.inputs["Normal"])
    mat.diffuse_color = srgb((214, 192, 160))
    return mat


def mat_glass(name):
    """Clear window glass: transparent with a Fresnel sky reflection (review render; engine maps to URP
    transparent Lit)."""
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    nt = mat.node_tree
    for n in list(nt.nodes):
        if n.type != "OUTPUT_MATERIAL":
            nt.nodes.remove(n)
    out = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    tr.inputs["Color"].default_value = (0.93, 0.95, 0.96, 1)
    gl = nt.nodes.new("ShaderNodeBsdfGlossy")
    gl.inputs["Roughness"].default_value = 0.04
    gl.inputs["Color"].default_value = (0.62, 0.68, 0.76, 1)
    fr = nt.nodes.new("ShaderNodeFresnel")
    fr.inputs["IOR"].default_value = 1.5
    add = nt.nodes.new("ShaderNodeMath")
    add.operation = "ADD"
    add.use_clamp = True
    add.inputs[1].default_value = 0.22
    nt.links.new(fr.outputs[0], add.inputs[0])
    # soft sky / street reflection (the street opposite isn't modelled): glossy + a pale blue-grey sheen
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = srgb((136, 150, 182))
    em.inputs["Strength"].default_value = 0.55
    refl = nt.nodes.new("ShaderNodeAddShader")
    nt.links.new(gl.outputs[0], refl.inputs[0])
    nt.links.new(em.outputs[0], refl.inputs[1])
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(add.outputs[0], mix.inputs["Fac"])
    nt.links.new(tr.outputs[0], mix.inputs[1])
    nt.links.new(refl.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs["Surface"])
    mat.surface_render_method = "BLENDED"
    mat.use_backface_culling = False
    mat.diffuse_color = (0.6, 0.65, 0.7, 0.3)
    return mat


def mat_terracotta(name):
    """Clean fired clay: smooth orange-brown, continuous (no ramp), with a faint low-frequency mottle
    blended in at 12% so it never bands."""
    mat = mat_basic(name, (170, 84, 52), rough=0.72)
    nt = mat.node_tree
    b = _bsdf(mat)
    tc = nt.nodes.new("ShaderNodeTexCoord")
    nz = nt.nodes.new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = 6.0
    nz.inputs["Detail"].default_value = 2.0
    nt.links.new(tc.outputs["Object"], nz.inputs["Vector"])
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.blend_type = "MIX"
    fac = nt.nodes.new("ShaderNodeMath")
    fac.operation = "MULTIPLY"
    fac.inputs[1].default_value = 0.24
    nt.links.new(nz.outputs["Fac"], fac.inputs[0])
    nt.links.new(fac.outputs[0], mix.inputs["Factor"])
    mix.inputs[6].default_value = srgb((170, 84, 52))
    mix.inputs[7].default_value = srgb((150, 74, 48))
    nt.links.new(mix.outputs[2], b.inputs["Base Color"])
    return mat


def make_materials(tex_dir):
    M = {}
    M["stone"] = mat_stone("m_aa_trim_stone", tex_dir)
    M["carved"] = mat_stone("m_aa_trim_stone_carved", tex_dir, cavity=0.045, power=2.4, value=0.8)
    M["wood"] = mat_basic("m_aa_window_timber", (58, 34, 24), rough=0.42)
    M["glass"] = mat_glass("m_aa_window_glass")
    M["curtain"] = mat_basic("m_aa_window_curtain", (238, 238, 242), rough=0.9, alpha=0.5, translucent=0.65,
                             emit=(255, 246, 232), emit_strength=0.1)   # sheer, faint room backlight
    M["cord"] = mat_basic("m_aa_window_cord", (222, 210, 186), rough=0.85)
    M["iron"] = mat_basic("m_aa_wrought_iron", (14, 14, 15), rough=0.45)
    M["flash"] = mat_basic("m_aa_sill_flashing", (12, 15, 22), rough=0.26)
    M["terracotta"] = mat_terracotta("m_aa_terracotta")
    M["copper"] = mat_basic("m_aa_copper_pot", (235, 160, 120), rough=0.32, metal=1.0)
    M["soil"] = mat_basic("m_aa_potting_soil", (40, 28, 20), rough=0.95)
    M["leaf"] = mat_basic("m_aa_foliage", (255, 255, 255), rough=0.38, tint_attr="leaf_tint", translucent=0.3)
    M["stem"] = mat_basic("m_aa_foliage_stem", (60, 74, 34), rough=0.7)
    M["petal_pink"] = mat_basic("m_aa_flower_magenta", (222, 40, 120), rough=0.6, translucent=0.2)
    M["petal_orange"] = mat_basic("m_aa_flower_orange", (235, 120, 30), rough=0.6, translucent=0.2)
    M["petal_red"] = mat_basic("m_aa_flower_red", (205, 38, 34), rough=0.6, translucent=0.2)
    M["petal_yellow"] = mat_basic("m_aa_flower_yellow", (238, 196, 40), rough=0.6, translucent=0.2)
    M["petal_white"] = mat_basic("m_aa_flower_white", (240, 238, 228), rough=0.6, translucent=0.2)
    M["petal_center"] = mat_basic("m_aa_flower_centre", (240, 200, 60), rough=0.6)
    M["void"] = mat_basic("m_aa_interior_void", (92, 86, 80), rough=0.9, emit=(120, 112, 102), emit_strength=0.9)
    M["lamp_glass"] = mat_basic("m_aa_lamp_glass", (230, 232, 230), rough=0.25, alpha=0.55)
    M["bulb"] = mat_basic("m_aa_lamp_bulb", (255, 200, 120), rough=0.2, emit=(255, 170, 80), emit_strength=6.0)
    M["brass"] = mat_basic("m_aa_lamp_brass", (220, 180, 110), rough=0.35, metal=1.0)
    M["slate"] = mat_basic("m_aa_roof_slate", (52, 58, 70), rough=0.6)
    return M


# --------------------------------------------------------------------------------------
# misc
# --------------------------------------------------------------------------------------
def set_color_attr(ob, name, per_face_rgb):
    me = ob.data
    at = me.color_attributes.get(name) or me.color_attributes.new(name, "FLOAT_COLOR", "CORNER")
    arr = np.zeros((len(me.loops), 4), dtype=np.float32)
    for p in me.polygons:
        c = per_face_rgb[p.index] if p.index < len(per_face_rgb) else (1, 1, 1)
        for li in p.loop_indices:
            arr[li] = (c[0], c[1], c[2], 1.0)
    at.data.foreach_set("color", arr.ravel())


def rng(seed):
    return random.Random(seed)
