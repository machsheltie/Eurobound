# The Participation Trophy - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_circus_participation_trophy_01`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, cutout props, emission masks and state overlays
- **Source boundary:** Dedicated location brief and approved package spec.

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

## Visual and Spatial Target

A deliberately underwhelming booth where ticket economics convert effort into garbage.

1. **Weathered Prize Booth** — Peeling carnival booth beneath a faded Everyone's a Winner banner.
2. **Display-Only Grand Shelf** — Unreachable prizes staged above the real inventory.
3. **Good Prize Shelf** — Technically obtainable high-tier stock.
4. **Consolation Shelves** — Ordinary redemption inventory.
5. **Participation Floor Bin** — The real low-ticket prize supply.
6. **Yolanda Counter** — Ticket count, direct purchase and Frequent Loser reactions.
7. **Circus Exit** — Returns to circus grounds.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `participation_trophy_exterior` | `participation_trophy_exterior.png` | exterior/threshold painted layer | `pt_booth` |
| `participation_trophy_interior` | `participation_trophy_interior.png` | interior/service footprint | `pt_grand_shelf` |
| `participation_trophy_node_pt_grand_shelf` | `participation_trophy_pt_grand_shelf.png` | display landmark | `pt_grand_shelf` |
| `participation_trophy_node_pt_good_shelf` | `participation_trophy_pt_good_shelf.png` | shop landmark | `pt_good_shelf` |
| `participation_trophy_node_pt_consolation` | `participation_trophy_pt_consolation.png` | shop landmark | `pt_consolation` |
| `participation_trophy_node_pt_floor_junk` | `participation_trophy_pt_floor_junk.png` | shop landmark | `pt_floor_junk` |
| `participation_trophy_node_pt_counter` | `participation_trophy_pt_counter.png` | service landmark | `pt_counter` |
| `participation_trophy_node_pt_exit` | `participation_trophy_pt_exit.png` | exit landmark | `pt_exit` |
| `participation_trophy_npc_pt_npc_yolanda` | `participation_trophy_pt_npc_yolanda.png` | character sprite | `pt_counter` |
| `participation_trophy_item_pt_sad_plush` | `participation_trophy_pt_sad_plush.png` | item icon | global |
| `participation_trophy_item_pt_plastic_medal` | `participation_trophy_pt_plastic_medal.png` | item icon | global |
| `participation_trophy_item_pt_mystery_trinket` | `participation_trophy_pt_mystery_trinket.png` | item icon | global |
| `participation_trophy_item_pt_grand_display` | `participation_trophy_pt_grand_display.png` | item icon | global |
| `participation_trophy_item_pt_direct_junk` | `participation_trophy_pt_direct_junk.png` | item icon | global |
| `participation_trophy_ui` | `participation_trophy_ui.png` | interaction/status UI | global |
| `participation_trophy_fx` | `participation_trophy_fx.png` | particles and overlays | global |
| `participation_trophy_masks` | `participation_trophy_masks.png` | emission/occlusion masks | global |

## Accessibility Assets

- High-contrast ticket costs.
- Display-only labels.
- Reduced carnival flicker.
- Text prize-tier hierarchy.
- Clean plates without steam, smoke, flies, flash or reflection motion.
- Text/icon equivalents for timing, audio, color and status-only cues.

## Delivery Checklist

- [ ] Asset IDs match `sprite_mapping/participation_trophy_sprite_mapping.json`.
- [ ] Interactive states match the interaction and node files.
- [ ] Parent transitions stop at the location boundary.
- [ ] Transparent PNGs have clean alpha and 8 px atlas padding.

