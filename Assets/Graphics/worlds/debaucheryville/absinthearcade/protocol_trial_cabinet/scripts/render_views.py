"""Trial 2 review renders (protocol step 9/10): fixed ortho cameras around the mesh bbox, Workbench flat albedo or neutral clay.
blender -b --factory-startup --python render_views.py -- <glb> <out_prefix> <mode albedo|clay> [px_h 740] [views front,right,back,left]
Views: front (viewer -Y), right (viewer +X: cabinet front on the image left, matches the reference side view), back (+Y), left (-X).
Also writes <out_prefix>_bbox.json. Transparent background; alpha PNG."""
import bpy, sys, json
from mathutils import Vector
a = sys.argv[sys.argv.index("--") + 1:]
glb, pre, mode = a[0], a[1], a[2]
PH = int(a[3]) if len(a) > 3 else 740
views = a[4].split(",") if len(a) > 4 else ["front", "right", "back", "left"]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
obs = [o for o in bpy.data.objects if o.type == "MESH"]
ws = [o.matrix_world @ v.co for o in obs for v in o.data.vertices]
mn = Vector([min(w[i] for w in ws) for i in range(3)])
mx = Vector([max(w[i] for w in ws) for i in range(3)])
c = (mn + mx) / 2
dim = mx - mn
json.dump({"min": list(mn), "max": list(mx)}, open(pre + "_bbox.json", "w"))
sc = bpy.context.scene
sc.render.engine = "BLENDER_WORKBENCH"
sh = sc.display.shading
sh.light = "FLAT"
sh.color_type = "TEXTURE" if mode == "albedo" else "SINGLE"
sh.single_color = (0.6, 0.6, 0.6)
sh.show_shadows = False
sc.display.render_aa = "8"
sc.render.film_transparent = True
sc.view_settings.view_transform = "Standard"
sc.render.image_settings.file_format = "PNG"
sc.render.image_settings.color_mode = "RGBA"
if mode == "clay":
    sh.light = "STUDIO"
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam"))
sc.collection.objects.link(cam)
sc.camera = cam
cam.data.type = "ORTHO"
cam.data.clip_end = 100
D = {"front": (0, -1, 0), "back": (0, 1, 0), "right": (1, 0, 0), "left": (-1, 0, 0)}
for v in views:
    d = Vector(D[v])
    cam.location = c + d * 5
    cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
    horiz = dim.x if v in ("front", "back") else dim.y
    cam.data.ortho_scale = dim.z * 1.04
    sc.render.resolution_y = PH
    sc.render.resolution_x = int(PH * (horiz / dim.z) * 1.04 + 8)
    sc.render.filepath = f"{pre}_{v}.png"
    bpy.ops.render.render(write_still=True)
print("rendered", views, "dim", [round(x, 3) for x in dim])
