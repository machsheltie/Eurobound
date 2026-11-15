"""Battle HUD status icon: a round badge with a colour-coded border ring and ONE simple 3D object on it (0 Tripo credits).

Run (headless):
  blender -b --python Tools/item3d/hud_badge.py -- --object grease_fingers --border E23A3A --out dev/asset_team/hud_icons/grease_fingers_256.png --final game/assets/ui/status_icons/grease_fingers.png
Options:
  --object  id of an object builder in OBJECTS below (one per status; add new ones there, nothing else changes)
  --border  hex of the border ring (#3D7BFF buff, #E23A3A or #FF8A2A debuff, #9AA0A6 neutral / action; design/ux/battle_hud_icon_pictures.md)
  --inner   hex of the inner field (default INNER, see below)
  --out     256 x 256 RGBA master
  --final   optional 28 x 28 file: premultiplied-alpha LANCZOS downscale of the master (needs system python with Pillow + numpy)
Look: tools/char3d/look.py (toon ramp, warm key upper left, cool fill, EEVEE transparent film, Standard view transform), the same
settings as Tools/item3d/render_item.py, but straight-on orthographic (no yaw or pitch) so the badge is a true circle.
No lettering anywhere.

INNER, the neutral dark field: #6B748A (cool slate, lightness about 48 of 100; lightened in round 2 to separate from dark UI). One value for all 26 objects because it is the only
mid-tone that keeps both ends of the palette readable: near-black and dark objects (8-ball, iron dumbbell, mic mesh, dark stub) stay
darker than the field, pale objects (cotton, cream card, frosting, white cube face) stay far lighter, and mid-tone objects (oil gold,
blush pink, orange, pink) keep hue contrast. It also sits clear of every border colour (red, orange, blue, grey are all lighter or
more saturated) and clear of the near-black battle UI strip around the badge.
"""
import math, os, subprocess, sys
import bpy
import bmesh
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
for d in (os.path.join(HERE, "..", "char3d"), os.environ.get("CHAR3D_DIR", "")):
    if d and os.path.exists(os.path.join(d, "look.py")):
        sys.path.insert(0, d)
        break
import look

INNER = "6B748A"
RES = 256
R_OUT, R_RING_OUT, R_RING_IN = 0.500, 0.460, 0.335   # badge radius, border ring outer + inner radius (unit = badge diameter 1.0)
ORTHO = 1.03


def lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def hexlin(h):
    h = h.lstrip("#")
    return tuple(lin(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))


def flat_material(name, hexcol):
    """Unlit exact-colour material (the inner field, so its colour is the colour in the file)."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = hexlin(hexcol) + (1,)
    nt.links.new(em.outputs[0], out.inputs["Surface"])
    return m


def badge_toon(name, hexcol):
    """Toon material for the ring: top ramp band is white so the lit face is the exact hex."""
    cfg = {"ramp0": (0.62, 0.62, 0.66), "ramp1": (0.84, 0.84, 0.86), "ramp2": (1.0, 1.0, 1.0)}
    return look.toon_material(name, base=hexlin(hexcol) + (1,), cfg=cfg)


def new_obj(name, verts, faces, mat, smooth=True):
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    if smooth:
        for p in me.polygons:
            p.use_smooth = True
    o = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(o)
    me.materials.append(mat)
    return o


def lathe(name, profile, mat, seg=64, closed_axis=True):
    """Revolve [(radius, z), ...] about the Z axis. Z is up in the render. Faces point out for a profile listed bottom to top, outer side."""
    verts, faces = [], []
    n = len(profile)
    for i in range(seg):
        a = 2 * math.pi * i / seg
        ca, sa = math.cos(a), math.sin(a)
        for r, z in profile:
            verts.append((r * ca, r * sa, z))
    for i in range(seg):
        j = (i + 1) % seg
        for k in range(n - 1):
            faces.append((i * n + k, j * n + k, j * n + k + 1, i * n + k + 1))
    o = new_obj(name, verts, faces, mat)
    return o


def to_front(o):
    """Lathe objects stand along Z; the camera looks along +Y, so Z already is image up. Nothing to do, kept for clarity."""
    return o


def build_badge(border, inner):
    """Badge lies in the XZ plane facing the camera at -Y. Built as lathes about Y, via an axis swap."""
    # profile in (radius, y) so we can reuse lathe about Z, then rotate X by 90 deg so Z axis -> -Y... simpler: build about Z, rotate.
    holder = bpy.data.objects.new("badge", None)
    bpy.context.scene.collection.objects.link(holder)
    th = 0.05
    parts = []
    # inner field: a slightly domed dark disc, flat colour
    field = lathe("field", [(0, 0.0), (R_RING_IN + 0.01, 0.0)], flat_material("field", inner), seg=96)
    # a plain disc needs a face fan; lathe of one segment gives a ring strip with zero-area centre, which is fine as an annulus from 0
    parts.append(field)
    # border ring: a rounded bevel profile (thick, reads as a raised rim)
    prof = []
    steps = 10
    rm = (R_RING_OUT + R_RING_IN) / 2
    hw = (R_RING_OUT - R_RING_IN) / 2
    for k in range(steps + 1):                       # half-round bead from inner edge over the top to the outer edge
        t = math.pi * k / steps
        prof.append((rm - hw * math.cos(t), 0.0 + th * math.sin(t) * 0.9))
    ring = lathe("ring", prof, badge_toon("ring", border), seg=96)
    parts.append(ring)
    # dark outer rim, a thin flat band so the badge edge holds on a dark strip
    rim = lathe("rim", [(R_RING_OUT - 0.004, 0.0), (R_OUT, 0.0)], flat_material("rim", "14161C"), seg=96)
    parts.append(rim)
    for p in parts:
        p.parent = holder
    holder.rotation_euler = (math.radians(90), 0, 0)   # +Z axis of the lathes -> -Y, toward the camera
    return holder


def srgb_hex_to_lin_tuple(h):
    return hexlin(h)


# ---------------------------------------------------------------- objects (each placed in the badge's local frame: Z up, +Z toward camera is Y flip)

def obj_grease_fingers(scene):
    """A DRIP, mid-fall: thin dark nozzle stub, a stretched thin tail of oil from it, a visible gap, then a fat round teardrop with a
    pointed top falling below. Oil gold #E8A020, highlight #FFD766 (bold white-gold specular #FFF1B8), stub #4A3A28."""
    gold = look.toon_material("oil", base=hexlin("E8A020") + (1,))
    stub = look.toon_material("stub", base=hexlin("4A3A28") + (1,))
    hi = flat_material("hi", "FFF1B8")
    # falling teardrop: round bottom, pointed top (profile radius, z), bottom to top
    zc, rb, ztop = -0.15, 0.13, 0.04
    prof = []
    for k in range(0, 13):
        ang = -math.pi / 2 + (math.pi / 2) * (k / 12)
        prof.append((rb * math.cos(ang), zc + rb * math.sin(ang)))
    for k in range(1, 13):
        t = k / 12
        prof.append((rb * math.cos(t * math.pi / 2) ** 1.5, zc + (ztop - zc) * t))
    drop = lathe("drop", prof, gold, seg=48)
    # stretched tail still hanging from the nozzle: thin, tapering to a point above the gap
    tz0, tz1 = 0.225, 0.12
    tail_prof = [(0.0, tz1)] + [(0.036 * (k / 8) ** 0.8 * (1 + 0.5 * (k / 8) ** 4), tz1 + (tz0 - tz1) * k / 8) for k in range(1, 9)]
    tail = lathe("tail", tail_prof, gold, seg=32)
    # thin dark nozzle (narrower than the drop) with a small lip
    z0 = tz0 - 0.005
    stub_prof = [(0.0, z0), (0.056, z0), (0.056, z0 + 0.012), (0.046, z0 + 0.02), (0.046, z0 + 0.085), (0.0, z0 + 0.085)]
    st = lathe("stub", stub_prof, stub, seg=32)
    # bold specular on the bulb's upper-left
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, segments=24, ring_count=12, location=(-0.055, -0.104, zc + 0.04))
    h = bpy.context.active_object
    h.scale = (0.036, 0.016, 0.066)
    h.rotation_euler = (0, math.radians(18), 0)
    h.data.materials.append(hi)
    return [drop, tail, st, h], 1.08, -0.01


def obj_embarrassed(scene, inner=INNER):
    """One solid round blush-pink patch, soft feathered edge, no face. Blush pink #F08AA0, hot centre #E85D7E."""
    import numpy as np
    N = 256
    ys, xs = np.mgrid[0:N, 0:N]
    d = np.hypot(xs - (N - 1) / 2, ys - (N - 1) / 2) / (N / 2)      # 0 centre .. 1 at image edge
    R_SOLID, R_EDGE = 0.72, 1.0                                     # solid to 55%, feather out to 98% of the plane
    t = np.clip((d - R_SOLID) / (R_EDGE - R_SOLID), 0, 1)
    a = 1 - (t * t * (3 - 2 * t))                                    # smoothstep feather
    hot = np.array(hexlin("E85D7E"))
    pink = np.array(hexlin("F08AA0"))
    fld = np.array(hexlin(inner))
    c = np.clip(d / 0.62, 0, 1)[..., None] ** 1.3                    # hot centre -> pink rim of the solid patch
    patch = hot * (1 - c) + pink * c
    rgb = fld * (1 - a[..., None]) + patch * a[..., None]
    px = np.concatenate([rgb, np.ones((N, N, 1))], axis=2).astype("float32")
    img = bpy.data.images.new("blush", N, N, float_buffer=True)
    img.colorspace_settings.name = "Non-Color"                       # values above are already linear; Standard view applies the sRGB curve
    img.pixels.foreach_set(px.ravel())
    img.pack()
    m = bpy.data.materials.new("blush")
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    t_ = nt.nodes.new("ShaderNodeTexImage")
    t_.image = img
    t_.interpolation = "Linear"
    t_.extension = "EXTEND"
    nt.links.new(t_.outputs["Color"], em.inputs["Color"])
    nt.links.new(em.outputs[0], out.inputs["Surface"])
    rad, seg = 0.32, 64                                              # circular patch, so no square corners reach the ring
    v = [(0, 0, 0)] + [(rad * math.cos(2 * math.pi * i / seg), rad * math.sin(2 * math.pi * i / seg), 0) for i in range(seg)]
    f = [(0, 1 + i, 1 + (i + 1) % seg) for i in range(seg)]
    me = bpy.data.meshes.new("blush")
    me.from_pydata(v, [], f)
    uv = me.uv_layers.new(name="UVMap")
    for li, lp in enumerate(me.loops):
        x, y, _ = v[lp.vertex_index]
        uv.data[li].uv = (0.5 + 0.5 * x / rad, 0.5 + 0.5 * y / rad)
    me.materials.append(m)
    o = bpy.data.objects.new("blush", me)
    scene.collection.objects.link(o)
    return [o], 1.0, 0.0


OBJECTS = {"grease_fingers": obj_grease_fingers, "embarrassed": obj_embarrassed}


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    opt = {"--inner": INNER}
    for i in range(0, len(argv), 2):
        opt[argv[i]] = argv[i + 1]
    name, border, out = opt["--object"], opt["--border"].lstrip("#"), os.path.abspath(opt["--out"])
    inner = opt["--inner"].lstrip("#")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    badge = build_badge(border, inner)
    builder = OBJECTS[name]
    objs, scl, dz = builder(scene, inner) if name == "embarrassed" else builder(scene)
    # objects are authored Z-up facing the camera at -Y; a group empty sets size, centring and the small lift in front of the badge
    grp = bpy.data.objects.new("grp", None)
    scene.collection.objects.link(grp)
    for o in objs:
        if o.name not in scene.collection.objects:
            scene.collection.objects.link(o)
        o.parent = grp
    grp.scale = (scl, scl, scl)
    grp.location = (0, -0.06, dz * scl)
    if name == "embarrassed":
        objs[0].rotation_euler = (math.radians(90), 0, 0)

    cam = bpy.data.cameras.new("cam")
    cam.type = "ORTHO"
    cam.ortho_scale = ORTHO
    co = bpy.data.objects.new("cam", cam)
    scene.collection.objects.link(co)
    co.location = (0, -4, 0)
    co.rotation_euler = (math.radians(90), 0, 0)
    scene.camera = co
    scene.render.resolution_x = scene.render.resolution_y = RES
    scene.render.resolution_percentage = 100
    look.lights(scene)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    look.render(scene, out, samples=32)

    if "--final" in opt:
        fin = os.path.abspath(opt["--final"])
        os.makedirs(os.path.dirname(fin), exist_ok=True)
        code = ("from PIL import Image;import numpy as np;"
                "im=np.asarray(Image.open(r'%s').convert('RGBA')).astype('float64')/255;"
                "a=im[...,3:4];pm=np.concatenate([im[...,:3]*a,a],axis=2);"
                "ch=[Image.fromarray((pm[...,i]*255).round().astype('uint8')).resize((28,28),Image.LANCZOS) for i in range(4)];"
                "p=np.stack([np.asarray(c).astype('float64')/255 for c in ch],axis=2);"
                "al=p[...,3:4];rgb=np.where(al>1e-4,p[...,:3]/np.maximum(al,1e-4),0);"
                "o=np.concatenate([np.clip(rgb,0,1),al],axis=2);"
                "Image.fromarray((o*255).round().astype('uint8'),'RGBA').save(r'%s')" % (out, fin))
        subprocess.run(["python", "-c", code], check=True)
        print("WROTE", fin)


main()
