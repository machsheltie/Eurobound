"""Build a clean bevelled card slab with a hang-slot notch, textured with a rectified face image (0 Tripo credits).

blender -b --python tools/item3d/card_slab.py -- <face_rect.png> <out.glb> [tilt_deg=40]
 - card 0.77 x 1.0 x 0.06 (about 1:1.3, chunky backing card) (the Forty-Eight-Hour Tramp Stamp card proportions), flat, face up (+Z), top edge toward +Y
 - bevelled edges, hang slot cut near the top with a boolean
 - front face UVs planar 0..1; every other face is UV-mapped onto a plain cream patch of the same image (one material,
   because render_item.py keeps only the first material slot)
 - tilt_deg: rotation about X that leans the face toward the camera (render_item camera sits at -Y); baked into the mesh
"""
import bpy, bmesh, sys, os, math
import numpy as np
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
face_png, out_glb = os.path.abspath(argv[0]), os.path.abspath(argv[1])
tilt = float(argv[2]) if len(argv) > 2 else 58.0
W, H, T = 0.77, 1.0, 0.06

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.mesh.primitive_cube_add(size=1)
card = bpy.context.active_object
card.name = "card"
card.scale = (W, H, T)
bpy.ops.object.transform_apply(scale=True)

# hang slot: a stadium-ish notch (two cubes + bevel) cut through the thickness near the top centre
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, H / 2 - 0.06, 0))
slot = bpy.context.active_object
slot.scale = (0.26, 0.07, T * 3)
bpy.ops.object.transform_apply(scale=True)
bv = slot.modifiers.new("bv", "BEVEL"); bv.width = 0.03; bv.segments = 5; bv.limit_method = 'NONE'
bpy.context.view_layer.objects.active = slot
bpy.ops.object.modifier_apply(modifier="bv")
bl = card.modifiers.new("cut", "BOOLEAN"); bl.operation = 'DIFFERENCE'; bl.object = slot; bl.solver = 'EXACT'
bpy.context.view_layer.objects.active = card
bpy.ops.object.modifier_apply(modifier="cut")
bpy.data.objects.remove(slot, do_unlink=True)

# bevel the outer edges a little (applied after the cut so the slot edge is soft too)
bv2 = card.modifiers.new("bv2", "BEVEL"); bv2.width = 0.014; bv2.segments = 3; bv2.limit_method = 'ANGLE'
bpy.ops.object.modifier_apply(modifier="bv2")

# image + cream patch
img = bpy.data.images.load(face_png)
iw, ih = img.size
px = np.empty(iw * ih * 4, dtype=np.float32); img.pixels.foreach_get(px); px = px.reshape(ih, iw, 4)   # rows bottom-up
best = None
for cy in range(int(ih * 0.03), int(ih * 0.2), 6):
    for cx in range(int(iw * 0.08), int(iw * 0.92), 12):
        p = px[cy - 4:cy + 5, cx - 4:cx + 5, :3]
        sc = p.std() - p.mean() * 0.05
        if p.mean() > 0.7 and (best is None or sc < best[0]):
            best = (sc, cx, cy)
cream_uv = (best[1] / iw, best[2] / ih)

bm = bmesh.new(); bm.from_mesh(card.data)
bm.normal_update()
uv = bm.loops.layers.uv.verify()
for f in bm.faces:
    front = f.normal.z > 0.9
    for l in f.loops:
        co = l.vert.co
        l[uv].uv = (co.x / W + 0.5, co.y / H + 0.5) if front else cream_uv
print("FRONT FACES", sum(1 for f in bm.faces if f.normal.z > 0.9), "of", len(bm.faces))
bm.to_mesh(card.data); bm.free()
bpy.ops.object.shade_smooth()

mat = bpy.data.materials.new("card_mat"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = 'Linear'
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Base Color"].default_value = (1, 1, 1, 1); bsdf.inputs["Metallic"].default_value = 0.0; bsdf.inputs["Roughness"].default_value = 0.8
card.data.materials.clear()
card.data.materials.append(mat)
for p in card.data.polygons:
    p.material_index = 0

# lean toward the render camera and bake it
bpy.ops.object.select_all(action='DESELECT'); card.select_set(True)
card.rotation_euler = (math.radians(tilt), 0, 0)
bpy.ops.object.transform_apply(rotation=True)

bpy.ops.export_scene.gltf(filepath=out_glb, export_format="GLB", export_image_format="AUTO", export_jpeg_quality=95)
print("MATS", len(card.data.materials), [p.material_index for p in card.data.polygons][:5], [o.name for o in bpy.data.objects])
print("CARD", out_glb, "cream uv", cream_uv, "verts", len(card.data.vertices))
