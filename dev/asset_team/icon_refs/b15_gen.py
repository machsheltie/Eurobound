"""Batch 15 flat art generator (Pillow only, no image tool). Round 2.
python dev/asset_team/icon_refs/b15_gen.py <out_dir>
Writes: cracked_mirror_shard_face.png + _outline.json, absinthe_shot_paint.png, item_tan_line_neon_shooter_paint.png, glowstick_nunchucks_paint.png
All flat colour, bold shapes. Layouts match Tools/item3d/lathe_item.py, shard_slab.py and chain_item.py.
"""
import json, os, random, sys
from PIL import Image, ImageDraw

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
random.seed(15)
PLUM = (43, 26, 46)
GRIME = (110, 90, 60)


def hx(s):
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def drip(d, x, y0, y1, w, c):
    d.rectangle((x - w // 2, y0, x + w // 2, y1), fill=c)
    d.ellipse((x - w // 2, y1 - w // 2, x + w // 2, y1 + w // 2), fill=c)


# ------------------------------------------------------------------ cracked mirror shard
W, H, HA = 1024, 1024, 1152
PTS = [(200, 950), (150, 760), (250, 640), (230, 500), (340, 380), (380, 230), (470, 60), (520, 250), (610, 360), (590, 520),
       (690, 640), (650, 780), (540, 940), (420, 900)]
json.dump({"pts": PTS}, open(os.path.join(out, "cracked_mirror_shard_outline.json"), "w"))
SILVER, LIGHT, MID, DARK, WHITE = (196, 210, 222), (224, 234, 242), (150, 170, 186), (112, 132, 148), (255, 255, 255)
STEEL = (94, 106, 116)
im = Image.new("RGB", (W, HA), STEEL)
d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, H), fill=SILVER)
for c, x0, wd in ((LIGHT, -250, 190), (MID, 20, 80), (WHITE, 300, 130), (LIGHT, 470, 140), (MID, 700, 110), (DARK, 880, 90)):
    d.polygon([(x0, H + 200), (x0 + wd, H + 200), (x0 + wd + 900, -200), (x0 + 900, -200)], fill=c)
d.polygon([(400, 1024), (1024, 300), (1024, 1024)], fill=(240, 176, 112))      # warm reflected colour, lower-right corner
d.polygon([(340, 1024), (390, 1024), (1024, 270), (1024, 220)], fill=(252, 222, 176))
ox, oy = 420, 650
for pts, w in (
    ([(ox, oy), (330, 560), (300, 430), (360, 320), (420, 200)], 28),
    ([(ox, oy), (520, 600), (600, 540), (650, 610)], 28),
    ([(ox, oy), (500, 730), (540, 850), (520, 930)], 28),
    ([(ox, oy), (330, 740), (260, 820), (230, 900)], 28),
    ([(ox, oy), (330, 650), (230, 640)], 28),
    ([(300, 430), (240, 400), (230, 350)], 20),
    ([(520, 600), (540, 500), (520, 420)], 20),
    ([(540, 850), (610, 840), (640, 800)], 20),
):
    d.line(pts, fill=PLUM, width=w, joint="curve")
    for p in pts:
        d.ellipse((p[0] - w // 2, p[1] - w // 2, p[0] + w // 2, p[1] + w // 2), fill=PLUM)
d.ellipse((ox - 40, oy - 40, ox + 40, oy + 40), fill=PLUM)
for (x, y, rx, ry) in ((230, 880, 60, 40), (590, 880, 44, 30), (450, 140, 34, 26)):          # edge grime, flat
    d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=GRIME)
fx, fy = 300, 560                                                                          # grimy fingerprint smudge, flat area
d.ellipse((fx - 85, fy - 110, fx + 85, fy + 110), fill=(150, 138, 112))
for k in (70, 45, 20):
    d.arc((fx - k, fy - k * 1.3, fx + k, fy + k * 1.3), 200, 340, fill=(112, 100, 80), width=12)
d.rectangle((0, 1024, W, HA), fill=STEEL)
im.save(os.path.join(out, "cracked_mirror_shard_face.png"))


# ------------------------------------------------------------------ glass tile (cyl), front of glass at x about 0.17 * 1024 = 175
def glass_tile(d, ox_, oy_, z_top, fill_z, floor_z, body, upper, base, rings, drips, prints, scuffs, residue):
    tw, th = 1024, 512
    py = lambda z: oy_ + th * (1 - z / z_top)
    d.rectangle((ox_, oy_, ox_ + tw, oy_ + th), fill=upper)
    d.rectangle((ox_, py(fill_z), ox_ + tw, py(floor_z - 0.0)), fill=body)
    d.rectangle((ox_, py(floor_z), ox_ + tw, oy_ + th), fill=base)
    return py


# absinthe: PH 1280. glass tile at (0,0), coaster at (0,512,512,1024), flame (512,512,768,768), spoon (0,1024,1024,1279)
im = Image.new("RGB", (1024, 1280), (200, 200, 200))
d = ImageDraw.Draw(im)
TOP = 0.574
py = glass_tile(d, 0, 0, TOP, 0.42, 0.03, hx("6EE81E"), hx("C4D8DC"), hx("8EA4A8"), 0, 0, 0, 0, 0)
d.rectangle((0, py(0.42), 1024, py(0.42) + 10), fill=hx("3A9E0A"))                          # fill line
for x, y1, w in ((95, 330, 30), (160, 400, 34), (230, 300, 28), (300, 380, 32)):            # caramel drips down the glass
    drip(d, x, 0, y1, w, hx("A87C3A"))
for (x, y, rx, ry) in ((130, 250, 46, 62), (215, 330, 50, 66), (290, 230, 44, 60)):         # greasy thumbprint smudges
    d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=hx("DCEAE6"))
    d.ellipse((x - rx // 2, y - ry // 2, x + rx // 2, y + ry // 2), fill=hx("B4FF7E"))
d.polygon([(360, 470), (420, 470), (440, 512), (380, 512)], fill=hx("3A9E0A"))               # sticky green at the base
# coaster (planar -0.52..0.52 over 512 px)
cx = lambda v: (v / 1.04 + 0.5) * 512
cy = lambda v: 512 + (0.5 - v / 1.04) * 512
d.rectangle((0, 512, 512, 1024), fill=hx("E8E4D8"))
for r0, r1, c in ((0.27, 0.37, "3A9E0A"), (0.43, 0.485, "7E6244")):
    d.ellipse((cx(-r1), cy(r1), cx(r1), cy(-r1)), fill=hx(c))
    d.ellipse((cx(-r0), cy(r0), cx(r0), cy(-r0)), fill=hx("E8E4D8") if c == "7E6244" else hx("3A9E0A"))
d.ellipse((cx(-0.27), cy(0.27), cx(0.27), cy(-0.27)), fill=hx("E8E4D8"))
d.ellipse((cx(0.1), cy(-0.22), cx(0.36), cy(-0.36)), fill=hx("A87C3A"))
d.ellipse((cx(-0.46), cy(0.08), cx(-0.3), cy(-0.1)), fill=hx("B8B2A2"))
# flame bands by height (z-banded rect 512..768)
d.rectangle((512, 512, 768, 768), fill=hx("F8E86E"))
d.rectangle((512, 512 + 256 * 0.40, 768, 768), fill=hx("F0A418"))
d.rectangle((512, 512 + 256 * 0.74, 768, 768), fill=hx("3E7EE8"))
# spoon: tarnished dull silver, dark patches (planar x -0.45..0.45, y -0.08..0.08 over 1024 x 255)
d.rectangle((0, 1024, 1024, 1279), fill=hx("9AA3A6"))
for (x, y, rx, ry) in ((120, 1100, 90, 50), (420, 1200, 70, 40), (640, 1090, 80, 46), (900, 1190, 100, 52), (30, 1220, 60, 40)):
    d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=hx("5E5A52"))
d.rectangle((0, 1024, 1024, 1050), fill=hx("C2C8CA"))
im.save(os.path.join(out, "absinthe_shot_paint.png"))

# ------------------------------------------------------------------ neon shooter (1024 x 512, z 0..0.914)
im = Image.new("RGB", (1024, 512), (200, 200, 200))
d = ImageDraw.Draw(im)
TOP = 0.914
py = glass_tile(d, 0, 0, TOP, 0.74, 0.30, hx("5B2BFF"), hx("C4D8DC"), hx("8EA4A8"), 0, 0, 0, 0, 0)
RES = hx("2E1580")
for yy in (py(0.74) + 4, py(0.52), py(0.36)):                                                # sticky residue rings
    d.rectangle((0, yy, 1024, yy + 22), fill=hx("3A1AA8"))
drip(d, 150, 0, 250, 34, RES)                                                                # a drip from the rim
drip(d, 230, py(0.74), py(0.74) + 130, 26, RES)
for (x, y, rx, ry) in ((120, 470, 70, 24), (250, 440, 56, 20)):                              # scuffed base
    d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=hx("5E6A74"))
for x0 in (60, 170, 290, 380):
    d.polygon([(x0, 495), (x0 + 50, 440), (x0 + 74, 440), (x0 + 24, 495)], fill=hx("E6F0EE"))
d.rectangle((0, 505, 1024, 512), fill=hx("5E6A74"))
im.save(os.path.join(out, "item_tan_line_neon_shooter_paint.png"))

# ------------------------------------------------------------------ nunchucks (1024 x 1280; stick tiles 1024 x 640, axis mapping, front at x 512)
im = Image.new("RGB", (1024, 1280), (200, 200, 200))
d = ImageDraw.Draw(im)


def stick_tile(oy_, base, core, dark, tape, crack):
    d.rectangle((0, oy_, 1024, oy_ + 640), fill=hx(base))
    d.rectangle((486, oy_ + 30, 546, oy_ + 600), fill=hx(core))                              # lighter core stripe
    if dark:
        d.rectangle((0, oy_ + 160, 1024, oy_ + 300), fill=hx(dark))                          # darker pooled section
    if tape:
        d.rectangle((0, oy_ + 490, 1024, oy_ + 585), fill=hx("1A1A1E"))
    if crack:
        pts = [(330, oy_ + 345), (400, oy_ + 310), (450, oy_ + 350), (510, oy_ + 305), (570, oy_ + 345), (630, oy_ + 310), (700, oy_ + 340)]
        d.line(pts, fill=hx("1A1A1E"), width=22, joint="curve")
        for p in pts:
            d.ellipse((p[0] - 11, p[1] - 11, p[0] + 11, p[1] + 11), fill=hx("1A1A1E"))
    for (x, y, rx, ry) in ((380, 130, 40, 26), (640, 400, 46, 28), (700, 90, 34, 22), (330, 450, 38, 24)):     # scuffed plastic
        d.ellipse((x - rx, oy_ + y - ry, x + rx, oy_ + y + ry), fill=hx("8E9298"))
    for (x, y, rx, ry) in ((420, 570, 60, 34), (610, 40, 70, 30), (350, 250, 40, 40)):                          # grime
        d.ellipse((x - rx, oy_ + y - ry, x + rx, oy_ + y + ry), fill=hx("5E5A3A"))


stick_tile(0, "7EF018", "C4FF8E", None, True, False)
stick_tile(640, "F018A8", "FF8ED8", "9E0A66", False, True)
im.save(os.path.join(out, "glowstick_nunchucks_paint.png"))
print("WROTE all b15 art")
