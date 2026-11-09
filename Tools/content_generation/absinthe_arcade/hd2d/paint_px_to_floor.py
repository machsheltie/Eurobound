"""Map hall-v8 pixels to floor positions through the interior paint camera.

Prints (x, z) in painting units (origin mid-floor, -Z toward the back wall), the same space as
OCCLUDERS and the room outline in absinthe_arcade_interior_hd2d.gd. Use the pixel where an object
meets the floor (bottom centre of its box).

Usage: python paint_px_to_floor.py U,V [U,V ...]
"""
import math
import sys

W, H = 2752, 1536
FOCAL = 4150.0
PITCH = math.radians(29.0)
CAM_H = 14.1
CAM_Z = 22.4


def px_to_floor(u: float, v: float) -> tuple[float, float]:
    dx = (u - W / 2) / FOCAL
    dy = -(v - H / 2) / FOCAL
    # Camera looks down -Z, pitched down by PITCH (rotation about X by -PITCH).
    a = -PITCH
    wy = dy * math.cos(a) + math.sin(a)       # dz = -1
    wz = dy * math.sin(a) - math.cos(a)
    if wy >= 0:
        raise ValueError(f"pixel {u},{v} is above the horizon")
    t = CAM_H / -wy
    return dx * t, CAM_Z + wz * t


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        u, v = (float(s) for s in arg.split(","))
        x, z = px_to_floor(u, v)
        print(f"{arg}: x {x:.2f}  z {z:.2f}")
