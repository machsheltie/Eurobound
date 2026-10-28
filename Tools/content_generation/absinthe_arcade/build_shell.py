"""Build aa_shell_facade as real masonry (architectural quality pass, 2026-10-27).

The facade is no longer one plane with things stuck on it. Depth planes, from
the street inward:

  plinth (proud 0.26)  ->  ground-floor banded rustication (0.10)  ->  wall (0)
  central entrance bay (risalit, proud 0.16 above the ground cornice) with
  edge lesenes (0.24)

Windows are openings cut through 0.55 m of masonry with reveals, sash windows set
back in them, and surrounds that differ by storey (heavy ground floor, richest
first floor, plainer above, one later repair). The entrance is a deep arch with
three stepped orders of individual voussoirs, rusticated jambs and a projecting
keystone that carries the Headphone Gentleman, who sits in a carved ring (dark
groove between two mouldings) that the ground cornice breaks around; the marquee
is sized to the arch and hung proud of it (its steel is in build_fittings.py). String courses are dimensional
sill courses with drips; the eave cornice has frieze, dentils, modillions and
a corona with a shadowed soffit. Quoins are quieter, varied, upper floors only.
History, kept restrained: one recast span of ground cornice, one replaced
rustication block, one replaced lintel and sill, and the sill courses chased out
where the downpipes pass.

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
# Ring behind the gentleman's head (entrance reference, gentleman panel): a dark groove
# cut into the bay between two stone mouldings, which his conduit loop rides over. The
# ground cornice breaks around it, so he reads as carved with the building.
RING_C = (0.0, 6.24)             # centre: the conduit loop over his crown
RING_GROOVE = (0.62, 0.86)       # dark groove radii
RING_OUTER = 1.04                # outer edge of the moulded frame; the cornice stops here
RING_FOOT = RUST_TOP + 0.07      # the legs come down to the cornice line
# The marquee is a lightbox hung in front of the arch on steel standoffs (build_fittings):
# its back sits just proud of the impost blocks, as in the entrance reference.
MARQUEE_PARTS = ("aa_arch_hero_marquee", "aa_arch_hero_tagline_panel")
MARQUEE_BACK = -RUST_P - ORDERS[-1][1] - 0.08
# Overall width: wider than the opening, about 93% of the outer order, so its ends sit
# across the arch moulding and impost blocks as in the reference.
MARQUEE_W = 5.15

# Windows: (x, sill z, storey style)
UPPER_WINDOWS = [(x, z, s) for z, s in ((6.9, "piano"), (10.5, "middle"), (14.1, "upper"))
                 for x in (-4.6, 4.6)]
REPAIRED = (4.6, 10.5)           # later replacement lintel and sill
REPAIRED_CORNICE = (4.85, 5.6)   # span of ground cornice recast in a plainer profile
STONE_PATCH = (5.05, 5.6, 2.18, 2.62)    # replaced rustication block (x0, x1, z0, z1)
# Author ruling 2026-10-27: the black cat sits outside the left first-floor window, which
# is open: its lower sash is pushed up (metres raised) so the curtain shows through.
OPEN_WINDOWS = {(-4.6, 6.9): 0.55}
WIN_W = 1.16
# Opening height by storey: the top floor's windows are shorter, as on real buildings of
# this type, which also keeps their heads clear of the eave cornice.
WIN_H = {"piano": 1.85, "middle": 1.85, "upper": 1.48}
# Arched ground-floor window (reference: the author's ground-floor crop): round head,
# moulded surround, keystone tucked under the ground cornice, sill slab on corbels,
# tracery fanlight, iron balconette with pots.
GW_X, GW_HALF, GW_SILL, GW_SPRING = -4.4, 0.55, 3.66, 4.76     # crown = spring + half
# Top-floor balconies: (x, window sill z, variant). Variant 1 is the older-looking one
# with a bent baluster and a mismatched replacement finial.
BALCONIES = [(-4.6, 14.1, 0), (4.6, 14.1, 1)]
BAL_DEPTH, BAL_HALF, BAL_SLAB, BAL_RAIL_H = 0.56, 0.98, 0.15, 0.86
SASH_SET = 0.24              # how far the frame sits back from the wall face
# Downpipes (built in build_fittings.py). Not symmetrical, as in the reference: the left one
# drops between the corner and the windows, the right one hugs the corner. The sill courses
# were chased out where they pass, so the pipe stands in a notch in each course.
DRAIN_X = (-5.9, 6.75)
DRAIN_CHASE = 0.1           # half-width of the notch cut in each course


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
        # Slots first: clearing slots after writing geometry resets every face to slot 0.
        me.materials.clear()
        for m in mats:
            me.materials.append(m)
        self.bm.to_mesh(me)
        self.bm.free()
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
    prof_gc = [(0, z), (0.12, z), (0.12, z + 0.05), (0.15, z + 0.07), (0.15, z + 0.13), (0.19, z + 0.17),
             (0.27, z + 0.24), (0.42, z + 0.28), (0.44, z + 0.31), (0.44, z + 0.38), (0.48, z + 0.41),
             (0.48, z + 0.45), (0, z + 0.45)]
    # Later cement repair: a plain chamfer instead of the cove and corona, no drip.
    prof_rep = [(0, z), (0.13, z), (0.13, z + 0.12), (0.43, z + 0.29), (0.46, z + 0.31), (0.46, z + 0.42),
                (0.44, z + 0.45), (0, z + 0.45)]
    r0, r1 = REPAIRED_CORNICE
    # Broken around the gentleman's ring; the capped ends read as the cornice returning.
    for x0, x1 in ((-hx - 0.48, -RING_OUTER), (RING_OUTER, r0), (r1, hx + 0.48)):
        b.sweep(prof_gc, x0, x1)
        # Drip groove under the corona (reads as a dark line).
        b.box(max(x0, -hx - 0.4), min(x1, hx + 0.4), -0.40, -0.36, z + 0.265, z + 0.285, bevel=0.0)
    b.sweep(prof_rep, r0, r1)
    # One replaced rustication block, new stone set a few millimetres proud of the old.
    px0, px1, pz0, pz1 = STONE_PATCH
    b.box(px0, px1, -RUST_P - 0.008, -RUST_P + 0.02, pz0, pz1, bevel=0.004)
    # Sill courses under each row of upper windows (they double as floor lines).
    for z in (6.9, 10.5, 14.1):
        zc = z - 0.26
        prof = [(0, zc - 0.06), (0.05, zc - 0.06), (0.05, zc), (0.12, zc + 0.03), (0.15, zc + 0.08),
                (0.15, zc + 0.2), (0.12, zc + 0.24), (0.0, zc + 0.26)]
        # Side bays run on the wall; the central bay's run sits on its projection.
        for x0, x1 in chased(-hx - 0.15, -BAY_HALF) + chased(BAY_HALF, hx + 0.15):
            b.sweep(prof, x0, x1, 0.0)
        if z == 6.9:        # stops either side of the gentleman's ring
            b.sweep(prof, -BAY_HALF - 0.02, -RING_OUTER, -BAY_P)
            b.sweep(prof, RING_OUTER, BAY_HALF + 0.02, -BAY_P)
        else:
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


def chased(x0, x1):
    """Split a course's span at the downpipe notches."""
    spans = [(x0, x1)]
    for dx in DRAIN_X:
        nxt = []
        for a, b in spans:
            if a < dx - DRAIN_CHASE and dx + DRAIN_CHASE < b:
                nxt += [(a, dx - DRAIN_CHASE), (dx + DRAIN_CHASE, b)]
            else:
                nxt.append((a, b))
        spans = nxt
    return spans


def soften(obj, width, angle=30.0):
    """Arris bevel on hard edges (applied on export) so raw cuts and sweeps catch light."""
    mod = obj.modifiers.get("aa_soften") or obj.modifiers.new("aa_soften", "BEVEL")
    mod.width = width
    mod.segments = 2
    mod.profile = 0.6
    mod.limit_method = "ANGLE"
    mod.angle_limit = math.radians(angle)
    mod.use_clamp_overlap = True
    mod.harden_normals = False
    return mod


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
    """Surround + reveal lining + sill for one upper window; sash window into b_frame."""
    hw, top = WIN_W / 2, sill + WIN_H[style]
    face = -BAY_P if abs(x) < BAY_HALF else 0.0
    repaired = (x, sill) == REPAIRED
    on_balcony = any((bx, bz) == (x, sill) for bx, bz, _ in BALCONIES)
    # Sill: projecting slab with a drip; the repaired one is a plain thin replacement, and
    # balcony windows step straight out onto the balcony slab instead.
    if on_balcony:
        pass
    elif repaired:
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
    y0, y1 = face, SASH_SET
    # Linings sit just inside the opening so they, not the boolean-cut faces, are what shows.
    b_stone.box(x - hw, x - hw + 0.02, y0, y1, sill, top, bevel=0.0)
    b_stone.box(x + hw - 0.02, x + hw, y0, y1, sill, top, bevel=0.0)
    b_stone.box(x - hw, x + hw, y0, y1, top - 0.02, top, bevel=0.0)
    sash_window(b_frame, x, sill, top, hw, OPEN_WINDOWS.get((x, sill), 0.0))


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


def sheer(b, xs0, xs1, cy, z0, z1, mat, pitch=0.06, depth=0.03):
    """Sheer curtain: a single sheet gathered into soft vertical folds."""
    folds = max(4, int((xs1 - xs0) / pitch))
    pts = [(xs0 + (xs1 - xs0) * i / (folds * 2), cy + (depth if i % 2 else 0.0))
           for i in range(folds * 2 + 1)]
    vb = [b.bm.verts.new((px, py, z0)) for px, py in pts]
    vt = [b.bm.verts.new((px, py, z1)) for px, py in pts]
    for i in range(len(pts) - 1):
        f = b.bm.faces.new((vb[i], vb[i + 1], vt[i + 1], vt[i]))
        f.material_index = mat


def sash_window(b, x, sill, top, hw, raised=0.0):
    """Timber window set back in the reveal: fixed frame with a glazed upper light (two panes
    either side of a mullion) and a lower sash that slides up in an inner track, as in the
    reference. `raised` lifts the lower sash behind the upper light, opening the bottom.
    Nothing is hinged: the lower sash only ever slides up (author ruling 2026-10-27)."""
    y = SASH_SET
    fr = 0.075
    WOOD, GLASS, CURTAIN = 0, 1, 2
    # Fixed frame and meeting rail.
    b.box(x - hw, x + hw, y, y + 0.08, sill, sill + fr, mat=WOOD, bevel=0.004)
    b.box(x - hw, x + hw, y, y + 0.08, top - fr, top, mat=WOOD, bevel=0.004)
    b.box(x - hw, x - hw + fr, y, y + 0.15, sill, top, mat=WOOD, bevel=0.004)
    b.box(x + hw - fr, x + hw, y, y + 0.15, sill, top, mat=WOOD, bevel=0.004)
    tz = sill + (top - sill) * 0.62
    b.box(x - hw, x + hw, y - 0.01, y + 0.06, tz - 0.035, tz + 0.035, mat=WOOD, bevel=0.004)
    # Fixed upper light: two glazed panes either side of a centre mullion.
    b.box(x - 0.028, x + 0.028, y, y + 0.06, tz + 0.035, top - fr, mat=WOOD, bevel=0.003)
    b.box(x - hw + fr, x + hw - fr, y + 0.025, y + 0.035, tz + 0.035, top - fr, mat=GLASS, bevel=0.0)
    # Lower sash in the inner track (behind the upper light, so it can slide up past it).
    sx0, sx1 = x - hw + fr, x + hw - fr
    z0, z1 = sill + fr + raised, tz + 0.035 + raised
    st = 0.055
    yt0, yt1 = y + 0.075, y + 0.13
    b.box(sx0, sx1, yt0, yt1, z0, z0 + st, mat=WOOD, bevel=0.003)
    b.box(sx0, sx1, yt0, yt1, z1 - st, z1, mat=WOOD, bevel=0.003)
    b.box(sx0, sx0 + st, yt0, yt1, z0, z1, mat=WOOD, bevel=0.003)
    b.box(sx1 - st, sx1, yt0, yt1, z0, z1, mat=WOOD, bevel=0.003)
    b.box(x - 0.018, x + 0.018, yt0 + 0.01, yt1 - 0.01, z0, z1, mat=WOOD, bevel=0.0)
    b.box(sx0 + st, sx1 - st, yt0 + 0.025, yt0 + 0.035, z0 + st, z1 - st, mat=GLASS, bevel=0.0)
    # Sheer hanging close behind the whole window; through the raised opening it is the
    # bright backdrop the cat sits against.
    sheer(b, sx0, sx1, y + 0.2, sill + fr + 0.02, top - fr, CURTAIN)
    b.box(x - hw - 0.2, x + hw + 0.2, WALL_T - 0.02, WALL_T, sill - 0.2, top + 0.2, mat=3, bevel=0.0)


def ring(b, cx, cz, r0, r1, y0, y1, mat=0, n=24, bevel=0.006, gap=0.0):
    """Semicircular band between radii r0 and r1 (an arch moulding), built from n solids."""
    for i in range(n):
        t0 = math.pi * i / n + gap
        t1 = math.pi * (i + 1) / n - gap
        pts = [(cx + r0 * math.cos(t0), cz + r0 * math.sin(t0)),
               (cx + r1 * math.cos(t0), cz + r1 * math.sin(t0)),
               (cx + r1 * math.cos(t1), cz + r1 * math.sin(t1)),
               (cx + r0 * math.cos(t1), cz + r0 * math.sin(t1))]
        b.prism(pts, y0, y1, mat=mat, bevel=bevel)


def corbel(b, x, top, face, w=0.14, depth=0.3, h=0.33):
    """Scrolled corbel under a slab: an S profile extruded across x."""
    prof = [(0.0, top), (depth, top), (depth, top - 0.07), (depth * 0.66, top - 0.13),
            (depth * 0.46, top - 0.23), (depth * 0.26, top - 0.31), (0.0, top - h)]
    vl = [b.bm.verts.new((x - w / 2, face - pp, z)) for pp, z in prof]
    vr = [b.bm.verts.new((x + w / 2, face - pp, z)) for pp, z in prof]
    n = len(prof)
    for i in range(n):
        j = (i + 1) % n
        b.bm.faces.new((vl[i], vl[j], vr[j], vr[i]))
    b.bm.faces.new(vl[::-1])
    b.bm.faces.new(vr)
    vs = vl + vr
    bmesh.ops.recalc_face_normals(b.bm, faces=list({f for v in vs for f in v.link_faces}))
    b._finish(vs, 0, 0.006)


def ground_window(b_stone, b_frame, b_iron):
    """Arched ground-floor window: surround, sill and corbels into b_stone; frame, fanlight
    tracery, glass and sheer into b_frame; balconette into b_iron."""
    x, hw, sill, spring = GW_X, GW_HALF, GW_SILL, GW_SPRING
    face = -RUST_P
    crown = spring + hw
    # Moulded surround: outer band and inner fillet, jambs plus a round head.
    for band, p_out, p_in, bev in ((0.18, 0.09, -0.005, 0.01), (0.06, 0.14, 0.085, 0.006)):
        y0, y1 = face - p_out, face - p_in
        for sx in (-1, 1):
            xa, xb = sorted((x + sx * hw, x + sx * (hw + band)))
            b_stone.box(xa, xb, y0, y1, sill, spring, bevel=bev)
        ring(b_stone, x, spring, hw, hw + band, y0, y1, n=40, bevel=0.0)   # one smooth moulding
    # Impost blocks at the springing.
    for sx in (-1, 1):
        xa, xb = sorted((x + sx * (hw - 0.01), x + sx * (hw + 0.22)))
        b_stone.box(xa, xb, face - 0.12, face + 0.01, spring - 0.08, spring + 0.02, bevel=0.008)
    # Keystone, tapering up to meet the ground-floor cornice.
    b_stone.prism([(x - 0.11, crown - 0.04), (x + 0.11, crown - 0.04), (x + 0.16, RUST_TOP),
                   (x - 0.16, RUST_TOP)], face - 0.19, face + 0.01, bevel=0.01)
    # Projecting sill slab with a drip, carried on two scrolled corbels.
    b_stone.box(x - hw - 0.32, x + hw + 0.32, face - 0.36, face + 0.04, sill - 0.13, sill, bevel=0.012)
    b_stone.box(x - hw - 0.28, x + hw + 0.28, face - 0.33, face - 0.25, sill - 0.17, sill - 0.13,
                bevel=0.006)
    for sx in (-1, 1):
        corbel(b_stone, x + sx * (hw + 0.12), sill - 0.13, face)
    # Reveal linings: jambs and a soffit ring, inside the opening.
    for sx in (-1, 1):
        xa, xb = sorted((x + sx * hw, x + sx * (hw - 0.02)))
        b_stone.box(xa, xb, face, SASH_SET, sill, spring, bevel=0.0)
    ring(b_stone, x, spring, hw - 0.02, hw, face, SASH_SET, bevel=0.0)

    # Window: frame following the arch, transom at the springing, tracery fanlight.
    WOOD, GLASS, CURTAIN = 0, 1, 2
    y, fr = SASH_SET, 0.07
    for sx in (-1, 1):
        xa, xb = sorted((x + sx * (hw - 0.02), x + sx * (hw - 0.02 - fr)))
        b_frame.box(xa, xb, y, y + 0.08, sill, spring, mat=WOOD, bevel=0.004)
    b_frame.box(x - hw + 0.02, x + hw - 0.02, y, y + 0.08, sill, sill + fr, mat=WOOD, bevel=0.004)
    ring(b_frame, x, spring, hw - 0.02 - fr, hw - 0.02, y, y + 0.08, mat=WOOD, n=20, bevel=0.003)
    b_frame.box(x - hw + 0.02, x + hw - 0.02, y - 0.01, y + 0.08, spring - 0.035, spring + 0.035,
                mat=WOOD, bevel=0.004)
    # Fanlight tracery: centre bar, an inner arc and two diagonals.
    r_in = hw - 0.02 - fr
    b_frame.box(x - 0.018, x + 0.018, y + 0.01, y + 0.07, spring, spring + r_in, mat=WOOD, bevel=0.0)
    ring(b_frame, x, spring, r_in * 0.52, r_in * 0.52 + 0.03, y + 0.01, y + 0.07, mat=WOOD, n=14,
         bevel=0.0)
    for sx in (-1, 1):
        t = math.radians(90 - sx * 45)
        p0 = Vector((x + r_in * 0.53 * math.cos(t), spring + r_in * 0.53 * math.sin(t)))
        p1 = Vector((x + r_in * math.cos(t), spring + r_in * math.sin(t)))
        d = (p1 - p0).normalized() * 0.015
        nrm = Vector((-d.y, d.x))
        b_frame.prism([tuple(p0 + nrm), tuple(p1 + nrm), tuple(p1 - nrm), tuple(p0 - nrm)],
                      y + 0.01, y + 0.07, mat=WOOD, bevel=0.0)
    fan = [(x + r_in * math.cos(math.pi * i / 24),
            spring + 0.035 + (r_in - 0.035) * math.sin(math.pi * i / 24)) for i in range(25)]
    b_frame.prism(fan, y + 0.035, y + 0.045, mat=GLASS, bevel=0.0)
    # Lower lights: centre mullion, one glazing bar, glass, sheer behind.
    b_frame.box(x - 0.025, x + 0.025, y, y + 0.08, sill, spring, mat=WOOD, bevel=0.003)
    zb = sill + (spring - sill) * 0.55
    b_frame.box(x - hw + 0.02, x + hw - 0.02, y + 0.01, y + 0.07, zb - 0.014, zb + 0.014, mat=WOOD,
                bevel=0.0)
    b_frame.box(x - hw + 0.02 + fr, x + hw - 0.02 - fr, y + 0.035, y + 0.045, sill + fr,
                spring - 0.035, mat=GLASS, bevel=0.0)
    sheer(b_frame, x - hw + 0.09, x + hw - 0.09, y + 0.14, sill + fr + 0.02, spring - 0.04, CURTAIN)
    b_frame.box(x - hw - 0.2, x + hw + 0.2, WALL_T - 0.02, WALL_T, sill - 0.2, crown + 0.2, mat=3,
                bevel=0.0)

    # Balconette: wrought-iron rail on the sill slab, returned to the wall, with a cross finial.
    top_z, front = sill + 0.44, face - 0.31
    xl, xr = x - hw - 0.24, x + hw + 0.24
    rail = 0.022
    for z0 in (sill + 0.03, top_z - 0.03):
        b_iron.box(xl, xr, front - rail, front + rail, z0 - rail, z0 + rail, bevel=0.004)
        for xe in (xl, xr):
            b_iron.box(xe - rail, xe + rail, front, face, z0 - rail, z0 + rail, bevel=0.004)
    b_iron.box(xl - 0.035, xr + 0.035, front - 0.035, front + 0.03, top_z - 0.02, top_z + 0.012,
               bevel=0.006)
    xb_, i = xl, 0
    while xb_ <= xr + 1e-6:
        b_iron.box(xb_ - 0.009, xb_ + 0.009, front - 0.009, front + 0.009, sill + 0.03, top_z - 0.02,
                   bevel=0.0)
        if i % 2 == 1:      # C-scroll pair in every other bay
            ring(b_iron, xb_ + 0.065, sill + 0.21, 0.04, 0.052, front - 0.008, front + 0.008, n=10,
                 bevel=0.0)
            ring(b_iron, xb_ - 0.065, sill + 0.21, 0.04, 0.052, front - 0.008, front + 0.008, n=10,
                 bevel=0.0)
        xb_ += 0.13
        i += 1
    b_iron.box(x - 0.012, x + 0.012, front - 0.012, front + 0.012, top_z, top_z + 0.16, bevel=0.003)
    b_iron.box(x - 0.06, x + 0.06, front - 0.012, front + 0.012, top_z + 0.08, top_z + 0.105,
               bevel=0.003)
    # Anchor plates where the rail returns meet the wall.
    for xe in (xl, xr):
        b_iron.box(xe - 0.05, xe + 0.05, face - 0.008, face + 0.002, sill + 0.01, top_z + 0.01,
                   bevel=0.003)


def balcony(b_stone, b_iron, x, z_top, variant):
    """Stone balcony slab on corbels with a wrought-iron rail anchored into the wall."""
    face = -BAY_P if abs(x) < BAY_HALF else 0.0
    d, hw, t = BAL_DEPTH, BAL_HALF, BAL_SLAB
    front = face - d
    # Slab: the walking surface runs into the wall (it is the floor of the room inside).
    b_stone.box(x - hw, x + hw, front, face + 0.25, z_top - t, z_top, bevel=0.012)
    # Moulded nosing round the free edges, and a drip groove line on the soffit.
    b_stone.box(x - hw - 0.03, x + hw + 0.03, front - 0.03, front + 0.06, z_top - t - 0.04,
                z_top - t + 0.03, bevel=0.01)
    for sx in (-1, 1):
        xa, xb = sorted((x + sx * hw, x + sx * (hw + 0.03)))
        b_stone.box(xa, xb, front - 0.03, face, z_top - t - 0.04, z_top - t + 0.03, bevel=0.01)
    b_stone.box(x - hw + 0.06, x + hw - 0.06, front + 0.07, front + 0.09, z_top - t - 0.012,
                z_top - t, bevel=0.0)
    # Corbels carrying the slab (deeper than the window corbels: this one is load-bearing).
    for sx in (-1, 1):
        corbel(b_stone, x + sx * (hw - 0.2), z_top - t - 0.04, face, w=0.18, depth=d - 0.08, h=0.5)
    # Drain spout at the front corner, so the slab sheds water clear of the facade.
    sx = 1 if variant == 0 else -1
    b_stone.box(x + sx * (hw - 0.12) - 0.025, x + sx * (hw - 0.12) + 0.025, front - 0.14, front + 0.05,
                z_top - t + 0.01, z_top - t + 0.05, bevel=0.006)

    # Railing: front and two returns, top rail, bottom rail, balusters, scroll band.
    r_top = z_top + BAL_RAIL_H
    fy = front + 0.05
    xl, xr = x - hw + 0.04, x + hw - 0.04
    for z0 in (z_top + 0.06, r_top - 0.03, z_top + 0.32):
        b_iron.box(xl, xr, fy - 0.014, fy + 0.014, z0 - 0.014, z0 + 0.014, bevel=0.003)
        for xe in (xl, xr):
            b_iron.box(xe - 0.014, xe + 0.014, fy, face, z0 - 0.014, z0 + 0.014, bevel=0.003)
    b_iron.box(xl - 0.03, xr + 0.03, fy - 0.035, fy + 0.03, r_top - 0.02, r_top + 0.015, bevel=0.006)
    for xe in (xl, xr):
        b_iron.box(xe - 0.03, xe + 0.03, fy - 0.035, face, r_top - 0.02, r_top + 0.015, bevel=0.006)
    i, xb_ = 0, xl
    while xb_ <= xr + 1e-6:
        before = set(b_iron.bm.verts)
        b_iron.box(xb_ - 0.01, xb_ + 0.01, fy - 0.01, fy + 0.01, z_top + 0.06, r_top - 0.02, bevel=0.0)
        if variant == 1 and i == 5:
            # An old knock: one baluster bowed outward.
            bent = [v for v in b_iron.bm.verts if v not in before]
            for v in bent:
                k = math.sin(math.pi * (v.co.z - z_top) / BAL_RAIL_H)
                v.co.y -= 0.035 * max(0.0, k)
        if i % 2 == 1:
            ring(b_iron, xb_ + 0.06, z_top + 0.19, 0.04, 0.052, fy - 0.008, fy + 0.008, n=10, bevel=0.0)
            ring(b_iron, xb_ - 0.06, z_top + 0.19, 0.04, 0.052, fy - 0.008, fy + 0.008, n=10, bevel=0.0)
        xb_ += 0.12
        i += 1
    # Side returns get their own balusters.
    for xe in (xl, xr):
        yb = fy
        while yb < face - 0.06:
            b_iron.box(xe - 0.01, xe + 0.01, yb - 0.01, yb + 0.01, z_top + 0.06, r_top - 0.02, bevel=0.0)
            yb += 0.12
    # Corner finials: the original ball on one, a later mismatched spike on the other balcony.
    for xe in (xl, xr):
        if variant == 0:
            b_iron.box(xe - 0.03, xe + 0.03, fy - 0.03, fy + 0.03, r_top + 0.015, r_top + 0.075, bevel=0.025)
        else:
            b_iron.prism([(xe - 0.02, r_top + 0.015), (xe + 0.02, r_top + 0.015), (xe, r_top + 0.12)],
                         fy - 0.012, fy + 0.012, bevel=0.0)
    # Anchor plates and bolts where the rail meets the wall.
    for xe in (xl, xr):
        for z0 in (z_top + 0.06, r_top - 0.03):
            b_iron.box(xe - 0.045, xe + 0.045, face - 0.008, face + 0.002, z0 - 0.045, z0 + 0.045,
                       bevel=0.003)


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


def horseshoe(r0, r1, cx, cz, foot, n=28):
    """Closed (x, z) outline of a round-headed band between radii r0 and r1, legs to `foot`."""
    outer = [(cx + r1 * math.cos(math.pi * i / n), cz + r1 * math.sin(math.pi * i / n))
             for i in range(n + 1)]
    inner = [(cx + r0 * math.cos(math.pi * i / n), cz + r0 * math.sin(math.pi * i / n))
             for i in range(n, -1, -1)]
    return ([(cx + r1, foot)] + outer + [(cx - r1, foot), (cx - r0, foot)] + inner
            + [(cx + r0, foot)])


def ring_cutter():
    """The dark groove, 0.10 deep into the bay face."""
    r0, r1 = RING_GROOVE
    return cutter("aa_cut_gentleman_ring", horseshoe(r0, r1, *RING_C, RING_FOOT), -BAY_P - 0.5,
                  -BAY_P + 0.10)


def cartouche():
    """Mouldings framing the groove, a dark lining in it, and plinth blocks at the feet."""
    b = Builder()
    cx, cz = RING_C
    r0, r1 = RING_GROOVE
    face = -BAY_P
    # Dark lining at the bottom of the groove (sooted, as in the reference).
    b.prism(horseshoe(r0, r1, cx, cz, RING_FOOT), face + 0.085, face + 0.10, mat=1, bevel=0.0)
    # Inner bead and a stepped outer architrave.
    for ra, rb, proud in ((r0 - 0.08, r0, 0.07), (r1, r1 + 0.07, 0.13), (r1 + 0.07, RING_OUTER, 0.08)):
        b.prism(horseshoe(ra, rb, cx, cz, RING_FOOT), face - proud, face + 0.01, bevel=0.01)
    # Plinth blocks where the legs land on the cornice line.
    for sx in (-1, 1):
        xa, xb = sorted((cx + sx * (r0 - 0.12), cx + sx * (RING_OUTER + 0.03)))
        b.box(xa, xb, face - 0.16, face + 0.01, RUST_TOP, RING_FOOT + 0.3, bevel=0.012)
    return b


def seat_marquee():
    """Size the marquee (and its tagline panel) to the arch and hang it clear of the orders.
    Uniform scale about its bottom edge, so the lettering keeps its proportions. Idempotent."""
    co = [v.co for v in bpy.data.objects["aa_arch_hero_marquee"].data.vertices]
    k = MARQUEE_W / (max(c.x for c in co) - min(c.x for c in co))
    y_back, z_foot = max(c.y for c in co), min(c.z for c in co)
    if abs(k - 1) < 1e-3 and abs(MARQUEE_BACK - y_back) < 1e-3:
        return 0.0
    m = (Matrix.Translation((0, MARQUEE_BACK, z_foot)) @ Matrix.Scale(k, 4)
         @ Matrix.Translation((0, -y_back, -z_foot)))
    for name in MARQUEE_PARTS:
        me = bpy.data.objects[name].data
        me.transform(m)
        me.update()
    return round(k, 3)


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

SOFTEN = {"aa_shell_facade_mouldings": 0.006}


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
    # Old float glass: faintly green-grey, glossy, mostly see-through so the sheer reads.
    glass = material("m_aa_window_glass", (0.10, 0.13, 0.13), rough=0.02, metallic=0.0, alpha=0.42)
    curtain = material("m_aa_window_curtain", (0.82, 0.8, 0.74), rough=0.9, alpha=0.8)
    dark = material("m_aa_interior_void", (0.01, 0.012, 0.012), rough=1.0)
    roof_m = material("m_aa_roof_tile", (0.16, 0.11, 0.10), rough=0.75)

    cutters = [cutter("aa_cut_entrance", arch_outline(ARCH_HALF, ARCH_SPRING, ARCH_RISE, bottom=-0.1),
                      -1.0, ARCH_DEPTH)]
    for i, (x, z, style) in enumerate(UPPER_WINDOWS):
        h = WIN_H[style]
        cutters.append(cutter(f"aa_cut_win_{i}", [(x - WIN_W / 2, z), (x + WIN_W / 2, z),
                                                  (x + WIN_W / 2, z + h), (x - WIN_W / 2, z + h)],
                              -1.0, WALL_T + 0.1))
    # arch_outline() is centred on x = 0; shift it to the window's bay.
    cutters.append(cutter("aa_cut_ground_window",
                          [(px + GW_X, pz) for px, pz in arch_outline(GW_HALF, GW_SPRING, GW_HALF,
                                                                      bottom=GW_SILL)],
                          -1.0, WALL_T + 0.1))
    cutters.append(rustication_cutter(B))
    cutters.append(ring_cutter())
    if "aa_shell_facade_walls" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["aa_shell_facade_walls"], do_unlink=True)
    walls = facade_wall(B, cutters)

    made = {"walls": len(walls.data.polygons)}
    stone_b = Builder()
    frame_b = Builder()
    iron_b = Builder()
    for x, z, s in UPPER_WINDOWS:
        window(stone_b, frame_b, x, z, s)
    ground_window(stone_b, frame_b, iron_b)
    for bx, bz, var in BALCONIES:
        balcony(stone_b, iron_b, bx, bz, var)
    iron = material("m_aa_wrought_iron", (0.025, 0.025, 0.027), rough=0.45, metallic=0.6)
    for name, builder, mats in (
            ("aa_shell_facade_mouldings", mouldings(B), [trim]),
            ("aa_shell_facade_quoins", quoins(B), [trim]),
            ("aa_shell_facade_window_surrounds", stone_b, [trim]),
            ("aa_shell_facade_sash_windows", frame_b, [wood, glass, curtain, dark]),
            ("aa_shell_facade_ironwork", iron_b, [iron]),
            ("aa_shell_facade_roof", roof(B), [roof_m]),
            ("aa_shell_facade_interior_void", void(B), [dark])):
        o = builder.to_object(name, mats, coll)
        made[name] = len(o.data.polygons)
        # Boxes are bevelled as they are built; the swept profiles are not.
        if name in SOFTEN:
            soften(o, SOFTEN[name])
    soften(walls, 0.01)
    av, pl = entrance(B)
    replace_mesh("aa_arch_hero_archivolt", av, [trim])
    replace_mesh("aa_arch_hero_plinths", pl, [trim])
    if "aa_arch_hero_cartouche" not in bpy.data.objects:
        cartouche().to_object("aa_arch_hero_cartouche", [trim, dark], bpy.data.collections["aa_arch_hero"])
    else:
        replace_mesh("aa_arch_hero_cartouche", cartouche(), [trim, dark])
    made["gentleman_lift"] = seat_gentleman()
    made["marquee_shift"] = seat_marquee()
    return made


if __name__ == "__main__" or "AA_RUN" in globals():
    result = main()
    print(result)
