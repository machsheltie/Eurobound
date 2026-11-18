"""Promote finished 3D item icons to the live icon folder; retire their pixel twins.

Author ruling (Eurobound Desk asset-team-icon-swap-live-folder, 2026-11-15):
"Swap as they're finished: each 3D icon goes live and its pixel twin moves to a
legacy folder; pixel icons with no 3D version stay live until replaced".

What it does, per icon id:
  1. Gate: the LATEST A4 line for the id in dev/asset_team/reviews/qc_log.jsonl
     must be pass: true. A failed, pending or missing A4 means skip.
  2. Pixel twin: game/assets/items/icons/<id>_64.png and <id>_128.png (and their
     .import files) move to game/assets/items/icons/legacy_pixel/. Tracked files
     move with `git mv`; untracked ones (Godot .import churn) with a plain move.
     Nothing is deleted.
  3. 3D icon: game/assets/items/icons/3d/<id>_128.png and _512.png are COPIED to
     game/assets/items/icons/. The 3d/ folder stays the render output folder.
     The .import files are not copied (that would duplicate Godot UIDs); Godot
     makes new ones on the next editor scan.

It never commits. Run from the repo root:
  python -I Tools/item3d/promote_icons.py              # every pending twin, dry run
  python -I Tools/item3d/promote_icons.py --apply      # do it
  python -I Tools/item3d/promote_icons.py --apply <id> [<id> ...]   # named ids only
  --hold <id>   never touch this id (repeatable), e.g. an icon being redone.

A promoted id is one whose live <id>_512.png exists. If the 3d/ render later
changes, rerun with the id to refresh the live copy (the script reports stale
copies). Godot needs an editor rescan/reimport after a run.
"""
import argparse
import filecmp
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LIVE = ROOT / "game/assets/items/icons"
SRC3D = LIVE / "3d"
LEGACY = LIVE / "legacy_pixel"
QC_LOG = ROOT / "dev/asset_team/reviews/qc_log.jsonl"
PIXEL_SIZES = ("64", "128")
SIZES_3D = ("128", "512")


def latest_a4(item_id):
    """Return (line_no, entry) of the last A4 line for item_id, or (None, None)."""
    found = (None, None)
    for n, line in enumerate(QC_LOG.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("gate") == "A4" and d.get("item") in (item_id, "item_" + item_id):
            found = (n, d)
    return found


def tracked(path):
    r = subprocess.run(["git", "ls-files", "--error-unmatch", str(path.relative_to(ROOT))],
                       cwd=ROOT, capture_output=True)
    return r.returncode == 0


def move(src, dst, apply):
    if not src.exists():
        return
    how = "git mv" if tracked(src) else "mv"
    print(f"    {how} {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
    if not apply:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if how == "git mv":
        subprocess.run(["git", "mv", str(src.relative_to(ROOT)), str(dst.relative_to(ROOT))],
                       cwd=ROOT, check=True)
    else:
        shutil.move(str(src), str(dst))


def ids_3d():
    return sorted({p.name.rsplit("_", 1)[0] for p in SRC3D.glob("*_512.png")})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="icon ids (default: every 3D icon with a pixel twin still live)")
    ap.add_argument("--apply", action="store_true", help="make the changes (default is a dry run)")
    ap.add_argument("--hold", action="append", default=[], help="id to leave alone")
    a = ap.parse_args()

    named = bool(a.ids)
    ids = a.ids or [i for i in ids_3d() if (LIVE / f"{i}_64.png").exists()
                    and not (LIVE / f"{i}_512.png").exists()]
    promoted, skipped = [], []
    for i in ids:
        if i in a.hold:
            skipped.append((i, "held (--hold)"))
            continue
        missing = [s for s in SIZES_3D if not (SRC3D / f"{i}_{s}.png").exists()]
        if missing:
            skipped.append((i, f"no 3d render at {', '.join(missing)} px"))
            continue
        n, d = latest_a4(i)
        if d is None:
            skipped.append((i, "no A4 line in the QC log"))
            continue
        if d.get("pass") is not True:
            skipped.append((i, f"latest A4 (qc_log line {n}, round {d.get('round')}) is not a pass"))
            continue
        live512 = LIVE / f"{i}_512.png"
        if live512.exists() and not named:
            continue
        print(f"{i}: A4 pass at qc_log line {n} (round {d.get('round')}, {d.get('reviewer')})")
        for s in PIXEL_SIZES:
            if (SRC3D / f"{i}_{s}.png").exists() and live512.exists():
                continue  # live _128 is already the 3D copy; never move it to legacy
            for suffix in (".png", ".png.import"):
                move(LIVE / f"{i}_{s}{suffix}", LEGACY / f"{i}_{s}{suffix}", a.apply)
        for s in SIZES_3D:
            src, dst = SRC3D / f"{i}_{s}.png", LIVE / f"{i}_{s}.png"
            if dst.exists() and filecmp.cmp(src, dst, shallow=False):
                print(f"    live {dst.name} already current")
                continue
            print(f"    copy {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
            if a.apply:
                shutil.copy2(src, dst)
        promoted.append((i, n))

    # Stale check: live 3D copies that no longer match their 3d/ render.
    for p in sorted(LIVE.glob("*_512.png")):
        src = SRC3D / p.name
        if src.exists() and not filecmp.cmp(src, p, shallow=False):
            print(f"STALE: {p.name} differs from 3d/{p.name}; rerun with its id after it passes A4")

    print(f"\n{'PROMOTED' if a.apply else 'WOULD PROMOTE'}: {len(promoted)}")
    for i, n in promoted:
        print(f"  {i} (qc_log line {n})")
    print(f"SKIPPED: {len(skipped)}")
    for i, why in skipped:
        print(f"  {i}: {why}")
    if a.apply and promoted:
        print("\nGodot: open the editor (or run an import) to rescan the moved and copied icons.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
