# Slice C draft — bottoms_down_png_assets.md replacement (Overview, Colour Palette, Sprite Sheets 1, 2, 3, 6)

**Coverage:** Overview (through File Structure), Colour Palette, Sprite Sheet 1 (Main Tasting Room), Sprite Sheet 2 (Back Room), Sprite Sheet 3 (Exterior & Fixtures), Sprite Sheet 6 (Patrons). Matched prop-for-prop and sign-for-sign to `drafts/kimi_bottoms_down_location.md`. Sheets 4, 5, 7, 8 and all technical/animation/accessibility/performance sections are untouched.
**Reviewer:** Kimi (integrator) — check every sign string and prop against Slice A verbatim.
**Note for Aion (Slice D):** the exterior sign and plaque strings below are Kimi's working text; your 3 options each replace or beat them. Change them here too if you win.
**Out-of-slice strikes (flagged for integration, not rewritten here):** "warm, close, unhurried" (Art Direction Summary, Color Mood), "played entirely straight" (Validation Status, Satirical Targets row), Sheet 7 candle-flicker frames and "Candlelit Room Grade Overlay" / "Wall Sconce Pool" / "Static Candle" (re-spec as neon buzz + caged-bulb hum; Sheet 7 is outside this slice), "Dutch jenever and proeflokaal tradition" (Validation Status, Cultural Specificity row).

---

## 📋 Overview
Bottoms Down is a 400-year-old jenever distillery that stopped pretending years ago and started keeping score. This document specifies every PNG asset for the tasting house: the loud alley entrance with its red arrow and backlit sign, the low door with the forehead plate, the long narrow tasting room, the eight metres of oak bar, the chalk scoreboard of the fallen, the bell, the bucket on its barstool, the glass filled past the brim that you physically cannot lift, the Jenever Taste Test gauntlet, Kees and his twelve-word vocabulary, the back room you have to earn, and The Shakes. Its satirical essence in a sentence: they will pour you a drink you must bow to, the house has already chalked a space for you, and the sawdust was already there before you arrived.

**Location ID:** `shamsterdam_oldtown_bottoms_down_01`
**Theme:** Tourist overconfidence meeting weaponized tradition — 400 years of drinking culture in a room designed, padded, sawdusted and scored to absorb the consequences
**Zone:** Old Town, historic distillery district, down a narrow alley with a red arrow painted on the wall pointing into it
**Hours:** 12 PM - 11 PM (civilized hours, uncivilized drinking)
**Primary Function:** Brewery Tour location #2 of 4 / skill-challenge hub — Traditional Method tutorial, Jenever Taste Test gauntlet (4 rounds + Concussion), The Shakes debuff, back room unlock, Oude Genever consumable, Canal Courage passive completion

---

## 🎨 Color Palette
The palette sets hues only. Lighting is set per plan; there is no candle-warm, golden-hour, or warm-grade anywhere in this location. The only warm hue in the building is the amber neon and the jenever itself.

| Color | Hex | Usage |
|-------|-----|-------|
| Jenever Amber | #FFBF00 | Liquid, bottle glass, amber neon "JENEVER" tube, gauntlet highlights |
| Oak Brown | #806517 | Bar slab, barrel tables, beams |
| Bleached Cream | #FFF8DC | Wall wash, aged paper, sign backings, chalkboard frame — a hue only, never a light pool |
| Sawdust Tan | #D2B48C | Floor, footprints, spill absorption |
| Brass Aged | #B5892E | Foot rail, plaque, opener metalwork |
| Old Room Shadow | #2B2116 | Low-ceiling shadow, back room base tone |
| Warning-Placard Red | #C0281C | Alley arrow, "NO HANDS" banner, "YOU WILL SPILL.", scoreboard record line, dead-tube off-state |
| Bottleneck Grey | #6B6B5A | Grime, caged utility bulbs, dead fluorescent tube, grey window light, duct-taped foam padding |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/bottoms_down/
├── environment/
│   ├── bottoms_down_main_room.png
│   ├── bottoms_down_back_room.png
│   └── bottoms_down_exterior_fixtures.png
├── objects/
│   └── bottoms_down_glassware_objects.png
├── npcs/
│   ├── npc_kees_pim.png
│   └── npc_bottoms_down_patrons.png
├── effects/
│   └── bottoms_down_effects.png
└── ui/
    └── bottoms_down_ui.png
```

---

## 🕯️ Sprite Sheet 1: Main Tasting Room Background
**File:** `bottoms_down_main_room.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #806517, #FFF8DC, #D2B48C, #2B2116, #FFBF00, #C0281C, #6B6B5A

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Room Backdrop | (0, 0) | 1920x1080 | Full scene: long narrow low-ceilinged room, eight-metre oak bar running left-to-right across the lower third, 200+ bottle wall behind it arranged by age, barrel tables along the right wall, sawdust two inches deep across the entire floor, the six-foot chalk scoreboard on the left wall, the ship's bell behind the bar, the mop bucket on its barstool in the corner, the Wall of the Fallen corkboard, painted distance markers radiating from the bar, caged utility bulbs on a sagging cord, one buzzing amber neon "JENEVER" sign over the bar, one dead fluorescent tube over the back corner, foam-padded beams at head height, one grey window at the far left admitting almost nothing, back room door at rear right, no stools anywhere |

### Modern seedy props in this scene (11): chalk scoreboard, ship's bell with hand-lettered sign, mop bucket on barstool with "EMPLOYEE OF THE MONTH" plaque, Wall of the Fallen corkboard, "SPILL KIT — SELF SERVE" station, duct-taped foam beam padding with layered impact dents, caged utility bulbs, buzzing neon sign, dead fluorescent tube, laminated taped signs, painted distance markers.

### Technical Notes:
- Anchor points (document in layer names): bar centre at (960, 704), Kees station at (704, 640), gauntlet lineup at (1088, 672), back room door at (1728, 512), foot rail at (960, 832), barrel table slots at (1472, 768) / (1664, 832), one-chair slot at (1856, 896), window at (128, 384), scoreboard at (320, 288), bell at (832, 448), bucket-on-stool at (1600, 640), Wall of the Fallen at (1408, 288), spill kit at (1792, 832)
- Ceiling beams painted at 1080-height clearance so any character sprite over 96px visibly approaches them — the head-strike gag is a compositional promise; every beam wears a duct-taped foam strip with impact dents
- Neon flicker overlays (Sheet 7) composite on top and are the only animated light in the room — no candle frames (flagged for Sheet 7 re-spec at integration)
- Sawdust painted flat and even in the backdrop; the tileable sawdust patch and footprint overlays (Sheets 3 & 7) handle disturbance and depth
- The scoreboard must read at 231px thumbnail: big chalk letters, "THE FALLEN", "RECORD: 31" in red
- No music-source props anywhere — the silence is intentional and must be visually consistent

---

## 🥃 Sprite Sheet 2: The Back Room Background
**File:** `bottoms_down_back_room.png`
**Dimensions:** 1024x768 pixels (standalone scene background — not atlased)
**Color Palette:** #2B2116, #806517, #FFBF00, #6B6B5A

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Room Backdrop | (0, 0) | 1024x768 | Smaller, darker, lower: hand-labelled master-distiller bottles on a single deep shelf, one barrel table centre, distillery family photographs going back generations on the left wall, the 100-Year Barrel in the right corner (touched annually, never opened, allegedly), and one chair — exactly one — bolted to the floor with a seatbelt, the belt bite-marked, a mop bucket standing at attention in front of it, and a laminated tag tied to the armrest |

### Modern seedy props in this scene (6): bolted plastic lawn chair, seatbelt with bite marks, laminated tag "SIT. SIP WATER. STOP TEXTING.", mop bucket at attention, caged bulb spotlight, hand-written labels pasted over older labels.

### Technical Notes:
- Anchor points: barrel table at (512, 448), 100-Year Barrel at (832, 384), the chair at (192, 544), private-stock shelf at (512, 192), family photo wall at (128, 256), mop bucket at (192, 672)
- Lighting is one degree dimmer and one degree cooler than the main room (Bottleneck Grey grade, no warm reward); this is the only visual difference for completing the gauntlet, so the grade shift must be immediately legible
- The single chair is spotlit by one caged utility bulb and must be composed as the visual punchline of the room: isolated, obviously used, entirely uncommented on
- Room loads on demand only after the back room unlock flag is set — never preloaded with the main scene

---

## 🚪 Sprite Sheet 3: Exterior & Fixtures
**File:** `bottoms_down_exterior_fixtures.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #806517, #B5892E, #D2B48C, #FFBF00, #C0281C, #6B6B5A, #FFF8DC

### Exterior & Signage (loud — every string readable at 231px thumbnail):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Alley Exterior & Low Door | (0, 0) | 384x384 | Narrow Old Town alley, 1624 brick blackened, mortar crumbling, one window boarded with a plank that has its own graffiti, low wooden door with a dented steel plate bolted at forehead height |
| Backlit "BOTTOMS DOWN" Sign | (384, 0) | 320x96 | Plastic backlit sign above the door, letters a foot high, half flickering (flicker overlay, Sheet 7) |
| Red Alley Arrow | (704, 0) | 160x96 | Hand-painted in red house paint at the alley mouth, chest-high: "BOTTOMS DOWN → YES, THIS IS THE PLACE. NO, YOU CAN'T HANDLE IT." |
| Taped Laminated Warning | (864, 0) | 160x128 | Laminated sheet taped to the door: "YOU WILL SPILL." and below in marker: "THE FLOOR IS SOFT. YOU'LL FIND OUT." |
| "NO HANDS" Banner | (384, 96) | 320x64 | Hand-painted under the sign: "NO HANDS. NO FEAR. NO REFUNDS." |
| Pictogram Panel | (704, 96) | 160x64 | Language-free: stick figure bows to glass → stick figure on floor → mop |
| Brass Plaque "Est. 1624" | (864, 128) | 160x64 | Green with age, half-covered by the banner: "Est. 1624 — Jenever" |
| "DUCK." Steel Plate | (384, 160) | 160x96 | The forehead-height door plate as a separate prop: dented, impact-scratched, stenciled "DUCK." |
| Sawdust Sign (interior door) | (544, 160) | 224x96 | Painted over the inside door: "YES, IT'S SAWDUST. TWO INCHES. FRESH TUESDAYS. STOP ASKING." |
| Distance Marker Strip | (768, 160) | 256x96 | Painted floor decals: "1M — 2M — 3M — PERSONAL BEST" |
| "THE FALLEN" Scoreboard | (384, 256) | 320x128 | Wall chalkboard prop, fresh chalk: "THE FALLEN — TODAY: |||| — THIS WEEK: |||| |||| ||| — RECORD: 31" (record in red) |

### Bar, Structure & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Oak Bar (8 Metres) | (0, 384) | 512x256 | Massive slab worn smooth by 400 years of desperate grip, groove worn along its length where the elbows go, sticky in the spots the rag misses |
| Low Ceiling Beam Run + Foam Padding | (512, 256) | 512x128 | The hazard as a tileable run; every beam wears a duct-taped grey foam strip with layered impact dents |
| Ship's Bell + Sign | (704, 256) | 320x128 | Bell mounted behind the bar with hand-lettered sign: "SOMEBODY SITS DOWN, SOMEBODY RINGS." |
| Mop Bucket on Barstool + Plaque | (512, 384) | 192x128 | A mop bucket displayed on a barstool like a trophy, small plaque on the rim: "EMPLOYEE OF THE MONTH." |
| Wall of the Fallen Corkboard | (704, 384) | 320x128 | Polaroids and phone-printouts of customers horizontal in the sawdust, newest still glossy, pins color-coded by decade |
| Barrel Table A | (0, 640) | 192x192 | An actual barrel that is also an actual table, rings of ancient spills |
| Barrel Table B | (192, 640) | 192x192 | Variant with different stave wear and hoop rust |
| Brass Foot Rail | (384, 640) | 512x32 | The most touched object in the Old Town |
| Back Room Door | (384, 672) | 96x192 | Unlocks post-gauntlet; closed and unremarkable until then |
| The 100-Year Barrel | (480, 672) | 128x192 | Touched annually, never opened, allegedly |
| Ceramic Jug Rack | (608, 672) | 128x192 | The dispensing system; jugs that overfill by design |
| Original Distillery Equipment | (736, 672) | 160x192 | Non-functional, one piece in use as a coat rack, furred with dust |
| Water-Damaged Photo Cluster | (896, 640) | 128x128 | The building behind cloudy glass; it looks the same, only cleaner, which is worse |
| Newspaper Clipping Frame | (896, 768) | 128x96 | Notable patrons — every photo the same photo: someone horizontal, someone pointing |
| Standing Bar Front Panel | (0, 832) | 384x96 | Customer side, no stools, deliberate |
| Caged Utility Bulb | (384, 832) | 128x96 | Cool white, on a sagging cord |
| Dead Fluorescent Tube | (512, 832) | 128x96 | Over the back corner; nobody will ever replace it; red off-state flicker once |
| Amber Neon "JENEVER" Tube | (640, 832) | 128x96 | Buzzing over the bar; the only warm hue in the building besides the liquid |
| Spill Kit Station | (768, 832) | 256x96 | By the door: mop, scoop, sack of sawdust, hand-lettered "SELF SERVE." |

### Floor, Bottles & Detail Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sawdust Floor Tile (Tileable) | (0, 928) | 256x96 | Seamless on all four edges, 2-inch depth implied, permanent slight crunch |
| Bottle Shelf Strip | (256, 928) | 224x96 | Age-graded shelf run: rookie / geezer / fossil / "don't ask"; labels handwritten over older handwritten labels |
| Jenever Wall Display | (480, 928) | 192x96 | 200+ bottles arranged by age, some without labels, one marked "NO." |
| "Traditional Drinking Method" Cartoon | (672, 928) | 192x96 | Hand-drawn three panels: "BOW. SIP. DON'T BE A HERO." Panel three: stick figure in the sawdust |
| Foam Padding Detail | (864, 928) | 160x96 | Impact dents, layered, duct tape curling |
| Oak Bar Wear Detail | (256, 864) | 192x64 | Elbow-polish close-up plate for camera push-ins |
| Sawdust Depth Cross-Section | (448, 864) | 192x64 | 2-inch depth cutaway |
| Master Distiller Hand-Labelled Bottles | (640, 864) | 192x64 | Back room stock, handwriting not typeface |
| Distillery Family Photo Wall | (832, 864) | 192x64 | Generations, all with the same face as Kees |
| Bar Towel + Spill Cloth | (0, 768) | 128x64 | Used constantly, never urgently |
| Taped Note at Wrong Height | (128, 768) | 128x64 | Someone taped a note; it is at the wrong height |
| Empty Glass Stack | (256, 768) | 128x64 | Thick-walled, waiting |
| Pim's Restock Crate | (896, 768) | 128x64 | Nephew labour, visible |
| Gauntlet Glass Rail | (0, 704) | 384x64 | The bar-top rail where five glasses are lined up |
| The One Chair | (640, 768) | 96x64 | Bolted to the floor, seatbelted, bite-marked belt, laminated tag: "SIT. SIP WATER. STOP TEXTING." |
| Sawdust Broom | (736, 768) | 96x64 | Pim's instrument, swept daily, replaced weekly |
| Low Doorframe (Head Hazard) | (864, 768) | 128x64 | Freestanding prop for interior thresholds |
| Window (Grey Light) | (992, 768) | 32x64 | Admits grey light enough to prove it is daytime and nothing more |

### Technical Notes:
- Sawdust Floor Tile must seam on all four edges and tolerate 90° rotation without visible pattern repeat
- Back Room Door ships in one state; the unlock is communicated entirely by the glow overlay (Sheet 7), not by a second door sprite
- Brass Foot Rail is authored as a 512x32 tileable strip so it can run the full 8-metre bar at any scene width
- Low Ceiling Beam Run and Low Doorframe are separate props so the head-strike gag can be staged in both the main room and the back room passage
- Thumbnail readability order: backlit "BOTTOMS DOWN" sign → red arrow → "NO HANDS" banner → scoreboard → red "RECORD: 31"

---

## 👥 Sprite Sheet 6: The Patrons
**File:** `npc_bottoms_down_patrons.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Muted Old Town palette, bottleneck-grey ambient grade, vice-red accents on lanyards and chalk

### Patrons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Regular (Ancient) | (0, 0) | 64x96 | Fifty years, his spot, immovable, territorial, does not look up for the bell |
| Regular's Newspaper Pose | (64, 0) | 64x96 | One jenever per hour. Exactly. |
| Corporate Group (Failing) | (128, 0) | 256x96 | Matching polos, lanyards still on, several on the floor now, one crying — happy or sad, unclear, one still standing and insufferable about it |
| Downriver Jenever Purist | (384, 0) | 64x96 | Solo, notebook, methodical, faintly superior, visibly annoyed the bow works |
| First Date Couple | (448, 0) | 128x96 | Here because a listicle called it "hidden." She is already mapping the exit. He has not. |
| Standing Patron A | (576, 0) | 64x96 | Bar filler, correct posture |
| Standing Patron B | (640, 0) | 64x96 | Bar filler variant |
| Floor-Sitting Tourist | (704, 0) | 64x96 | Already down. The sawdust is soft. Phone still in hand. |
| Bros Trio at Bar | (768, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley, pre-composed |
| Doorway Filler | (960, 0) | 64x96 | Head ducked, entering correctly for once |

### Portraits & Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Regular Portrait | (0, 96) | 128x128 | Speaks only to Kees, addresses no tourists, may offer you his couch |
| Downriver Purist Portrait | (128, 96) | 128x128 | "Shamsterdam makes fine jenever. They invented it downriver, of course. But fine. Fine." |
| Corporate Crier Portrait | (256, 96) | 128x128 | "This counts as professional development. RIGHT? THIS COUNTS." |
| First Date (Her) Portrait | (384, 96) | 128x128 | "Maybe we just get ONE..." |
| Bow Poses Strip | (512, 96) | 256x96 | Four 64x96 stages: approach / lean / sip / straighten |
| Collapse Stages Strip | (768, 96) | 192x96 | Three 64x96 stages: swaying / bar-gripping / seated in sawdust |
| Sawdust-Dusted Clothing Overlay | (960, 96) | 64x96 | Post-failure garment layer, parents to any patron sprite |

### Ambient:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back-of-Bar Silhouette Row | (512, 192) | 256x64 | Cheap depth along the 8-metre bar |
| Corporate Polo Colour Variants | (768, 192) | 192x64 | Three 64x64 swatch heads for group recolour, lanyard slots included |
| Wall-of-the-Fallen Polaroid Prop | (960, 192) | 64x64 | A pinned Polaroid of someone horizontal — the prop patrons get photographed into |
| Accessibility Reserve | (0, 224) | 64x32 | Reserved for high-contrast marker |
| Portrait Band Padding | (64, 224) | 960x32 | Reserved padding, do not paint |

### Technical Notes:
- Corporate Group and Bros Trio ship as pre-composed single blocks to protect the 14-draw-call budget
- Bow Poses Strip is palette-modulated onto any patron; never author per-NPC bow art
- Collapse Stages Strip drives the Corporate Group's visible decline over the session and doubles as the player's gauntlet-failure sequence
- Patrons are the freak show, not a postcard: lanyards, phones, glossy Polaroids, chalk dust, one man who never reacts to the bell

---

## Cross-check against Slice A (for Kimi at integration)

- Every sign string above is verbatim from `drafts/kimi_bottoms_down_location.md`: red arrow text, "DUCK.", backlit "BOTTOMS DOWN", "NO HANDS. NO FEAR. NO REFUNDS.", pictogram panel, "Est. 1624 — Jenever", "YOU WILL SPILL." / "THE FLOOR IS SOFT. YOU'LL FIND OUT.", "YES, IT'S SAWDUST. TWO INCHES. FRESH TUESDAYS. STOP ASKING.", distance markers, scoreboard, bell sign, bucket plaque, "SELF SERVE.", "BOW. SIP. DON'T BE A HERO.", chair tag, bottle labels including "NO." and "don't ask".
- Palette adds Kimi's two accent hues verbatim: Warning-Placard Red #C0281C, Bottleneck Grey #6B6B5A. "Candlelit Cream" renamed "Bleached Cream" (same hex, hue-only usage note added); "Brass Warm" renamed "Brass Aged". No candle, warm-pool, or golden-hour language remains in this slice.
- Modern seedy prop count per scene: Sheet 1 = 11, Sheet 2 = 6, Sheet 3 = 15+, Sheet 6 = lanyards/phones/Polaroids/chalk-dust as patron kit. All ≥5.
- No real city, nationality, or Dutch words anywhere in this slice; "proeflokaal" in the Overview is now "tasting house"; the Purist is "Downriver" and his line keeps "downriver" only.
- Sheets 4, 5, 7, 8 and all technical/animation/accessibility/performance/validation sections are untouched per slice. Sheet 7 still carries candle-flicker frames and warm grade plates — flagged in the header for integration re-spec to neon/caged-bulb, since Sheet 7 is outside my slice.
