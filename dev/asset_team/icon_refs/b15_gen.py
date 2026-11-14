"""Batch 15 flat art generator (Pillow only). Writes the cracked_mirror_shard face art + outline.
python dev/asset_team/icon_refs/b15_gen.py <out_dir>
"""
import json, os, random, sys
from PIL import Image, ImageDraw

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
W, H, HA = 1024, 1024, 1152
PTS = [(200, 950), (150, 760), (250, 640), (230, 500), (340, 380), (380, 230), (470, 60), (520, 250), (610, 360), (590, 520),
       (690, 640), (650, 780), (540, 940), (420, 900)]
json.dump({"pts": PTS}, open(os.path.join(out, "cracked_mirror_shard_outline.json"), "w"))

random.seed(15)
SILVER, LIGHT, MID, DARK, GLINT = (176, 190, 200), (216, 226, 232), (130, 148, 160), (96, 112, 124), (244, 248, 250)
PLUM, GRIME, STEEL = (43, 26, 46), (110, 90, 60), (94, 106, 116)
im = Image.new("RGB", (W, HA), STEEL)
d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, H), fill=SILVER)
# flat diagonal reflection bands (hard edged)
for c, x0, wd in ((LIGHT, -200, 170), (MID, 60, 90), (GLINT, 250, 60), (LIGHT, 380, 200), (MID, 700, 120), (DARK, 900, 100), (GLINT, 560, 40)):
    d.polygon([(x0, H + 200), (x0 + wd, H + 200), (x0 + wd + 900, -200), (x0 + 900, -200)], fill=c)
# bold painted cracks radiating from an impact point
ox, oy = 420, 650
def crack(pts, w):
    d.line(pts, fill=PLUM, width=w, joint="curve")
for pts, w in (
    ([(ox, oy), (330, 560), (300, 430), (360, 320), (420, 200)], 14),
    ([(ox, oy), (520, 600), (600, 540), (650, 610)], 14),
    ([(ox, oy), (500, 730), (540, 850), (520, 930)], 14),
    ([(ox, oy), (330, 740), (260, 820), (230, 900)], 14),
    ([(ox, oy), (330, 650), (230, 640)], 14),
    ([(300, 430), (240, 400), (230, 350)], 9),
    ([(520, 600), (540, 500), (520, 420)], 9),
    ([(540, 850), (610, 840), (640, 800)], 9),
):
    crack(pts, w)
d.ellipse((ox - 26, oy - 26, ox + 26, oy + 26), fill=PLUM)
# flat sticky grime blotches and a coffee ring, edge-heavy
for (x, y, rx, ry) in ((230, 880, 60, 40), (590, 870, 40, 30), (450, 130, 30, 24), (650, 640, 36, 28), (270, 560, 30, 24)):
    d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=GRIME)
d.ellipse((380, 720, 480, 820), outline=GRIME, width=12)
for _ in range(14):
    x, y = random.randint(230, 600), random.randint(250, 880)
    d.ellipse((x, y, x + 14, y + 9), fill=GRIME)
# plain steel strip for back and edges (rows 1024..1152) already STEEL
im.save(os.path.join(out, "cracked_mirror_shard_face.png"))
print("WROTE shard face")
