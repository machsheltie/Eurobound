"""Gate C review sheet for the restroom statue cut-out (bead Eurobound-pg9a). Writes dev/asset_team/reviews/pg9a_*.jpg.

python -I Tools/content_generation/absinthe_arcade/hd2d/restroom_statue_review.py
Panels: original day plate | clean day plate | statue re-composited on the clean plate (should match the original) |
statue layer on magenta (halo check) | clean night + statue | clean emit | |recomposite - original| x4 |
Jakub's layering (statue node, then Jakub, then the hand cut-outs) is checked in the Godot scene, not here: he is
placed in world units (absinthe_arcade_restroom_hd2d.gd JAKUB_AT), so a plate-pixel mock would mislead.
"""
import json, os
import numpy as np
from PIL import Image, ImageDraw, ImageChops

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 4))
G = os.path.join(ROOT, "game/assets/worlds/debaucheryville/absinthe_arcade/interior/restroom")
REF = os.path.join(ROOT, "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Interior/plates_with_statue")
OUT = os.path.join(ROOT, "dev/asset_team/reviews")
spec = json.load(open(os.path.join(G, "props/statue.json")))
hands = json.load(open(os.path.join(G, "props/statue_hands.json")))
xy = tuple(spec["plate_xy"])
CROP = (850, 0, 1900, 950)


def plate(k, clean=True):
    return Image.open(os.path.join(G if clean else REF, f"aa_int_restroom_{k}.png" if clean else f"aa_int_restroom_{k}_with_statue.png")).convert("RGBA")


def with_statue(k):
    p = plate(k)
    p.alpha_composite(Image.open(os.path.join(G, "props", spec["files"][k])), xy)
    return p


panels = []
orig_day = plate("day", clean=False)
panels.append(("A original day plate (with statue)", orig_day.crop(CROP)))
panels.append(("B clean day plate (statue removed)", plate("day").crop(CROP)))
rec = with_statue("day")
panels.append(("C statue layer re-composited on B", rec.crop(CROP)))
mag = Image.new("RGBA", (spec["size"][0], spec["size"][1]), (255, 0, 255, 255))
mag.alpha_composite(Image.open(os.path.join(G, "props", spec["files"]["day"])))
panels.append(("D statue day layer on magenta (halo check)", mag))
panels.append(("E clean night plate + statue night layer", with_statue("night").crop(CROP)))
panels.append(("F clean emit plate", plate("emit").crop(CROP)))
diff = ImageChops.difference(rec.convert("RGB"), orig_day.convert("RGB")).point(lambda v: min(255, v * 4))
panels.append(("G |C - A| x4 (black = identical)", diff.crop(CROP).convert("RGBA")))
TW, TH = 520, 470
sheet = Image.new("RGB", (TW * 4 + 50, (TH + 30) * 2 + 10), (40, 40, 48))  # 7 panels
d = ImageDraw.Draw(sheet)
for i, (lab, im) in enumerate(panels):
    im = im.copy(); im.thumbnail((TW, TH), Image.LANCZOS)
    x, y = 10 + (i % 4) * (TW + 10), 10 + (i // 4) * (TH + 30)
    sheet.paste(im.convert("RGB"), (x, y))
    d.text((x, y + TH + 6), lab, fill=(235, 235, 235))
sheet.save(os.path.join(OUT, "pg9a_gate_c_sheet.jpg"), quality=92)
game = with_statue("night").convert("RGB").resize((1280, 714), Image.LANCZOS)
game.save(os.path.join(OUT, "pg9a_game_size_night.jpg"), quality=92)
with_statue("day").convert("RGB").resize((1280, 714), Image.LANCZOS).save(os.path.join(OUT, "pg9a_game_size_day.jpg"), quality=92)
big = Image.new("RGB", (1050 * 2 + 10, 950), (40, 40, 48))
big.paste(plate("day").crop(CROP).convert("RGB"), (0, 0)); big.paste(plate("night").crop(CROP).convert("RGB"), (1060, 0))
big.save(os.path.join(OUT, "pg9a_clean_niche_full_res.jpg"), quality=92)
print("max |C-A| inside plate:", int(np.asarray(ImageChops.difference(rec.convert("RGB"), orig_day.convert("RGB"))).max()),
      "mean:", round(float(np.asarray(ImageChops.difference(rec.convert("RGB"), orig_day.convert("RGB"))).mean()), 3))
