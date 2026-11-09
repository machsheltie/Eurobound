"""E5 URP texture sets (plain Python: numpy, scipy, Pillow). Run after e5_mural.py. Re-runnable.

  stone tile (2048, tiles every 1.6 m; from the author's references/Exterior/texture.jpg):
      e5_stone_basecolor.png, e5_stone_normal.png (OpenGL), e5_stone_mask.png (R metal, G AO, B 0, A smoothness)
  mural sheet (facade space, same size as e5_mural_basecolor.png):
      e5_mural_basecolor.png (RGBA, from e5_mural.py), e5_mural_emissive.png (from e5_mural.py),
      e5_mural_normal.png (brush/flake relief), e5_mural_mask.png
  e5_peel_zones.png (from e5_mural.py): where the plaster peels (author-repaintable mask).
"""
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
OUT = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/textures/e5_surface"
STONE_TINT = (0.95, 0.92, 0.85)
SRC = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/texture.jpg"


def normal_from_height(h, strength, wrap):
    mode = "wrap" if wrap else "nearest"
    dx = ndi.sobel(h, axis=1, mode=mode) / 8.0
    dy = ndi.sobel(h, axis=0, mode=mode) / 8.0
    n = np.stack([-dx * strength, dy * strength, np.ones_like(h)], -1)
    n /= np.linalg.norm(n, axis=-1, keepdims=True)
    return ((n * 0.5 + 0.5) * 255).astype(np.uint8)


def main():
    Image.MAX_IMAGE_PIXELS = None
    s = Image.open(SRC).convert("RGB").resize((2048, 2048), Image.LANCZOS)
    # warm the author's texture toward the bible's cream-ochre wall (texture median 233,208,178 -> ~221,191,151)
    tint = np.array(STONE_TINT, np.float32)
    s = Image.fromarray(np.clip(np.asarray(s).astype(np.float32) * tint, 0, 255).astype(np.uint8))
    s.save(OUT / "e5_stone_basecolor.png")
    a = np.asarray(s).astype(np.float32) / 255
    lum = a.mean(-1)
    h = lum - ndi.gaussian_filter(lum, 24, mode="wrap")          # high-pass: flakes, pits, edges
    Image.fromarray(normal_from_height(h, 6.0, True)).save(OUT / "e5_stone_normal.png")
    ao = np.clip(0.75 + 1.6 * (ndi.gaussian_filter(lum, 3, mode="wrap") - ndi.gaussian_filter(lum, 30, mode="wrap")), 0, 1)
    smooth = np.clip(0.1 + 0.15 * (lum - lum.mean()), 0, 1)
    mask = np.stack([np.zeros_like(lum), ao, np.zeros_like(lum), smooth], -1)
    Image.fromarray((mask * 255).astype(np.uint8), "RGBA").save(OUT / "e5_stone_mask.png")
    m = np.asarray(Image.open(OUT / "e5_mural_basecolor.png")).astype(np.float32) / 255
    ml = m[..., :3].mean(-1)
    mh = (ml - ndi.gaussian_filter(ml, 6)) * 0.5 + m[..., 3] * 0.3
    Image.fromarray(normal_from_height(mh, 3.0, False)).save(OUT / "e5_mural_normal.png")
    mm = np.stack([np.zeros_like(ml), np.ones_like(ml), np.zeros_like(ml), np.full_like(ml, 0.28)], -1)
    Image.fromarray((mm * 255).astype(np.uint8), "RGBA").save(OUT / "e5_mural_mask.png")
    for p in sorted(OUT.iterdir()):
        im = Image.open(p)
        print("E5 TEX", p.name, im.size, im.mode)


if __name__ == "__main__":
    main()
