"""aa_bible_cam as a pinhole in bible pixels (5248x4796): world (Blender metres) <-> pixel.

proj(P) -> (u, v); ray(u, v); to_plane_y(u, v, y) / to_plane_x(u, v, x) back-project a pixel onto a
facade-parallel or side-parallel plane. Camera from manifest.json -> bible_camera. numpy only.
"""
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
BIBLE = str(REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/absinthearcadedaytime.png")
CAM = json.loads((HERE.parent / "manifest.json").read_text(encoding="utf-8"))["bible_camera"]
def _rot(rx, ry, rz):
    cx, sx, cy, sy, cz, sz = map(float, (math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)))
    Rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    Rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return Rz @ Ry @ Rx
L = np.array(CAM["location"]); R = _rot(*[math.radians(a) for a in CAM["rotation_euler_xyz_deg"]])
W, H = CAM["resolution"]; F = CAM["lens_mm"] / CAM["sensor_width_mm"] * W
def proj(P):
    P = np.atleast_2d(np.asarray(P, float))
    c = (P - L) @ R           # R^T q
    return np.stack([W / 2 + F * c[:, 0] / -c[:, 2], H / 2 - F * c[:, 1] / -c[:, 2]], 1)
def ray(u, v):
    d = np.array([(u - W / 2) / F, -(v - H / 2) / F, -1.0])
    return R @ d
def to_plane_y(u, v, y):
    d = ray(u, v); t = (y - L[1]) / d[1]; p = L + t * d; return p
def to_plane_x(u, v, x):
    d = ray(u, v); t = (x - L[0]) / d[0]; p = L + t * d; return p
