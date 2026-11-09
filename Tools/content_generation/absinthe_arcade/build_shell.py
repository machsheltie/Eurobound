"""Build aa_shell_facade to the daytime bible's proportions (E1 massing pass, 2026-10-28).

Replaces the earlier wide symmetrical palazzo. Every number comes from manifest.json ->
"facade", measured off the bible through aa_bible_cam (bible_camera.py) on the rectified
facade plane, and from the asset sheet above the bible's crop (Q-001 answer A).

The building, as the bible shows it: a narrow three-bay front, 8.44 m from the left
arris to the right downspout seam. Left window column (arched ground-floor window over
the awning, the cat window, the balcony window), the mural field over the arch, and a
right column tight against the seam that sits about 0.4 m lower than the left. On the
left the corner is canted at 45 degrees into a corner bay with a window per upper
storey, stacked stone cornices and a corner pilaster with its capital under the
ground-floor cornice. No string courses cross the mural: the bible only shows the short
ground-floor cornice runs at the two edges. Three masonry storeys, then the slate
mansard with two dormers, the carved stone gable and four chimney stacks.

Depth planes, street inward: arch ring and keystone (proud 0.14-0.26), piers and corner
pilaster (0.12-0.15), surrounds (0.07), wall face (0), window frames set back 0.2 in
0.55 m of masonry. Openings are real holes with reveals.

Blender space: main wall face on y=0, street toward -Y, z up, X=0 on the arch axis.
Re-runnable: replaces the shell collection's contents and the arch hero's masonry
(archivolt, plinths; the cartouche is removed per interfaces v2), and re-seats the gentleman
and marquee on the new arch.
"""

import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

M = aa.load_manifest()
FA = M["facade"]
BLD = M["building"]

BEVEL = 0.012                    # default arris softening on stone
WALL_T = FA["wall_t"]
BACK_T = FA.get("walls", {}).get("back_t", WALL_T)
X_LEFT, X_RIGHT = FA["x_left"], FA["x_right"]
EAVE0, EAVE1 = FA["eave_cornice_z"]
DEPTH = BLD["depth"]

# Arch (shared with aa_arch_hero and build_fittings.py). v2: the ring springs at +-ARCH_HALF about
# X=0; the right jamb sits at JAMB_R (the bible's pier arris), the left jamb at -ARCH_HALF.
AR = FA["arch"]
ARCH_HALF, ARCH_SPRING, ARCH_RISE = AR["half"], AR["springing"], AR["rise"]
JAMB_L, JAMB_R = -ARCH_HALF, AR.get("jamb_r", ARCH_HALF)
EXT_HALF, EXT_RISE = AR["ext_half"], AR["ext_rise"]
ARCH_DEPTH = AR["interior_void_y"]
RUST_P = 0.0                     # no rustication on this front (kept for build_fittings)
PLINTH_P = FA["plinth_course"]["proud"]
# build_fittings reads ORDERS[-1] = (offset of the outer edge from the intrados, proud):
# its green neon rides just outside the ring, as in the bible.
ORDERS = [(EXT_HALF - ARCH_HALF + 0.11, AR["ring_proud"])]
MARQUEE_PARTS = ("aa_arch_hero_marquee", "aa_arch_hero_tagline_panel")
MARQUEE_BACK = -AR["ring_proud"] - 0.08
MQ = FA["arch"].get("marquee", {"width": 4.64, "bottom_z": 2.77})
MARQUEE_W = MQ["width"]
MARQUEE_FOOT = MQ["bottom_z"]

WINDOWS = FA["windows"]
SUR = FA["surround"]
SASH_SET = SUR["reveal_depth"]
DRAIN = FA["drainpipes"]
DRAIN_X = (DRAIN["left"]["x_upper"], DRAIN["right"]["x"])     # compatibility (box_over_pipe)

CB = FA["corner_bay"]
CB_A = math.radians(CB["angle_deg"])
CB_D = Vector((-math.cos(CB_A), math.sin(CB_A), 0.0))           # along the cant, from the arris
CB_N = Vector((-math.sin(CB_A), -math.cos(CB_A), 0.0))          # outward normal of the cant
CB_ARRIS = Vector((X_LEFT, 0.0, 0.0))
CB_FAR = CB_ARRIS + CB_D * CB["width"]
# Local frame of the cant face, so facade-style builders work on it: x' runs from the far
# end (0) to the arris (width), y' into the wall, z up.
CB_MAT = Matrix(((-CB_D.x, -CB_N.x, 0.0, CB_FAR.x),
                 (-CB_D.y, -CB_N.y, 0.0, CB_FAR.y),
                 (0.0, 0.0, 1.0, 0.0),
                 (0.0, 0.0, 0.0, 1.0)))
# Right side elevation (Q-011 answer A): local x' = world Y (0 at the front face), y' into the
# building (world -X), face on world X = X_RIGHT. Seen from outside, x' runs to the right.
SR = FA["side_right"]
SIDE_MAT = Matrix(((0.0, -1.0, 0.0, X_RIGHT),
                   (1.0, 0.0, 0.0, 0.0),
                   (0.0, 0.0, 1.0, 0.0),
                   (0.0, 0.0, 0.0, 1.0)))
# Left side wall behind the corner bay: x' = -(world Y) from the back corner, y' = world +X.
LEFT_MAT = Matrix(((0.0, 1.0, 0.0, CB_FAR.x),
                   (-1.0, 0.0, 0.0, DEPTH),
                   (0.0, 0.0, 1.0, 0.0),
                   (0.0, 0.0, 0.0, 1.0)))


# --------------------------------------------------------------------------- mesh helpers

def material(name, color, rough=0.8, metallic=0.0, alpha=1.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metallic
    b.inputs["Alpha"].default_value = alpha
    if alpha < 1.0:
        m.surface_render_method = "DITHERED"
    m.diffuse_color = (*color, 1)
    return m


def slate_material():
    """m_aa_roof_tile: blue-grey slates in horizontal courses (procedural, world space): a brick
    pattern on (x + y, z) with per-slate tone variation, dark gaps and a small bump. Courses are
    0.17 m, slates 0.32 m wide, alternate courses half-offset."""
    m = bpy.data.materials.get("m_aa_roof_tile") or bpy.data.materials.new("m_aa_roof_tile")
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    N = nt.nodes.new
    out = N("ShaderNodeOutputMaterial")
    bsdf = N("ShaderNodeBsdfPrincipled")
    geo = N("ShaderNodeNewGeometry")
    sep = N("ShaderNodeSeparateXYZ")
    add = N("ShaderNodeMath")
    add.operation = "ADD"
    comb = N("ShaderNodeCombineXYZ")
    brick = N("ShaderNodeTexBrick")
    brick.offset, brick.offset_frequency = 0.5, 2
    brick.inputs["Color1"].default_value = (0.026, 0.032, 0.046, 1)
    brick.inputs["Color2"].default_value = (0.050, 0.058, 0.080, 1)
    brick.inputs["Mortar"].default_value = (0.012, 0.013, 0.016, 1)
    brick.inputs["Scale"].default_value = 1.0
    brick.inputs["Mortar Size"].default_value = 0.012
    brick.inputs["Mortar Smooth"].default_value = 0.2
    brick.inputs["Bias"].default_value = 0.0
    brick.inputs["Brick Width"].default_value = 0.32
    brick.inputs["Row Height"].default_value = 0.17
    noise = N("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 3.0
    tone = N("ShaderNodeMix")
    tone.data_type = "RGBA"
    tone.blend_type = "MULTIPLY"
    tone.inputs["Factor"].default_value = 0.35
    bump = N("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.35
    bump.inputs["Distance"].default_value = 0.01
    inv = N("ShaderNodeMath")
    inv.operation = "SUBTRACT"
    inv.inputs[0].default_value = 1.0
    L = nt.links.new
    L(geo.outputs["Position"], sep.inputs["Vector"])
    L(sep.outputs["X"], add.inputs[0])
    L(sep.outputs["Y"], add.inputs[1])
    L(add.outputs["Value"], comb.inputs["X"])
    L(sep.outputs["Z"], comb.inputs["Y"])
    L(comb.outputs["Vector"], brick.inputs["Vector"])
    L(comb.outputs["Vector"], noise.inputs["Vector"])
    L(brick.outputs["Color"], tone.inputs["A"])
    L(noise.outputs["Color"], tone.inputs["B"])
    L(tone.outputs["Result"], bsdf.inputs["Base Color"])
    L(brick.outputs["Fac"], inv.inputs[1])
    L(inv.outputs["Value"], bump.inputs["Height"])
    L(bump.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Roughness"].default_value = 0.62
    L(bsdf.outputs["BSDF"], out.inputs["Surface"])
    m.diffuse_color = (0.07, 0.08, 0.1, 1)
    return m


def base_material(name, color):
    """The shell's base stone/trim materials (kept with a fake user: after integration E5's
    materials replace them on every slot, and an unused material would be purged on save)."""
    m = bpy.data.materials.get(name) or material(name, color, rough=0.85)
    m.use_fake_user = True
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
        s = Vector((abs(x1 - x0), abs(y1 - y0), abs(z1 - z0)))
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

    def prism_xy(self, outline_xy, z0, z1, mat=0, bevel=BEVEL):
        """Extrude a closed (x, y) footprint from z0 to z1."""
        lo = [self.bm.verts.new((x, y, z0)) for x, y in outline_xy]
        hi = [self.bm.verts.new((x, y, z1)) for x, y in outline_xy]
        n = len(outline_xy)
        self.bm.faces.new(lo)
        self.bm.faces.new(hi[::-1])
        for i in range(n):
            j = (i + 1) % n
            self.bm.faces.new((lo[i], hi[i], hi[j], lo[j]))
        verts = lo + hi
        bmesh.ops.recalc_face_normals(self.bm, faces=list({f for v in verts for f in v.link_faces}))
        self._finish(verts, mat, bevel)
        return verts

    def loft(self, ring_a, ring_b, mat=0, cap=True):
        """Solid between two closed 3D rings with the same vertex count."""
        a = [self.bm.verts.new(p) for p in ring_a]
        b = [self.bm.verts.new(p) for p in ring_b]
        n = len(a)
        faces = []
        for i in range(n):
            j = (i + 1) % n
            faces.append(self.bm.faces.new((a[i], a[j], b[j], b[i])))
        if cap:
            faces.append(self.bm.faces.new(a[::-1]))
            faces.append(self.bm.faces.new(b))
        bmesh.ops.recalc_face_normals(self.bm, faces=faces)
        for f in faces:
            f.material_index = mat
        return a + b

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

    def absorb(self, other, matrix=None):
        """Merge another builder's geometry, optionally transformed (e.g. the cant frame)."""
        if matrix is not None:
            bmesh.ops.transform(other.bm, matrix=matrix, verts=other.bm.verts)
        me = bpy.data.meshes.new("aa_tmp_absorb")
        other.bm.to_mesh(me)
        other.bm.free()
        self.bm.from_mesh(me)
        bpy.data.meshes.remove(me)

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


def arch_outline(half, spring, rise, n=40, bottom=0.0, jamb_r=None):
    """Closed (x, z) outline of a segmental-elliptic arch opening down to `bottom`. jamb_r widens
    the opening right of the ring's springing (v2: the bible's right pier arris)."""
    pts = [(-half, bottom), (-half, spring)]
    for i in range(1, n):
        t = math.pi - math.pi * i / n
        pts.append((half * math.cos(t), spring + rise * math.sin(t)))
    pts += [(half, spring)]
    if jamb_r is not None and jamb_r > half + 1e-4:
        pts += [(jamb_r, spring), (jamb_r, bottom)]
    else:
        pts += [(half, bottom)]
    return pts


def arch_point(half, spring, rise, t, off=0.0):
    """Point on the arch intrados at angle t (0..pi), pushed outward along its normal."""
    p = Vector((half * math.cos(t), spring + rise * math.sin(t)))
    n = Vector((math.cos(t) / max(half, 1e-6), math.sin(t) / max(rise, 1e-6))).normalized()
    return p + n * off


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


def ring(b, cx, cz, r0, r1, y0, y1, mat=0, n=24, bevel=0.006, gap=0.0, rz0=None, rz1=None):
    """Arch band between two concentric half-ellipses (x semi-axes r0, r1; z semi-axes rz0, rz1,
    default = r0, r1: semicircular), built from n solids."""
    rz0 = r0 if rz0 is None else rz0
    rz1 = r1 if rz1 is None else rz1
    for i in range(n):
        t0 = math.pi * i / n + gap
        t1 = math.pi * (i + 1) / n - gap
        pts = [(cx + r0 * math.cos(t0), cz + rz0 * math.sin(t0)),
               (cx + r1 * math.cos(t0), cz + rz1 * math.sin(t0)),
               (cx + r1 * math.cos(t1), cz + rz1 * math.sin(t1)),
               (cx + r0 * math.cos(t1), cz + rz0 * math.sin(t1))]
        b.prism(pts, y0, y1, mat=mat, bevel=bevel)


def cutter_obj(name, builder):
    me = bpy.data.meshes.new(name)
    builder.bm.to_mesh(me)
    builder.bm.free()
    obj = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(obj)
    obj.hide_render = True
    return obj


# --------------------------------------------------------------------------- walls

def window_cut_outline(w):
    hw = w["w"] / 2
    x = w["cx"]
    if w["kind"] == "arched":
        r = w["crown"] - w["springing"]
        pts = [(x - hw, w["sill"]), (x - hw, w["springing"])]
        for i in range(1, 32):
            t = math.pi - math.pi * i / 32
            pts.append((x + hw * math.cos(t), w["springing"] + r * math.sin(t)))
        return pts + [(x + hw, w["springing"]), (x + hw, w["sill"])]
    return [(x - hw, w["sill"]), (x + hw, w["sill"]), (x + hw, w["head"]), (x - hw, w["head"])]


def cant_windows():
    """(x' centre, sill, head) of the corner bay's windows, in the cant's local frame."""
    xc = CB["width"] / 2
    return [(xc, s, h) for s, h in CB.get("windows_z", [(6.85, 8.60), (10.17, 11.92)])]


def build_walls():
    """Main wall, the cant wall of the corner bay, side, back and party walls; openings cut."""
    b = Builder()
    b.box(X_LEFT, X_RIGHT, 0.0, WALL_T, 0.0, EAVE0, bevel=0.0)
    cb = Builder()
    cb.box(0.0, CB["width"], 0.0, WALL_T, 0.0, EAVE0, bevel=0.0)    # meets the main wall inside
    b.absorb(cb, CB_MAT)
    side_x = CB_FAR.x
    b.box(side_x, side_x + WALL_T, CB_FAR.y, DEPTH, 0.0, EAVE0, bevel=0.0)
    b.box(side_x, X_RIGHT, DEPTH - BACK_T, DEPTH, 0.0, EAVE0, bevel=0.0)
    b.box(X_RIGHT - WALL_T, X_RIGHT, WALL_T, DEPTH, 0.0, EAVE0, bevel=0.0)
    stone = base_material("m_aa_limestone_weathered", (0.72, 0.64, 0.52))
    obj = b.to_object("aa_shell_facade_walls", [stone], shell_coll())

    cutters = []
    c = Builder()
    c.prism(arch_outline(ARCH_HALF, ARCH_SPRING, ARCH_RISE, bottom=-0.1, jamb_r=JAMB_R), -1.0, WALL_T + 0.3,
            bevel=0.0)
    cutters.append(cutter_obj("aa_cut_entrance", c))
    for k, w in WINDOWS.items():
        c = Builder()
        c.prism(window_cut_outline(w), -1.0, WALL_T + 0.1, bevel=0.0)
        cutters.append(cutter_obj(f"aa_cut_{k}", c))
    for i, (xc, sill, head) in enumerate(cant_windows()):
        c = Builder()
        hw = CB["window_w"] / 2
        c.box(xc - hw, xc + hw, -1.0, WALL_T + 0.1, sill, head, bevel=0.0)
        c2 = Builder()
        c2.absorb(c, CB_MAT)
        cutters.append(cutter_obj(f"aa_cut_cant_{i}", c2))
    for k, w in SR["windows"].items():
        c = Builder()
        c.prism(window_cut_outline(w), -1.0, WALL_T + 0.1, bevel=0.0)
        c2 = Builder()
        c2.absorb(c, SIDE_MAT)
        cutters.append(cutter_obj(f"aa_cut_{k}", c2))
    for cu in cutters:
        mod = obj.modifiers.new(cu.name, "BOOLEAN")
        mod.operation = "DIFFERENCE"
        mod.solver = "EXACT"
        mod.use_self = True             # the walls are overlapping solids, not one shell
        mod.use_hole_tolerant = True
        mod.object = cu
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(obj.evaluated_get(dg))
    old = obj.data
    obj.modifiers.clear()
    obj.data = me
    bpy.data.meshes.remove(old)
    me.name = "aa_shell_facade_walls"
    for cu in cutters:
        bpy.data.objects.remove(cu, do_unlink=True)
    return obj


# --------------------------------------------------------------------------- mouldings

def cornice_profile(z0, z1, proud):
    """Simple stone cornice: fillet, cove, corona with drip, cymatium; scaled into z0..z1."""
    h = z1 - z0
    return [(0, z0), (proud * 0.25, z0), (proud * 0.25, z0 + h * 0.18), (proud * 0.45, z0 + h * 0.32),
            (proud * 0.85, z0 + h * 0.5), (proud * 0.85, z0 + h * 0.72), (proud, z0 + h * 0.8),
            (proud, z0 + h), (0, z1)]


def build_mouldings():
    b = Builder()
    pc = FA["plinth_course"]
    # Low plinth course along the main wall (the doorway and the plinth blocks interrupt it).
    for x0, x1 in ((X_LEFT, -ARCH_HALF - 0.48), (FA["right_pier"]["x"][1] + 0.06, X_RIGHT)):
        b.sweep([(0, 0), (pc["proud"], 0), (pc["proud"], pc["z_top"] - 0.05),
                 (pc["proud"] - 0.03, pc["z_top"]), (0, pc["z_top"])], x0, x1)
    # Ground-floor cornice runs: left (over the arched window, round the arris onto the
    # cant as the corner bay's base cornice) and right (into the seam).
    g = FA["gf_cornice"]
    L, R = g["left"], g["right"]
    b.sweep(cornice_profile(L["z"][0], L["z"][1], L["proud"]), L["x"][0], L["x"][1])
    b.sweep(cornice_profile(R["z"][0], R["z"][1], R["proud"]), R["x"][0], R["x"][1])
    # Eave cornice along the main wall (above the bible's crop; asset sheet proportions).
    b.sweep(cornice_profile(EAVE0, EAVE1, 0.42), X_LEFT, X_RIGHT)
    # Returns on the side elevations: eave cornice and plinth course; the right ground-floor
    # cornice turns the corner as far as the pilaster's wrap.
    side = Builder()
    side.sweep(cornice_profile(EAVE0, EAVE1, 0.42), -0.42, DEPTH + 0.42)
    side.sweep([(0, 0), (pc["proud"], 0), (pc["proud"], pc["z_top"] - 0.05),
                (pc["proud"] - 0.03, pc["z_top"]), (0, pc["z_top"])], 0.3, DEPTH)
    side.sweep(cornice_profile(R["z"][0], R["z"][1], R["proud"]), -R["proud"],
               FA["right_corner"]["wrap"] + 0.06)
    b.absorb(side, SIDE_MAT)
    left = Builder()
    left.sweep(cornice_profile(EAVE0, EAVE1, 0.42), -0.42, DEPTH - CB_FAR.y + 0.3)
    b.absorb(left, LEFT_MAT)
    # Corner bay cornices, built in the cant frame and turned onto it.
    cb = Builder()
    for z0, z1, proud in CB.get("cornices", [(*c, CB["cornice_proud"]) for c in CB["cornice_z"]]):
        cb.sweep(cornice_profile(z0, z1, proud), -0.05, CB["width"] + 0.02)
    b.absorb(cb, CB_MAT)
    return b


def build_corner_bay():
    """Corner pilaster, plinth block, cant-face pilasters and window surrounds + hoods."""
    b = Builder()
    cp = CB["corner_pilaster"]
    x0, x1 = cp["x"]
    zc0, zc1 = cp["capital_z"]
    pl = CB["plinth"]
    b.box(x0, x1, -cp["proud"], 0.02, pl["z_top"], zc0, bevel=0.01)                  # shaft
    b.box(x0 - 0.04, x1 + 0.05, -cp["proud"] - 0.06, 0.02, zc0, zc1 - 0.1, bevel=0.012)  # bell
    b.box(x0 - 0.07, x1 + 0.08, -cp["proud"] - 0.1, 0.02, zc1 - 0.1, zc1, bevel=0.01)   # abacus
    b.box(pl["x"][0], pl["x"][1], -pl["proud"], 0.02, 0.0, pl["z_top"], bevel=0.015)   # plinth
    loc = Builder()
    w = CB["width"]
    pw, pp = CB["pilaster_w"], CB["pilaster_proud"]
    # Plinth and pilaster wrap onto the cant at the arris; a second pilaster at the far end.
    loc.box(w - pl["wrap"], w + 0.02, -pl["proud"], 0.02, 0.0, pl["z_top"], bevel=0.015)
    for xa, xb in ((w - pw, w + 0.02), (0.0, pw)):
        loc.box(xa, xb, -pp, 0.02, pl["z_top"], EAVE0, bevel=0.01)
        loc.box(xa - 0.03, xb + 0.03, -pp - 0.06, 0.02, zc0, zc1, bevel=0.012)
    for xc, sill, head in cant_windows():
        hw = CB["window_w"] / 2
        band = SUR["band"]
        frame(loc, xc, sill, head + 0.003, hw + 0.003, band, -SUR["proud"], 0.02, 0.008)
        sp, hp = CB.get("sill_proud", 0.2), CB.get("hood_proud", 0.26)
        loc.box(xc - hw - 0.14, xc + hw + 0.14, -sp, 0.0, sill - 0.12, sill, bevel=0.01)          # sill
        loc.box(xc - hw - band - 0.08, xc + hw + band + 0.08, -hp, 0.02, head + band,
                head + band + 0.14, bevel=0.01)                                               # hood
        for sx in (-1, 1):                                                                    # lining
            xa, xb = sorted((xc + sx * (hw - 0.003), xc + sx * (hw - 0.023)))
            loc.box(xa, xb, 0.003, SASH_SET, sill + 0.003, head - 0.003, bevel=0.0)
        loc.box(xc - hw + 0.003, xc + hw - 0.003, 0.003, SASH_SET, head - 0.023, head - 0.003, bevel=0.0)
    b.absorb(loc, CB_MAT)
    build_right_corner(b)
    return b


def build_right_corner(b):
    """Right corner (asset sheet): plinth block, pilaster with capital under the right
    ground-floor cornice, quoins to the eave; each piece wraps onto the side elevation."""
    RC = FA["right_corner"]
    x0, x1 = RC["x"]
    wrap = RC["wrap"]
    pl, pi, q = RC["plinth"], RC["pilaster"], RC["quoins"]

    def wrapped(xa, depth, z0, z1, proud, bevel):
        b.box(xa, x1 + proud, -proud, 0.02, z0, z1, bevel=bevel)          # front face
        b.box(x1 - 0.02, x1 + proud, -proud, depth, z0, z1, bevel=bevel)  # side return

    # The plinth starts where the arch's right plinth cap ends (no coplanar tops at z_top).
    wrapped(max(x0 - 0.04, FA["right_pier"]["x"][1] + 0.06), wrap + 0.04, 0.0, pl["z_top"], pl["proud"], 0.015)
    c0, c1 = pi["capital_z"]
    wrapped(x0, wrap, pl["z_top"], c0, pi["proud"], 0.01)
    wrapped(x0 - 0.04, wrap + 0.04, c0, c1 - 0.1, pi["proud"] + 0.05, 0.012)   # bell
    wrapped(x0 - 0.07, wrap + 0.07, c1 - 0.1, c1, pi["proud"] + 0.09, 0.01)    # abacus
    z, i = q["z"][0], 0
    while z < q["z"][1] - 0.05:
        h = min(q["course"], q["z"][1] - z)
        front = q["long"] if i % 2 == 0 else q["short"]
        side = q["short"] if i % 2 == 0 else q["long"]
        b.box(x1 - front, x1 + q["proud"], -q["proud"], 0.02, z + 0.01, z + h - 0.01, bevel=0.012)
        b.box(x1 - 0.02, x1 + q["proud"], -q["proud"], side, z + 0.01, z + h - 0.01, bevel=0.012)
        z += h
        i += 1


CAM_LOC = M["bible_camera"]["location"]
# E2's window kits (frame, sashes, architrave, sill/slab, crest, rail, flowers) replace E1's clay
# surrounds, linings and placeholder sashes once integrate_elements.py has appended them.
E2_KIT = {"left_w1_arched": "aa_window_l1_arched", "left_w2_cat": "aa_window_l2_cat",
          "left_w3_balcony": "aa_window_l3_balcony", "right_w1": "aa_window_r1", "right_w2": "aa_window_r2",
          "side_w0_ground": "aa_window_side_w0", "side_w1": "aa_window_side_w1", "side_w2": "aa_window_side_w2"}


def has_kit(key):
    return E2_KIT.get(key) in bpy.data.collections
LINING_T = SUR.get("lining_board_t", 0.04)


def frame_rect(w, bible=True):
    """(x0, x1, top, spring) of the timber frame's front outline at the reveal. Front windows: the
    bible's frame trace (on the face plane) moved back along aa_bible_cam's rays to y = SASH_SET,
    then slid into the hole if the lining is thinner than the parallax (interfaces v2
    frame_at_reveal). Side windows (not in the bible): the frame as specified."""
    f = w["frame"]
    top = f.get("crown", f.get("top"))
    hole_l, hole_r = w["cx"] - w["w"] / 2, w["cx"] + w["w"] / 2
    head = w.get("crown", w.get("head"))
    spring = f.get("springing")
    if not bible:
        return f["x"][0], f["x"][1], top, spring
    t = (w.get("reveal", SASH_SET) - CAM_LOC[1]) / -CAM_LOC[1]
    mv = lambda a, c: c + (a - c) * t                          # noqa: E731
    x0, x1, top = mv(f["x"][0], CAM_LOC[0]), mv(f["x"][1], CAM_LOC[0]), mv(top, CAM_LOC[2])
    if spring is not None:
        spring = mv(spring, CAM_LOC[2])
    shift = max(0.0, hole_l + 0.01 - x0) - max(0.0, x1 - (hole_r - 0.01))
    return x0 + shift, x1 + shift, min(top, head - 0.01), spring


def lining_board(b, w, x0, x1, top, spring=None):
    """Stone lining at the frame plane between the frame and the hole (the light band the bible
    shows round every frame). Placeholder: E2's window kits carry their own lining."""
    hole_l, hole_r = w["cx"] - w["w"] / 2, w["cx"] + w["w"] / 2
    head = w.get("head", spring)
    zt = spring if spring is not None else head
    y0 = w.get("reveal", SASH_SET)
    y1 = y0 + LINING_T
    if x0 - hole_l > 0.005:
        b.box(hole_l + 0.002, x0, y0, y1, w["sill"], zt, bevel=0.0)
    if hole_r - x1 > 0.005:
        b.box(x1, hole_r - 0.002, y0, y1, w["sill"], zt, bevel=0.0)
    if spring is None and head - top > 0.005:
        b.box(x0, x1, y0, y1, top, head - 0.002, bevel=0.0)


def build_side_right(stone_b, frame_b):
    """The asset sheet's one-bay right side: three windows on the right column's floors,
    clay surrounds, placeholder sashes, and a pilaster strip at the back corner."""
    st, fr = Builder(), Builder()
    for k, w in SR["windows"].items():
        if has_kit(k):
            continue
        surround(st, w)
        x0, x1, top, _ = frame_rect(w, bible=False)
        lining_board(st, w, x0, x1, top)
        sash_window(fr, (x0 + x1) / 2, w["sill"], top, (x1 - x0) / 2)
    u0, u1 = SR["back_pilaster"]["u"]
    st.box(u0, u1 + 0.02, -SR["back_pilaster"]["proud"], 0.02, FA["plinth_course"]["z_top"], EAVE0, bevel=0.01)
    stone_b.absorb(st, SIDE_MAT)
    frame_b.absorb(fr, SIDE_MAT)


def cant_glazing():
    """Simple timber frames, glass and dark backing in the corner bay's windows (E2 replaces)."""
    loc = Builder()
    for xc, sill, head in cant_windows():
        sash_window(loc, xc, sill, head, CB["window_w"] / 2)
    out = Builder()
    out.absorb(loc, CB_MAT)
    return out


# --------------------------------------------------------------------------- entrance

def ellipse_pt(half, rise, t):
    return Vector((half * math.cos(t), ARCH_SPRING + rise * math.sin(t)))


def build_entrance():
    """Arch ring of voussoirs between the intrados and extrados ellipses, piers with capitals at
    the springing. No keystone and no crown voussoir (interfaces v2): the bible's carved head
    (E4) and its volutes sit in front of the archivolt there. Returns (archivolt, plinths)."""
    av = Builder()
    proud = AR["ring_proud"]
    n = 15
    for i in range(n):
        if i == n // 2:
            continue                                   # the keystone takes the crown
        t0 = math.pi * i / n + 0.004
        t1 = math.pi * (i + 1) / n - 0.004
        pts = []
        steps = 4
        for k in range(steps + 1):
            pts.append(tuple(ellipse_pt(ARCH_HALF, ARCH_RISE, t0 + (t1 - t0) * k / steps)))
        for k in range(steps, -1, -1):
            pts.append(tuple(ellipse_pt(EXT_HALF, EXT_RISE, t0 + (t1 - t0) * k / steps)))
        av.prism(pts, -proud, 0.02, bevel=0.01)
        # Inner moulding step on the intrados edge (reads as the ring's moulded lip).
        lip = []
        for k in range(steps + 1):
            lip.append(tuple(ellipse_pt(ARCH_HALF, ARCH_RISE, t0 + (t1 - t0) * k / steps)))
        for k in range(steps, -1, -1):
            lip.append(tuple(ellipse_pt(ARCH_HALF + 0.07, ARCH_RISE + 0.07, t0 + (t1 - t0) * k / steps)))
        av.prism(lip, -proud - 0.04, -proud + 0.01, bevel=0.006)
    # Piers either side of the opening, capitals at the springing (v2: the bible's right pier
    # 2.37..2.80; the left one, under the posters and conduits, has its inner face on the left
    # jamb). The right impost covers the 0.07 shelf between the ring's springing and the jamb.
    for side, rp in ((-1, FA["left_pier"]), (1, FA["right_pier"])):
        xa, xb = rp["x"]
        av.box(xa, xb, -rp["proud"], 0.02, rp["base_z_top"], rp["capital_z"][0], bevel=0.01)
        c0, c1 = rp["capital_z"]
        av.box(xa - 0.05, xb + 0.05, -rp["proud"] - 0.08, 0.02, c0, c1 - 0.12, bevel=0.012)
        av.box(xa - 0.08, xb + 0.08, -rp["proud"] - 0.12, 0.02, c1 - 0.12, c1, bevel=0.01)
    pl = Builder()
    for side, rp in ((-1, FA["left_pier"]), (1, FA["right_pier"])):
        inner, outer = (rp["x"][1], rp["x"][0]) if side < 0 else rp["x"]
        xa, xb = sorted((inner - side * 0.09, outer + side * 0.04))
        pl.box(xa, xb, -rp["proud"] - 0.07, 0.02, 0.0, rp["base_z_top"] - 0.08, bevel=0.015)   # under the cap
        pl.box(xa - 0.02, xb + 0.02, -rp["proud"] - 0.1, 0.0, rp["base_z_top"] - 0.08,
               rp["base_z_top"], bevel=0.01)
    if "aa_e3_doorway" not in bpy.data.collections:          # E3 brings its own threshold and floor
        st = AR["step"]
        pl.box(st["x"][0], st["x"][1], st["y_front"], 0.3, 0.0, st["z_top"], bevel=0.012)   # step
        pl.box(JAMB_L, JAMB_R, 0.3, ARCH_DEPTH, -0.2, st["z_top"] - 0.02, bevel=0.0)          # floor
    return av, pl


# --------------------------------------------------------------------------- windows

def frame(b, x, sill, top, hw, band, y0, y1, bevel):
    """Architrave band round an opening: two jambs and a head (the sill closes the bottom)."""
    b.box(x - hw - band, x - hw, y0, y1, sill, top + band, bevel=bevel)
    b.box(x + hw, x + hw + band, y0, y1, sill, top + band, bevel=bevel)
    b.box(x - hw, x + hw, y0, y1, top, top + band, bevel=bevel)


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
    either side of a mullion) and a lower sash that slides up in an inner track. `raised`
    lifts the lower sash behind the upper light. Nothing is hinged: the lower sash only ever
    slides up (author ruling 2026-10-27). Placeholder until E2's windows replace it."""
    y = SASH_SET
    fr = 0.075
    WOOD, GLASS, CURTAIN = 0, 1, 2
    b.box(x - hw, x + hw, y, y + 0.08, sill, sill + fr, mat=WOOD, bevel=0.004)
    b.box(x - hw, x + hw, y, y + 0.08, top - fr, top, mat=WOOD, bevel=0.004)
    b.box(x - hw, x - hw + fr, y, y + 0.15, sill, top, mat=WOOD, bevel=0.004)
    b.box(x + hw - fr, x + hw, y, y + 0.15, sill, top, mat=WOOD, bevel=0.004)
    tz = sill + (top - sill) * 0.66
    b.box(x - hw, x + hw, y - 0.01, y + 0.06, tz - 0.035, tz + 0.035, mat=WOOD, bevel=0.004)
    b.box(x - 0.028, x + 0.028, y, y + 0.06, tz + 0.035, top - fr, mat=WOOD, bevel=0.003)
    b.box(x - hw + fr, x + hw - fr, y + 0.025, y + 0.035, tz + 0.035, top - fr, mat=GLASS, bevel=0.0)
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
    sheer(b, sx0, sx1, y + 0.2, sill + fr + 0.02, top - fr, CURTAIN)
    b.box(x - hw - 0.1, x + hw + 0.1, WALL_T + 0.01, WALL_T + 0.03, sill - 0.1, top + 0.1, mat=3, bevel=0.0)


def surround(b, w):
    """Clay massing of a window's stone trim (E2 replaces with the carved Baroque trim):
    architrave band, sill slab with drip, apron with corbels, hood and pediment mass."""
    x, hw = w["cx"], w["w"] / 2
    band, p = SUR["band"], SUR["proud"]
    sill, top = w["sill"], w.get("head")
    sx0, sx1 = w["slab"]["x"]
    sp = w["slab"]["proud"]
    if w["kind"] in ("sill",):
        b.box(sx0, sx1, -sp, 0.0, sill - 0.13, sill, bevel=0.012)
        b.box(sx0 + 0.04, sx1 - 0.04, -sp + 0.03, -sp + 0.11, sill - 0.17, sill - 0.13, bevel=0.006)
        if "apron_z" in w:
            a0, a1 = w["apron_z"]
            b.box(x - hw, x + hw, -0.06, 0.02, a0, a1, bevel=0.008)
            for s in (-1, 1):
                corbel(b, x + s * (hw + 0.1), sill - 0.13, 0.0, w=0.16, depth=sp - 0.04,
                       h=sill - 0.13 - a0)
    elif w["kind"] in ("balcony", "arched"):
        t = 0.17
        b.box(sx0, sx1, -sp, 0.0, sill - t, sill, bevel=0.012)                        # slab
        b.box(sx0 - 0.03, sx1 + 0.03, -sp - 0.03, -sp + 0.06, sill - t - 0.04, sill - t + 0.03,
              bevel=0.01)                                                              # nosing
        for s in (-1, 1):
            corbel(b, (sx0 + sx1) / 2 + s * ((sx1 - sx0) / 2 - 0.22), sill - t - 0.04, 0.0, w=0.18,
                   depth=sp - 0.06, h=0.42)
    if w["kind"] == "arched":
        r = w["crown"] - w["springing"]
        cz = w["springing"]
        fa = SUR["fascia"]
        for sx in (-1, 1):
            xa, xb = sorted((x + sx * (hw + 0.003), x + sx * (hw + fa)))
            b.box(xa, xb, -SUR["fascia_proud"], 0.02, sill, cz, bevel=0.006)          # fascia
            xa, xb = sorted((x + sx * (hw + fa), x + sx * (hw + fa + 0.22)))
            b.box(xa, xb, -0.09, 0.02, sill, cz, bevel=0.01)
            xa, xb = sorted((x + sx * (hw - 0.003), x + sx * (hw - 0.023)))
            b.box(xa, xb, 0.003, w.get("reveal", SASH_SET), sill + 0.003, cz, bevel=0.0)   # lining
        # Elliptical head (v2): every band follows the opening's half-ellipse (hw x r), offset out.
        ring(b, x, cz, hw + 0.003, hw + fa, -SUR["fascia_proud"], 0.02, n=36, bevel=0.0,
             rz0=r + 0.003, rz1=r + fa)                                                  # fascia
        ring(b, x, cz, hw + fa, hw + fa + 0.22, -0.09, 0.02, n=36, bevel=0.0,
             rz0=r + fa, rz1=r + fa + 0.22)                                              # moulding
        ring(b, x, cz, hw + fa + 0.22, hw + fa + 0.32, -0.05, 0.02, n=36, bevel=0.0,
             rz0=r + fa + 0.22, rz1=r + fa + 0.32)
        ring(b, x, cz, hw - 0.023, hw - 0.003, 0.003, w.get("reveal", SASH_SET), n=24, bevel=0.0,
             rz0=r - 0.023, rz1=r - 0.003)                                               # lining
        b.prism([(x - 0.12, cz + r - 0.03), (x + 0.12, cz + r - 0.03), (x + 0.16, cz + r + 0.44),
                 (x - 0.16, cz + r + 0.44)], -0.2, 0.02, bevel=0.01)                   # keystone
        return
    fa = SUR["fascia"]
    frame(b, x, sill, top + 0.003, hw + 0.003, fa - 0.003, -SUR["fascia_proud"], 0.02, 0.006)  # fascia
    frame(b, x, sill, top + fa, hw + fa, band, -p, 0.02, 0.008)                    # architrave
    frame(b, x, sill, top + fa, hw + fa, 0.04, -p - 0.04, -p + 0.005, 0.006)       # bead
    for sx in (-1, 1):                                                                  # lining
        xa, xb = sorted((x + sx * (hw - 0.003), x + sx * (hw - 0.023)))
        b.box(xa, xb, 0.003, SASH_SET, sill + 0.003, top - 0.003, bevel=0.0)
    b.box(x - hw + 0.003, x + hw - 0.003, 0.003, SASH_SET, top - 0.023, top - 0.003, bevel=0.0)
    hz = top + fa + band
    b.box(x - hw - fa - band - 0.06, x + hw + fa + band + 0.06, -0.16, 0.02, hz, hz + 0.16, bevel=0.01)  # hood
    if "pediment_z" in w:
        p0, p1 = w["pediment_z"]
        pw = w["pediment_w"] / 2
        b.prism([(x - pw, p0), (x + pw, p0), (x + pw * 0.8, p0 + (p1 - p0) * 0.7), (x, p1),
                 (x - pw * 0.8, p0 + (p1 - p0) * 0.7)], -0.16, 0.02, bevel=0.01)


def ground_window_glazing(b_frame, w, x0, x1, crown, spring):
    """Arched window frame (elliptical head), transom, fanlight tracery, glass, sheer. Placeholder
    for E2, sized to the v2 frame outline at the reveal (x0..x1, crown, springing)."""
    x, hw, sill = (x0 + x1) / 2, (x1 - x0) / 2, w["sill"]
    r = crown - spring
    WOOD, GLASS, CURTAIN = 0, 1, 2
    y, fr = w.get("reveal", SASH_SET), 0.07
    for sx in (-1, 1):
        xa, xb = sorted((x + sx * hw, x + sx * (hw - fr)))
        b_frame.box(xa, xb, y, y + 0.08, sill, spring, mat=WOOD, bevel=0.004)
    b_frame.box(x - hw, x + hw, y, y + 0.08, sill, sill + fr, mat=WOOD, bevel=0.004)
    ring(b_frame, x, spring, hw - fr, hw, y, y + 0.08, mat=WOOD, n=20, bevel=0.003, rz0=r - fr, rz1=r)
    b_frame.box(x - hw, x + hw, y - 0.01, y + 0.08, spring - 0.035, spring + 0.035,
                mat=WOOD, bevel=0.004)
    a_in, r_in = hw - fr, r - fr
    b_frame.box(x - 0.018, x + 0.018, y + 0.01, y + 0.07, spring, spring + r_in, mat=WOOD, bevel=0.0)
    fan = [(x + a_in * math.cos(math.pi * i / 24), spring + 0.035 + (r_in - 0.035) * math.sin(math.pi * i / 24))
           for i in range(25)]
    b_frame.prism(fan, y + 0.035, y + 0.045, mat=GLASS, bevel=0.0)
    b_frame.box(x - 0.025, x + 0.025, y, y + 0.08, sill, spring, mat=WOOD, bevel=0.003)
    b_frame.box(x - hw + fr, x + hw - fr, y + 0.035, y + 0.045, sill + fr,
                spring - 0.035, mat=GLASS, bevel=0.0)
    sheer(b_frame, x - hw + 0.07, x + hw - 0.07, y + 0.14, sill + fr + 0.02, spring - 0.04, CURTAIN)
    b_frame.box(w["cx"] - w["w"] / 2 - 0.1, w["cx"] + w["w"] / 2 + 0.1, WALL_T + 0.01, WALL_T + 0.03,
                sill - 0.1, w["crown"] + 0.1, mat=3, bevel=0.0)


def rail(b_iron, xl, xr, front, face, z0, top_z, step=0.12):
    """Wrought-iron rail on a slab: top and bottom rails, balusters, returns to the wall."""
    r = 0.016
    for z in (z0 + 0.04, top_z - 0.03):
        b_iron.box(xl, xr, front - r, front + r, z - r, z + r, bevel=0.003)
        for xe in (xl, xr):
            b_iron.box(xe - r, xe + r, front, face, z - r, z + r, bevel=0.003)
    b_iron.box(xl - 0.03, xr + 0.03, front - 0.03, front + 0.03, top_z - 0.02, top_z + 0.012, bevel=0.005)
    xb, i = xl, 0
    while xb <= xr + 1e-6:
        b_iron.box(xb - 0.009, xb + 0.009, front - 0.009, front + 0.009, z0 + 0.04, top_z - 0.02, bevel=0.0)
        if i % 2 == 1:
            ring(b_iron, xb + 0.06, z0 + 0.2, 0.04, 0.052, front - 0.008, front + 0.008, n=10, bevel=0.0)
            ring(b_iron, xb - 0.06, z0 + 0.2, 0.04, 0.052, front - 0.008, front + 0.008, n=10, bevel=0.0)
        xb += step
        i += 1


# --------------------------------------------------------------------------- roof

def offset_polygon(poly, dists):
    """Inset a convex CCW (x, y) polygon: edge i (poly[i] -> poly[i+1]) moves inward by dists[i]."""
    n = len(poly)
    lines = []
    for i in range(n):
        a, b = Vector(poly[i]), Vector(poly[(i + 1) % n])
        d = (b - a).normalized()
        nrm = Vector((-d.y, d.x))                      # inward for a CCW polygon
        lines.append((a + nrm * dists[i], d))
    out = []
    for i in range(n):
        p1, d1 = lines[i - 1]
        p2, d2 = lines[i]
        den = d1.x * d2.y - d1.y * d2.x
        t = ((p2.x - p1.x) * d2.y - (p2.y - p1.y) * d2.x) / den
        out.append(tuple(p1 + d1 * t))
    return out


def solid(b, res, mat):
    """Tag a bmesh.ops create_* result as one solid with a material."""
    for f in {f for v in res["verts"] for f in v.link_faces}:
        f.material_index = mat
    return res["verts"]


def cyl(b, x, y, z0, z1, r0, r1, mat, seg=12):
    """Upright (tapered) cylinder from z0 to z1."""
    res = bmesh.ops.create_cone(b.bm, cap_ends=True, cap_tris=False, segments=seg, radius1=r0, radius2=r1,
                                depth=z1 - z0, matrix=Matrix.Translation((x, y, (z0 + z1) / 2)))
    return solid(b, res, mat)


def roll(b, p, q, r, mat, seg=8):
    """Round roll (zinc trim) from p to q."""
    p, q = Vector(p), Vector(q)
    d = q - p
    if d.length < 0.02:
        return None
    rot = d.normalized().to_track_quat("Z", "Y").to_matrix().to_4x4()
    res = bmesh.ops.create_cone(b.bm, cap_ends=True, segments=seg, radius1=r, radius2=r, depth=d.length,
                                matrix=Matrix.Translation((p + q) / 2) @ rot)
    return solid(b, res, mat)


def spear(b, x, y, z, mat, s=1.0):
    """Cresting finial: ball, collar and a four-sided spear point."""
    solid(b, bmesh.ops.create_icosphere(b.bm, subdivisions=1, radius=0.026 * s,
                                        matrix=Matrix.Translation((x, y, z + 0.026 * s))), mat)
    solid(b, bmesh.ops.create_cone(b.bm, cap_ends=True, segments=4, radius1=0.034 * s, radius2=0.0,
                                   depth=0.11 * s, matrix=Matrix.Translation((x, y, z + 0.044 * s + 0.055 * s))
                                   @ Matrix.Rotation(math.radians(45), 4, "Z")), mat)


def bezier2(p0, p1, p2, p3, n):
    out = []
    for i in range(n + 1):
        t = i / n
        a, bb, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t * t, t ** 3
        out.append((a * p0[0] + bb * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + bb * p1[1] + c * p2[1] + d * p3[1]))
    return out


def gable_curve(G, z0):
    """Right half of the gable's top edge, from the post foot up and over to the crown (x>=0):
    post, C-scroll shoulder roll, then a concave-convex sweep rising to the arched crown (sheet crops 09/13)."""
    hw, pt, r = G["half"], G["post_top"], G["scroll_r"]
    pts = [(hw, z0), (hw, pt)]
    cx, cz = hw - r * 0.67, pt + r
    for a in (-40, -10, 20, 50, 80, 110):
        t = math.radians(a)
        pts.append((cx + r * math.cos(t), cz + r * math.sin(t)))
    s0 = pts[-1]
    # Ogee: rises convex off the shoulder, reverses, and runs concave into a slightly pointed apex.
    pts += bezier2(s0, (s0[0] + 0.06, s0[1] + 0.95), (0.5, G["top_z"] - 0.45), (0.0, G["top_z"]), 22)[1:]
    return pts


def offset_curve(pts, d):
    """Offset an open (x, z) polyline by d along its left normal (inward for a curve traced
    right-to-left over the top)."""
    out = []
    n = len(pts)
    for i in range(n):
        a = Vector(pts[max(i - 1, 0)])
        c = Vector(pts[min(i + 1, n - 1)])
        t = (c - a).normalized()
        out.append(tuple(Vector(pts[i]) + Vector((-t.y, t.x)) * d))
    return out


def apex_clamp(outer, inner):
    """Keep an inward offset of the gable's top edge on its own side of the axis near the pointed
    apex (a large offset of the ogee point would cross over and twist the band)."""
    out = []
    for (xo, _), (xi, zi) in zip(outer, inner):
        if xo > 1e-6:
            xi = max(xi, 0.0)
        elif xo < -1e-6:
            xi = min(xi, 0.0)
        else:
            xi = 0.0
        out.append((xi, zi))
    return out


def band_prism(b, outer, inner, y0, y1, mat, bevel=0.0):
    """Ribbon between two matching open polylines, extruded along y, built as one small solid per
    segment: a single n-gon for the whole band mis-tessellates where the inner edge pinches at the
    gable's pointed apex (it filled the arch field and hid the head)."""
    for i in range(len(outer) - 1):
        q = [outer[i], outer[i + 1], inner[i + 1], inner[i]]
        pts = [p for k, p in enumerate(q) if (Vector(p) - Vector(q[k - 1])).length > 1e-4]
        if len(pts) < 3:
            continue
        area = sum(pts[k][0] * pts[(k + 1) % len(pts)][1] - pts[(k + 1) % len(pts)][0] * pts[k][1]
                   for k in range(len(pts)))
        if abs(area) < 1e-7:
            continue
        b.prism(pts, y0, y1, mat=mat, bevel=bevel)


def cresting_run(iron, p0, p1, z, h, bay, skip=None):
    """Iron cresting along p0->p1 (plan points) at height z: rails, scroll circles and spear finials.
    skip(x, y) -> True leaves a gap (the gable)."""
    a, c = Vector((p0[0], p0[1], 0)), Vector((p1[0], p1[1], 0))
    L = (c - a).length
    if L < 0.2:
        return
    d = (c - a) / L
    nb = max(1, round(L / bay))
    step = L / nb
    ang = math.atan2(d.y, d.x)
    loc = Builder()
    # local frame: x along the run, y across (thin), z up; transformed onto the run afterwards
    segs, cur = [], None
    for i in range(nb):
        q = a + d * (step * (i + 0.5))
        ok = not (skip and skip(q.x, q.y))
        if ok and cur is None:
            cur = [i, i]
        elif ok:
            cur[1] = i
        elif cur is not None:
            segs.append(cur)
            cur = None
    if cur is not None:
        segs.append(cur)
    r = 0.016
    for i0, i1 in segs:
        x0, x1 = step * i0, step * (i1 + 1)
        for zz in (z + 0.03, z + h - 0.02):          # rails stop inside the end posts (no coplanar
            loc.box(x0 + 0.012, x1 - 0.012, -r, r, zz - r, zz + r, bevel=0.0)   # tops at corners)
        for k in range(i0, min(i1 + 2, nb)):          # the edge's end post is the next edge's first
            xk = step * k
            loc.box(xk - 0.012, xk + 0.012, -0.012, 0.012, z, z + h + 0.02, bevel=0.0)
            spear(loc, xk, 0.0, z + h + 0.02, 0, s=1.15)
        for k in range(i0, i1 + 1):
            xm = step * (k + 0.5)
            lo, hi = z + 0.03 + r, z + h - 0.02 - r       # rail faces the scrolls hang between
            zc, rr = (lo + hi) / 2, (hi - lo) / 2 + 0.004   # the circle touches both rails
            ring(loc, xm, zc, rr - 0.012, rr, -0.008, 0.008, n=10, bevel=0.0)
            ring(loc, xm, zc, rr - 0.012, rr, -0.008, 0.008, n=10, bevel=0.0, rz0=-(rr - 0.012), rz1=-rr)
            for sx in (-1, 1):   # C-scrolls standing on the bottom rail either side of the circle
                ring(loc, xm + sx * step * 0.36, lo - 0.004, 0.03, 0.042, -0.007, 0.007, n=8, bevel=0.0)
            spear(loc, xm, 0.0, z + h - 0.01, 0, s=0.7)
    iron.absorb(loc, Matrix.Translation((a.x, a.y, 0.0)) @ Matrix.Rotation(ang, 4, "Z"))


def dormer_body(rb, D, M):
    """One dormer body in dormer-local coordinates (x across, y back from the front face, z up from
    the window sill), the asset sheet's form: stone face with pilasters on bases, entablature,
    triangular pediment with a raking cornice and a medallion, stone cheeks, a gabled slate roof.
    E2's dormer window kit (frame, architrave, ledge, rail, flowers) sits in the opening.
    Returns the opening cutter (local Builder)."""
    SL, ST = M
    W, band, mold = D["frame_w"], D["band"], D["mold"]
    o = W / 2 + band + mold                      # E2's architrave outer edge
    xo = D["body_w"] / 2
    hz = D["head"] - D["sill"]
    zb = EAVE1 - D["sill"] - 0.02                # foot: on the eave cornice
    z_ent0 = D["frame_h"] + band + mold + 0.01          # entablature foot (E2 stand-in)
    zt = z_ent0 + 0.12
    ph = max(0.2, D["ridge"] - D["sill"] - zt - 0.06)
    dep = D["body_depth"]
    # face panel (the opening is cut through it) and the stone cheeks
    rb.box(-xo, xo, 0.0, 0.12, zb, zt, mat=ST, bevel=0.0)
    for sx in (-1, 1):
        xa, xb = sorted((sx * (xo - 0.07), sx * xo))
        rb.box(xa, xb, 0.0, dep, zb, zt, mat=ST, bevel=0.006)
        xa, xb = sorted((sx * (o - 0.004), sx * xo))
        rb.box(xa, xb, -0.07, 0.01, zb, z_ent0, mat=ST, bevel=0.006)                         # pilaster
        rb.box(xa - 0.012, xb + 0.012, -0.085, 0.01, zb, zb + 0.08, mat=ST, bevel=0.006)    # base
        rb.box(xa - 0.012, xb + 0.012, -0.085, 0.01, z_ent0 - 0.06, z_ent0, mat=ST, bevel=0.006)  # cap
    rb.box(-xo - 0.03, xo + 0.03, -0.09, 0.12, z_ent0, zt, mat=ST, bevel=0.008)              # entablature
    rb.prism([(-xo, zt), (xo, zt), (0.0, zt + ph * 0.86)], -0.04, 0.12, mat=ST, bevel=0.004)  # tympanum
    for sx in (-1, 1):                                                                        # raking cornice
        a = Vector((sx * (xo + 0.05), zt - 0.005))
        c = Vector((0.0, zt + ph))
        t = (c - a).normalized()
        nrm = Vector((-t.y, t.x)) if sx > 0 else Vector((t.y, -t.x))
        if nrm.y < 0:
            nrm = -nrm
        q = [a, c + t * 0.02, c + t * 0.02 + nrm * 0.10, a + nrm * 0.10]
        rb.prism([tuple(p) for p in q], -0.10, 0.12, mat=ST, bevel=0.004)
    medal = [(0.075 * math.cos(math.tau * i / 16), zt + ph * 0.36 + 0.075 * math.sin(math.tau * i / 16))
             for i in range(16)]
    rb.prism(medal, -0.075, -0.035, mat=ST, bevel=0.006)                                      # medallion
    for sx in (-1, 1):                                                                        # slate roof
        a = Vector((sx * (xo + 0.07), zt - 0.03))
        c = Vector((0.0, zt + ph + 0.03))
        t = (c - a).normalized()
        up = Vector((-t.y, t.x)) if sx > 0 else Vector((t.y, -t.x))
        if up.y < 0:
            up = -up
        q = [a, c, c + up * 0.05, a + up * 0.05]
        rb.prism([tuple(p) for p in q], 0.10, dep + 0.05, mat=SL, bevel=0.0)
    rb.prism([(-xo + 0.06, zt), (xo - 0.06, zt), (0.0, zt + ph * 0.9)], 0.10, dep, mat=ST, bevel=0.0)  # roof fill
    ow = D["opening_w"] / 2
    cut = Builder()
    cut.box(-ow, ow, -0.5, 0.95, 0.0, hz, bevel=0.0)
    return cut


def build_roof():
    """Asset-sheet roof (crops 09, 10, 12, 13): bell-cast slate mansard with a flatter upper
    slope, the tall stone gable (C-scroll shoulders, arched crown, moulded edge, slate coping)
    with a placeholder for the carved head, four stone chimney stacks with clay pots, the
    dormer bodies and the iron cresting. Returns (roof_builder [slate, stone, clay],
    iron_builder, dormer_cutters, head_builder)."""
    RF = FA["roof"]
    MS = RF["mansard"]
    foot = [(X_LEFT, 0.0), (X_RIGHT, 0.0), (X_RIGHT, DEPTH), (CB_FAR.x, DEPTH), (CB_FAR.x, CB_FAR.y)]
    s, top_s = RF["mansard_setback"], RF["top_setback"]
    z0, z1 = EAVE1, RF["mansard_top_z"]
    z2 = z1 + MS["upper_rise"]
    roof = Builder()
    SLATE, STONE, CLAY = 0, 1, 2
    # Bell-cast lower slope: the inset grows fastest at the eave (the kick) and the slope stiffens
    # upward; then the flatter upper slope to the ridge.
    rings = []
    n = MS["rings"]
    for i in range(n + 1):
        t = i / n
        f = MS["bell"] * t + (1 - MS["bell"]) * (1 - (1 - t) ** 2)
        d = -MS["eave_kick"] + (s + MS["eave_kick"]) * f
        rings.append([(x, y, z0 + (z1 - z0) * t) for x, y in offset_polygon(foot, [d] * 5)])
    rings.append([(x, y, z2) for x, y in offset_polygon(foot, [top_s] * 5)])
    for ra, rb_ in zip(rings, rings[1:]):
        roof.loft(ra, rb_, mat=SLATE, cap=False)
    vb = [roof.bm.verts.new(p) for p in rings[0]]
    vt = [roof.bm.verts.new(p) for p in rings[-1]]
    roof.bm.faces.new(vb[::-1])
    roof.bm.faces.new(vt)
    bmesh.ops.remove_doubles(roof.bm, verts=roof.bm.verts, dist=1e-5)
    bmesh.ops.recalc_face_normals(roof.bm, faces=roof.bm.faces)
    for f in roof.bm.faces:
        f.material_index = SLATE
    # Light zinc rolls on the hips, the curb and the ridge (asset sheet). Their own object: kept
    # out of the dormer-opening boolean, which would slice the slates along every roll.
    zinc = Builder()
    for i in range(5):
        for j in range(len(rings) - 1):                                   # hips
            roll(zinc, rings[j][i], rings[j + 1][i], 0.035, 0)
        for rr_, rad in ((rings[n], 0.04), (rings[-1], 0.03)):           # curb, ridge
            roll(zinc, rr_[i], rr_[(i + 1) % 5], rad, 0)

    # Dormer bodies (front pair and the side one), cutters for their openings.
    D = dict(RF["dormer"])
    cutters = []
    for dm in RF["dormers"]:
        loc = Builder()
        cut = dormer_body(loc, D, (SLATE, STONE))
        m = Matrix.Translation((dm["cx"], D["proud_of_wall"], D["sill"]))
        roof.absorb(loc, m)
        c2 = Builder()
        c2.absorb(cut, m)
        cutters.append(cutter_obj(f"aa_cut_{dm['id']}", c2))
    sd = RF["side_dormer"]
    loc = Builder()
    cut = dormer_body(loc, D, (SLATE, STONE))
    m = SIDE_MAT @ Matrix.Translation((sd["u"], D["proud_of_wall"], D["sill"]))
    roof.absorb(loc, m)
    c2 = Builder()
    c2.absorb(cut, m)
    cutters.append(cutter_obj(f"aa_cut_{sd['id']}", c2))

    # Central gable: stone panel in the wall plane, moulded edge band and slate coping following
    # the scrolled outline, an inner bead, pilaster posts with caps.
    G = RF["gable"]
    orn = Builder()       # gable and chimneys: their own object, outside the dormer boolean
    right = gable_curve(G, z0)                    # right foot -> post top -> scroll -> crown
    left = [(-x, z) for x, z in right]            # left foot -> ... -> crown
    outline = left + right[::-1][1:]              # left foot -> crown -> right foot
    orn.prism(outline, -0.04, 0.9, mat=STONE, bevel=0.0)
    top = outline[1:-1]                           # left post top -> crown -> right post top
    inner = apex_clamp(top, offset_curve(top[::-1], G["band"])[::-1])
    band_prism(orn, top, inner, -0.04 - G["band_proud"], -0.03, STONE)
    cop_o = offset_curve(top[::-1], -G["coping"])[::-1]
    band_prism(orn, cop_o, top, -0.06 - G["band_proud"], 0.9, SLATE)
    # thick moulded frame: a second, less proud step inside the band, then a bead
    step_i = apex_clamp(top, offset_curve(top[::-1], G["band"] + 0.08)[::-1])
    band_prism(orn, inner, step_i, -0.04 - G["band_proud"] * 0.55, -0.03, STONE)
    arch = [p for p in top if p[1] > G["post_top"] + G["scroll_r"] * 1.5]
    bead_o = offset_curve(arch[::-1], G["band"] + 0.12)[::-1]
    bead_i = offset_curve(arch[::-1], G["band"] + 0.17)[::-1]
    band_prism(orn, bead_o, bead_i, -0.09, -0.03, STONE)
    # carved spandrel ornament (clean architectural scrolls; the carving pass can replace them)
    for sx in (-1, 1):
        cx, cz = sx * G["spandrel_x"], G["spandrel_z"]
        ring(orn, cx, cz, 0.15, 0.19, -0.1, -0.03, mat=STONE, n=14, bevel=0.0)
        ring(orn, cx - sx * 0.05, cz, 0.06, 0.1, -0.1, -0.03, mat=STONE, n=10, bevel=0.0, rz0=-0.06, rz1=-0.1)
        ring(orn, cx - sx * 0.02, cz - 0.02, 0.012, 0.045, -0.11, -0.03, mat=STONE, n=8, bevel=0.0)
        # (the leaf tip that used to sit here poked past the ogee outline at the shoulder)
    hw = G["half"]
    for sx in (-1, 1):
        xa, xb = sorted((sx * hw, sx * (hw - G["post_w"])))
        orn.box(xa - 0.02, xb + 0.02, -0.14, 0.0, z0, G["post_top"] - 0.1, mat=STONE, bevel=0.01)
        orn.box(xa - 0.04, xb + 0.04, -0.17, 0.0, G["post_top"] - 0.1, G["post_top"], mat=STONE, bevel=0.01)
    orn.box(-0.06, 0.06, -0.16, 0.05, G["top_z"] - 0.05, G["top_z"] + 0.12, mat=STONE, bevel=0.02)  # finial base
    cyl(orn, 0.0, -0.06, G["top_z"] + 0.12, G["top_z"] + 0.36, 0.05, 0.0, STONE, seg=8)              # finial
    # Carved head: a marked placeholder relief (replace with the Tripo carving).
    head = Builder()
    h0, h1 = G["head_z"]
    hc = Vector((0.0, -0.12, (h0 + h1) / 2))       # set high in the arch, above the ridge line
    res = bmesh.ops.create_uvsphere(head.bm, u_segments=24, v_segments=14, radius=1.0,
                                    matrix=Matrix.Translation(hc) @ Matrix.Diagonal((0.34, 0.16, (h1 - h0) / 2, 1.0)))
    solid(head, res, 0)
    rx, rz = 0.5, (h1 - h0) / 2 + 0.1
    plate = [(rx * math.cos(math.tau * i / 28), hc.z + rz * math.sin(math.tau * i / 28)) for i in range(28)]
    head.prism(plate, -0.1, -0.03, mat=0, bevel=0.01)

    # Chimney stacks with clay pots.
    for ch in RF["chimneys"]:
        w2, d2 = ch["w"] / 2, ch["d"] / 2
        x, y = ch["x"], ch["y"]
        orn.box(x - w2, x + w2, y - d2, y + d2, z0 + 0.5, ch["top"] - 0.16, mat=STONE, bevel=0.01)
        orn.box(x - w2 - 0.05, x + w2 + 0.05, y - d2 - 0.05, y + d2 + 0.05, ch["top"] - 0.16, ch["top"] - 0.04,
                 mat=STONE, bevel=0.012)
        orn.box(x - w2 + 0.03, x + w2 - 0.03, y - d2 + 0.03, y + d2 - 0.03, ch["top"] - 0.04, ch["top"],
                 mat=STONE, bevel=0.008)
        npots = ch["pots"]
        for k in range(npots):
            px = x + (k - (npots - 1) / 2) * min(0.26, ch["w"] / max(npots, 1))
            cyl(orn, px, y, ch["top"], ch["top"] + 0.06, 0.11, 0.11, CLAY)
            cyl(orn, px, y, ch["top"] + 0.06, ch["top"] + ch["pot_h"], 0.1, 0.082, CLAY)
            cyl(orn, px, y, ch["top"] + ch["pot_h"], ch["top"] + ch["pot_h"] + 0.04, 0.095, 0.095, CLAY)

    # Iron cresting round the ridge (upper-slope top edge), gapped behind the gable.
    iron = Builder()
    CR = RF["cresting"]
    ridge = [(x, y) for x, y, _ in rings[-1]]
    gap = lambda x, y: abs(x) < G["half"] + 0.1 and y < 2.0      # noqa: E731
    for i in range(len(ridge)):
        cresting_run(iron, ridge[i], ridge[(i + 1) % len(ridge)], z2, CR["h"], CR["bay"], skip=gap)
    return roof, iron, cutters, head, zinc, orn


# --------------------------------------------------------------------------- arch hero seats

def seat_marquee():
    """Size the marquee (and its tagline panel) to the bible and hang it on the arch: uniform
    scale about its bottom edge, then drop it to the bible's slogan line. Idempotent."""
    co = [v.co for v in bpy.data.objects["aa_arch_hero_marquee"].data.vertices]
    k = MARQUEE_W / (max(c.x for c in co) - min(c.x for c in co))
    y_back, z_foot = max(c.y for c in co), min(c.z for c in co)
    if abs(k - 1) < 1e-3 and abs(MARQUEE_BACK - y_back) < 1e-3 and abs(z_foot - MARQUEE_FOOT) < 1e-3:
        return 0.0
    m = (Matrix.Translation((0, MARQUEE_BACK, MARQUEE_FOOT)) @ Matrix.Scale(k, 4)
         @ Matrix.Translation((0, -y_back, -z_foot)))
    for name in MARQUEE_PARTS:
        me = bpy.data.objects[name].data
        me.transform(m)
        me.update()
    return round(k, 3)


GENTLEMAN_PARTS = ("aa_arch_hero_gentleman", "aa_arch_hero_gentleman_hardware")
GENTLEMAN_BASE = AR["keystone"].get("head_base_z", 4.60)


def seat_gentleman():
    """The mascaron sits on the keystone at the bible's height. Idempotent; returns the lift."""
    bust = bpy.data.objects["aa_arch_hero_gentleman"]
    dz = GENTLEMAN_BASE - min(v.co.z for v in bust.data.vertices)
    if abs(dz) < 1e-3:
        return 0.0
    for name in GENTLEMAN_PARTS:
        me = bpy.data.objects[name].data
        me.transform(Matrix.Translation((0, 0, dz)))
        me.update()
    return round(dz, 3)


DOOR_PARTS = ("aa_arch_hero_door_leaf_l", "aa_arch_hero_door_leaf_r")


def seat_doors():
    """Temporary (E3 replaces): scale the Tripo leaves to the bible's doorway height and set
    them in the bible's inner-door positions. Idempotent."""
    st = AR["doors"]
    out = {}
    for name, xc in zip(DOOR_PARTS, st["centers_x"]):
        me = bpy.data.objects[name].data
        co = [v.co for v in me.vertices]
        lo = Vector([min(c[i] for c in co) for i in range(3)])
        hi = Vector([max(c[i] for c in co) for i in range(3)])
        k = st["height"] / (hi.z - lo.z)
        cx = (lo.x + hi.x) / 2
        if abs(k - 1) < 1e-3 and abs(cx - xc) < 1e-3 and abs(lo.z - st["z0"]) < 1e-3:
            out[name] = 0.0
            continue
        m = (Matrix.Translation((xc, lo.y, st["z0"])) @ Matrix.Scale(k, 4)
             @ Matrix.Translation((-cx, -lo.y, -lo.z)))
        me.transform(m)
        me.update()
        out[name] = round(k, 3)
    return out


# --------------------------------------------------------------------------- main

SOFTEN = {"aa_shell_facade_mouldings": 0.006}


def shell_coll():
    return bpy.data.collections["aa_shell_facade"]


def replace_mesh(obj_name, builder, mats, coll_name="aa_arch_hero"):
    obj = bpy.data.objects.get(obj_name)
    coll = obj.users_collection[0] if obj else bpy.data.collections[coll_name]
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
    coll = shell_coll()
    for o in list(coll.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    stone = base_material("m_aa_limestone_weathered", (0.72, 0.64, 0.52))
    trim = base_material("m_aa_trim_weathered", (0.78, 0.71, 0.6))
    wood = material("m_aa_window_timber", (0.10, 0.055, 0.03), rough=0.55)
    glass = material("m_aa_window_glass", (0.10, 0.13, 0.13), rough=0.02, alpha=0.42)
    curtain = material("m_aa_window_curtain", (0.82, 0.8, 0.74), rough=0.9, alpha=0.8)
    dark = material("m_aa_interior_void", (0.01, 0.012, 0.012), rough=1.0)
    slate = slate_material()
    zinc = material("m_aa_roof_zinc", (0.42, 0.44, 0.47), rough=0.45, metallic=0.35)
    iron = material("m_aa_wrought_iron", (0.025, 0.025, 0.027), rough=0.45, metallic=0.6)
    clay = material("m_aa_chimney_pot", (0.42, 0.13, 0.06), rough=0.75)

    walls = build_walls()
    made = {"walls": len(walls.data.polygons)}
    stone_b, frame_b, iron_b = Builder(), Builder(), Builder()
    for k, w in WINDOWS.items():
        if has_kit(k):
            made.setdefault("e2_kits", []).append(E2_KIT[k])
            continue
        surround(stone_b, w)
        x0, x1, top, spring = frame_rect(w)
        lining_board(stone_b, w, x0, x1, top, spring)
        if w["kind"] == "arched":
            ground_window_glazing(frame_b, w, x0, x1, top, spring)
            sx0, sx1 = w["slab"]["x"]
            front = -w["slab"]["proud"] + 0.05
            rail(iron_b, sx0 + 0.06, sx1 - 0.06, front, 0.0, w["sill"], w["sill"] + 0.42, step=0.13)
        else:
            sash_window(frame_b, (x0 + x1) / 2, w["sill"], top, (x1 - x0) / 2, w.get("open", 0.0))
            if w["kind"] == "balcony":
                sx0, sx1 = w["slab"]["x"]
                front = -w["slab"]["proud"] + 0.05
                rail(iron_b, sx0 + 0.04, sx1 - 0.04, front, 0.0, w["sill"], w["rail_top"])
    frame_b.absorb(cant_glazing())
    build_side_right(stone_b, frame_b)
    roof_b, crest_b, dormer_cutters, head_b, zinc_b, orn_b = build_roof()
    iron_b.absorb(crest_b)
    if "aa_roof_gable_head" in bpy.data.collections:      # E2's carving is integrated
        head_b.bm.free()
        made["gable_head"] = "kit aa_roof_gable_head"
    else:
        head = head_b.to_object("aa_shell_facade_roof_gable_head_PLACEHOLDER", [trim], coll)
        head["replace_with"] = "Tripo carving: the gable's carved head relief (asset sheet crops 09/13)"
        made["gable_head"] = "placeholder"

    for name, builder, mats in (
            ("aa_shell_facade_mouldings", build_mouldings(), [trim]),
            ("aa_shell_facade_corner_bay", build_corner_bay(), [trim]),
            ("aa_shell_facade_window_surrounds", stone_b, [trim]),
            ("aa_shell_facade_sash_windows", frame_b, [wood, glass, curtain, dark]),
            ("aa_shell_facade_ironwork", iron_b, [iron]),
            ("aa_shell_facade_roof_zinc", zinc_b, [zinc]),
            ("aa_shell_facade_roof_gable_chimneys", orn_b, [slate, trim, clay]),
            ("aa_shell_facade_roof", roof_b, [slate, trim, clay])):
        o = builder.to_object(name, mats, coll)
        made[name] = len(o.data.polygons)
        if name in SOFTEN:
            soften(o, SOFTEN[name])
    roof = bpy.data.objects["aa_shell_facade_roof"]
    for cu in dormer_cutters:
        mod = roof.modifiers.new(cu.name, "BOOLEAN")
        mod.operation, mod.solver, mod.use_self, mod.use_hole_tolerant = "DIFFERENCE", "EXACT", True, True
        mod.object = cu
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(roof.evaluated_get(dg))
    old = roof.data
    roof.modifiers.clear()
    roof.data = me
    bpy.data.meshes.remove(old)
    me.name = "aa_shell_facade_roof"
    for poly in me.polygons:                      # slate courses read faceted; no smoothing streaks
        if poly.material_index == 0:
            poly.use_smooth = False
    for cu in dormer_cutters:
        bpy.data.objects.remove(cu, do_unlink=True)
    void = Builder() if "aa_e3_interior_set" not in bpy.data.collections else None
    # Dark backstop just in front of the back wall's inner face (DEPTH - BACK_T); E3's interior
    # set (interfaces v2: door line 0.34 + 3.40) stays in front of it.
    if void is not None:                  # E3's interior set replaces the backstop
        void.box(JAMB_L - 0.3, JAMB_R + 0.3, ARCH_DEPTH - 0.005, ARCH_DEPTH, 0.0,
                 ARCH_SPRING + ARCH_RISE + 0.3, bevel=0.0)
        void.to_object("aa_shell_facade_interior_void", [dark], coll)
    soften(walls, 0.01)
    av, pl = build_entrance()
    replace_mesh("aa_arch_hero_archivolt", av, [trim])
    replace_mesh("aa_arch_hero_plinths", pl, [trim])
    # v2: no cartouche/keystone block; the bible's head (E4) sits in front of the crown.
    cart = bpy.data.objects.get("aa_arch_hero_cartouche")
    if cart is not None:
        old = cart.data
        bpy.data.objects.remove(cart, do_unlink=True)
        if old is not None and old.users == 0:
            bpy.data.meshes.remove(old)
        made["cartouche"] = "removed"
    made["gentleman_lift"] = seat_gentleman()
    made["marquee_scale"] = seat_marquee()
    made["doors"] = seat_doors()
    return made


if __name__ == "__main__" or "AA_RUN" in globals():
    result = main()
    print(result)
