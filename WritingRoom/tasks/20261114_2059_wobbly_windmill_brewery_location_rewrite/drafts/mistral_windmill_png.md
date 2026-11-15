# Mistral — Slice C: Wobbly Windmill Brewery PNG asset rewrite (loud / seedy / specific)

**Scope:** `design/worlds/shamsterdam/PNG_Assets/wobbly_windmill_brewery_png_assets.md` — Overview, Palette, and Sheets 1–4 (exterior, ground floor, grinding floor, tasting/blade), Sheet 7 (staff & patrons), plus the signage cells, matched to `drafts/kimi_windmill_location.md`. Animation / Accessibility / Performance / Technical Integration sections are carried with candle wording fixed only.
**Reviewer:** Kimi (integration). Deepseek — patron-sheet staging notes below answer your `npc_wobbly_windmill_cast.png` question directly.
**Ruled and untouched:** all 8 filenames, all sheet dimensions, all existing cell positions and sizes, all sprite labels except the four label-only renames listed below, all hex values already in the palette, all prices/hours/IDs/flags. Sign *wording* on the main sign, machinery sign and queue/gift-shop sign is Aion's slice D — cells here are marked [AION SIGN SHEET] and carry placeholder text only.
**Label-only renames (position/size/frames unchanged, so no engineering impact):**
- `Rustic Fixture` (Sheet 2) → `Utility Bulb Fixture` — "rustic" is banned painter-bait.
- `Candle Fixture Flicker 1-2` (Sheet 4) → `Tea-Light Cups (unlit) 1-2` — fire-code electric tea lights, never lit; flicker frames are the fluorescent tube's, reassigned.
- `Beer Blogger (German)` (Sheet 7) → `Beer Blogger (Big-City Paper)` — real nationality out; matches Kimi's patron block and Deepseek's Hendrik profile.
- `Bachelor Party Group` descriptions — "Dutch locals" → "Locals"; the stumble-frame quote loses the name "Johannes" (ucpf ruling): the shout is just "are we spinning?"
**Banned-word sweep:** charming, cozy, quaint, storybook, fairy-tale, rustic, heritage, faded, barely visible, warm candlelight, golden hour, half-timbered, ancient — all absent. "Dutch"/"German" absent. "Europe" absent (Euromemeia). vuqj-q3 honoured: palette sets hues only; lighting is per-plan, never candle-warm or golden-hour.
**New prop cells** are added only in free atlas space; no existing cell was moved or resized. Added cells are marked [ADDED CELL].
**Known pre-existing mismatch (noted, not fixed — filenames ruled):** sprite file `eva_tour_guide.png` vs. NPC "Tour Guide Tessa".

---

## 📋 Overview
The Wobbly Windmill Brewery is a 350-year-old working windmill in the Shamsterdam countryside converted into a craft brewery mini-dungeon — a spinning building where tourists pay 25 SOVS to be queued, counted and spun while Brewmaster Hendrik lectures about respecting the grain and a Yeast Golem rises from the grinding floor. This document specifies every PNG asset across the four floors (ground/gift shop, grinding floor boss arena, tasting room, blade level), the exterior and countryside approach, the Yeast Golem boss with all three phases, staff and visitor NPCs, and the tasting/selfie/opener systems. Its satirical essence in a sentence: a real machine wrapped in the loudest tourist trap in Euromemeia — backlit sign wider than the door, turnstile, queue rope, hazard tape — that charges you to get dizzy and sells you the mug on the way out.

**Thumbnail line (matches Kimi's Visual Design, revised per Deepseek's 231 px note):** *A windmill wearing a tourist trap: backlit sign wider than the door, queue rope and turnstile on the path, hazard tape on every visible surface.*

**Location ID:** `shamsterdam_countryside_wobbly_windmill_brewery_01`
**Theme:** "Authentic" experience tourism — paying premium to be processed, counted, spun and upsold; craft beer pretension; windmill fetishization
**Zone:** Shamsterdam Countryside (short train ride from central, 8 SOVS round trip, views are fields)
**Hours:** 11 AM - 8 PM (brewery tour hours, last tour at 6 PM)
**Primary Function:** Brewery Tour Location #1 / mini-dungeon — Yeast Golem boss battle, tasting flight system with Spin Meter, brewmaster speech endurance challenge, selfie timing mini-game, bottle opener gating (Blarney Trap prerequisite + Windmill opener), "Canal Courage" quest progress

---

## 🎨 Color Palette (hues only — hexes ruled, lighting set per plan, never candle-warm or golden-hour, vuqj-q3)
| Color | Hex | Usage |
|-------|-----|-------|
| Grain Gold | #DAA520 | Grain, beer, signage accents, chalk marks |
| Copper | #B87333 | Brewing vats, opener — reads COLD under caged bulbs, no fire-glow reflections |
| Windmill Wood | #8B4513 | Structure, beams, barrels — weather-dark below the balcony line |
| Flour White | #FFFAF0 | Dust haze, golem body, flour clouds, spill rings |
| Countryside Green | #6B8E23 | Flat fields parallax strip, train approach |
| Amber Neon | #FFB347 | (hex unchanged; label was "Candle Warm") Ground-floor neon "GRAIN" sign, amber accents. The ONLY warm hue in the building — it is electric, it hums, it is aimed at the merch |
| Hazard Yellow [ADDED HUE] | #FFD400 | Hazard tape, blade-warning placard, queue standing sign, turnstile accents |
| Grime Grey [ADDED HUE] | #6B6B5A | Fluorescent-lit grey, grimy metal, gear housings, worn grip tape |
| Retail White [ADDED HUE] | #E8E8E8 | Caged utility bulbs (cool white), fluorescent tube, laminated sign faces |
| CCTV Red [ADDED HUE] | #C0281C | Blinking dome, flickering sign letters, "OUT OF ORDER" tags |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/wobbly_windmill_brewery/
├── environment/
│   ├── wobbly_windmill_brewery_exterior.png
│   ├── wobbly_windmill_ground_floor.png
│   ├── wobbly_windmill_grinding_floor.png
│   └── wobbly_windmill_tasting_blade_level.png
├── npcs/
│   └── npc_wobbly_windmill_cast.png
├── boss/
│   ├── yeast_golem_battle.png
│   └── yeast_golem_phases.png
└── ui/
    └── wobbly_windmill_items_ui.png
```
*(unchanged — filenames ruled)*

---

## 🌾 Sprite Sheet 1: Exterior & Countryside
**File:** `wobbly_windmill_brewery_exterior.png`
**Dimensions:** 1024x768 pixels

### The Windmill:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Windmill Exterior Body | (0, 0) | 512x512 | Circa-1680 windmill, brewery conversion circa 2008. Cap and sails are the real thing; everything below the balcony line is signage, merch racks and hazard tape. Wood weather-dark, swollen, holding — dark the way a bar floor is dark |
| Blade Assembly Rotation 1-4 | (512, 0) / (704, 0) / (512, 192) / (704, 192) | 192x192 each | Four rotation positions; also driven by Godot node rotation for smooth spin. One gear rattles on every third pass (FX layer) |
| Entrance Door | (896, 256) | 96x128 | Heavy wooden door at the windmill base, "BREWERY" carved above it — carving doesn't glow |
| Accessibility Ramp | (896, 192) | 128x64 | Modern code-requirement ramp bolted against the old wood, with a small sign taking credit for it |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Backlit Sign [AION SIGN SHEET — main sign] | (896, 0) | 128x64 | Backlit plastic, letters a foot high, WIDER than the door, two letters flickering. Placeholder text: "THE WOBBLY WINDMILL BREWERY — EST. 1680 / 2008 / FOREVER." Final wording from Aion's sign sheet |
| Sandwich Board [AION SIGN SHEET] | (896, 64) | 128x32 | Peeling laminated board: "CRAFT BEER TOURS — TASTING FLIGHTS — GIFT SHOP." |
| Hazard Placard | (896, 96) | 128x64 | Bolted hazard-yellow: "WINDMILL OPERATIONAL — BLADES ROTATE — WATCH HEAD." |
| Liability Sign | (896, 160) | 128x32 | Smaller, under the placard: "The spinning is intentional. The dizziness is not our fault." |

### Approach:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Train Station Exterior | (512, 384) | 512x256 | Rural platform, transport hub, tourists photographing the windmill from the platform (the last free angle) and comparing tasting notes, holding the bench |
| Countryside Background | (0, 512) | 512x256 | Flat fields parallax strip (tileable horizontally) |
| Platform Tourist Cluster | (512, 640) | 256x128 | Tourists waiting for the return train |

### Loud tourist-trap props [ADDED CELLS — free space, right column / lower band]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Turnstile | (768, 384) | 64x96 | Just inside the door. Counts you. Small digital counter on the till displays the number like a high score |
| Queue Poles + Retractable Belt | (832, 384) / (896, 384) | 32x96 each | Switchback of retractable-belt queue poles on the path, deployed every day regardless of demand — for a party of three |
| Queue Standing Sign [AION SIGN SHEET — queue sign] | (768, 480) | 96x64 | Laminated, planted two metres from the door: "WAIT FROM HERE: 45 MIN." |
| Vending Machine | (896, 480) | 96x128 | Against the wall: motion-sickness pills, phone cables, earplugs. Earplug slot empty, has been for some time |
| Photo Cutout | (768, 576) | 128x96 | Plywood beer mug with three face holes, paint worn off at the chin rest |
| Tasting-Cup Bin | (896, 608) | 64x64 | By the door, overflowing with used tasting cups |

### Technical Notes:
- Blade assembly renders on separate node above windmill body; casts the interior window shadows (Sheet 3)
- Countryside strip tiles seamlessly for the "scenic" train ride transition
- Blade rotation speed varies with "wind" variable — sync with grinding mechanism speed
- Retail radio leaks from the building (audio, not sprite); no neighbours to complain to

---

## 🛍️ Sprite Sheet 2: Ground Floor & Gift Shop
**File:** `wobbly_windmill_ground_floor.png`
**Dimensions:** 1024x512 pixels

### Reception & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reception Desk | (0, 0) | 256x128 | "Reclaimed barrel wood" (claimed). Card reader taped over with handwritten note: "CASH ONLY. READER IS BROKEN. YES, STILL." Tour purchase point (25 SOVS) |
| Bottled Product Case | (256, 0) | 128x128 | Display bottles — available in gift shop, also reception, also bar, everywhere |
| Windmill History Panels | (384, 0) | 192x128 | Laminated, corners lifting. 5% windmill history, 95% beer marketing |
| Coat Hooks | (576, 0) | 64x128 | For the tasting flight aftermath |
| Gift Shop Shelving | (640, 0) | 256x128 | Branded EVERYTHING wall unit, merch stacked to the beams |

### Gift Shop Merchandise:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Branded Glasses Display | (0, 128) | 128x96 | "Wobbly Windmill" glasses 18 SOVS (the beer is 6 SOVS). Same mug in three sizes, each labelled a different "edition" |
| Mini Windmill Souvenirs | (128, 128) | 128x96 | 25 SOVS, made overseas, painted here — paint still tacky on the bottom row |
| Brewmaster's Book Stack | (256, 128) | 96x96 | "Respect The Grain" 35 SOVS, self-published, unreadable, display copy furred with grain dust |
| T-Shirt Rack | (352, 128) | 128x96 | "I SURVIVED THE SPIN" 30 SOVS (they know) |
| Survivor Pack Display | (480, 128) | 96x96 | Motion-sickness pills 3 SOVS + water 2 SOVS = 5 SOVS bundle. The MOST-STOCKED shelf in the building |

### Structure Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Curved Wall Segments 1-8 | (0, 224) to (224, 224), 32px steps | 32x32 each | Round-room wall pieces (it's a windmill) |
| Wood Plank Floor | (256, 224) | 32x32 | Base flooring |
| Worn Plank Floor | (288, 224) | 32x32 | Foot-traffic variant |
| Utility Bulb Fixture (was "Rustic Fixture") | (320, 224) | 32x64 | Caged utility bulb on a sagging cord, buzzing — the 2015 flat-pack purchase pretending to predate the building |
| Stairs Up | (384, 224) | 96x96 | To the grinding floor |
| Bram's Counter Zone | (480, 224) | 128x96 | Gift shop attendant post — unavoidable on entry AND exit |

### Loud/seedy props [ADDED CELLS — lower band y≥320]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Queue Rope | (0, 320) | 192x64 | Switchback between door and till, deployed even when the room is empty. Especially when it's empty |
| Neon "GRAIN" Sign | (224, 320) | 128x48 | Buzzing amber neon over the till — exists because the merch needed a mood |
| Till Counter Display | (384, 320) | 64x32 | Digital readout on the turnstile, displayed like a high score |
| CCTV Dome | (480, 320) | 48x48 | In the rafters, blinking red, aimed at the merch |
| Hand-Sanitizer Pump | (544, 320) | 32x64 | Bolted to the desk, empty, label peeling |
| Sticker Pole | (608, 320) | 32x128 | Support pole layered with stickers from every tour operator that has ever existed, like geology |
| No-Refunds Placard | (672, 320) | 128x32 | Laminated at the till: "NO REFUNDS. THE SPINNING IS ON THE WEBSITE." |

### Technical Notes:
- Curved wall segments assemble the circular room via TileMap
- Gift shop displays are interaction hotspots (44px+ click zones) with price-shock tooltips
- Lighting: grey daylight through small windows + caged bulbs + neon hum. Nothing glows warm except the neon and the beer

---

## ⚙️ Sprite Sheet 3: Grinding Floor (Boss Arena)
**File:** `wobbly_windmill_grinding_floor.png`
**Dimensions:** 1024x1024 pixels

### The Grinding Mechanism:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Millstone Mechanism Rotation 1-4 | (0, 0) / (256, 0) / (512, 0) / (768, 0) | 256x256 each | Massive central grindstone, connected to blades, actually grinding. Floor actually vibrates |
| Wooden Gears Large | (512, 256) | 192x192 | Original, terrifying, functional |
| Gear Small Rotation 1-2 | (704, 256) / (832, 256) | 128x128 each | Secondary gear meshing |
| Zip-Tied Gear Guard [ADDED CELL] | (896, 256) | 96x96 | The guard is held on with zip ties — the newest thing in the building. Rattles on every third pass (FX sync) |

### Brewing Equipment:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Copper Vat A / B / C | (0, 256) / (128, 256) / (256, 256) | 128x192 each | Hard-spotlit brewing vats around the circle, each with a drip pan underneath, each drip pan with a history |
| Grain Storage Bins | (384, 256) | 128x128 | Open-topped, safety concern, one with a scoop handle sticking out like a flag |

### Windows & Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Window Blade Shadow 1-4 | (0, 448) / (128, 448) / (256, 448) / (384, 448) | 128x128 each | Rotating blade shadow sweeping the room (disorienting) |
| Machinery Sign [AION SIGN SHEET — vuqj-q4] | (512, 448) | 160x64 | English header plus pictograms so it reads in every language and needs no words but the English: a hand with a red cross, a gear, a skull. Placeholder header: "DO NOT TOUCH MACHINERY." NOT five languages |
| Danger Rail | (672, 448) | 128x32 | Tourists grab this when the floor vibrates. The most-touched surface in the building |

### Arena & Atmosphere:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Vibration Overlay | (0, 576) | 512x128 | Shake-line overlay strip for grinding vibration |
| Flour Haze Overlay | (512, 576) | 256x256 | Semi-transparent dust atmosphere tile |
| Arena Floor Base / Flour-Dusted / Worn / Tape-Ring Gap | (0, 704) / (32, 704) / (64, 704) / (96, 704) | 32x32 each | Boss arena floor tiles. Last tile is the worn gap in the hazard-tape ring exactly where the golem rises — nobody has re-taped it |
| Grain Dust Particles 1-2 | (128, 704) / (192, 704) | 64x64 each | Constant ambient dust |
| Boss Spawn Dust Swirl 1-3 | (256, 704) / (352, 704) / (448, 704) | 96x96 each | Unnatural swirl pattern preceding golem rise |
| Stairs Up / Stairs Down | (768, 576) / (864, 576) | 96x96 each | Floor transitions |

### Seedy props [ADDED CELLS — y≥832 band]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Golem Chalkboard | (0, 832) | 128x96 | Nailed to a post: "DAYS SINCE LAST GOLEM: 0." The zero is chalked with unusual confidence |
| Flour-Furred Extinguisher | (160, 832) | 48x96 | Inspection tag dangling |
| Coin-Op Earplug Dispenser | (224, 832) | 64x96 | Mounted by the stairs, empty, knob painted shut |

### Technical Notes:
- Millstone rotation speed syncs to exterior blade speed (shared "wind" variable)
- Floor Vibration Overlay pulses while grinding — also ripples beer glasses (Sheet 8 liquid ripple)
- Flour haze density drops per LOD tier
- Zip-tied guard rattle is an FX/audio layer on every third gear pass, not a separate animated sprite
- Lighting: dusty grey daylight + single hard spotlight on the vats. Nothing glows warm; the vats glow industrially
---

## 🍺 Sprite Sheet 4: Tasting Room & Blade Level
**File:** `wobbly_windmill_tasting_blade_level.png`
**Dimensions:** 1024x512 pixels

### Tasting Room (Second Floor):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Barrel Table Variants 1-3 | (0, 0) / (96, 0) / (192, 0) | 96x96 each | Circle around the central shaft, logo-printed plastic tablecloths sticky in a way that predates tonight. Variant 3 carries the spill ring with its brass plaque |
| Spill Plaque [ADDED CELL] | (288, 128) | 96x32 | Brass plaque on one barrel table: "SPILL OF 2019 — LEST WE FORGET." The ring is still sticky |
| Brewmaster's Throne | (288, 0) | 96x128 | Fancy chair at head table, one armrest re-attached with a strap |
| Chalkboard Offerings | (384, 0) | 128x192 | Today's beers with pretentious descriptions ("notes of barnyard, verticality, consequence") under a FLICKERING fluorescent tube |
| Central Shaft Segment | (512, 0) | 64x192 | Rotating shaft through the room |
| Tasting Flight Board (set) | (576, 0) | 256x96 | Five glasses, escalating ABV (5% → 11%), escalating mistake |
| Tea-Light Cups (unlit) 1-2 (was "Candle Fixture Flicker") | (576, 96) / (640, 96) | 64x64 each | Row of electric tea lights in plastic cups on the shelf, NEVER lit since the grand opening — fire code bought them, the switch is behind the merch. Frame 1 = off; frame 2 = fluorescent flicker, not candle flicker. Reduced-motion holds frame 1 |
| Window Countryside Day | (832, 0) | 128x128 | Reorientation aid |
| Window Countryside Dusk | (832, 128) | 128x128 | Late-tour variant — still grey, never golden |

### Tasting-room seedy props [ADDED CELLS — y≥192 band]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Motion-Bag Dispenser | (0, 192) | 64x96 | Wall-mounted: "COMPLIMENTARY — TAKE ONE." Refilled hourly. Always empty |
| Charging Locker | (96, 192) | 64x96 | Door zip-tied shut, sign: "OUT OF ORDER." |
| Grip-Tape Rail Segment | (192, 192) | 96x32 | Railing grip tape worn smooth at hand height |
| Table Card "IT IS BOTH." | (288, 192) | 64x32 | Laminated card on every table: "IT IS BOTH." |
| Selfie-Window Grime + Squeegee | (384, 192) | 128x96 | Window overlooking blades, smeared with forehead and phone prints at exact standing height; squeegee hangs from the rail on a chain — the chain is the cleanest thing up here |

### Blade Level (Post-Boss):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Blade Level Platform | (0, 192) — see note | — | NOTE: blade-level cells below keep their ruled positions in the lower half of the sheet; the tasting-room added cells above use the y≥192 band left of x=384 only. Blade-level layout unchanged |
| Blade Level Platform | (0, 288) | 384x192 | Cramped platform below blade hub. Danger: theoretical — rails exist, lawyers insisted, bolts checked weekly, checklist taped to the door signed in advance through next month |
| Safety Railing | (384, 288) | 192x64 | Lawyers insisted |
| Wind Gust Lines | (384, 352) | 128x64 | SIGNIFICANT wind indicator |
| Selfie Spot Marker | (512, 352) | 64x64 | Photo trigger zone; floor stencil "STAND HERE," scuffed to a smear |
| Hair Chaos Overlay | (576, 288) | 96x96 | Wind-destroyed hair for photo results |
| Blade Sweep Close-Up 1-4 | (0, 384) / (256, 384) / (512, 384) / (768, 384) | 256x128 each | Selfie mini-game blade positions (dramatic → face-blocking) |

### Blade-level props [ADDED CELLS]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Photo Rig (OUT OF ORDER) | (640, 352) | 96x64 | Camera on a clamp, zip-tied to the rail, sign: "OUT OF ORDER." |
| Phone Lanyard Hook | (736, 352) | 32x64 | Labelled "PHONE LANYARDS." The hook is empty |
| Wind-Warning Pictogram | (768, 288) | 64x64 | Placard: a hat leaving a head. Pictogram, no words |
| Lost-and-Found Hat Bin | (832, 352) | 96x96 | Below the platform: eleven hats and one toupee [PROPOSED — Kimi's flag; cut the toupee, keep ten hats, if the author prefers] |

### Technical Notes:
- Blade Sweep frames drive the timing mini-game — frame 2 is the "Perfect Windmill Shot" window
- Tasting room applies progressive room-spin via shader (CanvasLayer rotation/warp), intensity = Spin Meter; no PNG overlay needed
- Reduced-motion: tea-light cups hold frame 1 (off); spin replaced with static vignette + "Dizzy" text
- Lighting: grey window light + one flickering fluorescent tube. No warm light anywhere; the beer is the warmest colour in the room

---

## 🍞 Sprite Sheet 5: Yeast Golem — Battle Core
**File:** `yeast_golem_battle.png`
**Dimensions:** 1024x1024 pixels
**Sprite Size:** 192x256 pixels
*(carried unchanged — no banned wording, no nationality, no lighting claims; palette hues per above)*

### Phase 1 "Rising Dough":
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rising 1-4 | (0, 0) / (192, 0) / (384, 0) / (576, 0) | 192x256 each | Emerges from grain dust and forgotten yeast cultures through the worn gap in the hazard-tape ring |
| Idle Breathing 1-3 | (0, 256) / (192, 256) / (384, 256) | 192x256 each | Semi-solid dough mass, slow bubble |
| Flour Cloud Attack 1-4 | (0, 512) / (192, 512) / (384, 512) / (576, 512) | 192x256 each | AoE cast — applies "Bleary" (-Accuracy) |
| Yeast Punch 1-4 | (0, 768) / (192, 768) / (384, 768) / (576, 768) | 192x256 each | Single-target doughy haymaker |
| Dough Hook 1-2 | (768, 256) / (768, 512) | 192x256 each | Phase 3 pull attack — drags party member into melee |

### Technical Notes:
- Weakness window after Flour Cloud: reuse Idle frame 3 with 20% brightness lift (shader), no extra sprite
- Body reads as flour-white (#FFFAF0) with grain-gold veining; fire/alcohol hits tint it toast-brown

---

## 🥖 Sprite Sheet 6: Yeast Golem — Phases & Adds
**File:** `yeast_golem_phases.png`
**Dimensions:** 1024x1024 pixels
*(carried unchanged)*

### Phase 2-3 Bodies:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Expanding 1-3 | (0, 0) / (256, 0) / (512, 0) | 256x320 each | Fermentation Frenzy growth — every 3 turns, bigger and slower |
| Final Rise Charge 1-3 | (0, 320) / (256, 320) / (512, 320) | 256x320 each | 2-turn massive AoE charge; vulnerability if hit with fire/alcohol |
| Collapse to Bread 1-4 | (0, 640) / (256, 640) / (512, 640) / (768, 640) | 256x320 each | Defeat: deflates into harmless loaf |

### Adds & Drops:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sourdough Sprite Idle 1-2 | (768, 0) / (864, 0) | 96x96 each | Weak summoned adds (Wild Fermentation) |
| Sourdough Sprite Attack 1-2 | (768, 96) / (864, 96) | 96x96 each | Tiny tangy lunge |
| Harmless Bread Loaf | (768, 192) | 96x64 | Post-defeat arena prop; drops Windmill Grist recipe |

### Technical Notes:
- Expansion frames anchor bottom-center so golem grows upward from arena floor
- Collapse frame 4 crossfades into Harmless Bread Loaf prop

---

## 👥 Sprite Sheet 7: Staff & Visitor NPCs
**File:** `npc_wobbly_windmill_cast.png`
**Dimensions:** 1024x384 pixels
**Sprite Size:** 64x96 pixels (groups noted)

### Staff (Row 0, y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hendrik Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Grain-grey canvas apron worn since 2008, gaffer-tape name strip across the chest (HENDRIK in marker — third strip), beard that could filter beer, house polo underneath. DEAD VERTICAL in every frame — he is the only vertical line in a room full of leaners |
| Hendrik Lecturing 1-4 | (128, 0) / (192, 0) / (256, 0) / (320, 0) | 64x96 each | 40-minute passion, arms conducting the grain. Lecture loop runs the entire endurance challenge; frames 2-4 shuffle randomly |
| Hendrik Approval 1-2 | (384, 0) / (448, 0) | 64x96 each | Post-golem respect nod — two frames, the whole reward |
| Tessa Idle 1-2 | (512, 0) / (576, 0) | 64x96 each | Brewery polo, practical shoes for catching people, lanyard with a whistle she has never blown |
| Tessa Pointing 1-2 | (640, 0) / (704, 0) | 64x96 each | Directing tour flow |
| Tessa Catch-Ready | (768, 0) | 64x96 | Trained reflexes for dizzy tourists — always between a tourist and a railing gap |
| Bram Idle 1-2 | (832, 0) / (896, 0) | 64x96 each | Gift shop, slightly bored, has stopped hearing the whoosh the way you stop hearing a fridge |

### Staff & Visitors (Row 1, y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bram Upsell 1-3 | (0, 96) / (64, 96) / (128, 96) | 64x96 each | "You could buy those glasses." |
| Beer Blogger (Big-City Paper) 1-2 (was "(German)") | (192, 96) / (256, 96) | 64x96 each | Notebook, reverent nodding, respects the grain — the one visitor who responds correctly |
| Repeat Visitor 1-2 | (320, 96) / (384, 96) | 64x96 each | Mysteriously unaffected by full flight; drinks without visible effect |
| Instagram Couple 1-2 | (448, 96) / (576, 96) | 128x96 each | 300 photos, zero beers; she has wiped a phone-sized circle in the selfie-window grime with a wet wipe |
| Bachelor Party Group Frame 1 | (704, 96) | 256x96 | Locals, further along in the flight, one wearing the "I SURVIVED THE SPIN" shirt he bought forty minutes ago over his other shirt |

### Visitors (Row 2, y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bachelor Party Group Frame 2 | (0, 192) | 256x96 | Supporting each other literally |
| Bachelor Party Stumble | (256, 192) | 256x96 | Shouting "are we spinning?" — no name (ucpf ruling; Deepseek's patch) |
| Tourist Grabbing Rail 1-2 | (512, 192) / (576, 192) | 64x96 each | Floor vibration response |
| Dizzy Tourist 1-2 | (640, 192) / (704, 192) | 64x96 each | Spiral-eyed wobble |

### Technical Notes:
- **Staging rule for Deepseek's question:** in ANY frame Hendrik shares with Tourist Grabbing Rail or Dizzy Tourist, Hendrik must be drawn dead vertical — his stability against everyone else's wobble is the location's best silent joke. Also: never stage him facing the millstone in a neutral frame (`millstone_watch` is the frame where he is most nearly happy).
- Apron must read as grimy canvas at 64x96, not cream linen; the chest tape must be visible or the joke is wasted (two art notes, no new frames)
- Max 3 visitor NPCs per floor (draw call budget)
- Visitor NPCs escalate in dishevelment by floor: composed at reception, rail-clutching upstairs

---

## 🏅 Sprite Sheet 8: Items, Effects & UI
**File:** `wobbly_windmill_items_ui.png`
**Dimensions:** 512x512 pixels
*(carried unchanged — icons, meters, effects; no banned wording)*

### Tasting & Rewards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Flight Glasses 1-5 | (0, 0) to (128, 0), 32px steps | 32x48 each | Landfill Lager → Windmill Grist, deepening color |
| Windmill Grist Bottle | (160, 0) | 48x64 | Consumable icon: +40 HP, -20% Navigation |
| Bottle Opener (Static) | (208, 0) | 48x48 | Miniature windmill, brushed copper, "Respect The Grain" |
| Opener Blade Spin 1-4 | (256, 0) / (304, 0) / (352, 0) / (400, 0) | 48x48 each | Blade arms actually rotate |
| Tour Stamp "Windmill Grist" | (448, 0) | 64x64 | Keychain stamp — 1 of 4 Shamsterdam breweries |
| Tasting Token | (384, 256) | 32x32 | Included with 25 SOVS tour |

### UI Panels & Effects: *(cells unchanged)*
Spin Meter (0,64), Selfie Timing Mini-Game UI (96,64), Tasting Flight Tracker (352,64), Yeast Slayer Title Badge (352,192), Navigation Debuff Icon (96,256), Bleary Status Icon (128,256), Liquid Ripple 1-2 (0,256)/(48,256), Spin Vignette Corner (160,256), Beer Foam Sparkle 1-3 (288,256)-(352,256), Camera Shutter Flash (0,304), Grain Dust Puff (64,304).

### Technical Notes:
- Room spin is shader-driven (CanvasLayer warp); Spin Vignette Corner is the only texture it needs
- Opener spin animation plays in inventory when item is inspected
---

## 🎬 Animation Specifications (carried; lighting wording fixed)

### Windmill Blade Rotation (Sheets 1, 3, 4):
- **Duration:** 8 seconds per revolution (continuous; frames crossfade at 0.5 FPS, node rotation interpolates between)
- **Frames:** 4 positions
- **Pattern:** Continuous loop, speed scales with "wind" variable
- **Trigger:** Constant while location loaded
- **Purpose:** The whole building's identity — and the source of the dizziness
- **Audio Sync:** Blade whoosh on each 90° position pass; the zip-tied guard rattles on every third pass
- **Performance Optimization:** Static blade shadows on older devices (profile-mandated)

### Millstone Grinding (Sheet 3):
- **Duration:** 2 seconds per cycle (4 frames at 2 FPS)
- **Frames:** 4
- **Pattern:** Continuous loop synced to blade speed
- **Trigger:** Constant on grinding floor
- **Purpose:** The windmill actually works; the floor actually vibrates
- **Audio Sync:** Grinding rumble loop locked to cycle; low-frequency emphasis + guard rattle every third pass
- **Performance Optimization:** Simplified grinding animation (2 frames) on older devices

### Floor Vibration (Sheets 3, 8):
- **Duration:** 0.3-second shake bursts every 2 seconds while grinding
- **Frames:** Overlay strip + 2-frame liquid ripple
- **Pattern:** Vibration overlay pulses; glasses ripple in sync
- **Trigger:** Grinding active (first floor); echoes faintly in tasting room
- **Purpose:** Tourists grab rails; beer ripples; history is felt
- **Audio Sync:** Rumble peak on each burst
- **Performance Optimization:** Overlay only, no ripple, on Low LOD

### Yeast Golem Rising (Sheet 5):
- **Duration:** 3 seconds (4 frames at ~1.3 FPS), single play
- **Frames:** 4 + 3 spawn dust swirls
- **Pattern:** Dust swirl 1-3 → Rising 1-4 → Idle loop, rising through the worn gap in the hazard-tape ring
- **Trigger:** Boss encounter start on grinding floor
- **Purpose:** "From the accumulated flour and forgotten yeast cultures, something RISES."
- **Audio Sync:** Reversed, slowed bread-baking sounds building to a boom on frame 4
- **Performance Optimization:** 2 dust swirls on Low LOD

### Golem Expansion (Sheet 6):
- **Duration:** 1.5 seconds per expansion (3 frames at 2 FPS), every 3 turns in Phase 2
- **Frames:** 3
- **Pattern:** Expand → hold larger silhouette; weakness window during frames 2-3
- **Trigger:** Phase 2 turn counter
- **Purpose:** Over-proofing readability — bigger, stronger, slower
- **Audio Sync:** Dough stretch squelch on each frame
- **Performance Optimization:** None needed

### Final Rise & Collapse (Sheet 6):
- **Duration:** Charge 4 seconds (2 game turns, 3 frames looping at 1 FPS); Collapse 2.5 seconds (4 frames at ~1.6 FPS), single play
- **Frames:** 3 + 4
- **Pattern:** Charge loop (interruptible by fire/alcohol) → Collapse 1-4 → bread loaf prop
- **Trigger:** Phase 3 script
- **Purpose:** Climax and punchline — the boss becomes bread
- **Audio Sync:** Rising oven-timer tick during charge; soft "poof" + oven ding on collapse frame 4
- **Performance Optimization:** None needed

### Tasting Room Spin (Sheets 4, 8):
- **Duration:** Continuous; intensity ramps with Spin Meter (0-5 beers) over the flight
- **Frames:** Shader-driven, vignette corner texture
- **Pattern:** Subtle wobble at beer 2 → definite rotation at beer 4 → full "why is the floor moving" at Windmill Grist
- **Trigger:** Each flight beer consumed
- **Purpose:** Each beer makes the spinning more noticeable; the building doesn't help
- **Audio Sync:** Room-spin audio effect layers in per beer
- **Performance Optimization:** Vignette-only (no warp shader) on Low LOD; fully disabled in reduced-motion mode

### Selfie Blade Timing (Sheet 4):
- **Duration:** 4-second blade sweep loop (4 frames at 1 FPS); shutter window 0.5 seconds on frame 2
- **Frames:** 4 + shutter flash
- **Pattern:** Sweep loop → player clicks → flash → result (Perfect/Unfortunate Windmill Shot)
- **Trigger:** Selfie Spot Marker interaction (post-boss)
- **Purpose:** Timing mini-game; wind factor option adds hair chaos overlay
- **Audio Sync:** Camera shutter on tap; wind howl constant at blade level
- **Performance Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements (carried; candle cell renamed)

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stairs/exit outlines | Sheet 8, (416, 256) | 32x32 x2 (x416, x448) | Bold-outline floor-transition markers for the circular, disorienting layout |
| Boss weakness flash | Sheet 8, (128, 304) | 64x64 | High-contrast burst marking fire/alcohol vulnerability window |
| Rail interaction highlight | Sheet 8, (192, 304) | 64x32 | Outline variant for the grab-rail during vibration |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static blade shadow | Sheet 3 (Window Blade Shadow 1) | 128x128 | Reduced-motion mode holds shadow frame 1 |
| Steady tea-light cups (was "Steady candle") | Sheet 4 (Tea-Light Cups 1) | 64x64 | Non-flickering variant — the cups stay OFF; the flicker belongs to the fluorescent tube |
| Spin effect disabled note | Sheet 8 (Spin Vignette Corner) | 128x128 | Reduced-motion replaces warp with static vignette + "Dizzy" status text |

### Visual Audio Cues: *(unchanged)*
Grinding rumble icon (256, 304), blade whoosh marker (288, 304), oven-ding defeat cue (320, 304), charge warning icon (352, 304).

### Colorblind Considerations: *(unchanged)*
- Flight beers differ by glass shape and fill level, not color alone; ABV numerals printed on flight board
- Boss weakness window uses brightness flash + icon, never a color-only tint
- Spin Meter uses needle position + numeric readout
- Click zones minimum 44px for tasting choices, selfie shutter, and gift shop interactions

---

## 🖥️ Performance & Assets (carried unchanged)

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import); chalkboard and signage need higher quality (readable text)
- **Fallback:** PNG high quality for boss sheets (phase silhouettes are gameplay-critical)

### Texture Atlases: *(unchanged)*
| Atlas | Contents | Max Size |
|-------|----------|----------|
| wobbly_windmill_environment | exterior, ground floor, grinding floor, tasting/blade | 2048x2048 |
| wobbly_windmill_boss | golem battle + phases | 2048x1024 |
| wobbly_windmill_characters_ui | NPC cast, items/effects/UI | 1024x1024 |

### LOD Levels: *(unchanged)*
High: full blade rotation, dust particles, spin shader, all visitor NPCs. Medium: reduced dust, 2-frame grinding, vignette-only spin, 2 visitor NPCs. Low: static blade shadows, no dust, no spin shader, staff NPCs only.

### Performance Targets: *(unchanged)*
60 FPS, max 18 draw calls, 42 MB memory footprint, 25 particles.

### Performance Notes: *(unchanged)*
Load floors as separate scenes; boss sheets load on grinding-floor entry, unload after victory; blade/millstone share one rotation driver script. Added prop cells fit inside existing sheet dimensions — no new files, no new draw calls beyond the existing prop budget.

---

## 🔧 Technical Integration Notes (carried; sign wording deferred to Aion)

### Godot Engine Integration: *(unchanged)*
All sprites designed for Godot 4.x, top-left origin. TileMap (floors), AnimatedSprite2D (golem, NPCs, mechanisms), CPUParticles2D (grain dust, flour), CanvasLayer + warp shader (room spin), Camera2D shake (floor vibration). Special systems: dual bottle-opener gate (Blarney Trap opener = tour access; Windmill opener = stamp access, earned via golem only, never sold), Spin Meter accumulator, brewmaster speech skip/Bravado check, selfie timing evaluator, boss phase state machine with fire/alcohol interrupt.

### Audio Sync Points: *(unchanged, one line added)*
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Blade rotation positions | Rhythmic whoosh | Each 90° pass |
| Zip-tied guard rattle | Metallic rattle | Every third gear pass |
| Millstone frames | Grinding rumble loop | Locked to 4-frame cycle |
| Golem rising | Reversed/slowed bread-baking build | Frames 1-4, boom on 4 |
| Collapse frame 4 | Soft poof + oven ding | On frame display |
| Flight glass raise | Pour + toast clink | On consume action |
| Selfie shutter | Camera click + wind howl bed | On player tap |
| Turnstile entry | Click + counter beep | On entry (ambient until [QUESTION FOR AUTHOR] is ruled) |
| Hendrik lecture frames | Reverent baritone VO bed | Loop during endurance challenge |

### Quest Integration: *(unchanged)*
Shamsterdam Brewery Tour (1 of 4, any order) — tour stamp, opener sprites, flight tracker. "Canal Courage" passive — flight tracker completion. Yeast Golem boss — both boss sheets, arena tiles, Yeast Slayer badge. Couchsurf — Beer Blogger sprites. Selfie Spot Challenge — blade sweep frames, shutter flash, hair chaos.

### Cross-Location Dependencies: *(unchanged)*
Bottoms Down (shared stamp/keychain UI style), The Tolerance Hostel (Windmill Grist bottle as conversation prop), Starbaked (dialogue reference), Train Station central Shamsterdam (8 SOVS round-trip transition).

---

## 🎨 Art Direction Summary (rewritten loud/seedy)

### Visual Aesthetic:
- **Primary Theme:** "350 years of stubborn wood that still genuinely works, wrapped in the loudest tourist machine in Euromemeia — and the machine is winning"
- **Color Mood:** Grain gold and cold copper under caged cool-white bulbs and grey daylight — the only warm hue is the amber neon over the till and the beer itself. The light never flatters; it surveils
- **Lighting:** Grey daylight through small windows, buzzing caged utility bulbs, one hard spotlight on the vats, one flickering fluorescent over the chalkboard, amber neon over the merch. The light sways with the spin because the building spins
- **Texture:** Grain dust on everything including the visitors; wood worn smooth only where tourists grab it; merch paint still tacky; zip ties on the gear guard; hazard tape with a worn gap nobody re-taped

### Environmental Storytelling:
- The gift shop bookends the tour (entry AND exit) — the funnel is the architecture
- "History" panels that are 95% beer marketing tell you what the past is for here
- Open grain bins and a taped-over card reader read as uninsurable on purpose
- The Survivor Pack display admits everything the tour pretends not to know
- The turnstile counts tourists and has never counted Hendrik — he goes around it, through the staff gap, four times a day

### Character Integration Notes:
- Hendrik dominates rooms — position him centrally, dead vertical, lecture frames large in the composition
- Tessa orbits the tour group edges, always between a tourist and a railing gap
- Bram stands at the till, which is also the exit — he is unavoidable twice
- Visitor NPCs escalate in dishevelment by floor: composed at reception, rail-clutching on the grinding floor, wobbling upstairs
- The golem must stay comedic-threatening: dough physics, never horror

---

## 🎯 Social Media Viral Potential (rewritten)

### Screenshot-Worthy Moments:
1. **Fighting Bread** — the Yeast Golem mid-expansion rising through the worn gap in the hazard tape; "I fought bread" energy
2. **The Perfect Windmill Shot** — selfie mini-game success (and its face-blocked failure twin)
3. **The Spin Meter Maxed** — full tasting flight with the room warping
4. **Collapse to Loaf** — boss defeat becoming a harmless bread prop
5. **The Turnstile High Score** — the counter on the till ticking up over a bro's head
6. **"I SURVIVED THE SPIN" Rack** — the gift shop admitting the business model

### Quote Potential:
- "Respect The Grain. Fear The Spin."
- "The first beer teaches you humility. The second teaches you character. The third teaches you why we have railings."
- "It's made of BREAD. How is BREAD this AGGRESSIVE?"
- "I fought bread. I have footage of fighting BREAD. This trip is INSANE."
- "The spinning is intentional. The dizziness is not our fault."
- "NO REFUNDS. THE SPINNING IS ON THE WEBSITE."

---

## 📋 Required PNG Files (8 Total) — unchanged

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | wobbly_windmill_brewery_exterior.png | 1024x768 |
| 2 | wobbly_windmill_ground_floor.png | 1024x512 |
| 3 | wobbly_windmill_grinding_floor.png | 1024x1024 |
| 4 | wobbly_windmill_tasting_blade_level.png | 1024x512 |
| 5 | yeast_golem_battle.png | 1024x1024 |
| 6 | yeast_golem_phases.png | 1024x1024 |
| 7 | npc_wobbly_windmill_cast.png | 1024x384 |
| 8 | wobbly_windmill_items_ui.png | 512x512 |

**Total Estimated Memory:** ~22 MB raw RGBA texture data; ~42 MB maximum total footprint (location performance budget)

---

## 📦 File Delivery Checklist (carried)

### Quality Requirements:
Format PNG-24 with alpha, sRGB, 72 DPI, lossless, snake_case, layers preserved in master. Primary: individual PNGs; backup: master PSD; documentation: animation timing sheet + rotation sync guide + boss phase chart.

---

## ✅ Final Delivery Validation (rewritten to the loud/seedy bar)

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly; hues per the palette table; NO candle-warm or golden-hour light anywhere (vuqj-q3)
- [ ] Key gags read clearly at 231 px thumbnail: backlit sign wider than the door, queue rope + turnstile on the path, hazard tape on every visible surface
- [ ] Seedy gags read clearly: Survivor Pack most-stocked shelf, always-empty motion-bag dispenser, "DAYS SINCE LAST GOLEM: 0", spill plaque, zip-tied guard, taped-over card reader, overflowing cup bin, empty earplug slot, hat bin with the toupee [PROPOSED]
- [ ] Machinery sign is English header + pictograms (hand with red cross, gear, skull) — never five languages (vuqj-q4)
- [ ] Hendrik drawn dead vertical next to wobble sprites; apron grimy; chest tape visible at 64x96
- [ ] Accessibility visual alternatives included for all audio cues (rumble, whoosh, charge warning, oven ding, turnstile beep)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets: experience tourism processed, queued, counted, spun and upsold — the house works, the machine is real, the tourist pays
- [ ] No real nationality words, no "Europe", no banned painter-bait words anywhere in descriptions
- [ ] Hidden areas/interactions have discoverable visual cues (blade level unlock, worn tape gap)
- [ ] Performance optimized (CPU particles, atlas limits, per-floor scene loading, added cells within existing sheet bounds)
- [ ] Click zone sizing considered (44px minimum)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status (rewritten)

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city/place/nationality names) | ✅ | Shamsterdam countryside only; patrons "Local" / "Big-City Paper"; no "Europe" — Euromemeia |
| Loud tourist-trap read at thumbnail | ✅ | Backlit sign wider than door, queue rope, turnstile, hazard tape, merch in every sightline |
| Seedy & specific | ✅ | ≥5 modern seedy props per scene (turnstile, CCTV, taped reader, empty dispensers, vending machine, zip ties, plaque, grime) |
| Old, never charming | ✅ | Banned-word sweep clean; age reads as grime, damage, stubbornness |
| Cultural Specificity | ✅ | Windmill experience-tourism + craft beer sermon culture |
| Satirical Targets Appropriate | ✅ | Experience-tourist exploitation and brewery pretension; the working mill is respected, the trap is mocked |
| Seedy Underbelly Present | ✅ | 40 SOVS flights in a disorientation machine, liability placards, gift shop selling the cure at the till |
| Gameplay Value Established | ✅ | Boss, Spin Meter flight, speech endurance, selfie mini-game, opener gating — all ruled mechanics untouched |
| Technical Feasibility | ✅ | Per-floor scenes, shared rotation driver, shader spin, CPU particles documented; added cells within existing sheets |
| Performance Budget | ✅ | 60 FPS, 18 draw calls, 42 MB |
| Accessibility Features | ✅ | Visual mirrors for audio cues, reduced-motion spin disable, 44px zones, tea-light cells stay off |
| No Crypto Elements | ✅ | Pure traditional brewing |
| Social Media Integration | ✅ | 6 screenshot moments + quote bank |

---

## Notes for reviewers

- **Kimi:** every descriptive cell above is matched to your `drafts/kimi_windmill_location.md` — exterior (turnstile, queue, vending machine, cutout, cup bin), ground floor (neon GRAIN, CCTV, sanitizer pump, sticker pole, no-refunds placard, Survivor Pack), grinding floor (zip-tied guard, golem chalkboard, flour-furred extinguisher, dead earplug dispenser), tasting room (spill plaque, unlit tea lights, motion-bag dispenser, zip-tied locker, squeegee chain), blade level (photo rig OUT OF ORDER, empty lanyard hook, pictogram placard, hat bin). The thumbnail line uses Deepseek's 231 px revision of your sentence — confirm it matches your Visual Design edit at integration.
- **Deepseek:** Sheet 7 staging notes answer your cast-sheet question — Hendrik dead vertical beside the wobble sprites, apron grimy, tape visible; `millstone_watch` never staged neutral. The Bachelor Party stumble frame now shouts "are we spinning?" with no name, matching your Johannes patch.
- **Aion:** the three sign cells (main backlit sign, machinery sign per vuqj-q4, queue standing sign) are marked [AION SIGN SHEET] with placeholder text only — your `drafts/aion_windmill_signs.md` wording drops straight in; cell positions and sizes are reserved.
- **Open flags carried, not decided:** hat-bin toupee [PROPOSED]; turnstile counter tick and golem-chalkboard reset remain [QUESTION FOR AUTHOR] per Kimi's interactables table; `eva_tour_guide.png` filename vs. "Tessa" mismatch noted only (filenames ruled).
