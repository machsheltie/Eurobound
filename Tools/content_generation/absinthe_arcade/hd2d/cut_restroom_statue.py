"""Cut the whole bronze Green Fairy statue out of the Absinthe Arcade restroom plates (bead Eurobound-pg9a).

Arcade rework plan §3.5 (docs/superpowers/plans/2026-11-14-arcade-rework-plan.md, approved Desk 31uj-q1).

Steps (run from the repo root, system python with Pillow + numpy):
  mask       union the SAM zones (tools/paint_zones/zones/aa_restroom_statue_day.json -> work/.../masks/*.png),
             close slivers, fill holes -> statue mask; also a dilated, feathered inpaint mask
  composite  paste an inpainted clean niche (a Gemini 3.1 edit of the day plate) into the day plate inside the
             inpaint mask only, so every pixel outside it stays pixel-identical; derive the night niche from the
             clean day niche with a colour transform fitted on the niche wall around the statue (day -> night),
             and the emit niche from the night composite with the hall's emit rule; write the statue layers
  python Tools/content_generation/absinthe_arcade/hd2d/cut_restroom_statue.py mask
  python Tools/content_generation/absinthe_arcade/hd2d/cut_restroom_statue.py composite <gemini_clean_day.png>

Outputs in game/assets/worlds/debaucheryville/absinthe_arcade/interior/restroom/:
  aa_int_restroom_{day,night,emit}.png   rewritten clean plates (originals kept once as *_with_statue.png beside the
                                         reference art in Assets/.../references/Interior/plates_with_statue/)
  props/aa_int_restroom_statue_{day,night,emit}.png + props/statue.json   the statue, cropped, with plate_xy
The two hand cut-outs (props/statue_hands.json) are unchanged: they still sit over Jakub.
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 4))
G = os.path.join(ROOT, "game/assets/worlds/debaucheryville/absinthe_arcade/interior/restroom")
REF = os.path.join(ROOT, "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Interior/plates_with_statue")
ZONES = os.path.join(ROOT, "tools/paint_zones/work/aa_restroom_statue_day/masks")
WORK = os.path.join(ROOT, "Tools/content_generation/absinthe_arcade/hd2d/work_restroom_statue")
ZONE_NAMES = ("body", "wings", "plinth", "rolls_left", "rolls_right")
PAD = 8


def L(a):
    return Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8), "L")


def arr(im):
    return np.asarray(im).astype(np.float32) / 255.0


def dilate(mask, r):
    """Square dilation of a boolean mask by r px (summed-area table; PIL MaxFilter is far too slow at this size)."""
    k = 2 * r + 1
    c = np.pad(np.pad(mask.astype(np.int32), r).cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    return (c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]) > 0


def originals():
    """The plates WITH the statue: the kept copies once they exist, else the live files."""
    out = {}
    for k in ("day", "night", "emit"):
        kept = os.path.join(REF, f"aa_int_restroom_{k}_with_statue.png")
        out[k] = kept if os.path.exists(kept) else os.path.join(G, f"aa_int_restroom_{k}.png")
    return out


def step_mask():
    os.makedirs(WORK, exist_ok=True)
    m = None
    for z in ZONE_NAMES:
        a = np.asarray(Image.open(os.path.join(ZONES, z + ".png")).convert("L")) > 127
        m = a if m is None else (m | a)
    im = L(m.astype(np.float32))
    im = im.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.MinFilter(9))       # close slivers between parts
    a = np.asarray(im) > 127
    bg = Image.fromarray(np.where(a, 255, 0).astype(np.uint8)).copy()                # fill holes (copy: floodfill needs owned pixels)
    from PIL import ImageDraw
    ImageDraw.floodfill(bg, (0, 0), 128)
    statue = np.asarray(bg) != 128
    L(statue.astype(np.float32)).save(os.path.join(WORK, "statue_mask.png"))
    inp = L(dilate(statue, 40).astype(np.float32)).filter(ImageFilter.GaussianBlur(10))   # 40 px: the painted cast shadow and outline reach past the statue
    inp.save(os.path.join(WORK, "inpaint_mask.png"))
    ys, xs = np.nonzero(statue)
    print("statue px", int(statue.sum()), "bbox", int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()))


def emit_map(night):
    """Same rule as cut_interior_layers.emit_map (hall): saturated neon and near-white lamp cores."""
    mx, mn = night.max(-1), night.min(-1)
    sat = (mx - mn) / (mx + 1e-4)
    neon = np.clip((sat * mx - 0.38) / 0.30, 0, 1)
    lamp = np.clip((night.mean(-1) - 0.80) / 0.15, 0, 1)
    m = np.clip(neon + lamp, 0, 1)
    m = arr(L(m).filter(ImageFilter.GaussianBlur(1.2)))
    return night * m[..., None]


def step_composite(clean_path):
    src = originals()
    os.makedirs(REF, exist_ok=True)
    for k, p in src.items():                                   # keep the with-statue originals once
        kept = os.path.join(REF, f"aa_int_restroom_{k}_with_statue.png")
        if not os.path.exists(kept):
            Image.open(p).save(kept)
    src = originals()
    day = arr(Image.open(src["day"]).convert("RGB"))
    night = arr(Image.open(src["night"]).convert("RGB"))
    emit = arr(Image.open(src["emit"]).convert("RGB"))
    H, W = day.shape[:2]
    statue = arr(Image.open(os.path.join(WORK, "statue_mask.png")))
    inp = arr(Image.open(os.path.join(WORK, "inpaint_mask.png")))

    clean = Image.open(clean_path).convert("RGB")
    if clean.size != (W, H):
        clean = clean.resize((W, H), Image.LANCZOS)
    clean = arr(clean)
    # match the generated pixels to the plate on a band just OUTSIDE the inpaint area, where Gemini was told to keep
    # the painting unchanged (a ring on the statue's own edge picks up its dark outline and darkens the patch)
    inside = inp > 0.02
    band = dilate(inside, 40) & ~inside
    gain = day[band].mean(0) / np.maximum(clean[band].mean(0), 1e-4)
    clean = np.clip(clean * gain, 0, 1)
    a = inp[..., None]
    day_c = day * (1 - a) + clean * a

    # night niche: affine colour map day -> night fitted on the niche wall around the statue
    yy, xx = np.nonzero(statue > 0.5)
    x0, x1, y0, y1 = xx.min() - 120, xx.max() + 120, yy.min(), yy.max()
    box = np.zeros((H, W), bool)
    box[max(y0, 0):y1, max(x0, 0):min(x1, W)] = True
    fit = box & ~dilate(statue > 0.5, 40)
    X = np.concatenate([day[fit], np.ones((int(fit.sum()), 1), np.float32)], 1)
    M, *_ = np.linalg.lstsq(X, night[fit], rcond=None)
    pred = np.concatenate([day_c.reshape(-1, 3), np.ones((H * W, 1), np.float32)], 1) @ M
    pred = np.clip(pred.reshape(H, W, 3), 0, 1)
    err = np.abs(pred[fit] - night[fit]).mean()
    night_c = night * (1 - a) + pred * a
    emit_c = emit * (1 - a) + emit_map(night_c) * a

    for k, im in (("day", day_c), ("night", night_c), ("emit", emit_c)):
        Image.fromarray((im * 255 + 0.5).astype(np.uint8), "RGB").save(os.path.join(G, f"aa_int_restroom_{k}.png"))

    # statue layers: crop with PAD, alpha = statue mask softened by 1 px
    alpha = arr(L(statue).filter(ImageFilter.GaussianBlur(0.8)))
    bx0, by0 = max(int(xx.min()) - PAD, 0), max(int(yy.min()) - PAD, 0)
    bx1, by1 = min(int(xx.max()) + PAD + 1, W), min(int(yy.max()) + PAD + 1, H)
    os.makedirs(os.path.join(G, "props"), exist_ok=True)
    spec = {"plate_size": [W, H], "plate_xy": [bx0, by0], "size": [bx1 - bx0, by1 - by0],
            "note": "Whole bronze Green Fairy statue (wings, gown, plinth, both roll stacks), cut from the restroom "
                    "plates for bead Eurobound-pg9a; top-left xy on the plate. Day, night and emit share one alpha. "
                    "The hand cut-outs in statue_hands.json still layer over Jakub.",
            "object_id": "green_fairy_statue", "node_id": "aa_node_restroom_statue",
            "files": {k: f"aa_int_restroom_statue_{k}.png" for k in ("day", "night", "emit")}}
    for k, im in (("day", day), ("night", night), ("emit", emit)):
        rgba = np.dstack([im, alpha])[by0:by1, bx0:bx1]
        Image.fromarray((rgba * 255 + 0.5).astype(np.uint8), "RGBA").save(
            os.path.join(G, "props", f"aa_int_restroom_statue_{k}.png"))
    json.dump(spec, open(os.path.join(G, "props", "statue.json"), "w"), indent=1)
    print("composited; tone gain", np.round(gain, 3).tolist(), "night fit mean abs err", round(float(err), 4),
          "statue crop", spec["plate_xy"], spec["size"])


if __name__ == "__main__":
    if sys.argv[1] == "mask":
        step_mask()
    elif sys.argv[1] == "composite":
        step_composite(sys.argv[2])
