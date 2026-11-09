"""Finalize Absinthe Arcade street props into engine billboard sprites.

For each prop: day master + night relight (registered to day) ->
  <id>_day.png, <id>_night.png  (identical alpha cut from the DAY image: white bg removed,
                                 only the largest connected shape kept, so generator ghosts drop)
  <id>_emit.png                 (night emission: bright saturated pixels)
plus props.json with world size (metres) and a bottom-centre pivot.

Usage: python finalize_props.py <gen_dir> <out_dir>
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).parent))
from normalize_face import emission_mask, flood_alpha  # noqa: E402
from register_to import main as register  # noqa: E402

PPM = 400.0  # px per metre for props: they are seen close up, keep generator detail

# Every prop is an ORTHOGRAPHIC view (front elevation, or pure side profile), so it can be
# mounted on a box face / wall / flat card without baked-in slant. Generated in Firefly with the
# front facade attached first as the camera anchor (Nano Banana copies the first image's angle).
# id: (day file, night file, size in metres, size axis "h" or "w", optional silhouette mask file)
PROPS = {
    "aa_prop_cabinet_front": ("aa_prop_cabinet_front_day_v2.png", "aa_prop_cabinet_front_night_v1.png", 1.85, "h", None),
    "aa_prop_cabinet_side": ("aa_prop_cabinet_side_day_v3.png", "aa_prop_cabinet_side_night_v1.png", 1.85, "h",
                             "aa_prop_cabinet_side_mask.png"),
    "aa_prop_chalkboard": ("aa_prop_chalkboard_front_day_v1.png", "aa_prop_chalkboard_front_night_v1.png", 1.15, "h", None),
    "aa_prop_wall_sign_tokens": ("aa_prop_sign_tokens_front_day_v1.png", "aa_prop_sign_tokens_front_night_v1.png", 1.6, "h", None),
    "aa_prop_awning_bracket": ("aa_prop_awning_bracket_day_v1.png", "aa_prop_awning_bracket_night_v1.png", 1.05, "h",
                               "aa_prop_awning_bracket_mask.png"),
    "aa_prop_wall_lantern_front": ("aa_prop_lantern_front_day_v1.png", "aa_prop_lantern_front_night_v1.png", 0.8, "h", None),
    "aa_prop_wall_lantern_side": ("aa_prop_wall_lantern_day_v1.png", "aa_prop_wall_lantern_night_v1.png", 0.95, "h", None),
    "aa_prop_bollard": ("aa_prop_bollard_day_v1.png", "aa_prop_bollard_night_v1.png", 0.9, "h", None),
    "aa_prop_potted_shrub": ("aa_prop_potted_shrub_day_v1.png", "aa_prop_potted_shrub_night_v1.png", 1.3, "h", None),
    "aa_prop_metal_bucket": ("aa_prop_bucket_front_day_v1.png", "aa_prop_bucket_front_night_v1.png", 0.38, "h", None),
}


def main_shape(alpha: np.ndarray) -> np.ndarray:
    solid = alpha > 128
    lab, n = ndimage.label(ndimage.binary_dilation(solid, iterations=6))
    if n <= 1:
        return alpha
    sizes = ndimage.sum(solid, lab, range(1, n + 1))
    keep = np.isin(lab, [int(np.argmax(sizes)) + 1])
    return np.where(keep, alpha, 0).astype(np.uint8)


def main(gen: str, out: str) -> None:
    gen_p, out_p = Path(gen), Path(out)
    out_p.mkdir(parents=True, exist_ok=True)
    report = {"ppm": PPM, "props": {}}
    for pid, (day_f, night_f, size_m, axis, mask_f) in PROPS.items():
        night_reg = gen_p / night_f.replace(".png", "_reg.png")
        if not (gen_p / night_f).exists():
            print(f"skip {pid}: missing {night_f}")
            continue
        register(str(gen_p / day_f), str(gen_p / night_f), str(night_reg))
        day = np.asarray(Image.open(gen_p / day_f).convert("RGB"))
        night = np.asarray(Image.open(night_reg).convert("RGB"))
        alpha = main_shape(flood_alpha(day, 14).copy())
        # Background trapped inside scrollwork/brackets is not border-connected; clear large
        # pockets of pure white (small white details such as chalk strokes are kept).
        pure = day.min(axis=2) >= 246
        lab, n = ndimage.label(pure & (alpha > 0))
        if n:
            sizes = ndimage.sum(pure, lab, range(1, n + 1))
            big = np.isin(lab, [i + 1 for i, sz in enumerate(sizes) if sz > 600])
            alpha[ndimage.binary_dilation(big, iterations=1)] = 0
        if mask_f:
            mask = np.asarray(Image.open(gen_p / mask_f).convert("L")) > 127
            alpha = np.where(mask, alpha, 0).astype(np.uint8)
        ys, xs = np.where(alpha > 8)
        x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
        s = size_m * PPM / ((y1 - y0) if axis == "h" else (x1 - x0))
        size = (max(1, round((x1 - x0) * s)), max(1, round((y1 - y0) * s)))
        height_m = size[1] / PPM
        outs = {}
        for tag, rgb in (("day", day), ("night", night)):
            im = Image.fromarray(np.dstack([rgb, alpha]), "RGBA").crop((x0, y0, x1, y1)).resize(size, Image.LANCZOS)
            im.save(out_p / f"{pid}_{tag}.png", optimize=True)
            outs[tag] = im
        Image.fromarray(emission_mask(np.asarray(outs["night"]), 0.6, 0.35), "RGBA").save(
            out_p / f"{pid}_emit.png", optimize=True)
        report["props"][pid] = {"texture_px": list(size), "height_m": round(height_m, 3),
                                "width_m": round(size[0] / PPM, 3), "pivot": "bottom_center"}
        print(f"{pid}: {size[0]}x{size[1]} px  ({size[0] / PPM:.2f} x {height_m} m)")
    (out_p / "props.json").write_text(json.dumps(report, indent=2))


if __name__ == "__main__":
    main(*sys.argv[1:3])
