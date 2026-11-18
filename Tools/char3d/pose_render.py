"""Jakub 3D trial: import Tripo rigged GLB, pose him cradled/passed out, toon render.
blender -b --python pose_render.py -- <glb> <outdir> [pass_tag]
"""
import bpy, sys, math, json, os
from mathutils import Vector, Matrix, Quaternion
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "item3d"))
from material_lookup import base_image   # follows the Principled Base Color link (Eurobound-2bb9)

argv = sys.argv[sys.argv.index("--") + 1:]
GLB, OUT = argv[0], argv[1]
TAG = argv[2] if len(argv) > 2 else "p1"
CFG = json.loads(open(argv[3]).read()) if len(argv) > 3 else {}

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB)
for o in list(bpy.data.objects):
    if o.name.startswith("Icosphere"):
        bpy.data.objects.remove(o, do_unlink=True)

arm = next(o for o in bpy.data.objects if o.type == "ARMATURE")
body = next(o for o in bpy.data.objects if o.type == "MESH")
bpy.context.view_layer.update()
REST_MW = body.matrix_world.copy()
root = arm
while root.parent:
    root = root.parent
P = "mixamorig:"


def B(sx, sy, dx=0.0):
    """scene direction (sx right=toward feet, sy up, dx away from camera) -> body frame
    body frame: +Z up the spine, -Y his front, +X his left."""
    return Vector((dx, -sy, -sx)).normalized()


def aim(name, d, scale=None):
    pb = arm.pose.bones[P + name]
    bone = pb.bone
    bpy.context.view_layer.update()
    head = pb.head.copy()
    rest_dir = (bone.tail_local - bone.head_local).normalized()
    d = (arm.matrix_world.to_3x3().normalized().inverted() @ d).normalized()
    q = rest_dir.rotation_difference(d)
    m = q.to_matrix().to_4x4() @ bone.matrix_local.to_3x3().to_4x4()
    m.translation = head
    pb.matrix = m
    if scale:
        pb.scale = (scale, scale, scale)
    bpy.context.view_layer.update()


def front_render_rest():
    pass


# ---------------- materials: toon ----------------
mat0 = body.data.materials[0]
tex_img = base_image(mat0)
if tex_img is None:
    raise SystemExit("pose_render: material %r has no image texture" % mat0.name)
print("TEXTURE", tex_img.name, tex_img.size[:])


def toon_material(name, base=None, img=None):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    dif = nt.nodes.new("ShaderNodeBsdfDiffuse")
    dif.inputs["Color"].default_value = (1, 1, 1, 1)
    s2r = nt.nodes.new("ShaderNodeShaderToRGB")
    bw = nt.nodes.new("ShaderNodeRGBToBW")
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.interpolation = "CONSTANT"
    cr = ramp.color_ramp
    cr.elements[0].position = 0.0
    cr.elements[0].color = tuple(CFG.get("ramp0", (0.50, 0.42, 0.45))) + (1,)   # shadow, slightly cool
    cr.elements[1].position = 0.30
    cr.elements[1].color = tuple(CFG.get("ramp1", (0.80, 0.74, 0.70))) + (1,)   # mid
    e = cr.elements.new(0.62)
    e.color = tuple(CFG.get("ramp2", (1.0, 0.95, 0.86))) + (1,)                  # warm lit
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.blend_type = "MULTIPLY"
    mix.inputs["Factor"].default_value = 1.0
    if img is not None:
        t = nt.nodes.new("ShaderNodeTexImage")
        t.image = img
        t.interpolation = "Linear"
        nt.links.new(t.outputs["Color"], mix.inputs["A"])
    else:
        mix.inputs["A"].default_value = base
    em = nt.nodes.new("ShaderNodeEmission")
    nt.links.new(dif.outputs[0], s2r.inputs[0])
    nt.links.new(s2r.outputs["Color"], bw.inputs[0])
    nt.links.new(bw.outputs[0], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], mix.inputs["B"])
    nt.links.new(mix.outputs["Result"], em.inputs["Color"])
    nt.links.new(em.outputs[0], out.inputs["Surface"])
    return m


toon = toon_material("jakub_toon", img=tex_img)
sock = toon_material("jakub_sock", base=(0.42, 0.42, 0.41, 1))
body.data.materials.clear()
body.data.materials.append(toon)
body.data.materials.append(sock)

# ---------------- sock: left (far) foot loses its shoe ----------------
vg = {g.index: g.name for g in body.vertex_groups}
foot_groups = {P + "LeftFoot", P + "LeftToeBase"}
sock_verts = set()
for v in body.data.vertices:
    if not v.groups:
        continue
    g = max(v.groups, key=lambda g: g.weight)
    if vg[g.group] in foot_groups and v.co.z < 0.085 if True else False:
        sock_verts.add(v.index)
# glTF import keeps mesh in Y-up? check in world space instead
mw = body.matrix_world
sock_verts = set()
for v in body.data.vertices:
    if not v.groups:
        continue
    g = max(v.groups, key=lambda g: g.weight)
    w = mw @ v.co
    if vg[g.group] in foot_groups and w.z < 0.075 and w.x > 0.02:
        sock_verts.add(v.index)
for p in body.data.polygons:
    if sum(1 for i in p.vertices if i in sock_verts) >= 2:
        p.material_index = 1
print("SOCK verts", len(sock_verts))

# ---------------- real-world scale: rest height (feet to head) -> height_m ----------------
_zs = [(body.matrix_world @ v.co).z for v in body.data.vertices]
H_REST = max(_zs) - min(_zs)
_k = CFG.get("height_m", 1.8) / H_REST
root.scale = root.scale * _k
bpy.context.view_layer.update()
_zs = [(body.matrix_world @ v.co).z for v in body.data.vertices]
print("HEIGHT before", round(H_REST, 3), "after", round(max(_zs) - min(_zs), 3))

# ---------------- pose ----------------
C = CFG
for o in bpy.data.objects:
    o.select_set(False)
bpy.context.view_layer.objects.active = arm
bpy.ops.object.mode_set(mode="POSE")

if C.get("rest"):
    pass
else:
    aim("Spine", B(*C.get("spine", (-0.97, 0.22))))
    aim("Spine1", B(*C.get("spine1", (-0.95, 0.30))))
    aim("Spine2", B(*C.get("spine2", (-0.93, 0.36))))
    aim("Neck", B(*C.get("neck", (-0.97, -0.25))))
    aim("Head", B(*C.get("head", (-0.70, -0.71))), scale=C.get("head_scale"))
    # legs: near = Right (camera side), far = Left
    aim("RightUpLeg", B(*C.get("r_thigh", (0.95, 0.30, -0.05))))
    aim("RightLeg", B(*C.get("r_shin", (0.10, -0.99, -0.03))))
    aim("RightFoot", B(*C.get("r_foot", (0.85, -0.50))))
    aim("RightToeBase", B(*C.get("r_toe", (0.98, -0.2))))
    aim("LeftUpLeg", B(*C.get("l_thigh", (0.86, 0.50, 0.05))))
    aim("LeftLeg", B(*C.get("l_shin", (0.30, -0.95, 0.03))))
    aim("LeftFoot", B(*C.get("l_foot", (0.80, -0.60))), scale=C.get("sock_scale", 0.82))
    aim("LeftToeBase", B(*C.get("l_toe", (0.90, -0.45))))
    # near arm dangles
    aim("RightArm", B(*C.get("r_arm", (0.28, -0.96, -0.12))))
    aim("RightForeArm", B(*C.get("r_fore", (-0.05, -1.0, -0.06))))
    aim("RightHand", B(*C.get("r_hand", (0.05, -1.0, 0.0))), scale=C.get("hand_scale"))
    # far arm: hangs behind body
    aim("LeftArm", B(*C.get("l_arm", (0.15, -0.99, 0.15))))
    aim("LeftForeArm", B(*C.get("l_fore", (0.0, -1.0, 0.1))))
    aim("LeftHand", B(*C.get("l_hand", (0.0, -1.0, 0.0))))
    # generic config-driven tweaks: bone_scale {name:[x,y,z]} (pose-bone local), bone_rot {name:[x,y,z deg]},
    # no_inherit_scale [names] (child ignores parent's scale so values stay absolute)
    for n in C.get("no_inherit_scale", []):
        arm.data.bones[P + n].inherit_scale = "NONE"
    for n, r in C.get("bone_rot", {}).items():
        pb = arm.pose.bones.get(P + n)
        if pb:
            pb.rotation_mode = "XYZ"
            pb.rotation_euler = tuple(math.radians(a) for a in r)
    for n, sc_ in C.get("bone_scale", {}).items():
        pb = arm.pose.bones.get(P + n)
        if pb:
            pb.scale = tuple(sc_)
    bpy.context.view_layer.update()
bpy.ops.object.mode_set(mode="OBJECT")

# lay the whole thing down: body Z -> world -X, body -Y -> world +Z, body X -> world +Y
M = Matrix(((0, 0, -1), (1, 0, 0), (0, -1, 0))).to_4x4()
tilt = math.radians(C.get("tilt", 20.0))
roll = Matrix.Rotation(tilt, 4, "X")
if not C.get("rest"):
    root.matrix_world = roll @ M @ root.matrix_world
bpy.context.view_layer.update()

for n in ["Hips","Spine2","Head","RightUpLeg","RightLeg","RightFoot","LeftUpLeg","LeftLeg","RightArm","RightForeArm"]:
    pb=arm.pose.bones[P+n]
    h=arm.matrix_world@pb.head; t=arm.matrix_world@pb.tail
    print("PB",n,tuple(round(x,3) for x in h),tuple(round(x,3) for x in (t-h).normalized()), "constraints",len(pb.constraints))
print("MODS",[(m.type,getattr(m,'object',None) and m.object.name) for m in body.modifiers], "arm pose_position", arm.data.pose_position)
# ---------------- cull faces the pose stretched (tool handle / hook webbing) ----------------
import bmesh
dg = bpy.context.evaluated_depsgraph_get()
ev = body.evaluated_get(dg)
me = ev.to_mesh()
dpos = [v.co.copy() for v in me.vertices]
ev.to_mesh_clear()
rest = [v.co.copy() for v in body.data.vertices]
bm = bmesh.new()
bm.from_mesh(body.data)
bm.verts.ensure_lookup_table()
kill = []
LIM = C.get("stretch", 2.2)
for f in bm.faces:
    worst = 0
    for e in f.edges:
        a, b = e.verts[0].index, e.verts[1].index
        r = (rest[a] - rest[b]).length
        d = (dpos[a] - dpos[b]).length
        if r > 1e-6:
            worst = max(worst, d / r)
    if worst > LIM:
        kill.append(f)
# also drop the stub of the tool handle: rest-pose verts below/outside the right fist
mwi = REST_MW
for f in bm.faces:
    c = mwi @ f.calc_center_median()
    if c.x < -0.09 and 0.355 < c.z < 0.48 and (c.y < C.get("stick_y0", -0.085) or c.y > C.get("stick_y1", 0.03)):
        kill.append(f)
for f in bm.faces:
    c = mwi @ f.calc_center_median()
    for bx in C.get("cull_boxes", []):   # [xmin,xmax,ymin,ymax,zmin,zmax] rest world space; any vertex inside kills the face
        if any(bx[0] <= q.x <= bx[1] and bx[2] <= q.y <= bx[3] and bx[4] <= q.z <= bx[5]
               for q in (mwi @ rest[v.index] for v in f.verts)):
            kill.append(f)
kill = list(set(kill))
bmesh.ops.delete(bm, geom=kill, context="FACES")
loose = [v for v in bm.verts if not v.link_faces]
bmesh.ops.delete(bm, geom=loose, context="VERTS")
bm.to_mesh(body.data)
bm.free()
body.data.update()
print("CULLED faces", len(kill))
bpy.context.view_layer.update()

# ---------------- bbox of deformed mesh ----------------
dg = bpy.context.evaluated_depsgraph_get()
ev = body.evaluated_get(dg)
me = ev.to_mesh()
pts = [ev.matrix_world @ v.co for v in me.vertices]
ev.to_mesh_clear()
mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
ctr = (mn + mx) / 2
print("BBOX", tuple(mn), tuple(mx))

# ---------------- camera ----------------
pitch = math.radians(C.get("pitch", 17.0))
cam_d = bpy.data.cameras.new("cam")
cam_d.type = "ORTHO"
cam = bpy.data.objects.new("cam", cam_d)
bpy.context.scene.collection.objects.link(cam)
cam.rotation_euler = (math.pi / 2 - pitch, 0, 0)
fwd = Vector((0, math.cos(pitch), -math.sin(pitch)))
cam.location = ctr - fwd * 5
bpy.context.scene.camera = cam
sc = bpy.context.scene
up = Vector((0, math.sin(pitch), math.cos(pitch)))
span_x = (mx.x - mn.x)
proj = [p.dot(up) for p in pts]
pmin, pmax = min(proj), max(proj)
span_y = pmax - pmin
PPM = C.get("ppm")
if PPM:
    MARGIN = C.get("margin_px", 20)
    W = int(math.ceil(span_x * PPM)) + 2 * MARGIN
    H = int(math.ceil(span_y * PPM)) + 2 * MARGIN
    cam_d.ortho_scale = max(W, H) / PPM
    # centre camera on the projected bbox
    cx = (mn.x + mx.x) / 2
    cpy = (pmin + pmax) / 2
    base = Vector((cx, ctr.y, ctr.z))
    base = base + up * (cpy - base.dot(up))
    cam.location = base - fwd * 5
    sc.render.resolution_x, sc.render.resolution_y = W, H
    sc.render.resolution_percentage = 100

    def to_px(p):
        return (W / 2 + (p.x - cx) * PPM, H / 2 - (p.dot(up) - cpy) * PPM)
    for nm in ("Spine2", "Spine1", "Hips", "Head", "RightUpLeg", "RightLeg"):
        pb = arm.pose.bones[P + nm]
        print("PX", nm, tuple(round(v) for v in to_px(arm.matrix_world @ pb.head)))
    print("CANVAS", W, H)
else:
    W = 1024
    aspect = span_y / span_x
    H = int(W * min(1.0, aspect * 1.12 + 0.02))
    sc.render.resolution_x = W
    sc.render.resolution_y = max(H, 256)
    cam_d.ortho_scale = span_x * 1.08 if aspect < 1 else span_y * 1.12

# ---------------- lights ----------------
def sun(name, travel_dir, strength, color):
    ld = bpy.data.lights.new(name, "SUN")
    ld.energy = strength
    ld.color = color
    ld.use_shadow = C.get("shadows", False)
    ld.angle = math.radians(5)
    o = bpy.data.objects.new(name, ld)
    sc.collection.objects.link(o)
    o.rotation_euler = Vector(travel_dir).normalized().to_track_quat("-Z", "Y").to_euler()
    return o


sun("key", C.get("key_dir", (1.0, 0.8, -1.0)), C.get("key", 3.4), (1.0, 0.86, 0.66))
sun("fill", C.get("fill_dir", (-0.8, 1.0, -0.3)), C.get("fill", 1.0), (0.75, 0.82, 1.0))
world = bpy.data.worlds.new("w")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.08, 0.07, 0.07, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0
sc.world = world

# ---------------- render ----------------
eng = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
sc.render.engine = "BLENDER_EEVEE" if "BLENDER_EEVEE" in eng else "BLENDER_EEVEE_NEXT"
sc.render.film_transparent = True
sc.view_settings.view_transform = "Standard"
sc.view_settings.look = "None"
try:
    sc.eevee.taa_render_samples = C.get("samples", 16)
except Exception:
    pass
sc.render.image_settings.file_format = "PNG"
sc.render.image_settings.color_mode = "RGBA"
sc.render.filepath = os.path.abspath(os.path.join(OUT, f"render_{TAG}.png"))
bpy.ops.render.render(write_still=True)
print("RENDERED", sc.render.filepath, sc.render.resolution_x, sc.render.resolution_y)
if C.get("save_blend"):
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, C["save_blend"]))
    print("SAVED blend")
