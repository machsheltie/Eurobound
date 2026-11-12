# Three-Crown Keg Haus - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_shadowexchange_threecrownkeghaus_brewery_03`
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

1. **Three-Crown Alley** — Sticky alley beneath three rusting crowns.
2. **Bravado Threshold** — Dive-bar door and confidence check.
3. **Creaky Floor Route** — Safe and unsafe tiles among passed-out patrons.
4. **Slurring Bar Flies** — Mini-mob patrol around booths.
5. **Keg Sentinel Arena** — Final challenge near the keg stacks.
6. **Bartender Service** — Tour rewards and 10-SOV Iron Gut Tripel.
7. **Velvet Keg Throne** — Drunken monarchy selfie landmark.
8. **Alley Exit** — Returns toward Shadow Exchange.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `three_crown_keg_haus_exterior` | `three_crown_keg_haus_exterior.png` | exterior/threshold painted layer | `tck_alley` |
| `three_crown_keg_haus_interior` | `three_crown_keg_haus_interior.png` | interior painted faces | `tck_entry` |
| `three_crown_keg_haus_node_tck_entry` | `three_crown_keg_haus_tck_entry.png` | gate landmark | `tck_entry` |
| `three_crown_keg_haus_node_tck_floor` | `three_crown_keg_haus_tck_floor.png` | puzzle landmark | `tck_floor` |
| `three_crown_keg_haus_node_tck_barflies` | `three_crown_keg_haus_tck_barflies.png` | encounter landmark | `tck_barflies` |
| `three_crown_keg_haus_node_tck_sentinel` | `three_crown_keg_haus_tck_sentinel.png` | boss landmark | `tck_sentinel` |
| `three_crown_keg_haus_node_tck_service` | `three_crown_keg_haus_tck_service.png` | service landmark | `tck_service` |
| `three_crown_keg_haus_node_tck_throne` | `three_crown_keg_haus_tck_throne.png` | selfie landmark | `tck_throne` |
| `three_crown_keg_haus_node_tck_exit` | `three_crown_keg_haus_tck_exit.png` | exit landmark | `tck_exit` |
| `three_crown_keg_haus_npc_tck_npc_bartender` | `three_crown_keg_haus_tck_npc_bartender.png` | character sprite | `tck_service` |
| `three_crown_keg_haus_npc_tck_npc_barflies` | `three_crown_keg_haus_tck_npc_barflies.png` | character sprite | `tck_barflies` |
| `three_crown_keg_haus_npc_tck_npc_sentinel` | `three_crown_keg_haus_tck_npc_sentinel.png` | character sprite | `tck_sentinel` |
| `three_crown_keg_haus_item_opener_three_crown_keg_haus` | `three_crown_keg_haus_opener_three_crown_keg_haus.png` | tour item/icon | global |
| `three_crown_keg_haus_item_stamp_three_crown_keg_haus` | `three_crown_keg_haus_stamp_three_crown_keg_haus.png` | tour item/icon | global |
| `three_crown_keg_haus_item_beer_three_crown_keg_haus` | `three_crown_keg_haus_beer_three_crown_keg_haus.png` | tour item/icon | global |
| `three_crown_keg_haus_ui` | `three_crown_keg_haus_ui.png` | puzzle/tour UI | global |
| `three_crown_keg_haus_fx` | `three_crown_keg_haus_fx.png` | environmental and combat FX | global |
| `three_crown_keg_haus_masks` | `three_crown_keg_haus_masks.png` | emission/occlusion masks | global |

## Tour and Challenge States

- `three_crown_route_discovered`: base/changed indicator where visible.
- `three_crown_challenge_complete`: base/changed indicator where visible.
- `three_crown_tour_rewards_deferred`: base/changed indicator where visible.
- `three_crown_tour_rewards_granted`: base/changed indicator where visible.
- `three_crown_selfie_unlocked`: base/changed indicator where visible.
- **Three-Crown Keg Haus Bottle Opener:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Three-Crown Keg Haus Stamp:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Iron Gut Tripel:** exact icon and acquired/unavailable/purchasable states; price 10 SOVS.

## Accessibility Assets

- High-contrast safe tiles.
- Detection-cone alternative.
- Reduced haze.
- Subtitled floor and patron cues.
- Clean plates without vapor, haze, strobe, reflections or scrolling screens.
- Text/icon equivalents for audio, timing, route and boss cues.

## Delivery Checklist

- [ ] All asset IDs appear in `sprite_mapping/three_crown_keg_haus_sprite_mapping.json`.
- [ ] Opener/stamp/beer IDs match authoritative item files.
- [ ] Deferred and granted reward states are visually distinct.
- [ ] Parent-location art stops at the transition threshold.
- [ ] Transparent PNGs use clean alpha and 8 px atlas padding.

