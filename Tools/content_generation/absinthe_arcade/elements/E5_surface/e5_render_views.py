"""E5 view windows (bible px) from facade boxes through aa_bible_cam; no bpy."""
from e5_cam import BibleCam


FACADE_BOXES = {                 # facade-space boxes (x0, x1, z0, z1) framed through aa_bible_cam
    "facade": (-7.0, 3.4, 0.0, 13.3),        # crop 01 framing: the whole frontage
    "mural": (-2.9, 2.9, 4.3, 11.2),         # crop 06 framing: the mural
    "stone": (-5.45, -4.35, 8.7, 10.3),      # peeling plaster beside the left top window
}


def window(box, y=0.0):
    cm = BibleCam()
    x0, x1, z0, z1 = box
    pts = [cm.project((x, y, z)) for x in (x0, x1) for z in (z0, z1)]
    u0, u1 = max(0, min(p[0] for p in pts)), min(cm.W, max(p[0] for p in pts))
    v0, v1 = max(0, min(p[1] for p in pts)), min(cm.H, max(p[1] for p in pts))
    return (round(u0), round(v0), round(u1), round(v1))


def views():
    return {k: window(b) for k, b in FACADE_BOXES.items()}


