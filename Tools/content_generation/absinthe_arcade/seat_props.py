"""Seat wall-mounted props on the stone they are fixed to, and write manifest.json.

The facade has depth planes (rustication, central bay, lesenes, cornices), so a
prop placed at the old flat wall plane ends up buried or floating. For each
instance of a wall-pivot asset this raycasts the stone at the points where the
kit mesh's back touches the wall and sets the instance's street depth (engine z)
so the back sits on the most-proud face it covers. Run build_shell.py first and
setup_scene.py after (it re-places the layout from the manifest).

Window crests are left alone: they sit on the pediments by design.
"""

import json
import sys
from pathlib import Path

import bpy
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402
from build_fittings import Facade  # noqa: E402

SEATED = ("aa_prop_wall_lantern", "aa_prop_awning", "aa_prop_hanging_sign", "aa_prop_doorframe_sign",
          "aa_prop_house_number", "aa_ornament_rosette_painted")
GAP = 0.003
MAX_CONTACTS = 160


def contacts(asset_id):
    """(x, z) offsets of the kit mesh's back-face vertices, and the back plane's y."""
    pts = []
    for o in aa.mesh_objects(aa.kit_collection(asset_id)):
        n = len(o.data.vertices)
        a = np.empty(n * 3)
        o.data.vertices.foreach_get("co", a)
        a = a.reshape(-1, 3)
        m = np.array(o.matrix_world)
        pts.append(a @ m[:3, :3].T + m[:3, 3])
    pts = np.vstack(pts)
    back = pts[:, 1].max()
    c = pts[pts[:, 1] > back - 0.02]
    if len(c) > MAX_CONTACTS:
        c = c[np.linspace(0, len(c) - 1, MAX_CONTACTS).astype(int)]
    return [(float(x), float(z)) for x, _, z in c], float(back)


def main():
    face = Facade()
    with open(aa.MANIFEST_PATH, encoding="utf-8") as f:
        manifest = json.load(f)
    moved = {}
    for asset in manifest["assets"]:
        if asset["id"] not in SEATED:
            continue
        offs, back = contacts(asset["id"])
        for k, inst in enumerate(asset["instances"]):
            bx, _, bz = aa.to_blender(inst["pos"])
            wall = min(face.surf(bx + dx, bz + dz) for dx, dz in offs)
            depth = round(-(wall - GAP - back), 3)
            moved[f"{asset['id']}#{k}"] = [inst["pos"][2], depth]
            inst["pos"][2] = depth
    with open(aa.MANIFEST_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(manifest, indent=2, ensure_ascii=False))
    return moved


if __name__ == "__main__" or "AA_RUN" in globals():
    result = main()
    print(result)
