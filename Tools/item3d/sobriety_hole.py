"""Darken the goal hole of the Sobriety Test Deluxe on its Tripo atlas (bead Eurobound-ioxj).

Run (headless):
  "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python Tools/item3d/sobriety_hole.py -- \
      dev/asset_team/icon_refs/aa_prize_sobriety_test_deluxe_tripo.glb dev/asset_team/icon_refs/aa_prize_sobriety_test_deluxe_tripo_hole.glb
then render the output GLB with Tools/item3d/render_item.py at the default framing (yaw 28, pitch 22, the framing of the
existing icon; the source GLB re-renders it pixel for pixel):
  ... render_item.py -- dev/asset_team/icon_refs/aa_prize_sobriety_test_deluxe_tripo_hole.glb game/assets/items/icons/3d/aa_prize_sobriety_test_deluxe_512.png

Why: blind A4 (qc_log round jmii-1) failed only the goal hole. Canon (game/assets/data/items/key_items.json;
design/worlds/debaucheryville/items/absinthe_arcade_prize_catalogue.md line 41) names "one hole", and the approved
reference (dev/asset_team/icon_refs/aa_prize_sobriety_test_deluxe_ref.png) shows it with a near-black interior. Tripo
painted the hole walls the same royal blue as the slab, so the render read as a shallow blue dimple.

Source GLB: Tripo Studio asset fe489ed7-2524-4b7a-8754-24c0ce5d7d22 (the 18,447-face retopo of rebuild 2, re-exported
as GLB with the 4k texture on 2026-11-17; export is free, 0 credits). GLBs are gitignored, so the file lives only on disk.

What it paints (fixed, deterministic; no hand edits, no image tool): only texels of faces inside the hole, found from
the 3D geometry. Everything else on the atlas is written back unchanged.
  * The hole is the empty circular pit at the goal end of the bottom path. Its axis is found by a circle fit to the
    near-vertical wall faces around HOLE_GUESS (model units, Tripo export, Z up); RIM_Z is the median height of the
    up-facing groove floor in a ring just outside the wall.
  * A face belongs to the hole when its centre lies within the fitted radius + RIM_PAD of the axis and below RIM_Z.
    Faces of the groove walls sit above the groove floor, so they are never selected.
  * Each selected texel is mixed toward HOLE_BLACK by depth below the rim: the lip (the first LIP_DEPTH units) ramps
    from the old blue to black, so the edge stays a crisp round opening rather than a painted disc.
  * Chart gutters next to painted texels are dilated so texture filtering never pulls the old blue back in.
"""
import os
import sys

import bpy
import numpy as np

HOLE_GUESS = (0.268, -0.382)      # approx. hole centre on the top-down plan (x, y), model units
SEARCH_R = 0.07                   # wall faces within this radius of HOLE_GUESS feed the circle fit
FLOOR_RING = (0.07, 0.10)         # ring (radii) where the groove floor around the hole is measured
RIM_PAD = 0.004                   # selection radius = fitted wall radius + this (the rounded lip only; more paints the channel mouth)
RIM_EPS = 0.003                   # texels this far below the floor already start to darken
LIP_DEPTH = 0.012                 # depth over which the lip ramps from the old blue to HOLE_BLACK
MIN_Z = 0.05                      # ignore the slab's bottom faces (z ~ 0)
HOLE_BLACK = np.array([5, 5, 8], np.float32) / 255.0   # near black, the reference interior (lum ~3)


def base_image(mat):
    for link in mat.node_tree.links:
        if link.to_node.type == "BSDF_PRINCIPLED" and link.to_socket.name == "Base Color" \
                and link.from_node.type == "TEX_IMAGE":
            return link.from_node.image
    raise SystemExit("no base colour image")


def raster(uv_px, H, W):
    """Yield (rows, cols, barycentrics) of texel centres inside one triangle given in pixel coords."""
    (x0, y0), (x1, y1), (x2, y2) = uv_px
    c0, c1 = int(np.floor(min(x0, x1, x2))), int(np.ceil(max(x0, x1, x2)))
    r0, r1 = int(np.floor(min(y0, y1, y2))), int(np.ceil(max(y0, y1, y2)))
    c0, r0, c1, r1 = max(c0, 0), max(r0, 0), min(c1, W - 1), min(r1, H - 1)
    if c1 < c0 or r1 < r0:
        return None
    cs, rs = np.meshgrid(np.arange(c0, c1 + 1), np.arange(r0, r1 + 1))
    px, py = cs.ravel() + 0.5, rs.ravel() + 0.5
    den = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
    if abs(den) < 1e-12:
        return None
    b0 = ((y1 - y2) * (px - x2) + (x2 - x1) * (py - y2)) / den
    b1 = ((y2 - y0) * (px - x2) + (x0 - x2) * (py - y2)) / den
    b2 = 1 - b0 - b1
    m = (b0 >= -1e-6) & (b1 >= -1e-6) & (b2 >= -1e-6)
    if not m.any():
        return None
    return rs.ravel()[m], cs.ravel()[m], np.stack([b0[m], b1[m], b2[m]], 1)


def dilate(img, painted, covered, steps=4):
    """Grow painted texels into uncovered gutter texels so filtering never reads the old paint."""
    for _ in range(steps):
        grow = np.zeros_like(painted)
        src = np.zeros_like(img)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            sh_p = np.roll(painted, (dr, dc), (0, 1))
            sh_i = np.roll(img, (dr, dc), (0, 1))
            new = sh_p & ~painted & ~covered & ~grow
            src[new] = sh_i[new]
            grow |= new
        img[grow] = src[grow]
        painted |= grow


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    src, dst = os.path.abspath(argv[0]), os.path.abspath(argv[1])
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    meshes = [o for o in bpy.data.objects if o.type == "MESH"]
    if len(meshes) != 1:
        raise SystemExit("expected one Tripo mesh, found %d" % len(meshes))
    obj = meshes[0]
    me = obj.data
    me.calc_loop_triangles()
    im = base_image(obj.material_slots[0].material)
    W, H = im.size
    mw = np.array(obj.matrix_world, np.float32)

    co = np.empty(len(me.vertices) * 3, np.float32); me.vertices.foreach_get("co", co)
    co = co.reshape(-1, 3) @ mw[:3, :3].T + mw[:3, 3]
    uvl = np.empty(len(me.loops) * 2, np.float32); me.uv_layers.active.data.foreach_get("uv", uvl); uvl = uvl.reshape(-1, 2)
    nt = len(me.loop_triangles)
    tv = np.empty(nt * 3, np.int32); me.loop_triangles.foreach_get("vertices", tv); tv = tv.reshape(-1, 3)
    tl = np.empty(nt * 3, np.int32); me.loop_triangles.foreach_get("loops", tl); tl = tl.reshape(-1, 3)
    tp = np.empty(nt, np.int32); me.loop_triangles.foreach_get("polygon_index", tp)
    npoly = len(me.polygons)
    pn = np.empty(npoly * 3, np.float32); me.polygons.foreach_get("normal", pn)
    pn = pn.reshape(-1, 3) @ mw[:3, :3].T
    pn /= np.linalg.norm(pn, axis=1, keepdims=True) + 1e-12
    pc = np.empty(npoly * 3, np.float32); me.polygons.foreach_get("center", pc)
    pc = pc.reshape(-1, 3) @ mw[:3, :3].T + mw[:3, 3]

    # --- hole axis: circle fit to the near-vertical wall faces around the guess, below the groove floor
    d0 = np.linalg.norm(pc[:, :2] - np.array(HOLE_GUESS), axis=1)
    ring = (d0 > FLOOR_RING[0]) & (d0 < FLOOR_RING[1]) & (pn[:, 2] > 0.8) & (pc[:, 2] > MIN_Z)
    rim_z = float(np.median(pc[ring, 2]))
    wall = (d0 < SEARCH_R) & (np.abs(pn[:, 2]) < 0.3) & (pc[:, 2] > MIN_Z) & (pc[:, 2] < rim_z)
    if wall.sum() < 50:
        raise SystemExit("hole walls not found (%d faces)" % wall.sum())
    x, y = pc[wall, 0], pc[wall, 1]
    s = np.linalg.lstsq(np.c_[2 * x, 2 * y, np.ones_like(x)], x * x + y * y, rcond=None)[0]
    cx, cy = s[0], s[1]
    radius = float(np.sqrt(s[2] + cx * cx + cy * cy))
    if not (0.03 < radius < 0.08) or np.hypot(cx - HOLE_GUESS[0], cy - HOLE_GUESS[1]) > 0.03:
        raise SystemExit("hole fit off: centre %.3f,%.3f radius %.3f" % (cx, cy, radius))
    sel_r = radius + RIM_PAD

    d = np.linalg.norm(pc[:, :2] - np.array([cx, cy]), axis=1)
    hole = (d < sel_r) & (pc[:, 2] > MIN_Z) & (pc[:, 2] < rim_z + RIM_EPS)

    # --- paint
    pix = np.empty(W * H * 4, np.float32); im.pixels.foreach_get(pix); pix = pix.reshape(H, W, 4)
    before = pix.copy()
    tuv = uvl[tl]
    tri_px = np.stack([tuv[..., 0] * W, tuv[..., 1] * H], -1)   # Blender pixel rows run bottom-up, like v
    sel_t = np.where(hole[tp])[0]
    covered = np.zeros((H, W), bool)
    painted = np.zeros((H, W), bool)
    img = pix[..., :3]
    # coverage of every triangle near the hole charts, so dilation only fills true gutters
    b = tri_px[sel_t].reshape(-1, 2)
    lo, hi = b.min(0) - 8, b.max(0) + 8
    near = np.where(((tri_px.max(1) >= lo) & (tri_px.min(1) <= hi)).all(1))[0]
    for t in near:
        r = raster(tri_px[t], H, W)
        if r is not None:
            covered[r[0], r[1]] = True
    n_tex = 0
    for t in sel_t:
        r = raster(tri_px[t], H, W)
        if r is None:
            continue
        rows, cols, bc = r
        p3 = bc @ co[tv[t]]                                         # 3D position of every texel
        depth = (rim_z + RIM_EPS) - p3[:, 2]
        rad = np.linalg.norm(p3[:, :2] - np.array([cx, cy]), axis=1)
        a = np.clip(depth / LIP_DEPTH, 0, 1) * (rad < sel_r)
        a = (a * a * (3 - 2 * a))[:, None]                           # smoothstep: soft lip, solid black below it
        img[rows, cols] = img[rows, cols] * (1 - a) + HOLE_BLACK * a
        painted[rows, cols] |= a[:, 0] > 0
        n_tex += int((a[:, 0] > 0).sum())
    bb = tri_px[sel_t].reshape(-1, 2)
    c0, r0 = np.maximum(np.floor(bb.min(0)).astype(int) - 6, 0)
    c1, r1 = np.minimum(np.ceil(bb.max(0)).astype(int) + 6, [W, H])
    sub_i, sub_p = img[r0:r1, c0:c1], painted[r0:r1, c0:c1]
    dilate(sub_i, sub_p, covered[r0:r1, c0:c1])
    img[r0:r1, c0:c1], painted[r0:r1, c0:c1] = sub_i, sub_p
    changed = np.abs(pix - before).max(-1) > 1e-6

    # write the atlas to a temporary PNG, load it as a fresh packed image, swap it into the material, export
    out = bpy.data.images.new("aa_prize_sobriety_test_deluxe_basecolor", W, H, alpha=True)
    out.pixels.foreach_set(pix.ravel())
    png = os.path.splitext(dst)[0] + "_basecolor_tmp.png"
    out.filepath_raw = png
    out.file_format = "PNG"
    out.save()
    new = bpy.data.images.load(png)
    new.pack()
    for link in obj.material_slots[0].material.node_tree.links:
        if link.to_socket.name == "Base Color" and link.from_node.type == "TEX_IMAGE":
            link.from_node.image = new
    bpy.ops.export_scene.gltf(filepath=dst, export_format="GLB", export_image_format="AUTO")
    os.remove(png)
    print("ATLAS %dx%d" % (W, H))
    print("HOLE centre %.4f,%.4f radius %.4f (select %.4f), rim z %.4f, %d wall faces in fit"
          % (cx, cy, radius, sel_r, rim_z, wall.sum()))
    print("FACES hole %d, triangles %d; TEXELS painted %d, changed incl. gutters %d"
          % (hole.sum(), len(sel_t), n_tex, changed.sum()))
    print("WROTE", dst)


main()
