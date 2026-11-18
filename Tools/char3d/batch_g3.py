"""Batch QC prep for Tripo characters (headless Blender, one at a time). Resumable via Assets/Graphics/characters3d/_batch_status.txt.
python tools/char3d/batch_g3.py <stage> [id ...]    stages: raw  rig  render  colors  twin   (rig = jpeg + shared_rig; render = g3 renders + sheet)
Logs: Assets/Graphics/characters3d/_batch_logs/<id>_<stage>.log"""
import sys, os, json, shutil, subprocess, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "item3d"))
from blender_lock import blender_lock
import numpy as np
from PIL import Image
ROOT = os.getcwd(); BL = "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe"
CH = "Assets/Graphics/characters3d"; T = "tools/char3d"
STATUS = f"{CH}/_batch_status.txt"; LOGD = f"{CH}/_batch_logs"; os.makedirs(LOGD, exist_ok=True)
def A(**k):
    b = dict(stride=1.0, knee=1.0, arm=1.0, elbow=1.0, bounce=1.0, sway=1.0, breathe=1.0); b.update(k); return b
C = {  # id: folder, glb stem, source, height, doc, amp, lean
 "tomas_two_fifty": ("tomas_two_fifty", "tomas_two_fifty_rigged", "tomas_two_fifty_portrait.png", 1.72, "bored, unhurried slouch", A(stride=.8, knee=.8, arm=.55, elbow=.7, bounce=.5, sway=.7, breathe=.8), 3),
 "cara": ("cara", "cara_rigged", "cara_portrait.png", 1.65, "smug birthday-girl strut in heels", A(stride=.9, knee=.85, arm=.9, elbow=.8, bounce=1.2, sway=1.5, breathe=1.0), 0),
 "woo_woo_whitney": ("woo_woo_whitney", "woo_woo_whitney_rigged", "woo_woo_whitney_tripo_src.png", 1.63, "bubbly, bouncy, tipsy", A(stride=.95, knee=1.0, arm=1.2, elbow=1.0, bounce=1.9, sway=1.7, breathe=1.3), 0),
 "brynleigh": ("brynleigh", "brynleigh_rigged", "brynleigh_tripo_src.png", 1.70, "loud swagger", A(stride=1.1, knee=1.0, arm=1.2, elbow=1.0, bounce=1.3, sway=1.4, breathe=1.2), 0),
 "ashleigh": ("ashleigh", "ashleigh_rigged", "ashleigh_tripo_src.png", 1.66, "cool, composed", A(stride=.9, knee=.9, arm=.7, elbow=.8, bounce=.7, sway=.8, breathe=.8), 0),
 "kenleigh": ("kenleigh", "kenleigh_rigged", "kenleigh_tripo_src.png", 1.64, "giggly, can't stand still", A(stride=1.0, knee=1.0, arm=1.3, elbow=1.1, bounce=1.8, sway=1.5, breathe=1.6), 0),
 "accounts_receivable": ("accounts_receivable_accounts", "accounts_receivable_rigged", "accounts_receivable_accounts_portrait.png", 1.95, "heavy, slow, menacing", A(stride=.85, knee=.9, arm=.6, elbow=.7, bounce=.6, sway=.5, breathe=1.0), 2),
}
def status(msg):
    open(STATUS, "a").write(msg + "\n"); print(msg)
def done(cid, st): return os.path.exists(STATUS) and f"{cid} {st} DONE" in open(STATUS).read()
def blender(py, args, log):
    with blender_lock("char3d " + os.path.basename(py)), open(log, "w") as f:   # one Blender at a time (Eurobound-1nvh)
        r = subprocess.run([BL, "-b", "--factory-startup", "--python", py, "--"] + args, stdout=f, stderr=subprocess.STDOUT)
    return r.returncode
def prof(cid):
    folder, stem, src, h, doc, amp, lean = C[cid]
    base = json.load(open(f"{T}/profiles/bradley.json"))
    base["_doc"] = f"{cid}: {doc}."; base["amp"] = amp; base["lean_deg"] = lean
    json.dump(base, open(f"{T}/profiles/{cid}.json", "w"), indent=1)
    sh = json.load(open(f"{T}/poses/bradley_shared.json"))
    sh["profile"] = cid; sh["height_m"] = h; sh["contact"] = f"{CH}/{folder}/g3/contact.png"
    json.dump(sh, open(f"{T}/poses/{cid}_shared.json", "w"), indent=1)
def stage_raw(cid):
    folder, stem, *_ = C[cid]; g = f"{CH}/{folder}/{stem}.glb"; raw = f"{CH}/{folder}/{stem}_tripo_raw.glb"
    if not os.path.exists(raw): shutil.copy(g, raw)
    blender(f"{T}/glb_inspect.py", [raw], f"{LOGD}/{cid}_inspect.log")
    L = open(f"{LOGD}/{cid}_inspect.log", errors="ignore").read().splitlines()
    meshes = [l for l in L if l.startswith("OBJ") and " MESH " in l]; print(cid, "meshes:", [m.split()[1] for m in meshes])
    status(f"{cid} raw DONE meshes={len(meshes)}")
def stage_rig(cid):
    folder, stem, *_ = C[cid]; g = f"{CH}/{folder}/{stem}.glb"; prof(cid)
    if not done(cid, "jpeg") or "--force" in sys.argv:
        subprocess.run(["python", f"{T}/glb_jpeg.py", g, g + ".tmp"], check=True, capture_output=True)
        os.replace(g + ".tmp", g); status(f"{cid} jpeg DONE")
    rc = blender(f"{T}/shared_rig.py", [g, "--profile", cid], f"{LOGD}/{cid}_rig.log")
    sz = os.path.getsize(f"{CH}/{folder}/{stem.replace('_rigged','')}_shared.glb") / 1e6
    status(f"{cid} rig DONE rc={rc} shared={sz:.1f}MB")
def render(glb, out, cid, cfg, log):
    json.dump(cfg, open(f"{out}/_cfg.json", "w"))
    return blender(f"{T}/render_dirs.py", [glb, out, cid, f"{out}/_cfg.json"], log)
def stage_render(cid):
    folder, stem, src, h, *_ = C[cid]; d = f"{CH}/{folder}"; g3 = f"{d}/g3"; os.makedirs(g3, exist_ok=True)
    glb = f"{d}/{stem.replace('_rigged','')}_shared.glb"; tmp = f"{d}/_render_tmp"; os.makedirs(tmp, exist_ok=True)
    base = json.load(open(f"{T}/poses/{cid}_shared.json"))
    for dr in "SEN":
        render(glb, tmp, cid, dict(base, only=["idle", dr]), f"{LOGD}/{cid}_r{dr}.log")
        shutil.copy(f"{tmp}/idle/{dr}/00.png", f"{g3}/idle_{dr}_00.png")
    cz = h - 0.19
    render(glb, tmp, cid, dict(base, canvas=1024, ppm=3413, center_z=cz, only=["idle", "S"]), f"{LOGD}/{cid}_rf.log")
    shutil.copy(f"{tmp}/idle/S/00.png", f"{g3}/face_closeup_before.png")
    shutil.rmtree(tmp)
    sheet(cid, g3); status(f"{cid} render DONE")
def sheet(cid, g3):
    S = Image.open(f"{g3}/idle_S_00.png").convert("RGBA"); bb = S.getchannel("A").getbbox(); x0, y0, x1, y1 = bb
    cx = (x0 + x1) // 2; crop = S.crop((max(cx - 140, 0), max(y0 - 30, 0), max(cx - 140, 0) + 280, max(y0 - 30, 0) + 280)).resize((560, 560), Image.LANCZOS)
    g = Image.new("RGB", (560, 560), (150, 150, 150)); g.paste(crop, (0, 0), crop); g.save(f"{g3}/face_game.png")
    W, Hh = 1000, 640; sh = Image.new("RGB", (W, Hh), (150, 150, 150))
    for i, dr in enumerate("SEN"):
        im = Image.open(f"{g3}/idle_{dr}_00.png").convert("RGBA").crop((140, 20, 500, 620)).resize((216, 360), Image.LANCZOS); sh.paste(im, (i * 216, 0), im)
    fc = Image.open(f"{g3}/face_closeup_before.png").convert("RGBA").resize((352, 352), Image.LANCZOS); sh.paste(fc, (648, 0), fc)
    gm = g.resize((280, 280), Image.LANCZOS); sh.paste(gm, (0, 370)); sh.save(f"{g3}/g3_sheet.jpg", quality=88)
def dom(path, n=4, crop=None):
    im = Image.open(path).convert("RGBA")
    if crop: im = im.crop(crop)
    a = np.array(im); m = a[..., 3] > 200; px = a[m][:, :3].astype(int)
    q = (px // 32); key = q[:, 0] * 64 + q[:, 1] * 8 + q[:, 2]
    u, c = np.unique(key, return_counts=True); out = []
    for k in u[np.argsort(-c)][:n]:
        sel = px[key == k]; out.append((tuple(int(v) for v in np.median(sel, 0)), round((key == k).mean(), 2)))
    return out
def stage_colors(cid):
    folder, stem, src, *_ = C[cid]; g3 = f"{CH}/{folder}/g3"
    p = Image.open(f"{CH}/{folder}/{src}").convert("RGB"); a = np.array(p); bg = a.min(2) < 225
    ref = Image.fromarray(np.dstack([a, (bg * 255).astype(np.uint8)]), "RGBA"); ref.save(f"{LOGD}/{cid}_ref_fig.png")
    print(cid, "REF", dom(f"{LOGD}/{cid}_ref_fig.png", 5)); print(cid, "RND", dom(f"{g3}/idle_S_00.png", 5))
if __name__ == "__main__":
    st = sys.argv[1]; ids = [a for a in sys.argv[2:] if not a.startswith("--")] or list(C)
    for cid in ids:
        if st != "colors" and done(cid, st) and "--force" not in sys.argv: continue
        globals()["stage_" + st](cid)
