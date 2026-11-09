"""E2 window set: parametric parts. All functions append to MB builders in the sill-pivot frame.

Opening: x in [-W/2, W/2], z in [0, H], facade plane y = 0, street -Y, wall +Y.
"""
import math

from mathutils import Matrix, Vector

from e2_lib import MB, arc_pts, cyma, dedupe, ovolo, rng

FLASH_T = 0.012  # sill flashing thickness; flashing top = z 0 (opening bottom)


# ======================================================================================
# Stone
# ======================================================================================
def architrave_profile(band, mold, proj_band, proj_mold, reveal=0.0):
    """Closed (d, p) profile: flat inner band then a moulded outer architrave.

    The inner band is the stone lining between the hole edge (d = band) and the timber frame
    (d = 0); it runs back to the frame face (p = -reveal) so it fills the reveal.
    """
    b, m = band, mold
    pts = [(0.0, -reveal), (0.0, proj_band)]
    pts += [(b * 0.92, proj_band), (b, proj_band + 0.006)]            # small fillet step
    pts += cyma(b, proj_band + 0.006, b + m * 0.45, proj_mold * 0.82, 6)
    pts += [(b + m * 0.55, proj_mold * 0.82), (b + m * 0.6, proj_mold)]
    pts += ovolo(b + m * 0.6, proj_mold, b + m, proj_mold * 0.55, 4)[1:]
    pts += [(b + m, 0.0)]
    if reveal > 0:
        pts += [(b, 0.0), (b, -reveal)]
    return dedupe(pts)


def surround_rect(mb, W, H, band, mold, pb, pm, mat="stone", reveal=0.0):
    path = [Vector((-W / 2, 0, 0)), Vector((-W / 2, 0, H)), Vector((W / 2, 0, H)), Vector((W / 2, 0, 0))]
    mb.sweep(path, architrave_profile(band, mold, pb, pm, reveal), mat)


def crown_cornice(mb, x0, x1, z0, proj, h, mat="stone"):
    """Projecting crown moulding across the head (profile extruded along X), returns top z."""
    p = proj
    prof = [(0.0, z0), (-p * 0.35, z0), (-p * 0.35, z0 + h * 0.15)]
    prof += [(y, z) for (z, y) in [(z0 + h * 0.15 + (h * 0.55) * t, -p * 0.35 - p * 0.55 * (0.5 - 0.5 * math.cos(math.pi * t))) for t in [i / 6 for i in range(1, 7)]]]
    prof += [(-p, z0 + h * 0.75), (-p, z0 + h), (0.0, z0 + h)]
    mb.prism_x(dedupe(prof), x0, x1, mat)
    return z0 + h


def sill_slab(mb, w, proj, back, t, mat="stone", flash=True, nose=0.03):
    """Through-stone sill: top at z=-FLASH_T, front nose with a drip band, back to y=back."""
    zt = -FLASH_T if flash else 0.0
    prof = [(back, zt), (-proj, zt), (-proj, zt - t * 0.55), (-proj + nose, zt - t * 0.62),
            (-proj + nose, zt - t), (back, zt - t)]
    mb.prism_x(prof, -w / 2, w / 2, mat)
    if flash:
        # painted metal cap: top sheet with a rounded drip nose wrapped over the front edge
        r = 0.016
        cap = [(back, 0.0), (-proj, 0.0)]
        for i in range(1, 12):
            a = math.pi / 2 + math.pi * i / 11
            cap.append((-proj + r * math.cos(a), -r + r * math.sin(a)))
        cap += [(-proj + 0.005, -2 * r), (-proj + 0.005, zt), (back, zt)]
        mb.prism_x(dedupe(cap), -w / 2 - 0.012, w / 2 + 0.012, "flash")
    return zt - t


def fascia(mb, w, z_top, h, proj, mat="stone"):
    prof = [(0.0, z_top), (-proj, z_top), (-proj, z_top - h * 0.7), (-proj * 0.7, z_top - h), (0.0, z_top - h)]
    mb.prism_x(prof, -w / 2, w / 2, mat)


def console(mb, xc, cw, z_top, D, Hc, mat="stone", drop=False):
    """Scrolled console bracket (side profile extruded along X), top at z_top, back on y=0."""
    pts = [(0.0, 0.0), (-D, 0.0), (-D, -0.13 * Hc), (-D * 0.9, -0.16 * Hc)]
    # concave sweep down to the scroll
    for i in range(1, 8):
        t = i / 8
        y = -D * (0.9 - 0.5 * math.sin(math.pi / 2 * t))
        z = -0.16 * Hc - t * 0.56 * Hc
        pts.append((y, z))
    # bottom volute (half circle bulging forward)
    cy, cz, r = -D * 0.4, -0.84 * Hc, 0.12 * Hc
    for i in range(1, 9):
        a = math.pi / 2 - math.pi * i / 8
        pts.append((cy - r * math.cos(a), cz + r * math.sin(a)))
    pts += [(cy * 0.75, -Hc), (0.0, -Hc)]
    pts = dedupe([(y, z + z_top) for y, z in pts])
    mb.prism_x(pts, xc - cw / 2, xc + cw / 2, mat)
    # sunk side panel on the front face for the scroll's leaf
    mb.box((xc - cw * 0.28, -D - 0.006, z_top - 0.13 * Hc - 0.02 * Hc), (xc + cw * 0.28, -D + 0.002, z_top - 0.12 * Hc), mat)
    if drop:
        mb.lathe([(0.0, 0.0), (cw * 0.22, 0.0), (cw * 0.18, -0.05), (cw * 0.08, -0.09), (0.0, -0.1)],
                 10, mat, center=(xc, -D * 0.3, z_top - Hc + 0.001), cap_bottom=False, cap_top=True)


def offset_poly(poly, d):
    """Mitred inward (d>0) offset of a CCW polygon [(x, z)]."""
    n = len(poly)
    out = []
    for i in range(n):
        p0, p1, p2 = Vector(poly[i - 1]), Vector(poly[i]), Vector(poly[(i + 1) % n])
        e1 = (p1 - p0).normalized()
        e2 = (p2 - p1).normalized()
        n1 = Vector((-e1.y, e1.x))
        n2 = Vector((-e2.y, e2.x))
        m = (n1 + n2)
        m = m.normalized() if m.length > 1e-9 else n1
        k = d / max(m.dot(n1), 0.3)
        out.append(tuple(p1 + m * k))
    return out


def chamfer_block(mb, poly, t, c, mat="stone", y0=0.0):
    """Polygon [(x, z)] CCW (seen from the street) extruded to depth t toward -Y with a front chamfer c."""
    inner = offset_poly(poly, c)
    n = len(poly)
    vs = [(x, y0, z) for x, z in poly] + [(x, y0 - (t - c), z) for x, z in poly] + [(x, y0 - t, z) for x, z in inner]
    fs = [tuple(range(n))]
    for i in range(n):
        j = (i + 1) % n
        fs.append((i, j, n + j, n + i))
        fs.append((n + i, n + j, 2 * n + j, 2 * n + i))
    fs.append(tuple(reversed(range(2 * n, 3 * n))))
    mb.add(vs, fs, mat)


# ======================================================================================
# Joinery: cased frame and sashes
# ======================================================================================
def cased_frame(mb, W, H, y0, fw, fd, mat="wood", arch=False):
    """Box frame lining the opening. fw = visible face width, fd = depth (y0 .. y0+fd)."""
    if not arch:
        mb.box((-W / 2, y0, 0.0), (-W / 2 + fw, y0 + fd, H), mat)
        mb.box((W / 2 - fw, y0, 0.0), (W / 2, y0 + fd, H), mat)
        mb.box((-W / 2 + fw, y0, H - fw), (W / 2 - fw, y0 + fd, H), mat)
    else:
        s = H - W / 2
        path = [Vector((W / 2, y0, 0.0)), Vector((W / 2, y0, s))]
        path += [Vector((W / 2 * math.cos(a), y0, s + W / 2 * math.sin(a))) for a in [math.pi * i / 24 for i in range(1, 24)]]
        path += [Vector((-W / 2, y0, s)), Vector((-W / 2, y0, 0.0))]
        prof = [(0.0, 0.0), (fw, 0.0), (fw, -fd), (0.0, -fd)]
        mb.sweep(path, prof, mat, normal=(0, -1, 0))
    # timber sill: sloped weathering, projects 0.025 in front of the frame
    prof = [(y0 + fd, 0.001), (y0 - 0.025, 0.001), (y0 - 0.025, 0.018), (y0 + 0.02, 0.04), (y0 + fd, 0.04)]
    mb.prism_x(prof, -W / 2 + fw - 0.001, W / 2 - fw + 0.001, mat)


def sash(mb, x0, x1, z0, z1, y0, sd, sw, top_rail, bot_rail, mullions=0, transoms=0, bar=0.024,
         bar_d=None, mat="wood", glass=True):
    """Rectangular sash: stiles, rails, glazing bars, one glass sheet."""
    bar_d = bar_d or sd * 0.7
    mb.box((x0, y0, z0), (x0 + sw, y0 + sd, z1), mat)
    mb.box((x1 - sw, y0, z0), (x1, y0 + sd, z1), mat)
    mb.box((x0 + sw, y0, z1 - top_rail), (x1 - sw, y0 + sd, z1), mat)
    mb.box((x0 + sw, y0, z0), (x1 - sw, y0 + sd, z0 + bot_rail), mat)
    gx0, gx1, gz0, gz1 = x0 + sw, x1 - sw, z0 + bot_rail, z1 - top_rail
    yb = y0 + (sd - bar_d) / 2
    for k in range(1, mullions + 1):
        xc = gx0 + (gx1 - gx0) * k / (mullions + 1)
        mb.box((xc - bar / 2, yb, gz0), (xc + bar / 2, yb + bar_d, gz1), mat)
    for k in range(1, transoms + 1):
        zc = gz0 + (gz1 - gz0) * k / (transoms + 1)
        mb.box((gx0, yb, zc - bar / 2), (gx1, yb + bar_d, zc + bar / 2), mat)
    if glass:
        yg = y0 + sd * 0.5
        mb.box((gx0 - 0.004, yg - 0.002, gz0 - 0.004), (gx1 + 0.004, yg + 0.002, gz1 + 0.004), "glass")
    return (gx0, gx1, gz0, gz1)


def sash_window(objs, W, H, P):
    """Builds the cased frame + upper (fixed) and lower (sliding) sashes.

    Returns dict of MB builders: frame, sash_upper, sash_lower (lower authored CLOSED at its own
    origin = bottom centre of the sash; the pose offset goes on object location z).
    """
    R = P["reveal"]
    fw, fd = P["frame_w"], P["frame_d"]
    sd = 0.042
    frame = MB()
    cased_frame(frame, W, H, R, fw, fd)
    # parting bead between the tracks + inner staff bead (thin strips on the pulley stiles)
    for sx in (-1, 1):
        x_in = sx * (W / 2 - fw)
        frame.box((min(x_in, x_in - sx * 0.012), R + 0.058, 0.04), (max(x_in, x_in - sx * 0.012), R + 0.066, H - fw - 0.012), "wood")
    frame.box((-W / 2 + fw, R + 0.058, H - fw - 0.012), (W / 2 - fw, R + 0.066, H - fw), "wood")
    zt = H - fw
    zb = 0.04
    split = zb + (zt - zb) * (1 - P["upper_frac"])
    mr = 0.036  # meeting rail
    up = MB()
    sash(up, -W / 2 + fw, W / 2 - fw, split - mr * 0.5, zt, R + 0.014, sd, P["stile"], P["stile"], mr,
         mullions=P["upper_mullions"])
    lo = MB()
    lo_h = split + mr * 0.5 - zb
    sash(lo, -W / 2 + fw, W / 2 - fw, 0.0, lo_h, R + 0.07 - 0.0, sd, P["stile"], mr, P["bottom_rail"],
         mullions=P["lower_mullions"])
    travel_max = zt - (zb + lo_h)
    return {"frame": frame, "sash_upper": up, "sash_lower": lo}, zb, travel_max


# ======================================================================================
# Arched window (L1)
# ======================================================================================
def tracery_quarter(mb, cx, cz, R, side, y, r_bar, seed=1):
    """Interlaced-arc tracery clipped to a quarter-circle pane (side -1 left, +1 right)."""
    def inside(x, z):
        dx, dz = x - cx, z - cz
        return dz > r_bar * 1.2 and dx * side > r_bar * 1.2 and dx * dx + dz * dz < (R - r_bar * 1.2) ** 2

    arcs = []
    # concentric inner arc
    arcs.append((cx, cz, R * 0.52))
    # intersecting arcs springing from the bottom rail
    for k, fx in enumerate((0.15, 0.55, 0.95)):
        arcs.append((cx + side * R * fx, cz, R * 0.55))
    # arcs hung from the outer rim (pointed net)
    for ang in (75, 50, 25):
        a = math.radians(ang)
        arcs.append((cx + side * R * math.cos(a), cz + R * math.sin(a), R * 0.48))
    for ai, (ax, az, r) in enumerate(arcs):
        yy = y + (ai - (len(arcs) - 1) / 2) * 0.0022   # interlace depth: crossing bars never share a plane
        run = []
        for i in range(181):
            a = 2 * math.pi * i / 180
            x, z = ax + r * math.cos(a), az + r * math.sin(a)
            if inside(x, z):
                run.append((x, yy, z))
            else:
                if len(run) > 2:
                    mb.tube(run, r_bar, "wood", sides=4)
                run = []
        if len(run) > 2:
            mb.tube(run, r_bar, "wood", sides=4)


# L1 fanlight leaded tracery, traced from crop bible_w1 (crop px). Each pane is mapped from its pixel
# box (outer edge, mullion edge, transom, top at the mullion) onto the pane and clipped to the arch.
FAN_BOX = {-1: dict(x_out=165, x_in=302, y_bot=455, y_top=355), 1: dict(x_out=482, x_in=345, y_bot=440, y_top=352)}
FAN_LINES = {
    -1: [[(232, 372), (265, 404), (298, 432)],
         [(222, 445), (262, 410), (298, 384)],
         [(262, 410), (250, 430), (240, 455)],
         [(250, 430), (222, 440)],
         [(283, 372), (284, 410), (282, 452)],
         [(284, 410), (298, 418)],
         [(200, 445), (215, 415), (245, 385), (275, 365)],
         [(205, 452), (196, 440), (204, 428)]],
    1: [[(348, 362), (375, 382), (400, 400), (440, 430)],
        [(350, 425), (378, 395), (400, 372), (415, 352)],
        [(398, 356), (420, 382), (445, 412)],
        [(388, 420), (425, 390), (468, 358)],
        [(398, 378), (404, 388), (398, 396), (392, 390), (396, 382)],
        [(442, 410), (465, 400), (480, 395)],
        [(430, 352), (440, 365), (452, 360)]],
}


def ell(a, b, s, t):
    return a * math.cos(t), s + b * math.sin(t)


def traced_fanlight(mb, rin, rise_in, s, mull, y, r_bar):
    for side, lines in FAN_LINES.items():
        bx = FAN_BOX[side]

        def to_pane(px, pz):
            u = (px - bx["x_in"]) / (bx["x_out"] - bx["x_in"])          # 0 at mullion, 1 at outer edge
            v = (bx["y_bot"] - pz) / (bx["y_bot"] - bx["y_top"])        # 0 at transom, 1 at top
            x = side * (mull / 2 + u * (rin - mull / 2))
            z = s + v * rise_in * 0.98
            return x, z

        def inside(x, z):
            if z < s + r_bar or abs(x) < mull / 2 + r_bar * 0.5:
                return False
            return (x / (rin - r_bar)) ** 2 + ((z - s) / (rise_in - r_bar)) ** 2 < 1.0
        for li, line in enumerate(lines):
            # each traced line becomes one smooth curving bar: bowed as a whole (direction alternating
            # line to line, so neighbours interlace as loops) through a Catmull-Rom curve, with a small
            # closing curl at its free end (crop w1top: curving loops and S-curls)
            (ax, ay), (bx2, by2) = line[0], line[-1]
            L = max(((bx2 - ax) ** 2 + (by2 - ay) ** 2) ** 0.5, 1e-6)
            nx, ny = -(by2 - ay) / L, (bx2 - ax) / L
            sg = 1 if li % 2 == 0 else -1
            m = len(line) - 1
            bowed = []
            for i, (px, py) in enumerate(line):
                t = i / max(m, 1)
                b = sg * 0.18 * L * math.sin(math.pi * t)
                bowed.append((px + nx * b, py + ny * b))
            if len(bowed) == 2:
                (ax, ay), (bx2, by2) = bowed
                bowed.insert(1, ((ax + bx2) / 2 + nx * sg * 0.18 * L, (ay + by2) / 2 + ny * sg * 0.18 * L))
            ex, ey = bowed[-1]
            dx, dy = ex - bowed[-2][0], ey - bowed[-2][1]
            dl = max((dx * dx + dy * dy) ** 0.5, 1e-6)
            dx, dy = dx / dl, dy / dl
            rc = 9.0   # curl radius (crop px, ~2.6 mm each): stays above the bar radius so the tube never folds
            cxp, cyp = ex - dy * rc * sg, ey + dx * rc * sg
            a0 = math.atan2(ey - cyp, ex - cxp)
            for k in range(1, 7):
                aa = a0 + sg * k * 0.9
                rr = rc * (1 - 0.05 * k)
                bowed.append((cxp + rr * math.cos(aa), cyp + rr * math.sin(aa)))
            pts = [to_pane(px, pz) for px, pz in catmull(bowed, 8)]
            yy = y + (li - len(lines) / 2) * 0.0021
            run = []
            for x, z in pts:
                if inside(x, z):
                    run.append((x, yy, z))
                else:
                    if len(run) > 9:   # drop clipped slivers that would float free
                        mb.tube(run, r_bar, "wood", sides=6)
                    run = []
            if len(run) > 9:   # drop clipped slivers that would float free
                mb.tube(run, r_bar, "wood", sides=6)


def arched_window(W, H, P):
    """Arched cased frame with an elliptical head (rise = rise_frac * W/2), fixed fanlight with traced
    leaded tracery either side of a broad central mullion, and the lower sash."""
    R = P["reveal"]
    fw, fd = P["frame_w"], P["frame_d"]
    rise = P.get("rise_frac", 1.0) * W / 2
    s = H - rise
    frame = MB()
    # cased frame along the elliptical head
    path = [Vector((W / 2, R, 0.0)), Vector((W / 2, R, s))]
    path += [Vector((*[ell(W / 2, rise, s, math.pi * i / 32)][0][:1], R, ell(W / 2, rise, s, math.pi * i / 32)[1]))
             for i in range(1, 32)]
    path += [Vector((-W / 2, R, s)), Vector((-W / 2, R, 0.0))]
    frame.sweep(path, [(0.0, 0.0), (fw, 0.0), (fw, -fd), (0.0, -fd)], "wood", normal=(0, -1, 0))
    prof = [(R + fd, 0.001), (R - 0.025, 0.001), (R - 0.025, 0.018), (R + 0.02, 0.04), (R + fd, 0.04)]
    frame.prism_x(prof, -W / 2 + fw - 0.001, W / 2 - fw + 0.001, "wood")
    rin = W / 2 - fw
    rise_in = rise - fw
    tr = 0.065
    mull = 0.07
    # transom keyed 1 cm into the jambs (no end faces on the jamb faces)
    frame.box((-rin - 0.01, R + 0.01, s - tr), (rin + 0.01, R + 0.07, s), "wood")
    frame.box((-mull / 2, R + 0.014, s - 0.002), (mull / 2, R + 0.066, s + rise_in - 0.004), "wood")
    n = 40
    # fanlight glass: its lower edge sits 1 cm down inside the transom (no face on the transom top)
    poly = [ell(rin, rise_in, s, math.pi * i / n) for i in range(n + 1)]
    poly = [poly[0][:1] + (s - 0.01,)] + poly + [poly[-1][:1] + (s - 0.01,)]
    yg = R + 0.04
    frame.prism_y(poly, yg - 0.002, yg + 0.002, "glass")
    traced_fanlight(frame, rin, rise_in, s, mull, R + 0.024, 0.006)
    lo = MB()
    sash(lo, -rin, rin, 0.0, s - tr - 0.04, R + 0.07, 0.042, P["stile"], P["stile"], P["bottom_rail"],
         mullions=P["lower_mullions"], bar=P.get("bar", 0.05))
    return {"frame": frame, "sash_lower": lo}, 0.04, s


def arch_surround(mb, W, H, P):
    """Moulded arched architrave on the elliptical head: inner lining band, a slim voussoir ring and an
    outer moulding (crop w1)."""
    rise = P.get("rise_frac", 1.0) * W / 2
    s = H - rise
    b1, b2, b3 = P["band"], P["ring"], P["mold"]

    def path():
        pts = [Vector((-W / 2, 0, 0)), Vector((-W / 2, 0, s))]
        for i in range(1, 40):
            x, z = ell(W / 2, rise, s, math.pi - math.pi * i / 40)
            pts.append(Vector((x, 0, z)))
        pts += [Vector((W / 2, 0, s)), Vector((W / 2, 0, 0))]
        return pts
    R = P.get("reveal", 0.0)
    inner = [(0.0, -R), (0.0, 0.022), (b1, 0.022), (b1, -R)]
    mb.sweep(path(), inner, "stone")
    o0 = b1 + b2 + 0.002
    outer = [(o0, 0.0), (o0, 0.045), (o0 + b3 * 0.3, 0.05)] + cyma(o0 + b3 * 0.3, 0.05, o0 + b3, 0.018, 5)[1:] + [(o0 + b3, 0.0)]
    mb.sweep(path(), dedupe(outer), "stone")
    nv = P["voussoirs"]
    gap = 0.0015
    a0r, b0r = W / 2 + b1, rise + b1
    a1r, b1r = W / 2 + b1 + b2, rise + b1 + b2
    for i in range(nv):
        t0 = math.pi - math.pi * i / nv - 0.004
        t1 = math.pi - math.pi * (i + 1) / nv + 0.004
        key = (i == nv // 2)
        ext = 0.03 if key else 0.0
        pts = [ell(a0r, b0r, s, t0 + (t1 - t0) * k / 4) for k in range(5)]
        pts += [ell(a1r + ext, b1r + ext, s, t1 + (t0 - t1) * k / 4) for k in range(5)]
        area = sum(pts[k][0] * pts[(k + 1) % len(pts)][1] - pts[(k + 1) % len(pts)][0] * pts[k][1] for k in range(len(pts)))
        if area < 0:
            pts = pts[::-1]
        chamfer_block(mb, pts, 0.05 if not key else 0.065, 0.006, y0=0.004)
    nb = P["jamb_blocks"]
    for side in (-1, 1):
        for k in range(nb):
            z0 = s * k / nb + gap
            z1 = s * (k + 1) / nb - gap
            xa, xb = side * a0r, side * a1r
            pts = [(min(xa, xb), z0), (max(xa, xb), z0), (max(xa, xb), z1), (min(xa, xb), z1)]
            chamfer_block(mb, pts, 0.05, 0.006, y0=0.004)
    return s + b1r + 0.03


# ======================================================================================
# Ironwork
# ======================================================================================
def scroll_c(cx, cz, r, a0, turns, sgn=1, n=28):
    """Spiral C-scroll centred at (cx, cz): radius shrinks to 30% over `turns`."""
    pts = []
    for i in range(n + 1):
        t = i / n
        a = a0 + sgn * 2 * math.pi * turns * t
        rr = r * (1 - 0.7 * t)
        pts.append((cx + rr * math.cos(a), cz + rr * math.sin(a)))
    return pts


def railing(mb, x0, x1, h, y_fn, posts, finials, seed=3, r_bar=0.007, belly=False):
    """Wrought-iron flower guard. y_fn(z) gives the railing's front plane y at height z (bombé).

    Each element family sits at its own small depth offset so crossing bars never share a plane.
    """
    def P3(x, z, dy=0.0):
        return (x, y_fn(z) + dy, z)
    # rails
    for z in (0.012, h * 0.12, h - 0.012):
        mb.tube([P3(x0, z, 0.0045), P3(x1, z, 0.0045)], r_bar * (1.6 if z > h * 0.5 else 1.2), "iron", sides=6)
    # handrail cap (flat bar)
    mb.tube([P3(x0 - 0.01, h), P3(x1 + 0.01, h)], r_bar * 2.0, "iron", sides=8)
    # posts
    for px in posts:
        pts = [P3(px, z) for z in [h * i / 10 for i in range(11)]]
        mb.tube(pts, r_bar * 1.6, "iron", sides=6)
    # finials
    for px, kind in finials:
        x, y, z = P3(px, h)
        if kind == "urn":
            mb.lathe([(0.0, 0.0), (0.012, 0.0), (0.016, 0.01), (0.008, 0.02), (0.018, 0.035), (0.016, 0.05),
                      (0.006, 0.06), (0.01, 0.068), (0.0, 0.08)], 10, "iron", center=(x, y, z - 0.004), cap_top=True)
        else:
            mb.sphere((x, y, z + 0.016), 0.015, "iron", seg=10, rings=6)
    # infill: S-scroll pairs + rings between bars
    nb = max(2, int(round((x1 - x0) / (h * 0.55))))
    bw = (x1 - x0) / nb
    zl, zh = h * 0.12, h - 0.012
    zm = (zl + zh) / 2
    for i in range(nb):
        cx = x0 + bw * (i + 0.5)
        r = min(bw, zh - zl) * 0.26
        for sgn in (-1, 1):
            # upper and lower C-scrolls mirrored about the bay centre (lyre motif)
            up = scroll_c(cx + sgn * r * 0.95, zm + r * 0.95, r, math.pi if sgn > 0 else 0.0, 0.85, sgn=-sgn)
            lo = scroll_c(cx + sgn * r * 0.95, zm - r * 0.95, r, math.pi if sgn > 0 else 0.0, 0.85, sgn=sgn)
            for sc, dy in ((up, -0.003 if sgn > 0 else -0.0015), (lo, 0.0015 if sgn > 0 else 0.003)):
                mb.tube([P3(x, z, dy) for x, z in sc], r_bar * 0.8, "iron", sides=5)
        # central vertical tying the scrolls into the rails
        mb.tube([P3(cx, z, -0.0045) for z in [zl + (zh - zl) * k / 8 for k in range(9)]], r_bar * 0.8, "iron", sides=5)
        # cast boss where the scrolls meet the centre bar
        mb.sphere(P3(cx, zm, -0.0045), r_bar * 1.5, "iron", seg=8, rings=6)
        # bay divider bars
        if i > 0:
            xb = x0 + bw * i
            mb.tube([P3(xb, z, -0.0075) for z in [zl + (zh - zl) * k / 8 for k in range(9)]], r_bar, "iron", sides=5)


def side_returns(mb, x, y_front, y_back, h, r_bar=0.007):
    y_back = y_back + 0.012  # key the return into the stone so no face sits on the moulding
    for z in (0.012, h - 0.012):
        mb.tube([(x, y_front, z), (x, y_back, z)], r_bar * 1.4, "iron", sides=6)
    # post foot sunk 4 mm into the slab: its cap no longer shares the z=0 plane with the surround's foot
    mb.tube([(x, y_back, -0.004), (x, y_back, h)], r_bar * 1.4, "iron", sides=6)
    n = max(2, int(abs(y_back - y_front) / 0.06))
    for k in range(1, n):
        y = y_front + (y_back - y_front) * k / n
        mb.tube([(x, y, 0.012), (x, y, h - 0.012)], r_bar * 0.8, "iron", sides=5)


# ======================================================================================
# Pots, plants, flowers
# ======================================================================================
def pot(mb, c, rt, h, rb=None, mat="terracotta", rim=0.18, bulge=0.0):
    rb = rb if rb is not None else rt * 0.72
    x, y, z = c
    th = max(0.006, rt * 0.06)
    rim_h = h * rim
    prof = [(0.0, 0.0), (rb, 0.0)]
    for i in range(1, 6):
        t = i / 6
        r = rb + (rt - rb) * t + bulge * math.sin(math.pi * t) * rt
        prof.append((r, (h - rim_h) * t))
    prof += [(rt + th * 1.2, h - rim_h), (rt + th * 1.3, h - rim_h * 0.15), (rt + th * 0.8, h),
             (rt - th * 0.4, h), (rt - th * 0.6, h - rim_h * 0.5), (rt * 0.92 - th, h * 0.86), (0.0, h * 0.86)]
    mb.lathe(prof, 28, mat, center=(x, y, z), cap_bottom=True, cap_top=False)
    soil_z = z + h * 0.86
    # soil mound touching the pot wall
    r_s = rt * 0.92 - th
    mb.lathe([(r_s + 0.002, 0.0), (r_s * 0.8, 0.006), (0.0, 0.012)], 20, "soil", center=(x, y, soil_z), cap_bottom=True)
    return (x, y, soil_z + 0.006), r_s


LEAF_T = [0.0, 0.2, 0.45, 0.7, 1.0]


def leaf_geo(base, axis, side_dir, size, width, fold=0.25, curl=0.15, shape=None):
    """Return (verts, faces, uvs) for one leaf: single base and tip vertices, folded on the midrib."""
    shape = shape or (lambda t: math.sin(math.pi * min(t * 1.08, 1.0)) ** 0.8)
    nrm = axis.cross(side_dir).normalized()
    inner = LEAF_T[1:-1]

    def mid(t):
        return base + axis * (size * t) - nrm * (curl * size * t * t)
    verts = [base]
    uvv = [(0.5, 0.0)]
    for t in inner:
        c = mid(t)
        w = max(width * size * shape(t) * 0.5, 1e-4)
        verts += [c, c + side_dir * w - nrm * (fold * w), c - side_dir * w - nrm * (fold * w)]
        uvv += [(0.5, t), (1.0, t), (0.0, t)]
    verts.append(mid(1.0))
    uvv.append((0.5, 1.0))
    tip = len(verts) - 1
    faces = [(0, 2, 1), (0, 1, 3)]
    for i in range(len(inner) - 1):
        a, b = 1 + 3 * i, 1 + 3 * (i + 1)
        faces.append((a, a + 1, b + 1, b))
        faces.append((a, b, b + 2, a + 2))
    l = 1 + 3 * (len(inner) - 1)
    faces += [(l, l + 1, tip), (l, tip, l + 2)]
    uvs = [[uvv[k] for k in f] for f in faces]
    return verts, faces, uvs


def shrub(leaves, stems, tints, base, height, spread, n_stems, leaf_size, seed, lean=(0, 0),
          leaf_w=0.7, leaves_per=10, palette=None, droop=0.0, stem_r=0.0028, flowers=None):
    """Bushy plant: curved stems from `base`, alternate ovate leaves, optional flower heads."""
    R = rng(seed)
    palette = palette or [(0.075, 0.13, 0.035), (0.055, 0.10, 0.028), (0.10, 0.16, 0.045), (0.045, 0.085, 0.025)]
    bx, by, bz = base
    for s in range(n_stems):
        ang = R.uniform(0, 2 * math.pi)
        out = R.uniform(0.2, 1.0)
        tip = Vector((bx + math.cos(ang) * spread * out + lean[0], by + math.sin(ang) * spread * out * 0.8 + lean[1],
                      bz + height * R.uniform(0.55, 1.0)))
        if droop:
            tip.z = bz + height * R.uniform(-0.2, 0.6)
        p0 = Vector((bx + R.uniform(-0.022, 0.022), by + R.uniform(-0.022, 0.022), bz - 0.01))
        ctrl = Vector((p0.x + (tip.x - p0.x) * 0.25, p0.y + (tip.y - p0.y) * 0.25, tip.z * 0.4 + p0.z * 0.6 + height * 0.35))
        pts = []
        for i in range(9):
            t = i / 8
            p = p0 * (1 - t) ** 2 + ctrl * 2 * t * (1 - t) + tip * t * t
            p += Vector((R.uniform(-1, 1), R.uniform(-1, 1), 0)) * 0.004 * t
            pts.append(p)
        stems.tube(pts, stem_r, "stem", sides=5, r_end=stem_r * 0.4, roll=R.uniform(0, 6.283))
        nl = int(leaves_per * 1.8 * R.uniform(0.7, 1.3))
        for k in range(nl):
            t = 0.15 + 0.85 * (k + R.random()) / nl
            i = min(int(t * 8), 7)
            f = t * 8 - i
            p = pts[i].lerp(pts[i + 1], f)
            tang = (pts[i + 1] - pts[i]).normalized()
            side = tang.orthogonal().normalized()
            rot = Matrix.Rotation(R.uniform(0, 2 * math.pi), 3, tang)
            side = rot @ side
            axis = (side * 0.8 + tang * 0.45 + Vector((0, 0, R.uniform(0.0, 0.5)))).normalized()
            if droop:
                axis = (axis + Vector((0, 0, -0.5 * droop))).normalized()
            sd = axis.cross(Vector((0, 0, 1)))
            if sd.length < 1e-3:
                sd = Vector((1, 0, 0))
            sd.normalize()
            sz = leaf_size * R.uniform(0.7, 1.15) * (1.0 - 0.35 * t)
            v, fc, uv = leaf_geo(p, axis, sd, sz, leaf_w, fold=0.3, curl=R.uniform(0.05, 0.3))
            leaves.add(v, fc, "leaf", uvs=uv)
            col = palette[R.randrange(len(palette))]
            j = R.uniform(0.85, 1.15)
            tints.extend([(col[0] * j, col[1] * j, col[2] * j)] * len(fc))
        if flowers:
            fr, fmat, fcount = flowers
            for k in range(fcount):
                t = R.uniform(0.55, 1.0)
                i = min(int(t * 8), 7)
                p = pts[i].lerp(pts[i + 1], t * 8 - i)
                fm = fmat if isinstance(fmat, str) else fmat[R.randrange(len(fmat))]
                flower(stems, p, fr * R.uniform(0.8, 1.2), fm, R)
    return


def flower(mb, p, r, mat, R):
    """Five-petal flower head facing outward/up, centre disc touching the stem point."""
    nrm = Vector((R.uniform(-1, 1), R.uniform(-1.2, -0.2), R.uniform(0.0, 1.0))).normalized()
    u = nrm.orthogonal().normalized()
    v = nrm.cross(u)
    ring = []
    n = 15
    for i in range(n):
        a = 2 * math.pi * i / n
        petal = 0.65 + 0.35 * abs(math.cos(5 * a / 2))
        ring.append(p + (u * math.cos(a) + v * math.sin(a)) * r * petal + nrm * r * 0.25 * petal)
    c = p + nrm * 0.002
    vs = [c] + ring
    fs = [(0, 1 + i, 1 + (i + 1) % n) for i in range(n)]
    mb.add([tuple(x) for x in vs], fs, mat)
    _centre_dome(mb, c + nrm * 0.001, nrm, r * 0.2)


def vine(leaves, stems, tints, start, length, n, seed, side=-1, fmats=("petal_pink",)):
    """Trailing flowering vine cascading down from `start`."""
    R = rng(seed)
    sx, sy, sz = start
    for s in range(n):
        L = length * R.uniform(0.45, 1.0)
        out = R.uniform(0.0, 0.26)
        ox, oy = R.uniform(-0.035, 0.035), R.uniform(-0.03, 0.03)   # each stem roots at its own spot
        pts = []
        for i in range(14):
            t = i / 13
            x = ox + sx + side * (out * math.sin(math.pi / 2 * min(t * 2, 1)) + R.uniform(-0.02, 0.02) * t) + side * 0.05 * t
            y = oy + sy - 0.02 - 0.12 * math.sin(math.pi / 2 * min(t * 3, 1)) - R.uniform(0.0, 0.05) * t
            z = sz + 0.06 * math.sin(math.pi * min(t * 3, 1)) - L * max(0.0, t - 0.15) / 0.85
            pts.append(Vector((x, y, z)))
        stems.tube(pts, 0.0028, "stem", sides=5, r_end=0.0012, roll=R.uniform(0, 6.283))
        for k in range(int(40 * L / length) + 12):
            t = R.uniform(0.05, 1.0)
            i = min(int(t * 13), 12)
            p = pts[i].lerp(pts[i + 1], t * 13 - i)
            tang = (pts[i + 1] - pts[i]).normalized()
            side_v = tang.orthogonal().normalized()
            side_v = Matrix.Rotation(R.uniform(0, 2 * math.pi), 3, tang) @ side_v
            axis = (side_v + Vector((0, -0.6, 0.2))).normalized()
            sd = axis.cross(Vector((0, 0, 1)))
            sd = sd.normalized() if sd.length > 1e-3 else Vector((1, 0, 0))
            v, fc, uv = leaf_geo(p, axis, sd, 0.04 * R.uniform(0.7, 1.25), 0.65, fold=0.25)
            leaves.add(v, fc, "leaf", uvs=uv)
            g = R.uniform(0.85, 1.1)
            tints.extend([(0.07 * g, 0.13 * g, 0.04 * g)] * len(fc))
        nf = R.randint(3, 8)
        for k in range(nf):
            t = R.uniform(0.0, 0.85) ** 1.6
            i = min(int(t * 13), 12)
            p = pts[i].lerp(pts[i + 1], t * 13 - i)
            flower(stems, p, 0.022 * R.uniform(0.8, 1.2), fmats[R.randrange(len(fmats))], R)


# ======================================================================================
# Curtains
# ======================================================================================
def cord_curtain(mb_curtain, mb_cord, x0, x1, z_tie, z_bot, sag, y, folds=7, seed=5, flap=0.05):
    """One sheer sheet hung from a sagging cord pinched at the centre (bible L2/R1)."""
    R = rng(seed)
    w = x1 - x0
    phase = [R.uniform(0, 2 * math.pi) for _ in range(3)]

    def cord_z(u):
        return z_tie - sag * math.sin(math.pi * u)

    # cord (slight extra droop either side of the pinch)
    cp = [(x0 + w * u, y - 0.006, cord_z(u)) for u in [i / 24 for i in range(25)]]
    mb_cord.tube(cp, 0.005, "cord", sides=6)
    # knot / clothes-peg at the pinch
    mb_cord.sphere((x0 + w / 2, y - 0.012, cord_z(0.5) - 0.004), 0.012, "cord", seg=8, rings=5)

    def fn(u, v):
        # v = 0 at the cord (top), 1 at the bottom
        x = x0 + w * u
        top = cord_z(u)
        z = top - (top - z_bot) * v
        # gathering toward the pinch near the top
        pinch = math.exp(-((u - 0.5) / 0.12) ** 2) * (1 - v) ** 2
        x = x + (x0 + w / 2 - x) * 0.35 * pinch
        amp = 0.012 + 0.018 * (1 - v) * (1 - abs(u - 0.5) * 1.6) + 0.01 * v
        d = amp * math.sin(2 * math.pi * folds * u + phase[0] + 2.5 * v) + 0.006 * math.sin(2 * math.pi * 3.3 * u + phase[1])
        # drape: centre of the sheet billows slightly toward the glass
        d += 0.015 * math.sin(math.pi * u) * v
        d *= min(1.0, v * 10.0)
        return (x, y + d, z)
    mb_curtain.grid(fn, 48, 36, "curtain")
    # flap draped over the cord
    def fn2(u, v):
        x = x0 + w * u
        top = cord_z(u)
        pinch = math.exp(-((u - 0.5) / 0.12) ** 2)
        x = x + (x0 + w / 2 - x) * 0.25 * pinch
        return (x, y - 0.006 - 0.012 * v, top + 0.004 - flap * v * (0.6 + 0.4 * math.sin(math.pi * u)))
    mb_curtain.grid(fn2, 24, 3, "curtain")


def gathered_curtains(mb, x0, x1, z0, z1, y, seed=7):
    """L1: sheer panels gathered softly toward each side, hanging straight."""
    R = rng(seed)
    w = x1 - x0
    for side in (-1, 1):
        def fn(u, v, side=side):
            # each panel covers ~45% of the width, gathered to its side
            if side < 0:
                x = x0 + w * 0.47 * u
                g = 1 - u
            else:
                x = x1 - w * 0.47 * u
                g = 1 - u
            z = z0 + (z1 - z0) * v
            d = (0.01 + 0.012 * g) * math.sin(2 * math.pi * 6 * u + 1.7 * side + 0.8 * v) * (1 - v) ** 0.5
            return (x, y + d, z)
        mb.grid(fn, 30, 24, "curtain")


# ======================================================================================
# Lamp (R1 sill): glass-dome filament lamp on a stalk
# ======================================================================================
def dome_lamp(mb, base, top, dome_r):
    bx, by, bz = base
    tx, ty, tz = top
    pts = []
    for i in range(10):
        t = i / 9
        pts.append((bx + (tx - bx) * t, by + (ty - by) * t + 0.01 * math.sin(math.pi * t), bz + (tz - bz) * t))
    mb.tube(pts, 0.004, "brass", sides=6)
    # socket + bulb
    mb.lathe([(0.0, 0.0), (0.009, 0.0), (0.009, 0.022), (0.0, 0.022)], 10, "brass", center=(tx, ty, tz - 0.004), cap_top=True)
    mb.sphere((tx, ty, tz - 0.012), 0.016, "bulb", seg=10, rings=6, sz=1.25)
    # dome (mushroom cap, glass): shell profile
    mb.lathe([(dome_r * 0.96, 0.0), (dome_r, 0.0), (dome_r * 0.97, 0.014), (dome_r * 0.8, 0.034), (dome_r * 0.5, 0.05),
              (dome_r * 0.15, 0.058), (0.0, 0.06)], 24, "lamp_glass", center=(tx, ty, tz + 0.012), cap_bottom=False)
    mb.lathe([(0.009, 0.0), (0.009, 0.022)], 8, "brass", center=(tx, ty, tz + 0.012 + 0.052), cap_bottom=True, cap_top=True)
    # top finial connects dome to socket stem (rod through)
    mb.tube([(tx, ty, tz + 0.012), (tx, ty, tz + 0.012 + 0.06)], 0.0025, "brass", sides=6)


# ======================================================================================
# Dormer
# ======================================================================================
def medallion(mb, cx, cz, r, y):
    """Round carved medallion (asset-sheet dormer tympanum): rim ring + domed boss."""
    mb.lathe([(r, 0.0), (r, 0.018), (r * 0.82, 0.024), (r * 0.7, 0.014), (r * 0.5, 0.02), (r * 0.25, 0.034), (0.0, 0.038)],
             24, "stone", center=(0, 0, 0), cap_bottom=True)
    n = 24 * 7
    mb.v[-n:] = [(cx + vx, y - vz, cz + vy) for vx, vy, vz in mb.v[-n:]]


def shell_fan(mb, cx, cz, r, y, ribs=9):
    for i in range(ribs):
        a0 = math.pi * i / ribs + 0.02
        a1 = math.pi * (i + 1) / ribs - 0.02
        pts = [(cx, cz)] + [(cx + r * math.cos(a), cz + r * math.sin(a)) for a in [a0 + (a1 - a0) * k / 3 for k in range(4)]]
        chamfer_block(mb, pts, 0.025, 0.006, y0=y)


# ======================================================================================
# Round 2 ironwork: dense lattices traced from the crops
# ======================================================================================
def _c_scroll(cx, cz, r, start, sweep, n=22):
    """C-scroll curl: arc of `sweep` radians from angle `start`, radius tightening 35% at the end."""
    pts = []
    for i in range(n + 1):
        t = i / n
        a = start + sweep * t
        rr = r * (1 - 0.35 * t * t)
        pts.append((cx + rr * math.cos(a), cz + rr * math.sin(a)))
    return pts


def railing_lattice(mb, x0, x1, h, y_fn, posts, finials, style="scroll", r_bar=0.0085, bay=None):
    """Heavy wrought-iron guard with a dense infill.

    style "scroll": every bay holds an S of two opposed C-scrolls, mirrored bay to bay, with a tie
    collar at mid height (L1 balconette). style "x": every bay holds an X of two diagonals with
    curled ends and a boss at the crossing (L3 belly rail, R2). Each element family sits at its own
    depth offset so no two bars share a plane.
    """
    def P3(x, z, dy=0.0):
        return (x, y_fn(z) + dy, z)
    zl, zh = h * 0.10, h - 0.014
    # rails, handrail, posts, finials
    for z, rr in ((0.012, 1.2), (zl, 1.0), (zh, 1.3)):
        mb.tube([P3(x0, z, 0.0045), P3(x1, z, 0.0045)], r_bar * rr, "iron", sides=6)
    mb.tube([P3(x0 - 0.012, h), P3(x1 + 0.012, h)], r_bar * 1.8, "iron", sides=8)
    for px in posts:
        mb.tube([P3(px, -0.004)] + [P3(px, z) for z in [h * i / 12 for i in range(1, 13)]], r_bar * 1.5, "iron", sides=6)
    for px, kind in finials:
        x, y, z = P3(px, h)
        if kind == "urn":
            mb.lathe([(0.0, 0.0), (0.013, 0.0), (0.018, 0.012), (0.009, 0.022), (0.02, 0.04), (0.017, 0.055),
                      (0.007, 0.066), (0.011, 0.074), (0.0, 0.088)], 12, "iron", center=(x, y, z - 0.004), cap_top=True)
        else:
            mb.sphere((x, y, z + 0.018), 0.017, "iron", seg=10, rings=6)
    bw_t = bay or (h * (0.3 if style == "scroll" else 0.72))
    nb = max(2, int(round((x1 - x0) / bw_t)))
    bw = (x1 - x0) / nb
    hz = zh - zl
    for i in range(nb):
        bx0 = x0 + bw * i
        cx = bx0 + bw / 2
        if i > 0:
            mb.tube([P3(bx0, z, -0.0075) for z in [zl + hz * k / 8 for k in range(9)]], r_bar * 0.9, "iron", sides=5)
        if style == "scroll":
            sg = 1 if i % 2 == 0 else -1
            r = min(bw * 0.42, hz * 0.24)
            zm = zl + hz / 2
            up = _c_scroll(cx, zm + r, r, -math.pi / 2, sg * 1.75 * math.pi)
            lo = _c_scroll(cx, zm - r, r, math.pi / 2, sg * 1.75 * math.pi)
            mb.tube([P3(x, z, -0.0025) for x, z in up], r_bar * 0.75, "iron", sides=6)
            mb.tube([P3(x, z, 0.0015) for x, z in lo], r_bar * 0.75, "iron", sides=6)
            # stems joining the scrolls to the rails
            mb.tube([P3(cx, zm + 2 * r - 0.004, -0.0045), P3(cx, zh)], r_bar * 0.7, "iron", sides=5)
            mb.tube([P3(cx, zm - 2 * r + 0.004, 0.003), P3(cx, zl)], r_bar * 0.7, "iron", sides=5)
            mb.sphere(P3(cx, zm, -0.0005), r_bar * 1.4, "iron", seg=8, rings=6)
        else:
            m = 0.012
            a = (bx0 + m, zl + m)
            b = (bx0 + bw - m, zh - m)
            c2 = (bx0 + m, zh - m)
            d = (bx0 + bw - m, zl + m)
            mb.tube([P3(a[0] + (b[0] - a[0]) * k / 8, a[1] + (b[1] - a[1]) * k / 8, -0.0025) for k in range(9)],
                    r_bar * 0.7, "iron", sides=5)
            mb.tube([P3(c2[0] + (d[0] - c2[0]) * k / 8, c2[1] + (d[1] - c2[1]) * k / 8, 0.0015) for k in range(9)],
                    r_bar * 0.7, "iron", sides=5)
            rr = bw * 0.16
            for (px, pz), st in ((a, 0.25 * math.pi), (b, 1.25 * math.pi), (c2, -0.25 * math.pi), (d, 0.75 * math.pi)):
                cxx = px + rr * math.cos(st + math.pi) * -1
                czz = pz + rr * math.sin(st + math.pi) * -1
                curl = _c_scroll(cxx, czz, rr, st + math.pi, 1.6 * math.pi, n=14)
                mb.tube([P3(x, z, -0.005) for x, z in curl], r_bar * 0.6, "iron", sides=5)
            mb.sphere(P3(cx, zl + hz / 2, -0.0005), r_bar * 1.5, "iron", seg=8, rings=6)


def _centre_dome(mb, c, nrm, r):
    """Open hemispherical flower centre (no closed shell)."""
    nrm = nrm.normalized()
    u = nrm.orthogonal().normalized()
    v = nrm.cross(u)
    ring = [c + (u * math.cos(2 * math.pi * i / 8) + v * math.sin(2 * math.pi * i / 8)) * r for i in range(8)]
    mid = [c + (u * math.cos(2 * math.pi * i / 8) + v * math.sin(2 * math.pi * i / 8)) * r * 0.6 + nrm * r * 0.6 for i in range(8)]
    top = c + nrm * r * 0.85
    vs = [tuple(x) for x in ring + mid] + [tuple(top)]
    fs = [(i, (i + 1) % 8, 8 + (i + 1) % 8, 8 + i) for i in range(8)] + [(8 + i, 8 + (i + 1) % 8, 16) for i in range(8)]
    mb.add(vs, fs, "petal_center")


# ======================================================================================
# Round 4: curves traced from the crops
# ======================================================================================
def catmull(pts, n=10, closed=False):
    """Smooth Catmull-Rom curve through 2D/3D points (tuples)."""
    P = [Vector(p) for p in pts]
    if closed:
        P = P + P[:3]
    else:
        P = [P[0] * 2 - P[1]] + P + [P[-1] * 2 - P[-2]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2
                              + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    if not closed:
        out.append(P[-2])
    return [tuple(p) for p in out]


# L1 balconette infill: centres of the openings in the iron web, traced from crop bible_w1 (crop px).
# Visible holes plus those behind the plants and pots, read from their edges.
RAIL_HOLES_PX = [
    (126, 830), (103, 865), (120, 898), (95, 915), (145, 865), (160, 830), (185, 869), (210, 842),
    (205, 878), (228, 915), (247, 844), (253, 878), (270, 834), (274, 878), (297, 861), (287, 898),
    (312, 846), (374, 823), (391, 842), (412, 819), (433, 840), (437, 865), (420, 907), (437, 911),
    (158, 915), (187, 915), (253, 919), (312, 898), (337, 873), (353, 848), (366, 877), (383, 865),
    (337, 915), (374, 915), (395, 898), (330, 830)]


def _rail_uv(px, py):
    """Crop px -> (u along the rail 0..1 left to right, v 0 at the bottom rail .. 1 under the top rail)."""
    u = (px - 40) / 420.0
    top = 822 - 50 * u + 18
    bot = 948 - 22 * u
    return u, (bot - py) / (bot - top)


def _clip_poly(poly, a, b, c):
    """Keep the part of convex polygon poly [(x, z)] with a*x + b*z <= c."""
    out = []
    n = len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        fp = a * p[0] + b * p[1] - c
        fq = a * q[0] + b * q[1] - c
        if fp <= 0:
            out.append(p)
        if fp * fq < 0:
            t = fp / (fp - fq)
            out.append((p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t))
    return out


def railing_web(mb, x0, x1, h, y_rail, finials, r_bar=0.0085, seed=4):
    """L1 balconette (crop w1): heavy double top rail, bottom rail, end posts and finials, and an
    irregular web of rounded openings between them with no vertical bars. Each opening is the
    Voronoi cell of a traced hole centre, inset and rounded into a smooth closed loop; neighbouring
    loops run side by side as the web's bars. A big S-volute closes the left end (crop)."""
    import random
    R = random.Random(seed)

    def P3(x, z, dy=0.0):
        return (x, y_rail + dy, z)
    zl, zh = h * 0.07, h * 0.80
    mb.tube([P3(x0 - 0.014, h), P3(x1 + 0.014, h)], r_bar * 2.2, "iron", sides=8)
    e_ = 0.004   # rail ends stop inside the posts, off the post's centre plane
    mb.tube([P3(x0 + e_, zh + 0.012, 0.004), P3(x1 - e_, zh + 0.012, 0.004)], r_bar * 1.3, "iron", sides=6)
    mb.tube([P3(x0 + e_, zl - 0.006, 0.004), P3(x1 - e_, zl - 0.006, 0.004)], r_bar * 1.2, "iron", sides=6)
    mb.tube([P3(x0 + e_, 0.012, 0.0045), P3(x1 - e_, 0.012, 0.0045)], r_bar * 1.1, "iron", sides=6)
    for px in (x0, x1):
        mb.tube([P3(px, -0.004)] + [P3(px, h * i / 10) for i in range(1, 11)], r_bar * 1.7, "iron", sides=6)
    for px, kind in finials:
        x, y, z = P3(px, h)
        if kind == "urn":
            mb.lathe([(0.0, 0.0), (0.014, 0.0), (0.02, 0.014), (0.01, 0.026), (0.022, 0.046), (0.019, 0.064),
                      (0.008, 0.076), (0.012, 0.086), (0.0, 0.1)], 12, "iron", center=(x, y, z - 0.004), cap_top=True)
        else:
            mb.sphere((x, y, z + 0.02), 0.019, "iron", seg=10, rings=6)
    xa, xb = x0 + 0.06, x1 - 0.012
    seeds = []
    for px, py in RAIL_HOLES_PX:
        u, v = _rail_uv(px, py)
        if 0.0 <= v <= 1.05:
            seeds.append((xa + (xb - xa) * u, zl + (zh - zl) * min(max(v, 0.04), 0.96)))
    rect = [(xa, zl), (xb, zl), (xb, zh), (xa, zh)]
    gap = r_bar * 0.42   # neighbouring loops overlap: the web is one welded piece, as forged
    for i, s in enumerate(seeds):
        poly = rect[:]
        for j, t in enumerate(seeds):
            if i == j:
                continue
            a, b = t[0] - s[0], t[1] - s[1]
            c = (t[0] ** 2 + t[1] ** 2 - s[0] ** 2 - s[1] ** 2) / 2
            poly = _clip_poly(poly, a, b, c)
            if len(poly) < 3:
                break
        if len(poly) < 3:
            continue
        cx = sum(p[0] for p in poly) / len(poly)
        cz = sum(p[1] for p in poly) / len(poly)
        ins = []
        for p in poly:
            dx, dz = p[0] - cx, p[1] - cz
            L = max((dx * dx + dz * dz) ** 0.5, 1e-6)
            k = max(0.15, 1 - gap / L)
            ins.append((cx + dx * k, cz + dz * k))
        for _ in range(3):   # Chaikin corner cutting: rounded openings
            nxt = []
            for k in range(len(ins)):
                p, q = ins[k], ins[(k + 1) % len(ins)]
                nxt += [(0.75 * p[0] + 0.25 * q[0], 0.75 * p[1] + 0.25 * q[1]),
                        (0.25 * p[0] + 0.75 * q[0], 0.25 * p[1] + 0.75 * q[1])]
            ins = nxt
        dy = (i % 3 - 1) * 0.0018
        mb.tube([P3(x, z, dy) for x, z in ins], r_bar * 0.62, "iron", sides=6, closed=True)
        area = 0.5 * abs(sum(ins[k][0] * ins[(k + 1) % len(ins)][1] - ins[(k + 1) % len(ins)][0] * ins[k][1]
                             for k in range(len(ins))))
        if area > 0.0035 and R.random() < 0.6:   # a curl inside the larger openings
            rr = (area ** 0.5) * 0.28
            a0 = R.uniform(0, 6.283)
            curl = [(cx + rr * (1 - 0.6 * t) * math.cos(a0 + 4.2 * t), cz + rr * (1 - 0.6 * t) * math.sin(a0 + 4.2 * t))
                    for t in [k / 14 for k in range(15)]]
            # the curl springs from its loop (welded on, not floating)
            st = min(ins, key=lambda q: (q[0] - curl[0][0]) ** 2 + (q[1] - curl[0][1]) ** 2)
            curl = [st, ((st[0] + curl[0][0]) / 2, (st[1] + curl[0][1]) / 2)] + curl
            mb.tube([P3(x, z, dy + (0.0 if k_ == 0 else 0.004)) for k_, (x, z) in enumerate(curl)],
                    r_bar * 0.5, "iron", sides=5)
    vx = x0 + 0.03   # left-end S-volute (crop x 60-100 px)
    s_pts = [(vx + 0.01, zh), (vx + 0.05, zh - 0.05), (vx + 0.03, zh - 0.12), (vx - 0.005, zh - 0.17),
             (vx + 0.02, zl + 0.08), (vx + 0.06, zl + 0.03), (vx + 0.04, zl)]
    mb.tube([P3(x, z, -0.003) for x, z in catmull(s_pts, 8)], r_bar * 0.9, "iron", sides=6)
