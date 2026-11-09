# Vintage Beer Pong Paddle

> **Asset slug:** `weapon-vintage-beer-pong-paddle`  
> **Type / slot:** Weapon — Lord Pilsner (Alt)  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `lordpilsnersweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Bouncing attacks that ricochet off multiple enemies.

**Flavor text:** *"He was, at one point, regionally competitive."*

**Why it's funny (the thing the art has to sell):** A table tennis paddle from a tournament that had a trophy and a bracket and about eleven participants. He still says 'regionally competitive.' The rubber is coming off.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A table tennis paddle held at a slight angle, showing the face and the edge. The blade is thin plywood with a visible five-ply edge stripe rendered as alternating pale and dark 1px bands. The face rubber is a faded brick red, worn to a pale bald patch dead center where every shot has landed, with the edge of the rubber peeling away from the blade along one side revealing dried yellow glue. A small illegible pixel brand stamp near the handle. The handle is flared cork-and-wood with the lacquer worn through to bare pale wood where the hand grips, and a dark sweat stain in the grain. A strip of grip tape is wrapped at the base, curling loose. A ping pong ball with a visible dent rests beside it.

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
#2B1A2E outline / #A83A2E rubber red / #6E1E16 red shadow / #D86E5E red highlight / #C4A87E bald patch / #C9BEA8 plywood pale / #8E7A56 plywood dark / #7E5A2E handle wood / #4E3418 wood shadow / #C9BE8E dried glue / #EDE8DA pingpong ball / #4A423A sweat stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Table tennis paddle at a slight angle showing face and edge, thin plywood blade with a five-ply edge stripe as alternating pale and dark 1px bands, faded brick-red face rubber worn to a pale bald patch dead center with the rubber peeling away along one side revealing dried yellow glue, small illegible pixel brand stamp near the handle, flared cork-and-wood handle with lacquer worn through to bare pale wood at the grip and a dark sweat stain in the grain, curling loose grip tape at the base, a dented ping pong ball resting beside it, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A83A2E rubber red / #6E1E16 red shadow / #D86E5E red highlight / #C4A87E bald patch / #C9BEA8 plywood pale / #8E7A56 plywood dark / #7E5A2E handle wood / #4E3418 wood shadow / #C9BE8E dried glue / #EDE8DA pingpong ball / #4A423A sweat stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Ricochet FX frame (96x64)** — the ball as a hard-edged pixel dot with a stepped zigzag trail bouncing between three points.
- **Pair variant** — two paddles crossed, for a trophy-case or shop display.
- **Battle idle sprite (48x48)** — front-view combat orientation, paddle raised.

## 6. Art-director notes

- The bald center patch is the whole story — thousands of shots, one spot. Make it clearly worn through to a paler tone.
- Five-ply edge stripe is a small authenticity detail that costs three pixels and reads instantly to anyone who has held one.
- Keep this visually distinct from the pledge paddle: rounder blade, shorter, red rubber vs bare oak.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

