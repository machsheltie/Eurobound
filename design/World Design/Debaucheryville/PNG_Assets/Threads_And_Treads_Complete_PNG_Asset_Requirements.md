# Threads & Treads - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_shop_threads_treads_01`
- **Authoritative slug:** `threads_and_treads`
- **Engine:** Godot 4.4
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** A dark leather-and-chrome shop selling defense, style and late-night reinvention.

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

1. **Chrome Storefront** — Narrow black façade with leather mannequins and chrome sign.
2. **Jacket Gauntlet** — Immediate wall of leather and denim.
3. **Footwear Wall** — Combat boots and defensive shoes.
4. **Chains and Accessories** — Style and equipment-slot accessories.
5. **Mirror Assessment** — Identity preview and Cool Factor assessment.
6. **Zdeněk Counter** — Checkout and transformation choice.
7. **Quarter Exit** — Returns to the neon street.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `threads_and_treads_exterior` | `threads_and_treads_exterior.png` | exterior/threshold painted layer | `tt_storefront` |
| `threads_and_treads_interior` | `threads_and_treads_interior.png` | interior/service footprint | `tt_jacket_gauntlet` |
| `threads_and_treads_node_tt_jacket_gauntlet` | `threads_and_treads_tt_jacket_gauntlet.png` | shop landmark | `tt_jacket_gauntlet` |
| `threads_and_treads_node_tt_footwear` | `threads_and_treads_tt_footwear.png` | shop landmark | `tt_footwear` |
| `threads_and_treads_node_tt_accessories` | `threads_and_treads_tt_accessories.png` | shop landmark | `tt_accessories` |
| `threads_and_treads_node_tt_fitting_mirror` | `threads_and_treads_tt_fitting_mirror.png` | interaction landmark | `tt_fitting_mirror` |
| `threads_and_treads_node_tt_counter` | `threads_and_treads_tt_counter.png` | service landmark | `tt_counter` |
| `threads_and_treads_node_tt_exit` | `threads_and_treads_tt_exit.png` | exit landmark | `tt_exit` |
| `threads_and_treads_npc_tt_npc_zdenek` | `threads_and_treads_tt_npc_zdenek.png` | character sprite | `tt_counter` |
| `threads_and_treads_item_tt_leather_jacket` | `threads_and_treads_tt_leather_jacket.png` | item/service icon | global |
| `threads_and_treads_item_tt_denim_vest` | `threads_and_treads_tt_denim_vest.png` | item/service icon | global |
| `threads_and_treads_item_tt_combat_boots` | `threads_and_treads_tt_combat_boots.png` | item/service icon | global |
| `threads_and_treads_item_tt_chain_wallet` | `threads_and_treads_tt_chain_wallet.png` | item/service icon | global |
| `threads_and_treads_item_tt_identity_overhaul` | `threads_and_treads_tt_identity_overhaul.png` | item/service icon | global |
| `threads_and_treads_ui` | `threads_and_treads_ui.png` | interaction/status UI | global |
| `threads_and_treads_fx` | `threads_and_treads_fx.png` | environmental FX | global |
| `threads_and_treads_masks` | `threads_and_treads_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- **Zdeněk:** idle, talk, react and service frames; Dark work shirt, tape measure and chrome rings.
- `threads_treads_2am_crowd`: provide a readable base/change indicator where visually applicable.
- `threads_treads_transformation_chosen`: provide a readable base/change indicator where visually applicable.
- `cool_factor_assessed`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- Mirror preview without distortion.
- High-contrast equipment stats.
- Text Cool Factor assessment.
- Reduced chrome glare.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/threads_and_treads_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

