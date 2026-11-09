# Hemp Necklace Visible Through Deep V-Neck

> **Asset slug:** `hemp-necklace-deep-v-neck`  
> **Type / slot:** Torso  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Chill Vibes, +2 Pseudo-Spirituality.

**Flavor text:** *"Bought during that 'finding myself' semester abroad."*

**Era Cringe:** The V goes down to the sternum.

**Why it's funny (the thing the art has to sell):** The shirt is a delivery mechanism for the necklace. The necklace is a delivery mechanism for a story about a semester abroad that nobody asked to hear.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A deep V-neck t-shirt hanging flat on an invisible form, with the V cut plunging absurdly low — well past where a neckline should stop, nearly to the middle of the chest. Heather-grey jersey cotton rendered with a fine 1px two-tone stipple. Draped in the exposed V opening is a knotted hemp cord necklace in natural tan, with a small carved wooden bead and a chipped turquoise-blue stone pendant, the cord fraying at the knot. The shirt's V edge is stretched wavy and out of shape. A small permanent yellow underarm shadow. The hem is uneven. A few chest hairs rendered as three dark curved pixel strokes in the V opening.

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
#2B1A2E outline / #9EA0A4 heather grey / #6E7074 grey shadow / #C4C6CA grey highlight / #C9A870 hemp tan / #96784A hemp shadow / #E8D4A8 hemp highlight / #2E96A8 turquoise / #17606E turquoise shadow / #6EC8D8 turquoise highlight / #7E5A2E wooden bead / #C9BE8E underarm yellow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Deep V-neck heather grey jersey t-shirt hanging flat on an invisible form with the V plunging absurdly low nearly to mid-chest, fine 1px two-tone stipple texture, knotted natural tan hemp cord necklace draped in the exposed V with a small carved wooden bead and a chipped turquoise stone pendant and fraying cord, stretched wavy V edge, yellow underarm shadow, uneven hem, three dark curved pixel strokes as chest hair, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #9EA0A4 heather grey / #6E7074 grey shadow / #C4C6CA grey highlight / #C9A870 hemp tan / #96784A hemp shadow / #E8D4A8 hemp highlight / #2E96A8 turquoise / #17606E turquoise shadow / #6EC8D8 turquoise highlight / #7E5A2E wooden bead / #C9BE8E underarm yellow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Necklace-only asset (32x32)** — the hemp necklace alone, since it's also referenced in the Necklaces slot lineup.
- **Equipped variant (48x48)** — on a torso silhouette, V exposing a lot of pale chest.
- **Alt colorways** — washed black and a truly regrettable deep purple.

## 6. Art-director notes

- The V depth is the joke — take it past the point of plausibility. If it looks like a normal V-neck, cut it deeper.
- The necklace must be visible in the main icon, since the item name is about the combination.
- Three chest-hair pixel strokes. Not a texture. Three strokes. Restraint is funnier.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

