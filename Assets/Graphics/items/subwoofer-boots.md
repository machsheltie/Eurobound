# Subwoofer Boots (Bass Enhanced)

> **Asset slug:** `subwoofer-boots`  
> **Type / slot:** Footwear — Regional  
> **World:** Sinfonia  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Movement Speed, +2 Ground Pound Attack, -1 Stealth.

**Flavor text:** *"Every step drops a fat beat and rattles windows."*

**Era Cringe:** Automatically plays bass drops when you walk, announcing your presence to everyone within three blocks.

**Why it's funny (the thing the art has to sell):** Boots with speakers built into the soles, worn in an opera house. He cannot turn them off. He does not want to turn them off. The stealth penalty is not a penalty in his view.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single chunky mid-height boot at a three-quarter side angle with an absurdly thick platform sole housing visible speaker hardware — a round mesh grille set into the outer side of the sole, rendered as a regular grid of dark pixel holes inside a chrome ring, plus a small illegible pixel control panel with two tiny buttons and a red LED pixel near the heel. The upper is black synthetic leather with chrome buckle hardware and a fine 1px stipple texture. A short coiled cable runs from the sole panel up into the ankle collar. The sole is scuffed white at the toe and heel edges. Four hard-edged concentric pixel arcs radiate from the speaker grille to indicate active output. A small battery hatch on the heel sits slightly proud.

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
#2B1A2E outline / #1A1A1E leather black / #34343E black mid / #56565E black highlight / #A8AEB4 chrome / #6E7478 chrome shadow / #E0E6EA chrome highlight / #2A2A32 grille hole / #E82424 LED red / #C4C8CC sole scuff / #7E8288 sole grey / #F0F4F8 sound arc / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single chunky mid-height boot at a three-quarter side angle with an absurdly thick platform sole housing a round speaker mesh grille rendered as a grid of dark pixel holes in a chrome ring plus a small illegible control panel with two tiny buttons and a red LED pixel near the heel, black synthetic leather upper with chrome buckles and a fine 1px stipple, short coiled cable running from the sole panel into the ankle collar, sole scuffed white at toe and heel, four hard-edged concentric pixel arcs radiating from the grille, battery hatch sitting proud on the heel, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1A1A1E leather black / #34343E black mid / #56565E black highlight / #A8AEB4 chrome / #6E7478 chrome shadow / #E0E6EA chrome highlight / #2A2A32 grille hole / #E82424 LED red / #C4C8CC sole scuff / #7E8288 sole grey / #F0F4F8 sound arc / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Pair variant (64x48)** — both boots, one mid-step with a full arc burst.
- **Ground Pound FX frame (96x64)** — the boot slamming down with eight hard-edged concentric pixel shockwave rings and four debris pixels, for the attack animation.
- **Silent variant** — no sound arcs, for the inventory icon and for the doomed attempt at stealth.

## 6. Art-director notes

- The speaker grille must be clearly a speaker — chrome ring plus dark hole grid. Without it this is just a platform boot.
- Sound arcs are hard-edged concentric partial rings, never soft waves. Four in the base icon, eight in the FX frame.
- Platform thickness should be comic. If the sole looks structurally sensible, thicken it.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

