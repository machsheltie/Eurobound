# Public Restroom - Grease Trap Shrine - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_kebab_alley_grease_trap_shrine_01`
- **Engine:** Godot 4.4
- **Pipeline:** Painterly HD-2D painted faces, depth cards, cutout props, emission masks and state overlays
- **Source boundary:** Only the restroom portion before the appended Mystery Meat Cart heading belongs here.

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

A grease-glazed biohazard shrine lit like a sacred fryer exhaust.

1. **Inside Crawlspace** — Interior tunnel from the kebab stand's tent flap.
2. **Grease-Coated Fixture** — Tiny toilet with warm 2004 receipt paper.
3. **Cursed Sink Collection** — Cursed coin, half-chewed antacid and napkin swan.
4. **Meat-Glyph Mirror** — Cracked mirror with QR codes and Sheltie crown glyph.
5. **Fistø Pilgrimage Tag** — Puked here in '99 pilgrimage graffiti.
6. **Hungover Kebab Icon** — Googly-eyed pixel kebab glows only while Hungover.
7. **Grease Haiku Wall** — Three-line shrine haiku and completion tracker.
8. **Return Crawlspace** — Returns to Kebab Alley.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `public_restroom_grease_trap_shrine_exterior` | `public_restroom_grease_trap_shrine_exterior.png` | exterior/threshold painted layer | `gts_crawlspace` |
| `public_restroom_grease_trap_shrine_interior` | `public_restroom_grease_trap_shrine_interior.png` | interior/service footprint | `gts_fixture` |
| `public_restroom_grease_trap_shrine_node_gts_fixture` | `public_restroom_grease_trap_shrine_gts_fixture.png` | interaction landmark | `gts_fixture` |
| `public_restroom_grease_trap_shrine_node_gts_sink` | `public_restroom_grease_trap_shrine_gts_sink.png` | examine landmark | `gts_sink` |
| `public_restroom_grease_trap_shrine_node_gts_mirror` | `public_restroom_grease_trap_shrine_gts_mirror.png` | lore landmark | `gts_mirror` |
| `public_restroom_grease_trap_shrine_node_gts_fisto_tag` | `public_restroom_grease_trap_shrine_gts_fisto_tag.png` | lore landmark | `gts_fisto_tag` |
| `public_restroom_grease_trap_shrine_node_gts_kebab_icon` | `public_restroom_grease_trap_shrine_gts_kebab_icon.png` | quest landmark | `gts_kebab_icon` |
| `public_restroom_grease_trap_shrine_node_gts_haiku` | `public_restroom_grease_trap_shrine_gts_haiku.png` | quest landmark | `gts_haiku` |
| `public_restroom_grease_trap_shrine_node_gts_exit` | `public_restroom_grease_trap_shrine_gts_exit.png` | exit landmark | `gts_exit` |
| `public_restroom_grease_trap_shrine_item_gts_cursed_coin` | `public_restroom_grease_trap_shrine_gts_cursed_coin.png` | item icon | global |
| `public_restroom_grease_trap_shrine_item_gts_half_antacid` | `public_restroom_grease_trap_shrine_gts_half_antacid.png` | item icon | global |
| `public_restroom_grease_trap_shrine_item_gts_warm_receipt` | `public_restroom_grease_trap_shrine_gts_warm_receipt.png` | item icon | global |
| `public_restroom_grease_trap_shrine_ui` | `public_restroom_grease_trap_shrine_ui.png` | interaction/status UI | global |
| `public_restroom_grease_trap_shrine_fx` | `public_restroom_grease_trap_shrine_fx.png` | particles and overlays | global |
| `public_restroom_grease_trap_shrine_masks` | `public_restroom_grease_trap_shrine_masks.png` | emission/occlusion masks | global |

## Accessibility Assets

- Static grease reflections.
- Reduced steam and flies.
- Text glyph descriptions.
- High-contrast graffiti completion.
- Clean plates without steam, smoke, flies, flash or reflection motion.
- Text/icon equivalents for timing, audio, color and status-only cues.

## Delivery Checklist

- [ ] Asset IDs match `sprite_mapping/public_restroom_grease_trap_shrine_sprite_mapping.json`.
- [ ] Interactive states match the interaction and node files.
- [ ] Parent transitions stop at the location boundary.
- [ ] Transparent PNGs have clean alpha and 8 px atlas padding.

