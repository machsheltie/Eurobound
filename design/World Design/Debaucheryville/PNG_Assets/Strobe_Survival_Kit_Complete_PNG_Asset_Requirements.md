# The Strobe Survival Kit - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_vendor_strobe_survival_01`
- **Authoritative slug:** `strobe_survival_kit`
- **Engine:** Godot 4.4
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** Military-surplus efficiency applied to rave survival.

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

1. **Fold-Out Stall** — Pegboard military-rave stall near club approaches.
2. **Audio Defense** — Earplug grades and hearing warning display.
3. **Visual Enhancement** — Glow sticks, LED glasses and visibility gear.
4. **Chemical Support** — Documented club-support consumables.
5. **Decibel Warning Display** — Live nearby-club hazard readout.
6. **Miroslav Counter** — Checkout and tactical briefing point.
7. **Quarter Exit** — Returns to the neon street.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `strobe_survival_kit_exterior` | `strobe_survival_kit_exterior.png` | exterior/threshold painted layer | `ssk_stall` |
| `strobe_survival_kit_interior` | `strobe_survival_kit_interior.png` | interior/service footprint | `ssk_audio_defense` |
| `strobe_survival_kit_node_ssk_audio_defense` | `strobe_survival_kit_ssk_audio_defense.png` | shop landmark | `ssk_audio_defense` |
| `strobe_survival_kit_node_ssk_visual_gear` | `strobe_survival_kit_ssk_visual_gear.png` | shop landmark | `ssk_visual_gear` |
| `strobe_survival_kit_node_ssk_support_shelf` | `strobe_survival_kit_ssk_support_shelf.png` | shop landmark | `ssk_support_shelf` |
| `strobe_survival_kit_node_ssk_decibel_display` | `strobe_survival_kit_ssk_decibel_display.png` | interaction landmark | `ssk_decibel_display` |
| `strobe_survival_kit_node_ssk_operator` | `strobe_survival_kit_ssk_operator.png` | service landmark | `ssk_operator` |
| `strobe_survival_kit_node_ssk_exit` | `strobe_survival_kit_ssk_exit.png` | exit landmark | `ssk_exit` |
| `strobe_survival_kit_npc_ssk_npc_miroslav` | `strobe_survival_kit_ssk_npc_miroslav.png` | character sprite | `ssk_operator` |
| `strobe_survival_kit_item_ssk_foam_earplugs` | `strobe_survival_kit_ssk_foam_earplugs.png` | item/service icon | global |
| `strobe_survival_kit_item_ssk_musician_earplugs` | `strobe_survival_kit_ssk_musician_earplugs.png` | item/service icon | global |
| `strobe_survival_kit_item_ssk_strobe_shades` | `strobe_survival_kit_ssk_strobe_shades.png` | item/service icon | global |
| `strobe_survival_kit_item_ssk_glow_bundle` | `strobe_survival_kit_ssk_glow_bundle.png` | item/service icon | global |
| `strobe_survival_kit_item_ssk_tactical_pouch` | `strobe_survival_kit_ssk_tactical_pouch.png` | item/service icon | global |
| `strobe_survival_kit_ui` | `strobe_survival_kit_ui.png` | interaction/status UI | global |
| `strobe_survival_kit_fx` | `strobe_survival_kit_fx.png` | environmental FX | global |
| `strobe_survival_kit_masks` | `strobe_survival_kit_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- **Miroslav:** idle, talk, react and service frames; Military-surplus vest, hearing protection and clipboard.
- `strobe_survival_open`: provide a readable base/change indicator where visually applicable.
- `strobe_survival_midnight_markup`: provide a readable base/change indicator where visually applicable.
- `strobe_tactical_briefing_seen`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- No unavoidable strobe preview.
- Reduced-emission merchandise.
- Text decibel readout.
- Color-independent stock categories.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/strobe_survival_kit_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

