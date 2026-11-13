"""Render one Tripo item GLB to a 512 RGBA icon master plus a 128 Lanczos downscale.

Run (headless):
  "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python tools/item3d/render_item.py -- <glb> <out_512.png>
Writes <out_512.png> and <out_512 with _512 -> _128>.png. Look comes from tools/char3d/look.py (toon ramp, warm key upper-left, cool fill).
Optional trailing args: yaw_degrees (default 28), pitch_degrees (default 22).
"""
import math, os, subprocess, sys
import bpy
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
LOOK_DIRS = [os.path.join(HERE, "..", "char3d"), r"C:/Users/heirr/Desktop/Hope2_Studio/Eurobound/tools/char3d"]
for d in LOOK_DIRS:
    if os.path.exists(os.path.join(d, "look.py")):
        sys.path.insert(0, d)
        break
import look

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


for o in meshes:                           # toon material, keep the model's own texture colours
    old = o.material_slots[0].material if o.material_slots else None
    m = look.toon_material("toon_" + o.name, img=base_image(old), base=base_color(old))
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

look.lights(scene)
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
look.render(scene, out)

out128 = out.replace("_512", "_128") if "_512" in out else out[:-4] + "_128.png"
code = ("from PIL import Image;im=Image.open(r'%s').convert('RGBA');"
        "im.resize((128,128),Image.LANCZOS).save(r'%s')" % (out, out128))
subprocess.run(["python", "-c", code], check=True)
print("WROTE", out128)
