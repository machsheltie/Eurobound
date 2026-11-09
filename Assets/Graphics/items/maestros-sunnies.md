# Maestro's Sunnies (Tinted Prescription)

> **Asset slug:** `maestros-sunnies`  
> **Type / slot:** Head Gear — Regional  
> **World:** Sinfonia  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Coolness, +1 Mystery, +3 Indoor Vision Problems.

**Flavor text:** *"For looking sophisticated while squinting at everything."*

**Era Cringe:** Worn indoors during classical concerts because 'the music is too bright'.

**Why it's funny (the thing the art has to sell):** Tinted prescription glasses worn indoors at an opera house. He cannot see. He is navigating by memory and confidence. He has already walked into one pillar.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A pair of small rectangular tinted sunglasses seen face-on with the arms folded partway in at asymmetric angles. Thin gold-tone wire frames with a visible prescription thickness at the lens edges rendered as a stepped double outline. The lenses are a rich amber-brown gradient stepped into exactly three hard horizontal tone bands, dark at the top, lighter at the bottom, with one hard specular highlight bar across the upper left. A visible smudged fingerprint on one lens. The gold plating has worn through to grey at both hinges and along one arm. The nose pads are yellowed and one is cracked. One arm is bent slightly out of alignment so the glasses would not sit level. A tiny screw is missing from one hinge.

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
#2B1A2E outline / #C9A227 frame gold / #8A6E14 gold shadow / #F0D874 gold highlight / #8E8A82 worn plating / #5E3E18 lens dark / #8E6428 lens mid / #C49A56 lens light / #E8D8B4 lens spec / #C9BE8E nose pad / #9E9268 pad shadow / #A8A296 fingerprint smudge / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Small rectangular tinted prescription sunglasses face-on with the arms folded partway in at asymmetric angles, thin gold-tone wire frames with visible prescription lens thickness rendered as a stepped double outline, rich amber-brown lenses stepped into exactly three hard horizontal tone bands dark at top and lighter at bottom with one hard specular highlight bar across the upper left, smudged fingerprint on one lens, gold plating worn to grey at both hinges and along one arm, yellowed nose pads with one cracked, one arm bent out of alignment, a missing hinge screw, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C9A227 frame gold / #8A6E14 gold shadow / #F0D874 gold highlight / #8E8A82 worn plating / #5E3E18 lens dark / #8E6428 lens mid / #C49A56 lens light / #E8D8B4 lens spec / #C9BE8E nose pad / #9E9268 pad shadow / #A8A296 fingerprint smudge / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (48x48)** — on a head silhouette, sitting slightly crooked because of the bent arm.
- **Indoor Vision Problems FX (48x48)** — the world seen through the lenses as a heavily darkened three-band amber field with vague pixel shapes, for the debuff overlay.
- **Case variant (48x32)** — a cracked hard-shell case with a squashed lid, for the shop display.

## 6. Art-director notes

- Three hard tone bands in the lens, never a smooth gradient. That stepping is the SNES signature and it also reads as 'cheap tint.'
- Prescription thickness at the lens edge is a small, specific detail that tells you he actually needs these. Keep the stepped double outline.
- The bent arm means the worn variant should sit visibly crooked. That asymmetry is worth the effort.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

