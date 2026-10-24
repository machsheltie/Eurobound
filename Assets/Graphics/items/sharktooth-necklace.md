# Sharktooth Necklace (Souvenir Shop Special)

> **Asset slug:** `sharktooth-necklace`  
> **Type / slot:** Necklace  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Intimidation against surfers, +1 Fake Danger.

**Flavor text:** *"Definitely from a real shark (plastic mold #47)."*

**Era Cringe:** Worn to intimidate people who've never seen the ocean.

**Why it's funny (the thing the art has to sell):** The tooth is plastic. The mold number is faintly visible on the back. He tells a story about how he got it that involves an actual shark and a boat.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single large pendant tooth hanging from a black leather cord, laid flat with the cord in a shallow loop. The tooth is off-white with a beige root section, but it is unmistakably molded plastic — a visible mold seam line runs straight down both edges, the surface is too smooth and slightly glossy, and a faint raised pixel numeral is embossed near the root. The tooth is oversized, larger than any real tooth would plausibly be. The cord is cracked pleather with the coating flaking to reveal grey fabric underneath. A crude wire wrap holds the tooth at the top, one loop coming undone. Two small plastic bead spacers in fake turquoise.

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
#2B1A2E outline / #EDE6D4 tooth white / #C0B8A2 tooth shadow / #FBF6EA tooth highlight / #C9A870 root beige / #96784A root shadow / #1E1A1C cord black / #56504E cord flaking / #8E8A82 cord fabric / #2E96A8 fake turquoise / #17606E turquoise shadow / #A8AEB4 wire wrap / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single oversized pendant shark tooth hanging from a black leather cord laid flat in a shallow loop, off-white with a beige root but unmistakably molded plastic with a visible mold seam running down both edges, too-smooth slightly glossy surface and a faint raised embossed numeral near the root, cracked pleather cord flaking to reveal grey fabric underneath, crude wire wrap at the top with one loop coming undone, two fake turquoise plastic bead spacers, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #EDE6D4 tooth white / #C0B8A2 tooth shadow / #FBF6EA tooth highlight / #C9A870 root beige / #96784A root shadow / #1E1A1C cord black / #56504E cord flaking / #8E8A82 cord fabric / #2E96A8 fake turquoise / #17606E turquoise shadow / #A8AEB4 wire wrap / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (48x48)** — over a deep V-neck, cross-referencing `hemp-necklace-deep-v-neck.md`.
- **Mold-seam close-up (32x32)** — the tooth rotated to show the seam and mold number. For the 'Fake Danger' tooltip.
- **Multi-tooth variant** — three teeth on one cord, escalating.

## 6. Art-director notes

- The mold seam is the joke and it must be visible at 64px. A hard 1px line down the center edge on both sides.
- Oversize the tooth. Plausibility is the enemy here.
- Do not render the mold number as legible digits — a raised pixel blob is enough.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

