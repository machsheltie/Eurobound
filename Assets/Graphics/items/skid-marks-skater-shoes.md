# Skid-Marks Skater Shoes (Velcro Straps)

> **Asset slug:** `skid-marks-skater-shoes`  
> **Type / slot:** Footwear  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Grip, +1 Skater Cred, -2 Adult Credibility.

**Flavor text:** *"Velcro because laces are for try-hards."*

**Era Cringe:** Worn by someone who's never touched a skateboard.

**Why it's funny (the thing the art has to sell):** Skate shoes with velcro straps, worn by a man who has never once stood on a board. The soles are pristine because they have never done anything.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single chunky low-top skate shoe seen at a three-quarter side angle, absurdly padded — a fat rolled tongue, a thick puffed collar, and a wide gum-rubber cupsole. Black suede-effect upper rendered with a fine 1px stipple, with white leather side panels and an oversized illegible pixel logo patch. Two wide black velcro straps across the instep instead of laces, one strap curled up at the end with the hook side gone grey and furry with lint. The gum sole is bright orange-tan and completely unworn, with the factory tread pattern crisply intact. Slight creasing across the toe box. A stray thread at the heel tab.

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
#2B1A2E outline / #1E1A1C suede black / #383234 suede mid / #56504E suede highlight / #F0EDE2 leather white / #C4BFAE white shadow / #E8A65E gum sole / #B87A32 sole shadow / #FBD09E sole highlight / #8E9A9E velcro lint / #6E7278 lint shadow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single chunky low-top skate shoe at a three-quarter side angle, absurdly padded with a fat rolled tongue, thick puffed collar and wide gum-rubber cupsole, black suede-effect upper with a fine 1px stipple and white leather side panels and an oversized illegible pixel logo patch, two wide black velcro straps across the instep instead of laces with one strap curled and gone grey and furry, bright orange-tan gum sole completely unworn with crisp factory tread, slight toe-box creasing, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E1A1C suede black / #383234 suede mid / #56504E suede highlight / #F0EDE2 leather white / #C4BFAE white shadow / #E8A65E gum sole / #B87A32 sole shadow / #FBD09E sole highlight / #8E9A9E velcro lint / #6E7278 lint shadow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Pair variant (64x48)** — both shoes, one lying on its side showing the pristine sole. The unworn tread is the punchline.
- **Equipped variant** — on feet below the JNCO hem, mostly buried in denim.
- **Alt colorways** — white/red and an unwise all-brown.

## 6. Art-director notes

- Pristine sole is the joke. Explicitly forbid wear, scuffing or scratched tread on the outsole.
- Padding should look excessive — fat tongue, fat collar. Skate shoes of this era were architectural.
- Furry grey velcro is the one point of visible age, and it's on the strap, not the sole. Keep that contrast.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

