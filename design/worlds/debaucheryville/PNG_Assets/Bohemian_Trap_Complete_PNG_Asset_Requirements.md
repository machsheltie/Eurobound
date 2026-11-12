# The Bohemian Trap - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_vendor_bohemian_trap_01`
- **Authoritative slug:** `bohemian_trap`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** A 2015 cart artificially aged into Belle Époque tourist mythology.

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

1. **Cart Approach** — Nightly neon-quarter anchor with ornate green-and-gold cart.
2. **Absinthe Array** — Backlit bottles ranked by invented authenticity.
3. **Ritual Station** — Spoons, cubes, drips and controlled flame theater.
4. **Performer Counter** — Vendor delivers mythology and Bravado reactions.
5. **Customer Reaction Space** — Standing zone for consumption and control-reversal aftermath.
6. **Quarter Exit** — Returns to the neon entertainment street.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `bohemian_trap_exterior` | `bohemian_trap_exterior.png` | exterior/threshold painted layer | `bt_cart_approach` |
| `bohemian_trap_interior` | `bohemian_trap_interior.png` | interior/service footprint | `bt_bottle_display` |
| `bohemian_trap_node_bt_bottle_display` | `bohemian_trap_bt_bottle_display.png` | shop landmark | `bt_bottle_display` |
| `bohemian_trap_node_bt_ritual_station` | `bohemian_trap_bt_ritual_station.png` | interaction landmark | `bt_ritual_station` |
| `bohemian_trap_node_bt_performer` | `bohemian_trap_bt_performer.png` | service landmark | `bt_performer` |
| `bohemian_trap_node_bt_customer_space` | `bohemian_trap_bt_customer_space.png` | social landmark | `bt_customer_space` |
| `bohemian_trap_node_bt_exit` | `bohemian_trap_bt_exit.png` | exit landmark | `bt_exit` |
| `bohemian_trap_npc_bt_npc_performer` | `bohemian_trap_bt_npc_performer.png` | character sprite | `bt_performer` |
| `bohemian_trap_item_bt_house_absinthe` | `bohemian_trap_bt_house_absinthe.png` | item/service icon | global |
| `bohemian_trap_item_bt_authentic_absinthe` | `bohemian_trap_bt_authentic_absinthe.png` | item/service icon | global |
| `bohemian_trap_item_bt_hemingway_tier` | `bohemian_trap_bt_hemingway_tier.png` | item/service icon | global |
| `bohemian_trap_item_bt_absinthe_ritual` | `bohemian_trap_bt_absinthe_ritual.png` | item/service icon | global |
| `bohemian_trap_ui` | `bohemian_trap_ui.png` | interaction/status UI | global |
| `bohemian_trap_fx` | `bohemian_trap_fx.png` | environmental FX | global |
| `bohemian_trap_masks` | `bohemian_trap_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- **The Absinthe Performer:** idle, talk, react and service frames; Belle Époque costume with suspiciously modern shoes.
- `bohemian_trap_open`: provide a readable base/change indicator where visually applicable.
- `bohemian_trap_ritual_complete`: provide a readable base/change indicator where visually applicable.
- `bohemian_trap_control_reversal_active`: provide a readable base/change indicator where visually applicable.
- `bohemian_trap_worth_it_checked`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- Flame-free ritual alternative.
- Control-reversal warning and opt-out.
- Reduced green pulse.
- Text product effects.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/bohemian_trap_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

