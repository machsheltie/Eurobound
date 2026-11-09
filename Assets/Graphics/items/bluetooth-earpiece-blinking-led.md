# Bluetooth Earpiece (Blinking LED)

> **Asset slug:** `bluetooth-earpiece-blinking-led`  
> **Type / slot:** Consumable — Utility / Accessory (dual-listed)  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `items.md + equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

> [!] **Canon flag:** Dual-listed in both `items.md` (Utility) and `equipment.md` (Accessories, as "Bluetooth Earpiece (Always On)"). One sprite serves both entries — no need for separate art.

---

## 1. What this thing is

**Effect:** **As item:** allows remote communication during stealth sections. **As accessory:** +2 Multitasking, -3 Social Awareness.

**Flavor text:** *"Yes, I'm talking to you. No, I'm not crazy."*

**Era Cringe:** Worn even when not on a call, flashing blue LED.

**Why it's funny (the thing the art has to sell):** He wears it at dinner. He wears it in the shower, probably. The blinking blue LED is a beacon announcing that this man believes he is important.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single over-ear Bluetooth earpiece in glossy black plastic with a chrome accent strip, seen at a three-quarter angle showing the ear hook curving away. The hook is bent slightly out of shape. A blue LED on the body is rendered as one hard saturated pixel with a tight 4-pixel cross of lighter blue around it — hard-edged, no glow. The rubber ear-tip is discolored, waxy and yellowed. A hairline crack runs across the chrome strip. Skin grease dulls the black finish near the ear-tip. Comically oversized for what it does.

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
#2B1A2E outline / #1A1A20 gloss black / #3E3E48 black highlight / #5A5A66 black spec / #A8AEB4 chrome / #6E7278 chrome shadow / #E8EEF2 chrome highlight / #1E7EF0 LED blue / #7EC4FF LED cross / #C9BE8E ear tip yellowed / #9E9268 ear tip shadow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single over-ear Bluetooth earpiece in glossy black plastic with a chrome accent strip, three-quarter angle showing the bent ear hook, blue LED as one hard saturated pixel with a tight 4-pixel cross of lighter blue and no glow, discolored yellowed waxy rubber ear tip, hairline crack in the chrome, greasy dulled black finish, comically oversized, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1A1A20 gloss black / #3E3E48 black highlight / #5A5A66 black spec / #A8AEB4 chrome / #6E7278 chrome shadow / #E8EEF2 chrome highlight / #1E7EF0 LED blue / #7EC4FF LED cross / #C9BE8E ear tip yellowed / #9E9268 ear tip shadow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn-on-ear variant (32x32)** — for the character equip preview.
- **LED-off variant** — for the dead-battery gag.
- **Charging-cradle variant** — earpiece in a chunky black dock, for the hostel nightstand prop.

## 6. Art-director notes

- The LED cross must stay hard-edged. Four pixels, orthogonal, one lighter tone. No bloom.
- Yellowed ear-tip is the detail that sells the age. Do not let the generator render it clean white.
- Oversize it. Modern earpieces are tiny; this one should look like a piece of 2007 call-center equipment.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

