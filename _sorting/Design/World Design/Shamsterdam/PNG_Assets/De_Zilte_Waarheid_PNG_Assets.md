# De Zilte Waarheid - Complete PNG Asset Requirements

## 📋 Overview
De Zilte Waarheid ("The Salty Truth") is a pristine white-and-blue herring cart in the Harbor District where tourists discover that "wanting an authentic experience" and "being willing to tilt your head back and lower a raw fish into your mouth in front of strangers" are two very different things. This document specifies every PNG asset for the stand: the harbor environment, the stand and display case, Visser Dirk and Assistant Evi, the atmospheric customer gallery, seagull Hendrik, the full traditional eating method animation set, and the UI for method choice and status effects. Its satirical essence in a sentence: the fish doesn't judge — the locals, the seagulls, and the camera do.

**Location ID:** `shamsterdam_harbor_herring_stand_01`
**Theme:** Dutch haring tradition as a public vulnerability test; tourist bravado vs. raw fish reality
**Zone:** Harbor District, near the old fish market
**Hours:** 10 AM - 6 PM (fresh fish hours, tradition demands)
**Primary Function:** Street food vendor / cultural initiation rite / dignity checkpoint — traditional-method eating challenge, Bravado economy, status effects (Fish Breath, Onion Aura, Courage Buff), seagull hazard system

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| North Sea Blue | #4A7C99 | Cart trim, water, method signage |
| Fish Silver | #C0C0C0 | Herring skin, ice glint, display case |
| Harbor Gray | #708090 | Quay stone, background boats, sky haze |
| Onion White | #F5F5F5 | Cart paint, onion bowls, napkins |
| Ice Blue | #D6EEF5 | Crushed ice bed, cold highlights |
| Warning Red | #B22222 | Price board accents, seagull threat indicator |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/de_zilte_waarheid/
├── environment/
│   ├── harbor_background.png
│   └── herring_stand_structures.png
├── objects/
│   └── herring_food_items.png
├── npcs/
│   ├── npc_dirk_evi.png
│   └── npc_harbor_customers.png
├── effects/
│   └── eating_method_animations.png
└── ui/
    └── herring_ui_effects.png
```

---

## 🌊 Sprite Sheet 1: Harbor Background
**File:** `harbor_background.png`
**Dimensions:** 2048x1024 pixels
**Color Palette:** #708090, #4A7C99, #D6EEF5

### Background Layers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Harbor District Backdrop | (0, 0) | 1920x512 | Working waterfront: quay, fish market facade, masts, gray-blue sky |
| Distant Fishing Boats | (0, 512) | 512x192 | Parallax layer: moored boats, rigging, gull silhouettes |
| Water Surface Strip A | (512, 512) | 512x96 | Tileable canal-harbor water, calm state |
| Water Surface Strip B | (512, 608) | 512x96 | Tileable water, breeze ripple state (2-frame swap with Strip A) |
| Quay Stone Tiles | (1024, 512) | 256x128 | Tileable wet cobble/quay edge, 32x32 grid |
| Seagull Perch (Lamp Post) | (1280, 512) | 128x96 | Hendrik's surveillance post, guano-weathered |
| Sea Mist Overlay | (1408, 512) | 512x192 | Soft alpha mist band for harbor atmosphere |
| Sky Haze Gradient | (0, 704) | 1024x128 | Overlay strip for morning/late-afternoon light shift |
| Market Crates & Nets | (1024, 704) | 384x192 | Set dressing props: fish crates, coiled nets, buoys |
| Gull Silhouette Flock | (1408, 704) | 256x128 | 4 static distant gulls (64x64 each) for background layer |

### Technical Notes:
- Backdrop drawn for 1920-wide viewport; parallax boats scroll at 0.3x camera speed
- Water strips swap at 0.8s intervals (simplified water per mobile optimization note in profile)
- Sea Mist Overlay rendered at 20% alpha, additive OFF (plain alpha blend)
- Background gulls are STATIC on mobile (profile requirement)

---

## 🐟 Sprite Sheet 2: The Stand & Service Stations
**File:** `herring_stand_structures.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #F5F5F5, #4A7C99, #C0C0C0

### Stand Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Herring Cart Full | (0, 0) | 384x384 | White-painted wood, blue trim, impeccably clean, "Haring Sinds 1952" signage |
| Display Case (Fish on Ice) | (384, 0) | 256x192 | Glass case, silver fillets in neat rows on crushed ice, parsley garnish |
| Display Case (Half Empty) | (384, 192) | 256x192 | Late-day state: gaps in the rows, ice melting slightly |
| Chopping Station | (640, 0) | 128x128 | Worn block, knife, decades of efficiency in the scarring |
| Method Illustration Sign | (768, 0) | 192x256 | "THE SHAMSTERDAM WAY" — Grip / Tilt / Lower / Repeat, illustrated |
| Price Board | (768, 256) | 192x128 | "Haring €4 / Met Uitjes €4.50 / De Waarheid Platter €8" + raw-fish warning |

### Service Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Onion Bowls | (640, 128) | 96x64 | Diced raw white onion, the traditional accompaniment |
| Pickle Selection | (640, 192) | 96x64 | Augurken, small, sour, palate cleansers |
| Napkin Dispenser | (640, 256) | 64x64 | Industrial strength; you'll need them |
| Toothpick Cup | (704, 256) | 64x64 | For the timid |
| Tail Grip Demo Placard | (0, 384) | 128x128 | Close-up hand-holding-tail diagram for the demonstration area |
| Mint Tin (Fish Breath Cure) | (128, 384) | 64x64 | €1 counter item, purchasable cure |
| Cart Awning States | (192, 384) | 384x128 | Open (192x128) at (192,384) + breeze-flutter frame (192x128) at (384,384) |
| Ice Refill Bucket | (576, 384) | 96x128 | Prop for Dirk's restock loop |

### Technical Notes:
- Cart Full renders behind Display Case node so case can swap Full/Half-Empty by time of day
- Awning flutter is a 2-frame swap, 1.2s interval, disabled in reduced-motion mode
- Method sign is a separate interactable (readable close-up uses same texture, scaled)

---

## 🍽️ Sprite Sheet 3: Food & Consumables
**File:** `herring_food_items.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #C0C0C0, #F5F5F5, #D6EEF5

### Menu Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Haring (Traditional) | (0, 0) | 64x48 | Whole fillet held by tail, butterflied, ready |
| Haring met Uitjes | (64, 0) | 64x48 | Same, dusted in raw onion |
| Broodje Haring | (128, 0) | 64x48 | On bread; acceptable but noted |
| Kibbeling Basket | (192, 0) | 64x64 | Fried retreat option, no judgment (some judgment) |
| De Waarheid Platter | (0, 48) | 128x96 | Two herrings, onions, pickles, bread — the full spread |
| "Just the Bread" | (128, 64) | 64x48 | Coward's Comfort, €2 |
| Raw Onion Portion | (192, 64) | 32x32 | Diced, powerful |
| Pickle Portion | (224, 64) | 32x32 | Augurken single serving |
| Fish Tail Remaining | (128, 112) | 32x16 | Victory evidence |
| Dropped Fish (Ground) | (160, 112) | 48x32 | Pre-seagull-acquisition state, 1-second lifespan |
| Herring Inventory Icon | (0, 144) | 32x32 | Item icon for menus |
| Platter Inventory Icon | (32, 144) | 32x32 | Item icon for menus |
| Mints Inventory Icon | (64, 144) | 32x32 | Fish Breath cure icon |

### Technical Notes:
- All food sprites share one atlas region for a single draw call at the counter
- Dropped Fish spawns only during the Fish Dropped sequence (Sheet 6) — never persists

---

## 👥 Sprite Sheet 4: Stand Staff — Dirk & Evi
**File:** `npc_dirk_evi.png`
**Dimensions:** 512x384 pixels
**Sprite Size:** 64x96 per frame
**Color Palette:** #708090, #F5F5F5, #4A7C99

### Visser Dirk (Rows 0-2):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dirk Idle | (0, 0) | 64x96 | Weathered face, fisherman's apron, seen-everything neutrality |
| Dirk Idle Blink | (64, 0) | 64x96 | Minimal blink variant |
| Dirk Approving Nod | (128, 0) | 64x96 | "Good." (highest praise available) |
| Dirk Preparing Frame 1 | (0, 96) | 64x96 | Fillet lift from ice |
| Dirk Preparing Frame 2 | (64, 96) | 64x96 | Knife work, decades of efficiency |
| Dirk Preparing Frame 3 | (128, 96) | 64x96 | Hand-over to customer |
| Dirk Demonstrating Frame 1 | (0, 192) | 64x96 | The Grip — tail between thumb and forefinger |
| Dirk Demonstrating Frame 2 | (64, 192) | 64x96 | The Tilt — head back, face to sky |
| Dirk Demonstrating Frame 3 | (128, 192) | 64x96 | The Lower — fish descends |
| Dirk Demonstrating Frame 4 | (192, 192) | 64x96 | The Bite — effortless, instant |

### Assistant Evi (Row 3 + Row 0 remainder):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Evi Idle | (0, 288) | 64x96 | Practical ponytail, efficient stance |
| Evi Encouraging | (64, 288) | 64x96 | The mastered "you can do this" expression |
| Evi Handing Napkins | (128, 288) | 64x96 | "You'll want several. Trust me." |
| Evi Onion Chopping Frame 1 | (192, 288) | 64x96 | Rhythmic dicing, down-stroke |
| Evi Onion Chopping Frame 2 | (256, 288) | 64x96 | Rhythmic dicing, up-stroke |
| Dirk Portrait (Dialogue) | (256, 0) | 128x128 | Close-up: eyes that have witnessed humanity's relationship with raw fish |
| Evi Portrait (Dialogue) | (384, 0) | 128x128 | Close-up: encouraging, herring philosophy in progress |

### Technical Notes:
- Portraits sit in the unused right block of rows 0-1 (256-512px); do not scale portraits below 128px
- Dirk's demonstration loop is also the tutorial reference — frame timing must match the player eating animation (Sheet 6) exactly

---

## 🧳 Sprite Sheet 5: Customers & Hendrik
**File:** `npc_harbor_customers.png`
**Dimensions:** 1024x512 pixels
**Sprite Size:** 64x96 per single NPC frame
**Color Palette:** Mixed tourist palette over #708090 harbor tones

### Atmospheric Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Local Lunch Regular Idle | (0, 0) | 64x96 | Dutch office worker; 90 seconds total, order to gone |
| Local Lunch Regular Eating | (64, 0) | 64x96 | Effortless traditional method, mid-tilt |
| Retired Fisherman Idle | (128, 0) | 64x96 | Cap, thousand-yard North Sea stare |
| Retired Fisherman Savoring | (192, 0) | 64x96 | Eats slowly, judges silently |
| Repeat Tourist Idle | (256, 0) | 64x96 | American, confident, "the fish resets me" |
| Repeat Tourist Eating | (320, 0) | 64x96 | Met uitjes, efficient, proof tourists can master this |
| Hen Party Group | (384, 0) | 256x96 | Four-across: one committed, one struggling, one photographing, one retreated to kibbeling |
| Hen Party Reaction Variant | (640, 0) | 256x96 | Same four, one beat later: "EMMA YOU HAVE TO— oh god she actually—" |
| Queue Filler A (Back View) | (0, 96) | 64x96 | Line-body for stand queue |
| Queue Filler B (Back View) | (64, 96) | 64x96 | Line-body variant |
| Photographing Tourist | (128, 96) | 64x96 | Phone raised at someone else's vulnerable moment |

### Seagull Hendrik:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hendrik Perched | (0, 192) | 48x48 | Fat, bold, optimal-distance patience |
| Hendrik Head Track | (48, 192) | 48x48 | Head follows the fish, body still |
| Hendrik Wings Ready | (96, 192) | 48x48 | Pre-swoop tension |
| Hendrik Swoop Frame 1 | (0, 240) | 64x64 | Launch |
| Hendrik Swoop Frame 2 | (64, 240) | 64x64 | Descent, wings back |
| Hendrik Swoop Frame 3 | (128, 240) | 64x64 | Acquisition — fish secured, generations of practice |
| Hendrik Victory Ascent | (192, 240) | 64x64 | Departing with prize |
| Hendrik Hover (Static Mobile) | (256, 240) | 64x64 | Single-frame hover for low-end devices (profile: static seagulls) |

### Technical Notes:
- Hen Party group blocks are pre-composed to save draw calls (one sprite, four characters)
- Hendrik swoop triggers ONLY on Dropped Fish event; hover/perch loops otherwise
- Queue fillers are recolorable via modulate to fake crowd variety

---

## 🎬 Sprite Sheet 6: The Traditional Method — Player Animations
**File:** `eating_method_animations.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** Player palette + #C0C0C0 fish

### Eating Method Sequences:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Traditional Method Frame 1 | (0, 0) | 128x192 | The Grip — fish hangs freely, commitment shown |
| Traditional Method Frame 2 | (128, 0) | 128x192 | The Tilt — head back, dignity suspended |
| Traditional Method Frame 3 | (256, 0) | 128x192 | The Lower — fish descends toward mouth |
| Traditional Method Frame 4 | (384, 0) | 128x192 | First Bite — significant, committed |
| Traditional Method Frame 5 | (512, 0) | 128x192 | The Repeat — working down the fillet |
| Traditional Method Frame 6 | (640, 0) | 128x192 | Tail only remains — victory posture |
| Struggle Frame 1 | (0, 192) | 128x192 | Fish held too long, doubt entering |
| Struggle Frame 2 | (128, 192) | 128x192 | "Tourist grip" modification attempt |
| Struggle Frame 3 | (256, 192) | 128x192 | Visible negotiation with self |
| Struggle Frame 4 | (384, 192) | 128x192 | Fish lowered — the seagulls stir |
| Success Pose A | (512, 192) | 128x96 | Completion, satisfaction, fish breath acquired |
| Success Pose B | (512, 288) | 128x96 | Wiping hands, fractional local respect earned |
| Fish Dropped Frame 1 | (640, 192) | 96x96 | The slip |
| Fish Dropped Frame 2 | (736, 192) | 96x96 | The horror |
| Fish Dropped Frame 3 | (832, 192) | 96x96 | The acceptance (Hendrik inbound) |

### Reaction & Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Customer Reaction Strip | (0, 384) | 256x96 | Four 64x96 faces: awe, horror, respect, camera-up |
| Onion Tears Effect | (256, 384) | 32x32 | Optional realism, 2-frame welling |
| Onion Tears Frame 2 | (288, 384) | 32x32 | Tear release |
| Commitment Flash | (320, 384) | 64x64 | Brief white-blue pulse on full first bite |
| Hesitation Wobble Lines | (384, 384) | 64x64 | Comic wobble marks for struggle state |
| Bro Reaction Pilsner | (0, 480) | 64x96 | "It's looking at me. Do they always look at you?" |
| Bro Reaction Chadwick | (64, 480) | 64x96 | Filming mid-swallow, incoherent fish noises |
| Bro Reaction Bradley | (128, 480) | 64x96 | "...I'm busy..." — quiet trust in the fish |

### Technical Notes:
- Traditional frames 1-6 and Dirk's demonstration must share identical timing curves so the tutorial reads as a mirror
- Struggle sequence loops frames 1-3 while the 30-second hesitation timer runs; frame 4 fires only on retreat
- Commitment Flash draws once, 0.2s, skipped entirely in reduced-motion mode

---

## 🧭 Sprite Sheet 7: UI, Status & Badges
**File:** `herring_ui_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #4A7C99, #B22222, #FFD700 accents on UI chrome

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Method Choice Panel | (0, 0) | 192x128 | Traditional (by tail) vs. Tourist (on bread) selection |
| Menu Order Panel | (192, 0) | 192x128 | Six-item price list with herring thumbnails |
| Seagull Threat Indicator | (384, 0) | 64x32 | Hendrik proximity warning, red gull silhouette |
| Hesitation Timer Bar | (384, 32) | 96x24 | 30-second struggle countdown, fills Warning Red |
| First Bite Prompt | (384, 64) | 96x48 | "COMMIT" tap prompt for the moment of truth |
| Fish Breath Status Icon | (0, 128) | 32x32 | Green wisp over fish silhouette |
| Onion Aura Status Icon | (32, 128) | 32x32 | Stacking ring variant, onion motif |
| Courage Buff Icon | (64, 128) | 32x32 | Blue-flame heart — faced a fear |
| Coward's Comfort Icon | (96, 128) | 32x32 | Bread slice, gray-toned |
| Fish Wasted Icon | (128, 128) | 32x32 | Tail-only silhouette, seagull check mark |
| Herring Survivor Badge | (160, 128) | 64x64 | Achievement: completed the method |
| Fish Mentor Badge | (224, 128) | 64x64 | Helped another tourist with technique |
| Fish Respect Badge | (288, 128) | 64x64 | Ate while making eye contact with Dirk |
| Bravado +/- Popups | (352, 128) | 96x64 | Paired +BRAVADO / -BRAVADO floaters (96x32 each, stacked) |
| Respect Nod Icon | (448, 128) | 32x32 | Fractional local respect indicator |

### Technical Notes:
- All status icons ship with pattern-differentiated variants (see Accessibility)
- Threat indicator pulses at 1s intervals; static high-contrast variant provided
- Touch targets for Method Choice options rendered at minimum 44px despite 192x128 art

---

## 🎬 Animation Specifications

### Traditional Method (Sheet 6, Frames 1-6):
- **Duration:** 4.5 seconds total (Grip 1.0s → Tilt 0.75s → Lower 0.75s → Bite 0.5s → Repeat 1.0s → Tail 0.5s)
- **Frames:** 6
- **Pattern:** Play once, frame-by-frame, no loop
- **Trigger:** Player selects Traditional and commits at the First Bite Prompt
- **Purpose:** The core comedy beat — public vulnerability rendered in full
- **Audio Sync:** Gull cry fades at 0.0s; bite crunch at 3.0s (Frame 4 start); subtle triumphant note at 4.5s completion
- **Mobile Optimization:** None needed (single character, one-shot)

### Struggle Loop (Sheet 6, Frames 1-3 of Struggle):
- **Duration:** 2.4 seconds per loop (0.8s per frame), loops for up to 30 seconds
- **Frames:** 3 (+1 retreat frame)
- **Pattern:** 1 → 2 → 3 → 1... ; frame 4 plays once on retreat
- **Trigger:** Player hesitates after receiving fish
- **Purpose:** Hesitation Penalty visualization — the visible struggle everyone politely doesn't comment on
- **Audio Sync:** Tourist-hesitation ambience swells at loop 3; hesitation-penalty sting on retreat frame
- **Mobile Optimization:** Wobble lines overlay dropped on Low LOD

### Dirk Preparing (Sheet 4, Row 1):
- **Duration:** 1.5 seconds (0.5s per frame)
- **Frames:** 3
- **Pattern:** Play once per order, then return to idle
- **Trigger:** Any menu purchase
- **Purpose:** Efficiency-of-decades characterization; order feedback
- **Audio Sync:** Knife-on-block tap at Frame 2 (0.5s); paper-wrap rustle at Frame 3 (1.0s)
- **Mobile Optimization:** None needed

### Evi Onion Chopping (Sheet 4, Row 3):
- **Duration:** 0.8 seconds per cycle, ambient loop
- **Frames:** 2
- **Pattern:** Continuous loop while stand is open
- **Trigger:** Constant (ambient)
- **Purpose:** Rhythmic background life; onion vapor source point
- **Audio Sync:** Chop tick locked to down-stroke frame every 0.8s
- **Mobile Optimization:** Loop rate halved on Low LOD

### Hendrik Swoop (Sheet 5):
- **Duration:** 1.2 seconds (0.3s per frame + 0.3s ascent)
- **Frames:** 4 (3 swoop + victory ascent)
- **Pattern:** Play once: perch → swoop 1-3 → ascent → despawn
- **Trigger:** Fish Dropped event only
- **Purpose:** Consequence for weakness; the circle of life
- **Audio Sync:** Aggressive gull shriek at 0.0s; wing flap at 0.6s; comedy "gone" whistle at 1.2s
- **Mobile Optimization:** Low LOD replaces swoop with static Hover frame + fish despawn

### Water & Awning Ambient:
- **Duration:** Water 0.8s two-frame swap; awning 1.2s two-frame swap
- **Frames:** 2 each
- **Pattern:** Continuous alternation
- **Trigger:** Constant
- **Purpose:** Harbor breeze atmosphere without particle cost
- **Audio Sync:** Harbor wave loop is continuous; no frame lock required
- **Mobile Optimization:** Both freeze to frame A on Low LOD; static per reduced-motion setting

### Onion Tears (Sheet 6):
- **Duration:** 1.0 second (0.5s per frame), plays up to 3 times
- **Frames:** 2
- **Pattern:** Well → release → repeat while near Onion Station
- **Trigger:** Player stands adjacent to onion chopping for 3+ seconds
- **Purpose:** Optional realism gag
- **Audio Sync:** None
- **Mobile Optimization:** Disabled on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stand Interaction Outline | (448, 160) | 64x64 | Bold white/black outline marker for the order point (Sheet 7 reserve block) |
| Method Sign High-Contrast | (0, 192) | 96x64 | Black-on-white redraw of the four method steps (Sheet 7 reserve block) |
| Hendrik Threat Silhouette | (96, 192) | 64x32 | Solid-black gull with warning chevrons — readable without color (Sheet 7 reserve block) |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Water Frame | Sheet 1 (Strip A) | 512x96 | Reduced-motion mode locks water to Strip A |
| Static Awning Frame | Sheet 2 (Awning Open) | 192x128 | No flutter in reduced-motion mode |
| Non-Pulsing Threat Indicator | (160, 192) | 64x32 | Constant-fill seagull warning, no pulse (Sheet 7 reserve block) |
| Commitment Flash Removal | — | — | Flash skipped entirely; Success Pose A carries the feedback |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gull Shriek Icon | (224, 192) | 24x24 | Beak-open icon flashes at swoop start, mirrors the shriek (Sheet 7 reserve block) |
| Bite Crunch Marker | (248, 192) | 24x24 | Starburst on Frame 4 of the traditional method, mirrors crunch audio |
| Success Note Marker | (272, 192) | 24x24 | Small rising-note glyph on completion, mirrors triumphant sting |
| Chop Rhythm Tick | (296, 192) | 24x24 | Metronome tick over Evi during chopping, mirrors chop audio |

### Colorblind Considerations:
- Fish Breath (green) vs. Onion Aura (yellow-white) icons differ by shape: wisp vs. ring — never color alone
- Hesitation Timer uses fill-length plus hatching pattern, not just red saturation
- Seagull threat readable via silhouette + chevrons, independent of red tint
- Touch zones minimum 44px for the order point, method choice, and First Bite Prompt

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (fallback PVRTC 4BPP); Method Illustration Sign and portraits need ASTC 4x4 (readable text/faces)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for the Method Illustration Sign (text-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| herring_environment | harbor_background, herring_stand_structures | 2048x2048 |
| herring_characters | npc_dirk_evi, npc_harbor_customers, eating_method_animations | 2048x2048 |
| herring_ui | herring_food_items, herring_ui_effects | 1024x1024 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Sea mist overlay, water/awning swaps, Hendrik full swoop, onion tears, all ambient NPC loops |
| Medium | Mist at half alpha steps, ambient loops at half rate, swoop retained |
| Low | Static water/awning/gulls, Hendrik hover frame substitution, no mist, no onion tears |

### Performance Targets:
- **Target FPS:** 45 (per location performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 32 MB maximum
- **Particle Limit:** 12 (sea mist motes, onion vapor, fish-scale glint)

### Performance Notes:
- Profile mandates: simplified water effects, static seagulls in background, reduced particle count
- Hen party and queue fillers pre-composed into group sprites to stay under draw-call budget
- Eating animations are one-shots — no persistent animated player overlays

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: ParallaxBackground (harbor layers), AnimatedSprite2D (NPCs, eating sequences, Hendrik), CPUParticles2D (mist/vapor — not GPU), CanvasLayer (method UI), Area2D (seagull threat radius)
- Special systems: 30-second hesitation timer with penalty states, First Bite outcome check (Commitment / Hesitation / Retreat), Bravado delta hooks, time-of-day display case swap, Fish Breath / Onion Aura duration timers with stacking

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Traditional Method Frame 4 | Bite crunch | 3.0s into sequence |
| Traditional Method completion | Subtle triumphant note | On Frame 6 end (4.5s) |
| Struggle retreat frame | Hesitation penalty sting | On retreat frame start |
| Hendrik Swoop Frame 1 | Aggressive gull shriek | 0.0s of swoop |
| Dirk Preparing Frame 2 | Knife-on-block tap | 0.5s into prep |
| Evi chop down-stroke | Chop tick | Every 0.8s, frame-locked |
| Fish handed to player | Fish-received sound | On Dirk Preparing Frame 3 |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Herring Achievement Track — "Fish Curious" | Traditional Method frames, Herring Survivor Badge | First traditional completion |
| "Fish Committed" / "Fish & Onion Alliance" | Haring met Uitjes sprite, Onion Aura icon | Three completions / met uitjes mastery |
| "Fish Mentor" | Repeat Tourist / Hen Party sprites, Fish Mentor Badge | Help another tourist with technique |
| "Fish Respect" | Dirk Approving Nod, Fish Respect Badge | Eat while making eye contact with Dirk |
| Cultural Courage Network | Courage Buff icon | Feeds courage progression shared with Proeflokaal and Brouwerij |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| FEBO Automat | Fish Breath icon persists into FEBO scenes | Late-night contrast: raw intention vs. processed desperation |
| Proeflokaal 't Kansen | Courage Buff carries into gauntlet attempts | Shared public-vulnerability courage system |
| The Pancake House | Price board comparison gag | "Herring = authentic, pancakes = trap" dialogue callbacks |
| Stroopwafel Cart | Success Pose B hand-off | Recovery comfort route after herring challenge |
| Harbor District hub | Harbor background layers shared | Geographic continuity along the waterfront |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Impeccable Dutch cleanliness framing a moment of maximum personal chaos"
- **Color Mood:** Cold silvers and North Sea blues against clean white — the stand is calm; only the humans are not
- **Lighting:** Natural harbor daylight, reflective ice glow from the display case, no artificial drama
- **Texture:** Scrubbed wood, wet quay stone, glistening fish skin — everything honest, nothing hidden

### Environmental Storytelling:
- The display case's neat rows vs. the late-day half-empty state track the stand's quiet, relentless turnover
- The method sign's cheerful illustrations are the only warning tourists get — and it's inescapable
- Hendrik's guano-weathered lamp post says the seagull war is generational
- The napkin dispenser's industrial scale quietly promises mess

### Character Integration Notes:
- Dirk is a fixture behind the case; he never leaves frame — stability against tourist chaos
- Evi orbits: napkins, onions, encouragement — the stand's warmth channel
- Customer gallery renders behind the player during eating sequences: the Viewing Gallery is always watching, politely
- Hendrik must read as patient, not aggressive, until the exact moment he isn't

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Tilt** — player mid-traditional-method, head back, harbor behind: the definitive Shamsterdam vulnerability portrait
2. **Hendrik's Acquisition** — the swoop frame 3 fish-theft, comedy in one image
3. **The Hen Party Panel** — four simultaneous stages of herring courage in a single group sprite
4. **Dirk's Nod** — the rarest approval in the Harbor District, worth framing
5. **The Method Sign** — "The fish is raw. Your reaction will be witnessed."

### Quote Potential:
- "The fish is fresh. Your courage is the variable."
- "The trick is commitment. The fish knows if you're afraid."
- "Seagull was faster. Want another?"
- "It's looking at me. Do they always look at you?"
- "In my day the fish were bigger. The tourists were braver. Both lies."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | harbor_background.png | 2048x1024 |
| 2 | herring_stand_structures.png | 1024x1024 |
| 3 | herring_food_items.png | 256x256 |
| 4 | npc_dirk_evi.png | 512x384 |
| 5 | npc_harbor_customers.png | 1024x512 |
| 6 | eating_method_animations.png | 1024x1024 |
| 7 | herring_ui_effects.png | 512x256 |

**Total Estimated Memory:** ~26 MB in-memory (uncompressed RGBA worst case), within the 32 MB location budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `harbor_background.png` (2048x1024)
- [ ] `herring_stand_structures.png` (1024x1024)
- [ ] `herring_food_items.png` (256x256)
- [ ] `npc_dirk_evi.png` (512x384)
- [ ] `npc_harbor_customers.png` (1024x512)
- [ ] `eating_method_animations.png` (1024x1024)
- [ ] `herring_ui_effects.png` (512x256)

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
- **Documentation:** Animation timing reference sheet + parallax layer guide (harbor background layers)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: the Tilt silhouette, Hendrik's swoop, the method sign's inescapable instructions, the half-empty late-day case
- [ ] Accessibility visual alternatives included for all audio cues (gull shriek, bite crunch, success note, chop rhythm)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (tourist reaction is the joke, never the Dutch tradition)
- [ ] Hidden areas/interactions have discoverable visual cues (mint tin cure, tail-grip demo placard, Dirk eye-contact achievement)
- [ ] Mobile performance optimized (CPU particles, atlas limits respected, static-seagull fallback)
- [ ] Touch zone sizing considered (44px minimum for order point, method choice, First Bite Prompt)
- [ ] Colorblind-friendly alternatives available where color codes meaning (status icon shapes, hatched timer)
- [ ] Social media viral potential maximized in composition choices (the Tilt framed against open harbor sky)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam Harbor District only; "The Shamsterdam Way" signage in-world |
| Cultural Specificity | ✅ | Dutch haring tradition rendered with respect; tourist reaction carries the comedy |
| Satirical Targets Appropriate | ✅ | Tourist hesitation, photo-op culture, and bro bravado — never Dutch food culture |
| Seedy Underbelly Present | ✅ | €4 existential revelations, maximum-visibility stand placement, seagull opportunism economy |
| Gameplay Value Established | ✅ | Method challenge, Bravado economy, three status effects, seagull hazard, achievement track |
| Technical Feasibility | ✅ | Static-seagull fallback, 2-frame ambients, pre-composed crowds documented |
| Mobile Performance Budget | ✅ | 45 FPS, 14 draw calls, 32 MB, 12 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all four audio cues, reduced-motion set, 44px touch zones |
| No Crypto Elements | ✅ | Pure traditional fish stand; all transactions in Euros |
| Social Media Integration | ✅ | 5 screenshot moments + 5 quotable lines identified |

**Once these assets ship, De Zilte Waarheid becomes the game's cleanest comedy machine: a spotless little cart where every player must choose, in public, between the bread and the truth.**
