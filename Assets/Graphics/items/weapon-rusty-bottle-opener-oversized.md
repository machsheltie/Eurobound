# Rusty Bottle Opener (Oversized)

> **Asset slug:** `weapon-rusty-bottle-opener-oversized`  
> **Type / slot:** Weapon — Lord Pilsner (Alt)  
> **World:** Global  
> **Rarity / tier:** Common / Upgradeable  
> **Canon source:** `lordpilsnersweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Prying attacks, "cap removal" finishing moves.

**Flavor text:** *"His one marketable skill, forged into a weapon."*

**Why it's funny (the thing the art has to sell):** An enormous steel church-key bottle opener, scaled up to sword length. It is his single most transferable life skill, made literal and heavy.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A flat steel church-key bottle opener scaled up to the size of a short sword, held vertically. The business end is the classic hooked cap-lifter with a triangular piercing point, rendered oversized and chunky. The steel is dull grey mottled with heavy orange-brown rust rendered as irregular hard-edged pixel patches concentrated around the hook and along one edge, with pitting shown as scattered darker 1px holes. The handle section has a stamped illegible pixel logo and a punched hanging hole. Wrapped around the grip is a length of grubby cloth tape, dark with hand grease and unraveling at one end. The cap-lifter hook is bent slightly out of true. Two bottle caps are still jammed in the hook's throat, crimped and bent.

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
#2B1A2E outline / #7E8288 steel grey / #4E5258 steel shadow / #B4BAC0 steel highlight / #B84A16 rust orange / #7E2E0A rust dark / #D8763E rust highlight / #3A342E pitting / #8E8478 cloth tape / #5E564C tape greasy / #C42A16 bottle cap red / #C9A227 bottle cap gold / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Flat steel church-key bottle opener scaled up to short-sword size held vertically, classic oversized chunky hooked cap-lifter with a triangular piercing point, dull grey steel heavily mottled with irregular hard-edged orange-brown rust patches around the hook and one edge with scattered darker 1px pitting, stamped illegible pixel logo and a punched hanging hole in the handle, grubby grease-darkened cloth tape grip wrap unraveling at one end, hook bent slightly out of true, two crimped bottle caps still jammed in the hook throat, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #7E8288 steel grey / #4E5258 steel shadow / #B4BAC0 steel highlight / #B84A16 rust orange / #7E2E0A rust dark / #D8763E rust highlight / #3A342E pitting / #8E8478 cloth tape / #5E564C tape greasy / #C42A16 bottle cap red / #C9A227 bottle cap gold / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **TIER 1 — Rusty** — as described.
- **TIER 2 — Chrome (64x64)** — the same shape in bright polished chrome, two hard highlight bands, no rust, a moulded rubber grip.
- **TIER 3 — Swiss Army (64x64)** — the opener as one blade of an oversized multi-tool, three other tools fanned partway out, red scales with an illegible pixel cross-shaped emblem.
- **TIER 4 — Tactical Multi-Tool (64x64)** — matte black anodized, knurled grip, hex-bit sockets, a small illegible pixel serial etch. Add two hard-edged pale pixel gleam marks.
- **Cap Removal finisher FX frame (96x64)** — a bottle cap flying off as a spinning hard-edged pixel disc with a stepped trail.

## 6. Art-director notes

- Four tiers means four full renders — budget accordingly. Silhouette must stay constant across all four for the animation rig.
- Rust is the highest-value texture in the set. Irregular hard-edged patches plus 1px pitting; never a smooth wash.
- The jammed bottle caps in the hook are a small detail that makes the object feel used rather than displayed.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

