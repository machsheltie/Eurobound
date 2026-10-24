# Sextuple Espresso (Gas Station Special)

> **Asset slug:** `sextuple-espresso-gas-station`  
> **Type / slot:** Consumable — Full Party Heal (Mythic)  
> **World:** Global  
> **Rarity / tier:** Mythic  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Full HP restore to entire party, grants "Heart Palpitations" (+Priority next turn, minor HP tick damage) for 3 turns.

**Flavor text:** *"Six shots of liquid regret. Your heart beats in morse code."*

**Why it's funny (the thing the art has to sell):** Six shots pulled from a gas station machine into one styrofoam cup with a lid that does not fit. The cup is visibly straining. Mythic tier.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A tall white styrofoam cup, over-filled, with a black plastic lid that is clearly not seated correctly on one side. Dark near-black coffee is welling up through the sip hole and running down the outside in two thick drips. The cup wall is bulging and stress-marked. A thin brown cardboard sleeve is on crooked. The whole cup is vibrating — render motion as a hard-edged 1px double-image ghost offset to the right in a lighter tone, blocky and pixelated, not blurred. Six tiny pixel jitter-lines radiate from the sides. A faint gas-station receipt is stuck to the base.

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
#2B1A2E outline / #F4F2EC styrofoam / #C9C6BC styrofoam shadow / #FFFFFF styrofoam highlight / #1E1410 coffee / #3A2A1E coffee mid / #5C4630 coffee highlight / #2A2A2E lid / #4A4A50 lid highlight / #A87C4A sleeve / #6E4E2A sleeve shadow / #D8D4C8 ghost offset / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Tall white styrofoam coffee cup badly overfilled, black plastic lid not seated on one side, near-black coffee welling through the sip hole and running down in thick drips, bulging stressed cup wall, crooked cardboard sleeve, hard-edged 1px pixel ghost double-image showing it vibrating, receipt stuck to the base, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #F4F2EC styrofoam / #C9C6BC styrofoam shadow / #FFFFFF styrofoam highlight / #1E1410 coffee / #3A2A1E coffee mid / #5C4630 coffee highlight / #2A2A2E lid / #4A4A50 lid highlight / #A87C4A sleeve / #6E4E2A sleeve shadow / #D8D4C8 ghost offset / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Crushed variant** — cup flattened, brown stain spreading, for the post-battle floor.
- **Machine variant** — the gas station espresso machine itself, mid-pour, as a 48x48 overworld prop.
- **Battle-use FX frame** — cup at maximum vibration, three ghost offsets instead of one, jitter lines doubled.

## 6. Art-director notes

- The vibration ghost is the mythic tier signal. Keep it a hard-edged solid-color offset copy — never motion blur.
- Cup must read as styrofoam, not paper. Slightly bulged sides, matte, one visible seam ridge.
- Mythic renders 1.25x footprint like Four Loko. Tall silhouette, keep the lid overhang wide so it doesn't read as a soda cup at 32px.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

