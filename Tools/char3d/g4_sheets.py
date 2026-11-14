"""G4 review sheets from rendered look-B frames (PIL only).

python tools/char3d/g4_sheets.py <frames_dir> <portrait.png> <out_dir>
  frames_dir holds idle/<DIR>/NN.png and walk/<DIR>/NN.png (640x640, 8 directions).
Writes to out_dir: g4_walk.jpg (rows S..SW, columns = walk frames, red line = idle near-foot row), g4_idle.jpg
(per direction idle frame 0 and the breath-peak frame, plus S enlarged), game_size_S.png (160 px), portrait_700.jpg,
and prints frame counts per direction plus the breath-peak frame index.
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw

F, PORT, O = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(O, exist_ok=True)
D = ["S", "SE", "E", "NE", "N", "NW", "W", "SW"]


def frames(a, d):
    p = os.path.join(F, a, d)
    return sorted(f for f in os.listdir(p) if f.endswith(".png")) if os.path.isdir(p) else []


def fr(a, d, i):   # frames on a canvas other than 640 (a taller character) are scaled to 640 for the sheets
    im = Image.open(os.path.join(F, a, d, "%02d.png" % i)).convert("RGBA")
    return im if im.size == (640, 640) else im.resize((640, 640), Image.LANCZOS)


def bottom(im):
    return int(np.where((np.array(im)[..., 3] > 128).any(1))[0].max())


ref = Image.open(PORT).convert("RGB")
ref.resize((int(ref.width * 700 / ref.height), 700), Image.LANCZOS).save(os.path.join(O, "portrait_700.jpg"), quality=90)
nw = max(len(frames("walk", d)) for d in D)
tw, th = 84, 132
W = Image.new("RGB", (max(nw, 1) * tw, 8 * th), (150, 150, 150)); dr = ImageDraw.Draw(W)
for r, d in enumerate(D):
    for c in range(len(frames("walk", d))):
        im = fr("walk", d, c).crop((120, 20, 520, 640)).resize((tw, int(620 * tw / 400)), Image.LANCZOS).crop((0, 0, tw, th))
        W.paste(im, (c * tw, r * th), im)
    if frames("idle", d):
        fy = r * th + int((bottom(fr("idle", d, 0)) - 20) * tw / 400)
        dr.line([(0, fy), (W.width, fy)], fill=(220, 0, 0))
W.save(os.path.join(O, "g4_walk.jpg"), quality=88)
# breath peak = idle frame that differs most from frame 0 (S view)
ni = len(frames("idle", "S"))
pk = 0
if ni > 1:
    a0 = np.array(fr("idle", "S", 0)).astype(int)
    pk = max(range(1, ni), key=lambda i: int((np.abs(np.array(fr("idle", "S", i)).astype(int) - a0).sum(2) > 30).sum()))
I = Image.new("RGB", (16 * 64, 280), (150, 150, 150))
for k, d in enumerate(D):
    if not frames("idle", d):
        continue
    for j, i in enumerate((0, pk)):
        im = fr("idle", d, i).crop((120, 20, 520, 640)).resize((64, 99), Image.LANCZOS); I.paste(im, ((2 * k + j) * 64, 0), im)
if ni:
    for j, i in enumerate((0, pk)):
        im = fr("idle", "S", i).crop((180, 20, 460, 300)).resize((180, 180), Image.LANCZOS); I.paste(im, (j * 190, 100), im)
    g = fr("idle", "S", 0).resize((160, 160), Image.LANCZOS); bg = Image.new("RGB", (160, 160), (90, 70, 80)); bg.paste(g, (0, 0), g)
    bg.save(os.path.join(O, "game_size_S.png"))
I.save(os.path.join(O, "g4_idle.jpg"), quality=88)
print("frames idle/walk:", {d: (len(frames("idle", d)), len(frames("walk", d))) for d in D}, "breath peak", pk)
