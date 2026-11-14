# Absinthe Arcade interactables rework plan (Eurobound-bcnr)

Planning only. No repo file was changed, no image generated, no bead filed (this window had no shell, so `bd` could not run; child beads are specs in section 3 for the orchestrator to file).

Sources: `design/style_guides/location_interactables_rule.md`; `docs/superpowers/reports/2026-11-14-arcade-interactables-audit.md` (cited "audit"); the location files cited by the audit (ia, sm, ln, env, core, man, png, cmr-*, at-*, final.md). Paths below are relative to the repo root unless short.

Short paths:
- GA = `game/assets/worlds/debaucheryville/absinthe_arcade/` (engine assets)
- TR = `Assets/Graphics/worlds/debaucheryville/absinthearcade/tripo_raw/`
- XP = `Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_exterior/07_props/`
- REF = `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Interior/`
- gd = `game/worlds/debaucheryville/` scripts

Owners: ADT = Asset Development Team (art). AO = Absinthe Orchestrator (scenes, data, tests).

Scope: 33 items = 25 VIOLATION + 8 MISSING. Mirror corridor and the two maze rooms have no violations or missing rows, so they need no work (their audit caveats are not in the 33). Already filed and NOT duplicated: Eurobound-kzh9 (load the closet's 11 cut-outs, code only) and Eurobound-v2bb (data and id reconciliation: sprite mapping, id table, restroom location files, stale manifest). Existing art beads that overlap: Eurobound-koq3 (token price board), Eurobound-w2ig (DDR pips art).

Reuse check results (one Glob per area):
- TR holds only exterior kit GLBs plus `aa_prop_window_cat.glb` and `door_leaf_tripo_raw.glb`. There is NO interior GLB (no claw, skee-ball, foosball, DDR, bidet, door).
- XP (exterior prop plates) holds street cabinet, chalkboard, awning, bollard, lantern, shrub, bucket, TOKENS sign. Nothing covers any of the 33 items. There is no cat plate in XP and no cat in `XP/props.json`.
- Hall cut-outs on disk: `GA/interior/hall/props/` (3 cabinets, DDR pads/screen, token machine, bar counter, prize counter; JSONs `aa_hall_*.json`). None of the 33 is among them. (My filename glob only confirmed the `_day` files; night/emit for these were not checked.)
- Depth layers on disk: `GA/interior/depth_layers/aa_int_layer_claw_alcove_{day,night,emit}.png`, `aa_int_layer_entry_doors_*`, `aa_int_layer_north_arch_*`. The claw is painted inside the alcove layer, so it is a source of pixels, not a separate prop.
- Closet: `GA/interior/closet/props/` 11 cut-outs + emit masks (kzh9). Night plate only. Reference decal `REF/decals/aa_closet_decal_pixel_graffiti.png` shows the pixel-boobs graffiti (pink pixel art, flat).
- No Sea-Monkeys art exists anywhere under `Assets/` or `game/assets/`.

Standing method for every "cut out + inpaint" action: cut the existing pixels to a separate sprite per state, inpaint the plate behind it, for day, night and emit, registered to the same footprint. One inpaint pass per room (all of that room's cut-outs batched). Use the PlatePropLayer format (`gd/plate_prop_layer.gd`: `<prefix>_<state>_<day|night|emit>.png` + a JSON of x, y, w, h).

---

## 1. Tables per room

Columns: # | item | bucket | action | REUSE | NEW REF ART? | states (from docs) | interaction id (code / location-file) | owner.

### 1a. Exterior (plate `exterior/faces/aa_face_front_day.png`; gd `absinthe_arcade_exterior_hd2d.gd`)

| # | Item | Bucket | Action | REUSE | New ref art? | States | Id (code / data) | Owner |
|---|---|---|---|---|---|---|---|---|
| E1 | Free Wi-Fi hotspot (in street cabinet) | interactive | Data only: declare in ia/sm and the `wifihotspots.md` lists (two copies: `design/World Design/Interactables/wifihotspots.md`, `design/worlds/shared/interactables/wifihotspots.md`). Scene already code-drawn (gd:859-878). | `wifi_hotspot.tscn` exists | No | none given | `debaucheryville_absinthe_arcade_facade` / none yet | AO |
| E2 | Window cat (left first-floor sill) | interactive (examine) + idle loop | Cut out of front face day/night/emit; inpaint sill and window; place card on sill. Cat must stay (canon). | `TR/aa_prop_window_cat.glb` exists (candidate pose source, not yet in `props.json` or any script); engine text `game/assets/data/locations/debaucheryville/absinthe_arcade_hall_lines.json:29` | No (the plate cat is approved; the GLB is optional for the idle loop, author to say) | idle loop (png:144); no named states | `window_cat` / sm:378 `aa_prop_window_cat` | ADT art, AO placement |
| E3 | Front stained-glass doors + entrance glimpse | interactive (door) | Cut door leaves and the entrance glimpse as a layer (png:127 `aa_layer_entrance_interior`, never built); inpaint behind; keep `exit_front_door` trigger. | `TR/door_leaf_tripo_raw.glb` exists (unverified match to the painted stained glass; do not assume); interior counterpart layer `aa_int_layer_entry_doors_*` exists | No (derivative of plate) | none given (low priority per audit; open/close optional) | scene exit `exit_front_door` / core:48-53, ln:64 | ADT art, AO wiring |

### 1b. Hall (plate `GA/interior/hall/aa_int_hall_{day,night,emit}.png`; gd `absinthe_arcade_interior_hd2d.gd`)

| # | Item | Bucket | Action | REUSE | New ref art? | States | Id (code / data) | Owner |
|---|---|---|---|---|---|---|---|---|
| H1 | Rigged absinthe claw (PRIZES alcove) | interactive (quest) | Cut out of the alcove layer as a prop; inpaint layer and plate; PAYOUT light stays a code light (gd:317-324). | Source pixels: `aa_int_layer_claw_alcove_*` (static layer, gd:220-221) | Derived states (play, near_miss, win, shake_warning) are new paint of approved art: author sees them at the room review, no separate ref | sm:281-292: sea_monkeys_present, play, near_miss, win, sea_monkeys_absent, shake_warning; ia:463 post_win_state sea_monkeys_gone_and_joke_prizes | `rigged_absinthe_claw_machine` (gd:96) / same (ia:463); sm file `aa_cab_claw_rigged` | ADT, AO wiring |
| H2 | Sea-Monkeys inside the claw | pickup (NFT) | New asset: prize sprite in the claw glass, present/absent, plus inventory icon. Blocks the merged claw Sea-Monkeys win from ever showing visibly. | None. No Sea-Monkeys art anywhere. | YES. Nothing approved shows it. | present / absent (env:262 `empty_sea_monkeys_spot`) | `ArcadeClaw.TOP_PRIZE_ID` + `item_sea_monkeys` / items:89, ln:150; icon in `aa_ui_item_icons` (man:271) | ADT, AO state hook |
| H3 | Beanie Baby claw (west wall) | interactive | Cut out + inpaint; light/state overlay. | None | No | ia:402-408: idle, insert_token, playing, grab_miss, grab_win | `beanie_baby_claw` (gd:94) / `beanie_baby_claw` (ia:306), asset id `aa_cab_claw_beanie` | ADT, AO |
| H4 | Skee-ball lanes x3 | interactive | Cut out + inpaint; floor blocker gd:184 already exists. | None | No | ia:260-265: idle, insert_token, playing, results | `skee_ball` (gd:89) / `skeeball_lanes` (ia:230), asset `aa_prop_skeeball_lane` | ADT, AO |
| H5 | Foosball table | interactive | Cut out + inpaint; blocker gd:183. | None | No | ia:297-303: idle, insert_token, playing, results_win, results_loss | `foosball` (gd:90) / `foosball_table` (ia:269), asset `aa_prop_foosball_table` | ADT, AO |
| H6 | Bidet bar stool | interactive (examine + chime) | Cut out as `aa_prop_bidet_stool`; inpaint bar front and floor. The bar cut-out JSON already carves the stool out of the bar sprite on purpose (`aa_hall_bar_counter.json`). | Source pixels in plate; man:227 marks `aa_prop_bidet_stool` SUPERSEDED (needs un-superseding via v2bb) | YES, pending author ruling (Q1): plate shows a plain toilet, canon is "porcelain bidet bolted to a brass bar-stool base" (ia:615-616) | none (single examine; chime effect) | `bidet_stool` (gd:107) / `bidet_bar_stool` (ia:610) | ADT, AO |
| H7 | Restroom door (left-wall arch) | interactive (door, `press_door`) | Door asset over the arch; core exit + ia entry (data part also in v2bb scope for the restroom's location files; coordinate). | Arch painted behind TOKENS HERE; no door leaf shown anywhere | YES, pending Q5: nothing approved shows a door leaf | none given (open/closed implied) | `restroom_door` (gd:100) / none (undeclared) | ADT, AO |
| H8 | Fake VIP arrows (3, loop back to bar) | interactive | New 3-arrow asset, then place the hotspot on it (gd:104-106 comment assumes painted arrows; they are not). | None | YES. Not in plate. Placement conflict, Q2. | none (static loop); after Taproom discovery "bar arrow flickers toward north wing" (ia:641) | `vip_arrows` (gd:106) / `fake_vip_wayfinding` (ia:619); sm:356 `aa_prop_wayfinding` | ADT, AO |
| H9 | Token price board "1 SOV = 1 TOKEN" | prop | New asset. Owned by existing bead Eurobound-koq3; this plan only integrates and places it. | none | YES (koq3 owns the ref); text is 1 SOV = 1 TOKEN (man:110; png:214 "1 KC = 5 TOKENS" retired) | none | none / ln:92 | ADT (koq3), AO |
| H10 | Scratched service note (claw clue) | interactive (clue) | Hold: do not build until Q3 answered. | None | YES if kept; Q3 doc conflict | none | none / ln:152, env:61-63 | ADT/AO after Q3 |
| H11 | Backpack Girl floor nest / couchsurf hook | interactive (couchsurf trigger) | New nest prop + trigger. Her sprite (man:253) and NPC placement are separate and not part of the 33. | None | YES. Doc text only (env:235-236: notebook pages, charger cables, kebab wrapper, backpack wear) | none; NPC schedule 14:00-22:00 floor spot (ia:595) | none / `backpack_girl_couchsurf_hook` (ia:589), env:235 `cabinet_resident_nest` | ADT, AO |

### 1c. North wing (plate `GA/interior/north_wing/aa_int_north_wing_{day,night,emit}.png`; gd `absinthe_arcade_north_wing_hd2d.gd`)

| # | Item | Bucket | Action | REUSE | New ref art? | States | Id (code / data) | Owner |
|---|---|---|---|---|---|---|---|---|
| N1 | Broken DDR (cracked pad + cabinet) | interactive | Cut out + inpaint. Pips stay a code stand-in until Eurobound-w2ig. | None (hall DDR cut-outs are a different machine) | No | sm:299-306: error, token_0..3_of_3, unlock_pulse; return visit: pips three_lit (ia:636) | `broken_ddr` (gd:36) / `broken_ddr_restroom_unlock` (ia:495) | ADT, AO |
| N2 | Maintenance door + sign + lamps | interactive (stateful door) | Cut out the door; repaint the lamp region as separate lamp states (plate paints red and green lit at once); unlock light stays code (gd:146-152). | None | Lamp-off/red/green are derived from the approved lamps; author sees them at room review | sm:333-341: locked_red, unlocked_green, opening_exterior_only; return visit green | `maintenance_door` (gd:37) / `maintenance_restroom_door` (ia:519) | ADT, AO |
| N3 | Taproom curtain + brass plaque | interactive | Cut out curtain; glow as its own layer; inpaint. | None | Day/evening/night/discovered variants derived from the approved glow | sm:324-329: day_inert, evening_faint, night_breathing, discovered; active 20:00-04:00 (ia:539); after discovery "subtle after 20:00" | `taproom_curtain` (gd:40) / `absinthium_taproom_curtain` (ia:532) | ADT, AO |
| N4 | Cracked Time Crisis cabinet (gun) | prop with states | Cut out + inpaint. Bound to the curtain. | None | Derived hidden/displaced states: author sees at review | sm:309-317: curtain_hidden, displaced_revealed, night_glow | none (floor blocker gd:61) / sm `aa_cab_time_crisis_cracked`; add an id | ADT, AO |
| N5 | Green vapour at curtain base | FX anchor | Paint the baked vapour out of the plate (part of the N3 inpaint); vapour FX layer shown 20:00-04:00 only. | None (code mist gd:74 exists) | No | active 20:00-04:00 (env:173-178) | none / `aa_transition_taproom_vapor` | ADT, AO |

### 1d. Mirror corridor and Taproom maze rooms M1/M5

No VIOLATION or MISSING rows (audit: 6 and 5 OK). No work in this plan. Caveats stay with the audit.

### 1e. Public restroom (plate `GA/interior/restroom/aa_int_restroom_{day,night,emit}.png`; gd `absinthe_arcade_restroom_hd2d.gd`)

| # | Item | Bucket | Action | REUSE | New ref art? | States | Id (code / data) | Owner |
|---|---|---|---|---|---|---|---|---|
| R1 | Bronze Green Fairy statue (toilet-paper holder; Jakub sleeps in her arms) | prop, quest-relevant | Cut the full statue out; inpaint behind; keep Jakub placement (gd:142). Create the restroom's location files (that file creation is in v2bb). | Hand cut-outs exist: `GA/interior/restroom/props/aa_int_restroom_statue_hand_{left,right}_day.png` + `statue_hands.json` (and REF copies in `REF/props/restroom_statue_hands/`); extend or replace them with the full statue | No (plate is approved) | none given (Jakub asleep/awake is NPC-side) | none (scene runs on entry) / none; assign an id | ADT, AO |

### 1f. Taproom (plate `GA/interior/taproom/aa_int_taproom_{day,night,emit}.png`; gd `absinthe_arcade_taproom_hd2d.gd`)

| # | Item | Bucket | Action | REUSE | New ref art? | States | Id (code / data) | Owner |
|---|---|---|---|---|---|---|---|---|
| T1 | Floating absinthe chalice (selfie spot) | interactive | Cut out + inpaint back wall; animated float; hotspot in code. | None (spec at.md:407 `floating_chalice.png` 48x64, not on disk) | No | floating idle; selfie variants are photos, not prop states (at.md:242-245, 331) | none in code / `at_selfie` (at-interactions:104, 185) | ADT, AO |

### 1g. Claw Machine Maintenance Closet Restroom (night plate `GA/interior/closet/aa_int_closet_night.png`; gd `absinthe_arcade_maintenance_closet_hd2d.gd`, `game/core/closet_props.gd`)

| # | Item | Bucket | Action | REUSE | New ref art? | States | Id (code / data) | Owner |
|---|---|---|---|---|---|---|---|---|
| C1 | DDR-arrow toilet | interactive | Code only (kzh9 wires the 8 arrow cut-outs). Toilet body stays painted unless it must move. | `closet/props/aa_closet_ddr_arrow_{up,down,left,right}_{on,off}.png` + `_on_emit` | No | arrows on/off; cmr states available, unavailable, completed (cmr-interactions:89-93) | `ddr_toilet` (gd:41) / `cmr_ddr_toilet` node, `cmr_use_fixture` event (reconcile in v2bb) | AO |
| C2 | CRT mirror (INSERT COIN) | interactive | Code only (kzh9). | `aa_closet_crt_insert_coin.png`, `aa_closet_crt_glitch.png` + emit | No | insert_coin, glitch; read-outs cycle (closet_props.gd:45-49) | `crt_mirror` (gd:42) / `cmr_crt_mirror`, `cmr_scan_mirror` | AO |
| C3 | Sock prize chute | interactive | Code only (kzh9) + add interactions entry (data; v2bb id table, confirm it includes this one). | `aa_closet_sock_chute.png` (also covers the painted sock) | No | idle, dispense (sock) | `sock_chute` (gd:43) / none (cmr.md:46, 98 only) | AO |
| C4 | Sparking wiring | interactive / FX | New wiring decal + spark FX; data entry. | None | YES. Not painted at the hotspot; sparks not built. Q4b: is "hazard mini-game" (cmr.md:99) in scope? | spark intervals 2-5 s (cmr.md:173); "when player passes too close" (cmr.md:44) | `sparking_wiring` (gd:44) / none (cmr.md:44, 99 only) | ADT, AO |
| C5 | Graffiti "He moaned SMAAAASH..." | interactive (read) | Split as a decal layer from the left wall; inpaint wall. | Plate pixels | No (plate is approved); visibility rule is Q4 | blacklight-only per cmr.md:45, 127 (Q4) | `graffiti_smaaaash` (gd:45) / `cmr_graffiti_wall`, `cmr_read_graffiti` (one node for all) | ADT, AO |
| C6 | Graffiti pixel boobs (+ space invader) | interactive (read) | Split as decal; inpaint. | `REF/decals/aa_closet_decal_pixel_graffiti.png` (pink pixel boobs, flat; verify it equals the plate version before use) | No | as C5 | `graffiti_pixel_boobs` (gd:47) / same node | ADT, AO |
| C7 | Graffiti cheat codes (Konami, IDDQD, heart, crown) | interactive (read) | Split as decal (right wall); inpaint. | Plate pixels | No | as C5 | `graffiti_cheat_codes` (gd:49) / same node | ADT, AO |
| C8 | Tekken haiku | interactive (read) | New decal (text is final: closet_props.gd:60-65). | None | YES. Not painted. | as C5 | `graffiti_tekken_haiku` (gd:48) / cmr.md:91 | ADT, AO |
| C9 | Joystick-with-lips | interactive, status-gated | New decal; glows only while a bro is Embarrassed (code gate `closet_props.gd:88-91`). | None | YES. No art. | hidden / glowing (Embarrassed) | `graffiti_joystick_lips` (gd:46) / cmr.md:115 | ADT, AO |
| C10 | Claw-arm chandelier | interactive (examine; gives Broken Prize Tag) | Cut out; animated hanging prop; add hotspot (none in code). Inpaint ceiling. | Plate pixels | No for the prop (plate approved); hanging animation is derived | hanging idle (cmr.md:165) | none / node `cmr_claw_bucket`, event `cmr_examine_claw` (cmr-interactions:52, 119). Note: the same node name is used for the foot-soak mop bucket (cmr.md:100); give the chandelier its own id (v2bb) | ADT, AO |
| C11 | Broken Prize Tag | pickup | New: item entry check, world prop, inventory icon. | `cmr-items:6` item entry; sm names `claw_machine_maintenance_closet_restroom_cmr_broken_prize_tag.png` (not on disk) | YES. No art. | in world / collected | none / cmr-items:6 | ADT, AO |
| C12 | Door to the north wing | interactive (exit) | Cut a door layer; keep exit trigger (gd:98-102). Low priority. | none | No | none given | scene exit / cmr_exit, `cmr_return` (cmr-interactions:68) | ADT, AO |

Audit tally check: E 3, H 11, N 5, R 1, T 1, C 12 = 33.

---

## 2. Recommended order

Principles: rooms where the player already interacts with painted pixels come first; anything blocking a merged feature comes before polish; each room's plate is repainted ONCE (all cut-outs in one inpaint pass), with day, night, emit kept registered.

0. Code-only and data-only first (no art, unblocks everything): kzh9 (closet cut-outs), v2bb (ids, sprite mapping, restroom files), E1 (Wi-Fi declaration). Reason: removes id ambiguity before children bind interaction ids.
1. Hall. The player already presses hotspots on painted pixels here (claw, beanie, skee-ball, foosball, bidet, restroom door), and the merged Sea-Monkeys win cannot show the prize leaving (H1+H2). Largest room, so it goes first and is split in two passes: (a) H1-H5 cut-outs and inpaint, (b) new assets H6-H9, H11 after the author's reference approvals. Reason for one inpaint pass: H1-H7 all touch the same plate; the claw alcove layer and the bar front overlap.
2. North wing. Painted DDR/door/curtain/Time Crisis are live hotspots with stateful docs (lamps red+green at once, vapour at all hours). One inpaint pass for N1-N5. Depends on the Hall only for the shared cut-out workflow, not for pixels.
3. Closet. Mostly decals and new assets; the plate is night-only so only one plate set. Depends on kzh9 and the blacklight decision (Q4). The Broken Prize Tag is a pickup and should land with C10.
4. Exterior. Cat and doors are examine-only/low-state; one front-face pass. The cat is canon, so risk is high even though player impact is small: do it carefully, after the interior method is proven.
5. Restroom (statue) and Taproom (chalice): one item each, one inpaint pass each, lowest player impact. Restroom depends on v2bb creating its location files.
6. Held until the author answers: H10 service note, plus any asset whose reference art is unapproved.

---

## 3. Child-bead specs (one per room)

All carry: found_by Eurobound-bcnr; `--deps discovered-from:Eurobound-bcnr`; labels agent:/effort:. Anything marked "needs reference art" must wait on the Desk answer (label `author-ruling` on the dependency bead, not on the build bead). Every bead description for a cold reader is below; the orchestrator files them.

### 3.1 Hall: separate the interactables from the plate (H1-H8, H11; H9 via koq3)
- Title: Arcade hall: split claw, Sea-Monkeys, Beanie claw, skee-ball, foosball, bidet, restroom door out of the plate; add VIP arrows and Backpack Girl nest
- Description: `docs/superpowers/reports/2026-11-14-arcade-interactables-audit.md` Hall table lists 7 painted-in violations and 4 missing items. Cut each existing item to its own sprite per state (day/night/emit) in the PlatePropLayer format (`game/worlds/debaucheryville/plate_prop_layer.gd`, JSON like `GA/interior/hall/props/aa_hall_cabinets.json`), batched into ONE inpaint of `GA/interior/hall/aa_int_hall_*.png` plus the alcove layer `GA/interior/depth_layers/aa_int_layer_claw_alcove_*`. Register each prop in `PROPS` at `game/worlds/debaucheryville/absinthe_arcade_interior_hd2d.gd:230-239` and bind to the existing `INTERACT_POINTS` ids (gd:79-108). Items: claw (states sm:281-292), Sea-Monkeys prize sprite + icon (present/absent after `ArcadeClaw.TOP_PRIZE_ID` win), Beanie claw (ia:402-408), skee-ball (ia:260-265), foosball (ia:297-303), bidet stool, restroom door, VIP arrows, nest. Move the VIP hotspot onto the arrows (gd:104-106).
- Acceptance: each of the 11 items loads as a separate node with its own id; hall plate has no pixels of them (visual diff in day, night, emit, registered); claw shows the Sea-Monkeys before the win and not after; each state in the docs renders; existing hall tests green; no hotspot points at empty floor; the price board is placed via koq3.
- Owner: ADT (art) + AO (scenes, tests). Agent types: art agent for cut/inpaint, then gd/GUT agent. Effort: high.
- Dependencies: v2bb (ids), Desk answers Q1, Q2, Q3, Q5, Q6 (new reference art), koq3 (price board). Split into two pieces if needed: 3.1a H1-H5 cut/inpaint (no ref art needed, start now), 3.1b new assets (after approvals).

### 3.2 North wing: separate broken DDR, maintenance door, curtain, Time Crisis; remove baked vapour
- Title: Arcade north wing: split N1-N5 out of the plate and give them their documented states
- Description: Audit North wing table, 5 violations. Cut each to a sprite per state (sm:295-341), inpaint `GA/interior/north_wing/aa_int_north_wing_*.png` once, repaint the maintenance door lamps as separate lamp states (plate shows red and green at once), move the vapour into an FX layer shown 20:00-04:00 only (env:173-178). Wire ids `broken_ddr`, `maintenance_door`, `taproom_curtain` (gd:36-40) and add an id for the Time Crisis cabinet. Pips remain a stand-in until Eurobound-w2ig.
- Acceptance: five separate nodes; plate shows no baked vapour or lit lamps; door shows locked_red / unlocked_green from the flag `arcade_maintenance_restroom_unlocked`; curtain shows day/evening/night/discovered by time (active 20:00-04:00); Time Crisis shows hidden/displaced/night_glow; day, night, emit registered; tests green.
- Owner: ADT + AO. Agent types: art agent, then gd/GUT agent. Effort: high.
- Dependencies: v2bb.

### 3.3 Closet: decals, new props, chandelier, pickup, door
- Title: Arcade closet: graffiti decals, sparking wiring, claw-arm chandelier, Broken Prize Tag, door layer
- Description: Audit Closet table (8 violations, 4 missing; C1-C3 are covered by kzh9 and v2bb). Split graffiti C5-C7 from the night plate `GA/interior/closet/aa_int_closet_night.png` (reuse `REF/decals/aa_closet_decal_pixel_graffiti.png` for C6 after checking it matches), make new decals C8, C9 (`closet_props.gd:18, 88-91` gate), wiring decal + spark FX C4, animated chandelier + hotspot C10, Broken Prize Tag item/prop/icon C11, door layer C12. One inpaint pass. Prop JSON follows `GA/interior/closet/props/aa_closet_props.json`.
- Acceptance: every graffiti id in `closet_props.gd:10-21` has its own decal node; joystick appears only with Embarrassed; chandelier has a hotspot and animation and grants the tag once; tag has icon and location-file entry; plate has none of these painted; tests green.
- Owner: ADT + AO. Agent types: art agent, then gd/GUT agent. Effort: high.
- Dependencies: kzh9, v2bb, Desk answers Q4 (blacklight rule, wiring mini-game), Q6 (haiku, joystick, tag, wiring reference art).

### 3.4 Exterior: window cat and front doors
- Title: Arcade exterior: cut the window cat and the front door leaves out of the front face
- Description: Audit Exterior table. Cut the cat (canon, must stay) and the door leaves + entrance glimpse out of `aa_face_front` day/night/emit, inpaint sill, window and entrance; place the cat card at `window_cat` (gd:886); optional idle loop (png:144); `TR/aa_prop_window_cat.glb` is a candidate source. E1 (Wi-Fi) declaration is done under v2bb or as a one-line data edit.
- Acceptance: cat is a separate card on the sill in all three variants, with the plate sill clean behind it; the cat is never removed from the game; doors separate with `exit_front_door` unchanged; the examine text (`absinthe_arcade_hall_lines.json:29`) still plays; tests green.
- Owner: ADT + AO. Agent types: art agent, gd agent. Effort: medium.
- Dependencies: v2bb (sm filename fix).

### 3.5 Public restroom: full Green Fairy statue prop
- Title: Arcade restroom: cut the full bronze Green Fairy statue out of the plate
- Description: Audit Restroom table. Only the two hands are cut-outs now (`GA/interior/restroom/props/statue_hands.json`). Cut the whole statue, inpaint `GA/interior/restroom/aa_int_restroom_*.png`, keep Jakub placed on it (`absinthe_arcade_restroom_hd2d.gd:142`) and the hand occlusion working. Give it an interaction/prop id declared in the restroom's new location files.
- Acceptance: statue is one separate node with hands layered correctly; plate has no statue; Jakub still reads as asleep in her arms; id declared in the location file; tests green.
- Owner: ADT + AO. Agent types: art agent, gd agent. Effort: medium.
- Dependencies: v2bb (restroom location files).

### 3.6 Taproom: floating chalice
- Title: Absinthium Taproom: cut out and animate the floating chalice selfie spot
- Description: Audit Taproom table. The chalice is painted on the back wall of `GA/interior/taproom/aa_int_taproom_*.png`. Cut it out, inpaint the wall, animate a float, add a hotspot bound to `at_selfie` (at-interactions:104, 185; spec at.md:242-245, 407).
- Acceptance: chalice is its own animated node; wall clean; hotspot triggers the selfie flow with the id `at_selfie`; tests green.
- Owner: ADT + AO. Agent types: art agent, gd agent. Effort: low.
- Dependencies: v2bb.

---

## 4. Open for the author (tap options; nothing invented)

Q1. Bidet stool: plate shows a plain toilet; canon is a porcelain bidet bolted to a brass bar-stool base (ia:615-616; man:26 "bidet/toilet stool").
- A: Keep the plate's toilet as approved; change the doc text to match it.
- B: Make new reference art of the canon bidet on a brass stool; repaint the prop to it.
- C: Cut out the plate toilet now; swap to the canon bidet later.

Q2. Fake VIP arrows: where do they hang? Env says mezzanine stair landing (env:240-242); the interaction is on the bar node (`aa_node_bottle_bar`) and the code hotspot is on open floor in front of the bar (gd:106). Either way they need new reference art.
- A: At the bar front.
- B: On the mezzanine stair landing.
- C: Both a bar-front arrow and a landing arrow.

Q3. Scratched service note (claw clue): ln:152 and env:61-63 still list it, but the claw's "service-note" method was dropped in round v27 (ia:473).
- A: Drop the note from the location files.
- B: Keep it as a plain examinable clue; it needs new reference art.
- C: Replace it with the Token Attendant's hint only.

Q4. Closet graffiti visibility: docs say blacklight-only (cmr.md:45, 92, 127) and the examine line says "under the blacklight" (`closet_props.gd:31`), but no blacklight exists in the room.
- A: Always-visible decals (examine line unchanged).
- B: Build a blacklight state (needs a mechanic ruling) and show decals only under it.
- C: Decals visible always, with the glow/fluorescent look only under the room's green light.
Q4b. Sparking wiring: cmr.md:99 says "hazard mini-game".
- A: Spark FX and examine only.
- B: Also the hazard mini-game (needs a mechanic ruling).

Q5. Restroom door: only an open arch is painted, hidden behind TOKENS HERE; nothing shows a door leaf.
- A: The arch itself is the door; no leaf, just a labelled hotspot.
- B: New reference art for a door leaf (with a sign).
- C: Keep it hidden behind the token machine and add a separate door sign.

Q6. New reference art that must be approved before building (nothing approved shows them): Sea-Monkeys prize (H2), VIP arrows (H8), Backpack Girl nest (H11), Tekken haiku decal (C8), joystick-with-lips (C9), sparking wiring (C4), Broken Prize Tag (C11), restroom door leaf (H7, Q5), canon bidet (Q1), service note (Q3). Token price board is already in koq3.
- A: Generate all references now on Firefly and post them on the Desk in one batch.
- B: One room at a time (Hall first), on the Desk.
- C: The author supplies the references.

Q7. Window cat: the GLB `TR/aa_prop_window_cat.glb` exists. Should the cat be a flat card cut from the plate or the 3D model?
- A: Flat card cut from the approved plate (default).
- B: Use the 3D model for the idle loop.

Note, not a question: node id `cmr_claw_bucket` names both the mop bucket and the claw chandelier examine (cmr.md:100; cmr-interactions:52, 119). v2bb should split the ids; no author decision needed unless a new object name is wanted.

---

## 5. Desk card summary (150 words)

The author ruled the Arcade plates get reworked. The audit found 33 things the player can use that are painted into the background or missing: 25 painted in, 8 missing. Mirror corridor and maze rooms are fine. Plan: for each item, cut the existing pixels out as a separate sprite, repaint the wall behind it once per room, keep day, night and emit lined up, and give each its game id. The proposed order is Hall first (claws, skee-ball, foosball, bidet, restroom door, and the Sea-Monkeys that can never visibly leave the claw), then North Wing, Closet, Exterior (the cat stays), Restroom statue and Taproom chalice. Code-only closet wiring and data fixes are already filed. Seven questions need you, mainly: approve new reference art for ten things nothing shows yet, the bidet versus plain toilet, where the VIP arrows hang, the dropped service note, and graffiti blacklight.
