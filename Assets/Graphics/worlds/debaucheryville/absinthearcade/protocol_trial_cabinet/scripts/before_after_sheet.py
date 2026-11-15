"""Before/after sheet (<= 1600 px wide): reference | before (Tripo raw mesh, its own texture) | after neutral | after game light, front row + side row (+ back row for after).
python before_after_sheet.py <package dir> <out.jpg>"""
import sys
from PIL import Image, ImageDraw
PK, OUT = sys.argv[1], sys.argv[2]
H = 470
def get(p, bg=(70, 70, 74)):
    im = Image.open(p).convert("RGBA"); s = H / im.height; im = im.resize((max(1, int(im.width * s)), H), Image.LANCZOS)
    b = Image.new("RGB", im.size, bg); b.paste(im, (0, 0), im); return b
rows = [
    ("FRONT", [f"{PK}/source_references/aa_prop_cabinet_front_day.png", f"{PK}/renders/before_tripo_raw_front.png", f"{PK}/renders/cabinet_neutral_front.png", f"{PK}/renders/cabinet_game_front.png", f"{PK}/renders/cabinet_neutral_back.png"]),
    ("SIDE", [f"{PK}/source_references/aa_prop_cabinet_side_day.png", f"{PK}/renders/before_tripo_raw_right.png", f"{PK}/renders/cabinet_neutral_right.png", f"{PK}/renders/cabinet_game_right.png", f"{PK}/renders/before_tripo_raw_back.png"]),
]
heads = ["REFERENCE (approved)", "BEFORE: Tripo raw", "AFTER: neutral light", "AFTER: game light", "back / extra (see row)"]
cells = [[get(p) for p in r[1]] for r in rows]
# Phase B: extra row for the -X flank (new approved art, seen from -X | the first pass copied the +X art mirrored | after neutral | after game | after back)
LEFT = [f"{PK}/source_references/aa_prop_cabinet_side_other_mirror_day.png", f"{PK}/source_references/aa_prop_cabinet_side_mirrored_before.png", f"{PK}/renders/cabinet_neutral_left.png", f"{PK}/renders/cabinet_game_left.png", f"{PK}/renders/cabinet_game_back.png"]
rows.append(("LEFT (-X)", LEFT)); cells.append([get(p) for p in LEFT])
# column widths = max of the two rows
cw = [max(c[i].width for c in cells) for i in range(5)]
# the 5th column: after-back on top row, before-back on bottom row (back is unseen in the reference)
gap = 6; top = 22
W = sum(cw) + gap * 6
if W > 1600:
    sc = 1600 / W
    cells = [[c.resize((int(c.width * sc), int(c.height * sc))) for c in r] for r in cells]
    cw = [int(w * sc) for w in cw]; W = sum(cw) + gap * 6; hh = cells[0][0].height
else:
    hh = H
sheet = Image.new("RGB", (W, top + len(cells) * (hh + gap) + 2), (32, 32, 36)); d = ImageDraw.Draw(sheet)
x = gap
for i in range(5):
    d.text((x, 5), heads[i], fill=(235, 235, 235))
    for r in range(len(cells)):
        sheet.paste(cells[r][i], (x, top + r * (hh + gap)))
    x += cw[i] + gap
sheet.convert("RGB").save(OUT, quality=88)
print(sheet.size)
