"""Generate E3 texture maps (plain Python: numpy, scipy, Pillow). Re-runnable.

Outputs to Assets/Graphics/worlds/debaucheryville/absinthearcade/textures/e3_entrance/:
  e3_led_normal.png        tileable square-LED grid normal map (OpenGL, Y+), one LED per 32 px
  e3_led_height.png        matching height, used as a brightness break-up mask on the letter faces
  e3_glass_<id>.png        stained-glass panes: the lead pattern traced off the rectified bible crop,
                           cleaned to flat glass colours + black came (no grime, no weathering)
  e3_emblem_<id>.png       emissive line emblems traced off the crop (token, kick-plate X marks)
  e3_flyer_<n>.png         abstract flyers / stickers (colour blocks only, no lettering)
Run: <venv python> e3_textures.py
"""
import math
import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as ndi

from e3_trace_lib import REPO, hsv, rectified

OUT = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/textures/e3_entrance"

# Stained-glass panes: rectified canvas boxes (x0, y0, x1, y1) and the glass colour family.
GLASS = {
    "l_transom_a": ((688, 930, 782, 1090), "green"),
    "l_main": ((686, 1105, 790, 1785), "green"),
    "l_transom_b": ((858, 995, 936, 1150), "green"),
    "l_purple": ((850, 1180, 940, 1910), "purple"),
    "r_transom": ((1835, 935, 1966, 1080), "green"),
    "r_main": ((1838, 1118, 1990, 1785), "green"),
    "strip": ((2336, 880, 2468, 1700), "green"),
}
# flat palette (sRGB) the cleaned glass is snapped to
PAL = {
    "green": (150, 168, 80),
    "green_dk": (120, 150, 60),
    "purple": (175, 85, 200),
    "purple_dk": (110, 50, 150),
    "amber": (210, 150, 60),
    "lead": (14, 14, 12),
}

EMBLEMS = {
    "token": ((508, 528, 702, 716), "green"),        # green disc with the hourglass/X mark
    "kick_l": ((706, 1996, 776, 2068), "green"),     # left door kick-plate square/X
    "kick_r": ((1892, 2002, 1974, 2084), "green"),   # right door kick-plate square/X
}


def led_maps(px=512, leds=16):
    """Square LEDs with soft rounded shoulders -> height + normal (tileable)."""
    n = px // leds
    t = (np.arange(px) % n) / n                        # 0..1 inside each LED cell
    gx = np.minimum(t, 1 - t)                          # distance to cell edge
    d = np.minimum.outer(gx, gx)
    h = np.clip(d / 0.16, 0, 1) ** 0.6                 # flat top, 16% bevel to the gap
    h = ndi.gaussian_filter(h, 1.0, mode="wrap")
    dy, dx = np.gradient(h)
    strength = 6.0
    nx, ny, nz = -dx * strength, dy * strength, np.ones_like(h)   # OpenGL: green up
    ln = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
    nrm = np.stack([nx / ln, ny / ln, nz / ln], -1) * 0.5 + 0.5
    Image.fromarray((nrm * 255).astype(np.uint8)).save(OUT / "e3_led_normal.png")
    Image.fromarray((h * 255).astype(np.uint8)).save(OUT / "e3_led_height.png")


def mode_filter(lab, k=5):
    """Majority filter on a small label image."""
    out = lab.copy()
    best = np.zeros(lab.shape, np.float32)
    for v in np.unique(lab):
        cnt = ndi.uniform_filter((lab == v).astype(np.float32), k)
        sel = cnt > best
        out[sel] = v
        best[sel] = cnt[sel]
    return out


def glass_textures(img, scale=4):
    h, s, v = hsv(img)
    for gid, (box, fam) in GLASS.items():
        x0, y0, x1, y1 = box
        hh, ss, vv = h[y0:y1, x0:x1], s[y0:y1, x0:x1], v[y0:y1, x0:x1]
        # upsample so the came keeps smooth curves at texture resolution
        z = lambda a: ndi.zoom(a, scale, order=1)
        hh, ss, vv = z(hh), z(ss), z(vv)
        # relative threshold: the transoms sit in the marquee's shadow and read darker overall
        lead = vv < 0.48 * np.percentile(vv, 85)
        lead = ndi.binary_opening(ndi.binary_closing(lead, iterations=2), iterations=2)
        # remove specks smaller than a came segment (grime, chips)
        lab, n = ndi.label(lead)
        sizes = ndi.sum(lead, lab, range(1, n + 1))
        lead = np.isin(lab, [i + 1 for i, sz in enumerate(sizes) if sz > 60 * scale * scale])
        # glass colour classes
        cls = np.zeros(lead.shape, np.uint8)            # 0 green
        purple = (hh > 0.70) & (hh < 0.95) & (ss > 0.18)
        amber = (hh > 0.06) & (hh < 0.14) & (ss > 0.35) & (vv > 0.45)
        cls[purple] = 2
        cls[amber] = 3
        if fam == "purple":
            dark_glass = ~purple & ~amber & (vv < 0.45)
            cls[dark_glass] = 4                        # deep purple/black in the purple column
        cls = mode_filter(cls, 9 * scale // 2 * 2 + 1)
        cls[lead] = 9
        rgb = np.zeros(cls.shape + (3,), np.uint8)
        base = PAL["green"] if fam == "green" else PAL["purple_dk"]
        rgb[:] = base
        rgb[cls == 2] = PAL["purple"]
        rgb[cls == 3] = PAL["amber"]
        rgb[cls == 4] = (60, 30, 80)
        rgb[cls == 9] = PAL["lead"]
        im = Image.fromarray(rgb).filter(ImageFilter.SMOOTH)
        im.save(OUT / f"e3_glass_{gid}.png")
        # emission mask: glass glows, came does not
        em = (~lead).astype(np.uint8) * 255
        Image.fromarray(em).filter(ImageFilter.GaussianBlur(1)).save(OUT / f"e3_glass_{gid}_mask.png")


def emblem_textures(img, scale=4):
    h, s, v = hsv(img)
    for eid, (box, fam) in EMBLEMS.items():
        x0, y0, x1, y1 = box
        z = lambda a: ndi.zoom(a, scale, order=1)
        hh, ss, vv = z(h[y0:y1, x0:x1]), z(s[y0:y1, x0:x1]), z(v[y0:y1, x0:x1])
        lit = (hh > 0.12) & (hh < 0.32) & (ss > 0.25) & (vv > 0.40)
        lit = ndi.binary_opening(ndi.binary_closing(lit, iterations=2), iterations=1)
        lab, n = ndi.label(lit)
        sizes = ndi.sum(lit, lab, range(1, n + 1))
        lit = np.isin(lab, [i + 1 for i, sz in enumerate(sizes) if sz > 30 * scale * scale])
        Image.fromarray(lit.astype(np.uint8) * 255).filter(ImageFilter.GaussianBlur(0.8)).save(
            OUT / f"e3_emblem_{eid}.png")


# Painted ornament on the marquee casing, traced as colour masks (canvas box of the decal image).
DECAL_BOX = (150, 20, 2440, 760)
DECAL_GREEN = [(690, 105, 880, 200), (1690, 120, 1840, 215)]          # green curls in the casing corners
DECAL_PURPLE = [(1125, 100, 1235, 205), (1305, 100, 1420, 205)]       # purple swirls in the apex box


def marquee_decal(img):
    h, s, v = hsv(img)
    x0, y0, x1, y1 = DECAL_BOX
    out = np.zeros((y1 - y0, x1 - x0, 3), np.uint8)
    for boxes, fam, col in ((DECAL_GREEN, "g", (150, 205, 60)), (DECAL_PURPLE, "p", (190, 90, 230))):
        for (a, b, c, d) in boxes:
            hh, ss, vv = h[b:d, a:c], s[b:d, a:c], v[b:d, a:c]
            if fam == "g":
                m = (hh > 0.13) & (hh < 0.32) & (ss > 0.3) & (vv > 0.35)
            else:
                m = (hh > 0.70) & (hh < 0.95) & (ss > 0.2) & (vv > 0.3)
            m = ndi.binary_opening(ndi.binary_closing(m, iterations=1), iterations=1)
            out[b - y0:d - y0, a - x0:c - x0][m] = col
    Image.fromarray(out).filter(ImageFilter.SMOOTH).save(OUT / "e3_decal_marquee.png")


def flyer_textures(count=14, seed=7):
    """Abstract flyers: paper ground + colour blocks/shapes. Deliberately no glyphs of any kind."""
    rnd = random.Random(seed)
    grounds = [(232, 120, 190), (244, 206, 70), (240, 236, 226), (70, 120, 190), (236, 226, 210)]
    inks = [(30, 60, 140), (230, 170, 40), (200, 60, 80), (20, 20, 20), (90, 160, 210), (240, 240, 240)]
    for i in range(count):
        w, h = 256, 320
        g = grounds[i % len(grounds)]
        im = Image.new("RGB", (w, h), g)
        d = ImageDraw.Draw(im)
        for _ in range(rnd.randint(3, 6)):
            c = rnd.choice([k for k in inks if k != g])
            x0, y0 = rnd.randint(-40, w - 40), rnd.randint(-40, h - 40)
            x1, y1 = x0 + rnd.randint(40, 180), y0 + rnd.randint(30, 160)
            kind = rnd.random()
            if kind < 0.45:
                d.rectangle([x0, y0, x1, y1], fill=c)
            elif kind < 0.8:
                d.ellipse([x0, y0, x1, y1], fill=c)
            else:
                d.polygon([(x0, y1), ((x0 + x1) // 2, y0), (x1, y1)], fill=c)
        d.rectangle([0, 0, w - 1, h - 1], outline=(250, 250, 245), width=10)   # white print margin
        im.save(OUT / f"e3_flyer_{i:02d}.png")


# ---------------------------------------------------------------------------------------------
# round 2 additions
# ---------------------------------------------------------------------------------------------
def bead_maps(px=512, beads=16):
    """Round domed LED beads (ARCADE's sequined faces) -> normal + height, tileable."""
    n = px // beads
    t = (np.arange(px) % n) / n - 0.5
    r = np.sqrt(np.add.outer(t ** 2, t ** 2)) / 0.42
    h = np.sqrt(np.clip(1 - r ** 2, 0, 1))                      # hemispherical dome, 84% of the cell
    h = ndi.gaussian_filter(h, 0.7, mode="wrap")
    dy, dx = np.gradient(h)
    s = 9.0
    nx, ny, nz = -dx * s, dy * s, np.ones_like(h)
    ln = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
    nrm = np.stack([nx / ln, ny / ln, nz / ln], -1) * 0.5 + 0.5
    Image.fromarray((nrm * 255).astype(np.uint8)).save(OUT / "e3_bead_normal.png")
    Image.fromarray((h * 255).astype(np.uint8)).save(OUT / "e3_bead_height.png")


def came_normals():
    """Raised lead came: height from each glass mask (came = high, rounded), as a normal map;
    plus a seedy cathedral-glass brightness variation for the backlight."""
    for gid in GLASS:
        m = np.asarray(Image.open(OUT / f"e3_glass_{gid}_mask.png").convert("L")).astype(np.float32) / 255
        lead = 1 - m
        dist = ndi.distance_transform_edt(lead > 0.5)
        h = np.clip(dist / 6.0, 0, 1) ** 0.5                       # rounded profile across the came
        h = ndi.gaussian_filter(h, 1.2)
        dy, dx = np.gradient(h)
        s = 5.0
        nx, ny, nz = -dx * s, dy * s, np.ones_like(h)
        ln = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
        nrm = np.stack([nx / ln, ny / ln, nz / ln], -1) * 0.5 + 0.5
        Image.fromarray((nrm * 255).astype(np.uint8)).save(OUT / f"e3_glass_{gid}_normal.png")
        rnd = np.random.default_rng(len(gid))
        noise = ndi.gaussian_filter(rnd.random(h.shape), 6)
        noise = (noise - noise.min()) / (np.ptp(noise) + 1e-6)
        Image.fromarray(((0.75 + 0.25 * noise) * m * 255).astype(np.uint8)).save(OUT / f"e3_glass_{gid}_glow.png")


def _illustration(rnd, w, h, palette):
    """Abstract illustrated print: graded ground, inked blobs, strokes, halftone patch. No glyphs."""
    a = np.zeros((h, w, 3), np.float32)
    c0, c1 = np.array(rnd.choice(palette), np.float32), np.array(rnd.choice(palette), np.float32)
    g = np.linspace(0, 1, h)[:, None, None]
    a[:] = c0 * (1 - g) + c1 * g
    im = Image.fromarray(a.astype(np.uint8))
    d = ImageDraw.Draw(im)
    for _ in range(rnd.randint(3, 6)):
        col = tuple(int(v) for v in rnd.choice(palette))
        x0, y0 = rnd.randint(-30, w - 30), rnd.randint(-30, h - 30)
        x1, y1 = x0 + rnd.randint(40, 150), y0 + rnd.randint(40, 150)
        pts = [(x0 + rnd.randint(0, x1 - x0), y0 + rnd.randint(0, y1 - y0)) for _ in range(rnd.randint(5, 8))]
        pts.sort(key=lambda p: math.atan2(p[1] - (y0 + y1) / 2, p[0] - (x0 + x1) / 2))
        d.polygon(pts, fill=col, outline=(25, 25, 35), width=3)
    for _ in range(rnd.randint(1, 3)):
        col = tuple(int(v) for v in rnd.choice(palette))
        pts = [(rnd.randint(0, w), rnd.randint(0, h)) for _ in range(4)]
        d.line(pts, fill=col, width=rnd.randint(6, 14), joint="curve")
    if rnd.random() < 0.6:
        hx, hy = rnd.randint(0, w // 2), rnd.randint(0, h // 2)
        col = tuple(int(v) for v in rnd.choice(palette))
        for yy in range(hy, hy + h // 2, 9):
            for xx in range(hx, hx + w // 2, 9):
                rr = 1 + 3 * ((xx - hx) / (w / 2))
                d.ellipse([xx - rr, yy - rr, xx + rr, yy + rr], fill=col)
    return im.filter(ImageFilter.SMOOTH)


def flyer_textures_v2(count=14, seed=11):
    """Paper flyers/prints: white border, illustrated abstract image, paper tooth. No lettering."""
    rnd = random.Random(seed)
    palettes = [
        [(40, 80, 160), (230, 190, 60), (245, 240, 230), (30, 30, 40), (120, 170, 220)],
        [(235, 120, 170), (250, 210, 220), (60, 40, 70), (240, 240, 235), (160, 60, 110)],
        [(240, 200, 70), (40, 90, 170), (250, 245, 235), (200, 70, 60), (25, 25, 30)],
        [(245, 245, 240), (200, 60, 70), (60, 120, 190), (230, 180, 60), (40, 40, 45)],
    ]
    for i in range(count):
        w, h = 256, 320
        im = Image.new("RGB", (w, h), (246, 243, 236))
        border = rnd.randint(10, 22)
        art = _illustration(rnd, w - 2 * border, h - 2 * border - rnd.choice([0, 0, 30]), palettes[i % 4])
        im.paste(art, (border, border))
        a = np.asarray(im).astype(np.float32)
        tooth = np.asarray(Image.effect_noise((w, h), 18).convert("L")).astype(np.float32)[..., None] / 255
        fade = np.linspace(1.0, 0.9, w)[None, :, None]
        a = np.clip(a * (0.94 + 0.06 * tooth) * fade + 10 * (1 - fade), 0, 255)
        Image.fromarray(a.astype(np.uint8)).save(OUT / f"e3_flyer_{i:02d}.png")
    # pink sign at the top of the left pier: pink card, darker abstract squiggles, no glyphs
    w, h = 512, 320
    im = Image.new("RGB", (w, h), (233, 140, 190))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w - 1, h - 1], outline=(250, 200, 225), width=14)
    for k in range(5):
        y = 70 + k * 45
        pts = [(60 + j * 30, y + int(10 * math.sin(j * 1.7 + k))) for j in range(14)]
        d.line(pts, fill=(120, 50, 95), width=7, joint="curve")
    im.filter(ImageFilter.SMOOTH).save(OUT / "e3_pink_sign.png")


def cabinet_art(seed=5):
    """Cabinet screens (dark field, pixel sprites, starfield) and marquees (orange pixel art). No text."""
    rnd = random.Random(seed)
    for k in range(5):
        w, h = 192, 256
        im = Image.new("RGB", (w, h), (8, 14, 40))
        d = ImageDraw.Draw(im)
        for _ in range(60):
            d.point((rnd.randint(0, w), rnd.randint(0, h)), fill=(200, 220, 255))
        for _ in range(5):
            col = rnd.choice([(80, 200, 255), (255, 255, 255), (255, 90, 200), (120, 255, 120), (255, 200, 60)])
            cx, cy, ps = rnd.randint(20, w - 40), rnd.randint(20, h - 60), rnd.choice([4, 5, 6])
            for gy in range(5):
                for gx in range(5):
                    if rnd.random() < 0.55 or gx == 2:
                        d.rectangle([cx + gx * ps, cy + gy * ps, cx + gx * ps + ps - 1, cy + gy * ps + ps - 1], fill=col)
        d.rectangle([0, h - 30, w, h], fill=(20, 40, 90))
        for x in range(8, w, 22):
            d.rectangle([x, h - 22, x + 10, h - 12], fill=(255, 170, 60))
        im.filter(ImageFilter.GaussianBlur(0.6)).save(OUT / f"e3_cab_screen_{k}.png")
        mq = Image.new("RGB", (256, 64), (235, 95, 25))
        d = ImageDraw.Draw(mq)
        for x in range(10, 246, 12):
            hh = rnd.randint(12, 40)
            d.rectangle([x, 32 - hh // 2, x + 7, 32 + hh // 2],
                        fill=rnd.choice([(255, 200, 90), (120, 25, 10), (200, 50, 20)]))
        d.rectangle([0, 0, 255, 63], outline=(255, 220, 150), width=4)
        mq.filter(ImageFilter.GaussianBlur(0.8)).save(OUT / f"e3_cab_marquee_{k}.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    img = rectified()
    led_maps()
    glass_textures(img)
    emblem_textures(img)
    marquee_decal(img)
    bead_maps()
    came_normals()
    flyer_textures_v2()          # replaces the round-1 flat colour cards
    cabinet_art()
    print(sorted(p.name for p in OUT.iterdir()))


if __name__ == "__main__":
    main()
