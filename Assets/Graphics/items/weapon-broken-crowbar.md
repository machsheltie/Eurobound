# Broken Crowbar

> **Asset slug:** `weapon-broken-crowbar`  
> **Type / slot:** Weapon — Bradley (Alt)  
> **World:** Global  
> **Rarity / tier:** Common / Upgradeable  
> **Canon source:** `bradleysweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Prying attacks, leverage moves; can open locked doors.

**Flavor text:** *"From the handyman phase, which ended in a letter."*

**Why it's funny (the thing the art has to sell):** A crowbar from his brief self-improvement era, which ended when a homeowners association sent a letter about a shed. He kept the crowbar.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A steel crowbar held at a diagonal, with the classic curved claw at one end and a flattened chisel wedge at the other — but the claw is snapped, one fork sheared off short with a bright jagged fracture face showing raw crystalline metal as hard-edged pale pixels. The bar is painted a faded safety red, chipped and flaking across every high point to reveal dull grey steel and orange rust patches underneath as irregular hard-edged pixel areas. The hexagonal shaft shows visible flats. The chisel end is mushroomed and burred from being struck with a hammer. Dried grey paint and plaster crust the claw. A grimy fingerprint-darkened section marks the natural grip point. One deep gouge scores the shaft.

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
#2B1A2E outline / #B4241E paint red / #6E0E0A red shadow / #E06E62 red highlight / #7E8288 steel grey / #4E5258 steel shadow / #E8EEF2 fracture bright / #B84A16 rust / #7E2E0A rust dark / #C9C4B8 dried plaster / #4A443E grip grime / #A8AEB4 burr metal / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Steel crowbar at a diagonal with a curved claw at one end and a flattened chisel wedge at the other, the claw snapped with one fork sheared short showing a bright jagged fracture face of raw crystalline metal as hard-edged pale pixels, faded safety-red paint chipped and flaking on every high point revealing dull grey steel and irregular orange rust patches, visible hexagonal shaft flats, chisel end mushroomed and burred from hammer strikes, dried grey paint and plaster crusting the claw, a grimy darkened grip section, one deep gouge in the shaft, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #B4241E paint red / #6E0E0A red shadow / #E06E62 red highlight / #7E8288 steel grey / #4E5258 steel shadow / #E8EEF2 fracture bright / #B84A16 rust / #7E2E0A rust dark / #C9C4B8 dried plaster / #4A443E grip grime / #A8AEB4 burr metal / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **TIER 1 — Rusty** — as described.
- **TIER 2 — Reinforced (64x64)** — the sheared fork rebuilt with a welded steel plate and visible bead, repainted in fresh red, a wrapped cord grip added.
- **TIER 3 — Tactical Breaching Tool (64x64)** — matte black with a hooked head, a serrated edge section, a knurled grip and an illegible pixel serial etch, plus two hard-edged pale pixel gleam marks.
- **Door-pry FX frame (96x64)** — the claw wedged into a door edge with three hard-edged pixel splinter shapes and a blocky strain arc.

## 6. Art-director notes

- The sheared fork with a bright fracture face is what makes this 'broken' rather than 'a crowbar.' High-contrast pale metal against faded red — reads instantly at 32px.
- Paint chipping on high points only. That's how painted tools actually age and it's a fast believability win.
- Three tiers, constant silhouette.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

