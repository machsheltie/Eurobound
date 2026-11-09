# Sachertorte Slice

> **Asset slug:** `sachertorte-slice`  
> **Type / slot:** Consumable — Regional Specialty  
> **World:** Sinfonia  
> **Rarity / tier:** Rare  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Expensive but provides "Refined" status (social interaction bonuses). Also listed as HP++, cures Thirsty.

**Flavor text:** *"Classy enough to impress, sweet enough to remember."*

**Why it's funny (the thing the art has to sell):** The one genuinely elegant item in the entire inventory, and it costs more than everything else in the shop. The party bought it to seem cultured and ate it standing up outside.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A wedge of dense chocolate torte seen at a three-quarter angle on a small white porcelain plate with a thin gold rim line. The cake shows distinct horizontal layers: dark chocolate sponge, a thin bright apricot jam stripe, more sponge, topped with a smooth glossy dark chocolate glaze rendered with two hard-edged highlight bands. A small chocolate seal disc sits on top with an illegible embossed pixel mark. A generous quenelle of unsweetened whipped cream sits beside it, rendered as a rounded off-white mass with three hard shading tones. A silver dessert fork rests on the plate edge. One clean bite is already missing from the tip of the wedge.

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
#2B1A2E outline / #2E1A10 chocolate dark / #4A2C18 chocolate mid / #7E4E2A chocolate highlight / #E88A18 apricot jam / #B85E0A jam shadow / #FBF8F0 cream white / #D8D2C4 cream shadow / #F4F2EE porcelain / #C9C4B8 porcelain shadow / #C9A227 gold rim / #A8AEB4 fork silver / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Wedge of dense dark chocolate torte at a three-quarter angle on a small white porcelain plate with a thin gold rim, distinct horizontal layers of chocolate sponge with a bright apricot jam stripe, glossy dark chocolate glaze with two hard highlight bands, small embossed chocolate seal disc on top, quenelle of whipped cream beside it, silver dessert fork on the plate edge, one bite already missing from the tip, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #2E1A10 chocolate dark / #4A2C18 chocolate mid / #7E4E2A chocolate highlight / #E88A18 apricot jam / #B85E0A jam shadow / #FBF8F0 cream white / #D8D2C4 cream shadow / #F4F2EE porcelain / #C9C4B8 porcelain shadow / #C9A227 gold rim / #A8AEB4 fork silver / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Untouched variant** — no bite taken, for the Kaffeehaus Row shop display.
- **Refined status icon (24x24)** — a tiny fork and a raised pinky finger silhouette in hard pixels.
- **Boxed variant** — the torte in a small wooden presentation box, for the Sinfonia quest reward.

## 6. Art-director notes

- This is the highest-craft sprite in the food set — it is supposed to look genuinely good, because the joke is contextual, not visual. Do not make the cake gross.
- The apricot stripe is the identifying feature. Keep it bright and thin — one or two pixel rows, high chroma against the chocolate.
- Gold rim on the plate should be exactly 1px. Any thicker and it reads as cheap.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

