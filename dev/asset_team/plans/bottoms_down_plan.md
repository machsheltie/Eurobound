# Bottoms Down (`bottoms_down`) repaint plan, round 2

Refs: BD = `design/worlds/shamsterdam/bottoms_down.md`, PNG = `PNG_Assets/bottoms_down_png_assets.md`. Files read: BD, PNG, `npcs/bottoms_down/npc_kees.md`; MISSING: `core/`, `environment/`, `interactions/`, `items/`, `location_nodes/`, `sprite_mapping/`, `events/`. Signs verified against BD 53-58: all five match; BD wins over PNG's extra taped line.

<!-- BODY START -->
## Hook
BD 46: "A bar that brags about knocking people down." **One exaggeration:** giant flickering "BOTTOMS DOWN" sign over a red arrow alley, a chalk scoreboard of the fallen, a mop-bucket trophy.

**Seedy props (7):** 1 flickering backlit plastic sign (BD 53); 2 red house-paint arrow (BD 49); 3 taped laminated "YOU WILL SPILL." (BD 57); 4 chalk scoreboard (BD 70); 5 mop bucket "EMPLOYEE OF THE MONTH" (BD 72); 6 duct-taped foam beams (BD 64); 7 seatbelted chair, bite marks (BD 102).
**Lighting:** caged cool bulbs, buzzing neon, grey window (BD 65, 115). No candles.

## Palette (PNG 14-27)
Amber #FFBF00 dominates: sign face (Q1), neon, bottle wall, glasses. Oak #806517: bar, barrels, beams. Cream #FFF8DC: paper, chalkboard frame. Sawdust #D2B48C: floor. Brass #B5892E: rail, plaque. Shadow #2B2116: ceiling, back room. Red #C0281C: arrow, banner, warning, record. Grey #6B6B5A: grime, bulbs, foam, window.

## Exterior
Flat-fronted plain-cornice brick slab, alley's end, angled view; no gable, tiles, half-timbering. All signs, door, windows per BD 49-58.

## Interior
Sawdust floor (BD 66), distance markers (BD 69). Main room: bar, beams, scoreboard, bell, bucket, corkboard, barrels. Back room: dark, spotlit chair.

## Satire beats
1. Arrow, "YOU CAN'T HANDLE IT" (BD 49).
2. Scoreboard, record 31 (BD 70).
3. Bucket trophy (BD 72).
4. Sawdust as amenity (BD 66).
5. Seatbelt chair (BD 102).

## Needs approval
- Q1 Sign colour: propose amber face.
- Q2 Storeys, roofline.
- Q3 Window graffiti: propose illegible.
- Q4 Back-room floor.
- Q5 PNG's extra taped line: unpainted.
- Q6 No Dutch painted: neon and labels blank; no "JENEVER", no "Oude Genever". English parody word wanted (Writers' Room supplies)?
- Q7 Ground, alley clutter: doc silent.
- Q8 Oak on door; Shadow as brick: proposals.
- Q9 Prop folders; Pillow lettering.
<!-- BODY END -->

---

## (A) Scene decomposition
SHELL baked; PROP separate; INT interactive (no interactions JSON exists, so each needs a bead/Desk card); PICK pickup; NPC spot only; FX anchor; UI trigger.

### Exterior
| Item | Class |
|---|---|
| Brick walls, mortar, fascia, cornice, boarded window, glazed window frame | SHELL |
| Plaque, pictogram, window paper (blank faces, Pillow text) | SHELL |
| Front door + DUCK plate + taped "YOU WILL SPILL." | INT (map transition) |
| Backlit "BOTTOMS DOWN" sign | PROP + FX |
| "NO HANDS" banner; red arrow sign | PROP |
| Neon haze | FX |
| Patron wall spot; photo-tourist spot | NPC |
| Door threshold | UI |

### Main room
| Item | Class |
|---|---|
| Brick/beam shell, foam beams, 8 m bar counter, foot rail, sawdust floor, markers, window, photos, clippings, equipment, bottle shelves, taped signs, sawdust sign | SHELL |
| Caged bulbs, dead tube | SHELL + FX |
| Bar point; Concussion spot | INT + UI |
| Gauntlet glass row; scoreboard; bell; corkboard; spill kit; method diagram; back-room door; DON'T ASK trigger; distance-marker trigger | INT |
| Bucket on stool; barrel tables x2; jugs and glasses; neon tube assembly (blank face); towel, glass stack, Pim's crate, broom, sawdust sack | PROP (jugs, neon also FX) |
| Motes, vapour, puddles | FX |
| Kees, Pim, Regular, Corporate Group, Purist, First Date | NPC |
| Entry/exit | UI |

### Back room
| Item | Class |
|---|---|
| Brick shell, shelf, family photos | SHELL |
| Spotlight bulb | SHELL + FX |
| Chair (seatbelt, tags) ; 100-Year Barrel | INT |
| Barrel table; mop bucket | PROP |

### Pickups
Opener, stamp, consumable: reward-only, not painted in (item team icons).

---

## (B) Asset requirements
Root `game/assets/worlds/shamsterdam/bottoms_down/`. Plates 16:9, 2048+ px, clean of INT/PROP.

| File | Notes |
|---|---|
| `exterior/bottoms_down_ext_day.png`, `_ext_night.png`, `_ext_front_elevation_day.png` | plates |
| `interior/bottoms_down_int_day.png`, `_int_night.png` | main room |
| `interior/bottoms_down_int_back_room_day.png`, `_night.png` | back room |
| `exterior_props/bd_front_door.png` | INT, collision, open/closed |
| `exterior_props/bd_sign_backlit.png` | FX on/half/off |
| `exterior_props/bd_banner_no_hands.png`, `bd_alley_arrow_sign.png` | static |
| `props/bd_bar_trigger.png`, `bd_dont_ask_shelf_trigger.png` | invisible INT |
| `props/bd_gauntlet_glass_row.png` | INT, 4 states |
| `props/bd_glass_tulip_{full,spilled,empty}.png`, `bd_ceramic_jug.png` | PROP, pour FX |
| `props/bd_scoreboard.png`, `bd_bell.png`, `bd_wall_fallen.png`, `bd_spill_kit.png`, `bd_method_diagram.png` | INT |
| `props/bd_backroom_door.png`, `bd_chair_seatbelt.png`, `bd_barrel_100yr.png` | INT |
| `props/bd_barrel_table_{a,b}.png`, `bd_mop_bucket_stool.png` | PROP, collision |
| `props/bd_neon_tube.png` | PROP + FX, blank face (Q6) |
| `props/bd_pim_crate.png`, `bd_broom.png`, `bd_glass_stack.png`, `bd_bar_towel.png`, `bd_sawdust_sack.png` | PROP |
| `props/fx_sawdust_motes.png`, `fx_neon_haze.png`, `fx_dead_tube_flicker.png`, `fx_spill_puddle_{large,small}.png` | FX |
| `props/bd_sawdust_tile.png` | seamless floor |

Review sheets: `dev/asset_team/reviews/bottoms_down_ext_review.jpg`, `_int_review.jpg`. Barrel tables and sawdust tile reusable; rest unique. Materials: oak, brick, sawdust, brass, foam.
