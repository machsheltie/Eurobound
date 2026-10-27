"""Build aa_shell_facade as real masonry (architectural quality pass, 2026-10-27).

The facade is no longer one plane with things stuck on it. Depth planes, from
the street inward:

  plinth (proud 0.26)  ->  ground-floor banded rustication (0.10)  ->  wall (0)
  central entrance bay (risalit, proud 0.16 above the ground cornice) with
  edge lesenes (0.24)

Windows are openings cut through 0.55 m of masonry with reveals, casements set
back in them, and surrounds that differ by storey (heavy ground floor, richest
first floor, plainer above, one later repair). The entrance is a deep arch with
three stepped orders of individual voussoirs, rusticated jambs and a projecting
keystone that carries the Headphone Gentleman. String courses are dimensional
sill courses with drips; the eave cornice has frieze, dentils, modillions and
a corona with a shadowed soffit. Quoins are quieter, varied, upper floors only.

Every piece is a closed solid with small bevels so edges catch light.
Blender space: side-bay wall face on y=0, street toward -Y, z up.
Re-runnable: replaces the shell collection's contents (and the arch hero's
archivolt/plinth meshes). Dimensions come from manifest.json -> building.
"""

import math
import random
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

SEED = 1907                      # the building's construction year, near enough
WALL_T = 0.55                    # masonry thickness at the facade
BEVEL = 0.012                    # default arris softening on stone

# Depth planes (proud distance toward the street, metres)
PLINTH_P, RUST_P, BAY_P, LESENE_P = 0.26, 0.10, 0.16, 0.24
PLINTH_TOP = 0.72
RUST_TOP = 5.55                  # rustication stops under the ground cornice
BAY_HALF = 3.3                   # central entrance bay half-width
LESENE_W = 0.32

# Entrance (shared with aa_arch_hero)
ARCH_HALF, ARCH_SPRING, ARCH_RISE, ARCH_DEPTH = 2.2, 3.6, 1.9, 1.6
ORDERS = [(0.16, 0.10), (0.36, 0.18), (0.58, 0.27)]   # (ring width outward, proud)
KEYSTONE = (0.78, 1.05, 0.46)    # width at top, height, proud

# Windows: (x, sill z, storey style)
UPPER_WINDOWS = [(x, z, s) for z, s in ((6.9, "piano"), (10.5, "middle"), (14.1, "upper"))
                 for x in (-4.6, 4.6)]
REPAIRED = (4.6, 10.5)           # later replacement lintel and sill
# Author ruling 2026-10-27: the black cat sits outside the left first-floor window, which
# is open. Leaf swing in degrees (left leaf, right leaf), inward.
OPEN_WINDOWS = {(-4.6, 6.9): (42.0, 35.0)}
WIN_W, WIN_H = 1.16, 1.85
CASEMENT_SET = 0.24              # how far the frame sits back from the wall face


# --------------------------------------------------------------------------- mesh helpers

def material(name, color, rough=0.8, metallic=0.0, alpha=1.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metallic
    b.inputs["Alpha"].default_value = alpha
    if alpha < 1.0:
        m.surface_render_method = "DITHERED"
    m.diffuse_color = (*color, 1)
    return m


class Builder:
    """Accumulates closed solids into one bmesh with per-face material indices."""

    def __init__(self):
        self.bm = bmesh.new()

    def _finish(self, verts, mat, bevel):
        faces = list({f for v in verts for f in v.link_faces})
        for f in faces:
            f.material_index = mat
        if bevel:
            edges = list({e for v in verts for e in v.link_edges})
            bmesh.ops.bevel(self.bm, geom=edges, offset=bevel, segments=2, profile=0.6,
                            affect="EDGES", clamp_overlap=True)

    def box(self, x0, x1, y0, y1, z0, z1, mat=0, bevel=BEVEL):
        r = bmesh.ops.create_cube(self.bm, size=1.0)
        c = Vector(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2))
        s = Vector((x1 - x0, y1 - y0, z1 - z0))
        for v in r["verts"]:
            v.co = c + Vector((v.co.x * s.x, v.co.y * s.y, v.co.z * s.z))
        self._finish(r["verts"], mat, min(bevel, min(s) * 0.3))
        return r["verts"]

    def prism(self, outline_xz, y0, y1, mat=0, bevel=BEVEL):
        """Extrude a closed (x, z) outline from y0 to y1 into a solid."""
        front = [self.bm.verts.new((x, y0, z)) for x, z in outline_xz]
        back = [self.bm.verts.new((x, y1, z)) for x, z in outline_xz]
        n = len(outline_xz)
        self.bm.faces.new(front)
        self.bm.faces.new(back[::-1])
        for i in range(n):
            j = (i + 1) % n
            self.bm.faces.new((front[i], back[i], back[j], front[j]))
        verts = front + back
        bmesh.ops.recalc_face_normals(self.bm, faces=list({f for v in verts for f in v.link_faces}))
        self._finish(verts, mat, bevel)
        return verts

    def sweep(self, profile, x0, x1, y_base=0.0, mat=0):
        """Moulding: a (proud, z) profile swept along X from x0 to x1, capped."""
        left = [self.bm.verts.new((x0, y_base - p, z)) for p, z in profile]
        right = [self.bm.verts.new((x1, y_base - p, z)) for p, z in profile]
        n = len(profile)
        for i in range(n - 1):
            f = self.bm.faces.new((left[i], left[i + 1], right[i + 1], right[i]))
            f.material_index = mat
        for cap in (left, right[::-1]):
            f = self.bm.faces.new(cap)
            f.material_index = mat
        bmesh.ops.recalc_face_normals(self.bm, faces=list({f for v in left + right for f in v.link_faces}))

    def to_object(self, name, mats, coll):
        bmesh.ops.remove_doubles(self.bm, verts=self.bm.verts, dist=1e-5)
        box_uvs(self.bm)
        me = bpy.data.meshes.get(name) or bpy.data.meshes.new(name)
        self.bm.to_mesh(me)
        self.bm.free()
        me.materials.clear()
        for m in mats:
            me.materials.append(m)
        me.set_sharp_from_angle(angle=math.radians(35))
        obj = bpy.data.objects.get(name) or bpy.data.objects.new(name, me)
        obj.data = me
        if obj.name not in coll.objects:
            coll.objects.link(obj)
        return obj


def box_uvs(bm, tile=2.8):
    uvm = bm.loops.layers.uv.get("uv_material") or bm.loops.layers.uv.new("uv_material")
    uvb = bm.loops.layers.uv.get("uv_bake") or bm.loops.layers.uv.new("uv_bake")
    if not bm.verts:
        return
    lo = [min(v.co[i] for v in bm.verts) for i in range(3)]
    hi = [max(v.co[i] for v in bm.verts) for i in range(3)]
    for f in bm.faces:
        ax = max(range(3), key=lambda i: abs(f.normal[i]))
        a, b = [i for i in range(3) if i != ax]
        for lp in f.loops:
            c = lp.vert.co
            lp[uvm].uv = (c[a] / tile, c[b] / tile)
            lp[uvb].uv = ((c[a] - lo[a]) / max(hi[a] - lo[a], 1e-6) * 0.98 + 0.01,
                          (c[b] - lo[b]) / max(hi[b] - lo[b], 1e-6) * 0.98 + 0.01)


def arch_outline(half, spring, rise, n=40, bottom=0.0):
    """Closed (x, z) outline of a segmental-elliptic arch opening down to `bottom`."""
    pts = [(-half, bottom), (-half, spring)]
    for i in range(1, n):
        t = math.pi - math.pi * i / n
        pts.append((half * math.cos(t), spring + rise * math.sin(t)))
    pts += [(half, spring), (half, bottom)]
    return pts


def arch_point(half, spring, rise, t, off=0.0):
    """Point on the arch intrados at angle t (0..pi), pushed outward along its normal."""
    p = Vector((half * math.cos(t), spring + rise * math.sin(t)))
    n = Vector((math.cos(t) / max(half, 1e-6), math.sin(t) / max(rise, 1e-6))).normalized()
    return p + n * off


# --------------------------------------------------------------------------- masonry

def facade_wall(B, cutters):
    """Wall slab, rustication, central bay and lesenes, with openings boolean-cut."""
    W, EAVE = B["facade_width"], B["eave_height"]
    hx = W / 2
    b = Builder()
    b.box(-hx, hx, 0.0, WALL_T, 0.0, EAVE, bevel=0.0)
    b.box(-hx, hx, -RUST_P, 0.0, PLINTH_TOP, RUST_TOP, bevel=0.0)
    b.box(-BAY_HALF, BAY_HALF, -BAY_P, 0.0, RUST_TOP, EAVE - 0.85, bevel=0.0)
    for sx in (-1, 1):
        x0, x1 = sorted((sx * BAY_HALF, sx * (BAY_HALF - LESENE_W)))
        b.box(x0, x1, -LESENE_P, -BAY_P + 0.01, RUST_TOP + 0.45, EAVE - 0.85, bevel=0.008)
    # Hull: side walls, back wall and gables (silhouette only).
    D, RIDGE = B["depth"], B["ridge_height"]
    b.box(-hx, -hx + 0.3, WALL_T, D, 0.0, EAVE, bevel=0.0)
    b.box(hx - 0.3, hx, WALL_T, D, 0.0, EAVE, bevel=0.0)
    b.box(-hx, hx, D - 0.3, D, 0.0, EAVE, bevel=0.0)
    for sx in (-1, 1):
        g = [b.bm.verts.new((sx * hx, y, z)) for y, z in ((0.0, EAVE), (D, EAVE), (D / 2, RIDGE))]
        b.bm.faces.new(g if sx > 0 else g[::-1])
    stone = bpy.data.materials["m_aa_limestone_weathered"]
    obj = b.to_object("aa_shell_facade_walls", [stone], shell_coll())
    for c in cutters:
        mod = obj.modifiers.new(c.name, "BOOLEAN")
        mod.operation = "DIFFERENCE"
        mod.solver = "EXACT"
        mod.use_self = True             # the wall is overlapping solids, not one shell
        mod.use_hole_tolerant = True
        mod.object = c
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(obj.evaluated_get(dg))
    old = obj.data
    obj.modifiers.clear()
    obj.data = me
    bpy.data.meshes.remove(old)
    me.name = "aa_shell_facade_walls"
    for c in cutters:
        bpy.data.objects.remove(c, do_unlink=True)
    return obj


def cutter(name, outline_xz, y0, y1):
    b = Builder()
    b.prism(outline_xz, y0, y1, bevel=0.0)
    me = bpy.data.meshes.new(name)
    b.bm.to_mesh(me)
    b.bm.free()
    obj = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(obj)
    obj.hide_render = True
    return obj


def rustication_cutter(B):
    """Banded rustication: horizontal channels cut 35 mm into the ground-floor face."""
    hx = B["facade_width"] / 2
    b = Builder()
    z = PLINTH_TOP + 0.48
    while z < RUST_TOP - 0.2:
        for x0, x1 in ((-hx - 0.05, -ARCH_HALF - ORDERS[-1][0] - 0.05),
                       (ARCH_HALF + ORDERS[-1][0] + 0.05, hx + 0.05)):
            b.box(x0, x1, -RUST_P - 0.05, -RUST_P + 0.035, z - 0.022, z + 0.022, bevel=0.0)
        z += 0.48
    me = bpy.data.meshes.new("aa_cut_rustication")
    b.bm.to_mesh(me)
    b.bm.free()
    obj = bpy.data.objects.new("aa_cut_rustication", me)
    bpy.context.scene.collection.objects.link(obj)
    obj.hide_render = True
    return obj


def mouldings(B):
    W, EAVE, GF = B["facade_width"], B["eave_height"], B["ground_floor_height"]
    hx = W / 2
    b = Builder()
    # Plinth: base course with a weathered chamfer and a torus.
    b.sweep([(0, 0), (PLINTH_P, 0), (PLINTH_P, 0.5), (PLINTH_P - 0.04, 0.54), (PLINTH_P - 0.04, 0.6),
             (RUST_P + 0.04, PLINTH_TOP - 0.02), (RUST_P, PLINTH_TOP), (0, PLINTH_TOP)],
            -hx - PLINTH_P, hx + PLINTH_P)
    # Ground-floor cornice: architrave, frieze, cove, corona with drip, cymatium.
    z = RUST_TOP
    b.sweep([(0, z), (0.12, z), (0.12, z + 0.05), (0.15, z + 0.07), (0.15, z + 0.13), (0.19, z + 0.17),
             (0.27, z + 0.24), (0.42, z + 0.28), (0.44, z + 0.31), (0.44, z + 0.38), (0.48, z + 0.41),
             (0.48, z + 0.45), (0, z + 0.45)], -hx - 0.48, hx + 0.48)
    # Drip groove under the ground cornice corona (reads as a dark line).
    b.box(-hx - 0.4, hx + 0.4, -0.40, -0.36, z + 0.265, z + 0.285, bevel=0.0)
    # Sill courses under each row of upper windows (they double as floor lines).
    for z in (6.9, 10.5, 14.1):
        zc = z - 0.26
        prof = [(0, zc - 0.06), (0.05, zc - 0.06), (0.05, zc), (0.12, zc + 0.03), (0.15, zc + 0.08),
                (0.15, zc + 0.2), (0.12, zc + 0.24), (0.0, zc + 0.26)]
        # Side bays run on the wall; the central bay's run sits on its projection.
        b.sweep(prof, -hx - 0.15, -BAY_HALF, 0.0)
        b.sweep(prof, BAY_HALF, hx + 0.15, 0.0)
        b.sweep(prof, -BAY_HALF - 0.02, BAY_HALF + 0.02, -BAY_P)
    # Eave cornice: architrave, frieze, bed mould, corona with soffit, cymatium.
    z = EAVE - 0.95
    b.sweep([(0, z), (0.06, z), (0.06, z + 0.04), (0.09, z + 0.08), (0.09, z + 0.14), (0.04, z + 0.16),
             (0.04, z + 0.44), (0.10, z + 0.47), (0.14, z + 0.52), (0.20, z + 0.55), (0.22, z + 0.6),
             (0.74, z + 0.6), (0.74, z + 0.62), (0.76, z + 0.7), (0.76, z + 0.78), (0.82, z + 0.86),
             (0.86, z + 0.95), (0, z + 0.95)], -hx - 0.86, hx + 0.86)
    # Dentils in the bed mould and modillions under the corona soffit.
    x = -hx + 0.06
    while x < hx - 0.06:
        b.box(x, x + 0.07, -0.2, -0.12, z + 0.47, z + 0.55, bevel=0.004)
        x += 0.13
    x = -hx + 0.25
    while x < hx - 0.2:
        console(b, x, z + 0.6, 0.16, 0.6, 0.22)
        x += 0.62
    return b


def console(b, x, z_top, w, depth, h):
    """Scrolled bracket (modillion/console): a stepped S profile extruded across x."""
    prof = [(0.0, z_top), (depth, z_top), (depth, z_top - h * 0.35), (depth * 0.82, z_top - h * 0.45),
            (depth * 0.55, z_top - h * 0.5), (depth * 0.4, z_top - h * 0.7), (depth * 0.2, z_top - h * 0.95),
            (0.0, z_top - h)]
    verts_l = [b.bm.verts.new((x - w / 2, -p, z)) for p, z in prof]
    verts_r = [b.bm.verts.new((x + w / 2, -p, z)) for p, z in prof]
    n = len(prof)
    for i in range(n):
        j = (i + 1) % n
        b.bm.faces.new((verts_l[i], verts_l[j], verts_r[j], verts_r[i]))
    b.bm.faces.new(verts_l[::-1])
    b.bm.faces.new(verts_r)
    vs = verts_l + verts_r
    bmesh.ops.recalc_face_normals(b.bm, faces=list({f for v in vs for f in v.link_faces}))
    b._finish(vs, 0, 0.006)


def quoins(B):
    """Quieter quoins: upper storeys only, varied block lengths, small projection."""
    W, EAVE = B["facade_width"], B["eave_height"]
    hx = W / 2
    rng = random.Random(SEED)
    b = Builder()
    for sx in (-1, 1):
        z, i = RUST_TOP + 0.45, 0
        while z < EAVE - 1.0:
            h = min(rng.uniform(0.34, 0.46), EAVE - 1.0 - z)
            long_ = (i % 2 == 0)
            fw = (0.66 if long_ else 0.42) + rng.uniform(-0.05, 0.05)
            sw = (0.42 if long_ else 0.66) + rng.uniform(-0.05, 0.05)
            p = 0.045 + rng.uniform(-0.01, 0.012)
            if abs(z - 6.64) < 0.3 or abs(z - 10.24) < 0.3 or abs(z - 13.84) < 0.3:
                z += 0.3               # let the sill courses run through cleanly
                continue
            x0, x1 = sorted((sx * hx, sx * (hx - fw)))
            b.box(x0, x1, -p, 0.0, z + 0.012, z + h - 0.012, bevel=0.014)
            y_side = (sx * hx, sx * (hx + p))
            b.box(min(y_side), max(y_side), 0.0, sw, z + 0.012, z + h - 0.012, bevel=0.014)
            z += h
            i += 1
    return b


# --------------------------------------------------------------------------- entrance

def entrance(B):
    """Stepped arch orders of voussoirs, rusticated jambs, keystone. Returns (archivolt, plinths)."""
    av = Builder()
    for k, (ring, proud) in enumerate(ORDERS):
        inner = 0.0 if k == 0 else ORDERS[k - 1][0]
        y_front = -RUST_P - proud
        n_vous = 15 + 2 * k
        for i in range(n_vous):
            t0 = math.pi * i / n_vous
            t1 = math.pi * (i + 1) / n_vous
            if i == n_vous // 2:
                continue                       # the keystone takes the crown
            gap = 0.006
            a0 = arch_point(ARCH_HALF, ARCH_SPRING, ARCH_RISE, t0 + gap, inner)
            a1 = arch_point(ARCH_HALF, ARCH_SPRING, ARCH_RISE, t1 - gap, inner)
            b1 = arch_point(ARCH_HALF, ARCH_SPRING, ARCH_RISE, t1 - gap, ring)
            b0 = arch_point(ARCH_HALF, ARCH_SPRING, ARCH_RISE, t0 + gap, ring)
            av.prism([tuple(a0), tuple(b0), tuple(b1), tuple(a1)], y_front, 0.02 + k * 0.0,
                     bevel=0.01)
        # Jambs below the springing: stacked blocks, alternately long and short.
        z, j = PLINTH_TOP, 0
        while z < ARCH_SPRING - 0.05:
            h = min(0.48, ARCH_SPRING - z)
            extra = 0.12 if (j % 2 == 0 and k == len(ORDERS) - 1) else 0.0
            for sx in (-1, 1):
                xa, xb = sorted((sx * (ARCH_HALF + inner), sx * (ARCH_HALF + ring + extra)))
                av.box(xa, xb, y_front, 0.02, z + 0.006, z + h - 0.006, bevel=0.01)
            z += h
            j += 1
    # Impost blocks at the springing, slightly proud of the outer order.
    for sx in (-1, 1):
        xa, xb = sorted((sx * (ARCH_HALF - 0.04), sx * (ARCH_HALF + ORDERS[-1][0] + 0.08)))
        av.box(xa, xb, -RUST_P - ORDERS[-1][1] - 0.06, 0.02, ARCH_SPRING - 0.14, ARCH_SPRING + 0.02,
               bevel=0.012)
    # Keystone: tapered, deeply projecting, breaking up into the ground cornice.
    crown = ARCH_SPRING + ARCH_RISE
    kw, kh, kp = KEYSTONE
    av.prism([(-kw * 0.32, crown - 0.05), (kw * 0.32, crown - 0.05), (kw / 2, crown + kh),
              (-kw / 2, crown + kh)], -RUST_P - kp, 0.02, bevel=0.015)
    pl = Builder()
    # Pedestal bases under the jambs: the "proper sill/base transitions".
    for sx in (-1, 1):
        xa, xb = sorted((sx * (ARCH_HALF - 0.02), sx * (ARCH_HALF + ORDERS[-1][0] + 0.2)))
        pl.box(xa, xb, -RUST_P - ORDERS[-1][1] - 0.1, 0.02, 0.0, PLINTH_TOP + 0.08, bevel=0.015)
        pl.box(xa, xb, -RUST_P - ORDERS[-1][1] - 0.13, 0.0, PLINTH_TOP + 0.02,
               PLINTH_TOP + 0.12, bevel=0.01)
    # Threshold step.
    pl.box(-ARCH_HALF, ARCH_HALF, -0.42, ARCH_DEPTH, 0.0, 0.14, bevel=0.012)
    return av, pl


# --------------------------------------------------------------------------- windows

def window(b_stone, b_frame, x, sill, style):
    """Surround + reveal lining + sill for one upper window; casement into b_frame."""
    hw, top = WIN_W / 2, sill + WIN_H
    face = -BAY_P if abs(x) < BAY_HALF else 0.0
    repaired = (x, sill) == REPAIRED
    # Sill: projecting slab with a drip; the repaired one is a plain thin replacement.
    if repaired:
        b_stone.box(x - hw - 0.12, x + hw + 0.12, face - 0.12, face + 0.06, sill - 0.08, sill, bevel=0.004)
    else:
        b_stone.box(x - hw - 0.2, x + hw + 0.2, face - 0.17, face + 0.06, sill - 0.12, sill, bevel=0.012)
        b_stone.box(x - hw - 0.16, x + hw + 0.16, face - 0.14, face - 0.06, sill - 0.16, sill - 0.12,
                    bevel=0.006)
    # Architrave: two-step band round the opening, real projection.
    band, p1, p2 = 0.17, 0.06, 0.1
    frame(b_stone, x, sill, top, hw, band, face - p1, face + 0.02, 0.01)
    frame(b_stone, x, sill, top, hw, 0.05, face - p2, face - p1 + 0.005, 0.008)
    if style == "piano":
        # Eared architrave + frieze + segmental pediment on scrolled consoles.
        for sx in (-1, 1):
            xe = x + sx * (hw + band)
            b_stone.box(min(xe, xe + sx * 0.1), max(xe, xe + sx * 0.1), face - p1, face + 0.02,
                        top + band - 0.22, top + band, bevel=0.008)
            console_v(b_stone, x + sx * (hw + band + 0.02), top + band + 0.02, face)
        fz = top + band
        b_stone.box(x - hw - band - 0.05, x + hw + band + 0.05, face - 0.07, face + 0.02,
                    fz, fz + 0.2, bevel=0.008)
        pediment(b_stone, x, fz + 0.2, hw + band + 0.18, 0.28, face)
    elif style == "middle":
        hood_z = top + band
        if repaired:
            # Replacement concrete lintel: flat, no keystone, a different depth.
            b_stone.box(x - hw - band, x + hw + band, face - 0.05, face + 0.02, hood_z, hood_z + 0.16,
                        bevel=0.003)
        else:
            b_stone.box(x - hw - band - 0.06, x + hw + band + 0.06, face - 0.08, face + 0.02,
                        hood_z, hood_z + 0.14, bevel=0.008)
            b_stone.box(x - hw - band - 0.12, x + hw + band + 0.12, face - 0.2, face + 0.02,
                        hood_z + 0.14, hood_z + 0.24, bevel=0.01)
            b_stone.prism([(x - 0.12, top - 0.02), (x + 0.12, top - 0.02), (x + 0.16, hood_z + 0.14),
                           (x - 0.16, hood_z + 0.14)], face - 0.16, face + 0.02, bevel=0.01)
    else:
        # Upper storey: plain lintel band, as if simplified in a later renovation.
        b_stone.box(x - hw - band, x + hw + band, face - 0.075, face + 0.02, top + band - 0.02,
                    top + band + 0.1, bevel=0.006)
    # Reveal linings (opening sides, head, sill top) so the cut reads as dressed stone.
    y0, y1 = face, CASEMENT_SET
    b_stone.box(x - hw - 0.02, x - hw, y0, y1, sill, top, bevel=0.0)
    b_stone.box(x + hw, x + hw + 0.02, y0, y1, sill, top, bevel=0.0)
    b_stone.box(x - hw, x + hw, y0, y1, top, top + 0.02, bevel=0.0)
    casement(b_frame, x, sill, top, hw, OPEN_WINDOWS.get((x, sill), (0.0, 0.0)))


def frame(b, x, sill, top, hw, band, y0, y1, bevel):
    """Architrave band round an opening: two jambs and a head (the sill closes the bottom)."""
    b.box(x - hw - band, x - hw, y0, y1, sill, top + band, bevel=bevel)
    b.box(x + hw, x + hw + band, y0, y1, sill, top + band, bevel=bevel)
    b.box(x - hw, x + hw, y0, y1, top, top + band, bevel=bevel)


def console_v(b, x, z_top, face):
    """Small vertical scroll console under a pediment end."""
    w, d, h = 0.12, 0.2, 0.42
    prof = [(0.0, z_top), (d, z_top), (d, z_top - 0.08), (d * 0.6, z_top - 0.16), (d * 0.5, z_top - 0.3),
            (d * 0.3, z_top - h), (0.0, z_top - h)]
    vl = [b.bm.verts.new((x - w / 2, face - p, z)) for p, z in prof]
    vr = [b.bm.verts.new((x + w / 2, face - p, z)) for p, z in prof]
    n = len(prof)
    for i in range(n):
        j = (i + 1) % n
        b.bm.faces.new((vl[i], vl[j], vr[j], vr[i]))
    b.bm.faces.new(vl[::-1])
    b.bm.faces.new(vr)
    vs = vl + vr
    bmesh.ops.recalc_face_normals(b.bm, faces=list({f for v in vs for f in v.link_faces}))
    b._finish(vs, 0, 0.006)


def pediment(b, x, z, half, rise, face):
    """Segmental pediment: curved cornice over a flat tympanum, both with thickness."""
    n = 18
    arc_out = [(x + half * math.cos(math.pi * i / n), z + rise * math.sin(math.pi * i / n))
               for i in range(n + 1)]
    arc_in = [(x + (half - 0.12) * math.cos(math.pi * i / n),
               z + (rise - 0.1) * math.sin(math.pi * i / n)) for i in range(n, -1, -1)]
    b.prism(arc_out + arc_in, face - 0.2, face + 0.02, bevel=0.01)          # raking cornice
    b.prism([p for p in arc_in[::-1]], face - 0.06, face + 0.02, bevel=0.006)  # tympanum
    b.box(x - half, x + half, face - 0.2, face + 0.02, z - 0.06, z + 0.02, bevel=0.008)  # base


def casement(b, x, sill, top, hw, open_deg=(0.0, 0.0)):
    """Timber double casement set back in the reveal: fixed frame and transom light, two
    hinged leaves (opening inward, as Central European casements do), glass, sheer curtain."""
    y = CASEMENT_SET
    fr = 0.075
    WOOD, GLASS, CURTAIN = 0, 1, 2
    # Fixed frame and transom.
    b.box(x - hw, x + hw, y, y + 0.08, sill, sill + fr, mat=WOOD, bevel=0.004)
    b.box(x - hw, x + hw, y, y + 0.08, top - fr, top, mat=WOOD, bevel=0.004)
    b.box(x - hw, x - hw + fr, y, y + 0.08, sill, top, mat=WOOD, bevel=0.004)
    b.box(x + hw - fr, x + hw, y, y + 0.08, sill, top, mat=WOOD, bevel=0.004)
    tz = sill + (top - sill) * 0.72
    b.box(x - hw, x + hw, y - 0.01, y + 0.08, tz - 0.035, tz + 0.035, mat=WOOD, bevel=0.004)
    b.box(x - hw + fr, x + hw - fr, y + 0.035, y + 0.045, tz + 0.035, top - fr, mat=GLASS, bevel=0.0)
    # Two leaves below the transom, each hinged on its outer jamb.
    lw = hw - fr                       # leaf width
    z0, z1 = sill + fr, tz - 0.035
    for side, ang in ((-1, open_deg[0]), (1, open_deg[1])):
        before = set(b.bm.verts)
        hinge_x = x + side * lw
        xa, xb = sorted((hinge_x, x))
        st = 0.055
        b.box(xa, xb, y + 0.005, y + 0.065, z0, z0 + st, mat=WOOD, bevel=0.003)
        b.box(xa, xb, y + 0.005, y + 0.065, z1 - st, z1, mat=WOOD, bevel=0.003)
        b.box(xa, xa + st, y + 0.005, y + 0.065, z0, z1, mat=WOOD, bevel=0.003)
        b.box(xb - st, xb, y + 0.005, y + 0.065, z0, z1, mat=WOOD, bevel=0.003)
        for zb in (z0 + (z1 - z0) / 3, z0 + 2 * (z1 - z0) / 3):
            b.box(xa, xb, y + 0.015, y + 0.055, zb - 0.012, zb + 0.012, mat=WOOD, bevel=0.0)
        b.box(xa + st, xb - st, y + 0.03, y + 0.04, z0 + st, z1 - st, mat=GLASS, bevel=0.0)
        if ang:
            leaf = [v for v in b.bm.verts if v not in before]
            # Inward (+Y): the left leaf turns counter-clockwise, the right one clockwise.
            rot = Matrix.Rotation(math.radians(ang) * -side, 3, "Z")
            bmesh.ops.rotate(b.bm, verts=leaf, cent=(hinge_x, y + 0.035, 0), matrix=rot)
    # Sheer curtain behind the glass in soft vertical folds; drawn aside when open.
    is_open = any(open_deg)
    zt, zb2 = tz - 0.06, sill + fr + 0.05
    cy = y + (0.42 if is_open else 0.14)
    spans = ([(x - hw + fr, x - hw + fr + 0.22), (x + hw - fr - 0.22, x + hw - fr)] if is_open
             else [(x - hw + fr, x + hw - fr)])
    for xs0, xs1 in spans:
        folds = max(4, int((xs1 - xs0) / 0.06))
        pts = [(xs0 + (xs1 - xs0) * i / (folds * 2), cy + (0.03 if i % 2 else 0.0))
               for i in range(folds * 2 + 1)]
        vb = [b.bm.verts.new((px, py, zb2)) for px, py in pts]
        vt = [b.bm.verts.new((px, py, zt)) for px, py in pts]
        for i in range(len(pts) - 1):
            f = b.bm.faces.new((vb[i], vb[i + 1], vt[i + 1], vt[i]))
            f.material_index = CURTAIN
    # The room behind: dark, deeper when the window is open so the gap reads as space.
    back = WALL_T + (1.2 if is_open else 0.0)
    b.box(x - hw - 0.2, x + hw + 0.2, back - 0.02, back, sill - 0.2, top + 0.2, mat=3, bevel=0.0)
    if is_open:
        # Pale sheer hanging just inside the opening, where daylight reaches it: the cat
        # reads as a silhouette against it, as in the reference.
        folds = 18
        x0c, x1c = x - hw - 0.15, x + hw + 0.15
        pts = [(x0c + (x1c - x0c) * i / (folds * 2), WALL_T + 0.07 + (0.035 if i % 2 else 0.0))
               for i in range(folds * 2 + 1)]
        vb = [b.bm.verts.new((px, py, sill - 0.1)) for px, py in pts]
        vt = [b.bm.verts.new((px, py, top + 0.1)) for px, py in pts]
        for i in range(len(pts) - 1):
            f = b.bm.faces.new((vb[i], vb[i + 1], vt[i + 1], vt[i]))
            f.material_index = CURTAIN
        for sx in (-1, 1):
            xs = sorted((x + sx * (hw + 0.2), x + sx * (hw + 0.22)))
            b.box(xs[0], xs[1], WALL_T, back, sill - 0.2, top + 0.2, mat=3, bevel=0.0)


# --------------------------------------------------------------------------- roof / void

def roof(B):
    W, D, EAVE, RIDGE = B["facade_width"], B["depth"], B["eave_height"], B["ridge_height"]
    hx, ov = W / 2 + 0.5, 0.95
    b = Builder()
    rise = RIDGE - EAVE
    for y0, y1 in ((-ov, D / 2), (D + ov, D / 2)):
        drop = rise * ov / (D / 2)
        z0 = EAVE - drop + 0.12
        a = [(-hx, y0, z0), (hx, y0, z0), (hx, y1, RIDGE + 0.12), (-hx, y1, RIDGE + 0.12)]
        va = [b.bm.verts.new(p) for p in a]
        vb = [b.bm.verts.new((p[0], p[1], p[2] + 0.2)) for p in a]
        b.bm.faces.new(va[::-1])
        b.bm.faces.new(vb)
        for i in range(4):
            j = (i + 1) % 4
            b.bm.faces.new((va[i], va[j], vb[j], vb[i]))
    bmesh.ops.recalc_face_normals(b.bm, faces=b.bm.faces)
    return b


def void(B):
    b = Builder()
    b.prism(arch_outline(ARCH_HALF, ARCH_SPRING, ARCH_RISE, bottom=0.0), ARCH_DEPTH, ARCH_DEPTH + 0.02,
            bevel=0.0)
    return b


# --------------------------------------------------------------------------- gentleman

GENTLEMAN_PARTS = ("aa_arch_hero_gentleman", "aa_arch_hero_gentleman_hardware", "aa_arch_hero_neon_loop")
GENTLEMAN_BASE = ARCH_SPRING + ARCH_RISE - 0.08    # chin scrolls overlap the keystone head


def seat_gentleman():
    """The mascaron is the keystone's face: lift him (with his retrofit) onto it. Idempotent."""
    bust = bpy.data.objects["aa_arch_hero_gentleman"]
    dz = GENTLEMAN_BASE - min(v.co.z for v in bust.data.vertices)
    if abs(dz) < 1e-3:
        return 0.0
    for name in GENTLEMAN_PARTS:
        me = bpy.data.objects[name].data
        me.transform(Matrix.Translation((0, 0, dz)))
        me.update()
    return round(dz, 3)


# --------------------------------------------------------------------------- main

def shell_coll():
    return bpy.data.collections["aa_shell_facade"]


def replace_mesh(obj_name, builder, mats):
    obj = bpy.data.objects.get(obj_name)
    coll = obj.users_collection[0] if obj else shell_coll()
    if obj:
        old = obj.data
        new = builder.to_object(obj_name + "__tmp", mats, coll)
        obj.data = new.data
        bpy.data.objects.remove(new, do_unlink=True)
        if old.users == 0:
            bpy.data.meshes.remove(old)
        obj.data.name = obj_name
        return obj
    return builder.to_object(obj_name, mats, coll)


def main():
    B = aa.load_manifest()["building"]
    coll = shell_coll()
    keep = {"aa_shell_facade_walls"}
    for o in list(coll.objects):
        if o.name not in keep:
            bpy.data.objects.remove(o, do_unlink=True)
    stone = bpy.data.materials.get("m_aa_limestone_weathered")
    trim = bpy.data.materials.get("m_aa_trim_weathered")
    wood = material("m_aa_window_timber", (0.10, 0.055, 0.03), rough=0.55)
    glass = material("m_aa_window_glass", (0.02, 0.025, 0.03), rough=0.05, metallic=0.0, alpha=0.35)
    curtain = material("m_aa_window_curtain", (0.82, 0.8, 0.74), rough=0.9, alpha=0.8)
    dark = material("m_aa_interior_void", (0.01, 0.012, 0.012), rough=1.0)
    roof_m = material("m_aa_roof_tile", (0.16, 0.11, 0.10), rough=0.75)

    cutters = [cutter("aa_cut_entrance", arch_outline(ARCH_HALF, ARCH_SPRING, ARCH_RISE, bottom=-0.1),
                      -1.0, ARCH_DEPTH)]
    for i, (x, z, _) in enumerate(UPPER_WINDOWS):
        cutters.append(cutter(f"aa_cut_win_{i}", [(x - WIN_W / 2, z), (x + WIN_W / 2, z),
                                                  (x + WIN_W / 2, z + WIN_H), (x - WIN_W / 2, z + WIN_H)],
                              -1.0, WALL_T + 0.1))
    cutters.append(rustication_cutter(B))
    if "aa_shell_facade_walls" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["aa_shell_facade_walls"], do_unlink=True)
    walls = facade_wall(B, cutters)

    made = {"walls": len(walls.data.polygons)}
    stone_b = Builder()
    frame_b = Builder()
    for x, z, s in UPPER_WINDOWS:
        window(stone_b, frame_b, x, z, s)
    for name, builder, mats in (
            ("aa_shell_facade_mouldings", mouldings(B), [trim]),
            ("aa_shell_facade_quoins", quoins(B), [trim]),
            ("aa_shell_facade_window_surrounds", stone_b, [trim]),
            ("aa_shell_facade_casements", frame_b, [wood, glass, curtain, dark]),
            ("aa_shell_facade_roof", roof(B), [roof_m]),
            ("aa_shell_facade_interior_void", void(B), [dark])):
        o = builder.to_object(name, mats, coll)
        made[name] = len(o.data.polygons)
    av, pl = entrance(B)
    replace_mesh("aa_arch_hero_archivolt", av, [trim])
    replace_mesh("aa_arch_hero_plinths", pl, [trim])
    made["gentleman_lift"] = seat_gentleman()
    return made


if __name__ == "__main__" or "AA_RUN" in globals():
    result = main()
    print(result)
