# Absinthe Arcade: interactables audit (Eurobound-31uj.2)

Read-only audit of every Absinthe Arcade room against `design/style_guides/location_interactables_rule.md` (author, 2026-11-14). No repo file was changed and no image was generated. Whether the approved plates get reworked now is still open with the author (Desk `Eurobound-31uj-q1`, rule line 5). This report sizes that rework; it does not decide it.

## Part 1: Summary

**85 rows: 52 OK, 25 VIOLATION, 8 MISSING.** MISSING means the code or docs refer to an interactable that has no art anywhere, so it is not painted in, but nothing has been built either. Many OK rows carry caveats; see column 8.

**Worst violations**
- **Hall:** both claw machines (including the Sea-Monkeys, which can never visibly leave), the skee-ball lanes, the foosball table, the bidet stool and the restroom door are all painted. Each has a live hotspot.
- **North wing:** the broken DDR, the maintenance door (its painted lamps show red and green at once), the Taproom curtain, the Time Crisis cabinet and the vapour are painted, though the docs give each of them states.
- **Closet:** almost every hotspot is painted. Cut-outs for the DDR arrows, the CRT and the sock chute already exist but nothing loads them.
- **Others:** the window cat, the restroom statue and the Taproom chalice are painted.

**Rework estimate**
- **Inpaint and cut** (day, night and emit):
  - hall plate: 6 machines, the toilet and the claw alcove;
  - north wing plate: 5 items;
  - exterior front face: the cat and the doors;
  - restroom plate: the statue;
  - Taproom plate: the chalice;
  - closet plate: the toilet, the claw arm and 3 graffiti decals.
- **New assets:** VIP arrows, token price board, service note, Backpack Girl nest, haiku, joystick-with-lips, wiring sparks, Broken Prize Tag.
- **Code only:** wire the 11 existing closet cut-outs.
- **Location data:** add the missing entries and reconcile the ids.

## Part 2: Full table

### Legend and short paths
- **gd/** = `game/worlds/debaucheryville/`.
- **ia** = `design/worlds/debaucheryville/interactions/absinthe_arcade_interactions.json`.
- **sm** = `.../sprite_mapping/absinthe_arcade_sprite_mapping.json`.
- **ln** = `.../location_nodes/absinthe_arcade_location_nodes.json`.
- **env** = `.../environment/absinthe_arcade_environment.json`.
- **core** = `.../core/absinthe_arcade_core.json`.
- **items** = `.../items/absinthe_arcade_items.json`.
- **man** = `.../absinthearcade_interior_3d_asset_manifest.md`.
- **png** = `.../PNG_Assets/Absinthe_Arcade_Complete_PNG_Asset_Requirements.md`.
- **cmr-\*** = the `claw_machine_maintenance_closet_restroom_*` companion files.
- **cmr.md** = `clawmachinemaintenanceclosetrestroom.md`.
- **at-\*** = the `absinthium_taproom_*` companion files.
- **at.md** = `the_absinthium_taproom.md`.
- **final.md** = `WritingRoom/tasks/20261112_1419_absinthe_arcade_completion_lines/final.md`.
- **Cut-out**: a PlatePropLayer sprite cut from the plate and laid back over the same pixels (`gd/plate_prop_layer.gd`). It can change state in place. The painted copy is still in the plate underneath, though, so the item cannot move, break or disappear without inpainting the plate.

### Cross-cutting findings
1. **The sprite mapping does not match the build.** sm:249-383 points every interior prop, cabinet and transition at files that do not exist (`interior/props/`, `interior/cabinets/`, `interior/transitions/`, `exterior/props/aa_prop_street_cabinet_day.png`, `aa_prop_window_cat_day.png`). The real art is plate cut-outs under other names (`interior/hall/props/aa_hall_*`, `exterior/props/aa_prop_cabinet_front/side`).
2. **Code and data use different ids, and no table maps one to the other.** Examples:

   | Code id | Data id |
   |---|---|
   | `cabinet_frogger` | `frogger_existential_edition` |
   | `token_machine` | `token_exchange_machine` |
   | `skee_ball` | `skeeball_lanes` |
   | `foosball` | `foosball_table` |
   | `prize_counter` | `prize_redemption_counter` |
   | `bidet_stool` | `bidet_bar_stool` |
   | `vip_arrows` | `fake_vip_wayfinding` |
   | `broken_ddr` | `broken_ddr_restroom_unlock` |
   | `maintenance_door` | `maintenance_restroom_door` |
   | `taproom_curtain` | `absinthium_taproom_curtain` |
   | `ddr_toilet` | `cmr_ddr_toilet` / `cmr_use_fixture` |

   Column 5 says "yes" when the object has an entry under its data id.
3. **No location files exist for the public restroom (the Green Fairy statue room).** `public_restroom_grease_trap_shrine_*` belongs to a different location. The engine copies under `game/assets/data/locations/debaucheryville/` hold only `absinthe_arcade_hall_lines.json` and `_microcopy.json`, with no per-object data.
4. **The man "Build audit" is stale.** man:197-224 calls the cabinets, DDR and token machine painted with no state art. The round v43 hall cut-outs (`gd/absinthe_arcade_interior_hd2d.gd:224-239`) now cover them.
5. **The closet cut-outs are built but unwired.** `interior/closet/props/aa_closet_props.json` lists 8 DDR arrows (on/off), 2 CRT states and the sock chute. No script loads them (grep: no reference in `game/`).

### Exterior (`gd/absinthe_arcade_exterior_hd2d.gd`; plate viewed: `exterior/faces/aa_face_front_day.png`)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| Exterior | Street cabinet (sticker-bombed, "OUT OF ORDER") | interactive | Separate 3D prop: front and side cards on a box (`gd:43`, `_build_cabinet` 268-298) | yes: sm:368 (wrong file name), ln:57 | `street_cabinet` (examine, gd:884) | OK | Nothing to paint. Add an ia entry for the examine and fix the sm file name |
| Exterior | Free Wi-Fi hotspot (in the street cabinet) | interactive | Code-drawn `wifi_hotspot.tscn` with its sign hidden (gd:859-878) | no: the id is in no design or data file | `debaucheryville_absinthe_arcade_facade` | VIOLATION | Declare it in the location files (ia/sm, and the `wifihotspots.md` list). No art needed |
| Exterior | Chalkboard (REAL ARCADE / REAL ABSINTHE / REAL BAD DECISIONS) | interactive | Separate A-frame prop (gd:46, 302-313) | yes: sm:373, ln:58, png:137 | `chalkboard` (gd:885) | OK | Add an ia entry for the examine |
| Exterior | Window cat (black cat on the left first-floor sill) | interactive (examine); png:144 also wants an idle loop | Painted into `aa_face_front` day/night | yes: sm:378 (points at a missing `aa_prop_window_cat_day.png`), core:141, png:144 | `window_cat` (gd:886) | VIOLATION: examined, specced to animate, but painted into the face | Cut the cat out of front-face day/night/emit as a card, inpaint the sill and window behind it, and place the card on the sill. The cat must stay (canon) |
| Exterior | Club-flyer panel (empty / posted) | interactive | Separate overlay cards with 2 states (gd:170-222) | yes: ia:572 (says node `aa_node_entry_vestibule`, i.e. inside), env:267-269 (`exterior_flyer_panel`), png:145 | `flyer_panel` (gd:896) | OK | Nothing to paint. Make ia and env agree on where it hangs |
| Exterior | Front stained-glass doors and painted entrance glimpse | interactive (door the bros enter) | Painted into `aa_face_front`; walk-through Area3D `exit_front_door` (gd:842-853) | yes: core:48-53 (exit), ln:64 | scene exit only | VIOLATION (low): an entered door is painted, with no states | Cut the door leaves and the entrance glimpse as a layer (png:127 `aa_layer_entrance_interior`, never built) |
| Exterior | Street dressing: awning, bucket, TOKENS wall sign, 2 lanterns, shrub, 4 bollards | prop | Separate cards and billboards (gd:42-55) | partly: png:136-143 (none in sm) | none | OK | Nothing |
| Exterior | Facade scenery: mural, Headphone Gentleman, marquee, menu board, "13" plaque, conduit, junction boxes, window boxes, roof | background | Painted faces | yes: core:131-140; png:125-126 spec the marquee and keystone as depth layers (not built) | none | OK | Nothing (unless the marquee flicker in sm:527 is wanted, which needs a layer) |

### Hall (`gd/absinthe_arcade_interior_hd2d.gd`; plate viewed: `interior/hall/aa_int_hall_day.png`)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| Hall | Frogger cabinet (back row #2) | interactive | Cut-out `cab_frogger`, attract/in_use (gd:231) | yes: ia:87, sm:263 (file missing) | `cabinet_frogger` (gd:80) | OK | Nothing for its states. Inpaint behind it only if it must ever move or vanish |
| Hall | Street Fighter cabinet (back row #4) | interactive | Cut-out `cab_street_fighter` (gd:232) | yes: ia:121, sm:269 | `cabinet_street_fighter` (gd:81) | OK | As Frogger |
| Hall | Kebab Kombat cabinet (right wall) | interactive | Cut-out `cab_kebab_kombat` (gd:233) | yes: ia:155, sm:275 | `cabinet_kebab_kombat` (gd:84) | OK | As Frogger |
| Hall | DDR dance-off: 3 pads, wall screen and coin kiosk | interactive | Cut-outs `ddr_pads` (idle/lit) and `ddr_screen` (5 states) (gd:234-235). The kiosk stays painted | yes: ia:195, man:210-211 | `ddr_dance_off` (gd:85) | OK | Nothing (the game screen is unwired, waiting on songs) |
| Hall | TOKENS HERE token machine | interactive | Cut-out `token_machine`, 4 states (gd:236, 664-672) | yes: ia:63, sm:251, ln:91 | `token_machine` (gd:86) | OK | Nothing (`temporarily_jammed` art is unhooked) |
| Hall | Signage: TOKENS HERE arrow, PRIZES arch, PRIZE REDEMPTION sign and bar-front placard | background (wayfinding) | Painted. The placard falls inside the prize-counter cut-out | yes: man:230, png:218 | none (the placard is the `prize_counter` anchor) | OK | Nothing |
| Hall | Token price board "1 SOV = 1 TOKEN" | prop (first-entry camera beat) | Not in the plate; not built | yes: ln:92, png:214, man:225 (TO BUILD); final.md:89 | none | MISSING | New asset (man bead `Eurobound-koq3`) |
| Hall | Cracked-bottle bar counter (POS screen, back-bar bottles) | prop / landmark; quest site ("buy the girls a round") | Cut-out `bar_counter`, default state only (gd:237), plus occluder prism (gd:203-216) | yes: ln:105-115, env:67, sm:188 | none (bark node `aa_node_bottle_bar`) | OK | Caveat: the bottle display is painted inside the cut-out, though the rule lists it as a separate prop |
| Hall | Prize Redemption counter and prize cabinet (Tomáš) | interactive | Cut-out `prize_counter`, default state (gd:238) | yes: ia:411, png:215 | `prize_counter` (gd:103) | OK | Caveat: the shelf prizes are painted, so stock can never visibly run down |
| Hall | Bidet bar stool (a toilet at the bar front) | interactive (examine, chime) | Painted. `aa_hall_bar_counter.json` cuts it out of the bar sprite on purpose, so the plate shows through. Floor blocker gd:192 | yes: ia:610, env:245, ln:113, man:227 | `bidet_stool` (gd:107) | VIOLATION: examined, but painted | Cut it as `aa_prop_bidet_stool` and inpaint the bar front and floor. The art shows a plain toilet, not the canon "bidet on a brass stool base" (ia:616) |
| Hall | Fake VIP arrows (3, looping back to the bar) | interactive | Not in the plate. The hotspot sits on open floor; the gd:104-105 comment assumes the arrows are painted | yes: ia:619, env:240 (mezzanine stair landing), sm:356 (file missing), png:218 | `vip_arrows` (gd:106) | MISSING: the hotspot points at nothing | New 3-arrow asset, then place the hotspot on it |
| Hall | Rigged absinthe claw (PRIZES alcove) | interactive | Painted inside the static depth layer `aa_int_layer_claw_alcove` (gd:220). The PAYOUT light is a code OmniLight (gd:317-324) | yes: ia:463, sm:281 (7 states, file missing), man:203 | `rigged_absinthe_claw_machine` (gd:96) | VIOLATION: has states and a quest prize, but painted | Separate claw prop with its states and light. Inpaint the alcove layer and the plate |
| Hall | Sea-Monkeys inside the rigged claw | pickup (NFT) | Painted among the plush, if it is there at all. Can never visibly leave after the win | yes: items:89, ln:150, env:262 (`empty_sea_monkeys_spot` after the win) | none (`ArcadeClaw.TOP_PRIZE_ID`) | VIOLATION | Separate prize sprite in the claw glass, present/absent, plus an inventory icon (`aa_ui_item_icons`, man:271) |
| Hall | Beanie Baby claw with plush (west wall) | interactive | Painted | yes: ia:306, man:214 | `beanie_baby_claw` (gd:94) | VIOLATION | Separate prop with 5 states; inpaint |
| Hall | Skee-ball lanes ×3 | interactive | Painted (floor blocker gd:184) | yes: ia:230, man:212 | `skee_ball` (gd:89) | VIOLATION | Separate lane props with states; inpaint |
| Hall | Foosball table | interactive | Painted (floor blocker gd:183) | yes: ia:269, man:213 | `foosball` (gd:90) | VIOLATION | Separate prop with states; inpaint |
| Hall | Restroom door (left-wall arch south of TOKENS HERE) | interactive (door, `press_door`) | Painted arch | no: absent from core exits (core:47-82) and ia; mentioned only at man:60 and 168 | `restroom_door` (gd:100) | VIOLATION: an entered door, painted and undeclared | Door asset over the arch, plus core exit and ia entries |
| Hall | Stained-glass entry doors (inside) | interactive (exit) | Static depth-layer cut-out `aa_int_layer_entry_doors` (gd:217-219) and trigger `exit_front_doors` (gd:879-890) | yes: core:48-53, ln:64-72, sm:209 | scene exit | OK | Caveat: one state only, no open/close |
| Hall | North arch to the mirror corridor | background (opening, no door leaf) | Painted; graybox opening and trigger (gd:44-51, 859-878) | yes: ln:161, sm:239 | scene exit | OK | Nothing |
| Hall | Bubble Bobble cabinet | prop | Painted | yes: man:106, 215 | none | OK | Caveat: whether it pays tickets is still open (man:106). If it becomes playable it must be split |
| Hall | Generic cabinet rows (back row, back-left uprights) and their stools | prop | Painted; floor blockers gd:185-186 | yes: man:216-219, ln:136 | none | OK | Caveat: the rule's prop bucket wants cabinets separate. Collision only, no logic |
| Hall | Bar stools and chairs; stools at Kebab Kombat and Bubble Bobble | prop | Painted; invisible blockers (gd:187-193) | yes: man:226 | none | OK | Caveat: "stools in front of counters" is on the rule's baked-by-accident list |
| Hall | Scratched service note (claw strategy clue) | interactive (clue) | Not in the plate; not built | yes: ln:152; env:61-63 | none | MISSING | New examinable asset (or confirm the attendant hint replaces it) |
| Hall | Backpack Girl floor nest / couchsurf hook | interactive (couchsurf trigger) | Not in the plate; no NPC placed | yes: ia:589, env:235, ln:90 | none | MISSING | Nest prop and trigger, plus her sprite (man:253) |
| Hall | Mezzanine: rails, café tables, plants, figures | background | Painted (`aa_int_layer_mezzanine` exists, but the hall does not load it) | yes: sm:199, ln:424 | none (bark node `aa_node_mezzanine` has no position, gd:111-115) | OK | Nothing |
| Hall | Shell: mural, stained glass, vaults, sconces, ivy, checker floor, scattered tickets | background | Painted | yes: man:174-180 | none | OK | Nothing |

### North wing (`gd/absinthe_arcade_north_wing_hd2d.gd`; plate viewed: `interior/north_wing/aa_int_north_wing_day.png`)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| North wing | Broken DDR (cracked pad and cabinet) | interactive | Painted | yes: ia:495, sm:295 (6 states), man:204 | `broken_ddr` (gd:36) | VIOLATION | Separate prop: error, 0-3 pips, unlock pulse; inpaint |
| North wing | DDR token pips | state overlay | Code-drawn ●○ text flash (gd:192) | yes: png:239, man:245 (TO BUILD) | part of `broken_ddr` | OK | Caveat: a stand-in; art bead `Eurobound-w2ig` |
| North wing | Maintenance door, MAINTENANCE ONLY sign, indicator lamps | interactive (door, locked/unlocked) | Painted; the lamps are painted red and green lit at once. The unlock light is a code OmniLight (gd:146-152) | yes: ia:519, core:67-81, sm:333 (locked_red / unlocked_green), man:244 | `maintenance_door` (gd:37) | VIOLATION: a stateful door, painted | Door prop with lock states; inpaint the lamp region |
| North wing | Taproom curtain (left arch) and brass plaque | interactive | Painted, glowing even in the day plate | yes: ia:532, core:55-66, sm:320 (4 time states), man:240-243 | `taproom_curtain` (gd:40) | VIOLATION: its time states cannot show | Curtain prop with day/evening/night/discovered states; glow as a layer |
| North wing | Cracked Time Crisis cabinet (gun, by the curtain) | prop with states in the docs | Painted in its displaced pose; floor blocker gd:61; mist point gd:74 | yes: sm:309 (curtain_hidden / displaced_revealed / night_glow, bound to the curtain), man:205 | none | VIOLATION: the docs give it 3 states; it is painted in one | Separate cabinet prop with states; inpaint |
| North wing | Green vapour at the curtain base | FX anchor | Painted, static; code mist particles too (gd:74) | yes: env:173-178 (20:00-04:00 only), man:242 | none | VIOLATION (low): baked vapour shows at all hours, against the time rule | Paint it out; vapour FX layer (`aa_transition_taproom_vapor`) |
| North wing | Wire bridge and junction panels (DDR to door) | background | Painted | yes: png:240, man:246 | none | OK | Nothing |
| North wing | Cabinet rows (~17) and stools | prop | Painted; floor blockers gd:56-62; screen-glitch points gd:80-81 | yes: ln:182 | none | OK | Caveat as for the hall cabinet rows |
| North wing | Shell: pendant lamps, stained window, posters, ivy, pots, floor | background | Painted | yes: man:179-180, 233-235 | none | OK | Nothing |

### Mirror corridor (`gd/absinthe_arcade_mirror_corridor_hd2d.gd`; plate viewed: `interior/mirror_corridor/aa_int_corridor_day.png`)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| Mirror corridor | Shadow switches 1-3 | interactive | Cut-outs, idle/pressed (gd:44-51, 191-204) | yes: ia:554 (switch_count 3), ln:169 | `shadow_switch_1` to `_3` (gd:135-136) | OK | Caveat: the individual switch ids are not declared in data |
| Mirror corridor | Gilded wall mirrors (both walls) | prop | Painted | yes: ln:168 (`lagging_mirror_panels`), png:177 | none | OK | Caveat: if the lagging reflections (`aa_fx_mirror_afterimages`, man:263) are ever drawn in the mirrors, they need mirror cards |
| Mirror corridor | Afterimage hint | FX | Code-drawn PartySprite3D (gd:258-320) | yes: ia:554 | none | OK | Nothing |
| Mirror corridor | Broken Game Boy | pickup | No world prop; granted when the puzzle is solved (`mirror_shadow_puzzle.gd:13`) | yes: ia:566, items:118, ln:170 (`broken_game_boy_hide`) | none | OK | Caveat: no world prop or hide object. Icon TO BUILD (man:271) |
| Mirror corridor | Velvet benches and potted palms | prop | Painted; floor blockers gd:28-37 | no | none | OK | Nothing |
| Mirror corridor | Shell: arches, sconces, light tubes, ivy, floor | background | Painted | yes: man:193 | scene exits | OK | Nothing |

### Public restroom (`gd/absinthe_arcade_restroom_hd2d.gd`; plate viewed: `interior/restroom/aa_int_restroom_day.png`)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| Restroom | Bronze Green Fairy statue (toilet-paper holder) | prop, quest-relevant (Jakub sleeps in her arms) | Painted. Only her two hands are cut-outs, for occlusion (gd:76-124). Jakub's sprite is placed on her (gd:142) | no: this room has no location files; man:60 and png:252 only | none (the scene runs on entry) | VIOLATION: quest-relevant, painted, undeclared | Full statue as a separate prop; create the restroom's location files |
| Restroom | Toilet-paper rolls in her hands | prop | Painted; the front pair sits inside the hands cut-out | no | none | OK | Nothing |
| Restroom | "ASK ME ABOUT TOKENS" pin | pickup | No world prop; given in the scene (gd:211) | no | none (`jakub_tokens_flair_pin`) | OK | Caveat: no data entry or icon |
| Restroom | Stalls with doors, toilets | prop | Painted | no | none | OK | Caveat: stall doors must split if ever made usable |
| Restroom | Urinals, vanity with sinks and soap, gilded mirror | prop | Painted; blockers gd:25-31 | no | none | OK | Caveat: sinks and the mirror are rule-listed props |
| Restroom | Mop bucket, wet-floor sign, bins, puddle | prop | Painted; blockers | no | none | OK | Nothing |
| Restroom | Shell: stained glass, sconces, pipes, ivy; exit at the screen edge | background | Painted | no | scene exit | OK | Nothing |

### Claw Machine Maintenance Closet Restroom (`gd/absinthe_arcade_maintenance_closet_hd2d.gd`, `game/core/closet_props.gd`; plate viewed: `interior/closet/aa_int_closet_night.png`, the room is night-only)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| Closet | DDR-arrow toilet | interactive | Painted. 8 arrow on/off cut-outs exist but are unwired | yes: cmr-interactions:5, 86 (`cmr_use_fixture` / `cmr_ddr_toilet`), cmr-sprite_mapping:43, cmr.md:40, 96 | `ddr_toilet` (gd:41) | VIOLATION | Wire the arrow cut-outs (code only); toilet as a prop if it ever needs to move |
| Closet | CRT mirror (INSERT COIN) | interactive | Painted. `crt_insert_coin` / `crt_glitch` cut-outs unwired | yes: cmr-interactions:21, cmr-sprite_mapping:49, cmr.md:42 | `crt_mirror` (gd:42) | VIOLATION | Wire the cut-outs; read-out states optional |
| Closet | Sock prize chute (paper-towel dispenser, lever) | interactive | Painted. `aa_closet_sock_chute` cut-out unwired | no: cmr.md:46, 98 only | `sock_chute` (gd:43) | VIOLATION | Wire the cut-out; add an interactions entry |
| Closet | Sparking wiring | interactive / FX | Not painted at the hotspot (free wall, gd:38-39); sparks not built | no: cmr.md:44, 99 only | `sparking_wiring` (gd:44) | MISSING | Wiring decal and spark FX (man:261); data entry |
| Closet | Graffiti "He moaned 'SMAAAASH'…" | interactive (read) | Painted decal baked into the left wall (round v37, gd:5-6) | yes: cmr-interactions:35 (one node for all graffiti), cmr.md:88 | `graffiti_smaaaash` (gd:45) | VIOLATION: a graffiti hotspot on the rule's baked-by-accident list; blacklight-only visibility (cmr.md:50) cannot show | Split as a decal layer |
| Closet | Graffiti pixel boobs (with the space invader) | interactive (read) | Painted, left wall | yes: cmr-interactions:35, cmr.md:91 | `graffiti_pixel_boobs` (gd:47) | VIOLATION | Split as a decal |
| Closet | Graffiti cheat codes (Konami, IDDQD, heart, crown) | interactive (read) | Painted, right wall | yes: cmr-interactions:35, cmr.md:91 | `graffiti_cheat_codes` (gd:49) | VIOLATION | Split as a decal |
| Closet | Tekken haiku | interactive (read) | Not painted; hotspot on free wall | yes: cmr.md:91 | `graffiti_tekken_haiku` (gd:48) | MISSING | New decal |
| Closet | Joystick-with-lips (visible only while Embarrassed) | interactive, status-gated | No art. The hotspot is gated in code (`closet_props.gd:88-91`) | yes: cmr.md:115 | `graffiti_joystick_lips` (gd:46) | MISSING | New decal that shows only while a bro is Embarrassed |
| Closet | Claw-arm chandelier | interactive per the data (examine, gives the Broken Prize Tag) | Painted; no hotspot in code | yes: cmr-interactions:52, 119, cmr-sprite_mapping:61, cmr.md:39, 165 (hanging animation) | none | VIOLATION: declared interactive and animated, but painted and unhooked | Separate animated prop and a hotspot |
| Closet | Broken Prize Tag | pickup | None | yes: cmr-items:6 | none | MISSING | Item, world prop and icon |
| Closet | Foot-soak mop bucket and cleaner bottles | prop (NPC station) | Painted; floor blocker gd:33 | yes: cmr.md:41, 100 (node `cmr_claw_bucket`) | none | OK | Nothing |
| Closet | Door to the north wing | interactive (exit door) | Painted; exit trigger (gd:98-102) | yes: cmr-interactions:68, cmr-sprite_mapping:127 | scene exit | VIOLATION (low) | Door layer |
| Closet | Sink | prop | Painted | yes: cmr.md:42 | none | OK | Nothing |
| Closet | Shell: pipes, neon tubes, ceiling marquee light, junction boxes, floor | background | Painted | no | none | OK | Nothing |

### The Absinthium Taproom (`gd/absinthe_arcade_taproom_hd2d.gd`; plate viewed: `interior/taproom/aa_int_taproom_day.png`)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| Taproom | Cracked-bottle bar (green tube) | prop / service counter | Painted; graybox wall `bar_front` (gd:124) | yes: at.md:81-87, at-sprite_mapping:67 (`at_service`) | none (`dr_vanek` marker in front of it) | OK | Caveat: the "constantly drips" animation (at.md:83) is not built |
| Taproom | Dr. Vaněk service point | NPC anchor | HallNpc placeholder sprite and marker (gd:21-28, 145-155) | yes: at-interactions:41-100, at-sprite_mapping:91 | `dr_vanek` | OK | Nothing |
| Taproom | Floating chalice (selfie spot) | interactive | Painted on the back wall | yes: at-interactions:104, 185 (`at_selfie`), at.md:242-245, 407 | none in code | VIOLATION: declared interactive and "floating", but painted | Separate animated chalice prop; inpaint; hotspot |
| Taproom | Stamp station | interactive (the rule's own example) | Not in the plate; stamping is a Vaněk menu option (`VanekTalk` MENU_STAMP) | yes: at.md:87 | none | OK | Caveat: the doc describes an object that does not exist; the function lives in dialogue |
| Taproom | Back-bar bottles / Absinthe Lager | prop / pickup (sold) | Painted; the Lager is sold through the menu | yes: items:193 | none | OK | Caveat: the bottle display is a rule-listed prop |
| Taproom | Portraits ("sometimes blink") | prop needing animation | Painted | yes: at.md:91 | none | OK | Caveat: blinking needs separate portraits |
| Taproom | Wall mirrors, small mirror on a stand | prop | Painted | no | none | OK | Nothing |
| Taproom | Tables, chairs, bar stools | prop | Painted; blockers gd:44-50 | no | none | OK | Caveat: stools in front of a counter (rule list) |
| Taproom | Shell: "Not for Introspection" plaque, candles, curtains, mist, floor | background | Painted | no | scene exit | OK | Nothing |

### Taproom mirror maze M1 and M5 (`gd/absinthe_arcade_taproom_maze_room.gd`, `_m1_hd2d.gd`, `_m5_hd2d.gd`; plates viewed: `interior/taproom_maze/aa_int_maze_m1_day.png`, `aa_int_maze_m5_day.png`)

| Room | Item | Bucket | How it exists | Location-file entry | Interaction id | Status | To comply |
|---|---|---|---|---|---|---|---|
| Maze M1 | Niche mirrors ×6 | interactive | Separate Sprite3D per niche, typed rest/revealed (maze_room.gd:110-152; m1 gd:22-29) | yes: at-interactions:5, 125 (`at_maze`), at.md:94-103 | `maze:<niche>` (maze_room.gd:61) | OK | Nothing |
| Maze M5 | Niche mirrors ×4 | interactive | As M1 (m5 gd:23-28) | yes: as M1 | `maze:<niche>` | OK | Nothing |
| Maze M1/M5 | Empty niche arches | background | Painted | yes: at.md:63-68 | none | OK | Nothing |
| Maze M5 | Open archway to the Taproom bar (True exit) | background (opening) | Painted; Area3D `exit_archway` (maze_room.gd:63-76) | yes: at.md:140-150 | `use_exit` trigger | OK | Nothing |
| Maze M1/M5 | Shell: candelabras, sconces, curtains, ivy, mist, floor, painted bar view | background | Painted | no | none | OK | Nothing |

**Totals:** 85 rows: 52 OK, 25 VIOLATION, 8 MISSING.

| Room | OK | VIOLATION | MISSING |
|---|---|---|---|
| Exterior | 5 | 3 | 0 |
| Hall | 15 | 7 | 4 |
| North wing | 4 | 5 | 0 |
| Mirror corridor | 6 | 0 | 0 |
| Public restroom | 6 | 1 | 0 |
| Closet | 3 | 8 | 4 |
| Taproom | 8 | 1 | 0 |
| Maze | 5 | 0 | 0 |
