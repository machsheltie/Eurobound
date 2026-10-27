"""Export every kit asset as its own file, plus the assembly layout.

  export/glb/<asset_id>.glb   glTF 2.0, Y-up, modifiers applied, tangents included
  export/fbx/<asset_id>.fbx   FBX, -Z forward / Y up, scale baked (Unity-friendly)
  export/aa_layout.json       every aa_layout instance in engine space (Y-up), so any
                              engine can rebuild the storefront from the kit pieces

Runs validate_assets.py first and skips failing assets unless --force. Placeholders
are skipped unless --allow-placeholders (useful for a greybox engine import).

Usage: blender aa_exterior.blend --background --python export_assets.py -- \
           [--only id,id] [--formats glb,fbx] [--force] [--allow-placeholders]
"""

import argparse
import json
import math
import runpy
import sys
from pathlib import Path

import bpy

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import aa_common as aa  # noqa: E402


def select_only(objs):
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]


def export_glb(path, objs):
    select_only(objs)
    bpy.ops.export_scene.gltf(filepath=str(path), export_format="GLB", use_selection=True,
                              export_yup=True, export_apply=True, export_texcoords=True,
                              export_normals=True, export_tangents=True,
                              export_materials="EXPORT")


def export_fbx(path, objs):
    select_only(objs)
    bpy.ops.export_scene.fbx(filepath=str(path), use_selection=True, object_types={"MESH"},
                             apply_unit_scale=True, apply_scale_options="FBX_SCALE_ALL",
                             axis_forward="-Z", axis_up="Y", bake_space_transform=True,
                             use_mesh_modifiers=True, mesh_smooth_type="FACE", use_tspace=True,
                             add_leaf_bones=False, path_mode="AUTO")


def layout_entries():
    out = []
    coll = bpy.data.collections.get(aa.LAYOUT_COLL)
    for e in sorted(coll.objects if coll else [], key=lambda o: o.name):
        aid = e.get("aa_asset_id")
        if not aid:
            continue
        rx, ry, rz = e.rotation_euler
        entry = {"instance": e.name, "asset_id": aid,
                 "glb": f"glb/{aid}.glb", "fbx": f"fbx/{aid}.fbx",
                 "position": [round(c, 4) for c in aa.to_engine(e.location)],
                 "yaw_deg": round(math.degrees(rz), 3),
                 "scale": [round(e.scale[0], 4)] * 3}
        if abs(rx) > 1e-4 or abs(ry) > 1e-4:
            entry["warning"] = "non-yaw rotation ignored"
        if any(abs(s - e.scale[0]) > 1e-4 for s in e.scale):
            entry["warning"] = "non-uniform scale ignored"
        out.append(entry)
    return out


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--formats", default="glb,fbx")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--allow-placeholders", action="store_true")
    args = ap.parse_args(argv)
    formats = set(args.formats.split(","))
    only = set(filter(None, args.only.split(",")))

    report = runpy.run_path(str(HERE / "validate_assets.py"), run_name="aa_validate")["result"]
    status = {e["id"]: e["status"] for e in report["assets"]}

    layer = aa.find_layer_collection(aa.KIT_COLL)
    was_hidden = layer.hide_viewport if layer else False
    if layer:
        layer.hide_viewport = False
    exported, skipped = [], {}
    try:
        for asset in aa.load_manifest()["assets"]:
            aid = asset["id"]
            if only and aid not in only:
                continue
            st = status.get(aid, "missing")
            if st == "missing" or (st == "fail" and not args.force) or \
                    (st == "placeholder" and not args.allow_placeholders):
                skipped[aid] = st
                continue
            objs = aa.mesh_objects(aa.kit_collection(aid))
            if st == "partial":  # ship the finished parts, not the stand-in box
                objs = [o for o in objs if not o.get("aa_placeholder")]
            for fmt, fn in (("glb", export_glb), ("fbx", export_fbx)):
                if fmt in formats:
                    (aa.EXPORT_DIR / fmt).mkdir(parents=True, exist_ok=True)
                    fn(aa.EXPORT_DIR / fmt / f"{aid}.{fmt}", objs)
            exported.append(aid)
    finally:
        if layer:
            layer.hide_viewport = was_hidden

    layout = {"units": "meters", "up": "+Y", "facade_faces": "+Z", "instances": layout_entries()}
    with open(aa.EXPORT_DIR / "aa_layout.json", "w", encoding="utf-8") as f:
        json.dump(layout, f, indent=2)
    return {"exported": exported, "skipped": skipped,
            "building_tris_measured": report["building_tris_measured"],
            "layout_instances": len(layout["instances"])}


if __name__ == "__main__":
    result = main(aa.script_args())
    print(result)
