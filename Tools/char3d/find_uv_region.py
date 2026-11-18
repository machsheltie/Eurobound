"""Find the UV box(es) of a small coloured part (a ring, a badge) on a GLB, by colour AND rest-pose world position.

blender -b --factory-startup --python tools/char3d/find_uv_region.py -- <glb> '<json>'
json: {"hue": [lo, hi], "sat": [min, max], "val": [min, max], "box": [x0, y0, z0, x1, y1, z1] (world metres, rest pose), "pad": 0.002}
Prints one line per UV cluster: uv_box [u0, v0, u1, v1] with v down like image rows (the format recolor_region.py uses),
plus the face count and world centre. Read-only: nothing is written.
Why: colour alone is ambiguous on a Tripo atlas (Tomas's red stripes read as pink), so faces are filtered by where they are.
"""
import bpy, sys, os, json, colorsys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "item3d"))
from material_lookup import base_image   # follows the Principled Base Color link (Eurobound-2bb9)

a = sys.argv[sys.argv.index("--") + 1:]
glb, cfg = a[0], json.loads(a[1])
bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.gltf(filepath=glb)
ob = max([o for o in bpy.data.objects if o.type == "MESH"], key=lambda o: len(o.data.vertices)); me = ob.data
img = base_image(me.materials[0]); W, H = img.size
t = np.empty(W * H * 4, np.float32); img.pixels.foreach_get(t); t = t.reshape(H, W, 4)   # rows bottom-up
uv = me.uv_layers.active.data; mw = ob.matrix_world
x0, y0, z0, x1, y1, z1 = cfg["box"]; hl, hh = cfg["hue"]; sl, sh = cfg.get("sat", [0, 1]); vl, vh = cfg.get("val", [0, 1])
hits = []
for p in me.polygons:
    co = mw @ p.center
    if not (x0 <= co.x <= x1 and y0 <= co.y <= y1 and z0 <= co.z <= z1):
        continue
    u = np.array([uv[l].uv for l in p.loop_indices]); c = u.mean(0)
    r, g, b = t[min(H - 1, int(c[1] * H)), min(W - 1, int(c[0] * W))][:3]
    h, s, v = colorsys.rgb_to_hsv(r ** (1 / 2.2), g ** (1 / 2.2), b ** (1 / 2.2))   # image pixels are linear; compare in sRGB
    inh = (hl <= h <= hh) if hl <= hh else (h >= hl or h <= hh)
    if inh and sl <= s <= sh and vl <= v <= vh:
        hits.append((u[:, 0].min(), 1 - u[:, 1].max(), u[:, 0].max(), 1 - u[:, 1].min(), co.copy()))
pad = cfg.get("pad", 0.002); clusters = []
for hb in hits:   # greedy merge of overlapping boxes
    for cl in clusters:
        if hb[0] <= cl["b"][2] + pad and hb[2] >= cl["b"][0] - pad and hb[1] <= cl["b"][3] + pad and hb[3] >= cl["b"][1] - pad:
            cl["b"] = [min(cl["b"][0], hb[0]), min(cl["b"][1], hb[1]), max(cl["b"][2], hb[2]), max(cl["b"][3], hb[3])]; cl["n"] += 1; cl["c"].append(hb[4]); break
    else:
        clusters.append({"b": list(hb[:4]), "n": 1, "c": [hb[4]]})
print("UVREGION faces", len(hits), "clusters", len(clusters))
for cl in sorted(clusters, key=lambda c: -c["n"]):
    cen = np.mean([[c.x, c.y, c.z] for c in cl["c"]], 0)
    print("UVREGION uv_box", [round(v - pad if i < 2 else v + pad, 4) for i, v in enumerate(cl["b"])], "faces", cl["n"], "centre", np.round(cen, 3).tolist())
