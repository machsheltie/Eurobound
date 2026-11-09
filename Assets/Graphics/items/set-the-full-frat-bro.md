# SET: The Full Frat Bro

> **Asset slug:** `set-the-full-frat-bro`  
> **Type / slot:** Special Combo Set  
> **World:** Global  
> **Rarity / tier:** Set Bonus  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Frosted Tips + Popped Collar + JNCO Jeans + Puka Shells. Bonus: +10 Nostalgia, +5 Cringe Resistance, -3 Dating Prospects.

**Flavor text:** *"He looks exactly like he did in the yearbook photo. That is the problem."*

**Why it's funny (the thing the art has to sell):** Four separate bad decisions that, worn together, become one coherent and much worse decision. The set bonus is that he stops being embarrassed, which is not an improvement.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A four-piece outfit laid out as a flat-lay set sheet, arranged head-to-toe in a vertical column on the magenta field: at the top the disembodied frosted-tips hairstyle, below it the layered salmon-over-mint popped-collar polos, below that the enormous bell-flared JNCO jeans, and at the bottom the puka shell necklace laid in a circle beside the jeans' hem. Each piece is rendered as its own separate object with its own outline and its own small drop shadow, evenly spaced with clear gaps between them — this is a set sheet, not a costume on a body. Between the pieces, three small hard-edged gold pixel plus-signs indicate the combination.

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
Combined from the four member items. Key anchors: #2B1A2E outline / #C9A85E frosted tip / #E8907E salmon polo / #8ED8A8 mint polo / #3E5E96 denim / #EDE8D8 puka shell / #C9A227 plus-sign gold / #6E5F72 cast shadow / #FF00FF chroma key. Total set sheet must still index to 16 colors — plan the shared palette before generating the members.

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Four-piece outfit flat-lay set sheet arranged head-to-toe in a vertical column, disembodied frosted-tips hairstyle at top, layered salmon-over-mint popped-collar polos below, enormous bell-flared JNCO jeans below that, puka shell necklace laid in a circle at the bottom, each piece a separate object with its own outline and small drop shadow evenly spaced with clear gaps, three small hard-edged gold pixel plus-signs between the pieces, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
Combined from the four member items. Key anchors: #2B1A2E outline / #C9A85E frosted tip / #E8907E salmon polo / #8ED8A8 mint polo / #3E5E96 denim / #EDE8D8 puka shell / #C9A227 plus-sign gold / #6E5F72 cast shadow / #FF00FF chroma key. Total set sheet must still index to 16 colors — plan the shared palette before generating the members.
```

## 5. Variants to generate in the same session

- **Equipped full-body variant (64x96)** — all four pieces worn on a single character silhouette. This is the set-bonus screen art and the funniest asset in the equipment set.
- **Set-bonus badge (32x32)** — a small icon combining the popped collar and a frosted spike, for the buff strip.
- **Before/after pair** — the same silhouette with and without the set, for the shop's hard-sell display.

## 6. Art-director notes

- Generate the four member items FIRST, then build the set sheet from their finished palettes. Do not generate the set independently or the colors will drift.
- Even spacing and clear gaps are what make this read as a set sheet rather than a mess. Enforce them.
- The 16-color cap is genuinely tight across four items. Consider dropping each member to 3 tones instead of 4 for this sheet.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

