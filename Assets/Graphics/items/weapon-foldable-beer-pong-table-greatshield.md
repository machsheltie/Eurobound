# Foldable Beer-Pong Table (Greatshield)

> **Asset slug:** `weapon-foldable-beer-pong-table-greatshield`  
> **Type / slot:** Weapon / Shield — Bradley Signature  
> **World:** Global  
> **Rarity / tier:** Signature  
> **Canon source:** `Game Design Spec Sheet / bradleysweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Bradley's signature. Heavy melee and crowd control; used as a greatshield. Powers: Keg Toss stuns multiple enemies.

**Flavor text:** *"Eight feet of laminate and one functioning hinge."*

**Why it's funny (the thing the art has to sell):** A folding beer pong table carried on one arm like a tower shield. It weighs as much as he does. He refuses to leave it anywhere, including nightclubs and an opera house.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A folding tabletop held vertically as a tower shield, seen face-on with a slight three-quarter turn showing the edge and the folded hinge seam down the center. The surface is a scuffed white laminate printed with a faded red beer-pong rack diagram — ten circles arranged in a triangle at each end, rendered as hard-edged red pixel rings, several worn away to ghosts. The laminate is stained with dark overlapping ring marks, one long scorch, and a deep gouge exposing the pale chipboard core. The steel folding legs are strapped flat against the back with a ratchet strap and hang slightly loose. A chunky central piano hinge runs the full height, one hinge pin replaced with a bolt. A padded arm strap and a crude bolted grip handle have been added to the back. Corners are crushed and rounded from impact.

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
#2B1A2E outline / #EDE8DA laminate white / #C0BAA8 laminate shadow / #FBF8F0 laminate highlight / #C42A16 rack red / #7E140A red shadow / #E86E5E red faded / #8E7A56 chipboard core / #4A3A26 ring stain / #2E2418 scorch / #8E9298 steel leg / #5E6268 leg shadow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Folding beer pong tabletop held vertically as a tower shield seen face-on with a slight three-quarter turn showing the edge and the central folded hinge seam, scuffed white laminate printed with a faded red ten-circle beer pong rack triangle at each end rendered as hard-edged red pixel rings with several worn to ghosts, dark overlapping ring stains, a long scorch mark, a deep gouge exposing pale chipboard core, steel folding legs strapped flat against the back with a loose ratchet strap, a chunky full-height piano hinge with one pin replaced by a bolt, a padded arm strap and a crude bolted grip handle on the back, crushed rounded corners, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #EDE8DA laminate white / #C0BAA8 laminate shadow / #FBF8F0 laminate highlight / #C42A16 rack red / #7E140A red shadow / #E86E5E red faded / #8E7A56 chipboard core / #4A3A26 ring stain / #2E2418 scorch / #8E9298 steel leg / #5E6268 leg shadow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Block pose FX frame (96x96)** — the table angled forward with four hard-edged pixel impact sparks and a blocky shockwave arc, for the guard animation.
- **Deployed variant (96x64)** — the table set up on its legs with cups arranged, for cutscenes and the Publandia tavern scene.
- **Keg Toss FX frame (96x96)** — a keg as a hard-edged pixel cylinder arcing over the table's top edge with a stepped motion trail.

## 6. Art-director notes

- Scale it large. This is a greatshield — it should be nearly as tall as a party member and read as absurd to be carrying.
- The worn-away rack circles tell you how many games have been played on it. Ghost three or four of the twenty.
- Signature weapon — generate at 256x256 and keep a hi-res master.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

