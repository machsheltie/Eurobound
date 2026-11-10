# Absinthe Arcade — Complete PNG Asset Requirements

## Overview

| Field | Value |
|---|---|
| Location ID | `debaucheryville_clocktower_arcade_01` |
| Engine | Godot 4.7 (Forward+) |
| Production style | Painterly HD-2D painted-box diorama |
| Exterior | Historic Debaucheryville Old Town facade vandalized by a green-and-purple arcade retrofit |
| Interior | Grand adaptive-reuse amusement hall organized around a monumental cracked-bottle bar |
| Camera | Fixed HD-2D tilt, approximately 30–40° down, narrow perspective FOV |
| Target | 60 FPS with scalable particles, emission and crowd layers |

This document supersedes the earlier four-sheet, pure pixel-art package. The final direction is painterly HD-2D: simple 3D room/building massing receives painted orthographic face textures, important forms stand proud as alpha depth cards or low-complexity geometry, and props/characters use `Sprite3D` cutouts or billboards where appropriate.

The hero facade is one authored building identity. It is **not** a 32-bit tile sheet. Tiles remain appropriate only for repeatable cobble, checkerboard flooring, generic limestone, roof slate, puddles and small utility surfaces.

### Source authority

1. `Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_exterior/hd2d_asset_manifest.md`
2. `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/mastercomponentbreakdown.md`
3. `design/World Design/Debaucheryville/absinthearcade.md`
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
- Destination authority: `design/World Design/Debaucheryville/the_absinthium_taproom.md`.
- Arcade-visible entrance: the west recess of the north wing, partially revealed behind a cracked Time Crisis cabinet.
- Required visual cues: heavy glowing green velvet curtain, vapor curling underneath, small brass plaque reading `NOT RECOMMENDED FOR THOSE PRONE TO INTROSPECTION`, and slow breathing green rim light after 20:00.
- Generate the curtain, plaque, cabinet displacement, vapor and approach floor only.
- Do **not** generate the Distortion Den, mirror maze, Dr. Vanek, Green Fairy Wisp, floating chalice, Taproom bar, brewery stamp or signature beer as Arcade assets.
- Fade or transition immediately behind the curtain before any destination interior is visible.

### Claw Machine Maintenance Closet Restroom

- Destination: `debaucheryville_arcade_maintenance_closet_01`.
- Destination authority: `design/World Design/Debaucheryville/clawmachinemaintenanceclosetrestroom.md`.
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
| `aa_cab_claw_rigged` | `aa_cab_claw_rigged.png` | Idle, relic-present, play, near-miss, win, relic-absent, shake-warning |
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
| `aa_char_arcade_employee` | `arcade_employee.png` | Idle, remote click, reset, flyer squint, claw-win double take |
| `aa_char_token_attendant` | `token_attendant.png` | Count, price-board tap, glass polish, fake-VIP circle point |
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
| `aa_ui_claw` | `aa_ui_claw.png` | Aim, sway, release, shake meter, strategy clue and relic result |
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

Never remove quest NPCs, the bottle-bar silhouette, token pips, door indicators, Taproom curtain/plaque, claw relic state or walkable-edge lighting.

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
- [ ] Beer Pong Saint Relic is visible in the claw machine before acquisition and absent afterward.
- [ ] Fake VIP wayfinding loops back to the public bar; no real VIP room is created.
- [ ] Every interaction has a visible non-color-only state cue.
- [ ] Collision, interaction and occlusion masks match approved compositions.
- [ ] High, low and motion-reduction contact sheets are reviewed at game scale.
- [ ] Godot 4.7 import uses linear filtering and mipmaps appropriate to painterly HD-2D.

## Final Art Rule

The venue should look like a genuinely magnificent old building that survived history only to become an aggressively branded tourist barcade. If the architecture looks cheap, the joke fails. If the neon is removed and the building still reads as specific and beautiful, the straight-man layer is working. If the two hidden entrances can be identified immediately without seeing beyond them, the interior-image package is ready for implementation.
