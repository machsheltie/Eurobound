"""Silhouette IoU of a bbox-fitted ortho render against the reference alpha (same idea as project_ref.py's reliability report, at full ref resolution).
python sil_iou.py <render.png> <ref.png> [out_overlay.png]"""
import sys
from PIL import Image
import numpy as np
r = Image.open(sys.argv[1]).convert("RGBA")
ref = Image.open(sys.argv[2]).convert("RGBA")
ra = np.array(r)[..., 3] > 128
ys, xs = np.where(ra)
r = r.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)).resize(ref.size, Image.BILINEAR)
a = np.array(r)[..., 3] > 128
b = np.array(ref)[..., 3] > 128
iou = (a & b).sum() / max((a | b).sum(), 1)
print("IoU", round(float(iou), 3), "aspect render", round((xs.max() - xs.min() + 1) / (ys.max() - ys.min() + 1), 3), "ref", round(ref.width / ref.height, 3))
if len(sys.argv) > 3:
    o = np.zeros(a.shape + (3,), np.uint8)
    o[a & b] = (200, 200, 200); o[a & ~b] = (230, 40, 40); o[~a & b] = (40, 80, 230)
    Image.fromarray(o).save(sys.argv[3])
