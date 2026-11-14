"""UV and texture validation without Blender: parses the trial GLB (json + binary), measures UV overlap, coverage and texel density, and the PBR maps.
Run with the paint_zones venv python (numpy, cv2, PIL): validate_package.py <package dir> <out.json>"""
import sys, json, struct
import numpy as np, cv2
from PIL import Image
PK, OUT = sys.argv[1], sys.argv[2]
raw = open(f"{PK}/mesh/street_cabinet_trial.glb", "rb").read()
jl, = struct.unpack("<I", raw[12:16]); js = json.loads(raw[20:20 + jl]); bin_ = raw[20 + jl + 8:]
def acc(i):
    a = js["accessors"][i]; bv = js["bufferViews"][a["bufferView"]]
    n = {"SCALAR": 1, "VEC2": 2, "VEC3": 3}[a["type"]]; dt = {5126: np.float32, 5123: np.uint16, 5125: np.uint32}[a["componentType"]]
    off = bv.get("byteOffset", 0) + a.get("byteOffset", 0)
    return np.frombuffer(bin_, dt, a["count"] * n, off).reshape(-1, n) if n > 1 else np.frombuffer(bin_, dt, a["count"], off)
P = js["meshes"][0]["primitives"][0]
pos = acc(P["attributes"]["POSITION"]); uv = acc(P["attributes"]["TEXCOORD_0"]); idx = acc(P["indices"]).reshape(-1, 3)
S = 2048
t = uv[idx] * S                                   # glTF v is top-down, matches a top-down image
a3 = pos[idx]; area3 = 0.5 * np.linalg.norm(np.cross(a3[:, 1] - a3[:, 0], a3[:, 2] - a3[:, 0]), axis=1)
d = t[:, 1] - t[:, 0]; e = t[:, 2] - t[:, 0]; area2 = 0.5 * np.abs(d[:, 0] * e[:, 1] - d[:, 1] * e[:, 0])
cnt = np.zeros((S, S), np.uint8)
for tri in t:
    m = np.zeros((S, S), np.uint8); cv2.fillPoly(m, [np.round(tri).astype(np.int32)], 1); cnt += m
cov = float((cnt > 0).mean()); ov = float((cnt > 1).sum() / max((cnt > 0).sum(), 1))
tex_density = np.sqrt(area2 / np.maximum(area3, 1e-12))   # texels per metre
ok = area3 > 1e-6
res = {"triangles": int(len(idx)), "verts": int(len(pos)), "bbox_m": [round(float(x), 3) for x in (pos.max(0) - pos.min(0))], "atlas_px": S,
       "uv_in_0_1": bool(uv.min() >= 0 and uv.max() <= 1), "uv_coverage": round(cov, 3), "uv_overlap_pixel_share_incl_shared_edges": round(ov, 4), "uv_area_sum_over_covered_area": round(float(area2.sum() / max((cnt > 0).sum(), 1)), 3),
       "texels_per_m_median": round(float(np.median(tex_density[ok])), 0), "texels_per_m_p5_p95": [round(float(np.percentile(tex_density[ok], p)), 0) for p in (5, 95)],
       "reference_ppm": 400, "degenerate_uv_tris": int((area2 < 1e-3).sum())}
orm = np.array(Image.open(f"{PK}/pbr/cabinet_orm.png").convert("RGB")).astype(np.float32) / 255
nrm = np.array(Image.open(f"{PK}/pbr/cabinet_normal.png").convert("RGB")).astype(np.float32) / 255 * 2 - 1
em = np.array(Image.open(f"{PK}/pbr/cabinet_emissive.png").convert("RGB")).astype(np.float32) / 255
cm = cnt > 0
res["orm"] = {"ao_mean_in_uv": round(float(orm[..., 0][cm].mean()), 3), "ao_min": round(float(orm[..., 0][cm].min()), 3), "roughness_range": [round(float(orm[..., 1][cm].min()), 2), round(float(orm[..., 1][cm].max()), 2)],
              "metallic_max": round(float(orm[..., 2][cm].max()), 2), "metallic_share_gt_0.3": round(float((orm[..., 2][cm] > 0.3).mean()), 4)}
nz = nrm[..., 2][cm]
res["normal"] = {"mean_z": round(float(nz.mean()), 4), "share_z_lt_0.98": round(float((nz < 0.98).mean()), 4), "note": "flat except sticker-edge relief derived from the SAM sticker mask (inferred)"}
res["emissive"] = {"share_lit_gt_0.15": round(float((em.max(-1)[cm] > 0.15).mean()), 4)}
json.dump(res, open(OUT, "w"), indent=1); print(json.dumps(res))
