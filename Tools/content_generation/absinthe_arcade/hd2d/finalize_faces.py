"""Finalize every Absinthe Arcade box face into engine textures at one shared world scale.

For each face: day master + registered night (same pixel frame as day) ->
  <id>_day.png, <id>_night.png (identical alpha from day), <id>_emit.png (from night),
plus faces.json with each face's world size so the Godot builder can size the boxes.

Scale rule: the WALL span (columns covered >60% through the storeys, ignoring overhangs such as
the hanging sign or eaves) maps to the face's world width at PPM pixels per metre. Ground line is
detected as the last mostly-covered row. Re-run after any face is regenerated.

Usage: python finalize_faces.py <gen_dir> <out_dir>
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from normalize_face import emission_mask, flood_alpha  # noqa: E402
from relief import HEIGHT_RANGE_M, encode_height, normal_map, relief_metres  # noqa: E402

# Optional relief source per face: a generated height/clay render registered to the day master.
HEIGHTS = {
    "aa_face_front": "aa_face_front_height_reg.png",
    "aa_face_left": "aa_face_left_height_reg.png",
    "aa_face_right": "aa_face_right_height_reg.png",
    "aa_face_back": "aa_face_back_height_reg.png",
}

PPM = 1024 / 15.4  # pixels per metre, fixed by the approved front face

FACES = {
    # id: (day master, night registered to day, wall width in metres)
    "aa_face_front": ("aa_face_front_day_v2.png", "aa_face_front_night_glow.png", 15.4),
    "aa_face_left": ("aa_face_left_day_fixed.png", "aa_face_left_night_fixed_glow.png", 18.0),
    "aa_face_right": ("aa_face_right_day_fixed.png", "aa_face_right_night_nbp_v1_reg_glow.png", 18.0),
    "aa_face_back": ("aa_face_back_day_fixed.png", "aa_face_back_night_nbp_v1_reg_glow.png", 15.4),
}


def wall_metrics(alpha: np.ndarray) -> tuple[int, int, int]:
    cov = alpha > 8
    h = cov.shape[0]
    rows = cov.mean(1)
    ground = int(np.where(rows > 0.3)[0].max()) + 1
    mid = cov[int(h * 0.45): int(ground * 0.95)].mean(0)
    cols = np.where(mid > 0.6)[0]
    return int(cols.min()), int(cols.max()) + 1, ground


def main(gen: str, out: str) -> None:
    gen_p, out_p = Path(gen), Path(out)
    out_p.mkdir(parents=True, exist_ok=True)
    report = {"ppm": PPM, "faces": {}}
    for fid, (day_f, night_f, width_m) in FACES.items():
        if not (gen_p / night_f).exists():
            print(f"skip {fid}: missing {night_f}")
            continue
        day = np.asarray(Image.open(gen_p / day_f).convert("RGB"))
        night = np.asarray(Image.open(gen_p / night_f).convert("RGB"))
        assert day.shape == night.shape, f"{fid}: night not registered to day {night.shape} vs {day.shape}"
        alpha = flood_alpha(day, 18).copy()
        wl, wr, ground = wall_metrics(alpha)
        alpha[ground:] = 0
        ys, xs = np.where(alpha > 8)
        x0, x1, y0 = xs.min(), xs.max() + 1, ys.min()
        s = (width_m * PPM) / (wr - wl)
        size = (round((x1 - x0) * s), round((ground - y0) * s))
        outs = {}
        for tag, rgb in (("day", day), ("night", night)):
            im = Image.fromarray(np.dstack([rgb, alpha]), "RGBA").crop((x0, y0, x1, ground))
            im = im.resize(size, Image.LANCZOS)
            im.save(out_p / f"{fid}_{tag}.png", optimize=True)
            outs[tag] = im
        Image.fromarray(emission_mask(np.asarray(outs["night"]), 0.55, 0.35), "RGBA").save(
            out_p / f"{fid}_emit.png", optimize=True)
        wall_x0 = (wl - x0) * s
        report["faces"][fid] = {
            "texture_px": list(size),
            "wall_width_m": width_m,
            "height_m": round(size[1] / PPM, 3),
            "wall_left_px": round(wall_x0),
            "wall_right_px": round(wall_x0 + width_m * PPM),
        }
        hsrc = gen_p / HEIGHTS.get(fid, "")
        if fid in HEIGHTS and hsrc.exists():
            render = np.asarray(Image.open(hsrc).convert("L"), float) / 255
            assert render.shape == alpha.shape, f"{fid}: height not registered to day"
            slab, detail = relief_metres(render, alpha)

            def fit(a: np.ndarray) -> np.ndarray:
                return np.asarray(Image.fromarray(a, "F").crop((x0, y0, x1, ground)).resize(size, Image.BILINEAR))

            hm_a = fit(slab)
            encode_height(hm_a).save(out_p / f"{fid}_height.png", optimize=True)
            normal_map(fit(detail), PPM).save(out_p / f"{fid}_normal.png", optimize=True)
            report["faces"][fid]["height_range_m"] = HEIGHT_RANGE_M
            print(f"  relief: {hm_a.min():+.2f} .. {hm_a.max():+.2f} m")
        print(f"{fid}: {size[0]}x{size[1]} px, height {size[1] / PPM:.2f} m, wall px {wall_x0:.0f}..{wall_x0 + width_m * PPM:.0f}")
    (out_p / "faces.json").write_text(json.dumps(report, indent=2))


if __name__ == "__main__":
    main(*sys.argv[1:3])
