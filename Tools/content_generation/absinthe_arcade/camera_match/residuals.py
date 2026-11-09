"""E1 model-vs-bible residuals, per feature, in bible pixels (5248 wide).

  <venv python> residuals.py [--render final_bible_cam_clay.png] [--out residuals.json] [--debug dbg.png]

For every feature: a 3D segment of the model (from dev/aa_team/interfaces.json v2, i.e. what
build_shell.py builds) is projected through aa_bible_cam; the bible's own edge is traced (full
res, robust line fit) in a band round that projection; the residual is the signed perpendicular
offset of the bible line from the model segment at its midpoint (+ = bible right of / below the
model). With --render, the same edge is also traced in the render (upscaled to 5248) to confirm
the render shows the geometry where the projection says (render_vs_model). Gate: |res| <= 1% of
the image width (52.5 px).
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bible_cam as bc  # noqa: E402

Image.MAX_IMAGE_PIXELS = None
IF = json.loads((bc.REPO / "dev/aa_team/interfaces.json").read_text(encoding="utf-8"))
W = IF["windows"]
GATE = 0.01 * bc.W


def fr(k):
    return W[k]["frame_at_reveal"]


def features():
    """name -> (p0, p1 world, orient 'v'|'h', bible edge mode, band px, group)."""
    f = {}
    for k, tag in (("left_w1_arched", "L1"), ("left_w2_cat", "L2"), ("left_w3_balcony", "L3"), ("right_w1", "R1")):
        a = fr(k)
        y = a["y"]
        z0 = W[k]["sill_z"] + 0.35
        z1 = (W[k].get("springing_z") or a["top_z"]) - 0.2
        f[f"{tag}_frame_left"] = ((a["x_left"], y, z0), (a["x_left"], y, z1), "v", "-", 28, tag)
        f[f"{tag}_frame_right"] = ((a["x_right"], y, z0), (a["x_right"], y, z1), "v", "+", 28, tag)
        if tag != "L1" and tag != "L3":
            f[f"{tag}_frame_top"] = ((a["x_left"] + 0.12, y, a["top_z"]), (a["x_right"] - 0.12, y, a["top_z"]),
                                     "h", "-", 28, tag)
    # sills: the dark cap line on the sill slab's top front edge
    slab = {"L1": ("left_w1_arched", 0.36), "L2": ("left_w2_cat", 0.28), "L3": ("left_w3_balcony", 0.45),
            "R1": ("right_w1", 0.28)}
    for tag, (k, proud) in slab.items():
        cx, s = W[k]["center_x"], W[k]["sill_z"]
        f[f"{tag}_sill"] = ((cx - 0.4, -proud, s), (cx + 0.4, -proud, s), "h", "dark", 30, tag)
    # facade edges, corner bay, arch / pier
    f["corner_arris_main"] = ((IF["facade"]["x_left_corner"], 0.0, 7.0), (IF["facade"]["x_left_corner"], 0.0, 9.5),
                              "v", "+", 40, "facade")
    rp = IF["arch"]["piers"]["right"]
    f["right_pier_arris_jamb"] = ((rp["x"][0], -rp["proud"], 1.3), (rp["x"][0], -rp["proud"], 2.5), "v", "+", 30, "arch")
    f["right_pier_outer"] = ((rp["x"][1], -rp["proud"], 1.7), (rp["x"][1], -rp["proud"], 2.6), "v", "-", 30, "arch")
    c1 = rp["capital_z"][1]
    f["right_capital_top"] = ((rp["x"][0] - 0.05, -rp["proud"] - 0.12, c1), (rp["x"][1] + 0.05, -rp["proud"] - 0.12, c1),
                              "h", "abs", 30, "arch")
    gl = IF["corner_bay"]["cornice_z"][0]
    f["gf_cornice_left_top"] = ((-4.9, -0.42, gl[1]), (-4.3, -0.42, gl[1]), "h", "abs", 30, "corner_bay")
    return f


def lum(img):
    return np.asarray(img.convert("L").filter(ImageFilter.GaussianBlur(1.5)), dtype=np.float32)


def trace(L, a, b, orient, mode, band, step=5):
    """Edge samples along the projected segment a->b (bible px) within +-band."""
    pts = []
    if orient == "v":
        for v in np.arange(min(a[1], b[1]), max(a[1], b[1]), step):
            t = (v - a[1]) / (b[1] - a[1])
            uc = a[0] + t * (b[0] - a[0])
            lo = int(round(uc - band))
            prof = L[int(v), lo:lo + 2 * band + 1]
            pts.append((v, lo + peak(prof, mode)))
    else:
        for u in np.arange(min(a[0], b[0]), max(a[0], b[0]), step):
            t = (u - a[0]) / (b[0] - a[0])
            vc = a[1] + t * (b[1] - a[1])
            lo = int(round(vc - band))
            prof = L[lo:lo + 2 * band + 1, int(u)]
            pts.append((u, lo + peak(prof, mode)))
    return np.array(pts)


def peak(prof, mode):
    if mode == "dark":
        v = -prof
    elif mode == "bright":
        v = prof
    else:
        d = np.gradient(prof)
        v = {"+": d, "-": -d, "abs": np.abs(d)}[mode]
    return float(np.argmax(v))


def robust_offset(pts, a, b, orient):
    """Median signed offset of the traced samples from the projected model line, after a 2.5-MAD clip."""
    s = pts[:, 0]
    t = (s - (a[1] if orient == "v" else a[0])) / ((b[1] - a[1]) if orient == "v" else (b[0] - a[0]))
    model = (a[0] + t * (b[0] - a[0])) if orient == "v" else (a[1] + t * (b[1] - a[1]))
    d = pts[:, 1] - model
    med = np.median(d)
    mad = max(1.4826 * np.median(np.abs(d - med)), 1.0)
    keep = np.abs(d - med) < 2.5 * mad
    return float(np.median(d[keep])), float(keep.mean()), float(np.std(d[keep]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render")
    ap.add_argument("--out")
    ap.add_argument("--debug")
    args = ap.parse_args()
    B = Image.open(bc.BIBLE).convert("RGB")
    LB = lum(B)
    LR = None
    if args.render:
        LR = lum(Image.open(args.render).convert("RGB").resize(B.size, Image.BICUBIC))
    dbg = ImageDraw.Draw(B) if args.debug else None
    rows = {}
    for name, (p0, p1, o, mode, band, grp) in features().items():
        a, b = bc.proj([p0, p1])
        res, inl, sd = robust_offset(trace(LB, a, b, o, mode, band), a, b, o)
        row = {"group": grp, "bible_vs_model_px": round(res, 1), "pct_width": round(abs(res) / bc.W * 100, 2),
               "inliers": round(inl, 2), "spread_px": round(sd, 1), "pass_1pct": abs(res) <= GATE}
        if LR is not None:
            rr, _, _ = robust_offset(trace(LR, a, b, o, "abs" if mode in ("dark", "bright") else mode, band), a, b, o)
            row["render_vs_model_px"] = round(rr, 1)
        rows[name] = row
        if dbg:
            dbg.line([tuple(a), tuple(b)], fill=(0, 255, 0), width=3)
            off = np.array([res, 0.0]) if o == "v" else np.array([0.0, res])
            dbg.line([tuple(a + off), tuple(b + off)], fill=(255, 0, 0), width=3)
    worst = max(abs(r["bible_vs_model_px"]) for r in rows.values())
    out = {"_doc": __doc__.split("\n\n")[1].replace("\n", " "), "gate_px": GATE, "worst_px": worst,
           "all_pass": all(r["pass_1pct"] for r in rows.values()), "features": rows}
    text = json.dumps(out, indent=1)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    for k, r in rows.items():
        print(f"{k:24s} {r['bible_vs_model_px']:+7.1f} px  {r['pct_width']:4.2f}%  inl {r['inliers']:.2f}"
              + (f"  render {r['render_vs_model_px']:+6.1f}" if "render_vs_model_px" in r else ""))
    print("worst", worst, "gate", GATE, "all_pass", out["all_pass"])
    if args.debug:
        B.save(args.debug)


if __name__ == "__main__":
    main()
