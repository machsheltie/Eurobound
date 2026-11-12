# Euro Ink 4 Less - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_gilded_square_euro_ink_4_less_01`
- **Authoritative slug:** `euro_ink_4_less`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props and selective in-world pixel content
- **Purpose:** Reconciles the existing JSON/sprite package and supersedes older/hash-prefixed PNG requirement documents.

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

## Visual Target

A cracked alley tattoo shop with failing pink neon, harsh fluorescents and dense low-budget flash art.

## Required Scene Layers

- Alley storefront, barker position and signage states
- Reception, waiting area and two curtained tattoo stations
- Viktor, Marta, barker and customer sprites
- Tattoo chair sequence, flash-art selection and reveal UI
- Permanent tattoo overlays and aftercare props

## Required Asset Families

- **storefront** — `euro_ink_exterior.png`; base, active, completed/closed and emission-mask states as applicable.
- **shop interior** — `euro_ink_interior.png`; base, active, completed/closed and emission-mask states as applicable.
- **tattoo stations** — `euro_ink_tattoo_station.png`; base, active, completed/closed and emission-mask states as applicable.
- **characters** — `euro_ink_characters.png`; base, active, completed/closed and emission-mask states as applicable.
- **cosmetics/UI** — `euro_ink_tattoo_ui.png`; base, active, completed/closed and emission-mask states as applicable.

## Accessibility Assets

- Reduced-flash and reduced-motion overlays.
- High-contrast interaction outlines and exit arrows.
- Text/icon substitutes for audio, color and timing-only cues.
- Clean plates with particles, crowds and distortion removed.

## Godot 4.7 Delivery

- Preserve every filename referenced by `sprite_mapping/euro_ink_4_less_sprite_mapping.json`.
- Supply color, alpha, normal/emission masks and atlas metadata where the current mapping expects them.
- Use painterly environmental layers; reserve pixel art for screens, signs, icons and deliberate retro props.
- Verify every interaction and node has base, unavailable and completed visual coverage.

