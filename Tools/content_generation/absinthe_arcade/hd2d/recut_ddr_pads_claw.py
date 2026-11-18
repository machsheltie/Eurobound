"""Re-cut the Absinthe Arcade hall DDR pads alpha so it holds no claw-cabinet pixels (Eurobound-ssv5).

The DDR pads cut-out (aa_hall_ddr_pads_{idle,lit}_{day,night,emit}.png, footprint 324,765 442x466 on
the 2752x1536 hall plate) was cut before the claw cabinet beside it became its own sprite. Its alpha
reaches into the bottom of that cabinet (the decal panel and the cabinet face behind the third pad's
handrail), so when the pads are drawn over the separated claw they repaint old claw pixels.

This script changes ALPHA ONLY. RGB, canvas size, footprint and file names stay as they are.

    new_alpha = shared_alpha * max(1 - K, R)

shared_alpha is the tight pads outline that lit_day, idle_night, lit_night and both emit masks
already shared (SHARED_ALPHA_FROM). idle_day alone had a wide soft floor cover (70f03dae); blind
gate C round 1 failed it (not tight, touches the claw edge, states not registered), so all six
files now take the one shared outline and switching states never changes the silhouette.

K (claw region, 0..1, plate coords) = the union of every claw-cabinet sprite's alpha (all states, day,
night and emit) plus CABINET_BEHIND_RAIL, the cabinet face the claw cut-out leaves to the plate
around the handrail. R (rail) = HANDRAIL, the third pad's handrail, which stands in front of the
cabinet and stays in the pads sprite. Both polygons are rasterised at 4x and box-filtered, so the
new edge is a 1 px anti-aliased line. Outside K the shared outline is untouched.

Sources are read from git so re-running is deterministic and never compounds:
  --pads-rev   commit holding the original pads (default 70f03dae, the last pads commit)
  --claw-rev   commit holding the claw cabinet sprites (default 1b35196d, Eurobound-fbqk 3.1a r3)

Usage (from the repo root):
  python -I Tools/content_generation/absinthe_arcade/hd2d/recut_ddr_pads_claw.py [--out DIR] [--check]
"""
import argparse
import io
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

PROPS = "game/assets/worlds/debaucheryville/absinthe_arcade/interior/hall/props"
PADS_JSON = f"{PROPS}/aa_hall_ddr.json"
PAD_FILES = [f"aa_hall_ddr_pads_{s}_{v}.png" for s in ("idle", "lit") for v in ("day", "night", "emit")]
SHARED_ALPHA_FROM = "aa_hall_ddr_pads_lit_day.png"
CLAW_JSONS = ["aa_cab_claw_beanie.json", "aa_cab_claw_rigged.json"]
PLATE = (2752, 1536)
SS = 4  # supersampling for the polygon edges

# Plate pixel coordinates (x, y), traced from the pads sprite and the pre-split hall plate.
# Cabinet face and claw foot behind the third pad's handrail that the claw sprite leaves to the
# plate. Right of the tube it stops at the claw sprite's side strip (y 815). Its bottom edge is the
# third (far) pad's back-rim highlight, y 848 at x 685 rising to y 853 at x 735 (gate C round 2):
# everything above that rim lies behind the pad; the rim and the deck stay in the pads sprite.
CABINET_BEHIND_RAIL = [(680, 750), (753, 750), (753, 815), (737, 815), (737, 853.2), (682, 847.7)]
# Sprite-local pixels (x, y) of background pinholes in the first (near) pad's handrail arch, joined
# to the arch's open interior (gate C round 2 note).
NEAR_ARCH_PINHOLES = [(149, 256), (150, 256), (149, 257), (150, 257), (149, 258), (150, 258),
                      (148, 258), (149, 259), (150, 259), (148, 259)]
# Third pad's handrail: left tube, arch, right tube (outer edge clockwise, then inner edge back).
HANDRAIL = [
    (687, 880), (687, 796), (688.5, 790), (691, 785), (694, 780), (698, 775), (703, 770),
    (707, 767), (710, 765.5), (722, 765.5), (726, 767), (729, 770), (730.5, 774), (731, 780),
    (731, 880),
    (720, 880), (720, 781), (716, 779), (710, 781), (705, 784.5), (701.5, 788), (699.5, 792),
    (699.5, 880),
]


def git_png(rev: str, path: str) -> Image.Image:
    data = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(data))


def git_json(rev: str, path: str) -> dict:
    data = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, check=True).stdout
    return json.loads(data)


def poly_mask(points: list) -> np.ndarray:
    """Anti-aliased 0..1 mask of a polygon on the plate."""
    big = Image.new("L", (PLATE[0] * SS, PLATE[1] * SS), 0)
    ImageDraw.Draw(big).polygon([(x * SS, y * SS) for x, y in points], fill=255)
    return np.asarray(big.reduce(SS), np.float32) / 255


def claw_region(claw_rev: str) -> np.ndarray:
    k = np.zeros(PLATE[::-1], np.float32)
    for name in CLAW_JSONS:
        spec = git_json(claw_rev, f"{PROPS}/{name}")
        for fname, s in spec["sprites"].items():
            a = np.asarray(git_png(claw_rev, f"{PROPS}/{fname}").convert("RGBA"))[..., 3] / 255.0
            sl = (slice(s["y"], s["y"] + s["h"]), slice(s["x"], s["x"] + s["w"]))
            k[sl] = np.maximum(k[sl], a)
    return np.maximum(k, poly_mask(CABINET_BEHIND_RAIL))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pads-rev", default="70f03dae")
    ap.add_argument("--claw-rev", default="1b35196d")
    ap.add_argument("--out", default=PROPS)
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    a = ap.parse_args()

    k = claw_region(a.claw_rev)
    rail = poly_mask(HANDRAIL)
    keep = np.maximum(1.0 - k, rail)
    spec = git_json(a.pads_rev, PADS_JSON)["sprites"]
    shared = np.asarray(git_png(a.pads_rev, f"{PROPS}/{SHARED_ALPHA_FROM}").convert("RGBA"))[..., 3]
    out = Path(a.out)
    for fname in PAD_FILES:
        s = spec[fname]
        im = git_png(a.pads_rev, f"{PROPS}/{fname}").convert("RGBA")
        assert im.size == (s["w"], s["h"]) == shared.shape[::-1], (fname, im.size)
        px = np.asarray(im).copy()
        sl = (slice(s["y"], s["y"] + s["h"]), slice(s["x"], s["x"] + s["w"]))
        old = shared.astype(np.float32)
        new = np.round(old * keep[sl]).astype(np.uint8)
        # Claw pixels left: alpha the pads still hold where K is fully set and R is not.
        leftover = int(((new > 0) & (k[sl] >= 0.999) & (rail[sl] == 0)).sum())
        print(f"{fname}: alpha changed {int((new != px[..., 3]).sum())} px, "
              f"nonzero {int((px[..., 3] > 0).sum())} -> {int((new > 0).sum())}, claw leftovers {leftover}")
        if not a.check:
            for x, y in NEAR_ARCH_PINHOLES:
                new[y, x] = 0
            px[..., 3] = new
            out.mkdir(parents=True, exist_ok=True)
            Image.fromarray(px, "RGBA").save(out / fname, optimize=True)


if __name__ == "__main__":
    main()
