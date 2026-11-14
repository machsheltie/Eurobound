"""Protocol step 10: region-by-region comparison of the neutral-light albedo render with the canonical reference, inside the SAM zone masks.
Both images share one pixel space (render fitted to the ref frame). Colour only compared where the render is diffuse/albedo-only (neutral mode).
Run with the paint_zones venv python (cv2): qa_compare.py <renders dir prefix> <out.json> [render_mask_dir]
Per zone: median colour of ref and render (hex), CIE76 dE of the medians, share of pixels with dE < 15, zone mask area, and a sticker/detail sharpness ratio
(Laplacian variance render/ref: < 0.5 means detail was lost in the projection)."""
import os, sys, json
import numpy as np, cv2
from PIL import Image
PK = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
SAMW = os.environ.get("PAINT_ZONES_WORK", "tools/paint_zones/work")  # machine-specific: set PAINT_ZONES_WORK
pre, outp = sys.argv[1], sys.argv[2]
def lab(rgb8):
    return cv2.cvtColor((rgb8.astype(np.float32) / 255.0)[None] if rgb8.ndim == 2 else rgb8.astype(np.float32) / 255.0, cv2.COLOR_RGB2LAB)
def flat(p):
    im = Image.open(p).convert("RGBA"); b = Image.new("RGBA", im.size, (0, 0, 0, 255)); b.alpha_composite(im); return np.array(b.convert("RGB"))
hexc = lambda c: "#%02X%02X%02X" % tuple(int(round(v)) for v in c)
res = {}
SETS = {"front": ("cabinet_trial_front", f"{PK}/source_references/aa_prop_cabinet_front_day.png", f"{pre}_neutral_front.png",
                  ["marquee", "marquee_ink", "crt_bezel", "crt_screen", "screen_invader", "control_panel", "joystick_red", "lower_fascia", "coin_door", "kick_panel_stickers", "rail_left", "rail_right"]),
        "side": ("cabinet_trial_side", f"{PK}/source_references/aa_prop_cabinet_side_day.png", f"{pre}_neutral_right.png", ["side_body", "side_stickers", "side_trim"])}
for key, (asset, refp, renp, zones) in SETS.items():
    ref = flat(refp); ren = flat(renp)
    assert ref.shape == ren.shape, (ref.shape, ren.shape)
    Lr, Ln = lab(ref), lab(ren)
    gr = cv2.cvtColor(ref, cv2.COLOR_RGB2GRAY).astype(np.float32); gn = cv2.cvtColor(ren, cv2.COLOR_RGB2GRAY).astype(np.float32)
    lr = cv2.Laplacian(gr, cv2.CV_32F); ln = cv2.Laplacian(gn, cv2.CV_32F)
    for z in zones:
        m = np.array(Image.open(f"{SAMW}/{asset}/masks/{z}.png").convert("L")) > 127
        m = cv2.erode(m.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)   # ignore the 2 px rim (edge antialiasing, bevels)
        if m.sum() < 20:
            continue
        mr, mn = np.median(ref[m], 0), np.median(ren[m], 0)
        dE = np.linalg.norm(Lr[m] - Ln[m], axis=1)
        dEm = float(np.linalg.norm(np.median(Lr[m], 0) - np.median(Ln[m], 0)))
        res[z] = {"view": key, "area_px": int(m.sum()), "ref_median": hexc(mr), "render_median": hexc(mn), "dE76_of_medians": round(dEm, 1),
                  "share_dE_lt_15": round(float((dE < 15).mean()), 3), "mean_dE": round(float(dE.mean()), 1),
                  "detail_ratio": round(float(ln[m].var() / max(lr[m].var(), 1e-6)), 2)}
json.dump(res, open(outp, "w"), indent=1)
print("zone  dE_med  share<15  detail")
for z, v in res.items():
    print(f"{z:22s} {v['dE76_of_medians']:6.1f} {v['share_dE_lt_15']:7.2f} {v['detail_ratio']:7.2f}  {v['ref_median']} -> {v['render_median']}")
