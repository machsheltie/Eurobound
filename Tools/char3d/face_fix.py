"""Hand-placed face pixels for sprite_p4: closed-eye line, open mouth, blush."""
import sys
from PIL import Image, ImageDraw
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
px = im.load()
LASH = (69, 39, 30, 255)
MOUTH = (36, 24, 22, 255)
LIP = (128, 51, 43, 255)
BLUSH = (237, 114, 95, 255)
SKIN = (237, 137, 98, 255)
SKIN_L = (243, 207, 160, 255)
# closed eye: short downward-curved lid line
for p in [(19, 47), (20, 48), (21, 48), (22, 47)]:
    px[p] = LASH
# brow
for p in [(19, 45), (20, 45), (21, 45)]:
    px[p] = (89, 49, 36, 255)
# nose highlight / cheek
px[(22, 43)] = SKIN_L
px[(23, 45)] = BLUSH; px[(24, 46)] = BLUSH; px[(18, 49)] = BLUSH
# open mouth (face points up, so the mouth opens at the top edge)
for p in [(25, 42), (26, 42)]:
    px[p] = MOUTH
for p in [(25, 43), (26, 43), (27, 42)]:
    px[p] = LIP
px[(24, 42)] = SKIN
im.save(dst)
bg = Image.new("RGBA", im.size, (40, 70, 40, 255)); bg.alpha_composite(im)
bg.resize((1024, 1024), Image.NEAREST).save(dst.replace(".png", "_8x.png"))
c = bg.crop((6, 30, 46, 70)).resize((640, 640), Image.NEAREST); c.save(dst.replace(".png", "_head.png"))
