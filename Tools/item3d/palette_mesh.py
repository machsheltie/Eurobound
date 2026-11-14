"""Shared helpers for scripted-geometry icons: build parts, give each a flat hex colour, fuse them into ONE mesh with ONE material.

Every colour is a swatch in a small atlas PNG (written next to the GLB, kept as source art); each face's UVs point at its swatch centre,
so render_item.py (which keeps only the first material slot) still renders every colour. Principled BSDF, base colour texture, no emission.
Use from a script run as: blender -b --python <script> -- <args>
"""
import bpy, bmesh, math, os

PARTS = []   # (object, hex)


def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    PARTS.clear()


def reg(obj, hexc):
    PARTS.append((obj, hexc.lstrip("#").upper()))
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


def finish(out_glb, tilt=0.0, smooth_deg=40, rough=0.7):
    """Fuse PARTS into one mesh, one atlas material, export GLB. Returns the fused object."""
    import numpy as np
    cols = []
    for _, h in PARTS:
        if h not in cols:
            cols.append(h)
    cell = 16
    arr = np.ones((cell, cell * len(cols), 4), dtype=np.float32)
    for i, h in enumerate(cols):
        arr[:, i * cell:(i + 1) * cell, :3] = [int(h[j:j + 2], 16) / 255.0 for j in (0, 2, 4)]
    img = bpy.data.images.new("palette_atlas", cell * len(cols), cell, alpha=False)
    img.pixels.foreach_set(arr.reshape(-1))
    atlas = os.path.splitext(out_glb)[0] + "_atlas.png"
    img.filepath_raw = atlas; img.file_format = "PNG"; img.save()
    mats = {h: bpy.data.materials.new("c_" + h) for h in cols}
    for ob, h in PARTS:
        ob.data.materials.clear(); ob.data.materials.append(mats[h])
        for p in ob.data.polygons:
            p.material_index = 0
    bpy.ops.object.select_all(action='DESELECT')
    for ob, _ in PARTS:
        ob.select_set(True)
    bpy.context.view_layer.objects.active = PARTS[0][0]
    bpy.ops.object.join()
    obj = bpy.context.active_object
    me = obj.data
    slot_hex = {i: s.material.name[2:] for i, s in enumerate(obj.material_slots)}
    bm = bmesh.new(); bm.from_mesh(me)
    uv = bm.loops.layers.uv.verify()
    for f in bm.faces:
        u = (cols.index(slot_hex[f.material_index]) + 0.5) / len(cols)
        for l in f.loops:
            l[uv].uv = (u, 0.5)
    bm.to_mesh(me); bm.free()
    bpy.ops.object.shade_smooth_by_angle(angle=math.radians(smooth_deg))
    mat = bpy.data.materials.new("flat_palette"); mat.use_nodes = True
    nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
    tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = "Closest"
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
