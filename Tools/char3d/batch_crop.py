"""python tools/char3d/batch_crop.py <id> <center_z m> <ppm> <out.png> [shared_glb]  (renders idle S frame 0 close-up, 1024 px; for lettering checks)"""
import sys, json, shutil, os
sys.path.insert(0, "tools/char3d"); import batch_g3 as b
cid, cz, ppm, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
folder, stem = b.C[cid][0], b.C[cid][1]
glb = sys.argv[5] if len(sys.argv) > 5 else f"{b.CH}/{folder}/{stem.replace('_rigged','')}_shared.glb"
tmp = f"{b.LOGD}/_crop_{cid}"; os.makedirs(tmp, exist_ok=True)
base = json.load(open(f"{b.T}/poses/{cid}_shared.json"))
b.render(glb, tmp, cid, dict(base, canvas=1024, ppm=ppm, center_z=cz, only=["idle", "S"]), f"{b.LOGD}/{cid}_crop.log")
shutil.copy(f"{tmp}/idle/S/00.png", out); shutil.rmtree(tmp); print("ok", out)
