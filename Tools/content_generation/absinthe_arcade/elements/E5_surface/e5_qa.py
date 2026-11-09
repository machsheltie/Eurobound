"""QA gate for E5: blender-asset-qa qa_check.run on aa_kit/aa_e5_mural, plus numbers.

  blender -b wip/E5_surface.blend --factory-startup --python e3_qa.py -- [--json out.json]
"""
import json
import sys
from collections import Counter
from pathlib import Path

import bpy

QA = Path("C:/Users/heirr/.claude/plugins/cache/blender-agent-skills/blender-agent-skills/1.1.0/skills/blender-asset-qa/scripts")
sys.path.insert(0, str(QA))
import qa_check  # noqa: E402


def tris(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    me = ob.evaluated_get(dg).to_mesh()
    n = sum(len(p.vertices) - 2 for p in me.polygons)
    ob.evaluated_get(dg).to_mesh_clear()
    return n


def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = {}
    for cname in ("aa_e5_mural",):
        c = bpy.data.collections[cname]
        obs = [o for o in c.all_objects if o.type == "MESH"]
        for o in obs:                       # check the bake layout (uv_bake), the one that must not overlap
            o.data.uv_layers.active = o.data.uv_layers["uv_bake"]
        r = qa_check.run(objects=[o.name for o in obs], profile="game", eps=0.001, tol=0.002)
        lo = [min((o.matrix_world @ v.co)[i] for o in obs for v in o.data.vertices) for i in range(3)]
        hi = [max((o.matrix_world @ v.co)[i] for o in obs for v in o.data.vertices) for i in range(3)]
        mats = sorted({m.name for o in obs for m in o.data.materials if m})
        out[cname] = {
            "pass": r.get("pass"),
            "errors": Counter(e.split(":")[0] if isinstance(e, str) else str(e.get("check", e))[:40]
                              for e in r.get("errors", [])),
            "errors_detail": r.get("errors", [])[:40],
            "warnings_detail": r.get("warnings", []),
            "uv_bake": {o: (m.get("uv_oob_pct"), m.get("uv_overlap_pct")) for o, m in r.get("objects", {}).items()},
            "warnings": Counter(w.split(":")[0] if isinstance(w, str) else str(w.get("check", w))[:40]
                                for w in r.get("warnings", [])),
            "objects": len(obs), "tris": sum(tris(o) for o in obs), "materials": len(mats),
            "bounds_min": [round(v, 3) for v in lo], "bounds_max": [round(v, 3) for v in hi],
            "dimensions": [round(h - l, 3) for l, h in zip(lo, hi)],
        }
    txt = json.dumps(out, indent=1, default=str)
    if "--json" in args:
        Path(args[args.index("--json") + 1]).write_text(txt)
    print("@@E5QA@@" + json.dumps({k: {kk: v[kk] for kk in ("pass", "errors", "warnings", "objects", "tris",
                                                           "materials", "dimensions")} for k, v in out.items()},
                                  default=str))


main()
