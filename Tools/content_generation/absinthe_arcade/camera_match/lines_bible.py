"""Trace the bible's facade line features (full res) used by solve_camera.py and residuals.py.
  <venv python> lines_bible.py [overlay_out.png]   -> lines_bible.json beside this script
"""
import json
import sys
from pathlib import Path

import numpy as np
import edges
from PIL import Image, ImageDraw
F = {
 # facade verticals (fv), world verticals (wv), facade horizontals (fh)
 "fv_lpipe_up":   ((1620, 150), (1490, 1640), "dark", "v", 30),
 "fv_rpipe_up_r": ((4612, 150), (4760, 1700), "+", "v", 30),
 "fv_r1_frame_l": ((4032, 520), (4048, 1120), "-", "v", 25),
 "fv_r1_frame_r": ((4397, 440), (4430, 1120), "+", "v", 30),
 "fv_cat_frame_l": ((1925, 850), (1907, 1440), "-", "v", 25),
 "fv_cat_frame_r": ((2224, 820), (2207, 1440), "+", "v", 25),
 "fv_l1_frame_l": ((1832, 2420), (1818, 2820), "-", "v", 20),
 "fv_l1_frame_r": ((2190, 2420), (2183, 2800), "+", "v", 20),
 "fv_door_lglass": ((2783, 3250), (2783, 3900), "+", "v", 22),
 "fv_door_rglass": ((4017, 3250), (4017, 3900), "-", "v", 22),
 "wv_lamppost1":  ((160, 3250), (118, 3690), "dark", "v", 25),
 "fh_slogan_top": ((2620, 2903), (4080, 2822), "bright", "h", 14),
 "fh_r1_sill":    ((3930, 1293), (4560, 1152), "dark", "h", 20),
 "fh_cat_sill":   ((1740, 1528), (2320, 1462), "dark", "h", 20),
 "fh_l1_sill":    ((1640, 2928), (2190, 2872), "dark", "h", 20),
 "fh_l3_sill":    ((1885, 435), (2310, 355), "dark", "h", 20),
 "fh_r1_top":     ((4045, 492), (4380, 414), "-", "h", 20),
 "fh_r1_transom": ((4050, 705), (4390, 672), "dark", "h", 20),
 "fh_cat_top":    ((1935, 852), (2218, 797), "-", "h", 20),
 "fh_cat_transom": ((1915, 1052), (2205, 1014), "dark", "h", 20),
 "fh_l1_transom": ((1850, 2405), (2180, 2385), "dark", "h", 20),
}
if __name__ == "__main__":
    out = {}
    for k, (p0, p1, mode, o, band) in F.items():
        pts = edges.trace(p0, p1, mode, o, band=band)
        a, b, rms, n, m = edges.fit(pts, o)
        out[k] = dict(a=float(a), b=float(b), rms=round(rms, 2), n=n, of=len(pts), p0=p0, p1=p1, o=o)
        print(f"{k:16s} a={a:9.1f} b={b:+.5f} rms={rms:5.2f} {n}/{len(pts)}")
    json.dump(out, open(Path(__file__).with_name("lines_bible.json"), "w"), indent=1)
    im = Image.open(edges.SRC).convert("RGB")
    d = ImageDraw.Draw(im)
    for k, L in out.items():
        a, b = L["a"], L["b"]
        if L["o"] == "h":
            xs = sorted([L["p0"][0], L["p1"][0]])
            d.line([(xs[0], a + b * xs[0]), (xs[1], a + b * xs[1])], fill=(255, 0, 0), width=3)
        else:
            ys = sorted([L["p0"][1], L["p1"][1]])
            d.line([(a + b * ys[0], ys[0]), (a + b * ys[1], ys[1])], fill=(255, 0, 0), width=3)
    im.save(sys.argv[1] if len(sys.argv) > 1 else "lines_overlay_full.png")
