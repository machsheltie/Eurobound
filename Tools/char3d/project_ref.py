"""Project reference-art pixels onto a Tripo GLB's base-colour texture (fixes garbled lettering).

blender -b --python tools/char3d/project_ref.py -- tools/char3d/poses/<id>_project.json

Config JSON (paths relative to the repo root; all boxes in reference-image pixels, x0,y0,x1,y1, y down):
 glb: rigged GLB (original saved once as <name>_orig.glb, later runs start from the _orig)
 views: [{ref, crop (box holding the one figure), side "front"|"back" (viewer at -Y / +Y), mask (box to paint),
          feather (px, 3), ndot (0.5), bg (225: pixel counts as figure when min(rgb) < bg), dx, dy (nudge, ref px)}]
 optional per-view crispness: sharpen [radius_px, percent] (unsharp mask) and contrast (factor about the mask mean), both applied to
   the reference pixels inside the mask only; bilinear true samples the reference with bilinear filtering instead of nearest.
 zoom [zx, zy] + zoom_c [x, y]: magnify the reference about zoom_c (ref px) before the dx/dy nudge (face: mesh head 10-20% larger than the painted head).
 ellipse p: use a superellipse inscribed in the mask box instead of the box (p 2 = ellipse, 3 = rounded oval patch), so a patch on a plain panel leaves the panel untouched.
 exclude_hsv [{hue:[lo,hi], sat:[lo,hi], val:[lo,hi]}]: ref pixels in any box are never written (blond hair must not land on skin). rotate deg: level a tilted painted head (about zoom_c).
 overlay: optional png path, silhouette overlay of the first view for the alignment check
 side also takes "left" | "right" (viewer at -X / +X: side elevations, e.g. an arcade cabinet's side view).
 mask_png (protocol step 6, nhxz): a SAM zone mask in the reference's pixel space (white = paint, from
   tools/paint_zones/segment_ref.py). Texels are written only where the mask is on, feathered by `feather` px; this
   also stops occluded surfaces (torso behind an arm) taking the occluder's pixels when the two are different zones.
   `mask` (box) becomes optional and defaults to the mask's bbox. Several views may use several masks.
 color_gain [r, g, b]: multiply the sampled reference pixels (sRGB 0-1) per channel, e.g. canonical median / source
   median for a zone, when the reliable camera is a derived image and the colour truth is the canonical reference.
 auto_align true | {max_px 30, pad_px 24}: measure dx/dy per view by phase-correlating the mesh's original texture
   (seen through the same projection) against the reference inside the mask box; replaces hand-tuned dx/dy.
 delight_px N (with mask_png): fallback albedo pass for protocol step 7 while Modddif is unavailable. Divides out the
   zone's large-scale luminance (box low-pass of radius N, zone pixels only) so painted lighting is not copied as base
   colour; fine detail (weave, prints, fading under N px) stays. Do not use on painted wear such as denim fades.
 ndot_soft S: fade the projection in as the surface turns toward the view, over n.v in [ndot, ndot+S] (faces: ndot 0.45,
   ndot_soft 0.3 keeps the front projection off the cheek sides, where it stretches into a smear and leaves a seam).
 clip {axis "x"|"y"|"z", min, max} or a list of them: keep only texels whose rest-pose world coordinate lies in the
   slab. The projection has no depth test, so on a ring, loop or wristband the far wall also faces the camera and gets
   painted twice; cut it. Viewer side -> axis: front (viewer at -Y) {"axis":"y","max":-0.3}, back {"axis":"y","min":..},
   left (-X) {"axis":"x","max":..}, right {"axis":"x","min":..}. Values are mesh units, for a ring centred on the origin.
 report: JSON path for the reliability report (default <out glb>_projection_report.json): per view, the silhouette
   IoU between the projected mesh and the reference figure (>= reliable_iou, default 0.85, counts as a reliable
   camera match) and the texels written. The protocol allows projection only where the match is reliable.
Method: rasterise each triangle in UV space (numpy) to give every texel its rest-pose 3D point + normal, project
orthographically along the view axis with the mesh bbox fitted to the figure bbox, sample the reference where the
texel faces the view and lies inside the mask. Prints <=5 lines.
"""
import bpy, sys, os, json, shutil, math
import numpy as np

cfg = json.load(open(sys.argv[sys.argv.index("--") + 1]))
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
P = lambda p: os.path.join(ROOT, p)
glb = P(cfg["glb"]); orig = glb.replace(".glb", "_orig.glb")
if not os.path.exists(orig): shutil.copy(glb, orig)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=orig)
meshes = [o for o in bpy.data.objects if o.type == "MESH" and o.data.materials and len(o.data.vertices) > 500]
ob = max(meshes, key=lambda o: len(o.data.vertices))
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
uvl = me.uv_layers.active.data
uv = np.array([tuple(l.uv) for l in uvl])
tris = np.array([t.loops for t in me.loop_triangles]); tv = np.array([t.vertices for t in me.loop_triangles])
nrm = np.array([[tuple(x) for x in t.split_normals] for t in me.loop_triangles])  # (T,3,3)
nrm = nrm @ np.array(mw.to_3x3()).T
bmin, bmax = vco.min(0), vco.max(0)

def load(p):
    im = bpy.data.images.load(P(p)); a = np.empty(im.size[0] * im.size[1] * 4, dtype=np.float32); im.pixels.foreach_get(a); a = a.reshape(im.size[1], im.size[0], 4)[::-1]
    return a  # rows top-down

def fit(view, a):
    x0, y0, x1, y1 = view["crop"]; sub = a[y0:y1, x0:x1, :3]
    fg = sub.min(2) < view.get("bg", 225) / 255.0
    ys, xs = np.where(fg); return x0 + xs.min(), x0 + xs.max(), y0 + ys.min(), y0 + ys.max()

REPORT = []
TEX0 = tex.copy()   # untouched texture, for auto_align
SPLAT = {}


def splat(key, proj_fn, vdir_, shape):
    """The mesh's original texture as seen through proj_fn: a reference-space image plus coverage (auto_align)."""
    if key in SPLAT:
        return SPLAT[key]
    img_ = np.zeros(shape + (3,), np.float32); cov = np.zeros(shape, bool)
    for ti in range(len(tv)):
        if (nrm[ti] @ vdir_).max() < 0.3:
            continue
        luv = uv[tris[ti]] * [W, H]
        lo = np.floor(luv.min(0)).astype(int); hi = np.ceil(luv.max(0)).astype(int)
        xs, ys = np.meshgrid(np.arange(lo[0], hi[0] + 1), np.arange(lo[1], hi[1] + 1))
        q = np.stack([xs + 0.5, ys + 0.5], -1).reshape(-1, 2)
        a0, b0, c0 = luv
        d = (b0[1] - c0[1]) * (a0[0] - c0[0]) + (c0[0] - b0[0]) * (a0[1] - c0[1])
        if abs(d) < 1e-9:
            continue
        w0 = ((b0[1] - c0[1]) * (q[:, 0] - c0[0]) + (c0[0] - b0[0]) * (q[:, 1] - c0[1])) / d
        w1 = ((c0[1] - a0[1]) * (q[:, 0] - c0[0]) + (a0[0] - c0[0]) * (q[:, 1] - c0[1])) / d
        w2 = 1 - w0 - w1; ok = (w0 >= 0) & (w1 >= 0) & (w2 >= 0)
        if not ok.any():
            continue
        w = np.stack([w0, w1, w2], 1)[ok]; qq = q[ok]
        n3 = w @ nrm[ti]; front = (n3 @ vdir_) > 0.3
        u2, v2 = proj_fn(w @ vco[tv[ti]])
        ix = np.clip(u2.astype(int), 0, shape[1] - 1); iy = np.clip(v2.astype(int), 0, shape[0] - 1)
        tx = np.clip(qq[:, 0].astype(int), 0, W - 1); ty = np.clip(qq[:, 1].astype(int), 0, H - 1)
        img_[iy[front], ix[front]] = TEX0[ty[front], tx[front], :3]; cov[iy[front], ix[front]] = True
    SPLAT[key] = (img_, cov)
    return SPLAT[key]


def phase_shift(ref_g, mesh_g, cov, max_px):
    """Shift d (dx, dy) so that ref(x + d) best matches mesh(x), by phase correlation (numpy only)."""
    m = mesh_g.copy(); m[~cov] = m[cov].mean() if cov.any() else 0
    r_ = ref_g - ref_g.mean(); m = m - m.mean()
    win = np.outer(np.hanning(r_.shape[0]), np.hanning(r_.shape[1]))
    F = np.fft.fft2(r_ * win) * np.conj(np.fft.fft2(m * win)); F /= np.abs(F) + 1e-9
    c = np.real(np.fft.ifft2(F)); c = np.fft.fftshift(c)
    cy, cx = np.array(c.shape) // 2
    c[:max(cy - max_px, 0)] = -1; c[cy + max_px + 1:] = -1; c[:, :max(cx - max_px, 0)] = -1; c[:, cx + max_px + 1:] = -1
    py_, px_ = np.unravel_index(np.argmax(c), c.shape)
    return int(px_ - cx), int(py_ - cy), float(c.max())


for vi, view in enumerate(cfg["views"]):
    a = load(view["ref"]); fx0, fx1, fy0, fy1 = fit(view, a)
    zm = None
    if view.get("mask_png"):
        zm = load(view["mask_png"])[..., 0] > 0.5
        _ys, _xs = np.where(zm)
        view.setdefault("mask", [int(_xs.min()), int(_ys.min()), int(_xs.max()) + 1, int(_ys.max()) + 1])
        _r = max(int(view.get("feather", 3)), 1); zf = zm.astype(np.float32)
        for _ax in (0, 1):   # separable box blur = soft edge of width ~feather, inside and out
            _c = np.cumsum(np.pad(zf, [(_r + 1, _r) if i == _ax else (0, 0) for i in (0, 1)], mode="edge"), axis=_ax)
            zf = (np.take(_c, range(2 * _r + 1, _c.shape[_ax]), axis=_ax) - np.take(_c, range(0, _c.shape[_ax] - 2 * _r - 1), axis=_ax)) / (2 * _r + 1)
        zf = np.clip((zf - 0.5) * 2, 0, 1)   # 0 at the rim, 1 a feather-width inside
    if view.get("sharpen") or view.get("contrast"):
        _x0, _y0, _x1, _y1 = view["mask"]; _pad = 4
        _bx0, _by0, _bx1, _by1 = _x0 - _pad, _y0 - _pad, _x1 + _pad, _y1 + _pad
        _f = a[_by0:_by1, _bx0:_bx1, :3].copy()
        if view.get("sharpen"):
            _r, _pc = view["sharpen"]; _k = np.exp(-0.5 * (np.arange(-int(3 * _r) - 1, int(3 * _r) + 2) / _r) ** 2); _k /= _k.sum()
            _bl = _f
            for _ax in (0, 1):
                _bl = np.apply_along_axis(lambda v: np.convolve(np.pad(v, len(_k) // 2, mode="edge"), _k, mode="valid"), _ax, _bl)
            _f = np.clip(_f + (_f - _bl) * (_pc / 100.0), 0, 1)
        if view.get("contrast"):
            _m = _f.mean(axis=(0, 1), keepdims=True); _f = np.clip(_m + (_f - _m) * view["contrast"], 0, 1)
        a = a.copy(); a[_by0:_by1, _bx0:_bx1, :3] = _f
    if view.get("delight_px") and zm is not None:   # fallback albedo pass: flatten large-scale shading inside the zone, keep fine detail
        _r = int(view["delight_px"]); _m = zm.astype(np.float32)
        _L = a[..., :3] @ np.array([0.299, 0.587, 0.114], np.float32)
        def _box(x, r):
            for _ax in (0, 1):
                _c = np.cumsum(np.pad(x, [(r + 1, r) if i == _ax else (0, 0) for i in (0, 1)], mode="edge"), axis=_ax)
                x = (np.take(_c, range(2 * r + 1, _c.shape[_ax]), axis=_ax) - np.take(_c, range(0, _c.shape[_ax] - 2 * r - 1), axis=_ax)) / (2 * r + 1)
            return x
        _lo = _box(_box(_L * _m, _r), _r) / np.maximum(_box(_box(_m, _r), _r), 1e-4)   # zone-only low-pass (normalised convolution)
        _tgt = float(np.median(_L[zm]))
        _gain = np.clip(_tgt / np.maximum(_lo, 1e-3), 0.6, 1.6)
        a = a.copy(); a[..., :3] = np.where(zm[..., None], np.clip(a[..., :3] * _gain[..., None], 0, 1), a[..., :3])
    side = view["side"]; back = side == "back"; sgn = -1.0 if back else 1.0
    ax_u, flip_u = {"front": (0, False), "back": (0, True), "left": (1, True), "right": (1, False)}[side]
    dx, dy = view.get("dx", 0), view.get("dy", 0)
    def proj(p):
        u = (p[..., ax_u] - bmin[ax_u]) / (bmax[ax_u] - bmin[ax_u]); u = 1 - u if flip_u else u
        px_, py_ = fx0 + u * (fx1 - fx0), fy1 - (p[..., 2] - bmin[2]) / (bmax[2] - bmin[2]) * (fy1 - fy0)
        if view.get("zoom"):   # local magnification of the reference about zoom_c (default: mask centre), for a head that is larger/smaller than the painting's
            zx, zy = view["zoom"]; zc = view.get("zoom_c", [(view["mask"][0] + view["mask"][2]) / 2, (view["mask"][1] + view["mask"][3]) / 2])
            px_ = zc[0] + (px_ - zc[0]) / zx; py_ = zc[1] + (py_ - zc[1]) / zy
        if view.get("rotate"):   # rotate the reference about zoom_c (deg, +ve = sample ref points lower on the right): levels a tilted painted head on a level mesh
            _t = math.radians(view["rotate"]); _zc = view.get("zoom_c", [(view["mask"][0] + view["mask"][2]) / 2, (view["mask"][1] + view["mask"][3]) / 2])
            _ox, _oy = px_ - _zc[0], py_ - _zc[1]
            px_ = _zc[0] + _ox * math.cos(_t) - _oy * math.sin(_t); py_ = _zc[1] + _ox * math.sin(_t) + _oy * math.cos(_t)
        return px_ + dx, py_ + dy
    vdir = np.array({"front": [0, -1.0, 0], "back": [0, 1.0, 0], "left": [-1.0, 0, 0], "right": [1.0, 0, 0]}[side])  # model -> viewer
    mx0, my0, mx1, my1 = view["mask"]; fe = view.get("feather", 3); nd = view.get("ndot", 0.5)
    if view.get("auto_align"):   # measure the ref<->mesh offset inside this zone instead of hand-tuning dx/dy
        _aa = view["auto_align"] if isinstance(view["auto_align"], dict) else {}
        _mp = _aa.get("max_px", 30); _pad = _aa.get("pad_px", 24)
        dx, dy = 0, 0
        _img, _cov = splat((view["ref"], side, tuple(view["crop"])), proj, vdir, a.shape[:2])
        _x0, _y0, _x1, _y1 = view["mask"]
        _x0 = max(_x0 - _pad, 0); _y0 = max(_y0 - _pad, 0); _x1 = min(_x1 + _pad, a.shape[1]); _y1 = min(_y1 + _pad, a.shape[0])
        _g = lambda im: im[_y0:_y1, _x0:_x1, :3] @ np.array([0.299, 0.587, 0.114], np.float32)
        _sx, _sy, _pk = phase_shift(_g(a), _g(_img), _cov[_y0:_y1, _x0:_x1], _mp)
        dx, dy = _sx, _sy
        view["_auto"] = {"dx": dx, "dy": dy, "peak": round(_pk, 3)}
    pu, pv = proj(vco)
    if vi == 0 and cfg.get("overlay"):
        o = a[..., :3].copy(); H2, W2 = o.shape[:2]
        ix = np.clip(pu.astype(int), 0, W2 - 1); iy = np.clip(pv.astype(int), 0, H2 - 1)
        o[iy, ix] = [1, 0, 0]; o[my0:my0 + 2, mx0:mx1] = [0, 0, 1]; o[my1:my1 + 2, mx0:mx1] = [0, 0, 1]
        o[my0:my1, mx0:mx0 + 2] = [0, 0, 1]; o[my0:my1, mx1:mx1 + 2] = [0, 0, 1]
        cx0, cy0, cx1, cy1 = view["crop"]; c = o[cy0:cy1, cx0:cx1][::-1]
        oi = bpy.data.images.new("ov", c.shape[1], c.shape[0]); oi.pixels = np.dstack([c, np.ones(c.shape[:2])]).ravel().tolist()
        oi.filepath_raw = P(cfg["overlay"]); oi.file_format = "PNG"; oi.save()
    n_w = 0
    for ti in range(len(tv)):
        vs = tv[ti]
        if not ((pu[vs] > mx0 - 20) & (pu[vs] < mx1 + 20) & (pv[vs] > my0 - 20) & (pv[vs] < my1 + 20)).any(): continue
        if (nrm[ti] @ vdir).max() < nd - 0.3: continue
        luv = uv[tris[ti]] * [W, H]
        lo = np.floor(luv.min(0)).astype(int); hi = np.ceil(luv.max(0)).astype(int)
        xs, ys = np.meshgrid(np.arange(lo[0], hi[0] + 1), np.arange(lo[1], hi[1] + 1))
        q = np.stack([xs + 0.5, ys + 0.5], -1).reshape(-1, 2)
        a0, b0, c0 = luv
        d = (b0[1] - c0[1]) * (a0[0] - c0[0]) + (c0[0] - b0[0]) * (a0[1] - c0[1])
        if abs(d) < 1e-9: continue
        w0 = ((b0[1] - c0[1]) * (q[:, 0] - c0[0]) + (c0[0] - b0[0]) * (q[:, 1] - c0[1])) / d
        w1 = ((c0[1] - a0[1]) * (q[:, 0] - c0[0]) + (a0[0] - c0[0]) * (q[:, 1] - c0[1])) / d
        w2 = 1 - w0 - w1; ok = (w0 >= -0.02) & (w1 >= -0.02) & (w2 >= -0.02)
        if not ok.any(): continue
        w = np.stack([w0, w1, w2], 1)[ok]; qq = q[ok]
        p3 = w @ vco[vs]; n3 = w @ nrm[ti]; n3 /= np.linalg.norm(n3, axis=1, keepdims=True) + 1e-9
        u2, v2 = proj(p3)
        edge = np.minimum.reduce([u2 - mx0, mx1 - u2, v2 - my0, my1 - v2])
        if view.get("ellipse"):   # mask = superellipse inscribed in the box (exponent `ellipse`, 2 = ellipse, 3-4 = rounded patch); feather is measured inward from its rim
            _p = float(view["ellipse"]); _rx = (mx1 - mx0) / 2; _ry = (my1 - my0) / 2
            _d = (np.abs((u2 - (mx0 + mx1) / 2) / _rx) ** _p + np.abs((v2 - (my0 + my1) / 2) / _ry) ** _p) ** (1 / _p)
            edge = (1 - _d) * min(_rx, _ry)
        al = np.clip(edge / max(fe, 1e-6), 0, 1) * (n3 @ vdir > nd)
        if zm is not None:   # SAM zone mask replaces the box edge
            _ix = np.clip(u2.astype(int), 0, zf.shape[1] - 1); _iy = np.clip(v2.astype(int), 0, zf.shape[0] - 1)
            al = zf[_iy, _ix] * (n3 @ vdir > nd)
        if view.get("ndot_soft"):   # fade in over [ndot, ndot+soft] instead of a hard cut: no stretched smear or seam where the surface turns away (cheeks)
            al = al * np.clip((n3 @ vdir - nd) / view["ndot_soft"], 0, 1)
        for _c in ([view["clip"]] if isinstance(view.get("clip"), dict) else view.get("clip", [])):   # world-space slab: no depth test, so cut far walls of rings/loops
            _v = p3[:, "xyz".index(_c["axis"])]
            al = al * (_v >= _c.get("min", -1e9)) * (_v <= _c.get("max", 1e9))
        sel = al > 0
        if not sel.any(): continue
        ix = np.clip(u2[sel].astype(int), 0, a.shape[1] - 1); iy = np.clip(v2[sel].astype(int), 0, a.shape[0] - 1)
        if view.get("bilinear"):
            fu = np.clip(u2[sel] - 0.5, 0, a.shape[1] - 1.001); fv = np.clip(v2[sel] - 0.5, 0, a.shape[0] - 1.001)
            i0 = fu.astype(int); j0 = fv.astype(int); tu = (fu - i0)[:, None]; tvv = (fv - j0)[:, None]
            samp = (a[j0, i0, :3] * (1 - tu) * (1 - tvv) + a[j0, i0 + 1, :3] * tu * (1 - tvv)
                    + a[j0 + 1, i0, :3] * (1 - tu) * tvv + a[j0 + 1, i0 + 1, :3] * tu * tvv)
        else:
            samp = a[iy, ix, :3]
        if view.get("color_gain"):   # per-channel gain: colour-correct a derived source to the canonical zone colour (nhxz)
            samp = np.clip(samp * np.array(view["color_gain"], dtype=np.float32), 0, 1)
        tx = np.clip(qq[sel, 0].astype(int), 0, W - 1); ty = np.clip(qq[sel, 1].astype(int), 0, H - 1)
        al = al[sel][:, None]
        if view.get("exclude_hsv"):   # ref pixels inside any {hue,sat,val} box (e.g. blond hair) are never written onto the texture
            _mx = samp.max(1); _mn = samp.min(1); _dd = _mx - _mn + 1e-9
            _h = np.where(_mx == samp[:, 0], ((samp[:, 1] - samp[:, 2]) / _dd) % 6, np.where(_mx == samp[:, 1], (samp[:, 2] - samp[:, 0]) / _dd + 2, (samp[:, 0] - samp[:, 1]) / _dd + 4)) / 6
            _s = _dd / (_mx + 1e-9); _v = _mx
            for _bx in view["exclude_hsv"]:
                _hit = (_h >= _bx["hue"][0]) & (_h <= _bx["hue"][1]) & (_s >= _bx.get("sat", [0, 1])[0]) & (_s <= _bx.get("sat", [0, 1])[1]) & (_v >= _bx.get("val", [0, 1])[0]) & (_v <= _bx.get("val", [0, 1])[1])
                al = al * (1 - _hit[:, None] * 1.0)
        tex[ty, tx, :3] = tex[ty, tx, :3] * (1 - al) + samp * al
        n_w += len(tx)
    # reliability: silhouette IoU at 1/8 scale (projected vertices vs the reference figure inside crop)
    _s = 8; cx0, cy0, cx1, cy1 = view["crop"]; gw, gh = (cx1 - cx0) // _s + 1, (cy1 - cy0) // _s + 1
    gm = np.zeros((gh, gw), bool)
    _cu, _cv = proj(vco[tv].mean(1))   # triangle centroids densify the silhouette
    for _u, _v in ((pu, pv), (_cu, _cv)):
        _gx = ((_u - dx - cx0) // _s).astype(int); _gy = ((_v - dy - cy0) // _s).astype(int)
        _k = (_gx >= 0) & (_gx < gw) & (_gy >= 0) & (_gy < gh); gm[_gy[_k], _gx[_k]] = True
    def _sh(m, op):   # 3x3 dilate (op=any) / erode (op=all) without scipy
        pm = np.pad(m, 1, constant_values=(op == "all")); st = [pm[1 + dy_:1 + dy_ + m.shape[0], 1 + dx_:1 + dx_ + m.shape[1]] for dy_ in (-1, 0, 1) for dx_ in (-1, 0, 1)]
        return np.logical_or.reduce(st) if op == "any" else np.logical_and.reduce(st)
    gm = _sh(_sh(gm, "any"), "all")   # close 1-cell holes
    _fg = a[cy0:cy1, cx0:cx1, :3].min(2) < view.get("bg", 225) / 255.0
    gr = np.zeros((gh, gw), bool); _yy, _xx = np.where(_fg); gr[_yy // _s, _xx // _s] = True
    iou = float((gm & gr).sum() / max((gm | gr).sum(), 1))
    REPORT.append({"view": vi, "side": side, "ref": view["ref"], "mask_png": view.get("mask_png"), "silhouette_iou": round(iou, 3),
                   "reliable": iou >= cfg.get("reliable_iou", 0.85), "texels_written": int(n_w), "auto_align": view.get("_auto")})
    print("view", side, view.get("_zone", vi), "iou", round(iou, 3), "texels", n_w, "auto", view.get("_auto"))

ni = bpy.data.images.new("base_fixed", W, H, alpha=True)
ni.colorspace_settings.name = img.colorspace_settings.name
ni.pixels.foreach_set(tex.ravel()); ni.update(); ni.file_format = "JPEG"
texnode.image = ni
out = P(cfg.get("out_glb", cfg["glb"]))
bpy.ops.export_scene.gltf(filepath=out, export_format="GLB", export_animations=True, export_skins=True, export_image_format="AUTO", export_jpeg_quality=92)
_rp = P(cfg["report"]) if cfg.get("report") else out.replace(".glb", "_projection_report.json")
json.dump({"glb": cfg["glb"], "out": cfg.get("out_glb", cfg["glb"]), "views": REPORT}, open(_rp, "w"), indent=1)
print("wrote", os.path.basename(out), "| report", os.path.basename(_rp), "| unreliable views:", [r["view"] for r in REPORT if not r["reliable"]] or "none")
