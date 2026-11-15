"""Generic 8-direction renderer for any rigged (optionally animated) Tripo GLB.

blender -b --python tools/char3d/render_dirs.py -- <glb[,glb2,...]> <out_dir> <id> [config.json]

- GLBs: one or more (comma separated). Each may hold animation clips; clip names become <anim> folders
  (mapped by `anim_names` in config, else idle/walk guessed from the clip or file name, else the clip name).
  A GLB with no clip renders its rest pose as "idle" (1 frame).
- Output: <out_dir>/<anim>/<dir>/<NN>.png  (dirs S SE E NE N NW W SW), 640x640 transparent, 300 px/m, feet bottom-centre.
- Contact sheet (first frame of each dir per anim, <=1024 px wide): config "contact" path or <out_dir>/contact.png
- Config keys (all optional): height_m (1.8), ppm (300), canvas (640), pitch (17), idle_frames (6), walk_frames (8),
  anim_names {clip: name}, bone_scale {bone: [x,y,z]}  (e.g. {"Spine": [1.3,1,1.3]} for the Barbie-waist fix),
  look cfg keys (ramp0..2, key, fill, ...), contact, face_yaw (degrees added to the rotation, default 0).
  supersample (2): render at supersample x ppm/canvas, then Lanczos-downscale + light UnsharpMask (r1, 60%, t2) to ppm.
  center_z m: centre the camera on that world height (head close-up: canvas 1024, ppm 3413, only [idle, S], center_z 1.68).
  rest true: render the un-animated rest pose as anim "rest". idle_frame_offset N: start the idle clip N frames in.
  only [anim, dir] (+ only_frame N, default 0): render just that frame of that anim/dir (test frame, no contact sheet).
  cull_boxes [[xmin,xmax,ymin,ymax,zmin,zmax], ...]: delete mesh faces whose centre lies inside a box, in the
  mesh's own rest-pose space (GLB metres, before the height rescale). Use it to strip held props.
  bone_rot {bone: [x,y,z deg]}: pose-bone LOCAL euler offsets (as pose_render.py), applied to every frame.
  bone_rot_arm {bone: [x,y,z deg]}: rotations about the bone's head in ARMATURE axes (x = left/right, y = front/back,
    z = up; the model faces -y; +x rotates a downward limb backward). Rig-agnostic; applied parent-first, on top of
    any clip/procedural pose, every frame.
  bone_rot_body {bone: [x,y,z deg]}: like bone_rot_arm but x/y follow the body's facing (armature axes yawed by -face_yaw),
    so x is the body's left/right axis (pitch) and y its front/back axis (roll). Procedural cycles use these body axes.
  bone_rot_pitch {bone: deg} + head_axis_yaw (deg): pitch about a horizontal axis yawed from armature x; use it to
    tune a head lift that must read from both front and profile views.
  body_rot_scale_by_dir {dir: factor}: scale bone_rot_body per render direction (a head lift that reads from the
    front is too much in profile, so give E/W a smaller factor).
  strip_weights {pattern, below_z, keep_radius, hard_z (below it every matched weight goes: hand-in-pocket)}: remove arm/hand skin weights from shorts/leg vertices (see strip_weights()).
  bone_rot_body_dir {dir: {bone: [x,y,z]}}: extra body-axis rotations for one render direction (e.g. spine un-sway).
  mirror_texture_region {pick:"blue", bone:"Head", offset:.003, min_diff:.15, plane_from_frame:true}: recreate a lens that Tripo only textured on one side.
    Head-weighted faces whose base-colour texel is the "pick" colour (blue) are duplicated, mirrored across the head's
    left-right symmetry plane (normal at yaw plane_yaw, default -face_yaw, offset found by a symmetry scan of the head faces), reversed and
    nudged `offset` m outward (plane_from_frame: the plane passes through the middle of the white frame's lateral extent); they keep the original UVs, so they use the same lens texels.
  recolor_back_band {bone:"Head", ear_f:-.01, white_sat:.18, white_val:.75, k:6}: white frame texels (low saturation, bright)
    on Head-weighted faces BEHIND the ears (forward coordinate < ear_f from the head centre) are repainted in the base
    texture with colours of the nearest hair faces, so sunglasses pushed up on the head end at the ears instead of
    running round the back like a headband. Needs the mirror plane (same symmetry scan).
  rig "shared" + profile "<name|path>": the GLB is a shared_rig.py output (canonical skeleton, faces -Y, so face_yaw stays 0).
    idle/walk then come from tools/char3d/anim_lib/*.json retimed by tools/char3d/profiles/<profile>.json (shared_motion.py):
    cycle lengths, amplitudes, lean, per-direction head lift, swayback counter, static pose. Needs no procedural/strip/cull keys.
  render_anims [names]: only render these anims (others are left on disk untouched).
  ground_lock [anim, ...]: per frame, move the figure so the lowest point of the posed mesh sits on the floor (z=0);
    use on walk so the planted foot stays on the floor line instead of floating or sinking with the hip bounce.
  proc_params.walk_adduct (deg, 0): thighs toward the midline during the walk (narrows a wide A-pose stance).
  procedural {anim: "breathe"|"walk"}: replace that anim's clip (or the missing clip) with a generated Mixamo-bone cycle
    of NFR frames (idle_frames/walk_frames). Tunables in proc_params: breathe_rise (m, .004), breathe_pitch (deg, 1.2),
    walk_stride (deg, 17), walk_knee (deg, 38), walk_arm (deg, 16), walk_elbow (deg, 14), leg_len (m, .45),
    walk_bob (m, .004). The walk is in place and loops (frame N == frame 0).
Prints <=5 lines.
"""
import bpy, sys, os, json, math, subprocess
from mathutils import Vector, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import look

argv = sys.argv[sys.argv.index("--") + 1:]
GLBS = argv[0].split(",")
OUT, CID = os.path.abspath(argv[1]), argv[2]
CFG = json.loads(open(argv[3]).read()) if len(argv) > 3 else {}
PPM, CAN, PITCH = CFG.get("ppm", 300), CFG.get("canvas", 640), math.radians(CFG.get("pitch", 17.0))
SS = max(1, int(CFG.get("supersample", 2)))
ONLY = CFG.get("only")
_PP = """import sys
from PIL import Image, ImageFilter
src, dst, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
im = Image.open(src).convert("RGBA")
im = im.resize((im.width // n, im.height // n), Image.LANCZOS)
im = im.filter(ImageFilter.UnsharpMask(radius=1, percent=60, threshold=2))
im.save(dst)
"""


def render_frame(scene, path):
    if SS == 1:
        look.render(scene, path)
        return
    tmp = path + ".ss.png"
    look.render(scene, tmp)
    subprocess.run(["python", "-c", _PP, tmp, path, str(SS)], check=True)
    os.remove(tmp)
DIRS = ["S", "SE", "E", "NE", "N", "NW", "W", "SW"]
NFR = {"idle": CFG.get("idle_frames", 6), "walk": CFG.get("walk_frames", 8)}
SHARED = None
if CFG.get("rig") == "shared":
    import shared_motion
    SHARED = shared_motion.Motion(CFG["profile"])
    NFR = {k: SHARED.frames(k, v) for k, v in NFR.items()}
P = "mixamorig:"

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.resolution_x = sc.render.resolution_y = CAN * SS
sc.render.resolution_percentage = 100
look.lights(sc, CFG)

cam_d = bpy.data.cameras.new("cam")
cam_d.type = "ORTHO"
cam_d.ortho_scale = CAN / PPM  # framing unchanged; resolution is SS x
cam = bpy.data.objects.new("cam", cam_d)
sc.collection.objects.link(cam)
cam.rotation_euler = (math.pi / 2 - PITCH, 0, 0)
fwd = Vector((0, math.cos(PITCH), -math.sin(PITCH)))
up = Vector((0, math.sin(PITCH), math.cos(PITCH)))
sc.camera = cam
# feet (world origin) land at bottom-centre, 20 px above the edge
foot_px = 44
cam.location = Vector((0, 0, 0)) + up * (CAN / 2 - foot_px) / PPM - fwd * 10
if CFG.get("center_z"):   # close-up: frame centred on world height center_z (m); set canvas/ppm for the zoom, e.g. canvas 1024 ppm 3413 = 0.3 m
    cam.location = Vector((0, 0, CFG["center_z"])) - fwd * 10


def _head_faces(me_o, bm, bone):
    import numpy as np
    dl = bm.verts.layers.deform.active
    gi = [g.index for g in me_o.vertex_groups if g.name.split(":")[-1] in (bone, bone + "Top_End")]
    img = None
    for n in (me_o.data.materials[0].node_tree.nodes if me_o.data.materials[0] and me_o.data.materials[0].node_tree else []):
        if n.type == "TEX_IMAGE" and n.image and any(l.to_socket.name == "Base Color" for o in n.outputs for l in o.links):
            img = n.image
    if img is None or dl is None or not gi:
        return None
    w, h = img.size
    px = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4)
    uv = bm.loops.layers.uv.active
    F, C, col, SM = [], [], [], []
    for f in bm.faces:
        wgt = sum(sum(v[dl].get(g, 0) for g in gi) for v in f.verts) / len(f.verts)
        if wgt <= 0.5:
            continue
        u = sum((l[uv].uv for l in f.loops), Vector((0, 0))) / len(f.loops)
        F.append(f)
        C.append(list(f.calc_center_median()))
        col.append(px[min(h - 1, max(0, int(u.y * h))), min(w - 1, max(0, int(u.x * w)))][:3])
        sm = []
        for l in f.loops:   # extra samples: halfway from the centre to each corner
            q = (u + l[uv].uv) / 2
            sm.append(px[min(h - 1, max(0, int(q.y * h))), min(w - 1, max(0, int(q.x * w)))][:3])
        SM.append(sm[:3] + [sm[0]] * (3 - len(sm)))
    return img, px, uv, F, np.array(C), np.array(col), np.array(SM)


def _sym_plane(C):
    """Left-right symmetry plane of the head face centres: returns (centre point, unit normal) in mesh space."""
    import numpy as np
    rng = np.random.RandomState(1)
    P = C[rng.choice(len(C), min(700, len(C)), replace=False)]
    c0 = C.mean(0)

    def err(th, d):
        n = np.array([math.cos(th), math.sin(th), 0.0])
        c = c0 + n * d
        Q = P - 2 * ((P - c) @ n)[:, None] * n[None]
        return np.mean(np.sqrt(((Q[:, None, :] - P[None]) ** 2).sum(-1)).min(1))
    th = math.radians(CFG.get("plane_yaw", -CFG.get("face_yaw", 0)))   # head lateral axis in mesh space (mesh yaw vs armature)
    bd = min((err(th, d / 1000.0), d / 1000.0) for d in range(-30, 31, 3))[1]
    n = np.array([math.cos(th), math.sin(th), 0.0])
    return c0 + n * bd, n


def fix_sunglasses(meshes):
    import bmesh, numpy as np
    mr, bb = CFG.get("mirror_texture_region"), CFG.get("recolor_back_band")
    if not (mr or bb):
        return
    for me_o in meshes:
        bm = bmesh.new()
        bm.from_mesh(me_o.data)
        bm.faces.ensure_lookup_table()
        bone = (mr or bb).get("bone", "Head")
        hf = _head_faces(me_o, bm, bone)
        if hf is None:
            bm.free()
            continue
        img, px, uv, F, C, col, SM = hf
        c, n = _sym_plane(C)
        fwd = np.array([n[1], -n[0], 0.0])
        if fwd[1] > 0:
            fwd = -fwd   # the model faces -y
        mx, mn = col.max(1), col.min(1)
        sat = (mx - mn) / np.maximum(mx, 1e-4)
        if mr and mr.get("plane_from_frame", True):   # sunglasses are centred on the frame, not the head: put the plane mid-frame
            wf = (sat < 0.18) & (mx > 0.75) & (C[:, 2] > c[2]) & ((C - c) @ fwd > 0.02)
            if wf.sum() > 3:
                lt = (C[wf] - c) @ n
                c = c + n * (lt.min() + lt.max()) / 2
        info = ["plane n=(%.2f,%.2f) c=(%.3f,%.3f,%.3f)" % (n[0], n[1], c[0], c[1], c[2])]
        if bb:
            allc = np.concatenate([col[:, None], SM], 1)   # centre + 3 samples per face
            amx, amn = allc.max(2), allc.min(2)
            iswhite = ((amx - amn) / np.maximum(amx, 1e-4) < bb.get("white_sat", 0.18)) & (amx > bb.get("white_val", 0.75))
            white = (iswhite.sum(1) >= 2) & ((C - c) @ fwd < bb.get("ear_f", -0.01))
            blue = (col[:, 2] > col[:, 0] + 0.15) & (col[:, 2] > col[:, 1] + 0.05)
            hair = (iswhite.sum(1) == 0) & ~blue & ((C - c) @ fwd < bb.get("ear_f", -0.01) + 0.03)
            hi = np.where(hair)[0]
            h, w = px.shape[:2]
            rng = np.random.RandomState(2)
            for wi in np.where(white)[0]:
                d = ((C[hi] - C[wi]) ** 2).sum(1)
                near = hi[np.argsort(d)[:bb.get("k", 6)]]
                tri = np.array([[l[uv].uv.x * w, l[uv].uv.y * h] for l in F[wi].loops])
                x0, y0 = np.floor(tri.min(0) - 1).astype(int).clip(0, [w - 1, h - 1])
                x1, y1 = np.ceil(tri.max(0) + 1).astype(int).clip(0, [w - 1, h - 1])
                ys, xs = np.mgrid[y0:y1 + 1, x0:x1 + 1]
                inside = np.zeros(xs.shape, bool)
                for t in range(1, len(tri) - 1):   # fan-triangulate, dilated by 1 px
                    a, b2, c2 = tri[0], tri[t], tri[t + 1]
                    d0 = (b2[0] - a[0]) * (c2[1] - a[1]) - (c2[0] - a[0]) * (b2[1] - a[1])
                    if abs(d0) < 1e-9:
                        continue
                    l1 = ((xs + .5 - a[0]) * (c2[1] - a[1]) - (c2[0] - a[0]) * (ys + .5 - a[1])) / d0
                    l2 = ((b2[0] - a[0]) * (ys + .5 - a[1]) - (xs + .5 - a[0]) * (b2[1] - a[1])) / d0
                    inside |= (l1 >= -.2) & (l2 >= -.2) & (l1 + l2 <= 1.2)
                pick = near[rng.randint(0, len(near), inside.sum())]
                px[ys[inside], xs[inside], :3] = col[pick]
            img.pixels.foreach_set(px.ravel())
            img.update()
            info.append("band faces repainted %d" % white.sum())
        if mr:
            blue = (col[:, 2] > col[:, 0] + mr.get("min_diff", 0.15)) & (col[:, 2] > col[:, 1] + 0.05)
            lens = [F[i] for i in np.where(blue)[0]]
            if lens:
                me_o["orig_nv"] = len(bm.verts)   # centring ignores the added lens verts so the figure does not shift
                dup = bmesh.ops.duplicate(bm, geom=lens)["geom"]
                nv = [g for g in dup if isinstance(g, bmesh.types.BMVert)]
                nf = [g for g in dup if isinstance(g, bmesh.types.BMFace)]
                for v in nv:
                    p = np.array(list(v.co))
                    q = p - 2 * np.dot(p - c, n) * n
                    q = q + (q - c) / max(np.linalg.norm(q - c), 1e-6) * mr.get("offset", 0.003)
                    v.co = Vector(q)
                bmesh.ops.reverse_faces(bm, faces=nf)
            info.append("lens faces mirrored %d" % len(lens))
        bm.to_mesh(me_o.data)
        bm.free()
        me_o.data.update()
        print("SUNGLASSES", "; ".join(info))


def cull_faces(meshes):
    import bmesh
    boxes = CFG.get("cull_boxes", [])
    if not boxes:
        return
    killed = 0
    for me_o in meshes:
        bm = bmesh.new()
        bm.from_mesh(me_o.data)
        bm.faces.ensure_lookup_table()
        kill = [f for f in bm.faces if any(
            b[0] <= (c := f.calc_center_median()).x <= b[1] and b[2] <= c.y <= b[3] and b[4] <= c.z <= b[5] for b in boxes)]
        killed += len(kill)
        bmesh.ops.delete(bm, geom=kill, context="FACES")
        bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context="VERTS")
        bm.to_mesh(me_o.data)
        bm.free()
        me_o.data.update()
    CULLED[0] += killed


CULLED = [0]
STRIPPED = [0]


def strip_weights(meshes, arm):
    """strip_weights {pattern: regex of bone names (default 'Arm|Hand'), below_z: m, keep_radius: m (.06)}:
    below below_z (mesh rest space), a matched bone keeps its weight on a vertex only if the vertex lies within
    keep_radius of that bone's rest segment (so real hands/forearms keep theirs); other matched weights are dropped
    and the rest renormalised. A vertex left with no weight goes to the nearest unmatched bone."""
    import re
    cfg = CFG.get("strip_weights")
    if not cfg:
        return
    rx = re.compile(cfg.get("pattern", "Arm|Hand"))
    zmax, rad, hard = cfg.get("below_z", 0.58), cfg.get("keep_radius", 0.06), cfg.get("hard_z", -1)
    mw = arm.matrix_world
    seg = {b.name: (mw @ b.head_local, mw @ b.tail_local) for b in arm.data.bones}

    def dist(p, a, b):
        ab = b - a
        t = 0.0 if ab.length_squared == 0 else max(0.0, min(1.0, (p - a).dot(ab) / ab.length_squared))
        return (p - (a + ab * t)).length
    near_pool = [n for n in seg if not rx.search(n) and not any(k in n for k in ("Shoulder", "Head", "Neck", "Toe"))]
    for o in meshes:
        match = {g.index: g.name for g in o.vertex_groups if rx.search(g.name)}
        names = {g.index: g.name for g in o.vertex_groups}
        for v in o.data.vertices:
            pw = o.matrix_world @ v.co
            if pw.z >= zmax:
                continue
            ws = [(g.group, g.weight) for g in v.groups]
            drop = [i for i, w in ws if i in match and (pw.z < hard or dist(pw, *seg[match[i]]) > rad)]
            if not drop:
                continue
            keep = [(i, w) for i, w in ws if i not in drop]
            for i in drop:
                o.vertex_groups[i].remove([v.index])
            tot = sum(w for _, w in keep)
            if tot > 1e-6:
                for i, w in keep:
                    o.vertex_groups[i].add([v.index], w / tot, "REPLACE")
            else:
                nb = min(near_pool, key=lambda n: dist(pw, *seg[n]))
                o.vertex_groups[next(g.index for g in o.vertex_groups if g.name == nb)].add([v.index], 1.0, "REPLACE")
            STRIPPED[0] += 1


def import_one(path):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=path)
    new = [o for o in bpy.data.objects if o not in before]
    for o in [o for o in new if o.name.startswith("Icosphere")]:
        bpy.data.objects.remove(o, do_unlink=True)
    new = [o for o in bpy.data.objects if o not in before]
    arm = next(o for o in new if o.type == "ARMATURE")
    meshes = [o for o in new if o.type == "MESH"]
    cull_faces(meshes)
    fix_sunglasses(meshes)
    strip_weights(meshes, arm)
    root = arm
    while root.parent:
        root = root.parent
    return arm, meshes, root


def toonify(meshes):
    for body in meshes:
        mats = []
        for m in body.data.materials:
            img = None
            if m and m.node_tree:
                for n in m.node_tree.nodes:
                    if n.type == "TEX_IMAGE" and n.image:
                        for l in n.outputs["Color"].links:
                            if l.to_socket.name == "Base Color":
                                img = n.image
                        if img is None:
                            img = n.image
            mats.append(look.toon_material("toon_" + (m.name if m else "x"), img=img, base=None if img else (0.8, 0.8, 0.8, 1), cfg=CFG))
        body.data.materials.clear()
        for m in mats or [look.toon_material("toon", base=(0.8, 0.8, 0.8, 1), cfg=CFG)]:
            body.data.materials.append(m)


def rest_height(meshes, root):
    """World-space height of the evaluated mesh at its current (rest) pose."""
    dg = bpy.context.evaluated_depsgraph_get()
    zs = []
    for b in meshes:
        e = b.evaluated_get(dg)
        me = e.to_mesh()
        zs += [(e.matrix_world @ v.co).z for v in me.vertices]
        e.to_mesh_clear()
    return min(zs), max(zs)


def export_posed(meshes, path):
    """Bake the current pose into plain meshes (original texture, no rig) and export them as one GLB."""
    dg = bpy.context.evaluated_depsgraph_get()
    outs = []
    for b in meshes:
        e = b.evaluated_get(dg)
        me = bpy.data.meshes.new_from_object(e)
        me.transform(e.matrix_world)
        me.materials.clear()
        for m in b.data.materials:
            img = next((n.image for n in m.node_tree.nodes if n.type == "TEX_IMAGE" and n.image), None) if m and m.node_tree else None
            pm = bpy.data.materials.new("posed_" + m.name); pm.use_nodes = True
            if img:
                t = pm.node_tree.nodes.new("ShaderNodeTexImage"); t.image = img
                bsdf = pm.node_tree.nodes["Principled BSDF"]
                pm.node_tree.links.new(t.outputs["Color"], bsdf.inputs["Base Color"])
                bsdf.inputs["Roughness"].default_value = 1.0
            me.materials.append(pm)
        o = bpy.data.objects.new("posed_" + b.name, me)
        sc.collection.objects.link(o)
        outs.append(o)
    bpy.ops.object.select_all(action="DESELECT")
    for o in outs:
        o.select_set(True)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=path, use_selection=True, export_format="GLB", export_animations=False, export_skins=False)
    print("POSED GLB", path)
    for o in outs:
        bpy.data.objects.remove(o, do_unlink=True)


PROC = CFG.get("procedural", {})
if SHARED:
    PROC = dict(PROC) or {"idle": "lib:idle", "walk": "lib:walk"}
PP = dict(breathe_rise=0.004, breathe_pitch=1.2, walk_stride=17, walk_knee=38, walk_arm=16, walk_elbow=14,
          leg_len=0.45, walk_bob=0.004)
PP.update(CFG.get("proc_params", {}))
_by = -math.radians(CFG.get("face_yaw", 0))   # body facing vs armature: lateral/forward axes of the body
AX = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1),
      "bx": (math.cos(_by), math.sin(_by), 0), "by": (-math.sin(_by), math.cos(_by), 0)}


def depth(pb):
    d = 0
    while pb.parent:
        pb, d = pb.parent, d + 1
    return d


def rot_arm(arm, name, axis, deg):
    pb = arm.pose.bones.get(P + name)
    if pb is None or not deg:
        return
    h = pb.head.copy()
    M = Matrix.Translation(h) @ Matrix.Rotation(math.radians(deg), 4, Vector(AX[axis] if isinstance(axis, str) else axis)) @ Matrix.Translation(-h)
    pb.matrix = M @ pb.matrix
    bpy.context.view_layer.update()


def move_arm(arm, name, dz):
    pb = arm.pose.bones.get(P + name)
    if pb is None or not dz:
        return
    pb.matrix = Matrix.Translation((0, 0, dz)) @ pb.matrix
    bpy.context.view_layer.update()


def proc_ops(kind, i, n):
    """-> (list of (bone, axis, deg), list of (bone, dz)) for frame i of n."""
    if kind.startswith("lib:"):
        return SHARED.ops(kind[4:], i, n)
    ph = 2 * math.pi * i / n
    rot, mv = [], []
    if kind == "breathe":
        s = math.sin(ph)
        rot += [("Spine", "bx", -PP["breathe_pitch"] * 0.5 * s), ("Spine1", "bx", -PP["breathe_pitch"] * s)]
        mv += [("Spine2", PP["breathe_rise"] * s), ("LeftShoulder", PP["breathe_rise"] * 0.6 * s),
               ("RightShoulder", PP["breathe_rise"] * 0.6 * s)]
    elif kind == "walk":
        A, K, AA, E = PP["walk_stride"], PP["walk_knee"], PP["walk_arm"], PP["walk_elbow"]
        dz = 0.0
        for side, off in (("Left", 0.0), ("Right", math.pi)):
            p = ph + off
            fwd = A * math.sin(p)                       # forward swing of the thigh (deg)
            flex = K * max(0.0, math.cos(p)) ** 1.5 + 4  # knee bends through the swing phase
            thigh_back = -fwd
            rot += [(side + "UpLeg", "bx", thigh_back), (side + "Leg", "bx", flex),
                    (side + "Foot", "bx", -(thigh_back + flex) * 0.8),
                    (side + "Arm", "bx", AA * math.sin(p)),      # opposite arm: forward when other leg is back
                    (side + "ForeArm", "bx", -E - 4 * max(0.0, -math.sin(p)))]
            dz = min(dz, -PP["leg_len"] * (1 - math.cos(math.radians(abs(fwd)))))
        AD = PP.get("walk_adduct", 0)   # deg: swing both thighs toward the midline (a wide Tripo A-pose stance reads as hopping in profile)
        if AD:
            rot += [("LeftUpLeg", "by", AD), ("RightUpLeg", "by", -AD), ("LeftFoot", "by", -AD), ("RightFoot", "by", AD)]
        mv += [("Hips", dz + PP["walk_bob"] * math.cos(2 * ph) - PP["walk_bob"])]
        rot += [("Spine1", "z", 2.5 * math.sin(ph)), ("Hips", "z", -3 * math.sin(ph))]
    return rot, mv


CUR_DIR = ["S"]


def set_pose(arm, key, act, i, n, fr):
    kind = PROC.get(key)
    if kind or act is None:   # generated / rest pose: start from identity
        for pb in arm.pose.bones:
            pb.location = (0, 0, 0)
            pb.rotation_mode = "QUATERNION"
            pb.rotation_quaternion = (1, 0, 0, 0)
            pb.scale = (1, 1, 1)
        for k, v in CFG.get("bone_scale", {}).items():
            pb = arm.pose.bones.get(P + k)
            if pb:
                pb.scale = tuple(v)
    else:
        sc.frame_set(fr)
    bpy.context.view_layer.update()
    rot, mv = proc_ops(kind, i, n) if kind else ([], [])
    for b, dz in mv:
        move_arm(arm, b, dz)
    rot = sorted(rot, key=lambda r: depth(arm.pose.bones[P + r[0]]) if arm.pose.bones.get(P + r[0]) else 0)
    for b, ax, dg in rot:
        rot_arm(arm, b, ax, dg)
    ra = CFG.get("bone_rot_arm", {})
    for b in sorted(ra, key=lambda b: depth(arm.pose.bones[P + b]) if arm.pose.bones.get(P + b) else 0):
        for ax, dg in zip("xyz", ra[b]):
            rot_arm(arm, b, ax, dg)
    rp = CFG.get("bone_rot_pitch", {})   # {bone: deg} about a horizontal axis at head_axis_yaw (deg, default -face_yaw)
    ha = math.radians(CFG.get("head_axis_yaw", math.degrees(_by)))
    for b in sorted(rp, key=lambda b: depth(arm.pose.bones[P + b]) if arm.pose.bones.get(P + b) else 0):
        rot_arm(arm, b, (math.cos(ha), math.sin(ha), 0), rp[b])
    k = CFG.get("body_rot_scale_by_dir", {}).get(CUR_DIR[0], 1.0)
    rb = {b: [a * k for a in v] for b, v in CFG.get("bone_rot_body", {}).items()}
    for b, v in CFG.get("bone_rot_body_dir", {}).get(CUR_DIR[0], {}).items():
        rb[b] = [a + c for a, c in zip(rb.get(b, [0, 0, 0]), v)]
    if SHARED:
        for b, v in SHARED.static(CUR_DIR[0]).items():
            rb[b] = [a + c for a, c in zip(rb.get(b, [0, 0, 0]), v)]
    for b in sorted(rb, key=lambda b: depth(arm.pose.bones[P + b]) if arm.pose.bones.get(P + b) else 0):
        for ax, dg in zip(("bx", "by", "z"), rb[b]):
            rot_arm(arm, b, ax, dg)
    for b, r in CFG.get("bone_rot", {}).items():
        pb = arm.pose.bones.get(P + b)
        if pb:
            pb.rotation_mode = "XYZ"
            pb.rotation_euler = tuple(math.radians(a) for a in r)
    bpy.context.view_layer.update()


entries = []   # (anim_key, arm, meshes, root, action)
h_before = h_after = None
for gi, g in enumerate(GLBS):
    arm, meshes, root = import_one(g)
    if arm.animation_data:
        arm.animation_data.action = None
    for pb in arm.pose.bones:
        pb.location = (0, 0, 0)
        pb.rotation_quaternion = (1, 0, 0, 0)
        pb.rotation_euler = (0, 0, 0)
        pb.scale = (1, 1, 1)
    bpy.context.view_layer.update()
    lo, hi = rest_height(meshes, root)
    hb = hi - lo
    root.scale = root.scale * (CFG.get("height_m", 1.8) / hb)
    bpy.context.view_layer.update()
    lo, hi = rest_height(meshes, root)
    root.location.z -= lo
    bpy.context.view_layer.update()
    if gi == 0:
        h_before, h_after = hb, hi - lo
    toonify(meshes)
    acts = [a for a in bpy.data.actions if not any(a is e[4] for e in entries)]
    acts = acts or [None]
    for act in acts:
        nm = ((act.name if act else "") + " " + os.path.basename(g)).lower()
        key = CFG.get("anim_names", {}).get(act.name if act else "")
        key = key or ("walk" if ("walk" in nm or "run" in nm) else "idle" if ("idle" in nm or "stand" in nm) or not act else act.name)
        entries.append((key, arm, meshes, root, act))

if PROC:
    first = entries[0]
    entries = [e for e in entries if e[0] not in PROC] + [(k,) + first[1:4] + (None,) for k in PROC]
if CFG.get("rest"):   # render the bind/rest pose only, as anim "rest"
    entries = [("rest",) + entries[0][1:4] + (None,)]

# centre x/y on the first model's rest bbox; same offset for every root
dg = bpy.context.evaluated_depsgraph_get()
pts = []
for b in entries[0][2]:
    e = b.evaluated_get(dg)
    me = e.to_mesh()
    pts += [e.matrix_world @ v.co for v in list(me.vertices)[:b.get('orig_nv', len(me.vertices))]]
    e.to_mesh_clear()
cx = sum(p.x for p in pts) / len(pts)
cy = sum(p.y for p in pts) / len(pts)
for r in {id(e[3]): e[3] for e in entries}.values():
    r.location.x -= cx
    r.location.y -= cy
bpy.context.view_layer.update()
for e in entries:
    for k, v in CFG.get("bone_scale", {}).items():
        pb = e[1].arm if False else e[1].pose.bones.get(P + k)
        if pb:
            pb.scale = tuple(v)
rest_mw = {id(e[3]): e[3].matrix_world.copy() for e in entries}
yaw0 = math.radians(CFG.get("face_yaw", 0))

sheet = []
nframes = {}
for key, arm, meshes, root, act in entries:
    for k2, a2, m2, r2, ac2 in entries:
        for m in m2:
            m.hide_render = not (m2 is meshes)
    if arm.animation_data is None:
        arm.animation_data_create()
    arm.animation_data.action = act
    f0, f1 = (int(act.frame_range[0]), int(act.frame_range[1])) if act else (1, 1)
    n = NFR.get(key, 6) if (act and f1 > f0) or key in PROC else 1
    nframes[key] = n
    if CFG.get("render_anims") and key not in CFG["render_anims"]:
        continue
    frames = [round(f0 + (f1 - f0) * i / n) for i in range(n)] if n > 1 else [f0]
    if key == "idle" and act:
        off = CFG.get("idle_frame_offset", 0)   # shifts which clip frame is frame 00
        frames = [f0 + (fr - f0 + off) % max(1, f1 - f0 + 1) for fr in frames]
    for di, dname in enumerate(DIRS):
        if ONLY and (key != ONLY[0] or dname != ONLY[1]):
            continue
        d = os.path.join(OUT, key, dname)
        os.makedirs(d, exist_ok=True)
        for fi, fr in enumerate(frames):
            if ONLY and fi != CFG.get("only_frame", 0):
                continue
            CUR_DIR[0] = dname
            set_pose(arm, key, act, fi, n, fr)
            root.matrix_world = Matrix.Rotation(math.radians(45 * di) + yaw0, 4, "Z") @ rest_mw[id(root)]
            bpy.context.view_layer.update()
            if key in CFG.get("ground_lock", []):   # plant the lowest point of the posed mesh on z=0 (stops walk float/sink; Pilsner G4 2026-11-14)
                lo_g, _ = rest_height(meshes, root)
                root.matrix_world = Matrix.Translation((0, 0, -lo_g)) @ root.matrix_world
                bpy.context.view_layer.update()
            p = os.path.join(d, "%02d.png" % fi)
            if CFG.get("export_glb"):   # with "only": write this one posed frame as a static GLB instead of rendering (in-game 3D mock shots, Eurobound-8c3z)
                export_posed(meshes, CFG["export_glb"])
                continue
            render_frame(sc, p)
            if fi == 0:
                sheet.append((key, dname, p))
results = {e[0]: None for e in entries}
if ONLY:
    print('TEST FRAME', os.path.join(OUT, ONLY[0], ONLY[1], '00.png'))
    raise SystemExit

# ---------------- contact sheet ----------------
import numpy as np
tile = 128
cols = len(DIRS)
rows = len(results)
img = np.zeros((rows * tile, cols * tile, 4), dtype=np.float32)
img[..., :3] = 0.55
img[..., 3] = 1
for (k, dname, p) in sheet:
    im = bpy.data.images.load(p)
    w, h = im.size
    a = np.array(im.pixels[:], dtype=np.float32).reshape(h, w, 4)
    # crop the canvas to the figure region then downscale by 5 (640 -> 128)
    s = w // tile
    a = a.reshape(tile, s, tile, s, 4).mean(axis=(1, 3))
    ri = list(results).index(k)
    ci = DIRS.index(dname)
    y0 = (rows - 1 - ri) * tile
    al = a[..., 3:4]
    img[y0:y0 + tile, ci * tile:(ci + 1) * tile, :3] = a[..., :3] * al + 0.55 * (1 - al)
    bpy.data.images.remove(im)
cs = CFG.get("contact", os.path.join(OUT, "contact.png"))
os.makedirs(os.path.dirname(cs), exist_ok=True)
out_im = bpy.data.images.new("contact", cols * tile, rows * tile, alpha=True)
out_im.pixels = img.flatten().tolist()
out_im.filepath_raw = cs
out_im.file_format = "PNG"
out_im.save()
print("HEIGHT before", round(h_before, 3), "after", round(h_after, 3))
print("CULLED faces", CULLED[0], "stripped-weight verts", STRIPPED[0])
print("ANIMS", {k: nframes[k] for k in nframes}, "frames per dir")
print("CONTACT", cs)
