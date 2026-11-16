"""Rebuild the Kokos base-colour texture as clean flat toon areas, painted by 3D position (run after texmap2)."""
import numpy as np, math
from PIL import Image
rng = np.random.default_rng(11)
d = np.load('map.npz'); ok = d['ok']
orig = np.array(Image.open('tex0.jpg').convert('RGB'))
idx = np.flatnonzero(ok.ravel())
P = d['pos'].reshape(-1, 3)[idx]; Nn = d['nor'].reshape(-1, 3)[idx]
O = orig.reshape(-1, 3)[idx].astype(np.float32)
x, y, z = P[:, 0], P[:, 1], P[:, 2]
r = np.hypot(x, y); az = np.degrees(np.arctan2(y, x))
nl = np.maximum(np.linalg.norm(Nn, axis=1), 1e-6); Nn = Nn / nl[:, None]
rad = (Nn[:, 0] * x + Nn[:, 1] * y) / np.maximum(r, 1e-6)
nz = Nn[:, 2]
AZC = -117.0
RR = 0.43
def adiff(a, b): return (a - b + 180) % 360 - 180
def U(off): return np.radians(adiff(az, AZC + off)) * RR

def c(*v): return np.array(v, np.float32)
SHELL = c(194, 130, 68); SHELL_DK = c(176, 116, 58); INNER = c(194, 128, 62)
out = np.zeros_like(O)

wall_out = (rad > 0.2) & (z < 0.43) & (r > 0.33)
rim_out = (rad > 0.2) & (z >= 0.43) & (r > 0.44) & (nz < 0.6)
rim_top = (nz >= 0.6) & (r > 0.44) & (z > 0.5)
under = nz < -0.5
inner = (rad < -0.3) & (z > 0.43) & (r > 0.36) & ~rim_top & ~under
rest = ~(wall_out | rim_out | rim_top | under | inner)
print('classes', wall_out.sum(), rim_out.sum(), rim_top.sum(), under.sum(), inner.sum(), rest.sum())

# --- region S: straws, ice, drink by nearest palette centroid of the ORIGINAL colour
reps = {'mag': c(215, 35, 125), 'lime': c(130, 205, 20), 'org': c(250, 120, 30), 'blue': c(40, 150, 230),
        'white': c(238, 238, 232), 'ice': c(160, 166, 168), 'drink': c(215, 170, 105), 'shell': c(171, 93, 17)}
outc = {'mag': c(255, 40, 150), 'lime': c(100, 232, 50), 'org': c(255, 138, 52), 'blue': c(45, 155, 255),
        'white': c(250, 248, 240), 'ice': c(168, 202, 228), 'drink': c(238, 216, 152), 'shell': c(238, 216, 152)}
names = list(reps)
Or = O[rest]
dist = np.stack([((Or - reps[n]) ** 2).sum(1) for n in names], 1)
cls = dist.argmin(1)
res = np.zeros_like(Or)
for i, n in enumerate(names): res[cls == i] = outc[n]
# drink cream only where the surface faces up; side-facing leftovers get the shell tan
upf = nz[rest] > 0.2
dr = np.isin(cls, [names.index('drink'), names.index('shell')])
res[dr & ~upf] = INNER
out[rest] = res

# --- inner wall: smooth tan, two faint rings, dried amber foam ring
out[inner] = INNER
zi = z[inner]; tmp = out[inner]
for zr in (0.565, 0.60):
    tmp[np.abs(zi - zr) < 0.004] *= 0.95
foam = np.abs(zi - 0.505) < 0.016
tmp[foam] = c(214, 168, 64)
crust = (np.abs(zi - 0.523) < 0.004) | ((np.abs(zi - 0.488) < 0.003))
tmp[crust] = c(240, 220, 150)
out[inner] = tmp

# --- rim top
out[rim_top] = SHELL
ht = rim_top & (np.abs(adiff(az, AZC - 42)) < 38)
out[ht] = c(238, 196, 132)
out[under] = SHELL_DK

# --- outer wall + rim sides: flat shell, husk blotches
body = wall_out | rim_out
out[body] = SHELL
zb_ = z[body]; ub = np.radians(adiff(az[body], AZC)) * RR
tmp = out[body]
for _ in range(9):
    cu = rng.uniform(-1.4, 1.4) if False else np.radians(rng.uniform(-180, 180)) * RR
    cz = rng.uniform(0.08, 0.36)
    # blob in wrapped arc coordinates
    du = np.radians(adiff(az[body], np.degrees(cu / RR) + AZC)) * RR
    dd = np.hypot(du / rng.uniform(0.05, 0.09), (zb_ - cz) / rng.uniform(0.035, 0.06))
    a = np.clip(1.2 - dd, 0, 1) ** 1.5 * 0.32
    tmp = tmp * (1 - a[:, None]) + SHELL_DK * a[:, None] * 0.97
out[body] = tmp

def seg_dist(px, pz, a, b):
    ax, az_ = a; bx, bz = b
    dx, dz = bx - ax, bz - az_
    t = np.clip(((px - ax) * dx + (pz - az_) * dz) / max(dx * dx + dz * dz, 1e-9), 0, 1)
    return np.hypot(px - (ax + t * dx), pz - (az_ + t * dz))

def outlined(fn, w=0.007):
    def g(u, v):
        m = fn(u, v)
        for k in range(8):
            th = k * math.pi / 4; m = np.maximum(m, fn(u + w * math.cos(th), v + w * math.sin(th)))
        return m
    return g

def paint_window(mask_extra, off, fn, col, alpha=1.0, zmax=0.44):
    """fn(u,v)->float mask in [0,1] evaluated on wall/rim texels inside a +-26 deg azimuth window."""
    sel = body & (np.abs(adiff(az, AZC + off)) < 26) & mask_extra & (z < zmax)
    u = np.radians(adiff(az[sel], AZC + off)) * RR; v = z[sel]
    m = np.clip(fn(u, v), 0, 1) * alpha
    cur = out[sel]
    out[sel] = cur * (1 - m[:, None]) + col * m[:, None]

ALL = np.ones_like(z, bool)
def soft(dist, edge=0.004): return np.clip(1 - dist / edge, 0, 1) if False else np.clip((0 - dist) / edge + 0.5, 0, 1)

# highlight streak (cheap gloss) on the left wall
def hl(u, v):
    return soft(np.abs(u) - 0.017, 0.012) * soft(np.maximum(v - 0.36, 0.06 - v), 0.03) * 0.85
# (painted highlight streak removed: gloss now comes from the material)

# spill streak, cream-gold, with a bulb at the end
def spill(u, v):
    m = soft(np.abs(u) - 0.008, 0.004) * soft(np.maximum(v - 0.47, 0.065 - v), 0.004)
    bulb = soft(np.hypot(u, v - 0.052) - 0.022, 0.005)
    return np.maximum(m, bulb)
paint_window(ALL, -42, spill, c(238, 204, 122))

# hibiscus (magenta), one petal smeared
def hib(u, v):
    dx, dz = u, v - 0.215
    rr = np.hypot(dx, dz); th = np.arctan2(dz, dx)
    edge = 0.115 * (0.62 + 0.38 * np.abs(np.cos(2.5 * (th - 1.2))) ** 0.6)
    return soft(rr - edge, 0.006)
def hib_throat(u, v):
    return soft(np.hypot(u, v - 0.215) - 0.05, 0.006)
def hib_stamen(u, v):
    return soft(np.hypot(u - 0.006, v - 0.215) - 0.016, 0.004)
def smear(u, v):
    # one petal dragged outward: pale streak
    return soft(seg_dist(u, v, (0.035, 0.235), (0.1, 0.275)) - 0.012, 0.005) * 0.75
paint_window(ALL, -30, outlined(hib), c(120, 62, 40), 0.7)
paint_window(ALL, -30, hib, c(255, 38, 150))
paint_window(ALL, -30, hib_throat, c(200, 10, 110))
paint_window(ALL, -30, hib_stamen, c(255, 214, 80))
paint_window(ALL, -30, smear, c(255, 120, 190))

# palm frond, laid across the seam
leaf_segs = []
for k in range(7):
    t = k / 6.0
    bx, bz = 0.02 * t, 0.09 + 0.27 * t
    L = 0.115 * (1 - 0.35 * abs(t - 0.45))
    for s in (-1, 1):
        ang = np.radians(35 + 20 * t) * s
        leaf_segs.append(((bx, bz), (bx + s * L * np.cos(np.radians(25 + 15 * t)), bz + L * np.sin(np.radians(25 + 15 * t) * 0.9) + 0.0 * ang)))
def frond(u, v):
    m = soft(seg_dist(u, v, (0.0, 0.08), (0.02, 0.37)) - 0.014, 0.004)
    for a_, b_ in leaf_segs:
        m = np.maximum(m, soft(seg_dist(u, v, a_, b_) - 0.019, 0.004))
    return m
paint_window(ALL, 4, outlined(frond), c(60, 90, 30), 0.65)
paint_window(ALL, 4, frond, c(100, 232, 50))

# orange sun, chewed off at the shoulder, with a drip
def sun(u, v):
    rr = np.hypot(u, v - 0.255)
    disc = soft(rr - 0.058, 0.005)
    bite = soft(np.hypot(u - 0.045, v - 0.295) - 0.032, 0.004)
    m = disc * (1 - bite)
    for k in range(9):
        th = np.radians(k * 40 + 10)
        a_ = (0.072 * np.cos(th), 0.255 + 0.072 * np.sin(th)); b_ = (0.118 * np.cos(th), 0.255 + 0.118 * np.sin(th))
        m = np.maximum(m, soft(seg_dist(u, v, a_, b_) - 0.013, 0.003) * (v > 0.2))
    drip = np.maximum(soft(seg_dist(u, v, (0.0, 0.2), (0.0, 0.13)) - 0.01, 0.003), soft(np.hypot(u, v - 0.12) - 0.017, 0.004))
    return np.maximum(m, drip)
paint_window(ALL, 34, outlined(sun), c(120, 62, 30), 0.7)
paint_window(ALL, 34, sun, c(255, 128, 28))

# mould seam through the frond
def seam(u, v):
    return soft(np.abs(u) - 0.0035, 0.002) * soft(np.maximum(v - 0.43, 0.04 - v), 0.003) * 0.9
paint_window(ALL, 4, seam, c(108, 66, 28))

# yellowed tape over the crack, with a dark crack line
def crack(u, v):
    return soft(np.abs(u) - 0.003, 0.002) * soft(np.maximum(v - 0.46, 0.33 - v), 0.003)
def tape(u, v):
    return soft(np.maximum(np.abs(u) - 0.055, np.abs(v - 0.405) - 0.03), 0.004)
paint_window(ALL, 4, crack, c(70, 44, 22), 0.9)
paint_window(ALL, 4, tape, c(228, 184, 76), 0.92)

# sticker with brown glue shadow, bottom-left of the rim
def glue(u, v):
    return soft(np.maximum(np.abs(u + 0.006) - 0.082, np.abs(v - 0.412 + 0.008) - 0.054), 0.005)
def sticker(u, v):
    return soft(np.maximum(np.abs(u) - 0.07, np.abs(v - 0.418) - 0.044), 0.004)
paint_window(ALL, -52, glue, c(92, 58, 28), 0.85)
paint_window(ALL, -52, sticker, c(244, 240, 230))

# coral lipstick smear on the rim, right
def lip(u, v):
    a = soft(np.hypot(u / 1.7, v - 0.47) - 0.032, 0.006)
    b = soft(seg_dist(u, v, (-0.03, 0.455), (0.045, 0.49)) - 0.009, 0.004) * 0.8
    return np.maximum(a, b)
paint_window(ALL, 44, lip, c(222, 84, 94), 1.0, 0.6)

# ejector-pin dots and sink dimple
def pin(u, v):
    return soft(np.hypot(u, v - 0.075) - 0.014, 0.003)
def pin_ring(u, v):
    return soft(np.hypot(u, v - 0.075) - 0.024, 0.004) * 0.5
for off in (-12, 16):
    paint_window(ALL, off, pin_ring, c(140, 88, 38))
    paint_window(ALL, off, pin, c(66, 40, 20))
def dimple(u, v):
    rr = np.hypot(u, v - 0.22)
    return soft(rr - 0.055, 0.02) * 0.45
paint_window(ALL, 48, dimple, c(160, 98, 40))

# foot ring: plain smooth plastic, sparse sand speckle only
foot = (wall_out | under) & (z < 0.05)
sp = foot & (rng.random(z.shape) < 0.06)
out[sp] = c(232, 212, 160)

# write back
img = np.zeros((4096 * 4096, 3), np.uint8); img[:] = SHELL.astype(np.uint8)
img[idx] = np.clip(out, 0, 255).astype(np.uint8)
img = img.reshape(4096, 4096, 3)
# bleed island borders by 4 texels so filtering does not pull in the background
from PIL import ImageFilter
m = Image.fromarray((ok * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))
im = Image.fromarray(img)
bl = im.filter(ImageFilter.BoxBlur(3))
a = np.array(m)[..., None] > 0
fin = np.where(ok[..., None], img, np.where(a, np.array(bl), img))
Image.fromarray(fin.astype(np.uint8)).save('tex_new.png')
Image.fromarray(fin.astype(np.uint8)).resize((1024, 1024)).save('tex_new_s.png')
print('texture written')




