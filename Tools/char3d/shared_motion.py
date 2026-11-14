"""Shared idle/walk library + per-character profile -> pose operations (pure python, no bpy).

Used by render_dirs.py when the config has {"rig": "shared", "profile": "<name|path>"}.
Library curves live in tools/char3d/anim_lib/{idle,walk}.json (see anim_lib/build_lib.py for the format);
profiles in tools/char3d/profiles/<id>.json:
  cycle_frames {idle, walk}   frames per loop (the game plays at a fixed fps, so fewer frames = faster cadence)
  amp {stride, knee, arm, elbow, bounce, sway, breathe}   multipliers on the library (1 = Lord Pilsner)
  phase_offset  walk sample offset in frames (default .5: no frame lands exactly on the passing or contact pose; 0 = approved Pilsner timing)
  leg_len_m   hips-drop lever (m, default .45)
  lean_deg    forward lean spread over Spine/Spine1/Spine2 (head counters it); applied in every view
  head_lift {Neck, Head} deg about the lateral axis, scaled per render direction by head_lift_by_dir
  spine_counter {bone: deg}   counter-rotation for baked swayback, scaled by |sin(view angle)| (0 front/back, 1 in profile)
  pose {bone: [x,y,z]}        static body-axis pose offsets, every frame (e.g. a bent forearm)
  rig {pocket_sides, cull_boxes, keep_radius_h}   read by shared_rig.py
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DIRS = ["S", "SE", "E", "NE", "N", "NW", "W", "SW"]
AXN = {"x": "bx", "y": "by", "z": "z"}


def _cr(k, t):
    n = len(k)
    x = (t % 1.0) * n
    i = int(math.floor(x))
    f = x - i
    p0, p1, p2, p3 = k[(i - 1) % n], k[i % n], k[(i + 1) % n], k[(i + 2) % n]
    return 0.5 * (2 * p1 + (-p0 + p2) * f + (2 * p0 - 5 * p1 + 4 * p2 - p3) * f * f + (-p0 + 3 * p1 - 3 * p2 + p3) * f ** 3)


class Motion:
    def __init__(self, profile):
        pp = profile if os.path.isfile(profile) else os.path.join(HERE, "profiles", profile + ".json")
        self.p = json.load(open(pp))
        self.lib = {k: json.load(open(os.path.join(HERE, "anim_lib", k + ".json"))) for k in ("idle", "walk")}
        self.amp = {"stride": 1, "knee": 1, "arm": 1, "elbow": 1, "bounce": 1, "sway": 1, "breathe": 1}
        self.amp.update(self.p.get("amp", {}))

    def frames(self, anim, default):
        return self.p.get("cycle_frames", {}).get(anim, default)

    def _val(self, ch, t):
        return sum(self.amp[pt["group"]] * _cr(pt["keys"], t) for pt in ch["parts"])

    def ops(self, anim, i, n):
        """-> (rot [(bone, axis, deg)], move [(bone, dz m)]) for frame i of n."""
        lib = self.lib[anim]
        off = self.p.get("phase_offset", 0.5) if anim == "walk" else 0.0   # frames; .5 = no frame on the exact passing/contact pose
        t = (i + off) / float(n)
        rot = [(c["bone"], AXN[c["axis"]], self._val(c, t)) for c in lib["rot"]]
        mv = [(c["bone"], self._val(c, t)) for c in lib.get("move", [])]
        d = lib.get("drop")
        if d:
            L = self.p.get("leg_len_m", 0.45)
            vals = {b: v for b, ax, v in rot if b in d["legs"] and ax == "bx"}
            dz = min(-L * (1 - math.cos(math.radians(abs(v)))) for v in vals.values())
            mv = [(b, z + dz) if b == d["bone"] else (b, z) for b, z in mv]
        return rot, mv

    def static(self, dname):
        """Static body-axis rotations {bone: [x,y,z]} for render direction dname."""
        p = self.p
        out = {}

        def add(b, x=0.0, y=0.0, z=0.0):
            o = out.setdefault(b, [0.0, 0.0, 0.0])
            o[0] += x
            o[1] += y
            o[2] += z
        k = p.get("head_lift_by_dir", {}).get(dname, 1.0)
        for b, v in p.get("head_lift", {}).items():
            add(b, v * k)
        sway = abs(math.sin(math.radians(45 * DIRS.index(dname))))
        for b, v in p.get("spine_counter", {}).items():
            add(b, v * sway)
        lean = p.get("lean_deg", 0.0)
        if lean:
            for b in ("Spine", "Spine1", "Spine2"):
                add(b, lean / 3.0)
            add("Neck", -0.4 * lean)
            add("Head", -0.6 * lean)
        for b, v in p.get("pose", {}).items():
            add(b, *v)
        return out
