"""Shared helpers for scripted-geometry icons: build parts, fuse them into ONE mesh with ONE material and ONE atlas image.

Atlas = (optional) painted flat-colour art on top + a strip of flat colour swatches along the bottom.
 - a part registered with a hex colour gets UVs on its swatch (plain flat colour)
 - a part registered with paint={...} gets UVs mapped into a rectangle of the painted art (Pillow-made, flat colour, bold shapes)
   modes: plane (planar on two world axes), cyl (around the Z axis), z (height only, banding), axis (around any axis)
   rect is in painted-image pixels, y down. cyl/axis rects must span the full image width (the sampler repeats horizontally for the seam).
Principled BSDF, base colour texture only, no emission. Run from a script: blender -b --python <script> -- <args>
"""
import bpy, bmesh, math, os
import numpy as np
from mathutils import Vector

PARTS = []   # (object, hex or None, paint dict or None)
STRIP = 64


def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    PARTS.clear()


def reg(obj, hexc=None, paint=None):
    PARTS.append((obj, hexc.lstrip("#").upper() if hexc else None, paint))
    return obj


def lathe(profile, n=48, name="lathe"):
    """profile: list of (r, z), z up. r == 0 points become a single pole vertex. Closed shapes start and end on r == 0."""
    bm = bmesh.new()
    rings = []
    for r, z in profile:
        if r <= 1e-9:
            rings.append([bm.verts.new((0, 0, z))])
        else:
            rings.append([bm.verts.new((r * math.cos(2 * math.pi * k / n), r * math.sin(2 * math.pi * k / n), z)) for k in range(n)])
    for i in range(len(profile) - 1):
        A, B = rings[i], rings[i + 1]
        for k in range(n):
            k2 = (k + 1) % n
            if len(A) == 1 and len(B) == 1:
                continue
            if len(A) == 1:
                bm.faces.new((A[0], B[k2], B[k]))
            elif len(B) == 1:
                bm.faces.new((A[k], A[k2], B[0]))
            else:
                bm.faces.new((A[k], A[k2], B[k2], B[k]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    return ob


def prim(kind, loc=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1), **kw):
    if kind == "cube":
        bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    elif kind == "cyl":
        bpy.ops.mesh.primitive_cylinder_add(vertices=kw.get("v", 32), radius=kw["r"], depth=kw["d"], location=loc)
    elif kind == "cone":
        bpy.ops.mesh.primitive_cone_add(vertices=kw.get("v", 6), radius1=kw["r"], radius2=0, depth=kw["d"], location=loc)
    elif kind == "torus":
        bpy.ops.mesh.primitive_torus_add(major_segments=kw.get("v", 28), minor_segments=kw.get("mv", 14), major_radius=kw["R"], minor_radius=kw["r"], location=loc)
    elif kind == "sphere":
        bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=14, radius=kw["r"], location=loc)
    ob = bpy.context.active_object
    ob.rotation_euler = tuple(math.radians(a) for a in rot)
    ob.scale = scale
    bpy.ops.object.transform_apply(rotation=True, scale=True)
    return ob


def bevel(ob, width=0.01, seg=2):
    bpy.context.view_layer.objects.active = ob
    m = ob.modifiers.new("bv", "BEVEL"); m.width = width; m.segments = seg; m.limit_method = 'ANGLE'
    bpy.ops.object.modifier_apply(modifier="bv")
    return ob


def difference(ob, cutter):
    bpy.context.view_layer.objects.active = ob
    m = ob.modifiers.new("d", "BOOLEAN"); m.operation = 'DIFFERENCE'; m.object = cutter; m.solver = 'EXACT'
    bpy.ops.object.modifier_apply(modifier="d")
    bpy.data.objects.remove(cutter, do_unlink=True)
    return ob


def _frac(spec, c, ang_fix):
    """world point -> (fu, fv) inside the part's painted rect"""
    m = spec["mode"]
    if m == "plane":
        (a, b), (a0, a1, b0, b1) = spec["ax"], spec["bounds"]
        return (c[a] - a0) / (a1 - a0), (c[b] - b0) / (b1 - b0)
    if m in ("cyl", "z"):
        z0, z1 = spec["zr"]
        fv = (c.z - z0) / (z1 - z0)
        return (0.5 if m == "z" else (ang_fix(math.atan2(c.y, c.x)) + math.pi) / (2 * math.pi)), fv
    if m == "axis":
        p0, d, e1 = spec["p0"], spec["d"], spec["e1"]
        e2 = d.cross(e1)
        rel = c - p0
        t0, t1 = spec["tr"]
        return (ang_fix(math.atan2(rel.dot(e2), rel.dot(e1))) + math.pi) / (2 * math.pi), (rel.dot(d) - t0) / (t1 - t0)
    raise ValueError(m)


def finish(out_glb, paint_png=None, tilt=0.0, smooth_deg=40, rough=0.7):
    """Fuse PARTS into one mesh, one atlas material, export GLB. Returns the fused object."""
    cols = []
    for _, h, p in PARTS:
        if h and h not in cols:
            cols.append(h)
    if paint_png:
        pimg = bpy.data.images.load(os.path.abspath(paint_png))
        W, PH = pimg.size
        pp = np.empty(W * PH * 4, dtype=np.float32); pimg.pixels.foreach_get(pp); pp = pp.reshape(PH, W, 4)
    else:
        W, PH = 16 * max(1, len(cols)), 0
    cell = W // max(1, len(cols))
    arr = np.ones((PH + STRIP, W, 4), dtype=np.float32)
    for i, h in enumerate(cols):
        x1 = (i + 1) * cell if i < len(cols) - 1 else W
        arr[:STRIP, i * cell:x1, :3] = [int(h[j:j + 2], 16) / 255.0 for j in (0, 2, 4)]
    if PH:
        arr[STRIP:] = pp
        arr[STRIP:, :, 3] = 1.0
    img = bpy.data.images.new("palette_atlas", W, PH + STRIP, alpha=False)
    img.pixels.foreach_set(arr.reshape(-1))
    atlas = os.path.splitext(out_glb)[0] + "_atlas.png"
    img.filepath_raw = atlas; img.file_format = "PNG"; img.save()
    TH = PH + STRIP
    for ob, h, spec in PARTS:
        bm = bmesh.new(); bm.from_mesh(ob.data)
        for lay in list(bm.loops.layers.uv):
            if lay.name != 'UVMap':
                bm.loops.layers.uv.remove(lay)
        uv = bm.loops.layers.uv.get('UVMap') or bm.loops.layers.uv.new('UVMap')
        mw = ob.matrix_basis
        for f in bm.faces:
            if spec is None:
                u = (cols.index(h) * cell + cell / 2.0) / W
                for l in f.loops:
                    l[uv].uv = (u, STRIP / 2.0 / TH)
                continue
            cc = mw @ f.calc_center_median()
            ac = math.atan2(cc.y, cc.x) if spec["mode"] != "axis" else None
            if spec["mode"] == "axis":
                rel = cc - spec["p0"]; ac = math.atan2(rel.dot(spec["d"].cross(spec["e1"])), rel.dot(spec["e1"]))
            fix = lambda a, ac=ac: ac + ((a - ac + math.pi) % (2 * math.pi) - math.pi)
            x0, y0, x1, y1 = spec["rect"]
            for l in f.loops:
                fu, fv = _frac(spec, mw @ l.vert.co, fix)
                fv = min(max(fv, 0.004), 0.996)
                if spec["mode"] in ("plane", "z"):
                    fu = min(max(fu, 0.004), 0.996)
                l[uv].uv = ((x0 + fu * (x1 - x0)) / W, (STRIP + PH - (y1 - fv * (y1 - y0))) / TH)
        bm.to_mesh(ob.data); bm.free()
    bpy.ops.object.select_all(action='DESELECT')
    for ob, _, _ in PARTS:
        ob.select_set(True)
    bpy.context.view_layer.objects.active = PARTS[0][0]
    bpy.ops.object.join()
    obj = bpy.context.active_object
    me = obj.data
    bpy.ops.object.shade_smooth_by_angle(angle=math.radians(smooth_deg))
    mat = bpy.data.materials.new("flat_palette"); mat.use_nodes = True
    nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
    tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = "Linear"; tex.extension = "REPEAT"
    nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Metallic"].default_value = 0.0; bsdf.inputs["Roughness"].default_value = rough
    me.materials.clear(); me.materials.append(mat)
    for p in me.polygons:
        p.material_index = 0
    if tilt:
        obj.rotation_euler = (math.radians(tilt), 0, 0)
        bpy.ops.object.transform_apply(rotation=True)
    bpy.ops.export_scene.gltf(filepath=out_glb, export_format="GLB", export_image_format="AUTO")
    print("FUSED", out_glb, "verts", len(me.vertices), "polys", len(me.polygons), "colours", len(cols))
    return obj
