# Audit: Late-Night Kebab Stand (full 8-file review)

**Files read** (all under `design/worlds/debaucheryville/`):
1. Main md: `Late-Night Kebab Stand.md`
2. `core/late_night_kebab_stand_core.json`
3. `environment/late_night_kebab_stand_environment.json`
4. `interactions/late_night_kebab_stand_interactions.json`
5. `items/late_night_kebab_stand_items.json`
6. `location_nodes/late_night_kebab_stand_location_nodes.json`
7. `npcs/Late_Night_Kebab_Stand/late_night_kebab_stand_npcs.json` and `npc_mr_chadz.md`
8. `PNG_Assets/Late_Night_Kebab_Stand_Complete_PNG_Asset_Requirements.md`
9. `sprite_mapping/late_night_kebab_stand_sprite_mapping.json`
`events/`: MISSING (folder empty or absent; no match). Nothing else is missing.
Review image: `dev/asset_team/reviews/late_night_kebab_stand_ext_review.jpg` (no interior; sprite_mapping lists the interior as `not_built_yet`).

## Q1, how well does it represent the location? Score 3/5 (unchanged)
Present: "MR. CHADZ KEBABS" sign, white LED strip, hookah pipe on the roof, vertical rotisserie, rusty cart between chain-link and wall, "NFT 4 LYFE" wall, rainbow puddle, flyer and cans. Recognisably this stand.
Missing: the cart reads as a tidy cooking stall, not "a fluorescent grease beacon wedged between nightclub fallout and a chain-link fence" (core.json atmosphere). No visible rat on chili (md L41); no condom confetti at readable scale; no tent flap, NOT A TOILET sign or chili-sauce trail at the cart (location_nodes `lks_crawlspace`); no burner phone at the counter (`lks_counter`); no queue of post-club customers or steam silhouettes (npcs.json ambient).

## Q2, how well does it lean into the design requirements? Score 2/5 (unchanged)
Md palette: #FFFFFF dominant, #FF6B35 accent, #2C2C2C ground. The plate is brown brick and cobble with a thin white strip, the "respectable Prague" look. PNG spec (L92-101) adds #FF1493 glitter pink, #4B4B4B vest gray, #FFD700 gold, #000000; none appear. PNG spec L537: "no soft light anywhere in the alley"; the painted light is warm and moody.

## Verdict: REDO (exterior), unchanged. The new files add required nodes the plate lacks. Interior: none (md L49 "Hidden Areas: None"; open-air).

## Redo plan
- **Hook:** "An edible walk of shame under fluorescent interrogation lighting" (PNG L535); core.json tagline "Open After Better Judgment Closes".
- **Palette:** #FFFFFF glare bank, largest mass; #FF6B35 grease slicks; #2C2C2C ground; #FF1493 LED accents (PNG L98); #4B4B4B cart metal; #FFD700 accents; #000000 deepest shadow.
- **Exterior (by node):** `lks_cart` rusty rotisserie under crooked sign and zip-tied LEDs, glare dominant; `lks_menu` eight-item menu board; `lks_counter` order point beside the burner phone, Mr. Chadz station (crop top over bulletproof vest, npc md L40-41); `lks_consume` standing zone of steam, wrappers, gutter reflections, queue along the chain-link (PNG L549); `lks_crawlspace` tent flap, NOT A TOILET sign, chili-sauce trail; `lks_exit` alley mouth toward the club.
- **Interior:** None.
- **Satire beats:** (1) glare vs dim alley; (2) rainbow grease; (3) rat on chili; (4) NFT graffiti; (5) condom and Red Bull confetti; (6) NOT A TOILET flap to the shrine; (7) vest tape "V.C.C. - DOOR 2" (npc md L190).
- **Conflicts, need approval:**
  - Md L49 says no hidden areas; core, nodes and interactions give a crawlspace (03:00-03:59) to the shrine. Which wins for the plate?
  - Palette: md/PNG hex versus core.json words ("grease amber", "chili red", "alley cyan"; cyan is in neither).
  - Prices: md and npc md say SOVS; items.json says "Kebab Coins or source-defined currency".
  - Mr. Chadz: sprite only, or in the plate?
