# Monster Energy (Original Formula)

> **Asset slug:** `monster-energy-original-formula`  
> **Type / slot:** Consumable — Party Revive (Mythic)  
> **World:** Global  
> **Rarity / tier:** Mythic  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Revive all party members + "Extreme" status (Double damage, cannot be stunned) for 3 turns.

**Flavor text:** *"Before they changed the recipe and ruined everything."*

**Why it's funny (the thing the art has to sell):** A mythic full-party revive that is a can of energy drink the party insists 'hits different' because it's the old formula. It is not the old formula. They cannot tell.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A tall matte-black energy drink can, MONSTER, with the three acid-green vertical claw slashes running down the front. The black is matte and dusty, not glossy. The can is cold-sweating with hard-edged pixel condensation droplets and a few frost pixels on the shoulder. A faded price sticker is stuck at an angle near the base with illegible pixel print. The tab is unopened. Framed as mythic: eight radiating hard-edged acid-green pixel spokes behind the can, blocky, plus four floating square green pixels rising off the top like embers, never soft or glowing.

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
#2B1A2E outline / #16161A matte black / #32323A black highlight / #0A0A0E black shadow / #8EF018 acid green / #4E9E0A green shadow / #C4FF6E green highlight / #DCE8EE condensation / #F4F8FA frost / #E8E2D2 price sticker / #B84A16 sticker red / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Tall matte black MONSTER energy drink can with three acid-green vertical claw slashes, dusty matte finish, hard-edged pixel condensation droplets and frost on the shoulder, faded crooked price sticker with illegible print, unopened tab, blocky pixelated acid-green radiating spokes behind it and four floating square green pixel embers rising off the top, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #16161A matte black / #32323A black highlight / #0A0A0E black shadow / #8EF018 acid green / #4E9E0A green shadow / #C4FF6E green highlight / #DCE8EE condensation / #F4F8FA frost / #E8E2D2 price sticker / #B84A16 sticker red / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Crushed variant** — can flattened, claw slashes distorted, for the floor-litter tileset.
- **Six-pack variant** — for the Dodgy Off-License premium shelf, sits next to the Four Loko rack.
- **Battle-use FX frame (96x96)** — can vertical center, full radiating green pixel burst, three party silhouette outlines rising, for the all-revive animation.

## 6. Art-director notes

- Matte, dusty black. These generators default to glossy soda-can render — expect to fight it. 'Matte, chalky, non-reflective, no highlights on the black' helps.
- Claw slashes must be hard-edged with no taper smoothing; three distinct strokes, uneven lengths.
- Mythic pairs with Sextuple Espresso as the two top-tier consumables. Keep their FX languages distinct: Espresso vibrates, Monster radiates.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

