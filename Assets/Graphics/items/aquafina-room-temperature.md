# Aquafina (Room Temperature)

> **Asset slug:** `aquafina-room-temperature`  
> **Type / slot:** Consumable — Status Cure  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Cures "Hungover," grants "Hydrated for Once" (immunity to Hangover, +1 HP regen) for 5 turns.

**Flavor text:** *"Tastes like tap water that costs $3. At least it's wet."*

**Why it's funny (the thing the art has to sell):** The most powerful hangover item in the game is a warm bottle of water, and the party treats it like a mythic relic. The art should be aggressively mundane.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A clear plastic single-serve water bottle, AQUAFINA, standing upright, about three-quarters full. The plastic is soft and slightly crumpled around the middle where it was gripped hard. The blue and white label is on crooked and has been peeled and re-stuck, with one bubbled corner. Blue screw cap, on tight. Zero condensation — the bottle is completely dry, warm, no droplets, no frost. A faint yellowish tint to the water. One small dent in the shoulder of the bottle.

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
#2B1A2E outline / #C6DDE4 water / #90B4BE water shadow / #EAF5F8 water highlight / #E8F1F4 plastic / #B0C4CA plastic shadow / #1B62B4 label blue / #10406F blue shadow / #F6F8F5 label white / #1B62B4 cap blue / #D8D8B8 warm tint / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Clear plastic single-serve water bottle labeled AQUAFINA three-quarters full, crumpled grip dent in the middle, crooked peeled and re-stuck blue and white label, blue screw cap, completely dry with no condensation, faint yellow tint to the water, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C6DDE4 water / #90B4BE water shadow / #EAF5F8 water highlight / #E8F1F4 plastic / #B0C4CA plastic shadow / #1B62B4 label blue / #10406F blue shadow / #F6F8F5 label white / #1B62B4 cap blue / #D8D8B8 warm tint / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Crushed empty variant** — for the floor-litter tileset and the 'Hydrated for Once' buff expiry gag.
- **Six-pack shrink-wrap variant** — for the Dodgy Off-License shelf.
- **Battle-use FX frame** — bottle tilted, a thin straight column of pale blue pixels pouring out, no splash arc.

## 6. Art-director notes

- Absence of condensation is the joke. Explicitly forbid water droplets, frost and cold-mist in every regeneration.
- The crumple dent should be a clear pixel indentation in the silhouette, not just shading.
- Blue is the only saturated color in the whole sprite — everything else stays washed. That contrast is what makes it read at 32px.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

