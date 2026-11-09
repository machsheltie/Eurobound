# Chug of the Gods (Mystery Beer)

> **Asset slug:** `chug-of-the-gods-mystery-beer`  
> **Type / slot:** Consumable — Party Heal  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Heal moderate HP to party, 15% chance inflicts "Sloppy" (-Accuracy) for 1 turn.

**Flavor text:** *"Found behind a radiator. Surprisingly refreshing."*

**Why it's funny (the thing the art has to sell):** Nobody knows what brand this is. The label has been steam-warped into illegibility. It has been behind that radiator since at least one lease ago and they are drinking it anyway.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single unlabeled-ish beer can, dented near the middle, standing slightly off-vertical. The aluminum is dull grey-silver with a green and gold label that has been heat-warped and bubbled — the printing is smeared into unreadable pixel mush, no legible letters, just suggestive color blocks. A furry grey layer of radiator dust clings to the top rim and shoulder of the can. The pull tab is already popped and bent back. A thin dark drip runs from the mouth down one side. Faint rust-orange speckling near the base.

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
#2B1A2E outline / #A8ACB0 aluminum / #6E7276 aluminum shadow / #D8DCE0 aluminum highlight / #2F6B34 label green / #1B3F1E green shadow / #C7A227 label gold / #8A6E14 gold shadow / #8E8578 dust grey / #B84A16 rust / #3A2E1E drip / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Dented unbranded beer can standing crooked, dull silver aluminum with a heat-warped bubbled green and gold label smeared unreadable, grey dust fuzz on the rim, popped bent pull tab, dark drip down the side, rust speckle at base, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A8ACB0 aluminum / #6E7276 aluminum shadow / #D8DCE0 aluminum highlight / #2F6B34 label green / #1B3F1E green shadow / #C7A227 label gold / #8A6E14 gold shadow / #8E8578 dust grey / #B84A16 rust / #3A2E1E drip / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Crushed variant** — post-use, flattened, for the floor-litter tileset in Temple Bar Alley.
- **Three-can cluster** — for the 'found a whole stash' loot drop.
- **Battle-use FX frame** — can tipped fully vertical, foam arc of hard-edged white pixels shooting up out of frame.

## 6. Art-director notes

- The unreadability is load-bearing. If the generator produces legible brand text, add 'label print completely melted and illegible, no readable letters' and regenerate.
- Radiator dust should read as fuzz — a jagged 1-2px irregular grey fringe on the top edges only, never on the front face.
- Keep the can dented but not crushed; crushed is the separate variant.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

