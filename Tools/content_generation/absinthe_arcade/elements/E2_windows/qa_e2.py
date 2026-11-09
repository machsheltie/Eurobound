"""Run blender-asset-qa qa_check.py per E2 kit and summarise numbers (tris, objects, materials, dims).

  blender -b <wip>/E2_windows.blend --python qa_e2.py -- [--out report.json]
"""
import json
import sys
from pathlib import Path

import bpy

QA = Path("C:/Users/heirr/.claude/plugins/cache/blender-agent-skills/blender-agent-skills/1.1.0/skills/blender-asset-qa/scripts")
sys.path.insert(0, str(QA))
import qa_check  # noqa: E402

KITS = ["aa_window_l1_arched", "aa_window_l2_cat", "aa_window_l3_balcony", "aa_window_r1", "aa_window_r2", "aa_window_dormer_l", "aa_window_dormer_r", "aa_window_side_w0", "aa_window_side_w1", "aa_window_side_w2", "aa_window_dormer_side"]


def main():
    a = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = Path(a[a.index("--out") + 1]) if "--out" in a else None
    kits = a[a.index("--kits") + 1:] if "--kits" in a else KITS
    dg = bpy.context.evaluated_depsgraph_get()
    rep = {}
    for k in kits:
        c = bpy.data.collections[k]
        obs = [o for o in c.objects if o.type == "MESH"]
        res = qa_check.run(objects=[o.name for o in obs], profile="game", tol=0.003, max_tris=1500000)
        tris = sum(sum(len(p.vertices) - 2 for p in o.evaluated_get(dg).data.polygons) for o in obs)
        mats = sorted({m.name for o in obs for m in o.data.materials if m})
        lo = [min((o.matrix_world @ v.co)[i] for o in obs for v in o.data.vertices) for i in range(3)]
        hi = [max((o.matrix_world @ v.co)[i] for o in obs for v in o.data.vertices) for i in range(3)]
        rep[k] = {
            "objects": len(obs), "tris": tris, "materials": mats,
            "kit_bbox_dims": [round(hi[i] - lo[i], 3) for i in range(3)],
            "dims": {o.name: [round(x, 3) for x in o.dimensions] for o in obs},
            "uv_layers_ok": all({"uv_material", "uv_bake"} <= {u.name for u in o.data.uv_layers} for o in obs),
            "qa_pass": res.get("pass"), "qa_errors": res.get("errors"), "qa_warnings": res.get("warnings"),
        }
    s = json.dumps(rep, indent=1, default=str)
    if out:
        out.write_text(s, encoding="utf-8")
    print("@@JSON@@" + json.dumps({k: {"objects": v["objects"], "tris": v["tris"], "qa_pass": v["qa_pass"],
                                       "n_err": len(v["qa_errors"] or []), "n_warn": len(v["qa_warnings"] or [])}
                                   for k, v in rep.items()}))


if __name__ == "__main__":
    main()
