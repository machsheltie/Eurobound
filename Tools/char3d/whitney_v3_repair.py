# One-off repair of Woo Woo Whitney build 3 (2026-11-16): closes the Tripo forehead hole (4 boundary
# edges at x~-0.004, z~0.94, split at UV seams, so a face is built from one vertex per corner) and
# pulls the AI idle's Neck back over the chest each frame while keeping the head's world angle.
# Run: blender -b --factory-startup -P Tools/char3d/whitney_v3_repair.py -- <in.glb> <out.glb> <render_dir>

import bpy, bmesh, sys, os, math
import numpy as np
from mathutils import Vector, Matrix
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "item3d"))
from material_lookup import base_image   # follows the Principled Base Color link (Eurobound-2bb9)
argv=sys.argv[sys.argv.index('--')+1:]
glb, out_glb, outdir = argv[0], argv[1], argv[2]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
mesh=max([o for o in bpy.data.objects if o.type=='MESH'], key=lambda o: len(o.data.vertices))
for o in bpy.data.objects:
    if o.type=='MESH' and o!=mesh: o.hide_render=True
idle=[a for a in bpy.data.actions if 'walk' not in a.name.lower()][0]
sc=bpy.context.scene
arm.animation_data.action=None
for pb in arm.pose.bones: pb.matrix_basis.identity()
bpy.context.view_layer.update()

# ---- texture as numpy ----
img=next(i for i in (base_image(m) for m in mesh.data.materials) if i is not None)
W,H=img.size; px=np.empty(W*H*4,dtype=np.float32); img.pixels.foreach_get(px); px=px.reshape(H,W,4)
def tex(uv):
    x=int(min(max(uv.x,0),0.9999)*W); y=int(min(max(uv.y,0),0.9999)*H); return px[y,x,:3]
def lum(c): return float(0.299*c[0]+0.587*c[1]+0.114*c[2])

# ---- 1. forehead diamond: ray-cast the exact faces, remap dark ones to forehead skin ----
dg=bpy.context.evaluated_depsgraph_get()
bm=bmesh.new(); bm.from_mesh(mesh.data); bm.faces.ensure_lookup_table(); uvl=bm.loops.layers.uv.active
C=Vector((-0.0074,0,0.9428))
bnd=[e for e in bm.edges if len(e.link_faces)==1]
hole=[]
for e in bnd:
    m=(e.verts[0].co+e.verts[1].co)/2
    if abs(m.x-C.x)<0.010 and abs(m.z-C.z)<0.010 and m.y<-0.052: hole.append(e)
print('HOLE edges',len(hole),[tuple(round(c,4) for c in (e.verts[0].co+e.verts[1].co)/2) for e in hole][:16])
if hole:
    vs=[v for e in hole for v in e.verts]
    groups=[]
    for v in vs:
        for g in groups:
            if (g[0].co-v.co).length<1e-4: g.append(v); break
        else: groups.append([v])
    print('CORNERS',len(groups))
    corners=[g[0] for g in groups]
    cen=sum((v.co for v in corners),Vector())/len(corners)
    corners.sort(key=lambda v: math.atan2(v.co.z-cen.z, v.co.x-cen.x))
    try:
        f=bm.faces.new(corners)
    except ValueError as ex:
        print('FACE exists',ex); f=None
    if f:
        f.normal_update()
        if f.normal.y>0: f.normal_flip()
        for l in f.loops:
            uvs=[ol[uvl].uv.copy() for g in groups if l.vert in g for gv in g for ol in gv.link_loops if ol.face is not f]
            if uvs: l[uvl].uv=sum(uvs,Vector((0,0)))/len(uvs)
        nb=[ff for e in f.edges for ff in e.link_faces if ff is not f]
        if nb: f.material_index=nb[0].material_index
        print('FILLED face normal',tuple(round(c,2) for c in f.normal))
        bm.to_mesh(mesh.data); mesh.data.update()
bm.free()

# ---- 2. idle: neck back over chest, head forward vector back to rest ----
P=arm.pose.bones
neck=P['mixamorig:Neck']; head=P['mixamorig:Head']
def lean(a,b): d=b-a; return math.atan2(-d.y,d.z)
rest_neck=lean(neck.head, head.head)
R0=head.matrix.to_3x3()
cols=[R0.col[i] for i in range(3)]
k=max(range(3), key=lambda i: abs(cols[i].dot(Vector((0,-1,0)))))
sgn=1 if cols[k].dot(Vector((0,-1,0)))>0 else -1
def fwd(pb): return (pb.matrix.to_3x3().col[k]*sgn).normalized()
rest_pitch=math.asin(-fwd(head).z)
print('REST neck %.1f head pitch-down %.1f (axis %d)'%(math.degrees(rest_neck),math.degrees(rest_pitch),k))
arm.animation_data.action=idle
f0,f1=int(idle.frame_range[0]),int(idle.frame_range[1])
log=[]
for f in range(f0,f1+1):
    sc.frame_set(f); bpy.context.view_layer.update()
    ln=lean(neck.head,head.head)-rest_neck
    pd0=math.asin(-fwd(head).z)-rest_pitch
    p=neck.head.copy()
    neck.matrix=Matrix.Translation(p)@Matrix.Rotation(-ln,4,'X')@Matrix.Translation(-p)@neck.matrix
    bpy.context.view_layer.update(); neck.keyframe_insert('rotation_quaternion',frame=f)
    p2=head.head.copy()
    head.matrix=Matrix.Translation(p2)@Matrix.Rotation(ln,4,'X')@Matrix.Translation(-p2)@head.matrix
    bpy.context.view_layer.update(); head.keyframe_insert('rotation_quaternion',frame=f)
    pd1=math.asin(-fwd(head).z)-rest_pitch
    if f%15==1: log.append((f,round(math.degrees(ln),1),round(math.degrees(pd0),1),round(math.degrees(pd1),1)))
print('FRAME neck_lean_before head_pitch_before head_pitch_after:',log)

# ---- renders ----
cd=bpy.data.cameras.new('cam'); cd.type='ORTHO'; cam=bpy.data.objects.new('cam',cd); sc.collection.objects.link(cam); sc.camera=cam
sc.render.engine='BLENDER_WORKBENCH'; sc.render.resolution_x=500; sc.render.resolution_y=500
sh=sc.display.shading; sh.light='FLAT'; sh.color_type='TEXTURE'
cd.ortho_scale=0.5; cam.location=(2,0,0.75); cam.rotation_euler=(math.radians(90),0,math.radians(90))
for f in (1,60,110):
    sc.frame_set(f); sc.render.filepath=outdir+'/r10_idle_side_%03d.png'%f; bpy.ops.render.render(write_still=True)
arm.animation_data.action=None
for pb in P: pb.matrix_basis.identity()
bpy.context.view_layer.update()
cd.ortho_scale=0.22; cam.location=(0,-2,0.917); cam.rotation_euler=(math.radians(90),0,0)
sc.render.filepath=outdir+'/r10_face.png'; bpy.ops.render.render(write_still=True)
# ---- export ----
for o in bpy.data.objects: o.select_set(o in (arm,mesh))
bpy.ops.export_scene.gltf(filepath=out_glb, export_format='GLB', use_selection=True, export_animation_mode='ACTIONS', export_image_format='AUTO', export_yup=True)
print('EXPORTED', out_glb)
