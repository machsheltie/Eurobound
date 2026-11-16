"""Flat unlit orthographic turnaround of a GLB in rest pose: <out>_front/left/back/right.png, 384x1024, white background.
Used as the ChatGPT repaint source for project_ref.py (Eurobound-8c3z). Frames the largest mesh with margin.
blender -b --factory-startup --python tools/char3d/turnaround_views.py -- <in.glb> <out_prefix>
"""
import bpy, sys, math
from mathutils import Vector
glb, out = sys.argv[sys.argv.index("--") + 1:][:2]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
for o in bpy.data.objects:
    if o.type == "ARMATURE":
        o.data.pose_position = "REST"
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
pts = []
big = max((o for o in bpy.data.objects if o.type == "MESH"), key=lambda o: len(o.data.vertices))
for o in [big]:
    if o.type == "MESH":
        e = o.evaluated_get(dg); m = e.to_mesh()
        pts += [o.matrix_world @ v.co for v in m.vertices]
        e.to_mesh_clear()
mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
c = (mn + mx) / 2; h = mx.z - mn.z
print("BBOX", tuple(round(v,3) for v in mn), tuple(round(v,3) for v in mx))
sc = bpy.context.scene
sc.render.engine = "BLENDER_WORKBENCH"
sc.display.shading.light = "FLAT"
sc.display.shading.color_type = "TEXTURE"
sc.view_settings.view_transform = "Standard"
sc.world = bpy.data.worlds.new("w"); sc.world.color = (1, 1, 1)
sc.display.shading.background_type = "WORLD"
sc.render.resolution_x = 384; sc.render.resolution_y = 1024
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.data.type = "ORTHO"; cam.data.ortho_scale = h * 1.18
for name, d in (("front", Vector((0, -1, 0))), ("left", Vector((-1, 0, 0))), ("back", Vector((0, 1, 0))), ("right", Vector((1, 0, 0)))):
    cam.location = c + d * 10
    cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
    sc.render.filepath = f"{out}_{name}.png"
    bpy.ops.render.render(write_still=True)
