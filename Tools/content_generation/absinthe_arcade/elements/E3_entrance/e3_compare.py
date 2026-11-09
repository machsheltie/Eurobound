import sys
from PIL import Image
ref, ren, out = sys.argv[1:4]
win = tuple(map(int, sys.argv[4:8])) if len(sys.argv) > 7 else None
a = Image.open(ref).convert("RGB")
if win: a = a.crop(win)
b = Image.open(ren).convert("RGB")
H = b.height
a = a.resize((round(a.width * H / a.height), H), Image.LANCZOS)
o = Image.new("RGB", (a.width + b.width + 12, H), (255, 255, 255))
o.paste(a, (0, 0)); o.paste(b, (a.width + 12, 0)); o.save(out)
