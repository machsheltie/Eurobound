"""Protocol step 10 (SAM-assisted QA). Two modes, run with the paint_zones venv python from the worktree root:
  sam_qa.py prep            -> writes zones/cabinet_qa_{front,side}.json: the SAME zone prompts as the references, but pointed at the neutral renders
  (then run tools/paint_zones/segment_ref.py on each, one job at a time)
  sam_qa.py compare <out.json> -> per-zone IoU and centroid shift between the SAM mask of the render and the SAM mask of the reference."""
import os, sys, json
import numpy as np
from PIL import Image
PK = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
SAMW = os.environ.get("PAINT_ZONES_WORK", "tools/paint_zones/work")  # machine-specific: set PAINT_ZONES_WORK
if sys.argv[1] == "prep":
    for v, ren in (("front", "neutral_front"), ("side", "neutral_right")):
        z = json.load(open(f"{PK}/scripts/zones/cabinet_{v}_ref.json"))
        z["asset_id"] = f"cabinet_qa_{v}"; z["image"] = f"{PK}/renders/cabinet_{ren}.png"; z.pop("sha256", None)
        json.dump(z, open(f"{PK}/scripts/zones/cabinet_qa_{v}.json", "w"), indent=1)
    print("prepped")
else:
    out = {}
    for v in ("front", "side"):
        ref = json.load(open(f"{SAMW}/cabinet_trial_{v}/segment.json"))["zones"]
        ren = json.load(open(f"{SAMW}/cabinet_qa_{v}/segment.json"))["zones"]
        for z in ref:
            a = np.array(Image.open(f"{SAMW}/cabinet_trial_{v}/masks/{z}.png").convert("L")) > 127
            b = np.array(Image.open(f"{SAMW}/cabinet_qa_{v}/masks/{z}.png").convert("L")) > 127
            iou = float((a & b).sum() / max((a | b).sum(), 1))
            ca = np.array(np.nonzero(a)).mean(1); cb = np.array(np.nonzero(b)).mean(1) if b.any() else ca
            out[z] = {"view": v, "mask_iou": round(iou, 3), "centroid_shift_px": [round(float(cb[1] - ca[1]), 1), round(float(cb[0] - ca[0]), 1)],
                      "area_ratio": round(float(b.sum() / max(a.sum(), 1)), 2), "sam_score_ref": ref[z]["score"], "sam_score_render": ren[z]["score"]}
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    for z, r in out.items():
        print(f"{z:22s} iou {r['mask_iou']:.2f} shift {r['centroid_shift_px']} area x{r['area_ratio']}")
