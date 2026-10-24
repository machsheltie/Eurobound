# Pager (Relic)

> **Asset slug:** `pager-relic`  
> **Type / slot:** Accessory — Relic  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Random "911" text grants an emergency Bravado surge once per dungeon.

**Flavor text:** *"Nobody has paged him in nineteen years. He keeps it charged."*

**Era Cringe:** Belt-clipped at all times. Checks it during conversations.

**Why it's funny (the thing the art has to sell):** A pager. In the present day. He checks it. Nothing has ever come through. The one time it does, it says 911 and it is a wrong number, and it is the most validated he has felt in a decade.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A small rectangular pager in translucent smoke-grey plastic, so you can dimly see the green circuit board shapes inside as blocky darker pixels. A narrow monochrome LCD strip across the top shows three characters of illegible pixel numerals and a tiny envelope icon. Two small rubber buttons below. A chunky spring-loaded metal belt clip on the back, visible at the three-quarter angle, bent slightly out of true. The plastic is scratched to a dull haze across the screen. A cracked corner has been repaired with a small square of silver duct tape — visually rhyming with `duct-tape-half-roll.md`. A single red LED pixel.

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
#2B1A2E outline / #6E6E78 smoke plastic / #46464E plastic shadow / #A8A8B4 plastic highlight / #2E6E4A circuit green / #1A4028 circuit shadow / #8EA894 LCD / #52685A LCD text / #A8AEB4 clip metal / #6E7278 clip shadow / #C9C4B8 duct tape / #E82424 LED red / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Small rectangular pager in translucent smoke-grey plastic showing dim green circuit board shapes inside, narrow monochrome LCD strip with three illegible pixel numerals and a tiny envelope icon, two small rubber buttons, chunky bent spring-loaded metal belt clip visible at three-quarter angle, dull hazed scratched screen, cracked corner patched with a small square of silver duct tape, one red LED pixel, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #6E6E78 smoke plastic / #46464E plastic shadow / #A8A8B4 plastic highlight / #2E6E4A circuit green / #1A4028 circuit shadow / #8EA894 LCD / #52685A LCD text / #A8AEB4 clip metal / #6E7278 clip shadow / #C9C4B8 duct tape / #E82424 LED red / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **911 alert FX frame (64x64)** — LCD lit, hard-edged pixel vibration ghost offset, four radiating jitter pixels, for the Bravado surge trigger.
- **Belt-clipped equipped variant (32x32)** — on a khaki waistband.
- **Dead variant** — LCD blank, for the between-dungeon cooldown state.

## 6. Art-director notes

- Translucent smoke plastic is the period-correct choice and it's more interesting than solid grey. Push the visible internals.
- The duct-tape patch is a deliberate cross-reference. Use the same tape colors as the duct tape sprite so the repair reads as in-universe.
- Belt clip must be visible in the main icon — it's the detail that says 'he wears this.'

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

