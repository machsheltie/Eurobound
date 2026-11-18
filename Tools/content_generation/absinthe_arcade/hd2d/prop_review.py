"""Gate C review sheet for a prop cut by cut_plate_prop.py. Writes dev/asset_team/reviews/<tag>_gate_c_sheet.jpg
(+ <tag>_game_size_{day,night}.jpg). First used for the Taproom chalice (bead Eurobound-j9ru).

python -I Tools/content_generation/absinthe_arcade/hd2d/prop_review.py <config.json> <tag> [crop_pad_px=220]
Panels: A original day (with prop) | B clean day | C prop re-composited on B | D prop on magenta (halo) |
E clean night + prop night | F clean emit | G |C - A| x4 | H float: the prop at -amp, 0, +amp over the clean plate
(only if the config's spec has a "float" block).
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageChops, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 4))
R = lambda p: os.path.join(ROOT, p)
cfg = json.load(open(R(sys.argv[1]), encoding="utf-8"))
tag = sys.argv[2]
cpad = int(sys.argv[3]) if len(sys.argv) > 3 else 220
G = R(cfg["plates_dir"]); OD = R(cfg["originals_dir"]); OUT = R("dev/asset_team/reviews")
spec = json.load(open(os.path.join(G, "props", cfg["prop_json"]), encoding="utf-8"))
x, y = spec["plate_xy"]; w, h = spec["size"]; W, H = spec["plate_size"]
CROP = (max(x - cpad, 0), max(y - cpad, 0), min(x + w + cpad, W), min(y + h + cpad, H))
plate = lambda k, clean=True: Image.open(os.path.join(G, f"{cfg['plate_base']}_{k}.png") if clean else
                                         os.path.join(OD, f"{cfg['plate_base']}_{k}_with_prop.png")).convert("RGBA")
layer = lambda k: Image.open(os.path.join(G, "props", spec["files"][k]))


def with_prop(k, dy=0):
    p = plate(k); p.alpha_composite(layer(k), (x, y + dy)); return p


orig = plate("day", clean=False)
rec = with_prop("day")
mag = Image.new("RGBA", (w, h), (255, 0, 255, 255)); mag.alpha_composite(layer("day"))
diff = ImageChops.difference(rec.convert("RGB"), orig.convert("RGB")).point(lambda v: min(255, v * 4)).convert("RGBA")
panels = [("A original day plate (with prop)", orig.crop(CROP)), ("B clean day plate", plate("day").crop(CROP)),
          ("C prop re-composited on B", rec.crop(CROP)), ("D prop day layer on magenta (halo check)", mag),
          ("E clean night + prop night layer", with_prop("night").crop(CROP)), ("F clean emit plate", plate("emit").crop(CROP)),
          ("G |C - A| x4 (black = identical)", diff.crop(CROP))]
fl = spec.get("float")
if fl:
    amp = int(fl["amplitude_plate_px"])
    strip = Image.new("RGBA", ((CROP[2] - CROP[0]) * 3, CROP[3] - CROP[1]))
    for i, dy in enumerate((-amp, 0, amp)):
        strip.paste(with_prop("night", dy).crop(CROP), (i * (CROP[2] - CROP[0]), 0))
    panels.append((f"H float at -{amp}, 0, +{amp} plate px (night), period {fl['period_seconds']} s", strip))
TW, TH = 520, 470
sheet = Image.new("RGB", (TW * 4 + 50, (TH + 30) * 2 + 10), (40, 40, 48))
d = ImageDraw.Draw(sheet)
for i, (lab, im) in enumerate(panels):
    im = im.copy(); im.thumbnail((TW, TH), Image.LANCZOS)
    px, py = 10 + (i % 4) * (TW + 10), 10 + (i // 4) * (TH + 30)
    sheet.paste(im.convert("RGB"), (px, py)); d.text((px, py + TH + 6), lab, fill=(235, 235, 235))
sheet.save(os.path.join(OUT, f"{tag}_gate_c_sheet.jpg"), quality=92)
for k in ("day", "night"):
    with_prop(k).convert("RGB").resize((1280, int(1280 * H / W)), Image.LANCZOS).save(os.path.join(OUT, f"{tag}_game_size_{k}.jpg"), quality=92)
big = Image.new("RGB", ((CROP[2] - CROP[0]) * 2 + 10, CROP[3] - CROP[1]), (40, 40, 48))
big.paste(plate("day").crop(CROP).convert("RGB"), (0, 0)); big.paste(plate("night").crop(CROP).convert("RGB"), (CROP[2] - CROP[0] + 10, 0))
big.save(os.path.join(OUT, f"{tag}_clean_full_res.jpg"), quality=92)
a = np.asarray(ImageChops.difference(rec.convert("RGB"), orig.convert("RGB")))
print("sheet written; |C-A| max", int(a.max()), "mean", round(float(a.mean()), 3))
