"""Protocol steps 1-3 package files: copies the SAM masks / crops / overlay sheets into the package and writes source_references.json (step 1) and material_manifest.json (step 3,
format of tools/paint_zones/manifest_schema.md). Colours come from the SAM crops' own pixels (segment.json), never from names. Run from the worktree root."""
import json, os, shutil, hashlib
PK = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
SAMW = os.environ.get("PAINT_ZONES_WORK", "tools/paint_zones/work")  # machine-specific: set PAINT_ZONES_WORK
for sub in ("masks", "crops", "sam_overlays"):
    os.makedirs(f"{PK}/{sub}", exist_ok=True)
seg = {}
for a in ("cabinet_trial_front", "cabinet_trial_side"):
    seg[a] = json.load(open(f"{SAMW}/{a}/segment.json"))
    for z in seg[a]["zones"]:
        for sub in ("masks", "crops"):
            src = f"{SAMW}/{a}/{sub}/{z}.png"
            if os.path.exists(src):
                shutil.copy(src, f"{PK}/{sub}/{a.replace('cabinet_trial_', '')}_{z}.png")
    shutil.copy(f"{SAMW}/{a}/segment_sheet.jpg", f"{PK}/sam_overlays/{a}_segment_sheet.jpg")
    shutil.copy(f"{SAMW}/{a}/segment.json", f"{PK}/masks/{a}_segment.json")
    shutil.copy(f"{SAMW}/{a}/segment_sheet_legend.txt", f"{PK}/sam_overlays/{a}_legend.txt")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
R = f"{PK}/source_references/aa_prop_cabinet_"
srcs = {"asset_id": "street_arcade_cabinet", "version": "exterior_07_props (generated 2026-10-26 set; day/night/emit registered together)",
        "registered": "2026-11-14", "note": "Canonical approved references, copied byte-identical; the originals in absinthearcade_exterior/07_props are untouched. Registered here, not in tools/paint_zones/refs/registry.json (shared untracked file in another checkout).",
        "canonical": [{"path": f"{R}{v}_{k}.png", "sha256": sha(f"{R}{v}_{k}.png"), "role": "canonical", "view": v, "pass": k} for v in ("front", "side") for k in ("day", "night", "emit")],
        "pixel_scale": {"front_px": [290, 740], "side_px": [383, 740], "height_m": 1.85, "width_m": 0.725, "depth_m": 0.958, "ppm": 400, "source": "07_props/props.json"},
        "derived": [{"path": "derived (tmp, not packaged): *_flat.png = canonical composited on white/black, *_mirror = horizontal flip of the side ref for the -X face", "role": "derived"}],
        "raw_mesh": {"path": f"{PK}/mesh/arcade_cabinet_tripo_raw.glb", "sha256": sha(f"{PK}/mesh/arcade_cabinet_tripo_raw.glb"), "role": "geometry measuring stick only; rejected as the trial mesh"}}
json.dump(srcs, open(f"{PK}/source_references.json", "w"), indent=1)

M = lambda a: 0.725 / 290
# zone: (label, finish, wear, markings, pattern, library/projection note)
FZ = {
 "marquee": ("lime-green marquee panel, pixel-font lettering, checker border, two invader sprites", "backlit acrylic, glossy", "light scuffs at the rim; faint gradient (painted glow is NOT in base colour: see emissive)", [{"text": "ABSINTHE ARCADE", "where": "marquee centre, dark green pixel font"}], "flat lime with dark ink"),
 "marquee_ink": ("dark green ink of the marquee: lettering, invaders, checker border", "printed on acrylic", "none visible", [{"text": "ABSINTHE ARCADE", "where": "two lines"}], "ink over lime"),
 "crt_bezel": ("black plastic CRT bezel and recess, with magenta hood reflection", "glossy plastic", "light scratches", [], "none"),
 "crt_screen": ("CRT glass, dark teal-grey", "glass, glossy", "painted reflection streak top-left (a painted feature)", [], "none"),
 "screen_invader": ("pale green space-invader sprite on the screen", "lit pixels (also in emissive)", "none", [{"text": "", "where": "invader sprite centre of screen"}], "pixel art"),
 "control_panel": ("yellow control deck with joystick and six buttons (red, white x2, red, yellow x2, blue x2 as painted)", "painted steel + plastic buttons", "paint wear on the deck edge", [], "none"),
 "joystick_red": ("red joystick ball", "glossy plastic", "none", [], "none"),
 "lower_fascia": ("black painted panel under the deck, vertical grime streaks", "matte paint", "grime streaks painted in the reference (distress: author hand-paints wear; the painted streaks are kept as approved pixels, nothing added)", [], "vertical streaks"),
 "coin_door": ("black steel coin door: two red coin lamps, two slots, hinge and lock", "painted metal", "worn edges", [], "none"),
 "kick_panel_stickers": ("yellow kick plate covered in stickers (sticker bomb)", "vinyl stickers on painted board", "none", [{"text": "various sticker art", "where": "whole plate"}], "sticker collage"),
 "rail_left": ("left yellow side rail", "painted wood/steel", "edge chipping", [], "none"),
 "rail_right": ("right yellow side rail", "painted wood/steel", "edge chipping", [], "none"),
 "side_body": ("black cabinet side with painted scuffs and chips, wear heaviest at the bottom", "matte paint", "scuffs/cracks painted in the reference (distress: the author's Ucupaint pass owns further wear)", [], "none"),
 "side_stickers": ("sticker bomb on the side panel", "vinyl stickers", "none", [{"text": "various sticker art", "where": "centre-right of side panel"}], "sticker collage"),
 "side_trim": ("thin yellow edge line around the side silhouette", "painted edge", "edge wear", [], "line"),
}
mats = []
for a, view in (("cabinet_trial_front", "front"), ("cabinet_trial_side", "side")):
    for z, v in seg[a]["zones"].items():
        lab, fin, wear, mk, pat = FZ[z]
        mats.append({"zone": z, "view": view, "label": lab, "library_ref": None,
                     "mask": f"masks/{view}_{z}.png", "crop": f"crops/{view}_{z}.png",
                     "colors": {"median": v["median"], "shadow": v["shadow"], "light": v["light"]}, "sam_score": v["score"], "area_px": v["area"],
                     "pattern": pat, "finish": fin, "wear": wear, "scale_m_per_px": round(M(0), 5),
                     "markings": mk, "observed": "direct", "inferred_from": None,
                     "projection": "camera_match (orthographic, no offset; mesh built from the references' own silhouette)",
                     "notes": "SAM 2.1 hiera_base_plus box+point prompts, masks overlay-checked by the technical artist (blind QC pending)."})
mats.append({"zone": "front_rest", "view": "front", "label": "remaining front surfaces not in a SAM zone (black body between zones, deck buttons)", "library_ref": None,
             "mask": "derived at projection time (front silhouette minus the zone masks)", "colors": {"median": seg["cabinet_trial_front"]["zones"]["lower_fascia"]["median"]},
             "finish": "matte paint / plastic buttons", "observed": "direct", "projection": "camera_match", "notes": "derived remainder, not a SAM mask"})
mats += [
 {"zone": "left_side_mirrored", "view": "-X face", "label": "-X side face (stickers + trim)", "observed": "inferred", "inferred_from": "the +X side reference mirrored horizontally; the real sticker layout on the other flank is not shown anywhere",
  "projection": "camera_match with mirrored ref + mirrored masks", "finish": "as +X side"},
 {"zone": "back_panel", "view": "back", "label": "back panel", "observed": "inferred", "inferred_from": "no back reference exists. Flat fill #231C24 (the +X side_body median from the reference): a single colour, NO paint detail, grain, wear or markings. (The first package filled it with a bugged near-black, mean RGB 3.)", "colors": {"median": "#231C24"}, "finish": "matte paint (assumed)", "projection": "none (flat fill)"},
 {"zone": "underside_walls_edges", "view": "top/bottom", "label": "underside, recess walls, bevel strips, texels outside the reference silhouette", "observed": "inferred", "inferred_from": "no reference. Underside, recess walls, bevel strips and texels beyond the reference silhouette: flat #231C24 body colour, no detail. The top slope is NOT in this entry: it carries the front reference projected onto the slope (marquee art stretched along it).", "colors": {"median": "#231C24"}, "finish": "matte paint (assumed)", "projection": "none (flat fill)"}]
man = {"asset_id": "street_arcade_cabinet", "reference": {"paths": [f"{R}front_day.png", f"{R}side_day.png"], "sha256": {"front_day": sha(f"{R}front_day.png"), "side_day": sha(f"{R}side_day.png")}, "version": "07_props day plates"},
       "sam": {"model": "sam2.1_hiera_base_plus", "mode": "points+box", "verified_by": "technical artist overlay check; blind reviewer pending (QC gate not run by the producer)"},
       "materials": mats,
       "unseen": ["back panel (flat #231C24)", "underside and plinth (flat #231C24)", "recess walls (CRT, coin door plate)", "-X flank sticker layout (mirrored from +X)"],
       "fallbacks": [
         {"step": 5, "tool": "Tripo multiview texturing (website, optional)", "used": "not run: the Tripo raw mesh failed the geometry check (wrong proportions/design); geometry rebuilt by script from the reference silhouettes (nhxz.3 method); 0 credits spent", "why": "reference silhouette IoU 0.75 on the raw mesh"},
         {"step": 7, "tool": "Modddif", "used": "named fallback is ChatGPT repaint + Blender (nhxz-q3); ChatGPT was NOT needed or used, only Blender/script fixes ran (see quality_report.md)", "why": "Desk nhxz-q3: neither Modddif nor ArmorPaint for now"},
         {"step": 8, "tool": "ArmorPaint", "used": "named fallback is Ucupaint in Blender (nhxz-q3); headless Ucupaint layer scripting failed twice, so scripted Blender AO bake / ORM pack stood in (see quality_report.md)", "why": "Desk nhxz-q3"}],
       "pbr_values_note": "roughness / metallic / sticker-relief height are ASSUMED per finish (inferred, not physically validated); AO is a real Cycles bake of the rebuilt mesh."}
json.dump(man, open(f"{PK}/material_manifest.json", "w"), indent=1)
print("manifest zones", len(mats))
