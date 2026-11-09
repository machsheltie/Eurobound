"""Normalize a generated HD-2D facade/prop image into an engine-ready texture.

Steps (deterministic, no generation):
  1. White background -> alpha, by flood fill from the image border (interior whites survive).
  2. Crop at the ground line (drops any sidewalk/plinth the generator added).
  3. Crop to the silhouette bbox, scale to the target width, bottom-anchor on a fixed canvas.
  4. Optional: write an emission mask (bright, saturated pixels = neon/lit windows) for night.

Usage:
  python normalize_face.py IN.png OUT.png --ground-y 1510 --size 1024x1536 [--emit OUT_emit.png]
"""
from __future__ import annotations

import argparse
from collections import deque

import numpy as np
from PIL import Image, ImageFilter


def flood_alpha(rgb: np.ndarray, tol: int) -> np.ndarray:
    """Return alpha (uint8) where border-connected near-white pixels are transparent."""
    h, w, _ = rgb.shape
    white = rgb.min(axis=2) >= 255 - tol
    bg = np.zeros((h, w), bool)
    q: deque[tuple[int, int]] = deque()
    for x in range(w):
        for y in (0, h - 1):
            if white[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if white[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if 0 <= ny < h and 0 <= nx < w and white[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True
                q.append((ny, nx))
    alpha = np.where(bg, 0, 255).astype(np.uint8)
    # Soften the 1px fringe so the cutout does not show a white halo.
    a = Image.fromarray(alpha).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.7))
    return np.asarray(a)


def emission_mask(rgba: np.ndarray, v_min: float, s_min: float) -> np.ndarray:
    """Colour emission map: keep pixels that are both bright and saturated (neon, lamplight)."""
    rgb = rgba[..., :3].astype(float) / 255.0
    mx, mn = rgb.max(axis=2), rgb.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    w = np.clip((mx - v_min) / (1 - v_min), 0, 1) * np.clip((sat - s_min) / (1 - s_min), 0, 1)
    w = np.asarray(Image.fromarray((w * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0)), float) / 255
    out = (rgb * w[..., None] * 255).astype(np.uint8)
    a = rgba[..., 3:4]
    return np.concatenate([out, a], axis=2)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("out")
    p.add_argument("--ground-y", type=int, required=True, help="first row below the building base")
    p.add_argument("--size", default="1024x1792")
    p.add_argument("--tol", type=int, default=18)
    p.add_argument("--emit")
    p.add_argument("--emit-v", type=float, default=0.55)
    p.add_argument("--emit-s", type=float, default=0.35)
    p.add_argument("--alpha-from", help="registered master image: reuse its silhouette and crop, "
                   "so day/night variants match pixel-for-pixel")
    a = p.parse_args()

    W, H = (int(v) for v in a.size.split("x"))
    rgb = np.asarray(Image.open(a.src).convert("RGB"))[: a.ground_y]
    if a.alpha_from:
        ref = np.asarray(Image.open(a.alpha_from).convert("RGB"))[: a.ground_y]
        assert ref.shape == rgb.shape, f"--alpha-from size {ref.shape} != src {rgb.shape}; register first"
        alpha = flood_alpha(ref, a.tol)
    else:
        alpha = flood_alpha(rgb, a.tol)
    rgba = np.dstack([rgb, alpha])

    ys, xs = np.where(alpha > 8)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    img = Image.fromarray(rgba, "RGBA").crop((x0, y0, x1, y1))
    scale = W / img.width
    nh = round(img.height * scale)
    img = img.resize((W, nh), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, max(H, nh)), (0, 0, 0, 0))
    canvas.paste(img, (0, canvas.height - nh))
    if canvas.height != H:
        canvas = canvas.crop((0, canvas.height - H, W, canvas.height))
    canvas.save(a.out, optimize=True)
    print(f"{a.out}: bbox=({x0},{y0},{x1},{y1}) scale={scale:.3f} content_h={nh}")

    if a.emit:
        Image.fromarray(emission_mask(np.asarray(canvas), a.emit_v, a.emit_s), "RGBA").save(a.emit, optimize=True)
        print(f"{a.emit}: emission mask")


if __name__ == "__main__":
    main()
