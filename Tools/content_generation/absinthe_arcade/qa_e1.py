"""E1 QA: blender-asset-qa qa_check.py on the shell and the arch masonry, plus counts.

  blender -b aa_exterior.blend --python-exit-code 1 --python qa_e1.py -- --out qa_e1.json

Groups are checked separately (one asset each). Profile "render" with eps 5 mm (environment
scale, per the skill's tuning notes); the per-object numbers (tris, materials, dimensions) are
written alongside. Nothing is saved.
"""

import json
import sys
from pathlib import Path

import bpy

QA_DIR = Path.home() / ".claude/plugins/cache/blender-agent-skills/blender-agent-skills/1.1.0/skills/blender-asset-qa/scripts"
sys.path.insert(0, str(QA_DIR))
import qa_check  # noqa: E402

GROUPS = {
    "shell_structure": ["aa_shell_facade_walls", "aa_shell_facade_mouldings", "aa_shell_facade_corner_bay",
                        "aa_shell_facade_window_surrounds", "aa_shell_facade_roof"],
    "roof_trims": ["aa_shell_facade_roof_zinc"],
    "roof_gable_chimneys": ["aa_shell_facade_roof_gable_chimneys"],
    "shell_windows_iron": ["aa_shell_facade_sash_windows", "aa_shell_facade_ironwork"],
    "arch_masonry": ["aa_arch_hero_archivolt", "aa_arch_hero_plinths"],
}


def tris(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    me = ob.evaluated_get(dg).to_mesh()
    me.calc_loop_triangles()
    n = len(me.loop_triangles)
    ob.evaluated_get(dg).to_mesh_clear()
    return n


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else None
    rep = {"groups": {}, "objects": {}}
    for g, names in GROUPS.items():
        names = [n for n in names if n in bpy.data.objects]
        r = qa_check.run(objects=names, profile="render", eps=0.005, tol=0.01, max_tris=2_000_000)
        rep["groups"][g] = {"pass": r["pass"], "errors": r["errors"], "warnings": r["warnings"],
                            "zfighting": r["zfighting"][:20], "floating": r["floating"][:20]}
        for n in names:
            ob = bpy.data.objects[n]
            rep["objects"][n] = {"tris": tris(ob), "materials": [m.name for m in ob.data.materials if m],
                                 "dimensions": [round(v, 3) for v in ob.dimensions]}
    rep["totals"] = {"objects": len(rep["objects"]), "tris": sum(o["tris"] for o in rep["objects"].values()),
                     "materials": sorted({m for o in rep["objects"].values() for m in o["materials"]})}
    rep["cartouche_present"] = "aa_arch_hero_cartouche" in bpy.data.objects
    text = json.dumps(rep, indent=1, default=str)
    if out:
        out.write_text(text, encoding="utf-8")
    print("@@JSON@@" + json.dumps({g: v["pass"] for g, v in rep["groups"].items()}))


main()
