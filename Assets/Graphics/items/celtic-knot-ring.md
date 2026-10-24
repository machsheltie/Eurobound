# Celtic Knot Ring (From a Mall Kiosk)

> **Asset slug:** `celtic-knot-ring`  
> **Type / slot:** Ring  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Mystique, +1 Fake Heritage.

**Flavor text:** *"Represents his 'deep connection' to Ireland (via a suburb)."*

**Era Cringe:** Turns finger green within hours.

**Why it's funny (the thing the art has to sell):** He has a deep spiritual connection to a country he has never visited, purchased for nineteen dollars next to a pretzel stand. In Publandia he will tell an actual local about it.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A band ring at a three-quarter angle with a raised interlaced knotwork pattern running around the entire circumference, rendered as chunky woven pixel strands with clear over-under crossings. The metal is a pale silver-tone plating that has flaked away in three visible patches, exposing dull yellow base alloy underneath. Heavy verdigris green is packed into every recess of the knotwork, and a green residue ring marks the inside of the band. The knotwork casting is soft and imprecise — the strands are unevenly thick and one crossing is malformed where the mold failed. A hairline crack runs through the band on one side. Faint illegible pixel stamp marks inside the band.

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
#2B1A2E outline / #B4BAC0 plating silver / #7A8086 plating shadow / #E8EEF2 plating highlight / #A89A5E base alloy / #7E7038 alloy shadow / #4E8E5E verdigris / #2E5E38 verdigris dark / #6EB87E verdigris highlight / #8E8A82 crack line / #5E5A54 recess dark / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Band ring at a three-quarter angle with a raised interlaced Celtic knotwork pattern running around the whole circumference rendered as chunky woven pixel strands with clear over-under crossings, pale silver-tone plating flaked away in three patches exposing dull yellow base alloy, heavy verdigris green packed into every knotwork recess and a green residue ring inside the band, soft imprecise casting with unevenly thick strands and one malformed crossing where the mold failed, hairline crack in the band, faint illegible stamp marks inside, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #B4BAC0 plating silver / #7A8086 plating shadow / #E8EEF2 plating highlight / #A89A5E base alloy / #7E7038 alloy shadow / #4E8E5E verdigris / #2E5E38 verdigris dark / #6EB87E verdigris highlight / #8E8A82 crack line / #5E5A54 recess dark / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Green-finger variant (32x32)** — matching the mood ring's discoloration gag, so the player sees he wears two rings that both do this.
- **Ring shelf lineup** — include in the four-ring velvet pad display with the class, mood and spinner rings.
- **Publandia-boosted variant** — same ring with three hard-edged gold sparkle pixels, for the +Mystique proc in Publandia only.

## 6. Art-director notes

- Knotwork must have visible over-under crossings or it reads as a texture instead of a knot. Chunky strands, clear weave.
- The malformed crossing is the cheap-casting tell. One bad crossing only — more and it stops reading as knotwork.
- Verdigris links this to the mood ring visually. Use the identical greens so the two read as a matched set of skin-staining garbage.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

