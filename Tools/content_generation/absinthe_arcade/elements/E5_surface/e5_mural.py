"""Build the mural texture set in facade space (plain Python: numpy, scipy, Pillow). Re-runnable.

  <venv python> e5_mural.py [--preview out.png]

Mural sheet: facade plane x in [SHEET_X0, SHEET_X1], z in [SHEET_Z0, SHEET_Z1] (metres, Blender frame),
4096 px tall. The decal mesh (e5_build.py) maps UVs by (x, z) onto this sheet.

Sources (author ruling Q-004/Q-010):
  * panel 1 ("Clean Artwork Reference") of references/Exterior/muralreference.png, warped onto the facade
    by control points matched against the bible rectified through aa_bible_cam (e5_rectify.py);
  * the rectified daytime bible, used where panel 1 does not reach (left vine, the pixel field down both
    sides of the arch, cut-off edges) and to decide where paint lies on the stone.
The painted keystone head of panel 1 is removed (E4's sculpture sits there) and the hole filled from the
surrounding paint. Outputs (textures/e5_surface/):
  e5_mural_basecolor.png   RGBA, alpha = paint coverage
  e5_mural_emissive.png    faint glow of the circuit traces and the neon pixels
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e5_rectify import REPO, rectify_bible, sheet_grid  # noqa: E402

OUT = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/textures/e5_surface"
PANEL = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/muralreference.png"
from e5_sheet import PPM, SHEET_X0, SHEET_X1, SHEET_Z0, SHEET_Z1  # noqa: E402,F401

# control points: panel-1 px (u, v)  <->  facade metres (x, z) read off the rectified bible
CTRL = [
    ((850, 1160), (-0.367, 9.233)),    # fairy's eye
    ((1044, 1206), (0.10, 9.033)),     # nose tip
    ((640, 1456), (-0.947, 8.68)),     # gold earring
    ((1380, 1440), (1.12, 8.467)),     # token centre
    ((410, 1310), (-1.567, 9.033)),    # big hair blossom
    ((240, 2740), (-1.787, 6.333)),    # lower-left blossom
    ((780, 3180), (0.0, 5.233)),       # keystone nose (panel's painted head)
]
PANEL_BOX = (30, 610, 1525, 3330)                 # panel-1 artwork area (px), below the caption
HEAD_HOLE = ((0.0, 5.4), (0.95, 0.85))            # facade ellipse (centre, radii) of the painted head/cups
# regions where the bible's paint is taken (facade metres): main mural + arch sides (all paint kinds);
# the left wall vines (green only)
REGIONS = [(-2.75, 2.9, 2.6, 10.95)]
VINE_REGIONS = [(-5.1, -2.6, 3.7, 9.8)]           # left window column: around the cat window, its pediment,
#                                                   down beside the arched window, and the far-left wall edge
VINE_EXCLUDE = [(-3.95, -2.75, 3.0, 5.05),          # arched window opening + its pots / balconette
                (-3.95, -2.8, 6.85, 9.0),           # cat window opening, curtains, pots and the cat
                (-3.95, -2.8, 10.1, 12.4)]          # balcony window, flowers
EXCLUDE = [(1.55, 2.65, 6.4, 9.7), (2.55, 3.0, 6.4, 12.4)]   # right window + sill plants; the downpipe strip


def hsv(rgb):
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx, mn = rgb.max(-1), rgb.min(-1)
    d = mx - mn
    h = np.zeros_like(mx)
    m = d > 1e-6
    rm = m & (mx == r)
    gm = m & (mx == g) & ~rm
    bm = m & ~rm & ~gm
    h[rm] = ((g - b)[rm] / d[rm]) % 6
    h[gm] = (b - r)[gm] / d[gm] + 2
    h[bm] = (r - g)[bm] / d[bm] + 4
    return h / 6.0, np.where(mx > 1e-6, d / np.maximum(mx, 1e-6), 0), mx


def e4_fixture_mask(X, Z):
    """E4's conduits, cables, hoses and boxes (bible px traces) projected onto the sheet: the 3D pieces sit on
    the wall there, so the bible's painted-over pipes must not end up in the mural paint."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "E4_keystone_conduits"))
    import e4_trace as T4
    from e5_rectify import Cam
    cam = Cam()
    from PIL import ImageDraw
    W, H = X.shape[1], X.shape[0]
    im = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(im)

    def to_sheet(u, v):
        ray = cam.R @ np.array([(u - cam.W / 2) / cam.f, -(v - cam.H / 2) / cam.f, -1.0])
        t = (0.0 - cam.loc[1]) / ray[1]
        x, z = cam.loc[0] + t * ray[0], cam.loc[2] + t * ray[2]
        return ((x - SHEET_X0) * PPM, (SHEET_Z1 - z) * PPM)
    for runs, pad in ((T4.PURPLE, 1.9), (T4.BLACK, 2.2), ([g[:3] for g in T4.GREEN], 1.5)):
        for r in runs:
            name, verts, wpx = r[0], r[1], r[2]
            pts = [to_sheet(u, v) for u, v in verts]
            d.line(pts, fill=255, width=max(4, int(wpx * pad * 0.42 * PPM / 410)), joint="curve")
    for name, (u, v), wpx, hpx, depth, feat in T4.BOXES:
        cx, cy = to_sheet(u, v)
        w, h = wpx * 0.45 * PPM / 410, hpx * 0.45 * PPM / 410
        d.rectangle([cx - w, cy - h, cx + w, cy + h], fill=255)
    return np.asarray(im) > 0


def fit_tps():
    """Thin-plate warp facade (x, z) -> panel (u, v) through every control point (affine part + bend)."""
    from scipy.interpolate import RBFInterpolator
    src = np.array([c[1] for c in CTRL], float)
    dst = np.array([c[0] for c in CTRL], float)
    return RBFInterpolator(src, dst, kernel="thin_plate_spline", degree=1, smoothing=0.0)


HAIR_WEIGHT = 1.0
HAIR_SPOTS = {"crown": (-1.4, 10.0), "left_locks": (-2.1, 9.3), "behind_ear": (-1.25, 8.3), "lower_left": (-2.2, 8.0),
              "right_back": (0.3, 8.6)}


def hsv2rgb(h, s, v):
    i = np.floor(h * 6).astype(int) % 6
    f = h * 6 - np.floor(h * 6)
    p, q, t = v * (1 - s), v * (1 - f * s), v * (1 - (1 - f) * s)
    r = np.choose(i, [v, q, p, p, t, v])
    g = np.choose(i, [t, v, v, q, p, p])
    b = np.choose(i, [p, p, t, v, v, q])
    return np.stack([r, g, b], -1)


def fit_affine():
    A, bu, bv = [], [], []
    for (u, v), (x, z) in CTRL:
        A.append([x, z, 1.0])
        bu.append(u)
        bv.append(v)
    A = np.array(A)
    cu, *_ = np.linalg.lstsq(A, np.array(bu), rcond=None)
    cv, *_ = np.linalg.lstsq(A, np.array(bv), rcond=None)
    res = [float(np.hypot(A[i] @ cu - bu[i], A[i] @ cv - bv[i])) for i in range(len(CTRL))]
    return cu, cv, res


def main():
    prev = sys.argv[sys.argv.index("--preview") + 1] if "--preview" in sys.argv else None
    OUT.mkdir(parents=True, exist_ok=True)
    X, Z = sheet_grid(SHEET_X0, SHEET_X1, SHEET_Z0, SHEET_Z1, PPM)
    bib, bvalid = rectify_bible(SHEET_X0, SHEET_X1, SHEET_Z0, SHEET_Z1, PPM)
    # ---- panel 1 warped onto the facade
    Image.MAX_IMAGE_PIXELS = None
    P = np.asarray(Image.open(PANEL).convert("RGB")).astype(np.float32) / 255.0
    cu, cv, res = fit_affine()
    tps = fit_tps()
    small = 8                                        # evaluate the warp on a coarse grid, then upsample
    Xs, Zs = X[::small, ::small], Z[::small, ::small]
    uv = tps(np.stack([Xs.ravel(), Zs.ravel()], -1)).reshape(Xs.shape + (2,))
    pu = ndi.zoom(uv[..., 0], (X.shape[0] / Xs.shape[0], X.shape[1] / Xs.shape[1]), order=1)[:X.shape[0], :X.shape[1]]
    pv = ndi.zoom(uv[..., 1], (X.shape[0] / Xs.shape[0], X.shape[1] / Xs.shape[1]), order=1)[:X.shape[0], :X.shape[1]]
    pan = np.zeros(X.shape + (3,), np.float32)
    for ch in range(3):
        pan[..., ch] = ndi.map_coordinates(P[..., ch], [pv - 0.5, pu - 0.5], order=1, mode="nearest")
    in_panel = (pu > PANEL_BOX[0]) & (pu < PANEL_BOX[2]) & (pv > PANEL_BOX[1]) & (pv < PANEL_BOX[3])
    (hx, hz), (rx, rz) = HEAD_HOLE
    hole = ((X - hx) / rx) ** 2 + ((Z - hz) / rz) ** 2 < 1.0
    # ---- where is paint on the stone (bible) / in the artwork (panel)
    h, s, v = hsv(bib)
    def boxes(bx):
        m = np.zeros(X.shape, bool)
        for (x0, x1, z0, z1) in bx:
            m |= (X > x0) & (X < x1) & (Z > z0) & (Z < z1)
        return m
    arch = ((X / 2.45) ** 2 + ((Z - 3.6) / 1.58) ** 2 < 1.0) | ((np.abs(X) < 2.45) & (Z < 3.6))
    region = boxes(REGIONS) & ~arch & ~boxes(EXCLUDE)
    vines = boxes(VINE_REGIONS)
    greenteal = (h > 0.17) & (h < 0.58) & (s > 0.18) & (v > 0.12)
    purple = (h > 0.68) & (h < 0.95) & (s > 0.22) & (v > 0.15)
    gold = (h > 0.08) & (h < 0.17) & (s > 0.5) & (v > 0.5)
    darkpix = (v < 0.17) & (s < 0.45) & ~((h > 0.02) & (h < 0.15))     # near-black pixels, not brown shadow
    vine_green = (h > 0.18) & (h < 0.52) & (s > 0.14) & (v > 0.1)
    vine_dark = (v < 0.22) & (h > 0.18) & (h < 0.55)                    # dark green outlines
    vines &= ~boxes(VINE_EXCLUDE)
    vpaint = vines & bvalid & (vine_green | vine_dark)
    vpaint = ndi.binary_opening(ndi.binary_closing(vpaint, iterations=2), iterations=1)
    # pale blossom petals (lower-left spandrel, hair flowers): near-white, only where green paint surrounds them
    petal = region & bvalid & (s < 0.16) & (v > 0.7) & ndi.binary_dilation(greenteal & region, iterations=int(0.02 * PPM))
    # near-black paint (the pixel field's dark squares) only in the artwork or down the arch sides: elsewhere a
    # near-black bible pixel is a moulding shadow, not paint
    darkpix &= in_panel | (Z < 6.6)
    sage = (h > 0.17) & (h < 0.5) & (s > 0.1) & (v > 0.22) & (v < 0.8)       # muted sage leaves and stems
    bpaint = (region & bvalid & (greenteal | purple | gold | darkpix | petal | sage)) | vpaint
    bpaint = ndi.binary_opening(ndi.binary_closing(bpaint, iterations=3), iterations=2)
    ph, ps, pv_ = hsv(pan)
    panel_bg_raw = ((pv_ < 0.27) & (ps < 0.55)) | ((ph > 0.55) & (ph < 0.75) & (pv_ < 0.24))   # panel 1's navy
    backdrop = ndi.binary_dilation(panel_bg_raw & in_panel, iterations=3)
    # panel 1's dark backdrop is paint wherever the bible shows saturated paint under it (dark hair strands, the
    # pixel field's dark squares: coloured from the bible); elsewhere it stays backdrop. Dark navy-hued panel
    # pixels with no bible paint nearby are backdrop too; dark teal hair strands are not navy, so they stay.
    bcream = (h > 0.06) & (h < 0.125) & (s > 0.12) & (s < 0.36) & (v > 0.55)   # beige: plaster (or pale skin)
    plaster = ndi.gaussian_filter(bcream.astype(np.float32), 0.015 * PPM) > 0.55
    bp_near = ndi.binary_dilation(bpaint, iterations=2)
    keep_dark = in_panel & panel_bg_raw & np.where(Z < 7.5, bp_near, bpaint) & bvalid   # tight around the fairy
    panel_bg = panel_bg_raw & ~keep_dark
    panel_bg |= in_panel & (pv_ < 0.36) & (ph > 0.55) & (ph < 0.8) & ~ndi.binary_dilation(bpaint, iterations=4)
    pfg = in_panel & ((pv_ > 0.15) | keep_dark) & ~panel_bg & ~hole & ~arch
    pfg = ndi.binary_opening(pfg, iterations=1)
    fixtures = e4_fixture_mask(X, Z)
    paint = (bpaint & ~fixtures) | pfg | (hole & ~arch)
    # the mural is painted solid inside its silhouette: close small gaps, fill enclosed holes < ~0.15 m2
    paint = ndi.binary_closing(paint, structure=np.ones((5, 5)), iterations=2)
    holes = ndi.binary_fill_holes(paint) & ~paint
    lab, n = ndi.label(holes)
    if n:
        sizes = ndi.sum(holes, lab, range(1, n + 1))
        plf = ndi.mean(plaster, lab, range(1, n + 1))       # holes the bible shows as bare plaster stay open
        small = np.isin(lab, [i + 1 for i, (sz, pf) in enumerate(zip(sizes, plf))
                              if sz < 0.15 * PPM * PPM or (sz < 0.6 * PPM * PPM and pf < 0.6)])
        paint |= small
    paint &= ~fixtures & ~arch
    # bible-colour fallback (painted, but not by panel 1): keep it only where the bible itself has paint nearby,
    # and inside the artwork area never where panel 1 says backdrop and the bible pixel is dark (halo specks)
    fallback = paint & ~pfg & ~hole
    # only where panel 1 shows its own backdrop AND the bible shows bare plaster (the halo-edge specks)
    bcream_px = (h > 0.05) & (h < 0.16) & (s < 0.38) & (v > 0.5)
    paint &= ~(fallback & in_panel & backdrop & bcream_px)
    alpha = paint.astype(np.float32)
    alpha = ndi.gaussian_filter(alpha, 1.2)
    # ---- colour: panel inside its area, the bible elsewhere; head hole filled from its surroundings
    # colour grade toward the bible's deeper, muted paint: per-channel mean/std match on co-painted pixels
    # (moment matching keeps the artwork's contrast; a regression would flatten it toward the mean)
    both = pfg & bpaint & ~hole
    pp, bb_ = pan[both], bib[both]
    gain = bb_.std(0) / np.maximum(pp.std(0), 1e-4)
    off = bb_.mean(0) - gain * pp.mean(0)
    pan = np.clip(pan * gain + off, 0, 1)
    # hair: per-pixel hue/saturation pulled hard toward the bible's emerald/teal (skin is mint: excluded)
    gh, gs, gv = hsv(pan)
    hair = (gh > 0.36) & (gh < 0.58) & (gs > 0.22)
    bh_, bs_, bv_ = hsv(bib)
    bhair = bpaint & (bh_ > 0.36) & (bh_ < 0.58) & (bs_ > 0.22)
    sig = 0.05 * PPM                                          # local bible hair colour, ~5 cm neighbourhood
    wb = ndi.gaussian_filter(bhair.astype(np.float32), sig)
    loc_h = ndi.gaussian_filter(np.where(bhair, bh_, 0), sig) / np.maximum(wb, 1e-4)
    loc_s = ndi.gaussian_filter(np.where(bhair, bs_, 0), sig) / np.maximum(wb, 1e-4)
    loc_v = ndi.gaussian_filter(np.where(bhair, bv_, 0), sig) / np.maximum(wb, 1e-4)
    ours_v = ndi.gaussian_filter(np.where(hair, gv, 0), sig) / np.maximum(ndi.gaussian_filter(hair.astype(np.float32), sig), 1e-4)
    gl_h, gl_s = float(np.median(bh_[bhair])), float(np.median(bs_[bhair]))
    have = np.clip(wb * 4, 0, 1)                              # where the bible has hair nearby use it, else global
    tgt_h = have * loc_h + (1 - have) * gl_h
    tgt_s = have * loc_s + (1 - have) * gl_s
    w = ndi.gaussian_filter(hair.astype(np.float32), 1.5) * HAIR_WEIGHT
    gh2 = gh + (tgt_h - gh) * w
    gs2 = np.clip(gs + (tgt_s - gs) * w, 0, 1)
    vk = np.where(have > 0.2, np.clip(loc_v / np.maximum(ours_v, 1e-3), 0.6, 1.2), 1.0)   # local tone, detail kept
    gv2 = np.clip(gv * (1 + (vk - 1) * w), 0, 1)
    pan = hsv2rgb(gh2 % 1.0, gs2, gv2)
    # report: 4 hair spots (facade metres) pan vs bible, hue / sat medians in 6 cm windows
    for nm, (sx, sz) in HAIR_SPOTS.items():
        c_ = int((sx - SHEET_X0) * PPM)
        r_ = int((SHEET_Z1 - sz) * PPM)
        win = (slice(r_ - 25, r_ + 25), slice(c_ - 25, c_ + 25))
        ph2, ps2, pv2 = hsv(pan[win])
        mh = hair[win] & bhair[win]
        if mh.sum() > 10:
            print("E5 HAIR SPOT", nm, "ours h/s/v", round(float(np.median(ph2[mh])), 3), round(float(np.median(ps2[mh])), 3),
                  round(float(np.median(pv2[mh])), 3), "bible", round(float(np.median(bh_[win][mh])), 3),
                  round(float(np.median(bs_[win][mh])), 3), round(float(np.median(bv_[win][mh])), 3))
    print("E5 GRADE gain", np.round(gain, 3).tolist(), "offset", np.round(off, 3).tolist())
    # where the bible covers the artwork, its own local paint colour (normalised blur inside the paint) carries
    # the colour and panel 1 only adds its crisp line detail on top: the mural matches the bible's saturation and
    # depth instead of a global grade
    pm = (alpha > 0.5).astype(np.float32)
    sg = 0.06 * PPM                     # regional colour only (warp residuals are 3-7 cm: no bible structure)
    wm = np.maximum(ndi.gaussian_filter(pm, sg), 1e-4)
    blo = np.stack([ndi.gaussian_filter(bib[..., c] * pm, sg) for c in range(3)], -1) / wm[..., None]
    plo = np.stack([ndi.gaussian_filter(pan[..., c] * pm, sg) for c in range(3)], -1) / wm[..., None]
    xfer = np.clip(blo + (pan - plo), 0, 1)
    # the fairy only (above the pixel field): panel 1's pixel grid does not line up with the bible's squares
    fairy = ndi.gaussian_filter(((Z > 7.5) & ndi.binary_erosion(bvalid, iterations=6)).astype(np.float32), 0.05 * PPM)
    cover = fairy[..., None]
    pan = xfer * cover + pan * (1 - cover)
    keep_pan = keep_dark & (Z < 7.5)          # the pixel field's dark squares: panel 1's own dark paint
    col = np.where((in_panel & ~panel_bg & ~(keep_dark & ~keep_pan))[..., None], pan, bib)    # never its backdrop
    # fill the painted-head hole with the circuit traces directly above it (they run down into the head)
    shift = int(round(1.0 * PPM))
    above = np.roll(col, shift, axis=0)
    col = np.where(hole[..., None], above, col)
    # ---- clean outer edges: within ~8 cm of the paint boundary, near-black pixels are dropped unless the bible
    # itself has a dark painted mark there (backdrop remnants and dark patch edges on bare plaster); then a
    # 1-2 px feather on the alpha edge
    band = paint & ~ndi.binary_erosion(paint, iterations=int(round(0.08 * PPM)))
    ch, cs, cv = hsv(col)
    near_black = (cv < 0.3) & (cs < 0.75)
    bible_dark_mark = bpaint & (v < 0.3)
    bible_bare = (h > 0.05) & (h < 0.15) & (s > 0.08) & (s < 0.42) & (v > 0.5)       # cream / ochre plaster
    drop = band & near_black & ~ndi.binary_dilation(bible_dark_mark, iterations=2)
    drop |= band & (cv < 0.45) & bible_bare                     # dark paint on stone the bible shows bare
    paint2 = paint & ~drop
    paint2 = ndi.binary_opening(paint2, iterations=1) | (paint2 & ~band)      # no 1-px slivers left on the edge
    lab, n = ndi.label(paint2 & band)
    if n:                                                                      # tiny islands left in the band
        sz = ndi.sum(paint2 & band, lab, range(1, n + 1))
        paint2 &= ~np.isin(lab, [i + 1 for i, z in enumerate(sz) if z < 40])
    alpha = ndi.gaussian_filter(paint2.astype(np.float32), 1.5)
    print("E5 EDGE CLEAN dropped px", int((paint & ~paint2).sum()), "band px", int(band.sum()))
    # ---- emissive: neon green traces and bright green / purple pixels glow faintly (bible)
    h2, s2, v2 = hsv(col)
    glow = (((h2 > 0.17) & (h2 < 0.30) & (s2 > 0.5) & (v2 > 0.62)) | ((h2 > 0.72) & (h2 < 0.9) & (s2 > 0.45) & (v2 > 0.6)))
    glow = ndi.binary_opening(glow, iterations=1) & (alpha > 0.5)
    emis = col * glow[..., None] * 0.9
    rgba = np.concatenate([col, alpha[..., None]], -1)
    if "--dump" in sys.argv:                                   # debugging aid: masks + colours at sheet scale
        np.savez_compressed(sys.argv[sys.argv.index("--dump") + 1], col=col[::4, ::4], bib=bib[::4, ::4],
                            pan=pan[::4, ::4], pfg=pfg[::4, ::4], keep=keep_dark[::4, ::4], pbg=panel_bg[::4, ::4],
                            bp=bpaint[::4, ::4], pl=plaster[::4, ::4], al=alpha[::4, ::4], inp=in_panel[::4, ::4])
    Image.fromarray((np.clip(rgba, 0, 1) * 255).astype(np.uint8), "RGBA").save(OUT / "e5_mural_basecolor.png")
    Image.fromarray((np.clip(emis, 0, 1) * 255).astype(np.uint8)).save(OUT / "e5_mural_emissive.png")
    print("E5 MURAL sheet", X.shape[::-1], "ppm", round(PPM, 1), "affine residuals px", [round(r, 1) for r in res],
          "paint cover %", round(100 * float((alpha > 0.5).mean()), 1), "glow %", round(100 * float(glow.mean()), 2))
    if prev:
        bg = np.full_like(col, 0.82)
        comp = col * alpha[..., None] + bg * (1 - alpha[..., None])
        Image.fromarray((np.clip(comp, 0, 1) * 255).astype(np.uint8)).resize((X.shape[1] // 4, X.shape[0] // 4)).save(prev)


def peel_zones():
    """Where the bible's plaster has peeled: local fraction of exposed ochre underlayer (brown, mid value),
    from the rectified bible, 1024 px tall. A starting mask the author can repaint (white = heavy peeling)."""
    from e5_sheet import ZONE_X0, ZONE_X1, ZONE_Z0, ZONE_Z1
    ppm = 1024 / (ZONE_Z1 - ZONE_Z0)
    img, valid = rectify_bible(ZONE_X0, ZONE_X1, ZONE_Z0, ZONE_Z1, ppm)
    h, s, v = hsv(img)
    ochre = (h > 0.045) & (h < 0.12) & (s > 0.32) & (s < 0.7) & (v > 0.38) & (v < 0.8) & valid
    frac = ndi.uniform_filter(ochre.astype(np.float32), size=int(0.35 * ppm))
    zone = np.clip((frac - 0.18) / 0.35, 0, 1)
    zone = ndi.gaussian_filter(zone, 2)
    Image.fromarray((zone * 255).astype(np.uint8)).save(OUT / "e5_peel_zones.png")
    print("E5 ZONES", zone.shape[::-1], "mean", round(float(zone.mean()), 3))


if __name__ == "__main__":
    peel_zones()
    main()
