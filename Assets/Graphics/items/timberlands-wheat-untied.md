# Timberlands (Wheat, Untied)

> **Asset slug:** `timberlands-wheat-untied`  
> **Type / slot:** Footwear  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Toughness, +1 Street Cred.

**Flavor text:** *"Laces dragging behind like sad tails."*

**Era Cringe:** Never been hiting, exclusively worn on pavement.

**Why it's funny (the thing the art has to sell):** Wheat-colored work boots that have never seen work. Laces untied on purpose. The soles are city-clean and the leather has one stain, from a kebab.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single wheat-tan nubuck work boot at a three-quarter side angle, six-eyelet, with a padded collar and a thick lugged rubber outsole in dark honey-brown. The boot is completely unlaced — the laces trail out of the top two eyelets and drape in a long loose S-curve across the ground beside it, ends frayed and grubby. The nubuck is a warm wheat tan with a fine 1px stipple, scuffed pale at the toe. Brass eyelets as small hard-edged gold discs, one tarnished green. A dark grease stain on the side panel. The lug sole is clean — no mud, no dirt in the treads, just pavement polish on the high points. A small illegible pixel logo tab at the heel.

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
#2B1A2E outline / #C9A468 wheat tan / #96764A tan shadow / #E8CE9E tan highlight / #8E6E3E sole honey / #5E4626 sole shadow / #B8945E sole highlight / #C9A227 brass eyelet / #6E8A4A tarnish green / #E8DCC4 lace / #7E7462 lace grubby / #3A2E22 grease stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single wheat-tan nubuck six-eyelet work boot at a three-quarter side angle with padded collar and thick lugged dark honey-brown rubber outsole, completely unlaced with the laces trailing from the top eyelets in a long loose S-curve across the ground with frayed grubby ends, fine 1px nubuck stipple scuffed pale at the toe, small gold brass eyelets with one tarnished green, dark grease stain on the side panel, lug sole clean with no mud and only pavement polish on the high points, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C9A468 wheat tan / #96764A tan shadow / #E8CE9E tan highlight / #8E6E3E sole honey / #5E4626 sole shadow / #B8945E sole highlight / #C9A227 brass eyelet / #6E8A4A tarnish green / #E8DCC4 lace / #7E7462 lace grubby / #3A2E22 grease stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Pair variant (64x48)** — both boots, laces tangled together, one tipped to show the clean sole.
- **Equipped variant** — on feet below cargo shorts, socks visible.
- **Muddy variant** — for the one sidequest where they actually go outside, as a visual gag.

## 6. Art-director notes

- Clean soles. Forbid mud, dirt, grass or trail wear explicitly. The pavement-only life is the joke.
- Untied laces must trail well outside the boot's footprint — that's the silhouette signature.
- Wheat tan is a very specific color. Warm, slightly yellow, not brown, not beige. Lock the palette.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

