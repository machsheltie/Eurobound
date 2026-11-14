"""Build the canonical Eurobound skeleton from a Tripo rigged GLB (Mixamo bone names).

blender -b --python tools/char3d/shared_rig.py -- <id_rigged.glb> [--profile <name|path>] [--weights tripo|auto] [--yaw DEG] [--png]

Writes <id>_shared.glb next to the input (never overwrites the input; "_rigged" is dropped from the name).

What it does
- Canonical 22-bone skeleton, Mixamo names kept so render_dirs.py works unchanged: Hips Spine Spine1 Spine2 Neck Head,
  L/R Shoulder Arm ForeArm Hand UpLeg Leg Foot ToeBase. No finger/HeadTop/Toe_End bones: finger weights merge into the
  hand, HeadTop_End into the head, Toe_End into the toe.
- Joints sit on the Tripo joint positions. Every bone points down its chain (head -> next joint) with roll fixed so the
  local Z axis faces the character's front: same convention on every character.
- Facing: the Tripo skeleton gives the facing (toe direction + shoulder/hip line), then a mirror-symmetry scan of the mesh
  refines it. Mesh and skeleton are rotated together so the character faces -Y (render_dirs needs face_yaw 0). --yaw
  overrides the detected facing (deg, direction the character faces before alignment).
- Weights: Tripo weights remapped to the canonical bones, then cleaned: arm/hand/shoulder weights are removed from
  anything below the waist unless the vertex is within keep_radius of that bone (generalised strip_weights); sides listed
  in the profile's rig.pocket_sides lose them below the waist outright (hand-in-pocket). --weights auto uses Blender
  automatic weights instead (then the same cleanup).
- Profile (optional) `rig` section: {pocket_sides:["Right"], cull_boxes:[[xmin,xmax,ymin,ymax,zmin,zmax]], keep_radius_h:.046}
  cull_boxes are in the source mesh's rest space (delete held props before rigging).
Prints <=5 lines.
"""
import bpy, sys, os, json, math, re, bmesh
import numpy as np
from mathutils import Vector, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
argv = sys.argv[sys.argv.index("--") + 1:]
SRC = os.path.abspath(argv[0])


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


PROFILE = opt("--profile")
WEIGHTS = opt("--weights", "tripo")
YAW = opt("--yaw")
P = "mixamorig:"
prof = {}
if PROFILE:
    pp = PROFILE if os.path.isfile(PROFILE) else os.path.join(HERE, "profiles", PROFILE + ".json")
    prof = json.load(open(pp))
RIG = prof.get("rig", {})
base = os.path.basename(SRC)
cid = re.sub(r"(_rigged)?(_orig)?\.glb$", "", base)
OUT = os.path.join(os.path.dirname(SRC), cid + "_shared.glb")
assert os.path.abspath(OUT) != SRC

CORE = ["Hips", "Spine", "Spine1", "Spine2", "Neck", "Head"]
LIMB = ["Shoulder", "Arm", "ForeArm", "Hand", "UpLeg", "Leg", "Foot", "ToeBase"]
PARENT = {"Spine": "Hips", "Spine1": "Spine", "Spine2": "Spine1", "Neck": "Spine2", "Head": "Neck"}
for s in ("Left", "Right"):
    PARENT.update({s + "Shoulder": "Spine2", s + "Arm": s + "Shoulder", s + "ForeArm": s + "Arm", s + "Hand": s + "ForeArm",
                   s + "UpLeg": "Hips", s + "Leg": s + "UpLeg", s + "Foot": s + "Leg", s + "ToeBase": s + "Foot"})
NAMES = CORE + [s + l for s in ("Left", "Right") for l in LIMB]
NEXT = {"Hips": "Spine", "Spine": "Spine1", "Spine1": "Spine2", "Spine2": "Neck", "Neck": "Head"}
for s in ("Left", "Right"):
    NEXT.update({s + "Shoulder": s + "Arm", s + "Arm": s + "ForeArm", s + "ForeArm": s + "Hand",
                 s + "UpLeg": s + "Leg", s + "Leg": s + "Foot", s + "Foot": s + "ToeBase"})

# ---------------- import ----------------
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=SRC)
old_arm = next(o for o in bpy.data.objects if o.type == "ARMATURE")
mesh = max((o for o in bpy.data.objects if o.type == "MESH"), key=lambda o: len(o.vertex_groups))
assert len(mesh.vertex_groups) > 0, "no skinned mesh"
me = mesh.data
mesh.parent = None
me.transform(mesh.matrix_world)
mesh.matrix_world = Matrix.Identity(4)
SH = {}
for b in old_arm.data.bones:
    SH[b.name.split(":")[-1]] = old_arm.matrix_world @ b.head_local
amw = old_arm.matrix_world.copy()

# ---------------- optional prop cull (source space) ----------------
boxes = RIG.get("cull_boxes", [])
culled = 0
if boxes:
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    kill = [f for f in bm.faces if any(b[0] <= (c := f.calc_center_median()).x <= b[1] and b[2] <= c.y <= b[3]
                                       and b[4] <= c.z <= b[5] for b in boxes)]
    culled = len(kill)
    bmesh.ops.delete(bm, geom=kill, context="FACES")
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context="VERTS")
    bm.to_mesh(me)
    bm.free()
    me.update()

# ---------------- facing ----------------
V = np.array([v.co[:] for v in me.vertices], dtype=np.float64)
H = V[:, 2].max() - V[:, 2].min()


def hz(v):
    return Vector((v.x, v.y, 0))


toe = sum((hz(SH[s + "ToeBase"] - SH[s + "Foot"]) for s in ("Left", "Right")), Vector())
lat = hz(SH["LeftUpLeg"] - SH["RightUpLeg"]) + hz(SH["LeftArm"] - SH["RightArm"]) + hz(SH["LeftShoulder"] - SH["RightShoulder"])
a_toe = math.atan2(toe.y, toe.x)
a_sk = math.atan2(lat.y, lat.x) - math.pi / 2
if math.cos(a_sk - a_toe) < 0:
    a_sk += math.pi
rng = np.random.RandomState(3)
pts = V[(V[:, 2] > 0.12 * H) & (V[:, 2] < 0.95 * H)]
pts = pts[rng.choice(len(pts), min(500, len(pts)), replace=False)]


def sym_err(a):
    c, s = math.cos(-math.pi / 2 - a), math.sin(-math.pi / 2 - a)
    q = pts[:, :2] @ np.array([[c, s], [-s, c]])   # rotate by (-90deg - a): facing -> -y, lateral -> x
    m = np.median(q[:, 0])
    r = q.copy()
    r[:, 0] = 2 * m - r[:, 0]
    return np.sqrt(((r[:, None] - q[None]) ** 2).sum(-1)).min(1).mean()


if YAW is not None:
    a_fit = math.radians(float(YAW))
else:
    a_fit = min((sym_err(a_sk + math.radians(d)), a_sk + math.radians(d)) for d in np.arange(-35, 35.1, 1.5))[1]
    a_fit = min((sym_err(a_fit + math.radians(d)), a_fit + math.radians(d)) for d in np.arange(-1.5, 1.51, 0.25))[1]
rot = -math.pi / 2 - a_fit
R3 = Matrix.Rotation(rot, 3, "Z")
me.transform(Matrix.Rotation(rot, 4, "Z"))
V = np.array([v.co[:] for v in me.vertices], dtype=np.float64)
S = {k: R3 @ v for k, v in SH.items()}

# ---------------- canonical armature ----------------
bpy.data.objects.remove(old_arm, do_unlink=True)
for o in [o for o in bpy.data.objects if o is not mesh]:
    bpy.data.objects.remove(o, do_unlink=True)
arm_d = bpy.data.armatures.new("Armature")
arm_o = bpy.data.objects.new("Armature", arm_d)
bpy.context.scene.collection.objects.link(arm_o)
bpy.context.view_layer.objects.active = arm_o
bpy.ops.object.mode_set(mode="EDIT")
front = Vector((0, -1, 0))
up = Vector((0, 0, 1))
tails = {}
for n in NAMES:
    h = S[n]
    side = "Left" if n.startswith("Left") else "Right" if n.startswith("Right") else ""
    core = n[len(side):]
    if n in NEXT:
        t = S[NEXT[n]]
    elif n == "Head":
        t = S.get("HeadTop_End", h + (h - S["Neck"]))
    elif core == "Hand":
        fk = S.get(side + "HandMiddle1")
        d = h - S[side + "ForeArm"]
        t = fk if fk is not None and (fk - h).length > 0.02 else h + d.normalized() * 0.06
    elif core == "ToeBase":
        te = S.get(side + "ToeBase_End") or S.get(side + "Toe_End")
        t = te if te is not None else h + hz(h - S[side + "Foot"]).normalized() * 0.05
    else:
        t = h + up * 0.02
    if (t - h).length < 0.01:
        t = h + (t - h).normalized() * 0.01 if (t - h).length > 1e-6 else h + up * 0.02
    tails[n] = t
for n in NAMES:
    eb = arm_d.edit_bones.new(P + n)
    eb.head, eb.tail = S[n], tails[n]
    eb.use_deform = True
for n, p in PARENT.items():
    arm_d.edit_bones[P + n].parent = arm_d.edit_bones[P + p]
for n in NAMES:
    eb = arm_d.edit_bones[P + n]
    ref = up if abs((eb.tail - eb.head).normalized().dot(front)) > 0.85 else front
    eb.align_roll(ref)
bpy.ops.object.mode_set(mode="OBJECT")
arm_o["eurobound_rig"] = "shared_v1"
arm_o["yaw_applied_deg"] = round(math.degrees(rot), 2)
SEG = {n: (S[n].copy(), tails[n].copy()) for n in NAMES}

# ---------------- weights ----------------
cidx = {P + n: i for i, n in enumerate(NAMES)}


def remap(g):
    b = g.split(":")[-1]
    m = re.match(r"(Left|Right)Hand(Thumb|Index|Middle|Ring|Pinky)\d", b)
    if m:
        b = m.group(1) + "Hand"
    elif b == "HeadTop_End":
        b = "Head"
    elif b.endswith("Toe_End") or b.endswith("ToeBase_End"):
        b = b.replace("Toe_End", "ToeBase").replace("ToeBase_End", "ToeBase")
    return b if b in NAMES else None


def read_w(remapped):
    W = np.zeros((len(me.vertices), len(NAMES)))
    gn = {g.index: g.name for g in mesh.vertex_groups}
    for v in me.vertices:
        for g in v.groups:
            t = remap(gn[g.group]) if remapped else gn[g.group].split(":")[-1]
            if t in NAMES:
                W[v.index, NAMES.index(t)] += g.weight
    return W


for m in list(mesh.modifiers):
    mesh.modifiers.remove(m)
if WEIGHTS == "auto":
    mesh.vertex_groups.clear()
    mesh.parent = arm_o
    for o in bpy.data.objects:
        o.select_set(False)
    mesh.select_set(True)
    arm_o.select_set(True)
    bpy.context.view_layer.objects.active = arm_o
    with bpy.context.temp_override(active_object=arm_o, object=arm_o, selected_objects=[mesh, arm_o],
                                   selected_editable_objects=[mesh, arm_o]):
        bpy.ops.object.parent_set(type="ARMATURE_AUTO")
    W = read_w(False)
else:
    W = read_w(True)
    mesh.vertex_groups.clear()
    mesh.parent = arm_o
    mesh.matrix_parent_inverse = arm_o.matrix_world.inverted()
    mesh.modifiers.new("Armature", "ARMATURE").object = arm_o


def seg_dist(Pn, a, b):
    ab = np.array(b - a)
    t = np.clip(((Pn - np.array(a)) @ ab) / max(ab @ ab, 1e-12), 0, 1)
    return np.linalg.norm(Pn - (np.array(a) + t[:, None] * ab), axis=1)


spine_z = S["Spine"].z
keep_r = RIG.get("keep_radius_h", 0.046) * H
low = V[:, 2] < spine_z + 0.04 * H
stripped = np.zeros(len(V), bool)
# nearest distance to any non-arm body bone: arm-weighted skin that is nearer to the arm than to the body is real arm
# (fat hands/fingers out beyond keep_radius must not be stripped, or they snap to the hips and stretch when the arm swings)
other = [n for n in NAMES if re.search(r"^(Hips|Spine|Spine1|Spine2)$|UpLeg|Leg$|Foot", n)]
D_other = np.min(np.stack([seg_dist(V, *SEG[n]) for n in other], 1), 1)
for i, n in enumerate(NAMES):
    if not re.search("Arm|Hand|Shoulder", n):
        continue
    d = seg_dist(V, *SEG[n])
    hard = (V[:, 2] < spine_z) & (("Left" if n.startswith("Left") else "Right") in RIG.get("pocket_sides", []))
    drop = low & (((d > keep_r) & (d >= 0.85 * D_other)) | hard) & (W[:, i] > 0)
    W[drop, i] = 0
    stripped |= drop
pool = [i for i, n in enumerate(NAMES) if re.search(r"^(Hips|Spine|Spine1|Spine2)$|UpLeg|Leg$|Foot", n)]
dead = W.sum(1) < 1e-6
if dead.any():
    D = np.stack([seg_dist(V[dead], *SEG[NAMES[i]]) for i in pool], 1)
    W[np.where(dead)[0], np.array(pool)[D.argmin(1)]] = 1.0
W[W < 0.01] = 0
top = np.argsort(-W, 1)[:, 4:]
np.put_along_axis(W, top, 0, 1)
W /= np.maximum(W.sum(1, keepdims=True), 1e-9)
# Unweld: Tripo meshes sometimes fuse a hand to the thigh/hip where they touch (shared surface, ~2 mm edges). Faces that
# bridge an arm-dominant vertex and a body-dominant vertex below the waist stretch into a flat paddle when the arm
# swings, so delete them (the contact area is hidden between the two surfaces) and drop the orphaned verts.
armset = np.array([bool(re.search("Arm|Hand|Shoulder", n)) for n in NAMES])
bodyset = np.array([bool(re.search(r"^(Hips|Spine|Spine1|Spine2)$|UpLeg|Leg$|Foot", n)) for n in NAMES])
dom = W.argmax(1)
is_arm, is_body = armset[dom], bodyset[dom]
lowv = V[:, 2] < spine_z + 0.04 * H
bm = bmesh.new()
bm.from_mesh(me)
oid = bm.verts.layers.int.new("oid")
bm.verts.ensure_lookup_table()
for v in bm.verts:
    v[oid] = v.index
bm.faces.ensure_lookup_table()
bad = [f for f in bm.faces if all(lowv[v.index] for v in f.verts)
       and any(is_arm[v.index] for v in f.verts) and any(is_body[v.index] for v in f.verts)]
unwelded = len(bad)
if bad:
    bmesh.ops.delete(bm, geom=bad, context="FACES")
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context="VERTS")
    keep = np.array([v[oid] for v in bm.verts])
    bm.to_mesh(me)
    me.update()
    W = W[keep]
bm.free()
for n in NAMES:
    mesh.vertex_groups.new(name=P + n)
for j, n in enumerate(NAMES):
    vg = mesh.vertex_groups[P + n]
    for vi in np.nonzero(W[:, j])[0]:
        vg.add([int(vi)], float(W[vi, j]), "REPLACE")

# ---------------- export ----------------
for o in bpy.data.objects:
    o.select_set(True)
kw = dict(filepath=OUT, export_format="GLB", export_animations=False, export_skins=True, export_extras=True)
if "--png" not in argv:
    kw.update(export_image_format="JPEG", export_image_quality=92)
bpy.ops.export_scene.gltf(**kw)
print("SHARED", OUT, "%.1f MB" % (os.path.getsize(OUT) / 1e6))
print("FACING skeleton %.1f deg, mesh-fit %.1f deg, rotated %.1f deg; height %.3f m" % (
    math.degrees(a_sk), math.degrees(a_fit), math.degrees(rot), H))
print("BONES", len(NAMES), "stripped-weight verts", int(stripped.sum()), "culled faces", culled, "weights", WEIGHTS, "unwelded faces", unwelded)
