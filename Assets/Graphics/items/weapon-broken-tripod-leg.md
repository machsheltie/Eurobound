# Broken Tripod Leg

> **Asset slug:** `weapon-broken-tripod-leg`  
> **Type / slot:** Weapon — Chadwick (Alt)  
> **World:** Global  
> **Rarity / tier:** Common / Upgradeable  
> **Canon source:** `chadwicksweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Telescoping reach attacks; can "set up" for combo moves.

**Flavor text:** *"The other two legs are in a closet in another country."*

**Why it's funny (the thing the art has to sell):** One leg, snapped off a tripod, used as a club. The other two legs are somewhere. He does not know where. He describes himself as a filmmaker.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single tripod leg detached from its head, held vertically. Three telescoping aluminum sections of decreasing width with black plastic flip-lock clamps, one clamp snapped off leaving a bare hinge pin and two exposed screw holes. At the top, a jagged torn mounting bracket where it was wrenched free from the tripod's shoulder — bright bare metal at the tear, with three splayed hard-edged aluminum burrs. At the bottom, a rubber foot worn flat on one side with a retractable metal spike stuck half-out and bent. The anodizing is scuffed to raw silver along the whole length with two dents. A faded illegible pixel spec label near the top. A stub of gaffer tape marks the section where it always slipped.

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
#2B1A2E outline / #8E9298 anodized grey / #5E6268 grey shadow / #C4CAD0 grey highlight / #E8EEF2 bare metal tear / #1E1E24 clamp black / #38383E black highlight / #2A2A32 rubber foot / #4A4A52 foot worn / #A8AEB4 spike steel / #7E7468 gaffer tape / #C9BE8E faded label / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single detached tripod leg held vertically with three telescoping aluminum sections of decreasing width and black plastic flip-lock clamps with one clamp snapped off leaving a bare hinge pin and two exposed screw holes, a jagged torn mounting bracket at the top where it was wrenched free showing bright bare metal and three splayed hard-edged aluminum burrs, a rubber foot at the bottom worn flat on one side with a bent metal spike stuck half-out, anodizing scuffed to raw silver along the whole length with two dents, faded illegible pixel spec label, a stub of gaffer tape, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #8E9298 anodized grey / #5E6268 grey shadow / #C4CAD0 grey highlight / #E8EEF2 bare metal tear / #1E1E24 clamp black / #38383E black highlight / #2A2A32 rubber foot / #4A4A52 foot worn / #A8AEB4 spike steel / #7E7468 gaffer tape / #C9BE8E faded label / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **TIER 1 — Broken Tripod Leg** — as described.
- **TIER 2 — Reinforced (64x64)** — the tear capped with a welded steel collar, clamps replaced with metal levers, a wrapped cord grip added.
- **TIER 3 — Carbon Fiber (64x64)** — matte black tube with a visible woven carbon crosshatch rendered as a fine regular 1px diagonal grid, red anodized collars, a moulded rubber grip.
- **TIER 4 — Professional Gimbal Staff (64x64)** — a balanced staff with a counterweighted gimbal head at the top holding a small camera, two hard-edged pale pixel gleam marks, a leather grip.
- **Set-Up combo FX frame (96x64)** — the leg planted vertically with three hard-edged pixel bracket marks framing an enemy, for the combo setup move.

## 6. Art-director notes

- The torn mounting bracket is the identity of this weapon. Bright bare metal at the tear against dull anodizing — high contrast, reads at 32px.
- Keep it visually separated from the boom pole: no fur, no cable, thicker sections, a rubber foot at the bottom.
- Four tiers, constant silhouette. Generate together.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

