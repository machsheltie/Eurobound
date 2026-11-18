"""Count the built, game-ready art for each location spec in a city.

Feeds the "Built art" column and the Summary of
design/worlds/<city>/PNG_Assets/_art_build_audit.md. Sibling of
spec_png_match.py, which feeds the "Spec PNGs in repo" column.

For each `*_Complete_PNG_Asset_Requirements.md` in design/worlds/<city>/PNG_Assets/:
  - folder   = game/assets/worlds/<city>/<slug>/, where <slug> is the spec name
               in snake_case without the suffix, or the same with a `the_`
               prefix. Arcade side rooms map to their Arcade subfolder (SIDE_ROOMS).
  - exterior = PNGs anywhere under <folder>/exterior/
  - interior = PNGs anywhere under <folder>/interior/
  - other    = PNGs anywhere else under <folder>
Folders holding a `.gdignore` are staging, not game-ready: their PNGs are
reported as `staged` and left out of the totals. `.import` files never count.

Usage (from the repo root):
    python -I Tools/data_validation/built_art_count.py
    python -I Tools/data_validation/built_art_count.py --detail   # per-subfolder counts and plate names
    python -I Tools/data_validation/built_art_count.py --city shamsterdam
    python -I Tools/data_validation/built_art_count.py --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPEC_SUFFIX = "_Complete_PNG_Asset_Requirements.md"
WORKING_ROOT = "Assets/Graphics/worlds"

# Specs whose art lives inside another location's folder.
SIDE_ROOMS = {
    "debaucheryville": {
        "claw_machine_maintenance_closet": "absinthe_arcade/interior/closet",
        "absinthium_taproom": "absinthe_arcade/interior/taproom",
    },
}


def spec_key(spec: Path) -> str:
    return spec.name[: -len(SPEC_SUFFIX)].lower()


def find_folder(city: str, key: str, art_root: Path) -> Path | None:
    side = SIDE_ROOMS.get(city, {}).get(key)
    candidates = [side] if side else [key, f"the_{key}"]
    for c in candidates:
        p = art_root / c
        if p.is_dir():
            return p
    return None


def count_pngs(folder: Path) -> dict:
    """PNG counts under folder, split by top-level part and by subfolder."""
    parts: Counter = Counter()
    subdirs: Counter = Counter()
    staged = 0
    files: list[str] = []
    for dirpath, dirs, names in os.walk(folder):
        here = Path(dirpath)
        pngs = [n for n in names if n.lower().endswith(".png")]
        if (here / ".gdignore").exists():
            staged += sum(1 for _ in _walk_pngs(here))
            dirs[:] = []
            continue
        if not pngs:
            continue
        rel = here.relative_to(folder)
        top = rel.parts[0] if rel.parts else "."
        part = top if top in ("exterior", "interior") else "other"
        parts[part] += len(pngs)
        subdirs[rel.as_posix()] += len(pngs)
        files.extend((rel / n).as_posix() for n in sorted(pngs))
    return {
        "exterior": parts["exterior"],
        "interior": parts["interior"],
        "other": parts["other"],
        "total": sum(parts.values()),
        "staged": staged,
        "subfolders": dict(sorted(subdirs.items())),
        "files": sorted(files),
    }


def _walk_pngs(folder: Path):
    for _dp, _d, names in os.walk(folder):
        for n in names:
            if n.lower().endswith(".png"):
                yield n


def kind(row: dict) -> str:
    if row["side_room"]:
        return "side room"
    if not row["total"]:
        return "none"
    if row["exterior"] and row["interior"]:
        return "ext+int"
    if row["exterior"]:
        return "ext only"
    if row["interior"]:
        return "int only"
    return "other only"


def audit(city: str) -> dict:
    spec_dir = REPO / "design" / "worlds" / city / "PNG_Assets"
    art_root = REPO / "game" / "assets" / "worlds" / city
    if not spec_dir.is_dir():
        sys.exit(f"no spec folder: {spec_dir.relative_to(REPO)}")
    rows = []
    used: set[str] = set()
    for spec in sorted(spec_dir.glob(f"*{SPEC_SUFFIX}")):
        key = spec_key(spec)
        folder = find_folder(city, key, art_root) if art_root.is_dir() else None
        counts = count_pngs(folder) if folder else {
            "exterior": 0, "interior": 0, "other": 0, "total": 0, "staged": 0,
            "subfolders": {}, "files": [],
        }
        row = {
            "spec": spec.name,
            "folder": folder.relative_to(REPO).as_posix() if folder else None,
            "side_room": key in SIDE_ROOMS.get(city, {}),
            **counts,
        }
        row["kind"] = kind(row)
        rows.append(row)
        if folder and not row["side_room"]:
            used.add(folder.name)
    unmatched = sorted(
        d.name for d in art_root.iterdir() if d.is_dir() and d.name not in used
    ) if art_root.is_dir() else []
    working = REPO / WORKING_ROOT / city
    working_files = {
        d.name: sum(len(f) for _dp, _d, f in os.walk(d))
        for d in sorted(working.iterdir()) if d.is_dir()
    } if working.is_dir() else {}
    return {"city": city, "rows": rows, "unmatched_folders": unmatched,
            "working_files": working_files}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--city", default="debaucheryville")
    ap.add_argument("--detail", action="store_true", help="per-subfolder counts and file names")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    result = audit(args.city)
    if args.json:
        print(json.dumps(result, indent=2))
        return
    rows = result["rows"]
    print(f"{'ext':>4} {'int':>4} {'oth':>4} {'total':>5}  {'kind':<10} spec")
    for r in rows:
        staged = f"  (+{r['staged']} staged, .gdignore)" if r["staged"] else ""
        where = r["folder"] or "no folder"
        print(f"{r['exterior']:>4} {r['interior']:>4} {r['other']:>4} {r['total']:>5}  "
              f"{r['kind']:<10} {r['spec']}  [{where}]{staged}")
        if args.detail and r["total"]:
            for sub, n in r["subfolders"].items():
                print(f"{'':>30}{n:>4}  {sub}/")
            if r["total"] <= 12:
                for f in r["files"]:
                    print(f"{'':>36}{f}")
    kinds = Counter(r["kind"] for r in rows)
    built = sum(1 for r in rows if r["total"])
    print(f"built art of any kind: {built} of {len(rows)}; "
          + ", ".join(f"{k}: {n}" for k, n in sorted(kinds.items())))
    for k in ("ext+int", "ext only", "int only", "none"):
        names = [r["spec"][: -len(SPEC_SUFFIX)] for r in rows if r["kind"] == k]
        print(f"  {k} ({len(names)}): {', '.join(names) or '-'}")
    if result["unmatched_folders"]:
        print("art folders with no spec: " + ", ".join(result["unmatched_folders"]))
    for d, n in result["working_files"].items():
        print(f"working files in {WORKING_ROOT}/{args.city}/{d}/: {n}")


if __name__ == "__main__":
    main()
