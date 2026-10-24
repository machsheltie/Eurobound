# Basketball Jersey (Oversized)

> **Asset slug:** `basketball-jersey-oversized`  
> **Type / slot:** Torso  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Street Cred, +1 Airflow.

**Flavor text:** *"From a player you can't name on a team you don't follow."*

**Era Cringe:** Worn to nightclubs as 'formal wear'.

**Why it's funny (the thing the art has to sell):** He cannot name the player. He cannot name the team. He bought it at a mall kiosk. He wears it to clubs that have a dress code, and argues about it at the door.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
An oversized sleeveless basketball jersey hanging flat on an invisible form, absurdly large — the armholes drop nearly to the hem. Deep purple mesh body with gold and white trim bands at the neck and armholes, rendered with the mesh as a regular grid of 1px darker holes. A large number on the chest rendered as blocky illegible pixel shapes, the vinyl heat-transfer cracked and peeling at the edges with a visible corner lifting. The hem is uneven from bad tailoring. A stiff yellowed deodorant ring at one armhole. The team name arc above the number is flaking to unreadable fragments. A price-tag hole punched at the hem.

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
#2B1A2E outline / #5E2E96 jersey purple / #38185E purple shadow / #8E5EC8 purple highlight / #C9A227 trim gold / #8A6E14 gold shadow / #F4F0E4 trim white / #C4BEB0 white shadow / #C9BE8E deodorant yellow / #9E9268 stain shadow / #E8E4D8 vinyl number / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Absurdly oversized sleeveless basketball jersey hanging flat on an invisible form with armholes dropping nearly to the hem, deep purple mesh body rendered as a grid of 1px darker holes with gold and white trim bands at neck and armholes, large blocky illegible number in cracked peeling vinyl heat-transfer with a lifting corner, flaking unreadable team arc, uneven hem, stiff yellowed deodorant ring at one armhole, punched price-tag hole, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #5E2E96 jersey purple / #38185E purple shadow / #8E5EC8 purple highlight / #C9A227 trim gold / #8A6E14 gold shadow / #F4F0E4 trim white / #C4BEB0 white shadow / #C9BE8E deodorant yellow / #9E9268 stain shadow / #E8E4D8 vinyl number / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn-over-a-t-shirt variant** — jersey layered over a white tee, the club-dress-code compromise.
- **Alt colorways** — faded teal/orange and red/black, for palette-swap shop stock.
- **Equipped variant (48x48)** — on a torso silhouette, the armholes exposing a lot more side than intended.

## 6. Art-director notes

- Oversize is the joke — push the proportions past realistic. Armhole to hem.
- Peeling vinyl number is the age tell. Make the lifted corner clearly visible at 64px.
- Number and team name must stay illegible pixel shapes. No real team, no real number, no real player.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

