# Digital Watch (Calculator Function)

> **Asset slug:** `digital-watch-calculator`  
> **Type / slot:** Watch / Bracelet  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Intelligence, +1 Nerd Cred.

**Flavor text:** *"For calculating tips and split checks."*

**Era Cringe:** Beeps every hour, on the hour.

**Why it's funny (the thing the art has to sell):** He uses the calculator function to split checks at the table, out loud, slowly, while everyone waits. The hourly beep has gone off during at least one funeral.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A chunky rectangular digital calculator watch seen face-on with the strap curving away on both sides. Silver-tone plastic case with a black resin bezel. A small monochrome LCD across the top shows illegible pixel numerals and a tiny alarm bell icon, with two dead segment bars stuck permanently on. Below the screen, a dense grid of twenty-plus tiny square rubber buttons in dark grey, several worn smooth and pale from use with the printed characters completely rubbed off. The resin strap is cracked at both spring-bar holes and one keeper loop is missing so the strap tail sticks out unsecured. The crystal is scratched to a dull haze with one deep gouge. A faint green corrosion bloom at the battery hatch.

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
#2B1A2E outline / #A8AEB4 case silver / #6E7478 case shadow / #E0E6EA case highlight / #1E1E24 bezel black / #3A3A44 bezel highlight / #8EA894 LCD green / #52685A LCD segment / #B8CEC0 LCD highlight / #4A4A52 button grey / #8E9298 button worn / #4E8E5E corrosion / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Chunky rectangular silver-tone digital calculator watch face-on with the resin strap curving away, black bezel, small monochrome LCD with illegible pixel numerals a tiny alarm bell icon and two dead segment bars stuck on, dense grid of twenty-plus tiny dark grey square rubber buttons with several worn smooth and pale with the characters rubbed off, cracked resin strap at both spring-bar holes with a missing keeper so the tail sticks out, deeply scratched hazy crystal, green corrosion bloom at the battery hatch, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A8AEB4 case silver / #6E7478 case shadow / #E0E6EA case highlight / #1E1E24 bezel black / #3A3A44 bezel highlight / #8EA894 LCD green / #52685A LCD segment / #B8CEC0 LCD highlight / #4A4A52 button grey / #8E9298 button worn / #4E8E5E corrosion / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Hourly-beep FX frame (48x48)** — watch with four hard-edged radiating pixel sound arcs, for the comedy trigger.
- **Worn variant (32x32)** — on a wrist, sitting loose and rotated so the face is on the underside.
- **Calculator-in-use variant** — a finger poised over the buttons, for the Intelligence stat tooltip.

## 6. Art-director notes

- Button count is the joke. Twenty-plus tiny squares. If it reads as a normal watch, add buttons.
- Worn-blank buttons are the age tell — pick three or four to render as featureless pale squares.
- LCD stuck segments: two dark bars that clearly do not belong. Cheap detail, big payoff.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

