# Bottoms Down (`bottoms_down`) repaint plan (asset team, plan job, no generation)

Source: the Writers' Room rewrite, author-approved (Desk 3ho-q12). Doc line refs are to `design/worlds/shamsterdam/bottoms_down.md` (BD) and `PNG_Assets/bottoms_down_png_assets.md` (PNG).

## Files read (id `shamsterdam_oldtown_bottoms_down_01`)
- READ: `bottoms_down.md`; `PNG_Assets/bottoms_down_png_assets.md`; `npcs/bottoms_down/npc_kees.md` (the only file in that folder).
- MISSING (no file with the stem or the id exists in the folder): `core/`, `environment/`, `interactions/`, `items/`, `location_nodes/`, `sprite_mapping/`, `events/`.
- Also consulted: `design/items/brewery_tour/{beer,opener,stamp}_bottoms_down_item.md` (found by grep, not opened in full); `WritingRoom/tasks/shamsterdam_rename_final_map.md` (grep); TEAM_BRIEF, QC.md, PAINT_JOB.md, `location_interactables_rule.md`; old reviews `bottoms_down_ext_review.jpg` and `bottoms_down_int_review.jpg` (cottage and candlelit tavern: the new art must not look like them); both contact sheets.
- Sign text checked against BD 48-61: all five requested strings match the doc exactly. The doc also gives the banner, arrow, DUCK plate and interior sawdust sign. PNG adds a second taped line ("THE FLOOR IS SOFT. YOU'LL FIND OUT.") that BD lacks. BD wins, so it is not painted (Q5).

## Hook
BD 44-46: "A bar that brags about knocking people down."
**The one exaggeration, readable at thumbnail size:** a giant flickering backlit "BOTTOMS DOWN" sign over a red-painted arrow alley, a chalk scoreboard of the fallen, and a mop bucket on a barstool with an "EMPLOYEE OF THE MONTH" plaque.

## Palette (PNG 14-27; every hex is the doc's)
- Jenever Amber #FFBF00: sign letters (Q1), neon JENEVER tube, bottle wall, brim-full glasses.
- Oak Brown #806517: bar slab, barrel tables, beams, door.
- Bleached Cream #FFF8DC: laminate and paper, chalkboard frame, sign backings (a hue, never a light pool).
- Sawdust Tan #D2B48C: floor and footprints, crumbling mortar.
- Brass Aged #B5892E: foot rail, plaque.
- Old Room Shadow #2B2116: blackened brick, ceiling shadow, back-room base.
- Warning-Placard Red #C0281C: alley arrow, "NO HANDS" banner, "YOU WILL SPILL.", record line, dead-tube off-state.
- Bottleneck Grey #6B6B5A: grime, caged bulbs, window light, foam padding.

## Exterior
Not a cottage. A flat-fronted, plain-cornice, two-storey blackened-brick slab (storeys are a proposal, Q2) at the end of a narrow brick alley, seen at an angle down the alley. None of the stepped gable, tile roof, half-timbering, trees or canal railing of earlier plates. One window boarded with a graffitied plank; the other glazed, paper warning taped inside. Low door with the dented DUCK plate at forehead height. Above it the backlit sign, half its letters dead, with the "AS SEEN ON THE FLOOR." stencil on the fascia below. Under that, the red "NO HANDS. NO FEAR. NO REFUNDS." banner half-covering the green-aged plaque "EST. 1624. THE FLOOR HAS HOSTED KINGS. MOSTLY FACE-DOWN." Pictogram panel beside the door. Laminated "YOU WILL SPILL." taped to the door. Window paper "EVERYBODY BOWS EVENTUALLY. THE SMART ONES DO IT FACING THE BAR." Red arrow at the alley mouth, chest-high. Light: overcast grey by day; sign glare and caged bulbs by night. Neighbours: plain, unnamed brick.

## Interior
Differs from every existing plate: sawdust floor (BD 71, doc-named) with painted distance markers, cold caged-bulb light, no candles.
- **Main tasting room** (BD 62-93): long, low, 8 m oak bar, foam-taped beams, caged bulbs on a sagging cord, dead tube over the back corner, amber neon JENEVER, one grey window, scoreboard, bell, bucket, corkboard, barrel tables, no stools.
- **Back room** (BD 94-103): smaller, colder, one caged bulb on the chair. Floor unspecified (Q4).

## Satire beats made visible
1. BD 49-50: the red arrow shouting "YES, THIS IS THE PLACE. NO, YOU CAN'T HANDLE IT."
2. BD 79: the scoreboard, "THE FALLEN ... RECORD: 31", next gap already chalked.
3. BD 82: the mop bucket trophy, "EMPLOYEE OF THE MONTH".
4. BD 71-78: sawdust sold as an amenity, distance markers like a long-jump pit, "PERSONAL BEST".
5. BD 99: the seatbelted lawn chair with bite marks and a luggage tag, under one spotlight.

## Not in the file, needs approval
- Q1. Sign letter colour and amber's share. Doc gives none. Proposed: amber letters on a cream-backed box; sawdust tan covers most interior area while amber carries the saturation (palette Primary).
- Q2. Storeys, roofline, facade proportions, alley angle. Proposed above.
- Q3. Boarded-window graffiti content. Proposed: illegible tags, no words.
- Q4. Back-room floor material. Proposed: bare plank, sawdust-free.
- Q5. PNG's extra taped line and "Taped Note at Wrong Height" text. Proposed: not painted; note faces left blank.
- Q6. "JENEVER" on the neon and shelves (doc text, Dutch-origin word) and the "Oude Genever" label (rename map defers it to the drinks rename). Proposed: paint JENEVER as the doc spells it; leave Oude Genever labels blank until the rename lands.
- Q7. Alley clutter (bins, crates, drain). Proposed: none; doc silent.
- Q8. Separate-prop folder path. Proposed `props/` and `exterior_props/`.
- Q9. Lettering method. Proposed: all lettering typed with Pillow onto blank faces, never drawn by the image model.

---

## (A) Scene decomposition

Classes: SHELL (baked architectural shell), PROP (separate asset, no interaction), INT (interactive, separate, declared in location data), PICK (pickup), NPC (anchor spot only, no figure), FX (anchor), UI (trigger point). No interactions JSON exists for this location (MISSING above), so each INT needs a bead or Desk card for its interaction ID; none is invented here.

### A1. Exterior
| Item | Class | Note |
|---|---|---|
| Alley brick walls, blackened brick, crumbling mortar, cobbles, fascia, cornice | SHELL | |
| Boarded window with plank graffiti; glazed window frame | SHELL | graffiti per Q3 |
| Brass plaque, pictogram panel, taped window paper | SHELL | flat faces baked per BD; Pillow lettering |
| Front door with DUCK plate and taped "YOU WILL SPILL." | INT | map transition; plate and tape are dressing on the door asset; plate leaves a clean door recess |
| Backlit "BOTTOMS DOWN" sign assembly | PROP + FX | half the tubes flicker; fascia stencil baked |
| "NO HANDS" banner | PROP | separate per BD sign-assembly rule |
| Red alley arrow sign | PROP | separate; at alley mouth |
| Neon haze, sign glare | FX | |
| Patron single-file spot along the wall; tourist photo spot at the door | NPC | spots only |
| Door threshold | UI | entry prompt |

### A2. Main tasting room
| Item | Class | Note |
|---|---|---|
| Brick and beam shell, foam-padded beams with dents, low ceiling | SHELL | |
| 8 m oak bar counter, elbow groove, brass foot rail | SHELL | built in |
| Sawdust floor, painted distance markers | SHELL | markers also an examine trigger (INT) |
| Caged bulbs with sagging cord; dead tube | SHELL + FX | dead tube has a red off-state flicker |
| Grey window, water-damaged photos, newspaper clippings, distillery equipment incl. coat-rack piece | SHELL | |
| Bottle shelving (200+ bottles: rookie, geezer, fossil, DON'T ASK) | SHELL | DON'T ASK trigger over it is INT |
| Sawdust sign over the door, taped signs | SHELL | |
| Kees's bar interaction point | INT + UI | order, opener check, gauntlet start |
| Gauntlet five-glass row | INT | states: setup / correct / wrong |
| Concussion Attempt spot | UI | selfie trigger |
| Scoreboard "THE FALLEN" | INT | tally typed by script; TODAY stays static until the author rules |
| Ship's bell with sign | INT + FX | ring and chalk-sting anchors (ambient only until ruled) |
| Wall of the Fallen corkboard | INT | |
| Spill Kit station (mop, scoop, sawdust sack, SELF SERVE) | INT | examine only |
| "Traditional Drinking Method" diagram | INT | examine, tutorial hook |
| Back-room door | INT | one art state, unlock glow overlay |
| Mop bucket on barstool, plaque | PROP | collision |
| Barrel tables x2 | PROP | collision |
| Ceramic jugs, brim-full tulip glasses (full / spilled / empty) | PROP + FX | pour anchor |
| Neon "JENEVER" sign assembly | PROP + FX | flicker loop |
| Bar towel, empty glass stack, Pim's restock crate, sawdust broom, fresh sawdust sack | PROP | |
| Spill puddles | FX | runtime states |
| Sawdust motes, jenever vapour, neon haze | FX | |
| Kees station; Pim; the Regular (end of bar); Corporate Group; Purist; First Date | NPC | spots only |
| Entry marker; exit to alley | UI | |

### A3. Back room
| Item | Class | Note |
|---|---|---|
| Dark brick shell, deep shelf of hand-labelled bottles, family photo wall | SHELL | |
| Caged bulb spotlight on the chair | SHELL + FX | |
| The Chair (lawn chair, bolted, seatbelt with bite marks, laminated tag, luggage tag) | INT | one asset, tags attached |
| 100-Year Barrel | INT | examine only |
| Barrel table | PROP | collision |
| Mop bucket at attention | PROP | |
| Seatbelt-click audio anchor | FX | |

### A4. Pickups (reward-only, nothing painted in the rooms)
Bottoms Down bottle opener; Oude Genever stamp; Oude Genever consumable (name per Q6). Icons belong to the item team.

---

## (B) Asset requirements

Root: `game/assets/worlds/shamsterdam/bottoms_down/`. Plates are 16:9, at least 2048 px wide, clean: no INT, PROP or PICK item from list A painted in.

### Plates (PAINT_JOB step 5)
- `exterior/bottoms_down_ext_day.png`
- `exterior/bottoms_down_ext_night.png`
- `exterior/bottoms_down_ext_front_elevation_day.png`
- `interior/bottoms_down_int_day.png`
- `interior/bottoms_down_int_night.png`
- `interior/bottoms_down_int_back_room_day.png`
- `interior/bottoms_down_int_back_room_night.png`
- Review sheets: `dev/asset_team/reviews/bottoms_down_ext_review.jpg`, `dev/asset_team/reviews/bottoms_down_int_review.jpg`.

### Separate prop assets (path per Q8)
Fields per asset: collision, interaction, states, FX or sound, quest.

Exterior, `exterior_props/`:
- `bd_front_door.png`: INT; collision yes; map transition; closed/open; door sound; carries DUCK plate and taped notice.
- `bd_sign_backlit.png`: no collision; FX flicker states on / half / off; buzz.
- `bd_banner_no_hands.png`: static.
- `bd_alley_arrow_sign.png`: static.

Interior, `props/`:
- `bd_bar_trigger.png` (invisible): INT; Brewery Tour quest.
- `bd_gauntlet_glass_row.png`: INT; setup / correct / wrong / cleared; glass sounds; Gauntlet quest.
- `bd_glass_tulip_full.png`, `_spilled.png`, `_empty.png`; `bd_ceramic_jug.png`: PROP; pour FX.
- `bd_scoreboard.png`: INT; chalk states; chalk scratch.
- `bd_bell.png`: INT; swing frames; bell sound.
- `bd_wall_fallen.png`: INT; state per the pending author question.
- `bd_spill_kit.png`, `bd_method_diagram.png`: INT, examine only.
- `bd_dont_ask_shelf_trigger.png` (invisible): INT.
- `bd_backroom_door.png`: INT; one art state plus unlock glow overlay.
- `bd_chair_seatbelt.png`: INT; collision yes; failure-beat dialogue; seatbelt click.
- `bd_barrel_100yr.png`: INT, examine only.
- `bd_barrel_table_a.png`, `bd_barrel_table_b.png`: PROP; collision.
- `bd_mop_bucket_stool.png`: PROP; collision.
- `bd_neon_jenever.png`: PROP; FX on/off flicker; hum.
- `bd_pim_crate.png`, `bd_broom.png`, `bd_glass_stack.png`, `bd_bar_towel.png`, `bd_sawdust_sack.png`: PROP.
- FX layers: `fx_sawdust_motes.png`, `fx_neon_haze.png`, `fx_dead_tube_flicker.png`, `fx_spill_puddle_large.png`, `fx_spill_puddle_small.png`.
- Floor: `bd_sawdust_tile.png` (seamless; floor and footprint decals).

Reuse: barrel tables and sawdust tile are reusable; everything else is unique to this location. Inventory icons: item team (A4). Material sets: oak, blackened brick, sawdust, brass, grimy glass, duct-taped foam.
