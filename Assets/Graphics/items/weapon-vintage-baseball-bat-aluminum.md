# Vintage Baseball Bat (Aluminum)

> **Asset slug:** `weapon-vintage-baseball-bat-aluminum`  
> **Type / slot:** Weapon — Bradley (Alt)  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `bradleysweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Heavy swinging attacks; durable metal construction.

**Flavor text:** *"Little League. Not his."*

**Why it's funny (the thing the art has to sell):** A child's aluminum bat from a Little League season he attended as a parent. He carries it. He does not talk about why. The grip tape still has a kid's name written on it in marker.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
An aluminum youth baseball bat held vertically, barrel up — noticeably short and slim, clearly sized for a child, which makes it look wrong in an adult's hands. The barrel is anodized a faded royal blue with a scuffed silver band and illegible blocky pixel graphics, dented in two places with the anodizing scraped to raw metal along the sweet spot. The taper is smooth. The knob end is dinged. The grip is black rubber tape, worn shiny and split at the top wrap, with a small illegible pixel name written on it in silver marker, half rubbed away. The end cap is a dark plastic plug, cracked. Faint ball-impact scoring rings the barrel. One long scratch runs the full length.

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
#2B1A2E outline / #2E4E96 barrel blue / #16305E blue shadow / #6E8ECC blue highlight / #A8AEB4 silver band / #6E7478 band shadow / #E0E6EA raw metal / #1A1A1E grip tape / #3A3A44 tape worn / #56565E tape shiny / #C4CAD0 marker silver / #8E9298 scoring / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Aluminum youth baseball bat held vertically barrel up, noticeably short and slim and clearly child-sized, faded royal blue anodized barrel with a scuffed silver band and illegible blocky pixel graphics, two dents with the anodizing scraped to raw metal along the sweet spot, dinged knob end, black rubber grip tape worn shiny and split at the top wrap with a small half-rubbed illegible name in silver marker, cracked dark plastic end cap, faint ball-impact scoring rings, one long full-length scratch, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #2E4E96 barrel blue / #16305E blue shadow / #6E8ECC blue highlight / #A8AEB4 silver band / #6E7478 band shadow / #E0E6EA raw metal / #1A1A1E grip tape / #3A3A44 tape worn / #56565E tape shiny / #C4CAD0 marker silver / #8E9298 scoring / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Scale-comparison variant (64x64)** — the bat held in an adult hand silhouette, so the child sizing is unmistakable. Generate this.
- **Battle idle sprite (48x48)** — front-view combat orientation.
- **SMAAAASH crit FX frame (96x96)** — impact with a hard-edged pixel ping ring and six radiating spark pixels, for the metal-bat sound gag.

## 6. Art-director notes

- Child sizing is the entire weight of this item. If it reads as a normal adult bat, it is just a bat. Shorten it and slim the barrel until it looks wrong.
- The half-rubbed name in marker is the detail. Keep it illegible — the player fills in the blank, which is far better than the game telling them.
- Do not add sentiment to the art. Render it plainly and let the object do the work.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

