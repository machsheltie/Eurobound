"""Register a relit variant (e.g. night) onto its master (day) so the two cross-fade pixel-for-pixel.

SIFT features on CLAHE-equalized greyscale (robust to the lighting change) -> RANSAC affine ->
warp the variant into the master's pixel frame. Prints match/inlier counts and residuals; a
median residual above ~1 px means the generator redrew geometry and the variant should be redone.

Usage: python register_to.py MASTER.png VARIANT.png OUT.png
"""
import sys

import cv2
import numpy as np


def main(master: str, variant: str, out: str) -> None:
    M = cv2.imread(master, cv2.IMREAD_COLOR)
    V = cv2.imread(variant, cv2.IMREAD_COLOR)
    Vs = cv2.resize(V, (M.shape[1], M.shape[0]), interpolation=cv2.INTER_AREA)
    clahe = cv2.createCLAHE(3, (8, 8))
    g1 = clahe.apply(cv2.cvtColor(M, cv2.COLOR_BGR2GRAY))
    g2 = clahe.apply(cv2.cvtColor(Vs, cv2.COLOR_BGR2GRAY))
    sift = cv2.SIFT_create(8000)
    k1, d1 = sift.detectAndCompute(g1, None)
    k2, d2 = sift.detectAndCompute(g2, None)
    good = [a for a, b in cv2.BFMatcher().knnMatch(d2, d1, k=2) if a.distance < 0.7 * b.distance]
    src = np.float32([k2[a.queryIdx].pt for a in good])
    dst = np.float32([k1[a.trainIdx].pt for a in good])
    A, inl = cv2.estimateAffine2D(src, dst, ransacReprojThreshold=2.0)
    res = np.linalg.norm(src @ A[:, :2].T + A[:, 2] - dst, axis=1)[inl.ravel() == 1]
    print(f"matches={len(good)} inliers={int(inl.sum())} residual_median={np.median(res):.2f}px p90={np.percentile(res, 90):.2f}px")
    # Warp from the full-res variant for quality: fold the downscale into the affine.
    sx, sy = Vs.shape[1] / V.shape[1], Vs.shape[0] / V.shape[0]
    A_full = A @ np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    W = cv2.warpAffine(V, A_full, (M.shape[1], M.shape[0]), flags=cv2.INTER_LANCZOS4,
                       borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    # Cross-modal inputs (e.g. a grey height render vs the painted master) give few reliable
    # SIFT matches; a plain resize is often better when the generator kept the framing.
    # Keep whichever lines up more edges with the master.
    plain = cv2.resize(V, (M.shape[1], M.shape[0]), interpolation=cv2.INTER_AREA)

    def edge_overlap(img: np.ndarray) -> float:
        e_m = cv2.dilate(cv2.Canny(cv2.cvtColor(M, cv2.COLOR_BGR2GRAY), 60, 160), np.ones((3, 3), np.uint8)) > 0
        e_v = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 30, 90) > 0
        return float((e_m & e_v).sum()) / max(1, int(e_v.sum()))

    s_aff, s_plain = edge_overlap(W), edge_overlap(plain)
    print(f"edge overlap: affine={s_aff:.3f} plain_resize={s_plain:.3f}")
    if s_plain > s_aff:
        W = plain
        print("using plain resize")
    cv2.imwrite(out, W)
    print(f"wrote {out}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
