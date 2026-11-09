# Metronome Pendant (Constantly Ticking)

> **Asset slug:** `metronome-pendant`  
> **Type / slot:** Necklace — Regional  
> **World:** Sinfonia  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Rhythm, +1 Time Awareness, -2 Social Situations.

**Flavor text:** *"Keeps perfect time while driving everyone insane."*

**Era Cringe:** Tick-tick-tick never stops, even during romantic moments or funeral services.

**Why it's funny (the thing the art has to sell):** A working wind-up metronome shrunk to pendant size and worn around the neck. It cannot be stopped or muted. He thinks it makes him seem musical. It has ended two conversations tonight.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A miniature wind-up metronome worn as a pendant, hanging from a tarnished brass chain, seen face-on with its front cover removed so the mechanism is exposed. The body is a small lacquered mahogany-brown pyramid with a brass winding key on the side. The steel pendulum rod is captured mid-swing, tilted off-vertical, with a small brass weight partway up it — and its motion is rendered as two hard-edged 1px ghost copies of the rod offset to either side in a lighter tone, blocky, never blurred. A tiny illegible pixel tempo scale runs up the interior. Three short hard-edged pixel tick-marks radiate from the top corner to indicate sound. The lacquer is chipped at two corners revealing pale bare wood. The brass is spotted with dark tarnish.

STYLE RULES — follow all of them:
- Medium: 1990s Super Nintendo item sprite, drawn in the visual language of *EarthBound / MOTHER 2*.
- Framing: one single object, centered, slight three-quarter front view, floating on a flat pure-magenta `#FF00FF` chroma-key field. Nothing else in frame.
- Pixels: chunky, deliberate, visible square pixels. No anti-aliasing. No soft gradients. No blur. Ordered/checkerboard dither only, used sparingly.
- Palette: hard limit of 16 colors (15 + transparency), SNES 15-bit-safe. Warm and a little grubby — brick red, mustard, dull teal, muddy denim, off-cream. Never neon-clean.
- Outline: 1px dark plum-brown `#2B1A2E`, never pure black. Outline thickens by one pixel on the underside of the object.
- Shading: flat cel shading, exactly three tones per material — base, one shadow, one highlight — plus a single hard specular pixel-cluster. Light source upper-left.
- Form language: slightly lumpy and hand-sculpted, as though the object were built out of modeling clay, photographed, then reduced to pixels — the MOTHER 2 clay-model look. Edges bulge. Nothing is perfectly straight or perfectly symmetrical.
- Shadow: one small hard-edged elliptical drop shadow directly beneath the object, no blur, 1 tone darker than the key field.
- Readability: the silhouette must still read as the correct object when scaled down to 32x32.

PALETTE — use these and nothing else:
#2B1A2E outline / #6E3A1E mahogany / #421E0E mahogany shadow / #9E6238 mahogany highlight / #C9BE8E bare wood / #C9A227 brass / #8A6E14 brass shadow / #F0D874 brass highlight / #4A423A tarnish spot / #A8AEB4 steel rod / #D8DEE4 rod ghost / #E8EEF2 tick mark / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Miniature wind-up metronome worn as a pendant hanging from a tarnished brass chain, face-on with the front cover removed exposing the mechanism, small lacquered mahogany-brown pyramid body with a brass winding key on the side, steel pendulum rod captured mid-swing tilted off-vertical with a small brass weight partway up, motion rendered as two hard-edged 1px lighter ghost copies of the rod offset to either side and never blurred, tiny illegible pixel tempo scale up the interior, three short hard-edged pixel tick-marks radiating from the top corner, lacquer chipped at two corners revealing pale bare wood, dark tarnish spotting the brass, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #6E3A1E mahogany / #421E0E mahogany shadow / #9E6238 mahogany highlight / #C9BE8E bare wood / #C9A227 brass / #8A6E14 brass shadow / #F0D874 brass highlight / #4A423A tarnish spot / #A8AEB4 steel rod / #D8DEE4 rod ghost / #E8EEF2 tick mark / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (48x48)** — around a neck silhouette over formal wear, pendulum mid-swing.
- **Silent variant** — pendulum vertical and still, no ghosts, no tick marks, for the inventory icon.
- **Social Situations debuff icon (24x24)** — the pendulum plus three tick marks and a tiny turned-away NPC silhouette.

## 6. Art-director notes

- Two ghost copies of the pendulum, hard-edged, lighter tone, offset either side. This is the same motion technique as the spinner ring and the espresso cup — keep all three consistent.
- Exposed mechanism is the right call: a closed metronome reads as a wooden block at 32px.
- This is the most 'crafted' sprite in the Sinfonia set. Let the wood and brass look genuinely nice — the joke is the context, not the object.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

