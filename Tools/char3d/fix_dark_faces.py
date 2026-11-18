"""Repaint texels of dark (near-black) faces inside a head region with a fill colour (stray black hair-card artefacts).
blender -b --factory-startup --python tools/char3d/fix_dark_faces.py -- <glb> <zmin> <absx_min> <thresh> [r g b]
Reads <glb> (rest pose, world coords), paints in place after saving <glb stem>_darkfix_src.glb is NOT made: back the GLB up first."""
import bpy, sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "item3d"))
from material_lookup import base_image   # follows the Principled Base Color link (Eurobound-2bb9)
a = sys.argv[sys.argv.index("--") + 1:]; glb, zmin, axmin, th = a[0], float(a[1]), float(a[2]), float(a[3])
fill = [float(v) for v in a[4:7]] if len(a) >= 7 else None
bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.gltf(filepath=glb)
ob = max([o for o in bpy.data.objects if o.type == "MESH"], key=lambda o: len(o.data.vertices)); me = ob.data
img = base_image(me.materials[0]); W, H = img.size
t = np.empty(W * H * 4, np.float32); img.pixels.foreach_get(t); t = t.reshape(H, W, 4)
uv = me.uv_layers.active.data; mw = ob.matrix_world; n = 0; mask = np.zeros((H, W), bool)
for p in me.polygons:
    co = mw @ p.center
    if co.z < zmin or abs(co.x) < axmin: continue
    u = np.array([uv[l].uv for l in p.loop_indices]); c = u.mean(0)
    if t[min(H-1, int(c[1]*H)), min(W-1, int(c[0]*W))][:3].max() >= th: continue
    x0, x1 = int(u[:,0].min()*W), int(u[:,0].max()*W)+1; y0, y1 = int(u[:,1].min()*H), int(u[:,1].max()*H)+1
    mask[max(y0,0):y1, max(x0,0):x1] = True; n += 1
dark = t[..., :3].max(2) < th * 1.5
mask &= dark
if fill is None:   # median of bright texels near the painted area
    ys, xs = np.nonzero(mask); r = 40; reg = t[max(ys.min()-r,0):ys.max()+r, max(xs.min()-r,0):xs.max()+r, :3]; reg = reg[reg.max(2) > 0.35]
    fill = list(np.median(reg, 0))
t[mask, :3] = fill; img.pixels.foreach_set(t.reshape(-1)); img.pack()
print("faces", n, "texels", int(mask.sum()), "fill", np.round(fill, 2))
bpy.ops.export_scene.gltf(filepath=glb, export_format="GLB", export_animations=True, export_skins=True, export_image_format="AUTO", export_jpeg_quality=92)
