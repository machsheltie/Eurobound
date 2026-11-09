"""Redraw Bradley's HORNETS chest lettering on the diagonal frames.
SE shows the start of the word (HORN...), SW the end (...NETS): the word wraps round the torso.
Anchored on the jersey number '1' (median per animation, so breathing doesn't jitter the letters)."""
import sys, glob, os, re, numpy as np
from collections import defaultdict
from PIL import Image
F={'H':["1.1","1.1","111","1.1","1.1"],'O':["111","1.1","1.1","1.1","111"],'R':["11.","1.1","11.","1.1","1.1"],
   'N':["1..1","11.1","1.11","1..1","1..1"],'E':["111","1..","11.","1..","111"],'T':["111",".1.",".1.",".1.",".1."],'S':["111","1..","111","..1","111"]}
WHITE=(249,241,238,255); OUT=(19,67,146,255)
src,dst=sys.argv[1],sys.argv[2]
def word_mask(word):
    w=sum(len(F[c][0]) for c in word)+len(word)+1
    m=np.zeros((7,w),bool); x=1
    for c in word:
        for r,row in enumerate(F[c]):
            for k,v in enumerate(row):
                if v=='1': m[r+1,x+k]=True
        x+=len(F[c][0])+1
    o=m.copy()
    for dy in(-1,0,1):
        for dx in(-1,0,1): o|=np.roll(np.roll(m,dy,0),dx,1)
    return m,o
WORDS={"se":word_mask("HORN"),"sw":word_mask("HORN")}  # never end-of-word: "...NETS" reads as another team
def numtop(a):
    w=(a[...,3]>0)&(a[...,:3].astype(int).min(-1)>180); best=None
    for x in range(50,78):
        y=42
        while y<62:
            if w[y,x]:
                y1=y
                while y1<64 and w[y1,x]: y1+=1
                if y1-y>=6 and (best is None or y>best): best=y
                y=y1
            y+=1
    return best
files=sorted(glob.glob(src+"/*_south_east_*.png")+glob.glob(src+"/*_south_west_*.png"))
imgs={f:np.asarray(Image.open(f).convert("RGBA")).copy() for f in files}
groups=defaultdict(list)
for f in files: groups[re.sub(r"_\d+\.png$","",os.path.basename(f))].append(f)
for g,fs in groups.items():
    tops=[numtop(imgs[f]) for f in fs]; med=int(np.median([t for t in tops if t]))
    key="se" if "south_east" in g else "sw"; WM,WO=WORDS[key]
    for f,t in zip(fs,tops):
        nt=med if t is None else int(np.clip(t,med-1,med+1))
        a=imgs[f]; ai=a.astype(int); r,gc,b,al=[ai[...,i] for i in range(4)]
        teal=(al>0)&(r<60)&(gc>100)&(b>120)
        y0=nt-8
        los=[];his=[]
        for y in range(nt,nt+5):
            tx=np.where(teal[y])[0]
            if len(tx)>=5: los.append(tx.min()); his.append(tx.max())
        LO,HI=int(np.median(los)),int(np.median(his))
        for y in range(y0-1,nt):
            tx=np.where(teal[y])[0]; tx=tx[(tx>=LO)&(tx<=HI)]
            if len(tx)==0: continue
            for x in range(LO+1,HI):
                if not teal[y,x]: a[y,x]=a[y,tx[np.argmin(np.abs(tx-x))]]
        x0 = LO if key=="se" else max(LO, (LO+HI)//2 - WM.shape[1]//2)
        for yy in range(7):
            for xx in range(WM.shape[1]):
                X=x0+xx; Y=y0+yy
                if X<=LO or X>=HI: continue
                if WM[yy,xx]: a[Y,X]=WHITE
                elif WO[yy,xx]: a[Y,X]=OUT
        Image.fromarray(a).save(os.path.join(dst,os.path.basename(f)))
        print(os.path.basename(f),"num",t,"->",nt,"span",LO,HI)
