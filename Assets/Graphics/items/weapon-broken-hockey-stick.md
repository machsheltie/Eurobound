# Broken Hockey Stick

> **Asset slug:** `weapon-broken-hockey-stick`  
> **Type / slot:** Weapon — Lord Pilsner (Alt)  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `lordpilsnersweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Slashing attacks, ice-themed abilities ironically deployed in the European heat.

**Flavor text:** *"Snapped clean through in a game he insists he was winning."*

**Why it's funny (the thing the art has to sell):** A snapped hockey stick with a jagged composite fracture. He talks about the play it broke on. The play does not sound like it happened.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A hockey stick snapped roughly two-thirds down the shaft, held with the blade end down. The remaining shaft ends in a violent jagged composite fracture — splintered dark carbon fibers fanning out as hard-edged irregular pixel spikes, pale grey inner core exposed. The shaft is matte black with a faded red and white graphic band rendered as blocky illegible pixel shapes. The blade is curved, taped in black cloth hockey tape that is fraying and grey with wear, with the tape unraveling at the toe. The blade's bottom edge is scuffed white and gouged from ice and concrete. A layer of white friction tape spirals up the shaft above the grip. Faint scoring and puck marks across the blade face.

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
#2B1A2E outline / #1A1A1E shaft black / #34343E black mid / #56565E black highlight / #C42A16 graphic red / #F0EDE2 graphic white / #8E9298 exposed core / #5E6268 core shadow / #4A443E tape worn grey / #E8E4D8 friction tape / #C4C8CC blade scuff / #7E7A72 puck mark / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Hockey stick snapped roughly two-thirds down the shaft held blade-end down, violent jagged composite fracture with splintered dark carbon fibers fanning out as hard-edged irregular pixel spikes and pale grey inner core exposed, matte black shaft with a faded red and white graphic band in blocky illegible pixel shapes, curved blade taped in fraying grey-worn black cloth hockey tape unraveling at the toe, bottom edge scuffed white and gouged, white friction tape spiraling up the shaft above the grip, faint scoring and puck marks across the blade face, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1A1A1E shaft black / #34343E black mid / #56565E black highlight / #C42A16 graphic red / #F0EDE2 graphic white / #8E9298 exposed core / #5E6268 core shadow / #4A443E tape worn grey / #E8E4D8 friction tape / #C4C8CC blade scuff / #7E7A72 puck mark / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Ice-ability FX frame (96x64)** — hard-edged pale-cyan pixel shard shapes radiating from the blade, deliberately absurd in a European summer setting.
- **Intact variant (64x64)** — the unbroken stick, for a flashback or trophy display.
- **Battle idle sprite (48x48)** — front-view combat orientation, blade raised.

## 6. Art-director notes

- The fracture is the item. Splintered composite as hard-edged irregular spikes with a pale core — do not let it render as a clean cut.
- Grey-worn black tape is the detail that says this stick had a long life before it broke. Fray the toe.
- Ice FX in a heat-wave setting is a running gag; keep the cyan aggressively out of place against the warm palette.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

