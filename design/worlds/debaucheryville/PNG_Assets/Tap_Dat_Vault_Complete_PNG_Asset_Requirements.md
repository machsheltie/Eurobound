# The Tap Dat Vault - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_clocktower_tapdatvault_brewery_02`
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

1. **Clocktower Plaza Approach** — Tap Dat-owned plaza node with hidden switch and countdown glyphs.
2. **Vault Door** — Neon graffiti door active only during the midnight window.
3. **Subwoofer Vats** — Central brewing vats pulse rhythm cues.
4. **Vapor Pressure Console** — Audio-visual timing puzzle with three-strike ejection.
5. **Glitched Brew Ad Bot** — Spam mini-mob before the boss.
6. **Strobe Brewmistress Arena** — Final challenge with safe visual cue mode.
7. **Vault Service** — Tour rewards and 14-SOV Vape Stout.
8. **You Are Brewtiful Wall** — Hologram selfie landmark.
9. **Plaza Return** — Returns to Clocktower Plaza.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `tap_dat_vault_exterior` | `tap_dat_vault_exterior.png` | exterior/threshold painted layer | `tdv_plaza` |
| `tap_dat_vault_interior` | `tap_dat_vault_interior.png` | interior painted faces | `tdv_vault` |
| `tap_dat_vault_node_tdv_vault` | `tap_dat_vault_tdv_vault.png` | gate landmark | `tdv_vault` |
| `tap_dat_vault_node_tdv_vats` | `tap_dat_vault_tdv_vats.png` | interior landmark | `tdv_vats` |
| `tap_dat_vault_node_tdv_rhythm` | `tap_dat_vault_tdv_rhythm.png` | puzzle landmark | `tdv_rhythm` |
| `tap_dat_vault_node_tdv_adbot` | `tap_dat_vault_tdv_adbot.png` | encounter landmark | `tdv_adbot` |
| `tap_dat_vault_node_tdv_brewmistress` | `tap_dat_vault_tdv_brewmistress.png` | boss landmark | `tdv_brewmistress` |
| `tap_dat_vault_node_tdv_service` | `tap_dat_vault_tdv_service.png` | service landmark | `tdv_service` |
| `tap_dat_vault_node_tdv_selfie` | `tap_dat_vault_tdv_selfie.png` | selfie landmark | `tdv_selfie` |
| `tap_dat_vault_node_tdv_exit` | `tap_dat_vault_tdv_exit.png` | exit landmark | `tdv_exit` |
| `tap_dat_vault_npc_tdv_npc_glitch_bouncer` | `tap_dat_vault_tdv_npc_glitch_bouncer.png` | character sprite | `tdv_vault` |
| `tap_dat_vault_npc_tdv_npc_adbot` | `tap_dat_vault_tdv_npc_adbot.png` | character sprite | `tdv_adbot` |
| `tap_dat_vault_npc_tdv_npc_brewmistress` | `tap_dat_vault_tdv_npc_brewmistress.png` | character sprite | `tdv_brewmistress` |
| `tap_dat_vault_item_opener_tap_dat_vault` | `tap_dat_vault_opener_tap_dat_vault.png` | tour item/icon | global |
| `tap_dat_vault_item_stamp_tap_dat_vault` | `tap_dat_vault_stamp_tap_dat_vault.png` | tour item/icon | global |
| `tap_dat_vault_item_beer_tap_dat_vault` | `tap_dat_vault_beer_tap_dat_vault.png` | tour item/icon | global |
| `tap_dat_vault_ui` | `tap_dat_vault_ui.png` | puzzle/tour UI | global |
| `tap_dat_vault_fx` | `tap_dat_vault_fx.png` | environmental and combat FX | global |
| `tap_dat_vault_masks` | `tap_dat_vault_masks.png` | emission/occlusion masks | global |

## Tour and Challenge States

- `tap_dat_switch_discovered`: base/changed indicator where visible.
- `tap_dat_midnight_window_open`: base/changed indicator where visible.
- `tap_dat_rhythm_strikes`: base/changed indicator where visible.
- `tap_dat_challenge_complete`: base/changed indicator where visible.
- `tap_dat_tour_rewards_deferred`: base/changed indicator where visible.
- `tap_dat_tour_rewards_granted`: base/changed indicator where visible.
- `tap_dat_selfie_unlocked`: base/changed indicator where visible.
- **Tap Dat Vault Bottle Opener:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Tap Dat Vault Stamp:** exact icon and acquired/unavailable/purchasable states; never sold.
- **Vape Stout:** exact icon and acquired/unavailable/purchasable states; price 14 SOVS.

## Accessibility Assets

- Visual rhythm substitute.
- Reduced strobe.
- Reduced vapor.
- Three-strike count in text/icons.
- Clean plates without vapor, haze, strobe, reflections or scrolling screens.
- Text/icon equivalents for audio, timing, route and boss cues.

## Delivery Checklist

- [ ] All asset IDs appear in `sprite_mapping/tap_dat_vault_sprite_mapping.json`.
- [ ] Opener/stamp/beer IDs match authoritative item files.
- [ ] Deferred and granted reward states are visually distinct.
- [ ] Parent-location art stops at the transition threshold.
- [ ] Transparent PNGs use clean alpha and 8 px atlas padding.

