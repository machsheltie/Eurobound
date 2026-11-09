"""Strip the dithered ground shadow PixelLab bakes under a character's feet (the game draws real
shadows). Only touches light, low-saturation grey pixels in the bottom rows that border empty space
and do not touch the dark outline, so white socks and shoes survive. Leftovers go to the Aseprite
hand-fix pass.

    python tools/sprite_pipeline/remove_baked_shadow.py <src_dir> <dst_dir>

Copies the folder tree, cleaning every PNG.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image

BOTTOM_ROWS = 7


def _neighbours(m: np.ndarray, diagonal: bool) -> list[np.ndarray]:
    p = np.pad(m, 1)
    n = [p[:-2, 1:-1], p[2:, 1:-1], p[1:-1, :-2], p[1:-1, 2:]]
    if diagonal:
        n += [p[:-2, :-2], p[:-2, 2:], p[2:, :-2], p[2:, 2:]]
    return n


def clean(img: Image.Image) -> tuple[Image.Image, int]:
    a = np.asarray(img.convert("RGBA")).copy()
    bbox = img.getbbox()
    if not bbox:
        return img, 0
    removed = 0
    for _ in range(6):
        alpha = a[..., 3] > 0
        rgb = a[..., :3].astype(int)
        hi, lo = rgb.max(-1), rgb.min(-1)
        grey = (hi - lo <= 24) & (hi >= 110) & alpha
        dark = (hi < 95) & alpha
        empty_neighbours = sum((~n).astype(int) for n in _neighbours(alpha, False))
        touches_dark = np.logical_or.reduce(_neighbours(dark, True))
        rows = np.zeros_like(alpha)
        rows[bbox[3] - BOTTOM_ROWS:, :] = True
        kill = grey & rows & (empty_neighbours >= 1) & ~touches_dark
        if not kill.any():
            break
        removed += int(kill.sum())
        a[kill, 3] = 0
    # Stray specks: opaque pixels with at most one opaque 4-neighbour (edge noise from the model).
    for _ in range(2):
        alpha = a[..., 3] > 0
        opaque_neighbours = sum(n.astype(int) for n in _neighbours(alpha, False))
        specks = alpha & (opaque_neighbours <= 1)
        removed += int(specks.sum())
        a[specks, 3] = 0
    return Image.fromarray(a, "RGBA"), removed


def main() -> None:
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    for png in dst.rglob("*.png"):
        out, n = clean(Image.open(png))
        out.save(png)
        print(f"{png.relative_to(dst)}: removed {n} px")


if __name__ == "__main__":
    main()
