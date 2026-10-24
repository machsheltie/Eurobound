# Nokia N-Gage (Gaming Phone Hybrid)

> **Asset slug:** `nokia-n-gage`  
> **Type / slot:** Cellphone  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Gaming Cred, Immune to "Signal Loss" debuff, ICQ Compatible, unlocks T9 minigame.

**Flavor text:** *"It's a phone AND a gaming device! The future is now!"*

**Era Cringe:** Requires holding it sideways to your face like a taco.

**Why it's funny (the thing the art has to sell):** A phone you have to hold sideways against your ear to use, which is the single funniest industrial design failure of the decade, and he defends it.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A vertically-oriented handheld gaming phone in dark grey and silver plastic with an aggressive curved 'shell' form. A small square color LCD in the upper center showing illegible blocky pixel menu text. A directional pad on the left and four action buttons on the right of the screen, plus a full numeric keypad below in tiny rounded silver keys. Critically: the earpiece speaker is on the narrow left EDGE of the device, not the front face — render this edge speaker grille clearly visible as a row of small dark pixel slots. A stubby rubber antenna nub at the top. The silver trim is scratched down to grey plastic at the corners. A game cartridge slot flap on the back edge, hanging slightly open. Greasy fingerprints on the screen.

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
#2B1A2E outline / #4E5258 body grey / #2E3238 grey shadow / #7A8086 grey highlight / #A8AEB4 silver trim / #6E7478 trim shadow / #E0E6EA trim highlight / #2A4E6E LCD blue / #4A7EA8 LCD mid / #7EB4D8 LCD text / #1A1A1E button dark / #8E8A82 scratch grey / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Vertically-oriented dark grey and silver handheld gaming phone with an aggressive curved shell form, small square color LCD with illegible blocky pixel menu text, directional pad on the left and four action buttons on the right of the screen, full numeric keypad below in tiny rounded silver keys, earpiece speaker grille clearly visible as dark pixel slots on the narrow LEFT EDGE of the device rather than the front face, stubby rubber antenna nub, silver trim scratched to grey plastic at the corners, cartridge slot flap hanging open on the back edge, greasy screen fingerprints, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #4E5258 body grey / #2E3238 grey shadow / #7A8086 grey highlight / #A8AEB4 silver trim / #6E7478 trim shadow / #E0E6EA trim highlight / #2A4E6E LCD blue / #4A7EA8 LCD mid / #7EB4D8 LCD text / #1A1A1E button dark / #8E8A82 scratch grey / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Sidetalking variant (48x48)** — the phone held flat against the side of a head silhouette, edge-on, exactly as designed. Generate this. It is the entire joke.
- **Cartridge variant (32x32)** — a tiny game cartridge, for the T9 minigame unlock item.
- **Cellphone shelf lineup (96x64)** — all five phones on a shop rack.

## 6. Art-director notes

- The edge-mounted speaker must be visible in the base icon or the sidetalking variant makes no sense. Call it out explicitly every regeneration.
- Do not let the generator render a modern smartphone. Emphasize 'thick, curved, physical keypad, tiny screen, 2003 industrial design.'
- Sidetalking variant is the highest-value asset here. Prioritize it over the base icon if time is short.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

