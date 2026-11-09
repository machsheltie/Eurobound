# Class Ring (High School)

> **Asset slug:** `class-ring-high-school`  
> **Type / slot:** Ring  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Nostalgia, +2 Peak Achievement.

**Flavor text:** *"Still fits if you don't eat for three days."*

**Era Cringe:** Worn on dates to show 'accomplishments'.

**Why it's funny (the thing the art has to sell):** A high school class ring on a thirty-eight-year-old hand. Not college. High school. He wears it on dates. He brings it up.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A chunky gold-tone class ring standing upright at a three-quarter angle so both the face and one shank are visible. Enormous square face set with a deep synthetic red stone, faceted and rendered with three hard flat facet planes. The shanks are heavily sculpted with raised illegible pixel motifs — a shield shape on one side, blocky year numerals on the other, and a tiny sports-ball form. The gold plating has worn through to dull grey-white base metal across the high points of both shanks. The band is visibly narrow relative to the face, and there is a small sizing gap where it was resized badly, with a mismatched solder seam. Skin grime packed into the engraving recesses.

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
#2B1A2E outline / #C9A227 gold / #8A6E14 gold shadow / #F0D874 gold highlight / #8E8A82 worn base metal / #5E5A54 base shadow / #B4241E stone red / #6E0E0A stone shadow / #E86E5E stone facet / #FBAE9E stone highlight / #4A423A grime / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Chunky gold-tone high school class ring standing upright at a three-quarter angle showing the face and one shank, enormous square face set with a deep faceted synthetic red stone rendered in three hard flat facet planes, heavily sculpted shanks with raised illegible pixel motifs including a shield shape and blocky year numerals, gold plating worn through to dull grey-white base metal on the high points, narrow band relative to the face with a badly resized mismatched solder seam, skin grime packed into the engraving recesses, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C9A227 gold / #8A6E14 gold shadow / #F0D874 gold highlight / #8E8A82 worn base metal / #5E5A54 base shadow / #B4241E stone red / #6E0E0A stone shadow / #E86E5E stone facet / #FBAE9E stone highlight / #4A423A grime / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (32x32)** — on a thick finger, the band visibly biting into the skin. The 'still fits if you don't eat' line, rendered.
- **Ring shelf lineup (96x48)** — this plus the mood, spinner and Celtic knot rings on a velvet pad, for the shop display.
- **Alt stone** — blue and green synthetic stones, for palette-swap stock.

## 6. Art-director notes

- Oversize the face relative to the band. Class rings are architecturally absurd and that's free comedy.
- Worn-through plating on the high points is the single best age signal on any metal item. Reuse this treatment across all four rings.
- Never render legible school names or years. Blocky abstract glyphs only.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

