# Frosted Tips Hair Gel (Permanent)

> **Asset slug:** `frosted-tips-hair-gel-permanent`  
> **Type / slot:** Head Gear  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Charm, +1 Embarrassment.

**Flavor text:** *"Like icicles, but make it Chad."*

**Era Cringe:** Requires 45 minutes of morning prep time.

**Why it's funny (the thing the art has to sell):** This is a head-slot item that is technically a hairstyle. The bleach has fried it. The spikes are load-bearing. He does this every single morning, in hostels, in front of other people.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A disembodied hairstyle — a helmet-shaped mass of short gelled hair floating as an object, no head, no face, no skin. Dark ash-brown at the roots transitioning in a hard stepped band to bleached straw-yellow at the tips, with no blending, three distinct color steps only. The whole mass is sculpted into a dozen stiff forward-swept spikes, each with a hard specular highlight pixel at the tip. The texture reads as crunchy and lacquered, not soft. A few over-bleached strands are visibly damaged, rendered as paler frizzed pixels breaking the silhouette. A small applicator tub sits below and to the right, lid off, teal gel visible — the same tub as `hair-gel-industrial-strength.md`.

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
#2B1A2E outline / #4A3A2A root brown / #2E2418 root shadow / #6E5A42 root mid / #C9A85E tip straw / #E8D89E tip bleached / #FBF4D8 tip highlight / #A89268 damaged strand / #16C4C4 gel teal / #0A7E86 teal shadow / #1A1A1E tub black / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Disembodied helmet-shaped mass of short gelled hair floating with no head or face, dark ash-brown roots transitioning in hard stepped bands with no blending to bleached straw-yellow tips, sculpted into a dozen stiff forward-swept crunchy lacquered spikes each with a hard specular highlight pixel, a few paler frizzed damaged strands breaking the silhouette, small open gel tub with teal gel below right, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #4A3A2A root brown / #2E2418 root shadow / #6E5A42 root mid / #C9A85E tip straw / #E8D89E tip bleached / #FBF4D8 tip highlight / #A89268 damaged strand / #16C4C4 gel teal / #0A7E86 teal shadow / #1A1A1E tub black / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Equipped variant (48x48)** — the hairstyle on a head silhouette with a receding hairline, so the frosted tips sit on a visibly thinning scalp.
- **Grown-out variant** — dark roots two inches deep, for the late-game 'he stopped maintaining it' beat.
- **Charm buff FX (32x32)** — three hard-edged sparkle pixel crosses over the spikes.

## 6. Art-director notes

- Hard stepped color bands, no gradient. The bad frosting job IS the visual. Any smooth ombré and the joke dies.
- The receding hairline only appears in the equipped variant, and it should be unmistakable. That contrast is the payload.
- Spike tips should break the silhouette raggedly — this is the one sprite where a clean outline would be wrong.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

