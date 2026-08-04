# Café Existenz - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Café Existenz - the philosophical coffeehouse where pretentious intellectuals go to feel smart, tourists go to feel inadequate, and everyone's coffee gets cold because they're too busy debating whether temperature is subjective. It is Sinfonia's dialogue-combat arena and Wi-Fi hub, where losing three debates earns you the "Intellectually Defeated" status.

**Location ID:** `sinfonia_kaffeehausrow_cafe_existenz_01`
**Theme:** Coffeehouse intellectual culture — performative depth and competitive obscurity as social gatekeeping
**Zone:** Kaffeehaus Row, Intellectual Café District
**Hours:** 7 AM - 1 AM (intellectuals keep odd hours)
**Primary Function:** Dialogue combat hub / Wi-Fi hotspot / quest gossip node — "The Debate" system, Bravado drain economy, Regular status unlock, Eternal Student couchsurf

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Coffee Brown | #6F4E37 | Wood, tabletops, coffee everything |
| Intellectual Burgundy | #722F37 | Upholstery, drapes, accents |
| Cream Paper | #FFFDD0 | Walls, newspapers, menus |
| Judgment Gray | #808080 | Smoke, shadows, disapproval |
| Art Nouveau Gold | #CFB53B | Window lettering, chandelier trim |
| Espresso Black | #1C1C1C | Chess pieces, ink, formal wear |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/cafe_existenz/
├── environment/
│   ├── cafe_existenz_tileset.png
│   └── cafe_existenz_furnishings.png
├── npcs/
│   ├── cafe_existenz_staff.png
│   ├── cafe_existenz_philosophers.png
│   └── cafe_existenz_ambient_npcs.png
├── effects/
│   └── cafe_existenz_effects.png
└── ui/
    └── cafe_existenz_ui.png
```

---

## ☕ Sprite Sheet 1: Coffeehouse Tileset
**File:** `cafe_existenz_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #6F4E37 (Coffee Brown), #FFFDD0 (Cream Paper), #722F37 (Burgundy), #CFB53B (Gold)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Parquet Main Hall | (0, 0) | 32x32 | Warm herringbone wood |
| Parquet Worn | (32, 0) | 32x32 | Regulars'-path wear pattern |
| Vestibule Tile | (64, 0) | 32x32 | Checkered entry mosaic |
| Back Room Carpet | (96, 0) | 32x32 | Deep burgundy, quieter |
| Lounge Floorboard | (128, 0) | 32x32 | Smoke-stained boards |
| Cobblestone Exterior | (160, 0) | 32x32 | Street outside, tree-lined |

### Wall Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cream Wall Aged | (0, 32) | 32x64 | Nicotine-warmed plaster |
| Art Nouveau Panel | (32, 32) | 32x64 | Curvilinear wood inlay |
| Mirror Wall Section | (64, 32) | 32x64 | High mirror strip (for judging across the room) |
| Burgundy Drape Wall | (96, 32) | 32x64 | Heavy curtain segment |
| Lounge Wall Stained | (128, 32) | 32x64 | Smoke-tinted variant |
| Wainscot Cap | (160, 32) | 32x32 | Dark wood molding |

### Windows & Doors:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Large Front Window | (0, 96) | 64x80 | Displays chess games and newspaper readers to the street |
| Window Gold Lettering | (64, 96) | 64x80 | "Café Existenz" reversed interior view |
| Ornate Wooden Door | (128, 96) | 32x64 | Brass handles, judgmental weight |
| Back Room Door | (160, 96) | 32x64 | Regulars-only, unlockable |
| Lounge Archway | (192, 96) | 48x80 | Annexed smoking lounge connection |
| Tall Window Seat Bay | (240, 96) | 64x80 | Tourist section bay — best view, worst treatment |

### Ceiling & Architecture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chandelier | (0, 176) | 80x64 | Art nouveau brass and glass |
| Ceiling Rose | (80, 176) | 48x48 | Plaster medallion |
| Reading Lamp | (128, 176) | 24x40 | Green-shade table spot |
| Wall Sconce | (152, 176) | 16x32 | Warm reading light |

### Exterior Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Façade Section | (0, 240) | 96x96 | Art nouveau styling, upper story |
| Street Tree | (96, 240) | 48x96 | Kaffeehaus Row lindens |
| Outdoor Table Set | (144, 240) | 48x48 | Cobblestone seating spill |
| Chalkboard Sign | (192, 240) | 32x48 | "Today's Question" street stand |
| Awning Segment | (224, 240) | 64x32 | Burgundy canvas |

### Technical Notes:
- Worn parquet tiles map the regulars' territorial routes — environmental storytelling via flooring
- Window seat bay renders with warmest light and best chairs; the irony is intentional and unnoticed
- Lounge tiles get a permanent gray tint layer (last week's smoke)

---

## 📰 Sprite Sheet 2: Furnishings & Props
**File:** `cafe_existenz_furnishings.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #6F4E37 (Brown), #1C1C1C (Black), #FFFDD0 (Cream)

### Tables & Seating:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marble Café Table | (0, 0) | 32x32 | Eavesdropping-optimized placement unit |
| Table With Chess | (32, 0) | 40x32 | Decades-old game in progress |
| Table With Newspapers | (72, 0) | 40x32 | Wooden-holder spread |
| Bentwood Chair | (112, 0) | 24x32 | Thonet-style |
| Window Seat Armchair | (136, 0) | 32x32 | The most comfortable chair (tourist section) |
| Lounge Sofa | (168, 0) | 64x32 | Nap-friendly "thinking" couch |
| Standing Student Spot | (232, 0) | 24x40 | Standing-room rail section |

### The Judgment Zone (Vestibule):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Host Stand | (0, 48) | 32x48 | Herr Konditor's assessment post |
| Seating Chart Board | (32, 48) | 48x64 | Visibly a social hierarchy |
| Coat Rack With Scarves | (80, 48) | 32x64 | Scarves from every European philosophy department |
| Newspaper Stand 12 Languages | (112, 48) | 48x64 | All opinion sections |

### Café Service Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chess Set Detail | (160, 48) | 48x48 | Mid-game, elaborate pieces |
| Newspaper On Holder | (208, 48) | 40x24 | Traditional Viennese wooden rod |
| Coffee Service Tray | (248, 48) | 32x24 | Melange with water glass, tiny tongs |
| Sugar Cubes & Tongs | (280, 48) | 16x16 | Served with a disapproving look |
| Menu German Only | (296, 48) | 24x32 | No translations; asking = judgment |
| Bill As Equation | (320, 48) | 24x32 | Philosophical arithmetic |

### Wall Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Philosopher Portrait | (0, 112) | 48x64 | Framed, glowering |
| Chalkboard Daily Question | (48, 112) | 64x48 | "If a tourist orders and no local acknowledges them..." |
| Framed First Edition | (112, 112) | 40x48 | Untouchable, unread |
| Wi-Fi Sign (Discreet) | (152, 112) | 24x24 | Network name posted, password known by all |
| Eye-In-Cup Logo Plaque | (176, 112) | 32x32 | Café emblem |

### Back Room & Lounge Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Room Round Table | (0, 176) | 48x40 | Where the REAL conversations happen |
| Secret Menu Card | (48, 176) | 24x32 | Regulars-only items |
| Ashtray Stand | (72, 176) | 16x40 | Lounge fixture |
| Last Week's Papers Pile | (88, 176) | 40x24 | Lounge reading, expired |
| Bookcase Secret Door | (128, 176) | 64x80 | Back-room passage toward Baroness' Ballroom |

### Technical Notes:
- Chess sets never change state during a session — finishing would mean someone lost
- Bookcase secret door aligns to the ballroom café-route door frame (32x64 opening within 64x80 prop)
- Menu and bill props double as inspection-view UI textures

---

## 🎩 Sprite Sheet 3: Staff — Herr Konditor & Egon
**File:** `cafe_existenz_staff.png`
**Dimensions:** 384x288 pixels
**Color Palette:** #1C1C1C (Formal Black), #FFFFFF (Shirt White), #722F37 (Burgundy)

### Herr Konditor — The Maître D' (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Assessment Idle | (0, 0) | 48x96 | Monocle raised, judging before you speak |
| Long Pause | (48, 0) | 48x96 | "Table for... *long pause* ...three?" |
| Seat Assignment | (96, 0) | 48x96 | Gesturing toward your hierarchy tier |
| Charmed (Rare) | (144, 0) | 48x96 | Better-placement concession |

### Egon — The Server (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Eyebrow Idle | (192, 0) | 48x96 | Permanently raised eyebrow |
| Order Interrogation | (240, 0) | 48x96 | "Are you CERTAIN? Perhaps you meant the Franziskaner." |
| Order Forgotten | (288, 0) | 48x96 | Walking past tourist section, tray empty |
| Audible Exhale | (336, 0) | 48x96 | Response to "large coffee" |

### Egon Service States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tray Delivery | (0, 96) | 48x96 | Correct order, delivered with judgment |
| Interrupting Debate | (48, 96) | 48x96 | Environmental hazard state — breaks concentration |
| Lounge Friendly | (96, 96) | 48x96 | The only place servers are friendly |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Konditor's Monocle | (144, 96) | 16x16 | Functional, glinting |
| Egon's Order Pad | (160, 96) | 16x24 | Never consulted |
| Silver Tray | (176, 96) | 32x24 | Coffee service prop |
| Water Glass Proper | (208, 96) | 16x24 | Brought only if requested correctly |

### Judgment Escalation Row (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Judgment Level 1 | (0, 192) | 48x96 | Shared staff pose: mild disappointment |
| Judgment Level 2 | (48, 192) | 48x96 | Shared staff pose: visible pain |
| Judgment Level 3 | (96, 192) | 48x96 | Shared staff pose: "A Melange is a Melange. It has been a Melange for 200 years." |

### Character Notes:
- Konditor's monocle is functional and must glint on assessment frames
- Egon's eyebrow never lowers — it is load-bearing characterization
- Judgment escalation poses are palette-swapped for either staff member

---

## 🧠 Sprite Sheet 4: Philosophers & Debate Opponents
**File:** `cafe_existenz_philosophers.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Tweed browns, turtleneck blacks, #722F37 (Burgundy)

### Herr Doktor Professor von Grübelstein — Boss (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pipe Idle | (0, 0) | 64x96 | 70s, wild gray hair, tweed with elbow patches |
| Opening Challenge | (64, 0) | 64x96 | "What could you POSSIBLY teach me?" |
| Glasses Removal | (128, 0) | 64x96 | Pinching nose — Chadwick has spoken |
| Forty-Seven Years | (192, 0) | 64x96 | Full lecture eruption |
| Loneliness Break | (256, 0) | 64x96 | Kindness pierces the defense |
| Mentor Warm | (320, 0) | 64x96 | Befriended state, coffee companion |

### Standard Opponents (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Nihilist | (0, 96) | 48x80 | "Nothing matters. Why are you here?" — still drinking coffee |
| The Kantian | (48, 96) | 48x80 | Duty-posture, rigid |
| The Postmodernist | (96, 96) | 48x80 | Framework-rejecting gesture |
| The Graduate Student | (144, 96) | 48x80 | Aggressive citations, one theorist deep |
| The Amateur Intellectual | (192, 96) | 48x80 | Self-taught, credential-triggered |
| The Art School Dropout | (240, 96) | 48x80 | Everything is aesthetics |
| The Tourist Intellectual | (288, 96) | 48x80 | Also lost, potential ally |

### Debate Action Poses (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dramatic Gesture A | (336, 96) | 48x80 | Shared debate animation, point raised |
| Dramatic Gesture B | (384, 96) | 48x80 | Shared debate animation, dismissal wave |
| Defeated Slump | (432, 96) | 48x80 | Debate lost, aphorism exhausted |

### Environmental Hazard NPCs (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Eavesdropper | (0, 176) | 48x80 | Chair-scoot intrusion pose |
| The Corrector | (48, 176) | 48x80 | Mid-sentence pronunciation fix, finger raised |

### Victory Reward Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Void Sugar | (96, 176) | 32x32 | Removes debuffs by removing the concept of debuffs |
| Categorical Cappuccino | (128, 176) | 32x32 | Powerful but must be shared |
| Deconstructed Pastry | (160, 176) | 32x32 | Confusing but satisfying |
| Honorary Doctorate | (192, 176) | 48x48 | Fake, but +5 INT for showing it |

### Debate Table Scene:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Debate Table Two-Top | (0, 256) | 96x96 | Face-off framing piece for dialogue combat |
| Spectator Lean-In Pair | (96, 256) | 96x80 | Adjacent tables listening |
| Betting Regulars | (192, 256) | 96x80 | Three tables betting on how long the tourists last |

### Character Notes:
- Von Grübelstein's hair volume increases with debate intensity
- The Nihilist must always hold his coffee cup — his exploitable contradiction is visible
- Postmodernist wears the oversized glasses; Graduate Student clutches ONE book

---

## 👥 Sprite Sheet 5: Ambient NPCs
**File:** `cafe_existenz_ambient_npcs.png`
**Dimensions:** 384x192 pixels
**Color Palette:** Muted formals, tweed, travel-wear brights

### The Eternal Game (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chess Player 1 Frozen | (0, 0) | 48x80 | 20 years of concentration |
| Chess Player 1 Move | (48, 0) | 48x80 | One piece advanced |
| Chess Player 2 Frozen | (96, 0) | 48x80 | The other half of the silence |
| Chess Player 2 Sigh | (144, 0) | 48x80 | This is their entire relationship |

### The Eternal Student (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Thesis Idle | (192, 0) | 48x80 | 15 years into the dissertation |
| Thesis Summary | (240, 0) | 48x80 | Explaining, sleep-check active |
| Espresso Morning | (288, 0) | 48x80 | Couchsurf morning scene pose |
| "Almost Done" | (336, 0) | 48x80 | Has been almost done since 2009 |

### Hierarchy Filler NPCs (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Philosopher King Seated | (0, 96) | 48x80 | Back-room aphorism tier |
| Academic Correcting | (48, 96) | 48x80 | Quotes sources, fixes pronunciation |
| Window Artist | (96, 96) | 48x80 | Makes everything about their work |
| Over-Caffeinated Student | (144, 96) | 48x80 | Standing, desperate to be noticed |
| Confused Tourist Pair | (192, 96) | 64x80 | Window seats, unacknowledged order |
| Equally Confused Tourist | (256, 96) | 48x80 | +5 Bravado when found |

### Character Notes:
- Chess players share one two-frame cycle each; a move fires at most once per scene visit
- Hierarchy tiers must be readable by posture alone: Kings recline, Students hover
- Tourist money belts visible — the section identifier

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `cafe_existenz_effects.png`
**Dimensions:** 256x128 pixels
**Color Palette:** #FFFFFF (Steam), #808080 (Smoke), #FFFACD (Light)

### Coffee Steam (16x32 each, 3 frames):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steam Rise | (0, 0) | 16x32 | From untouched cooling cups |
| Steam Disperse | (16, 0) | 16x32 | Mid-fade |
| Steam Gone | (32, 0) | 16x32 | The coffee is now cold; the debate continues |

### Ambience:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Window Light Beam | (48, 0) | 32x64 | Afternoon shaft over tourist section |
| Dust Motes | (80, 0) | 48x48 | Floating in light beam |
| Cigarette Smoke Curl | (128, 0) | 16x48 | Lounge-only drift |
| Page Turn Flutter | (144, 0) | 24x24 | Newspaper animation accent |

### Debate Combat Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tension Lines | (0, 64) | 48x32 | Rising stakes between debaters |
| Devastating Counter Flash | (48, 64) | 48x48 | Gold burst — debate ends in victory |
| Wrong Answer Deflate | (96, 64) | 32x32 | Gray sag ring on debate loss |
| Mispronunciation Sting | (128, 64) | 32x32 | Jagged red slip glyph (-5 Bravado) |
| Judgment Aura | (160, 64) | 48x48 | Gray radiance from observing regulars |
| Aha Sparkle | (208, 64) | 24x24 | Intellectual victory glint |

### Technical Notes:
- Steam emitters cap at 6 concurrent cups; debate tables get priority
- Judgment aura is a pulsing overlay on NPCs witnessing player failure — subtle, 20% opacity max
- Devastating Counter flash doubles as the "Cogito Ergo OWNED" selfie effect

---

## 🖥️ Sprite Sheet 7: UI & Items
**File:** `cafe_existenz_ui.png`
**Dimensions:** 384x256 pixels
**Color Palette:** #722F37 (Burgundy), #FFFDD0 (Cream), #CFB53B (Gold)

### Debate Combat Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Debate UI Frame | (0, 0) | 256x128 | Turn-based dialogue combat panel |
| Response Tier — Confident Bluff | (256, 0) | 96x24 | High-risk option chip |
| Response Tier — Surface | (256, 24) | 96x24 | Safe option chip |
| Response Tier — Informed | (256, 48) | 96x24 | INT-check option chip (hatched border) |
| Response Tier — Devastating | (256, 72) | 96x24 | Rare counter chip (gold border) |
| Stalemate Icon | (256, 96) | 24x24 | Draw result glyph |

### Bravado Economy:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bravado Drain Meter | (0, 128) | 64x32 | Existential-weight timer (-1 per 10 min) |
| Bravado Gain Popup | (64, 128) | 48x24 | "+15" debate victory float |
| Embarrassed Status | (112, 128) | 32x32 | 30-minute debuff icon |
| Intellectually Defeated | (144, 128) | 32x32 | Three-loss failure status |

### Ordering & Wi-Fi:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Coffee Menu Panel | (0, 160) | 96x96 | Kleiner Brauner / Melange / Einspänner / Kapuziner, German only |
| Order Success Chime Glyph | (96, 160) | 24x24 | Ordered in German (+10 Bravado) |
| Wi-Fi Icon | (120, 160) | 32x32 | "Existence_Precedes_Essence_5G" |
| ICQ Panel | (152, 160) | 96x64 | Intellectual threads + Mom call (SP restore) |
| Daily Question Board UI | (248, 160) | 96x48 | Chalkboard text panel |

### Selfie & Progression:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cultured Selfie Frame | (0, 128) → moved | — | (superseded — see below) |
| Regular Status Badge | (176, 128) | 32x32 | Three-visit unlock, back-room key visual |
| Cultured Selfie Frame | (208, 128) | 96x64 | Window-seat photo overlay (+10 Bravado post) |
| Temporary Intellectualism Buff | (304, 128) | 32x32 | +2 INT couchsurf icon |

### Technical Notes:
- Response tier chips are shape- and border-coded, not color-only
- Debate UI must hold four response chips plus portrait at 44px+ touch sizing
- The duplicate "Cultured Selfie Frame" row above is a deliberate strike-through correction: use (208, 128) 96x64 as final placement

---

## 🎬 Animation Specifications

### Coffee Steam Fade:
- **Duration:** 2.0 second cycle
- **Frames:** 3
- **Pattern:** Rise → disperse → gone, loop while coffee is "hot"; stops permanently after 60s (coffee is cold now)
- **Trigger:** Any served cup
- **Purpose:** Cooling coffee is the café's thesis statement — everyone is too busy performing to drink
- **Audio Sync:** None
- **Mobile Optimization:** Cap 6 → 3 emitters

### Chess Piece Move:
- **Duration:** 1.5 seconds (move + opponent sigh)
- **Frames:** 2 per player
- **Pattern:** Player 1 move → 0.5s beat → Player 2 sigh; at most once per scene visit
- **Trigger:** Random, 90-180s after entry
- **Purpose:** The decades-old game advances one move; blink and you miss the entire relationship
- **Audio Sync:** Chess piece click on move frame; soft exhale on sigh frame
- **Mobile Optimization:** None needed

### Egon Order Interrogation:
- **Duration:** 2.5 seconds (hold on final frame)
- **Frames:** 3 (eyebrow idle → interrogation → exhale)
- **Pattern:** Single play, hold exhale during dialogue
- **Trigger:** Player orders anything non-canonical
- **Purpose:** The ordering gauntlet — every menu mistake is a social event
- **Audio Sync:** Audible exhale SFX on frame 3
- **Mobile Optimization:** None needed

### Von Grübelstein Glasses Removal:
- **Duration:** 1.8 seconds
- **Frames:** 3 (idle → glasses off → nose pinch)
- **Pattern:** Single play, hold pinch during "...continue."
- **Trigger:** Player selects a Confident Bluff that fails
- **Purpose:** The boss's signature tell — maximum disappointment, minimum motion
- **Audio Sync:** Dramatic sting (quiet) on pinch frame
- **Mobile Optimization:** None needed

### Debate Victory Flash:
- **Duration:** 0.8 seconds, single play
- **Frames:** 2 (flash → sparkle)
- **Pattern:** Burst on winning response, sparkle settle
- **Trigger:** Debate won / Devastating Counter played
- **Purpose:** The intellectual "aha" — visible vindication
- **Audio Sync:** Satisfying "aha" chime on frame 1
- **Mobile Optimization:** None needed

### Dramatic Gesturing (Ambient):
- **Duration:** 3.0 second cycle
- **Frames:** 2 (gesture A ↔ gesture B)
- **Pattern:** Loop on background debating NPCs, staggered phases per table
- **Trigger:** Constant in main hall
- **Purpose:** The room performs intelligence for an audience too busy performing to watch
- **Audio Sync:** Murmur bed swells match gesture peaks (loose sync)
- **Mobile Optimization:** Freeze to gesture A on Low LOD

### Newspaper Page Turn:
- **Duration:** 0.6 seconds, single play
- **Frames:** 2 (flutter → settled)
- **Pattern:** Random reader NPC every 10-20s
- **Trigger:** Ambient timer
- **Purpose:** Traditional coffeehouse texture
- **Audio Sync:** Page rustle on frame 1
- **Mobile Optimization:** Halve frequency

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Debate opponent outline | set at sheet layout | 48x80 | High-contrast rim on active debater |
| Host stand highlight | set at sheet layout | 32x48 | Entry interaction marker |
| Back room door frame | set at sheet layout | 32x64 | Unlockable-area cue |
| Menu board outline | set at sheet layout | 96x96 | Ordering interaction visibility |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static steam cups | set at sheet layout | 16x32 | No steam loop; hot/cold shown by cup saturation |
| Gesture-frozen debaters | set at sheet layout | 48x80 | Background NPCs locked to neutral pose |
| Dust-free light beam | set at sheet layout | 32x64 | Static beam without motes |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Exhale puff glyph | set at sheet layout | 24x24 | Over Egon on judgment exhale audio |
| Chess click marker | set at sheet layout | 16x16 | Ring on moved piece when click plays |
| Debate sting burst | set at sheet layout | 32x32 | Jagged glyph on loss sting; gold on victory chime |
| Murmur intensity bars | set at sheet layout | 24x16 | Ambient conversation level indicator |

### Colorblind Considerations:
- Response tier chips differ by border shape (rounded/square/hatched/double-line), never color alone
- Bravado gain vs. drain popups use +/- glyphs with distinct silhouettes
- Hot vs. cold coffee readable by steam presence and cup tone, not hue shift alone
- Touch zones minimum 44px for debate chips, menu, and Wi-Fi interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); philosophers sheet ASTC 4x4 — portrait close-ups in debate UI
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for tileset (window lettering must stay crisp)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cafe_existenz_environment | tileset, furnishings | 1024x1024 |
| cafe_existenz_characters | staff, philosophers, ambient NPCs | 1024x512 |
| cafe_existenz_effects_ui | effects, UI | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full steam (6 cups), dust motes, smoke curls, gesturing crowd, page turns |
| Medium | 3 steam cups, no smoke curls, halved page-turn frequency |
| Low | No ambient particles, frozen background NPCs, static chess |

### Performance Targets:
- **Target FPS:** 60 (per location profile budget)
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 45 MB maximum
- **Particle Limit:** 18 (steam 6, dust 8, smoke 4)

### Performance Notes:
- Back room and smoking lounge load on-demand (door-gated sub-scenes)
- Debate NPC conversations pre-rendered per profile mobile spec — no live crowd dialogue simulation
- Debate UI is a persistent CanvasLayer instanced only during encounters

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for staff and boss states; Sprite2D pool for hierarchy filler NPCs
- CPUParticles2D for steam, dust, smoke
- CanvasLayer for debate UI and Bravado meters
- Location state machine: `vestibule_judgment → seated(tier) → debate_active → debate_resolved → regular_unlocked` drives seating and NPC availability
- Wi-Fi hotspot node exposes ICQ panel + event calendar data (masquerade dates, concert schedules)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Egon exhale frame | Audible exhale | Frame 3 of interrogation |
| Chess piece move | Piece click | On move frame |
| Debate loss deflate | Dramatic sting | On deflate spawn |
| Debate victory flash | "Aha" chime | Frame 1 |
| Mispronunciation glyph | Sad trombone | On glyph spawn |
| Page turn | Paper rustle | Frame 1 |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Philosophy Debates | Debate UI, all opponent sprites, Bravado meters | Extended dialogue trees with Bravado consequences |
| The Eternal Student's Thesis | Eternal Student set, thesis props | Comedy fetch quest + couchsurf path |
| The Professor's Secret | Von Grübelstein full state set, mentor warm pose | Befriend route, tragic backstory unlock |
| Art Theft Investigation | ICQ panel, gossip NPC poses | Café gossip provides underground art market hints |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bassline Opera House | ICQ event calendar, cultural gossip NPCs | None (information only) |
| The Black-Tie Backroom | Regulars' hint dialogue poses | None (rumor only) |
| The Moderato Pub | Tempo-theory debater sprites shared reference | Standard street transition |
| Baroness' Ballroom | Bookcase secret door (café route entry) | Bookcase swing + waltz audio bleed |
| Café Sachertorte / Grounds For Concern | Kaffeehaus Row shared street ambience | None |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "The Temple of Thought — performative depth in art nouveau framing"
- **Color Mood:** Coffee browns and burgundy warmth undercut by judgment gray
- **Lighting:** Natural window shafts, warm chandeliers, green-shaded reading pools; the tourist section gets the best light and nobody appreciates it
- **Texture:** Aged plaster, marble tabletops, newsprint, pipe smoke

### Environmental Storytelling:
- Worn parquet paths map decades of regulars' territorial routes
- Seating chart visibly diagrams the social hierarchy Konditor enforces
- Untouched pastries and cold coffee on every debate table — consumption lost to performance
- The most comfortable chairs are in the "worst" section; the irony is noted by no one

### Character Integration Notes:
- Hierarchy readable by posture: Philosopher Kings recline, Academics sit upright, Students hover
- Egon and Konditor share the judgment escalation poses via palette swap
- Von Grübelstein's loneliness must be visible in the idle — intimidation as armor

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The daily chalkboard question** — infinitely replaceable meme text slot
2. **Von Grübelstein's glasses removal** mid-Chadwick-debate
3. **The betting regulars** watching tourists wait for a server who will never come
4. **The chess players' single move** — 20 years of silence, one advanced pawn

### Quote Potential:
- "Today's Question: If a tourist orders in a café and no local acknowledges them, did they really order?" - Chalkboard
- "A Melange is a Melange. It has been a Melange for 200 years." - Egon
- "Then you have not read him at all." - Philosopher, to Bradley
- "I have taught philosophy for 47 years. What could you POSSIBLY teach me?" - Herr Doktor Professor von Grübelstein
- "Cogito Ergo OWNED" - Debate Victor selfie caption

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | cafe_existenz_tileset.png | 1024x512 |
| 2 | cafe_existenz_furnishings.png | 512x384 |
| 3 | cafe_existenz_staff.png | 384x288 |
| 4 | cafe_existenz_philosophers.png | 512x384 |
| 5 | cafe_existenz_ambient_npcs.png | 384x192 |
| 6 | cafe_existenz_effects.png | 256x128 |
| 7 | cafe_existenz_ui.png | 384x256 |

**Total Estimated Memory:** ~5 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `cafe_existenz_tileset.png` (1024x512)
- [ ] `cafe_existenz_furnishings.png` (512x384)
- [ ] `cafe_existenz_staff.png` (384x288)
- [ ] `cafe_existenz_philosophers.png` (512x384)
- [ ] `cafe_existenz_ambient_npcs.png` (384x192)
- [ ] `cafe_existenz_effects.png` (256x128)
- [ ] `cafe_existenz_ui.png` (384x256)

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
- **Documentation:** Animation timing reference sheet + debate UI layout guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Hierarchy tiers readable by NPC posture at game resolution
- [ ] Egon's eyebrow raised in every frame
- [ ] Steam-fade tells the cold-coffee story on debate tables
- [ ] Chalkboard question panel supports swappable text
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (intellectual pretension, not learning) is clear throughout
- [ ] Back room and secret bookcase door have discoverable visual cues
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Viennese coffeehouse tradition evoked, never named |
| Cultural Specificity | ✅ | Kaffeehaus culture, Melange orthodoxy, newspaper-rod tradition, chess institutions |
| Satirical Targets Appropriate | ✅ | Pretension and gatekeeping satirized, not philosophy or learning — punches up |
| Seedy Underbelly Present | ✅ | Tourist order-forgetting, overcharging, judgment-as-service, betting on tourists |
| Gameplay Value Established | ✅ | Dialogue combat, Bravado economy, Wi-Fi hub, quest gossip, couchsurf |
| Technical Feasibility | ✅ | Seven sheets, atlas plan, pre-rendered crowd, LOD tiers documented |
| Mobile Performance Budget | ✅ | 60 FPS, 18 draw calls, 45 MB, 18 particles (per profile budget) |
| Accessibility Features | ✅ | Visual cues for all audio events; static motion variants |
| No Crypto Elements | ✅ | None present — philosophy satire only |
| Social Media Integration | ✅ | Chalkboard question, glasses removal, betting regulars identified |

**Café Existenz: Where the coffee is excellent, the judgment is complimentary, and every asset exists so a tourist can lose a debate he never agreed to enter.**
