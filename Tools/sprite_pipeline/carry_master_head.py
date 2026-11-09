"""Fit PixelLab animation frames to a character's approved still frames.

PixelLab animates from its own stored copy of a character, which predates our face pass and any
hand edits in Aseprite (Pilsner's goatee, jaw and blue eyes all vanished from his first walk cycle).
This script fixes every animation frame:

1. crops the animation canvas (PixelLab returns 176x176 for a 128 character) to 128x128, aligned
   to the approved still for that direction;
2. pastes the approved head (rows above `--cut`, the collar line) onto each frame at the offset
   where it best matches, so the face, hair and any hand edits stay identical while the body moves.

    python tools/sprite_pipeline/carry_master_head.py <stills_dir> <anim_dir> <out_dir> [--cut 29]

<stills_dir>  one PNG per direction named idle_<dir>.png (snake_case), e.g. exported from the
              approved .aseprite with:  Aseprite.exe -b file.aseprite --save-as <dir>/{tag}.png
<anim_dir>    PixelLab character export: <anim_dir>/<Anything>/animations/<clip>[-suffix]/<dir>/*.png
<out_dir>     written as <out_dir>/<clip>/<dir>/frame_NNN.png, ready for pack_aseprite.lua
              (clip "breathing_idle" is renamed "idle", "walking" is renamed "walk").
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

import numpy as np
from PIL import Image

SIZE = 128
CLIP_NAMES = {"breathing_idle": "idle", "breathing-idle": "idle", "walking": "walk"}


def load(p: Path) -> np.ndarray:
    return np.asarray(Image.open(p).convert("RGBA")).astype(int)


def mismatch(a: np.ndarray, b: np.ndarray) -> float:
    """Lower is better: silhouette disagreement plus colour distance where both are opaque."""
    am, bm = a[..., 3] > 0, b[..., 3] > 0
    both = am & bm
    colour = np.abs(a[..., :3] - b[..., :3]).sum(-1)[both].mean() if both.any() else 765.0
    return float(np.mean(am != bm) * 300 + colour)


def best_offset(img: np.ndarray, ref: np.ndarray, x0: int, y0: int, rng: int) -> tuple[int, int]:
    h, w = ref.shape[:2]
    best = None
    for dy in range(-rng, rng + 1):
        for dx in range(-rng, rng + 1):
            y, x = y0 + dy, x0 + dx
            if y < 0 or x < 0:
                continue
            crop = img[y:y + h, x:x + w]
            if crop.shape[:2] != (h, w):
                continue
            score = mismatch(crop, ref)
            if best is None or score < best[0]:
                best = (score, x, y)
    if best is None:
        raise ValueError("no valid offset")
    return best[1], best[2]


def fit_direction(still: np.ndarray, frames: list[Path], out: Path, cut: int) -> None:
    first = load(frames[0])
    base = (first.shape[1] - SIZE) // 2
    cx, cy = best_offset(first, still, base, base, 8)
    rows = np.where(still[..., 3].any(1))[0]
    top = int(rows[0]) if len(rows) else 0
    head = still[top:cut]
    cols = np.where(head[..., 3].any(0))[0]
    hx0, hx1 = max(0, int(cols.min()) - 1), min(SIZE, int(cols.max()) + 2)
    head = head[:, hx0:hx1]
    out.mkdir(parents=True, exist_ok=True)
    for i, fp in enumerate(frames):
        frame = load(fp)[cy:cy + SIZE, cx:cx + SIZE].copy()
        x, y = best_offset(frame, head, hx0, top, 4)
        frame[y:y + head.shape[0], x:x + head.shape[1]] = head
        Image.fromarray(frame.astype("uint8")).save(out / f"frame_{i:03d}.png")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("stills_dir", type=Path)
    ap.add_argument("anim_dir", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--cut", type=int, default=29, help="first row below the head (collar line)")
    args = ap.parse_args()
    if args.out_dir.exists():
        shutil.rmtree(args.out_dir)
    done = 0
    for clip_dir in sorted(args.anim_dir.glob("*/animations/*")):
        clip = CLIP_NAMES.get(re.sub(r"-[0-9a-f]{8}$", "", clip_dir.name), clip_dir.name)
        for dir_dir in sorted(p for p in clip_dir.iterdir() if p.is_dir()):
            frames = sorted(dir_dir.glob("*.png"))
            still_path = args.stills_dir / f"idle_{dir_dir.name.replace('-', '_')}.png"
            if not frames or not still_path.exists():
                print(f"skip {clip}/{dir_dir.name}: no frames or no still")
                continue
            fit_direction(load(still_path), frames, args.out_dir / clip / dir_dir.name, args.cut)
            done += 1
            print(f"{clip}/{dir_dir.name}: {len(frames)} frames")
    print(f"fitted {done} clips -> {args.out_dir}")


if __name__ == "__main__":
    main()
