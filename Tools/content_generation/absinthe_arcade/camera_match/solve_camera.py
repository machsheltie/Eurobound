"""<venv python> solve_camera.py lines_bible.json

Fit a pinhole camera (F, pitch, yaw, roll; principal point at image centre) to facade line families.
World/facade frame: X along facade to the right, Y into the facade (away from the street), Z up."""
import numpy as np, json, sys
W, H = 5248, 4796
CX, CY = W / 2, H / 2

def basis(pitch, yaw, roll):
    # camera looks along +Y with pitch up (rad), then yaw about Z (positive = turn left, CCW from above), roll about forward
    cp, sp = np.cos(pitch), np.sin(pitch)
    fw = np.array([0, cp, sp]); up = np.array([0, -sp, cp]); rt = np.array([1.0, 0, 0])
    cy_, sy_ = np.cos(yaw), np.sin(yaw)
    Rz = np.array([[cy_, -sy_, 0], [sy_, cy_, 0], [0, 0, 1]])
    fw, up, rt = Rz @ fw, Rz @ up, Rz @ rt
    cr, sr = np.cos(roll), np.sin(roll)
    rt2 = cr * rt + sr * up      # roll: positive rotates the image clockwise? (right axis toward up)
    up2 = -sr * rt + cr * up
    return fw, rt2, up2

def vp(d, F, pitch, yaw, roll, cx=CX, cy=CY):
    fw, rt, up = basis(pitch, yaw, roll)
    # homogeneous image point: (cx*z + F*x, cy*z - F*y, z) with x = d.rt, y = d.up, z = d.fw
    x, y, z = d @ rt, d @ up, d @ fw
    return np.array([cx * z + F * x, cy * z - F * y, z])

def project(P, C, F, pitch, yaw, roll, cx=CX, cy=CY):
    fw, rt, up = basis(pitch, yaw, roll)
    v = np.asarray(P) - C
    z = v @ fw
    return np.array([cx + F * (v @ rt) / z, cy - F * (v @ up) / z])

def seg_endpoints(L):
    a, b = L["a"], L["b"]
    if L["o"] == "h":
        xs = sorted([L["p0"][0], L["p1"][0]])
        return np.array([[xs[0], a + b * xs[0]], [xs[1], a + b * xs[1]]])
    ys = sorted([L["p0"][1], L["p1"][1]])
    return np.array([[a + b * ys[0], ys[0]], [a + b * ys[1], ys[1]]])

def seg_res(e, v):
    m = np.array([*(e.mean(0)), 1.0])
    l = np.cross(m, v)
    n = np.hypot(l[0], l[1])
    if n < 1e-12:
        return np.zeros(2)
    l = l / n
    return np.array([l @ np.array([*e[0], 1.0]), l @ np.array([*e[1], 1.0])])

DIRS = {"fv": np.array([0, 0, 1.0]), "wv": np.array([0, 0, 1.0]), "fh": np.array([1.0, 0, 0])}

def residuals(p, lines, prior=None):
    F, pitch, yaw, roll = p
    r = []
    for k, L in lines.items():
        fam = k.split("_")[0]
        v = vp(DIRS[fam], F, pitch, yaw, roll)
        r.extend(seg_res(seg_endpoints(L), v) * L.get("w", 1.0))
    if prior:
        # horizon y at x = prior[0] should be prior[1] (+- prior[2]); scaled to px residual weight prior[3]
        fw, rt, up = basis(pitch, yaw, roll)
        # horizon: image of horizontal directions; take two horizontal dirs and intersect
        h1 = vp(np.array([1.0, 0, 0]), F, pitch, yaw, roll); h2 = vp(np.array([0, 1.0, 0]), F, pitch, yaw, roll)
        hl = np.cross(h1, h2)
        yh = -(hl[0] * prior[0] + hl[2]) / hl[1]
        r.append((yh - prior[1]) / prior[2] * prior[3])
    return np.array(r)

def lm(fun, p0, iters=200):
    p = np.array(p0, float)
    lam = 1e-3
    r = fun(p); c = r @ r
    for _ in range(iters):
        J = np.empty((len(r), len(p)))
        for i in range(len(p)):
            dp = np.zeros(len(p)); dp[i] = 1e-6 * max(1.0, abs(p[i]))
            J[:, i] = (fun(p + dp) - r) / dp[i]
        A = J.T @ J; g = J.T @ r
        while True:
            step = -np.linalg.solve(A + lam * np.diag(np.diag(A) + 1e-12), g)
            pn = p + step; rn = fun(pn); cn = rn @ rn
            if cn < c:
                p, r, c = pn, rn, cn; lam *= 0.3; break
            lam *= 10
            if lam > 1e12:
                return p, r
        if np.linalg.norm(step) < 1e-10 * (1 + np.linalg.norm(p)):
            break
    return p, r

def horizon_y(p, x):
    F, pitch, yaw, roll = p
    h1 = vp(np.array([1.0, 0, 0]), F, pitch, yaw, roll); h2 = vp(np.array([0, 1.0, 0]), F, pitch, yaw, roll)
    hl = np.cross(h1, h2)
    return -(hl[0] * x + hl[2]) / hl[1]

if __name__ == "__main__":
    lines = json.load(open(sys.argv[1]))
    lines = {k: v for k, v in lines.items() if v["rms"] < 3.0}
    for prior in (None, (600, 3880, 60, 30.0), (600, 4100, 60, 30.0), (600, 4400, 60, 30.0)):
        p, r = lm(lambda q: residuals(q, lines, prior), [5500, np.radians(16), np.radians(-15), 0.0])
        F, pitch, yaw, roll = p
        res = r[:2 * len(lines)].reshape(-1, 2)
        print(f"prior={prior}: F={F:.0f}px ({F/W*36:.1f}mm) pitch={np.degrees(pitch):.2f} yaw={np.degrees(yaw):.2f} roll={np.degrees(roll):.2f} "
              f"rms={np.sqrt(np.mean(res**2)):.1f}px horizon@x600={horizon_y(p,600):.0f} @cx={horizon_y(p,CX):.0f}")
        vz = vp(np.array([0, 0, 1.0]), *p); vx = vp(np.array([1.0, 0, 0]), *p)
        print("   Vz", (vz[:2] / vz[2]).round(0), " Vx", (vx[:2] / vx[2]).round(0))
        for (k, L), rr in zip(lines.items(), res):
            print(f"     {k:16s} {rr[0]:+7.1f} {rr[1]:+7.1f}")
