import sys, numpy as np
from PIL import Image, ImageFilter
night = np.asarray(Image.open(sys.argv[1]).convert("RGB")).astype(np.float32)/255
day = np.asarray(Image.open(sys.argv[2]).convert("RGB").resize((night.shape[1],night.shape[0]),Image.LANCZOS)).astype(np.float32)/255
out = sys.argv[3]
# 1. warm afternoon grade on the relit base, gentle lift of the darks
warm = np.clip(day*np.array([1.10,1.03,0.90]),0,1); warm = 1-(1-warm)**1.15
# 2. emissive mask from the night image: saturated + bright (neon, screens, green glass, lamps)
mx=night.max(-1); mn=night.min(-1); sat=(mx-mn)/(mx+1e-4)
em=np.clip((sat*mx-0.35)/0.35,0,1)
lamp=np.clip((night.mean(-1)-0.80)/0.15,0,1)*0.5
m=np.clip(em+lamp,0,1)
m=np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32)/255
m=(m*0.65)[...,None]
# screen-blend the glow so it reads as light, not paint
glow=1-(1-warm)*(1-night*0.85)
res=warm*(1-m)+glow*m
Image.fromarray((np.clip(res,0,1)*255).astype(np.uint8)).save(out)
