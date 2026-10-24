# Money Clip (Empty)

> **Asset slug:** `money-clip-empty`  
> **Type / slot:** Accessory  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Wealth Illusion, -1 Actual Wealth.

**Flavor text:** *"For flashing non-existent cash with style."*

**Era Cringe:** Contains exactly three $1 bills and a Blockbuster card.

**Why it's funny (the thing the art has to sell):** The clip is chrome and confident. The contents are three singles and an expired video rental membership. The gap between the object's message and its contents is the entire character.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A polished chrome money clip, folded, holding a pathetically thin stack: three worn small-denomination banknotes rendered as pale green-grey pixel rectangles with illegible detail, plus one blue-and-yellow plastic membership card sticking out at an angle, its lettering illegible pixel noise. The clip's spring tension is far greater than the contents require, so the fold is nearly closed and the notes are crushed into a wrinkled wedge. The chrome is scratched, with two hard highlight bands and a smudged thumbprint. A small engraved monogram panel on the face, worn illegible. One note corner is torn.

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
#2B1A2E outline / #B4BAC0 chrome / #7A8086 chrome shadow / #EDF2F6 chrome highlight / #5A5E64 chrome dark / #A8B49E note green / #78846E note shadow / #D4DCC8 note highlight / #1E62B4 card blue / #F0C418 card yellow / #8E8A82 monogram / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Polished scratched chrome money clip folded almost fully shut because it holds only a pathetically thin crushed wedge of three worn pale green-grey banknotes plus one blue and yellow plastic membership card sticking out at an angle, illegible pixel lettering, two hard chrome highlight bands, smudged thumbprint, worn illegible engraved monogram panel, one torn note corner, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #B4BAC0 chrome / #7A8086 chrome shadow / #EDF2F6 chrome highlight / #5A5E64 chrome dark / #A8B49E note green / #78846E note shadow / #D4DCC8 note highlight / #1E62B4 card blue / #F0C418 card yellow / #8E8A82 monogram / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Flashing variant (48x48)** — clip held up open, notes fanned to look like more than three, for the Wealth Illusion buff icon.
- **Truly-empty variant** — clip alone, nothing in it.
- **Pairs with** `chain-wallet-3-foot-chain.md` — generate both in one session so the leather and chrome languages stay consistent.

## 6. Art-director notes

- Three notes. Exactly three. If the generator gives you a fat roll, regenerate — the emptiness is the joke.
- Chrome is hard for these models; two hard bands and a dark core reads better than trying to render true reflection.
- The membership card should read as obviously expired-era plastic: flat two-tone, no chip, no hologram.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

