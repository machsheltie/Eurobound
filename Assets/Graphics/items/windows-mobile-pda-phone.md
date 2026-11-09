# Windows Mobile PDA Phone (Crashes Frequently)

> **Asset slug:** `windows-mobile-pda-phone`  
> **Type / slot:** Cellphone  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Business Cred, ICQ Compatible, Random "Blue Screen" debuff.

**Flavor text:** *"Runs a full desktop OS! What could go wrong?"*

**Era Cringe:** Requires stylus and 5-minute boot time.

**Why it's funny (the thing the art has to sell):** It runs a full desktop operating system on a device the size of a deck of cards, which means it crashes exactly as often as a desktop and takes five minutes to come back. He considers this a feature.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A bulky slab PDA phone in matte charcoal with a chrome-effect bezel, held vertically, noticeably thicker than it needs to be. A large square touchscreen dominates the front, currently displaying a solid deep blue field with four rows of small illegible white pixel text — a crash screen, unmistakably. A tiny stylus sits in its silo along the right edge, its tip bent. A hardware button row along the bottom with four worn silver keys and a five-way pad. The chrome bezel is peeling at two corners, exposing dull plastic. A soft-reset pinhole is visible on the side, ringed with scratches from repeated jabbing. A stretched-out screen protector is bubbled and peeling at one corner.

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
#2B1A2E outline / #32323A charcoal / #1C1C22 charcoal shadow / #56565E charcoal highlight / #A8AEB4 chrome bezel / #6E7478 chrome shadow / #E0E6EA chrome highlight / #1E3A96 crash blue / #2E52C4 blue mid / #EDF2FA crash text / #8E8A82 peeled plastic / #C4CAD0 protector bubble / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Bulky matte charcoal slab PDA phone with a chrome-effect bezel held vertically and noticeably too thick, large square touchscreen showing a solid deep blue crash field with four rows of small illegible white pixel text, tiny stylus with a bent tip in its right-edge silo, bottom hardware row of four worn silver keys and a five-way pad, chrome bezel peeling at two corners exposing dull plastic, soft-reset pinhole ringed with scratches from repeated jabbing, bubbled peeling screen protector, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #32323A charcoal / #1C1C22 charcoal shadow / #56565E charcoal highlight / #A8AEB4 chrome bezel / #6E7478 chrome shadow / #E0E6EA chrome highlight / #1E3A96 crash blue / #2E52C4 blue mid / #EDF2FA crash text / #8E8A82 peeled plastic / #C4CAD0 protector bubble / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Blue Screen debuff icon (24x24)** — just the blue crash field with three text rows, for the status strip.
- **Booting variant (48x48)** — screen showing a hard-edged pixel progress bar frozen at 12%, for the five-minute boot gag.
- **Reset-pinhole close-up (32x32)** — the scratched ring around the pinhole, for the tooltip.

## 6. Art-director notes

- The crash screen is the hero state and should be the base icon, not a variant. That's unusual and correct here.
- Blue field must be flat and hard-edged with no glow. White text rows stay illegible.
- Peeling screen protector is the detail that says 'he tried to take care of this once.' Small, sad, keep it.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

