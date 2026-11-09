"""Integrate the element kits into aa_exterior.blend (E1 owns the main file). Re-runnable.

  blender -b aa_exterior.blend --python-exit-code 1 --python integrate_elements.py -- \
          --save <tmp.blend> [--elements E2 E3 E5] [--report r.json]

1. Refresh each element's kit collections in aa_kit/: delete the old copy, append the current one
   from the element's wip blend (bpy.data.libraries.load, link=False). Kits stay whole, so a
   newer wip is picked up by re-running.
2. Rebuild the shell (bible_camera + build_shell): build_shell leaves out E1's clay surrounds,
   linings, placeholder sashes and rails where an E2 kit exists, the step/floor where E3's
   doorway exists, and the interior backstop where E3's interior set exists.
3. Place every kit with a collection-instance empty in aa_layout (<kit>__01), per interfaces v2.1:
   E2 front kits at (e2_place.x, face_y, e2_place.sill); side kits turned +90 deg about Z (their
   street face -Y to +X) at (face_x, u_center, sill_z); E3 and E5 kits are modelled in place.
   The cat goes on L2's sill where E2 seats it.
4. Retire what the kits replace into aa_retired (excluded from the view layer, not deleted).
5. Put E5's stone and peeling-plaster materials on the shell's stone.
Saves a copy to --save; the caller swaps it over the main file after Blender exits.
"""

import argparse
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import aa_common as aa  # noqa: E402

WIP = aa.ASSET_ROOT / "blender" / "wip"
IFACE = json.loads((aa.REPO / "dev/aa_team/interfaces.json").read_text(encoding="utf-8"))

E2_KITS = ["aa_window_l1_arched", "aa_window_l2_cat", "aa_window_l3_balcony", "aa_window_r1", "aa_window_r2",
           "aa_window_side_w0", "aa_window_side_w1", "aa_window_side_w2",
           "aa_window_dormer_l", "aa_window_dormer_r", "aa_window_dormer_side"]
ELEMENTS = {
    "E2": dict(blend=WIP / "E2_windows.blend", kits=E2_KITS, place="e2"),
    "E3": dict(blend=WIP / "E3_entrance.blend", kits=["aa_e3_marquee", "aa_e3_doorway", "aa_e3_interior_set"],
               place="in_place"),
    "E5": dict(blend=WIP / "E5_surface.blend", kits=["aa_e5_mural"], place="in_place",
               materials=["m_e5_limestone_peeling", "m_e5_limestone_carved"]),
    "GH": dict(blend=WIP / "E2_roof_gable_head.blend", place="gable_head", kits=["aa_roof_gable_head"],
               objects=["aa_shell_facade_roof_gable_head"]),
    "E6": dict(blend=WIP / "E6_street.blend", place="in_place",
               kits=["aa_e6_cabinet", "aa_e6_chalkboard", "aa_e6_awning", "aa_e6_lantern_l", "aa_e6_lantern_r",
                     "aa_e6_shrub", "aa_e6_bollards", "aa_e6_wall_signs", "aa_e6_bucket", "aa_e6_clocktower_sign",
                     "aa_e6_stone_post", "aa_e6_ground"]),
}
RETIRE = {
    "E2": dict(layout=[f"aa_prop_window_pot__{i:02d}" for i in range(1, 8)]
               + ["aa_ornament_window_crest__01", "aa_ornament_window_crest__02"]),
    "E3": dict(objects=["aa_arch_hero_marquee", "aa_arch_hero_tagline_panel", "aa_arch_hero_marquee_mounts",
                        "aa_arch_hero_door_leaf_l", "aa_arch_hero_door_leaf_r"],
               layout=["aa_prop_doorframe_sign__01"]),
    "E5": dict(layout=[]),
    "E6": dict(layout=["aa_prop_arcade_cabinet__01", "aa_prop_chalkboard__01", "aa_prop_bollard__01",
                       "aa_prop_bollard__02", "aa_prop_wall_lantern__01", "aa_prop_wall_lantern__02",
                       "aa_prop_awning__01", "aa_prop_hanging_sign__01", "aa_prop_planter__01"]),
}
E5_STONE = {"aa_shell_facade_walls": "m_e5_limestone_peeling"}
E5_CARVED = ["aa_shell_facade_mouldings", "aa_shell_facade_corner_bay", "aa_shell_facade_window_surrounds",
             "aa_arch_hero_archivolt", "aa_arch_hero_plinths", "aa_shell_facade_roof",
             "aa_shell_facade_roof_gable_head_PLACEHOLDER", "aa_shell_facade_roof_gable_chimneys"]


def coll(name, parent):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
    if c.name not in [ch.name for ch in parent.children]:
        parent.children.link(c)
    return c


def drop_collection(name):
    c = bpy.data.collections.get(name)
    if c is None:
        return 0
    n = 0
    for ch in [c] + list(c.children_recursive):
        for o in list(ch.objects):
            bpy.data.objects.remove(o, do_unlink=True)
            n += 1
    for ch in reversed(list(c.children_recursive)):
        bpy.data.collections.remove(ch)
    bpy.data.collections.remove(c)
    return n


def refresh_objects(el, kit_root):
    """Kits delivered as objects only (append the object, wrap it in its own aa_kit collection)."""
    spec = ELEMENTS[el]
    k = spec["kits"][0]
    drop_collection(k)
    c = coll(k, kit_root)
    with bpy.data.libraries.load(str(spec["blend"]), link=False) as (src, dst):
        missing = [o for o in spec["objects"] if o not in src.objects]
        dst.objects = [o for o in spec["objects"] if o in src.objects]
    got = []
    for o in dst.objects:
        if o is None:
            continue
        c.objects.link(o)
        got.append(o.name)
    return dict(appended=got, missing=missing)


def place_gable_head():
    """Fill the gable arch where E1's placeholder was: the kit's pivot is bottom centre with its
    flat back on y=0 facing -Y, authored 1 m tall; scaled uniformly to the arch's head zone and set
    flush on the gable panel face."""
    G = aa.load_manifest()["facade"]["roof"]["gable"]
    h0, h1 = G["head_z"]
    c = bpy.data.collections.get("aa_roof_gable_head")
    if c is None or not c.objects:
        return None
    ob = c.objects[0]
    zs = [(ob.matrix_world @ v.co).z for v in ob.data.vertices]
    k = (h1 - h0 + 0.05) / max(max(zs) - min(zs), 1e-6)
    loc = instance("aa_roof_gable_head", (0.0, G.get("panel_face_y", -0.04), h0 - 0.05))
    e = bpy.data.objects["aa_roof_gable_head__01"]
    e.scale = (k, k, k)
    return loc + [round(k, 4)]


def refresh_kits(el, kit_root):
    spec = ELEMENTS[el]
    if "objects" in spec:
        return refresh_objects(el, kit_root)
    for k in spec["kits"]:
        drop_collection(k)
    with bpy.data.libraries.load(str(spec["blend"]), link=False) as (src, dst):
        missing = [k for k in spec["kits"] if k not in src.collections]
        dst.collections = [k for k in spec["kits"] if k in src.collections]
        if spec.get("materials"):
            dst.materials = [m for m in spec["materials"] if m in src.materials]
    got = []
    for c in dst.collections:
        if c is None:
            continue
        kit_root.children.link(c)
        got.append(c.name)
    return dict(appended=got, missing=missing,
                materials=[m.name for m in (dst.materials if spec.get("materials") else []) if m])


def instance(kit, loc, rot_z=0.0):
    lay = bpy.data.collections[aa.LAYOUT_COLL]
    name = f"{kit}__01"
    e = bpy.data.objects.get(name)
    if e is None:
        e = bpy.data.objects.new(name, None)
    if e.name not in lay.objects:
        lay.objects.link(e)
    e.instance_type = "COLLECTION"
    e.instance_collection = bpy.data.collections[kit]
    e.empty_display_size = 0.3
    e.location = loc
    e.rotation_euler = (0.0, 0.0, rot_z)
    e.scale = (1.0, 1.0, 1.0)
    e.hide_render = False
    return [round(v, 4) for v in loc] + [round(math.degrees(rot_z), 1)]


def place_e2():
    out = {}
    for k in E2_KITS:
        c = bpy.data.collections.get(k)
        if c is None:
            continue
        P = json.loads(c["e2_params"]) if "e2_params" in c else {}
        if "e2_side_place" in c:
            sp = json.loads(c["e2_side_place"])
            fx = sp.get("face_x", IFACE["side_right"]["frame"]["face_x"])
            out[k] = instance(k, (fx, sp["u_center"], sp["sill_z"]), math.radians(90.0))
        else:
            x, z = list(c["e2_place"])
            out[k] = instance(k, (x, P.get("face_y", 0.0), z))
    return out


def place_cat():
    """E2's seat for the cat (review_e2.place_cat): on L2's sill, right of centre, outside the glass."""
    c = bpy.data.collections.get("aa_window_l2_cat")
    cat_kit = bpy.data.collections.get("aa_prop_window_cat")
    e = bpy.data.objects.get("aa_prop_window_cat__01")
    if not (c and cat_kit and e and cat_kit.objects):
        return None
    k = c.get("e2_scale_k", 1.0)
    x, z = list(c["e2_place"])
    ob = cat_kit.objects[0]
    pts = [ob.matrix_world @ v.co for v in ob.data.vertices]
    y_mid = (max(p.y for p in pts) + min(p.y for p in pts)) / 2
    e.location = (x + 0.13 * k - ob.matrix_world.translation.x, -0.075 * k - y_mid, z - min(p.z for p in pts))
    e.rotation_euler = (0.0, 0.0, 0.0)
    return [round(v, 4) for v in e.location]


def retire(el):
    rc = bpy.data.collections.get("aa_retired") or bpy.data.collections.new("aa_retired")
    if rc.name not in [ch.name for ch in bpy.context.scene.collection.children]:
        bpy.context.scene.collection.children.link(rc)
    rc.hide_render = True
    out = []
    spec = RETIRE.get(el, {})
    for n in spec.get("objects", []) + spec.get("layout", []):
        o = bpy.data.objects.get(n)
        if o is None:
            continue
        for uc in list(o.users_collection):
            uc.objects.unlink(o)
        rc.objects.link(o)
        o.hide_render = True
        out.append(n)
    for lc in bpy.context.view_layer.layer_collection.children:
        if lc.name == "aa_retired":
            lc.exclude = True
    return out


def e5_materials_from_context():
    """Take E5's stone materials from the shell objects E5 actually painted (its context copies of
    the shell), not by name: E5's wip appends the main file's shell, so its own new materials can
    come out suffixed (.001). Appends those objects, copies their slot materials onto the real
    shell, removes the copies, drops the superseded materials and restores the canonical names."""
    names = list(E5_STONE) + [n for n in E5_CARVED if n.startswith(("aa_shell", "aa_arch"))]
    with bpy.data.libraries.load(str(ELEMENTS["E5"]["blend"]), link=False) as (src, dst):
        dst.objects = [n for n in names if n in src.objects]
    by_role = {}
    for ob in dst.objects:
        if ob is None:
            continue
        base = ob.name.rsplit(".", 1)[0] if ob.name not in names else ob.name
        mats = [sl.material for sl in ob.material_slots if sl.material]
        role = "peel" if base in E5_STONE else "carved"
        for mt in mats:
            if mt.name.startswith("m_e5_limestone"):
                by_role.setdefault(role, mt)
        me = ob.data
        bpy.data.objects.remove(ob, do_unlink=True)
        if me and me.users == 0:
            bpy.data.meshes.remove(me)
    out = {}
    for role, canon in (("peel", "m_e5_limestone_peeling"), ("carved", "m_e5_limestone_carved")):
        new = by_role.get(role)
        if new is None:
            continue
        for m in [m for m in bpy.data.materials if m.name.startswith(canon) and m != new]:
            m.user_remap(new)
            bpy.data.materials.remove(m)
        new.name = canon
        out[role] = new.name
    return out


def e5_materials():
    peel = bpy.data.materials.get("m_e5_limestone_peeling")
    carved = bpy.data.materials.get("m_e5_limestone_carved")
    if not (peel and carved):
        return "E5 materials missing"
    done = {}
    for n, mname in E5_STONE.items():
        o = bpy.data.objects.get(n)
        if o:
            for s in o.material_slots:
                s.material = peel
            done[n] = peel.name
    for n in E5_CARVED:
        o = bpy.data.objects.get(n)
        if not o:
            continue
        for s in o.material_slots:
            if s.material and s.material.name.startswith(("m_aa_trim", "m_aa_limestone")):
                s.material = carved
        done[n] = carved.name
    return done


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--save", required=True)
    ap.add_argument("--elements", nargs="*", default=["E2", "E3", "E5", "E6"])
    ap.add_argument("--report")
    a = ap.parse_args(argv)
    kit_root = bpy.data.collections[aa.KIT_COLL]
    rep = {"elements": a.elements, "kits": {}, "placed": {}, "retired": {}}
    for el in a.elements:
        rep["kits"][el] = refresh_kits(el, kit_root)
    import bible_camera
    import build_shell
    bible_camera.main()
    rep["shell"] = build_shell.main()
    for el in a.elements:
        if ELEMENTS[el]["place"] == "e2":
            rep["placed"].update(place_e2())
            rep["placed"]["aa_prop_window_cat"] = place_cat()
        elif ELEMENTS[el]["place"] == "gable_head":
            rep["placed"]["aa_roof_gable_head"] = place_gable_head()
        else:
            for k in ELEMENTS[el]["kits"]:
                if k in bpy.data.collections:
                    rep["placed"][k] = instance(k, (0.0, 0.0, 0.0))
        rep["retired"][el] = retire(el)
    if "E5" in a.elements:
        rep["e5_material_source"] = e5_materials_from_context()
        rep["e5_materials"] = e5_materials()
    bpy.context.view_layer.update()
    bpy.ops.wm.save_as_mainfile(filepath=a.save, copy=True)
    text = json.dumps(rep, indent=1, default=str)
    if a.report:
        Path(a.report).write_text(text, encoding="utf-8")
    print("@@JSON@@" + json.dumps({"saved": a.save, "placed": len(rep["placed"])}))


main()
