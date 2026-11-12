# The Absinthium Taproom - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_brewery_absinthium_taproom_01`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, cutout characters/props, emission masks, puzzle cues and state overlays
- **Tour reward rule:** Physical entry is never gated by an opener. Challenge completion while `brewery_tour_active` and carrying `bottle_opener_keychain` grants the local opener, stamp, selfie and signature-beer access; pre-tour completion defers those rewards without replay.

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

1. **Inside Green Veil** — Vapor transition from the Arcade curtain.
2. **Distortion Den** — Cracked-bottle bar and service landmark.
3. **Mirror Maze** — Stable node topology presented through deceptive infinite reflections.
4. **Mirror Chad Encounter** — Reflection roast and puzzle checkpoint.
5. **Green Fairy Wisp Arena** — Final challenge space in controlled green vapor.
6. **Dr. Vanek Service Point** — Tour reward and 12-SOV Absinthe Lager service.
7. **Floating Chalice Selfie** — Brewmaster selfie landmark.
8. **Arcade Return Veil** — Returns through the green curtain.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `absinthium_taproom_exterior` | `absinthium_taproom_exterior.png` | exterior/threshold painted layer | `at_veil` |
| `absinthium_taproom_interior` | `absinthium_taproom_interior.png` | interior painted faces | `at_den` |
| `absinthium_taproom_node_at_den` | `absinthium_taproom_at_den.png` | interior landmark | `at_den` |
| `absinthium_taproom_node_at_mirror_maze` | `absinthium_taproom_at_mirror_maze.png` | puzzle landmark | `at_mirror_maze` |
| `absinthium_taproom_node_at_mirror_chad` | `absinthium_taproom_at_mirror_chad.png` | encounter landmark | `at_mirror_chad` |
| `absinthium_taproom_node_at_wisp_arena` | `absinthium_taproom_at_wisp_arena.png` | boss landmark | `at_wisp_arena` |
| `absinthium_taproom_node_at_service` | `absinthium_taproom_at_service.png` | service landmark | `at_service` |
| `absinthium_taproom_node_at_selfie` | `absinthium_taproom_at_selfie.png` | selfie landmark | `at_selfie` |
| `absinthium_taproom_node_at_exit` | `absinthium_taproom_at_exit.png` | exit landmark | `at_exit` |
| `absinthium_taproom_npc_at_npc_vanek` | `absinthium_taproom_at_npc_vanek.png` | character sprite | `at_service` |
| `absinthium_taproom_npc_at_npc_mirror_chad` | `absinthium_taproom_at_npc_mirror_chad.png` | character sprite | `at_mirror_chad` |
| `absinthium_taproom_npc_at_npc_wisp` | `absinthium_taproom_at_npc_wisp.png` | character sprite | `at_wisp_arena` |
| `absinthium_taproom_item_opener_absinthium_taproom` | `absinthium_taproom_opener_absinthium_taproom.png` | tour item/icon | global |
| `absinthium_taproom_item_stamp_absinthium_taproom` | `absinthium_taproom_stamp_absinthium_taproom.png` | tour item/icon | global |
| `absinthium_taproom_item_beer_absinthium_taproom` | `absinthium_taproom_beer_absinthium_taproom.png` | tour item/icon | global |
| `absinthium_taproom_ui` | `absinthium_taproom_ui.png` | puzzle/tour UI | global |
| `absinthium_taproom_fx` | `absinthium_taproom_fx.png` | environmental and combat FX | global |
| `absinthium_taproom_masks` | `absinthium_taproom_masks.png` | emission/occlusion masks | global |

## Tour and Challenge States

- `absinthium_taproom_entrance_discovered`: base/changed indicator where visible.
- `absinthium_challenge_complete`: base/changed indicator where visible.
- `absinthium_tour_rewards_deferred`: base/changed indicator where visible.
- `absinthium_tour_rewards_granted`: base/changed indicator where visible.
- `absinthium_selfie_unlocked`: base/changed indicator where visible.
- **The Absinthium Taproom Bottle Opener:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Absinthium Taproom Stamp:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Absinthe Lager:** exact icon and acquired/unavailable/purchasable states; price 12 SOVS.

## Accessibility Assets

- Reduced mirror distortion.
- Static route markers.
- Reduced vapor.
- Text/audio-substitute puzzle cues.
- Clean plates without vapor, haze, strobe, reflections or scrolling screens.
- Text/icon equivalents for audio, timing, route and boss cues.

## Delivery Checklist

- [ ] All asset IDs appear in `sprite_mapping/absinthium_taproom_sprite_mapping.json`.
- [ ] Opener/stamp/beer IDs match authoritative item files.
- [ ] Deferred and granted reward states are visually distinct.
- [ ] Parent-location art stops at the transition threshold.
- [ ] Transparent PNGs use clean alpha and 8 px atlas padding.

