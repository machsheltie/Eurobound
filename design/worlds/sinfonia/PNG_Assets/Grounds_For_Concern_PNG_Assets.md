# Grounds For Concern - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Grounds For Concern — the Kaffeehaus Row espresso stand where the extraction is timed to the millisecond, the barista assesses you before you speak, and the tremor in your hands is not a side effect but a receipt. It is a Speed-buff vendor with a Luck-debuff price tag, a four-tier caffeine tolerance ladder, and a man named Ferdinand who has been genuinely broken by people who ask for sugar.

**Location ID:** `sinfonia_kaffeehausrow_grounds_concern_01`
**Theme:** Third-wave espresso pretension — Viennese coffeehouse reverence compressed into a stand with no large cups and no mercy
**Zone:** Kaffeehaus Row, Intellectual Café District (mobile — prime locations)
**Hours:** 6 AM - 10 PM (caffeine has limits, apparently)
**Primary Function:** Street vendor / espresso shop — Speed buffs with Luck debuffs, Caffeine Tolerance progression, status-effect system, three selfie variants

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Espresso Brown | #3C280D | Machine shadows, cart timber, coffee body, Ferdinand's apron shading |
| Brass Gold | #B5A642 | La Marzocco casing, counter rail, taps, obsessive polish highlights |
| Steam White | #F5F5F5 | Steam, morning light, pristine apron, cup ceramic |
| Crema Tan | #C4A35A | Crema layer, chalkboard chalk warmth, bean sacks |
| Kaffeehaus Stucco | #E8DCC4 | Façade walls, backdrop buildings (derived neutral for the street band) |
| Judgment Shadow | #2A2118 | Signage lettering, Ferdinand's eye shadow, high-contrast outlines |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/grounds_for_concern/
├── environment/
│   ├── grounds_concern_tileset.png
│   └── grounds_concern_machine.png
├── npcs/
│   ├── ferdinand_focused.png
│   └── grounds_concern_npcs.png
├── objects/
│   └── grounds_concern_drinks.png
├── effects/
│   └── grounds_concern_effects.png
└── ui/
    └── grounds_concern_ui.png
```

---

## ☕ Sprite Sheet 1: Kaffeehaus Row Street & Stand Tileset
**File:** `grounds_concern_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #E8DCC4 (Stucco), #3C280D (Espresso Brown), #B5A642 (Brass), #C4A35A (Crema Tan)

### Street & Ground Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kaffeehaus Cobble | (0, 0) | 32x32 | Base district paving |
| Cobble Coffee-Stained | (32, 0) | 32x32 | Years of knock-box spillage |
| Kerb Edge | (64, 0) | 32x32 | Street boundary |
| Gutter With Grounds | (96, 0) | 32x32 | Spent puck sediment |
| Terrace Paving | (128, 0) | 32x32 | Café seating apron |
| Stand Platform Board | (160, 0) | 32x32 | Ferdinand's raised working deck |
| Steam Grate | (192, 0) | 32x32 | Street vent, ambient wisp anchor |
| Queue Floor Decal | (224, 0) | 32x32 | Where you wait to be assessed |

### Wall & Façade (32x64 unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kaffeehaus Row Stucco | (0, 32) | 32x64 | Standard façade section |
| Stucco Gilt Line | (32, 32) | 32x64 | Imperial-era trim survivor |
| Shuttered Window | (64, 32) | 32x64 | Upper-floor apartment |
| Café Door Frame | (96, 32) | 32x64 | Neighbouring coffeehouse entry |
| Notice-Board Wall | (128, 32) | 32x64 | Concert bills, pasted over |
| Downpipe | (160, 32) | 16x64 | Cast-iron detail |
| Wall Corner Return | (176, 32) | 16x64 | Façade turn piece |

### Awnings, Lamps & Street Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Striped Awning Segment | (0, 96) | 64x32 | Tileable canopy |
| Awning End Cap | (64, 96) | 32x32 | Canopy terminator |
| Awning Scallop Fringe | (96, 96) | 64x16 | Lower trim strip |
| Street Lamp | (160, 96) | 24x96 | Morning-off, evening-on |
| A-Frame Chalkboard | (184, 96) | 48x64 | Bean origins, hand-lettered |
| Bean-Sack Stack | (232, 96) | 48x48 | Single-origin hessian |
| Bentwood Chair | (280, 96) | 24x40 | Kaffeehaus classic |
| Café Table Set | (304, 96) | 64x48 | Terrace two-top |
| Newspaper Rack | (368, 96) | 32x48 | Papers on wooden spines |
| Bicycle Leaned | (400, 96) | 48x40 | Regular's transport |
| Pigeon Cluster | (448, 96) | 32x24 | Uninterested in espresso |
| Tram-Stop Post | (480, 96) | 16x80 | District marker |

### Café-District Set Dressing (right block):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Distant Café Awning Row | (512, 0) | 256x64 | Rival establishments, all inferior |
| Kaffeehaus Row Street Sign | (768, 0) | 96x32 | Zone identifier |
| Hanging Café Lantern | (864, 0) | 32x48 | Evening warmth |
| Planter Box With Bay Tree | (896, 0) | 48x64 | Terrace dressing |
| Sandwich-Board Blank | (944, 0) | 48x64 | Reusable board for other vendors |

### Stand Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stand Counter Front | (0, 192) | 128x64 | Compact, efficient, no clutter |
| Stand Counter Side Panel | (128, 192) | 48x64 | Return face |
| Counter Brass Rail | (176, 192) | 96x16 | Polished daily, obsessively |
| Cup Shelf Unit | (272, 192) | 48x48 | Demitasse only |
| Under-Counter Bin | (320, 192) | 32x32 | Discreet waste |
| Knock Box | (352, 192) | 24x24 | Spent pucks, stacked neatly |
| Water Jug | (376, 192) | 16x24 | Served unasked, always |
| Tip Saucer | (392, 192) | 24x16 | Rarely acknowledged |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign "Grounds For Concern — Ristretto, Espresso, Doppio" | (0, 256) | 256x48 | Primary fascia |
| Secondary Sign "We Do Not Serve 'Regular Coffee.' Don't Ask." | (0, 304) | 256x32 | Non-negotiable |
| Tertiary Sign "Yes, You Will Shake. This Is Correct." | (0, 336) | 256x32 | Shaking is a feature |
| Bean-Origin Chalkboard | (256, 256) | 128x96 | Altitudes, varietals, processing |
| Tiny-Cup Display Rack | (384, 256) | 96x64 | Minimalist, deliberate |
| "No Large Cups" Placard | (384, 320) | 96x24 | Absence enforced in writing |
| Hours Plate "6 AM – 10 PM" | (480, 256) | 96x24 | Caffeine has limits |
| Price Card Strip | (480, 280) | 96x32 | 3 – 25 Sovs, visible, honest |
| Extraction-Timer Placard "23 Seconds" | (480, 312) | 96x24 | The number that matters |

### Backdrop / Parallax Layers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kaffeehaus Row Backdrop Far | (0, 384) | 512x128 | Slow parallax building line |
| Kaffeehaus Row Backdrop Near | (512, 384) | 384x128 | Fast parallax terrace layer |
| Morning Light Gradient Overlay | (896, 384) | 128x128 | Additive sunrise wash |

### Technical Notes:
- Brass on the counter rail and machine casing must read as *maintained*, not merely gold — a specular streak in the same place every frame communicates the polishing ritual
- Region x496–1024, y96–192 and x416–1024, y192–256 are reserved padding; do not repack without updating this table
- The three signs are a stacked block by design: they must be legible as a unit in a single 256px-wide screenshot crop
- Backdrop layers scroll at 0.25x (far) and 0.6x (near); the gradient overlay does not scroll

---

## ⚙️ Sprite Sheet 2: The Machine & Counter Craft
**File:** `grounds_concern_machine.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #B5A642 (Brass Gold), #F5F5F5 (Steam White), #3C280D (Espresso Brown), #C4A35A (Crema Tan)

### The La Marzocco (Polished Obsessively):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Espresso Machine Body | (0, 0) | 128x96 | Twin-group brass, mirror finish |
| Machine Group Head Left | (128, 0) | 32x32 | Primary extraction point |
| Machine Group Head Right | (160, 0) | 32x32 | Secondary, used for doubles |
| Portafilter Docked | (128, 32) | 32x32 | Locked and running |
| Portafilter Loose | (160, 32) | 32x32 | Held, being tamped |
| Steam Wand Idle | (192, 0) | 16x48 | Wiped after every use |
| Steam Wand Purging | (208, 0) | 16x48 | Pre-steam blast |
| Pressure Gauge | (224, 0) | 24x24 | 9 bar, non-negotiable |
| Drip Tray | (224, 24) | 48x16 | Emptied more than necessary |
| Machine Polish Highlight Overlay | (224, 40) | 48x24 | Additive specular pass |

### Grinder & Prep:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Doser Grinder | (272, 0) | 48x80 | Burr set, calibrated hourly |
| Grinder Hopper Beans | (320, 0) | 32x40 | Single origin, dated |
| Tamper Upright | (352, 0) | 16x32 | Weighted, personal |
| Tamping Mat | (368, 0) | 32x16 | Corner-worn |
| Bean Scoop | (400, 0) | 24x16 | Brass, of course |
| Cloth Folded | (424, 0) | 24x16 | Surgical |
| Scale With Timer | (352, 32) | 32x24 | The 23-second authority |
| Knock-Box Insert | (384, 32) | 32x24 | Removable liner |
| Milk Pitcher | (416, 32) | 24x32 | Used reluctantly |
| Cleaning Brush | (440, 32) | 24x24 | Between every shot |

### Counter Display & Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tiny Cup Pyramid | (0, 96) | 96x64 | Warmed, stacked, small |
| Demitasse Row | (96, 96) | 96x32 | Ready line |
| Saucer Stack | (96, 128) | 48x32 | Matched set |
| Sugar Bowl (Reluctant) | (144, 128) | 32x24 | Present but resented |
| Spoon Rest | (176, 128) | 32x16 | Aligned |
| Chalkboard Bean Origins | (192, 96) | 96x64 | Altitude and varietal notes |
| Composer-Free Wall Clock | (288, 96) | 32x32 | Time matters; music does not |
| Water Glass Row | (336, 96) | 64x32 | Served with every espresso |
| Extraction Log Book | (288, 128) | 48x32 | Every shot, recorded |
| Ferdinand's Reserve Tin | (336, 128) | 32x32 | One per day, no exceptions |
| Menu Board Small | (400, 96) | 96x64 | Six drinks, three items |

### Cups & Vessels (32x32 unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ristretto Cup Empty | (0, 160) | 32x32 | The respected vessel |
| Espresso Cup Empty | (32, 160) | 32x32 | Classic |
| Doppio Cup Empty | (64, 160) | 32x32 | Understood |
| Cappuccino Cup Empty | (96, 160) | 32x32 | Sighed over |
| Flat White Cup Empty | (128, 160) | 32x32 | Respectful nod (Australian invention) |
| Americano Glass, Tolerated | (160, 160) | 32x32 | Barely |
| Iced Cup ("It Should Not Be Done") | (192, 160) | 32x32 | Exists under protest |
| Paper Cup, Never Used, Dusty | (224, 160) | 32x32 | Environmental storytelling |
| Counter Overlay: Steam Condensation | (256, 160) | 64x32 | Multiply-blend film |
| Brass Reflection Strip | (320, 160) | 96x16 | Additive counter sheen |
| Counter Shadow Pool | (320, 176) | 96x16 | Contact shadow band |

### Extraction Sequence (32x48 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Extraction Frame 1 — First Drops | (0, 192) | 32x48 | Dark, slow, correct |
| Extraction Frame 2 — Honey Stream | (32, 192) | 32x48 | Mouse-tail forming |
| Extraction Frame 3 — Crema Blonding | (64, 192) | 32x48 | The warning colour |
| Extraction Frame 4 — Cut At 23s | (96, 192) | 32x48 | Stopped exactly on time |
| Milk Steam Frame A | (128, 192) | 32x48 | Vortex forming |
| Milk Steam Frame B | (160, 192) | 32x48 | Microfoam achieved |
| Pour Fail (Channeling) | (192, 192) | 32x48 | Discarded immediately, no charge |
| Ferdinand's Reserve Pour | (224, 192) | 32x48 | Ceremonial, once per day |

### Technical Notes:
- The machine body is the only asset on this sheet permitted a full specular ramp; everything else uses two-tone brass to stay inside the draw-call budget
- Extraction frames 1–4 must align on the cup rim so the sequence plays without sub-pixel jitter
- Channeling frame is visually distinct at 32px (split stream, pale) because it is the only way the player learns Ferdinand's standard without dialogue

---

## 🧑‍🍳 Sprite Sheet 3: Ferdinand the Focused
**File:** `ferdinand_focused.png`
**Dimensions:** 384x288 pixels
**Color Palette:** #F5F5F5 (Apron White), #3C280D (Espresso Brown), #2A2118 (Judgment Shadow), #B5A642 (Brass reflections)

### Craft States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Precision Idle | (0, 0) | 48x96 | Cloth in hand, mustache immaculate |
| Pre-Assessment Stare | (48, 0) | 48x96 | Silent evaluation of an approaching customer |
| Already Preparing | (96, 0) | 48x96 | Your drink began before you spoke |
| Tamping | (144, 0) | 48x96 | Exact pressure, exact angle |
| Portafilter Lock | (192, 0) | 48x96 | The satisfying quarter-turn |
| Watching Extraction | (240, 0) | 48x96 | Eyes on the timer, not on you |
| Cut The Shot | (288, 0) | 48x96 | Stopped at 23 seconds |
| Serving, Two Hands | (336, 0) | 48x96 | The handover is part of the craft |

### Reaction States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Approving Nod | (0, 96) | 48x96 | Ristretto ordered correctly |
| Rare Smile | (48, 96) | 48x96 | Transcendent tier only; blink and miss it |
| Slight Sigh | (96, 96) | 48x96 | Cappuccino |
| Visible Disappointment | (144, 96) | 48x96 | Latte |
| Respectful Nod | (192, 96) | 48x96 | Flat white — he concedes the Australians |
| Eyes Closed Briefly | (240, 96) | 48x96 | "With sugar" |
| Long Pause | (288, 96) | 48x96 | "Iced" — "It will be done. It should not be done." |
| Genuine Confusion | (336, 96) | 48x96 | "Decaf" — "Why are you HERE?" |

### Crisis & Extended States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Existential Crisis A | (0, 192) | 48x96 | "Regular coffee" — portafilter set down |
| Existential Crisis B | (48, 192) | 48x96 | The five-minute lecture begins |
| Directing You Elsewhere | (96, 192) | 48x96 | "There is a place three streets over." |
| Scientific Interest | (144, 192) | 48x96 | Watching a Quadruple take hold |
| Rush-Order Composure | (192, 192) | 48x96 | Queue deep, tempo unchanged |
| Extraction Sermon | (240, 192) | 48x96 | Genuine passion about beans |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mustache Detail | (288, 192) | 32x16 | Perfectly groomed, close-up |
| Pristine Apron Detail | (288, 208) | 32x40 | Cleaner than surgical scrubs |
| Steady Hands Close-Up | (288, 248) | 48x40 | His hands never shake. Yours will. |
| Portafilter In Hand | (320, 192) | 32x32 | Prop overlay |
| Timer Held Up | (352, 192) | 32x32 | "The extraction was 23 seconds." |
| Cloth Wipe Detail | (320, 224) | 32x24 | Between every single shot |
| Ferdinand's Reserve Key | (352, 224) | 32x24 | The tin is locked |
| Apron Crease Detail | (336, 248) | 48x40 | Deliberate, pressed |

### Animation Timing:
- Craft loop (idle → wipe → idle): 2fps, loop
- Tamp → lock → watch → cut: 4fps, single play, hold on Cut frame for the timer callout
- Reaction states: single-frame holds, 0.8s minimum before returning to idle
- Rare Smile: 1 frame, 0.4s, no ease — it must feel like it was almost not there

### Character Notes:
- Ferdinand's disappointment is never contempt; he is grieving a coffee that could have been better
- His hands are the only steady thing in the scene once the player is buffed — never add tremor to Ferdinand
- The mustache is a silhouette identifier at 48px; keep the profile shape consistent across every frame

---

## 👥 Sprite Sheet 4: The Regulars, The Queue & The Bros
**File:** `grounds_concern_npcs.png`
**Dimensions:** 384x192 pixels
**Color Palette:** Kaffeehaus earth tones, #F5F5F5 (highlights), #C4A35A (crema accents)

### Regulars & Queue (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shaky Writer Idle | (0, 0) | 48x96 | "Fourth one today." |
| Shaky Writer Tremor | (48, 0) | 48x96 | Notebook visibly vibrating |
| Vibrating Musician | (96, 0) | 48x96 | Bow hand blurred at the wrist |
| Steady Master Approach | (144, 0) | 48x96 | No words needed |
| Steady Master Nod-And-Go | (192, 0) | 48x96 | Receives drink, nods, leaves |
| Queue Tourist Confused | (240, 0) | 48x96 | Reading the "no regular coffee" sign |
| Queue Tourist Retreating | (288, 0) | 48x96 | Redirected three streets over |
| Regular Being Remembered | (336, 0) | 48x96 | Ferdinand starts the order on sight |

### The Bros & The Intervention (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner Ordering | (0, 96) | 48x96 | "I could use a pick-me-up." |
| Lord Pilsner Vibrating | (48, 96) | 48x96 | "Is the ground moving or is that me?" |
| Chadwick Caramel Request | (96, 96) | 48x96 | Large iced latte with caramel |
| Chadwick Seeing Sounds | (144, 96) | 48x96 | Post-Quadruple |
| Bradley Ristretto Order | (192, 96) | 48x96 | Single origin, no sugar |
| Bradley Calm Sip | (240, 96) | 48x96 | Unaffected, insufferable |
| Over-Caffeinated NPC In Distress | (288, 96) | 48x96 | "The Intervention" quest target |
| Intervention Administered | (336, 96) | 48x96 | Decaf accepted; shame present |

### Character Notes:
- The Steady Master never speaks and never trembles — he is the visual proof that tolerance is achievable
- Tremor NPCs use the same base sprite as their calm counterparts with the shake applied as an effects-sheet overlay, not baked frames
- Chadwick's caramel request pose must read as innocent; the joke is Ferdinand's response, not Chadwick

---

## ☕ Sprite Sheet 5: Drinks, Items & Status Icons
**File:** `grounds_concern_drinks.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #3C280D (Coffee), #C4A35A (Crema), #F5F5F5 (Milk/Ceramic), #B5A642 (Brass accents)

### Core Drinks (32x48 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ristretto | (0, 0) | 32x48 | 3 Sovs, +5% Speed / -3% Luck — the respected order |
| Espresso | (32, 0) | 32x48 | 4 Sovs, +8% Speed / -5% Luck |
| Doppio | (64, 0) | 32x48 | 6 Sovs, +15% Speed / -10% Luck |
| Triplo | (96, 0) | 32x48 | 8 Sovs, +25% Speed / -15% Luck, Shaky |
| The Quadruple | (128, 0) | 32x48 | 12 Sovs, +40% Speed / -25% Luck, Shaky, Heart Racing |
| Americano | (160, 0) | 32x48 | Tolerated |
| Ferdinand's Reserve | (192, 0) | 32x48 | 15 Sovs, +20% Speed, no side effects, 1/day |
| The Intervention | (224, 0) | 32x48 | 3 Sovs, removes all caffeine effects |

### Milk Drinks & Supplies:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cappuccino | (0, 48) | 32x48 | 5 Sovs — slight sigh |
| Latte | (32, 48) | 32x48 | 5 Sovs — visible disappointment |
| Flat White | (64, 48) | 32x48 | 6 Sovs — respectful nod |
| Bean Bag (10 Shots) | (96, 48) | 48x48 | 25 Sovs, portable supply |
| Bean Scoop Item | (144, 48) | 32x32 | Inventory prop |
| Sugar Sachet (Forbidden) | (176, 48) | 24x24 | +1 Sov processing fee |
| Milk Jug Item | (200, 48) | 24x32 | Carried apologetically |
| Receipt With 1 Sov Processing Fee | (224, 48) | 32x32 | Itemised judgment |

### Status & Buff Icons (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Speed Buff Icon | (0, 96) | 32x32 | Forward chevron, crema-toned |
| Luck Debuff Icon | (32, 96) | 32x32 | Cracked clover, jagged edge |
| Shaky Status | (64, 96) | 32x32 | Doubled hand outline |
| Heart Racing | (96, 96) | 32x32 | Pulse waveform |
| Over-Caffeinated | (128, 96) | 32x32 | Triple-stacked cup, all borders jagged |
| Caffeine Tolerance Badge | (160, 96) | 32x32 | Current tier stamp |
| Secret-Menu Token | (192, 96) | 32x32 | Transcendent unlock |
| Ferdinand's Approval Marker | (224, 96) | 32x32 | The rarest icon in Sinfonia |

### Tolerance Tier Badges:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Novice Badge | (0, 128) | 48x48 | 0 Sovs — full negative effects |
| Regular Badge | (48, 128) | 48x48 | 50 Sovs — -25% negatives |
| Aficionado Badge | (96, 128) | 48x48 | 100 Sovs — -40% negatives |
| Transcendent Badge | (144, 128) | 48x48 | 200 Sovs — -50%, secret menu |
| Achievement Rosette Blank | (192, 128) | 64x48 | Shared award frame |

### Selfie Props & Cup States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tiny Cup Held (Confused Scale) | (0, 176) | 48x48 | Standard photo prop |
| Empty Cup Cluster | (48, 176) | 64x48 | "The Vibration" evidence |
| Cup Half Drunk | (112, 176) | 32x48 | Mid-consumption state |
| Cup With Perfect Crema | (144, 176) | 32x48 | Ferdinand-approved surface |
| Spilled Espresso Decal | (176, 176) | 48x24 | Tremor consequence |
| Crema Ring Stain | (176, 200) | 48x24 | Counter residue |
| Napkin With Extraction Notes | (224, 176) | 32x48 | He wrote the time down for you |

### Selfie Caption Plates:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Caption "Authentic Experience" | (0, 224) | 96x32 | Standard photo |
| Caption "No Regrets (Many Regrets)" | (96, 224) | 96x32 | Requires Over-Caffeinated |
| Caption "He Smiled. ONCE." | (192, 224) | 64x32 | Requires Transcendent tolerance |

### Technical Notes:
- Drink silhouettes must scale by shot count — a player should be able to count the caffeine at 32px without reading a label
- The Intervention shares the Ristretto silhouette deliberately; only the colour (pale) differs, because the joke is that it looks like a real order
- Status icons are shape-differentiated first, colour second (see Accessibility)

---

## 💨 Sprite Sheet 6: Steam, Tremor & Comedy Stings
**File:** `grounds_concern_effects.png`
**Dimensions:** 256x192 pixels
**Color Palette:** #F5F5F5 (Steam), #C4A35A (Crema), #B5A642 (Brass glint), #3C280D (Coffee)

### Steam:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steam Plume Frame A | (0, 0) | 48x64 | Wand plume, rising |
| Steam Plume Frame B | (48, 0) | 48x64 | Mid-curl |
| Steam Plume Frame C | (96, 0) | 48x64 | Dissipating |
| Wand Purge Burst | (144, 0) | 32x48 | Sharp, brief |
| Cup Wisp A | (176, 0) | 24x32 | Demitasse thread |
| Cup Wisp B | (200, 0) | 24x32 | Frame B |
| Cup Wisp C | (224, 0) | 24x32 | Frame C |
| Sunlit Steam Shaft | (176, 32) | 80x32 | Morning light catching vapour |

### Coffee Physics & Ambience:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Extraction Drip A | (0, 64) | 16x32 | First drop |
| Extraction Drip B | (16, 64) | 16x32 | Stream forming |
| Crema Bloom 1 | (32, 64) | 24x24 | Surface forming |
| Crema Bloom 2 | (56, 64) | 24x24 | Thickening |
| Crema Bloom 3 | (80, 64) | 24x24 | Perfect, hazelnut |
| Milk Micro-Foam Swirl | (104, 64) | 32x32 | Reluctant latte art |
| Grounds Puff (Grinder) | (136, 64) | 32x24 | Dose burst |
| Brass Glint | (168, 64) | 24x24 | Polish payoff sparkle |
| Dust Mote Cluster | (192, 64) | 32x32 | Morning air |
| Morning Light Beam | (224, 64) | 32x32 | Additive shaft segment |

### Status Visuals:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tremor Shake Overlay A | (0, 96) | 48x48 | Character ghost offset, frame A |
| Tremor Shake Overlay B | (48, 96) | 48x48 | Frame B |
| Heart Pulse Ring 1 | (96, 96) | 32x32 | Screen-edge pulse, inner |
| Heart Pulse Ring 2 | (128, 96) | 32x32 | Outer |
| Screen Vignette Pulse | (160, 96) | 96x48 | Subtle Heart Racing overlay |

### Comedy Stings & Audio Glyphs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Speed Lines Overlay | (0, 144) | 96x48 | Buffed movement streak |
| Judgment Glint (Ferdinand's Eyes) | (96, 144) | 32x24 | The assessment lands |
| Sigh Puff Glyph | (128, 144) | 24x24 | Visual for the milk-drink sigh |
| Approval Sparkle | (152, 144) | 24x24 | Visual for the nod |
| Existential Crack Glyph | (176, 144) | 32x24 | "Regular coffee" hairline fracture |
| Discordant Sting Glyph | (208, 144) | 24x24 | Wrong-order audio marker |
| Vibration Motion Ghost | (232, 144) | 24x48 | Over-Caffeinated silhouette trail |
| Timer Ping Ring | (96, 168) | 32x24 | 23-second chime visual |
| Grinder Whir Glyph | (128, 168) | 48x24 | Grind audio marker |
| Steam Hiss Glyph | (176, 168) | 56x24 | Wand audio marker |

### Technical Notes:
- All particles are CPUParticles2D — the location's 10-draw-call ceiling does not permit GPU particle nodes
- Tremor overlays are applied to *player and NPC* sprites at runtime and are never baked into character sheets
- Steam plume and cup wisp loops run independently at different rates (3fps and 2fps) so the scene never pulses in unison

---

## 🖥️ Sprite Sheet 7: Order Interface & Tolerance HUD
**File:** `grounds_concern_ui.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #3C280D (Panel), #B5A642 (Brass frame), #F5F5F5 (Text field), #C4A35A (Highlight)

### Order Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Order Panel Frame | (0, 0) | 160x96 | Menu + Ferdinand reaction panel |
| Drink List Row Blank | (160, 0) | 96x24 | Unselected menu row |
| Drink Row Highlighted | (160, 24) | 96x24 | Selected state |
| Price Chip | (160, 48) | 48x24 | Price lettered as `N SOVS` — **the word is the symbol; no currency mark exists.** ⚠️ 48x24 is tight for numeral + `SOVS`: set the word at half-height under the figure, or widen the chip to 72x24. |
| Effect Chip Speed | (208, 48) | 48x24 | Buff preview |
| Effect Chip Luck-Debuff | (160, 72) | 48x24 | Cost preview |
| Ferdinand Reaction Portrait Slot | (208, 72) | 48x24 | Live expression window |

### Response Chips & Reaction:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Response Chip Approved (smooth border) | (0, 96) | 96x24 | Ristretto / "strongest thing you have" |
| Response Chip Tolerated (double border) | (96, 96) | 96x24 | Milk drinks, Americano |
| Response Chip Crisis (jagged border) | (0, 120) | 96x24 | "Regular coffee" / decaf |
| Reaction Meter Bar | (96, 120) | 96x24 | Ferdinand's running opinion of you |
| Extraction Timer Dial | (192, 96) | 64x48 | 23-second countdown ring |

### Status HUD:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Speed Buff Slot | (0, 144) | 32x32 | Active buff frame |
| Luck Debuff Slot | (32, 144) | 32x32 | Active debuff frame |
| Shaky Slot | (64, 144) | 32x32 | Tremor active |
| Heart Racing Slot | (96, 144) | 32x32 | Cannot rest |
| Over-Caffeinated Slot | (128, 144) | 32x32 | Everything doubled |
| Duration Ring Overlay | (160, 144) | 32x32 | Radial timer for any slot |
| Stack Counter Pip | (192, 144) | 24x24 | Shot count |
| Intervention Button | (216, 144) | 40x32 | Emergency purge |

### Tolerance Progression:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tolerance Track Bar | (0, 176) | 192x24 | 0 Sovs → 200 Sovs spend rail |
| Tier Marker Novice | (0, 200) | 24x24 | Locked/unlocked states |
| Tier Marker Regular | (24, 200) | 24x24 | 50 Sovs |
| Tier Marker Aficionado | (48, 200) | 24x24 | 100 Sovs |
| Tier Marker Transcendent | (72, 200) | 24x24 | 200 Sovs |
| Spend Counter Plate "N / 50 SOVS" | (96, 200) | 96x24 | Progress readout; word lettered, no currency mark |
| Secret Menu Unlock Banner | (192, 176) | 64x48 | Transcendent reveal |

### Toasts & Prompts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Achievement Toast Frame | (0, 224) | 128x32 | "First Shot" / "The Limit" / "Ferdinand's Approval" |
| "Ferdinand Remembers Your Order" Banner | (128, 224) | 96x32 | The Regular unlock |
| Selfie Prompt Icon | (224, 224) | 32x32 | Photo-op indicator |

### Technical Notes:
- Response chips are border-coded (smooth / double / jagged) as well as colour-coded
- The Extraction Timer Dial doubles as the Rush Order display — it never speeds up, which is the gag
- Intervention Button must be ≥44px touch target at 1x; the 40x32 art sits inside a 48x48 hit rect

---

## 🎬 Animation Specifications

### The Extraction:
- **Duration:** 2.3 seconds, single play (scaled representation of 23 seconds)
- **Frames:** 4 (first drops → honey stream → crema blonding → cut)
- **Pattern:** Sequential, hold on cut frame for 0.6s while Ferdinand announces the time
- **Trigger:** Any espresso-based purchase
- **Purpose:** The location's core satisfaction beat — precision rendered as spectacle
- **Audio Sync:** Pump hum begins frame 1; pour patter frames 2–3; lever click + timer ping on frame 4
- **Performance Optimization:** None needed

### Steam Wand Purge:
- **Duration:** 0.6 seconds, single play
- **Frames:** 3 (purge burst → plume A → plume B)
- **Pattern:** Sharp attack, soft dissipate
- **Trigger:** Any milk drink order
- **Purpose:** The hiss that punctuates Ferdinand's sigh
- **Audio Sync:** Steam hiss on frame 1; sigh SFX layered under frame 2
- **Performance Optimization:** Single-frame static plume on Low LOD

### Ambient Steam Loop:
- **Duration:** 1.5 second cycle
- **Frames:** 3 (plume A → B → C)
- **Pattern:** Continuous loop, offset per emitter so plumes never sync
- **Trigger:** Constant during opening hours
- **Purpose:** The stand reads as *alive* from across the street
- **Audio Sync:** Continuous low steam bed
- **Performance Optimization:** Two emitters instead of four on Medium; one on Low

### Ferdinand Reaction Hold:
- **Duration:** 0.8 seconds minimum per reaction, single play
- **Frames:** 1 (reaction) + return to Precision Idle
- **Pattern:** Snap to reaction, hold, ease back
- **Trigger:** Order confirmed
- **Purpose:** The judgment is the product
- **Audio Sync:** Sigh / nod breath / long silence, matched per reaction; "Regular coffee" gets 1.5s of nothing before the lecture
- **Performance Optimization:** None needed

### The Rare Smile:
- **Duration:** 0.4 seconds, single play, no ease
- **Frames:** 1
- **Pattern:** Cut in, cut out — the player must doubt they saw it
- **Trigger:** Perfect order at Transcendent tolerance
- **Purpose:** "He Smiled. ONCE." selfie variant unlock
- **Audio Sync:** None. Silence is the point.
- **Performance Optimization:** None needed

### Caffeine Tremor:
- **Duration:** Continuous while Shaky or Over-Caffeinated
- **Frames:** 2 (shake overlay A ↔ B)
- **Pattern:** 8fps offset ghost on the character sprite, ±1px
- **Trigger:** Triplo / Quadruple consumed, or Over-Caffeinated status
- **Purpose:** The debuff is visible on your own body before the UI tells you
- **Audio Sync:** UI sound tempo increases with buff stacks
- **Performance Optimization:** Reduce to ±1px every other frame on Low LOD; fully disabled by Reduced Motion

### Heart Racing Pulse:
- **Duration:** 1.0 second cycle
- **Frames:** 2 (pulse ring 1 → 2) plus vignette fade
- **Pattern:** Systole/diastole loop matched to a 100bpm heartbeat SFX
- **Trigger:** Heart Racing status
- **Purpose:** Subtle, constant, slightly alarming
- **Audio Sync:** Heartbeat SFX, one beat per cycle, locked to frame 1
- **Performance Optimization:** Vignette only (no rings) on Low LOD; static vignette under Reduced Motion

### Grinder Dose Puff:
- **Duration:** 0.5 seconds, single play
- **Frames:** 2
- **Pattern:** Puff out, settle
- **Trigger:** Grind step of any preparation
- **Purpose:** Texture; also the visual cue that your order has been committed
- **Audio Sync:** Grinder whir tail-off on frame 2
- **Performance Optimization:** Cut on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Espresso stand outline | set at sheet layout | 128x64 | Primary interactable high-contrast frame |
| Ferdinand outline | set at sheet layout | 48x96 | Vendor silhouette, thick rim |
| Order panel high-contrast frame | set at sheet layout | 160x96 | Increased border weight, flattened fill |
| Drink icon outlines (all 11) | set at sheet layout | 32x48 | White rim variants for menu legibility |
| Intervention button outline | set at sheet layout | 40x32 | Emergency action must be findable instantly |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static steam plume | set at sheet layout | 48x64 | Single held frame, no loop |
| Tremor-free character overlay | set at sheet layout | 48x96 | Shaky conveyed by icon + border only |
| Static heart vignette | set at sheet layout | 96x48 | No pulse; constant subtle edge tint |
| Non-scrolling backdrop frame | set at sheet layout | 512x128 | Parallax disabled variant |
| Static crema (no bloom) | set at sheet layout | 24x24 | Final frame only |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steam hiss glyph | (176, 168) | 56x24 | Fires on every wand hiss |
| Grinder whir glyph | (128, 168) | 48x24 | Fires on every grind |
| Timer ping ring | (96, 168) | 32x24 | Fires on the 23-second cut |
| Sigh puff glyph | (128, 144) | 24x24 | Fires on every audible sigh |
| Discordant sting glyph | (208, 144) | 24x24 | Fires on the wrong-order sting |
| Approval sparkle | (152, 144) | 24x24 | Fires on the approval sound |
| Heartbeat pulse ring | (96, 96) | 32x32 | Visualises the Heart Racing SFX |

### Colorblind Considerations:
- Status icons are shape-first: Speed = chevron, Luck debuff = cracked clover, Shaky = doubled outline, Heart Racing = waveform, Over-Caffeinated = triple stack. No two share a silhouette.
- Response chips use border geometry (smooth / double / jagged), never colour alone
- Tolerance tier badges differ by pip count (1–4), not by hue
- Buff-vs-debuff duration rings sweep in opposite directions (clockwise = buff, counter-clockwise = debuff)
- Touch zones minimum 44px for order rows, the Intervention button, and the selfie prompt

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) for environment and characters; uncompressed for `grounds_concern_ui.png` and `grounds_concern_drinks.png` (icon legibility), with alpha across all sheets
- **Fallback:** PNG high quality for `grounds_concern_machine.png` — the brass specular banding is visible under aggressive compression

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| grounds_concern_environment | tileset, machine | 1024x1024 |
| grounds_concern_characters | Ferdinand, regulars & bros | 512x512 |
| grounds_concern_items_fx | drinks, effects, UI | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Four steam emitters, dust motes, crema bloom, brass glint, tremor overlay, heart pulse rings, parallax backdrop |
| Medium | Two steam emitters, halved dust density, crema bloom retained, no brass glint, single-layer backdrop |
| Low | One static steam plume, no dust, final-frame crema only, tremor at half rate, static backdrop; extraction sequence retained (it is the content) |

### Performance Targets:
- **Target FPS:** 60 (game-wide standard; location profile predates the 60 FPS ruling)
- **Max Draw Calls:** 10 per frame (per location profile)
- **Memory Footprint:** 25 MB maximum (per location profile)
- **Particle Limit:** 16 (steam 8, dust 4, crema/grounds 4 — tremor and heart pulse are shader overlays, not particles)

### Performance Notes:
- Single-scene location; no sub-scenes, no on-demand loading required
- The backdrop is two parallax strips from the tileset sheet, not separate textures — keeps the environment atlas to one bind
- Queue NPCs cap at 3 concurrent sprites; additional regulars are swapped, not added
- Status overlays (tremor, vignette) are full-screen shaders and count against the draw-call budget: never run both plus parallax on Low LOD

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- `TileMap` for street/façade tiles; `ParallaxBackground` with two `ParallaxLayer` nodes for the backdrop strips
- `AnimatedSprite2D` for Ferdinand (craft loop + reaction states) and the extraction sequence
- `Sprite2D` pool (max 3) for queue regulars
- `CPUParticles2D` (not GPU) for steam, dust motes, grounds puff
- `CanvasLayer` for the order panel, status HUD, and tolerance track
- Screen-space `ShaderMaterial` for the tremor ghost and Heart Racing vignette; both read a single `caffeine_intensity` uniform driven by active shot count
- Location state machine: `idle → assessed → ordering → preparing → served → reaction` drives Ferdinand's sprite state and the reaction chip
- Tolerance controller persists `total_spent` and derives tier (Novice / Regular / Aficionado / Transcendent); tier gates the Rare Smile frame and the Secret Menu banner
- Over-Caffeinated is a compound state: it doubles every active modifier and locks the rest/sleep action until expiry or Intervention

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Extraction frame 1 | Pump engage hum | On frame in |
| Extraction frames 2–3 | Pour patter into ceramic | Continuous |
| Extraction frame 4 | Lever click + timer ping | On cut |
| Steam wand purge | Steam hiss | On burst frame |
| Grinder dose puff | Grinder whir tail | Frame 2 |
| Ferdinand sigh reaction | Audible sigh | On reaction frame in |
| Wrong-order chip | Discordant sting | On chip appear |
| Approval nod | Warm resolution chord | On nod frame |
| Heart Racing pulse ring 1 | Heartbeat thump | Every cycle, frame 1 |
| Tolerance tier-up | Brass chime | On badge swap |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| "Caffeine Tolerance" | Tolerance track bar, four tier badges, spend counter plate | Purchases accumulate; badge swaps at 50 Sovs / 100 Sovs / 200 Sovs |
| "Ferdinand's Respect" | Rare Smile frame, approval sparkle, Ferdinand's Approval marker | Perfect order at Transcendent tier |
| "The Limit" | Over-Caffeinated icon, tremor overlay, vibration motion ghost, empty cup cluster | Reach and survive Over-Caffeinated status |
| "The Intervention" | Over-Caffeinated NPC In Distress, Intervention Administered, Intervention drink sprite | Help an NPC who over-caffeinated |
| "Espresso Purist" | All six core drink sprites, milk-drink icons greyed | Complete run without purchasing a milk drink |
| Selfie Spot — Standard | Tiny Cup Held, sunlit steam shaft, caption "Authentic Experience" | Any visit |
| Selfie Spot — "The Vibration" | Empty cup cluster, vibration motion ghost, caption "No Regrets (Many Regrets)" | Requires Over-Caffeinated |
| Selfie Spot — "Ferdinand's Approval" | Rare Smile, Ristretto sprite, caption "He Smiled. ONCE." | Requires Transcendent tolerance |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Kaffeehaus Row | Shared district façade tiles, backdrop strips, street dressing | Standard street walk transition |
| Café Existenz | Speed/Luck status icons persist into philosophical debate checks | None (status carry-over) |
| The Bassline Opera House | Speed buff and tremor overlay feed rhythm-combat timing windows | None (buff carry-over; tremor narrows windows) |
| The Moderato Pub | Coffee/beer culture clash dialogue references tolerance tier badge | None (flag check on entry) |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A surgical theatre that sells coffee — everything gleams, nothing is optional"
- **Color Mood:** Espresso brown and brass gold against morning steam-white; warmth that is technically warm and emotionally not
- **Lighting:** Low morning sun from screen-left, catching steam and brass; hard contact shadows under the counter; no artificial light until dusk
- **Texture:** Mirror-polished metal, matte ceramic, hessian bean sacks, chalk dust on slate, one paper cup wearing visible dust

### Environmental Storytelling:
- No large cups exist anywhere in the scene — the absence is dressed, signposted, and enforced by a placard
- A single dusty paper cup on the shelf, never used, is the only concession to takeaway culture in the entire location
- The extraction log book is open and full: every shot Ferdinand has ever pulled, timed and recorded
- The sugar bowl is present, reachable, and positioned further from the customer than anything else on the counter
- Three signs stacked above the machine escalate from menu to prohibition to prophecy ("Yes, You Will Shake. This Is Correct.")
- Coffee-stained cobbles and a grounds-choked gutter show the stand has been here far longer than any tourist has

### Character Integration Notes:
- Ferdinand is rendered with harder outlines than the queue NPCs — he is the only fully in-focus person in the scene
- His hands are the visual control group: absolutely steady in every frame, against a queue of people vibrating
- Queue regulars are drawn at slightly reduced contrast so the eye lands on the machine and then on Ferdinand
- The bros are the only sprites permitted broad, loose posture; everyone else in this location stands correctly

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Rare Smile** — 0.4 seconds, once per playthrough, and the selfie caption is "He Smiled. ONCE."
2. **The Vibration selfie** — player visibly ghosting, six empty cups on the counter, Ferdinand observing with scientific interest
3. **Chadwick's caramel request** — portafilter set down, deep breath, the entire stand holding still
4. **The three stacked signs** in one crop — menu, prohibition, prophecy
5. **Bradley's ristretto moment** — Ferdinand stops, turns: "...You. You are welcome here."

### Quote Potential:
- "Welcome. What can I— actually, I already know. You want it strong." - Ferdinand the Focused
- "The extraction was 23 seconds. PERFECT. You're welcome." - Ferdinand the Focused
- "Decaffeinated espresso is like... a silent symphony. What is the POINT?" - Ferdinand the Focused
- "There is a place three streets over. They serve... that. Go there. Please." - Ferdinand the Focused
- "I... can provide this. But the coffee will not forgive you." - Ferdinand, on sugar
- "Fascinating. The heart rate must be extraordinary." - Ferdinand, watching a Quadruple land
- "Yes, You Will Shake. This Is Correct." - stand signage

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | grounds_concern_tileset.png | 1024x512 |
| 2 | grounds_concern_machine.png | 512x256 |
| 3 | ferdinand_focused.png | 384x288 |
| 4 | grounds_concern_npcs.png | 384x192 |
| 5 | grounds_concern_drinks.png | 256x256 |
| 6 | grounds_concern_effects.png | 256x192 |
| 7 | grounds_concern_ui.png | 256x256 |

**Total Estimated Memory:** ~4 MB (1,019,904 px uncompressed RGBA); ~1.1 MB after VRAM compression — comfortably inside the 25 MB profile budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `grounds_concern_tileset.png` (1024x512)
- [ ] `grounds_concern_machine.png` (512x256)
- [ ] `ferdinand_focused.png` (384x288)
- [ ] `grounds_concern_npcs.png` (384x192)
- [ ] `grounds_concern_drinks.png` (256x256)
- [ ] `grounds_concern_effects.png` (256x192)
- [ ] `grounds_concern_ui.png` (256x256)

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
- **Documentation:** Animation timing reference sheet + parallax layer guide (two strips, 0.25x / 0.6x) + status-overlay shader reference

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] No large cup appears anywhere in any sheet except the single dusty unused paper cup
- [ ] Ferdinand's hands are steady in all 22 of his frames — zero tremor, no exceptions
- [ ] Extraction frames 1–4 align on the cup rim with no sub-pixel drift
- [ ] Drink silhouettes are countable by shot volume at 32px without labels
- [ ] The three stacked signs are legible together in a 256px-wide crop
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (espresso snobbery, craft devotion weaponised) is clear throughout
- [ ] The Rare Smile reads as genuine and is visibly different from the Approving Nod
- [ ] Ferdinand's disappointment reads as grief, never contempt
- [ ] Performance optimized (CPU particles only, 10-draw-call ceiling respected, one atlas bind per group)
- [ ] Touch zone sizing considered (44px minimum for order rows, Intervention button, selfie prompt)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia and Kaffeehaus Row only; Viennese coffeehouse tradition evoked, never named as a real place |
| Cultural Specificity | ✅ | Viennese coffeehouse reverence colliding with third-wave espresso worship; extraction-time orthodoxy |
| Satirical Targets Appropriate | ✅ | Coffee snobbery and the bros' inability to read a room; Ferdinand is affectionate and genuinely skilled, not a national stereotype |
| Seedy Underbelly Present | ❌ | Profile documents no vice or exploitation operation. Nearest elements: the 1 Sov sugar "processing fee" and a spend-gated tolerance ladder that rewards escalating consumption. Flagged for owner — this location is intentionally benign |
| Gameplay Value Established | ✅ | Speed-buff/Luck-debuff shop, four-tier tolerance progression, four status effects, order-reaction system, three selfie variants, four quests |
| Technical Feasibility | ✅ | Seven sheets, three atlases, three LOD tiers, no sub-scenes, CPU particles only |
| Performance Budget | ✅ | 60 FPS / 10 draw calls / 25 MB taken verbatim from the profile's stated budget. Normalized to the game-wide 60 FPS standard (author ruling); effect density must be tuned to hold it|
| Accessibility Features | ✅ | Visual glyphs for all seven audio cues; static/reduced-motion variants for steam, tremor, heart pulse, parallax; shape-first status icons |
| No Crypto Elements | ✅ | None present, and the profile explicitly confirms "No crypto elements (Pure caffeine worship)" |
| Social Media Integration | ✅ | Three documented selfie variants with unlock conditions, five screenshot moments, seven quotable lines |

**Grounds For Concern: a stand the size of a wardrobe that will make you faster than you have ever been and luckier than you have ever been unlucky — where the only steady hands in Sinfonia belong to the man who took yours away.**
