"""Rectify the daytime bible onto the facade plane through aa_bible_cam (plain Python: numpy, scipy, Pillow).

Facade sheet coordinates: x (m, right) and z (m, up) on the plane y = Y_PLANE (Blender frame, arch axis x=0).
  rectify_bible(x0, x1, z0, z1, ppm) -> HxWx3 float image (row 0 = z1, top)
Used by e5_mural.py to fit the mural and to extend it, and for stone/compare crops.
"""
import json
import math
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
INTERFACES = REPO / "dev/aa_team/interfaces.json"
BIBLE = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/absinthearcadedaytime.png"
Y_PLANE = 0.0


def _rot(rx, ry, rz):
    cx, sx, cy, sy, cz, sz = math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)
    Rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    Rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return Rz @ Ry @ Rx


class Cam:
    def __init__(self):
        c = json.loads(INTERFACES.read_text(encoding="utf-8"))["camera"]
        self.loc = np.array(c["location"])
        self.R = _rot(*[math.radians(a) for a in c["rotation_euler_xyz_deg"]])
        self.W, self.H = c["resolution"]
        self.f = c["lens_mm"] / c["sensor_width_mm"] * self.W

    def project(self, P):
        """P: (..., 3) world points -> (u, v) bible px arrays."""
        q = P - self.loc
        c = q @ self.R              # R^T q per point
        u = self.W / 2 + self.f * c[..., 0] / -c[..., 2]
        v = self.H / 2 - self.f * c[..., 1] / -c[..., 2]
        return u, v


_BIBLE = None


def bible():
    global _BIBLE
    if _BIBLE is None:
        Image.MAX_IMAGE_PIXELS = None
        _BIBLE = np.asarray(Image.open(BIBLE).convert("RGB")).astype(np.float32) / 255.0
    return _BIBLE


def sheet_grid(x0, x1, z0, z1, ppm):
    W = int(round((x1 - x0) * ppm))
    H = int(round((z1 - z0) * ppm))
    xs = x0 + (np.arange(W) + 0.5) / ppm
    zs = z1 - (np.arange(H) + 0.5) / ppm
    X, Z = np.meshgrid(xs, zs)
    return X, Z


def rectify_bible(x0, x1, z0, z1, ppm, y=Y_PLANE, order=1):
    cam = Cam()
    X, Z = sheet_grid(x0, x1, z0, z1, ppm)
    P = np.stack([X, np.full_like(X, y), Z], -1)
    u, v = cam.project(P)
    B = bible()
    out = np.zeros(X.shape + (3,), np.float32)
    for ch in range(3):
        out[..., ch] = ndi.map_coordinates(B[..., ch], [v - 0.5, u - 0.5], order=order, mode="constant", cval=0)
    valid = (u >= 0) & (u < cam.W) & (v >= 0) & (v < cam.H)
    return out, valid


def save(img, path):
    Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)).save(path)


if __name__ == "__main__":
    import sys
    out = sys.argv[1]
    img, _ = rectify_bible(-6.0, 3.4, 0.0, 14.0, 120)
    save(img, out)
    print(img.shape)
