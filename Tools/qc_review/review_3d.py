"""SAM-assisted QA review (Reference-Locked 3D Texturing Protocol, steps 9-11).

Run from the repo root (the zone files' image paths are relative to it):
  tools/paint_zones/.venv/Scripts/python Tools/qc_review/review_3d.py <asset_id> \
      --ref-zones tools/paint_zones/zones/<id>_ref.json \
      --render <render_zones.json> [--lighting neutral] [--render ... --lighting game] \
      [--round 1] [--sheet] [--reference-lighting "painted reference"]

Segments the reference and each render with SAM (tools/paint_zones/segment_ref.py), ONE AT A TIME,
then compares zone by zone (median, shadow, light colour) in CIELAB with CIEDE2000.
Outcome is BLOCKED, REVISION REQUIRED or APPROVED-PENDING-MANUAL. It never says APPROVED:
colour alone cannot approve (protocol "Review outcome").
"""
import argparse, json, math, os, subprocess, sys
import numpy as np

# PROVISIONAL thresholds (dE00 on the median colour), pending real trials (Chadwick + one Arcade asset).
PASS_MAX = 10.0   # <= 10: pass
WARN_MAX = 20.0   # > 10 and <= 20: warn; > 20: fail

MANUAL_CHECKS = [
    "UV and texture validation (seams, stretching, texel density, no baked lighting in base colour)",
    "PBR behaviour (base colour, roughness, metallic, normal, AO checked independently)",
    "Acceptable look at intended in-game scale (view the game-size render)",
    "Surface character, markings and lettering, finish, texture scale, boundaries (not covered by colour delta)",
    "Silhouette and painterly style preserved (no generic photoreal substitute; no unjustified upscaling)",
    "Observed vs invented details labelled in the material manifest",
]


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_lab(rgb):
    """sRGB (0-255) to CIELAB, D65."""
    c = np.asarray(rgb, dtype=float) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    m = np.array([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    xyz = m @ c / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 216 / 24389, np.cbrt(xyz), (24389 / 27 * xyz + 16) / 116)
    return np.array([116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])])


def delta_e2000(lab1, lab2):
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if C1p else 0.0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if C2p else 0.0
    dL, dC = L2 - L1, C2p - C1p
    if C1p * C2p == 0:
        dh = 0.0
    else:
        dh = h2p - h1p
        dh = dh - 360 if dh > 180 else dh + 360 if dh < -180 else dh
    dH = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dh / 2))
    Lm, Cpm = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hm = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hm = (h1p + h2p) / 2
    else:
        hm = (h1p + h2p + 360) / 2 if h1p + h2p < 360 else (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hm - 30)) + 0.24 * math.cos(math.radians(2 * hm))
         + 0.32 * math.cos(math.radians(3 * hm + 6)) - 0.20 * math.cos(math.radians(4 * hm - 63)))
    SL = 1 + 0.015 * (Lm - 50) ** 2 / math.sqrt(20 + (Lm - 50) ** 2)
    SC, SH = 1 + 0.045 * Cpm, 1 + 0.015 * Cpm * T
    dth = 30 * math.exp(-(((hm - 275) / 25) ** 2))
    RC = 2 * math.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7))
    RT = -math.sin(math.radians(2 * dth)) * RC
    return math.sqrt((dL / SL) ** 2 + (dC / SC) ** 2 + (dH / SH) ** 2 + RT * (dC / SC) * (dH / SH))


def hex_delta_e(h1, h2):
    return delta_e2000(rgb_to_lab(hex_to_rgb(h1)), rgb_to_lab(hex_to_rgb(h2)))


def verdict_for(de):
    if de is None:
        return "fail"
    return "pass" if de <= PASS_MAX else "warn" if de <= WARN_MAX else "fail"


def zone_usable(info):
    return bool(info) and info.get("area", 0) > 0 and bool(info.get("median"))


def compare_zones(names, ref_zones, render_zones):
    """names: zones to compare. Returns per-zone row dicts."""
    rows = []
    for n in names:
        r, d = ref_zones.get(n), render_zones.get(n)
        row = {"zone": n, "ref_median": r.get("median") if r else None,
               "render_median": d.get("median") if d else None, "delta_e": None,
               "delta_e_shadow": None, "delta_e_light": None, "verdict": "fail", "issue": ""}
        if not zone_usable(r):
            row["issue"] = "reference mask missing or empty"
        elif not zone_usable(d):
            row["issue"] = "render mask missing or empty (zone not found in the render)"
        else:
            row["delta_e"] = round(hex_delta_e(r["median"], d["median"]), 2)
            for k in ("shadow", "light"):
                if r.get(k) and d.get(k):
                    row["delta_e_" + k] = round(hex_delta_e(r[k], d[k]), 2)
            row["verdict"] = verdict_for(row["delta_e"])
            if row["verdict"] != "pass":
                row["issue"] = f"median colour off by dE00 {row['delta_e']} (thresholds provisional)"
            for k in ("shadow", "light"):
                if (row["delta_e_" + k] or 0) > WARN_MAX:
                    row["issue"] += f"; {k} dE00 {row['delta_e_' + k]} (info only, lighting dependent)"
        rows.append(row)
    return rows


def overall_outcome(blocked, all_rows):
    if blocked:
        return "BLOCKED"
    if not all_rows or any(r["verdict"] == "fail" for r in all_rows):
        return "REVISION REQUIRED"
    return "APPROVED-PENDING-MANUAL"


def find_tool(root):
    for d in ("Tools", "tools"):
        p = os.path.join(root, d, "paint_zones")
        if os.path.exists(os.path.join(p, "segment_ref.py")):
            return p
    return None


def run_sam(tool, zones_path, sheet, root):
    py = next((os.path.join(tool, ".venv", s, e) for s, e in (("Scripts", "python.exe"), ("bin", "python"))
               if os.path.exists(os.path.join(tool, ".venv", s, e))), None)
    if not py:
        return None, "paint_zones venv python not found"
    cmd = [py, os.path.join(tool, "segment_ref.py"), os.path.abspath(zones_path)] + (["--sheet"] if sheet else [])
    try:
        p = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=900)
    except Exception as e:  # noqa
        return None, f"SAM run failed: {e}"
    if p.returncode != 0:
        return None, "SAM failed: " + (p.stderr or p.stdout).strip()[-400:]
    z = json.load(open(zones_path))
    seg = os.path.join(tool, "work", z["asset_id"], "segment.json")
    if not os.path.exists(seg):
        return None, f"SAM produced no segment.json at {seg}"
    sheet_p = os.path.join(tool, "work", z["asset_id"], "segment_sheet.jpg")
    return {"segment": seg, "sheet": sheet_p if sheet and os.path.exists(sheet_p) else None}, None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("asset_id")
    ap.add_argument("--ref-zones", required=True)
    ap.add_argument("--render", action="append", default=[], help="render zone file (repeatable)")
    ap.add_argument("--lighting", action="append", default=[], help="lighting label per --render, same order")
    ap.add_argument("--reference-lighting", default="painted reference (lighting baked into the art)")
    ap.add_argument("--round", type=int, default=1)
    ap.add_argument("--sheet", action="store_true")
    ap.add_argument("--root", default=os.getcwd(), help="repo root (default: cwd)")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports"))
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    tool = find_tool(root)
    blockers, report_renders, all_rows = [], [], []
    ref_sheet = None
    if tool is None:
        blockers.append("tools/paint_zones (segment_ref.py) not found under the repo root")
    if not os.path.exists(a.ref_zones):
        blockers.append(f"reference zone file missing: {a.ref_zones}")
    if not a.render:
        blockers.append("no render zone file given (--render)")
    for r in a.render:
        if not os.path.exists(r):
            blockers.append(f"render zone file missing: {r}")
    for fpath in [a.ref_zones] + a.render:
        if os.path.exists(fpath):
            img = json.load(open(fpath)).get("image", "")
            if not os.path.exists(os.path.join(root, img)):
                blockers.append(f"image missing for {os.path.basename(fpath)}: {img}")
    ref_seg = None
    if not blockers:
        ref_res, err = run_sam(tool, a.ref_zones, a.sheet, root)   # one SAM run at a time
        if err:
            blockers.append("reference: " + err)
        else:
            ref_seg = json.load(open(ref_res["segment"]))["zones"]
            ref_sheet = ref_res["sheet"]
    if not blockers:
        for i, rpath in enumerate(a.render):
            light = a.lighting[i] if i < len(a.lighting) else "unspecified"
            rz = json.load(open(rpath))
            res, err = run_sam(tool, rpath, a.sheet, root)
            if err:
                blockers.append(f"render {rpath}: {err}")
                break
            seg = json.load(open(res["segment"]))["zones"]
            rows = compare_zones(list(rz["zones"]), ref_seg, seg)
            all_rows += rows
            report_renders.append({"zone_file": rpath, "image": rz.get("image"), "lighting": light,
                                   "contact_sheet": res["sheet"], "zones": rows})
    outcome = overall_outcome(bool(blockers), all_rows)
    lights = [r["lighting"].lower() for r in report_renders]
    notes = ["Colour delta is only meaningful where the render lighting matches the reference "
             "(protocol step 10). Reference lighting: " + a.reference_lighting + ". Render lighting compared: "
             + (", ".join(r["lighting"] for r in report_renders) or "none") + "."]
    if report_renders and not any("neutral" in x for x in lights):
        notes.append("No neutral-lighting render was supplied; neutral vs reference was not compared.")
    notes.append(f"Thresholds are PROVISIONAL pending real trials: pass <= {PASS_MAX}, warn <= {WARN_MAX}, "
                 "fail above (CIEDE2000 on the median).")
    unavailable = [
        "Step 9 (render): not run by this script; renders were supplied by the caller. Fixed camera/exposure/colour management is the caller's responsibility.",
        "Step 10 (surface character, markings, texture scale, finish, boundaries, seams): not automated; fallback is the manual checklist below. Only the colour comparison ran.",
        "Step 11 (correction loop): not run; this report only supplies the failing zones.",
        "Step 12 (final asset package / quality report): not assembled by this script.",
    ]
    for b in reversed(blockers):
        unavailable.insert(0, "BLOCKED: " + b)
    rep = {"asset_id": a.asset_id, "round": a.round, "outcome": outcome, "blockers": blockers,
           "reference": {"zone_file": a.ref_zones, "lighting": a.reference_lighting, "contact_sheet": ref_sheet},
           "thresholds": {"pass_max": PASS_MAX, "warn_max": WARN_MAX, "metric": "CIEDE2000", "provisional": True},
           "renders": report_renders, "notes": notes,
           "manual_checks_required": MANUAL_CHECKS, "unavailable_or_fallback": unavailable,
           "regions": [{"region": r["zone"], "verdict": r["verdict"], "issue": r["issue"]} for r in all_rows]}
    os.makedirs(a.out, exist_ok=True)
    base = os.path.join(a.out, f"{a.asset_id}_qa_round{a.round}")
    json.dump(rep, open(base + ".json", "w"), indent=1)
    L = [f"# QA review: {a.asset_id}, round {a.round}", "", f"**OUTCOME: {outcome}**", ""]
    if outcome == "APPROVED-PENDING-MANUAL":
        L += ["The colour pass alone cannot approve. Tick every manual check below before marking APPROVED.", ""]
    if blockers:
        L += [f"- Blocker: {b}" for b in blockers] + [""]
    L += ["## Notes"] + [f"- {n}" for n in notes] + [""]
    if ref_sheet:
        L += [f"Reference contact sheet: `{ref_sheet}`", ""]
    for r in report_renders:
        L += [f"## Render `{r['image']}` (lighting: {r['lighting']})", ""]
        if r["contact_sheet"]:
            L += [f"Contact sheet: `{r['contact_sheet']}`", ""]
        L += ["| zone | ref median | render median | dE00 | verdict | issue |", "|---|---|---|---|---|---|"]
        L += [f"| {z['zone']} | {z['ref_median']} | {z['render_median']} | {z['delta_e']} | {z['verdict']} | {z['issue']} |"
              for z in r["zones"]]
        L += [""]
    L += ["## Manual checks (reviewer ticks)"] + [f"- [ ] {m}" for m in MANUAL_CHECKS] + [""]
    L += ["## Unavailable / fallback"] + [f"- {u}" for u in unavailable] + [""]
    open(base + ".md", "w", encoding="utf-8").write("\n".join(L))
    print(f"{outcome}: {base}.md")
    sys.exit(2 if outcome == "BLOCKED" else 0)


if __name__ == "__main__":
    main()
