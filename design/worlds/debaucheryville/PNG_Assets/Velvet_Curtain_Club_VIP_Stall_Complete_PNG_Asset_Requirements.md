# Velvet Curtain Club VIP Stall - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_velvetcurtain_vipstall_bathroom_01`
- **Authoritative slug:** `velvet_curtain_club_vip_stall`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** A tiny velvet-lined toilet trying to perform luxury through stains, RGB shimmer and crypto graffiti.

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

1. **Inside VIP Curtain** — Interior side of the STAFF ONLY curtain.
2. **Velvet Fixture** — Stained black-velvet toilet seat and chipped champagne holder.
3. **Selfie-Cam Mirror** — Overhead mirror with CryptoQueen filter.
4. **QR Code Graffiti** — The Millennium Bug (Mint #00) QR code graffiti, on the wall from the start; scanning plays the highlight glow, scan beep and success chime.
5. **Crypto Graffiti Wall** — ROI jokes, Fistø lore and DO NOT LOOK AT THE BABY clue.
6. **Club Return Curtain** — Returns to Velvet Curtain Club.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `velvet_curtain_club_vip_stall_exterior` | `velvet_curtain_club_vip_stall_exterior.png` | exterior/threshold painted layer | `vcs_inside_curtain` |
| `velvet_curtain_club_vip_stall_interior` | `velvet_curtain_club_vip_stall_interior.png` | interior/service footprint | `vcs_fixture` |
| `velvet_curtain_club_vip_stall_node_vcs_fixture` | `velvet_curtain_club_vip_stall_vcs_fixture.png` | interaction landmark | `vcs_fixture` |
| `velvet_curtain_club_vip_stall_node_vcs_selfie_mirror` | `velvet_curtain_club_vip_stall_vcs_selfie_mirror.png` | interaction landmark | `vcs_selfie_mirror` |
| `velvet_curtain_club_vip_stall_node_vcs_qr_tile` | `velvet_curtain_club_vip_stall_vcs_qr_tile.png` | quest landmark | `vcs_qr_tile` |
| `velvet_curtain_club_vip_stall_node_vcs_graffiti` | `velvet_curtain_club_vip_stall_vcs_graffiti.png` | lore landmark | `vcs_graffiti` |
| `velvet_curtain_club_vip_stall_node_vcs_exit` | `velvet_curtain_club_vip_stall_vcs_exit.png` | exit landmark | `vcs_exit` |
| `velvet_curtain_club_vip_stall_item_item_nft_millennium_bug` | `velvet_curtain_club_vip_stall_item_nft_millennium_bug.png` | item/service icon | global |
| `velvet_curtain_club_vip_stall_item_vcs_spite_reserve` | `velvet_curtain_club_vip_stall_vcs_spite_reserve.png` | item/service icon | global |
| `velvet_curtain_club_vip_stall_item_vcs_nft_affinity` | `velvet_curtain_club_vip_stall_vcs_nft_affinity.png` | item/service icon | global |
| `velvet_curtain_club_vip_stall_ui` | `velvet_curtain_club_vip_stall_ui.png` | interaction/status UI | global |
| `velvet_curtain_club_vip_stall_fx` | `velvet_curtain_club_vip_stall_fx.png` | environmental FX | global |
| `velvet_curtain_club_vip_stall_masks` | `velvet_curtain_club_vip_stall_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- No resident named NPC; parent-side gatekeepers remain in the parent package.
- `velvet_vip_stall_access_unlocked`: provide a readable base/change indicator where visually applicable.
- `millennium_bug_obtained`: provide a readable base/change indicator where visually applicable.
- `meme_black_market_graffiti_clue_read`: provide a readable base/change indicator where visually applicable.
- `vip_stall_fisto_lore_read`: provide a readable base/change indicator where visually applicable.
- `nft_affinity_protection_active`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- Static RGB alternative.
- Base QR remains visible through status overlays.
- Text selfie-filter description.
- Reduced champagne drip.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/velvet_curtain_club_vip_stall_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

