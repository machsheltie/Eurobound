"""Protocol step 10 (trial version): per-zone colour check of front renders against the canonical manifest.

Usage: tools/paint_zones/.venv/Scripts/python tools/paint_zones/qa_compare.py <manifest.json> <src_zones_dir> <src_image> <out.json> <label>=<render.png> [...]
  src_zones_dir: work/<id>/ of a SAM-segmented FRONT image whose framing matches the render (masks/<zone>.png).
  Each render is SEGMENTED WITH SAM (protocol step 10): each zone's box and points from the source zones file are
  carried into the render by fitting the figure's bounding box, then SAM traces the zone in the render itself; the
  mask is eroded 6 px (2 px for small parts). --carry uses the carried source masks without SAM (old behaviour). For each zone it prints CIE76 delta-E
  between the render's median colour and the canonical median. Lighting differs (toon render vs painting), so read
  the numbers comparatively (before vs after), not as absolute pass marks.
"""
import json, os, sys
import numpy as np, cv2
from PIL import Image

args = [a for a in sys.argv[1:] if a != "--carry"]
CARRY = "--carry" in sys.argv
man, zdir, src, out = args[:4]
renders = dict(a.split("=", 1) for a in args[4:])
ZCFG = None
for f in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "zones")):
    if f.endswith(".json"):
        _z = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "zones", f)))
        if _z.get("asset_id") == os.path.basename(os.path.normpath(zdir)) and "image" in _z:
            ZCFG = _z
PRED = None
if not CARRY:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from segment_ref import load_predictor
    import torch
    PRED, DEV = load_predictor((ZCFG or {}).get("model", "sam2.1_hiera_base_plus"))
M = json.load(open(man))
canon = {m["zone"]: m["colors"]["median"] for m in M["materials"]}
s = np.array(Image.open(src).convert("RGB"))
sfg = s.min(2) < 225
ys, xs = np.where(sfg); sb = (xs.min(), ys.min(), xs.max(), ys.max())


def lab(rgb):
    return cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2LAB)[0, 0].astype(float) * [100 / 255, 1, 1] - [0, 128, 128]


res = {}
for name, rp in renders.items():
    r = np.array(Image.open(rp).convert("RGBA"))
    ys, xs = np.where(r[..., 3] > 128); rb = (xs.min(), ys.min(), xs.max(), ys.max())
    sx = (rb[2] - rb[0]) / (sb[2] - sb[0]); sy = (rb[3] - rb[1]) / (sb[3] - sb[1])
    A = np.float32([[sx, 0, rb[0] - sb[0] * sx], [0, sy, rb[1] - sb[1] * sy]])
    res[name] = {}
    T_ = lambda x, y: (x * sx + rb[0] - sb[0] * sx, y * sy + rb[1] - sb[1] * sy)
    if PRED is not None:
        rgb_r = r[..., :3].copy(); rgb_r[r[..., 3] < 128] = 150   # flat grey background
        with torch.inference_mode(), torch.autocast(DEV, dtype=torch.bfloat16, enabled=(DEV == "cuda")):
            PRED.set_image(rgb_r)
    for f in sorted(os.listdir(os.path.join(zdir, "masks"))):
        z = f[:-4]
        if z not in canon:
            continue
        m = cv2.imread(os.path.join(zdir, "masks", f), 0)
        mw = cv2.warpAffine(m, A, (r.shape[1], r.shape[0]), flags=cv2.INTER_NEAREST)
        if PRED is not None and ZCFG and z in ZCFG["zones"]:
            zd = ZCFG["zones"][z]; kw = {}
            if zd.get("box"):
                x0, y0 = T_(*zd["box"][:2]); x1, y1 = T_(*zd["box"][2:])
                kw["box"] = np.array([x0, y0, x1, y1], np.float32)
            pts = [(T_(*p), 1) for p in zd.get("pos", [])] + [(T_(*p), 0) for p in zd.get("neg", [])]
            if pts:
                kw["point_coords"] = np.array([p for p, _ in pts], np.float32); kw["point_labels"] = np.array([l for _, l in pts], np.int32)
            with torch.inference_mode(), torch.autocast(DEV, dtype=torch.bfloat16, enabled=(DEV == "cuda")):
                mm, _, _ = PRED.predict(multimask_output=False, **kw)
            mw = ((mm[0] > 0.5) * 255).astype(np.uint8)
        for k in (13, 5):   # small parts (buckle, watch) fall back to a 5 px erosion
            me = (cv2.erode(mw, np.ones((k, k), np.uint8)) > 0) & (r[..., 3] > 200)
            if me.sum() >= 30:
                break
        mw = me
        if mw.sum() < 30:
            res[name][z] = None
            continue
        med = np.median(r[..., :3][mw], 0)
        c = [int(canon[z][i:i + 2], 16) for i in (1, 3, 5)]
        res[name][z] = round(float(np.linalg.norm(lab(med) - lab(c))), 1)
json.dump(res, open(out, "w"), indent=1)
zones = sorted({z for v in res.values() for z in v})
print("zone".ljust(14) + "".join(n[:10].rjust(11) for n in res))
for z in zones:
    print(z.ljust(14) + "".join(str(res[n].get(z)).rjust(11) for n in res))
