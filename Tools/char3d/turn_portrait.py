"""Turn-order portrait (132x56, transparent) cut from a look-B idle frame: head and shoulders, three-quarter view. PIL only.

python tools/char3d/turn_portrait.py <idle frame.png, e.g. .../idle/SE/00.png> <out.png> [head_px=72] [w=132] [h=56] [tall=1.42] [top=0.07]
Finds the head (top of the alpha), takes a w:h window `head_px`*tall high (1.42 with top 0.07 = the gate-P approved framing: head fills the height, clear rows above the hair; 1.55 is looser) starting top*head_px above the hair centred on the head's column, and area-downsamples
to w x h. head_px = the character's head height in the frame at 300 px/m (about 72 for a 1.8 m adult). Battle HUD plan:
dev/asset_team/plans/battle_hud_icons_plan.md (Eurobound-du51). No Blender needed.
"""
import sys
import numpy as np
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
hp = float(sys.argv[3]) if len(sys.argv) > 3 else 72.0
W = int(sys.argv[4]) if len(sys.argv) > 4 else 132
H = int(sys.argv[5]) if len(sys.argv) > 5 else 56
im = Image.open(src).convert("RGBA"); a = np.array(im)[..., 3] > 128
ys = np.where(a.any(1))[0]; top = int(ys.min())
xs = np.where(a[top:top + int(hp)].any(0))[0]; cx = (int(xs.min()) + int(xs.max())) / 2   # head column
TALL = float(sys.argv[6]) if len(sys.argv) > 6 else 1.42
TOP = float(sys.argv[7]) if len(sys.argv) > 7 else 0.07
ch = hp * TALL; cw = ch * W / H; y0 = top - hp * TOP
box = tuple(int(round(v)) for v in (cx - cw / 2, y0, cx + cw / 2, y0 + ch))
big = Image.new("RGBA", (box[2] - box[0], box[3] - box[1]), (0, 0, 0, 0))
big.paste(im.crop(box), (0, 0))
pm = np.array(big).astype(np.float32); pm[..., :3] *= pm[..., 3:4] / 255.0   # premultiply so the edge takes no dark fringe from empty pixels
sm = np.array(Image.fromarray(pm.clip(0, 255).astype(np.uint8), "RGBA").resize((W, H), Image.BOX)).astype(np.float32)
al = sm[..., 3:4]; sm[..., :3] = np.where(al > 0, sm[..., :3] * 255.0 / np.maximum(al, 1), 0)
Image.fromarray(sm.clip(0, 255).astype(np.uint8), "RGBA").save(out)
print("portrait", out, "crop", box, "scale", round(H / ch, 3))
