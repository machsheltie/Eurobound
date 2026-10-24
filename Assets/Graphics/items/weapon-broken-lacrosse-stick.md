# Broken Lacrosse Stick

> **Asset slug:** `weapon-broken-lacrosse-stick`  
> **Type / slot:** Weapon — Lord Pilsner (Alt)  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `lordpilsnersweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Scooping attacks; can steal items from enemies.

**Flavor text:** *"He could've gone D1 if the coach wasn't such a —"*

**Why it's funny (the thing the art has to sell):** A prep school lacrosse stick with a cracked head and a sagging pocket. It can steal items, which is thematically perfect and which he does not find insulting.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A lacrosse stick held vertically, head up. The plastic head is cracked through one sidewall with a hairline split running from the scoop, and the head is visibly warped out of plane. The mesh pocket has sagged into a deep bag, with two of the leather runners snapped and dangling and the sidewall lacing loose and uneven — several diamonds of the mesh are stretched wide. The head is a faded royal blue gone chalky from sun. The aluminum shaft is dented in two places and the anodizing is scuffed to bare metal along one flat. The butt end cap is missing entirely, showing the hollow tube. A strip of white athletic tape at the grip, grey and peeling. Faint illegible pixel initials written on the tape in marker.

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
#2B1A2E outline / #2E4E96 head blue / #16305E blue shadow / #6E8ECC blue highlight / #A8B4C8 blue chalky / #C9BEA8 mesh pocket / #8E8478 mesh shadow / #7E8288 aluminum / #4E5258 aluminum shadow / #C4CAD0 bare metal scuff / #E8E4D8 athletic tape / #8E8A7E tape grey / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Lacrosse stick held vertically head up, faded chalky royal blue plastic head cracked through one sidewall with a hairline split from the scoop and visibly warped out of plane, mesh pocket sagged into a deep bag with two snapped dangling leather runners and loose uneven sidewall lacing and several stretched-wide mesh diamonds, aluminum shaft dented in two places with the anodizing scuffed to bare metal along one flat, missing butt end cap showing the hollow tube, grey peeling white athletic tape at the grip with illegible marker initials, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #2E4E96 head blue / #16305E blue shadow / #6E8ECC blue highlight / #A8B4C8 blue chalky / #C9BEA8 mesh pocket / #8E8478 mesh shadow / #7E8288 aluminum / #4E5258 aluminum shadow / #C4CAD0 bare metal scuff / #E8E4D8 athletic tape / #8E8A7E tape grey / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Steal FX frame (96x64)** — the head scooping, with a small item icon lifting out of an enemy silhouette on a stepped hard-edged pixel arc.
- **Ball-in-pocket variant (48x48)** — a lacrosse ball sitting in the sagged pocket.
- **Battle idle sprite (48x48)** — front-view combat orientation.

## 6. Art-director notes

- The sagged pocket gives this a distinctive silhouette. Push the bag deeper than a functional stick would allow.
- Mesh must read as a diamond grid at 64px. Use 2px spacing minimum and let a few diamonds stretch irregularly.
- Warped head plus cracked sidewall is what separates this from a functional stick. Both must be visible in the base icon.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

