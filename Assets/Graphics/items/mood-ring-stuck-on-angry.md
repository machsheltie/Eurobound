# Mood Ring (Stuck on 'Angry')

> **Asset slug:** `mood-ring-stuck-on-angry`  
> **Type / slot:** Ring  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Emotion Detection, +1 Perpetual Rage.

**Flavor text:** *"The crystal knows what's in your heart: disappointment."*

**Era Cringe:** Leaves green marks on finger.

**Why it's funny (the thing the art has to sell):** The stone is frozen on the angry color. The ring is also dyeing his finger green. Both facts have been true for years and neither has prompted action.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A slim mood ring standing upright at a three-quarter angle. The oval liquid-crystal stone is a dull muddy amber-brown, flat and lifeless — stuck on the 'angry' reading — with a small dead patch in one corner where the crystal has failed entirely and gone grey. Two hard specular pixels on the dome. The band is thin base metal with the silver plating almost entirely gone, showing coppery-brass underneath and heavy verdigris green built up along the inside edge and around the stone setting. A visible green residue smear on the outer band where it has been transferring to skin. The setting prongs are bent, one splayed outward. A hairline crack across the stone.

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
#2B1A2E outline / #8E6A2E stone amber / #5E4418 amber shadow / #B89250 amber highlight / #7E7A74 dead patch grey / #A88E5E brass / #6E5A32 brass shadow / #C9BE8E brass highlight / #4E8E5E verdigris / #2E5E38 verdigris dark / #C4C8CC plating remnant / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Slim mood ring standing upright at a three-quarter angle, the oval liquid-crystal stone a dull muddy amber-brown flat and lifeless with a small grey dead patch where the crystal failed, two hard specular pixels on the dome, thin base metal band with the silver plating almost entirely gone showing coppery brass and heavy verdigris green built up along the inside edge and setting, green residue smear on the outer band, bent setting prongs with one splayed outward, hairline crack across the stone, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #8E6A2E stone amber / #5E4418 amber shadow / #B89250 amber highlight / #7E7A74 dead patch grey / #A88E5E brass / #6E5A32 brass shadow / #C9BE8E brass highlight / #4E8E5E verdigris / #2E5E38 verdigris dark / #C4C8CC plating remnant / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Green-finger variant (32x32)** — the ring on a finger with an unmistakable green band of skin discoloration beneath it. Generate this; it's the payoff.
- **Chart card variant** — the mood-chart insert, water-damaged, cross-referencing `mood-necklace-perpetually-black.md`.
- **Working variant** — stone lit blue-green, for the same one-time panic gag as the necklace.

## 6. Art-director notes

- Muddy amber, not a pretty color. This stone should look broken, not moody.
- Verdigris is the character. Build it up thick in the crevices — three or four green tones if the palette allows.
- Pair this generation session with the mood necklace so both dead stones share a rendering language.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

