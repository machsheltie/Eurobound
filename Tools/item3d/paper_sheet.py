"""Build a thin curling paper sheet textured with a rectified face image (0 Tripo credits). Sibling of card_slab.py.

blender -b --python tools/item3d/paper_sheet.py -- <face_rect.png> <out.glb> [tilt_deg=58] [width=0.714] [thickness=0.012]
 - sheet width x 1.0 (1:1.4 default), flat, face up (+Z), no slot, no card bevel; all four corners curl up toward the viewer
 - front UVs planar 0..1; back and edge faces use one plain patch of the image (render_item.py keeps one material slot)
 - tilt_deg: rotation about X that leans the face toward the render camera, baked into the mesh
"""
import bpy, bmesh, sys, os, math
import numpy as np

argv = sys.argv[sys.argv.index("--") + 1:]
face_png, out_glb = os.path.abspath(argv[0]), os.path.abspath(argv[1])
tilt = float(argv[2]) if len(argv) > 2 else 58.0
W = float(argv[3]) if len(argv) > 3 else 0.714
T = float(argv[4]) if len(argv) > 4 else 0.012
H = 1.0
NX, NY = 48, 66

bpy.ops.wm.read_factory_settings(use_empty=True)
bm = bmesh.new()
bmesh.ops.create_grid(bm, x_segments=NX, y_segments=NY, size=0.5)
for v in bm.verts:
    v.co.x *= W; v.co.y *= H
    # curl: lift each corner's neighbourhood toward +Z, a little more at the top corners
    for sx in (-1, 1):
        for sy in (-1, 1):
            dx = (sx * W / 2 - v.co.x) * sx; dy = (sy * H / 2 - v.co.y) * sy
            r = math.hypot(dx, dy); R = 0.17
            if r < R:
                k = (1 - r / R) ** 2
                v.co.z += 0.055 * k * (1.15 if sy > 0 else 0.9)
    # faint cupping along the fold line
    v.co.z += 0.004 * (abs(v.co.x) / (W / 2)) ** 2
me = bpy.data.meshes.new("sheet"); bm.to_mesh(me); bm.free()
sheet = bpy.data.objects.new("sheet", me); bpy.context.scene.collection.objects.link(sheet)
bpy.context.view_layer.objects.active = sheet; sheet.select_set(True)
sol = sheet.modifiers.new("sol", "SOLIDIFY"); sol.thickness = T; sol.offset = -1
bpy.ops.object.modifier_apply(modifier="sol")

img = bpy.data.images.load(face_png)
bm = bmesh.new(); bm.from_mesh(sheet.data); bm.normal_update()
uv = bm.loops.layers.uv.verify()
blank = (0.3, 0.3)   # plain paper patch (bottom-up UV): lower left, no print
for f in bm.faces:
    front = f.normal.z > 0.3 and f.calc_center_median().z > -T * 0.5 and all(l.vert.co.z > -1 for l in f.loops) and f.normal.z > 0
    for l in f.loops:
        co = l.vert.co
        l[uv].uv = (co.x / W + 0.5, co.y / H + 0.5) if front else blank
# back-side faces of the solidified sheet face -Z; front ones +Z (curled corners still have normal.z > 0)
bm.to_mesh(sheet.data); bm.free()
bpy.ops.object.shade_smooth()

mat = bpy.data.materials.new("paper_mat"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = 'Linear'
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Base Color"].default_value = (1, 1, 1, 1); bsdf.inputs["Metallic"].default_value = 0.0; bsdf.inputs["Roughness"].default_value = 0.9
sheet.data.materials.clear(); sheet.data.materials.append(mat)
for p in sheet.data.polygons: p.material_index = 0

bpy.ops.object.select_all(action='DESELECT'); sheet.select_set(True)
sheet.rotation_euler = (math.radians(tilt), 0, 0)
bpy.ops.object.transform_apply(rotation=True)
bpy.ops.export_scene.gltf(filepath=out_glb, export_format="GLB", export_image_format="AUTO", export_jpeg_quality=95)
print("SHEET", out_glb, "verts", len(sheet.data.vertices))
