"""Build E5 (stone + peeling plaster surface, the conformed mural decal) into wip/E5_surface.blend. Re-runnable.

  blender -b --factory-startup --python e5_build.py -- [--no-save]

* Appends mason's shell READ-ONLY (bpy.data.libraries.load, link=False) from aa_exterior.blend: nothing is
  ever written back to it. Re-run after mason changes the shell; the decal re-conforms.
* Stone: the author's seamless limestone (references/Exterior/texture.jpg) box-projected by face direction in
  world space (reveals and returns don't smear), under the procedural peeling-plaster layer (node group
  E5_PeelingPlaster: amount, scale, crevice width, ground band, right-pillar band, seed, all exposed for the
  author to tune). Applied to the appended stone objects in this wip (mason owns the shell).
* Mural: aa_kit/aa_e5_mural/aa_e5_mural_decal, a heightfield grid laid ON the stone (raycast onto mason's
  surfaces, 2 mm proud), only where the mural has paint, wrapping mouldings and window surrounds; UVs map the
  facade-space mural sheet (e5_mural.py). It peels with the plaster (same node group).
* Context (not kit): E3 marquee + doorway and E4 keystone/conduits/pipes/plaque appended from their wips.
"""
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import e5_sheet as MU  # noqa: E402

REPO = HERE.parents[4]
ASSET = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade"
MAIN = ASSET / "blender/aa_exterior.blend"
E3WIP = ASSET / "blender/wip/E3_entrance.blend"
E4WIP = ASSET / "blender/wip/E4_keystone_conduits.blend"
WIP = ASSET / "blender/wip/E5_surface.blend"
TEX = ASSET / "textures/e5_surface"
STONE_TEX = ASSET / "references/Exterior/texture.jpg"
STONE = ["aa_shell_facade_walls", "aa_shell_facade_mouldings", "aa_shell_facade_window_surrounds",
         "aa_shell_facade_corner_bay", "aa_arch_hero_archivolt", "aa_arch_hero_plinths"]
SHELL_OTHER = ["aa_shell_facade_sash_windows", "aa_shell_facade_ironwork", "aa_shell_facade_roof",
               "aa_shell_facade_interior_void"]
TILE_M = 1.6            # metres covered by one repeat of texture.jpg
DECAL_STEP = 0.025      # decal grid spacing (m)
DECAL_LIFT = 0.002


def coll(name, parent=None):
    c = bpy.data.collections.get(name) or bpy.data.collections.new(name)
    p = parent or bpy.context.scene.collection
    if c.name not in [x.name for x in p.children]:
        p.children.link(c)
    return c


# =========================================================================================
# peeling-plaster node group (shared by stone and mural)
# =========================================================================================
def peel_group():
    """Organic peeling: thresholded, domain-warped fractal noise (torn lobes, no polygon edges), small loose
    flakes and plaster islands, a raised lip and a thin dark shadow on the torn edge. Coverage is driven almost
    entirely by the Zones mask (traced off the bible) plus a light street band and right-pillar band."""
    ng = bpy.data.node_groups.get("E5_PeelingPlaster")
    if ng:
        bpy.data.node_groups.remove(ng)
    ng = bpy.data.node_groups.new("E5_PeelingPlaster", "ShaderNodeTree")
    I = ng.interface

    def inp(name, default, lo=-1e4, hi=1e4):
        sk = I.new_socket(name, in_out="INPUT", socket_type="NodeSocketFloat")
        sk.default_value, sk.min_value, sk.max_value = default, lo, hi
    I.new_socket("Position", in_out="INPUT", socket_type="NodeSocketVector")
    inp("Amount", 0.0, 0, 1)               # global coverage on top of the zones (bible: plaster mostly intact)
    inp("Scale", 2.4, 0.1, 50)             # lobe frequency per metre
    inp("Edge", 0.012, 0.001, 0.1)         # lip / shadow width (noise units)
    inp("Ground Band", 1.2, 0, 6)          # metres above the street with extra peeling
    inp("Ground Weight", 0.3, 0, 1)
    inp("Pillar X", 2.35, -10, 10)         # x beyond which the right pillar peels more
    inp("Pillar Weight", 0.35, 0, 1)
    inp("Seed", 0.0, 0, 100)
    inp("Zones", 0.0, 0, 1)                # peel-zones mask (e5_peel_zones.png, traced off the bible)
    inp("Zone Weight", 1.4, 0, 3)
    for n in ("Peel", "Crevice Mask", "Height", "Mask", "Lip"):
        I.new_socket(n, in_out="OUTPUT", socket_type="NodeSocketFloat")
    nt = ng.nodes
    L = ng.links.new
    gi, go = nt.new("NodeGroupInput"), nt.new("NodeGroupOutput")

    def m(op, a=None, b=None, v1=None, v2=None, c=None, v3=None):
        n = nt.new("ShaderNodeMath")
        n.operation = op
        for k, (x, v) in enumerate(((a, v1), (b, v2), (c, v3))):
            if x is not None:
                L(x, n.inputs[k])
            elif v is not None:
                n.inputs[k].default_value = v
        return n.outputs[0]

    def noise(vec, scale_sock=None, scale=1.0, detail=6.0, rough=0.6):
        n = nt.new("ShaderNodeTexNoise")
        n.inputs["Detail"].default_value = detail
        n.inputs["Roughness"].default_value = rough
        L(vec, n.inputs["Vector"])
        if scale_sock is not None:
            L(scale_sock, n.inputs["Scale"])
        else:
            n.inputs["Scale"].default_value = scale
        return n
    seedv = nt.new("ShaderNodeCombineXYZ")
    L(gi.outputs["Seed"], seedv.inputs[0])
    L(gi.outputs["Seed"], seedv.inputs[1])
    p0 = nt.new("ShaderNodeVectorMath")
    p0.operation = "ADD"
    L(gi.outputs["Position"], p0.inputs[0])
    L(seedv.outputs[0], p0.inputs[1])
    warp = noise(p0.outputs[0], scale=0.9, detail=4)
    wv = nt.new("ShaderNodeVectorMath")
    wv.operation = "MULTIPLY_ADD"
    L(warp.outputs["Color"], wv.inputs[0])
    wv.inputs[1].default_value = (0.35, 0.35, 0.35)
    L(p0.outputs[0], wv.inputs[2])
    n1 = noise(wv.outputs[0], gi.outputs["Scale"], detail=12, rough=0.62)
    fl = noise(wv.outputs[0], scale=26, detail=4, rough=0.5)           # small loose flakes / islands
    # coverage mask
    xyz = nt.new("ShaderNodeSeparateXYZ")
    L(gi.outputs["Position"], xyz.inputs[0])
    gb = m("MAXIMUM", m("SUBTRACT", None, m("DIVIDE", xyz.outputs["Z"], gi.outputs["Ground Band"]), v1=1.0), None, v2=0.0)
    pl = m("MINIMUM", m("MAXIMUM", m("MULTIPLY", m("SUBTRACT", xyz.outputs["X"], gi.outputs["Pillar X"]), None, v2=3.0),
                        None, v2=0.0), None, v2=1.0)
    mask = m("ADD", gi.outputs["Amount"], m("MULTIPLY", gb, gi.outputs["Ground Weight"]))
    mask = m("ADD", mask, m("MULTIPLY", pl, gi.outputs["Pillar Weight"]))
    mask = m("ADD", mask, m("MULTIPLY", gi.outputs["Zones"], gi.outputs["Zone Weight"]))
    mask = m("MINIMUM", mask, None, v2=1.0)
    # threshold: mask 0 -> almost nothing peels; mask 1 -> most of it, plaster islands left
    t = m("MULTIPLY_ADD", mask, None, v2=-0.38, c=None, v3=0.76)
    t_hi = m("ADD", t, gi.outputs["Edge"])
    peel = nt.new("ShaderNodeMapRange")
    peel.interpolation_type = "SMOOTHSTEP"
    L(n1.outputs["Fac"], peel.inputs["Value"])
    L(t, peel.inputs["From Min"])
    L(t_hi, peel.inputs["From Max"])
    isl = nt.new("ShaderNodeMapRange")                                  # plaster islands inside the peel
    isl.interpolation_type = "SMOOTHSTEP"
    L(fl.outputs["Fac"], isl.inputs["Value"])
    isl.inputs["From Min"].default_value = 0.64
    isl.inputs["From Max"].default_value = 0.67
    pk = m("MULTIPLY", peel.outputs["Result"], m("SUBTRACT", None, isl.outputs["Result"], v1=1.0))
    # torn edge: lip just outside the peel (raised, lighter), thin dark shadow just inside it
    t_lo = m("SUBTRACT", t, m("MULTIPLY", gi.outputs["Edge"], None, v2=2.5))
    lip = nt.new("ShaderNodeMapRange")
    lip.interpolation_type = "SMOOTHSTEP"
    L(n1.outputs["Fac"], lip.inputs["Value"])
    L(t_lo, lip.inputs["From Min"])
    L(t, lip.inputs["From Max"])
    lipv = m("MAXIMUM", m("SUBTRACT", lip.outputs["Result"], peel.outputs["Result"]), None, v2=0.0)
    shad = m("MULTIPLY", peel.outputs["Result"], m("SUBTRACT", None, peel.outputs["Result"], v1=1.0))
    shad = m("MINIMUM", m("MULTIPLY", shad, None, v2=4.0), None, v2=1.0)
    height = m("ADD", m("SUBTRACT", None, pk, v1=1.0), m("MULTIPLY", lipv, None, v2=0.35))
    L(pk, go.inputs["Peel"])
    L(shad, go.inputs["Crevice Mask"])
    L(height, go.inputs["Height"])
    L(mask, go.inputs["Mask"])
    L(lipv, go.inputs["Lip"])
    return ng


def lin(r, g, b):
    c = lambda v: (v / 255) / 12.92 if v / 255 <= 0.04045 else (((v / 255) + 0.055) / 1.055) ** 2.4
    return (c(r), c(g), c(b), 1.0)


def zones_node(nt, geo):
    """Sample e5_peel_zones.png by facade position (x, z)."""
    L = nt.links.new
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    L(geo.outputs["Position"], sep.inputs[0])
    comb = nt.nodes.new("ShaderNodeCombineXYZ")
    for comp, lo, hi, k in (("X", MU.ZONE_X0, MU.ZONE_X1, 0), ("Z", MU.ZONE_Z0, MU.ZONE_Z1, 1)):
        mr = nt.nodes.new("ShaderNodeMapRange")
        mr.inputs["From Min"].default_value = lo
        mr.inputs["From Max"].default_value = hi
        L(sep.outputs[comp], mr.inputs["Value"])
        L(mr.outputs["Result"], comb.inputs[k])
    t = nt.nodes.new("ShaderNodeTexImage")
    t.image = bpy.data.images.load(str(TEX / "e5_peel_zones.png"), check_existing=True)
    t.image.colorspace_settings.name = "Non-Color"
    t.extension = "EXTEND"
    t.label = "Peel zones (author: repaint)"
    L(comb.outputs[0], t.inputs["Vector"])
    return t.outputs["Color"]


def stone_material(ng, peel=True):
    m = bpy.data.materials.new("m_e5_limestone_peeling" if peel else "m_e5_limestone_carved")
    nt = m.node_tree
    L = nt.links.new
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (1 / TILE_M,) * 3
    L(geo.outputs["Position"], mp.inputs["Vector"])
    tx = nt.nodes.new("ShaderNodeTexImage")
    tx.image = bpy.data.images.load(str(TEX / "e5_stone_basecolor.png"), check_existing=True)   # tinted texture.jpg
    tx.projection = "BOX"                       # by face direction: reveals and returns don't smear
    tx.projection_blend = 0.25
    L(mp.outputs["Vector"], tx.inputs["Vector"])
    g = nt.nodes.new("ShaderNodeGroup")
    g.node_tree = ng
    g.label = "Peeling plaster (tune here)"
    L(geo.outputs["Position"], g.inputs["Position"])
    L(zones_node(nt, geo), g.inputs["Zones"])
    # intact plaster = the author's limestone; peeled cells expose a darker ochre underlayer; crevices dark
    under = nt.nodes.new("ShaderNodeMix")
    under.data_type = "RGBA"
    under.blend_type = "MULTIPLY"
    under.inputs["Factor"].default_value = 1.0
    L(tx.outputs["Color"], under.inputs["A"])
    under.data_type = "RGBA"
    under.blend_type = "MIX"
    under.inputs["Factor"].default_value = 0.92
    under.inputs["B"].default_value = lin(188, 148, 104)         # bible's exposed ochre / tan underlayer
    m1 = nt.nodes.new("ShaderNodeMix")
    m1.data_type = "RGBA"
    L(g.outputs["Peel"], m1.inputs["Factor"])
    L(tx.outputs["Color"], m1.inputs["A"])
    L(under.outputs["Result"], m1.inputs["B"])
    m2 = nt.nodes.new("ShaderNodeMix")
    m2.data_type = "RGBA"
    L(g.outputs["Crevice Mask"], m2.inputs["Factor"])
    L(m1.outputs["Result"], m2.inputs["A"])
    m2.inputs["B"].default_value = lin(120, 96, 70)              # thin shadow on the torn edge
    lipc = nt.nodes.new("ShaderNodeMix")
    lipc.data_type = "RGBA"
    lipc.blend_type = "SCREEN"
    L(g.outputs["Lip"], lipc.inputs["Factor"])
    L(m2.outputs["Result"], lipc.inputs["A"])
    lipc.inputs["B"].default_value = lin(70, 64, 56)
    L(lipc.outputs["Result"], b.inputs["Base Color"])
    if not peel:                                         # carved stone: the author's texture only
        L(tx.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.88
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.45 if peel else 0.0
    bump.inputs["Distance"].default_value = 0.003
    L(g.outputs["Height"], bump.inputs["Height"])
    tb = nt.nodes.new("ShaderNodeBump")               # fine relief from the limestone image itself
    tb.inputs["Strength"].default_value = 0.25
    tb.inputs["Distance"].default_value = 0.002
    L(tx.outputs["Color"], tb.inputs["Height"])
    L(tb.outputs["Normal"], bump.inputs["Normal"])
    L(bump.outputs["Normal"], b.inputs["Normal"])
    return m


def mural_material(ng):
    m = bpy.data.materials.new("m_e5_mural_paint")
    m.surface_render_method = "DITHERED"
    nt = m.node_tree
    L = nt.links.new
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    uv = nt.nodes.new("ShaderNodeUVMap")
    uv.uv_map = "uv_material"
    tb = nt.nodes.new("ShaderNodeTexImage")
    tb.image = bpy.data.images.load(str(TEX / "e5_mural_basecolor.png"), check_existing=True)
    L(uv.outputs["UV"], tb.inputs["Vector"])
    te = nt.nodes.new("ShaderNodeTexImage")
    te.image = bpy.data.images.load(str(TEX / "e5_mural_emissive.png"), check_existing=True)
    L(uv.outputs["UV"], te.inputs["Vector"])
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    g = nt.nodes.new("ShaderNodeGroup")
    g.node_tree = ng
    L(geo.outputs["Position"], g.inputs["Position"])
    L(zones_node(nt, geo), g.inputs["Zones"])
    # paint flakes off with the plaster: peeled cells keep only a ghost of paint, crevices none
    pmask = nt.nodes.new("ShaderNodeValue")
    pmask.label = "Peel through paint (0..1)"
    pmask.outputs[0].default_value = 0.06
    pk = nt.nodes.new("ShaderNodeMath")
    pk.operation = "MULTIPLY"
    L(g.outputs["Peel"], pk.inputs[0])
    L(pmask.outputs[0], pk.inputs[1])
    inv = nt.nodes.new("ShaderNodeMath")
    inv.operation = "SUBTRACT"
    inv.inputs[0].default_value = 1.0
    L(pk.outputs[0], inv.inputs[1])
    a1 = nt.nodes.new("ShaderNodeMath")
    a1.operation = "MULTIPLY"
    L(tb.outputs["Alpha"], a1.inputs[0])
    L(inv.outputs[0], a1.inputs[1])
    cr = nt.nodes.new("ShaderNodeMath")
    cr.operation = "MULTIPLY_ADD"
    L(g.outputs["Crevice Mask"], cr.inputs[0])
    cr.inputs[1].default_value = -0.15
    cr.inputs[2].default_value = 1.0
    a2 = nt.nodes.new("ShaderNodeMath")
    a2.operation = "MULTIPLY"
    L(a1.outputs[0], a2.inputs[0])
    L(cr.outputs[0], a2.inputs[1])
    L(a2.outputs[0], b.inputs["Alpha"])
    L(tb.outputs["Color"], b.inputs["Base Color"])
    L(te.outputs["Color"], b.inputs["Emission Color"])
    b.inputs["Emission Strength"].default_value = 1.4
    b.inputs["Roughness"].default_value = 0.9
    b.inputs["Specular IOR Level"].default_value = 0.12    # matte mineral paint: no milky sky sheen at grazing angles
    # the mural peels with the plaster: shares the plaster's per-cell value for a mild bump
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.4
    bump.inputs["Distance"].default_value = 0.003
    L(g.outputs["Height"], bump.inputs["Height"])
    L(bump.outputs["Normal"], b.inputs["Normal"])
    return m


# =========================================================================================
# context
# =========================================================================================
# E2 window kits (integrated by mason-2): their stone parts are what the paint lies on round the window columns;
# frames, sashes, interiors, curtains (the openings), pots, plants and railings are context only, never paint
E2_STONE_SUFFIX = ("_surround", "_surround_ledge", "_pediment_crest", "_apron_crest", "_apron_panel", "_sill",
                   "_slab", "_hood", "_keystone_floral")
E2_CONTEXT_SUFFIX = ("_frame", "_sash_upper", "_sash_lower", "_interior", "_curtain", "_curtain_rod", "_cord",
                     "_railing", "_pots", "_foliage", "_stems_flowers", "_lamp")
E2_STONE = []


def load_shell(C):
    with bpy.data.libraries.load(str(MAIN), link=False) as (src, dst):
        e2 = [n for n in src.objects if n.startswith("aa_window_") and n.endswith(E2_STONE_SUFFIX + E2_CONTEXT_SUFFIX)]
        dst.objects = [n for n in STONE + SHELL_OTHER if n in src.objects] + e2
    E2_STONE[:] = [o.name for o in dst.objects if o.name.startswith("aa_window_") and o.name.endswith(E2_STONE_SUFFIX)]
    # E2 kits live at the origin in aa_kit/<kit>; aa_layout's COLLECTION-instance empties place them. Read each
    # instancer's location / rotation (read-only link, library dropped again) and place the appended kit parts.
    with bpy.data.libraries.load(str(MAIN), link=True) as (src2, dst2):
        dst2.objects = [n for n in src2.objects if n.startswith("aa_window_") and "__" in n]
    place = {}
    for e in dst2.objects:
        if e.instance_type == "COLLECTION" and e.instance_collection:
            place[e.instance_collection.name] = (Matrix.Translation(e.location) @ e.rotation_euler.to_matrix().to_4x4()
                                                 @ Matrix.Diagonal((*e.scale, 1.0)))
    libs = {e.library for e in dst2.objects if e.library}
    for e in list(dst2.objects):
        bpy.data.objects.remove(e)
    for lib in libs:
        bpy.data.libraries.remove(lib)
    kits = sorted(place, key=len, reverse=True)
    n_placed = 0
    for o in dst.objects:
        if not o.name.startswith("aa_window_"):
            continue
        kit = next((k for k in kits if o.name.startswith(k + "_")), None)
        if kit:
            o.matrix_world = place[kit] @ o.matrix_world
            n_placed += 1
    print("E5 E2 PLACED", n_placed, "parts in", len(place), "kits")
    for o in dst.objects:
        C.objects.link(o)
    for im in bpy.data.images:
        if im.source == "FILE" and not im.packed_file:
            im.filepath = bpy.path.abspath(im.filepath, library=im.library)
    return {o.name: o for o in dst.objects}


def load_wip(path, colls, parent):
    if not path.exists():
        return []
    with bpy.data.libraries.load(str(path), link=False) as (src, dst):
        dst.collections = [n for n in colls if n in src.collections]
    for c in dst.collections:
        parent.children.link(c)
    return dst.collections


# =========================================================================================
# conformed mural decal
# =========================================================================================
def decal(stone_objs, C, M_mural, block_objs=()):
    import numpy as np
    im = bpy.data.images.load(str(TEX / "e5_mural_basecolor.png"), check_existing=True)
    W, H = im.size
    px = np.empty(W * H * 4, np.float32)
    im.pixels.foreach_get(px)
    a = px.reshape(H, W, 4)[::-1, :, 3]            # row 0 = top of the sheet
    dg = bpy.context.evaluated_depsgraph_get()
    trees = []
    for o in list(stone_objs) + list(block_objs):
        bm = bmesh.new()
        bm.from_object(o, dg)
        bm.transform(o.matrix_world)
        trees.append((BVHTree.FromBMesh(bm), o in block_objs))
        bm.free()
    x0, x1, z0, z1 = MU.SHEET_X0, MU.SHEET_X1, MU.SHEET_Z0, MU.SHEET_Z1
    nx = int((x1 - x0) / DECAL_STEP) + 1
    nz = int((z1 - z0) / DECAL_STEP) + 1
    # paint coverage per grid cell (dilated by one cell so the alpha edge isn't clipped)
    cov = np.zeros((nz, nx), bool)
    for j in range(nz - 1):
        for i in range(nx - 1):
            u0, u1 = int(i * DECAL_STEP * MU.PPM), int((i + 1) * DECAL_STEP * MU.PPM) + 1
            r1, r0 = H - int(j * DECAL_STEP * MU.PPM), H - int((j + 1) * DECAL_STEP * MU.PPM) - 1
            blk = a[max(r0, 0):max(r1, 0), u0:min(u1, W)]
            cov[j, i] = blk.size > 0 and blk.max() > 0.04
    d = cov.copy()                                  # one-cell dilation (numpy, no scipy in Blender)
    d[1:, :] |= cov[:-1, :]
    d[:-1, :] |= cov[1:, :]
    d[:, 1:] |= cov[:, :-1]
    d[:, :-1] |= cov[:, 1:]
    cov = d
    ys = np.full((nz, nx), np.nan)
    for j in range(nz):
        z = z0 + j * DECAL_STEP
        for i in range(nx):
            if not (cov[min(j, nz - 2), min(i, nx - 2)] or cov[max(j - 1, 0), max(i - 1, 0)]):
                continue
            x = x0 + i * DECAL_STEP
            best, blocked = None, False
            for t, is_block in trees:
                loc, nrm, _, d = t.ray_cast(Vector((x, -3.0, z)), Vector((0, 1, 0)), 6.0)
                if loc is not None and (best is None or d < best):
                    best, blocked = d, is_block
            if best is not None and not blocked:             # window openings (frames, sashes, interiors) block
                ys[j, i] = -3.0 + best
    bm = bmesh.new()
    uvl = bm.loops.layers.uv.new("uv_material")
    vid = {}

    def V(i, j):
        if (i, j) not in vid:
            vid[(i, j)] = bm.verts.new((x0 + i * DECAL_STEP, ys[j, i] - DECAL_LIFT, z0 + j * DECAL_STEP))
        return vid[(i, j)]
    nf = 0
    for j in range(nz - 1):
        for i in range(nx - 1):
            if not cov[j, i]:
                continue
            q = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
            yy = [ys[b_, a_] for a_, b_ in q]
            if any(np.isnan(yy)) or max(yy) - min(yy) > 0.12 or max(yy) > 0.12:   # steps, reveals, openings
                continue
            f = bm.faces.new([V(*p) for p in q])
            for l_, (a_, b_) in zip(f.loops, q):
                l_[uvl].uv = ((a_ * DECAL_STEP) / (x1 - x0), (b_ * DECAL_STEP) / (z1 - z0))
            nf += 1
    for f in bm.faces:
        if f.normal.y > 0:
            f.normal_flip()
    me = bpy.data.meshes.new("aa_e5_mural_decal")
    bm.to_mesh(me)
    bm.free()
    me.uv_layers.new(name="uv_bake")                      # copy of uv_material (non-overlapping heightfield)
    src, dst = me.uv_layers["uv_material"], me.uv_layers["uv_bake"]
    for k in range(len(src.data)):
        dst.data[k].uv = src.data[k].uv
    me.materials.append(M_mural)
    me.shade_smooth()
    ob = bpy.data.objects.new("aa_e5_mural_decal", me)
    C.objects.link(ob)
    return ob, nf


def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)
    ctx = coll("e5_context")
    shell = load_shell(coll("e5_context_mason_shell", ctx))
    load_wip(E3WIP, ["aa_e3_marquee", "aa_e3_doorway"], coll("e5_context_e3", ctx))
    load_wip(E4WIP, ["aa_e4_keystone", "aa_e4_conduits", "aa_e4_pipes", "aa_e4_plaque"], coll("e5_context_e4", ctx))
    ng = peel_group()
    Ms = stone_material(ng, peel=True)
    Mc = stone_material(ng, peel=False)
    Mm = mural_material(ng)
    for n in STONE:
        o = shell.get(n)
        if o:
            o.data.materials.clear()
            o.data.materials.append(Ms if n == "aa_shell_facade_walls" else Mc)   # carvings stay intact
    kit = coll("aa_kit")
    c_mur = coll("aa_e5_mural", kit)
    e2_open = [o for n, o in shell.items() if n.startswith("aa_window_") and
               n.endswith(("_frame", "_sash_upper", "_sash_lower", "_interior"))]
    ob, nf = decal([shell[n] for n in STONE if n in shell] + [shell[n] for n in E2_STONE if n in shell], c_mur, Mm,
                   block_objs=e2_open)
    print("E5 BUILD conformed to", len([n for n in STONE if n in shell]), "shell +", len(E2_STONE), "E2 stone parts")
    vs = [v.co for v in ob.data.vertices]
    print("E5 BUILD decal faces", nf, "bbox", [round(min(v[i] for v in vs), 3) for i in range(3)],
          [round(max(v[i] for v in vs), 3) for i in range(3)], "objects", len(bpy.data.objects))
    if "--no-save" not in args:
        WIP.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(WIP))
        print("saved", WIP)


main()
