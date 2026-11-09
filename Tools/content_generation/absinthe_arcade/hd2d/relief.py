"""Turn a generated (registered) clay/height render into an engine height map + normal map.

The generator's "height map" is really a soft clay render: mostly height, plus some baked
top-down shading and a faint emboss of painted detail. We keep only local relief:
  rel = render - large-scale median (the wall level)
then soft-threshold small values (painted detail stays flat), and map to metres with separate gains
for projections and recesses.

Encoding of the output height PNG: 8-bit grey, 128 = wall plane, 1 unit = HEIGHT_RANGE_M / 127 m,
so 255 = +HEIGHT_RANGE_M (proud of the wall) and 0 = -HEIGHT_RANGE_M (recessed).
"""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

HEIGHT_RANGE_M = 1.0


def relief_metres(render: np.ndarray, alpha: np.ndarray, *, out_gain_m: float = 0.75,
                  in_gain_m: float = 1.6, deadband: float = 0.05, base_px: int = 260,
                  closing_px: int = 15, opening_threshold: float = 0.12) -> tuple[np.ndarray, np.ndarray]:
    """render: float 0..1 greyscale in the face's pixel frame.
    Returns (slab, detail) heights in metres: slab drives vertex displacement, detail the normals."""
    h, w = render.shape
    inside = alpha > 8
    # Wall level varies mostly vertically (the generator's top-down shading). Take, per band of
    # rows, the median over building pixels across the FULL width: large features (doorway,
    # marquee) cover well under half a row, so they cannot drag the wall level with them.
    band = max(8, base_px // 6)
    level = np.full(h, np.nan)
    for y in range(h):
        rows = slice(max(0, y - band), min(h, y + band + 1))
        vals = render[rows][inside[rows]]
        if vals.size > 50:
            level[y] = np.median(vals)
    good = ~np.isnan(level)
    level = np.interp(np.arange(h), np.where(good)[0], level[good])
    level = ndimage.gaussian_filter1d(level, band / 2)
    rel = render - level[:, None]
    # Soft deadband: faint emboss of painted detail (mural, vines) stays flat.
    # Recesses only for true openings (windows, doors): shallow dark values are leaf shading or
    # crevices in the generator's render and must not dent the wall.
    rel = np.where(rel < 0, np.minimum(rel + opening_threshold, 0) * (1.0 / (1.0 - opening_threshold)), rel)
    rel = np.sign(rel) * np.maximum(np.abs(rel) - deadband, 0)
    metres = np.where(rel > 0, rel * out_gain_m / 0.5, rel * in_gain_m / 0.5)
    metres = np.clip(metres, -HEIGHT_RANGE_M, HEIGHT_RANGE_M)
    # Projections become solid slabs: a greyscale closing fills the gaps between raised letters
    # and carved detail, so painted lettering sits on one flat front plane instead of stretching
    # down the sides of every glyph. Recesses (windows, doorway) are left untouched.
    detail = ndimage.gaussian_filter(metres.astype(np.float32), 1.2)
    pos = ndimage.grey_closing(np.maximum(metres, 0), size=(closing_px, closing_px))
    slab = np.where(pos > 0, pos, metres)
    slab = ndimage.gaussian_filter(slab.astype(np.float32), 1.5)
    # (vertex height: solid slabs; detail: the carving, used only for the normal map)
    return np.where(inside, slab, 0).astype(np.float32), np.where(inside, detail, 0).astype(np.float32)


def encode_height(metres: np.ndarray) -> Image.Image:
    return Image.fromarray(np.clip(128 + metres / HEIGHT_RANGE_M * 127, 0, 255).astype(np.uint8), "L")


def normal_map(metres: np.ndarray, px_per_m: float, strength: float = 1.0) -> Image.Image:
    """Tangent-space normal map (OpenGL convention, +Y up, as Godot expects)."""
    gy, gx = np.gradient(metres * px_per_m * strength)
    nx, ny, nz = -gx, gy, np.ones_like(gx)
    n = np.sqrt(nx * nx + ny * ny + nz * nz)
    rgb = np.stack([nx / n, ny / n, nz / n], -1) * 0.5 + 0.5
    return Image.fromarray((rgb * 255).astype(np.uint8), "RGB")
