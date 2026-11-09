# Broken Pool Cue Staff

> **Asset slug:** `weapon-broken-pool-cue-staff`  
> **Type / slot:** Weapon — Bradley (Top Pick)  
> **World:** Global  
> **Rarity / tier:** Signature / Upgradeable  
> **Canon source:** `bradleysweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Rack 'Em Up (line sweep), Corner Pocket (high-crit thrust), Break Shot (formation shatter).

**Flavor text:** *"Back when he ran the table at a bar that no longer exists."*

**Why it's funny (the thing the art has to sell):** A snapped pool cue used as a bo staff. It is the one thing he was genuinely, verifiably good at, broken and repurposed into something he is much worse at.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A pool cue snapped near the tip and held as a fighting staff, oriented vertically. The shaft is pale maple with a warm grain rendered as fine 1px striations, transitioning to a dark stained butt section with a decorative inlay band of pale diamonds rendered as blocky pixel shapes, one diamond chipped out. The broken tip end shows a jagged fiberglass fracture with splintered pale fibers fanning out as hard-edged pixel spikes and a dark hollow core visible. A crude repair binds the crack with three wraps of black electrical tape. The wrap section is peeling Irish linen, grey and grimy. Blue chalk residue dusts the upper shaft as scattered pale-cyan pixels, and a faint blue smear marks the grip. Two beer-glass ring stains on the butt. The joint collar is loose and slightly cocked.

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
#2B1A2E outline / #D8BE8E maple pale / #A8905E maple shadow / #F0DCB4 maple highlight / #4E2E18 butt stain / #2E1A0E butt shadow / #7E5A38 butt highlight / #EDE8DA inlay diamond / #1A1A1E electrical tape / #8E8A7E linen wrap / #6EC4D8 chalk blue / #4A3A26 ring stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Pool cue snapped near the tip and held vertically as a fighting staff, pale maple shaft with fine 1px grain striations transitioning to a dark stained butt with a decorative inlay band of blocky pale pixel diamonds and one chipped out, jagged fiberglass fracture at the broken end with splintered pale fibers fanning as hard-edged pixel spikes and a dark hollow core, crude repair of three wraps of black electrical tape, grey grimy peeling Irish linen grip wrap, scattered pale-cyan chalk residue on the upper shaft and a blue smear at the grip, two beer ring stains on the butt, loose cocked joint collar, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #D8BE8E maple pale / #A8905E maple shadow / #F0DCB4 maple highlight / #4E2E18 butt stain / #2E1A0E butt shadow / #7E5A38 butt highlight / #EDE8DA inlay diamond / #1A1A1E electrical tape / #8E8A7E linen wrap / #6EC4D8 chalk blue / #4A3A26 ring stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **TIER 1 — Broken Pool Cue** — as described.
- **TIER 2 — Weighted Fighting Stick (64x64)** — the fracture capped with a turned brass ferrule, a lead weight collar added at the butt, the wrap replaced with fresh dark leather cord, chalk cleaned off.
- **TIER 3 — Legendary Pub Champion's Rod (64x64)** — deep polished rosewood with brass inlay bands at both ends, a mother-of-pearl diamond inlay rendered as pale cyan-and-cream pixel shapes, and four hard-edged gold pixel spokes behind it.
- **Break Shot FX frame (96x96)** — a hard-edged pixel triangle of scattering balls exploding outward with stepped motion trails.
- **Battle idle sprite (48x48)** — front-view combat orientation, staff held diagonally.

## 6. Art-director notes

- Chalk residue is the single detail that identifies this as a pool cue and not a stick. Scatter pale cyan pixels generously on the upper shaft.
- Fracture must be fiberglass-splintered, not a clean snap. Hard-edged fanning spikes with a dark hollow core.
- Three tiers, constant silhouette. The maple-to-rosewood progression is Bradley's arc — generate all three together.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

