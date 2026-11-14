"""Recolour a colour region of a GLB's base-colour texture (e.g. the polo). Pure Python (PIL + numpy), no Blender.

python tools/char3d/recolor_region.py tools/char3d/poses/<id>_recolor.json

Config (paths relative to the repo root):
 glb: input GLB; out: output GLB (default: overwrite glb)
 regions: [{ hue: [lo, hi]   0..1, may wrap (red = [0.96, 0.03]),
             sat: [min, max], val: [min, max]   (optional; keep other reds such as the hat patch, lips and sunglasses out)
             uv_box: [u0, v0, u1, v1]  optional, v down like image rows (Tripo atlases are scattered, so this rarely helps)
             target: [r, g, b] 0..255  the colour the region's MEDIAN should become in the texture
             soft: 0.02  (edge softness of the hue/sat/val limits) }]
Method: take the median HSV of the selected texels, then shift hue, scale saturation and value by the ratio to the target, so shading
and fabric detail survive. The toon ramp changes brightness a little: measure the RENDER against the reference and adjust target.
Keeps the image's format (JPEG q92 or PNG). Geometry, rig and other textures are copied byte for byte. Prints <=3 lines.
"""
import sys, json, struct, io, os
import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
cfg = json.load(open(sys.argv[1])); P = lambda p: os.path.join(ROOT, p)
src = P(cfg["glb"]); dst = P(cfg.get("out", cfg["glb"]))
d = open(src, "rb").read(); assert d[:4] == b"glTF"
off = 12; chunks = []
while off < len(d):
    ln, typ = struct.unpack_from("<I4s", d, off); chunks.append(d[off + 8:off + 8 + ln]); off += 8 + ln
js = json.loads(chunks[0]); binc = chunks[1]; bvs = js["bufferViews"]
datas = [binc[bv.get("byteOffset", 0):bv.get("byteOffset", 0) + bv["byteLength"]] for bv in bvs]
ti = js["materials"][0]["pbrMetallicRoughness"]["baseColorTexture"]["index"]
im = js["images"][js["textures"][ti]["source"]]; bi = im["bufferView"]
pic = Image.open(io.BytesIO(datas[bi])); fmt = pic.format; pic = pic.convert("RGB")
arr = np.array(pic); H, W = arr.shape[:2]

def hsv(a):
    a = a.astype(np.float32) / 255.0; mx = a.max(-1); mn = a.min(-1); dd = mx - mn + 1e-9
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    h = np.where(mx == r, ((g - b) / dd) % 6, np.where(mx == g, (b - r) / dd + 2, (r - g) / dd + 4)) / 6
    return h % 1.0, dd / (mx + 1e-9), mx

def rgb(h, s, v):
    h6 = (h % 1.0) * 6; i = np.floor(h6).astype(int) % 6; f = h6 - np.floor(h6)
    p = v * (1 - s); q = v * (1 - f * s); t = v * (1 - (1 - f) * s)
    out = np.stack([np.select([i == k for k in range(6)], c) for c in
                    ((v, q, p, p, t, v), (t, v, v, q, p, p), (p, p, t, v, v, q))], -1)
    return out

def ramp(x, lo, hi, soft):   # 1 inside [lo,hi], fading to 0 over `soft` outside
    return np.clip(np.minimum((x - lo) / soft + 1, (hi - x) / soft + 1), 0, 1)

def weight(h, s, v, rg, xs, ys):
    soft = rg.get("soft", 0.02); lo, hi = rg["hue"]
    if lo <= hi: wh = ramp(h, lo, hi, soft)
    else: wh = np.maximum(ramp(h, lo, 1.0 + 1e-6, soft), ramp(h, -1e-6, hi, soft))
    w = wh * ramp(s, *rg.get("sat", [0, 1]), soft * 2) * ramp(v, *rg.get("val", [0, 1]), soft * 2)
    if rg.get("uv_box"):
        u0, v0, u1, v1 = rg["uv_box"]; x = xs[None, :] / W; y = ys[:, None] / H
        w = w * ((x >= u0) & (x <= u1) & (y >= v0) & (y <= v1))
    return w

for rg in cfg["regions"]:
    sub = arr[::8, ::8]; h, s, v = hsv(sub)
    w = weight(h, s, v, rg, np.arange(0, W, 8), np.arange(0, H, 8))
    sel = w > 0.99
    mh, ms, mv = [float(np.median(c[sel])) for c in (h, s, v)]
    # median hue on a wrapped scale
    if rg["hue"][0] > rg["hue"][1]: mh = float(np.median(np.where(h[sel] > 0.5, h[sel] - 1, h[sel])))
    th, ts, tv = [float(c[0, 0]) for c in hsv(np.array([[rg["target"]]], dtype=np.float32))]
    print("region texels(1/64):", int(sel.sum()), "median rgb", np.round(np.median(sub[sel], 0)).tolist(), "-> target", rg["target"])
    for y0 in range(0, H, 512):
        blk = arr[y0:y0 + 512]; bh, bs, bv = hsv(blk); wb = weight(bh, bs, bv, rg, np.arange(W), np.arange(y0, min(H, y0 + 512)))
        if not wb.any(): continue
        bh2 = np.where((bh > 0.5) & (rg["hue"][0] > rg["hue"][1]), bh - 1, bh) if rg["hue"][0] > rg["hue"][1] else bh
        nh = bh2 + (th - mh); ns = np.clip(bs * (ts / max(ms, 1e-6)), 0, 1); nv = np.clip(bv * (tv / max(mv, 1e-6)), 0, 1)
        new = rgb(nh, ns, nv) * 255.0
        blk[:] = np.clip(blk * (1 - wb[..., None]) + new * wb[..., None], 0, 255).astype(np.uint8)

b = io.BytesIO()
if fmt == "JPEG": Image.fromarray(arr).save(b, "JPEG", quality=92)
else: Image.fromarray(arr).save(b, "PNG")
datas[bi] = b.getvalue()
out = bytearray()
for bv, dat in zip(bvs, datas):
    while len(out) % 4: out += b"\0"
    bv["byteOffset"] = len(out); bv["byteLength"] = len(dat); out += dat
while len(out) % 4: out += b"\0"
js["buffers"][0]["byteLength"] = len(out)
jb = json.dumps(js, separators=(",", ":")).encode()
while len(jb) % 4: jb += b" "
total = 12 + 8 + len(jb) + 8 + len(out)
open(dst, "wb").write(b"glTF" + struct.pack("<II", 2, total) + struct.pack("<I4s", len(jb), b"JSON") + jb + struct.pack("<I4s", len(out), b"BIN\0") + bytes(out))
print(os.path.basename(dst), "%.1f MB" % (total / 1e6))
