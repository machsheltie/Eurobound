"""Build a thick five-point sheriff star with ball tips, textured with a flat face image (0 Tripo credits).

blender -b --python Tools/item3d/star_slab.py -- <face.png> <out.glb> [tilt_deg=35]
 - outline matches dev/asset_team/icon_refs/b14_gen.py badge(): 1280 px canvas, star centre (640, 656), outer radius 470,
   inner radius 0.58 * 470, ball tips radius 34 at radius 464. 1 px = 0.001 unit, so the star is about 1.0 wide.
 - thickness 0.12, bevelled; front face UVs planar over the whole 1280 px canvas; every other face is UV-mapped onto a
   plain gold patch of the image (centre disc), so one material suffices (render_item.py keeps only the first slot)
 - Principled BSDF, base colour texture only, no emission
 - tilt_deg: rotation about X leaning the face toward the render camera (camera sits at -Y); baked into the mesh
"""
import bpy, bmesh, sys, os, math

argv = sys.argv[sys.argv.index("--") + 1:]
face_png, out_glb = os.path.abspath(argv[0]), os.path.abspath(argv[1])
tilt = float(argv[2]) if len(argv) > 2 else 35.0
S, CX, CY, K = 1280.0, 640.0, 656.0, 0.001
R, RIN, TIP_R, TIP_AT, T = 470.0, 470.0 * 0.58, 34.0, 464.0, 0.12

bpy.ops.wm.read_factory_settings(use_empty=True)
bm = bmesh.new()
pts = []
for i in range(10):
    a = math.radians(-90 + i * 36); rr = R if i % 2 == 0 else RIN
    pts.append((rr * math.cos(a) * K, -rr * math.sin(a) * K))   # image y is down, mesh y is up
verts = [bm.verts.new((x, y, -T / 2)) for x, y in pts]
face = bm.faces.new(verts)
r = bmesh.ops.extrude_face_region(bm, geom=[face])
top = [v for v in r["geom"] if isinstance(v, bmesh.types.BMVert)]
bmesh.ops.translate(bm, vec=(0, 0, T), verts=top)
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
mesh = bpy.data.meshes.new("star"); bm.to_mesh(mesh); bm.free()
star = bpy.data.objects.new("star", mesh); bpy.context.collection.objects.link(star)
bpy.context.view_layer.objects.active = star; star.select_set(True)

for i in range(5):                                             # ball tips, unioned
    a = math.radians(-90 + i * 72)
    bpy.ops.mesh.primitive_cylinder_add(vertices=40, radius=TIP_R * K, depth=T,
                                        location=(TIP_AT * math.cos(a) * K, -TIP_AT * math.sin(a) * K, 0))
    cyl = bpy.context.active_object
    bl = star.modifiers.new("u%d" % i, "BOOLEAN"); bl.operation = 'UNION'; bl.object = cyl; bl.solver = 'EXACT'
    bpy.context.view_layer.objects.active = star
    bpy.ops.object.modifier_apply(modifier=bl.name)
    bpy.data.objects.remove(cyl, do_unlink=True)

bv = star.modifiers.new("bv", "BEVEL"); bv.width = 0.012; bv.segments = 3; bv.limit_method = 'ANGLE'
bpy.ops.object.modifier_apply(modifier="bv")

img = bpy.data.images.load(face_png)
gold_uv = (CX / S, 1 - CY / S)                                   # plain light-gold centre disc
bm = bmesh.new(); bm.from_mesh(star.data); bm.normal_update()
uv = bm.loops.layers.uv.verify()
nfront = 0
for f in bm.faces:
    front = f.normal.z > 0.9
    nfront += front
    for l in f.loops:
        co = l.vert.co
        l[uv].uv = ((co.x / K + CX) / S, 1 - (CY - co.y / K) / S) if front else gold_uv
print("FRONT FACES", nfront, "of", len(bm.faces))
bm.to_mesh(star.data); bm.free()
bpy.ops.object.shade_smooth_by_angle(angle=math.radians(45))

mat = bpy.data.materials.new("star_mat"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = 'Linear'
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Base Color"].default_value = (1, 1, 1, 1); bsdf.inputs["Metallic"].default_value = 0.0; bsdf.inputs["Roughness"].default_value = 0.8
star.data.materials.clear(); star.data.materials.append(mat)
for p in star.data.polygons:
    p.material_index = 0

bpy.ops.object.select_all(action='DESELECT'); star.select_set(True)
star.rotation_euler = (math.radians(tilt), 0, 0)
bpy.ops.object.transform_apply(rotation=True)
bpy.ops.export_scene.gltf(filepath=out_glb, export_format="GLB", export_image_format="AUTO", export_jpeg_quality=95)
print("STAR", out_glb, "verts", len(star.data.vertices))
