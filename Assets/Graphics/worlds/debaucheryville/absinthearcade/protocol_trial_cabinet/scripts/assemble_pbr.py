"""Step 8 (scripted PBR assembly in Blender; Ucupaint layer file is made by ucupaint_layers.py): pulls the projected colour / emission / value textures
out of the three projection GLBs (same mesh, same UVs), bakes real ambient occlusion from the mesh (Cycles), builds the normal map from the sticker
relief height, packs ORM (R AO, G roughness, B metallic), and exports the final GLB with all maps.
blender -b --factory-startup --python assemble_pbr.py -- <day_proj.glb> <emit_proj.glb> <orm_proj.glb> <pbr_out_dir> <out.glb>
Everything except AO and the sticker-relief normal comes straight from reference pixels; roughness/metallic/height are assumed per finish (inferred)."""
import bpy, sys, os, hashlib
import numpy as np
a = sys.argv[sys.argv.index("--") + 1:]
DAY, EMIT, ORM, OUT, GLB = a
os.makedirs(OUT, exist_ok=True)

def load(glb):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    ob = [o for o in bpy.data.objects if o.type == "MESH"][0]
    img = [n.image for n in ob.data.materials[0].node_tree.nodes if n.type == "TEX_IMAGE"][0]
    W, H = img.size
    px = np.empty(W * H * 4, np.float32); img.pixels.foreach_get(px)
    uv = np.array([tuple(l.uv) for l in ob.data.uv_layers.active.data], np.float32)
    return px.reshape(H, W, 4), hashlib.md5(np.round(uv, 4).tobytes()).hexdigest(), (W, H)

day, h1, size = load(DAY)
emit, h2, _ = load(EMIT)
orm, h3, _ = load(ORM)
assert h1 == h2 == h3, "UV layouts differ between projection GLBs"
W, H = size
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=DAY)
ob = [o for o in bpy.data.objects if o.type == "MESH"][0]
mat = ob.data.materials[0]
FILL = np.array([0x23, 0x1c, 0x24], np.float32) / 255   # body-colour fill written by build_cabinet.py (hex 231c24)

def uv_coverage():
    """Texels covered by any UV triangle (numpy barycentric raster)."""
    me = ob.data; me.calc_loop_triangles()
    uvs = np.empty(len(me.loops) * 2, np.float32); me.uv_layers.active.data.foreach_get("uv", uvs); uvs = uvs.reshape(-1, 2)
    tl = np.empty(len(me.loop_triangles) * 3, np.int64); me.loop_triangles.foreach_get("loops", tl); tl = tl.reshape(-1, 3)
    cov = np.zeros((H, W), bool)
    for t in tl:
        q = uvs[t] * [W, H]
        lo = np.maximum(np.floor(q.min(0)).astype(int) - 1, 0); hi = np.minimum(np.ceil(q.max(0)).astype(int) + 1, [W - 1, H - 1])
        xs, ys = np.meshgrid(np.arange(lo[0], hi[0] + 1), np.arange(lo[1], hi[1] + 1)); px = np.stack([xs + .5, ys + .5], -1).reshape(-1, 2)
        a0, b0, c0 = q; d = (b0[1] - c0[1]) * (a0[0] - c0[0]) + (c0[0] - b0[0]) * (a0[1] - c0[1])
        if abs(d) < 1e-9:
            continue
        w0 = ((b0[1] - c0[1]) * (px[:, 0] - c0[0]) + (c0[0] - b0[0]) * (px[:, 1] - c0[1])) / d
        w1 = ((c0[1] - a0[1]) * (px[:, 0] - c0[0]) + (a0[0] - c0[0]) * (px[:, 1] - c0[1])) / d
        ok = (w0 >= -0.02) & (w1 >= -0.02) & (1 - w0 - w1 >= -0.02)
        cov[np.clip(px[ok, 1].astype(int), 0, H - 1), np.clip(px[ok, 0].astype(int), 0, W - 1)] = True
    return cov

def dil(img, cov, n=8):
    """Extend island colours outward n texels (average of filled neighbours), so mip/filter bleed at island edges never reads empty texels."""
    out = img.copy(); filled = cov.copy()
    for _ in range(n):
        acc = np.zeros_like(out); cnt = np.zeros(filled.shape, np.float32)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy or dx:
                    m = np.roll(filled, (dy, dx), (0, 1)); acc += np.roll(out, (dy, dx), (0, 1)) * m[..., None]; cnt += m
        new = (~filled) & (cnt > 0)
        out[new] = acc[new] / cnt[new][:, None]; filled |= new
    return out
COV = uv_coverage()
print("uv coverage", round(float(COV.mean()), 3))

def lin2srgb(x):
    """Image.pixels of an 8-bit PNG/JPEG already holds the stored (display-encoded) values / 255, NOT linear floats (a first version of this script
    applied the sRGB curve again and lifted every colour: found in the step-10 dE check). So this is a clamp; bytes in = bytes out."""
    return np.clip(x, 0, 1)

# ---- AO bake (Cycles, CPU), written into its own image
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 48
ao_img = bpy.data.images.new("ao", W, H, alpha=False); ao_img.colorspace_settings.name = "Non-Color"
nt = mat.node_tree; node = nt.nodes.new("ShaderNodeTexImage"); node.image = ao_img; nt.nodes.active = node
bpy.context.view_layer.objects.active = ob; ob.select_set(True)
sc.cycles.bake_type = "AO"
bpy.ops.object.bake(type="AO", margin=8, margin_type="EXTEND")
ao = np.empty(W * H * 4, np.float32); ao_img.pixels.foreach_get(ao); ao = ao.reshape(H, W, 4)[..., 0]
nt.nodes.remove(node)

# ---- normal from sticker relief height (R of the value texture), in UV space
orm_sr = lin2srgb(orm[..., :3])   # the value images went in as sRGB bytes and come out the same way
# texels the projection never touched still hold the body-colour fill of the shared mesh (R byte 0x23 = 0.137, never a painted R value): reset to default ORM
untouched = (np.abs(orm_sr[..., 0] - 35 / 255) < 0.03) & (np.abs(orm_sr[..., 1] - 28 / 255) < 0.03)
orm_sr[untouched] = (0.0, 0.85, 0.0)
orm_sr[..., 0] = np.where(untouched, 0.0, orm_sr[..., 0])
orm_sr = dil(orm_sr, COV)
orm_sr[..., 1] = np.maximum(orm_sr[..., 1], 0.04)   # no seam/fill texel below 0.04 roughness (glass is 0.08)
h = orm_sr[..., 0].copy()
k = np.exp(-0.5 * (np.arange(-4, 5) / 1.3) ** 2); k /= k.sum()
for ax in (0, 1):
    h = np.apply_along_axis(lambda v: np.convolve(np.pad(v, 4, mode="edge"), k, mode="valid"), ax, h)
STRENGTH = 2.0   # about 0.5 mm of vinyl edge at 400 px/m
dv, du = np.gradient(h)
n = np.stack([-du * STRENGTH, -dv * STRENGTH, np.ones_like(h)], -1); n /= np.linalg.norm(n, axis=-1, keepdims=True)
normal = np.dstack([(n + 1) / 2, np.ones_like(h)]).astype(np.float32)   # data, no colour transform

def save(name, rgb_srgb8, colorspace):
    """rgb_srgb8: float array HxWx3 in the value space to store (0-1); written straight into an 8-bit PNG."""
    im = bpy.data.images.new(name, W, H, alpha=False)
    im.colorspace_settings.name = colorspace
    buf = np.dstack([rgb_srgb8, np.ones((H, W), np.float32)]).astype(np.float32)
    # Blender holds sRGB images as linear floats; to store byte-exact data we set the image to Non-Color while writing the values, then relabel.
    im.colorspace_settings.name = "Non-Color"
    im.pixels.foreach_set(buf.ravel()); im.update()
    im.filepath_raw = os.path.join(OUT, name + ".png"); im.file_format = "PNG"
    im.save()
    im.colorspace_settings.name = colorspace
    return im

# colour textures: day / emit pixels are linear floats of the sRGB PNGs -> convert to sRGB values for byte storage
base = save("cabinet_basecolor", dil(lin2srgb(day[..., :3]), COV), "sRGB")
_e = lin2srgb(emit[..., :3])
_e = np.where((np.abs(_e - FILL).max(-1, keepdims=True) < 0.03), 0.0, _e)   # untouched texels still hold the body-colour fill: they must not glow
# the emit reference carries faint sticker-edge glow bleed (value < ~0.1) that is JPEG-level noise, not an authored light source: fade it out, keep the lit marquee / CRT / button glow
_e = _e * np.clip((_e.max(-1, keepdims=True) - 0.10) / 0.15, 0, 1)
emis = save("cabinet_emissive", dil(_e, COV), "sRGB")

packed = np.dstack([np.clip(ao, 0, 1), orm_sr[..., 1], orm_sr[..., 2]])
ormi = save("cabinet_orm", packed, "Non-Color")
nrmi = save("cabinet_normal", dil(normal[..., :3], COV), "Non-Color")

# ---- material
for n_ in list(nt.nodes):
    nt.nodes.remove(n_)
out = nt.nodes.new("ShaderNodeOutputMaterial"); bs = nt.nodes.new("ShaderNodeBsdfPrincipled"); nt.links.new(bs.outputs[0], out.inputs[0])
def tex(img, loc):
    t = nt.nodes.new("ShaderNodeTexImage"); t.image = img; t.location = loc; return t
tb = tex(base, (-700, 300)); nt.links.new(tb.outputs["Color"], bs.inputs["Base Color"])
te = tex(emis, (-700, 0)); nt.links.new(te.outputs["Color"], bs.inputs["Emission Color"]); bs.inputs["Emission Strength"].default_value = 1.0
to = tex(ormi, (-700, -300)); sep = nt.nodes.new("ShaderNodeSeparateColor"); sep.location = (-400, -300)
nt.links.new(to.outputs["Color"], sep.inputs["Color"]); nt.links.new(sep.outputs["Green"], bs.inputs["Roughness"]); nt.links.new(sep.outputs["Blue"], bs.inputs["Metallic"])
tn = tex(nrmi, (-700, -600)); nm = nt.nodes.new("ShaderNodeNormalMap"); nm.location = (-400, -600); nm.inputs["Strength"].default_value = 1.0
nt.links.new(tn.outputs["Color"], nm.inputs["Color"]); nt.links.new(nm.outputs["Normal"], bs.inputs["Normal"])
# glTF occlusion comes from R of the ORM texture through the exporter's custom group
for gname in ("glTF Material Output", "glTF Settings"):
    try:
        g = bpy.data.node_groups.new(gname, "ShaderNodeTree"); g.interface.new_socket("Occlusion", in_out="INPUT", socket_type="NodeSocketFloat")
        gn = nt.nodes.new("ShaderNodeGroup"); gn.node_tree = g; gn.location = (-100, -500); nt.links.new(sep.outputs["Red"], gn.inputs["Occlusion"]); break
    except Exception as e:
        print("group", gname, e)
bpy.ops.export_scene.gltf(filepath=GLB, export_format="GLB", export_image_format="AUTO")
print("ao mean", round(float(ao.mean()), 3), "uv md5", h1[:8], "tex", W, H, "-> ", GLB)
