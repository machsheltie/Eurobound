# Glowstick Nunchucks (UV Reactive)

> **Asset slug:** `glowstick-nunchucks`  
> **Type / slot:** Weapon / Accessory — Regional  
> **World:** Debaucheryville  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Attack, +3 Rave Cred, +1 Light Source, -1 Credibility.

**Flavor text:** *"Deadly weapons that also help you find the bathroom."*

**Era Cringe:** Makes swooshing sounds and leaves glowing trails in combat.

**Why it's funny (the thing the art has to sell):** Two glow sticks joined by a shoelace, wielded as martial arts weapons by a man with no martial arts training. They weigh forty grams. He does a whole routine.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
Two thick glow sticks joined end-to-end by a short knotted length of grubby white shoelace, laid out in a loose V. Both sticks are cracked and lit — one acid green, one hot magenta — rendered as flat saturated color with a hard-edged 1px lighter core stripe running the length, absolutely no glow or bloom. The plastic tubes are scuffed and one has a hairline stress crack with a slightly darker section where the fluid has pooled. The shoelace is knotted crudely at each end through drilled holes, with the aglets missing and the ends frayed. A short hard-edged motion trail of five spaced pixel dashes arcs off one stick. A strip of black electrical tape reinforces one knot.

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
#2B1A2E outline / #7EF018 acid green / #4A9E0A green shadow / #C4FF8E green core / #F018A8 hot magenta / #9E0A66 magenta shadow / #FF8ED8 magenta core / #E8E4D8 shoelace / #B8B2A2 lace grubby / #1A1A1E electrical tape / #8E9298 scuffed plastic / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Two thick glow sticks joined end-to-end by a short knotted length of grubby white shoelace laid out in a loose V, both cracked and lit in acid green and hot magenta as flat saturated color with a hard 1px lighter core stripe and absolutely no glow or bloom, scuffed plastic tubes with one hairline stress crack and a darker pooled section, shoelace crudely knotted through drilled holes with missing aglets and frayed ends, a short hard-edged motion trail of five spaced pixel dashes arcing off one stick, black electrical tape reinforcing one knot, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #7EF018 acid green / #4A9E0A green shadow / #C4FF8E green core / #F018A8 hot magenta / #9E0A66 magenta shadow / #FF8ED8 magenta core / #E8E4D8 shoelace / #B8B2A2 lace grubby / #1A1A1E electrical tape / #8E9298 scuffed plastic / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Battle swing FX frame (96x64)** — full arc of hard-edged pixel dashes in alternating green and magenta, for the attack animation.
- **Unlit variant** — both sticks dull and dead, for the depleted state after the light source expires.
- **Equipped variant (32x32)** — held in a hand silhouette mid-spin.

## 6. Art-director notes

- No glow, no bloom, no soft light. Repeat it in every regeneration. Flat saturated color plus a hard core stripe is the entire technique.
- This shares a rendering language with `glow-sticks-rave-quality.md` — generate them in the same session so the greens and magentas match exactly.
- The electrical-tape repair says this has already broken once and he fixed it rather than stopping. Keep it.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

