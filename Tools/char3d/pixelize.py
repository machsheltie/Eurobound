"""Render -> 128x128 pixel sprite in Jakub's palette.
usage: python pixelize.py <render.png> <out_stem> [target_width]
Palette: env PIXELIZE_PAL = path to the 44-colour palette .npy (superseded pixel pipeline; kept for history).
"""
import sys
import numpy as np
import cv2
from PIL import Image

import os
PAL = os.environ.get("PIXELIZE_PAL") or sys.exit("set PIXELIZE_PAL to the palette .npy")
src, stem = sys.argv[1], sys.argv[2]
TW = int(sys.argv[3]) if len(sys.argv) > 3 else 110
pal = np.load(PAL).astype(np.float32)
# drop the pure-yellow/green UI-ish entries? keep all; the bg green (50,78,41) is excluded
keep = [i for i in range(len(pal)) if tuple(pal[i].astype(int)) != (50, 78, 41)]
pal = pal[keep]

im = Image.open(src).convert("RGBA")
bb = im.getbbox()
im = im.crop(bb)
TH = round(im.height * TW / im.width)
K = 8
MODE = sys.argv[4] if len(sys.argv) > 4 else "majority"
# screen-space flattening: kill texture grime so areas read as flat colour at 1x
arr = np.array(im)
rgbf = cv2.cvtColor(arr[..., :3], cv2.COLOR_RGB2BGR)
for _ in range(int(sys.argv[5]) if len(sys.argv) > 5 else 3):
    rgbf = cv2.bilateralFilter(rgbf, 9, 28, 6)
arr[..., :3] = cv2.cvtColor(rgbf, cv2.COLOR_BGR2RGB)
im = Image.fromarray(arr, "RGBA")
big = im.resize((TW * K, TH * K), Image.LANCZOS)
a = np.array(big).astype(np.float32)
alpha = a[..., 3]
rgb = np.clip(a[..., :3], 0, 255).astype(np.uint8)
L = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB).reshape(-1, 3).astype(np.float32)
PL = cv2.cvtColor(pal.astype(np.uint8).reshape(1, -1, 3), cv2.COLOR_RGB2LAB).reshape(-1, 3).astype(np.float32)
# chroma-weighted distance keeps the candy stripes red/white instead of averaging to pink-brown
def nearest(Lab):
    d = (Lab[:, None, 0] - PL[None, :, 0]) ** 2 + 1.6 * ((Lab[:, None, 1:] - PL[None, :, 1:]) ** 2).sum(2)
    return np.argmin(d, 1)
qi = np.concatenate([nearest(L[i:i + 200000]) for i in range(0, len(L), 200000)]).reshape(TH * K, TW * K)
blocks = qi.reshape(TH, K, TW, K).transpose(0, 2, 1, 3).reshape(TH, TW, K * K)
ablk = alpha.reshape(TH, K, TW, K).transpose(0, 2, 1, 3).reshape(TH, TW, K * K)
mask = (ablk > 128).mean(2) > 0.42
idx = np.zeros((TH, TW), int)
npal = len(pal)
for y in range(TH):
    for x in range(TW):
        sel = blocks[y, x][ablk[y, x] > 128]
        if len(sel):
            idx[y, x] = np.bincount(sel, minlength=npal).argmax()
img = pal[idx].astype(np.uint8)
rgba = np.dstack([img, mask.astype(np.uint8) * 255])
canvas = np.zeros((TH + 2, TW + 2, 4), np.uint8)
canvas[1:-1, 1:-1] = rgba
al3 = canvas[..., 3] > 0
ring = np.zeros_like(al3)
for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    ring |= np.roll(np.roll(al3, dy, 0), dx, 1)
ring &= ~al3
canvas[ring] = (36, 24, 22, 255)
o = Image.fromarray(canvas, "RGBA")
full = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
ox = (128 - o.width) // 2
oy = max(0, 93 - o.height)
full.alpha_composite(o, (ox, oy))
full.save(f"{stem}.png")
print("size", TW, TH, "bbox", full.getbbox(), "offset", ox, oy)
bg = Image.new("RGBA", (128, 128), (40, 70, 40, 255))
bg.alpha_composite(full)
bg.resize((1024, 1024), Image.NEAREST).save(f"{stem}_8x.png")
