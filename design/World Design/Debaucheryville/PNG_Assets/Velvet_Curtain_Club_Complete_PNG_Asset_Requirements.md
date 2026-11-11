# Velvet Curtain Club - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_operaruins_velvetcurtainclub_nightclub_01`
- **Authoritative slug:** `velvet_curtain_club`
- **Engine:** Godot 4.4
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** Fraudulent exclusivity staged in burgundy fog, crushed velvet and vape-crystal chandeliers.

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

1. **Opera-Ruins Alley** — Graffiti lane, dumpster mural and rope checkpoint.
2. **Velvet Rope Gate** — Kamil and Marek guard the bass-pulsing curtain.
3. **Dance Floor** — Burgundy fog beneath vape-pen chandeliers.
4. **Broken-Throne DJ Dais** — DJ platform and club audio landmark.
5. **Crushed-Velvet Booths** — Semicircular social and quest seating.
6. **Club Bar** — Drink service and patron reactions.
7. **VIP Stall Path** — Glitter trail to STAFF ONLY curtain and Bravado gate.
8. **B.R.E.W. Lab Service Route** — Service route to QR pad and basement transition.
9. **Alley Exit** — Returns through the velvet curtain.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `velvet_curtain_club_exterior` | `velvet_curtain_club_exterior.png` | exterior/threshold painted layer | `vcc_alley` |
| `velvet_curtain_club_interior` | `velvet_curtain_club_interior.png` | interior/service footprint | `vcc_bouncer_gate` |
| `velvet_curtain_club_node_vcc_bouncer_gate` | `velvet_curtain_club_vcc_bouncer_gate.png` | gate landmark | `vcc_bouncer_gate` |
| `velvet_curtain_club_node_vcc_dance_floor` | `velvet_curtain_club_vcc_dance_floor.png` | social landmark | `vcc_dance_floor` |
| `velvet_curtain_club_node_vcc_dj_dais` | `velvet_curtain_club_vcc_dj_dais.png` | interaction landmark | `vcc_dj_dais` |
| `velvet_curtain_club_node_vcc_booths` | `velvet_curtain_club_vcc_booths.png` | social landmark | `vcc_booths` |
| `velvet_curtain_club_node_vcc_bar` | `velvet_curtain_club_vcc_bar.png` | service landmark | `vcc_bar` |
| `velvet_curtain_club_node_vcc_vip_path` | `velvet_curtain_club_vcc_vip_path.png` | transition landmark | `vcc_vip_path` |
| `velvet_curtain_club_node_vcc_lab_path` | `velvet_curtain_club_vcc_lab_path.png` | transition landmark | `vcc_lab_path` |
| `velvet_curtain_club_node_vcc_exit` | `velvet_curtain_club_vcc_exit.png` | exit landmark | `vcc_exit` |
| `velvet_curtain_club_npc_vcc_npc_kamil` | `velvet_curtain_club_vcc_npc_kamil.png` | character sprite | `vcc_bouncer_gate` |
| `velvet_curtain_club_npc_vcc_npc_marek` | `velvet_curtain_club_vcc_npc_marek.png` | character sprite | `vcc_bouncer_gate` |
| `velvet_curtain_club_npc_vcc_npc_vanessa` | `velvet_curtain_club_vcc_npc_vanessa.png` | character sprite | `vcc_booths` |
| `velvet_curtain_club_npc_vcc_npc_dj` | `velvet_curtain_club_vcc_npc_dj.png` | character sprite | `vcc_dj_dais` |
| `velvet_curtain_club_item_vcc_house_drink` | `velvet_curtain_club_vcc_house_drink.png` | item/service icon | global |
| `velvet_curtain_club_item_vcc_flyer_stack` | `velvet_curtain_club_vcc_flyer_stack.png` | item/service icon | global |
| `velvet_curtain_club_item_vcc_vip_wristbands` | `velvet_curtain_club_vcc_vip_wristbands.png` | item/service icon | global |
| `velvet_curtain_club_ui` | `velvet_curtain_club_ui.png` | interaction/status UI | global |
| `velvet_curtain_club_fx` | `velvet_curtain_club_fx.png` | environmental FX | global |
| `velvet_curtain_club_masks` | `velvet_curtain_club_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- **Kamil:** idle, talk, react and service frames; Cybernetic eye, black coat and unimpressed posture.
- **Marek:** idle, talk, react and service frames; Buff silhouette and velvet rope gloves.
- **Vape Witch Vanessa:** idle, talk, react and service frames; Burgundy clubwear, crystal vape and occult glow.
- **DJ Sound Alchemist:** idle, talk, react and service frames; Broken-throne silhouette and LED headphones.
- `vip_wristbands_all_bros`: provide a readable base/change indicator where visually applicable.
- `vip_wristband_quest_complete`: provide a readable base/change indicator where visually applicable.
- `velvet_curtain_club_access_was_always_free`: provide a readable base/change indicator where visually applicable.
- `velvet_vip_stall_entrance_discovered`: provide a readable base/change indicator where visually applicable.
- `velvet_vip_stall_access_unlocked`: provide a readable base/change indicator where visually applicable.
- `brew_lab_entrance_discovered`: provide a readable base/change indicator where visually applicable.
- `brew_lab_access_unlocked`: provide a readable base/change indicator where visually applicable.
- `club_flyer_triggered`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- Reduced fog.
- Reduced flash.
- Captioned bass/event cues.
- High-contrast exits and child doors.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/velvet_curtain_club_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

