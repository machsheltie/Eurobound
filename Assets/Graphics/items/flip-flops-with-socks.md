# Flip-Flops (With Socks)

> **Asset slug:** `flip-flops-with-socks`  
> **Type / slot:** Footwear  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Comfort, +5 Fashion Crime.

**Flavor text:** *"The socks are for 'warmth and style'."*

**Era Cringe:** Worn to formal events because 'feet need to breathe'.

**Why it's funny (the thing the art has to sell):** Socks. In flip-flops. The thong strap has to force its way between two sock-covered toes, and the sock is straining. This is a +5 Fashion Crime item and it earns every point.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single foam flip-flop seen at a three-quarter top-down angle with a white crew athletic sock worn inside it. The sock is a grubby off-white with two faded stripe bands at the ankle, and the toe section is visibly distorted — the rubber thong strap forces a hard wedge between the big toe and the second toe, stretching the sock fabric taut with visible strain lines rendered as short hard pale pixel dashes. The foam sole is dark navy, compressed and permanently molded with a darker heel-print depression. The strap is faded and one anchor point is pulling loose from the sole with a visible gap. A grey grime line along the foam's edge. Sock fabric pilled and fuzzy at the heel.

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
#2B1A2E outline / #E8E4D4 sock white / #B8B4A2 sock shadow / #FBF8EE sock highlight / #8E8A78 sock grubby / #1E2E5E foam navy / #10183A foam shadow / #3E5290 foam highlight / #2A2A2E strap / #4A4A54 strap faded / #7E8288 grime / #C42A16 sock stripe / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single dark navy foam flip-flop at a three-quarter top-down angle with a grubby off-white crew athletic sock worn inside it, two faded stripe bands at the ankle, the rubber thong strap forcing a hard wedge between the big toe and second toe and stretching the sock fabric taut with hard pale pixel strain dashes, compressed foam sole with a darker molded heel-print depression, faded strap with one anchor point pulling loose from the sole leaving a visible gap, grey grime line along the foam edge, pilled fuzzy sock heel, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #E8E4D4 sock white / #B8B4A2 sock shadow / #FBF8EE sock highlight / #8E8A78 sock grubby / #1E2E5E foam navy / #10183A foam shadow / #3E5290 foam highlight / #2A2A2E strap / #4A4A54 strap faded / #7E8288 grime / #C42A16 sock stripe / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Pair variant (64x48)** — both feet, so the symmetry of the crime is fully visible.
- **Formal-event variant** — the sock-flip-flop combo below the hem of pleated khakis. Generate this. It is the whole item.
- **Alt sock** — a black dress sock, which is somehow worse.

## 6. Art-director notes

- The strained toe-split is the single most important detail. Specify it every time — 'sock fabric visibly stretched and wedged apart by the thong strap between the toes.'
- Sock must read as grubby-worn, not fresh. Pilling at the heel, greyed sole.
- The formal-event variant paired with the khakis is the highest-value asset in the footwear set. Prioritize it.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

