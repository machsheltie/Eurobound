"""Fit each bible-camera render to its reference crop (runs in Blender's Python: numpy + bpy images).

  blender -b --factory-startup --python register_e2.py -- --renders DIR [--write]
  blender -b --factory-startup --python register_e2.py -- --renders DIR --check

Model: ref_px = s * render_px + t, render resized to the crop's pixel size. Matching is done on
blurred gradient-magnitude maps, weighted to the window (centre 70% of the crop), by FFT
cross-correlation over a scale sweep. The residual is reported in crop pixels and as % of the
crop's long side (the 1% rule).
"""
import argparse
import json
from pathlib import Path

import sys

import bpy
import numpy as np


class Img:
    """Tiny image wrapper over bpy images (Blender's Python ships numpy, not Pillow)."""

    def __init__(self, arr):
        self.a = arr  # H x W x 3 float, row 0 = top

    @staticmethod
    def open(path):
        im = bpy.data.images.load(str(path), check_existing=False)
        w, h = im.size
        px = np.empty(w * h * 4, dtype=np.float32)
        im.pixels.foreach_get(px)
        bpy.data.images.remove(im)
        return Img(px.reshape(h, w, 4)[::-1, :, :3].copy())

    @property
    def size(self):
        return self.a.shape[1], self.a.shape[0]

    def resize(self, wh):
        w, h = wh
        H, W = self.a.shape[:2]
        ys = (np.arange(h) + 0.5) * H / h - 0.5
        xs = (np.arange(w) + 0.5) * W / w - 0.5
        y0 = np.clip(np.floor(ys).astype(int), 0, H - 1)
        x0 = np.clip(np.floor(xs).astype(int), 0, W - 1)
        y1 = np.clip(y0 + 1, 0, H - 1)
        x1 = np.clip(x0 + 1, 0, W - 1)
        fy = np.clip(ys - y0, 0, 1)[:, None, None]
        fx = np.clip(xs - x0, 0, 1)[None, :, None]
        a = self.a
        top = a[y0][:, x0] * (1 - fx) + a[y0][:, x1] * fx
        bot = a[y1][:, x0] * (1 - fx) + a[y1][:, x1] * fx
        return Img(top * (1 - fy) + bot * fy)


def _blur(a, sig):
    r = int(3 * sig)
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / sig) ** 2)
    k /= k.sum()
    a = np.apply_along_axis(lambda m: np.convolve(m, k, mode="same"), 0, a)
    return np.apply_along_axis(lambda m: np.convolve(m, k, mode="same"), 1, a)

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
REF = REPO / "dev/aa_team/renders/E2/ref"
VIEWS = {"l2": "bible_w2.png", "l1": "bible_w1.png", "l3": "bible_w3.png", "r1": "bible_r1.png"}


def edges(im, blur=3.0):
    """Dark-silhouette map: the timber frame, glazing, ironwork and openings are the darkest shapes in
    both images; luminance below a soft threshold, blurred."""
    lum = im.a @ np.array([0.3, 0.59, 0.11], dtype=np.float32)
    m = np.clip((0.30 - lum) / 0.12, 0, 1)
    return _blur(m, blur)


def window(h, w, frac=0.7):
    yy = np.linspace(-1, 1, h)[:, None]
    xx = np.linspace(-1, 1, w)[None, :]
    return np.clip(1.2 - np.maximum(np.abs(xx), np.abs(yy)) / frac, 0, 1).astype(np.float32)


def xcorr(a, b):
    """Shift t maximising sum a(u) * b(u - t)."""
    H, W = a.shape
    fa = np.fft.rfft2(a, s=(2 * H, 2 * W))
    fb = np.fft.rfft2(b, s=(2 * H, 2 * W))
    c = np.fft.irfft2(fa * np.conj(fb), s=(2 * H, 2 * W))
    idx = np.unravel_index(np.argmax(c), c.shape)
    ty = idx[0] if idx[0] < H else idx[0] - 2 * H
    tx = idx[1] if idx[1] < W else idx[1] - 2 * W
    return tx, ty, c[idx]


def fit(ref_im, ren_im, scales):
    w, h = ref_im.size
    ren1 = ren_im.resize((w, h))
    er = edges(ref_im)
    wt = window(h, w)
    er = (er - er.mean()) * wt
    best = None
    for s in scales:
        sw, sh = max(8, int(round(w * s))), max(8, int(round(h * s)))
        sc = ren1.resize((sw, sh)).a
        canvas = np.full((h, w, 3), 0.5, dtype=np.float32)
        canvas[:min(sh, h), :min(sw, w)] = sc[:min(sh, h), :min(sw, w)]
        e = edges(Img(canvas))
        e = e - e.mean()
        tx, ty, v = xcorr(er, e)
        nv = v / (np.linalg.norm(er) * np.linalg.norm(e) + 1e-9)
        if best is None or nv > best[3]:
            best = (s, tx, ty, nv)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--renders", required=True)
    ap.add_argument("--tag", default="final")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    d = Path(a.renders)
    reg = {}
    for v, rf in VIEWS.items():
        p = d / f"{a.tag}_bible_{v}.png"
        if not p.exists():
            continue
        ref = Img.open(REF / rf)
        ren = Img.open(p)
        # work at half resolution for speed; shifts are scaled back
        half = (ref.size[0] // 2, ref.size[1] // 2)
        ref = ref.resize(half)
        if a.check:
            s, tx, ty, nv = fit(ref, ren, [1.0])
            # local refinement around the window only (tighter weight)
            long = max(ref.size)
            tx, ty, long = tx * 2, ty * 2, long * 2
            print(f"{v}: residual shift ({tx}, {ty}) px = {100 * max(abs(tx), abs(ty)) / long:.2f}% of {long}px, ncc {nv:.3f}")
            reg[v] = dict(tx=int(tx), ty=int(ty), pct=round(100 * max(abs(tx), abs(ty)) / long, 2), ncc=round(float(nv), 3))
            continue
        coarse = fit(ref, ren, [x / 100 for x in range(80, 141, 2)])
        s0 = coarse[0]
        s, tx, ty, nv = fit(ref, ren, [s0 + x / 1000 for x in range(-20, 21, 4)])
        print(f"{v}: s={s:.3f} t=({tx},{ty}) ncc={nv:.3f}")
        reg[v] = dict(s=round(float(s), 4), tx=float(tx) * 2, ty=float(ty) * 2, ncc=round(float(nv), 3))
    if a.write:
        (HERE / "registration.json").write_text(json.dumps(reg, indent=1), encoding="utf-8")
    print("@@JSON@@" + json.dumps(reg))


if __name__ == "__main__":
    main()
