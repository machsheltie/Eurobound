"""Extend the Green Fairy mural so its pixel/circuit base wraps the arch, per the reference.

The original decal stops on a straight line above the arch. In the production
reference the mosaic flares out over the archivolt's shoulders and runs down both
sides of the marquee, with circuit traces following the arch curve (denser
pixels on the right, traces on the left). This script:

  1. ray-casts the facade from the front to find what the paint must avoid
     (arch hero, windows, balconies, signs) and how far each wall point is from
     the arch silhouette;
  2. paints a pixel-mosaic + circuit "skirt" into a wider canvas around the
     original artwork (original pixels kept wherever they are opaque);
  3. rebuilds aa_decal_mural as a dense grid laid onto the walls and mouldings.

Writes m_aa_mural_decal_basecolor.png / _emissive.png (originals kept as *_v1.png).
Usage: exec in the live session (needs the layout instances visible).
"""

import math
import shutil
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

TEX = aa.REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/textures"
# The source artwork is 6.66 x 11 m at scale 1. Author ruling (2026-10-27): the
# figure ends halfway up the third set of windows (counting the arched ground
# window), i.e. ~11.7 m, so it is scaled down about the arch-anchored bottom.
ART_SIZE = (6.66, 11.0)
ART_BOTTOM = 5.05
ART_TOP = 11.7
OLD_SCALE = (ART_TOP - ART_BOTTOM) / ART_SIZE[1]
OLD_X = (-ART_SIZE[0] * OLD_SCALE / 2, ART_SIZE[0] * OLD_SCALE / 2)
OLD_Z = (ART_BOTTOM, ART_TOP)
CANVAS_X = (-4.6, 4.6)
CANVAS_Z = (3.6, 11.9)
MASK_STEP = 0.04          # m per ray for the avoid mask
GRID = 0.30               # mosaic cell, matches the original artwork's squares
SURFACE_OFFSET = 0.008    # decal sits this far off the stone
SEED = 13
# Where the pixel/circuit base spreads, read off the daytime reference: past the
# archivolt shoulders to the window columns, down to mid-marquee height.
FLARE_OUTLINE = [(-3.5, 4.0), (4.35, 4.0), (4.35, 6.4), (3.5, 6.6), (3.5, 8.4),
                 (2.2, 9.4), (-2.2, 9.0), (-3.4, 7.6), (-3.5, 5.7)]

ARCH_PREFIX = "aa_arch_hero"
AVOID_PREFIXES = (ARCH_PREFIX, "aa_window", "aa_balcony", "aa_prop_doorframe_sign",
                  "aa_prop_house_number", "aa_shell_facade_window_surrounds",
                  "aa_shell_facade_sash_windows", "aa_shell_facade_ironwork")
SURFACES = ("aa_shell_facade_walls", "aa_shell_facade_mouldings", "aa_shell_facade_quoins")

# sRGB 0..1
PIXEL_COLORS = {
    "lime": (0.62, 0.84, 0.30), "green": (0.27, 0.63, 0.30), "deep": (0.09, 0.40, 0.22),
    "teal": (0.05, 0.31, 0.27), "pale": (0.78, 0.86, 0.55),
    "purple": (0.42, 0.17, 0.63), "violet": (0.63, 0.40, 0.80),
}
GOLD = (0.80, 0.63, 0.27)
GOLD_DARK = (0.42, 0.30, 0.10)


def load_rgba(path, scale=1.0):
    img = bpy.data.images.load(str(path), check_existing=False)
    if scale != 1.0:
        img.scale(int(round(img.size[0] * scale)), int(round(img.size[1] * scale)))
    w, h = img.size
    arr = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(arr)
    bpy.data.images.remove(img)
    return arr.reshape(h, w, 4)     # row 0 = bottom


def save_rgba(arr, path):
    h, w = arr.shape[:2]
    img = bpy.data.images.new(path.stem, w, h, alpha=True)
    img.pixels.foreach_set(np.ascontiguousarray(arr, dtype=np.float32).ravel())
    img.filepath_raw = str(path)
    img.file_format = "PNG"
    img.save()
    bpy.data.images.remove(img)


def avoid_masks():
    """Front ray-cast of the facade: (arch mask, avoid mask) on a MASK_STEP grid."""
    mural_inst = bpy.data.objects.get("aa_decal_mural__01")
    if mural_inst:
        mural_inst.hide_viewport = True
    dg = bpy.context.evaluated_depsgraph_get()
    dg.update()
    xs = np.arange(CANVAS_X[0], CANVAS_X[1], MASK_STEP) + MASK_STEP / 2
    zs = np.arange(CANVAS_Z[0], CANVAS_Z[1], MASK_STEP) + MASK_STEP / 2
    arch = np.zeros((len(zs), len(xs)), bool)
    avoid = np.zeros_like(arch)
    sc = bpy.context.scene
    d = Vector((0, 1, 0))
    for j, z in enumerate(zs):
        for i, x in enumerate(xs):
            hit, loc, nrm, idx, obj, mat = sc.ray_cast(dg, Vector((x, -3.0, z)), d, distance=6.0)
            if not hit:
                avoid[j, i] = True
                continue
            name = obj.original.name if obj.original else obj.name
            if name.startswith(ARCH_PREFIX):
                arch[j, i] = avoid[j, i] = True
            elif name.startswith(AVOID_PREFIXES):
                avoid[j, i] = True
    if mural_inst:
        mural_inst.hide_viewport = False
    return arch, avoid


def distance_field(mask, step):
    """Chamfer distance (m) from True cells, two-pass 3-4 approximation."""
    big = 1e6
    d = np.where(mask, 0.0, big)
    h, w = d.shape
    a, b = 1.0, math.sqrt(2.0)
    for j in range(h):
        row = d[j]
        if j:
            up = d[j - 1]
            row = np.minimum(row, up + a)
            row[1:] = np.minimum(row[1:], up[:-1] + b)
            row[:-1] = np.minimum(row[:-1], up[1:] + b)
        for i in range(1, w):
            if row[i - 1] + a < row[i]:
                row[i] = row[i - 1] + a
        d[j] = row
    for j in range(h - 1, -1, -1):
        row = d[j]
        if j < h - 1:
            dn = d[j + 1]
            row = np.minimum(row, dn + a)
            row[1:] = np.minimum(row[1:], dn[:-1] + b)
            row[:-1] = np.minimum(row[:-1], dn[1:] + b)
        for i in range(w - 2, -1, -1):
            if row[i + 1] + a < row[i]:
                row[i] = row[i + 1] + a
        d[j] = row
    return d * step


def sample(field, xm, zm):
    """Bilinear sample of a MASK_STEP field at world coords (arrays)."""
    fx = (xm - CANVAS_X[0]) / MASK_STEP - 0.5
    fz = (zm - CANVAS_Z[0]) / MASK_STEP - 0.5
    h, w = field.shape
    x0 = np.clip(np.floor(fx).astype(int), 0, w - 2)
    z0 = np.clip(np.floor(fz).astype(int), 0, h - 2)
    tx = np.clip(fx - x0, 0, 1)
    tz = np.clip(fz - z0, 0, 1)
    f = field
    return ((f[z0, x0] * (1 - tx) + f[z0, x0 + 1] * tx) * (1 - tz)
            + (f[z0 + 1, x0] * (1 - tx) + f[z0 + 1, x0 + 1] * tx) * tz)


def flare_field():
    """Signed distance (m, positive inside) to the outline the mosaic flares out to."""
    xs = np.arange(CANVAS_X[0], CANVAS_X[1], MASK_STEP) + MASK_STEP / 2
    zs = np.arange(CANVAS_Z[0], CANVAS_Z[1], MASK_STEP) + MASK_STEP / 2
    X, Z = np.meshgrid(xs, zs)
    inside = np.zeros(X.shape, bool)
    pts = FLARE_OUTLINE
    for (x0, z0), (x1, z1) in zip(pts, pts[1:] + pts[:1]):
        crosses = (z0 > Z) != (z1 > Z)
        xi = x0 + (Z - z0) * (x1 - x0) / ((z1 - z0) or 1e-9)
        inside ^= crosses & (X < xi)
    return distance_field(~inside, MASK_STEP) - distance_field(inside, MASK_STEP)


def paint_skirt(ppm, dist, avoid_d, flare_d):
    W = int(round((CANVAS_X[1] - CANVAS_X[0]) * ppm))
    H = int(round((CANVAS_Z[1] - CANVAS_Z[0]) * ppm))
    col = np.zeros((H, W, 4), np.float32)
    emi = np.zeros((H, W, 4), np.float32)
    xm = (CANVAS_X[0] + (np.arange(W) + 0.5) / ppm).astype(np.float32)
    zm = (CANVAS_Z[0] + (np.arange(H) + 0.5) / ppm).astype(np.float32)
    X, Z = np.meshgrid(xm, zm)
    D = sample(dist, X, Z)
    clear = sample(avoid_d, X, Z) > 0.06       # stay 6 cm off windows, signs, the arch

    rng = np.random.default_rng(SEED)
    inside = sample(flare_d, X, Z)            # metres inside the flare outline
    zone = (inside > 0.0) & (D > 0.03) & clear

    # Circuit runs on the left flank: vertical gold traces dropping toward the
    # marquee, each turning in from the artwork and ending in a ring pad.
    trace = np.zeros((H, W), bool)
    pad = np.zeros((H, W), bool)
    for x_run in np.arange(-3.42, -2.7, 0.11):
        top = rng.uniform(5.6, 7.2)
        end = rng.uniform(4.05, 5.0)
        trace |= (np.abs(X - x_run) < 0.017) & (Z < top) & (Z > end)
        ring = (X - x_run) ** 2 + (Z - end) ** 2
        pad |= (ring < 0.045 ** 2) & (ring > 0.022 ** 2)
    # Offset curves hugging the archivolt on both shoulders.
    theta = np.arctan2(Z - 3.0, X)
    for k, r in enumerate((0.12, 0.26, 0.40)):
        wave = np.sin(theta * (7 + 2 * k) + rng.uniform(0, 6.28))
        trace |= (np.abs(D - r) < 0.017) & (wave > -0.35)
        pad |= (np.abs(D - r) < 0.04) & (np.abs(wave + 0.35) < 0.04)
    trace &= zone
    pad &= zone
    col[trace] = (*GOLD, 1.0)
    col[pad] = (*GOLD_DARK, 1.0)
    emi[trace] = (0.25, 0.9, 0.1, 1.0)

    # Pixel mosaic: solid inside the flare, dissolving into smaller, sparser
    # squares toward its outline; the right flank is denser and more purple.
    names = list(PIXEL_COLORS)
    cells_x = np.arange(CANVAS_X[0], CANVAS_X[1], GRID)
    cells_z = np.arange(CANVAS_Z[0], 10.0, GRID)
    for cz in cells_z:
        for cx in cells_x:
            mx, mz = cx + GRID / 2, cz + GRID / 2
            d = float(sample(dist, np.array([mx]), np.array([mz]))[0])
            fin = float(sample(flare_d, np.array([mx]), np.array([mz]))[0])
            if d <= 0.02 or fin <= -0.35:
                continue
            depth = (fin + 0.35) / (1.0 if mx > 0 else 1.5)
            p = min(1.0, max(0.0, depth)) ** 0.9
            if mx < 0:
                p *= 0.75
            if rng.random() > p:
                continue
            size = GRID * (0.86 if depth > 0.75 else (0.6 if depth > 0.4 else 0.38))
            if mx > 0:
                name = rng.choice(names, p=[0.12, 0.14, 0.12, 0.1, 0.06, 0.28, 0.18])
            else:
                name = rng.choice(names, p=[0.2, 0.22, 0.2, 0.16, 0.08, 0.09, 0.05])
            c = np.array(PIXEL_COLORS[name]) * rng.uniform(0.88, 1.06)
            x0 = int((mx - size / 2 - CANVAS_X[0]) * ppm)
            x1 = int((mx + size / 2 - CANVAS_X[0]) * ppm)
            z0 = int((mz - size / 2 - CANVAS_Z[0]) * ppm)
            z1 = int((mz + size / 2 - CANVAS_Z[0]) * ppm)
            x0, z0 = max(x0, 0), max(z0, 0)
            x1, z1 = min(x1, W), min(z1, H)
            if x1 <= x0 or z1 <= z0:
                continue
            ok = clear[z0:z1, x0:x1]
            blk = col[z0:z1, x0:x1]
            blk[ok] = (*np.clip(c, 0, 1), 1.0)
            # Thin dark rim and a centre dot, like the original squares.
            rim = max(2, int(0.012 * ppm))
            edge = np.zeros(ok.shape, bool)
            edge[:rim, :] = edge[-rim:, :] = True
            edge[:, :rim] = edge[:, -rim:] = True
            blk[edge & ok] = (*(np.clip(c, 0, 1) * 0.45), 1.0)
            yy, xx = np.mgrid[z0:z1, x0:x1]
            dot = ((xx - (x0 + x1) / 2) ** 2 + (yy - (z0 + z1) / 2) ** 2) < (0.022 * ppm) ** 2
            blk[dot & ok] = (*(np.clip(c, 0, 1) * 0.35), 1.0)
            if name in ("lime", "green", "purple", "violet", "pale"):
                e = emi[z0:z1, x0:x1]
                e[ok] = (*(np.clip(c, 0, 1) * 0.8), 1.0)
    return col, emi


def composite(old, skirt, ppm):
    H, W = skirt.shape[:2]
    out = skirt.copy()
    ox = int(round((OLD_X[0] - CANVAS_X[0]) * ppm))
    oz = int(round((OLD_Z[0] - CANVAS_Z[0]) * ppm))
    h, w = old.shape[:2]
    h, w = min(h, H - oz), min(w, W - ox)
    region = out[oz:oz + h, ox:ox + w]
    src = old[:h, :w]
    a = src[..., 3:4]
    region[..., :3] = src[..., :3] * a + region[..., :3] * (1 - a)
    region[..., 3:4] = np.maximum(a, region[..., 3:4])
    return out


def build_mesh(ppm):
    """Dense grid over the canvas, each vertex laid onto the nearest facade surface in front."""
    dg = bpy.context.evaluated_depsgraph_get()
    targets = []
    for name in SURFACES:
        obj = bpy.data.objects[name]
        ev = obj.evaluated_get(dg)
        me = ev.to_mesh()
        mw = obj.matrix_world
        targets.append(([mw @ v.co for v in me.vertices], [tuple(p.vertices) for p in me.polygons]))
        ev.to_mesh_clear()
    verts, polys, base = [], [], 0
    for vs, ps in targets:
        verts += vs
        polys += [tuple(i + base for i in p) for p in ps]
        base += len(vs)
    bvh = BVHTree.FromPolygons(verts, polys)
    step = 0.05
    nx = int(round((CANVAS_X[1] - CANVAS_X[0]) / step)) + 1
    nz = int(round((CANVAS_Z[1] - CANVAS_Z[0]) / step)) + 1
    co, uv = [], []
    for j in range(nz):
        z = CANVAS_Z[0] + j * step
        for i in range(nx):
            x = CANVAS_X[0] + i * step
            hit = bvh.ray_cast(Vector((x, -2.0, z)), Vector((0, 1, 0)), 4.0)
            y = (hit[0].y - SURFACE_OFFSET) if hit[0] is not None else -SURFACE_OFFSET
            co.append((x, y, z))
            uv.append(((x - CANVAS_X[0]) / (CANVAS_X[1] - CANVAS_X[0]),
                       (z - CANVAS_Z[0]) / (CANVAS_Z[1] - CANVAS_Z[0])))
    faces = [(j * nx + i, j * nx + i + 1, (j + 1) * nx + i + 1, (j + 1) * nx + i)
             for j in range(nz - 1) for i in range(nx - 1)]
    obj = bpy.data.objects["aa_decal_mural"]
    me = obj.data
    mats = list(me.materials)
    me.clear_geometry()
    me.from_pydata(co, [], faces)
    for name in [l.name for l in me.uv_layers]:
        me.uv_layers.remove(me.uv_layers[name])
    for name in ("uv_material", "uv_bake"):
        layer = me.uv_layers.new(name=name)
        for loop in me.loops:
            layer.data[loop.index].uv = uv[loop.vertex_index]
    me.materials.clear()
    for m in mats:
        me.materials.append(m)
    me.update()
    return len(co)


def main():
    # Always paint from the original artwork, so re-runs don't stack skirts.
    for stem in ("m_aa_mural_decal_basecolor", "m_aa_mural_decal_emissive"):
        backup = TEX / f"{stem}_v1.png"
        if not backup.exists():
            shutil.copy2(TEX / f"{stem}.png", backup)
    old_col = load_rgba(TEX / "m_aa_mural_decal_basecolor_v1.png", OLD_SCALE)
    old_emi = load_rgba(TEX / "m_aa_mural_decal_emissive_v1.png", OLD_SCALE)
    ppm = old_col.shape[0] / (OLD_Z[1] - OLD_Z[0])
    arch, avoid = avoid_masks()
    dist = distance_field(arch, MASK_STEP)
    avoid_d = distance_field(avoid, MASK_STEP)
    skirt_col, skirt_emi = paint_skirt(ppm, dist, avoid_d, flare_field())
    col = composite(old_col, skirt_col, ppm)
    # The emissive map has no useful alpha; composite it with the artwork's coverage.
    emi = composite(np.dstack([old_emi[..., :3], old_col[..., 3:4]]), skirt_emi, ppm)
    emi[..., 3] = 1.0
    save_rgba(col, TEX / "m_aa_mural_decal_basecolor.png")
    save_rgba(emi, TEX / "m_aa_mural_decal_emissive.png")
    for img in bpy.data.images:
        if img.filepath and "m_aa_mural_decal" in img.filepath:
            img.reload()
    n = build_mesh(ppm)
    return {"canvas_px": list(col.shape[:2]), "ppm": round(ppm, 2), "verts": n}


result = main()
print(result)
