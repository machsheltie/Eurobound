# Guinness (Room Temperature)

> **Asset slug:** `guinness-room-temperature`  
> **Type / slot:** Consumable — Regional Specialty  
> **World:** Publandia  
> **Rarity / tier:** Uncommon  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Gradual HP restore + "Philosophical" (wisdom buffs but slower reactions).

**Flavor text:** *"Tastes like liquid Ireland."*

**Why it's funny (the thing the art has to sell):** A pint of stout that has been sitting untouched long enough for the head to collapse into a sad ring. Someone ordered it to seem local and then didn't want it.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A pint glass of stout with the classic tulip profile, filled with near-black liquid that reads as very dark brown-black rather than pure black. The head has collapsed — only a thin uneven cream-colored ring clings to the glass rim with a few clumped bubbles, not a proper dome. Lacing rings from previous sips are etched down the inside of the glass as three or four faint horizontal pale lines. The glass is warm: absolutely no condensation, and one greasy thumbprint smudge on the side. A soggy beer mat sticks to the bottom of the glass. A single dead fruit fly floats in the collapsed head.

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
#2B1A2E outline / #1A0E08 stout black / #2E1A0E stout mid / #4A2A14 stout highlight / #E8DCC4 head cream / #C4B896 head shadow / #FBF4E4 head highlight / #C4D8DC glass / #8EA4A8 glass shadow / #A89478 beer mat / #7E6E52 mat shadow / #2A2018 fruit fly / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Tulip-profile pint glass of near-black stout with a collapsed head reduced to a thin uneven cream ring with clumped bubbles, faint horizontal lacing lines etched down the inside, absolutely no condensation, greasy thumbprint smudge, soggy beer mat stuck to the base, one dead fruit fly in the foam, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1A0E08 stout black / #2E1A0E stout mid / #4A2A14 stout highlight / #E8DCC4 head cream / #C4B896 head shadow / #FBF4E4 head highlight / #C4D8DC glass / #8EA4A8 glass shadow / #A89478 beer mat / #7E6E52 mat shadow / #2A2018 fruit fly / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Fresh-pour variant** — full domed head, cascading surge rendered as horizontal pixel bands. For the Publandia shop shelf, so the contrast between fresh and abandoned is visible.
- **Empty-with-lacing variant** — for the bar-top litter tileset.
- **Philosophical status icon (24x24)** — the pint with three small stepped thought-dot pixels rising.

## 6. Art-director notes

- The collapsed head is the entire joke. Absolutely no dome. If the generator gives you a perfect creamy head, regenerate with 'foam head has completely collapsed, only a thin patchy uneven ring remains, mostly bare liquid surface.'
- No condensation, no frost, no cold. Room temperature is the item name.
- The fruit fly is one dark pixel. Worth it.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

