"""Protocol step 3: build manifests/<asset_id>.json from segment.json plus the zone file's descriptive fields.

Usage: python tools/paint_zones/build_manifest.py tools/paint_zones/zones/<id>_ref.json
Descriptive fields per zone in the zones file (all optional): label, pattern, finish, wear, markings,
observed ("direct"|"inferred"), inferred_from, library_ref, projection, notes. Top level: height_m, unseen, fallbacks.
Colours always come from segment.json (sampled pixels), never from the zones file.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
z = json.load(open(sys.argv[1]))
aid = z["asset_id"]
seg = json.load(open(os.path.join(HERE, "work", aid, "segment.json")))
reg = json.load(open(os.path.join(HERE, "refs", "registry.json")))["assets"][aid]
canon = reg["canonical"]
fig_h_px = None
if z.get("height_m"):   # figure height in the ref = union bbox of all zones
    bb = [v["bbox"] for v in seg["zones"].values() if v.get("bbox")]
    fig_h_px = max(b[3] for b in bb) - min(b[1] for b in bb)
mats = []
for name, zd in z["zones"].items():
    s = seg["zones"].get(name, {})
    mats.append({
        "zone": name, "label": zd.get("label", name), "library_ref": zd.get("library_ref"),
        "mask": f"work/{aid}/masks/{name}.png", "crop": f"work/{aid}/crops/{name}.png",
        "colors": {k: s.get(k) for k in ("median", "shadow", "light")},
        "pattern": zd.get("pattern", "none"), "finish": zd.get("finish", ""), "wear": zd.get("wear", "none visible"),
        "scale_m_per_px": round(z["height_m"] / fig_h_px, 5) if fig_h_px else None,
        "markings": zd.get("markings", []), "observed": zd.get("observed", "direct"),
        "inferred_from": zd.get("inferred_from"), "projection": zd.get("projection", "camera_match"),
        "sam_score": s.get("score"), "area_px": s.get("area"), "notes": zd.get("notes", "")})
man = {"asset_id": aid, "reference": {"path": canon["path"], "sha256": canon["sha256"], "version": reg["version"]},
       "sam": {"model": seg.get("model"), "mode": "points+box", "verified_by": z.get("verified_by", "pending")},
       "materials": mats, "unseen": z.get("unseen", []), "fallbacks": z.get("fallbacks", [])}
os.makedirs(os.path.join(HERE, "manifests"), exist_ok=True)
out = os.path.join(HERE, "manifests", f"{aid}.json")
json.dump(man, open(out, "w"), indent=1)
missing = [m["zone"] for m in mats if not m["colors"]["median"]]
print(f"{len(mats)} materials -> {out}; no colour: {missing or 'none'}")
