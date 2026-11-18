"""Protocol step 2: segment a canonical reference with SAM into per-zone masks and unaltered crops.

Usage (from the repo root):
  tools/paint_zones/.venv/Scripts/python tools/paint_zones/segment_ref.py <zones.json> [--sheet]

zones.json:
  {"asset_id": "chadwick", "image": "<canonical ref path>", "sha256": "<from refs/registry.json>",
   "model": "sam2.1_hiera_base_plus",
   "zones": {"polo": {"pos": [[x,y],...], "neg": [[x,y],...], "box": [x0,y0,x1,y1] (optional),
                       "minus": ["other_zone", ...] (optional: subtract masks made earlier),
                       "keep_hsv": {"s": [lo, hi], "v": [lo, hi], "h": [lo, hi]} (optional, 0-1; keep only those pixels),
                       "close_px": N (optional, with keep_hsv: fill holes up to N px, e.g. prints on a strap),
                       "open_px": N (optional, with keep_hsv: cut bridges thinner than N px),
                       "cut_boxes": [[x0,y0,x1,y1], ...] (optional hand correction: remove these boxes),
                       "largest_cc": true (optional: keep only the biggest connected piece)}}}

Coordinates are pixels of the full-size reference. Writes work/<asset_id>/masks/<zone>.png,
work/<asset_id>/crops/<zone>.png (alpha = mask, pixels untouched) and work/<asset_id>/segment.json
(area, bbox, SAM score, median colour). --sheet also writes a <=1024 px overlay sheet for review.
Prints at most a few lines.
"""
import argparse, hashlib, json, os, sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = {"sam2.1_hiera_base_plus": ("configs/sam2.1/sam2.1_hiera_b+.yaml", "sam2.1_hiera_base_plus.pt"),
       "sam2.1_hiera_large": ("configs/sam2.1/sam2.1_hiera_l.yaml", "sam2.1_hiera_large.pt"),
       "sam2.1_hiera_small": ("configs/sam2.1/sam2.1_hiera_s.yaml", "sam2.1_hiera_small.pt")}
PALETTE = [(230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200), (245, 130, 48), (145, 30, 180),
           (70, 240, 240), (240, 50, 230), (210, 245, 60), (250, 190, 212), (0, 128, 128), (220, 190, 255),
           (170, 110, 40), (255, 250, 200), (128, 0, 0), (170, 255, 195), (128, 128, 0), (0, 0, 128)]


def load_predictor(model):
    import torch
    from sam2.build_sam import build_sam2
    from sam2.sam2_image_predictor import SAM2ImagePredictor
    cfg, ckpt = CFG[model]
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    sam = build_sam2(cfg, os.path.join(HERE, "checkpoints", ckpt), device=dev)
    return SAM2ImagePredictor(sam), dev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zones")
    ap.add_argument("--sheet", action="store_true")
    a = ap.parse_args()
    z = json.load(open(a.zones))
    raw = open(z["image"], "rb").read()
    if z.get("sha256") and hashlib.sha256(raw).hexdigest() != z["sha256"]:
        sys.exit("reference sha256 mismatch: the canonical image changed; re-register it first")
    img = Image.open(z["image"]).convert("RGBA")
    rgb = np.array(img.convert("RGB"))
    H, W = rgb.shape[:2]
    out = os.path.join(HERE, "work", z["asset_id"])
    os.makedirs(os.path.join(out, "masks"), exist_ok=True)
    os.makedirs(os.path.join(out, "crops"), exist_ok=True)

    import torch
    pred, dev = load_predictor(z.get("model", "sam2.1_hiera_base_plus"))
    masks, info = {}, {}
    with torch.inference_mode(), torch.autocast(dev, dtype=torch.bfloat16, enabled=(dev == "cuda")):
        pred.set_image(rgb)
        for name, zd in z["zones"].items():
            pts = [(p, 1) for p in zd.get("pos", [])] + [(p, 0) for p in zd.get("neg", [])]
            kw = {}
            if pts:
                kw["point_coords"] = np.array([p for p, _ in pts], dtype=np.float32)
                kw["point_labels"] = np.array([l for _, l in pts], dtype=np.int32)
            if zd.get("box"):
                kw["box"] = np.array(zd["box"], dtype=np.float32)
            m, sc, _ = pred.predict(multimask_output=False, **kw)
            mk = m[0] > 0.5
            if zd.get("keep_hsv"):   # keep only pixels in an HSV range (0-1), e.g. a navy strap over pale denim
                import cv2
                r = zd["keep_hsv"]
                hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV_FULL).astype(np.float32) / 255.0
                ok = np.ones(mk.shape, bool)
                for i, ch in enumerate("hsv"):
                    lo, hi = r.get(ch, [0.0, 1.0])
                    ok &= (hsv[..., i] >= lo) & (hsv[..., i] <= hi)
                keep = (mk & ok).astype(np.uint8)
                c = zd.get("close_px", 0)
                if c:   # fill small holes left by prints or highlights inside the kept part
                    keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (c, c)))
                o = zd.get("open_px", 0)
                if o:   # cut thin bridges (seams, stitching) after filling holes
                    keep = cv2.morphologyEx(keep, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (o, o)))
                mk &= keep.astype(bool)
            for x0, y0, x1, y1 in zd.get("cut_boxes", []):   # hand correction: zero these image-space boxes
                mk[y0:y1, x0:x1] = False
            if zd.get("largest_cc"):   # drop specks: keep only the biggest connected piece
                import cv2
                n, lab, st, _ = cv2.connectedComponentsWithStats(mk.astype(np.uint8), 8)
                if n > 1:
                    mk = lab == (1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])))
            for other in zd.get("minus", []):
                if other in masks:
                    mk &= ~masks[other]
            masks[name] = mk
            info[name] = {"score": round(float(sc[0]), 3)}
    for name, mk in masks.items():
        Image.fromarray((mk * 255).astype(np.uint8)).save(os.path.join(out, "masks", f"{name}.png"))
        ys, xs = np.nonzero(mk)
        if len(xs) == 0:
            info[name].update(area=0)
            continue
        x0, y0, x1, y1 = int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1
        crop = np.array(img)[y0:y1, x0:x1].copy()
        crop[..., 3] = np.where(mk[y0:y1, x0:x1], crop[..., 3], 0)
        Image.fromarray(crop).save(os.path.join(out, "crops", f"{name}.png"))
        px = rgb[mk].astype(np.float32)
        lum = px @ np.array([0.299, 0.587, 0.114])
        lo, hi = np.percentile(lum, 10), np.percentile(lum, 90)
        hexc = lambda c: "#%02X%02X%02X" % tuple(int(round(v)) for v in c)
        info[name].update(area=int(mk.sum()), bbox=[x0, y0, x1, y1], median=hexc(np.median(px, 0)),
                          shadow=hexc(np.median(px[lum <= lo], 0)), light=hexc(np.median(px[lum >= hi], 0)))
    overlap = sum(int((masks[a] & masks[b]).sum()) for i, a in enumerate(masks) for b in list(masks)[i + 1:])
    json.dump({"asset_id": z["asset_id"], "image": z["image"], "model": z.get("model"), "zones": info,
               "overlap_px": overlap}, open(os.path.join(out, "segment.json"), "w"), indent=1)
    if a.sheet:
        ov = rgb.astype(np.float32).copy()
        for i, (name, mk) in enumerate(masks.items()):
            ov[mk] = ov[mk] * 0.45 + np.array(PALETTE[i % len(PALETTE)]) * 0.55
        sheet = Image.fromarray(np.concatenate([rgb, ov.astype(np.uint8)], 1))
        sheet.thumbnail((1024, 1024))
        sheet.save(os.path.join(out, "segment_sheet.jpg"), quality=88)
        legend = ", ".join(f"{i}:{n}" for i, n in enumerate(masks))
        open(os.path.join(out, "segment_sheet_legend.txt"), "w").write(legend + "\n")
    low = [n for n, v in info.items() if v.get("score", 1) < 0.8 or v.get("area", 0) == 0]
    print(f"{len(masks)} zones -> {out}; overlap_px={overlap}; low/empty: {low or 'none'}")


if __name__ == "__main__":
    main()
