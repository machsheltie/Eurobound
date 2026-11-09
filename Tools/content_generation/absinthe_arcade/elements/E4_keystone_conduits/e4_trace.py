"""E4 traces, in BIBLE pixels of absinthearcadedaytime.png (5248 x 4796), read off gridded full-res crops.

Each run's vertices are cast through aa_bible_cam onto mason's stone (or a named plane) by e4_build.py;
between vertices the run is straight on the facade and follows the stone relief.
"""

# ---- purple conduits (glossy, glowing) : name, [bible px vertices], width px, couplings at vertex idx
PURPLE = [
    ("L_cornice", [(1833, 1800), (2240, 1724), (2327, 1713), (2351, 1753), (2347, 1975)], 17, [1]),
    ("L_jamb", [(2340, 2040), (2338, 2253), (2280, 2300), (2232, 2352), (2218, 2440), (2214, 2700)], 17, []),
    ("L_jamb2", [(2327, 2345), (2324, 2420), (2318, 2700)], 15, []),       # branches off L_jamb below its elbow
    ("L_device", [(2372, 1980), (2598, 1915)], 15, []),
    ("R_top", [(4187, 1440), (4240, 1429), (4327, 1467), (4333, 1600), (4353, 1680), (4453, 1747),
               (4473, 1784)], 18, []),
    ("R_down_l", [(4487, 1962), (4493, 2293), (4528, 2318)], 17, []),
    ("R_down_r", [(4618, 1853), (4653, 1893), (4660, 2293), (4632, 2318)], 17, []),
    ("R_stub", [(4625, 2330), (4690, 2330)], 15, []),
]

# ---- black cables (flex) and the second thin black pipe beside the downspout
BLACK = [
    ("L_cable_cornice", [(1805, 1835), (1812, 1885), (1780, 1900), (1500, 1905)], 9),
    ("L_cable_drop", [(1660, 2330), (1590, 2200), (1520, 2140), (1420, 2190)], 9),
    ("R_cable_capital", [(4600, 2378), (4640, 2480), (4700, 2474)], 9),
]
BLACK_PIPE_R = [(4627, 1205), (4627, 1760)]          # thin black pipe left of the downspout (stops at the box)

# ---- green: corrugated hoses (glowing). name, vertices, width px, target, collar vertex idx
GREEN = [
    ("cup_R_hose", [(3647, 1865), (3729, 1882), (3812, 1929), (3865, 1988), (3882, 2059), (3888, 2129),
                    (3894, 2176), (3924, 2224), (3976, 2259)], 30, "free", [5]),
    ("arch_L", [(2728, 2172), (2650, 2222), (2561, 2283), (2472, 2344), (2417, 2400), (2380, 2445)], 34, "stone", []),
    ("arch_R", [(4059, 2094), (4165, 2165), (4259, 2224), (4353, 2294), (4412, 2353), (4447, 2435)], 34, "stone", []),
    ("marquee_top", [(2905, 2286), (2986, 2230), (3010, 2208), (3690, 2196), (3722, 2212), (3770, 2262)], 22,
     "marquee", []),
]

# ---- headphones
CUPS = [("L", (3080, 1881), 86), ("R", (3569, 1839), 86)]          # bible: both ~170 px across          # centre px, radius px (bible: R bigger)
CROWN = [(3072, 1800), (3080, 1700), (3097, 1631), (3160, 1585), (3222, 1561), (3333, 1552), (3420, 1556),
         (3472, 1568), (3530, 1600), (3569, 1644), (3586, 1720), (3590, 1770)]
CROWN_W = 32                    # bible: the crown pipe is ~32 px thick
HEAD_PLANE_Y = -0.30            # cups and crown tube sit beside / over the head seat

# ---- junction boxes: name, centre px, w px, h px, depth m, features
BOXES = [
    ("L_small", (1800, 1816), 53, 55, 0.075, {"glands": 2}),
    ("L_mid", (2347, 2007), 58, 78, 0.07, {"glands": 2, "fitting": True}),
    ("L_device", (2622, 1918), 46, 40, 0.06, {"blue_led": True}),
    ("L_big", (1612, 2425), 138, 170, 0.15, {"hinge": "left", "round_sticker": True, "label": "blue", "glands": 2}),
    ("R_top", (4149, 1447), 73, 80, 0.09, {"label": "white", "glands": 1}),
    ("R_big", (4532, 1868), 142, 162, 0.15, {"hinge": "right", "triangle": True, "knob": True, "glands": 3}),
    ("R_low", (4575, 2347), 88, 96, 0.11, {"hinge": "left", "glands": 3}),
]

# ---- pipes
LEFT_PIPE = {"upper_x_px": 1450, "lower_x_px": 1617, "neck": [(1450, 1767), (1617, 1958)], "w_px": 42,
             "collars_px_y": [1958, 2133, 2608]}
DOWNSPOUT = {"x_px_top": 4710, "w_px": 70, "bells_px_y": [1740, 2053]}

# ---- "13" plaque on the right pier
PLAQUE = {"centre": (4675, 3185), "w_px": 110, "h_px": 104}

# ---- the head seat (Tripo v2 lands later): interfaces keystone_head_bible
HEAD_SEAT = {"x": 0.0, "z0": 4.6, "z1": 6.17, "proud": (0.4, 0.6)}
