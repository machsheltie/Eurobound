"""aa_bible_cam (mason, dev/aa_team/interfaces.json) as a pure-Python pinhole model, in BIBLE pixels.

E4 traces straight off the full-res bible (absinthearcadedaytime.png, 5248 x 4796): a bible pixel
(u, v) is cast through aa_bible_cam onto a facade-parallel plane y = const or a horizontal plane.
Crop 05 is the bible region CROP05 = (x0, y0, sx, sy): crop px (cu, cv) -> bible (x0 + cu*sx, y0 + cv*sy).
No bpy / numpy needed (runs inside Blender too).
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
INTERFACES = REPO / "dev/aa_team/interfaces.json"
BIBLE = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/absinthearcadedaytime.png"
CROP05_PNG = REPO / "dev/aa_team/crops/05_keystone_conduits_boxes.png"
# crop 05 inside the bible: fitted by e4_align.py (least squares on a 600 x 228 sample grid)
CROP05 = (1648.0, 1214.0, 1.333, 1.333)


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
        self.spec = cam
        self.loc = cam["location"]
        self.R = _rot(*[math.radians(a) for a in cam["rotation_euler_xyz_deg"]])
        self.W, self.H = cam["resolution"]
        self.f = cam["lens_mm"] / cam["sensor_width_mm"] * self.W
        self.cx, self.cy = self.W / 2.0, self.H / 2.0

    def ray(self, u, v):
        d = ((u - self.cx) / self.f, -(v - self.cy) / self.f, -1.0)
        return [sum(self.R[i][k] * d[k] for k in range(3)) for i in range(3)]

    def to_plane_y(self, u, v, y):
        """bible px -> (x, z) on the facade-parallel plane y."""
        d = self.ray(u, v)
        t = (y - self.loc[1]) / d[1]
        return (self.loc[0] + t * d[0], self.loc[2] + t * d[2])

    def to_plane_x(self, u, v, x):
        """bible px -> (y, z) on the plane x = const (e.g. a return face)."""
        d = self.ray(u, v)
        t = (x - self.loc[0]) / d[0]
        return (self.loc[1] + t * d[1], self.loc[2] + t * d[2])

    def project(self, p):
        q = [p[i] - self.loc[i] for i in range(3)]
        c = [sum(self.R[k][i] * q[k] for k in range(3)) for i in range(3)]
        return (self.cx + self.f * c[0] / -c[2], self.cy - self.f * c[1] / -c[2])


def crop05_to_bible(cu, cv):
    x0, y0, sx, sy = CROP05
    return (x0 + cu * sx, y0 + cv * sy)


def crop05_window():
    x0, y0, sx, sy = CROP05
    return (x0, y0, x0 + 2400 * sx, y0 + 910 * sy)


def to_plane_z(cam, u, v, z):
    """bible px -> (x, y) on the horizontal plane z."""
    d = cam.ray(u, v)
    t = (z - cam.loc[2]) / d[2]
    return (cam.loc[0] + t * d[0], cam.loc[1] + t * d[1])
