"""E3 layout: rectified-crop pixels -> metres, anchored on mason's aa_bible_cam (interfaces.json).

Runs inside Blender or plain Python (no bpy import).

Every traced coordinate is a pixel of my rectified crop-04 canvas (e3_trace_lib.rectified).
Mapping to the building frame (Blender: x right, -Y street, z up; origin = arch axis on the facade
plane at street level, pivot "facade"):
  canvas -> crop04 px (inverse of my rectification) -> ray of aa_bible_cam -> plane y = const.
Built geometry must stay rectilinear, so per region the projection is fitted with a separable
linear map on a reference plane (fit residuals are reported), then rescaled about the camera to
the depth plane each part actually sits on. That keeps parts that stand proud of the board
(letters, banner) where the bible shows them from the bible camera.
Fits to mason's numbers:
  marquee : kept where the bible camera puts it (its skull is ~0.06 m right of the arch axis;
            the board spans the jambs within a few cm and hangs in front of the stone)
  doorway : left edge kept at the bible position, right edge pulled in to the masonry jamb
            (arch.jamb_x): the bible draws the assembly overlapping the right jamb.
"""
import json
from pathlib import Path

from e3_bible_cam import BibleCam, canvas_to_crop, fit_region

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
INTERFACES = REPO / "dev/aa_team/interfaces.json"
TRACE = HERE / "trace" / "e3_trace.json"
TEX = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/textures/e3_entrance"
WIP = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/E3_entrance.blend"

IFACE = json.loads(INTERFACES.read_text(encoding="utf-8"))
ARCH = IFACE["arch"]
CAM = BibleCam()
CAMX, CAMY, CAMZ = CAM.loc

SKULL_XC = 1270                      # canvas column of the apex skull
DOOR_XC = (300, 2495)                # canvas columns of the doorway assembly's outer edges

REGIONS = {
    "marquee": fit_region(CAM, (190, 2350), (90, 900), -0.30),
    "door": fit_region(CAM, (300, 2500), (900, 2220), 0.0),
}
_m = REGIONS["marquee"]
MARQUEE_AXIS_OFFSET = _m["ax"] * SKULL_XC + _m["bx"] - ARCH["axis_x"]   # bible skull vs arch axis (kept)
_d = REGIONS["door"]
_jl, _jr = ARCH["jamb_x"]
_bible_l = _d["ax"] * DOOR_XC[0] + _d["bx"]
_bible_r = _d["ax"] * DOOR_XC[1] + _d["bx"]
# keep the left edge where the bible has it (inside the jamb: the bible shows stone + conduits
# between jamb and frame) and pull the right edge in to the masonry jamb
_left = max(_bible_l, _jl)
_d["ax"] = (_jr - _left) / (DOOR_XC[1] - DOOR_XC[0])
_d["bx"] = _left - _d["ax"] * DOOR_XC[0]
DOOR_SHIFT = 0.0
DOOR_FIT = dict(bible_left=_bible_l, bible_right=_bible_r, left=_left, right=_jr)
K = 1.0 / _m["ax"]                   # px per metre (marquee, for widths in px)

_R = "marquee"
_YP = REGIONS["marquee"]["yref"]
FIT_NOTE = (f"aa_bible_cam fit: marquee res {REGIONS['marquee']['max_res'][0]:.3f}/{REGIONS['marquee']['max_res'][1]:.3f} m,"
            f" doorway res {REGIONS['door']['max_res'][0]:.3f}/{REGIONS['door']['max_res'][1]:.3f} m,"
            f" doorway bible x {_bible_l:.3f}..{_bible_r:.3f} -> {_left:.3f}..{_jr:.3f};"
            f" marquee kept at bible x (skull {MARQUEE_AXIS_OFFSET:+.3f} m off the arch axis)")


def use(region, yp=None):
    """Select region map and depth plane for the following mx/mz/px calls."""
    global _R, _YP
    _R = region
    _YP = REGIONS[region]["yref"] if yp is None else yp


def plane(yp):
    global _YP
    _YP = yp


def _s():
    r = REGIONS[_R]
    return (_YP - CAMY) / (r["yref"] - CAMY)


def mx(x):
    r = REGIONS[_R]
    return CAMX + (r["ax"] * x + r["bx"] - CAMX) * _s()


def mz(y):
    r = REGIONS[_R]
    return CAMZ + (r["az"] * y + r["bz"] - CAMZ) * _s()


def px(x, y):
    return (mx(x), mz(y))


def mw(w):
    return abs(REGIONS[_R]["ax"]) * w * _s()


def mh(h):
    return abs(REGIONS[_R]["az"]) * h * _s()


def ipx(xc, yc, yp):
    """Exact per-point projection (interior set): canvas -> plane y=yp through aa_bible_cam."""
    x, z = CAM.crop_to_plane(*canvas_to_crop(xc, yc), yp)
    return (x + DOOR_SHIFT, z)


def load_trace():
    return json.loads(TRACE.read_text())


def ipz(xc, yc, z):
    """Exact per-point projection onto the horizontal plane at height z -> (x, y)."""
    u, v = canvas_to_crop(xc, yc)
    d = CAM.ray(u + 2296, v + 2099)
    t = (z - CAMZ) / d[2]
    return (CAMX + t * d[0] + DOOR_SHIFT, CAMY + t * d[1])


# ---- interior forced perspective (author ruling Q-011: building ~4.0 m deep, set within ~3.4 m) ----
# The hall is modelled at its natural depth (to INT_SRC_MAX), then every vertex slides along its
# aa_bible_cam ray until the depth fits INT_Y0..INT_DST_MAX. From the bible camera the image is
# unchanged; far parts come out smaller, the floor rises and the ceiling drops toward the back.
INT_Y0 = 0.34
INT_SRC_MAX = 7.7
_iface_depth = (IFACE.get("interior") or {}).get("set_depth") or (IFACE.get("building") or {}).get("interior_set_depth")
INT_DST_MAX = INT_Y0 + (_iface_depth or 3.4)


def compress(p):
    x, y, z = p
    if y <= INT_Y0:
        return (x, y, z)
    y2 = INT_Y0 + (y - INT_Y0) * (INT_DST_MAX - INT_Y0) / (INT_SRC_MAX - INT_Y0)
    t = (y2 - CAMY) / (y - CAMY)
    return (CAMX + (x - CAMX) * t, y2, CAMZ + (z - CAMZ) * t)
