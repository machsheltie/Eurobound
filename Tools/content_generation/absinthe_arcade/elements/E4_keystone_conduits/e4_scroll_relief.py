"""Trace the carved S / C scroll clusters under the keystone face off the bible into a relief field (plain Python:
numpy, scipy, Pillow). Re-runnable.

  <venv python> e4_scroll_relief.py [--preview out.png]

Inside three hand-traced cluster envelopes (bible px), every sandstone-coloured pixel is carving and every dark
pixel a carved-out gap. Height = rounded profile of the distance to the nearest gap (each curl gets a full rolled
section, the gaps stay deep), plus the bible's own fine shading as shallow grooves. e4_build.py casts the field
through aa_bible_cam into the aa_e4_keystone_scrolls mesh.
Output: scroll_relief.npz next to this script (u0, v0, step, mask, height_m).
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from e4_cam import BIBLE  # noqa: E402

U0, V0, U1, V1 = 2985, 1945, 3720, 2172          # nothing below the archivolt line (bible v ~2172)
# cluster envelopes (bible px): curls only, never the archivolt bands or the ear cups
ENVELOPES = [
    [(3060, 1995), (3205, 1988), (3228, 2060), (3224, 2168), (3150, 2172), (3085, 2160), (3040, 2125), (3000, 2102),
     (2992, 2052), (3020, 2030)],
    [(3440, 1975), (3520, 1945), (3640, 1950), (3702, 1955), (3714, 1992), (3692, 2050), (3642, 2078), (3600, 2102),
     (3562, 2150), (3470, 2170), (3430, 2100)],
    [(3226, 2088), (3290, 2102), (3360, 2102), (3428, 2085), (3420, 2168), (3228, 2168)],
]
EXCLUDE = [  # ear cup undersides, the right cup's fitting, the hose
    ("ellipse", (3075, 1890, 82, 98)), ("rect", (3525, 1930, 3595, 1968)),
]
ROUND_PX = 7.0            # curl section radius (px): full height reached this far inside a curl
H_M = 0.13                # relief height (m) above its base
GROOVE_M = 0.022          # bible shading -> shallow grooves / rolled lips


def hsv(rgb):
    mx, mn = rgb.max(-1), rgb.min(-1)
    d = mx - mn
    h = np.zeros_like(mx)
    m = d > 1e-6
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    i = m & (mx == r)
    h[i] = ((g - b)[i] / d[i]) % 6
    i = m & (mx == g)
    h[i] = (b - r)[i] / d[i] + 2
    i = m & (mx == b)
    h[i] = (r - g)[i] / d[i] + 4
    return h / 6, np.where(mx > 0, d / np.maximum(mx, 1e-6), 0), mx


def main():
    Image.MAX_IMAGE_PIXELS = None
    im = np.asarray(Image.open(BIBLE).convert("RGB").crop((U0, V0, U1, V1))).astype(np.float32) / 255
    H, W = im.shape[:2]
    env = Image.new("L", (W, H), 0)
    dr = ImageDraw.Draw(env)
    for poly in ENVELOPES:
        dr.polygon([(u - U0, v - V0) for u, v in poly], fill=255)
    for kind, p in EXCLUDE:
        if kind == "ellipse":
            cu, cv, ru, rv = p
            dr.ellipse([cu - ru - U0, cv - rv - V0, cu + ru - U0, cv + rv - V0], fill=0)
        else:
            dr.rectangle([p[0] - U0, p[1] - V0, p[2] - U0, p[3] - V0], fill=0)
    env = np.asarray(env) > 0
    h, s, v = hsv(im)
    stone = (h > 0.03) & (h < 0.14) & (s > 0.15) & (s < 0.7) & (v > 0.36)
    lum = im @ np.array([0.3, 0.59, 0.11], np.float32)
    stone |= (lum > 0.55) & (s < 0.7)                      # sunlit tops read pale
    mask = env & stone
    mask = ndi.binary_opening(ndi.binary_closing(mask, iterations=2), iterations=2)     # clean carved edges
    mask = (ndi.gaussian_filter(mask.astype(np.float32), 2.2) > 0.5) & env     # smooth, crisp carved outlines
    lab, n = ndi.label(mask)
    if n:
        sz = ndi.sum(mask, lab, range(1, n + 1))
        mask = np.isin(lab, [i + 1 for i, z in enumerate(sz) if z > 150])
    holes = ndi.binary_fill_holes(mask) & ~mask             # pin-holes from grain; real carved gaps are bigger
    lab, n = ndi.label(holes)
    if n:
        sz = ndi.sum(holes, lab, range(1, n + 1))
        mask |= np.isin(lab, [i + 1 for i, z in enumerate(sz) if z < 45])
    bed = ndi.binary_fill_holes(ndi.binary_closing(mask, iterations=6)) & env   # shadowed ground behind the curls
    bed = ndi.binary_erosion(bed, iterations=5)              # edges stay hidden behind the modelled curls
    dist = ndi.distance_transform_edt(mask)
    x = np.clip(dist / ROUND_PX, 0, 1)
    prof = np.sqrt(1 - (1 - x) ** 2)
    # the bible's shading separates the curls: shadowed (darker) carving lies deeper, lit rolls stand proud
    lum_s = ndi.median_filter(lum, 5)                       # drop the sandstone grain, keep the carved forms
    lit = ndi.gaussian_filter(np.clip((lum_s - 0.28) / 0.42, 0, 1), 3.0)
    hp = ndi.gaussian_filter(lum_s, 1.5) - ndi.gaussian_filter(lum_s, 7)
    height = H_M * (0.35 * prof + 0.65 * lit * np.sqrt(prof)) + GROOVE_M * np.clip(hp / 0.12, -1, 1) * x
    height = ndi.gaussian_filter(np.where(mask, height, 0), 1.6) * mask
    env_arr = np.array([[p for p in poly] + [(-1, -1)] * (12 - len(poly)) for poly in ENVELOPES], np.int32)
    np.savez_compressed(HERE / "scroll_relief.npz", u0=U0, v0=V0, step=1, mask=mask, height_m=height.astype(np.float32),
                        envelopes=env_arr, bed=bed)
    print("E4 SCROLL RELIEF", (W, H), "carved px", int(mask.sum()), "max h", round(float(height.max()), 3))
    if "--preview" in sys.argv:
        out = sys.argv[sys.argv.index("--preview") + 1]
        pv = (np.clip(height / H_M, 0, 1) * 255).astype(np.uint8)
        Image.fromarray(np.concatenate([(im * 255).astype(np.uint8), np.stack([pv] * 3, -1)], 1)).save(out)


if __name__ == "__main__":
    main()
