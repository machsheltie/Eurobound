# Ye Olde B.R.E.W. Lab - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_velvetcurtain_brew_lab_01`
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

1. **Inside Lab Stair** — Interior side of the Velvet service route.
2. **Brewing Vat Leg** — Bioluminescent vats and wired fermentation tanks.
3. **AI Console Leg** — NFT flavor screens and taste controls.
4. **Taste Profile Station** — Logic minigame and opener challenge.
5. **Fermenting Algorithm** — Mini-mob across LED floor paths.
6. **BrewBot Arena** — Final brewery-tour challenge.
7. **Robotic Bartender** — Tour rewards and volatile Blockchain Bock price.
8. **Algorithm Archive** — Blockchain-hash selfie terminal.
9. **Club Return Stair** — Returns to Velvet Curtain Club.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `ye_olde_brew_lab_exterior` | `ye_olde_brew_lab_exterior.png` | exterior/threshold painted layer | `ybl_stair` |
| `ye_olde_brew_lab_interior` | `ye_olde_brew_lab_interior.png` | interior painted faces | `ybl_vats` |
| `ye_olde_brew_lab_node_ybl_vats` | `ye_olde_brew_lab_ybl_vats.png` | interior landmark | `ybl_vats` |
| `ye_olde_brew_lab_node_ybl_consoles` | `ye_olde_brew_lab_ybl_consoles.png` | interaction landmark | `ybl_consoles` |
| `ye_olde_brew_lab_node_ybl_taste` | `ye_olde_brew_lab_ybl_taste.png` | puzzle landmark | `ybl_taste` |
| `ye_olde_brew_lab_node_ybl_algorithm` | `ye_olde_brew_lab_ybl_algorithm.png` | encounter landmark | `ybl_algorithm` |
| `ye_olde_brew_lab_node_ybl_brewbot` | `ye_olde_brew_lab_ybl_brewbot.png` | boss landmark | `ybl_brewbot` |
| `ye_olde_brew_lab_node_ybl_service` | `ye_olde_brew_lab_ybl_service.png` | service landmark | `ybl_service` |
| `ye_olde_brew_lab_node_ybl_selfie` | `ye_olde_brew_lab_ybl_selfie.png` | selfie landmark | `ybl_selfie` |
| `ye_olde_brew_lab_node_ybl_exit` | `ye_olde_brew_lab_ybl_exit.png` | exit landmark | `ybl_exit` |
| `ye_olde_brew_lab_npc_ybl_npc_robot_bartender` | `ye_olde_brew_lab_ybl_npc_robot_bartender.png` | character sprite | `ybl_service` |
| `ye_olde_brew_lab_npc_ybl_npc_algorithm` | `ye_olde_brew_lab_ybl_npc_algorithm.png` | character sprite | `ybl_algorithm` |
| `ye_olde_brew_lab_npc_ybl_npc_brewbot` | `ye_olde_brew_lab_ybl_npc_brewbot.png` | character sprite | `ybl_brewbot` |
| `ye_olde_brew_lab_item_opener_ye_olde_brew_lab` | `ye_olde_brew_lab_opener_ye_olde_brew_lab.png` | tour item/icon | global |
| `ye_olde_brew_lab_item_stamp_ye_olde_brew_lab` | `ye_olde_brew_lab_stamp_ye_olde_brew_lab.png` | tour item/icon | global |
| `ye_olde_brew_lab_item_beer_ye_olde_brew_lab` | `ye_olde_brew_lab_beer_ye_olde_brew_lab.png` | tour item/icon | global |
| `ye_olde_brew_lab_ui` | `ye_olde_brew_lab_ui.png` | puzzle/tour UI | global |
| `ye_olde_brew_lab_fx` | `ye_olde_brew_lab_fx.png` | environmental and combat FX | global |
| `ye_olde_brew_lab_masks` | `ye_olde_brew_lab_masks.png` | emission/occlusion masks | global |

## Tour and Challenge States

- `brew_lab_entrance_discovered`: base/changed indicator where visible.
- `brew_lab_access_unlocked`: base/changed indicator where visible.
- `brew_lab_challenge_complete`: base/changed indicator where visible.
- `brew_lab_tour_rewards_deferred`: base/changed indicator where visible.
- `brew_lab_tour_rewards_granted`: base/changed indicator where visible.
- `brew_lab_selfie_unlocked`: base/changed indicator where visible.
- `debaucheryville_brewery_tour_complete`: base/changed indicator where visible.
- **Ye Olde B.R.E.W. Lab Bottle Opener:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Ye Olde B.R.E.W. Lab Stamp:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Blockchain Bock:** exact icon and acquired/unavailable/purchasable states; price 18 ±5 SOVS.

## Accessibility Assets

- Reduced screen scroll.
- High-contrast LED paths.
- Reduced liquid glow.
- Text taste-logic cues.
- Clean plates without vapor, haze, strobe, reflections or scrolling screens.
- Text/icon equivalents for audio, timing, route and boss cues.

## Delivery Checklist

- [ ] All asset IDs appear in `sprite_mapping/ye_olde_brew_lab_sprite_mapping.json`.
- [ ] Opener/stamp/beer IDs match authoritative item files.
- [ ] Deferred and granted reward states are visually distinct.
- [ ] Parent-location art stops at the transition threshold.
- [ ] Transparent PNGs use clean alpha and 8 px atlas padding.

