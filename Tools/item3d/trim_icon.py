"""Trim a raw item render to about 400 px of 512 (premultiplied LANCZOS), centred, then write the 128 copy.
python Tools/item3d/trim_icon.py <raw_512.png> <out_512.png> [target=400]
"""
import sys
import numpy as np
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
target = int(sys.argv[3]) if len(sys.argv) > 3 else 400
im = Image.open(src).convert("RGBA")
bb = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
im = im.crop(bb)
k = target / max(im.size)
size = (max(1, round(im.width * k)), max(1, round(im.height * k)))
a = np.asarray(im).astype(np.float32) / 255.0
a[..., :3] *= a[..., 3:4]
chan = [Image.fromarray(a[..., i], "F").resize(size, Image.LANCZOS) for i in range(4)]
r = np.stack([np.asarray(c) for c in chan], -1)
r[..., :3] = np.where(r[..., 3:4] > 1e-4, r[..., :3] / np.maximum(r[..., 3:4], 1e-4), 0)
r = (np.clip(r, 0, 1) * 255 + 0.5).astype(np.uint8)
canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
canvas.paste(Image.fromarray(r, "RGBA"), ((512 - size[0]) // 2, (512 - size[1]) // 2))
canvas.save(out)
a = np.asarray(canvas).astype(np.float32) / 255.0
a[..., :3] *= a[..., 3:4]
chan = [Image.fromarray(a[..., i], "F").resize((128, 128), Image.LANCZOS) for i in range(4)]
r = np.stack([np.asarray(c) for c in chan], -1)
r[..., :3] = np.where(r[..., 3:4] > 1e-4, r[..., :3] / np.maximum(r[..., 3:4], 1e-4), 0)
Image.fromarray((np.clip(r, 0, 1) * 255 + 0.5).astype(np.uint8), "RGBA").save(out.replace("_512", "_128"))
print("TRIMMED", out, size)
