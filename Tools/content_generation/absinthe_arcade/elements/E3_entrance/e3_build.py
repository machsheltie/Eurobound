"""Build E3 (main entrance: marquee, doorway, interior set) into wip/E3_entrance.blend. Re-runnable.

  blender -b --factory-startup --python e3_build.py -- [--no-save]

Inputs: trace/e3_trace.json (e3_trace.py) and the e3_entrance textures (e3_textures.py).
Everything is modelled at the world origin in aa_kit/<asset_id> collections (pivot "facade":
arch centre, facade plane y=0, sidewalk z=0; street side is -Y). A context wall/arch (collection
e3_context, not part of the kit) is built only so the renders read against the bible.
"""
import math
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e3_kit import *  # noqa: E402,F401,F403
from e3_kit import _principled, _uv  # noqa: E402
import e3_parts2 as P2  # noqa: E402

PLINTH_IN = 0.09


def build_materials():
    M = {}
    M["black"] = mat("m_e3_black_metal", (0.016, 0.017, 0.02), rough=0.55)
    M["rim"] = mat("m_e3_rim_gunmetal", (0.020, 0.024, 0.034), rough=0.25, coat=0.5)
    M["iron"] = mat("m_e3_iron", (0.022, 0.022, 0.021), rough=0.5)
    M["let_g"] = mat_led("m_e3_led_green", tuple(0.2 * x for x in lin(173, 195, 105)), lin(173, 195, 105), 1.0)
    M["let_p"] = mat_led("m_e3_led_purple", tuple(0.2 * x for x in lin(152, 80, 183)), lin(150, 76, 182), 1.0)
    M["side_g"] = mat("m_e3_letter_side_green", (0.035, 0.08, 0.012), rough=0.5)
    M["side_p"] = mat("m_e3_letter_side_grey", (0.09, 0.085, 0.07), rough=0.55)
    M["stud_g"] = glow("m_e3_stud_green", (156, 188, 92), 0.75)
    M["stud_p"] = glow("m_e3_stud_purple", (187, 93, 205), 0.75)
    M["stud_d"] = mat("m_e3_stud_dark", (0.06, 0.06, 0.065), rough=0.3)
    M["stud_o"] = mat("m_e3_stud_olive", (0.17, 0.18, 0.11), rough=0.4)
    M["neon_p"] = glow("m_e3_neon_purple", (215, 140, 228), 1.4)
    M["tr_p"] = mat("m_e3_trace_purple", (0.5, 0.2, 0.65), rough=0.4, emit=(0.5, 0.18, 0.7), estr=0.7)
    M["tr_y"] = mat("m_e3_trace_yellow", (0.65, 0.55, 0.15), rough=0.4, emit=(0.65, 0.55, 0.12), estr=0.5)
    M["tr_g"] = mat("m_e3_trace_green", (0.40, 0.58, 0.14), rough=0.4, emit=(0.4, 0.6, 0.12), estr=0.5)
    M["tr_o"] = mat("m_e3_trace_orange", (0.75, 0.35, 0.10), rough=0.4, emit=(0.75, 0.32, 0.08), estr=0.5)
    M["brass"] = mat("m_e3_brass", (0.80, 0.60, 0.33), rough=0.28, metal=1.0)
    M["chrome"] = mat("m_e3_chrome", (0.86, 0.86, 0.88), rough=0.12, metal=1.0)
    M["gold"] = mat("m_e3_gold_leaf", (0.83, 0.62, 0.26), rough=0.35, metal=1.0)
    M["slogan"] = glow("m_e3_slogan_text", (221, 171, 235), 0.9)
    M["sign_txt"] = glow("m_e3_sign_text", (245, 245, 246), 0.75, base_k=0.6, rough=0.5)
    M["neon_w"] = glow("m_e3_neon_lavender", (246, 240, 250), 1.2)
    M["amber"] = glow("m_e3_cocktail_amber", (233, 192, 91), 0.9)
    M["pane_p"] = glow("m_e3_pane_purple", (175, 75, 195), 0.95, rough=0.2)
    M["inv"] = glow("m_e3_invader_green", (162, 196, 112), 0.85)
    M["token"] = mat_mask_emit("m_e3_token", L.TEX / "e3_emblem_token.png", dark=(0.03, 0.06, 0.02),
                               col=lin(181, 200, 130), estr=0.85)
    M["kick_l"] = mat_mask_emit("m_e3_emblem_kick_l", L.TEX / "e3_emblem_kick_l.png", col=lin(210, 233, 130), estr=1.0)
    M["kick_r"] = mat_mask_emit("m_e3_emblem_kick_r", L.TEX / "e3_emblem_kick_r.png", col=lin(210, 233, 130), estr=1.0)
    M["decal"] = mat_image("m_e3_casing_decal", L.TEX / "e3_decal_marquee.png", rough=0.6, estr=1.0)
    for gid in ("l_transom_a", "l_main", "l_transom_b", "l_purple", "r_transom", "r_main", "strip"):
        M["glass_" + gid] = mat_image(f"m_e3_glass_{gid}", L.TEX / f"e3_glass_{gid}.png", rough=0.15,
                                      estr=0.85, mask=L.TEX / f"e3_glass_{gid}_mask.png")
    M["glass_plain"] = glow("m_e3_glass_plain_green", (147, 163, 74), 0.8, rough=0.15)
    for i in range(14):
        M[f"flyer{i}"] = mat_image(f"m_e3_flyer_{i:02d}", L.TEX / f"e3_flyer_{i:02d}.png", rough=0.7)
    # interior
    M["floor"] = mat("m_e3_checker_floor", (0.5, 0.5, 0.5), rough=0.12)
    nt = M["floor"].node_tree
    ck = nt.nodes.new("ShaderNodeTexChecker")
    ck.inputs["Color1"].default_value = (0.80, 0.79, 0.76, 1)
    ck.inputs["Color2"].default_value = (0.012, 0.012, 0.012, 1)
    ck.inputs["Scale"].default_value = 1.0
    uvn = nt.nodes.new("ShaderNodeUVMap")
    uvn.uv_map = "uv_material"
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Rotation"].default_value = (0, 0, math.radians(45))
    mp.inputs["Scale"].default_value = (1 / 0.62, 1 / 0.62, 1)
    nt.links.new(uvn.outputs["UV"], mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"], ck.inputs["Vector"])
    nt.links.new(ck.outputs["Color"], _principled(M["floor"]).inputs["Base Color"])
    M["concrete"] = mat("m_e3_concrete_step", (0.36, 0.35, 0.33), rough=0.8)
    M["int_dark"] = mat("m_e3_interior_dark", (0.02, 0.018, 0.016), rough=0.7)
    M["int_wall"] = mat("m_e3_interior_wall", (0.035, 0.026, 0.02), rough=0.8)
    M["cab"] = mat("m_e3_cabinet_black", (0.015, 0.015, 0.018), rough=0.35)
    M["cab_trim"] = mat("m_e3_cabinet_yellow_trim", (0.75, 0.55, 0.10), rough=0.35, emit=(0.8, 0.55, 0.1), estr=0.25)
    M["cab_marq"] = glow("m_e3_cabinet_marquee_orange", (235, 130, 40), 1.4)
    M["cab_marq2"] = glow("m_e3_cabinet_marquee_amber", (230, 150, 60), 1.0)
    M["screen"] = glow("m_e3_cabinet_screen", (70, 140, 235), 1.6, rough=0.1)
    M["screen2"] = glow("m_e3_cabinet_screen_dim", (60, 110, 190), 0.8, rough=0.1)
    M["shade"] = mat("m_e3_lamp_shade", (0.06, 0.05, 0.04), rough=0.4, metal=0.0)
    M["bulb"] = mat("m_e3_lamp_bulb", (1.0, 0.8, 0.5), emit=(1.0, 0.72, 0.38), estr=12)
    M["shade_in"] = mat("m_e3_lamp_shade_inner", (0.9, 0.75, 0.5), emit=(1.0, 0.75, 0.42), estr=1.5)
    M["silh"] = mat("m_e3_silhouette", (0.008, 0.007, 0.007), rough=0.9)
    M["game"] = glow("m_e3_neon_game", (240, 90, 30), 2.0)
    M["neon_g_int"] = mat("m_e3_neon_green_interior", (0.5, 0.8, 0.2), emit=(0.55, 0.85, 0.15), estr=1.5)
    M["neon_o_int"] = mat("m_e3_neon_amber_interior", (0.9, 0.6, 0.2), emit=(1.0, 0.6, 0.15), estr=2)
    M["stone_ctx"] = mat("m_e3_context_stone", lin(205, 182, 146), rough=0.85)
    return M


# =========================================================================================
# marquee
# =========================================================================================
TRACES = [   # thin coloured circuit strips on the board: (colour, [canvas points])
    ("p", [(636, 227), (801, 227)]), ("y", [(437, 353), (498, 353)]),
    ("p", [(508, 352), (602, 352), (602, 308)]), ("p", [(326, 367), (376, 367)]),
    ("p", [(422, 358), (422, 394)]), ("y", [(426, 396), (325, 396), (325, 458)]),
    ("y", [(321, 502), (321, 571), (248, 571), (248, 720)]), ("p", [(346, 528), (346, 566)]),
    ("y", [(450, 590), (450, 630)]),
    ("p", [(921, 227), (939, 227)]), ("p", [(1086, 153), (1118, 153)]), ("y", [(1145, 166), (1145, 209)]),
    ("p", [(1189, 226), (1236, 226)]), ("p", [(1246, 226), (1296, 226)]), ("y", [(1325, 233), (1354, 233)]),
    ("o", [(1361, 233), (1393, 233)]), ("y", [(1400, 233), (1435, 233), (1435, 173)]),
    ("p", [(1443, 161), (1493, 161)]), ("p", [(1514, 233), (1543, 233)]), ("y", [(1612, 233), (1612, 246)]),
    ("p", [(1625, 247), (1650, 247)]), ("g", [(1437, 172), (1437, 199)]),
    ("p", [(1771, 256), (1939, 256)]),
    ("p", [(1885, 271), (1912, 322), (1932, 384)]), ("p", [(1934, 382), (2089, 382)]),
    ("y", [(2096, 384), (2164, 384)]), ("y", [(2174, 432), (2220, 432), (2227, 447)]),
    ("y", [(2224, 468), (2224, 536)]), ("g", [(2278, 597), (2298, 597)]),
    ("g", [(1143, 165), (1143, 214)]),
]


def build_marquee(M, C, T):
    P = L.px
    L.use("marquee", Y_BOARD_F)
    outline = [P(x, y) for x, y in T["board_outline"]]
    rim_w = L.mw(24)

    # board plate (decal material carries the apex-box swirls)
    mb = MB()
    dx0, dy0, dx1, dy1 = 150, 20, 2440, 760
    mb.uvbox[mb.mi(M["decal"])] = (L.mx(dx0), L.mx(dx1), L.mz(dy1), L.mz(dy0))
    mb.prism(outline, Y_BOARD_F, Y_BOARD_B, M["decal"], M["black"])
    mb.finish("aa_e3_marquee_board", C, bevel=0.004)

    # thick moulded bezel (round 2)
    P2.bezel(M, C, outline)
    rim_w = 0.065

    # purple neon trim inside the rim on the right flank (crop: from the second step down)
    pts = T["board_outline"]
    k0 = pts.index([2165, 312]) if [2165, 312] in pts else 14
    seg = offset_poly(outline, rim_w + 0.025)[k0:]
    tube("aa_e3_marquee_trim_right", C, [(x, Y_BOARD_F - 0.005, z) for x, z in seg], 0.006, M["neon_p"])

    # apex box: raised dark frame round the skull + its decal face (board decal shows through)
    bx0, by0, bx1, by1 = T["apex_box"]
    ob_o = [P(bx0, by1), P(bx1, by1), P(bx1, by0), P(bx0, by0)]
    mb = MB()
    mb.ring(ob_o, offset_poly(ob_o, L.mw(10)), Y_BOARD_F - 0.03, Y_BOARD_F + 0.005, M["rim"])
    mb.finish("aa_e3_marquee_apex_box", C, bevel=0.004)

    # brass skull crest at the apex
    sx, sz = P(1270, 148)
    P2.skull_crest(M, C, sx, sz - 0.01, Y_BOARD_F - 0.03)
    tube("aa_e3_marquee_skull_hanger", C, [(sx, Y_BOARD_F - 0.04, sz + 0.115), (sx, Y_BOARD_F - 0.04, L.mz(78))],
         0.006, M["tr_o"])

    # pixel studs
    L.plane(Y_BOARD_F - Y_STUD)
    groups = {"green": (M["stud_g"], []), "purple": (M["stud_p"], []), "dark": (M["stud_d"], []),
              "olive": (M["stud_o"], [])}
    for s in T["studs"]:
        groups[s["color"]][1].append(s)
    for colr, (m, studs) in groups.items():
        mb = MB(jitter=False)
        for s in studs:
            x0, x1 = L.mx(s["x0"]), L.mx(s["x1"])
            z0, z1 = L.mz(s["y1"]), L.mz(s["y0"])
            if s.get("hollow"):
                o = [(x0, z0), (x1, z0), (x1, z1), (x0, z1)]
                mb.ring(o, offset_poly(o, min(x1 - x0, z1 - z0) * 0.22), Y_BOARD_F - Y_STUD, Y_BOARD_F + 0.005, m)
            else:
                mb.box(x0, x1, Y_BOARD_F - Y_STUD, Y_BOARD_F + 0.005, z0, z1, m)
        if studs:
            mb.finish(f"aa_e3_marquee_studs_{colr}", C, bevel=0.003)

    # circuit strips
    L.plane(Y_BOARD_F - 0.006)
    tm = {"p": M["tr_p"], "y": M["tr_y"], "g": M["tr_g"], "o": M["tr_o"]}
    for colr in "pygo":
        mb = MB()
        n = 0
        for c, pts_ in TRACES:
            if c != colr:
                continue
            q = [P(*p) for p in pts_]
            k = "pygo".index(colr)                       # stacked strips never coplanar
            mb.prism(polyline_outline(q, L.mw(7)), Y_BOARD_F - 0.006 - 0.0015 * k,
                     Y_BOARD_F + 0.0015 + 0.0013 * k, tm[colr])
            n += 1
        if n:
            mb.finish(f"aa_e3_marquee_traces_{colr}", C)

    # lettering (mapped on their front plane: that is what the bible camera sees)
    L.plane(Y_LET_F)
    for key, mf, ms, nm in (("absinthe", M["let_g"], M["side_g"], "absinthe"),
                            ("arcade", M["let_p"], M["side_p"], "arcade")):
        w = T[key]
        cs = w["cell"]
        for i, Lr in enumerate(w["letters"]):
            cells = []
            for c, r in Lr["cells"]:
                xa = w["origin_x"] + c * cs
                yb = w["baseline_y"] - (r + 1) * cs
                cells.append((L.mx(xa), L.mx(xa + cs), L.mz(yb + cs), L.mz(yb)))
            mb = MB()
            mb.cells(cells, Y_LET_F, Y_BOARD_F + 0.005, mf, ms)
            mb.finish(f"aa_e3_letter_{nm}_{i}_{Lr['char']}", C, bevel=0.005, uv_scale=1.0)

    P2.bead_uvs(C, T["arcade"], "aa_e3_letter_arcade_")
    L.plane(Y_LET_F)

    # flanking icons: token (left of ARCADE) and invader (right)
    L.plane(Y_BOARD_F - 0.05)
    tx0, ty0, tx1, ty1 = T["token_box"]
    cx, cz = P((tx0 + tx1) / 2, (ty0 + ty1) / 2 + 2)
    r = L.mw(96)
    build_token(M, C, cx, cz, r)
    inv = T["invader"]
    cw = (inv["x1"] - inv["x0"]) / inv["cols"]
    ch = (inv["y1"] - inv["y0"]) / inv["rows"]
    cells = [(L.mx(inv["x0"] + c * cw), L.mx(inv["x0"] + (c + 1) * cw),
              L.mz(inv["y0"] + (r_ + 1) * ch), L.mz(inv["y0"] + r_ * ch)) for c, r_ in inv["cells"]]
    mb = MB(jitter=False)
    g = 0.0005                                   # hairline gap: blocks never share verts or planes
    for (a, b, c, d) in cells:
        mb.box(a + g, b - g, Y_BOARD_F - 0.04, Y_BOARD_F + 0.005, c + g, d - g, M["inv"])
    mb.finish("aa_e3_icon_invader", C, bevel=0.003)

    # casing tympanum (arched black metal filling the arch head behind the board)
    build_tympanum(M, C)

    # header ledge behind the slogan bar, plus end caps
    L.plane(Y_LEDGE_F)
    mb = MB()
    mb.box(L.mx(150), L.mx(2440), Y_LEDGE_F, Y_TYMP_F + 0.01, L.mz(848), L.mz(756), M["black"])
    mb.box(L.mx(150), L.mx(2440), Y_LEDGE_F - 0.025, -0.02, L.mz(848), L.mz(832), M["rim"])
    mb.box(L.mx(150), L.mx(212), Y_LEDGE_F - 0.04, -0.02, L.mz(842), L.mz(752), M["rim"])
    mb.box(L.mx(2380), L.mx(2440), Y_LEDGE_F - 0.04, -0.02, L.mz(842), L.mz(752), M["rim"])
    mb.finish("aa_e3_marquee_ledge", C, bevel=0.006)

    build_banner(M, C, T)

    # square-tube standoffs + plates: the board hangs off the arched casing (visibly fastened)
    mb = MB()
    for x in (-1.75, -0.6, 0.6, 1.75):
        for z in (3.25, 4.0 if abs(x) < 1.5 else 3.6):
            mb.box(x - 0.03, x + 0.03, Y_BOARD_B - 0.005, Y_TYMP_F + 0.005, z - 0.03, z + 0.03, M["rim"])
            mb.box(x - 0.07, x + 0.07, Y_TYMP_F - 0.012, Y_TYMP_F + 0.002, z - 0.07, z + 0.07, M["rim"])
    mb.finish("aa_e3_marquee_standoffs", C, bevel=0.003)


def build_skull(M, C, cx, cz, yf):
    """Small brass skull on an oval crest plate."""
    bm = bmesh.new()
    mtx = Matrix.Translation((cx, yf + 0.01, cz)) @ Matrix.Diagonal((0.065, 0.025, 0.085, 1))
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=12, radius=1.0, matrix=mtx)
    mtx = Matrix.Translation((cx, yf - 0.02, cz + 0.015)) @ Matrix.Diagonal((0.042, 0.035, 0.045, 1))
    bmesh.ops.create_uvsphere(bm, u_segments=20, v_segments=12, radius=1.0, matrix=mtx)        # cranium
    mtx = Matrix.Translation((cx, yf - 0.025, cz - 0.03)) @ Matrix.Diagonal((0.026, 0.025, 0.02, 1))
    bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=8, radius=1.0, matrix=mtx)         # jaw
    me = bpy.data.meshes.new("aa_e3_marquee_skull")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["brass"])
    _uv(me, {}, 1.0)
    ob = bpy.data.objects.get(me.name) or bpy.data.objects.new(me.name, me)
    ob.data = me
    if ob.name not in C.objects:
        C.objects.link(ob)
    me.shade_smooth()
    # eye sockets
    bm = bmesh.new()
    for ex in (-0.015, 0.015):
        mtx = Matrix.Translation((cx + ex, yf - 0.05, cz + 0.012)) @ Matrix.Diagonal((0.011, 0.008, 0.012, 1))
        bmesh.ops.create_uvsphere(bm, u_segments=12, v_segments=8, radius=1.0, matrix=mtx)
    me2 = bpy.data.meshes.new("aa_e3_marquee_skull_eyes")
    bm.to_mesh(me2)
    bm.free()
    me2.materials.append(M["iron"])
    _uv(me2, {}, 1.0)
    ob2 = bpy.data.objects.new(me2.name, me2)
    C.objects.link(ob2)


def build_token(M, C, cx, cz, r):
    bm = bmesh.new()
    mtx = Matrix.Translation((cx, Y_BOARD_F - 0.022, cz)) @ Matrix.Rotation(math.radians(90), 4, "X")
    bmesh.ops.create_cone(bm, cap_ends=True, segments=64, radius1=r, radius2=r, depth=0.05, matrix=mtx)
    me = bpy.data.meshes.new("aa_e3_icon_token")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["token"])
    _uv(me, {0: (cx - r * 1.01, cx + r * 1.01, cz - r * 1.01, cz + r * 1.01)}, 1.0)
    ob = bpy.data.objects.new(me.name, me)
    C.objects.link(ob)
    md = ob.modifiers.new("Bevel", "BEVEL")
    md.width = 0.006
    md.segments = 3
    md.limit_method = "ANGLE"
    md.harden_normals = True
    me.shade_smooth()


def ellipse_pts(half, rise, zs, n=48):
    return [(half * math.cos(math.pi * k / n), zs + rise * math.sin(math.pi * k / n)) for k in range(n + 1)][::-1]


def arch_curve(n=48):
    """Mason's masonry intrados (interfaces.json arch): semi-ellipse on the jambs, left to right."""
    half = ARCH["half_width"]
    zs = ARCH["springing_z"]
    rise = ARCH["crown_z"] - zs
    return ellipse_pts(half, rise, zs, n), (-half, half, zs)


def build_tympanum(M, C):
    """Arched black casing filling the arch head behind the marquee (inside the opening)."""
    pts, (xl, xr, zs) = arch_curve()
    L.plane(Y_TYMP_F)
    base = L.mz(760)
    k = 1 - 0.01 / ARCH["half_width"]
    poly = [(xl + 0.01, base)] + [(x * k, z - 0.01) for x, z in pts] + [(xr - 0.01, base)]
    mb = MB()
    mb.uvbox[mb.mi(M["decal"])] = (L.mx(150), L.mx(2440), L.mz(760), L.mz(20))
    mb.prism(poly, Y_TYMP_F, Y_TYMP_B, M["decal"], M["black"])
    mb.finish("aa_e3_marquee_casing_arch", C, bevel=0.004)


def build_banner(M, C, T):
    L.plane(Y_BANNER_F)
    x0, x1 = L.mx(420), L.mx(2160)
    zt, zb = L.mz(745), L.mz(885)
    mid = (zt + zb) / 2
    tip = 0.075
    poly = [(x0, zb), (x1, zb), (x1 + tip, mid), (x1, zt), (x0, zt), (x0 - tip, mid)]
    mb = MB()
    mb.prism(poly, Y_BANNER_F, Y_BANNER_B, M["black"])
    mb.finish("aa_e3_banner_bar", C, bevel=0.004)
    # glowing trim along top and bottom
    for nm, z in (("top", zt - 0.012), ("bottom", zb + 0.012)):
        tube(f"aa_e3_banner_trim_{nm}", C, [(x0 - 0.01, Y_BANNER_F - 0.004, z), (x1 + 0.01, Y_BANNER_F - 0.004, z)],
             0.0075, M["neon_p"])
    # slogan traced off the crop (round 2), chrome knot brackets over the ends
    P2.slogan_traced(M, C, T)
    for nm, cxp, czp, fl in (("left", 437, 800, 1), ("right", 2152, 795, -1)):
        cx, cz = L.px(cxp, czp)
        P2.chrome_knot(M, C, nm, cx, cz, Y_BANNER_F - 0.012, 0.11, fl)


# =========================================================================================
# doorway
# =========================================================================================
def build_doorway(M, C):
    P = L.px
    L.use("door", Y_FRAME_F)
    zs = STEP_Z
    zh = L.mz(885)
    # door head beam
    mb = MB()
    mb.box(L.mx(300), L.mx(2495), Y_FRAME_F - 0.02, Y_INT0, L.mz(935), zh, M["black"])
    mb.finish("aa_e3_door_head", C, bevel=0.004)

    # ---- (1) left fixed outer frame
    mb = MB()
    xa, xb = L.mx(300), L.mx(610)
    mb.box(xa, xb, Y_FRAME_F + 0.02, Y_FRAME_B, zs, L.mz(1040), M["black"])               # body
    mb.box(xa - 0.02, xb + 0.02, Y_FRAME_F - 0.03, Y_FRAME_B, L.mz(1100), L.mz(1040), M["black"])  # cornice
    mb.box(L.mx(395), L.mx(525), Y_FRAME_F, Y_FRAME_B, L.mz(1040), zh - 0.03, M["black"])  # cap box
    mb.box(xa - 0.01, xb + 0.01, Y_FRAME_F - 0.01, Y_FRAME_B, zs, L.mz(1915), M["iron"])    # kick panel
    mb.box(xa, L.mx(345), Y_FRAME_F, Y_FRAME_B, L.mz(1915), L.mz(1100), M["black"])        # panel stiles
    mb.box(L.mx(560), xb, Y_FRAME_F, Y_FRAME_B, L.mz(1915), L.mz(1100), M["black"])
    # lining between the masonry jamb and the frame (the bible shows the frame inset from the jamb)
    jl = ARCH["jamb_x"][0]
    if xa - jl > 0.005:
        mb.box(jl, xa, Y_FRAME_F + 0.08, Y_FRAME_B, zs, zh, M["black"])
    mb.finish("aa_e3_frame_left", C, bevel=0.005)
    # gold border round the flyer panel + gold square inlay on the kick panel
    mb = MB()
    gx0, gx1, gz0, gz1 = L.mx(352), L.mx(553), L.mz(1905), L.mz(1112)
    rect = [(gx0 - 0.004, gz0 - 0.004), (gx1 + 0.004, gz0 - 0.004), (gx1 + 0.004, gz1 + 0.004), (gx0 - 0.004, gz1 + 0.004)]
    mb.ring(rect, offset_poly(rect, 0.008), Y_FRAME_F - 0.004, Y_FRAME_F + 0.0225, M["gold"])
    ix, iz = P(455, 2065)
    sq = [(ix - 0.08, iz - 0.08), (ix + 0.08, iz - 0.08), (ix + 0.08, iz + 0.08), (ix - 0.08, iz + 0.08)]
    mb.ring(sq, offset_poly(sq, 0.014), Y_FRAME_F - 0.016, Y_FRAME_F - 0.008, M["gold"])
    dsq = [(ix, iz - 0.05), (ix + 0.05, iz), (ix, iz + 0.05), (ix - 0.05, iz)]
    mb.ring(dsq, offset_poly(dsq, 0.012), Y_FRAME_F - 0.016, Y_FRAME_F - 0.008, M["gold"])
    mb.finish("aa_e3_frame_left_gold", C)
    # flyers (abstract colour blocks), placed as the crop shows
    flyers = [(380, 1185, 510, 1265, 0), (430, 1270, 530, 1370, -2), (340, 1325, 430, 1440, 3),
              (505, 1380, 590, 1465, -4), (345, 1440, 420, 1510, 2), (420, 1440, 515, 1600, -1),
              (515, 1535, 595, 1625, 3), (520, 1630, 600, 1740, -3), (440, 1600, 505, 1700, 1),
              (425, 1700, 500, 1800, -2), (505, 1745, 560, 1900, 0), (430, 1810, 510, 1900, 2),
              (432, 1130, 462, 1170, 45), (358, 1580, 425, 1640, -1)]
    body_f = Y_FRAME_F + 0.02
    for i, (a, b, c, d, rot) in enumerate(flyers):
        fm = MB(jitter=False)
        x0f, x1f, z0f, z1f = L.mx(a), L.mx(c), L.mz(d), L.mz(b)
        fm.uvbox[fm.mi(M[f"flyer{i}"])] = (x0f, x1f, z0f, z1f)
        fm.box(x0f, x1f, body_f - 0.0011 * (i + 1), body_f + 0.001, z0f, z1f, M[f"flyer{i}"])
        if rot:
            cxf, czf = P((a + c) / 2, (b + d) / 2)
            fm.transform(Matrix.Translation((cxf, 0, czf)) @ Matrix.Rotation(math.radians(rot), 4, "Y") @
                         Matrix.Translation((-cxf, 0, -czf)))
        fm.finish(f"aa_e3_frame_left_flyer_{i:02d}", C)

    # ---- (4) right fixed outer frame: sign panel + green Art Nouveau strip
    mb = MB()
    sx0, sx1 = L.mx(2010), L.mx(2350)
    mb.box(sx0, sx1, Y_FRAME_F + 0.02, Y_FRAME_B, zs, L.mz(1050), M["black"])               # body
    mb.box(sx0 - 0.025, sx1 + 0.02, Y_FRAME_F - 0.03, Y_FRAME_B, L.mz(1050), L.mz(1000), M["black"])  # cap
    mb.box(L.mx(2050), L.mx(2310), Y_FRAME_F - 0.01, Y_FRAME_B, L.mz(1000), L.mz(965), M["black"])
    mb.box(sx0 - 0.01, sx1 + 0.01, Y_FRAME_F - 0.01, Y_FRAME_B, zs, L.mz(2010), M["iron"])  # base panel
    mb.box(L.mx(2040), L.mx(2320), Y_FRAME_F - 0.005, Y_FRAME_F + 0.03, L.mz(2000), L.mz(1055), M["black"])  # sign board
    # strip frame
    mb.box(L.mx(2318), L.mx(2338), Y_FRAME_F, Y_FRAME_B, zs, L.mz(870), M["black"])
    mb.box(L.mx(2468), L.mx(2495), Y_FRAME_F, Y_FRAME_B, zs, L.mz(870), M["black"])
    mb.box(L.mx(2318), L.mx(2495), Y_FRAME_F, Y_FRAME_B, L.mz(882), L.mz(870), M["black"])
    mb.box(L.mx(2318), L.mx(2495), Y_FRAME_F, Y_FRAME_B, zs, L.mz(2000), M["iron"])
    mb.finish("aa_e3_frame_right", C, bevel=0.005)
    plane("aa_e3_frame_right_strip_glass", C, L.mx(2336), L.mx(2468), L.mz(1700), L.mz(880), Y_FRAME_F + 0.06,
          M["glass_strip"])
    plane("aa_e3_frame_right_strip_glass_low", C, L.mx(2336), L.mx(2468), L.mz(2000), L.mz(1700), Y_FRAME_F + 0.06,
          M["glass_plain"])
    mb = MB()
    mb.seg(P(2402, 1700), P(2402, 2000), 0.012, Y_FRAME_F + 0.05, Y_FRAME_F + 0.058, M["iron"])
    mb.finish("aa_e3_frame_right_strip_came", C)
    # sign: gold border with corner curls, 8 white lines, neon cocktail
    yfs = Y_FRAME_F - 0.005
    mb = MB()
    bx0, bx1, bz0, bz1 = L.mx(2062), L.mx(2302), L.mz(1990), L.mz(1078)
    rect = [(bx0 - 0.003, bz0 - 0.003), (bx1 + 0.003, bz0 - 0.003), (bx1 + 0.003, bz1 + 0.003), (bx0 - 0.003, bz1 + 0.003)]
    mb.ring(rect, offset_poly(rect, 0.006), yfs - 0.004, yfs + 0.002, M["gold"])
    mb.seg(P(2100, 1697), P(2310, 1697), 0.005, yfs - 0.004, yfs + 0.002, M["gold"])
    mb.finish("aa_e3_sign_gold_border", C)
    for k, (cx_, cz_, a0) in enumerate(((bx0, bz1, -0.6), (bx1, bz1, 2.2), (bx0, bz0, 0.9), (bx1, bz0, 3.8))):
        sp = spiral(cx_ + (0.03 if k % 2 == 0 else -0.03), cz_ + (-0.03 if k < 2 else 0.03), 0.028, 1.4, 30, a0)
        tube(f"aa_e3_sign_filigree_{k}", C, [(x, yfs - 0.004, z) for x, z in sp], 0.0025, M["gold"])
    lines = [("ARCADE", 2090, 2265, 1110, 1160), ("ABSINTHE", 2085, 2275, 1190, 1240),
             ("PINBALL", 2100, 2270, 1280, 1328), ("POKER", 2125, 2255, 1365, 1410),
             ("&", 2170, 2202, 1425, 1465), ("POOR", 2140, 2250, 1490, 1535),
             ("LIFE", 2155, 2240, 1555, 1600), ("CHOICES", 2120, 2290, 1620, 1670)]
    for i, (t, a, b, c, d) in enumerate(lines):
        text_obj(f"aa_e3_sign_text_{i}_{t.replace('&', 'and')}", C, t, F_SIGN, M["sign_txt"],
                 L.mx(a), L.mx(b), L.mz(c), L.mz(d), yfs - 0.003, 0.003)
    # cocktail: neon outline glass, amber liquid, straw
    yg = yfs - 0.012
    rim_l, rim_r, vb = P(2148, 1762), P(2272, 1762), P(2208, 1832)
    tube("aa_e3_sign_cocktail_bowl", C, [(x, yg, z) for x, z in (rim_l, rim_r, vb)], 0.0045, M["neon_w"], cyclic=True)
    tube("aa_e3_sign_cocktail_stem", C, [(x, yg, z) for x, z in (vb, P(2208, 1918))], 0.0045, M["neon_w"])
    tube("aa_e3_sign_cocktail_foot", C, [(x, yg, z) for x, z in (P(2165, 1928), P(2208, 1915), P(2252, 1928),
                                                               P(2165, 1928))], 0.0045, M["neon_w"])
    tube("aa_e3_sign_cocktail_straw", C, [(x, yg - 0.004, z) for x, z in (P(2232, 1805), P(2280, 1742))],
         0.004, M["neon_p"])
    mb = MB()
    mb.prism([P(2160, 1785), P(2260, 1785), P(2208, 1826)], yg + 0.002, yg + 0.008, M["amber"])
    mb.finish("aa_e3_sign_cocktail_liquid", C)

    # ---- (2)(3) inner doors
    L.plane(Y_HINGE)
    build_left_door(M, C)
    build_right_door(M, C)

    # threshold step: full-width curb in front of the facade, then between the jambs into the doorway
    L.plane(0.0)
    jl, jr = ARCH["jamb_x"]
    mb = MB()
    mb.box(L.mx(110), L.mx(2560), -0.46, 0.0, 0.0, zs, M["concrete"])
    # interfaces v2.1: the pier plinths reach 0.09 m inside both jambs below z 1.03, in front of y 0.02
    mb.box(jl + PLINTH_IN, jr - PLINTH_IN, -0.01, 0.02, 0.0, zs, M["concrete"])
    mb.box(jl, jr, 0.02, Y_INT0 + 0.02, 0.0, zs, M["concrete"])
    mb.finish("aa_e3_threshold_step", C, bevel=0.01)


def leaf_local(hinge_xc, xc):
    return abs(L.mx(xc) - L.mx(hinge_xc))


def build_leaf(M, C, name, hinge_xc, side, parts, angle_deg, thick=0.06):
    """Door leaf built flat (hinge at local x=0, leaf toward `side` = +1 right / -1 left),
    then swung inward about the hinge by angle_deg. parts: list of (kind, xc0, xc1, yc0, yc1, extra)."""
    hx = L.mx(hinge_xc)
    zs = STEP_Z
    mb = MB(jitter=False)
    planes = []
    extra_obs = []
    for kind, a, b, c, d, extra in parts:
        u0, u1 = sorted((leaf_local(hinge_xc, a), leaf_local(hinge_xc, b)))
        x0, x1 = hx + side * u0, hx + side * u1
        z0, z1 = L.mz(d), L.mz(c)
        if kind == "iron":
            rail = abs(z1 - z0) < abs(x1 - x0)
            t2 = thick / 2 - (0.004 if rail else 0.0)          # rails sit 4 mm behind the stiles
            e = 0.0015 if rail else 0.0                         # and stop short of the stiles' planes
            xa, xb = sorted((x0, x1))
            mb.box(xa + e, xb - e, Y_HINGE - t2, Y_HINGE + t2, max(z0, zs + 0.006) + e, z1 - e, M["iron"])
        elif kind == "glass":
            t = 0.006 * (1 if x1 > x0 else -1)
            planes.append((x0 - t, x1 + t, z0 - 0.006, z1 + 0.006, M[extra]))
        elif kind == "pane2x2":
            x0, x1 = sorted((x0, x1))
            gap = 0.016
            xm, zm = (x0 + x1) / 2, (z0 + z1) / 2
            for (p0, p1, q0, q1) in ((x0, xm - gap, z0, zm - gap), (xm + gap, x1, z0, zm - gap),
                                     (x0, xm - gap, zm + gap, z1), (xm + gap, x1, zm + gap, z1)):
                mb.box(p0, p1, Y_HINGE - 0.012, Y_HINGE + 0.004, q0, q1, M["pane_p"])
            mb.box(x0 - 0.02, x1 + 0.02, Y_HINGE - 0.0085, Y_HINGE + 0.0105, z0 - 0.02, z1 + 0.02, M["iron"])
        elif kind == "emblem":
            em = MB(jitter=False)
            ex0, ex1 = sorted((x0, x1))
            em.uvbox[em.mi(M[extra])] = (ex0, ex1, z0, z1)
            yf = Y_HINGE - (thick / 2 - 0.004)              # kick rail face
            em.box(ex0, ex1, yf - 0.0025, yf + 0.004, z0, z1, M[extra])
            extra_obs.append(em.finish(f"{name}_emblem", C))
        elif kind == "handle":
            mb.box(x0, x1, Y_HINGE - thick / 2 - 0.06, Y_HINGE - thick / 2, z0, z1, M[extra])
    obs = list(extra_obs)
    ob = mb.finish(name, C, bevel=0.004)
    obs.append(ob)
    for k, pl in enumerate(planes):
        x0, x1, z0, z1, m = pl[:5]
        yoff = pl[5] if len(pl) > 5 else 0.0
        if side < 0:
            x0, x1 = x1, x0
        obs.append(plane(f"{name}_glass_{k}", C, min(x0, x1), max(x0, x1), z0, z1, Y_HINGE + yoff, m))
    # swing inward (+Y) about the hinge axis
    R = Matrix.Translation((hx, Y_HINGE, 0)) @ Matrix.Rotation(math.radians(angle_deg) * side, 4, "Z") @ \
        Matrix.Translation((-hx, -Y_HINGE, 0))
    for o in obs:
        o.data.transform(R)
        o.data.update()
    return obs


LEFT_HINGE, RIGHT_HINGE = 610, 2030
DOOR_ANGLE_L, DOOR_ANGLE_R = 20.0, 10.0


def build_left_door(M, C):
    top, kick = 915, 1915
    parts = [
        ("iron", 610, 686, top, 2215, None), ("iron", 782, 858, top, 2215, None),
        ("iron", 936, 1030, top, 2215, None), ("iron", 610, 1030, top, 930, None),
        ("iron", 610, 1030, 1090, 1105, None), ("iron", 610, 1030, 1905, 2215, None),
        ("glass", 688, 782, 930, 1090, "glass_l_transom_a"), ("glass", 686, 790, 1105, 1785, "glass_l_main"),
        ("glass", 858, 936, 930, 1090, "glass_l_transom_b"), ("glass", 850, 940, 1105, 1905, "glass_l_purple"),
        ("pane2x2", 692, 788, 1790, 1902, None),
        ("emblem", 706, 776, 1996, 2068, "kick_l"),
    ]
    build_leaf(M, C, "aa_e3_door_left", LEFT_HINGE, +1, parts, DOOR_ANGLE_L)


def build_right_door(M, C):
    top = 915
    parts = [
        ("iron", 1990, 2030, top, 2205, None), ("iron", 1720, 1838, top, 2205, None),
        ("iron", 1720, 2030, top, 935, None), ("iron", 1720, 2030, 1080, 1118, None),
        ("iron", 1720, 2030, 1905, 2205, None),
        ("glass", 1835, 1966, 935, 1080, "glass_r_transom"), ("glass", 1838, 1990, 1118, 1785, "glass_r_main"),
        ("pane2x2", 1842, 1988, 1788, 1902, None),
        ("emblem", 1892, 1974, 2002, 2084, "kick_r"),
        ("handle", 1730, 1748, 1210, 1275, "chrome"), ("handle", 1772, 1790, 1590, 1680, "brass"),
    ]
    build_leaf(M, C, "aa_e3_door_right", RIGHT_HINGE, -1, parts, DOOR_ANGLE_R)


# =========================================================================================
# interior set (only what the doorway shows)
# =========================================================================================
def build_interior(M, C):
    zf = STEP_Z
    x_l, x_r = -2.4, 1.95
    y0, y1 = Y_INT0, 7.6
    zc = 3.0
    mb = MB()
    mb.box(x_l, x_r, y0, y1, zf - 0.02, zf, M["floor"])
    mb.finish("aa_e3_int_floor", C)
    mb = MB()
    mb.box(x_l - 0.1, x_l, y0, y1, zf, zc, M["int_wall"])          # left wall
    mb.box(x_r, x_r + 0.1, y0, y1, zf, zc, M["int_wall"])          # right wall
    mb.box(x_l, x_r, y1, y1 + 0.1, zf, zc, M["int_wall"])          # rear wall
    mb.box(x_l, x_r, y0, y1, zc, zc + 0.1, M["int_dark"])          # ceiling
    mb.finish("aa_e3_int_shell", C)
    # arched ceiling ribs
    for k, y in enumerate([0.9, 2.0, 3.1, 4.2, 5.3, 6.4]):
        w = x_r - x_l
        pts = [(x_l + w * t, y, zc - 0.55 + 0.55 * math.sin(math.pi * t)) for t in [i / 16 for i in range(17)]]
        tube(f"aa_e3_int_rib_{k}", C, pts, 0.05, M["int_dark"])
    # pendant lamps, two rows
    # row a traced: the two lamps the bible shows sit on the line (-0.03, 1.6) -> (-1.31, 6.5)
    for row, dxr in (("a", 0.0), ("b", 1.1)):
        for k, (xr, y) in enumerate([(-0.03, 1.6), (-0.67, 4.05), (-1.31, 6.5)]):
            xr += dxr
            zl = 2.35 - (0.0 if row == "a" else 0.1)
            tube(f"aa_e3_int_lamp_{row}{k}_cord", C, [(xr, y, zc), (xr, y, zl + 0.16)], 0.004, M["int_dark"])
            bm = bmesh.new()
            bmesh.ops.create_cone(bm, cap_ends=False, segments=24, radius1=0.24, radius2=0.05, depth=0.16,
                                  matrix=Matrix.Translation((xr, y, zl + 0.08)))
            me = bpy.data.meshes.new(f"aa_e3_int_lamp_{row}{k}_shade")
            bm.to_mesh(me)
            bm.free()
            me.materials.append(M["shade"])
            me.materials.append(M["shade_in"])
            _uv(me, {}, 1.0)
            ob = bpy.data.objects.new(me.name, me)
            C.objects.link(ob)
            sol = ob.modifiers.new("Solidify", "SOLIDIFY")
            sol.thickness = 0.006
            sol.material_offset = 1
            bm = bmesh.new()
            bmesh.ops.create_uvsphere(bm, u_segments=12, v_segments=8, radius=0.045,
                                      matrix=Matrix.Translation((xr, y, zl + 0.02)))
            bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=0.022, radius2=0.022, depth=0.13,
                                  matrix=Matrix.Translation((xr, y, zl + 0.11)))
            me = bpy.data.meshes.new(f"aa_e3_int_lamp_{row}{k}_bulb")
            bm.to_mesh(me)
            bm.free()
            me.materials.append(M["bulb"])
            _uv(me, {}, 1.0)
            C.objects.link(bpy.data.objects.new(me.name, me))
    # arcade cabinets along the left wall, facing right (+X)
    # free-standing row down the left side, angled toward the door as the bible shows them
    for k, y in enumerate([1.25, 2.2, 3.15, 4.1, 5.05]):
        build_cabinet(M, C, k, -1.95 - 0.08 * k, y, zf, near=(k == 0), yaw=-32.0)
    # silhouettes deeper in
    for k, (x, y, h) in enumerate([(-0.2, 4.6, 1.78), (-0.75, 5.4, 1.7), (0.5, 5.9, 1.74), (-1.1, 6.3, 1.68),
                                   (0.2, 6.8, 1.8)]):
        build_person(M, C, k, x, y, zf, h)
    # neon on the rear wall and the left wall
    gx0, gx1 = -1.95, -1.15
    text_obj("aa_e3_int_game_sign", C, "GAME", F_GAME, M["game"], gx0 + 0.08, gx1 - 0.08, zf + 2.17, zf + 1.97,
             y1 - 0.06, 0.02)
    mb = MB()
    mb.box(gx0, gx1, y1 - 0.05, y1, zf + 1.9, zf + 2.24, M["int_dark"])
    mb.finish("aa_e3_int_game_box", C)
    tube("aa_e3_int_game_outline", C, [(gx0, y1 - 0.055, zf + 1.9), (gx1, y1 - 0.055, zf + 1.9),
                                       (gx1, y1 - 0.055, zf + 2.24), (gx0, y1 - 0.055, zf + 2.24)],
         0.008, M["neon_o_int"], cyclic=True)
    # vestibule return wall on the left (behind the open left leaf) carrying the neon the bible shows
    xv = -1.55
    mb = MB()
    mb.box(xv - 0.1, xv, y0, 0.88, zf, zc, M["int_wall"])
    mb.finish("aa_e3_int_vestibule_wall", C)
    tube("aa_e3_int_neon_green", C, [(xv + 0.011, 0.42, zf + 1.9), (xv + 0.011, 0.46, zf + 2.35),
                                     (xv + 0.011, 0.60, zf + 2.55), (xv + 0.011, 0.74, zf + 2.35),
                                     (xv + 0.011, 0.78, zf + 1.9)], 0.012, M["neon_g_int"])
    ov = [(xv + 0.011, 0.9 + 0.06 * math.cos(a), zf + 2.25 + 0.14 * math.sin(a)) for a in
          [i * math.pi / 12 for i in range(24)]]
    tube("aa_e3_int_neon_oval", C, ov, 0.01, M["neon_o_int"], cyclic=True)


CAB_PROFILE = [(0.0, 0.0), (0.60, 0.0), (0.60, 0.86), (0.74, 0.96), (0.72, 1.03), (0.50, 1.08),
               (0.56, 1.60), (0.68, 1.64), (0.68, 1.88), (0.05, 1.88), (0.0, 1.82)]


def compress_interior(C):
    """Forced perspective along aa_bible_cam rays (Q-011): the set fits the shallow building."""
    for o in C.all_objects:
        if o.type != "MESH":
            continue
        me = o.data
        for v in me.vertices:
            v.co = L.compress(tuple(o.matrix_world @ v.co))
        me.update()


def build_cabinet(M, C, k, xw, y, zf, near=False, yaw=0.0):
    """Upright cabinet: side profile extruded across its width, front facing +X, turned by yaw."""
    w = 0.62
    mb = MB()
    prof = [(xw + px_, zf + pz) for px_, pz in CAB_PROFILE]
    # MB.prism extrudes XZ polygons along Y: the side panels are the XZ faces
    mb.prism(prof, y - w / 2, y + w / 2, M["cab"])
    # marquee panel on the overhang front, screen on the sloped face
    mb.box(xw + 0.676, xw + 0.695, y - w / 2 + 0.03, y + w / 2 - 0.03, zf + 1.67, zf + 1.85,
           M["cab_marq"] if near or k % 2 == 0 else M["cab_marq2"])
    sb = MB()
    sb.box(-0.004, 0.012, -w / 2 + 0.07, w / 2 - 0.07, 0.06, 0.46, M["screen"] if near else M["screen2"])
    ang = math.atan2(0.56 - 0.50, 1.60 - 1.08)
    sb.transform(Matrix.Translation((xw + 0.50, y, zf + 1.08)) @ Matrix.Rotation(ang, 4, "Y"))
    # control deck buttons
    for dy in (-0.12, -0.04, 0.04, 0.12):
        mb.box(xw + 0.64, xw + 0.67, y + dy - 0.015, y + dy + 0.015, zf + 1.0, zf + 1.025, M["cab_trim"])
    cx = xw + 0.34
    R = Matrix.Translation((cx, y, 0)) @ Matrix.Rotation(math.radians(yaw), 4, "Z") @ Matrix.Translation((-cx, -y, 0))
    mb.transform(R)
    sb.transform(R)
    ob = mb.finish(f"aa_e3_int_cabinet_{k}", C, bevel=0.006)
    sb.finish(f"aa_e3_int_cabinet_{k}_screen", C)
    # yellow outline trim round both side panels (follows the profile)
    for side in (-1, 1):
        pts = [(R @ Vector((x, y + side * (w / 2 + 0.004), z))) for x, z in prof]
        tube(f"aa_e3_int_cabinet_{k}_trim_{'l' if side < 0 else 'r'}", C, [tuple(p) for p in pts], 0.008,
             M["cab_trim"], cyclic=True)
    return ob


def build_person(M, C, k, x, y, zf, h):
    bm = bmesh.new()
    s = h / 1.75
    for (cx, cz, rx, ry, rz) in [(0, 1.62, 0.1, 0.11, 0.12), (0, 1.22, 0.22, 0.13, 0.3), (0, 0.85, 0.18, 0.12, 0.2)]:
        mtx = Matrix.Translation((x + cx * s, y, zf + cz * s)) @ Matrix.Diagonal((rx * s, ry * s, rz * s, 1))
        bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=10, radius=1.0, matrix=mtx)
    for lx in (-0.08, 0.08):
        bmesh.ops.create_cone(bm, cap_ends=True, segments=10, radius1=0.065 * s, radius2=0.075 * s, depth=0.8 * s,
                              matrix=Matrix.Translation((x + lx * s, y, zf + 0.4 * s)))
    for ax in (-0.25, 0.25):
        bmesh.ops.create_cone(bm, cap_ends=True, segments=10, radius1=0.045 * s, radius2=0.06 * s, depth=0.6 * s,
                              matrix=Matrix.Translation((x + ax * s, y, zf + 1.1 * s)))
    me = bpy.data.meshes.new(f"aa_e3_int_silhouette_{k}")
    bm.to_mesh(me)
    bm.free()
    me.materials.append(M["silh"])
    _uv(me, {}, 1.0)
    C.objects.link(bpy.data.objects.new(me.name, me))
    me.shade_smooth()


# =========================================================================================
# context (not kit): limestone wall with the arch opening, sidewalk
# =========================================================================================
def build_context(M, C):
    pts, (xl, xr, zs) = arch_curve()
    # wall with the arch opening notched out of its bottom edge (one concave n-gon, no boolean)
    wall = [(-4.2, 0.0), (xl, 0.0)] + pts + [(xr, 0.0), (3.04, 0.0), (3.04, 6.4), (-4.2, 6.4)]
    mb = MB()
    mb.prism(wall, 0.0, Y_INT0, M["stone_ctx"])
    mb.finish("e3_ctx_wall", C)
    # archivolt band between intrados and extrados (mason's numbers), slightly proud
    ext = ellipse_pts(ARCH["extrados_half_width"], ARCH["extrados_rise"], ARCH["springing_z"], 48)
    intr = arch_curve(48)[0]
    band = ext + intr[::-1]
    mb = MB()
    mb.prism(band, -0.06, 0.0, M["stone_ctx"])
    mb.finish("e3_ctx_archivolt", C)
    mb = MB()
    mb.box(-4.2, 4.4, -3.0, 0.0, -0.05, 0.0, M["concrete"])
    mb.finish("e3_ctx_sidewalk", C)


# =========================================================================================
def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    pass
    T = L.load_trace()
    sc = bpy.context.scene
    sc.unit_settings.system = "METRIC"
    sc.unit_settings.scale_length = 1.0
    # fresh scene content
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    kit = coll("aa_kit")
    c_marq = coll("aa_e3_marquee", kit)
    c_door = coll("aa_e3_doorway", kit)
    c_int = coll("aa_e3_interior_set", kit)
    c_ctx = coll("e3_context")
    M = build_materials()
    P2.materials2(M)
    build_marquee(M, c_marq, T)
    P2.build_doorway2(M, c_door)
    P2.build_interior2(M, c_int)
    compress_interior(c_int)
    dz = P2.warp_floor(c_int)
    P2.place_props(M, c_int)
    build_context(M, c_ctx)
    P2.build_haze(c_ctx, M)
    nfin = P2.finalize(["aa_e3_marquee", "aa_e3_doorway", "aa_e3_interior_set"])
    print("E3 FINALIZE", nfin)
    uvr = P2.unwrap_bake(["aa_e3_marquee", "aa_e3_doorway", "aa_e3_interior_set"])
    print("E3 FLOOR raise at rear", round(dz, 3), "UNWRAP", uvr)
    for c in list(bpy.data.collections):
        if c.name.startswith("Collection"):
            bpy.data.collections.remove(c)
    print("E3 BUILD", L.FIT_NOTE, "objects", len(bpy.data.objects))
    if "--no-save" not in args:
        L.WIP.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(L.WIP))
        print("saved", L.WIP)


main()
