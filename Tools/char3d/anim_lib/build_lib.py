"""Regenerates idle.json and walk.json (pure python): python tools/char3d/anim_lib/build_lib.py

Baseline = Lord Pilsner's approved procedural breathe/walk from render_dirs.py (walk_stride 14, walk_arm 38,
walk_elbow 22, knee 38, bob .004 m, breathe pitch 1.2 deg, rise .004 m). Profile amp multipliers of 1.0 reproduce it.

Format: {"name", "keys": N samples per cycle (periodic, Catmull-Rom between them),
 "rot":  [{"bone", "axis": x|y|z (BODY axes: x lateral/pitch, y front-back/roll, z up/twist), "parts":[{"group","keys":[deg]}]}],
 "move": [{"bone", "parts":[{"group","keys":[m]}]}]  (vertical, armature z),
 "drop": {"bone", "legs":[bones whose x-rotation lifts the hips]}  (hips sink L*(1-cos(thigh angle)), L = profile leg_len_m)}
Channel value = sum(amp[group] * curve(t)), t = frame / cycle_frames in 0..1.
"""
import json, math, os
N = 24
HERE = os.path.dirname(os.path.abspath(__file__))
A, K, AA, E, BOB = 14.0, 38.0, 38.0, 22.0, 0.004


def curve(f):
    return [round(f(2 * math.pi * i / N), 5) for i in range(N)]


def part(g, f):
    return {"group": g, "keys": curve(f)}


rot, move = [], []
for side, off in (("Left", 0.0), ("Right", math.pi)):
    c = lambda ph, off=off: ph + off
    rot += [
        {"bone": side + "UpLeg", "axis": "x", "parts": [part("stride", lambda ph, c=c: -A * math.sin(c(ph)))]},
        {"bone": side + "Leg", "axis": "x", "parts": [part("knee", lambda ph, c=c: K * max(0.0, math.cos(c(ph))) ** 1.5 + 4)]},
        {"bone": side + "Foot", "axis": "x", "parts": [
            part("stride", lambda ph, c=c: 0.8 * A * math.sin(c(ph))),
            part("knee", lambda ph, c=c: -0.8 * (K * max(0.0, math.cos(c(ph))) ** 1.5 + 4))]},
        {"bone": side + "Arm", "axis": "x", "parts": [part("arm", lambda ph, c=c: AA * math.sin(c(ph)))]},
        {"bone": side + "ForeArm", "axis": "x", "parts": [part("elbow", lambda ph, c=c: -E - 4 * max(0.0, -math.sin(c(ph))))]},
    ]
rot += [{"bone": "Spine1", "axis": "z", "parts": [part("sway", lambda ph: 2.5 * math.sin(ph))]},
        {"bone": "Hips", "axis": "z", "parts": [part("sway", lambda ph: -3 * math.sin(ph))]}]
move = [{"bone": "Hips", "parts": [part("bounce", lambda ph: BOB * math.cos(2 * ph) - BOB)]}]
walk = {"name": "walk", "keys": N, "rot": rot, "move": move, "drop": {"bone": "Hips", "legs": ["LeftUpLeg", "RightUpLeg"]}}

idle = {"name": "idle", "keys": N, "rot": [
    {"bone": "Spine", "axis": "x", "parts": [part("breathe", lambda ph: -0.6 * math.sin(ph))]},
    {"bone": "Spine1", "axis": "x", "parts": [part("breathe", lambda ph: -1.2 * math.sin(ph))]}],
    "move": [{"bone": "Spine2", "parts": [part("breathe", lambda ph: 0.004 * math.sin(ph))]},
             {"bone": "LeftShoulder", "parts": [part("breathe", lambda ph: 0.0024 * math.sin(ph))]},
             {"bone": "RightShoulder", "parts": [part("breathe", lambda ph: 0.0024 * math.sin(ph))]}]}
for d in (walk, idle):
    json.dump(d, open(os.path.join(HERE, d["name"] + ".json"), "w"), separators=(",", ":"))
print("wrote idle.json walk.json")
