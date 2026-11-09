"""aa_bible_cam (mason, dev/aa_team/interfaces.json) as a pure-Python pinhole model.

Maps pixels of crop 04 (which sits at bible px offset CROP04_OFFSET, located by template match)
to points on a chosen facade-parallel plane y = const (metres, Blender frame), and back.
No bpy / numpy needed.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
INTERFACES = HERE.parents[4] / "dev/aa_team/interfaces.json"
CROP04_OFFSET = (2296, 2099)      # crop04 (0,0) in bible px (exact match)


def _rot(rx, ry, rz):
    cx, sx, cy, sy, cz, sz = math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)
    Rx = [[1, 0, 0], [0, cx, -sx], [0, sx, cx]]
    Ry = [[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]
    Rz = [[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]]
    mm = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    return mm(Rz, mm(Ry, Rx))


class BibleCam:
    def __init__(self):
        cam = json.loads(INTERFACES.read_text(encoding="utf-8"))["camera"]
        self.loc = cam["location"]
        self.R = _rot(*[math.radians(a) for a in cam["rotation_euler_xyz_deg"]])
        self.W, self.H = cam["resolution"]
        self.f = cam["lens_mm"] / cam["sensor_width_mm"] * self.W
        self.cx, self.cy = self.W / 2.0, self.H / 2.0
        self.spec = cam

    def ray(self, u, v):
        d = ((u - self.cx) / self.f, -(v - self.cy) / self.f, -1.0)
        R = self.R
        return [sum(R[i][k] * d[k] for k in range(3)) for i in range(3)]

    def crop_to_plane(self, uc, vc, y_plane):
        """crop04 px -> (x, z) on the plane y = y_plane."""
        u, v = uc + CROP04_OFFSET[0], vc + CROP04_OFFSET[1]
        d = self.ray(u, v)
        t = (y_plane - self.loc[1]) / d[1]
        return (self.loc[0] + t * d[0], self.loc[2] + t * d[2])

    def world_to_crop(self, p):
        R = self.R
        q = [p[i] - self.loc[i] for i in range(3)]
        c = [sum(R[k][i] * q[k] for k in range(3)) for i in range(3)]     # R^T q
        u = self.cx + self.f * c[0] / -c[2]
        v = self.cy - self.f * c[1] / -c[2]
        return (u - CROP04_OFFSET[0], v - CROP04_OFFSET[1])


# ---- my rectified canvas (e3_trace_lib) -> crop04 px: the forward warp of e3_trace_lib.rectify
# (constants duplicated from e3_trace_lib so Blender's Python needs no PIL/scipy)
_CX, _CY, _F, _VPX, _OX = 1100.0, 1970.0, 5600.0, -16100.0, 260.0


def canvas_to_crop(xc, yc):
    th = math.atan(_F / (_CX - _VPX))
    fr = _F * math.cos(th)
    dx = (xc - _OX - _CX) / fr - math.tan(th)
    dy = (yc - _CY) / fr
    c, s = math.cos(th), math.sin(th)
    rx = c * dx + s
    rz = -s * dx + c
    return (_CX + _F * rx / rz, _CY + _F * dy / rz)


def linfit(xs, ys):
    n = len(xs)
    mx_, my_ = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx_) ** 2 for x in xs)
    sxy = sum((x - mx_) * (y - my_) for x, y in zip(xs, ys))
    a = sxy / sxx
    return a, my_ - a * mx_


def fit_region(cam, xr, yr, yref, step=50):
    """Separable linear canvas->metres map on plane y=yref, least squares over a canvas box."""
    XC, YC, X, Z = [], [], [], []
    for xc in range(xr[0], xr[1] + 1, step):
        for yc in range(yr[0], yr[1] + 1, step):
            x, z = cam.crop_to_plane(*canvas_to_crop(xc, yc), yref)
            XC.append(xc); YC.append(yc); X.append(x); Z.append(z)
    ax, bx = linfit(XC, X)
    az, bz = linfit(YC, Z)
    rx = max(abs(x - (ax * xc + bx)) for xc, x in zip(XC, X))
    rz = max(abs(z - (az * yc + bz)) for yc, z in zip(YC, Z))
    return dict(ax=ax, bx=bx, az=az, bz=bz, yref=yref, max_res=(rx, rz))
