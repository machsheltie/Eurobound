# Proeflokaal 't Kansen - Complete PNG Asset Requirements

## 📋 Overview
Proeflokaal 't Kansen is a 400-year-old jenever distillery that has not changed because it has never needed to, and a floor covered in sawdust because it has always needed that. This document specifies every PNG asset for the proeflokaal: the unmarked alley entrance and head-height door, the long low tasting room, the eight metres of oak bar, the glass filled past the brim that you physically cannot lift, the Jenever Taste Test gauntlet, Kees and his twelve-word vocabulary, the back room you have to earn, and The Shakes. Its satirical essence in a sentence: they will pour you a drink you must bow to, and the sawdust was already there before you arrived.

**Location ID:** `shamsterdam_oldtown_proeflokaal_kansen_01`
**Theme:** Tourist overconfidence meeting weaponized tradition — 400 years of Dutch drinking culture in a room designed to absorb the consequences
**Zone:** Old Town, historic distillery district, down a narrow unmarked alley
**Hours:** 12 PM - 11 PM (civilized hours, uncivilized drinking)
**Primary Function:** Brewery Tour location #2 of 2 / skill-challenge hub — Traditional Method tutorial, Jenever Taste Test gauntlet (4 rounds + Kopstootje), The Shakes debuff, back room unlock, Oude Genever consumable, Canal Courage passive completion

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Jenever Amber | #FFBF00 | Liquid, bottle glass, gauntlet highlights |
| Oak Brown | #806517 | Bar slab, barrel tables, beams |
| Candlelit Cream | #FFF8DC | Light pools, wall wash, aged paper |
| Sawdust Tan | #D2B48C | Floor, footprints, spill absorption |
| Brass Warm | #B5892E | Foot rail, plaque, opener metalwork |
| Old Room Shadow | #2B2116 | Low-ceiling shadow, back room base tone |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/proeflokaal_t_kansen/
├── environment/
│   ├── proeflokaal_main_room.png
│   ├── proeflokaal_back_room.png
│   └── proeflokaal_exterior_fixtures.png
├── objects/
│   └── proeflokaal_glassware_objects.png
├── npcs/
│   ├── npc_kees_pim.png
│   └── npc_proeflokaal_patrons.png
├── effects/
│   └── proeflokaal_effects.png
└── ui/
    └── proeflokaal_ui.png
```

---

## 🕯️ Sprite Sheet 1: Main Tasting Room Background
**File:** `proeflokaal_main_room.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #806517, #FFF8DC, #D2B48C, #2B2116

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Room Backdrop | (0, 0) | 1920x1080 | Full scene: long narrow low-ceilinged room, eight-metre oak bar running left-to-right across the lower third, 200+ bottle wall behind it arranged by age, barrel tables along the right wall, sawdust across the entire floor, candle sconces at irregular 1624 spacing, one window at the far left admitting almost nothing, back room door dark at rear right, no stools anywhere |

### Technical Notes:
- Anchor points (document in layer names): bar centre at (960, 704), Kees station at (704, 640), gauntlet lineup at (1088, 672), back room door at (1728, 512), foot rail at (960, 832), barrel table slots at (1472, 768) / (1664, 832), one-chair slot at (1856, 896), window at (128, 384)
- Ceiling beams painted at 1080-height clearance so any character sprite over 96px visibly approaches them — the head-strike gag is a compositional promise
- Candle sconce positions painted dim; the flicker overlays (Sheet 7) composite on top and are the only animated light in the room
- Sawdust painted flat and even in the backdrop; the tileable sawdust patch and footprint overlays (Sheets 3 & 7) handle disturbance and depth
- No music-source props anywhere — the silence is intentional and must be visually consistent

---

## 🥃 Sprite Sheet 2: The Back Room Background
**File:** `proeflokaal_back_room.png`
**Dimensions:** 1024x768 pixels (standalone scene background — not atlased)
**Color Palette:** #2B2116, #806517, #FFBF00

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Room Backdrop | (0, 0) | 1024x768 | Smaller, darker, lower: hand-labelled master-distiller bottles on a single deep shelf, one barrel table centre, distillery family photographs going back generations on the left wall, the 100-Year Barrel in the right corner (touched annually, never opened, allegedly), and one chair — exactly one — for the truly fallen |

### Technical Notes:
- Anchor points: barrel table at (512, 448), 100-Year Barrel at (832, 384), the chair at (192, 544), private-stock shelf at (512, 192), family photo wall at (128, 256)
- Lighting is one degree dimmer and one degree warmer than the main room; this is the only visual reward for completing the gauntlet, so the grade difference must be immediately legible
- Room loads on demand only after the back room unlock flag is set — never preloaded with the main scene
- The single chair must be composed as the visual punchline of the room: isolated, spotlit, obviously used

---

## 🚪 Sprite Sheet 3: Exterior & Fixtures
**File:** `proeflokaal_exterior_fixtures.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #806517, #B5892E, #D2B48C, #FFBF00

### Exterior & Bar Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Alley Exterior & Low Door | (0, 0) | 384x384 | Narrow Old Town alley, 1624 brickwork, wooden door low enough that everyone hits their head, no meaningful signage |
| The Oak Bar (8 Metres) | (384, 0) | 512x256 | Massive slab worn smooth by 400 years of desperate grip |
| Low Ceiling Beam Run | (384, 256) | 512x128 | The hazard, drawn as a tileable horizontal run |
| Jenever Wall Display | (896, 0) | 128x384 | 200+ bottles arranged by age: jong, oud, zeer oud, "don't ask" |

### Room Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Barrel Table A | (0, 384) | 192x192 | An actual barrel that is also an actual table |
| Barrel Table B | (192, 384) | 192x192 | Variant with different stave wear and hoop rust |
| Brass Foot Rail | (384, 384) | 512x32 | The most touched object in the Netherlands |
| Back Room Door | (384, 416) | 96x192 | Unlocks post-gauntlet; closed and unremarkable until then |
| The 100-Year Barrel | (480, 416) | 128x192 | Touched annually, never opened, allegedly |
| Ceramic Jug Rack | (608, 416) | 128x192 | The dispensing system; jugs that overfill by design |
| Original Distillery Equipment | (736, 416) | 160x192 | Non-functional, displayed, magnificent |
| Historical Photo Cluster | (896, 384) | 128x128 | The building. It looks the same. |
| Newspaper Clipping Frame | (896, 512) | 128x96 | Notable patrons, all photographed horizontal |

### Signage & Instruction:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Traditional Drinking Method" Illustration | (0, 576) | 192x128 | Head back, no hands, glass overfilled — the historical instruction panel |
| Brass Plaque "Est. 1624" | (192, 576) | 192x64 | "Est. 1624 — Jenever — Proudly Confusing Tourists Since Then" |
| Faded Gold "Proeflokaal" Sign | (192, 640) | 192x64 | Barely visible above the door; they have not needed signs in four centuries |

### Floor, Light & Bottles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sawdust Floor Tile (Tileable) | (384, 608) | 256x256 | Seamless on all four edges, 2-inch depth implied, permanent slight crunch |
| Candle Wall Sconce | (640, 608) | 96x96 | Real candle, added-later iron bracket |
| Real Candle (Table) | (736, 608) | 64x96 | Barrel-table candle, drips accumulated |
| Bottle Shelf Strip | (800, 608) | 224x96 | Age-graded shelf run: jong / oud / zeer oud / "don't ask" |
| Standing Bar Front Panel | (0, 704) | 384x96 | Customer side, no stools, deliberate |
| Coat Hook Row | (0, 800) | 192x64 | The coat check. It is hooks. It is trust. |
| The One Chair | (192, 800) | 96x160 | For the truly fallen. Kees will point at it without unkindness. |
| Sawdust Broom | (288, 800) | 96x160 | Pim's instrument, swept daily, replaced weekly |
| Low Doorframe (Head Hazard) | (640, 704) | 128x160 | Freestanding prop for interior thresholds |
| Window (Minimal Light) | (768, 704) | 128x160 | Admits enough light to prove it is daytime and nothing more |
| Back Room Barrel Table | (896, 704) | 128x160 | Invitation only; technically you were invited |

### Detail & Back Room Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Oak Bar Wear Detail | (0, 864) | 192x96 | Elbow-polish close-up plate for camera push-ins |
| Sawdust Depth Cross-Section | (192, 864) | 192x96 | 2-inch depth cutaway; historical purpose, current purpose, same purpose |
| Master Distiller Hand-Labelled Bottles | (384, 864) | 192x160 | The good stuff, back room only, handwriting not typeface |
| Distillery Family Photo Wall | (576, 864) | 192x160 | Generations, all with the same expression |
| Bar Towel + Spill Cloth | (768, 864) | 128x96 | Used constantly, never urgently |
| Unofficial Ceiling Warning | (896, 864) | 128x96 | Someone taped a note. It is at the wrong height. |
| Empty Glass Stack | (768, 960) | 128x64 | Thick-walled, waiting |
| Pim's Restock Crate | (896, 960) | 128x64 | Nephew labour, visible |
| Gauntlet Glass Rail | (0, 960) | 384x64 | The bar-top rail where five glasses are lined up |

### Technical Notes:
- Sawdust Floor Tile must seam on all four edges and tolerate 90° rotation without visible pattern repeat
- Back Room Door ships in one state; the unlock is communicated entirely by the glow overlay (Sheet 7), not by a second door sprite
- Brass Foot Rail is authored as a 512x32 tileable strip so it can run the full 8-metre bar at any scene width
- Low Ceiling Beam Run and Low Doorframe are separate props so the head-strike gag can be staged in both the main room and the back room passage

---

## 🍸 Sprite Sheet 4: Glassware, Gauntlet & Openers
**File:** `proeflokaal_glassware_objects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFBF00, #B5892E, #D2B48C

### Glassware:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Overfilled Tulip Glass (Surface Tension) | (0, 0) | 48x64 | Filled above the brim, convex meniscus visible — cannot be lifted |
| Tulip Glass (Normal Fill) | (48, 0) | 48x64 | What tourists expect. They will not receive it. |
| Tulip Glass (Spilled) | (96, 0) | 48x64 | Post-lift-attempt state |
| Tulip Glass (Empty) | (144, 0) | 48x64 | Post-bow state |
| Beer Chaser Glass | (192, 0) | 48x64 | "Also available. Yes." |
| Kopstootje Setup | (240, 0) | 128x64 | Jenever and beer arranged for the headbutt |
| Ceramic Pouring Jug | (368, 0) | 64x64 | The overfill instrument |
| Jenever Bottle (Jong) | (432, 0) | 32x64 | 4 Sovs — "Young. Starter." |
| Jenever Bottle (Oud) | (464, 0) | 32x64 | 6 Sovs — "Old. Respect required." |
| Jenever Bottle (Zeer Oud) | (0, 64) | 32x64 | 12 Sovs — "Very old. Very serious." |
| Jenever Bottle (Korenwijn) | (32, 64) | 32x64 | 15 Sovs — "Grain wine. Not for beginners." |
| Jenever Bottle ("Don't Ask") | (64, 64) | 32x64 | No label. No date. No questions. |

### The Gauntlet:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gauntlet Five-Glass Row | (96, 64) | 256x96 | Five glasses arranged jong → zeer oud, pre-composed as one block |
| Gauntlet Correct Marker | (352, 64) | 32x32 | Checkmark plate — "Correct." (no elaboration) |
| Gauntlet Wrong Marker | (384, 64) | 32x32 | Cross plate — "Wrong. Try again." (no elaboration) |
| Blind Test Cover | (416, 64) | 96x64 | Round 3 concealment cloth over four similar glasses |
| Back Room Special Glass | (416, 128) | 96x32 | 25 Sovs, 40%, "If you qualify." |
| Spill Puddle (Large) | (352, 96) | 64x64 | The moment before the sawdust does its job |
| Sawdust Fresh Patch | (0, 128) | 64x32 | Loose material for kick-up and absorption staging |
| Spill Puddle (Small) | (64, 128) | 32x32 | Drip-scale variant |

### Player States, Consumables & Openers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Traditional Bow Position | (0, 160) | 96x96 | Player character bowing to the drink, because that is the technique |
| Lift Attempt / Spill Frame | (96, 160) | 96x96 | The other option, performed once, learned permanently |
| Oude Genever (Consumable) | (192, 160) | 32x48 | +40 SP, The Shakes, cannot be used in combat |
| Oude Genever Inventory Icon | (224, 160) | 32x32 | Item icon |
| The Shakes Icon | (256, 160) | 32x32 | Trembling-hand silhouette with motion hatching |
| "Jenever Master" Title Ribbon | (288, 160) | 96x32 | Questionable accuracy |
| "Jenever Survivor" Title Ribbon | (288, 192) | 96x32 | More accurate |
| Proeflokaal Bottle Opener | (384, 160) | 48x48 | Overfilled tulip glass shape, convex meniscus, brass, "No Hands. No Fear." |
| Proeflokaal Opener Leather Loop | (432, 160) | 24x24 | Sawdust-coloured loop detail |
| Blarney Trap Bottle Opener (Publandia) | (456, 160) | 48x48 | The shamrock prerequisite — Kees checks for this first |
| Bottle Opener Keychain Ring | (192, 208) | 32x32 | The ring the stamps hang from |
| Brewery Stamp — Oude Genever | (224, 208) | 64x48 | Overfilled tulip glass stamp for the keychain |
| Newspaper Clipping (Horizontal Patron) | (288, 224) | 96x32 | Framed proof that this happens to everyone |
| Sawdust-Coloured Leather Strip | (384, 208) | 64x32 | Material reference plate for the opener loop |
| Kopstootje Combo Icon | (448, 208) | 32x32 | Two-glass silhouette |
| Korenwijn Icon | (480, 208) | 32x32 | Squat-bottle silhouette |

### Technical Notes:
- The overfilled glass and the normal glass must be visually distinguishable at 48px through meniscus curvature alone — this is the location's central mechanic and cannot rely on a UI label
- Jenever bottles are shape-coded by neck length and shoulder profile (jong tall/narrow → korenwijn squat/wide) so the gauntlet is winnable colorblind
- Gauntlet Five-Glass Row ships pre-composed to keep the challenge at one draw call
- Both bottle openers render in the keychain UI at native 48x48; do not scale up

---

## 🧔 Sprite Sheet 5: Kees & Pim
**File:** `npc_kees_pim.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #806517, #D2B48C, #FFF8DC

### Bartender Kees — Service:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kees Idle | (0, 0) | 64x96 | 60s, built like the barrel he tends, apron older than most tourists |
| Kees Pour Frame 1 | (64, 0) | 64x96 | Jug raised, glass placed |
| Kees Pour Frame 2 | (128, 0) | 64x96 | Stream at the brim |
| Kees Pour Frame 3 | (192, 0) | 64x96 | Surface tension achieved, jug withdrawn, expression unchanged |
| Kees Nod Frame 1 | (256, 0) | 64x96 | The nod begins. This is rare. |
| Kees Nod Frame 2 | (320, 0) | 64x96 | The nod completes. This is the highest praise available. |
| Kees "Wrong." | (384, 0) | 64x96 | No elaboration frame |
| Kees "Correct." | (448, 0) | 64x96 | Also no elaboration frame; deliberately near-identical to "Wrong." |

### Kees — Instruction & Gatekeeping:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kees Demonstrating the Bow | (0, 96) | 64x96 | "Glass full. You bend. You drink. Simple." |
| Kees Pointing at Sawdust | (64, 96) | 64x96 | "Sawdust is there for this. Not the first time. Continue." |
| Kees Pointing at Chair | (128, 96) | 64x96 | "The chair is there." (not unkindly) |
| Kees Pointing at Back Room | (192, 96) | 64x96 | "Acceptable. Back room is there." |
| Kees Opener Check — Blarney Trap Only | (256, 96) | 64x96 | *nods* "Seamus." *points to gauntlet setup* |
| Kees Opener Check — Both Openers | (320, 96) | 64x96 | *nods once* "You have the glass. You earned it. Or bought it." |
| Kees Opener Check — No Shamrock | (384, 96) | 64x96 | "No shamrock." *waits* "No tour." *waits* |
| Kees Gauntlet Lineup Gesture | (448, 96) | 64x96 | Five glasses placed, one motion |

### Portraits & Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kees Portrait (Neutral, Eternal) | (0, 192) | 128x128 | Nothing surprises him. Nothing impresses him. Nothing. |
| Kees Portrait (The Nod) | (128, 192) | 128x128 | The single frame in the entire game where he approves of you |
| Pim Portrait | (256, 192) | 128x128 | Slightly more expressive. Slightly less eternal. |
| Kees Wiping Bar | (384, 192) | 64x96 | Ambient loop frame |
| Kees Kopstootje Setup | (448, 192) | 64x96 | Jenever placed, beer placed, no commentary |
| Reserve / Atlas Padding | (384, 288) | 128x32 | Reserved strip, do not paint |

### Assistant Barkeep Pim:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pim Idle | (0, 320) | 64x96 | Young, learning the trade, volunteered into the family business |
| Pim Restocking | (64, 320) | 64x96 | Crate to shelf, endless |
| Pim Sawdust Sweep Frame 1 | (128, 320) | 64x96 | Broom left |
| Pim Sawdust Sweep Frame 2 | (192, 320) | 64x96 | Broom right |
| Pim Physical Support | (256, 320) | 64x96 | Arm out, judgement absent |
| Pim Explaining His Uncle | (320, 320) | 64x96 | "He also doesn't frown. It's just... his face." |
| Pim Shrug | (384, 320) | 64x96 | "The trick is don't think about it." |
| Pim Back Room Reminiscence | (448, 320) | 64x96 | "I've been once. I don't remember it clearly." |

### Player & Accessibility Frames:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kees High-Contrast Silhouette | (0, 416) | 64x96 | Enhanced-visibility outline of the key interaction NPC |
| Player Bow Pose Frame 1 | (64, 416) | 64x96 | Approach and lean |
| Player Bow Pose Frame 2 | (128, 416) | 64x96 | Contact, sip, dignity intact |
| Player Lift-Attempt Fail | (192, 416) | 64x96 | Glass raised 2cm, catastrophe committed |
| Player The Shakes Frame | (256, 416) | 64x96 | Offset-by-2px duplicate for the vibration swap |
| Accessibility Reserve Block | (320, 416) | 192x96 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Kees "Wrong." and "Correct." must be near-identical by design — the joke is that his face carries no information, so the gauntlet UI must carry it instead
- Kees's three opener-check frames are selected by inventory state before any dialogue plays; the Blarney Trap check happens first and gates everything
- Player The Shakes frame is a 2px-offset duplicate of the idle pose; the debuff animates by swapping between them, never by transforming the sprite

---

## 👥 Sprite Sheet 6: The Patrons
**File:** `npc_proeflokaal_patrons.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Muted Old Town palette, candlelit-cream ambient grade

### Patrons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Regular (Ancient) | (0, 0) | 64x96 | Fifty years, his spot, immovable, territorial |
| Regular's Newspaper Pose | (64, 0) | 64x96 | One jenever per hour. Exactly. |
| Corporate Group (Failing) | (128, 0) | 256x96 | Matching polos, several floors in, one crying — happy or sad, unclear |
| Belgian Jenever Purist | (384, 0) | 64x96 | Solo, notebook, methodical, faintly superior |
| First Date Couple | (448, 0) | 128x96 | She has realised the situation. He has not. |
| Standing Patron A | (576, 0) | 64x96 | Bar filler, correct posture |
| Standing Patron B | (640, 0) | 64x96 | Bar filler variant |
| Floor-Sitting Tourist | (704, 0) | 64x96 | Already down. The sawdust is soft. |
| Bros Trio at Bar | (768, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley, pre-composed |
| Doorway Filler | (960, 0) | 64x96 | Head ducked, entering correctly for once |

### Portraits & Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Regular Portrait | (0, 96) | 128x128 | Speaks only Dutch, addresses no tourists, may offer you his couch |
| Belgian Purist Portrait | (128, 96) | 128x128 | "They invented it downriver, of course. But fine. Fine." |
| Corporate Crier Portrait | (256, 96) | 128x128 | "This counts as professional development. RIGHT?" |
| First Date (Her) Portrait | (384, 96) | 128x128 | "Maybe we just get ONE..." |
| Bow Poses Strip | (512, 96) | 256x96 | Four 64x96 stages: approach / lean / sip / straighten |
| Collapse Stages Strip | (768, 96) | 192x96 | Three 64x96 stages: swaying / bar-gripping / seated in sawdust |
| Sawdust-Dusted Clothing Overlay | (960, 96) | 64x96 | Post-failure garment layer, parents to any patron sprite |

### Ambient:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back-of-Bar Silhouette Row | (512, 192) | 256x64 | Cheap depth along the 8-metre bar |
| Corporate Polo Colour Variants | (768, 192) | 192x64 | Three 64x64 swatch heads for group recolour |
| Accessibility Reserve | (960, 192) | 64x64 | Reserved for high-contrast marker |
| Portrait Band Padding | (0, 224) | 512x32 | Reserved padding, do not paint |

### Technical Notes:
- Corporate Group and Bros Trio ship as pre-composed single blocks to protect the 14-draw-call budget
- Bow Poses Strip is palette-modulated onto any patron; never author per-NPC bow art
- Collapse Stages Strip drives the Corporate Group's visible decline over the session and doubles as the player's gauntlet-failure sequence

---

## ✨ Sprite Sheet 7: Effects — Candlelight, Sawdust & The Shakes
**File:** `proeflokaal_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFF8DC, #FFBF00, #D2B48C, #2B2116

### Light & Air:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Candle Flicker Frame 1 | (0, 0) | 64x64 | Real candlelight, low amplitude |
| Candle Flicker Frame 2 | (64, 0) | 64x64 | Mid |
| Candle Flicker Frame 3 | (128, 0) | 64x64 | Guttering |
| Candle Smoke Wisp | (192, 0) | 64x64 | Thin, slow, period-accurate |
| Sawdust Dust Motes Frame 1 | (256, 0) | 64x64 | Suspended in the window shaft |
| Sawdust Dust Motes Frame 2 | (320, 0) | 64x64 | Drift variant |
| Sawdust Kick-Up | (384, 0) | 64x64 | Footstep disturbance, one-shot |
| Jenever Vapour | (448, 0) | 64x64 | Juniper haze above a freshly poured glass |

### Liquid & Consequence:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Surface Tension Meniscus Overlay | (0, 64) | 64x64 | The convex dome that makes the glass unliftable |
| Surface Tension Break / Spill | (64, 64) | 64x64 | The instant the dome fails |
| Spill Absorption Into Sawdust | (128, 64) | 64x64 | Historical purpose fulfilled, in real time |
| The Shakes Vibration Overlay F1 | (192, 64) | 64x64 | Character-parented tremor plate |
| The Shakes Vibration Overlay F2 | (256, 64) | 64x64 | Offset tremor plate |
| Targeting Reticle Unstable | (320, 64) | 64x64 | Combat reticle wobble for the -15% Accuracy debuff |
| Kopstootje Impact Burst | (384, 64) | 64x64 | The headbutt, landing |
| Back Room Door Unlock Glow | (448, 64) | 64x64 | Warm rim-light on the rear door, one-shot then persistent |

### Ambient Grades & Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Window Light Shaft | (0, 128) | 128x128 | The room's only daylight, dust-bearing |
| Wall Sconce Pool | (128, 128) | 64x64 | Small warm floor pool under each sconce |
| Candlelit Room Grade Overlay | (192, 128) | 128x64 | Full-scene warm multiply plate |
| 100-Year Barrel Reverence Glow | (320, 128) | 64x64 | Back room only, extremely subtle |
| Kees Nod Approval Glint | (384, 128) | 32x32 | The rarest particle in the location |
| Head-on-Beam Impact Star | (416, 128) | 32x32 | One-shot, 1624 architecture doing its work |
| Sawdust Crunch Glyph | (448, 128) | 32x32 | Visual mirror of the constant underfoot crunch |
| Glass-on-Wood Glyph | (480, 128) | 32x32 | Visual mirror of thick glass hitting oak |
| Pour Sound Glyph | (128, 192) | 32x32 | Visual mirror of the precise pour |
| Spill Sound Glyph | (160, 192) | 32x32 | Visual mirror of the gentle-disappointment spill cue |
| Correct Answer Glyph | (192, 192) | 32x32 | Visual mirror of "Correct." |
| Wrong Answer Glyph | (224, 192) | 32x32 | Visual mirror of "Wrong. Try again." |
| Kopstootje Sequence Glyph | (256, 192) | 32x32 | Two-beat glyph for the shot-then-chaser cue |
| "Oh No" Ambient Glyph | (288, 192) | 32x32 | Visual mirror of the room's signature background sound |
| Tremolo (Shakes) Glyph | (320, 192) | 32x32 | Visual mirror of the debuff tremolo audio |
| Static Candle (Reduced Motion) | (352, 192) | 64x64 | Non-flickering candle substitute |
| Static Sawdust (Reduced Motion) | (416, 192) | 64x64 | Motionless mote plate |
| Dust-Free Grade Plate | (480, 192) | 32x64 | Clean-air variant of the window shaft |

### Technical Notes:
- Candle flicker is the only ambient animation in the room; if it is cut on Low LOD the scene must still read as candlelit via the static grade overlay
- The Shakes overlays parent to the affected character and to the combat reticle; there is no screen-space shake anywhere in this location
- Sawdust absorption is a one-shot triggered by any spill event and permanently darkens a 64x64 decal at the spill position until scene reload

---

## 🧭 Sprite Sheet 8: UI Elements
**File:** `proeflokaal_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #806517 UI chrome, #FFBF00 highlights, #2B2116 panel fill

### Gauntlet Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gauntlet Progress UI | (0, 0) | 256x128 | Four-stage tracker: Jong vs. Oud / The Middle Three / The Blind Test / The Kopstootje |
| Round Indicator Strip | (256, 0) | 256x64 | Four 64x64 round markers: pending / active / passed / failed |
| Jenever Age Identifier | (256, 64) | 192x64 | Jong / Oud / Zeer Oud selection labels with bottle-shape icons |
| Back Room Unlock Notification | (448, 64) | 64x64 | "Acceptable." — the only celebration this room permits |

### Technique & Status:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Traditional Method Tutorial | (0, 128) | 256x192 | The no-hands bow explained in three panels, optional, offered once |
| Kopstootje Timing UI | (256, 128) | 128x96 | Two-drink sequence bar: shot window then chaser window |
| The Shakes Status Bar | (384, 128) | 128x32 | 3-turn duration with stack indicator |
| Accuracy Penalty Readout | (384, 160) | 128x32 | Explicit "-15% Accuracy" text, not a colour bar |
| Opener Check Panel | (384, 192) | 128x128 | Kees's gate: Blarney Trap present? Proeflokaal opener present? |
| Menu / Price Board | (256, 224) | 128x96 | Eight-item list with Kees's one-line notes |
| First Drink Choice Panel | (256, 320) | 256x96 | "I'll lift it" / "Show me the traditional way" / "I know what I'm doing" |

### Quest & Rewards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Brewery Tour Progress (2 of 2) | (0, 320) | 128x96 | Shamsterdam brewery tour completion tracker |
| Canal Courage Passive Chip | (128, 320) | 128x96 | Small Shamsterdam flag icon, appears when the passive is active |
| Brewery Stamp — Oude Genever | (0, 416) | 64x64 | Overfilled tulip glass stamp, applied to the keychain |
| Blarney Trap Opener Icon | (64, 416) | 48x48 | Publandia prerequisite, shamrock |
| Proeflokaal Opener Icon | (112, 416) | 48x48 | Tulip glass with visible meniscus, brass, leather loop |
| Bottle Opener Keychain Panel | (160, 416) | 96x96 | The keychain with all earned stamps hanging |
| Title Plates (Master / Survivor) | (256, 416) | 128x64 | Two 128x32 plates: "Jenever Master" / "Jenever Survivor" |

### Icons & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Shakes Icon | (384, 416) | 32x32 | Trembling-hand silhouette with motion hatching |
| Liquid Courage Icon | (416, 416) | 32x32 | Upward-arrow-in-glass silhouette |
| Dignity Damage Icon | (448, 416) | 32x32 | Cracked-plate silhouette (recoverable) |
| Bravado Chip | (480, 416) | 32x32 | Shared-system chip, local styling |
| High-Contrast Bar Marker | (256, 480) | 64x32 | Bold outline for the bar interaction point |
| Glass Silhouette Set | (320, 480) | 128x32 | Five gauntlet glasses as stepped silhouettes with age labels |
| Touch-Zone Guide Overlay | (448, 480) | 64x32 | Dev-only 44px minimum overlay, stripped at build |
| Reserve / Padding | (0, 480) | 160x32 | Reserved strip, do not paint |

### Technical Notes:
- Every gauntlet answer target renders at 44px+ touch height; the five-glass row is subdivided into five discrete tap zones
- Jenever Age Identifier pairs each label with its bottle-shape icon so the gauntlet never depends on liquid colour, which is nearly identical across all five samples by design
- The Shakes readout shows explicit numeric text alongside the bar — the debuff is mechanically meaningful and must never be colour-only
- Opener Check Panel is evaluated before the scene's dialogue system initialises; a missing Blarney Trap opener blocks the entire tour branch

---

## 🎬 Animation Specifications

### The Overfill Pour (Sheets 4, 5, 7):
- **Duration:** 2.4 seconds (0.6s jug raise, 1.2s pour, 0.6s meniscus settle)
- **Frames:** 3 Kees pour frames + meniscus overlay fade-in
- **Pattern:** Play once per drink ordered
- **Trigger:** Any jenever order
- **Purpose:** The glass must visibly become unliftable while you watch, so the choice that follows is informed
- **Audio Sync:** Jug lift at 0.0s; steady pour 0.6-1.8s; the pour does not stop when it reaches the rim — that half-second past the brim is the whole gag
- **Performance Optimization:** Medium LOD reduces to 2 frames; Low LOD uses pour frame 3 only with an instant meniscus

### Traditional Method Bow (Sheets 5, 6, 7):
- **Duration:** 2.0 seconds (0.5s approach, 0.5s lean, 0.6s sip, 0.4s straighten)
- **Frames:** 4 (Bow Poses Strip)
- **Pattern:** Play once per drink consumed by the correct method
- **Trigger:** Player selects "Show me the traditional way" or has already learned the technique
- **Purpose:** You are bowing to your drink. Because you are.
- **Audio Sync:** Sawdust shuffle at 0.0s; sip at 1.0s; glass-on-wood at 1.6s; tiny triumph sting at 2.0s
- **Performance Optimization:** None needed (4 frames, cheap, narratively load-bearing)

### The Lift Attempt (Sheets 4, 5, 7):
- **Duration:** 1.4 seconds (0.4s grip, 0.2s failure, 0.8s absorption)
- **Frames:** Lift-Attempt Fail + surface tension break + sawdust absorption decal
- **Pattern:** Play once, first drink, if the player chooses to lift
- **Trigger:** "I'll lift it" selection, or the losing half of "I know what I'm doing"
- **Purpose:** The sawdust exists for a reason and the reason is now demonstrated
- **Audio Sync:** Glass scrape 0.0s; spill splash at 0.4s; gentle-disappointment sting at 0.6s; Kees's "Sawdust is there for this." at 1.0s
- **Performance Optimization:** None needed (one-shot, comedy-critical — never cut)

### Candlelight Flicker (Sheet 7):
- **Duration:** 1.8 seconds per irregular cycle
- **Frames:** 3, played in a non-uniform order (1-2-1-3-2-1) so it never reads as a loop
- **Pattern:** Continuous during all open hours
- **Trigger:** Constant
- **Purpose:** Real candlelight is the only thing moving in a room that has not moved in 400 years
- **Audio Sync:** None (silence is intentional in this location)
- **Performance Optimization:** Low LOD replaces all sconces with the static candle plate and relies on the room grade overlay; disabled in reduced-motion mode

### The Jenever Taste Test Gauntlet (Sheets 4, 5, 8):
- **Duration:** Per round: 0.8s glass select, 0.6s judgment beat, 1.0s Kees reaction hold
- **Frames:** Correct/Wrong markers + Kees "Correct."/"Wrong." frames + round indicator advance
- **Pattern:** Four rounds sequential; accumulating Shakes stacks on failure
- **Trigger:** Player accepts the gauntlet (or purchases the 20 Sovs Flight)
- **Purpose:** A skill challenge where the judge's face gives you nothing, so the UI must
- **Audio Sync:** Glass lift 0.0s; 0.6s of silence; "Correct." or "Wrong." at 1.4s; round advance chime at 2.4s
- **Performance Optimization:** None needed (UI-driven, negligible cost)

### The Kopstootje (Sheets 4, 7, 8):
- **Duration:** 3.0 seconds (1.2s bow-and-shoot window, 0.3s transition, 1.5s chaser window)
- **Frames:** Bow strip + Kopstootje Impact Burst
- **Pattern:** One-shot final boss of the gauntlet, two timed inputs
- **Trigger:** Gauntlet round 4
- **Purpose:** "Little headbutt." Two drinks, one moment, one very specific kind of regret
- **Audio Sync:** Jenever shot at 1.2s; beer grab at 1.5s; impact burst at 2.6s; on failure, the sawdust does its job at 3.0s
- **Performance Optimization:** Impact burst reduced to a single flash frame on Low LOD

### The Shakes Onset (Sheets 5, 7, 8):
- **Duration:** 0.8s onset, then a 0.25s two-frame tremor cycle held for 3 combat turns
- **Frames:** 2 vibration overlays + unstable reticle
- **Pattern:** Onset → tremor loop → fade on expiry; stacks extend duration, not amplitude
- **Trigger:** Oude Genever, Zeer Oude Jenever, or any gauntlet failure
- **Purpose:** -15% Accuracy, visible in the hand and in the reticle, mechanically honest
- **Audio Sync:** Subtle tremolo bed for the duration
- **Performance Optimization:** Tremor at half rate on Low LOD; in reduced-motion mode the sprite holds still and only the numeric readout and reticle tint communicate the debuff

### Back Room Unlock (Sheets 3, 5, 7):
- **Duration:** 2.0 seconds (0.4s Kees nod, 0.6s point, 1.0s door glow bloom)
- **Frames:** 2 nod frames + point frame + unlock glow
- **Pattern:** One-shot ceremony, once per save
- **Trigger:** Gauntlet round 3 success
- **Purpose:** The highest praise available in this building, delivered in four words
- **Audio Sync:** "Acceptable." at 0.4s; "Back room is there." at 1.0s; low door creak at 1.8s
- **Performance Optimization:** Glow bloom replaced by an instant lit state in reduced-motion mode

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Bar Marker | Sheet 8 (256, 480) | 64x32 | Bold outline for the bar ordering interaction point |
| Glass Silhouette Set | Sheet 8 (320, 480) | 128x32 | Five gauntlet glasses as bold stepped silhouettes with age text labels |
| Kees High-Contrast Silhouette | Sheet 5 (0, 416) | 64x96 | Enhanced-visibility outline of the key interaction NPC |
| Accessibility Reserve Block | Sheet 5 (320, 416) | 192x96 | Overflow space for additional high-contrast variants |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Candle | Sheet 7 (352, 192) | 64x64 | Non-flickering candle substitute across all sconces |
| Static Sawdust | Sheet 7 (416, 192) | 64x64 | Motionless dust-mote plate |
| Dust-Free Grade Plate | Sheet 7 (480, 192) | 32x64 | Window shaft without drifting particles |
| Static Shakes Presentation | Sheet 8 (384, 128) + (384, 160) | 128x32 each | Reduced-motion replaces the tremor entirely with the bar and the "-15% Accuracy" text |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sawdust Crunch Glyph | Sheet 7 (448, 128) | 32x32 | Mirrors the constant underfoot crunch |
| Glass-on-Wood Glyph | Sheet 7 (480, 128) | 32x32 | Mirrors thick glass landing on oak |
| Pour Sound Glyph | Sheet 7 (128, 192) | 32x32 | Mirrors the precise pour |
| Spill Sound Glyph | Sheet 7 (160, 192) | 32x32 | Mirrors the gentle-disappointment spill sting |
| Correct Answer Glyph | Sheet 7 (192, 192) | 32x32 | Mirrors "Correct." |
| Wrong Answer Glyph | Sheet 7 (224, 192) | 32x32 | Mirrors "Wrong. Try again." |
| Kopstootje Sequence Glyph | Sheet 7 (256, 192) | 32x32 | Two-beat glyph for the shot-then-chaser timing windows |
| "Oh No" Ambient Glyph | Sheet 7 (288, 192) | 32x32 | Mirrors the room's signature background sound |
| Tremolo (Shakes) Glyph | Sheet 7 (320, 192) | 32x32 | Mirrors the debuff tremolo bed |

### Colorblind Considerations:
- Jenever ages are coded by bottle silhouette (neck length, shoulder width) and by written labels; the five gauntlet liquids are near-identical in colour by design and must never be the only differentiator
- Gauntlet correct/wrong markers use checkmark and cross shapes with distinct silhouettes, never green/red fill alone
- The Shakes is communicated by explicit numeric text, tremor motion, and reticle wobble — three independent channels
- Overfilled vs. normal glass reads through meniscus curvature and rim highlight geometry, not tint
- Touch zones minimum 44px for all five gauntlet glasses, the three first-drink options, the bar interaction, and both Kopstootje timing inputs

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) Traditional Method Tutorial, price board, brass plaque, and all portraits kept uncompressed (readable text and faces)
- **Fallback:** PNG high quality for `proeflokaal_main_room.png` and `proeflokaal_back_room.png` (candlelight gradient banding is visible under lossy compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| proeflokaal_environment | proeflokaal_exterior_fixtures | 1024x1024 |
| proeflokaal_characters | npc_kees_pim, npc_proeflokaal_patrons | 1024x1024 |
| proeflokaal_fx_ui | proeflokaal_glassware_objects, proeflokaal_effects, proeflokaal_ui | 1024x1024 |

*(proeflokaal_main_room.png loads standalone; proeflokaal_back_room.png loads on demand after the unlock flag. Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Irregular 3-frame candle flicker on every sconce, drifting dust motes, full pour and bow sequences, Shakes tremor, sawdust kick-up per footstep |
| Medium | Flicker on hero sconces only, dust motes at half density, pour at 2 keyframes, kick-up on player footsteps only |
| Low | Static candlelight (profile requirement), static sawdust (profile requirement), single-frame pour, no kick-up, one-shot lift-attempt spill retained |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 36 MB maximum
- **Particle Limit:** 12 (dust motes, candle smoke, sawdust kick-up)

### Performance Notes:
- Corporate Group and Bros Trio are pre-composed single blocks; maximum 4 individually animated NPCs on screen
- The back room is a separate scene load, never resident alongside the main room — this is what keeps a two-background location inside 36 MB
- All sconces share one AnimatedSprite2D texture with per-instance frame offset and randomised phase; one material, N instances
- Sawdust absorption decals are pooled at a hard cap of 8; the ninth spill overwrites the oldest

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (both room backgrounds, fixtures), AnimatedSprite2D (Kees, Pim, candles, pour, Shakes overlays), CPUParticles2D (dust motes, sawdust kick-up, candle smoke — not GPU), CanvasLayer (gauntlet UI, tutorial, opener check), Area2D (bar, gauntlet rail, back room door, barrel tables, the one chair)
- Special systems: two-key inventory gate (Blarney Trap opener required for tour access, Proeflokaal opener required for stamp and Oude Genever purchase), four-round gauntlet state machine with accumulating Shakes stacks, Traditional Method learned-flag, back room unlock flag with on-demand scene load, spill decal pool, Couchsurf offer trigger keyed to the rare Kees nod, Brewery Tour completion handshake with Brouwerij de Molen

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Pour frame 2 → 3 | Continuous pour that does not stop at the rim | 0.6-1.8s of pour |
| Bow strip frame 3 | Sip | 1.0s of bow |
| Bow strip frame 4 | Glass on oak + tiny triumph sting | 1.6s / 2.0s |
| Surface tension break | Spill splash + gentle-disappointment sting | 0.4s / 0.6s of lift attempt |
| Gauntlet judgment beat | Silence (deliberate) | 0.8-1.4s per round |
| Kees "Correct." / "Wrong." | Single flat word, no music | 1.4s per round |
| Kopstootje impact burst | Two-drink landing thud | 2.6s of kopstootje |
| The Shakes tremor loop | Subtle tremolo bed | Continuous during debuff |
| Back room door glow | Low creak | 1.8s of unlock |
| Any footstep | Sawdust crunch | Per step, always |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Shamsterdam Brewery Tour (2 of 2) | Brewery Tour Progress panel, Oude Genever stamp, keychain panel, both opener icons | Completing here closes out the Shamsterdam brewery pair |
| Canal Courage (Passive Unlock) | Canal Courage chip, small Shamsterdam flag icon | Awarded on completing both Shamsterdam breweries; 25% reduced Bravado loss while intoxicated |
| The Jenever Taste Test Gauntlet | Five-glass row, correct/wrong markers, Kees reaction frames, round indicators, Kopstootje timing UI | Four rounds; success grants Oude Genever x5, back room access, and the Jenever Master title |
| Traditional Method (Cultural Tutorial) | Tutorial panel, Kees Demonstrating the Bow, Bow Poses Strip, Lift-Attempt Fail | First drink; the choice between lifting and bowing is permanent characterisation |
| Couchsurf: The Regular | Regular portrait, Kees Nod frames, Kees Pointing gestures | Rare nod after gauntlet success → the Regular mutters, Kees translates: "He says you can stay." |
| The Footage (Chadwick) | Bros Trio block, Collapse Stages Strip | Chadwick auto-documents the gauntlet; success and failure both produce a content item |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| **Publandia (The Blarney Trap)** | **Blarney Trap Bottle Opener icon (Sheet 4 and Sheet 8); Kees's "Seamus." recognition frame (Sheet 5)** | **Hard prerequisite: without the shamrock opener in inventory, Kees's No-Shamrock frame plays and the entire brewery tour branch is locked. With it, he nods and says one word — "Seamus." — the cross-world handshake between Publandia and Shamsterdam.** |
| Brouwerij de Molen | Shared Bottle Opener Keychain panel and stamp ring | Partner brewery; completing both fires the Canal Courage passive with the shared flag icon |
| De Groene Gids | Staff dialogue hook referencing "trying the hard stuff" | Arriving here already affected raises the gauntlet difficulty modifier |
| The Tolerance Hostel | Kitchen gossip references "the place with the sawdust" | Sawdust-Dusted Clothing overlay persists into the hostel scene until the next sleep |
| FEBO Automat | Post-jenever recovery hook | Recommended absorption stop; The Shakes duration ticks faster after eating |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Four hundred years of tradition in a low room with a floor built for your failure"
- **Color Mood:** Amber liquid and oak brown under candlelit cream, sawdust tan underfoot — warm, close, unhurried, entirely unimpressed by you
- **Lighting:** Real candlelight as the only moving light, one narrow window doing almost nothing, wall sconces added centuries late and still barely helping
- **Texture:** Four-hundred-year elbow polish on oak, dry loose sawdust, thick uneven glass, cold brass, aged handwritten labels

### Environmental Storytelling:
- There are no stools. Standing is traditional; falling is also traditional.
- The sawdust is 2 inches deep and swept daily, which means it is used daily
- The ceiling is low enough to be a hazard and nobody has ever considered raising it
- There is exactly one chair in the entire establishment and it is not at a table
- The bottle wall's fourth category is literally labelled "don't ask"
- The framed newspaper clippings of notable patrons are all photographs of horizontal people

### Character Integration Notes:
- Kees's authority comes from stillness; he has more idle-hold frames than motion frames, deliberately
- Kees's "Correct." and "Wrong." faces are near-identical — the UI carries all the information, he carries none
- Pim is the only character in the room permitted more than one expression, and even then, barely
- The Regular must be composed as the most competent figure in every frame he appears in, including frames where he is doing nothing
- The Corporate Group's decline is staged across three composited stages so the player can watch their own future arrive on schedule

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Surface Tension Glass** — liquid domed above the rim, the physical impossibility, the whole location in one 48px sprite
2. **The Traditional Bow** — a grown adult bending to a stationary drink in a 1624 room
3. **Kees's Nod** — two frames, once per playthrough, the highest praise available
4. **The Sawdust Doing Its Job** — spill, absorption, and a man pointing at the floor without judgement
5. **The One Chair** — isolated in the back room, obviously used, entirely uncommented on

### Quote Potential:
- "Glass full. You bend. You drink. Simple."
- "Sawdust is there for this. Not the first time. Continue."
- "Wrong. Try again."
- "Acceptable. Back room is there."
- "The chair is there."
- "No shamrock. No tour. Return. With opener."
- "Four hundred years of tradition in one glass. Your ancestors are watching. They're disappointed but not surprised."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | proeflokaal_main_room.png | 1920x1080 |
| 2 | proeflokaal_back_room.png | 1024x768 |
| 3 | proeflokaal_exterior_fixtures.png | 1024x1024 |
| 4 | proeflokaal_glassware_objects.png | 512x256 |
| 5 | npc_kees_pim.png | 512x512 |
| 6 | npc_proeflokaal_patrons.png | 1024x256 |
| 7 | proeflokaal_effects.png | 512x256 |
| 8 | proeflokaal_ui.png | 512x512 |

**Total Estimated Memory:** ~19.8 MB in-memory (uncompressed RGBA worst case) with both rooms resident; ~16.7 MB in normal play since the back room loads on demand. Within the 36 MB location budget.

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `proeflokaal_main_room.png` (1920x1080)
- [ ] `proeflokaal_back_room.png` (1024x768)
- [ ] `proeflokaal_exterior_fixtures.png` (1024x1024)
- [ ] `proeflokaal_glassware_objects.png` (512x256)
- [ ] `npc_kees_pim.png` (512x512)
- [ ] `npc_proeflokaal_patrons.png` (1024x256)
- [ ] `proeflokaal_effects.png` (512x256)
- [ ] `proeflokaal_ui.png` (512x512)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve layers in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet + candle flicker phase-offset table + sawdust tile seam test render

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#FFBF00, #806517, #FFF8DC, #D2B48C, #B5892E, #2B2116)
- [ ] Key gags read clearly: the meniscus above the rim at 48px, zero stools anywhere, the exactly-one chair, the "don't ask" bottle shelf, the ceiling that is genuinely too low
- [ ] Accessibility visual alternatives included for all audio cues (sawdust crunch, glass-on-wood, pour, spill, correct, wrong, kopstootje, "oh no", tremolo)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (tourist hubris is the target; the jenever tradition is treated with total sincerity)
- [ ] Hidden areas/interactions have discoverable visual cues (back room door present-but-unremarkable before unlock, the one chair, the 100-Year Barrel, Kees's rare nod)
- [ ] Performance optimized (CPU particles, atlas limits respected, on-demand back room load, static candle/sawdust fallbacks)
- [ ] Touch zone sizing considered (44px minimum for all five gauntlet glasses and both kopstootje inputs)
- [ ] Colorblind-friendly alternatives available where color codes meaning (bottle silhouettes, checkmark/cross shapes, numeric Shakes readout)
- [ ] Social media viral potential maximized in composition choices (meniscus close-up framing, bow staging, the isolated chair)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam Old Town; the Belgian purist references "downriver," never a real city |
| Cultural Specificity | ✅ | Dutch jenever and proeflokaal tradition, 1624 distillery, kopstootje, the no-hands method, sawdust floors |
| Satirical Targets Appropriate | ✅ | Tourist overconfidence and the "I can handle my alcohol" fallacy — the tradition itself is played entirely straight |
| Seedy Underbelly Present | ✅ | Drinks engineered to humble, priced to profit, served in a room pre-built to absorb the outcome |
| Gameplay Value Established | ✅ | Four-round gauntlet, Traditional Method tutorial, The Shakes debuff, back room unlock, Canal Courage passive, Couchsurf branch |
| Technical Feasibility | ✅ | Static candlelight/sawdust fallbacks per profile; on-demand back room load; pooled spill decals; pre-composed groups |
| Performance Budget | ✅ | 60 FPS, 14 draw calls, 36 MB, 12 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all nine audio cues, reduced-motion set including a non-tremor Shakes presentation, 44px touch zones |
| No Crypto Elements | ✅ | Pure 400-year tradition; the only ledger is the sawdust |
| Social Media Integration | ✅ | 5 screenshot moments + 7 quotable lines identified |

**Once these assets ship, Proeflokaal 't Kansen becomes the game's quietest humiliation: a low room, a glass you cannot lift, a floor that was already prepared for you, and a man who will say exactly one word if you get it right — and it will feel like a standing ovation.**
