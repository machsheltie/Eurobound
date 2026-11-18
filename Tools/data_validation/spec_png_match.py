"""Count how many PNG filenames a location spec names exist as real files.

Feeds the "Spec PNGs in repo" column of
design/worlds/<city>/PNG_Assets/_art_build_audit.md (matched / named).

For each `*_Complete_PNG_Asset_Requirements.md` in the spec folder:
  - named   = unique `*.png` basenames written anywhere in the spec. Brace
              lists are expanded (`aa_int_closet_{day,night}.png` -> two
              names). Placeholders (`<slug>_exterior.png`, `*_day.png`) are
              skipped because they name no real file.
  - matched = how many of those basenames exist as files under
              game/assets/ or Assets/Graphics/ (case-insensitive basename
              match; any subfolder).

Usage (from the repo root):
    python -I Tools/data_validation/spec_png_match.py
    python -I Tools/data_validation/spec_png_match.py --city shamsterdam
    python -I Tools/data_validation/spec_png_match.py --missing   # list unmatched names
    python -I Tools/data_validation/spec_png_match.py --json
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ART_ROOTS = ("game/assets", "Assets/Graphics")
SPEC_GLOB = "*_Complete_PNG_Asset_Requirements.md"

# A filename token, optionally with {a,b} brace lists, ending in .png.
# The lookbehind rejects tokens glued to a placeholder (`<slug>_x.png`, `*_x.png`).
PNG_TOKEN = re.compile(r"(?<![\w\-*<>}.])((?:[\w\-]|\{[\w\-,]+\})+\.png)\b", re.IGNORECASE)


def expand_braces(token: str) -> list[str]:
    parts = re.split(r"(\{[^}]*\})", token)
    choices = [p[1:-1].split(",") if p.startswith("{") else [p] for p in parts]
    return ["".join(c) for c in itertools.product(*choices)]


def named_pngs(text: str) -> set[str]:
    names: set[str] = set()
    for m in PNG_TOKEN.finditer(text):
        for name in expand_braces(m.group(1)):
            names.add(name.lower())
    return names


def repo_pngs() -> set[str]:
    found: set[str] = set()
    for root in ART_ROOTS:
        base = REPO / root
        if not base.is_dir():
            continue
        for dirpath, _dirs, files in os.walk(base):
            for f in files:
                if f.lower().endswith(".png"):
                    found.add(f.lower())
    return found


def audit(city: str) -> list[dict]:
    spec_dir = REPO / "design" / "worlds" / city / "PNG_Assets"
    if not spec_dir.is_dir():
        sys.exit(f"no spec folder: {spec_dir.relative_to(REPO)}")
    on_disk = repo_pngs()
    rows = []
    for spec in sorted(spec_dir.glob(SPEC_GLOB)):
        names = named_pngs(spec.read_text(encoding="utf-8", errors="replace"))
        hit = sorted(n for n in names if n in on_disk)
        rows.append({
            "spec": spec.name,
            "matched": len(hit),
            "named": len(names),
            "matched_names": hit,
            "missing_names": sorted(names - set(hit)),
        })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--city", default="debaucheryville")
    ap.add_argument("--missing", action="store_true", help="list unmatched names per spec")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    rows = audit(args.city)
    if args.json:
        print(json.dumps(rows, indent=2))
        return
    for r in rows:
        print(f"{r['matched']:>3} / {r['named']:<3}  {r['spec']}")
        if args.missing and r["missing_names"]:
            for n in r["missing_names"]:
                print(f"            - {n}")
    m = sum(r["matched"] for r in rows)
    n = sum(r["named"] for r in rows)
    with_hits = sum(1 for r in rows if r["matched"])
    print(f"total {m} / {n}; {with_hits} of {len(rows)} specs have at least one match")


if __name__ == "__main__":
    main()
