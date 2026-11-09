# Claw Machine Maintenance Closet Restroom - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_arcade_maintenance_closet_01`
- **Authoritative slug:** `claw_machine_maintenance_closet_restroom`
- **Engine:** Godot 4.4
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** A mop closet mutated by broken arcade hardware into a sticky secret restroom.

## Resolution and Frame Layout

Every required PNG uses one of these production classes; do not infer canvas size from the visible subject:

| Asset role | Resolution class | Frame layout |
|---|---:|---|
| Exterior, threshold or full interior scene plate | 2048x1152 px | Single 16:9 frame; provide clean plate and separate depth cards |
| Node or landmark cutout | 1024x1024 px | Single transparent frame with 8 px safe padding |
| NPC or creature animation | 2048x512 px | Four 512x512 cells in one row: idle, talk, react, service/combat; 8 fps unless mapping overrides |
| Item, reward or inventory icon | 256x256 px | Single transparent frame with 16 px safe area |
| UI atlas | 2048x1024 px | Power-of-two atlas; label frame rectangles in delivery manifest |
| FX atlas | 2048x2048 px | 8x8 grid of 256x256 cells; unused cells transparent |
| Emission/occlusion mask | Match its source asset exactly | One grayscale mask per source frame; preserve frame order |

## Spatial Composition

1. **Inside Maintenance Door** — Interior face of the permanently unlocked Arcade maintenance door.
2. **DDR Toilet Fixture** — Sticky dance-pad toilet seat in impossible clearance.
3. **INSERT COIN Mirror** — Repurposed CRT mirror looping an INSERT COIN prompt.
4. **Graffiti Wall** — Layered bathroom-network and Rival Trio tags.
5. **Claw Arm and Bucket Zone** — Claw-arm chandelier, janitor bucket foot soak and cleaning clutter.
6. **Arcade Return Door** — Returns to Absinthe Arcade's DDR maintenance recess.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `claw_machine_maintenance_closet_restroom_exterior` | `claw_machine_maintenance_closet_restroom_exterior.png` | exterior/threshold painted layer | `cmr_inside_door` |
| `claw_machine_maintenance_closet_restroom_interior` | `claw_machine_maintenance_closet_restroom_interior.png` | interior/service footprint | `cmr_ddr_toilet` |
| `claw_machine_maintenance_closet_restroom_node_cmr_ddr_toilet` | `claw_machine_maintenance_closet_restroom_cmr_ddr_toilet.png` | interaction landmark | `cmr_ddr_toilet` |
| `claw_machine_maintenance_closet_restroom_node_cmr_crt_mirror` | `claw_machine_maintenance_closet_restroom_cmr_crt_mirror.png` | interaction landmark | `cmr_crt_mirror` |
| `claw_machine_maintenance_closet_restroom_node_cmr_graffiti_wall` | `claw_machine_maintenance_closet_restroom_cmr_graffiti_wall.png` | lore landmark | `cmr_graffiti_wall` |
| `claw_machine_maintenance_closet_restroom_node_cmr_claw_bucket` | `claw_machine_maintenance_closet_restroom_cmr_claw_bucket.png` | examine landmark | `cmr_claw_bucket` |
| `claw_machine_maintenance_closet_restroom_node_cmr_exit` | `claw_machine_maintenance_closet_restroom_cmr_exit.png` | exit landmark | `cmr_exit` |
| `claw_machine_maintenance_closet_restroom_item_cmr_broken_prize_tag` | `claw_machine_maintenance_closet_restroom_cmr_broken_prize_tag.png` | item/service icon | global |
| `claw_machine_maintenance_closet_restroom_item_cmr_rival_icq_snapshot` | `claw_machine_maintenance_closet_restroom_cmr_rival_icq_snapshot.png` | item/service icon | global |
| `claw_machine_maintenance_closet_restroom_ui` | `claw_machine_maintenance_closet_restroom_ui.png` | interaction/status UI | global |
| `claw_machine_maintenance_closet_restroom_fx` | `claw_machine_maintenance_closet_restroom_fx.png` | environmental FX | global |
| `claw_machine_maintenance_closet_restroom_masks` | `claw_machine_maintenance_closet_restroom_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- No resident named NPC; parent-side gatekeepers remain in the parent package.
- `arcade_maintenance_restroom_unlocked`: provide a readable base/change indicator where visually applicable.
- `claw_restroom_graffiti_read`: provide a readable base/change indicator where visually applicable.
- `claw_restroom_icq_callback_sent`: provide a readable base/change indicator where visually applicable.
- `claw_restroom_bathroom_network_registered`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- Reduced fluorescent flicker.
- Static CRT mirror frame.
- Text cue for audio gags.
- Tight-room camera cutaway.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/claw_machine_maintenance_closet_restroom_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

