# Fake ID (Laminated at Kinko's)

> **Asset slug:** `fake-id-laminated-at-kinkos`  
> **Type / slot:** Consumable — Support / Key  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Grants access to restricted areas or age-gated content.

**Flavor text:** *"Works 60% of the time, every time."*

**Why it's funny (the thing the art has to sell):** A driver's license from a state the holder has never visited, laminated by hand with visible bubbles, bearing a photo of a man who is very obviously thirty-eight.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A landscape-orientation plastic ID card. Washed-out pale blue and grey card design with a state seal rendered as an unreadable pixel blob. The photo panel shows a blocky pixel portrait of a heavy-set balding man with a goatee, clearly middle-aged, badly lit. All text on the card is illegible pixel noise except a deliberately oversized birth-year field. The lamination is homemade — visible trapped air bubbles as small hard-edged pale ovals, and one edge where the laminate has separated and peeled up. Corners are unevenly trimmed. A hologram overlay is rendered as three sparse cyan-magenta pixels that clearly aren't doing anything.

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
#2B1A2E outline / #DCE4EA card pale blue / #A8B8C4 card shadow / #F4F8FA card highlight / #8E96A0 seal grey / #C4A88E photo skin / #8E6E52 photo shadow / #4A3E38 photo hair / #E8EEF2 laminate bubble / #3EC6D8 holo cyan / #D83EC0 holo magenta / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Landscape plastic driver license ID card in washed pale blue and grey, unreadable pixel state seal, blocky photo of a balding middle-aged goateed man, illegible pixel text, obvious trapped air bubbles in homemade lamination, one peeling separated laminate edge, unevenly trimmed corners, three sparse cyan-magenta hologram pixels, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #DCE4EA card pale blue / #A8B8C4 card shadow / #F4F8FA card highlight / #8E96A0 seal grey / #C4A88E photo skin / #8E6E52 photo shadow / #4A3E38 photo hair / #E8EEF2 laminate bubble / #3EC6D8 holo cyan / #D83EC0 holo magenta / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Confiscated variant** — card with a bouncer's black marker X across the photo, one corner snapped off.
- **Three-card wallet spread** — three different states, three different bad photos, same face.
- **Close-up photo panel (32x32)** — just the portrait, for the ICQ profile-picture gag.

## 6. Art-director notes

- The photo is where the joke lands. Make him unmistakably late-thirties: receding hairline, goatee, tired eyes. Do not let the generator make him young.
- Air bubbles in the lamination must be hard-edged pale ovals, not soft blobs.
- The oversized birth year is the only legible element — but leave the actual digits to the game's text layer, render it as a blank raised panel.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

