"""Trace E3 marquee parts off the rectified bible crop -> trace/e3_trace.json (+ debug overlay).

Plain Python (numpy, scipy, Pillow). Coordinates in the JSON are rectified canvas pixels
(see e3_trace_lib.rectified); e3_layout.py converts them to metres.

Traced automatically:
  letters   ABSINTHE (green fronts) and ARCADE (purple fronts), quantized to a pixel-font grid
  invader   the green 8-bit invader right of ARCADE, quantized to its own pixel grid
  studs     square green / purple / dark pixel studs on the marquee board
  traces    thin coloured strips (purple / yellow / green circuit lines) on the board
Run:  <venv python> e3_trace.py [--debug out.png]
"""
import json
import sys

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi

from e3_trace_lib import HERE, hsv, rectified

# Board outline (outer edge of the metal rim), traced by hand on the rectified canvas, clockwise.
BOARD_OUTLINE = [
    (190, 748), (190, 430), (215, 375), (245, 340), (375, 338), (380, 283), (545, 278),
    (552, 198), (875, 195), (955, 100), (1590, 95), (1680, 222), (2015, 225), (2035, 250),
    (2040, 308), (2165, 312), (2250, 395), (2280, 445), (2285, 475), (2330, 485), (2340, 748),
]
# Areas excluded from stud detection: letters, icons, banner, apex box.
LETTER_BOX_ABS = (560, 222, 1915, 472)
LETTER_BOX_ARC = (770, 415, 1835, 700)
TOKEN_BOX = (505, 525, 705, 715)
INVADER_BOX = (1900, 495, 2170, 705)
BANNER_BOX = (380, 735, 2200, 900)
APEX_BOX = (1130, 92, 1410, 200)


# Hand curation after reviewing the numbered detection overlay against the crop.
# Detected blobs that are NOT studs (keyed by their rounded top-left corner): apex-box swirl
# ornaments, a trim corner, a hook, shadows.
STUD_DROP = {(1196, 120), (1388, 136), (2165, 355), (323, 395), (1133, 121), (941, 195), (2163, 433)}
# Studs the colour masks miss (dark-on-black, olive, or merged with trims): (x0, y0, x1, y1, colour, hollow)
STUD_ADD = [
    (596, 248, 630, 309, "purple", False),   # tall purple, left top step
    (630, 237, 683, 276, "olive", False),    # olive-grey square beside it
    (358, 466, 387, 519, "olive", False),    # olive-grey beside the left tall purple
    (755, 510, 787, 543, "purple", True),    # small purple with a dark centre, left of ARCADE
    (451, 708, 493, 741, "dark", False),     # plate under the token
    (710, 708, 756, 741, "dark", False),     # plate under the token
    (971, 200, 1000, 230, "olive", False),   # crown, left
    (2169, 470, 2209, 501, "olive", False),  # right, above the dark square
    (1862, 523, 1892, 548, "dark", True),    # small hollow bracket square above the invader's left
    (1881, 703, 1906, 732, "dark", False),   # right, under ARCADE's E
    (2196, 705, 2229, 741, "dark", False),   # right, bottom plate
]


def poly_mask(shape, pts):
    im = Image.new("L", (shape[1], shape[0]), 0)
    ImageDraw.Draw(im).polygon(pts, fill=1)
    return np.asarray(im).astype(bool)


def box_mask(shape, b, pad=0):
    m = np.zeros(shape, bool)
    m[max(0, b[1] - pad):b[3] + pad, max(0, b[0] - pad):b[2] + pad] = True
    return m


def colour_masks(img):
    h, s, v = hsv(img)
    green = (h > 0.15) & (h < 0.30) & (s > 0.30) & (v > 0.45)
    purple = (h > 0.72) & (h < 0.93) & (s > 0.28) & (v > 0.42)
    yellow = (h > 0.09) & (h <= 0.15) & (s > 0.35) & (v > 0.50)
    grey = (s < 0.35) & (v > 0.20) & (v < 0.55)
    return green, purple, yellow, grey, (h, s, v)


def comp_list(mask, min_area):
    lab, n = ndi.label(mask)
    res = []
    for i, sl in enumerate(ndi.find_objects(lab), start=1):
        if sl is None:
            continue
        sub = lab[sl] == i
        a = int(sub.sum())
        if a < min_area:
            continue
        y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
        res.append(dict(x0=int(x0), y0=int(y0), x1=int(x1), y1=int(y1), area=a,
                        fill=a / float((x1 - x0) * (y1 - y0))))
    return res


# letter column splits (rectified canvas x) where neighbouring letters touch in the mask
CELL = 14.0          # letter pixel pitch in canvas px (the crop's stair-step size)
SPLITS_ABS = [812, 994, 1165, 1245, 1420, 1565, 1738]
SPLITS_ARC = [998, 1188, 1358, 1532, 1690]
LETTERS_ABS = "ABSINTHE"
LETTERS_ARC = "ARCADE"


def trace_word(mask, box, cell, close_iter, hole_max, splits, letters):
    """Word mask -> per-letter cells on ONE word-wide grid (origin: word left x, baseline y)."""
    x0, y0, x1, y1 = box
    m = mask[y0:y1, x0:x1].copy()
    m = ndi.binary_closing(m, structure=np.ones((3, 3)), iterations=close_iter)
    holes = ndi.binary_fill_holes(m) & ~m
    lab, n = ndi.label(holes)
    sizes = ndi.sum(holes, lab, range(1, n + 1))
    for i, sz in enumerate(sizes, start=1):
        if sz < hole_max:
            m[lab == i] = True
    m = ndi.binary_opening(m, iterations=2)
    lab, n = ndi.label(m)
    sizes = ndi.sum(m, lab, range(1, n + 1))
    m = np.isin(lab, [i + 1 for i, s_ in enumerate(sizes) if s_ > 600])
    ys, xs = np.nonzero(m)
    gx0, base = xs.min(), ys.max() + 1                     # grid origin (local)
    ncol = int(np.ceil((xs.max() + 1 - gx0) / cell))
    nrow = int(np.ceil((base - ys.min()) / cell))
    cells = []
    for r in range(nrow):                                   # r = 0 is the bottom row
        yb = base - (r + 1) * cell
        for c in range(ncol):
            xa = gx0 + c * cell
            blk = m[int(round(yb)):int(round(yb + cell)), int(round(xa)):int(round(xa + cell))]
            if blk.size and blk.mean() >= 0.5:
                cells.append((c, r))
    edges = [x0 + gx0] + list(splits) + [x0 + xs.max() + 2]
    out = []
    for k, ch in enumerate(letters):
        a, b = edges[k], edges[k + 1]
        lc = [[c, r] for (c, r) in cells if a <= x0 + gx0 + (c + 0.5) * cell < b]
        out.append(dict(char=ch, cells=lc))
    word = dict(origin_x=float(x0 + gx0), baseline_y=float(y0 + base), cell=cell,
                cols=ncol, rows=nrow, letters=out)
    return word, m


CRAB = [                    # classic 11 x 8 crab invader; the traced crop matches it cell for cell
    "..#.....#..",          # (bar the right foot, which sits one cell further right in the crop)
    "...#...#...",
    "..#######..",
    ".##.###.##.",
    "###########",
    "#.#######.#",
    "#.#.....#.#",
    "...##.##...",
]


def trace_invader(green):
    """Fit the crab bitmap to the traced invader's bounding box."""
    x0, y0, x1, y1 = INVADER_BOX
    m = ndi.binary_opening(green[y0:y1, x0:x1], iterations=2)
    ys, xs = np.nonzero(m)
    cells = [[c, r] for r, row in enumerate(CRAB) for c, ch in enumerate(row) if ch == "#"]
    return dict(x0=int(x0 + xs.min()), x1=int(x0 + xs.max() + 1), y0=int(y0 + ys.min()),
                y1=int(y0 + ys.max() + 1), cols=11, rows=8, cells=cells)


SLOGAN_BOX = (488, 780, 2104, 860)       # the slogan's glyph band inside the bar (trims excluded)
SLOGAN_CELL = 2.5                        # px; fine enough that the cell steps vanish at render size


def trace_slogan(img):
    """Lavender slogan glyphs -> cell grid (origin x0, top y0). Traced, so the letterforms are the bible's."""
    h, s_, v = hsv(img)
    x0, y0, x1, y1 = SLOGAN_BOX
    m = (v[y0:y1, x0:x1] > 0.52) & (s_[y0:y1, x0:x1] < 0.62)
    m = ndi.binary_opening(ndi.binary_closing(m, iterations=1), iterations=1)
    lab, n = ndi.label(m)
    sizes = ndi.sum(m, lab, range(1, n + 1))
    m = np.isin(lab, [i + 1 for i, sz in enumerate(sizes) if sz > 60])
    rows = int((y1 - y0) / SLOGAN_CELL)
    cols = int((x1 - x0) / SLOGAN_CELL)
    cells = []
    for r in range(rows):
        for c in range(cols):
            blk = m[int(r * SLOGAN_CELL):int((r + 1) * SLOGAN_CELL), int(c * SLOGAN_CELL):int((c + 1) * SLOGAN_CELL)]
            if blk.size and blk.mean() >= 0.5:
                cells.append([c, r])
    return dict(x0=x0, y0=y0, cell=SLOGAN_CELL, cells=cells), m


def main():
    dbg = sys.argv[sys.argv.index("--debug") + 1] if "--debug" in sys.argv else None
    img = rectified()
    green, purple, yellow, grey, (h, s, v) = colour_masks(img)
    shape = green.shape

    absinthe, m_abs = trace_word(green, LETTER_BOX_ABS, CELL, 2, 400, SPLITS_ABS, LETTERS_ABS)
    arcade, m_arc = trace_word(purple, LETTER_BOX_ARC, CELL, 2, 400, SPLITS_ARC, LETTERS_ARC)
    invader = trace_invader(green)
    slogan, m_slogan = trace_slogan(img)

    board = poly_mask(shape, BOARD_OUTLINE)
    board_in = ndi.binary_erosion(board, iterations=22)          # stay off the rim
    excl = np.zeros(shape, bool)
    for b in (LETTER_BOX_ABS, LETTER_BOX_ARC, TOKEN_BOX, INVADER_BOX, BANNER_BOX):
        excl |= box_mask(shape, b, pad=6)
    area = board_in & ~excl

    studs, traces = [], []
    for name, m in (("green", green), ("purple", purple), ("yellow", yellow)):
        mm = ndi.binary_opening(m & area, iterations=1)
        for c in comp_list(mm, 40):
            w, hh = c["x1"] - c["x0"], c["y1"] - c["y0"]
            asp = max(w, hh) / max(1, min(w, hh))
            c["color"] = name
            if asp <= 2.2 and c["fill"] > 0.55 and min(w, hh) >= 12 and name != "yellow":
                studs.append(c)
            elif asp > 3 and min(w, hh) <= 14:
                traces.append(c)
            elif asp <= 1.7 and c["fill"] <= 0.55 and min(w, hh) >= 18:
                c["hollow"] = True
                studs.append(c)
    # dark studs: grey compact squares with a lit edge
    gm = ndi.binary_opening(grey & area, iterations=2)
    for c in comp_list(gm, 200):
        w, hh = c["x1"] - c["x0"], c["y1"] - c["y0"]
        if 14 <= min(w, hh) and max(w, hh) <= 70 and max(w, hh) / min(w, hh) < 1.5 and c["fill"] > 0.5:
            c["color"] = "dark"
            studs.append(c)

    studs = [s_ for s_ in studs if (s_["x0"], s_["y0"]) not in STUD_DROP]
    for (a, b, c_, d_, colr, hol) in STUD_ADD:
        studs.append(dict(x0=a, y0=b, x1=c_, y1=d_, color=colr, hollow=hol, manual=True))
    out = dict(space="rectified canvas px (e3_trace_lib.rectified)",
               board_outline=BOARD_OUTLINE, absinthe=absinthe, arcade=arcade,
               invader=invader, studs=studs, traces=traces, slogan=slogan,
               token_box=TOKEN_BOX, apex_box=APEX_BOX, banner_box=BANNER_BOX)
    (HERE / "trace").mkdir(exist_ok=True)
    (HERE / "trace" / "e3_trace.json").write_text(json.dumps(out, indent=1))
    print("letters", [len(L["cells"]) for L in absinthe["letters"]], [len(L["cells"]) for L in arcade["letters"]], "studs", len(studs),
          {k: sum(1 for s_ in studs if s_["color"] == k) for k in ("green", "purple", "dark", "olive")},
          "traces", len(traces), "invader cells", len(invader["cells"]))

    print("slogan cells", len(slogan["cells"]))
    if dbg:
        Image.fromarray((m_slogan * 255).astype(np.uint8)).save(dbg.replace(".png", "_slogan.png"))
        im = Image.fromarray((img * 255).astype(np.uint8))
        d = ImageDraw.Draw(im)
        d.line(BOARD_OUTLINE + [BOARD_OUTLINE[0]], fill=(0, 255, 255), width=3)
        col = dict(green=(0, 255, 0), purple=(255, 0, 255), dark=(255, 128, 0), yellow=(255, 255, 0), olive=(0, 128, 255))
        for s_ in studs:
            d.rectangle([s_["x0"], s_["y0"], s_["x1"], s_["y1"]], outline=col[s_["color"]], width=3)
        for t in traces:
            d.rectangle([t["x0"], t["y0"], t["x1"], t["y1"]], outline=(255, 255, 255), width=1)
        for word, colr in ((absinthe, (0, 255, 0)), (arcade, (255, 0, 255))):
            cc = word["cell"]
            for L in word["letters"]:
                for c, r in L["cells"]:
                    xa = word["origin_x"] + c * cc
                    yb = word["baseline_y"] - (r + 1) * cc
                    d.rectangle([xa, yb, xa + cc - 1, yb + cc - 1], outline=colr)
        L = invader
        cw = (L["x1"] - L["x0"]) / L["cols"]
        ch = (L["y1"] - L["y0"]) / L["rows"]
        for c, r in L["cells"]:
            d.rectangle([L["x0"] + c * cw, L["y0"] + r * ch, L["x0"] + (c + 1) * cw - 1,
                         L["y0"] + (r + 1) * ch - 1], outline=(255, 255, 255))
        im.crop((100, 40, 2500, 950)).save(dbg)


if __name__ == "__main__":
    main()
