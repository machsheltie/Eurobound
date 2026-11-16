"""GLOSS variant of render_item.py, for the Kokos Loco Bucket icon only (author ruling: glossy render for this icon).
Same camera, ortho scale, size and transparent film as render_item.py, but a lit Principled material (specular + clearcoat)
rendered with Cycles under area lights, so the plastic shows real highlights and soft shadows.

Render one Tripo item GLB to a 512 RGBA icon master plus a 128 Lanczos downscale.

Run (headless):
  "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python tools/item3d/render_item.py -- <glb> <out_512.png>
Writes <out_512.png> and <out_512 with _512 -> _128>.png. Gloss variant: Cycles + Principled with clearcoat under area lights.
Optional trailing args: yaw_degrees (default 28), pitch_degrees (default 22).
"""
import math, os, subprocess, sys
import bpy
from mathutils import Vector


ORTHO_SCALE = 0.95   # model is normalised so its bounding-sphere diameter = 1.0 unit -> constant px/unit for every icon
RES = 512

argv = sys.argv[sys.argv.index("--") + 1:]
glb, out = os.path.abspath(argv[0]), os.path.abspath(argv[1])
yaw = float(argv[2]) if len(argv) > 2 else 28.0
pitch = float(argv[3]) if len(argv) > 3 else 22.0

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
bpy.ops.import_scene.gltf(filepath=glb)

for o in list(bpy.data.objects):          # Tripo helper objects wreck the camera fit
    if o.name.startswith("Icosphere") or o.type != "MESH":
        bpy.data.objects.remove(o, do_unlink=True)
meshes = [o for o in bpy.data.objects if o.type == "MESH"]


def base_image(mat):
    if mat and mat.use_nodes:
        for n in mat.node_tree.nodes:
            if n.type == "TEX_IMAGE" and n.image:
                return n.image
    return None


def base_color(mat):
    if mat and mat.use_nodes:
        for n in mat.node_tree.nodes:
            if n.type == "BSDF_PRINCIPLED":
                return tuple(n.inputs["Base Color"].default_value)
    return (0.8, 0.8, 0.8, 1)


for o in meshes:                           # glossy plastic, keeps the model's own base-colour texture
    old = o.material_slots[0].material if o.material_slots else None
    img = base_image(old)
    m = bpy.data.materials.new("gloss_" + o.name)
    m.use_nodes = True
    nt = m.node_tree
    bsdf = [n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"][0]
    if img is not None:
        tn = nt.nodes.new("ShaderNodeTexImage"); tn.image = img
        nt.links.new(tn.outputs["Color"], bsdf.inputs["Base Color"])
    else:
        bsdf.inputs["Base Color"].default_value = base_color(old)
    def put(name, val):
        if name in bsdf.inputs: bsdf.inputs[name].default_value = val
    put("Roughness", 0.2)
    put("Specular IOR Level", 0.75)
    put("Coat Weight", 0.65)
    put("Coat Roughness", 0.06)
    o.data.materials.clear()
    o.data.materials.append(m)

# rotate the whole model about Z for the three-quarter view, then centre + scale on world bounds
root = bpy.data.objects.new("root", None)
scene.collection.objects.link(root)
for o in meshes:
    o.parent = root
root.rotation_euler = (0, 0, math.radians(yaw))
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
pts = []
for o in meshes:
    ev = o.evaluated_get(dg)
    mw = ev.matrix_world
    pts += [mw @ Vector(c) for c in ev.bound_box]
lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
ctr, diam = (lo + hi) / 2, (hi - lo).length
s = 1.0 / diam
root.scale = (s, s, s)
root.location = -ctr * s
bpy.context.view_layer.update()

cam = bpy.data.cameras.new("cam")
cam.type = "ORTHO"
cam.ortho_scale = ORTHO_SCALE
co = bpy.data.objects.new("cam", cam)
scene.collection.objects.link(co)
p = math.radians(pitch)
co.location = (0, -4 * math.cos(p), 4 * math.sin(p))
co.rotation_euler = (math.radians(90) - p, 0, 0)
scene.camera = co
scene.render.resolution_x = scene.render.resolution_y = RES
scene.render.resolution_percentage = 100

def area(name, loc, power, size, color=(1, 1, 1)):
    ld = bpy.data.lights.new(name, "AREA"); ld.energy = power; ld.size = size; ld.color = color
    lo_ = bpy.data.objects.new(name, ld); scene.collection.objects.link(lo_)
    lo_.location = loc
    d = Vector((0, 0, 0)) - Vector(loc)
    lo_.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
area("key", (-2.6, -2.2, 3.2), 150, 2.2, (1.0, 0.96, 0.9))
area("fill", (3.0, -1.8, 1.4), 45, 3.0, (0.85, 0.92, 1.0))
area("rim", (1.0, 3.0, 2.6), 90, 1.6, (1, 1, 1))
area("top", (0, -0.3, 4.0), 35, 3.0, (1, 1, 1))
w = bpy.data.worlds.new("w"); w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.72, 0.74, 0.8, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.18
scene.world = w
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
scene.render.engine = "CYCLES"
scene.cycles.samples = 96
scene.cycles.use_denoising = True
scene.cycles.device = "CPU"
scene.render.film_transparent = True
scene.view_settings.view_transform = "Standard"
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"
scene.render.filepath = out
bpy.ops.render.render(write_still=True)
print("RENDERED", out, RES, RES)

out128 = out.replace("_512", "_128") if "_512" in out else out[:-4] + "_128.png"
code = ("from PIL import Image;im=Image.open(r'%s').convert('RGBA');"
        "im.resize((128,128),Image.LANCZOS).save(r'%s')" % (out, out128))
subprocess.run(["python", "-c", code], check=True)
print("WROTE", out128)

