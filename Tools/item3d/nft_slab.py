"""Shared Legacy Vault NFT slab (0 Tripo credits). Every NFT icon calls this unchanged; only --art differs.

python tools/item3d/nft_slab.py --art <flat_art.png> --out <icon_512.png> [--work tmp_nft] [--tilt 40]

Spec: design/items/docs/nft_icon_slab.md. Steps:
 1. Pillow composes ONE face texture (5:7): clear grey-blue case, beveled rim shading, paper label strip with the typed
    lettering, the art in the window (crooked in its sleeve, one curled corner), red AUTHENTIC sticker, barcode sticker,
    scratches, dust, fingerprint smudge, stress crack. All lettering is typed here, never drawn by an image tool.
 2. Blender runs card_slab.py (a thick 5:7 slab, no hang slot) -> GLB, then render_item.py (unchanged) -> 512 + 128.
 3. Pillow trims and rescales to about 400 px of 512 with premultiplied LANCZOS, then rebuilds the 128.
Needs system python with Pillow and numpy.
"""
import argparse, os, random, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blender_lock import blender_lock
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BLENDER = os.environ.get("BLENDER", "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe")
W, H = 800, 1120                      # 5:7 face texture
SLAB_W, SLAB_T = 0.714, 0.14          # slab 0.714 x 1.0 x 0.14 (thick clear case)
LINES = ["BROCHAIN CERTIFIED", "GRADE BRO 10", "SERIAL 00-BRO-99"]
STICKER = "AUTHENTIC"
CASE, WHITE, LIP, BLOOM = (221, 227, 230), (255, 255, 255), (154, 163, 168), (201, 210, 214)
PAPER, INK, RED, BAR, DUST = (245, 245, 240), (26, 26, 26), (208, 42, 42), (17, 17, 17), (107, 107, 107)
FONT = next((p for p in ["C:/Windows/Fonts/arialbd.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
             if os.path.exists(p)), None)


def font(size):
    return ImageFont.truetype(FONT, size)


def fit(draw, text, max_w, start):
    s = start
    while draw.textlength(text, font=font(s)) > max_w and s > 10:
        s -= 1
    return s


def rot_paste(base, layer, center, angle):
    r = layer.rotate(angle, expand=True, resample=Image.BICUBIC)
    base.alpha_composite(r, (int(center[0] - r.width / 2), int(center[1] - r.height / 2)))


def build_face(art_path, out_path, curl_corner="bl"):
    rnd = random.Random(1999)
    img = Image.new("RGBA", (W, H), CASE + (255,))
    g = np.linspace(0.97, 1.02, H)[:, None, None]          # sheen, wrong on purpose (dull top, glossy bottom)
    img = Image.fromarray(np.clip(np.asarray(img).astype(np.float32) * g, 0, 255).astype(np.uint8))
    bl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(bl)      # cloudy bloom, two patches
    bd.ellipse((420, 330, 760, 560), fill=BLOOM + (150,)); bd.ellipse((40, 760, 330, 980), fill=BLOOM + (130,))
    img.alpha_composite(bl.filter(ImageFilter.GaussianBlur(40)))
    # label strip: crooked paper sticker, three typed lines
    strip = Image.new("RGBA", (680, 176), PAPER + (255,)); sd = ImageDraw.Draw(strip)
    sd.rectangle((0, 0, 679, 175), outline=(215, 215, 208, 255), width=2)
    size = min(fit(sd, t, 470, 44) for t in LINES)
    y = 14
    for t in LINES:
        sd.text((26, y), t, font=font(size), fill=INK + (255,)); y += 54
    sd.line((6, 170, 660, 163), fill=(120, 120, 120, 70), width=5)          # toner streak
    bub = Image.new("RGBA", (680, 176), (0, 0, 0, 0)); ImageDraw.Draw(bub).ellipse(
        (596, 10, 640, 40), fill=(255, 255, 255, 150), outline=(190, 190, 185, 200))   # air bubble
    strip.alpha_composite(bub)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    rot_paste(sh, Image.new("RGBA", (684, 180), (60, 70, 75, 110)).filter(ImageFilter.GaussianBlur(3)), (406, 148), 1.4)
    img.alpha_composite(sh)
    rot_paste(img, strip, (400, 144), 1.4)
    # window sleeve (a size too big) and the art card, crooked
    wx0, wy0, wx1, wy1 = 66, 252, 734, 1062
    d = ImageDraw.Draw(img)
    d.rectangle((wx0, wy0, wx1, wy1), fill=BLOOM + (255,))
    art = Image.open(art_path).convert("RGBA")
    cw, ch = (wx1 - wx0) - 28, (wy1 - wy0) - 30
    k = max(cw / art.width, ch / art.height)
    art = art.resize((int(art.width * k + .5), int(art.height * k + .5)), Image.LANCZOS)
    l, t = (art.width - cw) // 2, (art.height - ch) // 2
    card = art.crop((l, t, l + cw, t + ch))
    cd = ImageDraw.Draw(card)                                              # curled corner (lower left) lifts off
    tri = {"bl": [(0, ch - 70), (70, ch), (0, ch)], "br": [(cw, ch - 70), (cw - 70, ch), (cw, ch)],
           "tl": [(0, 70), (70, 0), (0, 0)], "tr": [(cw, 70), (cw - 70, 0), (cw, 0)]}.get(curl_corner)
    if tri:
        cd.polygon(tri, fill=(236, 238, 238, 255))
        cd.line([tri[0], tri[1]], fill=(120, 125, 128, 255), width=2)
    cs = Image.new("RGBA", (cw + 20, ch + 20), (0, 0, 0, 0))
    cs.paste(Image.new("RGBA", (cw, ch), (40, 50, 55, 120)), (14, 14)); cs = cs.filter(ImageFilter.GaussianBlur(5))
    wc = ((wx0 + wx1) / 2 + 6, (wy0 + wy1) / 2 + 2)
    rot_paste(img, cs, (wc[0] + 3, wc[1] + 4), -1.1); rot_paste(img, card, wc, -1.1)
    d = ImageDraw.Draw(img)
    d.rectangle((wx0 - 4, wy0 - 4, wx1 + 4, wy1 + 4), outline=LIP + (255,), width=5)         # inner shadow lip
    d.rectangle((2, 2, W - 3, H - 3), outline=LIP + (255,), width=4)                          # beveled rim shading
    d.rectangle((14, 14, W - 15, H - 15), outline=WHITE + (160,), width=3)
    d.line((34, 9, W - 34, 9), fill=WHITE + (255,), width=7)                  # the one hard highlight along the top rim
    d.line((9, 40, 9, H - 60), fill=WHITE + (140,), width=3)
    d.line((W - 8, 60, W - 8, H - 40), fill=LIP + (200,), width=5)
    d.line((40, H - 7, W - 40, H - 7), fill=LIP + (220,), width=7)
    # red AUTHENTIC sticker, overlapping the strip's right end
    st = Image.new("RGBA", (210, 210), (0, 0, 0, 0)); td = ImageDraw.Draw(st)
    td.ellipse((8, 8, 202, 202), fill=(140, 20, 20, 255)); td.ellipse((12, 10, 200, 198), fill=RED + (255,))
    td.ellipse((24, 22, 186, 184), outline=(235, 120, 120, 255), width=2)
    fs = fit(td, STICKER, 146, 34)
    tw = td.textlength(STICKER, font=font(fs))
    td.text((105 - tw / 2, 105 - fs * 0.55), STICKER, font=font(fs), fill=(255, 255, 255, 255))
    rot_paste(img, st, (676, 228), 13)
    # barcode sticker, bottom-right, crooked, bars only
    bc = Image.new("RGBA", (170, 92), (250, 250, 248, 255)); bcd = ImageDraw.Draw(bc)
    x = 14
    while x < 152:
        w = rnd.choice([2, 3, 4, 6]); bcd.rectangle((x, 12, x + w - 1, 80), fill=BAR + (255,)); x += w + rnd.choice([2, 3, 5])
    bcd.rectangle((0, 0, 169, 91), outline=(200, 200, 196, 255), width=2)
    rot_paste(img, bc, (632, 1046), -3.0)
    # wear: scratches (denser toward the bottom), scuff, dust, smudge, crack
    wl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); wd = ImageDraw.Draw(wl)
    for _ in range(150):
        yy = H * (rnd.random() ** 0.6); xx = rnd.uniform(-50, W - 100); ln = rnd.uniform(80, 520)
        a = rnd.randint(28, 85); c = (255, 255, 255, a) if rnd.random() < .7 else (80, 90, 95, a // 2)
        wd.line((xx, yy, xx + ln, yy - ln * 0.05 + rnd.uniform(-5, 5)), fill=c, width=1)
    for i in range(6):                                                      # deeper scuff, top-left
        wd.line((24 + i * 7, 70 + i * 3, 110 + i * 9, 36 + i * 2), fill=(255, 255, 255, 190), width=2)
    for _ in range(3):                                                       # dust sealed under plastic
        px, py = rnd.randint(120, 700), rnd.randint(300, 1000)
        wd.ellipse((px, py, px + 4, py + 4), fill=DUST + (230,))
    img.alpha_composite(wl)
    sm = Image.new("RGBA", (W, H), (0, 0, 0, 0)); smd = ImageDraw.Draw(sm)
    smd.ellipse((470, 800, 700, 960), fill=(255, 255, 255, 70))
    for r in range(6):
        smd.arc((500 + r * 8, 825 + r * 6, 670 - r * 8, 935 - r * 6), 0, 360, fill=(255, 255, 255, 60), width=2)
    img.alpha_composite(sm.filter(ImageFilter.GaussianBlur(5)))
    d = ImageDraw.Draw(img)                                                  # stress whitening crack, lower-left corner
    for pts in ([(4, H - 90), (22, H - 70), (14, H - 52), (34, H - 30)], [(22, H - 70), (46, H - 76), (58, H - 60)]):
        d.line(pts, fill=(255, 255, 255, 235), width=2)
    img.convert("RGB").save(out_path)


def premult_resize(im, size):
    a = np.asarray(im.convert("RGBA")).astype(np.float32) / 255.0
    pm = (np.dstack([a[..., :3] * a[..., 3:], a[..., 3:]]) * 255).round().astype(np.uint8)
    b = np.asarray(Image.fromarray(pm, "RGBA").resize(size, Image.LANCZOS)).astype(np.float32) / 255.0
    al = b[..., 3:]
    rgb = np.where(al > 1e-4, b[..., :3] / np.maximum(al, 1e-4), 0)
    return Image.fromarray((np.dstack([rgb.clip(0, 1), al]) * 255).round().astype(np.uint8), "RGBA")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--work", default="tmp_nft"); ap.add_argument("--tilt", default="40")
    ap.add_argument("--curl-corner", default="bl", choices=["bl", "br", "tl", "tr", "none"])
    a = ap.parse_args()
    os.makedirs(a.work, exist_ok=True)
    face, glb = os.path.join(a.work, "slab_face.png"), os.path.join(a.work, "slab.glb")
    build_face(a.art, face, a.curl_corner.replace("-", "_"))
    with blender_lock("nft_slab card_slab"):             # one Blender at a time (Eurobound-1nvh)
        subprocess.run([BLENDER, "-b", "--python", os.path.join(HERE, "card_slab.py"), "--", face, glb, a.tilt,
                        str(SLAB_W), str(SLAB_T), "0", "1.0"], check=True)
    with blender_lock("nft_slab render_item"):
        subprocess.run([BLENDER, "-b", "--python", os.path.join(HERE, "render_item.py"), "--", glb, a.out], check=True)
    im = Image.open(a.out).convert("RGBA")
    box = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    crop = im.crop(box); k = 400 / max(crop.size)
    crop = premult_resize(crop, (round(crop.width * k), round(crop.height * k)))
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    canvas.alpha_composite(crop, ((512 - crop.width) // 2, (512 - crop.height) // 2))
    canvas.save(a.out)
    premult_resize(canvas, (128, 128)).save(a.out.replace("_512", "_128"))
    print("DONE", a.out)


if __name__ == "__main__":
    main()
