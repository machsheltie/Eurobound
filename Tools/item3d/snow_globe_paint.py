"""Flat painted art for Tools/item3d/snow_globe.py (Pillow only, lettering typed from the item doc, no image tool).
python Tools/item3d/snow_globe_paint.py <out.png>
Layout (2048 wide): base wall cyl rect (0,0,2048,340) z 0..0.36 ; dome shell cyl rect (0,340,2048,910) z 0.35..0.92.
Front of the model faces final angle -118 deg, back +62 deg (u = (angle + 180) / 360).
"""
import random, sys
from PIL import Image, ImageDraw, ImageFont

W, HB, HS = 2048, 340, 570
random.seed(7)
FRONT, BACK = -118.0, 62.0


def hx(s):
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


TAN, TAN_D, TAN_L = hx("A08C6E"), hx("8B7355"), hx("B8A586")
GOLD, GOLD_W, BROWN = hx("CFB53B"), hx("B8912F"), hx("4A3B2C")
BAND = hx("6B5A44")
AQUA, GLASS, HAZE = hx("AECFC9"), hx("CFE3E2"), hx("C3DCD8")
SEAM, MURK = hx("93B8B3"), hx("9DC2BC")
im = Image.new("RGB", (W, HB + HS), TAN)
d = ImageDraw.Draw(im)


def px(a):
    return ((a + 180.0) % 360.0) / 360.0 * W


def zy(z):   # base wall rect: z 0..0.36 -> y 340..0
    return HB - z / 0.36 * HB


# ---------------- base wall
d.rectangle((0, int(zy(0.05)), W, HB), fill=TAN_D)                     # stepped foot, darker stone
d.rectangle((0, 0, W, int(zy(0.30))), fill=TAN_L)                      # top lip
d.rectangle((0, int(zy(0.30)), W, int(zy(0.05))), fill=TAN)
BY0, BY1 = int(zy(0.155)), int(zy(0.065))                                # banner band around the foot
d.rectangle((0, BY0, W, BY1), fill=BAND)
for y in (BY0, BY1 - 5):                                                 # dry-brushed gold rules, broken
    x = 0
    while x < W:
        w = random.randint(40, 140)
        if random.random() < 0.7:
            d.rectangle((x, y, x + w, y + 5), fill=GOLD)
        x += w + random.randint(10, 40)
cx = px(FRONT)
SY0, SY1 = int(zy(0.295)), int(zy(0.17))                                 # the tiny square scene, front face
d.rectangle((cx - 150, SY0, cx + 150, SY1), fill=TAN_D)
d.rectangle((cx - 142, SY0 + 8, cx + 142, SY1 - 8), fill=hx("9A8668"))
bump = hx("7A6A52")
for i in range(6):                                                       # six faceless tourist bumps, raised phone rects
    x = cx - 115 + i * 46 + random.randint(-5, 5)
    y = SY1 - 14 - random.randint(0, 8)
    r = random.randint(15, 19)
    d.ellipse((x - r, y - r - 18, x + r, y + r + 6), fill=bump)
    d.ellipse((x - 9, y - r - 32, x + 9, y - r - 14), fill=bump)
    d.rectangle((x + 4, y - r - 14, x + 16, y - r + 4), fill=hx("D8CCB2"))
for _ in range(30):                                                      # gold only catches the high points
    x, y = cx + random.randint(-135, 135), random.randint(SY0 + 14, SY1 - 10)
    d.ellipse((x, y, x + 6, y + 4), fill=GOLD_W)


def fit(text, maxw, maxh, path="C:/Windows/Fonts/impact.ttf"):
    s = maxh
    while s > 8:
        f = ImageFont.truetype(path, s)
        if f.getlength(text) <= maxw:
            return f
        s -= 1
    return ImageFont.truetype(path, 8)


def lettering(cxp, lines):
    n = len(lines)
    h = (BY1 - BY0 - 14) // n
    for i, t in enumerate(lines):
        f = fit(t, 308, h)
        w = f.getlength(t)
        y = BY0 + 7 + i * h
        for dx, dy, c in ((3, 3, BROWN), (0, 0, GOLD)):
            d.text((cxp - w / 2 + dx, y + dy), t, font=f, fill=c)
    for _ in range(22):                                                  # worn-off specks over the letters
        x, y = cxp + random.randint(-150, 150), random.randint(BY0 + 8, BY1 - 8)
        d.ellipse((x, y, x + 6, y + 5), fill=BAND)


lettering(px(FRONT), ["ASTRONOMICAL", "COCK-UP"])
lettering(px(BACK), ["DEBAUCHERYVILLE"])
for a in (FRONT + 60, FRONT - 60, FRONT + 120, FRONT - 120):             # soft lumpy relief on the other faces
    for _ in range(5):
        x, y = px(a) + random.randint(-120, 120), random.randint(int(zy(0.29)), int(zy(0.17)))
        r = random.randint(8, 16)
        d.ellipse((x - r, y - r, x + r, y + r), fill=TAN_D if random.random() < .7 else TAN_L)

# ---------------- dome shell (z 0.35 bottom .. 0.92 top): murky aqua, water cast
Y0 = HB
d.rectangle((0, Y0, W, Y0 + HS), fill=AQUA)
d.rectangle((0, Y0 + HS - 62, W, Y0 + HS), fill=GLASS)                  # faint blue-green rim cast
d.rectangle((0, Y0, W, Y0 + 34), fill=GLASS)                            # top cap
for _ in range(26):                                                      # murk blotches
    x, y = random.randint(0, W), random.randint(Y0 + 60, Y0 + HS - 90)
    rx, ry = random.randint(40, 120), random.randint(20, 50)
    d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=MURK)
fx, fy = px(BACK + 70), Y0 + 330                                        # greasy fingerprint haze, one side
d.ellipse((fx - 130, fy - 110, fx + 130, fy + 110), fill=HAZE)
for k in (90, 60, 30):
    d.arc((fx - k, fy - k * 0.8, fx + k, fy + k * 0.8), 190, 350, fill=GLASS, width=9)
sx = px(BACK - 28)                                                       # vertical blown-glass seam
d.rectangle((sx, Y0 + 40, sx + 7, Y0 + HS - 70), fill=SEAM)
gx, gy = px(BACK + 20), Y0 + 410                                        # crescent scratch
d.arc((gx - 90, gy - 90, gx + 90, gy + 90), 200, 290, fill=hx("E8F3F2"), width=8)
im.save(sys.argv[1])
print("PAINT", sys.argv[1], im.size)
