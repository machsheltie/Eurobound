# Fanny Pack (Worn Frontally)

> **Asset slug:** `fanny-pack-worn-frontally`  
> **Type / slot:** Accessory  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Item Slots, +5 Tourist Vibes.

**Flavor text:** *"For hands-free storage of emergency snacks and dignity."*

**Era Cringe:** Worn over the shirt for 'easy access'.

**Why it's funny (the thing the art has to sell):** Worn on the front. Over the shirt. Stuffed past capacity. It is a tourist beacon visible from orbit.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A nylon fanny pack in faded teal and purple with a black zip, seen three-quarter front and packed so full the fabric is drum-tight and the zip is straining with a visible gap at the pull. A rolled paper map, a water bottle neck and a passport corner protrude from the gap. The black plastic side-release buckle is sun-faded to grey and one prong is cracked. The webbing strap is twisted and the loose tail dangles unsecured. A small key ring hangs off the zip pull. Bleached patches where the color has faded unevenly. A dried food smear near the bottom seam.

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
#2B1A2E outline / #2E8E96 teal / #175E64 teal shadow / #5EC4CC teal highlight / #6E3E96 purple / #42225E purple shadow / #A46ED8 purple highlight / #2A2A2E zip black / #8E8A82 faded buckle / #E8E2D2 map paper / #C9A56E passport / #8E6E3A food smear / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Nylon fanny pack in faded teal and purple with a black zip, three-quarter front, packed drum-tight so the zip strains open at the pull with a rolled map, water bottle neck and passport corner protruding, sun-faded grey side-release buckle with a cracked prong, twisted webbing strap with a dangling loose tail, key ring on the zip pull, uneven bleached patches, dried food smear near the bottom seam, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #2E8E96 teal / #175E64 teal shadow / #5EC4CC teal highlight / #6E3E96 purple / #42225E purple shadow / #A46ED8 purple highlight / #2A2A2E zip black / #8E8A82 faded buckle / #E8E2D2 map paper / #C9A56E passport / #8E6E3A food smear / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn-frontally equipped variant (48x48)** — strapped across a torso silhouette at navel height, for the character equip preview.
- **Empty deflated variant** — for the emptied-inventory state.
- **Contents-spilled variant** — pack on its side with the map, bottle and passport scattered, for the pickpocket-fail cutscene.

## 6. Art-director notes

- Over-stuffing is the gag. If it looks like it closes comfortably, add 'grossly overpacked, fabric stretched drum-tight, zipper visibly straining and gapping.'
- Teal and purple is the exact 1994 colorway — resist any modern neutral.
- Front-worn is a positional joke that only lands in the equipped variant, so prioritize generating that one.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

