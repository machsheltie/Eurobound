"""Stamp legible text onto round buttons (or any round patch) in a Tripo GLB's base-colour texture.

blender -b --factory-startup --python tools/char3d/stamp_text.py -- tools/char3d/poses/<id>_stamp.json

Why: Tripo paints badges as blurry glyph soup. The words are rendered with PIL into a disc bitmap and written into the
texels that the button covers (found by projecting the front view, as project_ref.py does).

Config JSON (paths relative to the repo root; boxes/points in reference-image pixels, y down):
 glb: input GLB (never modified);  out_glb: output GLB (re-exported uncompressed: run glb_jpeg.py afterwards)
 ref: front-view reference image, crop [x0,y0,x1,y1] (box holding the one figure), bg (225)
 font: ttf path (default C:/Windows/Fonts/arialbd.ttf)
 delete_strays: true (default) deletes every mesh object that is not the main skinned mesh (Tripo leaves an Icosphere)
 buttons: [{ center [x,y], r (ref px, the button's radius),
            lines ["ASK ME","ABOUT","TOKENS"],
            fill [r,g,b] 0..255 (default: median of the brightest third of the button in the reference, i.e. the button's own light colour),
            ink [r,g,b] (default 30,24,22), rim (rim darkness factor, default 0.55), margin (0.14 fraction of r kept clear of the rim),
            search (px, +-range of the automatic registration, default 40),
            fixed [ox, oy, scale] (skip the slow search; the printed result of an earlier run, nudged by eye) }]
Method: every texel gets a rest-pose 3D point + normal (UV rasterisation, numpy). The front projection maps it to reference
pixels. The projection is nudged per button (dx, dy) by a search that minimises the colour difference between the existing
texture and the reference inside the button, so the disc lands on the real button. Texels inside the disc facing the viewer
are replaced by the bitmap (rim ring, flat fill, bold dark text), pre-blurred to the texel footprint.
Needs a system `python` with Pillow on PATH (cfg "python" to override). Prints <=1 line per button.
"""
import bpy, sys, os, json, shutil, math, subprocess
import numpy as np

cfg = json.load(open(sys.argv[sys.argv.index("--") + 1]))
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
P = lambda p: os.path.join(ROOT, p)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=P(cfg["glb"]))
skinned = [o for o in bpy.data.objects if o.type == "MESH" and len(o.vertex_groups) > 0]
ob = max(skinned, key=lambda o: len(o.data.vertices))
if cfg.get("delete_strays", True):
    for o in [o for o in bpy.data.objects if o.type == "MESH" and o is not ob]:
        print("deleted stray mesh", o.name, len(o.data.vertices), "verts")
        bpy.data.objects.remove(o, do_unlink=True)
me = ob.data
img = None
for n in me.materials[0].node_tree.nodes:
    if n.type == "BSDF_PRINCIPLED" and n.inputs["Base Color"].links:
        texnode = n.inputs["Base Color"].links[0].from_node; img = texnode.image
W, H = img.size
tex = np.empty(W * H * 4, dtype=np.float32); img.pixels.foreach_get(tex); tex = tex.reshape(H, W, 4)

mw = ob.matrix_world
vco = np.array([tuple(mw @ v.co) for v in me.vertices])
me.calc_loop_triangles()
uv = np.array([tuple(l.uv) for l in me.uv_layers.active.data])
tris = np.array([t.loops for t in me.loop_triangles]); tv = np.array([t.vertices for t in me.loop_triangles])
nrm = np.array([[tuple(x) for x in t.split_normals] for t in me.loop_triangles]) @ np.array(mw.to_3x3()).T
bmin, bmax = vco.min(0), vco.max(0)

im = bpy.data.images.load(P(cfg["ref"]))
ref = np.empty(im.size[0] * im.size[1] * 4, dtype=np.float32); im.pixels.foreach_get(ref); ref = ref.reshape(im.size[1], im.size[0], 4)[::-1, :, :3]
RH, RW = ref.shape[:2]
x0, y0, x1, y1 = cfg["crop"]
fg = ref[y0:y1, x0:x1].min(2) < cfg.get("bg", 225) / 255.0
ys, xs = np.where(fg); fx0, fx1, fy0, fy1 = x0 + xs.min(), x0 + xs.max(), y0 + ys.min(), y0 + ys.max()
vdir = np.array([0, -1.0, 0])
pu = fx0 + (vco[:, 0] - bmin[0]) / (bmax[0] - bmin[0]) * (fx1 - fx0)
pv = fy1 - (vco[:, 2] - bmin[2]) / (bmax[2] - bmin[2]) * (fy1 - fy0)
PYEXE = cfg.get("python", "python")   # system Python with Pillow
FONT = cfg.get("font", "C:/Windows/Fonts/arialbd.ttf")


def samp(a, u, v):
    fu = np.clip(u - 0.5, 0, a.shape[1] - 1.001); fv = np.clip(v - 0.5, 0, a.shape[0] - 1.001)
    i0 = fu.astype(int); j0 = fv.astype(int); tu = (fu - i0)[:, None]; tw = (fv - j0)[:, None]
    return (a[j0, i0] * (1 - tu) * (1 - tw) + a[j0, i0 + 1] * tu * (1 - tw) + a[j0 + 1, i0] * (1 - tu) * tw + a[j0 + 1, i0 + 1] * tu * tw)


def texels(cx, cy, rad):
    """all texels of front-facing triangles whose projection touches the box: (tx, ty, u, v, ok_normal)"""
    out = []
    for ti in range(len(tv)):
        vs = tv[ti]
        if not ((pu[vs] > cx - rad) & (pu[vs] < cx + rad) & (pv[vs] > cy - rad) & (pv[vs] < cy + rad)).any(): continue
        if (nrm[ti] @ vdir).max() < 0.2: continue
        luv = uv[tris[ti]] * [W, H]
        lo = np.floor(luv.min(0)).astype(int); hi = np.ceil(luv.max(0)).astype(int)
        xs_, ys_ = np.meshgrid(np.arange(lo[0], hi[0] + 1), np.arange(lo[1], hi[1] + 1))
        q = np.stack([xs_ + 0.5, ys_ + 0.5], -1).reshape(-1, 2)
        a0, b0, c0 = luv
        d = (b0[1] - c0[1]) * (a0[0] - c0[0]) + (c0[0] - b0[0]) * (a0[1] - c0[1])
        if abs(d) < 1e-9: continue
        w0 = ((b0[1] - c0[1]) * (q[:, 0] - c0[0]) + (c0[0] - b0[0]) * (q[:, 1] - c0[1])) / d
        w1 = ((c0[1] - a0[1]) * (q[:, 0] - c0[0]) + (a0[0] - c0[0]) * (q[:, 1] - c0[1])) / d
        w2 = 1 - w0 - w1; ok = (w0 >= -0.02) & (w1 >= -0.02) & (w2 >= -0.02)
        if not ok.any(): continue
        w = np.stack([w0, w1, w2], 1)[ok]; qq = q[ok]
        p3 = w @ vco[vs]; n3 = w @ nrm[ti]; n3 /= np.linalg.norm(n3, axis=1, keepdims=True) + 1e-9
        u2 = fx0 + (p3[:, 0] - bmin[0]) / (bmax[0] - bmin[0]) * (fx1 - fx0)
        v2 = fy1 - (p3[:, 2] - bmin[2]) / (bmax[2] - bmin[2]) * (fy1 - fy0)
        out.append(np.column_stack([qq[:, 0].astype(int), qq[:, 1].astype(int), u2, v2, n3 @ vdir]))
    return np.vstack(out) if out else np.zeros((0, 5))


def bitmap_png(lines, fill, ink, rimf, margin, blur, path):
    """disc bitmap over [-1,1]^2 made by stamp_text_bitmap.py in the system Python (Blender's Python has no PIL)"""
    args = json.dumps({"lines": lines, "fill": [float(c) for c in fill], "ink": [float(c) for c in ink], "rim": rimf,
                       "margin": margin, "blur": blur, "font": FONT, "out": path})
    r = subprocess.run([PYEXE, os.path.join(os.path.dirname(os.path.abspath(__file__)), "stamp_text_bitmap.py"), args], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-400:]
    return int(r.stdout.strip().split()[-1])


for bi, bt in enumerate(cfg["buttons"]):
    cx, cy = bt["center"]; r = float(bt["r"]); sr = bt.get("search", 40)
    T = texels(cx, cy, r * 1.7 + sr + 12)
    T = T[T[:, 4] > 0.3]
    if len(T) < 50:
        print("button", bi, "no texels"); continue
    orig = tex[T[:, 1].astype(int), T[:, 0].astype(int), :3]
    best = (9, 0, 0, 1.0)
    if bt.get("fixed"): best = (0.0, *bt["fixed"])   # skip the search: [ox, oy, scale] from an earlier run, tuned by eye
    for stage in (() if bt.get("fixed") else (0, 1)):
        if stage == 0: oxs = oys = np.arange(-sr, sr + 1e-6, 4.0); sss = np.arange(0.9, 1.65, 0.05)
        else:
            oxs = np.arange(best[1] - 4, best[1] + 4.01, 1.0); oys = np.arange(best[2] - 4, best[2] + 4.01, 1.0); sss = np.arange(best[3] - 0.07, best[3] + 0.071, 0.02)
        for sc_ in sss:
            for oy in oys:
                for ox in oxs:
                    d = np.hypot(T[:, 2] + ox - cx, T[:, 3] + oy - cy) / (r * sc_)
                    m = d < 0.85
                    if m.sum() < 40: continue
                    ru = cx + (T[m, 2] + ox - cx) / sc_; rv = cy + (T[m, 3] + oy - cy) / sc_
                    sc = np.abs(samp(ref, ru, rv) - orig[m]).mean()
                    if sc < best[0]: best = (sc, ox, oy, sc_)
    sc, ox, oy, ss = best
    R = r * ss   # button radius as it appears on the mesh
    d = np.hypot(T[:, 2] + ox - cx, T[:, 3] + oy - cy) / R
    # button's own light colour from the reference
    yy, xx = np.mgrid[int(cy - r):int(cy + r) + 1, int(cx - r):int(cx + r) + 1]
    disc = ref[yy, xx][np.hypot(xx - cx, yy - cy) < r * 0.85]
    lum = disc.sum(1); light = disc[lum >= np.quantile(lum, 0.66)]
    fill = np.array([c / 255 for c in bt["fill"]]) if bt.get("fill") else np.median(light, 0)
    ink = np.array([c / 255 for c in bt.get("ink", [30, 24, 22])])
    # texel footprint (bitmap px per texel) from how many texels the disc holds
    inside = d <= 1.0
    rt = max(math.sqrt(inside.sum() / math.pi), 1.0)
    bpath = os.path.join(os.path.dirname(P(cfg["out_glb"])), "_stamp_btn%d.png" % bi)
    fsz = bitmap_png(bt["lines"], fill, ink, bt.get("rim", 0.55), bt.get("margin", 0.14), max(0.0, 512.0 / rt * 0.45), bpath)
    bim = bpy.data.images.load(bpath); bm = np.empty(1024 * 1024 * 4, dtype=np.float32); bim.pixels.foreach_get(bm)
    bm = bm.reshape(1024, 1024, 4)[::-1, :, :3].copy(); os.remove(bpath)
    sel = d <= 1.02
    lx = (T[sel, 2] + ox - cx) / R; ly = (T[sel, 3] + oy - cy) / R
    col = samp(bm, (lx + 1) * 512, (ly + 1) * 512)
    a = np.clip((1.02 - d[sel]) / 0.04, 0, 1)[:, None]
    tx = T[sel, 0].astype(int); ty = T[sel, 1].astype(int)
    tex[ty, tx, :3] = tex[ty, tx, :3] * (1 - a) + col * a
    print("button", bi, bt["lines"], "offset", ox, oy, "scale", round(ss, 2), "match", round(float(sc), 3), "texel radius", round(rt, 1), "font px", fsz, "texels", int(sel.sum()))

ni = bpy.data.images.new("base_stamped", W, H, alpha=True)
ni.colorspace_settings.name = img.colorspace_settings.name
ni.pixels.foreach_set(tex.ravel()); ni.update(); ni.file_format = "PNG"
texnode.image = ni
out = P(cfg["out_glb"])
bpy.ops.export_scene.gltf(filepath=out, export_format="GLB", export_animations=True, export_skins=True, export_image_format="AUTO", export_jpeg_quality=92)
print("wrote", os.path.basename(out), "figure bbox", fx0, fx1, fy0, fy1)
