"""Batch 14 flat face art (pure Pillow, 0 credits): trivia_champ_badge, already_spent_credit, mango_og_gushers.
python dev/asset_team/icon_refs/b14_gen.py   (run from repo root)"""
import math, random
from PIL import Image, ImageDraw, ImageFont, ImageChops
F = "C:/Windows/Fonts/"
GREY = (214, 214, 216)
OUT = "dev/asset_team/icon_refs/"


def font(n, s):
    return ImageFont.truetype(F + n, s)


def stains(d, rnd, box, n, cols, rmin, rmax):
    for _ in range(n):
        x = rnd.randint(box[0], box[2]); y = rnd.randint(box[1], box[3]); r = rnd.randint(rmin, rmax)
        c = rnd.choice(cols)
        pts = [(x + math.cos(a) * r * rnd.uniform(.6, 1.2), y + math.sin(a) * r * rnd.uniform(.6, 1.2))
               for a in [i * math.pi / 6 for i in range(12)]]
        d.polygon(pts, fill=c)


def arc_text(img, text, cx, cy, rad, span_deg, fnt, fill, center_deg=-90):
    """upright-outward text along a circle, centred at center_deg (screen degrees, -90 = top), reading clockwise."""
    n = len(text); step = span_deg / max(n - 1, 1)
    start = center_deg - span_deg / 2
    for i, ch in enumerate(text):
        a = start + i * step
        w, h = 160, 160
        t = Image.new("RGBA", (w, h), (0, 0, 0, 0)); td = ImageDraw.Draw(t)
        td.text((w / 2, h / 2), ch, font=fnt, fill=fill, anchor="mm")
        t = t.rotate(-(a + 90), resample=Image.BICUBIC)
        px = cx + rad * math.cos(math.radians(a)); py = cy + rad * math.sin(math.radians(a))
        img.alpha_composite(t, (int(px - w / 2), int(py - h / 2)))


def margins(path):
    im = Image.open(path).convert("RGB"); w, h = im.size
    bg = Image.new("RGB", im.size, im.getpixel((2, 2)))
    bb = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 24 else 0).getbbox()
    return [round(100 * v, 1) for v in (bb[0] / w, (w - bb[2]) / w, bb[1] / h, (h - bb[3]) / h)]


# ---- trivia_champ_badge: gold-painted gray plastic five-point sheriff star
def badge():
    S = 1280; rnd = random.Random(14)
    img = Image.new("RGBA", (S, S), GREY + (255,)); d = ImageDraw.Draw(img)
    cx, cy = S / 2, S / 2 + 16; R = 470; r_in = R * 0.58

    def star(R_, rin, rot=-90):
        pts = []
        for i in range(10):
            a = math.radians(rot + i * 36); rr = R_ if i % 2 == 0 else rin
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
        return pts
    GOLD = (222, 168, 28); GOLD_D = (160, 108, 14); GOLD_L = (244, 206, 86); PLASTIC = (122, 122, 126)
    d.polygon(star(R, r_in), fill=GOLD_D)
    d.polygon(star(R - 22, r_in - 12), fill=GOLD)
    d.polygon(star(R - 62, r_in - 34), fill=GOLD_L)
    for i in range(5):
        a = math.radians(-90 + i * 72); tx, ty = cx + (R - 6) * math.cos(a), cy + (R - 6) * math.sin(a)
        d.ellipse((tx - 34, ty - 34, tx + 34, ty + 34), fill=GOLD_D)
        d.ellipse((tx - 25, ty - 25, tx + 25, ty + 25), fill=GOLD)
        px, py = cx + (R - 50) * math.cos(a), cy + (R - 50) * math.sin(a)
        d.ellipse((px - 20, py - 14, px + 20, py + 14), fill=PLASTIC)   # paint already thin at the points on Day 1
    rc = 232
    d.ellipse((cx - rc, cy - rc, cx + rc, cy + rc), fill=GOLD_D)
    d.ellipse((cx - rc + 14, cy - rc + 14, cx + rc - 14, cy + rc - 14), fill=GOLD)
    d.ellipse((cx - 130, cy - 130, cx + 130, cy + 130), fill=GOLD_L)
    for k, ang in enumerate((-90, -18, 54, 126, 198)):   # grime only on the arms, never near the text ring
        a = math.radians(ang + (7 if k % 2 else -7)); sx, sy = cx + 330 * math.cos(a), cy + 330 * math.sin(a)
        d.ellipse((sx - 22, sy - 16, sx + 22, sy + 16), fill=[(112, 78, 22), (138, 96, 24), (96, 70, 30)][k % 3])
    d.ellipse((cx + 200, cy + 300, cx + 250, cy + 335), fill=(150, 96, 22))
    txt = "SUMMER VACATION TRIVIA CHAMP 2003"
    big = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    arc_text(big, txt, cx, cy, 182, 322, font("ariblk.ttf", 31), (252, 250, 240, 255), center_deg=-90)
    img.alpha_composite(big)
    d2 = ImageDraw.Draw(img)
    for _ in range(90):
        x = rnd.randint(int(cx - 330), int(cx + 330)); y = rnd.randint(int(cy - 330), int(cy + 330))
        if 290 < math.hypot(x - cx, y - cy) < 440 and img.getpixel((x, y))[:3] != GREY and img.getpixel((x + 4, y + 4))[:3] != GREY:
            d2.rectangle((x, y, x + 4, y + 4), fill=rnd.choice([(255, 236, 140, 255), (190, 130, 20, 255)]))
    img.convert("RGB").save(OUT + "trivia_champ_badge_ref.png")
    return OUT + "trivia_champ_badge_ref.png"


# ---- already_spent_credit: round arcade token stamped CREDIT 00
def token():
    S = 1280; rnd = random.Random(15)
    img = Image.new("RGBA", (S, S), GREY + (255,)); d = ImageDraw.Draw(img)
    cx = cy = S / 2; R = 490
    BR = (176, 140, 58); BR_D = (104, 78, 28); BR_L = (206, 172, 84)
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=BR_D)
    d.ellipse((cx - R + 26, cy - R + 26, cx + R - 26, cy + R - 26), fill=BR_L)
    d.ellipse((cx - R + 80, cy - R + 80, cx + R - 80, cy + R - 80), fill=BR_D)
    d.ellipse((cx - R + 100, cy - R + 100, cx + R - 100, cy + R - 100), fill=BR)
    for i in range(48):
        a = math.radians(i * 7.5); x0, y0 = cx + (R - 14) * math.cos(a), cy + (R - 14) * math.sin(a)
        d.ellipse((x0 - 6, y0 - 6, x0 + 6, y0 + 6), fill=BR_D)
    inner = (int(cx - 330), int(cy - 330), int(cx + 330), int(cy + 330))
    stains(d, rnd, inner, 8, [(96, 120, 84), (112, 132, 96)], 20, 46)
    stains(d, rnd, inner, 8, [(122, 92, 34), (90, 70, 38)], 18, 44)
    d.polygon([(cx - 380, cy + 240), (cx - 300, cy + 220), (cx + 20, cy + 318), (cx - 40, cy + 340)], fill=BR_D)
    INK = (70, 50, 18)
    d.text((cx, cy - 70), "CREDIT", font=font("impact.ttf", 190), fill=INK, anchor="mm")
    d.text((cx, cy + 120), "00", font=font("impact.ttf", 220), fill=INK, anchor="mm")
    for _ in range(140):
        x = rnd.randint(int(cx - 300), int(cx + 300)); y = rnd.randint(int(cy - 190), int(cy + 240))
        if img.getpixel((x, y))[:3] == INK:
            d.rectangle((x, y, x + 5, y + 5), fill=BR)
    img.convert("RGB").save(OUT + "already_spent_credit_ref.png")
    return OUT + "already_spent_credit_ref.png"


# ---- mango_og_gushers: vape box sleeve front face (portrait), flat
def mango():
    W, H = 880, 1600; rnd = random.Random(16)
    f = Image.new("RGBA", (W, H), (255, 214, 40, 255)); d = ImageDraw.Draw(f)
    ORANGE = (255, 130, 20); GREEN = (40, 160, 70); DKG = (20, 100, 50); YEL = (255, 214, 40)
    RED = (230, 60, 40); WH = (255, 250, 235)
    d.rectangle((0, 0, W, 250), fill=GREEN)
    d.rectangle((0, H - 340, W, H), fill=GREEN)
    bx, by = W / 2, 700
    pts = []
    for i in range(32):
        a = math.radians(i * 360 / 32); rr = 400 if i % 2 == 0 else 250
        pts.append((bx + rr * math.cos(a), by + rr * math.sin(a)))
    d.polygon(pts, fill=ORANGE)
    d.ellipse((bx - 245, by - 245, bx + 245, by + 245), fill=RED)
    m = Image.new("RGBA", (W, H), (0, 0, 0, 0)); md = ImageDraw.Draw(m)
    md.ellipse((bx - 170, by - 130, bx + 170, by + 150), fill=(255, 176, 30, 255), outline=(200, 90, 10, 255), width=12)
    md.ellipse((bx - 110, by - 80, bx - 40, by + 20), fill=(255, 226, 120, 255))
    md.polygon([(bx + 10, by - 125), (bx + 120, by - 215), (bx + 175, by - 150), (bx + 60, by - 110)], fill=DKG + (255,))
    m = m.rotate(-18, center=(bx, by), resample=Image.BICUBIC)
    f.alpha_composite(m)
    d = ImageDraw.Draw(f)
    cols = [(255, 90, 160), (120, 80, 220), (60, 190, 230), (255, 120, 20), (140, 220, 60)]
    for i in range(14):
        x = rnd.choice([rnd.randint(40, 170), rnd.randint(W - 170, W - 40)]); y = rnd.randint(330, 1180)
        c = cols[i % 5]; r = rnd.randint(28, 46)
        d.ellipse((x - r, y - r * .8, x + r, y + r * .8), fill=c, outline=(40, 30, 30), width=5)
        d.ellipse((x - r * .5, y - r * .5, x - r * .1, y - r * .2), fill=WH)

    def outlined(xy, s, fnt, fill, ol, w=8):
        for dx in range(-w, w + 1, 2):
            for dy in range(-w, w + 1, 2):
                d.text((xy[0] + dx, xy[1] + dy), s, font=fnt, fill=ol, anchor="mm")
        d.text(xy, s, font=fnt, fill=fill, anchor="mm")
    outlined((W / 2, 80), "MANGO OG", font("impact.ttf", 115), WH, DKG)
    outlined((W / 2, 190), "GUSHERS\u2122", font("impact.ttf", 115), YEL, DKG)
    outlined((W / 2, 1180), "Tropical. Juicy.", font("ariblk.ttf", 66), WH, (120, 50, 10), 5)
    outlined((W / 2, 1265), "Questionably Licensed.", font("ariblk.ttf", 56), YEL, (120, 50, 10), 5)
    d.rounded_rectangle((90, 1370, W - 90, 1540), radius=40, fill=WH, outline=DKG, width=8)
    d.text((W / 2, 1420), "OG FORMULA", font=font("ariblk.ttf", 56), fill=RED, anchor="mm")
    d.text((W / 2, 1490), "ALL MANGO. NO LUNCHBOX.", font=font("arialbd.ttf", 41), fill=DKG, anchor="mm")
    stains(d, rnd, (0, 300, W, 1100), 12, [(190, 120, 30), (170, 150, 40), (140, 110, 40)], 18, 48)
    d.ellipse((620, 960, 800, 1140), outline=(120, 70, 20), width=14)
    for _ in range(10):
        x = rnd.randint(40, W - 200); y = rnd.randint(300, 1100)
        d.line((x, y, x + rnd.randint(60, 150), y + rnd.randint(-30, 30)), fill=(235, 225, 190), width=6)
    f = f.convert("RGB"); f.save(OUT + "mango_og_gushers_face_rect.png")
    cw, ch = 1330, 1900
    ff = f.resize((int(ch * .76 * W / H), int(ch * .76)))
    c = Image.new("RGB", (cw, ch), GREY); c.paste(ff, ((cw - ff.size[0]) // 2, (ch - ff.size[1]) // 2))
    c.save(OUT + "mango_og_gushers_ref.png")
    return OUT + "mango_og_gushers_ref.png"


if __name__ == "__main__":
    for fn in (badge, token, mango):
        p = fn(); print(p, margins(p))
