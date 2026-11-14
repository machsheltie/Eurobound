"""python tools/char3d/batch_fix.py <id> <dx> <dy> <center_z> <ppm> <out_crop.png>  : set dx/dy in poses/<id>_project.json, project_ref, jpeg+shared_rig, crop render."""
import sys, json, subprocess
sys.path.insert(0, "tools/char3d"); import batch_g3 as b
cid, dx, dy, cz, ppm, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
p = f"{b.T}/poses/{cid}_project.json"; d = json.load(open(p))
for v in d["views"]: v["dx"] = dx; v["dy"] = dy
json.dump(d, open(p, "w"))
b.blender(f"{b.T}/project_ref.py", [p], f"{b.LOGD}/{cid}_project.log")
sys.argv = ["x", "rig", cid, "--force"]; b.stage_rig(cid)
subprocess.run(["python", f"{b.T}/batch_crop.py", cid, cz, ppm, out], check=True)
