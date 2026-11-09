"""PixelLab API client for the character sprite pipeline (design/style_guides/character_sprite_pipeline.md).

The API key is read from the user-level Claude Code MCP config (~/.claude.json, server "pixellab")
or the PIXELLAB_API_KEY environment variable. It is never printed or written to the repo.

    python tools/sprite_pipeline/pixellab_client.py balance
    python tools/sprite_pipeline/pixellab_client.py create --concept sheet.png --desc-file desc.txt \
        --style "..." --size 96 --out <dir> [--view "low top-down"] [--seed N]
    python tools/sprite_pipeline/pixellab_client.py animate --character <id> --template walking-8-frames \
        --out <dir> [--directions south,east,...]
    python tools/sprite_pipeline/pixellab_client.py fetch --character <id> --out <dir>
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import sys
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

API = "https://api.pixellab.ai/v2"


def api_key() -> str:
    if os.environ.get("PIXELLAB_API_KEY"):
        return os.environ["PIXELLAB_API_KEY"]
    cfg = json.loads((Path.home() / ".claude.json").read_text(encoding="utf-8"))
    server = cfg.get("mcpServers", {}).get("pixellab", {})
    auth = server.get("headers", {}).get("Authorization", "")
    if not auth.startswith("Bearer "):
        sys.exit("No PixelLab key: set PIXELLAB_API_KEY or add the 'pixellab' MCP server.")
    return auth[len("Bearer "):]


def call(method: str, path: str, body: dict | None = None, raw: bool = False):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None)
    req.add_header("Authorization", f"Bearer {api_key()}")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} on {path}: {e.read().decode(errors='replace')[:800]}")
    return data if raw else json.loads(data)


def b64_png(path: Path, max_side: int) -> dict:
    from PIL import Image

    im = Image.open(path).convert("RGBA")
    im.thumbnail((max_side, max_side), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG")
    return {"type": "base64", "base64": base64.b64encode(buf.getvalue()).decode(), "format": "png"}


def wait_job(job_id: str, label: str, timeout_s: int = 1800) -> dict:
    t0 = time.time()
    while True:
        job = call("GET", f"/background-jobs/{job_id}")
        status = job.get("status")
        if status in ("completed", "failed", "cancelled"):
            print(f"{label}: {status} after {int(time.time() - t0)}s")
            if status != "completed":
                sys.exit(json.dumps(job)[:1500])
            return job
        if time.time() - t0 > timeout_s:
            sys.exit(f"{label}: timed out (job {job_id})")
        time.sleep(10)


def job_id_of(resp: dict) -> str:
    for k in ("background_job_id", "job_id", "id"):
        if resp.get(k):
            return resp[k]
    sys.exit("No job id in response: " + json.dumps(resp)[:800])


def fetch_character(character_id: str, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    data = call("GET", f"/characters/{character_id}/zip", raw=True)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        z.extractall(out)
    (out / "character.json").write_text(json.dumps(call("GET", f"/characters/{character_id}"), indent=2))
    print(f"character {character_id} -> {out}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("balance")
    c = sub.add_parser("create")
    c.add_argument("--concept", required=True)
    c.add_argument("--desc-file", required=True)
    c.add_argument("--style", default="")
    c.add_argument("--size", type=int, default=96)
    c.add_argument("--view", default="low top-down")
    c.add_argument("--seed", type=int)
    c.add_argument("--out", required=True)
    a = sub.add_parser("animate")
    a.add_argument("--character", required=True)
    a.add_argument("--template", help="template animation id (omit and pass --action for a custom motion)")
    a.add_argument("--action", help="custom motion description (skeleton-v3 / v3 without a template)")
    a.add_argument("--frames", type=int, help="frame count for a custom motion")
    a.add_argument("--directions")
    a.add_argument("--mode", default="template", choices=["template", "skeleton-v3", "v3"],
                   help="skeleton-v3 moves the existing sprite instead of redrawing it (steadier face)")
    a.add_argument("--out", required=True)
    v = sub.add_parser("convert", help="concept art -> pixel art at an exact size (keeps proportions)")
    v.add_argument("--image", required=True)
    v.add_argument("--size", type=int, default=96)
    v.add_argument("--strength", type=int, default=200)
    v.add_argument("--reinterpret", action="store_true",
                   help="redraw as clean pixel art instead of copying the source's shading")
    v.add_argument("--out", required=True, help="output PNG")
    r = sub.add_parser("rotate", help="one south-facing sprite -> 8-direction character")
    r.add_argument("--image", required=True)
    r.add_argument("--desc-file", required=True)
    r.add_argument("--size", type=int, default=96)
    r.add_argument("--view", default="low top-down")
    r.add_argument("--out", required=True)
    k = sub.add_parser("correct", help="tidy stray/blurry pixels in a folder of frames (same size)")
    k.add_argument("--src", required=True, help="folder of PNG frames, corrected together")
    k.add_argument("--strength", type=float, default=0.25)
    k.add_argument("--out", required=True)
    n = sub.add_parser("inpaint", help="redraw a rectangle of a sprite from a description (Pro)")
    n.add_argument("--image", required=True)
    n.add_argument("--box", required=True, help="x0,y0,x1,y1 in pixels (inclusive-exclusive)")
    n.add_argument("--desc", required=True)
    n.add_argument("--seed", type=int)
    n.add_argument("--out", required=True)
    f = sub.add_parser("fetch")
    f.add_argument("--character", required=True)
    f.add_argument("--out", required=True)
    args = ap.parse_args()

    if args.cmd == "balance":
        print(json.dumps(call("GET", "/balance"), indent=2))
    elif args.cmd == "create":
        body = {
            "description": Path(args.desc_file).read_text(encoding="utf-8").strip(),
            "image_size": {"width": args.size, "height": args.size},
            "method": "create_from_concept",
            "concept_image": b64_png(Path(args.concept), 1024),
            "view": args.view,
            "no_background": True,
        }
        if args.style:
            body["style_description"] = args.style
        if args.seed is not None:
            body["seed"] = args.seed
        resp = call("POST", "/create-character-pro", body)
        job = wait_job(job_id_of(resp), "create")
        cid = job.get("last_response", {}).get("character_id") or resp.get("character_id")
        fetch_character(cid, Path(args.out))
    elif args.cmd == "animate":
        body = {"character_id": args.character, "mode": args.mode}
        if args.template:
            body["template_animation_id"] = args.template
        if args.action:
            body["action_description"] = args.action
        if args.frames:
            body["frame_count"] = args.frames
        if args.directions:
            body["directions"] = args.directions.split(",")
        resp = call("POST", "/characters/animations", body)
        ids = resp.get("background_job_ids") or [job_id_of(resp)]
        for i, jid in enumerate(ids):
            wait_job(jid, f"animate {i + 1}/{len(ids)}")
        fetch_character(args.character, Path(args.out))
    elif args.cmd == "convert":
        from PIL import Image

        src = Image.open(args.image)
        body = {
            "image": b64_png(Path(args.image), 2048),
            "image_size": {"width": src.width, "height": src.height},
            "output_size": {"width": args.size, "height": args.size},
            "fixer": not args.reinterpret,
            "init_image_strength": args.strength,
        }
        resp = call("POST", "/image-to-pixelart", body)
        if "background_job_id" in resp:
            resp = wait_job(resp["background_job_id"], "convert").get("last_response", {})
        img = resp.get("image") or resp.get("images", [{}])[0]
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_bytes(base64.b64decode(img["base64"]))
        print(f"converted -> {args.out}")
    elif args.cmd == "rotate":
        body = {
            "description": Path(args.desc_file).read_text(encoding="utf-8").strip(),
            "image_size": {"width": args.size, "height": args.size},
            "method": "rotate_character",
            "reference_image": b64_png(Path(args.image), 168),
            "view": args.view,
            "no_background": True,
        }
        resp = call("POST", "/create-character-pro", body)
        job = wait_job(job_id_of(resp), "rotate")
        cid = job.get("last_response", {}).get("character_id") or resp.get("character_id")
        fetch_character(cid, Path(args.out))
    elif args.cmd == "correct":
        frames = sorted(Path(args.src).glob("*.png"))
        body = {"images": [b64_png(p, 1024) for p in frames], "strength": args.strength}
        resp = call("POST", "/correct-pixelart", body)
        if "background_job_id" in resp:
            resp = wait_job(resp["background_job_id"], "correct").get("last_response", {})
        images = resp.get("images") or [resp.get("image")]
        out = Path(args.out)
        out.mkdir(parents=True, exist_ok=True)
        for p, img in zip(frames, images):
            (out / p.name).write_bytes(base64.b64decode(img["base64"]))
        print(f"corrected {len(images)} frames -> {out}")
    elif args.cmd == "inpaint":
        from PIL import Image, ImageDraw

        src = Image.open(args.image).convert("RGBA")
        x0, y0, x1, y1 = (int(v) for v in args.box.split(","))
        mask = Image.new("RGB", src.size, (0, 0, 0))
        ImageDraw.Draw(mask).rectangle([x0, y0, x1 - 1, y1 - 1], fill=(255, 255, 255))
        buf = io.BytesIO()
        mask.save(buf, "PNG")
        size = {"width": src.width, "height": src.height}
        body = {
            "description": args.desc,
            "inpainting_image": {"image": b64_png(Path(args.image), 512), "size": size},
            "mask_image": {"image": {"type": "base64", "format": "png",
                                     "base64": base64.b64encode(buf.getvalue()).decode()},
                           "size": size},
            "no_background": True,
        }
        if args.seed is not None:
            body["seed"] = args.seed
        resp = call("POST", "/inpaint-v3", body)
        if "background_job_id" in resp:
            resp = wait_job(resp["background_job_id"], "inpaint").get("last_response", {})
        img = resp.get("image") or (resp.get("images") or [{}])[0]
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_bytes(base64.b64decode(img["base64"]))
        print(f"inpainted -> {args.out}")
    elif args.cmd == "fetch":
        fetch_character(args.character, Path(args.out))


if __name__ == "__main__":
    main()
