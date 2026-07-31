# Voetgangerstunnel - Complete PNG Asset Requirements

*Artist Reference Document for the Underground Labyrinth of Wrong Turns*

**Location ID**: `shamsterdam_voetgangerstunnel_01`  
**Priority**: MEDIUM (Bike Crossing Shortcut, Navigation Puzzle, Comedy Reveal Location)  
**Total Sheets Required**: 9  
**Mobile Optimization**: Standard (60 FPS, simple geometry)

---

## Art Direction Summary

### Visual Identity
This is **1970s Dutch infrastructure brutalism**—clean, functional, and utterly confusing. White tile walls with meaningless color-coded stripes. Fluorescent lighting that occasionally flickers. Signs that point everywhere and nowhere. A time capsule of Amsterdam's underground that hasn't been updated since before the Euro.

### Key Visual Themes
- **Functional Confusion**: Everything looks helpful but isn't
- **Dutch Efficiency (Ironic)**: Clean design that somehow leads you astray
- **Time Capsule**: Ads from 2003, pre-Euro references, vintage infrastructure
- **Liminal Space Energy**: Endless corridors, flickering lights, eternal busker

### Color Palette

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

## SHEET 1: Tunnel Tileset
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
- **Tip Jar**: Willem's hat with €2.47

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

## SHEET 2: Henk the Security Guard
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

## SHEET 3: Marloes the Map Vendor
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

## SHEET 4: Willem the Eternal Busker
**Filename**: `npc_willem_busker.png`  
**Dimensions**: 192 × 256 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Instrument**: Ancient accordion, well-worn
- **Clothing**: Indeterminate decade (could be 1970s, could be 1990s)
- **Props**:
  - Hat on ground with exactly €2.47
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

## SHEET 5: Lost Tourist Variants
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

## SHEET 6: Mevrouw Jansen
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

## SHEET 7: Effects and Particles
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

## SHEET 8: UI Elements
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

## SHEET 9: Exit Reveals
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

## Lighting Requirements

### Underground Baseline
- Harsh fluorescent lighting
- Yellow/white cast (#FFFACD)
- Occasional flicker in specific zones

### Zone Variations

**Entrance Hall**
- Brightest (0.8 intensity)
- Surface light bleeding in
- Hopeful but false

**Intersection of Doubt**
- Standard (0.7 intensity)
- No flicker
- Functional, confusing

**Long Corridor**
- Dimmer (0.6 intensity)
- Flicker probability 10%
- Endless perspective
- Willem's accordion creates audio landmark

**Wrong Turn Zone**
- Dimmest (0.5 intensity)
- Flicker probability 15%
- Uncertainty atmosphere
- Exit preview lighting varies

**Correct Exit**
- Daylight blend
- Warm natural light from above
- Triumph glow

### Emergency Signs
- Always lit (green #00FF00)
- Subtle glow effect
- Reliable navigation secret

---

## Animation Frame Rates

| Element | FPS | Notes |
|---------|-----|-------|
| Fluorescent flicker | 8 | Random trigger |
| NPC idle | 0.25-0.5 | Very slow, underground lethargy |
| NPC active | 1-2 | When interacting |
| Willem accordion | 2 | Constant rhythm |
| Ghost effect | 0.3 | Very slow, uncertain |
| Debuff indicators | 2-3 | Visible but not distracting |

---

## Perspective and Endless Corridor Effect

### Long Corridor Visual Trick
- Use forced perspective scaling
- Tiles get smaller toward vanishing point
- Willem appears same size despite distance (unsettling)
- Creates "endless" feeling despite 150m actual length

### Intersection Confusion
- All five corridors use identical tile palette
- No distinguishing landmarks
- All signs point vaguely same direction
- Audio cues are the only reliable guide

---

## Social Media Viral Moments

### Key Screenshot Opportunities
1. **Red Light Emergence**: Player appearing between windows
2. **Henk Pointing Wrong**: Security guard confident, arrow clearly wrong
3. **Willem the Eternal**: Same busker, same spot, every time
4. **Wall Map Fail**: "You Are Here" dot in wrong location
5. **Graffiti Wisdom**: "DON'T FOLLOW HENK"

### TikTok Potential
- "POV: You took the 'shortcut'"
- Navigation fail compilations
- "Is Willem a ghost?" investigation
- Speedrun attempts

---

## Technical Specifications

### File Format
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **Resolution**: 72 DPI
- **Compression**: Lossless

### Mobile Optimization
- Simple corridor geometry
- Baked lighting with dynamic flicker only
- Audio-based navigation reduces visual load
- Quick zone transitions (preload adjacent)
- 60 FPS target
- <40MB memory budget
- <35 draw calls

---

## Cross-Reference: Related Assets

### Connects To
- Bike Crossing assets (entry point)
- Red Light District assets (wrong exit)
- Coffeeshop Quarter assets (wrong exit)
- FEBO Automat assets (hidden exit)

### Unique to This Location
- All tunnel-specific tiles
- Navigation signage
- Henk, Marloes, Willem NPCs
- Lost Tourist variants
- Wrong exit reveal scenes

---

**END OF ASSET REQUIREMENTS**

*Voetgangerstunnel: Where "shortcut" is Dutch for "you're about to be very confused and possibly very embarrassed." Follow the green signs. Ignore Henk. Tip Willem. Good luck.*
