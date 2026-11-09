"""Cut the Absinthe Arcade interior depth layers out of the approved main-hall painting.

Hall v8 is one painting at night plus a pixel-registered day version, so every layer is a crop of
the same canvas: `<id>_day.png`, `<id>_night.png` and (unless the layer has no glow) `<id>_emit.png`,
all with the same alpha. Also writes the whole hall as `aa_int_hall_{day,night,emit}.png` (the
backdrop) and `layers.json` (crop rectangles in hall pixels) for the Godot scene.

Emit is black except where the night painting emits light: saturated bright colour (neon, screens,
green bar glass) and near-white lamp cores. It is the night colour there, ready to add on top.

Usage:
  python cut_interior_layers.py NIGHT.png DAY.png POLYS.json OUT_DIR [--pad 6] [--feather 1.5]
"""
import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def emit_map(night: np.ndarray) -> np.ndarray:
    """RGB emission (0..1) from the night painting."""
    mx, mn = night.max(-1), night.min(-1)
    sat = (mx - mn) / (mx + 1e-4)
    neon = np.clip((sat * mx - 0.38) / 0.30, 0, 1)
    lamp = np.clip((night.mean(-1) - 0.80) / 0.15, 0, 1)
    m = np.clip(neon + lamp, 0, 1)
    m = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)),
                   np.float32) / 255
    return night * m[..., None]


def to_img(a: np.ndarray, alpha: np.ndarray | None = None) -> Image.Image:
    rgb = (np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)
    if alpha is None:
        return Image.fromarray(rgb, "RGB")
    return Image.fromarray(np.dstack([rgb, (alpha * 255 + 0.5).astype(np.uint8)]), "RGBA")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("night")
    p.add_argument("day")
    p.add_argument("polys")
    p.add_argument("out_dir")
    p.add_argument("--pad", type=int, default=6)
    p.add_argument("--feather", type=float, default=1.5)
    a = p.parse_args()

    night_im = Image.open(a.night).convert("RGB")
    day_im = Image.open(a.day).convert("RGB")
    if day_im.size != night_im.size:
        raise SystemExit(f"day {day_im.size} and night {night_im.size} must be the same canvas")
    cfg = json.load(open(a.polys, encoding="utf-8"))
    if tuple(cfg["source_size"]) != night_im.size:
        raise SystemExit(f"polygons were traced on {cfg['source_size']}, hall is {night_im.size}")
    night = np.asarray(night_im, np.float32) / 255
    day = np.asarray(day_im, np.float32) / 255
    emit = emit_map(night)
    w, h = night_im.size

    out = Path(a.out_dir)
    (out / "depth_layers").mkdir(parents=True, exist_ok=True)
    (out / "hall").mkdir(parents=True, exist_ok=True)
    for tag, arr in (("day", day), ("night", night), ("emit", emit)):
        to_img(arr).save(out / "hall" / f"aa_int_hall_{tag}.png", optimize=True)

    meta = {"source_size": [w, h], "layers": {}}
    for lid, spec in cfg["layers"].items():
        mask = Image.new("L", (w, h), 0)
        d = ImageDraw.Draw(mask)
        for poly in spec["polys"]:
            d.polygon([tuple(pt) for pt in poly], fill=255)
        if a.feather > 0:
            mask = mask.filter(ImageFilter.GaussianBlur(a.feather))
        x0, y0, x1, y1 = mask.getbbox()
        x0, y0 = max(0, x0 - a.pad), max(0, y0 - a.pad)
        x1, y1 = min(w, x1 + a.pad), min(h, y1 + a.pad)
        alpha = np.asarray(mask, np.float32)[y0:y1, x0:x1] / 255
        tags = [("day", day), ("night", night)] + ([("emit", emit)] if spec.get("emit", True) else [])
        for tag, arr in tags:
            to_img(arr[y0:y1, x0:x1], alpha).save(out / "depth_layers" / f"{lid}_{tag}.png", optimize=True)
        meta["layers"][lid] = {"rect_px": [x0, y0, x1 - x0, y1 - y0], "emit": spec.get("emit", True)}
        print(f"{lid}: rect {x0},{y0} {x1 - x0}x{y1 - y0}  tags {[t for t, _ in tags]}")
    (out / "depth_layers" / "layers.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
