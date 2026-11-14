"""Re-render one character's G3 sheet (rig + 3 idle dirs + face closeup) from <id>_rigged.glb; hardcoded to bradley (height 1.9).
Usage: python tools/char3d/render_g3_single.py (repo root); set env norig=1 to skip the jpeg+rig step."""
import sys, os, json, shutil, subprocess
sys.path.insert(0, "tools/char3d"); sys.argv=["x"]
import batch_g3 as b
cid="bradley"; d=f"{b.CH}/bradley"; g=f"{d}/bradley_rigged.glb"
if "norig" not in os.environ:
    subprocess.run(["python", f"{b.T}/glb_jpeg.py", g, g+".tmp"], check=True, capture_output=True); os.replace(g+".tmp", g)
    print("rig rc", b.blender(f"{b.T}/shared_rig.py", [g, "--profile", cid], f"{b.LOGD}/bradley_rig.log"))
glb=f"{d}/bradley_shared.glb"; g3=f"{d}/g3"; tmp=f"{d}/_render_tmp"; os.makedirs(tmp, exist_ok=True)
base=json.load(open(f"{b.T}/poses/bradley_shared.json")); base["contact"]=f"{g3}/contact.png"
for dr in "SEN":
    b.render(glb,tmp,cid,dict(base,only=["idle",dr]),f"{b.LOGD}/bradley_r{dr}.log"); shutil.copy(f"{tmp}/idle/{dr}/00.png", f"{g3}/idle_{dr}_00.png")
b.render(glb,tmp,cid,dict(base,canvas=1024,ppm=3413,center_z=1.9-0.19,only=["idle","S"]),f"{b.LOGD}/bradley_rf.log")
shutil.copy(f"{tmp}/idle/S/00.png", f"{g3}/face_closeup_before.png"); shutil.rmtree(tmp); b.sheet(cid,g3); print("done")
