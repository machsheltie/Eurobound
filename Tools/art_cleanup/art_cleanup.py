"""Cleanup for AI-generated sprites and props (Firefly / GPT image) before they go into Godot.

Run with the bundled venv:
    tools/art_cleanup/.venv/Scripts/python tools/art_cleanup/art_cleanup.py <command> ...

Commands (each takes one or more input files or globs, writes to --out):
    cutout    Remove the background. AI model (rembg) by default, or --key for a flat
              colour background (fast, exact, no model download).
    defringe  Kill the light/dark halo AI cutouts leave on edges: drop near-transparent
              pixels and bleed edge colour outward so Godot's filtering doesn't pull in
              the old background.
    trim      Crop to visible pixels, pad, and optionally anchor to a fixed canvas with the
              feet on the bottom edge (consistent pivots for billboards).
    palette   'extract' a palette PNG from reference art, or 'apply' one so a batch of
              generations shares the same colours.
    sheet     Contact sheet on checker / dark / light backgrounds for halo and
              consistency review. Read the result before shipping anything.
    pipeline  cutout -> defringe -> trim in one pass.
"""
from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


# ---------------------------------------------------------------- helpers

def expand(patterns: list[str]) -> list[Path]:
    files: list[Path] = []
    for p in patterns:
        hits = glob.glob(p, recursive=True)
        files.extend(Path(h) for h in (hits or [p]))
    missing = [f for f in files if not f.is_file()]
    if missing:
        sys.exit(f"not found: {', '.join(map(str, missing))}")
    return files


def out_path(src: Path, out: str | None, suffix: str = "") -> Path:
    base = Path(out) if out else src.parent / "cleaned"
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{src.stem}{suffix}.png"


def rgba(img: Image.Image) -> Image.Image:
    return img if img.mode == "RGBA" else img.convert("RGBA")


# ---------------------------------------------------------------- cutout

_session = None


def cutout_ai(img: Image.Image, model: str, matting: bool) -> Image.Image:
    global _session
    from rembg import new_session, remove  # imported lazily: heavy

    if _session is None:
        _session = new_session(model)
    return rgba(remove(img, session=_session, alpha_matting=matting,
                       alpha_matting_foreground_threshold=240,
                       alpha_matting_background_threshold=15,
                       alpha_matting_erode_size=8))


def cutout_key(img: Image.Image, key: str | None, tol: float, soft: float) -> Image.Image:
    a = np.asarray(rgba(img)).astype(np.float32)
    rgb = a[..., :3]
    if key in (None, "auto"):
        # Sample the border: AI "plain background" prompts give a near-uniform frame.
        border = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]])
        k = np.median(border, axis=0)
    else:
        k = np.array(Image.new("RGB", (1, 1), key).getpixel((0, 0)), np.float32)
    dist = np.linalg.norm(rgb - k, axis=-1)
    alpha = np.clip((dist - tol) / max(soft, 1e-3), 0, 1)
    # Despill: pull the key colour out of semi-transparent edge pixels.
    w = alpha[..., None]
    safe = np.where(w > 0.01, w, 1)
    rgb = np.where(w > 0.01, np.clip((rgb - k * (1 - w)) / safe, 0, 255), rgb)
    a[..., :3] = rgb
    a[..., 3] = np.minimum(a[..., 3], alpha * 255)
    return Image.fromarray(a.astype(np.uint8), "RGBA")


# ---------------------------------------------------------------- defringe

def defringe(img: Image.Image, floor: int, erode: int, bleed: int) -> Image.Image:
    img = rgba(img)
    a = np.asarray(img).copy()
    alpha = a[..., 3]
    alpha[alpha < floor] = 0
    if erode:
        m = Image.fromarray(alpha).filter(ImageFilter.MinFilter(erode * 2 + 1))
        alpha = np.minimum(alpha, np.asarray(m))
    a[..., 3] = alpha
    # Bleed: fill RGB of fully transparent pixels with nearest opaque colour so bilinear
    # filtering / mipmaps in Godot never sample the old background.
    rgb = a[..., :3].astype(np.float32)
    known = alpha > 0
    for _ in range(bleed):
        if known.all():
            break
        acc = np.zeros_like(rgb)
        cnt = np.zeros(alpha.shape, np.float32)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == dx == 0:
                    continue
                k = np.roll(np.roll(known, dy, 0), dx, 1)
                acc += np.roll(np.roll(rgb, dy, 0), dx, 1) * k[..., None]
                cnt += k
        grow = (~known) & (cnt > 0)
        rgb[grow] = acc[grow] / cnt[grow][:, None]
        known |= grow
    a[..., :3] = rgb.astype(np.uint8)
    return Image.fromarray(a, "RGBA")


# ---------------------------------------------------------------- trim

def trim(img: Image.Image, pad: int, canvas: tuple[int, int] | None, anchor: str) -> Image.Image:
    img = rgba(img)
    bbox = img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    if not bbox:
        return img
    img = img.crop(bbox)
    if canvas is None:
        out = Image.new("RGBA", (img.width + pad * 2, img.height + pad * 2), (0, 0, 0, 0))
        out.paste(img, (pad, pad))
        return out
    cw, ch = canvas
    scale = min((cw - pad * 2) / img.width, (ch - pad * 2) / img.height, 1.0)
    if scale < 1.0:
        img = img.resize((max(1, round(img.width * scale)), max(1, round(img.height * scale))),
                         Image.LANCZOS)
    x = (cw - img.width) // 2
    y = ch - pad - img.height if anchor == "bottom" else (ch - img.height) // 2
    out = Image.new("RGBA", canvas, (0, 0, 0, 0))
    out.paste(img, (x, y))
    return out


# ---------------------------------------------------------------- palette

def palette_extract(files: list[Path], colors: int, out: Path) -> None:
    pixels = []
    for f in files:
        a = np.asarray(rgba(Image.open(f)))
        pixels.append(a[a[..., 3] > 128][:, :3])
    allpx = np.concatenate(pixels)
    if len(allpx) > 400_000:
        allpx = allpx[np.random.default_rng(0).choice(len(allpx), 400_000, replace=False)]
    strip = Image.fromarray(allpx[None, :, :].astype(np.uint8), "RGB")
    q = strip.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
    pal = np.array(q.getpalette()[: colors * 3], np.uint8).reshape(-1, 3)
    swatch = Image.fromarray(np.repeat(np.repeat(pal[None], 16, 0), 16, 1), "RGB")
    out.parent.mkdir(parents=True, exist_ok=True)
    swatch.save(out)
    print(f"palette ({len(pal)} colours) -> {out}")


def palette_apply(img: Image.Image, palette_png: Path, strength: float, dither: bool) -> Image.Image:
    img = rgba(img)
    pal = np.asarray(Image.open(palette_png).convert("RGB")).reshape(-1, 3)
    pal = np.unique(pal, axis=0)[:256]
    pimg = Image.new("P", (1, 1))
    flat = pal.flatten().tolist()
    pimg.putpalette(flat + flat[:3] * (256 - len(pal)))
    q = img.convert("RGB").quantize(palette=pimg, dither=Image.Dither.FLOYDSTEINBERG if dither
                                    else Image.Dither.NONE).convert("RGB")
    mixed = Image.blend(img.convert("RGB"), q, strength)
    mixed.putalpha(img.getchannel("A"))
    return mixed


# ---------------------------------------------------------------- sheet

def checker(size: tuple[int, int], cell: int = 12) -> Image.Image:
    im = Image.new("RGB", size, (200, 200, 200))
    d = ImageDraw.Draw(im)
    for y in range(0, size[1], cell):
        for x in range((y // cell % 2) * cell, size[0], cell * 2):
            d.rectangle([x, y, x + cell - 1, y + cell - 1], fill=(150, 150, 150))
    return im


def sheet(files: list[Path], out: Path, tile: int) -> None:
    bgs = [("checker", None), ("dark", (20, 16, 28)), ("light", (245, 240, 228)),
           ("magenta", (255, 0, 255))]
    label_h = 18
    W = tile * len(bgs)
    H = (tile + label_h) * len(files)
    canvas = Image.new("RGB", (W, H), (40, 40, 40))
    d = ImageDraw.Draw(canvas)
    for r, f in enumerate(files):
        im = rgba(Image.open(f))
        im.thumbnail((tile - 8, tile - 8), Image.LANCZOS)
        y0 = r * (tile + label_h)
        d.text((4, y0 + 2), f.name, fill=(230, 230, 230))
        for c, (_, col) in enumerate(bgs):
            bg = checker((tile, tile)) if col is None else Image.new("RGB", (tile, tile), col)
            bg.paste(im, ((tile - im.width) // 2, (tile - im.height) // 2), im)
            canvas.paste(bg, (c * tile, y0 + label_h))
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out)
    print(f"sheet -> {out}")


# ---------------------------------------------------------------- cli

def parse_canvas(s: str | None) -> tuple[int, int] | None:
    if not s:
        return None
    w, h = s.lower().split("x")
    return int(w), int(h)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p, out_default_help="folder (default: <input dir>/cleaned)"):
        p.add_argument("inputs", nargs="+")
        p.add_argument("--out", help=out_default_help)

    def cut_args(p):
        p.add_argument("--key", nargs="?", const="auto",
                       help="chroma-key instead of AI; colour like '#00ff00', or omit value to sample the border")
        p.add_argument("--tol", type=float, default=30, help="key: distance fully removed")
        p.add_argument("--soft", type=float, default=40, help="key: feather width")
        p.add_argument("--model", default="isnet-general-use",
                       help="rembg model: isnet-general-use | isnet-anime | u2net | birefnet-general")
        p.add_argument("--matting", action="store_true", help="rembg alpha matting (hair, soft edges)")

    def fringe_args(p):
        p.add_argument("--floor", type=int, default=24, help="alpha below this becomes 0")
        p.add_argument("--erode", type=int, default=0, help="shrink alpha edge by N px")
        p.add_argument("--bleed", type=int, default=16, help="px of colour bleed into transparency")

    def trim_args(p):
        p.add_argument("--pad", type=int, default=4)
        p.add_argument("--canvas", help="fixed WxH canvas, e.g. 512x768")
        p.add_argument("--anchor", choices=["bottom", "center"], default="bottom")

    p = sub.add_parser("cutout"); common(p); cut_args(p)
    p = sub.add_parser("defringe"); common(p); fringe_args(p)
    p = sub.add_parser("trim"); common(p); trim_args(p)
    p = sub.add_parser("pipeline"); common(p); cut_args(p); fringe_args(p); trim_args(p)

    p = sub.add_parser("palette")
    p.add_argument("action", choices=["extract", "apply"])
    p.add_argument("inputs", nargs="+")
    p.add_argument("--out", help="extract: palette PNG path; apply: output folder")
    p.add_argument("--colors", type=int, default=32)
    p.add_argument("--palette", help="apply: palette PNG")
    p.add_argument("--strength", type=float, default=1.0, help="apply: 0..1 blend toward palette")
    p.add_argument("--dither", action="store_true")

    p = sub.add_parser("sheet")
    p.add_argument("inputs", nargs="+")
    p.add_argument("--out", required=True, help="sheet PNG path")
    p.add_argument("--tile", type=int, default=256)

    a = ap.parse_args()

    if a.cmd == "sheet":
        return sheet(expand(a.inputs), Path(a.out), a.tile)
    if a.cmd == "palette" and a.action == "extract":
        return palette_extract(expand(a.inputs), a.colors, Path(a.out or "palette.png"))

    for f in expand(a.inputs):
        img = Image.open(f)
        if a.cmd in ("cutout", "pipeline"):
            img = cutout_key(img, a.key, a.tol, a.soft) if a.key else cutout_ai(img, a.model, a.matting)
        if a.cmd in ("defringe", "pipeline"):
            img = defringe(img, a.floor, a.erode, a.bleed)
        if a.cmd in ("trim", "pipeline"):
            img = trim(img, a.pad, parse_canvas(a.canvas), a.anchor)
        if a.cmd == "palette":
            if not a.palette:
                sys.exit("palette apply needs --palette")
            img = palette_apply(img, Path(a.palette), a.strength, a.dither)
        dst = out_path(f, a.out)
        img.save(dst)
        print(f"{f.name} -> {dst}")


if __name__ == "__main__":
    main()
