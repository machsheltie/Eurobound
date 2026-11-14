"""Re-encode opaque PNG textures inside a GLB as JPEG (q92). Geometry/rig untouched. usage: glb_jpeg.py in.glb out.glb"""
import sys, json, struct, io
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
d = open(src, 'rb').read()
assert d[:4] == b'glTF'
off = 12; chunks = []
while off < len(d):
    ln, typ = struct.unpack_from('<I4s', d, off); chunks.append((typ, d[off+8:off+8+ln])); off += 8 + ln
js = json.loads(chunks[0][1]); binc = chunks[1][1]
bvs = js['bufferViews']; datas = [binc[bv.get('byteOffset', 0):bv.get('byteOffset', 0)+bv['byteLength']] for bv in bvs]
n = 0
for im in js.get('images', []):
    if 'bufferView' not in im or im.get('mimeType') != 'image/png': continue
    i = im['bufferView']; pic = Image.open(io.BytesIO(datas[i]))
    if pic.mode in ('RGBA', 'LA') and pic.getchannel('A').getextrema()[0] < 255: continue
    b = io.BytesIO(); pic.convert('RGB').save(b, 'JPEG', quality=92); datas[i] = b.getvalue(); im['mimeType'] = 'image/jpeg'; n += 1
out = bytearray()
for bv, dat in zip(bvs, datas):
    while len(out) % 4: out += b'\0'
    bv['byteOffset'] = len(out); bv['byteLength'] = len(dat); out += dat
while len(out) % 4: out += b'\0'
js['buffers'][0]['byteLength'] = len(out)
jb = json.dumps(js, separators=(',', ':')).encode()
while len(jb) % 4: jb += b' '
total = 12 + 8 + len(jb) + 8 + len(out)
open(dst, 'wb').write(b'glTF' + struct.pack('<II', 2, total) + struct.pack('<I4s', len(jb), b'JSON') + jb + struct.pack('<I4s', len(out), b'BIN\0') + bytes(out))
print(f"{src.split('/')[-1]}: {n} png->jpeg, {len(d)/1e6:.1f} MB -> {total/1e6:.1f} MB")
