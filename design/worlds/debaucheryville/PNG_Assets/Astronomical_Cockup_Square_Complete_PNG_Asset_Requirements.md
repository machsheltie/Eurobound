# Astronomical Cock-Up Square - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_oldtown_astronomical_cockup_square_01`
- **Authoritative slug:** `astronomical_cockup_square`
- **Engine:** Godot 4.4
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

A sincere Gothic Old Town square overwhelmed by tourist density, scam stalls and phone flashes.

## Required Scene Layers

- Clock tower and astronomical dial hero façade
- Crowd and hourly-show density states
- Vendor ring with viewing-spot pillar, monk rug, Clock Wine cart and merchandise tables
- Euro Ink alley sightline and roaming wristband seller territory

## Required Asset Families

- **square architecture** — `astronomical_square_environment.png`; base, active, completed/closed and emission-mask states as applicable.
- **clock show** — `astronomical_clock_show.png`; base, active, completed/closed and emission-mask states as applicable.
- **vendor cluster** — `astronomical_square_vendors.png`; base, active, completed/closed and emission-mask states as applicable.
- **crowds** — `astronomical_square_crowds.png`; base, active, completed/closed and emission-mask states as applicable.
- **quest/UI** — `astronomical_square_ui.png`; base, active, completed/closed and emission-mask states as applicable.

## Accessibility Assets

- Reduced-flash and reduced-motion overlays.
- High-contrast interaction outlines and exit arrows.
- Text/icon substitutes for audio, color and timing-only cues.
- Clean plates with particles, crowds and distortion removed.

## Godot 4.4 Delivery

- Preserve every filename referenced by `sprite_mapping/astronomical_cockup_square_sprite_mapping.json`.
- Supply color, alpha, normal/emission masks and atlas metadata where the current mapping expects them.
- Use painterly environmental layers; reserve pixel art for screens, signs, icons and deliberate retro props.
- Verify every interaction and node has base, unavailable and completed visual coverage.

