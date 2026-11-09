# Folding Chair (Reinforced)

> **Asset slug:** `weapon-folding-chair-reinforced`  
> **Type / slot:** Weapon — Bradley (Alt)  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `bradleysweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Folding and unfolding mechanics with defensive and offensive modes; stronger when surrounded by other frustrated middle-aged men.

**Flavor text:** *"He has a whole entrance for this."*

**Why it's funny (the thing the art has to sell):** A reinforced steel folding chair, wielded exactly the way you think. He has a taunt, a pose, and an entrance. He does the entrance every time, including once in a cathedral.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A steel folding chair shown partly folded at roughly forty degrees, held by the backrest, giving an asymmetric hinged silhouette. The frame is powder-coated a faded slate grey, chipped at every joint and corner to reveal bright bare steel and small orange rust blooms. The seat and back panels are stamped steel with a repeating pattern of small pressed dimples rendered as a regular grid of 1px darker marks, and both are visibly dented — one deep bowl-shaped impact dent in the seat. Two extra steel reinforcement bars have been welded across the underside with crude, lumpy weld beads. The rubber feet are cracked and one is missing. The hinge is bent so the fold does not close square. A strip of grip tape wraps the backrest's top rail.

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
#2B1A2E outline / #5E6268 slate grey / #3A3E44 grey shadow / #8E9298 grey highlight / #C4CAD0 bare steel / #E8EEF2 steel highlight / #B84A16 rust bloom / #7E2E0A rust dark / #A8AEB4 weld bead / #1A1A1E grip tape / #2A2A32 rubber foot / #4A4A52 foot cracked / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Steel folding chair shown partly folded at roughly forty degrees held by the backrest giving an asymmetric hinged silhouette, faded slate-grey powder coat chipped at every joint and corner revealing bright bare steel and small orange rust blooms, stamped steel seat and back panels with a regular grid of 1px pressed dimple marks and visible dents including one deep bowl-shaped impact dent in the seat, two extra steel reinforcement bars crudely welded across the underside with lumpy weld beads, cracked rubber feet with one missing, bent hinge so the fold does not close square, grip tape wrapping the top rail, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #5E6268 slate grey / #3A3E44 grey shadow / #8E9298 grey highlight / #C4CAD0 bare steel / #E8EEF2 steel highlight / #B84A16 rust bloom / #7E2E0A rust dark / #A8AEB4 weld bead / #1A1A1E grip tape / #2A2A32 rubber foot / #4A4A52 foot cracked / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Fully folded variant (48x64)** — flat, for the inventory icon and the defensive-mode pose.
- **Fully open variant (64x64)** — set up as a chair, for cutscenes and the moment he sits down mid-argument.
- **Overhead entrance FX frame (96x96)** — the chair raised above a silhouette with four hard-edged pixel impact lines and a blocky SMAAAASH-style burst behind it.

## 6. Art-director notes

- Partly folded is the hero pose — a fully open chair reads as furniture and a folded one reads as a plank. Forty degrees splits the difference and gives a memorable silhouette.
- The crude welded reinforcement bars are the 'reinforced' in the name and they should look homemade. Lumpy beads, uneven spacing.
- Three states matter for animation: folded, forty degrees, open. Generate all three in one session.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

