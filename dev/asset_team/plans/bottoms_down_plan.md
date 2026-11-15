# Bottoms Down (`bottoms_down`) repaint plan, round 3

Refs: BD = `design/worlds/shamsterdam/bottoms_down.md`, PNG = `PNG_Assets/bottoms_down_png_assets.md`. Files read: BD, PNG, `npcs/bottoms_down/npc_kees.md`, and `design/items/brewery_tour/{opener,stamp,beer}_bottoms_down_item.md` (cited at BD 429-431). I also searched `design/` and `docs/` for item files outside the city folder: none beyond those three. MISSING: `core/`, `environment/`, `interactions/`, `items/`, `location_nodes/`, `sprite_mapping/`, `events/`. Signs verified against BD 53-58; BD wins over PNG's extra taped line. Item visual cues: tulip glass overfilled, convex meniscus, amber-tinted brass, sawdust-coloured leather loop, amber ink with cream foam.

<!-- BODY START -->
## Hook
BD 46: "A bar that brags about knocking people down." **One exaggeration:** a sign bigger than the building, over a red arrow alley, plus a chalk scoreboard of the fallen.

**Seedy props (7):** 1 flickering backlit plastic sign (BD 53); 2 red house-paint arrow (BD 49); 3 taped laminated "YOU WILL SPILL." (BD 57); 4 chalk scoreboard (BD 70); 5 mop bucket trophy (BD 72); 6 duct-taped foam beams (BD 64); 7 seatbelted chair (BD 102).
**Lighting:** caged cool bulbs, buzzing neon, grey window. No candles.

## Palette (PNG 14-27)
Amber #FFBF00 leads: exterior about 40% (sign wash and neon spill over blackened brick), main room about 45% (neon flooding bar, sawdust, amber glass bottle wall), back room 15%. Oak #806517: bar, barrels, beams. Cream #FFF8DC: paper, chalkboard frame. Sawdust #D2B48C: floor. Brass #B5892E: rail, plaque. Shadow #2B2116: ceiling, back room. Red #C0281C: arrow, banner, warning. Grey #6B6B5A: grime, bulbs, foam.

## Exterior (proposed)
Squat one-storey blackened-brick box, flat parapet, two small asymmetric windows (one boarded), low door, rooftop sign twice its height, red arrow on the alley wall. Differs: contact-sheet fronts are multi-storey and many-windowed; this is a low box under a giant sign.

## Interior
Sawdust floor (BD 66), markers (BD 69); back room cold, spotlit.

## Satire beats
1. Arrow "YOU CAN'T HANDLE IT" (BD 49).
2. Scoreboard record 31 (BD 70).
3. Bucket trophy (BD 72).
4. Sawdust amenity (BD 66).
5. Seatbelt chair (BD 102).

## Needs approval
- Q1 Sign face amber; amber shares.
- Q2 Exterior shape above.
- Q3 Graffiti: illegible.
- Q4 Back-room floor.
- Q5 PNG extra line: unpainted.
- Q6 No Dutch painted: neon and labels blank. English parody word wanted (Writers' Room)?
- Q7 Ground, clutter.
- Q8 Oak door; Shadow brick; Pillow lettering.
<!-- BODY END -->

---

## (A) Scene decomposition
SHELL baked; PROP separate; INT interactive; NPC spot; FX anchor; UI trigger. Every INT and UI has a row in (B).

| Area | Item | Class |
|---|---|---|
| Ext | Brick walls, mortar, fascia, parapet, boarded window, glazed frame, plaque, pictogram, window paper | SHELL |
| Ext | Front door (DUCK plate, taped warning), door threshold | INT + UI |
| Ext | Backlit sign; banner; red arrow sign | PROP (sign + FX) |
| Ext | Patron wall spot; photo-tourist spot | NPC |
| Main | Brick/beam shell, foam beams, bar counter, foot rail, sawdust floor, window, photos, clippings, equipment, bottle shelves, taped signs, sawdust sign | SHELL |
| Main | Caged bulbs, dead tube | SHELL + FX |
| Main | Bar point; Concussion spot; distance-marker trigger; DON'T ASK trigger | INT/UI |
| Main | Gauntlet row; scoreboard; bell; corkboard; spill kit; diagram; back-room door | INT |
| Main | Bucket on stool; barrel tables; jugs, glasses; neon tube (blank face); towel, glass stack, Pim's crate, broom, sawdust sack | PROP |
| Main | Motes, vapour, puddles | FX |
| Main | Kees, Pim, Regular, Corporate Group, Purist, First Date | NPC |
| Back | Brick shell, shelf, family photos | SHELL |
| Back | Spotlight bulb | SHELL + FX |
| Back | Chair; 100-Year Barrel | INT |
| Back | Barrel table; mop bucket | PROP |
| Pickups | Opener, stamp, consumable | reward-only, not painted in |

---

## (B) Asset requirements
Root `game/assets/worlds/shamsterdam/bottoms_down/`. Plates 16:9, 2048+ px, clean of INT/PROP. Interaction IDs are pending: no interactions JSON exists; bead **Eurobound-bsma** owns writing them (I added a comment listing the three items the doc leaves without one). Columns: R reuse/unique, Col collision, ID interaction ID, St states, An animation, Snd sound, Q quest, Ic inventory icon, Mat material set.

### Plates
`exterior/bottoms_down_ext_day.png`, `_ext_night.png`, `_ext_front_elevation_day.png`; `interior/bottoms_down_int_day.png`, `_int_night.png`, `_int_back_room_day.png`, `_int_back_room_night.png`. Review sheets `dev/asset_team/reviews/bottoms_down_ext_review.jpg`, `_int_review.jpg`.

### Separate assets
| File | R | Col | ID | St | An | Snd | Q | Ic | Mat |
|---|---|---|---|---|---|---|---|---|---|
| `exterior_props/bd_front_door.png` | U | yes | pending | open/closed | door | door | n/a | n/a | oak, steel |
| `exterior_props/bd_sign_backlit.png` | U | no | n/a | on/half/off | flicker | buzz | n/a | n/a | plastic |
| `exterior_props/bd_banner_no_hands.png`, `bd_alley_arrow_sign.png` | U | no | n/a | 1 | n/a | n/a | n/a | n/a | paint, cloth |
| `props/bd_bar_trigger.png` (invisible) | U | no | pending | 1 | n/a | n/a | Brewery Tour | n/a | n/a |
| `props/bd_concussion_spot_trigger.png` (invisible) | U | no | pending | 1 | n/a | n/a | Footage | n/a | n/a |
| `props/bd_distance_marker_trigger.png` (invisible) | U | no | pending | 1 | n/a | n/a | n/a | n/a | n/a |
| `props/bd_dont_ask_shelf_trigger.png` (invisible) | U | no | pending | 1 | n/a | n/a | n/a | n/a | n/a |
| `props/bd_gauntlet_glass_row.png` | U | no | pending | setup/correct/wrong/cleared | fill | glass | Gauntlet | n/a | glass |
| `props/bd_glass_tulip_{full,spilled,empty}.png`, `bd_ceramic_jug.png` | U | no | n/a | 3 | pour | pour | n/a | n/a | glass, ceramic |
| `props/bd_scoreboard.png` | U | no | pending | chalk tallies | chalk | scratch | n/a | n/a | slate |
| `props/bd_bell.png` | U | no | pending | still/swing | swing | bell | n/a | n/a | brass |
| `props/bd_wall_fallen.png` | U | no | pending | 1 (more pending ruling) | n/a | n/a | n/a | n/a | cork, paper |
| `props/bd_spill_kit.png`, `bd_method_diagram.png` | U | spill kit yes | pending | 1 | n/a | n/a | tutorial (diagram) | n/a | mixed |
| `props/bd_backroom_door.png` | U | yes | pending | locked/unlocked glow | glow | latch | Gauntlet | n/a | oak |
| `props/bd_chair_seatbelt.png` | U | yes | pending | 1 | n/a | seatbelt click | Gauntlet fail | n/a | plastic, webbing |
| `props/bd_barrel_100yr.png` | U | yes | pending | 1 | n/a | n/a | n/a | n/a | oak |
| `props/bd_barrel_table_{a,b}.png` | reuse | yes | n/a | 1 | n/a | n/a | n/a | n/a | oak |
| `props/bd_mop_bucket_stool.png`; `bd_mop_bucket_back.png` | U | yes | n/a | 1 | n/a | n/a | n/a | n/a | metal, wood |
| `props/bd_neon_tube.png` (blank, Q6) | U | no | n/a | on/off | flicker | hum | n/a | n/a | glass |
| `props/bd_pim_crate.png`, `bd_broom.png`, `bd_glass_stack.png`, `bd_bar_towel.png`, `bd_sawdust_sack.png` | U | crate, sack yes | n/a | 1 | n/a | n/a | n/a | n/a | mixed |
| `props/fx_sawdust_motes.png`, `fx_neon_haze.png`, `fx_dead_tube_flicker.png`, `fx_spill_puddle_{large,small}.png` | U | no | n/a | 1-2 | loop | n/a | n/a | n/a | n/a |
| `props/bd_sawdust_tile.png` (seamless) | reuse | no | n/a | 1 | n/a | n/a | n/a | n/a | sawdust |

Pickup icons (opener, stamp, consumable) belong to the item team, per their item docs.
