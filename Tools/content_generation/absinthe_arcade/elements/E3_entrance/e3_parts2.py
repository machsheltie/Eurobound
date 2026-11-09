"""E3 round 2 parts (runs inside Blender): moulded iron doorway, backlit stained glass, sign frame,
paper flyers, marquee bezel / skull crest / chrome knots / traced slogan, the lit hazy interior set
with its forced-perspective floor, and the uv_bake unwrap.

Called from e3_build.py. Canvas coordinates are pixels of the rectified crop 04 (e3_trace_lib).
"""
import math

import bmesh
import bpy
from mathutils import Matrix, Vector

from e3_kit import (ARCH, L, MB, STEP_Z, Y_BANNER_F, Y_BOARD_B, Y_BOARD_F, Y_FRAME_B, Y_FRAME_F, Y_HINGE, Y_INT0,
                    _principled, _uv, glow, img, lin, mat, mat_image, offset_poly, spiral, tex_node, tube)

PI = math.pi


# =========================================================================================
# materials
# =========================================================================================
def materials2(M):
    # near-black glossy iron (crop board/door blacks sample sRGB ~ 20-35); soft specular from a clear coat
    M["black"] = mat("m_e3_iron_black_gloss", lin(10, 11, 13), rough=0.36, coat=0.18)
    M["iron"] = M["black"]
    M["rim"] = mat("m_e3_bezel_black", lin(7, 7, 9), rough=0.42, coat=0.12)
    M["bolt"] = mat("m_e3_bolt_steel", (0.45, 0.45, 0.47), rough=0.3, metal=1.0)
    M["chrome"] = mat("m_e3_chrome", (0.90, 0.90, 0.92), rough=0.08, metal=1.0)
    M["brass"] = mat("m_e3_brass", (0.66, 0.47, 0.22), rough=0.34, metal=1.0)
    M["brass_dark"] = mat("m_e3_brass_shadow", lin(30, 22, 12), rough=0.6)
    M["gold"] = mat("m_e3_gold_leaf", (0.86, 0.64, 0.28), rough=0.28, metal=1.0)
    T = L.load_trace()
    w = T["arcade"]
    from e3_kit import Y_LET_F
    L.use("marquee", Y_LET_F)
    zb, zt = L.mz(w["baseline_y"]), L.mz(w["baseline_y"] - w["rows"] * w["cell"])
    M["let_p"] = mat_bead("m_e3_led_purple_beads", lin(205, 150, 240), lin(96, 34, 160), zb, zt)
    M["neon_cocktail"] = glow("m_e3_neon_cocktail_lavender", (214, 150, 244), 3.2)
    M["paper_back"] = mat("m_e3_paper_back", lin(225, 220, 208), rough=0.85)
    M["pink_sign"] = mat_image("m_e3_pink_sign", L.TEX / "e3_pink_sign.png", rough=0.6)
    for gid in ("l_transom_a", "l_main", "l_transom_b", "l_purple", "r_transom", "r_main", "strip"):
        M["glass_" + gid] = mat_glass(f"m_e3_glass_{gid}", gid)
    for k in range(5):
        M[f"scr{k}"] = mat_image(f"m_e3_cab_screen_{k}", L.TEX / f"e3_cab_screen_{k}.png", rough=0.08,
                                 estr=2.2 if k < 2 else 1.4)
        M[f"mq{k}"] = mat_image(f"m_e3_cab_marquee_{k}", L.TEX / f"e3_cab_marquee_{k}.png", rough=0.3,
                                estr=1.1 if k < 2 else 0.8)
    M["cab"] = mat("m_e3_cabinet_black", lin(14, 14, 18), rough=0.3, coat=0.4)
    M["cab_trim"] = glow("m_e3_cabinet_yellow_trim", (235, 190, 40), 0.6, base_k=0.7, rough=0.3)
    M["btn_r"] = glow("m_e3_button_red", (230, 40, 40), 0.8, base_k=0.6)
    M["btn_b"] = glow("m_e3_button_blue", (50, 110, 240), 0.8, base_k=0.6)
    M["btn_y"] = glow("m_e3_button_yellow", (240, 210, 50), 0.8, base_k=0.6)
    M["coin"] = glow("m_e3_coin_slot_orange", (255, 120, 30), 2.0)
    M["int_wall"] = mat("m_e3_interior_wall", lin(5, 4, 3), rough=0.9)
    M["int_dark"] = mat("m_e3_interior_vault", lin(4, 3, 3), rough=0.9)
    M["rib"] = mat("m_e3_interior_rib", lin(9, 7, 6), rough=0.5, coat=0.15)
    M["bulb"] = mat("m_e3_lamp_bulb", (1.0, 0.8, 0.5), emit=(1.0, 0.66, 0.30), estr=18)
    M["shade"] = mat("m_e3_lamp_shade_bronze", (0.42, 0.30, 0.14), rough=0.4, metal=1.0)
    M["shade_in"] = mat("m_e3_lamp_shade_inner", (0.9, 0.78, 0.55), emit=(1.0, 0.80, 0.52), estr=7)
    M["silh"] = mat("m_e3_silhouette", (0.004, 0.0035, 0.003), rough=0.95)
    M["haze"] = mat_haze()
    fl = M["floor"]
    b = _principled(fl)
    b.inputs["Roughness"].default_value = 0.06
    b.inputs["Coat Weight"].default_value = 0.6
    for n in fl.node_tree.nodes:
        if n.type == "MAPPING":
            n.inputs["Scale"].default_value = (1 / TILE, 1 / TILE, 1)
    return M


TILE = 0.62          # checker tile edge (uncompressed metres), diagonal as the bible shows


BEADS_PER_CELL = 3


PLINTH_IN = 0.09


def mat_bead(name, col_top, col_bot, zb, zt):
    """ARCADE faces: fine domed LED sequins (3 x 3 per letter cell), each bead lit at its crown with its own
    random brightness, coloured by a vertical gradient (lavender at the top, deep purple at the bottom)."""
    m = mat(name, tuple(0.15 * c for c in col_bot), rough=0.18, emit=col_bot, estr=1.0)
    nt = m.node_tree
    b = _principled(m)
    sc = BEADS_PER_CELL / 16.0   # uv_material in letter-cell units (bead_uvs); the bead tile holds 16 beads
    tn = tex_node(m, img(L.TEX / "e3_bead_normal.png", True), scale=sc)
    nm = nt.nodes.new("ShaderNodeNormalMap")
    nm.uv_map = "uv_material"
    nm.inputs["Strength"].default_value = 1.2
    nt.links.new(tn.outputs["Color"], nm.inputs["Color"])
    nt.links.new(nm.outputs["Normal"], b.inputs["Normal"])
    th = tex_node(m, img(L.TEX / "e3_bead_height.png", True), scale=sc)
    rng = nt.nodes.new("ShaderNodeMapRange")
    rng.inputs["To Min"].default_value = 0.05
    rng.inputs["To Max"].default_value = 1.5
    nt.links.new(th.outputs["Color"], rng.inputs["Value"])
    # per-bead sparkle: white noise on the bead index (floor of uv * beads)
    uvn = nt.nodes.new("ShaderNodeUVMap")
    uvn.uv_map = "uv_material"
    scl = nt.nodes.new("ShaderNodeVectorMath")
    scl.operation = "SCALE"
    scl.inputs["Scale"].default_value = float(BEADS_PER_CELL)
    nt.links.new(uvn.outputs["UV"], scl.inputs[0])
    fl = nt.nodes.new("ShaderNodeVectorMath")
    fl.operation = "FLOOR"
    nt.links.new(scl.outputs["Vector"], fl.inputs[0])
    wn = nt.nodes.new("ShaderNodeTexWhiteNoise")
    wn.noise_dimensions = "2D"
    nt.links.new(fl.outputs["Vector"], wn.inputs["Vector"])
    sp = nt.nodes.new("ShaderNodeMapRange")
    sp.inputs["To Min"].default_value = 0.55
    sp.inputs["To Max"].default_value = 1.35
    nt.links.new(wn.outputs["Value"], sp.inputs["Value"])
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    nt.links.new(rng.outputs["Result"], mul.inputs[0])
    nt.links.new(sp.outputs["Result"], mul.inputs[1])
    nt.links.new(mul.outputs["Value"], b.inputs["Emission Strength"])
    # vertical gradient from world z (letters are modelled in place)
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(geo.outputs["Position"], sep.inputs[0])
    gz = nt.nodes.new("ShaderNodeMapRange")
    gz.inputs["From Min"].default_value = zb
    gz.inputs["From Max"].default_value = zt
    nt.links.new(sep.outputs["Z"], gz.inputs["Value"])
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs["A"].default_value = (*col_bot, 1)
    mix.inputs["B"].default_value = (*col_top, 1)
    nt.links.new(gz.outputs["Result"], mix.inputs["Factor"])
    nt.links.new(mix.outputs["Result"], b.inputs["Emission Color"])
    dk = nt.nodes.new("ShaderNodeMix")
    dk.data_type = "RGBA"
    dk.blend_type = "MULTIPLY"
    dk.inputs["Factor"].default_value = 1.0
    dk.inputs["B"].default_value = (0.25, 0.25, 0.25, 1)
    nt.links.new(mix.outputs["Result"], dk.inputs["A"])
    nt.links.new(dk.outputs["Result"], b.inputs["Base Color"])
    return m


def bead_uvs(C, word, prefix):
    """ARCADE letters: uv_material in word-grid cell units so every cell carries whole beads."""
    cs = word["cell"]
    x0 = L.mx(word["origin_x"])
    zb = L.mz(word["baseline_y"])
    cw = L.mw(cs)
    for o in C.objects:
        if not o.name.startswith(prefix):
            continue
        me = o.data
        uvm = me.uv_layers["uv_material"]
        for p in me.polygons:
            for li in p.loop_indices:
                co = me.vertices[me.loops[li].vertex_index].co
                if abs(p.normal.y) > 0.5:
                    uvm.data[li].uv = ((co.x - x0) / cw, (co.z - zb) / cw)
                elif abs(p.normal.x) > 0.5:
                    uvm.data[li].uv = (co.y / cw, (co.z - zb) / cw)
                else:
                    uvm.data[li].uv = ((co.x - x0) / cw, co.y / cw)


def mat_glass(name, gid):
    """Backlit cathedral glass: traced colours, raised-came normal map, glow only through the glass."""
    m = mat(name, rough=0.1, coat=0.6)
    nt = m.node_tree
    b = _principled(m)
    t = tex_node(m, img(L.TEX / f"e3_glass_{gid}.png"))
    nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
    nt.links.new(t.outputs["Color"], b.inputs["Emission Color"])
    g = tex_node(m, img(L.TEX / f"e3_glass_{gid}_glow.png", True))
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    mul.inputs[1].default_value = 1.15
    nt.links.new(g.outputs["Color"], mul.inputs[0])
    nt.links.new(mul.outputs["Value"], b.inputs["Emission Strength"])
    n = tex_node(m, img(L.TEX / f"e3_glass_{gid}_normal.png", True))
    nm = nt.nodes.new("ShaderNodeNormalMap")
    nm.uv_map = "uv_material"
    nm.inputs["Strength"].default_value = 1.6
    nt.links.new(n.outputs["Color"], nm.inputs["Color"])
    nt.links.new(nm.outputs["Normal"], b.inputs["Normal"])
    nt.links.new(nm.outputs["Normal"], b.inputs["Coat Normal"])
    return m


def mat_haze():
    m = bpy.data.materials.get("m_e3_interior_haze") or bpy.data.materials.new("m_e3_interior_haze")
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    v = nt.nodes.new("ShaderNodeVolumePrincipled")
    v.inputs["Color"].default_value = (1.0, 0.72, 0.45, 1)
    v.inputs["Density"].default_value = 0.003
    v.inputs["Anisotropy"].default_value = 0.35
    nt.links.new(v.outputs[0], out.inputs["Volume"])
    return m


# =========================================================================================
# moulding helpers
# =========================================================================================
def rect(x0, x1, z0, z1):
    return [(x0, z0), (x1, z0), (x1, z1), (x0, z1)]


def moulding(mb, x0, x1, z0, z1, yf, m, w=0.028, proud=0.016, back=0.002):
    """Bolection moulding round an opening on a face at y=yf: a raised band plus a stepped inner bead."""
    x0, x1 = sorted((x0, x1))
    z0, z1 = sorted((z0, z1))
    mb.ring(rect(x0 - w, x1 + w, z0 - w, z1 + w), rect(x0, x1, z0, z1), yf - proud, yf + back, m)
    e = 0.004
    mb.ring(rect(x0 - w * 0.62, x1 + w * 0.62, z0 - w * 0.62, z1 + w * 0.62),
            rect(x0 - e, x1 + e, z0 - e, z1 + e), yf - proud - 0.008, yf - proud + 0.001, m)


def frustum(mb, x0, x1, z0, z1, inset, yback, yfront, m):
    """Raised-and-fielded panel: back face full size, front face inset (chamfered field)."""
    x0, x1 = sorted((x0, x1))
    z0, z1 = sorted((z0, z1))
    bm = mb.bm
    b = [bm.verts.new((x, yback, z)) for x, z in rect(x0, x1, z0, z1)]
    f = [bm.verts.new((x, yfront, z)) for x, z in rect(x0 + inset, x1 - inset, z0 + inset, z1 - inset)]
    faces = [bm.faces.new(f[::-1]), bm.faces.new(b)]
    for k in range(4):
        j = (k + 1) % 4
        faces.append(bm.faces.new((b[k], b[j], f[j], f[k])))
    mb._faces(faces, m)
    bmesh.ops.recalc_face_normals(bm, faces=faces)


def stepped(mb, x0, x1, z0, z1, yf, yb, steps, m):
    """Stack of boxes widening by `steps` = [(dx, dz_height, proud)] from z0 upward (capital/cornice)."""
    z = z0
    for dx, hz, pr in steps:
        mb.box(x0 - dx, x1 + dx, yf - pr, yb, z, z + hz, m)
        z += hz
    return z


def grid_cells(outer, holes):
    """Solid cells of an axis-aligned grid: outer rect minus hole rects (all as (x0,x1,z0,z1))."""
    xs = sorted({round(v, 6) for r in [outer] + holes for v in r[:2]})
    zs = sorted({round(v, 6) for r in [outer] + holes for v in r[2:]})
    out = []
    for i in range(len(xs) - 1):
        for j in range(len(zs) - 1):
            cx, cz = (xs[i] + xs[i + 1]) / 2, (zs[j] + zs[j + 1]) / 2
            if not (outer[0] < cx < outer[1] and outer[2] < cz < outer[3]):
                continue
            if any(h[0] < cx < h[1] and h[2] < cz < h[3] for h in holes):
                continue
            out.append((xs[i], xs[i + 1], zs[j], zs[j + 1]))
    return out


def cr(xc0, xc1, yc0, yc1):
    """Canvas rect -> metres rect (x0, x1, z0, z1) on the current layout plane."""
    xa, xb = sorted((L.mx(xc0), L.mx(xc1)))
    za, zb = sorted((L.mz(yc0), L.mz(yc1)))
    return (xa, xb, za, zb)


def scroll(cx, cz, r, turns, a0, sign=1, n=40):
    return spiral(cx, cz, r, turns, n, a0, sign)[::-1]


def filigree_corner(C, name, cx, cz, sx, sz, y, m, size=0.045, rad=0.0035):
    """Fuller gold corner scroll: a C-scroll along each edge curling into spirals, plus a leaf tip."""
    a = scroll(cx + sx * size * 1.1, cz + sz * size * 0.35, size * 0.42, 1.25, PI / 2 if sz > 0 else -PI / 2,
               sign=sx * sz)
    b = scroll(cx + sx * size * 0.35, cz + sz * size * 1.1, size * 0.42, 1.25, 0 if sx > 0 else PI, sign=-sx * sz)
    tube(f"{name}_a", C, [(x, y, z) for x, z in a] + [(cx + sx * 0.004, y, cz + sz * 0.004)], rad, m)
    tube(f"{name}_b", C, [(x, y, z) for x, z in b] + [(cx + sx * 0.004, y, cz + sz * 0.004)], rad, m)
    leaf = [(cx + sx * size * 0.55, cz + sz * size * 0.55), (cx + sx * size * 0.95, cz + sz * size * 0.8),
            (cx + sx * size * 1.25, cz + sz * size * 1.25), (cx + sx * size * 0.8, cz + sz * size * 0.95)]
    tube(f"{name}_leaf", C, [(x, y, z) for x, z in leaf], rad * 0.9, m, cyclic=True)


# =========================================================================================
# doorway
# =========================================================================================
FLYERS = [  # canvas (x0, y0, x1, y1, rot_deg, curl_corner or None); 0 = the pink sign
    (380, 1185, 510, 1265, 0, None), (360, 1285, 440, 1360, -2, "tr"), (445, 1275, 528, 1350, 2, None),
    (330, 1330, 430, 1440, 3, "bl"), (420, 1330, 500, 1420, -3, None), (500, 1380, 590, 1470, -4, "tr"),
    (330, 1440, 420, 1520, 2, None), (420, 1440, 510, 1560, -1, "br"), (510, 1530, 595, 1620, 3, None),
    (438, 1540, 508, 1612, 1, None), (510, 1630, 600, 1740, -3, "tl"), (420, 1610, 500, 1700, 2, None),
    (420, 1700, 500, 1810, -2, "bl"), (420, 1790, 510, 1900, 2, None), (500, 1730, 560, 1900, 0, None),
]


def build_doorway2(M, C):
    L.use("door", Y_FRAME_F)
    zs = STEP_Z
    zh = L.mz(885)
    yf = Y_FRAME_F + 0.02           # pier front face

    # ---- head: beam + moulded cornice band under the banner
    mb = MB()
    mb.box(L.mx(300), L.mx(2495), Y_FRAME_F - 0.02, Y_INT0, L.mz(935), zh, M["black"])
    stepped(mb, L.mx(300), L.mx(2495), L.mz(935), zh, Y_FRAME_F - 0.02, Y_FRAME_F + 0.04,
            [(0.0, 0.025, 0.035), (0.0, 0.02, 0.055), (0.0, 0.025, 0.075)], M["black"])
    mb.finish("aa_e3_door_head", C, bevel=0.006, segments=3)

    # ---- (1) left pier
    xa, xb = L.mx(300), L.mx(610)
    flyer_field = cr(326, 596, 1112, 1905)
    kick_field = cr(330, 580, 1935, 2160)
    mb = MB()
    mb.box(xa, xb, yf, Y_FRAME_B, zs, L.mz(1100), M["black"])                         # body
    zc = stepped(mb, xa, xb, L.mz(1100), 0, yf, Y_FRAME_B,                              # capital
                 [(0.0, 0.03, 0.02), (0.012, 0.03, 0.04), (0.026, 0.04, 0.06)], M["black"])
    mb.box(L.mx(380), L.mx(540), yf, Y_FRAME_B, zc, L.mz(940), M["black"])             # cap block
    stepped(mb, xa, xb, zs, 0, yf, Y_FRAME_B, [(0.024, 0.05, 0.05), (0.012, 0.04, 0.035)], M["black"])  # plinth
    jl = ARCH["jamb_x"][0]
    if xa - jl > 0.005:
        mb.box(jl, xa - 0.03, yf + 0.08, Y_FRAME_B, zs, zh, M["black"])
    moulding(mb, *flyer_field, yf, M["black"], w=0.03, proud=0.018)
    moulding(mb, *kick_field, yf, M["black"], w=0.026, proud=0.016)
    frustum(mb, *kick_field, 0.03, yf + 0.001, yf - 0.014, M["black"])
    cb = cr(395, 525, 950, 1030)
    moulding(mb, *cb, yf, M["black"], w=0.018, proud=0.012)
    mb.finish("aa_e3_frame_left", C, bevel=0.005, segments=3)
    # gold lines and inlay
    mb = MB()
    gx0, gx1, gz0, gz1 = flyer_field
    r_o = rect(gx0 + 0.006, gx1 - 0.006, gz0 + 0.006, gz1 - 0.006)
    mb.ring(r_o, offset_poly(r_o, 0.006), yf - 0.003, yf + 0.001, M["gold"])
    ix, iz = (kick_field[0] + kick_field[1]) / 2, (kick_field[2] + kick_field[3]) / 2
    yk = yf - 0.014
    sq = rect(ix - 0.075, ix + 0.075, iz - 0.075, iz + 0.075)
    mb.ring(sq, offset_poly(sq, 0.012), yk - 0.006, yk + 0.002, M["gold"])
    dsq = [(ix, iz - 0.05), (ix + 0.05, iz), (ix, iz + 0.05), (ix - 0.05, iz)]
    mb.ring(dsq, offset_poly(dsq, 0.011), yk - 0.006, yk + 0.002, M["gold"])
    mb.finish("aa_e3_frame_left_gold", C, bevel=0.002)
    k0 = kick_field
    for k, (cx, cz, sx, sz) in enumerate(((k0[0] + 0.04, k0[3] - 0.04, 1, -1), (k0[1] - 0.04, k0[3] - 0.04, -1, -1),
                                          (k0[0] + 0.04, k0[2] + 0.04, 1, 1), (k0[1] - 0.04, k0[2] + 0.04, -1, 1))):
        filigree_corner(C, f"aa_e3_frame_left_kick_filigree_{k}", cx, cz, sx, sz, yk - 0.003, M["gold"], 0.035)
    build_flyers(M, C, yf)

    # ---- (4) right pier: sign board + strip
    sx0, sx1 = L.mx(2010), L.mx(2318)
    base = cr(2030, 2300, 2020, 2175)
    mb = MB()
    mb.box(sx0, sx1, yf, Y_FRAME_B, zs, L.mz(1050), M["black"])
    zc = stepped(mb, sx0, sx1, L.mz(1050), 0, yf, Y_FRAME_B,
                 [(0.0, 0.03, 0.02), (0.012, 0.03, 0.04), (0.026, 0.04, 0.06)], M["black"])
    mb.box(L.mx(2060), L.mx(2290), yf, Y_FRAME_B, zc, L.mz(940), M["black"])
    stepped(mb, sx0, sx1, zs, 0, yf, Y_FRAME_B, [(0.024, 0.05, 0.05), (0.012, 0.04, 0.035)], M["black"])
    moulding(mb, *base, yf, M["black"], w=0.026, proud=0.016)
    frustum(mb, *base, 0.03, yf + 0.001, yf - 0.014, M["black"])
    # strip frame (stiles, head, sill) with moulding round the glass
    st = cr(2336, 2468, 880, 2000)
    mb.finish("aa_e3_frame_right", C, bevel=0.005, segments=3)
    sm = MB(jitter=False)
    sm.cells(grid_cells((L.mx(2318), L.mx(2495) - 0.003, zs + 0.003, L.mz(889)), [st]), yf + 0.0015, Y_FRAME_B - 0.002,
             M["black"], M["black"])
    moulding(sm, *st, yf + 0.0015, M["black"], w=0.022, proud=0.014)
    sm.finish("aa_e3_frame_right_strip", C, bevel=0.004, segments=2)
    # strip glass: traced pane above, plain cathedral glass below (hidden by the E6 plant in the bible)
    gm = MB(jitter=False)
    up = (st[0] - 0.004, st[1] + 0.004, L.mz(1700), st[3] + 0.004)
    gm.uvbox[gm.mi(M["glass_strip"])] = up
    gm.box(up[0], up[1], yf + 0.03, yf + 0.036, up[2], up[3], M["glass_strip"])
    gm.box(up[0], up[1], yf + 0.03, yf + 0.036, st[2] - 0.004, up[2] - 0.0015, M["glass_plain"])
    gm.finish("aa_e3_frame_right_strip_glass", C, weld=False)
    build_sign(M, C)

    # ---- (2)(3) inner doors
    L.plane(Y_HINGE)
    left = dict(outer=(610, 1030, 915, 2215), hinge=610, side=+1, angle=20.0,
                glass=[(688, 782, 930, 1090, "glass_l_transom_a"), (858, 936, 930, 1090, "glass_l_transom_b"),
                       (686, 790, 1105, 1785, "glass_l_main"), (850, 940, 1105, 1905, "glass_l_purple")],
                p2x2=[(692, 788, 1790, 1902)],
                kicks=[(632, 812, 1930, 2190, (706, 776, 1996, 2068), "kick_l"), (832, 1008, 1930, 2190, None, None)],
                handles=[])
    right = dict(outer=(1720, 2030, 915, 2205), hinge=2030, side=-1, angle=10.0,
                 glass=[(1835, 1966, 935, 1080, "glass_r_transom"), (1838, 1990, 1118, 1785, "glass_r_main")],
                 p2x2=[(1842, 1988, 1788, 1902)],
                 kicks=[(1850, 2005, 1930, 2180, (1892, 1974, 2002, 2084), "kick_r")],
                 handles=[(1730, 1748, 1210, 1275, "chrome"), (1772, 1790, 1590, 1680, "brass")])
    build_leaf2(M, C, "aa_e3_door_left", left)
    build_leaf2(M, C, "aa_e3_door_right", right)

    # threshold step
    L.plane(0.0)
    jl, jr = ARCH["jamb_x"]
    mb = MB()
    mb.box(L.mx(110), L.mx(2560), -0.46, 0.0, 0.0, zs, M["concrete"])
    # interfaces v2.1: the pier plinths reach 0.09 m inside both jambs below z 1.03, in front of y 0.02
    mb.box(jl + PLINTH_IN, jr - PLINTH_IN, -0.01, 0.02, 0.0, zs, M["concrete"])
    mb.box(jl, jr, 0.02, Y_INT0 + 0.02, 0.0, zs, M["concrete"])
    mb.finish("aa_e3_threshold_step", C, bevel=0.01)


def build_flyers(M, C, yf):
    """Paper on the pier: thin sheets overlapping at slight angles, a few with curled corners."""
    for i, (a, b, c, d, rot, curl) in enumerate(FLYERS):
        m = M["pink_sign"] if i == 0 else M[f"flyer{(i - 1) % 14}"]
        a, c = max(a, 330), min(c, 592)
        x0, x1, z0, z1 = cr(a, c, b, d)
        y = yf - 0.0012 * (i + 1)
        fm = MB(jitter=False)
        fm.uvbox[fm.mi(m)] = (x0, x1, z0, z1)
        bm = fm.bm
        cut = 0.035 if curl else 0.0
        # sheet outline with the curled corner cut off diagonally
        pts = {"bl": (x0, z0), "br": (x1, z0), "tr": (x1, z1), "tl": (x0, z1)}
        poly = []
        for key in ("bl", "br", "tr", "tl"):
            px_, pz = pts[key]
            if key == curl:
                sx = 1 if key in ("bl", "tl") else -1
                sz = 1 if key in ("bl", "br") else -1
                nxt = [(px_, pz + sz * cut), (px_ + sx * cut, pz)]
                poly += nxt if key in ("bl", "tr") else nxt[::-1]
            else:
                poly.append((px_, pz))
        vf = [bm.verts.new((x, y - 0.0006, z)) for x, z in poly]
        vb = [bm.verts.new((x, yf + 0.0006 + 0.0011 * i, z)) for x, z in poly]   # sheet pressed onto the pier
        f = bm.faces.new(vf[::-1])
        g = bm.faces.new(vb)
        sides = [bm.faces.new((vf[k], vf[(k + 1) % len(vf)], vb[(k + 1) % len(vf)], vb[k])) for k in range(len(vf))]
        fm._faces([f, g] + sides, m)
        if curl:
            # the curled-up corner: the cut triangle folded back out from the sheet (paper back showing)
            px_, pz = pts[curl]
            sx = 1 if curl in ("bl", "tl") else -1
            sz = 1 if curl in ("bl", "br") else -1
            p1 = Vector((px_, y - 0.0006, pz + sz * cut))
            p2 = Vector((px_ + sx * cut, y - 0.0006, pz))
            tip = Vector((px_ + sx * cut * 0.7, y - cut * 0.55, pz + sz * cut * 0.7))
            off = Vector((0, -0.0011, 0))
            t = [bm.verts.new(p + off) for p in (p1, p2, tip)]
            tf = [bm.faces.new(t)]
            fm._faces(tf, M["paper_back"])
        if rot:
            cx, cz = (x0 + x1) / 2, (z0 + z1) / 2
            fm.transform(Matrix.Translation((cx, 0, cz)) @ Matrix.Rotation(math.radians(rot), 4, "Y") @
                         Matrix.Translation((-cx, 0, -cz)))
        fm.finish(f"aa_e3_frame_left_flyer_{i:02d}", C)
    # small pink diamond card above the pink sign
    x0, x1, z0, z1 = cr(432, 462, 1130, 1170)
    cx, cz = (x0 + x1) / 2, (z0 + z1) / 2
    fm = MB(jitter=False)
    fm.uvbox[fm.mi(M["pink_sign"])] = (x0, x1, z0, z1)
    fm.box(x0, x1, yf - 0.0015, yf + 0.0005, z0, z1, M["pink_sign"])
    fm.transform(Matrix.Translation((cx, 0, cz)) @ Matrix.Rotation(math.radians(45), 4, "Y") @
                 Matrix.Translation((-cx, 0, -cz)))
    fm.finish("aa_e3_frame_left_flyer_diamond", C)


def sign_outline(tab=True, inset=0.0):
    """Board outline with concave (arched) top corners and a raised centre tab, canvas -> metres."""
    x0, x1, z0, z1 = cr(2040, 2312, 1060, 2000)
    x0, x1, z0, z1 = x0 + inset, x1 - inset, z0 + inset, z1 - inset
    r = 0.065 + inset
    # concave quarter-circle notch at each top corner (centre on the corner)
    pts = [(x0, z0), (x1, z0), (x1, z1 - r)]
    pts += [(x1 + r * math.cos(a), z1 + r * math.sin(a)) for a in [-PI / 2 - k * (PI / 2) / 8 for k in range(1, 9)]]
    cx = (x0 + x1) / 2
    if tab:
        pts += [(cx + 0.05, z1), (cx + 0.035, z1 + 0.025), (cx - 0.035, z1 + 0.025), (cx - 0.05, z1)]
    pts += [(x0 + r * math.cos(a), z1 + r * math.sin(a)) for a in [-k * (PI / 2) / 8 for k in range(0, 8)]]
    pts.append((x0, z1 - r))
    return pts


def build_sign(M, C):
    L.plane(Y_FRAME_F)
    yfs = Y_FRAME_F - 0.005
    outline = sign_outline()
    mb = MB()
    mb.prism(outline, yfs, Y_FRAME_F + 0.028, M["black"])                             # board
    mb.finish("aa_e3_sign_board", C, bevel=0.003, segments=2)
    mb = MB()
    mb.ring(offset_poly(outline, -0.03), offset_poly(outline, 0.002), yfs - 0.022, Y_FRAME_F + 0.03, M["black"])
    mb.finish("aa_e3_sign_frame", C, bevel=0.005, segments=3)                         # moulded frame
    mb = MB()
    mb.ring(offset_poly(outline, -0.012), offset_poly(outline, 0.006), yfs - 0.032, yfs - 0.0205, M["black"])
    mb.finish("aa_e3_sign_frame_bead", C, bevel=0.004, segments=3)
    mb = MB()
    mb.ring(sign_outline(tab=False, inset=0.028), sign_outline(tab=False, inset=0.034), yfs - 0.0055, yfs + 0.002,
            M["gold"])
    a, b = cr(2100, 2300, 1697, 1697)[:2]
    zz = L.mz(1697)
    mb.box(a + 0.008, b - 0.008, yfs - 0.0028, yfs + 0.002, zz - 0.0025, zz + 0.0025, M["gold"])
    mb.finish("aa_e3_sign_gold_border", C)
    x0, x1, z0, z1 = cr(2040, 2320, 1060, 2000)
    for k, (cx, cz, sx, sz) in enumerate(((x0 + 0.05, z1 - 0.1, 1, -1), (x1 - 0.05, z1 - 0.1, -1, -1),
                                          (x0 + 0.05, z0 + 0.05, 1, 1), (x1 - 0.05, z0 + 0.05, -1, 1))):
        filigree_corner(C, f"aa_e3_sign_filigree_{k}", cx, cz, sx, sz, yfs - 0.003, M["gold"], 0.05, 0.0035)
    # text
    from e3_kit import text_obj, F_SIGN
    lines = [("ARCADE", 2090, 2265, 1110, 1160), ("ABSINTHE", 2085, 2275, 1190, 1240),
             ("PINBALL", 2100, 2270, 1280, 1328), ("POKER", 2125, 2255, 1365, 1410),
             ("&", 2170, 2202, 1425, 1465), ("POOR", 2140, 2250, 1490, 1535),
             ("LIFE", 2155, 2240, 1555, 1600), ("CHOICES", 2120, 2290, 1620, 1670)]
    for i, (t, a, b, c, d) in enumerate(lines):
        text_obj(f"aa_e3_sign_text_{i}_{t.replace('&', 'and')}", C, t, F_SIGN, M["sign_txt"],
                 L.mx(a), L.mx(b), L.mz(c), L.mz(d), yfs - 0.0035, 0.0025)
    # cocktail: glowing lavender-purple neon tube outline, amber liquid, straw
    P = L.px
    yg = yfs - 0.012
    rim_l, rim_r, vb = P(2148, 1762), P(2272, 1762), P(2208, 1832)
    nm = M["neon_cocktail"]
    tube("aa_e3_sign_cocktail_bowl", C, [(x, yg, z) for x, z in (rim_l, rim_r, vb)], 0.011, nm, cyclic=True)
    tube("aa_e3_sign_cocktail_stem", C, [(x, yg, z) for x, z in (vb, P(2208, 1918))], 0.011, nm)
    tube("aa_e3_sign_cocktail_foot", C, [(x, yg, z) for x, z in (P(2160, 1930), P(2208, 1914), P(2256, 1930))],
         0.011, nm, cyclic=True)
    tube("aa_e3_sign_cocktail_straw", C, [(x, yg - 0.006, z) for x, z in (P(2228, 1810), P(2282, 1740))],
         0.006, M["neon_p"])
    mb = MB()
    mb.prism([P(2163, 1772), P(2257, 1772), P(2208, 1825)], yg + 0.002, yfs + 0.001, M["amber"])
    mb.finish("aa_e3_sign_cocktail_liquid", C)
    # neon standoffs (tube clips) so the outline is fastened to the board
    mb = MB()
    for (xc, yc) in ((2160, 1765), (2260, 1765), (2208, 1870), (2208, 1925)):
        x, z = P(xc, yc)
        mb.box(x - 0.006, x + 0.006, yg - 0.002, yfs + 0.001, z - 0.006, z + 0.006, M["black"])
    mb.finish("aa_e3_sign_cocktail_clips", C)


def build_leaf2(M, C, name, d):
    """Iron door leaf: solid stile/rail grid round the openings, bolection mouldings on every opening,
    backlit stained glass, 2x2 purple panes on a cross mullion, raised kick panels with set-in emblems."""
    hx = L.mx(d["hinge"])
    zs = STEP_Z
    thick = 0.06
    yF, yB = Y_HINGE - thick / 2, Y_HINGE + thick / 2
    xo0, xo1, zo0, zo1 = cr(d["outer"][0], d["outer"][1], d["outer"][2], d["outer"][3])
    zo0 = max(zo0, zs + 0.006)
    holes = [cr(*g[:4]) for g in d["glass"]] + [cr(*p) for p in d["p2x2"]]
    mb = MB(jitter=False)
    mb.cells(grid_cells((xo0, xo1, zo0, zo1), holes), yF, yB, M["iron"], M["iron"])
    ob_frame = mb.finish(name, C, bevel=0.004, segments=2)
    obs = [ob_frame]
    mm = MB()
    for i, h in enumerate(holes):
        moulding(mm, *h, yF, M["iron"], w=0.024, proud=0.014 + 0.0017 * i, back=0.002 + 0.0014 * i)
    # outer raised stile edge moulding (the leaf's perimeter bead)
    mm.ring(rect(xo0, xo1, zo0, zo1), rect(xo0 + 0.022, xo1 - 0.022, zo0 + 0.022, zo1 - 0.022),
            yF - 0.01, yF + 0.0009, M["iron"])
    kick_parts = []
    for i, (a, b, c, e, emb, mk) in enumerate(d["kicks"]):
        kf = cr(a, b, c, e)
        moulding(mm, *kf, yF, M["iron"], w=0.022, proud=0.0125 - 0.0011 * i, back=0.0105 + 0.0013 * i)
        frustum(mm, *kf, 0.028, yF + 0.001, yF - 0.013, M["iron"])
        kick_parts.append((kf, emb, mk))
    for (a, b, c, e, mh) in d["handles"]:
        hr = cr(a, b, c, e)
        hxm = (hr[0] + hr[1]) / 2
        mm.box(hxm - 0.009, hxm + 0.009, yF - 0.055, yF - 0.04, hr[2], hr[3], M[mh])
        for zz in (hr[2] + 0.01, hr[3] - 0.01):
            mm.box(hxm - 0.006, hxm + 0.006, yF - 0.042, yF + 0.001, zz - 0.006, zz + 0.006, M[mh])
    obs.append(mm.finish(f"{name}_mouldings", C, bevel=0.004, segments=3))
    # glass at mid-depth, tucked into the frame
    gm = MB(jitter=False)
    for (a, b, c, e, gid) in d["glass"]:
        g = cr(a, b, c, e)
        mi = gm.mi(M[gid])
        gm.uvbox[mi] = g
        gm.box(g[0] - 0.003, g[1] + 0.003, Y_HINGE - 0.003, Y_HINGE + 0.003, g[2] - 0.003, g[3] + 0.003, M[gid])
    obs.append(gm.finish(f"{name}_glass", C))
    # 2x2 purple panes on a cross mullion
    pm = MB(jitter=False)
    for p in d["p2x2"]:
        x0, x1, z0, z1 = cr(*p)
        xm, zm = (x0 + x1) / 2, (z0 + z1) / 2
        gap = 0.014
        for (p0, p1, q0, q1) in ((x0, xm - gap, z0, zm - gap), (xm + gap, x1, z0, zm - gap),
                                 (x0, xm - gap, zm + gap, z1), (xm + gap, x1, zm + gap, z1)):
            pm.box(p0 - 0.004, p1 + 0.004, Y_HINGE - 0.004, Y_HINGE + 0.004, q0 - 0.004, q1 + 0.004, M["pane_p"])
        pm.box(xm - gap, xm + gap, yF - 0.004, yB - 0.01, z0, z1, M["iron"])
        pm.box(x0, x1, yF - 0.0045, yB - 0.011, zm - gap, zm + gap, M["iron"])
    obs.append(pm.finish(f"{name}_panes", C, bevel=0.002))
    # kick emblems in moulded squares + gold filigree on the field
    for k, (kf, emb, mk) in enumerate(kick_parts):
        yk = yF - 0.013
        if emb:
            e = cr(*emb)
            em = MB(jitter=False)
            em.uvbox[em.mi(M[mk])] = e
            em.box(e[0], e[1], yk - 0.003, yk + 0.002, e[2], e[3], M[mk])
            sq = rect(e[0] - 0.02, e[1] + 0.02, e[2] - 0.02, e[3] + 0.02)
            em.ring(sq, rect(e[0] - 0.002, e[1] + 0.002, e[2] - 0.002, e[3] + 0.002), yk - 0.012, yk + 0.002,
                    M["iron"])
            obs.append(em.finish(f"{name}_emblem_{k}", C, bevel=0.003))
        for j, (cx, cz, sx, sz) in enumerate(((kf[0] + 0.04, kf[3] - 0.04, 1, -1), (kf[1] - 0.04, kf[3] - 0.04, -1, -1),
                                              (kf[0] + 0.04, kf[2] + 0.04, 1, 1), (kf[1] - 0.04, kf[2] + 0.04, -1, 1))):
            nm = f"{name}_kick{k}_filigree_{j}"
            filigree_corner(C, nm, cx, cz, sx, sz, yk - 0.003, M["gold"], 0.03, 0.003)
            obs += [bpy.data.objects[f"{nm}_{s}"] for s in ("a", "b", "leaf")]
    # swing inward (+Y) about the hinge
    R = Matrix.Translation((hx, Y_HINGE, 0)) @ Matrix.Rotation(math.radians(d["angle"]) * d["side"], 4, "Z") @ \
        Matrix.Translation((-hx, -Y_HINGE, 0))
    for o in obs:
        o.data.transform(R)
        o.data.update()
    # hinge knuckles on the hinge stile
    hm = MB()
    for zc in (L.mz(1000), L.mz(1550), L.mz(2120)):
        hm.box(hx - 0.012, hx + 0.012, Y_HINGE - 0.045, Y_HINGE - 0.02, zc - 0.05, zc + 0.05, M["iron"])
    hm.finish(f"{name}_hinges", C, bevel=0.004)


# =========================================================================================
# marquee hardware
# =========================================================================================
def bezel(M, C, outline):
    """Thick black bezel with a rounded moulded edge, a stepped inner bead, bolts and corner plates."""
    w = 0.065
    inner = offset_poly(outline, w)
    mb = MB()
    mb.ring(outline, inner, Y_BOARD_F - 0.075, Y_BOARD_F + 0.0085, M["rim"])
    mb.finish("aa_e3_marquee_rim", C, bevel=0.02, segments=5)
    inner2 = offset_poly(outline, w + 0.016)
    mb = MB()
    inner2 = offset_poly(outline, w + 0.007)
    mb.ring(offset_poly(outline, w - 0.004), inner2, Y_BOARD_F - 0.03, Y_BOARD_F - 0.0105, M["rim"])
    mb.finish("aa_e3_marquee_rim_bead", C, bevel=0.006, segments=3)
    # bolts along the bezel centreline, plates at the corners
    mid = offset_poly(outline, w * 0.5)
    bm = bmesh.new()
    n = len(mid)
    yb = Y_BOARD_F - 0.075 - 0.004
    for k in range(n):
        a, b = Vector(mid[k]), Vector(mid[(k + 1) % n])
        ln = (b - a).length
        cnt = max(1, int(ln / 0.3))
        for j in range(cnt):
            p = a + (b - a) * ((j + 0.5) / cnt)
            if min((p - Vector(q)).length for q in mid) < 0.06:      # leave room for the corner plates
                continue
            bmesh.ops.create_cone(bm, cap_ends=True, segments=6, radius1=0.011, radius2=0.011, depth=0.012,
                                  matrix=Matrix.Translation((p.x, yb, p.y)) @ Matrix.Rotation(PI / 2, 4, "X"))
    me = bpy.data.meshes.new("aa_e3_marquee_bolts")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["bolt"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    mb = MB()
    for k in range(n):
        p = Vector(mid[k])
        dy = 0.0013 * (k % 3)
        mb.box(p.x - 0.035, p.x + 0.035, Y_BOARD_F - 0.082 - dy, Y_BOARD_F - 0.07, p.y - 0.025, p.y + 0.025, M["rim"])
    mb.finish("aa_e3_marquee_rim_plates", C, bevel=0.003)


def skull_crest(M, C, cx, cz, yf):
    """Brass skull on a teardrop cartouche with brass rim and side scrolls (crop: apex box)."""
    # cartouche: rounded top, pointed bottom
    pts = []
    for k in range(25):
        a = PI * k / 24
        pts.append((cx + 0.075 * math.cos(a), cz + 0.03 + 0.07 * math.sin(a)))
    pts = pts[::-1]
    pts = [(cx - 0.075, cz + 0.03)] + pts[1:-1] + [(cx + 0.075, cz + 0.03), (cx + 0.055, cz - 0.06), (cx, cz - 0.12),
                                                  (cx - 0.055, cz - 0.06)]
    pts = pts[::-1]
    mb = MB()
    mb.prism(pts, yf - 0.02, yf + 0.005, M["rim"])
    mb.finish("aa_e3_marquee_crest_plate", C, bevel=0.006, segments=3)
    tube("aa_e3_marquee_crest_rim", C, [(x, yf - 0.021, z) for x, z in pts], 0.0055, M["brass"], cyclic=True)
    # skull
    bm = bmesh.new()

    def blob(x, y, z, sx, sy, sz, seg=24):
        mtx = Matrix.Translation((x, y, z)) @ Matrix.Diagonal((sx, sy, sz, 1))
        bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg // 2, radius=1.0, matrix=mtx)
    y0 = yf - 0.045
    blob(cx, y0, cz + 0.022, 0.05, 0.04, 0.052)               # cranium
    blob(cx, y0 - 0.012, cz - 0.012, 0.042, 0.032, 0.03)      # cheekbones / maxilla
    blob(cx - 0.03, y0 - 0.01, cz - 0.004, 0.016, 0.02, 0.016, 12)
    blob(cx + 0.03, y0 - 0.01, cz - 0.004, 0.016, 0.02, 0.016, 12)
    blob(cx, y0 - 0.006, cz - 0.05, 0.03, 0.026, 0.018)       # jaw
    for k in range(6):                                         # teeth
        tx = cx - 0.0175 + k * 0.007
        bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((tx, y0 - 0.036, cz - 0.034)) @
                              Matrix.Diagonal((0.0055, 0.006, 0.01, 1)))
    me = bpy.data.meshes.new("aa_e3_marquee_skull")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["brass"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    me.shade_smooth()
    bm = bmesh.new()
    for ex in (-0.018, 0.018):                                  # eye sockets
        bmesh.ops.create_uvsphere(bm, u_segments=12, v_segments=8, radius=1.0,
                                  matrix=Matrix.Translation((cx + ex, y0 - 0.036, cz + 0.008)) @
                                  Matrix.Diagonal((0.0135, 0.008, 0.014, 1)))
    bmesh.ops.create_cone(bm, cap_ends=True, segments=3, radius1=0.009, radius2=0.0, depth=0.016,
                          matrix=Matrix.Translation((cx, y0 - 0.043, cz - 0.014)) @ Matrix.Rotation(PI / 2, 4, "X"))
    me = bpy.data.meshes.new("aa_e3_marquee_skull_sockets")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["brass_dark"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    # brass scrolls either side and a finial on top
    for s, nm in ((-1, "l"), (1, "r")):
        sp = scroll(cx + s * 0.1, cz + 0.01, 0.03, 1.3, PI / 2, sign=s)
        tube(f"aa_e3_marquee_crest_scroll_{nm}", C, [(cx + s * 0.07, yf - 0.012, cz + 0.06)] +
             [(x, yf - 0.012, z) for x, z in sp], 0.005, M["brass"])
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=12, v_segments=8, radius=0.014,
                              matrix=Matrix.Translation((cx, yf - 0.01, cz + 0.112)))
    me = bpy.data.meshes.new("aa_e3_marquee_crest_finial")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["brass"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    me.shade_smooth()


def chrome_knot(M, C, nm, cx, cz, y, s=0.11, flip=1):
    """Banner end bracket: a heavy chrome diamond with a knotted cross-bar figure and ball knobs."""
    dia = [(cx, cz + s), (cx + s * 0.8, cz), (cx, cz - s), (cx - s * 0.8, cz)]
    tube(f"aa_e3_banner_bracket_{nm}", C, [(x, y, z) for x, z in dia], 0.017, M["chrome"], cyclic=True)
    bars = [
        [(cx - s * 0.55, cz + s * 0.05), (cx - s * 0.1, cz + s * 0.12), (cx + s * 0.25, cz - s * 0.05),
         (cx + s * 0.6, cz - s * 0.02)],
        [(cx - s * 0.05 * flip, cz + s * 0.85), (cx + s * 0.1 * flip, cz + s * 0.3), (cx - s * 0.05 * flip, cz - s * 0.2),
         (cx + s * 0.25 * flip, cz - s * 0.7)],
        [(cx - s * 0.35 * flip, cz - s * 0.35), (cx - s * 0.05 * flip, cz - s * 0.15), (cx + s * 0.3 * flip, cz + s * 0.3)],
    ]
    for k, b in enumerate(bars):
        tube(f"aa_e3_banner_bracket_{nm}_bar{k}", C, [(x, y - 0.014 - 0.005 * k, z) for x, z in b], 0.013,
             M["chrome"])
    bm = bmesh.new()
    for (x, z) in ((cx - s * 0.6, cz + s * 0.05), (cx + s * 0.62, cz - s * 0.02), (cx + s * 0.25 * flip, cz - s * 0.72),
                   (cx - s * 0.36 * flip, cz - s * 0.36), (cx, cz + s * 1.0)):
        bmesh.ops.create_uvsphere(bm, u_segments=14, v_segments=8, radius=0.017,
                                  matrix=Matrix.Translation((x, y - 0.014, z)))
    bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((cx, y + 0.01, cz + s)) @
                          Matrix.Diagonal((0.03, 0.04, 0.03, 1)))
    me = bpy.data.meshes.new(f"aa_e3_banner_bracket_{nm}_knobs")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["chrome"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    me.shade_smooth()


def slogan_traced(M, C, T):
    """The slogan as traced glyph cells (the bible's own rounded techno letterforms)."""
    s = T["slogan"]
    cs = s["cell"]
    L.plane(Y_BANNER_F - 0.004)
    cs_set = {tuple(c) for c in s["cells"]}
    changed = True
    while changed:
        changed = False
        for (c, r) in list(cs_set):
            for dc, dr in ((1, 1), (1, -1)):
                if (c + dc, r + dr) in cs_set and (c + dc, r) not in cs_set and (c, r + dr) not in cs_set:
                    cs_set.add((c + dc, r))
                    changed = True
    cells = []
    for c, r in sorted(cs_set):
        xa = s["x0"] + c * cs
        ya = s["y0"] + r * cs
        cells.append((L.mx(xa), L.mx(xa + cs), L.mz(ya + cs), L.mz(ya)))
    mb = MB(jitter=False)
    mb.cells(cells, Y_BANNER_F - 0.006, Y_BANNER_F + 0.001, M["slogan"], M["slogan"])
    return mb.finish("aa_e3_banner_text", C, bevel=0.0008)


# =========================================================================================
# interior
# =========================================================================================
X_L, X_R, Y_REAR, Z_C, Z_SPRING = -2.4, 1.95, 7.6, 3.0, 2.35


def vault_z(x):
    t = (x - X_L) / (X_R - X_L)
    return Z_SPRING + (Z_C - Z_SPRING) * math.sin(PI * t)


def build_interior2(M, C):
    from e3_kit import F_GAME, text_obj
    zf = STEP_Z
    y0, y1 = Y_INT0, Y_REAR
    mb = MB()
    # floor: subdivided along depth so the forced-perspective warp can bend it
    for k in range(24):
        ya, yb = y0 + (y1 - y0) * k / 24, y0 + (y1 - y0) * (k + 1) / 24
        mb.box(X_L, X_R, ya, yb, zf - 0.02, zf, M["floor"])
    mb.finish("aa_e3_int_floor", C)
    mb = MB()
    mb.box(X_L - 0.1, X_L, y0, y1, zf, Z_SPRING, M["int_wall"])
    mb.box(X_R, X_R + 0.1, y0, y1, zf, Z_SPRING, M["int_wall"])
    mb.box(X_L, X_R, y1, y1 + 0.1, zf, Z_C, M["int_wall"])
    mb.finish("aa_e3_int_shell", C)
    # barrel vault surface
    bm = bmesh.new()
    nx, ny = 24, 12
    vs = [[bm.verts.new((X_L + (X_R - X_L) * i / nx, y0 + (y1 - y0) * j / ny, vault_z(X_L + (X_R - X_L) * i / nx)))
           for i in range(nx + 1)] for j in range(ny + 1)]
    for j in range(ny):
        for i in range(nx):
            bm.faces.new((vs[j][i], vs[j][i + 1], vs[j + 1][i + 1], vs[j + 1][i]))
    me = bpy.data.meshes.new("aa_e3_int_vault")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["int_dark"])
    _uv(me, {}, 1.0)
    ob = bpy.data.objects.new(me.name, me)
    C.objects.link(ob)
    sol = ob.modifiers.new("Solidify", "SOLIDIFY")
    sol.thickness = 0.04
    # arched ribs: rectangular section bands hanging below the vault
    for k, y in enumerate([0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9]):
        outer = [(X_L + (X_R - X_L) * i / 24, vault_z(X_L + (X_R - X_L) * i / 24) + 0.01) for i in range(25)]
        inner = [(x, z - 0.16) for x, z in outer]
        rb = MB()
        rb.prism(outer + inner[::-1], y - 0.07, y + 0.07, M["rib"])
        rb.finish(f"aa_e3_int_rib_{k}", C, bevel=0.012, segments=2)
    # cabinets, silhouettes and the GAME sign are placed after the warp (place_props)
    xv = -1.55
    mb = MB()
    mb.box(xv - 0.1, xv, y0, 0.88, zf, Z_SPRING, M["int_wall"])
    mb.finish("aa_e3_int_vestibule_wall", C)
    tube("aa_e3_int_neon_green", C, [(xv + 0.011, 0.42, zf + 1.9), (xv + 0.011, 0.46, zf + 2.25),
                                     (xv + 0.011, 0.60, zf + 2.4), (xv + 0.011, 0.74, zf + 2.25),
                                     (xv + 0.011, 0.78, zf + 1.9)], 0.012, M["neon_g_int"])
    ov = [(xv + 0.011, 0.9 + 0.06 * math.cos(a), zf + 2.15 + 0.14 * math.sin(a)) for a in
          [i * PI / 12 for i in range(24)]]
    tube("aa_e3_int_neon_oval", C, ov, 0.01, M["neon_o_int"], cyclic=True)


CAB_PROFILE = [(0.0, 0.0), (0.60, 0.0), (0.60, 0.86), (0.76, 0.95), (0.74, 1.03), (0.50, 1.08),
               (0.56, 1.60), (0.70, 1.64), (0.70, 1.88), (0.05, 1.88), (0.0, 1.82)]


def build_cabinet2(M, C, k, xw, y, zf, yaw=0.0, detailed=True, scale=1.0):
    """Upright cabinet: side panels proud of the body with yellow T-moulding, recessed lit screen,
    lit marquee, control deck (joystick, buttons), coin door; front faces +X, then turned by yaw."""
    w = 0.62
    prof = [(xw + px_, zf + pz) for px_, pz in CAB_PROFILE]
    mb = MB()
    mb.prism(prof, y - w / 2 + 0.02, y + w / 2 - 0.02, M["cab"])                     # body
    side_prof = [(x + (0.012 if x > xw + 0.3 else 0.0), z) for x, z in prof]
    for s in (-1, 1):                                                                 # side panels
        ya = y + s * (w / 2 - 0.021)
        mb.prism(side_prof, min(ya, ya + s * 0.022), max(ya, ya + s * 0.022), M["cab"])
    # marquee box (lit) under the overhang
    mm = MB(jitter=False)
    mq = (xw + 0.70, xw + 0.715, y - w / 2 + 0.035, y + w / 2 - 0.035, zf + 1.66, zf + 1.86)
    mi = mm.mi(M[f"mq{k}"])
    mm.box(*mq[:2], *mq[2:4], *mq[4:], M[f"mq{k}"])
    # screen on the sloped face, in a dark bezel
    ang = math.atan2(0.56 - 0.50, 1.60 - 1.08)
    sm = MB(jitter=False)
    sm.box(-0.002, 0.012, -w / 2 + 0.08, w / 2 - 0.08, 0.08, 0.44, M[f"scr{k}"])
    sm.box(-0.006, 0.003, -w / 2 + 0.05, w / 2 - 0.05, 0.05, 0.47, M["cab"])
    sm.transform(Matrix.Translation((xw + 0.50, y, zf + 1.08)) @ Matrix.Rotation(ang, 4, "Y"))
    # control deck: joystick + buttons; coin door with lit slots
    if detailed:
        bm = mb.bm
        bmesh.ops.create_cone(bm, cap_ends=True, segments=10, radius1=0.008, radius2=0.008, depth=0.08,
                              matrix=Matrix.Translation((xw + 0.66, y - 0.12, zf + 1.07)))
        for j, (dy, bmat) in enumerate(((0.0, "btn_r"), (0.06, "btn_y"), (0.12, "btn_b"), (0.18, "btn_r"))):
            mb.box(xw + 0.65, xw + 0.68, y + dy - 0.014, y + dy + 0.014, zf + 1.025, zf + 1.042, M[bmat])
        bb = bmesh.new()
        bmesh.ops.create_uvsphere(bb, u_segments=12, v_segments=8, radius=0.022,
                                  matrix=Matrix.Translation((xw + 0.66, y - 0.12, zf + 1.12)))
        me = bpy.data.meshes.new(f"aa_e3_int_cabinet_{k}_ball")
        bb.to_mesh(me)
        bb.free()
        me.materials.append(M["btn_r"])
        _uv(me, {}, 1.0)
        ball = bpy.data.objects.new(me.name, me)
        C.objects.link(ball)
        mb.box(xw + 0.6, xw + 0.612, y - 0.12, y + 0.04, zf + 0.35, zf + 0.62, M["cab"])     # coin door
        for dy in (-0.08, -0.01):
            mb.box(xw + 0.611, xw + 0.616, y + dy - 0.012, y + dy + 0.012, zf + 0.5, zf + 0.55, M["coin"])
    cx = xw + 0.35
    R = Matrix.Translation((cx, y, zf)) @ Matrix.Rotation(math.radians(yaw), 4, "Z") @ \
        Matrix.Diagonal((scale, scale, scale, 1)) @ Matrix.Translation((-cx, -y, -zf))
    mb.transform(R)
    sm.transform(R)
    mm.transform(R)
    ob = mb.finish(f"aa_e3_int_cabinet_{k}", C, bevel=0.005)
    # screen + marquee get 0..1 UVs on their lit faces
    for part, name, mat_ in ((sm, f"aa_e3_int_cabinet_{k}_screen", M[f"scr{k}"]),
                             (mm, f"aa_e3_int_cabinet_{k}_marquee", M[f"mq{k}"])):
        part.uvbox = {}
        o = part.finish(name, C)
        uv_lit_face(o, mat_)
    if detailed:
        bpy.data.objects[f"aa_e3_int_cabinet_{k}_ball"].data.transform(R)
    # yellow T-moulding following both side profiles
    for s in (-1, 1):
        pts = [tuple(R @ Vector((x, y + s * (w / 2 + 0.002), z))) for x, z in side_prof]
        tube(f"aa_e3_int_cabinet_{k}_trim_{'l' if s < 0 else 'r'}", C, pts, 0.009, M["cab_trim"], cyclic=True)
    return ob


def uv_lit_face(ob, m):
    """0..1 uv_material over the largest face set using material m (projected on its own plane)."""
    me = ob.data
    idx = list(me.materials).index(m)
    polys = [p for p in me.polygons if p.material_index == idx]
    if not polys:
        return
    big = max(polys, key=lambda p: p.area)
    n = big.normal
    t1 = n.cross(Vector((0, 0, 1)))
    if t1.length < 1e-3:
        t1 = n.cross(Vector((1, 0, 0)))
    t1.normalize()
    t2 = n.cross(t1).normalized()
    vs = [me.vertices[i].co for p in polys for i in p.vertices]
    us = [v.dot(t1) for v in vs]
    ws = [v.dot(t2) for v in vs]
    u0, u1, w0, w1 = min(us), max(us), min(ws), max(ws)
    uvm = me.uv_layers["uv_material"]
    for p in polys:
        for li in p.loop_indices:
            co = me.vertices[me.loops[li].vertex_index].co
            uvm.data[li].uv = ((co.dot(t1) - u0) / (u1 - u0 + 1e-9), (co.dot(t2) - w0) / (w1 - w0 + 1e-9))


def build_person2(M, C, k, x, y, zf, h, turn=0.0):
    """Backlit human silhouette: head, neck, shoulders, tapered torso, upper/lower arms, hips, legs, feet."""
    s = h / 1.75
    bm = bmesh.new()

    def ell(px_, pz, rx, ry, rz, seg=16):
        bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg // 2, radius=1.0,
                                  matrix=Matrix.Translation((px_ * s, 0, pz * s)) @ Matrix.Diagonal((rx * s, ry * s, rz * s, 1)))

    def limb(a, b, r0, r1):
        a, b = Vector(a) * s, Vector(b) * s
        d = b - a
        mtx = Matrix.Translation((a + b) / 2) @ d.to_track_quat("Z", "Y").to_matrix().to_4x4()
        bmesh.ops.create_cone(bm, cap_ends=True, segments=10, radius1=r0 * s, radius2=r1 * s, depth=d.length,
                              matrix=mtx)
        bmesh.ops.create_uvsphere(bm, u_segments=8, v_segments=6, radius=r1 * s, matrix=Matrix.Translation(b))
    ell(0, 1.64, 0.085, 0.095, 0.11)                        # head
    limb((0, 0, 1.5), (0, 0, 1.56), 0.045, 0.04)            # neck
    ell(0, 1.36, 0.2, 0.11, 0.15)                           # chest / shoulders
    ell(0, 1.12, 0.16, 0.1, 0.17)                           # waist
    ell(0, 0.93, 0.17, 0.11, 0.1)                           # hips
    for sx in (-1, 1):
        limb((sx * 0.19, 0, 1.42), (sx * 0.24, 0.02, 1.12), 0.045, 0.04)     # upper arm
        limb((sx * 0.24, 0.02, 1.12), (sx * 0.22, -0.04, 0.86), 0.04, 0.032)  # forearm
        limb((sx * 0.09, 0, 0.92), (sx * 0.1, 0, 0.48), 0.07, 0.055)         # thigh
        limb((sx * 0.1, 0, 0.48), (sx * 0.11, 0.02, 0.06), 0.055, 0.04)      # shin
        ell(sx * 0.11, 0.035, 0.05, 0.12, 0.035, 10)                           # foot
    bmesh.ops.transform(bm, matrix=Matrix.Translation((x, y, zf)) @ Matrix.Rotation(math.radians(turn), 4, "Z"),
                        verts=bm.verts)
    me = bpy.data.meshes.new(f"aa_e3_int_silhouette_{k}")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["silh"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    me.shade_smooth()


# ---- forced-perspective floor (after L.compress): raise the floor toward the back so the hall shows
# the bible's floor area from aa_bible_cam; everything below the vault is sheared with it.
FLOOR_REAR_ROW = 1905.0      # crop-04 pixel row where the bible's floor meets the rear of the hall


def floor_dz_rear():
    yr = L.INT_DST_MAX
    xc = -0.3
    zf = L.compress((xc, Y_REAR, STEP_Z))[2]
    lo, hi = zf, zf + 1.5
    for _ in range(40):
        mid = (lo + hi) / 2
        if L.CAM.world_to_crop((xc, yr, mid))[1] > FLOOR_REAR_ROW:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2 - zf


def warp_floor(C):
    dzr = floor_dz_rear()
    y0, yr = Y_INT0, L.INT_DST_MAX
    zc0 = Z_C
    zcr = L.compress((0.0, Y_REAR, Z_C))[2]
    zf0 = STEP_Z
    zfr = L.compress((0.0, Y_REAR, STEP_Z))[2]
    _WARP.update(dzr=dzr, zf0=zf0, zfr=zfr)
    for o in C.all_objects:
        if o.type != "MESH":
            continue
        me = o.data
        for v in me.vertices:
            x, y, z = v.co
            t = min(max((y - y0) / (yr - y0), 0.0), 1.0)
            dz = dzr * t
            zc = zc0 + (zcr - zc0) * t
            zf = zf0 + (zfr - zf0) * t
            if z < zc:
                v.co.z = z + dz * (zc - z) / max(zc - zf, 1e-3)
        me.update()
    return dzr


_WARP = {}


def floor_z(y):
    """Final (compressed + warped) floor height at depth y."""
    w = _WARP
    t = min(max((y - Y_INT0) / (L.INT_DST_MAX - Y_INT0), 0.0), 1.0)
    return w["zf0"] + (w["zfr"] - w["zf0"]) * t + w["dzr"] * t


def ceiling_z(x, y):
    """Underside of the (compressed, warped) vault above (x, y), by ray cast down onto the vault mesh."""
    from mathutils.bvhtree import BVHTree
    o = bpy.data.objects["aa_e3_int_vault"]
    dg = bpy.context.evaluated_depsgraph_get()
    bvh = BVHTree.FromObject(o, dg)
    hit = bvh.ray_cast(Vector((x, y, 0.5)), Vector((0, 0, 1)))
    return hit[0].z if hit[0] is not None else 2.6


def ray_xz(u, v, y):
    """crop-04 pixel -> (x, z) on the plane y (final space; the crop is what aa_bible_cam sees)."""
    d = L.CAM.ray(u + 2296, v + 2099)
    t = (y - L.CAMY) / d[1]
    return (L.CAMX + t * d[0], L.CAMZ + t * d[2])


# image-space props: (crop u centre, crop v top, depth y in the set, yaw, detailed)
CABINETS = [(935, 1280, 1.05, -38.0, True), (1150, 1490, 1.85, -38.0, True), (1215, 1585, 2.3, -38.0, False),
            (1240, 1630, 2.85, -38.0, False), (1258, 1660, 3.38, -38.0, False)]
# figures: crop columns shifted 55 px left, because our right leaf sits ~40 px left of the bible's
# (right jamb fit) and would otherwise hide the main figure
FIGURES = [(1385, 1688, 2.6, 0.0), (1300, 1712, 3.05, 20.0), (1460, 1720, 3.3, -15.0), (1240, 1750, 3.45, 10.0),
           (1530, 1745, 3.55, 0.0)]


def u_fit(u):
    """Shift a crop column with the doorway's jamb fit so props keep their place relative to the leaves
    (measured: ~-25 px at the left leaf, ~-106 px at the right leaf's free edge)."""
    # interfaces v2 moved the right jamb to the bible's pier arris (2.37): the doorway now sits where the bible
    # has it, so the interior needs no compensating shift any more
    return u
GAME_BOX = (1345, 1440, 1475, 1505)       # crop px of the neon box
# pendant lamps: (crop u of the shade centre, crop v of the shade rim, shade width px, depth y).
# Row a is the crop's centre line (two lamps fully visible); row b runs parallel, further right.
LAMPS = [(1265, 1152, 145, 1.0), (1275, 1372, 130, 2.2), (1282, 1530, 85, 3.3)]   # one line down the centre (crop)


def dome_lamp(M, C, name, x, y, z_rim, r, z_ceiling):
    """Industrial dome pendant: dark metal dome on a cord, warm lit inside, bright bulb under the rim."""
    bm = bmesh.new()
    seg, rings = 32, 10
    verts = []
    for i in range(rings + 1):
        a = (PI / 2) * i / rings                     # 0 at the rim, 90 deg at the crown
        rr = r * (0.3 + 0.7 * math.cos(a) ** 1.6)       # flared industrial dome
        zz = z_rim + r * 0.62 * math.sin(a)
        ring = [bm.verts.new((x + rr * math.cos(2 * PI * k / seg), y + rr * math.sin(2 * PI * k / seg), zz))
                for k in range(seg)] if i < rings else [bm.verts.new((x, y, zz))]
        verts.append(ring)
    for i in range(rings - 1):
        for k in range(seg):
            bm.faces.new((verts[i][k], verts[i][(k + 1) % seg], verts[i + 1][(k + 1) % seg], verts[i + 1][k]))
    for k in range(seg):
        bm.faces.new((verts[rings - 1][k], verts[rings - 1][(k + 1) % seg], verts[rings][0]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(f"{name}_shade")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["shade"])
    me.materials.append(M["shade_in"])
    _uv(me, {}, 1.0)
    ob = bpy.data.objects.new(me.name, me)
    C.objects.link(ob)
    sol = ob.modifiers.new("Solidify", "SOLIDIFY")
    sol.thickness = r * 0.04
    sol.material_offset = 1
    sol.offset = -1.0
    me.shade_smooth()
    crown = z_rim + r * 0.62
    tube(f"{name}_cord", C, [(x, y, z_ceiling), (x, y, crown - r * 0.14)], max(0.004, r * 0.03), M["int_dark"])
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=r * 0.16, radius2=r * 0.16, depth=r * 0.4,
                          matrix=Matrix.Translation((x, y, crown - r * 0.3)))     # socket, top below the crown
    bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=10, radius=r * 0.24,
                              matrix=Matrix.Translation((x, y, z_rim + r * 0.06)))
    me = bpy.data.meshes.new(f"{name}_bulb")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["bulb"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    me.shade_smooth()


def place_props(M, C):
    from e3_kit import F_GAME, text_obj
    rows = "aaa"
    for k, (u, v, wpx, y) in enumerate(LAMPS):
        x, z_rim = ray_xz(u_fit(u), v, y)
        x2, _ = ray_xz(u_fit(u) + wpx, v, y)
        r = abs(x2 - x) / 2
        dome_lamp(M, C, f"aa_e3_int_lamp_{rows[k]}{k % 3}", x, y, z_rim, r, ceiling_z(x, y))
    for k, (u, v, y, yaw, det) in enumerate(CABINETS):
        x_top, z_top = ray_xz(u_fit(u), v, y)
        zb = floor_z(y)
        sc_ = (z_top - zb) / 1.88
        build_cabinet2(M, C, k, x_top - 0.62 * sc_, y, zb, yaw=yaw, detailed=det, scale=sc_)
    for k, (u, v, y, turn) in enumerate(FIGURES):
        x, z_top = ray_xz(u_fit(u), v, y)
        zb = floor_z(y)
        build_person2(M, C, k, x, y, zb, z_top - zb, turn)
    yr = L.INT_DST_MAX - 0.09          # clear of the compressed rear wall (y 3.69-3.74)
    gx0, gz1 = ray_xz(u_fit(GAME_BOX[0]), GAME_BOX[1], yr)
    gx1, gz0 = ray_xz(u_fit(GAME_BOX[2]), GAME_BOX[3], yr)
    mb = MB()
    mb.box(gx0, gx1, yr, yr + 0.025, gz0, gz1, M["int_dark"])
    mb.finish("aa_e3_int_game_box", C)
    pad_x, pad_z = (gx1 - gx0) * 0.06, (gz1 - gz0) * 0.18
    text_obj("aa_e3_int_game_sign", C, "GAME", F_GAME, M["game"], gx0 + pad_x, gx1 - pad_x, gz1 - pad_z, gz0 + pad_z,
             yr - 0.012, 0.012)
    tube("aa_e3_int_game_outline", C, [(gx0, yr - 0.004, gz0), (gx1, yr - 0.004, gz0), (gx1, yr - 0.004, gz1),
                                       (gx0, yr - 0.004, gz1)], 0.005, M["neon_o_int"], cyclic=True)


def build_haze(C, M):
    """Warm volumetric haze filling the hall (render-only helper, not part of the kit)."""
    mb = MB()
    mb.box(-2.4, 2.3, Y_INT0 + 0.02, L.INT_DST_MAX - 0.02, STEP_Z + 0.01, 3.05, M["haze"])
    ob = mb.finish("e3_ctx_interior_haze", C)
    return ob


# =========================================================================================
# uv_bake: real non-overlapping unwrap, one packed atlas per kit collection
# =========================================================================================
def finalize(collections):
    """Apply each kit mesh's modifiers, weld/clean degenerate bevel output, fix winding, then restore
    smooth-by-angle shading with a Weighted Normal modifier (no topology change)."""
    dg = bpy.context.evaluated_depsgraph_get()
    n = 0
    for cname in collections:
        for o in list(bpy.data.collections[cname].all_objects):
            if o.type != "MESH":
                continue
            had_mods = bool(o.modifiers)
            if had_mods:
                me = bpy.data.meshes.new_from_object(o.evaluated_get(dg))
                old = o.data
                o.modifiers.clear()
                o.data = me
                if old.users == 0:
                    bpy.data.meshes.remove(old)
            me = o.data
            bm = bmesh.new()
            bm.from_mesh(me)
            bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
            bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-6)
            loose = [v for v in bm.verts if not v.link_faces]
            if loose:
                bmesh.ops.delete(bm, geom=loose, context="VERTS")
            bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
            for e in bm.edges:
                e.smooth = not (e.is_manifold and e.calc_face_angle(0) > math.radians(40)) and e.is_manifold
            for f in bm.faces:
                f.smooth = True
            bm.to_mesh(me)
            bm.free()
            if had_mods:
                wn = o.modifiers.new("WeightedNormal", "WEIGHTED_NORMAL")
                wn.keep_sharp = True
                wn.mode = "FACE_AREA"
            n += 1
    return n


def unwrap_bake(collections):
    vl = bpy.context.view_layer
    res = {}
    for cname in collections:
        obs = [o for o in bpy.data.collections[cname].all_objects if o.type == "MESH"]
        for o in obs:
            o.data.uv_layers.active = o.data.uv_layers["uv_bake"]
            o.select_set(True)
        for o in bpy.context.scene.objects:
            if o not in obs:
                o.select_set(False)
        vl.objects.active = obs[0]
        with bpy.context.temp_override(active_object=obs[0], object=obs[0], selected_objects=obs,
                                       selected_editable_objects=obs):
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_all(action="SELECT")
            r = bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.002, area_weight=0.0,
                                         scale_to_bounds=False)
            bpy.ops.object.mode_set(mode="OBJECT")
        res[cname] = (len(obs), list(r))
        for o in obs:
            o.data.uv_layers.active = o.data.uv_layers["uv_material"]
            o.select_set(False)
    return res
