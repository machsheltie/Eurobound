"""Flat atlas art for the Already-Spent Credit token (0 credits). Pillow only.

python Tools/item3d/credit_art.py <out_atlas.png>
Atlas 2048x1280: front face (0..1024), back face (1024..2048, mirrored in mesh), rim strip (bottom 256 rows).
Palette from the item doc (already_spent_credit_item.md). Lettering: Impact, CREDIT / 00 only on the front.
Reverse emblem: the angular hourglass-X mark on the facade token of the approved Absinthe Arcade front plate.
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageChops

S = 2                       # supersample
N = 1024 * S
BRASS, HI, SH, ZINC = (201, 164, 93), (231, 215, 183), (138, 110, 20), (168, 154, 148)
VERD, BROWN, INK, UV = (11, 107, 80), (58, 46, 42), (42, 33, 24), (57, 255, 20)
C = N // 2
IMPACT = "C:/Windows/Fonts/impact.ttf"
random.seed(11)


def ring(d, r, w, fill):
    d.ellipse((C - r, C - r, C + r, C + r), outline=fill, width=w)


def arc(d, r, a0, a1, w, fill):
    d.arc((C - r, C - r, C + r, C + r), a0, a1, fill=fill, width=w)


def blank():
    return Image.new("L", (N, N), 0)


def face(back=False):
    im = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((0, 0, N - 1, N - 1), fill=SH)                      # rim shoulder shadow
    fr = int(C * 0.915)
    d.ellipse((C - fr, C - fr, C + fr, C + fr), fill=BRASS)       # flat face
    ring(d, fr, 8 * S, HI)
    nd = 44                                                       # milled dots round the shoulder band
    for k in range(nd):
        a = 2 * math.pi * k / nd
        r = C * 0.955
        x, y = C + r * math.cos(a), C + r * math.sin(a)
        rr = 17 * S
        worn = k % 5 in (0, 2)
        d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=ZINC if worn else HI)
    gr = int(C * 0.80)                                            # groove ring, verdigris, two UV flecks
    ring(d, gr, 16 * S, SH)
    ring(d, gr + 9 * S, 4 * S, HI)
    for (a0, a1) in ((200, 262), (330, 20), (95, 130)):
        arc(d, gr, a0, a1, 16 * S, VERD)
    for a in (math.radians(148), math.radians(305)):
        x, y = C + gr * math.cos(a), C + gr * math.sin(a)
        d.ellipse((x - 14 * S, y - 14 * S, x + 14 * S, y + 14 * S), fill=UV)
    ba = math.radians(-140 if back else -40)                                        # flat bite out of the rim (zinc, hard-edged)
    nx, ny = math.cos(ba), math.sin(ba)
    px, py = -ny, nx
    q = lambda rad, s: (C + nx * C * rad + px * s * S, C + ny * C * rad + py * s * S)
    d.polygon([q(0.93, 150), q(0.93, -150), q(1.05, -150), q(1.05, 150)], fill=ZINC)
    sm = Image.new("L", (N, N), 0)                                # brown smear, hard-edged
    ImageDraw.Draw(sm).polygon([(C - 560 * S, C + 200 * S), (C - 420 * S, C + 150 * S), (C - 330 * S, C + 260 * S),
                                (C - 380 * S, C + 400 * S), (C - 520 * S, C + 380 * S)], fill=255)
    d.bitmap((0, 0), sm, fill=BROWN)
    if not back:
        f = ImageFont.truetype(IMPACT, 330 * S)
        w = d.textlength("CREDIT", font=f)
        f = ImageFont.truetype(IMPACT, int(330 * S * 590 * S / w))
        f2 = ImageFont.truetype(IMPACT, 330 * S)
        for txt, fnt, cy in (("CREDIT", f, C - 105 * S), ("00", f2, C + 150 * S)):
            w = d.textlength(txt, font=fnt)
            m = blank(); ImageDraw.Draw(m).text((C - w / 2, cy), txt, font=fnt, fill=255, anchor="lm")
            lip = blank(); lip.paste(m, (4 * S, 5 * S))           # recess lip: lower-right light edge
            d.bitmap((0, 0), lip, fill=HI)
            d.bitmap((0, 0), m, fill=INK)
            fl = blank(); fd = ImageDraw.Draw(fl); bb = m.getbbox()   # bare-metal flecks on stroke tops
            for _ in range(9):
                x = random.randint(bb[0], bb[2]); y = random.randint(bb[1], bb[1] + (bb[3] - bb[1]) // 3)
                fd.rectangle((x, y, x + random.randint(10, 26) * S, y + random.randint(5, 9) * S), fill=255)
            d.bitmap((0, 0), ImageChops.multiply(fl, m), fill=HI)
    else:
        e = 250 * S                                               # angular hourglass-X emblem, worn
        top, bot, bw = C - e, C + e, 70 * S
        sh = blank(); sd = ImageDraw.Draw(sh)
        sd.rectangle((C - e, top, C + e, top + bw), fill=255)
        sd.rectangle((C - e, bot - bw, C + e, bot), fill=255)
        sd.polygon([(C - e * 0.85, top + bw), (C + e * 0.85, top + bw), (C + 25 * S, C), (C - 25 * S, C)], fill=255)
        sd.polygon([(C - e * 0.85, bot - bw), (C + e * 0.85, bot - bw), (C + 25 * S, C), (C - 25 * S, C)], fill=255)
        mark = sh
        lip = blank(); lip.paste(mark, (5 * S, 6 * S))
        d.bitmap((0, 0), lip, fill=HI)
        d.bitmap((0, 0), mark, fill=SH)
        wear = blank(); wd = ImageDraw.Draw(wear)                 # worn nearly smooth
        for (x, y, r) in ((C - 150 * S, top + 20 * S, 45 * S), (C + 90 * S, C + 190 * S, 50 * S), (C + 140 * S, top + 30 * S, 35 * S)):
            wd.ellipse((x - r, y - r, x + r, y + r), fill=255)
        d.bitmap((0, 0), ImageChops.multiply(wear, mark), fill=BRASS)
        z = blank(); ImageDraw.Draw(z).polygon([(C - 150 * S, bot - 60 * S), (C - 40 * S, bot - 70 * S), (C - 60 * S, bot + 5 * S), (C - 160 * S, bot)], fill=255)
        d.bitmap((0, 0), ImageChops.multiply(z, mark), fill=ZINC)
        for k in range(12):                                       # ring of ticks, as on the facade token
            a = 2 * math.pi * k / 12 + 0.26
            r0, r1 = C * 0.68, C * 0.74
            d.line((C + r0 * math.cos(a), C + r0 * math.sin(a), C + r1 * math.cos(a), C + r1 * math.sin(a)), fill=SH, width=9 * S)
    mk = Image.new("L", (N, N), 0); ImageDraw.Draw(mk).ellipse((0, 0, N - 1, N - 1), fill=255)
    out = Image.new("RGBA", (N, N), (0, 0, 0, 0)); out.paste(im, (0, 0), mk)
    return out.resize((1024, 1024), Image.LANCZOS)


def rim_strip():
    w, h = 2048 * S, 256 * S
    im = Image.new("RGB", (w, h), BRASS); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, w, 30 * S), fill=SH); d.rectangle((0, h - 30 * S, w, h), fill=SH)
    n = 44
    for k in range(n):                                                     # milled ridges: thin dark grooves
        x = (k + 0.5) * w / n
        d.rectangle((x - 9 * S, 30 * S, x + 9 * S, h - 30 * S), fill=SH)
        if k % 5 in (0, 2):
            d.rectangle((x + 14 * S, 40 * S, x + 40 * S, h - 40 * S), fill=ZINC)   # worn flats
    d.rectangle((int(w * 0.31), 0, int(w * 0.36), h), fill=ZINC)          # flat gouge across the wall
    d.polygon([(int(w * 0.6), 0), (int(w * 0.66), 0), (int(w * 0.64), h), (int(w * 0.58), h)], fill=VERD)
    return im.resize((2048, 256), Image.LANCZOS)


atlas = Image.new("RGBA", (2048, 1280), SH + (255,))
fa, ba_ = face(False), face(True)
atlas.paste(fa, (0, 0), fa); atlas.paste(ba_, (1024, 0), ba_)
atlas.paste(rim_strip(), (0, 1024))
atlas.convert("RGB").save(sys.argv[1])
