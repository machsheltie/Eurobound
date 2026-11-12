# Neon & Chrome Boutique - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_shop_neon_chrome_01`
- **Authoritative slug:** `neon_and_chrome_boutique`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** A glass-and-chrome nightclub simulation that sells the idea of entry before the club does.

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

1. **Glass Storefront** — Chrome glass frontage with fully styled mannequins.
2. **Eyewear Station** — Strobe shades and programmable LED glasses.
3. **Footwear Station** — Club shoes and status footwear.
4. **Premium Stock** — Locked stock opened by Velvet stage-7 completion.
5. **Fitting Area** — Mirror and equipment preview.
6. **Club Simulation** — Safe preview of club gear effects.
7. **Katarina Counter** — Checkout and VIP Potential assessment.
8. **Quarter Exit** — Returns to the neon street.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `neon_and_chrome_boutique_exterior` | `neon_and_chrome_boutique_exterior.png` | exterior/threshold painted layer | `ncb_storefront` |
| `neon_and_chrome_boutique_interior` | `neon_and_chrome_boutique_interior.png` | interior/service footprint | `ncb_eyewear` |
| `neon_and_chrome_boutique_node_ncb_eyewear` | `neon_and_chrome_boutique_ncb_eyewear.png` | shop landmark | `ncb_eyewear` |
| `neon_and_chrome_boutique_node_ncb_footwear` | `neon_and_chrome_boutique_ncb_footwear.png` | shop landmark | `ncb_footwear` |
| `neon_and_chrome_boutique_node_ncb_premium` | `neon_and_chrome_boutique_ncb_premium.png` | shop landmark | `ncb_premium` |
| `neon_and_chrome_boutique_node_ncb_fitting` | `neon_and_chrome_boutique_ncb_fitting.png` | interaction landmark | `ncb_fitting` |
| `neon_and_chrome_boutique_node_ncb_simulation` | `neon_and_chrome_boutique_ncb_simulation.png` | interaction landmark | `ncb_simulation` |
| `neon_and_chrome_boutique_node_ncb_counter` | `neon_and_chrome_boutique_ncb_counter.png` | service landmark | `ncb_counter` |
| `neon_and_chrome_boutique_node_ncb_exit` | `neon_and_chrome_boutique_ncb_exit.png` | exit landmark | `ncb_exit` |
| `neon_and_chrome_boutique_npc_ncb_npc_katarina` | `neon_and_chrome_boutique_ncb_npc_katarina.png` | character sprite | `ncb_counter` |
| `neon_and_chrome_boutique_npc_ncb_npc_host` | `neon_and_chrome_boutique_ncb_npc_host.png` | character sprite | `ncb_fitting` |
| `neon_and_chrome_boutique_item_ncb_led_glasses` | `neon_and_chrome_boutique_ncb_led_glasses.png` | item/service icon | global |
| `neon_and_chrome_boutique_item_ncb_strobe_shades` | `neon_and_chrome_boutique_ncb_strobe_shades.png` | item/service icon | global |
| `neon_and_chrome_boutique_item_ncb_chrome_shoes` | `neon_and_chrome_boutique_ncb_chrome_shoes.png` | item/service icon | global |
| `neon_and_chrome_boutique_item_ncb_premium_wrist_cuff` | `neon_and_chrome_boutique_ncb_premium_wrist_cuff.png` | item/service icon | global |
| `neon_and_chrome_boutique_item_ncb_glow_harness` | `neon_and_chrome_boutique_ncb_glow_harness.png` | item/service icon | global |
| `neon_and_chrome_boutique_ui` | `neon_and_chrome_boutique_ui.png` | interaction/status UI | global |
| `neon_and_chrome_boutique_fx` | `neon_and_chrome_boutique_fx.png` | environmental FX | global |
| `neon_and_chrome_boutique_masks` | `neon_and_chrome_boutique_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- **Katarina:** idle, talk, react and service frames; Chrome tailoring, neon headset and immaculate posture.
- **Showroom Host:** idle, talk, react and service frames; Club-host black with light piping.
- `neon_chrome_open`: provide a readable base/change indicator where visually applicable.
- `neon_chrome_premium_unlocked`: provide a readable base/change indicator where visually applicable.
- `vip_potential_assessed`: provide a readable base/change indicator where visually applicable.
- `club_simulation_complete`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- Reduced-flash simulation.
- Low-reflection chrome.
- Text equipment comparisons.
- No-color-only stock tiers.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/neon_and_chrome_boutique_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

