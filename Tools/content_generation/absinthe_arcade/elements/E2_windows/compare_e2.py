"""Side-by-side compares for E2 (plain Python + Pillow): reference left, render right, same height.

  python compare_e2.py [--dir dev/aa_team/renders/E2] [--tag final]
Writes compare_<mode>_<view>.png next to the renders.
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parents[5]
REFS = {"l2": "bible_w2.png", "l1": "bible_w1.png", "l3": "bible_w3.png", "r1": "bible_r1.png",
        "r2": "sheet_r2.png", "dormer_l": "sheet_dormer_l.png", "dormer_r": "sheet_dormer_r.png",
        "side_w0": "sheet_side_w0.png", "side_w1": "sheet_side_w1.png", "side_w2": "sheet_side_w2.png",
        "dormer_side": "sheet_dormer_side.png"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(REPO / "dev/aa_team/renders/E2"))
    ap.add_argument("--tag", default="final")
    a = ap.parse_args()
    d = Path(a.dir)
    refdir = REPO / "dev/aa_team/renders/E2/ref"
    out = []
    for p in sorted(d.glob(f"{a.tag}_*_*.png")):
        _, mode, view = p.stem.split("_", 2)
        if view not in REFS:
            continue
        ref = Image.open(refdir / REFS[view]).convert("RGB")
        ren = Image.open(p).convert("RGB")
        h = max(ref.height, ren.height, 1600)
        ref = ref.resize((round(ref.width * h / ref.height), h), Image.LANCZOS)
        ren = ren.resize((round(ren.width * h / ren.height), h), Image.LANCZOS)
        gap = 16
        im = Image.new("RGB", (ref.width + gap + ren.width, h + 40), (20, 20, 20))
        im.paste(ref, (0, 40))
        im.paste(ren, (ref.width + gap, 40))
        dr = ImageDraw.Draw(im)
        dr.text((8, 12), f"reference: {REFS[view]}", fill=(230, 230, 230))
        dr.text((ref.width + gap + 8, 12), f"render: {p.name}", fill=(230, 230, 230))
        fp = d / f"compare_{a.tag}_{mode}_{view}.png" if a.tag != "final" else d / f"compare_{mode}_{view}.png"
        im.save(fp)
        out.append(str(fp))
    print("\n".join(out))


if __name__ == "__main__":
    main()
