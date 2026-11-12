# Absinthe Arcade — Complete PNG Asset Requirements

## Overview

| Field | Value |
|---|---|
| Location ID | `debaucheryville_clocktower_arcade_01` |
| Engine | Godot 4.7 (Forward+) |
| Production style | Painterly HD-2D painted-box diorama |
| Exterior | Historic Clocktower Plaza facade vandalized by a green-and-purple arcade retrofit |
| Interior | Grand adaptive-reuse amusement hall organized around a monumental cracked-bottle bar |
| Camera | Fixed HD-2D tilt, approximately 30–40° down, narrow perspective FOV |
| Target | 60 FPS with scalable particles, emission and crowd layers |

This document supersedes the earlier four-sheet, pure pixel-art package. The final direction is painterly HD-2D: simple 3D room/building massing receives painted orthographic face textures, important forms stand proud as alpha depth cards or low-complexity geometry, and props/characters use `Sprite3D` cutouts or billboards where appropriate.

The hero facade is one authored building identity. It is **not** a 32-bit tile sheet. Tiles remain appropriate only for repeatable cobble, checkerboard flooring, generic limestone, roof slate, puddles and small utility surfaces.

### Source authority

1. `Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_exterior/hd2d_asset_manifest.md`
2. `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/mastercomponentbreakdown.md`
3. `design/worlds/debaucheryville/absinthearcade.md`
4. `design/Quests/debaucheryville/`

## Locked Visual Canon

### Exterior read

The building must read in this order:

1. Beautiful, sincere cream limestone/plaster architecture with carved surrounds, mansard roof, dormers, chimneys, iron balconies, plants and the canonical black window cat.
2. Monumental Green Fairy mural: Art Nouveau flowers and hair transition into pixel squares and circuit traces.
3. Headphone Gentleman keystone: classical carved male head, vandal moustache, industrial ear cups, green ribbed tubes, purple conduit and believable junction hardware.
4. Black stepped marquee with green `ABSINTHE`, purple `ARCADE`, token emblem, pixel invader and `LOSE YOUR MIND ONE TOKEN AT A TIME`.
5. Stained-glass doors, checkerboard threshold, exterior cabinet, corrugated awning, chalkboard, lanterns, bollards, planters, metal bucket and wet-cobble reflections.

Historic architecture is the straight man. It must remain dignified and plausible enough for the retrofit to feel disrespectful.

### Interior read

The interior is not a generic black room full of neon. It is the same historic building inside:

- Cream carved stone and aged plaster.
- Arched ceiling bays and iron mezzanine rails.
- Warm amber pendant lights and wall sconces.
- Glossy black-and-white checkerboard floor with selective green/purple pixel inlays.
- A monumental cracked green absinthe-bottle reservoir rising from the circular central bar.
- Readable cabinet aisles looping around the bar.
- A darker L-shaped north wing containing the two hidden-location approaches.

Toxic green, neon purple, sticker-bombed machines, exposed retrofit conduit, localized cabinet mist and bad signage corrupt the historic shell without erasing it.

### Interior layout landmarks

1. Stained-glass vestibule and checkerboard threshold.
2. Token exchange with Backpack Girl seated against a cabinet beside it.
3. Central cracked-bottle bar and clear circulation ring.
4. Twisted cabinet gallery.
5. Rigged claw/prize alcove.
6. Delayed-reflection corridor.
7. North wing with visibly distinct Taproom and maintenance-restroom approaches.

## Linked-Location Boundary Rules

### The Absinthium Taproom

- Destination: `debaucheryville_brewery_absinthium_taproom_01`.
- Destination authority: `design/worlds/debaucheryville/the_absinthium_taproom.md`.
- Arcade-visible entrance: the west recess of the north wing, partially revealed behind a cracked Time Crisis cabinet.
- Required visual cues: heavy glowing green velvet curtain, vapor curling underneath, small brass plaque reading `NOT RECOMMENDED FOR THOSE PRONE TO INTROSPECTION`, and slow breathing green rim light after 20:00.
- Generate the curtain, plaque, cabinet displacement, vapor and approach floor only.
- Do **not** generate the Distortion Den, mirror maze, Dr. Vanek, Green Fairy Wisp, floating chalice, Taproom bar, brewery stamp or signature beer as Arcade assets.
- Fade or transition immediately behind the curtain before any destination interior is visible.

### Claw Machine Maintenance Closet Restroom

- Destination: `debaucheryville_arcade_maintenance_closet_01`.
- Destination authority: `design/worlds/debaucheryville/clawmachinemaintenanceclosetrestroom.md`.
- Arcade-visible entrance: east service recess of the north wing beside the broken DDR machine.
- Required visual cues: three dark token pips that light green one at a time, hacked coin slot, exposed wire bridge, dented steel door, smudged `MAINTENANCE ONLY` label, `XXX PAC-MAN: THE DIRECTOR'S CUT` sticker and red/green latch indicator.
- Generate the DDR machine, token progress states, door exterior and unlock FX only.
- Do **not** generate the toilet/dance pad, graffiti, claw-arm chandelier, CRT mirror, prize-chute towel dispenser, foot-soak bucket or any other restroom interior prop as Arcade assets.
- The door reveals no interior; transition immediately after it opens.

## Delivery Structure

```text
assets/sprites/locations/debaucheryville/absinthe_arcade/
├── exterior/
│   ├── faces/
│   ├── depth_layers/
│   ├── props/
│   ├── surfaces/
│   └── fx/
├── interior/
│   ├── faces/
│   ├── depth_layers/
│   ├── cabinets/
│   ├── props/
│   ├── transitions/
│   └── fx/
├── characters/
├── ui/
├── masks/
└── source/
```

## Exterior Building Faces

Painted faces use strict orthographic elevation art so they map onto simple boxes without perspective distortion. Day and night are registered swap textures, not cross-fades. Emission masks align exactly to their matching night textures.

| Asset ID | Filename | Recommended size | States | Notes |
|---|---|---:|---|---|
| `aa_face_front` | `aa_face_front_day.png`, `aa_face_front_night.png`, `aa_face_front_emit.png` | 1024×1792 | Day/night/emit | Existing hero face; bottom-anchored and registration locked |
| `aa_face_left` | `aa_face_left_day.png`, `aa_face_left_night.png`, `aa_face_left_emit.png` | Match front storey scale | Day/night/emit | Includes angled corner-bay continuation |
| `aa_face_right` | `aa_face_right_day.png`, `aa_face_right_night.png`, `aa_face_right_emit.png` | Match front storey scale | Day/night/emit | No invented neighboring cafe architecture |
| `aa_face_back` | `aa_face_back_day.png`, `aa_face_back_night.png`, `aa_face_back_emit.png` | Match front storey scale | Day/night/emit | Service-facing historic shell; lower brand density |
| `aa_roof_mansard` | `aa_roof_mansard_day.png`, `aa_roof_mansard_night.png`, `aa_roof_mansard_emit.png` | 2048×1024 | Day/night/emit | Slate slopes, dormers, chimneys and iron cresting |

### Exterior depth layers

| Asset ID | Filename pattern | Purpose |
|---|---|---|
| `aa_layer_marquee` | `aa_layer_marquee_{day,night,emit}.png` | Sign housing, dimensional letters, token and invader marks |
| `aa_layer_keystone_head` | `aa_layer_keystone_head_{day,night,emit}.png` | Headphone Gentleman, ear cups and green tubes |
| `aa_layer_entrance_interior` | `aa_layer_entrance_interior_{day,night}.png` | Shallow interior glimpse through stained-glass doors |
| `aa_layer_awning` | `aa_layer_awning_{day,night}.png` | Corrugated cover, brackets, wires and warm bulbs |

Depth layers must include clean alpha, bottom/attachment pivots, and enough edge padding for mipmaps. Do not bake cast shadows that belong on a different surface into alpha edges.

### Exterior cutout props

| Asset ID | Filename pattern | Pivot | States |
|---|---|---|---|
| `aa_prop_street_cabinet` | `aa_prop_street_cabinet_{day,night,emit}.png` | Bottom center | Screen and marquee states |
| `aa_prop_chalkboard` | `aa_prop_chalkboard_{day,night}.png` | Bottom center | `REAL ARCADE / REAL ABSINTHE / REAL BAD DECISIONS` |
| `aa_prop_wall_sign_tokens` | `aa_prop_wall_sign_tokens_{day,night,emit}.png` | Bracket attachment | `TOKENS / DRINKS / GAMES / REGRETS` |
| `aa_prop_hanging_sign_clocktower` | `aa_prop_hanging_sign_clocktower_{day,night,emit}.png` | Bracket attachment | Clocktower Plaza sign and lantern |
| `aa_prop_wall_lantern` | `aa_prop_wall_lantern_{day,night,emit}.png` | Wall attachment | Warm orange practical |
| `aa_prop_bollard` | `aa_prop_bollard_day.png` | Bottom center | Reusable street line |
| `aa_prop_planter` | `aa_prop_planter_{day,night}.png` | Bottom center | Terracotta and green shrub variants |
| `aa_prop_metal_bucket` | `aa_prop_metal_bucket_day.png` | Bottom center | Beside exterior cabinet |
| `aa_prop_window_cat` | `aa_prop_window_cat_{day,night}.png` | Sill contact | Canonical black cat; subtle idle only |
| `aa_prop_club_flyer` | `aa_prop_club_flyer.png` | Poster center | State overlay after `club_flyer_placed` |

### Exterior repeatable surfaces

- `aa_tile_limestone_wall.png`
- `aa_tile_slate_roof.png`
- `aa_tile_cobblestone_dry.png`
- `aa_tile_cobblestone_wet.png`
- `aa_tile_curb_gutter.png`
- `aa_overlay_cobble_neon_reflection.png`

These are support textures, not replacements for the unique facade.

## Interior Room Faces

The interior uses a small number of painted room faces mapped to simple shell geometry. Keep spatial lighting broad and stable in the painted face; local quest lights, emission and particles remain separate.

| Asset ID | Filename | Recommended size | Content |
|---|---|---:|---|
| `aa_int_face_floor` | `aa_int_face_floor_day.png`, `aa_int_face_floor_night.png`, `aa_int_face_floor_emit.png` | 2048×2048 | Checkerboard field, wear, brass inlays, restrained green/purple pixels |
| `aa_int_face_walls` | `aa_int_face_walls_day.png`, `aa_int_face_walls_night.png`, `aa_int_face_walls_emit.png` | 2048×2048 atlas | Cream stone/plaster bays, arches, cabinet-wall zones, conduit attachment points |
| `aa_int_face_ceiling` | `aa_int_face_ceiling_day.png`, `aa_int_face_ceiling_night.png`, `aa_int_face_ceiling_emit.png` | 2048×1024 | Historic painted vaults, pendant anchors, bottle-tower opening |
| `aa_int_face_north_wing` | `aa_int_face_north_wing_day.png`, `aa_int_face_north_wing_night.png`, `aa_int_face_north_wing_emit.png` | 2048×1024 | Denser cabinet backdrop and two visually separate hidden-entry recesses |

### Interior depth layers

| Asset ID | Filename pattern | Content and requirements |
|---|---|---|
| `aa_int_layer_bottle_bar` | `aa_int_layer_bottle_bar_{day,night,emit}.png` | Circular bar, monumental green glass bottle, controlled internal crack, brass rail, bottle shelving |
| `aa_int_layer_mezzanine` | `aa_int_layer_mezzanine_{day,night}.png` | Iron rail, balcony edge and visual-only ambient figures |
| `aa_int_layer_entry_doors` | `aa_int_layer_entry_doors_{day,night,emit}.png` | Interior view of stained-glass entry and threshold |
| `aa_int_layer_claw_alcove` | `aa_int_layer_claw_alcove_{day,night,emit}.png` | Prize arch and readable machine silhouette |
| `aa_int_layer_mirror_corridor` | `aa_int_layer_mirror_corridor_{day,night,emit}.png` | Pilasters, mirror cards and purple route markers |
| `aa_int_layer_north_arch` | `aa_int_layer_north_arch_{day,night,emit}.png` | Framing arch that compresses the route into the north wing |

The bottle bar is the dominant interior mass and must remain readable from the vestibule, token exchange, main cabinet loop and start of the north wing.

## Cabinet and Interactive Prop Package

### Hero cabinets

| Asset ID | Filename | Required states |
|---|---|---|
| `aa_cab_frogger_existential` | `aa_cab_frogger_existential.png` | Idle, attract, active, win, failure, screen-off |
| `aa_cab_identity_crisis` | `aa_cab_identity_crisis.png` | Idle, fighter-select, input-remap, active, win, failure |
| `aa_cab_kebab_kombat` | `aa_cab_kebab_kombat.png` | Idle, REGRET pulse, sauce-danger, perfect hit, coupon dispense |
| `aa_cab_claw_rigged` | `aa_cab_claw_rigged.png` | Idle, sea-monkeys-present, play, near-miss, win, sea-monkeys-absent, shake-warning |
| `aa_cab_ddr_broken` | `aa_cab_ddr_broken.png` | Idle error, 0/3, 1/3, 2/3, 3/3 token pips, unlock pulse |
| `aa_cab_time_crisis_cracked` | `aa_cab_time_crisis_cracked.png` | Curtain-hidden, displaced/revealed, green-glow night state |

Cabinet bodies may use low-complexity 3D boxes with painted side/front cards. Screens, marquees, buttons and quest-state overlays remain separate so state changes do not require replacing the full cabinet.

### Generic cabinet kit

- `aa_cab_generic_upright_a.png`
- `aa_cab_generic_upright_b.png`
- `aa_cab_generic_cocktail.png`
- `aa_cab_generic_broken.png`
- `aa_cab_screen_attract_atlas.png`
- `aa_cab_marquee_atlas.png`
- `aa_cab_sticker_overlay_atlas.png`

Generic machines support the room rhythm; they must not compete with quest cabinets.

### Interior service and furniture props

| Asset ID | Filename | Notes |
|---|---|---|
| `aa_prop_token_exchange` | `aa_prop_token_exchange.png` | Idle, pay, dispense and jam screen states |
| `aa_prop_token_price_board` | `aa_prop_token_price_board.png` | Legible `1 SOV = 1 TOKEN` (author ruling 2026-11-02) |
| `aa_prop_prize_counter` | `aa_prop_prize_counter.png` | Sincere PRIZES sign, cheap stock, clear claw sightline |
| `aa_prop_bar_seating` | `aa_prop_bar_seating.png` | Normal stools plus highchair, beanbag and one discoverable bidet stool |
| `aa_prop_standing_tables` | `aa_prop_standing_tables.png` | Brass/wood tables, branded coasters, clear walkable footprint |
| `aa_prop_wayfinding` | `aa_prop_wayfinding.png` | Tokens, bar, prizes, restroom and circular fake-VIP arrows |
| `aa_prop_floor_clutter` | `aa_prop_floor_clutter.png` | Tokens, receipts, flyers, bottle caps, gum and damp footprints |

## Hidden-Entrance Asset Sets

### Arcade-side Taproom set

| Asset ID | Filename | States |
|---|---|---|
| `aa_transition_taproom_curtain` | `aa_transition_taproom_curtain.png` | Day/inert, evening/faint, night/breathing, discovered highlight |
| `aa_transition_taproom_plaque` | `aa_transition_taproom_plaque.png` | Brass warning plaque, clean readable text |
| `aa_transition_taproom_vapor` | `aa_transition_taproom_vapor.png` | 8-frame localized loop plus low-motion still |
| `aa_transition_taproom_glow` | `aa_transition_taproom_glow.png` | Emission-only breathing strip |

Every Taproom entrance contact sheet must show the cracked Time Crisis cabinet, curtain, plaque and vapor together in the north-wing west recess. It must not show any destination interior.

### Arcade-side maintenance-restroom set

| Asset ID | Filename | States |
|---|---|---|
| `aa_transition_maintenance_door` | `aa_transition_maintenance_door.png` | Locked red, unlocked green, opening exterior-only |
| `aa_transition_ddr_token_pips` | `aa_transition_ddr_token_pips.png` | 0/3, 1/3, 2/3 and 3/3 |
| `aa_transition_ddr_wire_bridge` | `aa_transition_ddr_wire_bridge.png` | Hacked slot, exposed cable and latch connection |
| `aa_transition_maintenance_labels` | `aa_transition_maintenance_labels.png` | `MAINTENANCE ONLY`, warning stickers and promo sticker |
| `aa_transition_maintenance_unlock_fx` | `aa_transition_maintenance_unlock_fx.png` | 6-frame green latch pulse |

Every maintenance entrance contact sheet must show the broken DDR machine immediately beside the door. It must not show through the doorway.

## Character Assets

| Asset ID | Filename | Required poses/loops |
|---|---|---|
| `aa_char_backpack_girl` | `backpack_girl_arcade.png` | Strum (4), scribble (2), tune (2), kebab offer (2), head tilt (2), stand-and-go (3) |
| `aa_char_arcade_employee` | `arcade_employee.png` | Idle, flyer squint, claw-win double take (machine-reset job moved to the Token Attendant, round v26) |
| `aa_char_token_attendant` | `token_attendant.png` | Count, price-board tap, machine fixing (jog-to-machine, left-side smack, machine reset), mopping, sleeping on the Green Fairy statue (public restroom), fake-VIP circle point |
| `aa_char_hacker_variants` | `arcade_hacker_patron_variants.png` | Three silhouettes with idle, type and hint gesture |
| `aa_char_edm_ghost_variants` | `edm_ghost_variants.png` | Two translucent silhouettes with restrained dance loops |
| `aa_char_rogue_backpackers` | `rogue_backpacker_variants.png` | Four distinct travelers, seated/standing/chat variants |
| `aa_char_speedrunners` | `arcade_speedrunner_variants.png` | Two variants with timer check and DDR/door-point gestures |

Backpack Girl's backpack is her primary silhouette. Leave clear space around her ukulele, notebook and offered kebab. She is exactly where she intends to be; do not make her look pitiable.

## Effects and Animation Atlases

| Asset ID | Filename | Specification |
|---|---|---|
| `aa_fx_cabinet_mist` | `aa_fx_cabinet_mist.png` | 8-frame green mist loop, localized and low to floor |
| `aa_fx_electrical_sparks` | `aa_fx_electrical_sparks.png` | Rare 4-frame bursts with anticipation blink |
| `aa_fx_digital_artifacts` | `aa_fx_digital_artifacts.png` | Small scanline/pixel cards; never full-screen by default |
| `aa_fx_mirror_afterimages` | `aa_fx_mirror_afterimages.png` | Character-neutral delayed silhouettes plus static accessibility frame |
| `aa_fx_floor_pixels` | `aa_fx_floor_pixels.png` | Random pulse and steady-lit accessibility variants |
| `aa_fx_bottle_bar_glow` | `aa_fx_bottle_bar_glow.png` | Slow internal bottle pulse and controlled crack emission |
| `aa_fx_neon_signage` | `aa_fx_neon_signage.png` | 4–6 frame flickers for marquee and wayfinding |
| `aa_fx_wet_reflections` | `aa_fx_wet_reflections.png` | Exterior green/purple/amber reflection overlays |

Effects must not conceal walkable edges, cabinet controls, token pips, the brass Taproom plaque or the maintenance door handle.

## UI Assets

| Asset ID | Filename | Contents |
|---|---|---|
| `aa_ui_tokens` | `aa_ui_tokens.png` | Token icon, balance counter, insert animation and insufficient-token state |
| `aa_ui_claw` | `aa_ui_claw.png` | Aim, sway, release, shake meter, strategy clue and Sea-Monkeys result |
| `aa_ui_cabinet_games` | `aa_ui_cabinet_games.png` | Shared score frame plus game-specific meters |
| `aa_ui_hidden_entrances` | `aa_ui_hidden_entrances.png` | Restroom wrench, Taproom coupe, discovered/locked states |
| `aa_ui_item_icons` | `aa_ui_item_icons.png` | Beer Pong Saint, broken handheld, Ballad page and kebab coupon |
| `aa_ui_dialogue_portraits` | `aa_ui_dialogue_portraits.png` | Backpack Girl, employee and attendant expressions |

UI must never depend on green versus purple alone. Pair every state with shape, icon, label or fill-count changes.

## Technical Masks and Guides

| Asset ID | Filename | Requirement |
|---|---|---|
| `aa_mask_exterior_collision` | `aa_mask_exterior_collision.png` | Match exterior footprint and props |
| `aa_mask_exterior_occlusion` | `aa_mask_exterior_occlusion.png` | Awning, door leaves, signs and foreground plant overlaps |
| `aa_mask_interior_collision` | `aa_mask_interior_collision.png` | Shell, bar, cabinets, furniture and service recess boundaries |
| `aa_mask_interior_interaction` | `aa_mask_interior_interaction.png` | Token machine, games, claw, mirror switches, curtain, DDR and door |
| `aa_mask_interior_occlusion` | `aa_mask_interior_occlusion.png` | Bar rail, cabinet tops, arches and selected foreground furniture |
| `aa_guide_node_overlay` | `aa_guide_node_overlay.png` | Labels every `aa_node_*` landmark over the approved interior image |
| `aa_guide_scale_camera` | `aa_guide_scale_camera.png` | Player scale, camera crop, walkable lanes and sightlines |

Collision and interaction masks are authored manually after composition approval. Do not generate them as decorative art.

## Required Composition Boards

Before individual interior assets are accepted, create these review images:

1. `aa_board_exterior_canon.png` — facade, palette, materials, mural, Headphone Gentleman, signage and street props.
2. `aa_board_interior_main_hall.png` — vestibule, token exchange, Backpack Girl, bottle bar, cabinet loop and claw alcove in one coherent view.
3. `aa_board_interior_north_wing.png` — mirror corridor entrance, Time Crisis/Taproom west recess and DDR/maintenance east recess.
4. `aa_board_hidden_entrance_states.png` — Taproom inert/night/discovered and maintenance 0/3 through unlocked.
5. `aa_board_game_scale_contact.png` — every prop and character at gameplay scale on checkerboard/cobble reference planes.

### Main-hall image prompt brief

Create a painterly HD-2D game-environment view of the Absinthe Arcade interior in a fixed elevated perspective. Show a grand historic Central European amusement hall with cream carved stone arches, iron mezzanine rails, warm amber pendant lamps, stained glass and a glossy black-and-white checkerboard floor. At the center, a circular brass-and-dark-wood bar wraps around a monumental cracked green absinthe bottle reservoir rising toward the ceiling. Readable arcade cabinet aisles loop around it. The green-and-purple arcade retrofit is tacky, physically attached and visibly newer than the architecture. Keep circulation clear. Include the token exchange and a small seated backpacker woman with an enormous backpack near the entry-side cabinets. The image should feel beautiful first and commercially corrupted second, not like a generic neon nightclub.

### North-wing image prompt brief

Create a matching painterly HD-2D game-environment view of the Absinthe Arcade's L-shaped north wing. The historic hall compresses into denser cabinet rows, lower amber lamps and localized green haze. On the west side, a cracked Time Crisis cabinet reveals a heavy glowing green velvet curtain with vapor curling underneath and a small brass warning plaque. On the east side, a broken DDR machine sits immediately beside a dented steel maintenance door with three token indicator pips, hacked wiring, a smudged MAINTENANCE ONLY label and an XXX PAC-MAN promo sticker. Make the two entrances visually distinct and readable. Show only their Arcade-facing approaches; do not show either destination interior.

## State and Accessibility Requirements

### Time states

- Day: architecture and mural dominate; neon is physically present but subdued.
- Evening: amber and neon balance; Taproom curtain begins a faint pulse after 20:00.
- Night: green/purple emission and wet reflections intensify, but amber navigation pools remain.
- Late night: reduced emission and crowd layers; no loss of interaction readability.

### Motion reduction

- Mirror lag becomes one static offset afterimage.
- Random floor pulses become steady-lit route tiles.
- Cabinet mist becomes low static haze.
- Glitch screens become a single scanline frame.
- Taproom breathing glow may become a steady rim light.

### Low-spec LOD

Remove in this order:

1. Tertiary clutter variants.
2. Extra ambient NPCs.
3. Digital artifact cards.
4. Secondary mist emitters.
5. Decorative screen animations.

Never remove quest NPCs, the bottle-bar silhouette, token pips, door indicators, Taproom curtain/plaque, claw Sea-Monkeys state or walkable-edge lighting.

## Naming and Export Rules

- Lowercase snake case for filenames.
- `aa_face_*` for painted shell faces.
- `aa_layer_*` and `aa_int_layer_*` for depth cards.
- `aa_prop_*` and `aa_cab_*` for cutout props and cabinets.
- `aa_transition_*` for Arcade-side hidden-location entrances.
- `aa_char_*`, `aa_fx_*`, `aa_ui_*`, `aa_mask_*` and `aa_guide_*` for their respective groups.
- Color textures are sRGB; masks, normals and roughness are linear/non-color.
- Use straight alpha with clean edge colors and at least 8 px transparent padding at source scale.
- Bottom-center pivots for floor props and characters; attachment pivots for wall/ceiling pieces.
- Day/night swap textures must share canvas, pivot and registration.
- Emission files are black except for emissive pixels and must align 1:1 with the matching color texture.
- Preserve layered source files in `source/`; exported PNGs contain no guides or notes.

## Delivery Checklist

- [ ] Exterior front face day/night/emit remains registered and canon-accurate.
- [ ] Left, right, back and roof faces match the approved front-face scale.
- [ ] Headphone Gentleman, marquee, mural and window cat remain canonical.
- [ ] Main-hall board establishes a navigable loop around the bottle bar.
- [ ] North-wing board shows both hidden entrances in their correct recesses.
- [ ] Taproom entrance names `debaucheryville_brewery_absinthium_taproom_01` and shows no Taproom interior.
- [ ] Maintenance entrance names `debaucheryville_arcade_maintenance_closet_01`, shows 0/3–3/3 states and shows no restroom interior.
- [ ] Backpack Girl reads as small person plus enormous backpack at gameplay scale.
- [ ] Sea-Monkeys (Mint #73) is visible in the claw machine before acquisition and absent afterward.
- [ ] Fake VIP wayfinding loops back to the public bar; no real VIP room is created.
- [ ] Every interaction has a visible non-color-only state cue.
- [ ] Collision, interaction and occlusion masks match approved compositions.
- [ ] High, low and motion-reduction contact sheets are reviewed at game scale.
- [ ] Godot 4.7 import uses linear filtering and mipmaps appropriate to painterly HD-2D.

## Final Art Rule

The venue should look like a genuinely magnificent old building that survived history only to become an aggressively branded tourist barcade. If the architecture looks cheap, the joke fails. If the neon is removed and the building still reads as specific and beautiful, the straight-man layer is working. If the two hidden entrances can be identified immediately without seeing beyond them, the interior-image package is ready for implementation.

---

## Legacy sprite-sheet detail (folded in 2026-11-12, Eurobound-x0c; HD-2D sheet above is the spec of record)

> Folded in verbatim from the earlier four-sheet pixel-art spec that sat at this path in `design/worlds/` (the HD-2D sheet above came from `design/World Design/`). Where anything in this section contradicts the HD-2D sheet above, the HD-2D sheet wins.

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Absinthe Arcade location. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this psychedelic corrupted barcade where childhood nostalgia meets bad trip aesthetics.

**Location ID:** `debaucheryville_clocktower_arcade_01`  
**Theme:** Dave & Buster's if it was haunted by your bad trip  
**Zone:** Clocktower Plaza (side street beneath a green-lit arch)  
**Hours:** Always accessible; lighting effects change dramatically after 10 PM  
**Primary Function:** NFT Hunt location, Brewery Tour entrance, Couchsurfing host, Parody arcade minigames

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Toxic Green | #39FF14 | Dominant glow — floor tiles, screen glow, absinthe bar, mist |
| UV Fairy Green | #00FF41 | UV reactive surfaces, Green Fairy mural form |
| Neon Purple | #BF00FF | Accent elements, circuit corruption patterns |
| Deep Black | #0A0A0A | Background voids, ceiling, unlit surfaces |
| Cabinet Pink | #FF1493 | Arcade cabinet bodies |
| Neon Pink | #FF69B4 | Environmental neon accents |
| Cyan | #00FFFF | Cabinet screens, mist tint, glitch artifacts |
| Cabinet Wood Grain | #8B4513 | Cabinet trim, worn wood surfaces |
| Token Gold | #FFD700 | Tokens, exchange machine highlights |
| Spark Yellow | #FFFF00 | Electrical spark tint |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/absinthe_arcade/
├── environment/
│   ├── absinthe_arcade_tileset.png
│   └── green_fairy_mural_parallax.png
├── objects/
│   └── arcade_machines_spritesheet.png
└── effects/
    └── environmental_effects.png
```

---

## 🎨 Sprite Sheet 1: Absinthe Arcade Tileset
**File:** `absinthe_arcade_tileset.png`  
**Dimensions:** 1024x1024 pixels  
**Color Palette:** #39FF14 (toxic green), #BF00FF (neon purple), #0A0A0A (deep black), #00FF41 (UV reactive green)

### Floor Tiles (32x32 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Standard Floor | (0, 0) | 32x32 | Base tile, dark with subtle texture |
| Light-Up Tile Off | (32, 0) | 32x32 | Inactive state, dim surface |
| Light-Up Tile Frame 1 | (64, 0) | 32x32 | Dim glow beginning |
| Light-Up Tile Frame 2 | (96, 0) | 32x32 | Medium brightness |
| Light-Up Tile Frame 3 | (128, 0) | 32x32 | Peak brightness, full toxic green |
| Light-Up Tile Flicker | (160, 0) | 32x32 | Malfunction state, erratic glow |
| Cracked Floor Variation 1 | (192, 0) | 32x32 | Visible damage, minor cracks |
| Cracked Floor Variation 2 | (224, 0) | 32x32 | Heavy wear, deep cracks |
| Green Glow Floor | (256, 0) | 32x32 | UV reactive permanent glow tile |

### Wall Tiles (64x64 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Blacklight Wall Base | (0, 32) | 64x64 | Standard blacklight wash surface |
| Mirror Wall Normal | (64, 32) | 64x64 | Reflective surface, clean |
| Mirror Wall Lagged | (128, 32) | 64x64 | 0.2s reflection delay state visual |
| Cracked Wall Light | (192, 32) | 64x64 | Minor structural damage |
| Cracked Wall Heavy | (256, 32) | 64x64 | Significant arcade decay |
| Circuit Pattern Wall | (320, 32) | 64x64 | Green Fairy mural integration pattern |

### Ceiling Tiles (48x48 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Standard Ceiling | (0, 96) | 48x48 | Dark overhead surface |
| Exposed Wiring | (48, 96) | 48x48 | Electrical hazard visible |
| Flickering Light Source | (96, 96) | 48x48 | Unstable illumination fixture |
| Green Glow Wash | (144, 96) | 48x48 | Toxic atmospheric tint overlay |

### Green Glow Overlay Effects (128x128 each):
| Effect Name | Position | Size | Description |
|-------------|----------|------|-------------|
| Subtle Glow | (384, 0) | 128x128 | Gentle toxic green wash |
| Medium Intensity | (512, 0) | 128x128 | Standard arcade glow level |
| Peak Intensity | (640, 0) | 128x128 | Overwhelming green effect |
| Pulsing Animation Frame 1 | (768, 0) | 128x128 | Breathing effect start |
| Pulsing Animation Frame 2 | (896, 0) | 128x128 | Breathing effect peak |

### Technical Notes - Tileset:
- Floor tiles use random activation pattern (0.5-3 second delays between tiles)
- Approximately 20% of light-up tiles active at any given time
- Mirror lag effect: 0.2-second delay on player reflection requires shader support
- Green glow overlays use additive blend mode for proper layering
- UV reactive materials respond to blacklight ambient lighting

---

## 🕹️ Sprite Sheet 2: Arcade Machines Spritesheet
**File:** `arcade_machines_spritesheet.png`  
**Dimensions:** 2048x1024 pixels  
**Color Palette:** #39FF14 (screen glow), #FF1493 (cabinet pink), #00FFFF (cyan screens), #8B4513 (cabinet wood grain)

### Frogger: Existential Edition Cabinet (128x192):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle State | (0, 0) | 128x192 | Standard cabinet with philosophical title |
| Active Playing | (128, 0) | 128x192 | Screen lit, existential obstacles visible |
| Broken Leaking Mist | (256, 0) | 128x192 | Cracked cabinet with green fog emission |
| Screen Content Frame 1 | (384, 0) | 64x48 | Philosophical obstacles on screen |
| Screen Content Frame 2 | (448, 0) | 64x48 | Existential traffic hazards |
| Screen Content Frame 3 | (512, 0) | 64x48 | Life questions as game obstacles |

### Street Fighter: Identity Crisis Cabinet (128x192):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle State | (0, 192) | 128x192 | Cabinet with identity confusion theme |
| Active Mid-Combo | (128, 192) | 128x192 | Characters questioning their moves |
| Broken State | (256, 192) | 128x192 | Damaged, identity completely lost |
| Screen Identity Question 1 | (384, 192) | 64x48 | "Who am I hitting?" text |
| Screen Identity Question 2 | (448, 192) | 64x48 | Character self-doubt animation |
| Screen Identity Question 3 | (512, 192) | 64x48 | Move confusion visual |

### Kebab Kombat Cabinet (128x192):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle State | (0, 384) | 128x192 | Fighting game aesthetic cabinet |
| Active Regret Button | (128, 384) | 128x192 | Single REGRET button glowing |
| Broken State | (256, 384) | 128x192 | Leaking mystery meat vapor |
| Regret Button Glow Dim | (384, 384) | 64x64 | Button in dim state |
| Regret Button Glow Bright | (448, 384) | 64x64 | Button at peak brightness |
| Regret Button Pressed | (512, 384) | 64x64 | Active press state, depressed |

### Rigged Absinthe Arcade Claw Machine (256x384):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle Operating | (576, 0) | 256x384 | Standard claw machine front view |
| Claw Moving | (832, 0) | 256x384 | Rigged physics in action |
| Dispensing NFT | (1088, 0) | 256x384 | Sea-Monkeys (Mint #73) dropping |
| NFT Prize Inside | (576, 384) | 64x64 | Sea-Monkeys (Mint #73) visible; artwork PROPOSED — NEEDS AUTHOR RULING |
| Claw Mechanism Open | (640, 384) | 48x64 | Claw in open position |
| Claw Mechanism Closing | (688, 384) | 48x64 | Claw closing on prize |
| Rigged Physics Visual | (736, 384) | 96x96 | Obviously unfair grab animation |

### Broken DDR Machine (192x256):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Cabinet Base | (1344, 0) | 192x256 | Dance Dance Revolution full setup |
| Broken Pad | (1536, 0) | 96x128 | Non-functional dance surface |
| Token Slot | (1632, 0) | 64x96 | 3-token unlock mechanism slot |
| Token Insert 1/3 | (1696, 0) | 64x32 | First token progress indicator |
| Token Insert 2/3 | (1760, 0) | 64x32 | Second token progress indicator |
| Token Insert 3/3 | (1824, 0) | 64x32 | Third token, unlock complete glow |

### Cracked Time Crisis Machine - Hidden Entrance (192x256):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Cabinet Closed | (1344, 256) | 192x256 | Normal damaged cabinet, concealing passage |
| Cabinet Opening | (1536, 256) | 192x256 | Swinging aside, revealing passage |
| Hidden Passage Visible | (1728, 256) | 192x256 | Absinthium Taproom access revealed |
| Secret Entrance Glow | (1920, 256) | 64x96 | Discovery indicator green glow |

### Universal Cabinet Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Green Mist Particle | (1920, 352) | 32x32 | Leaking from damaged machines |
| Electrical Spark | (1952, 352) | 24x24 | Random cabinet malfunction spark |
| Screen Flicker Effect | (1976, 352) | 48x48 | 2-second interval glitch overlay |

### Technical Notes - Arcade Machines:
- All cabinets designed for front-facing oblique EarthBound perspective
- Screen content loops independently from cabinet state
- Claw machine physics deliberately shows unfairness for comedy
- Green mist particles spawn from seams of "broken" cabinets
- DDR token slot should show visible progress with each token inserted

---

## 🧚 Sprite Sheet 3: Green Fairy Mural Parallax
**File:** `green_fairy_mural_parallax.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #00FF41 (fairy green), #BF00FF (circuit purple), #39FF14 (toxic glow), #0A0A0A (background black)

### Layer 1 - Circuit Board Background (Furthest - 0.1x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Circuit Pattern Base | (0, 0) | 512x256 | Deep background technology pattern |
| Circuit Glow Points | (512, 0) | 512x256 | Pulsing connection nodes overlay |

### Layer 2 - Fairy Silhouette (Middle-Far - 0.3x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fairy Form Solid | (0, 256) | 256x256 | Green Fairy iconic shape, intact |
| Fairy Form Dissolving | (256, 256) | 256x256 | Beginning melt/corruption effect |
| Fairy Form Melted | (512, 256) | 256x256 | Heavy digital corruption state |

### Layer 3 - Melting Effect (Middle-Near - 0.5x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Drip Frame 1 | (768, 0) | 256x128 | Initial melt, drips forming |
| Drip Frame 2 | (768, 128) | 256x128 | Progressive melting |
| Drip Frame 3 | (768, 256) | 256x128 | Advanced decay state |
| Drip Frame 4 | (768, 384) | 256x128 | Near-complete melt |

### Layer 4 - Circuit Overlay (Nearest - 0.7x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Circuit Overlay Active | (0, 512) | 512x256 | Foreground tech corruption lines |
| Circuit Overlay Pulsing 1 | (512, 512) | 256x128 | Pulse animation frame 1 |
| Circuit Overlay Pulsing 2 | (768, 512) | 256x128 | Pulse animation frame 2, peak |

### Parallax Movement Specifications:
| Layer | Scroll Speed | Purpose |
|-------|--------------|---------|
| Layer 1 (Circuit Background) | 0.1x player speed | Deep background, barely moves |
| Layer 2 (Fairy Silhouette) | 0.3x player speed | Mid-ground focal point |
| Layer 3 (Melting Effect) | 0.5x player speed | Near-ground dynamic element |
| Layer 4 (Circuit Overlay) | 0.7x player speed | Foreground framing |

### Animation Timing:
| Animation | Frames | FPS | Duration | Loop |
|-----------|--------|-----|----------|------|
| Melting Effect | 4 | 1.33 | 3 seconds | Yes |
| Circuit Pulse | 2 | 1.33 | 1.5 seconds | Yes |
| Fairy Dissolve | 3 | 0.5 | 6 seconds | Yes (gradual) |

### Technical Notes - Parallax:
- Use ParallaxBackground node in Godot 4.x
- Each layer should be separate texture for proper scroll
- Fairy dissolve is gradual transformation, not abrupt switch
- Circuit overlay uses additive blend for glow effect
Low-spec: Can reduce to 2 layers on min-spec hardware

---

## 🍾 Sprite Sheet 4: Environmental Effects
**File:** `environmental_effects.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #39FF14 (absinthe glow), #FF69B4 (neon pink), #00FFFF (cyan mist), #FFD700 (token gold)

### Absinthe Bottle Bar System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bottle Bar Base | (0, 0) | 256x128 | Cracked bottle shape structure |
| Glow Animation Frame 1 | (256, 0) | 256x128 | Dim internal glow |
| Glow Animation Frame 2 | (512, 0) | 256x128 | Medium brightness |
| Glow Animation Frame 3 | (768, 0) | 256x128 | Peak toxic green intensity |
| Glow Animation Frame 4 | (0, 128) | 256x128 | Pulsing descent |

**Bar Glow Animation:** 4-frame pulse, 3 seconds total, continuous loop

### Mismatched Bar Seating:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Highchair Seat | (256, 128) | 64x96 | Absurdly inappropriate child's highchair |
| Beanbag Seat | (320, 128) | 64x64 | Collapsed gaming furniture, deflated |
| Bidet Seat | (384, 128) | 64x96 | The infamous bathroom fixture stool |
| Normal Stool | (448, 128) | 48x72 | Only one "normal" option, ironic |

### Token Exchange Machine:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Machine Idle | (0, 224) | 128x192 | Ready for overpriced exchange |
| Machine Active | (128, 224) | 128x192 | Processing transaction animation |
| Machine Dispensing | (256, 224) | 128x192 | Tokens falling out animation |
| Screen Display (1KC=5T) | (384, 224) | 96x48 | Overpriced conversion rate visible |
| Token Slot Detail | (480, 224) | 48x64 | Kebab coin insertion point |

### Particle Systems:

#### Green Mist (From Cabinets):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mist Wisp 1 | (0, 416) | 32x32 | Light fog particle, translucent |
| Mist Wisp 2 | (32, 416) | 32x32 | Medium density wisp |
| Mist Wisp 3 | (64, 416) | 32x32 | Dense fog particle |
| Mist Wisp 4 | (96, 416) | 32x32 | Dissipating wisp |

**Mist Animation:** 4 frames, 0.3s per frame, additive blend, upward drift

#### Electrical Sparks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spark Frame 1 | (128, 416) | 16x16 | Initial spark burst |
| Spark Frame 2 | (144, 416) | 16x16 | Peak brightness |
| Spark Frame 3 | (160, 416) | 16x16 | Fading arc |

**Spark Animation:** 3 frames, 0.1s per frame, yellow #FFFF00 tint

#### Digital Artifacts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glitch Fragment 1 | (176, 416) | 24x24 | Cyan pixelated fragment |
| Glitch Fragment 2 | (200, 416) | 24x24 | Magenta glitch piece |
| Glitch Fragment 3 | (224, 416) | 24x24 | Yellow digital debris |
| Screen Tear Effect | (272, 416) | 48x32 | Visual distortion |

**Glitch Animation:** 3 frames, 0.4s per frame, random drift movement

### Particle Emission Rates:
- **Green Mist:** 3 particles/second from damaged cabinets
- **Electrical Sparks:** Random 1-4 second intervals
- **Digital Artifacts:** Continuous low-density atmospheric effect

### UI Elements (Location-Specific):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Token Counter Background | (0, 448) | 128x32 | HUD element for token count |
| Token Icon | (128, 448) | 16x16 | Single token sprite for counter |
| Score Display | (0, 480) | 96x24 | Arcade game score readout |
| Game Over Overlay | (96, 480) | 128x32 | Failure state overlay |
| Examine Prompt | (224, 480) | 64x24 | "Examine" interaction button |
| Play Prompt | (288, 480) | 64x24 | "Play" interaction button |
| Insert Token Prompt | (352, 480) | 96x24 | "Insert Token" prompt |

---

## 🎬 Animation Specifications

### Floor Tile Random Activation:
- **Duration:** Random 0.5-3 second delays per tile
- **Pattern:** Off → Dim (Frame 1) → Medium (Frame 2) → Bright (Frame 3) → Medium → Dim → Off
- **Coverage:** Approximately 20% of tiles active at any time
- **Purpose:** Disorienting atmosphere, creates "something's wrong" feeling
- **Performance Optimization:** Reduce active percentage to 10% on min-spec hardware

### Arcade Cabinet Screen Flicker:
- **Duration:** 2-second intervals between flicker events
- **Pattern:** Normal display → Glitch artifacts → Brief static → Return to normal
- **Consistency:** All cabinets flicker independently (random offset)
- **Purpose:** Arcade decay aesthetic, corrupted nostalgia theme
- **Audio Sync:** Brief analog distortion sound accompanies each flicker

### Green Fairy Mural Melting:
- **Duration:** 6-second gradual transformation cycle
- **Pattern:** Solid fairy → Dissolving edges → Circuit corruption visible → Reform to solid
- **Parallax:** All 4 layers move at different speeds during player movement
- **Purpose:** Psychedelic atmosphere, reality breakdown visualization
- **Performance Optimization:** Can use 2-layer simplified version

### Absinthe Bottle Bar Glow:
- **Duration:** 4-frame pulse, 3 seconds total cycle
- **Pattern:** Dim → Medium → Peak → Descent (smooth sine wave)
- **Continuous:** Never stops glowing while location is active
- **Purpose:** Toxic green atmosphere, bar centerpiece attention draw
- **Audio Sync:** Subtle hum increases with glow intensity

### Mirror Reflection Lag:
- **Duration:** 0.2-second delay on all player movement near mirrors
- **Pattern:** Player moves → Mirror reflection updates 0.2s later
- **Technical:** Duplicate player sprite with transform delay shader
- **Purpose:** Subtle wrongness feeling, reality distortion theme
- **Performance Optimization:** Disable on devices below medium settings

### Rigged Claw Machine Physics:
- **Duration:** Variable based on player input timing
- **Pattern:** Claw descends → Grabs prize → Lifts → Visibly weakens grip → Drops prize
- **Visual:** Claw obviously loosens when near success (comedy beat)
- **Purpose:** Satirical tourist trap mechanics, intentional frustration
- **Strategy:** After 5 failures, success probability increases slightly

---

## ♿ Accessibility Sprite Requirements

*(All accessibility sprites live in `environmental_effects.png` at the coordinates below.)*

### High Contrast Alternatives (Colorblind-Friendly):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Enhanced Floor Tiles | (528, 416) | 256x96 | High contrast for light-up patterns |
| Cabinet Screen Clarity | (784, 416) | 128x96 | Readable game content |
| Mural Visibility | (912, 416) | 112x96 | Pattern-based instead of color-only |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Mural Alternative | (544, 0) | 480x256 | Non-parallax Green Fairy |
| Reduced Flicker Lighting | (544, 256) | 256x128 | Gentle floor tile pulse |
| Minimal Particle Mode | (800, 256) | 224x128 | Essential mist only |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cabinet Sound Visual | (528, 384) | 32x32 | Audio indicator for deaf players |
| Token Machine Beep | (560, 384) | 32x24 | Transaction confirmation visual |
| Hidden Entrance Reveal | (592, 384) | 48x32 | Discovery cue without audio dependency |

### Colorblind Considerations:
- Light-up floor tiles, mural corruption, and DDR token progress all offer pattern/shape-based indicators wherever color codes meaning
- Click zones minimum 44px for interactive elements (cabinets, token machine, prompts)

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.7 import) for green glow effects, maintains toxic aesthetic with alpha for mist particle transparency
- **Fallback:** PNG high quality for mural parallax detail

### Sprite Atlasing Strategy:
- **Tileset Atlas:** Floor + walls + ceiling combined (1024x1024)
- **Arcade Machines Atlas:** All cabinets + claw machine (2048x1024)
- **Mural Parallax Atlas:** 4 layers separate for parallax effect (1024x512)
- **Environmental Effects Atlas:** Bar + seating + particles (1024x512)
- **Max Atlas Size:** 2048x2048 for broad GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full particle systems, parallax mural, mirror lag effect
- **Medium Devices:** Reduced particle density, simplified parallax (2 layers)
- **Low-End Devices:** Static mural, minimal particles, no mirror lag
- **Potato Mode:** Essential cabinets and bar only, no effects

### Performance Targets:
- **Target FPS:** 60 fps (psychedelic atmosphere requires smoothness)
- **Max Draw Calls:** 15 per frame
- **Memory Footprint:** 50MB maximum for location

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Parallax layers: Use ParallaxBackground and ParallaxLayer nodes
- Particle systems: CPUParticles2D for performance (not GPU particles)
- Mirror effect: Custom shader with position delay, or sprite duplication with offset
- Floor tile system: TileMap with animated tiles, random activation script

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Floor tile activation | Electronic beep | On glow start |
| Cabinet screen flicker | Analog distortion burst | On glitch frame |
| Claw machine NFT dispense | Remixed "Für Elise" | On prize drop |
| Token exchange complete | Metallic clink | On dispense animation |
| Hidden entrance reveal | Atmospheric drone swell | On passage open |
| Regret button press | Deep bass thump + sizzle | On button press |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| NFT Hunt | Claw machine, NFT prize sprite | Sea-Monkeys (Mint #73) acquisition |
| Brewery Tour | Cracked Time Crisis, hidden passage | Absinthium Taproom access |
| Couchsurf System | (NPC sprites separate) | Backpack Girl interaction |
| Sinfonia Prep | Hidden Game Boy (discoverable item) | Symbol puzzle preparation |
| Hidden Bathroom | DDR machine, token slot | 3-token unlock mechanic |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Absinthium Taproom | Time Crisis passage sprites | Green glow intensifies, fade transition |
| Claw Machine Maintenance Closet | DDR token progress sprites | Mechanical grinding, door reveal |
| Clocktower Plaza | (Exterior handled separately) | Arcade sounds fade, plaza ambience rises |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Corrupted childhood nostalgia meets psychedelic tourist trap"
- **Color Mood:** Toxic green dominance (#39FF14), neon purple accents (#BF00FF), deep black voids (#0A0A0A)
- **Lighting:** Blacklight wash with UV-reactive materials, flickering point sources, no natural light
- **Texture:** Cracked arcade surfaces, digital melting imagery, grimy yet glowing

### Arcade Cabinet Direction:
- **Parody Games:** Obvious twists on 80s/90s classics (Frogger, Street Fighter)
- **Visual Decay:** Green mist leaking from cabinet seams, cracked screens still functional
- **Screen Content:** Game parodies visible and recognizable, philosophical/absurd text readable
- **Nostalgic Corruption:** Familiar shapes made uncomfortable through color and decay

### Green Fairy Mural Philosophy:
- **Iconic Imagery:** Classic absinthe advertising fairy, recognizable silhouette
- **Digital Corruption:** Circuit board patterns eating into organic fairy form
- **Parallax Depth:** Creates sense of the mural being a portal, not flat surface
- **Melting Effect:** Suggests reality breakdown, absinthe hallucination aesthetic

### Environmental Storytelling:
- **Mismatched Seating:** Haphazard tourist trap setup (highchair, beanbag, bidet at bar)
- **Overpriced Exchange:** Token machine prominently displays unfair rates
- **Mirror Lag:** Subtle wrongness players notice subconsciously
- **Hidden Areas:** Reward exploration with discoverable passages

### Character Integration Notes:
- NPCs (Backpack Girl, Twitchy Hackers, EDM Ghosts) require separate sprite sheets
- NPC positions should account for bar seating, cabinet clustering, north wing depth
- EDM Ghosts should have translucent rendering with glow stick color accents

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Green Fairy Mural** - Psychedelic parallax melting effect, perfect for "trippy game" posts
2. **Bidet Bar Stool** - Absurd seating choice, guaranteed "WTF" reactions
3. **Kebab Kombat Cabinet** - Single "REGRET" button fighting game, meme-ready
4. **Mirror Lag Effect** - Reflection delay creates creepy video content
5. **Rigged Claw Machine** - Obviously unfair NFT grab, rage-bait comedy

### TikTok Potential:
- "Childhood arcade games reimagined wrong" (cabinet tour video)
- "When your reflection is late to the party" (mirror lag showcase)
- "The most cursed bar seating ever" (bidet stool reaction)
- "Found the absinthe arcade tourist trap" (location reveal)
- "POV: You're trying to win a fake NFT" (claw machine frustration)

### Twitter/X Quote Potential:
- "I got high and accidentally joined a DAO" (NPC dialogue)
- "This place accepted crypto before it was a currency… or a cult" (NPC dialogue)
- Every arcade parody game title is meme material
- "Lose Your Mind One Token at a Time" (location tagline)
- "The only button is REGRET" (Kebab Kombat description)

---

## 📋 Required PNG Files (4 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | absinthe_arcade_tileset.png | 1024x1024 |
| 2 | arcade_machines_spritesheet.png | 2048x1024 |
| 3 | green_fairy_mural_parallax.png | 1024x512 |
| 4 | environmental_effects.png | 1024x512 |

**Total Estimated Memory:** ~16 MB uncompressed RGBA (well within the 50MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files (4 Total):
- [ ] `absinthe_arcade_tileset.png` (1024x1024)
- [ ] `arcade_machines_spritesheet.png` (2048x1024)
- [ ] `green_fairy_mural_parallax.png` (1024x512)
- [ ] `environmental_effects.png` (1024x512)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve parallax layers separately in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/Photoshop file with organized layer groups
- **Documentation:** Animation timing reference sheet, parallax layer guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 4 PNG files match exact dimensions specified
- [ ] Floor tiles create believable disorienting random pattern when tiled
- [ ] Arcade cabinets show clear parody game content on screens
- [ ] Green Fairy mural has 4 distinct parallax layers with proper scroll speeds
- [ ] Mirror reflection lag is technically achievable with provided assets
- [ ] Claw machine NFT prize (Sea-Monkeys) is intentionally ugly
- [ ] Bidet bar stool is clearly identifiable and absurd
- [ ] Green glow maintains toxic aesthetic throughout all elements
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility visual alternatives included for audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Arcade parodies are instantly recognizable yet twisted
- [ ] Green Fairy mural creates genuine psychedelic depth
- [ ] Environmental effects support tourist trap atmosphere
- [ ] Hidden areas (bathroom entrance, brewery passage) have discoverable visual cues
- [ ] Nostalgic corruption theme is clear throughout all assets
- [ ] Performance optimized (particle systems use CPU, not GPU)
- [ ] All elements support "childhood corrupted" satire consistently
- [ ] Social media viral potential maximized in composition choices
- [ ] Click zone sizing considered for interactive elements (44px minimum)
- [ ] Colorblind-friendly alternatives available where color-coded

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ PASS | Debaucheryville only |
| Cultural Specificity | ✅ PASS | Debaucheryville absinthe/arcade culture |
| Satirical Targets Appropriate | ✅ PASS | Tourist behavior, not locals |
| Seedy Underbelly Present | ✅ PASS | Rigged games, overpriced tokens |
| Gameplay Value Established | ✅ PASS | NFT hunt, brewery access, minigames |
| Technical Feasibility | ✅ PASS | Desktop performance budget documented |
| Performance Budget | ✅ PASS | 60 FPS, 15 draw calls, 50MB |
| Accessibility Features | ✅ PASS | Visual audio cues included |
| No Crypto Elements | ✅ PASS | Sea-Monkeys NFT is satirical and established in source material; no functional crypto |
| Social Media Integration | ✅ PASS | Multiple viral moments identified |

**Once validated, the Absinthe Arcade becomes the psychedelic quest hub where players experience corrupted gaming nostalgia, meet Backpack Girl Who Never Left, obtain the Sea-Monkeys NFT from a rigged claw machine, discover hidden passages to the Absinthium Taproom and secret bathroom, and play parody arcade games while bros think they're experiencing sophisticated underground European culture!**
