# Vintage Ring Light Mace

> **Asset slug:** `weapon-vintage-ring-light-mace`  
> **Type / slot:** Weapon — Chadwick (Top Pick)  
> **World:** Global  
> **Rarity / tier:** Signature / Upgradeable  
> **Canon source:** `chadwicksweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Basic attack with a chance to dazzle. Powers: Harsh Lighting, Going Viral, Engagement Boost, Viral Moment.

**Flavor text:** *"Three hundred dollars. Used twice. Now it's a mace."*

**Why it's funny (the thing the art has to sell):** A heavy circular ring light on a stick, swung like a morning star. He bought it in his 'serious content' era. Half the bulbs are dead. Every swing is a small funeral.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A heavy metal ring light mounted on a short steel haft to make a mace, held vertically with the ring at the top. The ring is a thick circular frame in scuffed matte black holding eight chunky halogen bulbs around its inner edge — four are lit a harsh pale white, two are dead grey-black, one is visibly cracked with a dark filament, and one is missing entirely leaving an empty socket with exposed wire pixels. The lit bulbs are rendered as flat saturated pale-white shapes with a hard-edged 1px brighter core, absolutely no glow or bloom. A frayed fabric-wrapped power cord is coiled around the haft as a makeshift grip, its plug dangling. The frame is dented on one side and scratched to bare aluminum along the outer edge. A small illegible pixel control dial on the haft.

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
#2B1A2E outline / #1E1E24 frame black / #38383E black mid / #56565E black highlight / #F8F8F0 bulb lit / #D0D0C4 bulb shadow / #FFFFFF bulb core / #4E4E56 bulb dead / #2A2A32 filament dark / #A8AEB4 bare aluminum / #7E7468 cord fabric / #C9A227 plug brass pin / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Heavy circular ring light mounted on a short steel haft as a mace held vertically with the ring at the top, thick scuffed matte black circular frame holding eight chunky halogen bulbs around the inner edge with four lit harsh pale white as flat saturated shapes with a hard 1px brighter core and no glow, two dead grey-black, one cracked with a dark filament and one missing leaving an empty socket with exposed wire pixels, frayed fabric-wrapped power cord coiled around the haft as a grip with the plug dangling, dented frame scratched to bare aluminum along the outer edge, illegible pixel control dial, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E1E24 frame black / #38383E black mid / #56565E black highlight / #F8F8F0 bulb lit / #D0D0C4 bulb shadow / #FFFFFF bulb core / #4E4E56 bulb dead / #2A2A32 filament dark / #A8AEB4 bare aluminum / #7E7468 cord fabric / #C9A227 plug brass pin / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **TIER 1 — Flickering Ring Light** — as described: four lit, four failed.
- **TIER 2 — LED Content Creator Array (64x64)** — the frame refinished in brushed silver, halogen bulbs replaced by a dense ring of small square LEDs all lit an even cool white, a slim battery pack on the haft, cord replaced by a neat braided sleeve.
- **TIER 3 — Professional Broadcast Halo (64x64)** — a wide sculpted ring in anodized dark grey with a continuous diffused LED band, a chunky counterweight at the haft's base, and four hard-edged pale pixel spokes radiating behind it.
- **Harsh Lighting FX frame (96x96)** — a hard-edged flat white pixel cone projecting forward with an enemy silhouette flattened inside it.
- **Battle idle sprite (48x48)** — front-view combat orientation.

## 6. Art-director notes

- Bulb states are the storytelling: four lit, two dead, one cracked, one missing. Count them out in the prompt every time.
- No glow on the lit bulbs. Flat saturated white plus a hard core pixel. This rule breaks constantly on light-emitting subjects — expect two or three regenerations.
- Three tiers share silhouette proportions. The upgrade arc is Chadwick's whole character, so generate all three together.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

