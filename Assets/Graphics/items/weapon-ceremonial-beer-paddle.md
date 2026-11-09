# Ceremonial Beer Paddle

> **Asset slug:** `weapon-ceremonial-beer-paddle`  
> **Type / slot:** Weapon — Lord Pilsner (Top Pick)  
> **World:** Global  
> **Rarity / tier:** Signature / Upgradeable  
> **Canon source:** `lordpilsnersweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Basic overhead swing with a chance to intimidate. Powers: Rush Week, Hazing Flashback, Brotherhood Bond, Alpha Sigma Slam.

**Flavor text:** *"The letters are barely visible now. He can still feel where they were."*

**Why it's funny (the thing the art has to sell):** A fraternity pledge paddle, wielded as a war club. It is the only object he owns that once meant he mattered to a group of people. He is now beating strangers with it in a foreign country.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A long wooden fraternity paddle held vertically, shaped like a broad flat oar with a narrow grip handle and a shoulder where the blade widens. The wood is a warm oak with a heavy visible grain rendered as irregular 1px darker striations. Across the blade, three large Greek-letter-shaped glyphs are wood-burned in, rendered as recessed dark blocky pixel forms, faded and worn shallow with two of the three nearly illegible. Below them, a column of small burned signature marks reduced to pixel noise. The blade is dinged and gouged along both edges with four visible impact dents and a split at the tip repaired with two brass tacks. The grip is wrapped in cracked black electrical tape. A lanyard hole is drilled through the handle with a frayed leather thong.

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
#2B1A2E outline / #A87C46 oak / #74501E oak shadow / #D8AE78 oak highlight / #5E3A16 grain dark / #2E1C0A burn mark / #1A1A1E tape black / #3A3A44 tape cracked / #C9A227 brass tack / #8A6E14 tack shadow / #8E6A3E leather thong / #C9BEA8 raw split wood / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Long wooden fraternity pledge paddle held vertically shaped like a broad flat oar with a narrow grip and a widening shoulder, warm oak with heavy 1px irregular grain striations, three large wood-burned Greek-letter-shaped glyphs on the blade rendered as recessed dark blocky pixel forms faded and worn with two nearly illegible, a column of small burned signature marks reduced to pixel noise, four impact dents and gouges along both edges, a split tip repaired with two brass tacks, cracked black electrical tape grip wrap, drilled lanyard hole with a frayed leather thong, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A87C46 oak / #74501E oak shadow / #D8AE78 oak highlight / #5E3A16 grain dark / #2E1C0A burn mark / #1A1A1E tape black / #3A3A44 tape cracked / #C9A227 brass tack / #8A6E14 tack shadow / #8E6A3E leather thong / #C9BEA8 raw split wood / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **TIER 1 — Weathered Pledge Paddle** — as described: faded letters, heavy damage, tape grip.
- **TIER 2 — Restored Chapter Paddle (64x64)** — the same paddle refinished: deep glossy varnish rendered as two hard highlight bands, letters re-burned crisp and dark, brass corner caps added, a proper leather grip wrap.
- **TIER 3 — Legendary President's Gavel (64x64)** — the paddle shortened and reshaped into a heavy gavel with an inlaid brass band, a polished hardwood head, and the three glyphs now in inlaid brass. Add four hard-edged gold pixel spokes behind it.
- **SMAAAASH crit FX frame (96x96)** — paddle at impact, three hard-edged wood splinter pixels flying, plus a blocky pixel shockwave arc.

## 6. Art-director notes

- Three tiers must share the same silhouette proportions so the battle animation rig does not need reworking. Only surface, color and small additions change.
- Greek-letter glyphs must be abstract blocky pixel forms, never actual Greek letters or a real organization's letters.
- The degradation-to-restoration arc is the character's whole story. Generate all three tiers in one session so the wood tone reads as the same paddle.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

