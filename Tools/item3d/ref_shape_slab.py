"""Build a thin 3D shape whose outline IS the reference art's cut-out, textured with that art (0 Tripo credits).

blender -b --python Tools/item3d/ref_shape_slab.py -- <cutout_rgba.png> <out.glb> [thickness=0.012] [bulge=0.05] [grid=160] [back_hex=EDEAE0] [smooth=16]

For soft, flat items (garments, flags, paper) where scripted outlines fail blind QC on shape: the silhouette comes
from the approved Firefly reference itself (alpha > 0.5 after the art_cleanup cut-out), so nothing about the form is
invented here. Author ruling for clothing icons: "Firefly reference, projected onto a flat 3D shape" (Desk
asset-team-qc-i_survived_tshirt, 2026-11-15).
 - front surface: a grid of `grid` cells along the longest side, kept where the cut-out is opaque; it faces -Y
   (render_item.py's camera side), X right, Z up, longest side 1.0 unit
 - bulge: the middle of the shape swells toward the camera by up to `bulge` units (a smoothed distance-from-edge), so
   the toon ramp gets a soft body instead of a flat card; the edge stays thin
 - thickness: solidified backwards; the back and the rim are UV-mapped onto a plain `back_hex` strip added under the
   art in one atlas (one material, because render_item.py keeps only the first slot)
Writes <out.glb> (atlas embedded) and prints <= 3 lines.
"""
import bpy, bmesh, sys, os
import numpy as np

argv = sys.argv[sys.argv.index("--") + 1:]
src, out = os.path.abspath(argv[0]), os.path.abspath(argv[1])
THICK = float(argv[2]) if len(argv) > 2 else 0.012
BULGE = float(argv[3]) if len(argv) > 3 else 0.05
GRID = int(argv[4]) if len(argv) > 4 else 160
BACK = argv[5] if len(argv) > 5 else "EDEAE0"
SMOOTH = int(argv[6]) if len(argv) > 6 else 16
STRIP = 64

bpy.ops.wm.read_factory_settings(use_empty=True)
im = bpy.data.images.load(src)
W, H = im.size
px = np.array(im.pixels[:], dtype=np.float32).reshape(H, W, 4)   # rows bottom-up
alpha = px[:, :, 3]

# --- atlas: the art on top, a plain strip of the back colour underneath (still bottom-up rows) ---
bc = np.array([int(BACK[i:i + 2], 16) / 255.0 for i in (0, 2, 4)], dtype=np.float32)
atlas = np.zeros((H + STRIP, W, 4), dtype=np.float32)
rgb = px[:, :, :3].copy()                                # bleed edge colours outward so the cell-rounded outline shows no fringe
known = alpha > 0.5
for _ in range(32):
    acc = np.zeros_like(rgb); cnt = np.zeros(alpha.shape, np.float32)
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
        k = np.roll(np.roll(known, dy, 0), dx, 1)
        acc += np.roll(np.roll(rgb, dy, 0), dx, 1) * k[..., None]; cnt += k
    grow = (~known) & (cnt > 0)
    if not grow.any():
        break
    rgb[grow] = acc[grow] / cnt[grow][:, None]; known |= grow
rgb[~known] = bc
atlas[STRIP:, :, :3] = rgb
atlas[:STRIP, :, :3] = bc
atlas[:, :, 3] = 1.0
aimg = bpy.data.images.new(os.path.splitext(os.path.basename(out))[0] + "_atlas", W, H + STRIP, alpha=False)
aimg.pixels[:] = atlas.ravel()
apng = os.path.splitext(out)[0] + "_atlas.png"
aimg.filepath_raw = apng
aimg.file_format = "PNG"
aimg.save()
AH = H + STRIP

# --- occupancy: a cell is kept if any pixel in it is opaque (keeps thin cords and pins); bulge from a blurred inside mask ---
step = max(W, H) / GRID
nx, nz = int(round(W / step)), int(round(H / step))
hard = (alpha > 0.5).astype(np.float32)
r = max(1, int(step / 2))
cs = np.pad(np.pad(hard, r).cumsum(0).cumsum(1), ((1, 0), (1, 0)))
k = 2 * r + 1
grown = (cs[k:, k:] - cs[:-k, k:] - cs[k:, :-k] + cs[:-k, :-k]) > 0     # box dilation by half a cell
occ = np.zeros((nz, nx), bool)                          # row 0 = bottom
for j in range(nz):
    r0, r1 = int(j * step), min(int((j + 1) * step), H)
    rowmax = grown[r0:r1].any(axis=0)
    for i in range(nx):
        occ[j, i] = rowmax[int(i * step):min(int((i + 1) * step), W)].any()


def blur(a, r):
    k = 2 * r + 1
    p = np.pad(a, r, mode="constant")
    c = p.cumsum(0).cumsum(1)
    c = np.pad(c, ((1, 0), (1, 0)))
    return (c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]) / (k * k)


d = occ.astype(np.float32)
for _ in range(3):
    d = blur(d, max(2, GRID // 40)) * occ
d = d / max(d.max(), 1e-6)
dv = np.pad(d, 1, mode="edge")
dv = (dv[:-1, :-1] + dv[1:, :-1] + dv[:-1, 1:] + dv[1:, 1:]) / 4    # cell values -> grid vertices [nz+1, nx+1]

scale = 1.0 / max(nx, nz)
bm = bmesh.new()
uvl = bm.loops.layers.uv.new("UVMap")
verts = {}


def vert(i, j):                                        # i = column (x), j = row (z), both on the vertex grid
    v = verts.get((i, j))
    if v is None:
        x = (i - nx / 2) * scale
        z = (j - nz / 2) * scale
        y = -BULGE * float(np.sqrt(dv[j, i]))
        v = bm.verts.new((x, y, z))
        verts[(i, j)] = v
    return v


for j in range(nz):
    for i in range(nx):
        if not occ[j, i]:
            continue
        bm.faces.new((vert(i, j), vert(i + 1, j), vert(i + 1, j + 1), vert(i, j + 1)))
# relax the stair-stepped outline (boundary verts only, in the XZ plane), then UVs straight from position
for _ in range(SMOOTH):
    edge = [v for v in bm.verts if v.is_boundary]
    bmesh.ops.smooth_vert(bm, verts=edge, factor=0.5, use_axis_x=True, use_axis_y=False, use_axis_z=True)
for f in bm.faces:
    for lp in f.loops:
        x, _, z = lp.vert.co
        lp[uvl].uv = ((x / scale + nx / 2) * step / W, (STRIP + (z / scale + nz / 2) * step) / AH)
bmesh.ops.reverse_faces(bm, faces=list(bm.faces))     # quads above wind toward +Y; flip so the front faces -Y
me = bpy.data.meshes.new("ref_shape")
bm.to_mesh(me)
bm.free()
ob = bpy.data.objects.new("ref_shape", me)
bpy.context.scene.collection.objects.link(ob)
n_front = len(me.polygons)

sol = ob.modifiers.new("solid", "SOLIDIFY")
sol.thickness = THICK
sol.offset = -1.0 if me.polygons[0].normal.y < 0 else 1.0   # grow away from the camera
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.ops.object.modifier_apply(modifier="solid")

# everything that does not face the camera goes onto the plain strip
uv = me.uv_layers["UVMap"].data
for p in me.polygons:
    if p.normal.y < -0.2:
        continue
    for li in p.loop_indices:
        uv[li].uv = (0.5, (STRIP * 0.5) / AH)

mat = bpy.data.materials.new("ref_shape_mat")
mat.use_nodes = True
nt = mat.node_tree
bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
tex = nt.nodes.new("ShaderNodeTexImage")
tex.image = aimg
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Roughness"].default_value = 0.9
me.materials.append(mat)
for p in me.polygons:
    p.use_smooth = True

os.makedirs(os.path.dirname(out), exist_ok=True)
bpy.ops.export_scene.gltf(filepath=out, export_format="GLB", use_selection=False)
print("SHAPE grid %dx%d, front quads %d, total faces %d" % (nx, nz, n_front, len(me.polygons)))
print("WROTE", out)
