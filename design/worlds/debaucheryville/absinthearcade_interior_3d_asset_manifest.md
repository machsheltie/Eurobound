# Absinthe Arcade Interior — 3D Asset Manifest

> **Status: asset list APPROVED by the author 2026-11-09.** Items still marked **PROPOSED** are agent proposals, not rulings.
>
> **Build method ruled 2026-11-09: projection.** The approved paintings are projected onto graybox geometry from a fixed camera per room (built by session eurobound-46: commits 702ba33, 80b49fa). Room faces are not repainted orthographically, so section A below is superseded by the projected plates. **No people are painted into room art**; every person is a movable NPC sprite. Hall source plates: `references/Interior/concepts/aa_interior_hall_v8_clean_{night,day}.png` (v8 with the four painted patrons removed). Bros are sized to the furniture (counter at waist height). North wing v4 approved. The mirror corridor is its own screen; the hall exit toward it is open with the author (A/B/C on the decisions page). The DDR dance-off is a playable rhythm mini-game (the player picks one bro, the other two are AI), so `aa_prop_ddr_danceoff_pads` + screen move from set dressing to an interactive asset. Battle cabinets: two in the back row, one on the right wall.

**Purpose:** production manifest for the Arcade interior kit. Built from `design/templates/3D_Asset_Manifest_Template.md`. That template and `design/style_guides/3d_asset_rules.md` still describe the retired Unity/Tripo kit. This manifest follows the Godot 4.7 painted-box method the exterior uses (`Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_exterior/hd2d_asset_manifest.md`), and keeps the template's section order.

- **Location docs:** `design/World Design/Debaucheryville/` Arcade package (`core/`, `location_nodes/absinthe_arcade_location_nodes.json`, `sprite_mapping/`, `PNG_Assets/Absinthe_Arcade_Complete_PNG_Asset_Requirements.md`)
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
| Cabinets | Frogger: Existential Edition, Street Fighter: Identity Crisis and Kebab Kombat are battle encounters. The rigged claw is the one real mini-game. Real game names stay as drawn (2026-11-08) |
| Economy on signage | 1 SOV = 1 token. DDR unlock 3 tokens. Claw 5 tokens per attempt |
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
 | DDR screen + 3 pads   Skee-Ball  foosball   shattered-glass   | Bubble Bobble
 | Beanie claw                                  bar + PRIZE      | right-wall row
 | TOKENS HERE + Backpack Girl     open floor   REDEMPTION       | PRIZES claw alcove
 |                  stained-glass entry doors (south)            |
 +---------------------------------------------------------------+   main hall 15 x 12 m
```

- Hall height to vault crown about 9 m, mezzanine deck about 4.5 m (PROPOSED: ground + first floor of the 4-storey exterior).
- North-wing vault about 5 m (PROPOSED: "lower" per the spec and v4).
- Not yet placed: **mirror corridor** (`aa_node_mirror_corridor`, between the cabinet loop and the north wing). Open question.

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
| `aa_cab_claw_rigged` | idle, relic-present, play, near-miss, win, relic-absent, shake-warning |
| `aa_cab_ddr_broken` (north wing) | idle error, 0/3-3/3 token pips, unlock pulse |
| `aa_cab_time_crisis_cracked` (north wing) | curtain-hidden, displaced, green-glow night |

### D. Hall attractions from the approved v8 (set dressing; only the claw plays)
| id | notes |
|---|---|
| `aa_prop_ddr_danceoff_pads` (x3) + `aa_int_layer_ddr_wall_screen` | Screen gets an animated arrow loop |
| `aa_prop_skeeball_lane` (x3) | |
| `aa_prop_foosball_table` | |
| `aa_cab_claw_beanie` | Beanie Baby claw (not the rigged claw) |
| `aa_cab_bubble_bobble` | Real title as drawn |
| `aa_cab_generic_upright_a/b/c`, `aa_cab_generic_broken` | Wall-row filler, marquee/screen atlases separate |

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
5. New assets from rulings: hero-cabinet marquee repaints with the real titles, a Kebab Kombat ladder indicator, `aa_prop_prize_tickets` (ticket strip + counter display), and the mirror-corridor screen's own painting.
