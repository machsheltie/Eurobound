"""Colour-segmentation helpers for tracing E3 parts off the bible crop (plain Python: numpy, scipy, Pillow).

Coordinates are pixels of dev/aa_team/crops/04_entrance_marquee_doors.png (2296 x 2329).
"""
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
CROP = REPO / "dev/aa_team/crops/04_entrance_marquee_doors.png"


def load_rgb():
    return np.asarray(Image.open(CROP).convert("RGB")).astype(np.float32) / 255.0


def hsv(rgb):
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx = rgb.max(-1)
    mn = rgb.min(-1)
    d = mx - mn
    h = np.zeros_like(mx)
    m = d > 1e-6
    rm = m & (mx == r)
    gm = m & (mx == g) & ~rm
    bm = m & ~rm & ~gm
    h[rm] = ((g - b)[rm] / d[rm]) % 6
    h[gm] = (b - r)[gm] / d[gm] + 2
    h[bm] = (r - g)[bm] / d[bm] + 4
    h = h / 6.0
    s = np.where(mx > 1e-6, d / np.maximum(mx, 1e-6), 0)
    return h, s, mx


def green_mask(h, s, v, vmin=0.45, smin=0.28):
    return (h > 0.13) & (h < 0.30) & (s > smin) & (v > vmin)


def purple_mask(h, s, v, vmin=0.40, smin=0.25):
    return (h > 0.70) & (h < 0.92) & (s > smin) & (v > vmin)


def clean(mask, open_r=1, close_r=2):
    if close_r:
        mask = ndi.binary_closing(mask, iterations=close_r)
    if open_r:
        mask = ndi.binary_opening(mask, iterations=open_r)
    return ndi.binary_fill_holes(mask) if False else mask


def components(mask, min_area=20):
    lab, n = ndi.label(mask)
    out = []
    for i, sl in enumerate(ndi.find_objects(lab), start=1):
        if sl is None:
            continue
        sub = lab[sl] == i
        area = int(sub.sum())
        if area < min_area:
            continue
        y0, y1 = sl[0].start, sl[0].stop
        x0, x1 = sl[1].start, sl[1].stop
        out.append({"x0": x0, "y0": y0, "x1": x1, "y1": y1, "area": area,
                    "fill": area / float((x1 - x0) * (y1 - y0))})
    return out


def quantize(mask, x0, y0, x1, y1, cell, thresh=0.5):
    """Mask -> set of (col, row) cells of size `cell` px whose coverage >= thresh."""
    cells = []
    sub = mask[y0:y1, x0:x1]
    rows = int(np.ceil((y1 - y0) / cell))
    cols = int(np.ceil((x1 - x0) / cell))
    for r in range(rows):
        for c in range(cols):
            blk = sub[int(r * cell):int((r + 1) * cell), int(c * cell):int((c + 1) * cell)]
            if blk.size and blk.mean() >= thresh:
                cells.append((c, r))
    return cells, cols, rows


def save_mask(mask, path):
    Image.fromarray((mask * 255).astype(np.uint8)).save(path)


# ---- camera reconstruction for the bible crop -------------------------------------------
# Horizontal facade lines in the crop converge to a vanishing point far left
# (fitted on the slogan-bar trims: VP x ~ -16100, horizon y ~ 1970), verticals stay vertical:
# the bible camera is yawed (right side of the facade nearer), not pitched.
CAM_CX = 1100.0      # principal point x (arch centre; the crop is centred on the building)
CAM_CY = 1970.0      # horizon row
CAM_F = 5600.0       # focal length in crop px (about a 50 deg horizontal FOV on the 5248 px bible)
VP_X = -16100.0


def cam_yaw():
    return float(np.arctan(CAM_F / (CAM_CX - VP_X)))


def rectify(rgb, theta=None, out_shape=None, order=1, sign=1.0, ox=0.0):
    """Remove the camera yaw: the crop as seen square-on from the same camera position.

    The arch centre (CAM_CX) stays put and keeps its scale (rectified focal = F cos(theta)).
    """
    theta = cam_yaw() if theta is None else theta
    H, W = rgb.shape[:2] if out_shape is None else out_shape
    vv, uu = np.mgrid[0:H, 0:W].astype(np.float64)
    uu = uu - ox
    fr = CAM_F * np.cos(theta)
    dx = (uu - CAM_CX) / fr - sign * np.tan(theta)
    dy = (vv - CAM_CY) / fr
    dz = np.ones_like(dx)
    c, s = np.cos(sign * theta), np.sin(sign * theta)
    rx = c * dx + s * dz
    rz = -s * dx + c * dz
    u = CAM_CX + CAM_F * rx / rz
    v = CAM_CY + CAM_F * dy / rz
    out = np.zeros((H, W, rgb.shape[2]), rgb.dtype)
    for ch in range(rgb.shape[2]):
        out[..., ch] = ndi.map_coordinates(rgb[..., ch], [v, u], order=order, mode="constant", cval=0)
    return out


RECT_OX = 260          # rectified canvas: x_rect = x_canvas - RECT_OX
RECT_W = 2560
RECT_H = 2329


def rectified():
    """Cached square-on copy of the crop (canvas coords: x_canvas = x_rect + RECT_OX)."""
    p = HERE / "trace" / "crop04_rectified.png"
    if p.exists():
        return np.asarray(Image.open(p).convert("RGB")).astype(np.float32) / 255.0
    p.parent.mkdir(exist_ok=True)
    r = rectify(load_rgb(), out_shape=(RECT_H, RECT_W), ox=RECT_OX)
    Image.fromarray((np.clip(r, 0, 1) * 255).astype(np.uint8)).save(p)
    return r
