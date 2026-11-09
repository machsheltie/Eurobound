"""Refine line features on the full-res bible. Modes: dark/bright ridge, edge (+ = brighter after, - = darker after)."""
import numpy as np
from PIL import Image
from PIL import ImageFilter
Image.MAX_IMAGE_PIXELS = None
from bible_cam import BIBLE as SRC  # noqa: E402  (full-res daytime bible, 5248x4796)
_L = None
def lum():
    global _L
    if _L is None:
        im = Image.open(SRC).convert("L").filter(ImageFilter.GaussianBlur(1.5))
        _L = np.asarray(im, dtype=np.float32)
    return _L

def _peak(prof, mode):
    if mode == "dark":
        v = -prof
    elif mode == "bright":
        v = prof
    else:
        d = np.gradient(prof)
        v = d if mode == "+" else -d
    i = int(np.argmax(v))
    if 0 < i < len(v) - 1:
        a, b, c = v[i - 1], v[i], v[i + 1]
        den = a - 2 * b + c
        off = 0.5 * (a - c) / den if den != 0 else 0.0
    else:
        off = 0.0
    return i + off, v[i]

def trace(p0, p1, mode, orient, band=18, step=6, width=None):
    """orient 'h': sample along x, find y. 'v': sample along y, find x.
    width: for dark/bright ridge on a thick feature, use centre of the run (half-max) instead of peak."""
    L = lum()
    (x0, y0), (x1, y1) = p0, p1
    pts = []
    if orient == "h":
        for x in np.arange(min(x0, x1), max(x0, x1) + 1, step):
            t = (x - x0) / (x1 - x0)
            yc = y0 + t * (y1 - y0)
            lo = int(round(yc - band)); hi = int(round(yc + band))
            prof = L[lo:hi + 1, int(x)]
            pk, s = _peak(prof, mode)
            pts.append((x, lo + pk, s))
    else:
        for y in np.arange(min(y0, y1), max(y0, y1) + 1, step):
            t = (y - y0) / (y1 - y0)
            xc = x0 + t * (x1 - x0)
            lo = int(round(xc - band)); hi = int(round(xc + band))
            prof = L[int(y), lo:hi + 1]
            pk, s = _peak(prof, mode)
            pts.append((lo + pk, y, s))
    return np.array(pts)

def fit(pts, orient, iters=6, k=2.5):
    """Robust line fit: 'h' -> y = a + b x ; 'v' -> x = a + b y. Returns a, b, rms, n_used, mask."""
    if orient == "h":
        u, w = pts[:, 0], pts[:, 1]
    else:
        u, w = pts[:, 1], pts[:, 0]
    m = np.ones(len(u), bool)
    for _ in range(iters):
        A = np.vstack([np.ones(m.sum()), u[m]]).T
        sol, *_ = np.linalg.lstsq(A, w[m], rcond=None)
        r = w - (sol[0] + sol[1] * u)
        s = max(1.4826 * np.median(np.abs(r[m])), 0.6)
        m = np.abs(r) < k * s
    r = w - (sol[0] + sol[1] * u)
    return sol[0], sol[1], float(np.sqrt(np.mean(r[m] ** 2))), int(m.sum()), m

def homog(a, b, orient):
    """line as homogeneous (A,B,C) with A x + B y + C = 0"""
    if orient == "h":   # y = a + b x -> b x - y + a = 0
        l = np.array([b, -1.0, a])
    else:               # x = a + b y -> x - b y - a = 0
        l = np.array([1.0, -b, -a])
    return l / np.hypot(l[0], l[1])
