# Voetgangerstunnel - Complete PNG Asset Requirements

*Artist Reference Document for the Underground Labyrinth of Wrong Turns*

**Location ID**: `shamsterdam_voetgangerstunnel_01`  
**Priority**: MEDIUM (Bike Crossing Shortcut, Navigation Puzzle, Comedy Reveal Location)  
**Total Sheets Required**: 9  
**Mobile Optimization**: Standard (60 FPS, simple geometry)

---

## 📋 Overview
The Voetgangerstunnel ("Pedestrian Tunnel") is the underground passage network beneath the Central Bike Crossing — a 1970s Dutch brutalist labyrinth that promises safety from the Bicycle Thunderdome above and delivers navigation confusion instead, most infamously emerging directly between two red-lit windows in Roodelicht Row. This document specifies every PNG asset for the tunnel: the tileset with its meaningless color stripes and lying signage, four NPC sheets (Henk, Marloes, Willem, the Lost Tourists), Mevrouw Jansen, effects, navigation UI, and the wrong-exit reveal scenes. Its satirical essence in a sentence: Dutch "helpful" signage that assumes you already know where you're going.

**Location ID:** `shamsterdam_voetgangerstunnel_01`
**Theme:** Amsterdam's genuinely confusing underground tunnel systems; "helpful" signage as tourist filter
**Zone:** Central / Underground Network
**Hours:** Always accessible (24 hours; busier during rush hours, eerier at night)
**Primary Function:** Navigation hazard / transition zone / ironic shortcut — probability-based navigation puzzle with five zones, wrong-exit comedy reveals, item vendor, hint NPCs, and hidden quests ("The Eternal Busker", "Red Light Discovery", "FEBO Shortcut")

---

## 🎨 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Tunnel White | #F0F0F0 | Wall tiles |
| Stripe Blue | #003DA5 | Navigation stripe (meaningless) |
| Stripe Orange | #FF6600 | Navigation stripe (also meaningless) |
| Stripe Yellow | #FFD700 | Navigation stripe (definitely meaningless) |
| Floor Speckle | #8B8B8B | Terrazzo base |
| Fluorescent Yellow | #FFFACD | Harsh overhead lighting |
| Emergency Green | #00FF00 | Exit signs (the only reliable ones) |
| Graffiti Various | Mixed | Hidden hints on walls |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/voetgangerstunnel/
├── environment/
│   ├── voetgangerstunnel_tileset.png
│   └── tunnel_exit_reveals.png
├── npcs/
│   ├── npc_henk_security.png
│   ├── npc_marloes_mapvendor.png
│   ├── npc_willem_busker.png
│   ├── npc_lost_tourist_variants.png
│   └── npc_mevrouw_jansen.png
├── effects/
│   └── tunnel_effects.png
└── ui/
    └── tunnel_ui.png
```

---

## 🚇 Sprite Sheet 1: Tunnel Tileset
**Filename**: `voetgangerstunnel_tileset.png`  
**Dimensions**: 1024 × 512 pixels  
**Tile Size**: 32 × 32 pixels

### Walls (Row 0)
- **White Tile Clean**: Pristine subway tile
- **White Tile Worn**: Slightly yellowed, decades of use
- **White Tile Grout**: Showing grout lines
- **Stripe Blue**: Blue navigation stripe (3 tiles wide)
- **Stripe Orange**: Orange navigation stripe
- **Stripe Yellow**: Yellow navigation stripe
- **Wall Corner**: Inside corner tile
- **Wall Intersection**: Where corridors meet

### Floor (Row 1)
- **Terrazzo Base**: Speckled grey floor
- **Terrazzo Worn Path**: Darker from foot traffic (shows actual routes)
- **Tile Line Blue**: Blue floor tiles (separate from wall stripe)
- **Tile Line Orange**: Orange floor tiles
- **Tile Line Yellow**: Yellow floor tiles
- **Floor Grate**: Ventilation grate
- **Stairs Down**: Descending into tunnel
- **Stairs Up**: Ascending to surface

### Ceiling (Row 2)
- **Fluorescent Fixture**: Standard tube light (2 tiles wide)
- **Fluorescent Flickering**: Animated flicker variant
- **Exposed Pipes**: Infrastructure visible above
- **Speaker Grille**: Announcement system (never used)
- **Ventilation Duct**: Air circulation
- **Emergency Light**: Battery-powered backup

### Signage (Row 3)
- **Sign Centraal Station**: Direction sign (2 tiles, may be lying)
- **Sign Museum Plein**: Direction sign (may also be lying)
- **Sign Centrum**: Vaguest possible direction
- **Sign Emergency Exit**: Green "Nooduitgang" (actually reliable)
- **Arrow Left**: Directional arrow
- **Arrow Right**: Directional arrow

### Interactive Objects (Rows 4-5)
- **Wall Map Frame**: Large map display (2×2 tiles)
- **You Are Here Dot**: Red dot (wrong location)
- **Kiosk Window**: Marloes's service window (2 tiles)
- **Security Booth**: Henk's station (2 tiles)
- **Tip Jar**: Willem's hat with 2 Sovs

### Graffiti (Row 6) - Flashlight-revealed
- **"STATION →"**: With scratched-over reversed arrow
- **"DON'T FOLLOW HENK"**: Warning graffiti
- **"Exit 7 = Red Light LOL"**: Helpful vandalism
- **"Willem knows"**: Cryptic hint

### Vintage Advertisements (Row 7)
- **Guilder Exchange**: Pre-Euro currency ad
- **Nokia Phone**: "The future of communication"
- **Travel to Publandia**: "Exotic destination!"
- **Film Development**: "Same day service!"

*Art Note*: All ads should look sun-faded and dated. These are time capsules from 2003 or earlier.

---

## 💂 Sprite Sheet 2: Henk the Security Guard
**Filename**: `npc_henk_security.png`  
**Dimensions**: 192 × 256 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Uniform**: Generic security guard uniform, clearly too tight
- **Expression**: Eyes of someone who stopped caring in 1997
- **Props**: 
  - Empty coffee cup (always empty)
  - Newspaper with unfinished crossword
  - Small booth/desk
- **Posture**: Permanently seated unless paid for escort

### Animation States (4 rows)
- **Row 0: Sitting Bored** (2 frames) - Minimal movement, staring at nothing
- **Row 1: Standing Slowly** (4 frames) - Takes forever to get up
- **Row 2: Pointing Confidently** (3 frames) - Points in random direction with full confidence
- **Row 3: Shrugging** (2 frames) - "Strange, it was there yesterday"

*Art Note*: Henk should look like he's been down here so long he's forgotten what the surface looks like.

---

## 🗺️ Sprite Sheet 3: Marloes the Map Vendor
**Filename**: `npc_marloes_mapvendor.png`  
**Dimensions**: 192 × 192 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Setting**: Tiny kiosk built into wall
- **Age**: Middle-aged, practical Dutch woman
- **Expression**: "I know you're lost" permanent look
- **Props**:
  - Reading glasses
  - Maps everywhere
  - Guidebooks
  - Batteries (for flashlights)
- **Clothing**: Sensible, warm (it's cold underground)

### Animation States (3 rows)
- **Row 0: Idle in Kiosk** (2 frames) - Subtle movement behind window
- **Row 1: Handing Item** (3 frames) - Passing map through window
- **Row 2: Disappointed Sigh** (2 frames) - When tourist ignores advice

*Art Note*: Marloes is the only genuinely helpful person in the tunnel, and she knows her advice will be ignored.

---

## 🪗 Sprite Sheet 4: Willem the Eternal Busker
**Filename**: `npc_willem_busker.png`  
**Dimensions**: 192 × 256 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Instrument**: Ancient accordion, well-worn
- **Clothing**: Indeterminate decade (could be 1970s, could be 1990s)
- **Props**:
  - Hat on ground with exactly 2 Sovs
  - Maybe a small stool
- **Expression**: Serene, timeless, possibly not alive
- **Aura**: Slight transparency effect available for ghost moments

### Animation States (4 rows)
- **Row 0: Playing Accordion** (4 frames) - Continuous playing loop
- **Row 1: Looking Up Mysterious** (2 frames) - When tipped, looks at player
- **Row 2: Pauses Playing** (2 frames) - Stops to speak
- **Row 3: Disappear/Reappear** (3 frames) - Ghost moment, very subtle

### Special Effect
- **Ghost Flicker**: Transparency pulse for third tip revelation
- Should be subtle—is he a ghost or just old?

*Art Note*: Willem is always in the same spot. Always. He may have been here since the tunnel opened. He may still be here when it closes.

---

## 🧳 Sprite Sheet 5: Lost Tourist Variants
**Filename**: `npc_lost_tourist_variants.png`  
**Dimensions**: 288 × 192 pixels  
**Sprite Size**: 48 × 64 pixels

### Variant Designs (3 columns)

**Column 0: American Tourist**
- Baseball cap (sports team)
- Cargo shorts
- Fanny pack
- Map held upside down
- Expression: Growing desperation

**Column 1: British Tourist**
- Football jersey
- Somehow still holding a pint glass
- Sunburned despite being underground
- Expression: Bewildered frustration

**Column 2: Australian Tourist**
- Thongs (flip-flops)
- Tank top
- Severe sunburn
- Expression: "No worries" but worried

### Animation States (3 rows, shared)
- **Row 0: Wandering Confused** (4 frames) - Aimless walking
- **Row 1: Staring at Map** (2 frames) - Turning map various directions
- **Row 2: Relieved at Help** (2 frames) - When player offers assistance

*Art Note*: Each lost tourist should be a new variant each visit. They all share the same animation rig.

---

## 🪟 Sprite Sheet 6: Mevrouw Jansen
**Filename**: `npc_mevrouw_jansen.png`  
**Dimensions**: 144 × 128 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Type**: Elderly Dutch woman
- **Setting**: Apartment window ABOVE Red Light District
- **Note**: NOT a worker—just a resident who's seen everything
- **Props**:
  - Watering can for window plants
  - Lace curtains
- **Expression**: Permanent disappointed judgment

### Animation States (2 rows)
- **Row 0: Watering Plants** (3 frames) - Casual plant care
- **Row 1: Looking Down Judging** (2 frames) - Watching confused tourist emerge

*Art Note*: She appears ONLY when player exits tunnel at wrong Red Light exit. She's seen this happen thousands of times.

---

## ✨ Sprite Sheet 7: Effects and Particles
**Filename**: `tunnel_effects.png`  
**Dimensions**: 256 × 256 pixels

### Effects

**Fluorescent Flicker** (64×16, 4 frames)
- Light tube flickering effect
- Yellow/white variation
- Used in Long Corridor and Wrong Turn zones

**Question Mark Debuff** (24×24, 3 frames)
- Animated question marks above head
- "Tunnel Confusion" status indicator
- Yellow/gold color

**Correct Direction Chime** (32×32, 4 frames)
- Subtle green sparkle
- Positive navigation feedback
- Barely visible (subconscious)

**Wrong Direction Pulse** (32×32, 3 frames)
- Subtle orange/red pulse
- Negative navigation feedback
- Also barely visible

**Ghost Flicker** (48×64, 3 frames)
- Willem transparency effect
- Very subtle—uncertainty is key
- Used for third tip revelation

**Emergency Glow** (32×32, 2 frames)
- Green glow around emergency signs
- Indicates reliability

---

## 🧭 Sprite Sheet 8: UI Elements
**Filename**: `tunnel_ui.png`  
**Dimensions**: 256 × 128 pixels

### Interface Elements

**Navigation Choice Prompt** (200×40)
- "Which direction?" interface
- Shows available options

**Direction Options** (150×30)
- List of corridor choices
- Sign text and icons

**Time Underground Indicator** (100×20)
- Clock/timer showing time spent
- Warning as Underground Dread approaches

**Wrong Turn Counter** (80×20)
- Tracks navigation failures
- Affects Tunnel Confusion debuff

---

## 🚪 Sprite Sheet 9: Exit Reveals
**Filename**: `tunnel_exit_reveals.png`  
**Dimensions**: 512 × 256 pixels

### Wrong Exit Scenes

**Red Light Emergence** (256×128)
- POV: Stairs emerging between two red-lit windows
- Player's feet visible on steps
- Red glow from both sides
- Comedy: Most embarrassing possible location
- Mevrouw Jansen visible in window above

**Coffeeshop Emergence** (128×128)
- Storage room interior
- Door bursting open
- Hazy atmosphere
- Unsurprised staff member visible

**Canal Emergence** (128×128)
- Narrow walkway, no railing
- Canal water visible
- Bicycle zooming past (blur)
- Surface chaos immediate

**FEBO Emergence** (128×128)
- Behind automat heating unit
- Warm glow
- 3 AM atmosphere regardless of time
- Kroket visible through automat glass

**Correct Exit** (128×128)
- Daylight bleeding down stairs
- Surface visible above
- Triumph (hollow)
- Destination signage visible

---

## 🎬 Animation Specifications

*Sprite positions within sheets follow the row layouts specified per sheet above; pixel coordinates set at sheet layout.*

### Fluorescent Flicker (Sheets 1 & 7):
- **Duration:** 0.5 seconds per burst (8 FPS, random trigger)
- **Frames:** 4
- **Pattern:** Random trigger → flicker burst → return to steady
- **Trigger:** Random, 10% probability in Long Corridor, 15% in Wrong Turn Zone
- **Purpose:** Liminal-space unease; zone identity
- **Audio Sync:** Fluorescent hum dips on flicker
- **Mobile Optimization:** Only dynamic lighting element — all other lighting baked

### Willem's Accordion (Sheet 4):
- **Duration:** 2 seconds per cycle (2 FPS, constant rhythm)
- **Frames:** 4
- **Pattern:** Frame 1 → 4 → loop, continuous
- **Trigger:** Constant — Willem never stops (except Pauses Playing row on tip/speech)
- **Purpose:** Audio-visual landmark: if you see/hear the accordion, you're in Zone 3
- **Audio Sync:** Dutch folk tune loop locked to frame cycle
- **Mobile Optimization:** None needed

### Ghost Flicker (Sheets 4 & 7):
- **Duration:** ~3 seconds (0.3 FPS, very slow, uncertain)
- **Frames:** 3 (transparency pulse)
- **Pattern:** Fade → one-second disappear → reappear, played once
- **Trigger:** Third 5 Sovs tip revelation ("The Eternal Busker" hidden quest)
- **Purpose:** Is he a ghost or just old? Uncertainty is the point — keep it subtle
- **Audio Sync:** Accordion continues uninterrupted (the unsettling detail)
- **Mobile Optimization:** Simple alpha modulation, no shader required

### Navigation Feedback (Sheet 7):
- **Duration:** ~1 second each (Correct Direction Chime 4 frames, Wrong Direction Pulse 3 frames)
- **Frames:** 3-4
- **Pattern:** Single play on navigation decision, barely visible
- **Trigger:** Player commits to a corridor choice
- **Purpose:** Subconscious feedback — must NOT clearly telegraph outcomes
- **Audio Sync:** Subtle positive chime / slight dissonance, matched to sprite
- **Mobile Optimization:** None needed

### Question Mark Debuff (Sheet 7):
- **Duration:** 1-1.5 second loop (2-3 FPS, visible but not distracting)
- **Frames:** 3
- **Pattern:** Loop above player head while debuffed
- **Trigger:** "Tunnel Confusion" status (multiple wrong turns in single visit)
- **Purpose:** Status readability
- **Audio Sync:** None
- **Mobile Optimization:** None needed

### NPC Idle/Active Loops (Sheets 2-6):
- **Duration:** 2-4 seconds idle (0.25-0.5 FPS, underground lethargy); 0.5-1 second active states (1-2 FPS)
- **Frames:** 2-4 per state row
- **Pattern:** Idle loop → interaction state → return to idle
- **Trigger:** Idle constant; active on dialogue/service (Henk Pointing Confidently, Marloes Handing Item, tourists Relieved at Help, Mevrouw Jansen Looking Down Judging)
- **Purpose:** Everyone underground moves slowly — lethargy is characterization
- **Audio Sync:** Marloes's sigh audio on Disappointed Sigh row
- **Mobile Optimization:** None needed

### Emergency Glow (Sheet 7):
- **Duration:** 2-second gentle pulse
- **Frames:** 2
- **Pattern:** Soft loop, always active
- **Trigger:** Constant on all "Nooduitgang" signs
- **Purpose:** The hidden navigation secret — the only reliable signs glow green
- **Audio Sync:** None
- **Mobile Optimization:** None needed

### Animation Frame Rates

| Element | FPS | Notes |
|---------|-----|-------|
| Fluorescent flicker | 8 | Random trigger |
| NPC idle | 0.25-0.5 | Very slow, underground lethargy |
| NPC active | 1-2 | When interacting |
| Willem accordion | 2 | Constant rhythm |
| Ghost effect | 0.3 | Very slow, uncertain |
| Debuff indicators | 2-3 | Visible but not distracting |

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Emergency sign high-contrast variant | set at sheet layout | 32×32 | Bold-outline "Nooduitgang" sign — the reliable-route cue must survive high-contrast mode |
| Corridor edge outlines | set at sheet layout | 32×32 tiles | High-contrast wall/floor boundary tiles for the five-corridor Intersection of Doubt |
| NPC interaction highlight | set at sheet layout | 48×64 | Outline variant marking Henk, Marloes, Willem, and lost tourists as interactive |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static fluorescent tile | Sheet 1 (Fluorescent Fixture) | 64×32 | Reduced-motion mode swaps Fluorescent Flickering for the steady fixture tile |
| Steady emergency glow | set at sheet layout | 32×32 | Non-pulsing constant green glow variant |
| Ghost fade (reduced) | set at sheet layout | 48×64 | Cross-fade variant without flicker strobing for Willem's revelation |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Directional sound icons | set at sheet layout | 24×24 | Visual icons per corridor mirroring the directional audio clue system: tram icon (→ station), music-note bass icon (→ Coffeeshop Quarter), water-drop icon (→ canal), silence/mute icon (→ Red Light, eerily quiet) |
| Accordion note marker | set at sheet layout | 24×24 | Floating note sprite marking Willem's audio landmark for Zone 3 |
| Correct Direction Chime | Sheet 7 | 32×32 | Visual mirror of the positive navigation chime |
| Wrong Direction Pulse | Sheet 7 | 32×32 | Visual mirror of the navigation dissonance cue |

### Colorblind Considerations:
- The blue/orange/yellow stripe joke is color-based by design — stripes must ALSO carry distinct end-cap patterns (the joke is that they're meaningless, not that they're invisible)
- Emergency reliability is coded green + distinct sign shape and glow, never color alone
- Navigation Choice Prompt options use text + icons, not color coding
- Touch zones minimum 44px for all navigation choices and NPC interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC (fallback PVRTC 4BPP); tileset signage and exit reveals need higher quality (readable text and scene detail)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for exit reveal scenes (detail-critical comedy shots)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| tunnel_environment | tileset, exit reveals | 1024x1024 |
| tunnel_characters | Henk, Marloes, Willem, lost tourists, Mevrouw Jansen | 1024x1024 |
| tunnel_effects | effects, UI | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full flicker effects, ghost transparency, all ambient NPC loops |
| Medium | Reduced flicker frequency, simplified navigation feedback sparkles |
| Low | Baked lighting only, static NPCs outside dialogue, no ambient particles (baseline LOD level 1 per core data) |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** Under 35
- **Memory Footprint:** Under 40 MB
- **Particle Limit:** 30 (fluorescent flicker, dust)

### Performance Notes:
- Simple corridor geometry; baked lighting with dynamic flicker only
- Audio-based navigation reduces visual load
- Quick zone transitions — preload adjacent zones
- Forced-perspective Long Corridor is a static visual trick, not real geometry

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (corridors), AnimatedSprite2D (NPCs, effects), CPUParticles2D (dust — not GPU), CanvasLayer (navigation UI), CanvasModulate for zone lighting tiers
- Special systems: probability-based navigation resolver (exit odds modified by sober/contact-high/space-cake/canal-confusion/map/guide/memory stacks), dynamic signage that changes between visits, five-zone transition triggers, flashlight-gated graffiti layer, Willem tip counter (3× 5 Sovs for ghost reveal)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Willem accordion frames | Dutch folk tune loop | Locked to 4-frame cycle, constant from Zone 3 |
| Corridor sound icons | Directional audio (tram / bass / water / silence) | While standing at Intersection of Doubt |
| Correct Direction Chime | Subtle positive chime | On correct corridor commit |
| Wrong Direction Pulse | Slight dissonance | On wrong corridor commit |
| Wrong exit reveal scenes | Record scratch / "dun dun DUN"; Red Light: distant bass, sudden silence, window taps | On emergence scene display |
| Fluorescent Flickering tile | Hum dip | On flicker burst |
| Marloes Disappointed Sigh row | Sigh audio | When player ignores advice |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Red Light Discovery | Red Light Emergence scene, Mevrouw Jansen sheet | First accidental Roodelicht emergence; "Scenic Route" achievement |
| The Eternal Busker | Willem sheet, Ghost Flicker, tip jar tile | Tip 5 Sovs three visits; "Willem's Friend" + accordion cosmetic |
| FEBO Shortcut Discovery | FEBO Emergence scene | Hidden entrance behind heating unit; "Back Door Regular" |
| Stay Away Campaign | Tileset (corridor props) | Pamphlet #4 found in tunnel |
| Tour Guide (achievement) | Lost Tourist variants (Relieved at Help row) | Escort a lost tourist to correct exit |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Central Bike Crossing | Stairs Down tile, entrance hall | Primary entrance (unlocked after 10 crossings or escort knowledge) |
| Centraal Chaos | Correct Exit scene | Intended exit (40% base probability) |
| Museum Mile | Correct Exit scene, parking entrance | Secondary intended exit / entry point |
| Roodelicht Row | Red Light Emergence scene | Infamous wrong exit (35%); no tunnel re-entry |
| Coffeeshop Quarter | Coffeeshop Emergence scene | Wrong exit into storage room (15%) |
| Canal Ring Promenade | Canal Emergence scene | Surface wrong exit with bicycle near-miss |
| FEBO Automat | FEBO Emergence scene | Hidden shortcut, 3 AM vibes always |

### Cross-Reference: Related Assets
- **Connects to**: Bike Crossing assets (entry point), Red Light District assets (wrong exit), Coffeeshop Quarter assets (wrong exit), FEBO Automat assets (hidden exit)
- **Unique to this location**: All tunnel-specific tiles, navigation signage, Henk/Marloes/Willem NPCs, Lost Tourist variants, wrong exit reveal scenes

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "1970s Dutch infrastructure brutalism — clean, functional, and utterly confusing"
- **Color Mood:** Tunnel white and terrazzo grey under harsh fluorescent yellow; the only warmth is the lying color stripes and the reliable emergency green
- **Lighting:** See Lighting Requirements below — zone-tiered fluorescent intensity from hopeful entrance to dim wrong-turn uncertainty
- **Texture:** Clean but worn — decades of use, yellowed tiles, worn terrazzo paths that show where people actually walk

### Visual Identity
This is **1970s Dutch infrastructure brutalism**—clean, functional, and utterly confusing. White tile walls with meaningless color-coded stripes. Fluorescent lighting that occasionally flickers. Signs that point everywhere and nowhere. A time capsule of Amsterdam's underground that hasn't been updated since before the Euro.

### Key Visual Themes
- **Functional Confusion**: Everything looks helpful but isn't
- **Dutch Efficiency (Ironic)**: Clean design that somehow leads you astray
- **Time Capsule**: Ads from 2003, pre-Euro references, vintage infrastructure
- **Liminal Space Energy**: Endless corridors, flickering lights, eternal busker

### Lighting Requirements

**Underground Baseline**
- Harsh fluorescent lighting
- Yellow/white cast (#FFFACD)
- Occasional flicker in specific zones

**Zone Variations**

*Entrance Hall*
- Brightest (0.8 intensity)
- Surface light bleeding in
- Hopeful but false

*Intersection of Doubt*
- Standard (0.7 intensity)
- No flicker
- Functional, confusing

*Long Corridor*
- Dimmer (0.6 intensity)
- Flicker probability 10%
- Endless perspective
- Willem's accordion creates audio landmark

*Wrong Turn Zone*
- Dimmest (0.5 intensity)
- Flicker probability 15%
- Uncertainty atmosphere
- Exit preview lighting varies

*Correct Exit*
- Daylight blend
- Warm natural light from above
- Triumph glow

**Emergency Signs**
- Always lit (green #00FF00)
- Subtle glow effect
- Reliable navigation secret

### Perspective and Endless Corridor Effect

**Long Corridor Visual Trick**
- Use forced perspective scaling
- Tiles get smaller toward vanishing point
- Willem appears same size despite distance (unsettling)
- Creates "endless" feeling despite 150m actual length

**Intersection Confusion**
- All five corridors use identical tile palette
- No distinguishing landmarks
- All signs point vaguely same direction
- Audio cues are the only reliable guide

### Environmental Storytelling:
- Worn terrazzo paths reveal the routes people actually take — contradicting every sign
- Vintage ads (guilder exchange, Nokia, film development) date the tunnel to a pre-Euro time capsule
- Flashlight-revealed graffiti is the tunnel's true folk knowledge: "DON'T FOLLOW HENK", "Willem knows"
- The wall map's wrong "You Are Here" dot tells the whole satirical premise in one prop

### Character Integration Notes:
- All NPCs are fixtures, not wanderers: Henk at his booth (Zone 2), Marloes in her kiosk (Zone 1), Willem always in the same spot (Zone 3)
- Lost Tourists rotate variants per visit on a shared animation rig
- Mevrouw Jansen renders only in the Red Light Emergence scene, window above
- Willem's optional transparency must stay ambiguous — ghost or just old, never confirmed

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Red Light Emergence**: Player appearing between windows
2. **Henk Pointing Wrong**: Security guard confident, arrow clearly wrong
3. **Willem the Eternal**: Same busker, same spot, every time
4. **Wall Map Fail**: "You Are Here" dot in wrong location
5. **Graffiti Wisdom**: "DON'T FOLLOW HENK"

### Quote Potential:
- "You wanted the station, didn't you? Everyone wants the station."
- "Strange, it was there yesterday."
- "The tunnel got you too?"
- "I've been here since... hmm. What year is it?"
- "The sign said Centraal Station. I've seen it four times. From different angles."

### TikTok Potential
- "POV: You took the 'shortcut'"
- Navigation fail compilations
- "Is Willem a ghost?" investigation
- Speedrun attempts

---

## 📋 Required PNG Files (9 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | voetgangerstunnel_tileset.png | 1024x512 |
| 2 | npc_henk_security.png | 192x256 |
| 3 | npc_marloes_mapvendor.png | 192x192 |
| 4 | npc_willem_busker.png | 192x256 |
| 5 | npc_lost_tourist_variants.png | 288x192 |
| 6 | npc_mevrouw_jansen.png | 144x128 |
| 7 | tunnel_effects.png | 256x256 |
| 8 | tunnel_ui.png | 256x128 |
| 9 | tunnel_exit_reveals.png | 512x256 |

**Total Estimated Memory:** ~40 MB maximum (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `voetgangerstunnel_tileset.png` (1024x512)
- [ ] `npc_henk_security.png` (192x256)
- [ ] `npc_marloes_mapvendor.png` (192x192)
- [ ] `npc_willem_busker.png` (192x256)
- [ ] `npc_lost_tourist_variants.png` (288x192)
- [ ] `npc_mevrouw_jansen.png` (144x128)
- [ ] `tunnel_effects.png` (256x256)
- [ ] `tunnel_ui.png` (256x128)
- [ ] `tunnel_exit_reveals.png` (512x256)

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
- **Documentation:** Animation timing reference sheet + forced-perspective corridor layout guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: wrong "You Are Here" dot, lying signage, Red Light Emergence framing, Willem's unchanging 2 Sovs
- [ ] Accessibility visual alternatives included for all audio cues (directional corridor audio, accordion landmark, navigation chimes)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (helpful-looking design that misleads)
- [ ] Hidden areas/interactions have discoverable visual cues (graffiti under flashlight, FEBO entrance, emergency sign secret)
- [ ] Mobile performance optimized (baked lighting, CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (stripe end-caps, emergency sign shape)
- [ ] Social media viral potential maximized in composition choices (Red Light Emergence POV framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam only; Dutch signage ("Nooduitgang", "Centraal") in-world |
| Cultural Specificity | ✅ | Dutch underground infrastructure, pre-Euro time capsule, "helpful" signage culture |
| Satirical Targets Appropriate | ✅ | Tourist navigation struggles — Red Light integration is embarrassment, not exploitation |
| Seedy Underbelly Present | ✅ | Red Light emergence, coffeeshop storage room, tourist-priced "help" economy |
| Gameplay Value Established | ✅ | Probability navigation puzzle, 5 zones, hidden quests, shortcut economy |
| Technical Feasibility | ✅ | Baked lighting, simple corridor geometry, audio-led navigation documented |
| Mobile Performance Budget | ✅ | 60 FPS, <35 draw calls, <40 MB, 30 particles |
| Accessibility Features | ✅ | Visual mirrors for all directional audio cues, reduced-motion variants, 44px touch zones |
| No Crypto Elements | ✅ | All transactions in Sovs (guilder ad is period set-dressing only) |
| Social Media Integration | ✅ | 5 screenshot moments + TikTok formats identified |

---

**END OF ASSET REQUIREMENTS**

*Voetgangerstunnel: Where "shortcut" is Dutch for "you're about to be very confused and possibly very embarrassed." Follow the green signs. Ignore Henk. Tip Willem. Good luck.*
