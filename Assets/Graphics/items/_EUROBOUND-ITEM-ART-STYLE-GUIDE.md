# Eurobound — Item Art Style Guide

Read this before generating anything in this folder. Every per-item file inherits these rules; the per-item file only overrides the subject, palette and variants.

---

## 1. The research finding that changes everything

**EarthBound has no item icons.** The SNES inventory is a plain text list — "Cracked Bat," "Fry Pan," "Cup of Lifenoodles" — rendered in a windowed text box. There is no sprite to copy.

So "EarthBound-style item icons" is an invention, and the reference has to be assembled from the things EarthBound *did* draw:

| Source | What we take from it |
| --- | --- |
| Overworld object sprites (mailboxes, trash cans, hot dog stands, phones) | Chunky forms, thick dark outlines, 3-tone flat shading, hard elliptical drop shadows |
| Enemy sprites | The clay-model look — Itoi's team sculpted enemies in clay, photographed them, and pixelated the photos. Forms bulge. Nothing is symmetrical. Edges are soft in silhouette but hard in pixel |
| Shop signage and interior props | Warm, grubby, slightly desaturated palette; hand-lettered chunky forms |
| Mother 2 print/manual illustration | The comedic register — mundane objects treated with total sincerity |

**The clay-model rule is the single most important one.** It is what separates this from generic pixel art. Every object should look like someone sculpted it slightly badly in Sculpey, lit it from the upper left, and photographed it.

## 2. Technical constraints

- **SNES sprite palettes are 16 colors** — 15 plus one transparency index. Every sprite in this set holds to that. (Confirmed against the EarthBound ROM palette tables: 8 palette entries, 32 bytes each, 15 colors + transparent.)
- **Native SNES resolution is 256×224.** Our target is a mobile-scaled 64×64 item icon with a 128×128 master.
- Color format on hardware is 15-bit BGR, so every hex in these files should be quantized to 5 bits per channel before it goes into the engine.

## 3. The shared style block

Every per-item file already contains this. It is repeated here so you can paste it into a fresh chat.

```text
- Medium: 1990s Super Nintendo item sprite, drawn in the visual language of EarthBound / MOTHER 2.
- Framing: one single object, centered, slight three-quarter front view, floating on a flat pure-magenta #FF00FF chroma-key field. Nothing else in frame.
- Pixels: chunky, deliberate, visible square pixels. No anti-aliasing. No soft gradients. No blur. Ordered/checkerboard dither only, used sparingly.
- Palette: hard limit of 16 colors (15 + transparency), SNES 15-bit-safe. Warm and a little grubby — brick red, mustard, dull teal, muddy denim, off-cream. Never neon-clean.
- Outline: 1px dark plum-brown #2B1A2E, never pure black. Outline thickens by one pixel on the underside of the object.
- Shading: flat cel shading, exactly three tones per material — base, one shadow, one highlight — plus a single hard specular pixel-cluster. Light source upper-left.
- Form language: slightly lumpy and hand-sculpted, as though the object were built out of modeling clay, photographed, then reduced to pixels. Edges bulge. Nothing is perfectly straight or perfectly symmetrical.
- Shadow: one small hard-edged elliptical drop shadow directly beneath the object, no blur, 1 tone darker than the key field.
- Readability: the silhouette must still read as the correct object when scaled down to 32x32.
```

## 4. The house palette

Individual items carry their own 16, but they all draw from this master set so the inventory grid reads as one game.

```
OUTLINE      #2B1A2E   plum-brown. Never #000000.
SHADOW       #6E5F72   cast shadow under every object.
KEY          #FF00FF   chroma background.

WARM         #A83A2E brick / #C98E2E beer amber / #C9A227 gold / #E8B430 mustard
COOL         #2E7E96 dull teal / #3E5E96 muddy denim / #1E3A6E navy
NEUTRAL      #EDE8D8 off-cream / #C9BFA6 dust / #8E8A82 grime / #4A443E dirt
METAL        #A8AEB4 nickel / #6E7478 metal shadow / #E0E6EA metal highlight
DECAY        #B84A16 rust / #4E8E5E verdigris / #C9BE8E yellowed
```

**Saturation is a tier signal.** Common items are grubby. Legendary and Mythic items (Four Loko, Monster, Sextuple Espresso, Portable DVD Player) are the only sprites allowed to be loud. Keep it that way and rarity reads without a border color.

## 5. Rules that break constantly — enforce them every regeneration

These generators fight the style in the same four ways every time:

1. **They add glow.** Anything light-emitting — glow sticks, ring light, LEDs, the absinthe flame, glowstick nunchucks — comes back with bloom. Fix: *"flat saturated color with a hard-edged 1px lighter core stripe, absolutely no glow, no bloom, no gradient, no transparency."*
2. **They make matte things glossy.** Matte black (Axe can, Monster can, Power Balance band) renders as shiny plastic. Fix: *"matte, chalky, non-reflective, no highlights on the black."*
3. **They render motion as blur.** Spinner ring, metronome pendant, espresso cup, pager alert. Fix: *"motion shown as a hard-edged solid-color duplicate offset, absolutely no blur or transparency."*
4. **They produce legible text.** Every label, engraving and screen in this set must be illegible pixel noise — it avoids a localization problem, a trademark problem, and a legibility problem at 32px all at once. Fix: *"all lettering is abstract illegible pixel shapes, no readable words or numbers."*

## 6. Post-process — every asset

1. Generate at 1024×1024.
2. Nearest-neighbor downsample to 128×128, then 64×64 in Aseprite.
3. Index to 16 colors (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline. The generator always leaves stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png`, keep the 128 as master.

**Treat every AI output as a paint-over base, not a shippable asset.** Neither Gemini Pro nor GPT Image 2 produces a true pixel grid — they produce a pixel-*flavored* raster that has to be resampled and repaired. Budget the hand-cleanup time; it is roughly equal to the generation time.

## 7. Canon flags raised while writing these

- **`absinthe-shot.md`** — source doc calls it "Prague Special." The World Naming Consistency Guide forbids real city names. Renamed here to **Debaucheryville Special**. `items.md` needs the same edit.
- **`bluetooth-earpiece-blinking-led.md`** — dual-listed in `items.md` (Utility) and `equipment.md` (Accessories, as "Bluetooth Earpiece (Always On)"). One sprite serves both; no second file needed.
- **`set-the-suburban-dad-regression.md`** — calls for white sneakers with crew socks, which does not exist as an individual entry in `equipment.md`. Built inside the set file. Consider promoting it to its own footwear item.
- **Real brand names are used throughout**, per author direction. Both Gemini and GPT Image 2 will refuse or distort some of these. Where a generator balks, the fastest workaround is to strip the brand from the prompt and keep the physical description — every subject block in this folder is written to be visually complete without the brand name doing any work.

## 8. Generation order

Some files depend on others being generated first:

1. **Consumables** — establishes the base palette discipline.
2. **Individual equipment** — accessories, headgear, torso, legs, footwear, necklaces, rings, watches, phones.
3. **Combo sets** — `set-*.md` files compose from finished member palettes. Do not generate these before their members exist or the colors will drift.
4. **Weapons** — signature weapons first at 256×256, then the alternates, then upgrade tiers in single sessions per weapon so each tier reads as the same object.

## 9. Sources

- [EarthBound / Sprite Palettes — Data Crystal](https://datacrystal.tcrf.net/wiki/EarthBound/Sprite_Palettes)
- [Objects & Effects — EarthBound — The Spriters Resource](https://www.spriters-resource.com/snes/earthbound/asset/146838/)
- [MOTHER 2 Art – Models — Mother Forever](https://mother4ever.net/art-mother2-models/)
- [MOTHER 2 / EarthBound Official Game Art — Starmen.net](https://starmen.net/mother2/images/official/)
- [MOTHER 2 / EarthBound Game Sprites — Starmen.net](https://starmen.net/mother2/images/game/)
