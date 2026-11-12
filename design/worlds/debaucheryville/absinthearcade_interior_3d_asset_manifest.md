# Absinthe Arcade Interior — 3D Asset Manifest

> **Status: asset list APPROVED by the author 2026-11-09.** Items still marked **PROPOSED** are agent proposals, not rulings.
>
> **Build method ruled 2026-11-09: projection.** The approved paintings are projected onto graybox geometry from a fixed camera per room (built by session eurobound-46: commits 702ba33, 80b49fa). Room faces are not repainted orthographically, so section A below is superseded by the projected plates. **No people are painted into room art**; every person is a movable NPC sprite. Hall source plates: `references/Interior/concepts/aa_interior_hall_v8_clean_{night,day}.png` (v8 with the four painted patrons removed). Bros are sized to the furniture (counter at waist height). North wing v4 approved. The mirror corridor is its own screen; the hall exit toward it is open with the author (A/B/C on the decisions page). The DDR dance-off is a playable rhythm mini-game (the player picks one bro, the other two are AI), so `aa_prop_ddr_danceoff_pads` + screen move from set dressing to an interactive asset. Battle cabinets: two in the back row, one on the right wall.

**Purpose:** production manifest for the Arcade interior kit. Built from `design/templates/3D_Asset_Manifest_Template.md`. That template and `design/style_guides/3d_asset_rules.md` still describe the retired Unity/Tripo kit. This manifest follows the Godot 4.7 painted-box method the exterior uses (`Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_exterior/hd2d_asset_manifest.md`), and keeps the template's section order.

- **Location docs:** `design/worlds/debaucheryville/` Arcade package (`core/`, `location_nodes/absinthe_arcade_location_nodes.json`, `sprite_mapping/`, `PNG_Assets/Absinthe_Arcade_Complete_PNG_Asset_Requirements.md`)
- **References (canon):** `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Interior/`
  - Main hall: `concepts/aa_interior_hall_v8_wall_rows_open_floor.png` (night, **approved 2026-11-09**) and `concepts/aa_interior_hall_v8_day.png` (day state)
  - North wing: `concepts/aa_interior_north_wing_v4_gpt25_wall_rows.png` (approval pending)
  - Content canon: `concepts/aa_interior_hero_v3_chatgpt_author_revision.png`, `Neon Absinthe Arcade Bar.png`
- **Superseded:** `design/worlds/debaucheryville/absinthearcade_3d_asset_manifest.md` (Unity, 14x12 m)
- **Delivery folder:** `Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_interior/` (mirrors `absinthearcade_exterior/`)
- **Godot scene:** `game/worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn` (to build)

## Decisions this kit is built on (author)

| Decision | Ruling |
|---|---|
| Style and camera | Bravely Default interior, same fixed HD-2D tilt camera as the exterior (2026-11-02) |
| Dimensions | 15.4 x 18 m footprint: main hall about 15 x 12 m, north L-wing about 8 x 6 m (2026-11-02) |
| Mezzanine | Visual only, never walkable (2026-11-02) |
| Main hall layout | Hall v8 approved (2026-11-09). Cabinets stand in straight wall rows, the centre floor stays open, and nothing blocks another machine (v7 rule, 2026-11-08) |
| Hall contents | Three-pad DDR dance-off facing one big wall screen; token/prize redemption counter built into the bar; Green Fairy mural inside; Skee-Ball, foosball, Beanie Baby claw, Bubble Bobble; one bidet/toilet stool (2026-11-08) |
| Cabinets | Frogger: Existential Edition, Street Fighter: Identity Crisis and Kebab Kombat are battle encounters. Real game names stay as drawn (2026-11-08). **Mini-games (round v25, 2026-11-11):** the rigged claw, the DDR dance-off, **Skee-Ball and foosball are real mini-games**, and **the claw machine must exist and work** |
| Economy on signage | 1 SOV = 1 token. Broken-DDR restroom unlock 3 tokens. Claw 5 tokens per attempt. DDR dance-off 2 tokens a song (0-30 tickets). Skee-Ball 2 tokens a game, 9 balls (0-20 tickets by score). Foosball 2 tokens a game vs an NPC (15 tickets win / 3 loss). Ticket-game numbers set by Claude under the author's round v25 delegation; see `design/worlds/debaucheryville/interactions/absinthe_arcade_interactions.json` |
| NPC placement | Backpack Girl sits on the primary route beside the token machine (v8 position) |

## Conventions

- **Units and axes:** metres, Y-up, real-world scale (author 2026-11-02). Characters are 1.8 m.
- **Build:** painted-box diorama, as on the exterior. Room shell = floor, three walls and ceiling as simple boxes wearing painted, orthographic textures. Cabinets, bar, furniture and NPCs are alpha cutout `Sprite3D` billboards or painted cards on low boxes.
- **Texture density (PROPOSED):** 133 px/m for room faces, twice the exterior's 66.5 px/m. The interior back wall fills the whole screen, so 66.5 px/m would leave a 15 m wall only 998 px wide on a 1920 px screen. Props stay at 400 px/m like the exterior props.
- **Filtering:** linear + mipmaps, sRGB albedo (painterly, not pixel art).
- **Day/night:** every lit face and prop ships `_day`, `_night` and `_emit` (neon, screens, bar glass, lamps), pixel-registered so they cross-fade, using the exterior's `register_to.py` / `night_glow.py` / `finalize_*` scripts. Night is the master here (v8 was painted at night); day comes from the Firefly Relight + `tools/art_cleanup/day_grade.py` method used for `aa_interior_hall_v8_day.png`.
- **Relief:** `_height` + `_normal` per wall face, as on the exterior (`hd2d_relief_face.gdshader`).
- **Naming:** `aa_int_<category>_<name>` for shell and layers; `aa_cab_*` cabinets; `aa_prop_*` props; `aa_transition_*` hidden-entrance sets; `aa_fx_*`, `aa_ui_*`, `aa_mask_*` as in the PNG spec.
- **Pivots:** props and cabinets bottom-centre; wall faces bottom-left at floor level.

## Structural layout (PROPOSED dimensions)

```
            north wing (8 x 6 m, darker, lower vault, no mezzanine)
            [Taproom curtain W]  cabinet rows  [broken DDR + MAINTENANCE door E]
                         |  north arch  |
 +---------------------------------------------------------------+
 | mezzanine (visual) -- back wall: Green Fairy mural, 5-cabinet row |
 | DDR screen + 3 pads   Skee-Ball  foosball   shattered-glass   |
 | Beanie claw (W wall, by foosball)            bar + PRIZE      | (E wall: Bubble Bobble, KK)
 | TOKENS HERE + Backpack Girl     open floor   REDEMPTION       | PRIZES claw alcove
 |                  stained-glass entry doors (south)            |
 +---------------------------------------------------------------+   main hall 15 x 12 m
```

- Hall height to vault crown about 9 m, mezzanine deck about 4.5 m (PROPOSED: ground + first floor of the 4-storey exterior).
- North-wing vault about 5 m (PROPOSED: "lower" per the spec and v4).
- **Mirror corridor** (`aa_node_mirror_corridor`): placed and built (hall north arch -> corridor -> north wing; art v1 approved round v25).
- Not yet placed: **the Arcade bathroom with the toilet-paper statue** (author, round v25: the bros find the Token Attendant asleep in the arms of a statue repurposed as a toilet-paper holder). **RESOLVED (author, round v26, 2026-11-11): public restroom screen approved, to be painted (night/day, same camera conventions).** It is a new screen, not yet in the hall art; the statue is a bronze Green Fairy repurposed as a toilet-paper holder, and the scene triggers on the first bathroom visit after 01:00 (see `design/worlds/debaucheryville/npcs/Absinthe_Arcade/jakub_tokens_dvorak.md`). Painted (aa_interior_restroom_v1_night/day, approved round v27). The hall exit to it is not yet placed (round v28 question restroom_door).

## Asset list

Status: ☐ todo · ◐ generated, needs QA · ☑ approved

### A. Room shell faces (box textures; day / night / emit / height)
| id | content | size (PROPOSED) |
|---|---|---|
| `aa_int_face_back_wall` | Green Fairy mural, stained-glass arches, mezzanine back edge | 15 x 9 m → 1995x1197 |
| `aa_int_face_west_wall` | DDR wall screen zone, TOKENS HERE wall, arches, conduit | 12 x 9 m → 1596x1197 |
| `aa_int_face_east_wall` | PRIZES arch, Bubble Bobble wall, sconces | 12 x 9 m → 1596x1197 |
| `aa_int_face_floor` | Checkerboard marble, wear, scattered tickets baked in | 15 x 12 m → 1995x1596 |
| `aa_int_face_ceiling` | Painted vaults (mostly off-screen at this tilt) | 1024x1024 |
| `aa_int_face_north_wing_walls` | Back/west/east atlas: vault, conduit, ivy, stained-glass window | 2048x1024 atlas |
| `aa_int_face_north_wing_floor` | Checkerboard, green-tinted wet sheen | 8 x 6 m → 1064x798 |

### B. Depth layers (cutouts that stand off the walls)
| id | content |
|---|---|
| `aa_int_layer_mezzanine_west` / `_east` | Iron rail, café tables, lamps; visual only |
| `aa_int_layer_bottle_bar` | Shattered green-glass bar with PRIZE REDEMPTION built into its broken end (replaces the PNG spec's circular bar) |
| `aa_int_layer_entry_doors` | Stained-glass door leaves, foreground |
| `aa_int_layer_claw_alcove` | PRIZES arch with the rigged claw |
| `aa_int_layer_north_arch` | Framing arch into the north wing |
| `aa_int_layer_mirror_corridor` | Pilasters + mirror cards (placement open) |

### C. Hero cabinets (card-on-box; screen, marquee and state overlays separate)
| id | states |
|---|---|
| `aa_cab_frogger_existential` | idle, attract, insert-token, villain-emerging, defeated/reset (battle states; replaces the mini-game states) |
| `aa_cab_identity_crisis` | same battle state set |
| `aa_cab_kebab_kombat` | same battle state set (+ ladder-rung indicator if the ladder is ruled in) |
| `aa_cab_claw_rigged` | idle, sea-monkeys-present, play, near-miss, win, sea-monkeys-absent, shake-warning, PAYOUT light blinking. Rig approved round v26: the claw slips on every grab unless the PAYOUT light blinks (hidden every-N-plays cycle the Token Attendant hints at); Sea-Monkeys (Mint #73) or nothing until Sea-Monkeys is won, then junk-shelf prizes (Sea-Monkeys replaces the struck Beer Pong Saint Relic, author 2026-11-11). Both claws work (ruled round v26) |
| `aa_cab_ddr_broken` (north wing) | idle error, 0/3-3/3 token pips, unlock pulse |
| `aa_cab_time_crisis_cracked` (north wing) | curtain-hidden, displaced, green-glow night |

### D. Hall attractions from the approved v8 (playable unless marked set dressing; round v25)
| id | notes |
|---|---|
| `aa_prop_ddr_danceoff_pads` (x3) + `aa_int_layer_ddr_wall_screen` | **Interactive** rhythm mini-game, 2 tokens a song. Screen gets an animated arrow loop |
| `aa_prop_skeeball_lane` (x3) | **Interactive** (round v25): ticket mini-game, states idle / insert-token / playing / results (no ticket-jam state: ticket machines do not jam mechanically, flavour only, ruled round v26) |
| `aa_prop_foosball_table` | **Interactive** (round v25): ticket mini-game vs an NPC, states idle / insert-token / playing / results win / loss |
| `aa_cab_claw_beanie` | Beanie Baby claw (not the rigged claw). **Interactive** (round v25: "the claw machine must exist and work"; which claw RESOLVED round v26: both claws work): 5 tokens, prize or nothing; prize pool NEEDS AUTHOR RULING. States idle / insert-token / playing / grab-miss / grab-win |
| `aa_cab_bubble_bobble` | Real title as drawn. Set dressing (whether it pays tickets is still open) |
| `aa_cab_generic_upright_a/b/c`, `aa_cab_generic_broken` | Set dressing. Wall-row filler, marquee/screen atlases separate |

### E. Service, furniture and clutter
`aa_prop_token_exchange` (TOKENS HERE machine; idle/pay/dispense/jam), `aa_prop_token_price_board` (**1 SOV = 1 TOKEN**; the PNG spec's "1 KC = 5 TOKENS" is retired), `aa_prop_bar_stool` set + `aa_prop_bidet_stool`, `aa_prop_cabinet_stool` set, `aa_prop_standing_tables`, `aa_prop_wayfinding`, `aa_prop_floor_clutter`, `aa_prop_wall_sconce`, `aa_prop_pendant_lamp` (north wing), `aa_prop_potted_plant`, `aa_prop_hanging_ivy`.

### F. Hidden-entrance sets (unchanged from the PNG spec)
Taproom: `aa_transition_taproom_curtain`, `_plaque`, `_vapor`, `_glow`. Maintenance: `aa_transition_maintenance_door`, `aa_transition_ddr_token_pips`, `_ddr_wire_bridge`, `_maintenance_labels`, `_maintenance_unlock_fx`. Neither shows a destination interior.

### G. Characters, FX, UI, masks
Unchanged from the PNG spec sections "Character Assets", "Effects and Animation Atlases", "UI Assets" and "Technical Masks and Guides", with one change: `aa_ui_cabinet_games` (mini-game meters) is dropped, because the cabinets are battles. Character sprites follow `design/style_guides/character_sprite_pipeline.md`.

### What does not get geometry
Mezzanine figures, the mural, stained glass and vault paintwork are texture only. Distant cabinet rows on the back wall can be painted into the face if they never change state (PROPOSED: the hero cabinets and anything with a state stay separate cutouts).

## Graybox review
None yet. Before any painting: block out the hall and north wing in Godot at true metres, put three 1.8 m capsules at the doors, and check against v8 at the game camera that the walls, mezzanine height and cabinet rows line up.

## Source method
1. Orthographic elevations per wall face, generated from v8 / north v4 as references (Firefly, Nano Banana Pro or GPT Image 2.5), the same way the exterior faces were made.
2. Cutouts: crop each prop from v8 at full resolution, regenerate it clean on a flat background, matte it, then finalize at 400 px/m.
3. Day states: Firefly Relight (Sunny) + `day_grade.py`.
4. Read every word on generated art and fix misspellings (the v6 pass wrote "RECEMPTION").

## UV and texture rules
Godot StandardMaterial3D or `hd2d_relief_face.gdshader`: albedo `_day`/`_night` cross-faded, `_emit` into the glow pass, `_height`/`_normal` for relief. The author hand-paints any distress beyond what the concept already shows.

## Emissive / neon
Single `_emit` RGB mask per asset (screens, neon, bar glass, lamps, stained glass at night). Bar glass gets `aa_fx_bottle_bar_glow`'s slow pulse.

## Godot import settings
PNG, lossless, mipmaps on, filter linear. Faces into `game/assets/worlds/debaucheryville/absinthe_arcade/interior/faces/`, props into `.../interior/props/` with a `props.json` like the exterior's.

## Pipeline
Generate → `register_to.py` → `night_glow.py` → `finalize_faces.py` / `finalize_props.py` → copy into `game/assets/...` → assemble `absinthe_arcade_interior_hd2d.tscn`.

## Open items for the author
1. Hall exit toward the mirror corridor (A under the mural / B west door / C east doors).
2. Which cabinet numbers are Frogger, Street Fighter and Kebab Kombat (proposed 2 / 4 / 6).
3. DDR dance-off: real songs vs sound-alikes; token cost and ticket payout.
4. Prize Redemption catalogue and ticket prices (draft in progress).
5. New assets from rulings: hero-cabinet marquee repaints with the real titles, a Kebab Kombat ladder indicator, `aa_prop_prize_tickets` (ticket strip + counter display), and the mirror-corridor screen's own painting; the new public restroom screen (night/day, same camera conventions) with a bronze Green Fairy toilet-paper-holder statue prop (round v26).

## Build audit (2026-11-12, Eurobound-rcj)

Read-only audit, ordered by the author (bead page, 2026-11-12: "Have an agent mark each id built/missing first, then ask me per section"). No asset was changed.

- **BUILT**: a file with this id (or a direct equivalent) exists in `game/`.
- **PAINTED-SCREEN**: no separate asset; the thing is painted into a projected room plate (or a depth layer cut from one), sometimes with a code hotspot or a 2D game screen on top.
- **MISSING**: neither a file nor a painted equivalent was found.

Short paths: `int/` = `game/assets/worlds/debaucheryville/absinthe_arcade/interior/`, `scr/` = `game/worlds/debaucheryville/`, `aa/` = `game/worlds/debaucheryville/absinthe_arcade/`. Plates: hall = `int/hall/aa_int_hall_{day,night,emit}.png` (v8); north wing = `int/north_wing/aa_int_north_wing_{day,night,emit}.png`. Hotspots are `INTERACT_POINTS` in `scr/absinthe_arcade_interior_hd2d.gd:79-104` and `scr/absinthe_arcade_north_wing_hd2d.gd:33-41`. No `aa_int_face_*`, `aa_cab_*`, interior `aa_prop_*`, `aa_transition_*`, `aa_fx_*`, `aa_ui_*` or `aa_mask_*` files exist anywhere in `game/` or `Assets/Graphics/` (the `aa_prop_*` files under `Assets/Graphics/.../absinthearcade_exterior/07_props/` are exterior props). `tools/content_generation/absinthe_arcade/manifest.json` is the exterior kit's manifest and lists no interior ids.

Audit notes:
- Built but not in this manifest: the `int/taproom/`, `int/closet/` (maintenance closet), `int/restroom/` and `int/mirror_corridor/` screens (day/night/emit each), and the battle backdrops `int/battle_backdrops/aa_battle_bg_{frogger_existential_v1,street_fighter_identity_crisis_v1,kebab_kombat_v2}.png`.
- Stale: the Structural layout note "The hall exit to it is not yet placed (round v28 question restroom_door)" is out of date. The exit is wired: the `restroom_door` hotspot and `RESTROOM_TARGET` in `scr/absinthe_arcade_interior_hd2d.gd:58,97-100,323-325` (round v28 door, round v29 press_door).
- Open item 1 (hall exit toward the mirror corridor) is also built: the north arch exit, `scr/absinthe_arcade_interior_hd2d.gd:44-51`.

### A. Room shell faces: 0 built, 7 painted, 0 missing
| id | status | where |
|---|---|---|
| `aa_int_face_back_wall` | PAINTED-SCREEN | hall plate (mural, stained glass, back cabinet row) |
| `aa_int_face_west_wall` | PAINTED-SCREEN | hall plate (DDR screen wall, TOKENS HERE) |
| `aa_int_face_east_wall` | PAINTED-SCREEN | hall plate (PRIZES arch, Bubble Bobble wall, sconces) |
| `aa_int_face_floor` | PAINTED-SCREEN | hall plate (checkerboard, tickets) |
| `aa_int_face_ceiling` | PAINTED-SCREEN | hall plate (vaults along the top edge) |
| `aa_int_face_north_wing_walls` | PAINTED-SCREEN | north wing plate |
| `aa_int_face_north_wing_floor` | PAINTED-SCREEN | north wing plate |

No `_height`/`_normal` relief maps exist for any face. The projection method (status note at the top) replaced section A.

### B. Depth layers: 6 built, 1 painted, 0 missing
| id | status | where |
|---|---|---|
| `aa_int_layer_mezzanine_west` | BUILT | `int/depth_layers/aa_int_layer_mezzanine_{day,night}.png`: one layer holds both sides (no emit, per `layers.json`) |
| `aa_int_layer_mezzanine_east` | BUILT | same file as west |
| `aa_int_layer_bottle_bar` | BUILT | `int/depth_layers/aa_int_layer_bottle_bar_{day,night,emit}.png` |
| `aa_int_layer_entry_doors` | BUILT | `int/depth_layers/aa_int_layer_entry_doors_{day,night,emit}.png` |
| `aa_int_layer_claw_alcove` | BUILT | `int/depth_layers/aa_int_layer_claw_alcove_{day,night,emit}.png` |
| `aa_int_layer_north_arch` | BUILT | `int/depth_layers/aa_int_layer_north_arch_{day,night,emit}.png`; exit wiring `scr/absinthe_arcade_interior_hd2d.gd:44-51` |
| `aa_int_layer_mirror_corridor` | PAINTED-SCREEN | the corridor is its own screen: `int/mirror_corridor/aa_int_corridor_{day,night,emit}.png`, `scr/absinthe_arcade_mirror_corridor_hd2d.gd` |

Layer outlines: `Tools/content_generation/absinthe_arcade/hd2d/interior_layer_polys.json`, cut by `hd2d/cut_interior_layers.py`.

### C. Hero cabinets: 0 built, 6 painted, 0 missing (no state overlays built for any)
| id | status | where |
|---|---|---|
| `aa_cab_frogger_existential` | PAINTED-SCREEN | hall plate, back row #2; hotspot `cabinet_frogger`; fight in `aa/arcade_battle.gd` over `aa_battle_bg_frogger_existential_v1.png`. Idle/attract/insert/villain/defeated states: MISSING |
| `aa_cab_identity_crisis` | PAINTED-SCREEN | hall plate, back row #4; hotspot `cabinet_street_fighter`; backdrop `aa_battle_bg_street_fighter_identity_crisis_v1.png`. States: MISSING |
| `aa_cab_kebab_kombat` | PAINTED-SCREEN | hall plate, east wall #6; hotspot `cabinet_kebab_kombat`; backdrop `aa_battle_bg_kebab_kombat_v2.png`. States and ladder-rung indicator: MISSING |
| `aa_cab_claw_rigged` | PAINTED-SCREEN | inside the `aa_int_layer_claw_alcove` cutout; hotspot `rigged_absinthe_claw_machine`; play in `aa/claw_screen.gd` + `aa/arcade_claw.gd`; the PAYOUT light is a code `OmniLight3D` (`scr/absinthe_arcade_interior_hd2d.gd:282-289,592-593`). Painted state overlays: MISSING |
| `aa_cab_ddr_broken` | PAINTED-SCREEN | north wing plate, front right; hotspot `broken_ddr`; `aa/broken_ddr.gd`. Token pips are a text flash (see F); error and unlock-pulse art: MISSING |
| `aa_cab_time_crisis_cracked` | PAINTED-SCREEN | north wing plate, left, in front of the curtain (painted in its displaced, green-glow pose). Curtain-hidden/displaced state swap: MISSING |

### D. Hall attractions: 0 built, 10 painted, 0 missing
| id | status | where |
|---|---|---|
| `aa_prop_ddr_danceoff_pads` (x3) | PAINTED-SCREEN | hall plate, west; hotspot `ddr_dance_off`; game screen `aa/ddr/ddr_screen.gd` exists but is not wired (waits on the songs, `scr/absinthe_arcade_interior_hd2d.gd:347`) |
| `aa_int_layer_ddr_wall_screen` | PAINTED-SCREEN | hall plate (static arrows painted on the screen). Animated arrow loop: MISSING |
| `aa_prop_skeeball_lane` (x3) | PAINTED-SCREEN | hall plate; hotspot `skee_ball`; `aa/rec/skee_ball_screen.gd`. Machine state art: MISSING |
| `aa_prop_foosball_table` | PAINTED-SCREEN | hall plate; hotspot `foosball`; `aa/rec/foosball_screen.gd`. State art: MISSING |
| `aa_cab_claw_beanie` | PAINTED-SCREEN | hall plate, west; hotspot `beanie_baby_claw`; `aa/claw_screen.gd`. State art: MISSING |
| `aa_cab_bubble_bobble` | PAINTED-SCREEN | hall plate, east wall |
| `aa_cab_generic_upright_a` | PAINTED-SCREEN | hall plate, back row |
| `aa_cab_generic_upright_b` | PAINTED-SCREEN | hall plate, back row |
| `aa_cab_generic_upright_c` | PAINTED-SCREEN | hall plate, back row / east wall |
| `aa_cab_generic_broken` | PAINTED-SCREEN | hall plate filler (no clearly broken unit identified); the north wing rows are also painted |

### E. Service, furniture and clutter: 0 built, 10 painted, 2 missing
| id | status | where |
|---|---|---|
| `aa_prop_token_exchange` | PAINTED-SCREEN | hall plate, TOKENS HERE machine; hotspot `token_machine`; picker in `aa/arcade_overlay.gd`. Pay/dispense/jam state art: MISSING |
| `aa_prop_token_price_board` | MISSING | no "1 SOV = 1 TOKEN" board in the hall plate |
| `aa_prop_bar_stool` set | PAINTED-SCREEN | hall plate |
| `aa_prop_bidet_stool` | PAINTED-SCREEN | hall plate (toilet stool at the bar front) |
| `aa_prop_cabinet_stool` set | PAINTED-SCREEN | hall and north wing plates |
| `aa_prop_standing_tables` | MISSING | none on the hall floor (the café tables belong to the mezzanine layer) |
| `aa_prop_wayfinding` | PAINTED-SCREEN | hall plate (TOKENS HERE, PRIZES, PRIZE REDEMPTION signs) |
| `aa_prop_floor_clutter` | PAINTED-SCREEN | hall plate (scattered tickets) |
| `aa_prop_wall_sconce` | PAINTED-SCREEN | hall and north wing plates |
| `aa_prop_pendant_lamp` | PAINTED-SCREEN | north wing plate |
| `aa_prop_potted_plant` | PAINTED-SCREEN | hall plate (mezzanine, back wall) and north wing plate |
| `aa_prop_hanging_ivy` | PAINTED-SCREEN | hall and north wing plates |

### F. Hidden-entrance sets: 0 built, 7 painted, 2 missing
| id | status | where |
|---|---|---|
| `aa_transition_taproom_curtain` | PAINTED-SCREEN | north wing plate, left-wall arch; hotspot `taproom_curtain` (`scr/absinthe_arcade_north_wing_hd2d.gd:38-40`) |
| `aa_transition_taproom_plaque` | PAINTED-SCREEN | north wing plate, beside the curtain arch |
| `aa_transition_taproom_vapor` | PAINTED-SCREEN | north wing plate (green vapour painted static; the 20:00-04:00 rule is code only, `TAPROOM_HOURS`) |
| `aa_transition_taproom_glow` | PAINTED-SCREEN | north wing plate (curtain glow) |
| `aa_transition_maintenance_door` | PAINTED-SCREEN | north wing plate, right; hotspot `maintenance_door` |
| `aa_transition_ddr_token_pips` | MISSING | stand-in: a filled/empty circle text flash, `scr/absinthe_arcade_north_wing_hd2d.gd:180-182` |
| `aa_transition_ddr_wire_bridge` | PAINTED-SCREEN | north wing plate (cabling between the broken DDR and the door panel) |
| `aa_transition_maintenance_labels` | PAINTED-SCREEN | north wing plate (MAINTENANCE ONLY sign) |
| `aa_transition_maintenance_unlock_fx` | MISSING | stand-in: the `maintenance_indicator` light, `scr/absinthe_arcade_north_wing_hd2d.gd:138,197` |

### G. Characters, FX, UI, masks (ids from the PNG spec): 1 built, 3 painted, 23 missing
| id | status | where |
|---|---|---|
| `aa_char_backpack_girl` | MISSING | no sprite found |
| `aa_char_arcade_employee` | MISSING | no sprite by this name (`tomas_two_fifty.aseprite` staffs the prize counter; whether he fills this role is unconfirmed) |
| `aa_char_token_attendant` | BUILT | `game/assets/characters/npcs/absinthe_arcade/jakub_tokens_dvorak.aseprite` + `jakub_tokens_dvorak_asleep_statue.png` |
| `aa_char_hacker_variants` | MISSING | |
| `aa_char_edm_ghost_variants` | MISSING | |
| `aa_char_rogue_backpackers` | MISSING | |
| `aa_char_speedrunners` | MISSING | |
| `aa_fx_cabinet_mist` | PAINTED-SCREEN | north wing plate (green floor mist by the cracked cabinet), static |
| `aa_fx_electrical_sparks` | MISSING | |
| `aa_fx_digital_artifacts` | MISSING | |
| `aa_fx_mirror_afterimages` | MISSING | |
| `aa_fx_floor_pixels` | PAINTED-SCREEN | lit floor tiles painted in the hall and north wing plates, static |
| `aa_fx_bottle_bar_glow` | PAINTED-SCREEN | `aa_int_layer_bottle_bar_emit.png` (glow, no pulse animation) |
| `aa_fx_neon_signage` | MISSING | |
| `aa_fx_wet_reflections` | MISSING | exterior effect |
| `aa_ui_tokens` | MISSING | code-drawn stand-in: `aa/arcade_overlay.gd` |
| `aa_ui_claw` | MISSING | code-drawn stand-in: `aa/claw_screen.gd` |
| `aa_ui_hidden_entrances` | MISSING | |
| `aa_ui_item_icons` | MISSING | |
| `aa_ui_dialogue_portraits` | MISSING | |
| `aa_mask_exterior_collision` | MISSING | exterior; colliders are in code |
| `aa_mask_exterior_occlusion` | MISSING | exterior; occluders are in code |
| `aa_mask_interior_collision` | MISSING | code equivalent: obstacle boxes, `scr/absinthe_arcade_interior_hd2d.gd:168-183` |
| `aa_mask_interior_interaction` | MISSING | code equivalent: `INTERACT_POINTS` |
| `aa_mask_interior_occlusion` | MISSING | code equivalent: occluder prisms + depth layers, `scr/absinthe_arcade_interior_hd2d.gd:185-211` |
| `aa_guide_node_overlay` | MISSING | |
| `aa_guide_scale_camera` | MISSING | |

`aa_ui_cabinet_games` is dropped by this manifest (cabinets are battles) and is not counted.
