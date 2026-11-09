"""Bake a neon glow pass into a registered night texture without moving any pixels.

Selects saturated neon green and neon purple light sources (plus optional extra discs such as
the Green Fairy's token), brightens their cores, and screen-blends a multi-radius bloom over the
image. Because it only adds light, the result stays pixel-registered to the day texture.

Usage: python night_glow.py IN.png OUT.png [--disc x,y,r,R,G,B ...] [--strength 1.0] [--mask OUT_mask.png]
"""
import argparse

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def hsv(rgb: np.ndarray):
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx, mn = rgb.max(-1), rgb.min(-1)
    d = mx - mn + 1e-6
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    s = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    return h, s, mx


def blur(a: np.ndarray, r: float) -> np.ndarray:
    chans = [np.asarray(Image.fromarray(np.clip(a[..., c] * 255, 0, 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(r)), float) / 255 for c in range(a.shape[-1])]
    return np.stack(chans, -1)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("out")
    p.add_argument("--disc", action="append", default=[], help="x,y,radius,R,G,B extra light source")
    p.add_argument("--strength", type=float, default=1.0)
    p.add_argument("--mask")
    p.add_argument("--darken", type=float, default=1.0, help="multiply non-emissive pixels (night contrast)")
    a = p.parse_args()

    im = Image.open(a.src).convert("RGB")
    rgb = np.asarray(im, float) / 255
    h, s, v = hsv(rgb)
    green = (h > 70) & (h < 165) & (s > 0.45) & (v > 0.45)
    purple = (h > 255) & (h < 315) & (s > 0.40) & (v > 0.40)
    src = np.zeros_like(rgb)
    src[green] = [0.45, 1.0, 0.25]
    src[purple] = [0.78, 0.25, 1.0]
    wsrc = np.clip((v - 0.35) / 0.65, 0, 1)[..., None] * (green | purple)[..., None]
    src = src * wsrc
    for d in a.disc:
        x, y, r, R, G, B = (float(t) for t in d.split(","))
        m = Image.new("L", im.size, 0)
        ImageDraw.Draw(m).ellipse((x - r, y - r, x + r, y + r), fill=255)
        mm = np.asarray(m.filter(ImageFilter.GaussianBlur(r * 0.15)), float)[..., None] / 255
        ring = np.clip(mm[..., 0] * 1.0, 0, 1)[..., None]
        src = np.maximum(src, ring * np.array([R, G, B]) / 255 * 0.55)
        # brighten the disc itself so it reads as emissive, keeping its painted detail
        rgb = np.clip(rgb * (1 + mm * 0.35) + mm * np.array([R, G, B]) / 255 * 0.10, 0, 1)
        src = np.maximum(src, mm * np.array([R, G, B]) / 255 * 0.0)

    lit = np.clip(blur(((green | purple)[..., None] * np.ones(3)).astype(float), 3)[..., :1] * 2, 0, 1)
    rgb = rgb * (a.darken + (1 - a.darken) * lit)

    # Brighten neon cores (keep detail: lift toward the neon colour, do not flatten).
    core = (green | purple)[..., None] * wsrc
    rgb = np.clip(rgb + core * src * 0.35, 0, 1)

    bloom = blur(src, 4) * 0.55 + blur(src, 14) * 0.45 + blur(src, 40) * 0.35
    bloom *= a.strength
    out = 1 - (1 - rgb) * (1 - np.clip(bloom, 0, 1))  # screen blend
    Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)).save(a.out)
    if a.mask:
        Image.fromarray((np.clip(src, 0, 1) * 255).astype(np.uint8)).save(a.mask)
    print(f"{a.out}: green px={int(green.sum())} purple px={int(purple.sum())}")


if __name__ == "__main__":
    main()
