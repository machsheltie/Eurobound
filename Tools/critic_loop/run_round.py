"""Blind critic loop runner. Usage:
  python -I tools/critic_loop/run_round.py prepare-refs            # one-off: build refs/*.jpg
  python -I tools/critic_loop/run_round.py capture [manifest.json] [--round N] [--shots id,id]
Runs exactly one windowed Godot, waits for it to exit, writes tools/critic_loop/<scene>/round_<n>/<id>.jpg.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
GODOT = os.environ.get("GODOT_BIN", r"C:\Users\heirr\Downloads\Godot_v4.7.2-stable_win64.exe\Godot_v4.7.2-stable_win64.exe")
# Approved reference sources. Some live untracked in the main checkout: set CRITIC_REF_ROOT to it.
REF_SRC = {
    "hall_night.jpg": "game/assets/worlds/debaucheryville/absinthe_arcade/interior/hall/aa_int_hall_night.png",
    "hall_day.jpg": "game/assets/worlds/debaucheryville/absinthe_arcade/interior/hall/aa_int_hall_day.png",
    "lord_pilsner_portrait.jpg": "Assets/Graphics/characters3d/lord_pilsner_v2/lord_pilsner_ref.png",
}


def prepare_refs():
    roots = [REPO] + ([Path(os.environ["CRITIC_REF_ROOT"])] if os.environ.get("CRITIC_REF_ROOT") else [])
    for name, rel in REF_SRC.items():
        src = next((r / rel for r in roots if (r / rel).exists()), None)
        if src is None:
            print("MISSING reference source:", rel, "(set CRITIC_REF_ROOT to the checkout that has it)")
            continue
        im = Image.open(src).convert("RGB")
        if im.width > 1280:
            im = im.resize((1280, round(im.height * 1280 / im.width)), Image.LANCZOS)
        im.save(HERE / "refs" / name, quality=85)
        print("ref", name, im.size)


def capture(manifest, rnd, shots):
    m = json.loads(Path(manifest).read_text())
    out = HERE / Path(manifest).stem / f"round_{rnd}"
    out.mkdir(parents=True, exist_ok=True)
    cmd = [GODOT, "--path", str(REPO / "game"), "--resolution", "1920x1080",
           "--script", str(HERE / "capture.gd"), "--", str(Path(manifest).resolve()), str(out)] + shots
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    (out.parent / f"round_{rnd}_godot.log").write_text(r.stdout + r.stderr)
    print("godot exit", r.returncode, "->", out)
    for s in m["shots"]:
        if not shots or s["id"] in shots:
            print(" ", "ok " if (out / (s["id"] + ".jpg")).exists() else "MISSING", s["id"], "ref", s["reference"])


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd, rest = a[0], a[1:]
    rnd = int(rest[rest.index("--round") + 1]) if "--round" in rest else 1
    shots = rest[rest.index("--shots") + 1].split(",") if "--shots" in rest else []
    pos = [x for x in rest if x.endswith(".json")]
    manifest = pos[0] if pos else str(HERE / "shots" / "arcade_hall.json")
    if cmd == "prepare-refs":
        prepare_refs()
    else:
        capture(manifest, rnd, shots)
