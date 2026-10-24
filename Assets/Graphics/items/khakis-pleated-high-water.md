# Khakis (Pleated, High-Water)

> **Asset slug:** `khakis-pleated-high-water`  
> **Type / slot:** Legs  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Business Casual, +3 Awkwardness.

**Flavor text:** *"Perfect for job interviews and ruining dates."*

**Era Cringe:** Shows ankle even with shoes on.

**Why it's funny (the thing the art has to sell):** Double-pleated, too short, and pressed with a crease so sharp it looks like a fold-out diagram. These are what he wears when he wants to be taken seriously.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A pair of pleated dress khakis hanging flat on an invisible form, front view, hemmed conspicuously short so the legs end well above where an ankle would be. Pale stone-beige twill with two deep front pleats per leg rendered as hard vertical shadow lines fanning from the waistband. A knife-sharp center crease down each leg as a single hard 1px pale line with a shadow line beside it. The waistband sits high with belt loops and a visible pleated overhang. The hem is a crisp turn-up cuff, over-pressed and shiny at the fold. A faint permanent iron-scorch patch on one thigh, slightly darker and glazed. Excess fabric bunches at the hip.

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
#2B1A2E outline / #D8CCAE khaki pale / #A89A78 khaki shadow / #F0E8D0 khaki highlight / #B8A886 khaki mid / #8E8060 pleat shadow / #C9BE9E scorch patch / #9E9070 scorch dark / #7E7458 waistband shadow / #E8E0C8 crease line / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Pleated pale stone-beige dress khakis hanging flat on an invisible form in front view, hemmed conspicuously short so the legs end well above the ankle, two deep front pleats per leg rendered as hard vertical shadow lines fanning from the high waistband, knife-sharp 1px pale center crease down each leg with a shadow line beside it, crisp over-pressed turn-up cuffs shiny at the fold, faint glazed iron-scorch patch on one thigh, excess fabric bunching at the hip, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #D8CCAE khaki pale / #A89A78 khaki shadow / #F0E8D0 khaki highlight / #B8A886 khaki mid / #8E8060 pleat shadow / #C9BE9E scorch patch / #9E9070 scorch dark / #7E7458 waistband shadow / #E8E0C8 crease line / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Equipped variant (48x48)** — on a legs silhouette showing a clear band of bare pale ankle above white athletic socks. This is the payoff — generate it.
- **Combo variant** — paired with the flip-flops-with-socks sprite for the ultimate crime.
- **Alt colorways** — grey and a deeply unwise pale sage.

## 6. Art-director notes

- The exposed ankle only exists in the equipped variant, so that variant matters more than the base icon here. Prioritize it.
- Pleats must fan visibly from the waistband — that's the period signal. Two per leg minimum.
- The crease is a single pale pixel line with a dark line beside it. Any softness and it stops reading as pressed.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

