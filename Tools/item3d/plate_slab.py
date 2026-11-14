"""Build a thick, rounded commemorative plate (lathed, chunky rim, raised foot ring) textured with a flat top-down face image (0 Tripo credits).

blender -b --python Tools/item3d/plate_slab.py -- <face.png> <out.glb> [tilt_deg=25]
 - diameter 1.0, about 0.16 thick: flat dial face up (+Z), rounded fat rim, recessed underside with a foot ring
 - face.png is a flat straight-down view of the plate face; it is cropped to the circle's bounding box and planar-mapped
   over the top face and the rounded rim shoulder (the artwork's gold rim band lands on the shoulder)
 - every other face (outer wall, underside) maps onto a plain off-white strip added to the bottom of the atlas, so the
   mesh needs only one material (render_item.py keeps only the first material slot)
 - Principled BSDF, base colour texture only, no emission (same as the Tripo GLBs)
 - tilt_deg: rotation about X that leans the face toward the render camera (camera sits at -Y); baked into the mesh
"""
import bpy, bmesh, sys, os, math
import numpy as np

argv = sys.argv[sys.argv.index("--") + 1:]
face_png, out_glb = os.path.abspath(argv[0]), os.path.abspath(argv[1])
tilt = float(argv[2]) if len(argv) > 2 else 25.0
bpy.ops.wm.read_factory_settings(use_empty=True)

# ---- atlas: cropped artwork on top, plain off-white strip underneath (bpy + numpy only, no Pillow)
src = bpy.data.images.load(face_png)
sw, sh = src.size
px = np.empty(sw * sh * 4, dtype=np.float32); src.pixels.foreach_get(px); px = px.reshape(sh, sw, 4)[::-1]   # rows top-down
a = px[:, :, :3] * 255
bg = np.median(np.concatenate([a[:6, :6].reshape(-1, 3), a[-6:, -6:].reshape(-1, 3)]), axis=0)
m = np.abs(a - bg).sum(2) > 40
ys, xs = np.where(m)
box = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
side = max(box[2] - box[0], box[3] - box[1])
cx, cy = (box[0] + box[2]) // 2, (box[1] + box[3]) // 2
x0, y0 = int(cx - side // 2), int(cy - side // 2)
crop = px[y0:y0 + side, x0:x0 + side][::-1].copy()          # back to bottom-up for bpy
tmp = bpy.data.images.new("crop", side, side, alpha=True)
tmp.pixels.foreach_set(crop.reshape(-1)); tmp.scale(1024, 1024)
art = np.empty(1024 * 1024 * 4, dtype=np.float32); tmp.pixels.foreach_get(art); art = art.reshape(1024, 1024, 4)
aa = art[:, :, :3] * 255
white = (aa.min(2) > 215) & ((aa.max(2) - aa.min(2)) < 25)
off = np.median(aa[white], axis=0) if white.sum() > 500 else np.array([236., 232., 222.])
STRIP = 128
atlas_px = np.ones((1024 + STRIP, 1024, 4), dtype=np.float32)
atlas_px[:STRIP, :, :3] = off / 255.0                         # bottom rows (bottom-up) = plain strip
atlas_px[STRIP:, :, :] = art
atl = bpy.data.images.new("plate_atlas", 1024, 1024 + STRIP, alpha=False)
atl.pixels.foreach_set(atlas_px.reshape(-1))
atlas_path = os.path.splitext(out_glb)[0] + "_atlas.png"
atl.filepath_raw = atlas_path; atl.file_format = "PNG"; atl.save()
off = tuple(int(v) for v in off)
H_ATLAS = 1024 + STRIP

# ---- lathe profile (r, z, on_face): z up
R = 0.5
prof = [
    (0.0, 0.10, 1), (0.30, 0.10, 1), (0.455, 0.10, 1),          # flat dial face
    (0.478, 0.092, 1), (0.494, 0.074, 1), (0.5, 0.05, 1),        # rounded shoulder (still takes the artwork)
    (0.5, 0.02, 0), (0.494, -0.01, 0), (0.476, -0.035, 0),       # fat outer wall, rounded under-lip
    (0.44, -0.05, 0), (0.37, -0.06, 0), (0.30, -0.06, 0),        # foot ring
    (0.285, -0.03, 0), (0.0, -0.02, 0),                           # recessed underside
]
prof = [(r, z * 1.45, f) for (r, z, f) in prof]   # chunkier: about 0.23 thick for a 1.0 diameter
N = 96
bm = bmesh.new()
uvl = bm.loops.layers.uv.new("UVMap")
rings = []
for (r, z, face) in prof:
    if r == 0.0:
        rings.append([bm.verts.new((0, 0, z))])
    else:
        rings.append([bm.verts.new((r * math.cos(2 * math.pi * k / N), r * math.sin(2 * math.pi * k / N), z)) for k in range(N)])
faces = []
for i in range(len(prof) - 1):
    A, B = rings[i], rings[i + 1]
    fl = prof[i][2] and prof[i + 1][2]
    for k in range(N):
        k2 = (k + 1) % N
        if len(A) == 1:
            f = bm.faces.new((A[0], B[k2], B[k]))     # top fan, normal +Z
        elif len(B) == 1:
            f = bm.faces.new((A[k], A[k2], B[0]))
        else:
            f = bm.faces.new((A[k], A[k2], B[k2], B[k]))
        faces.append((f, fl))
bm.normal_update()
# orient normals outward: top fan +Z; flip the whole mesh if the first face points down
if faces[0][0].normal.z < 0:
    for f, _ in faces:
        f.normal_flip()
    bm.normal_update()
for f, fl in faces:
    for l in f.loops:
        x, y = l.vert.co.x, l.vert.co.y
        if fl:
            l[uvl].uv = (x / (2 * R) + 0.5, (y / (2 * R) + 0.5) * 1024 / H_ATLAS + STRIP / H_ATLAS)
        else:
            l[uvl].uv = (0.5, STRIP / 2 / H_ATLAS)
mesh = bpy.data.meshes.new("plate"); bm.to_mesh(mesh); bm.free()
obj = bpy.data.objects.new("plate", mesh); bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj; obj.select_set(True)
bpy.ops.object.shade_smooth_by_angle(angle=math.radians(45))

img = atl
mat = bpy.data.materials.new("plate_mat"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = "Linear"
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Metallic"].default_value = 0.0; bsdf.inputs["Roughness"].default_value = 0.8
mesh.materials.clear(); mesh.materials.append(mat)

obj.rotation_euler = (math.radians(tilt), 0, 0)
bpy.ops.object.transform_apply(rotation=True)
bpy.ops.export_scene.gltf(filepath=out_glb, export_format="GLB", export_image_format="AUTO", export_jpeg_quality=95)
print("PLATE", out_glb, "verts", len(mesh.vertices), "polys", len(mesh.polygons), "off-white", off)
