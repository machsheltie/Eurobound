# SET: The Tech Bro Wannabe

> **Asset slug:** `set-the-tech-bro-wannabe`  
> **Type / slot:** Special Combo Set  
> **World:** Global  
> **Rarity / tier:** Set Bonus  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Backwards Trucker Hat + Deep V-Neck + Cargo Shorts + BlackBerry. Bonus: +5 Innovation Points, +3 Startup Delusions.

**Flavor text:** *"He has an idea. It is an app. It already exists."*

**Why it's funny (the thing the art has to sell):** A costume assembled from what he thinks successful people wear, sourced entirely from 2009. He has a pitch. He will give it to you unprompted, in a hostel kitchen, at 2am.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A four-piece outfit laid out as a flat-lay set sheet in a vertical column on the magenta field: at the top the backwards mesh trucker cap seen from the rear, below it the deep V-neck heather grey tee with the hemp necklace draped in the V, below that the overstuffed lumpy khaki cargo shorts, and at the bottom the glossy black BlackBerry Pearl lying flat. Each piece is a separate object with its own outline and small drop shadow, evenly spaced with clear gaps. Three small hard-edged gold pixel plus-signs sit between the pieces. The phone at the bottom is angled slightly, screen up.

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
Combined from the four member items. Key anchors: #2B1A2E outline / #A83A2E cap brick red / #E8E4D8 cap mesh / #9EA0A4 heather grey / #C9A870 hemp tan / #C4B48E khaki / #16161A phone black / #C9A227 plus-sign gold / #6E5F72 cast shadow / #FF00FF chroma key. Must index to 16 colors total.

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Four-piece outfit flat-lay set sheet in a vertical column, backwards mesh trucker cap seen from the rear at top, deep V-neck heather grey tee with hemp necklace draped in the V below, overstuffed lumpy khaki cargo shorts below that, glossy black BlackBerry Pearl lying flat and slightly angled screen-up at the bottom, each piece a separate object with its own outline and small drop shadow evenly spaced with clear gaps, three hard-edged gold pixel plus-signs between, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
Combined from the four member items. Key anchors: #2B1A2E outline / #A83A2E cap brick red / #E8E4D8 cap mesh / #9EA0A4 heather grey / #C9A870 hemp tan / #C4B48E khaki / #16161A phone black / #C9A227 plus-sign gold / #6E5F72 cast shadow / #FF00FF chroma key. Must index to 16 colors total.
```

## 5. Variants to generate in the same session

- **Equipped full-body variant (64x96)** — worn on a character silhouette, phone in hand, mid-pitch gesture.
- **Set-bonus badge (32x32)** — a tiny lightbulb-and-phone combination icon for the Startup Delusions buff.
- **Pitch-deck prop (48x32)** — a single crumpled printed slide with illegible pixel bullet points, as a bonus quest item.

## 6. Art-director notes

- Same rule: generate members first, harvest their palettes, then compose the sheet.
- This set's palette is much duller than the Full Frat Bro's — that contrast is intentional and reads as 'he thinks this is the mature version.'
- The pitch-deck prop is worth building. It's a free gag and it slots into the bulletin-board system.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

