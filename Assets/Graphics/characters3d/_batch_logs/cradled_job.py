import subprocess, time, os
def busy(): return b"blender.exe" in subprocess.run(["tasklist","/FI","IMAGENAME eq blender.exe"],capture_output=True).stdout
time.sleep(5)
while busy(): time.sleep(20)
os.makedirs("Assets/Graphics/characters3d/jakub/asleep", exist_ok=True)
with open("Assets/Graphics/characters3d/_batch_logs/jakub_cradled.log","w") as f:
    r=subprocess.run(["C:/Program Files/Blender Foundation/Blender 5.2/blender.exe","-b","--factory-startup","--python","tools/char3d/pose_render.py","--",
      "Assets/Graphics/characters3d/jakub/jakub_rigged.glb","Assets/Graphics/characters3d/jakub/asleep","cradled","tools/char3d/poses/jakub_cradled_v2.json"],stdout=f,stderr=subprocess.STDOUT)
print("rc",r.returncode)
for l in open("Assets/Graphics/characters3d/_batch_logs/jakub_cradled.log"):
    if l.startswith(("RENDERED","Error","Traceback")): print(l.strip()[:200])
