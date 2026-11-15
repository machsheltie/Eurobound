"""Protocol step 9: lit review renders with the real PBR material (Cycles CPU, fixed camera/exposure/colour management for every attempt).
blender -b --factory-startup --python render_lit.py -- <glb> <out_prefix> <neutral|game> [px_h 740] [views]
neutral: uniform white world 1.0, no sun (flat, shows albedo + AO + roughness response only). game: warm key sun (elev 40, azimuth 35 deg off the front, 3.0) + cool dim sky (0.25),
emission on - a stand-in for the Arcade street light; the in-game light rig is not part of this trial package.
Cameras: orthographic along the model axes, mesh bbox fitted to the frame exactly like the reference views (front, right = reference side view, back, left)."""
import bpy, sys, math
from mathutils import Vector
a = sys.argv[sys.argv.index("--") + 1:]
glb, pre, mode = a[0], a[1], a[2]
PH = int(a[3]) if len(a) > 3 else 740
views = a[4].split(",") if len(a) > 4 else ["front", "right", "back", "left"]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
obs = [o for o in bpy.data.objects if o.type == "MESH"]
ws = [o.matrix_world @ v.co for o in obs for v in o.data.vertices]
mn = Vector([min(w[i] for w in ws) for i in range(3)]); mx = Vector([max(w[i] for w in ws) for i in range(3)])
c = (mn + mx) / 2; dim = mx - mn
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 48; sc.cycles.filter_width = 0.6
sc.view_settings.view_transform = "Standard"; sc.view_settings.exposure = 0.0
sc.render.film_transparent = True
sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_mode = "RGBA"
if mode == "albedo":   # unlit base colour only, for the region-by-region comparison with the reference
    sc.render.engine = "BLENDER_WORKBENCH"; sh = sc.display.shading
    sh.light = "FLAT"; sh.color_type = "TEXTURE"; sh.show_shadows = False; sc.display.render_aa = "8"
w = bpy.data.worlds.new("w"); w.use_nodes = True; sc.world = w
bg = w.node_tree.nodes["Background"]
if mode == "neutral":
    bg.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1); bg.inputs["Strength"].default_value = 1.0
else:
    bg.inputs["Color"].default_value = (0.35, 0.45, 0.65, 1); bg.inputs["Strength"].default_value = 0.25
    sun = bpy.data.objects.new("sun", bpy.data.lights.new("sun", "SUN")); sc.collection.objects.link(sun)
    sun.data.energy = 3.0; sun.data.color = (1.0, 0.9, 0.78); sun.data.angle = math.radians(4)
    sun.rotation_euler = (math.radians(50), 0, math.radians(-35))   # light travels toward +Y (back) and +X: it comes from the front-left of the viewer, 40 deg elevation (a first version pointed it from behind)
if mode == "neutral":   # albedo-faithful: diffuse only, no specular lift on the near-black paint, no emission, so colour can be compared with the reference
    for m in bpy.data.materials:
        for n in m.node_tree.nodes if m.use_nodes else []:
            if n.type == "BSDF_PRINCIPLED":
                n.inputs["Specular IOR Level"].default_value = 0.0; n.inputs["Emission Strength"].default_value = 0.0
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.data.type = "ORTHO"; cam.data.clip_end = 100
D = {"front": (0, -1, 0), "back": (0, 1, 0), "right": (1, 0, 0), "left": (-1, 0, 0), "bottom": (0, 0, -1)}   # bottom (Phase B): the underside seen from below, front at the image bottom
for v in views:
    d = Vector(D[v]); cam.location = c + d * 5
    cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
    horiz = dim.x if v in ("front", "back", "bottom") else dim.y
    vert = dim.y if v == "bottom" else dim.z
    cam.data.ortho_scale = vert
    sc.render.resolution_y = PH; sc.render.resolution_x = int(round(PH * horiz / vert))
    sc.render.filepath = f"{pre}_{mode}_{v}.png"
    bpy.ops.render.render(write_still=True)
print("rendered", mode, views, [sc.render.resolution_x, sc.render.resolution_y])
