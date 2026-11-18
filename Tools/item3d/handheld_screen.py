"""Repaint the Broken Handheld's screen and neume on the Tripo atlas (bead Eurobound-rspb).

Run (headless):
  "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python Tools/item3d/handheld_screen.py -- \
      dev/asset_team/icon_refs/aa_broken_symbol_handheld_tripo.glb dev/asset_team/icon_refs/aa_broken_symbol_handheld_tripo_screen.glb
then render the output GLB with Tools/item3d/render_item.py at yaw 5, pitch 20 (the R1-R3 framing):
  ... render_item.py -- dev/asset_team/icon_refs/aa_broken_symbol_handheld_tripo_screen.glb       game/assets/items/icons/3d/aa_broken_symbol_handheld_512.png 5 20

What it paints (fixed, deterministic; no hand edits, no image tool):
  * every screen texel: flat dead screen #101010;
  * three cracks from one impact point near the upper right, plus a small star at the impact,
    in dark plum #2B1A2E with a thin light edge on the lit side (author, Eurobound Desk
    asset-team-qc-aa_broken_symbol_handheld-cracks, 2026-11-16: "A: Allow a thin light edge on the cracks").
    The edge colour is a light tint of the same plum, so the cracks stay plum;
  * the raised neume: the front lozenge and hook flat toxic green #39FF14, the fainter lozenge behind it
    flat at 60 percent of that green (#22990C, the R3 value).
  * the body: the R1 texture fix, a per-channel gain (BODY_GAIN) on yellow-hued texels.
Colours come from design/items/debaucheryville_items/broken_symbol_game_boy_item.md (colours row).

How: the screen is one flat Tripo chart (top-left of the atlas). Each screen triangle is rasterised in UV
space; every texel's 3D position is mapped into a 2D screen frame (right / up across the glass), and the
paint is a function of that 2D position, so the cracks follow the glass however Tripo laid out the UVs.
Neume faces are the raised faces over the screen; each is voted bright or dim from the old texture and its
neighbours, then filled flat. Chart gutters are dilated so texture filtering never pulls in the old paint.
"""
import os
import sys

import bpy
import numpy as np

SCREEN_UV = (0.0, 0.75, 0.31, 1.0)       # u0, v0, u1, v1 of Tripo's screen chart
NEUME_BOX = (0.29, 0.16, 0.68, 0.79)     # normalised screen frame (x0, y0, x1, y1) that holds the neume
NEUME_Z = (-0.004, 0.07)                 # height above the glass, model units


def hx(s):
    return np.array([int(s[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255.0


SCREEN, PLUM, EDGE = hx("101010"), hx("2B1A2E"), hx("B9A3BC")
GREEN = hx("39FF14")
GREEN_DIM = GREEN * 0.6

# Cracks in the normalised screen frame (0,0 = lower left of the glass, 1,1 = upper right).
# All three start at IMPACT; they keep clear of the tape (upper left), the bezel and the neume (checked below).
IMPACT = (0.84, 0.82)
CRACKS = [
    [IMPACT, (0.74, 0.86), (0.63, 0.83), (0.52, 0.88)],                                          # left, under the top bezel
    [IMPACT, (0.79, 0.68), (0.74, 0.47), (0.71, 0.30), (0.62, 0.15), (0.46, 0.10), (0.30, 0.16)],  # down, then left under the hook
    [IMPACT, (0.91, 0.71), (0.88, 0.56), (0.91, 0.40), (0.86, 0.22), (0.88, 0.11)],              # down the right side
]
STAR = [(10.0, 0.040), (65.0, 0.032), (120.0, 0.045), (165.0, 0.030), (215.0, 0.036), (290.0, 0.034), (330.0, 0.030)]  # deg, units
W_IMPACT, W_END = 0.014, 0.006            # plum core width along each crack, model units
W_EDGE = 0.006                            # thin light edge: the core offset this far toward the light (upper left)
LIGHT = (-0.7071, 0.7071)                 # screen-frame direction of the key light (look.py key: upper left)
TAPE_BOX = (0.0, 0.79, 0.44, 1.0)         # normalised screen frame area under and beside the tape: no cracks
MIN_CLEAR_EDGE = 0.03                     # units between any crack and the bezel or the tape box
JAG = 0.020                               # jag amplitude, normalised (angular, glassy breaks)
MIN_CLEAR_NEUME = 0.015                   # units between any crack edge and the neume footprint
BODY_GAIN = (1.005, 1.056, 1.141)         # per-channel gain on the yellowed body: matches the R1 body (render median 199,190,154), which passed A4


def base_image(mat):
    for link in mat.node_tree.links:
        if link.to_node.type == "BSDF_PRINCIPLED" and link.to_socket.name == "Base Color" \
                and link.from_node.type == "TEX_IMAGE":
            return link.from_node.image
    raise SystemExit("no base colour image")


def jagged(pts, rng):
    out = [pts[0]]
    for a, b in zip(pts[:-1], pts[1:]):
        a, b = np.array(a), np.array(b)
        d = b - a
        nrm = np.array([-d[1], d[0]]) / (np.linalg.norm(d) + 1e-9)
        for t in (0.33, 0.66):
            out.append(tuple(a + d * t + nrm * rng.uniform(-JAG, JAG)))
        out.append(tuple(b))
    return out


def segments(to_units):
    """List of (p0, p1, half-width0, half-width1) in model units."""
    rng = np.random.default_rng(7)
    segs = []
    for crack in CRACKS:
        pts = np.array([to_units(p) for p in jagged(crack, rng)])
        lens = np.r_[0, np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))]
        w = W_IMPACT + (W_END - W_IMPACT) * lens / lens[-1]
        for i in range(len(pts) - 1):
            segs.append((pts[i], pts[i + 1], w[i] / 2, w[i + 1] / 2))
    c = np.array(to_units(IMPACT))
    for deg, ln in STAR:
        a = np.radians(deg)
        segs.append((c, c + ln * np.array([np.cos(a), np.sin(a)]), W_IMPACT * 0.42, W_END * 0.3))
    return segs


def crack_field(xy, segs):
    """Signed distance to the crack cores (negative inside), per point."""
    f = np.full(len(xy), 1e9, np.float32)
    for p0, p1, h0, h1 in segs:
        d = p1 - p0
        t = np.clip(((xy - p0) @ d) / (d @ d), 0, 1)
        dist = np.linalg.norm(xy - (p0 + t[:, None] * d), axis=1)
        f = np.minimum(f, dist - (h0 + (h1 - h0) * t))
    return f


def raster(uv_px, H, W):
    """Yield (rows, cols, barycentrics) of texel centres inside one triangle given in pixel coords."""
    (x0, y0), (x1, y1), (x2, y2) = uv_px
    c0, c1 = int(np.floor(min(x0, x1, x2))), int(np.ceil(max(x0, x1, x2)))
    r0, r1 = int(np.floor(min(y0, y1, y2))), int(np.ceil(max(y0, y1, y2)))
    c0, r0, c1, r1 = max(c0, 0), max(r0, 0), min(c1, W - 1), min(r1, H - 1)
    if c1 < c0 or r1 < r0:
        return None
    cs, rs = np.meshgrid(np.arange(c0, c1 + 1), np.arange(r0, r1 + 1))
    px, py = cs.ravel() + 0.5, rs.ravel() + 0.5
    den = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
    if abs(den) < 1e-12:
        return None
    b0 = ((y1 - y2) * (px - x2) + (x2 - x1) * (py - y2)) / den
    b1 = ((y2 - y0) * (px - x2) + (x0 - x2) * (py - y2)) / den
    b2 = 1 - b0 - b1
    m = (b0 >= -1e-6) & (b1 >= -1e-6) & (b2 >= -1e-6)
    if not m.any():
        return None
    return rs.ravel()[m], cs.ravel()[m], np.stack([b0[m], b1[m], b2[m]], 1)


def body_desaturate(img, rows=256):
    """R1 body fix: per-channel BODY_GAIN on yellow-hued texels (hue 30-75 deg), a greyer, less orange yellowed grey."""
    for r in range(0, img.shape[0], rows):
        c = img[r:r + rows]
        mx, mn = c.max(-1), c.min(-1)
        chroma = mx - mn
        R, G, B = c[..., 0], c[..., 1], c[..., 2]
        with np.errstate(divide="ignore", invalid="ignore"):
            hue = np.where(mx == R, ((G - B) / chroma) % 6, np.where(mx == G, (B - R) / chroma + 2, (R - G) / chroma + 4)) * 60
        m = (chroma > 0.02) & (hue >= 30) & (hue <= 75)
        c[m] = np.clip(c[m] * np.array(BODY_GAIN, np.float32), 0, 1)


def dilate(img, painted, covered, steps=4):
    """Grow painted texels into uncovered gutter texels so filtering never reads the old paint."""
    for _ in range(steps):
        grow = np.zeros_like(painted)
        src = np.zeros_like(img)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            sh_p = np.roll(painted, (dr, dc), (0, 1))
            sh_i = np.roll(img, (dr, dc), (0, 1))
            new = sh_p & ~painted & ~covered & ~grow
            src[new] = sh_i[new]
            grow |= new
        img[grow] = src[grow]
        painted |= grow


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    src, dst = os.path.abspath(argv[0]), os.path.abspath(argv[1])
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    obj = [o for o in bpy.data.objects if o.type == "MESH"][0]
    me = obj.data
    me.calc_loop_triangles()
    im = base_image(obj.material_slots[0].material)
    W, H = im.size

    co = np.empty(len(me.vertices) * 3, np.float32); me.vertices.foreach_get("co", co); co = co.reshape(-1, 3)
    uvl = np.empty(len(me.loops) * 2, np.float32); me.uv_layers.active.data.foreach_get("uv", uvl); uvl = uvl.reshape(-1, 2)
    nt = len(me.loop_triangles)
    tv = np.empty(nt * 3, np.int32); me.loop_triangles.foreach_get("vertices", tv); tv = tv.reshape(-1, 3)
    tl = np.empty(nt * 3, np.int32); me.loop_triangles.foreach_get("loops", tl); tl = tl.reshape(-1, 3)
    tp = np.empty(nt, np.int32); me.loop_triangles.foreach_get("polygon_index", tp)
    npoly = len(me.polygons)
    pn = np.empty(npoly * 3, np.float32); me.polygons.foreach_get("normal", pn); pn = pn.reshape(-1, 3)
    pc = np.empty(npoly * 3, np.float32); me.polygons.foreach_get("center", pc); pc = pc.reshape(-1, 3)
    pa = np.empty(npoly, np.float32); me.polygons.foreach_get("area", pa)

    pix = np.empty(W * H * 4, np.float32); im.pixels.foreach_get(pix); pix = pix.reshape(H, W, 4)
    tuv = uvl[tl]                                        # (T,3,2)
    tri_uvc = tuv.mean(1)
    tri_px = np.stack([tuv[..., 0] * W, tuv[..., 1] * H], -1)   # Blender pixel rows run bottom-up, like v

    # --- screen plane and its 2D frame
    u0, v0, u1, v1 = SCREEN_UV
    box = (tri_uvc[:, 0] > u0) & (tri_uvc[:, 0] < u1) & (tri_uvc[:, 1] > v0) & (tri_uvc[:, 1] < v1)
    bp = np.unique(tp[box])
    n = (pn[bp] * pa[bp, None]).sum(0); n /= np.linalg.norm(n)
    for _ in range(2):
        keep = bp[pn[bp] @ n > 0.95]
        n = (pn[keep] * pa[keep, None]).sum(0); n /= np.linalg.norm(n)
    origin = (pc[keep] * pa[keep, None]).sum(0) / pa[keep].sum()
    keep = keep[np.abs((pc[keep] - origin) @ n) < 0.01]
    screen_poly = np.zeros(npoly, bool); screen_poly[keep] = True
    up = np.array([0, 0, 1.0]) - n * n[2]; up /= np.linalg.norm(up)
    rt = np.cross(up, n)
    rel = co - origin
    vx, vy, vz = rel @ rt, rel @ up, rel @ n
    sv = np.unique(tv[screen_poly[tp]])
    x_lo, x_hi, y_lo, y_hi = vx[sv].min(), vx[sv].max(), vy[sv].min(), vy[sv].max()
    to_units = lambda p: (x_lo + p[0] * (x_hi - x_lo), y_lo + p[1] * (y_hi - y_lo))

    # --- neume faces: raised over the glass inside NEUME_BOX
    cx, cy, cz = (pc - origin) @ rt, (pc - origin) @ up, (pc - origin) @ n
    nx = (cx - x_lo) / (x_hi - x_lo); ny = (cy - y_lo) / (y_hi - y_lo)
    neume = (~screen_poly) & (nx > NEUME_BOX[0]) & (nx < NEUME_BOX[2]) & (ny > NEUME_BOX[1]) & (ny < NEUME_BOX[3]) \
        & (cz > NEUME_Z[0]) & (cz < NEUME_Z[1])
    ni = np.where(neume)[0]
    # old colour at each neume face: mean over its triangles' UV centroids
    first_tri = {}
    for t, p in enumerate(tp):
        if neume[p] and p not in first_tri:
            first_tri[p] = t
    samp = np.array([pix[min(int(tri_px[first_tri[p]].mean(0)[1]), H - 1), min(int(tri_px[first_tri[p]].mean(0)[0]), W - 1), :3]
                     for p in ni])
    lab = np.full(len(ni), -1)
    lab[(samp[:, 1] > 0.55) & (samp[:, 0] < 0.5)] = 1                         # bright
    lab[(samp[:, 1] > 0.18) & (samp[:, 1] <= 0.55) & (samp[:, 1] > samp[:, 0] * 1.6)] = 0   # dim
    dark = (lab < 0) & (samp.max(1) < 0.2)                                    # black gaps (inside the hook): stay screen
    d2 = ((pc[ni][:, None] - pc[ni][None]) ** 2).sum(-1)
    order = np.argsort(d2, 1)[:, :15]
    vote = np.zeros(len(ni), int)
    for i in range(len(ni)):
        known = lab[order[i]][lab[order[i]] >= 0][:9]
        vote[i] = 1 if (known.size == 0 or known.mean() >= 0.5) else 0
    face_col = {p: (SCREEN if dk else GREEN if v else GREEN_DIM) for p, v, dk in zip(ni, vote, dark)}

    # --- crack clearance from the neume footprint (fails loudly instead of shipping a touching crack)
    segs = segments(to_units)
    foot = np.stack([cx[ni], cy[ni]], 1).astype(np.float32)
    clear = crack_field(foot, segs).min() - W_EDGE
    if clear < MIN_CLEAR_NEUME:
        raise SystemExit("crack too close to the neume: %.4f" % clear)
    tx0, ty0, tx1, ty1 = TAPE_BOX
    keep_out = [to_units((tx0, ty0)), to_units((tx1, ty1))]
    border = np.array([to_units((u, v)) for u in np.linspace(0, 1, 60) for v in (0, 1)]
                      + [to_units((u, v)) for v in np.linspace(0, 1, 60) for u in (0, 1)]
                      + [(x, keep_out[0][1]) for x in np.linspace(keep_out[0][0], keep_out[1][0], 30)]
                      + [(keep_out[1][0], y) for y in np.linspace(keep_out[0][1], keep_out[1][1], 30)], np.float32)
    clear_edge = crack_field(border, segs).min() - W_EDGE
    if clear_edge < MIN_CLEAR_EDGE:
        raise SystemExit("crack too close to the bezel or tape: %.4f" % clear_edge)

    # --- coverage of every triangle near the painted charts (so dilation only fills true gutters)
    tgt = screen_poly[tp] | neume[tp]
    lo = tri_px[tgt].reshape(-1, 2).min(0) - 8; hi = tri_px[tgt].reshape(-1, 2).max(0) + 8
    covered = np.zeros((H, W), bool)
    painted = np.zeros((H, W), bool)
    img = pix[..., :3]                                    # view: writes land in pix
    body_desaturate(img)
    near = np.where(((tri_px.max(1) >= lo) & (tri_px.min(1) <= hi)).all(1))[0]
    n_scr = n_neu = 0
    for t in near:
        r = raster(tri_px[t], H, W)
        if r is None:
            continue
        rows, cols, bc = r
        covered[rows, cols] = True
        p = tp[t]
        if screen_poly[p]:
            vs = tv[t]
            xy = np.stack([bc @ vx[vs], bc @ vy[vs]], 1).astype(np.float32)
            f = crack_field(xy, segs)
            aa = 0.5 / 2350.0                                   # about half a texel, model units
            fe = crack_field(xy - W_EDGE * np.array(LIGHT, np.float32), segs)   # core shifted toward the light
            core_a = np.clip(0.5 - f / (2 * aa), 0, 1)[:, None]
            edge_a = np.clip(0.5 - fe / (2 * aa), 0, 1)[:, None]
            col = SCREEN * (1 - edge_a) + EDGE * edge_a
            col = col * (1 - core_a) + PLUM * core_a
            img[rows, cols] = col
            painted[rows, cols] = True
            n_scr += len(rows)
        elif neume[p]:
            img[rows, cols] = face_col[p]
            painted[rows, cols] = True
            n_neu += len(rows)
    for sel in (screen_poly[tp], neume[tp]):              # dilate each painted region inside its own crop
        b = tri_px[sel].reshape(-1, 2)
        c0, r0 = np.maximum(np.floor(b.min(0)).astype(int) - 6, 0)
        c1, r1 = np.minimum(np.ceil(b.max(0)).astype(int) + 6, [W, H])
        sub_i, sub_p = img[r0:r1, c0:c1], painted[r0:r1, c0:c1]
        dilate(sub_i, sub_p, covered[r0:r1, c0:c1])
        img[r0:r1, c0:c1], painted[r0:r1, c0:c1] = sub_i, sub_p

    # write the atlas to a temporary PNG, load it as a fresh packed image, swap it into the material, export
    out = bpy.data.images.new("aa_broken_symbol_handheld_basecolor", W, H, alpha=True)
    out.pixels.foreach_set(pix.ravel())
    png = os.path.splitext(dst)[0] + "_basecolor_tmp.png"
    out.filepath_raw = png
    out.file_format = "PNG"
    out.save()
    new = bpy.data.images.load(png)
    new.pack()
    for link in obj.material_slots[0].material.node_tree.links:
        if link.to_socket.name == "Base Color" and link.from_node.type == "TEX_IMAGE":
            link.from_node.image = new
    bpy.ops.export_scene.gltf(filepath=dst, export_format="GLB", export_image_format="AUTO")
    os.remove(png)
    print("SCREEN frame x %.3f..%.3f y %.3f..%.3f, %d screen faces" % (x_lo, x_hi, y_lo, y_hi, screen_poly.sum()))
    print("NEUME faces %d (bright %d, dim %d, black %d); crack clearance: neume %.4f, bezel/tape %.4f units"
          % (len(ni), (vote & ~dark).sum(), ((vote == 0) & ~dark).sum(), dark.sum(), clear, clear_edge))
    print("TEXELS screen %d, neume %d" % (n_scr, n_neu))
    print("WROTE", dst)


main()
