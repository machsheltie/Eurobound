"""Check every kit asset against manifest.json and report.

Fails (blocks export):  missing uv_material/uv_bake, unapplied transforms, pivot
                        off the manifest rule, no materials, and over tri_budget
                        only where an asset has opted into one (budgets are null
                        by default: no polygon limits).
Warns:                  dims more than 15% off target, materials not in the
                        manifest, uv_bake outside 0..1.
An asset whose collection still holds a placeholder next to real meshes is
"partial": the real meshes are checked, the placeholder stands in for the rest.

Writes export/validation_report.json. With --strict, exits 1 on any failure.

Usage: blender aa_exterior.blend --background --python validate_assets.py -- [--strict]
"""

import json
import sys

import numpy as np
from pathlib import Path

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

DIM_TOL = 0.15


def check_transforms(objs):
    bad = []
    for o in objs:
        if o.parent is None and not o.matrix_world.is_identity:
            bad.append(o.name)
        elif o.parent is not None and not o.matrix_basis.is_identity:
            bad.append(o.name)
    return bad


def check_pivot(pivot, lo, hi, dims_b):
    tol = lambda i: aa.PIVOT_TOL + 0.05 * dims_b[i]  # noqa: E731
    center = [(lo[i] + hi[i]) / 2 for i in range(3)]
    problems = []
    if pivot == "ground":
        if abs(lo[2]) > aa.PIVOT_TOL:
            problems.append(f"bottom at z={lo[2]:.3f}, expected 0")
        for i, axis in ((0, "x"), (1, "y")):
            if abs(center[i]) > tol(i):
                problems.append(f"footprint center {axis}={center[i]:.3f}, expected 0")
    elif pivot == "wall":
        if abs(hi[1]) > aa.PIVOT_TOL:
            problems.append(f"back face at y={hi[1]:.3f}, expected 0 (asset must extend toward -Y)")
        for i, axis in ((0, "x"), (2, "z")):
            if abs(center[i]) > tol(i):
                problems.append(f"back face center {axis}={center[i]:.3f}, expected 0")
    elif pivot == "sill":
        if abs(center[0]) > tol(0):
            problems.append(f"center x={center[0]:.3f}, expected 0")
    # "facade" pieces are authored in building space; the origin is the rule.
    return problems


def check_uvs(objs):
    missing, out_of_bounds = [], []
    for o in objs:
        names = [uv.name for uv in o.data.uv_layers]
        for need in ("uv_material", "uv_bake"):
            if need not in names:
                missing.append(f"{o.name}:{need}")
        bake = o.data.uv_layers.get("uv_bake")
        if bake and len(bake.data):
            uv = np.empty(len(bake.data) * 2, dtype=np.float32)
            bake.data.foreach_get("uv", uv)
            if uv.min() < -1e-4 or uv.max() > 1 + 1e-4:
                out_of_bounds.append(o.name)
    return missing, out_of_bounds


def validate_asset(asset, manifest, depsgraph):
    entry = {"id": asset["id"], "budget": asset["tri_budget"], "instances": len(asset["instances"]),
             "fail": [], "warn": []}
    coll = aa.kit_collection(asset["id"])
    objs = aa.mesh_objects(coll)
    if not objs:
        entry.update(status="missing", tris=0)
        entry["fail"].append("no kit collection or no meshes; run setup_scene.py")
        return entry
    has_placeholder = any(o.get("aa_placeholder") for o in objs)
    objs = [o for o in objs if not o.get("aa_placeholder")]
    if not objs:
        entry.update(status="placeholder", tris=0)
        return entry

    entry["tris"] = sum(aa.tri_count(o, depsgraph) for o in objs)
    if asset["tri_budget"] is not None and entry["tris"] > asset["tri_budget"]:
        entry["fail"].append(f"{entry['tris']} tris > budget {asset['tri_budget']}")

    bad = check_transforms(objs)
    if bad:
        entry["fail"].append(f"unapplied transforms / not at origin: {bad}")

    dims_b = aa.blender_dims(asset["dims"])
    lo, hi = aa.world_bbox(objs)
    size = [hi[i] - lo[i] for i in range(3)]
    entry["size_xyz"] = [round(s, 3) for s in size]
    if not has_placeholder:  # a partial asset's bounds aren't the finished asset's
        entry["fail"] += check_pivot(asset["pivot"], lo, hi, dims_b)
    for i, axis in enumerate("xyz"):
        if has_placeholder:
            break
        if dims_b[i] > 0.05 and abs(size[i] - dims_b[i]) / dims_b[i] > DIM_TOL:
            entry["warn"].append(f"{axis} extent {size[i]:.2f} m vs target {dims_b[i]:.2f} m")

    missing, oob = check_uvs(objs)
    if missing:
        entry["fail"].append(f"missing UV layers: {missing}")
    if oob:
        entry["warn"].append(f"uv_bake outside 0..1: {oob}")

    mats = {s.material.name for o in objs for s in o.material_slots if s.material}
    if not mats:
        entry["fail"].append("no materials assigned")
    stray = sorted(mats - set(manifest["materials"]))
    if stray:
        entry["warn"].append(f"materials not in manifest (rebake/rename): {stray}")

    entry["status"] = "fail" if entry["fail"] else ("partial" if has_placeholder else "ok")
    return entry


def main():
    manifest = aa.load_manifest()
    depsgraph = bpy.context.evaluated_depsgraph_get()
    entries = [validate_asset(a, manifest, depsgraph) for a in manifest["assets"]]

    measured = sum(e["tris"] * e["instances"] for e in entries)
    budget = manifest["building"]["tri_budget_total"]
    report = {
        "assets": entries,
        "building_tris_measured": measured,
        "building_budget": budget,
        "building_over_budget": budget is not None and measured > budget,
        "counts": {s: sum(e["status"] == s for e in entries)
                   for s in ("ok", "partial", "fail", "placeholder", "missing")},
    }
    aa.EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    with open(aa.EXPORT_DIR / "validation_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    return report


result = main()
_failed = result["building_over_budget"] or result["counts"]["fail"] or result["counts"]["missing"]
print(json.dumps({k: v for k, v in result.items() if k != "assets"}, indent=2))
for e in result["assets"]:
    if e["fail"] or e["warn"]:
        print(f"[{e['status']}] {e['id']}: " + "; ".join(e["fail"] + e["warn"]))
if "--strict" in aa.script_args() and _failed:
    sys.exit(1)
