# Axe Body Spray (Concentrated Blast)

> **Asset slug:** `axe-body-spray-concentrated-blast`  
> **Type / slot:** Consumable — Offensive (AOE)  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** AOE damage to all enemies, chance to inflict "Overwhelmed".

**Flavor text:** *"Chemical warfare disguised as cologne."*

**Why it's funny (the thing the art has to sell):** Chemical weapon energy. The can should look like ordnance — matte black, military-adjacent branding, a nozzle that has been held down too long.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A tall matte-black aerosol can, AXE, with a broad silver-grey band and an aggressive angular logo mark rendered as blocky pixel shapes. Black plastic actuator cap with the spray nozzle visible and a crust of dried white product buildup around the hole. The can body has one long scuff revealing bare aluminum underneath. A hard-edged pixel mist plume is already escaping the nozzle — 8 to 12 individual pale grey-green square pixel puffs in a widening cone, blocky, never soft. Faint greasy fingerprints on the black surface.

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
#2B1A2E outline / #1E1E22 matte black / #38383E black highlight / #0E0E12 black shadow / #A8AEB4 silver band / #6E7278 silver shadow / #D8DEE4 silver highlight / #9EAE8E mist green / #C4D0B8 mist highlight / #E8E4D8 nozzle crust / #7E8288 bare aluminum / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Tall matte black AXE aerosol body spray can with silver-grey band and angular blocky logo, black actuator cap, dried white product crust around the nozzle hole, long scuff exposing bare aluminum, hard-edged pale grey-green square pixel mist cone escaping the nozzle, greasy fingerprints, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E1E22 matte black / #38383E black highlight / #0E0E12 black shadow / #A8AEB4 silver band / #6E7278 silver shadow / #D8DEE4 silver highlight / #9EAE8E mist green / #C4D0B8 mist highlight / #E8E4D8 nozzle crust / #7E8288 bare aluminum / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Full AOE FX frame (96x64)** — the can horizontal, full cone of hard-edged pixel mist crossing the whole frame, for the all-enemies attack animation.
- **Dented empty variant** — crushed, nozzle snapped off.
- **Locker-room three-pack** — for the Bradley gym sidequest shelf.

## 6. Art-director notes

- The mist must be individual square pixels in a cone. Any soft spray and the whole EarthBound read collapses.
- Matte black is a trap for these generators — they will render it glossy. Specify 'matte, no reflections, no gloss' and expect two regenerations.
- The dried crust around the nozzle is the 'this has been abused' detail. Keep it.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

