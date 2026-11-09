# BAWLS Guarana (Blue Bottle)

> **Asset slug:** `bawls-guarana-blue-bottle`  
> **Type / slot:** Consumable — Healing  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Restores moderate HP, grants "Hardcore Gamer" (+Speed, +Crit chance, -1 HP per turn) for 2 turns.

**Flavor text:** *"The nectar of LAN party gods. Tastes like commitment to the grind."*

**Why it's funny (the thing the art has to sell):** The bottle from every 2003 basement LAN party. The bumpy cobalt glass is instantly recognizable to exactly one demographic and that demographic is the target audience.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A cobalt-blue glass bottle with the distinctive raised bumps covering the entire body — render the bumps as a regular grid of 2x2 lighter-blue pixel clusters with a single highlight pixel each. Long neck, blue metal crown cap still on. The label is a small blue and silver wrap around the middle, slightly bubbled at the edge. The glass is deep saturated blue and mostly opaque, with one hard vertical highlight stripe down the left side. A ring of dried sticky residue around the base of the neck. Faint dust on the shoulders.

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
#2B1A2E outline / #12358E cobalt / #081C55 cobalt shadow / #2E5CC4 cobalt mid / #6E9AE8 bump highlight / #C4D8F8 glass highlight / #A8AEB4 cap silver / #6E7278 silver shadow / #E8E4D8 label / #8E7A3A residue / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Cobalt blue glass bottle covered in raised bumps rendered as a grid of lighter blue pixel clusters, long neck with blue crown cap on, small bubbled blue and silver label, hard vertical highlight stripe down the left, dried sticky residue ring around the neck base, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #12358E cobalt / #081C55 cobalt shadow / #2E5CC4 cobalt mid / #6E9AE8 bump highlight / #C4D8F8 glass highlight / #A8AEB4 cap silver / #6E7278 silver shadow / #E8E4D8 label / #8E7A3A residue / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Empty variant** — bottle clear-ish and dusty, cap off, for the LAN party set dressing.
- **Six-pack crate variant** — for the Dodgy Off-License shelf.
- **Battle-use FX frame** — bottle tilted, blue pixel stream, plus 4-6 floating hard-edged pixel sparks for the Hardcore Gamer buff.

## 6. Art-director notes

- The bumps ARE the recognition cue. If the generator smooths them out, add 'entire bottle surface covered in a regular grid of raised round bumps, clearly visible individual bumps.'
- Do not let the blue go purple. Cobalt with a slight green lean.
- At 32px the bump grid will alias badly — plan a simplified 3-row bump band for the small variant.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

