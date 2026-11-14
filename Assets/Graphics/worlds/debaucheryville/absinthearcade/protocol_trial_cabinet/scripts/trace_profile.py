"""Measuring-stick step (nhxz.3 method): trace the side reference silhouette into a simplified polygon (ref px, y down).
Run with the paint_zones venv python (has cv2): trace_profile.py <side_ref.png> <out.json> [eps_px 2.0]"""
import sys, json
import numpy as np, cv2
from PIL import Image
a = np.array(Image.open(sys.argv[1]).convert("RGBA"))[..., 3] > 128
m = a.astype(np.uint8) * 255
m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
m = cv2.copyMakeBorder(m, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
c = max(cs, key=cv2.contourArea) - 1
eps = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
p = cv2.approxPolyDP(c, eps, True)[:, 0, :]
json.dump({"size": [a.shape[1], a.shape[0]], "poly": p.tolist()}, open(sys.argv[2], "w"))
print("profile verts", len(p), "area px", int(cv2.contourArea(c)))
