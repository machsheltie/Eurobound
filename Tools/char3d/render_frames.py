"""Render 8-direction look-B idle + walk frames for shared-rig characters, one Blender at a time (tools/item3d/blender_lock.py, via batch_g3.blender), then G4 sheets.

python tools/char3d/render_frames.py <id> [<id> ...]     (repo root; waits for the Blender lock)
Uses Assets/Graphics/characters3d/<folder>/<glb stem>_shared.glb and tools/char3d/poses/<id>_shared.json; writes
<folder>/idle, <folder>/walk and <folder>/g4/ (g4_sheets.py). Folder/stem/portrait come from batch_g3.C, or JAKUB below.
"""
import os, sys, subprocess, time
sys.path.insert(0, "tools/char3d"); _argv = sys.argv; sys.argv = ["x"]
import batch_g3 as B
sys.argv = _argv
EXTRA = {"jakub": ("jakub", "jakub_rigged", "jakub_portrait_v2.png"),
         "accounts_receivable_receivable": ("accounts_receivable_receivable", "accounts_receivable_receivable_rigged", "receivable_ref.png")}
for cid in sys.argv[1:]:
    folder, stem, port = (B.C[cid][0], B.C[cid][1], B.C[cid][2]) if cid in B.C else EXTRA[cid]
    d = f"{B.CH}/{folder}"; glb = f"{d}/{stem.replace('_rigged', '')}_shared.glb"
    pose = f"{B.T}/poses/{cid if os.path.exists(f'{B.T}/poses/{cid}_shared.json') else 'accounts_receivable'}_shared.json"
    rc = B.blender(f"{B.T}/render_dirs.py", [glb, d, cid, pose], f"{B.LOGD}/{cid}_frames.log")
    print(cid, "frames rc", rc)
    p = f"{d}/{folder}_portrait.png" if os.path.exists(f"{d}/{folder}_portrait.png") else f"{d}/{port}"   # G4 compares with the approved portrait
    r = subprocess.run([sys.executable, f"{B.T}/g4_sheets.py", d, p, f"{d}/g4"], capture_output=True, text=True)
    print(cid, r.stdout.strip()[-300:], r.stderr.strip()[-200:])
