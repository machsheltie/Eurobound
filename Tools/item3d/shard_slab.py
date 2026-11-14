"""Build a thick, flat jagged shard slab textured with flat face art (0 Tripo credits). Same idea as star_slab.py with an arbitrary outline.

blender -b --python Tools/item3d/shard_slab.py -- <face.png> <outline.json> <out.glb> [tilt_deg=35] [thickness=0.09]
 - face.png: 1024 wide x 1152 tall. Top 1024 rows = the art (planar-mapped over the front face, 1 px = 0.001 unit);
   bottom 128 rows = a plain steel strip that every other face (back, edges) is UV-mapped onto, so one material suffices
 - outline.json: {"pts": [[x, y], ...]} in art pixels, y down
 - Principled BSDF, base colour texture only, no emission; bevelled edges
"""
import bpy, bmesh, sys, os, math, json

argv = sys.argv[sys.argv.index("--") + 1:]
face_png, outline, out_glb = os.path.abspath(argv[0]), os.path.abspath(argv[1]), os.path.abspath(argv[2])
tilt = float(argv[3]) if len(argv) > 3 else 35.0
T = float(argv[4]) if len(argv) > 4 else 0.09
W, HA, K = 1024.0, 1152.0, 0.001
pts = json.load(open(outline))["pts"]
cx = (min(p[0] for p in pts) + max(p[0] for p in pts)) / 2
cy = (min(p[1] for p in pts) + max(p[1] for p in pts)) / 2

bpy.ops.wm.read_factory_settings(use_empty=True)
bm = bmesh.new()
verts = [bm.verts.new(((x - cx) * K, -(y - cy) * K, -T / 2)) for x, y in pts]
face = bm.faces.new(verts)
r = bmesh.ops.extrude_face_region(bm, geom=[face])
top = [v for v in r["geom"] if isinstance(v, bmesh.types.BMVert)]
bmesh.ops.translate(bm, vec=(0, 0, T), verts=top)
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
me = bpy.data.meshes.new("shard"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("shard", me); bpy.context.collection.objects.link(ob)
bpy.context.view_layer.objects.active = ob; ob.select_set(True)
bv = ob.modifiers.new("bv", "BEVEL"); bv.width = 0.008; bv.segments = 2; bv.limit_method = 'ANGLE'
bpy.ops.object.modifier_apply(modifier="bv")
bm = bmesh.new(); bm.from_mesh(ob.data)
bmesh.ops.triangulate(bm, faces=bm.faces[:], quad_method='BEAUTY', ngon_method='EAR_CLIP')
bm.normal_update()
uv = bm.loops.layers.uv.verify()
plain = (0.5, 1 - (1024 + 64) / HA)
nfront = 0
for f in bm.faces:
    front = f.normal.z > 0.9
    nfront += front
    for l in f.loops:
        co = l.vert.co
        l[uv].uv = ((co.x / K + cx) / W, 1 - (cy - co.y / K) / HA) if front else plain
print("FRONT FACES", nfront, "of", len(bm.faces))
bm.to_mesh(ob.data); bm.free()
bpy.ops.object.shade_smooth_by_angle(angle=math.radians(45))

img = bpy.data.images.load(face_png)
mat = bpy.data.materials.new("shard_mat"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = 'Linear'
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Metallic"].default_value = 0.0; bsdf.inputs["Roughness"].default_value = 0.8
ob.data.materials.clear(); ob.data.materials.append(mat)
for p in ob.data.polygons:
    p.material_index = 0
ob.rotation_euler = (math.radians(tilt), 0, 0)
bpy.ops.object.transform_apply(rotation=True)
bpy.ops.export_scene.gltf(filepath=out_glb, export_format="GLB", export_image_format="AUTO", export_jpeg_quality=95)
print("SHARD", out_glb, "verts", len(ob.data.vertices))
