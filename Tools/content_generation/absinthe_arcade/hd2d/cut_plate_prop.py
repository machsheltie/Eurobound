"""Cut one painted-in prop out of an Absinthe Arcade interior plate set (day, night, emit) and inpaint behind it.

Generic form of cut_restroom_statue.py (bead Eurobound-pg9a); first used for the Taproom chalice (Eurobound-j9ru).
Interactables rule: design/style_guides/location_interactables_rule.md. Gate C: dev/qc/QC_COVERAGE.md.

  python -I Tools/content_generation/absinthe_arcade/hd2d/cut_plate_prop.py <config.json> mask
  python -I Tools/content_generation/absinthe_arcade/hd2d/cut_plate_prop.py <config.json> composite <clean_day.png>

config.json (paths relative to the repo root):
  {"plates_dir": "game/.../interior/taproom", "plate_base": "aa_int_taproom",
   "originals_dir": "Assets/.../references/Interior/plates_with_<prop>",   kept copies of the plates WITH the prop
   "zones_dir": "tools/paint_zones/work/<id>/masks", "zones": ["chalice"],  SAM masks to union
   "close_px": 4, "margin_px": 16,                                          sliver close; inpaint margin
   "prop_name": "aa_int_taproom_chalice", "prop_json": "chalice.json", "pad_px": 8,
   "work_dir": "Tools/content_generation/absinthe_arcade/hd2d/work_<prop>",
   "spec": {...extra keys copied into the prop json (ids, float spec)}}

mask       union the SAM zones, close slivers, fill holes -> work/prop_mask.png; dilate by margin_px and feather ->
           work/inpaint_mask.png
composite  paste the inpainted clean day plate (a Gemini edit of the day plate; it must be pixel-registered) inside
           the inpaint mask only, tone-matched on a band just outside it; night = affine day->night colour fit on the
           surroundings; emit = the hall emit rule on the night composite; write the clean plates over the live ones
           (originals kept once in originals_dir and always re-read), and the prop layers <prop_name>_{day,night,emit}.png
           (one shared alpha) + <prop_json> with plate_xy and size into plates_dir/props/.
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 4))
R = lambda p: os.path.join(ROOT, p)
KINDS = ("day", "night", "emit")


def L(a):
    return Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8), "L")


def arr(im):
    return np.asarray(im).astype(np.float32) / 255.0


def dilate(mask, r):
    k = 2 * r + 1
    c = np.pad(np.pad(mask.astype(np.int32), r).cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    return (c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]) > 0


def emit_map(night):
    """Same rule as cut_interior_layers.emit_map (hall): saturated neon and near-white lamp cores."""
    mx, mn = night.max(-1), night.min(-1)
    sat = (mx - mn) / (mx + 1e-4)
    neon = np.clip((sat * mx - 0.38) / 0.30, 0, 1)
    lamp = np.clip((night.mean(-1) - 0.80) / 0.15, 0, 1)
    m = arr(L(np.clip(neon + lamp, 0, 1)).filter(ImageFilter.GaussianBlur(1.2)))
    return night * m[..., None]


def originals(c):
    out = {}
    for k in KINDS:
        kept = R(os.path.join(c["originals_dir"], f"{c['plate_base']}_{k}_with_prop.png"))
        out[k] = kept if os.path.exists(kept) else R(os.path.join(c["plates_dir"], f"{c['plate_base']}_{k}.png"))
    return out


def step_mask(c):
    work = R(c["work_dir"]); os.makedirs(work, exist_ok=True)
    m = None
    for z in c["zones"]:
        a = np.asarray(Image.open(R(os.path.join(c["zones_dir"], z + ".png"))).convert("L")) > 127
        m = a if m is None else (m | a)
    cp = int(c.get("close_px", 4))
    if cp:
        m = ~dilate(~dilate(m, cp), cp)                                    # closing
    bg = Image.fromarray(np.where(m, 255, 0).astype(np.uint8)).copy()   # copy: floodfill needs owned pixels
    ImageDraw.floodfill(bg, (0, 0), 128)
    prop = np.asarray(bg) != 128
    L(prop.astype(np.float32)).save(os.path.join(work, "prop_mask.png"))
    L(dilate(prop, int(c.get("margin_px", 16))).astype(np.float32)).filter(
        ImageFilter.GaussianBlur(max(2, int(c.get("margin_px", 16)) // 4))).save(os.path.join(work, "inpaint_mask.png"))
    ys, xs = np.nonzero(prop)
    print("prop px", int(prop.sum()), "bbox", int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()))


def step_composite(c, clean_path):
    work = R(c["work_dir"])
    od = R(c["originals_dir"]); os.makedirs(od, exist_ok=True)
    for k, p in originals(c).items():
        kept = os.path.join(od, f"{c['plate_base']}_{k}_with_prop.png")
        if not os.path.exists(kept):
            Image.open(p).save(kept)
    src = originals(c)
    day, night, emit = (arr(Image.open(src[k]).convert("RGB")) for k in KINDS)
    H, W = day.shape[:2]
    prop = arr(Image.open(os.path.join(work, "prop_mask.png"))) > 0.5
    inp = arr(Image.open(os.path.join(work, "inpaint_mask.png")))
    clean = Image.open(R(clean_path) if not os.path.isabs(clean_path) else clean_path).convert("RGB")
    if clean.size != (W, H):
        clean = clean.resize((W, H), Image.LANCZOS)
    clean = arr(clean)
    inside = inp > 0.02
    band = dilate(inside, 40) & ~inside
    gain = day[band].mean(0) / np.maximum(clean[band].mean(0), 1e-4)
    clean = np.clip(clean * gain, 0, 1)
    a = inp[..., None]
    day_c = day * (1 - a) + clean * a

    yy, xx = np.nonzero(prop)
    box = np.zeros((H, W), bool)
    box[max(yy.min() - 120, 0):min(yy.max() + 120, H), max(xx.min() - 120, 0):min(xx.max() + 120, W)] = True
    fit = box & ~dilate(prop, 40)
    X = np.concatenate([day[fit], np.ones((int(fit.sum()), 1), np.float32)], 1)
    M, *_ = np.linalg.lstsq(X, night[fit], rcond=None)
    pred = np.clip((np.concatenate([day_c.reshape(-1, 3), np.ones((H * W, 1), np.float32)], 1) @ M).reshape(H, W, 3), 0, 1)
    err = float(np.abs(pred[fit] - night[fit]).mean())
    night_c = night * (1 - a) + pred * a
    emit_c = emit * (1 - a) + emit_map(night_c) * a
    for k, im in zip(KINDS, (day_c, night_c, emit_c)):
        Image.fromarray((im * 255 + 0.5).astype(np.uint8), "RGB").save(R(os.path.join(c["plates_dir"], f"{c['plate_base']}_{k}.png")))

    alpha = arr(L(prop.astype(np.float32)).filter(ImageFilter.GaussianBlur(0.8)))
    pad = int(c.get("pad_px", 8))
    bx0, by0 = max(int(xx.min()) - pad, 0), max(int(yy.min()) - pad, 0)
    bx1, by1 = min(int(xx.max()) + pad + 1, W), min(int(yy.max()) + pad + 1, H)
    pdir = R(os.path.join(c["plates_dir"], "props")); os.makedirs(pdir, exist_ok=True)
    spec = {"plate_size": [W, H], "plate_xy": [bx0, by0], "size": [bx1 - bx0, by1 - by0],
            "files": {k: f"{c['prop_name']}_{k}.png" for k in KINDS}}
    spec.update(c.get("spec", {}))
    for k, im in zip(KINDS, (day, night, emit)):
        Image.fromarray((np.dstack([im, alpha])[by0:by1, bx0:bx1] * 255 + 0.5).astype(np.uint8), "RGBA").save(
            os.path.join(pdir, spec["files"][k]))
    with open(os.path.join(pdir, c["prop_json"]), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
    print("composited; tone gain", np.round(gain, 3).tolist(), "night fit err", round(err, 4),
          "prop", spec["plate_xy"], spec["size"])


if __name__ == "__main__":
    cfg = json.load(open(R(sys.argv[1]) if not os.path.isabs(sys.argv[1]) else sys.argv[1], encoding="utf-8"))
    if sys.argv[2] == "mask":
        step_mask(cfg)
    elif sys.argv[2] == "composite":
        step_composite(cfg, sys.argv[3])
