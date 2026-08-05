# Kapsalon Koning - Complete PNG Asset Requirements

## 📋 Overview
Kapsalon Koning is the late-night temple where a barber's 2003 vision — fries, döner, melted Gouda, theoretical salad, both sauces — is served in an aluminum tray with a fork guaranteed to break. This document specifies every PNG asset for the shop: the crown-branded exterior, the Cheese Cathedral interior, the visible assembly-line theater, Big Wim and Kemal, the customer congregation, the fork-break and food-coma effect sets, and the ordering UI where "small" does not exist. Its satirical essence in a sentence: someone asked "what if ALL the things, together, with cheese?" and an entire country said yes.

**Location ID:** `shamsterdam_latenight_kapsalon_koning_01`
**Theme:** Dutch-Turkish fusion excess celebrated, not mocked; the "more is more" food philosophy at its logical conclusion
**Zone:** Late-night district, strategic position near Leeman's (friendly rivalry)
**Hours:** 4 PM - 6 AM (peak: midnight - 4 AM, when kapsalon calls loudest)
**Primary Function:** Late-night food vendor / cheese sweats generator — layered ordering system, Wim Assessment, fork break event, Food Coma mechanic, King Size Challenge with Wall of Fame, Kapsalon Battle Tray collectible

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Cheese Gold | #FFD700 | Melted Gouda, crown logo, signage |
| Port City Orange | #FF8C00 | Accent trim, neon, menu highlights |
| Aluminum Silver | #C0C0C0 | Trays, counter, salamander body |
| Sambal Red | #FF4500 | Sauce accents, fire warnings |
| Fry Yellow | #F5C542 | Fries foundation layer |
| Night Grease Brown | #6B4423 | Döner meat, interior shadow tones |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/kapsalon_koning/
├── environment/
│   ├── kapsalon_interior_main.png
│   └── kapsalon_exterior_fixtures.png
├── objects/
│   └── kapsalon_food_items.png
├── npcs/
│   ├── npc_wim_kemal.png
│   └── npc_kapsalon_customers.png
├── effects/
│   └── kapsalon_effects.png
└── ui/
    └── kapsalon_ui.png
```

---

## 🏪 Sprite Sheet 1: Interior Main Background
**File:** `kapsalon_interior_main.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #FFD700, #C0C0C0, #6B4423

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Backdrop | (0, 0) | 1920x1080 | Full scene: counter with visible assembly line left-center, cheese salamander glowing at center rear, single döner tower (they have ONE tower, focused), four cramped tables right, Wall of Fame rear right, neon accents, brighter-than-Leeman's chaos energy |

### Technical Notes:
- Anchor points (document in layer names): salamander at (832, 256), assembly station at (384, 448), Wall of Fame at (1536, 192), seating at (1408, 640), tray stack at (704, 512)
- Salamander glow zone painted dim in the backdrop — the animated glow overlay (Sheet 6) sits on top
- Wall of Fame photo grid painted with 3 empty slots for player photo insertion

---

## 👑 Sprite Sheet 2: Exterior & Fixtures
**File:** `kapsalon_exterior_fixtures.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #FFD700, #FF8C00, #C0C0C0

### Exterior:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kapsalon Koning Storefront | (0, 0) | 384x384 | Crown logo, neon presence, window kapsalon photos (photography magic) |
| Crown Logo Sign | (384, 640) | 128x128 | "KAPSALON KONING" crown emblem, separate for glow overlay |
| "No Small" Warning Sign | (512, 640) | 128x64 | "No Small Available. This Is Intentional." |
| Layer Explanation Sign | (512, 704) | 128x64 | "KAPSALON = Fries + Döner + Cheese + Salad + Sauce + Glory" |

### Interior Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wall of Fame | (384, 0) | 256x384 | Framed photos of King Size finishers; three empty slots wait |
| Cheese Salamander | (640, 0) | 192x192 | Industrial broiler, the glowing heart of operations |
| Menu Board | (832, 0) | 192x128 | Sizes and prices; the word "small" is conspicuously absent |
| Sauce Station | (832, 128) | 128x96 | Garlic and sambal pumps; "both" is the enlightened path |
| Fry Station | (640, 192) | 128x128 | The foundation; fresh-cut, golden |
| Döner Tower (Single) | (640, 320) | 128x256 | One tower, focused — the soul supply |
| Aluminum Tray Stack | (832, 224) | 128x96 | Vessels of delivery, stacked and ready |
| Assembly Station | (0, 384) | 384x256 | Counter-top build zone where the five layers happen in view |
| Seating Area | (384, 384) | 256x192 | Four tables, twelve seats, cramped and functional |
| Counter Front Panel | (0, 640) | 384x128 | Customer-side counter with fork dispenser and napkin canyon |
| Fork Dispenser Detail | (0, 768) | 64x64 | Standard plastic, not reinforced, 100% break certainty |
| Replacement Fork Cup | (64, 768) | 64x64 | The second fork, automatically provided |
| Salamander Rack (Tray In) | (128, 768) | 192x96 | Tray under the broiler, cheese mid-transformation |
| Big Wim's Quote Plaque | (320, 768) | 192x64 | "In the port city, we put cheese on everything." |

### Technical Notes:
- Salamander renders behind its glow overlay (Sheet 6) — keep interior lamp area neutral
- Wall of Fame photo slots (each 48x64 inside the 256x384 art) receive the player photo texture on King Size completion
- Döner tower is the rotation animation target — draw with vertical symmetry for a 2-frame shave illusion

---

## 🧀 Sprite Sheet 3: Food & The Five Layers
**File:** `kapsalon_food_items.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #F5C542, #6B4423, #FFD700, #FF4500

### The Kapsalon Range:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kapsalon Regular | (0, 0) | 96x64 | Standard glory, 10 Sovs, "large enough for most" |
| Kapsalon Large | (96, 0) | 128x72 | Committed glory, 14 Sovs, Food Coma risk visible in sheer mass |
| Kapsalon King Size | (224, 0) | 160x80 | Wall of Fame glory, 18 Sovs, structurally ambitious |
| Cheese Melt Cap | (384, 0) | 64x64 | Bubbling Gouda top layer, overlay-ready |
| Cola Cup | (448, 0) | 32x48 | "For the cheese" |
| Layers Cross-Section Diagram | (384, 64) | 128x192 | Educational cutaway: fries / döner / cheese / salad / sauce, labeled |
| Fries Foundation | (0, 80) | 64x48 | Layer 1 — the carb platform |
| Döner Meat Layer | (64, 80) | 64x48 | Layer 2 — the soul |
| Salad Top | (128, 80) | 64x32 | Layer 4 — the lies we tell ourselves |
| Both Sauces Drizzle | (192, 80) | 48x32 | Layer 5 — garlic + sambal, understanding achieved |
| Aluminum Tray Empty | (0, 128) | 96x48 | The vessel, pre-glory |
| Kapsalon Battle Tray | (96, 128) | 96x64 | Post-victory collectible: dented, faintly cheese-aromatic, +2 Defense |
| Wall of Fame Photo (Player) | (240, 128) | 64x96 | Polaroid-style frame for the champion wall |
| Kapsalon Inventory Icon | (0, 176) | 32x32 | Item icon |
| Battle Tray Inventory Icon | (32, 176) | 32x32 | Equipment icon |
| Half-Eaten Tray State | (64, 176) | 96x48 | Mid-journey state: "this is so much food" |
| Nearly-Done Tray State | (160, 176) | 96x48 | Final third: "I can do this" |

### Technical Notes:
- Regular/Large/King Size share silhouette language — scale must read instantly at gameplay zoom
- Layer sprites stack in assembly animation order at the Assembly Station anchor
- Tray eating states swap at 33%/66% progress during eat sequence

---

## 👨‍🍳 Sprite Sheet 4: Big Wim & Kemal
**File:** `npc_wim_kemal.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** Wim 64x128; Kemal 64x96
**Color Palette:** #FFD700 apron accents, #C0C0C0, #6B4423

### Big Wim (6'5" of Kapsalon Evangelism):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wim Idle | (0, 0) | 64x128 | Commanding presence, warm despite size, visible over everyone |
| Wim Assembling Frame 1 | (64, 0) | 64x128 | Fries poured — "Foundation. Without foundation, chaos." |
| Wim Assembling Frame 2 | (128, 0) | 64x128 | Meat shaved on — "The meat gives meaning." |
| Wim Assembling Frame 3 | (192, 0) | 64x128 | Tray into salamander — "This is where the port city happens." |
| Wim Assembling Frame 4 | (256, 0) | 64x128 | Salad + sauces flourish — "For health. ...okay, for texture." |
| Wim Approving | (320, 0) | 64x128 | Both sauces ordered: "You understand." |
| Wim Portrait (Dialogue) | (384, 0) | 128x128 | Close-up: enthusiasm of a man whose purpose is fixing hungry people |
| Wim Explaining Frame 1 | (0, 128) | 64x128 | The barber story begins — hands wide |
| Wim Explaining Frame 2 | (64, 128) | 64x128 | "He says 'everything together. With cheese.'" |
| Wim Explaining Frame 3 | (128, 128) | 64x128 | "This man is a VISIONARY. I am his disciple." |
| Wim Handing Fork | (192, 128) | 64x128 | Second fork extended before you even ask |
| Wim Watching (King Size) | (256, 128) | 64x128 | Judging, respecting, witnessing |
| Wim Pained ("Less Cheese") | (320, 128) | 64x128 | "...less cheese. Okay. But why." |

### Kemal (The Nephew, Learning the Trade):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kemal Idle | (0, 256) | 64x96 | Perpetual cheese residue, quiet pride |
| Kemal Cheese Station Frame 1 | (64, 256) | 64x96 | Watching the broiler — "The cheese must bubble. Not burn." |
| Kemal Cheese Station Frame 2 | (128, 256) | 64x96 | Tray pulled at exact bubble moment |
| Kemal Handing Fork | (192, 256) | 64x96 | "Fork broke? Here. It happens. It always happens." |
| Kemal Respect Nod | (256, 256) | 64x96 | "You finishing that? ...respect." |
| Kemal Overwhelmed (Peak Hours) | (320, 256) | 64x96 | 2 AM rush face |
| Kemal Portrait (Dialogue) | (384, 256) | 128x128 | Close-up: business student by day, cheese guardian by night |
| Wim Wall-Point Gesture | (0, 352) | 64x128 | Pointing a champion to their photo on the wall |
| Wim Laughing | (64, 352) | 64x128 | Full-body warmth for post-club pilgrims |

### Technical Notes:
- Wim's 128px height must clear all other NPCs in any shared frame — he is always visible
- Assembling frames align with layer sprites (Sheet 3) appearing at the Assembly Station anchor
- Kemal's cheese station frames pair with the salamander glow pulse (Sheet 6)

---

## 👥 Sprite Sheet 5: The Customer Congregation
**File:** `npc_kapsalon_customers.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame
**Color Palette:** Mixed night-crowd palette, cheese-gold ambient grade

### Atmospheric Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Post-Club Pilgrimage Group | (0, 0) | 256x96 | Friends in club clothes sharing large kapsalons, mess in progress, loving every moment |
| First-Timer Overwhelmed | (256, 0) | 64x96 | Fork in hand, staring at tray, unsure where to begin |
| First-Timer Committed | (320, 0) | 64x96 | Decision made, first bite loaded |
| King Size Champion | (384, 0) | 64x96 | Wall of Fame resident eating comfortably, veteran calm |
| Health-Conscious Compromiser | (448, 0) | 64x96 | "Less cheese... for health?" — the room disapproves gently |
| Competitive Eaters Group | (512, 0) | 192x96 | Three-across race: "FIRST ONE DONE DOESN'T PAY." |
| Seated Eater (Table Pose) | (704, 0) | 64x96 | Universal seated eating pose for table slots |
| Takeaway Departer | (768, 0) | 64x96 | Tray clutched, into the night, heavier and slower |
| Eating Poses Strip | (0, 96) | 256x96 | Four 64x96 stages: first bite joy / pacing / surrender / cheese-sweat glow |
| Food Coma Slump | (256, 96) | 96x96 | Seated full-surrender pose, tray empty, at peace |
| Champion Portrait (Dialogue) | (352, 96) | 128x128 | "Yeah, that's me." *points at wall* |
| Queue Filler A (Back View) | (480, 96) | 64x96 | Line body for peak hours |
| Queue Filler B (Back View) | (544, 96) | 64x96 | Line body variant |

### Technical Notes:
- Group blocks pre-composed (one sprite each) to protect the 14-draw-call budget
- Eating poses strip is palette-modulated onto any customer for table scenes
- Food Coma Slump doubles as the player's coma state at tables

---

## ✨ Sprite Sheet 6: Effects — Cheese, Forks & Comas
**File:** `kapsalon_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFD700, #FF4500, #C0C0C0

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fork Break Frame 1 | (0, 0) | 128x64 | The strain — tines vs. cheese-fused fries |
| Fork Break Frame 2 | (128, 0) | 128x64 | The snap — mid-bite, maximum comedy |
| Fork Break Frame 3 | (256, 0) | 128x64 | The two halves, held in disbelief |
| Cheese Bubble Frame 1 | (384, 0) | 64x64 | Under-salamander Gouda, first blisters |
| Cheese Bubble Frame 2 | (448, 0) | 64x64 | Full rolling bubble — "this is where the port city happens" |
| Salamander Glow Pulse | (384, 64) | 64x64 | Warm overlay for the broiler mouth |
| Cheese Sweats Aura | (0, 64) | 64x64 | Faint golden shimmer ring for status-affected characters |
| Cheese String Pull | (64, 64) | 64x64 | Tray-to-mouth strand, the unbreakable connection |
| Steam Rise | (128, 64) | 64x64 | Fresh tray steam, 2 stacked 64x32 frames |
| Sauce Drip | (192, 64) | 32x32 | Garlic/sambal drip for tray edge |
| Food Coma State | (224, 64) | 96x96 | Overlay: drifting Z's + tray halo, skip-turn indicator |
| Fire Addition Flare | (320, 64) | 64x64 | Extra sambal heat wisp — "Port City hot" |
| Neon Flicker Strip | (0, 160) | 128x32 | Two 64x32 exterior neon states |
| Crown Glow Overlay | (128, 160) | 128x128 | Exterior crown logo glow, night hours |
| Camera Flash (Wall of Fame) | (256, 160) | 64x64 | Photo-taken burst for champion induction |
| Grease Sheen Tile | (320, 160) | 64x64 | Tileable counter sheen overlay |

### Technical Notes:
- Fork break is a guaranteed one-shot on first kapsalon — timing is comedy-critical (see Animation Specs)
- Cheese bubble loops only while a tray is under the salamander
- Food Coma overlay parents to the slumped character sprite; no screen-wide effect

---

## 🧭 Sprite Sheet 7: UI Elements
**File:** `kapsalon_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FFD700 UI chrome, #FF4500 warnings

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Size Selection Panel | (0, 0) | 192x128 | Regular / Large / King Size — no small option exists, by design |
| King Size Challenge Panel | (192, 0) | 192x128 | Wall of Fame eligibility prompt with Wim witness note |
| "You Are Not Ready" Tooltip | (384, 0) | 128x64 | Appears if player searches for a smaller option |
| Sauce Selection Panel | (0, 128) | 192x96 | Garlic / Sambal / Both — "Both" is highlighted with subtle reverence |
| Meat Selection Panel | (192, 128) | 192x96 | Chicken / Veal / Mixed with Wim-opinion flavor text slots |
| Food Coma Risk Meter | (384, 64) | 128x64 | 20% / 40% / GUARANTEED risk display |
| Kapsalon Progress Bar | (0, 224) | 128x96 | Tray-shaped eating progress with layer strata |
| Cheese Sweats Status Bar | (128, 224) | 96x32 | Duration display, golden fill |
| Wim Respect Indicator | (128, 256) | 96x32 | Fills on both-sauces order and clean finishes |
| Fork Integrity Icon | (224, 224) | 32x32 | Always shows 100% — it lies |
| Achievement Badges Strip | (0, 320) | 384x64 | Six 64x64 badges: Initiated / Passionate / Understanding / Committed / Wall of Fame / Transcended |
| Battle Tray Equip Card | (384, 128) | 128x96 | +2 Defense shield/throwable item card |
| Wall of Fame Induction Panel | (0, 384) | 256x128 | Photo placement ceremony frame |
| Great Döner Debate Tracker | (256, 384) | 128x64 | Shamsterdam entry #2 quest chip ("döner-adjacent — counts") |
| Cheese Sweats Status Icon | (256, 320) | 32x32 | Golden droplet-ring silhouette |
| Food Coma Status Icon | (288, 320) | 32x32 | Crescent-and-tray silhouette |
| Fire Addition Status Icon | (320, 320) | 32x32 | Chili silhouette with hatching |

### Technical Notes:
- Size/sauce/meat panels all render options at 44px+ touch height
- Fork Integrity Icon is a running gag — it never changes, the fork always breaks
- Badges grayscale until earned (modulate, not separate art)

---

## 🎬 Animation Specifications

### The Assembly Line (Sheets 3, 4, 6):
- **Duration:** 6.0 seconds total (4 Wim frames at 1.2s + 1.2s salamander hold)
- **Frames:** 4 character frames + layer sprite stack + cheese bubble loop
- **Pattern:** Fries → meat → salamander (cheese bubble plays) → salad/sauce flourish → serve
- **Trigger:** Any kapsalon order
- **Purpose:** Visible theater — the five layers are the show
- **Audio Sync:** Fry basket shake 0.0s; meat shave 1.2s; salamander sizzle-bubble begins 2.4s; sauce double-squirt 4.8s; tray-slide 6.0s
- **Performance Optimization:** Low LOD uses static assembly (profile requirement) — single composed frame + serve

### Cheese Bubble (Sheet 6):
- **Duration:** 0.8 seconds per loop (0.4s per frame)
- **Frames:** 2
- **Pattern:** Continuous while any tray is under the salamander
- **Trigger:** Assembly step 3, and ambient when Kemal runs the station
- **Purpose:** That specific sizzle-bubble of melting Gouda — the location's heartbeat
- **Audio Sync:** Sizzle-bubble loop amplitude tied to loop phase
- **Performance Optimization:** Static cheese frame on Low LOD (profile: static cheese effects)

### Fork Break Event (Sheet 6):
- **Duration:** 1.1 seconds (0.3s strain, 0.2s snap, 0.6s disbelief hold)
- **Frames:** 3
- **Pattern:** Play once, mid-eating, 100% trigger on first kapsalon
- **Trigger:** Eating progress crosses 40% on first-ever kapsalon
- **Purpose:** Inevitable tradition; "the fork breaks because you eat with passion"
- **Audio Sync:** Plastic SNAP exactly at frame 2 start (0.3s); beat of silence; Wim's line at 1.1s
- **Performance Optimization:** None needed (one-shot, comedy-critical — never cut)

### Food Coma (Sheets 5 & 6):
- **Duration:** 3.0-second settle, then held overlay for one combat turn
- **Frames:** Slump pose + 2-frame Z drift
- **Pattern:** Slump → Z loop (1.5s per Z cycle) → recovery with full heal
- **Trigger:** 20% chance (Large), 40% (excess speed), 100% (King Size)
- **Purpose:** "The coma is the body processing greatness. Accept it."
- **Audio Sync:** Soft snore loop; triumphant chime on full-heal recovery
- **Performance Optimization:** Z drift at half rate on Low LOD

### Döner Tower Rotation (Sheet 2):
- **Duration:** 2.0 seconds per visual cycle
- **Frames:** 2 (symmetry swap)
- **Pattern:** Continuous slow alternation
- **Trigger:** Constant during open hours
- **Purpose:** The soul supply, steadily turning
- **Audio Sync:** None (ambient sizzle bed)
- **Performance Optimization:** Static frame on Low LOD

### Neon & Crown Glow (Sheet 6):
- **Duration:** Neon 0.5s flicker burst ~every 30s; crown glow 3s breathe
- **Frames:** 2 / 1 (alpha)
- **Pattern:** Random flicker / continuous breathe, night hours only
- **Trigger:** Clock-based
- **Purpose:** Late-night beacon energy, brighter chaos than Leeman's
- **Audio Sync:** Faint neon buzz on flicker
- **Performance Optimization:** Both static on Low LOD; disabled in reduced-motion mode

### Wall of Fame Induction (Sheets 2, 3, 6):
- **Duration:** 2.5 seconds (flash 0.2s, photo slide 1.0s, hold 1.3s)
- **Frames:** Camera flash + photo placement tween
- **Pattern:** One-shot ceremony
- **Trigger:** King Size completed under Wim's witness
- **Purpose:** Eternal recognition; the wall remembers
- **Audio Sync:** Camera click at 0.0s; applause murmur at 1.2s
- **Performance Optimization:** Flash replaced by instant photo placement in reduced-motion mode

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Order-Point Outline | (384, 224) | 64x64 | Bold outline marker for the ordering interaction (Sheet 6 reserve block) |
| Size Silhouette Set | (384, 288) | 128x64 | Regular/Large/King Size as bold stepped silhouettes with size labels (Sheet 7 reserve block at (352, 384)) |
| Fork Break Flash Frame | (448, 224) | 64x64 | High-contrast snapped-fork icon for event readability (Sheet 6 reserve block) |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Cheese Frame | Sheet 6 (Cheese Bubble Frame 1) | 64x64 | Reduced-motion locks the broiler to first-blister frame |
| Static Tower Frame | Sheet 2 (Döner Tower) | 128x256 | No rotation swap |
| No-Flicker Neon | Sheet 6 (Neon Strip frame 1) | 64x32 | Steady neon substitute |
| Instant Photo Induction | Sheet 3 (Wall of Fame Photo) | 64x96 | Flash-free Wall of Fame ceremony |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sizzle-Bubble Waves | (384, 160) | 24x24 | Heat-wave glyph over salamander, mirrors bubble audio (Sheet 6 reserve block) |
| Fork SNAP Marker | (408, 160) | 24x24 | Jagged burst glyph exactly on snap frame |
| Sauce Squirt Marker | (432, 160) | 24x24 | Double-drop glyph on sauce flourish |
| Recovery Chime Marker | (456, 160) | 24x24 | Rising-note glyph on Food Coma full-heal |

### Colorblind Considerations:
- Garlic vs. sambal coded by container shape (round pump vs. angular bottle) and drip pattern, never white/red alone
- Food Coma Risk Meter uses stepped segment count + text (20/40/100), not color gradient alone
- Status icons use distinct silhouettes: droplet-ring (sweats), crescent-tray (coma), hatched chili (fire)
- Touch zones minimum 44px for all size/sauce/meat options and counter interaction

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) menu board, layer diagram, and portraits kept uncompressed (readable text/faces)
- **Fallback:** PNG high quality for kapsalon_interior_main.png (scene-detail critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| kapsalon_environment | kapsalon_exterior_fixtures | 1024x1024 |
| kapsalon_characters | npc_wim_kemal, npc_kapsalon_customers | 2048x1024 |
| kapsalon_fx_ui | kapsalon_food_items, kapsalon_effects, kapsalon_ui | 1024x1024 |

*(kapsalon_interior_main.png loads standalone as a scene background; max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full assembly theater, cheese bubble loop, tower rotation, neon, coma Z drift |
| Medium | Assembly at 2 keyframes, bubble loop retained, neon off |
| Low | Static assembly and cheese (profile requirement), static tower, one-shot fork break retained |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 34 MB maximum
- **Particle Limit:** 15 (steam rise, cheese-glow motes, sauce drips)

### Performance Notes:
- Group customer blocks pre-composed; max 3 individual NPCs animated simultaneously
- Fork break, the single most important beat, is a 3-frame one-shot — cheap and never degraded
- Salamander glow is alpha overlay, no light nodes

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (interior background), AnimatedSprite2D (Wim, Kemal, effects, tower), CPUParticles2D (steam — not GPU), CanvasLayer (order UI), Area2D (counter/table interaction zones)
- Special systems: Wim Assessment dialogue branch on order composition, fork-break first-visit flag, Food Coma probability roll (20/40/100), King Size witness state machine, Wall of Fame photo persistence, Battle Tray inventory grant, eating-progress tracker with tray-state swaps

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Assembly step 1 (fries) | Fry basket shake | 0.0s of assembly |
| Assembly step 2 (meat) | Knife-on-tower shave | 1.2s |
| Cheese bubble loop | Sizzle-bubble of melting Gouda | Continuous, phase-locked |
| Assembly step 4 (sauces) | Double sauce squirt | 4.8s |
| Fork Break frame 2 | Plastic SNAP | 0.3s into event |
| Food Coma recovery | Triumphant full-heal chime | On coma end |
| Wall of Fame flash | Camera click + applause murmur | 0.0s / 1.2s of induction |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Great Döner Debate: International Expansion | Kapsalon sprites, Debate Tracker chip | Eating here = Shamsterdam entry #2 ("döner-adjacent — counts but is its own category") |
| Kapsalon Achievement Track | Badges strip, fork break, sauce panel, coma overlay | Initiated / Passionate / Understanding / Committed / Wall of Fame / Transcended |
| King Size Challenge | King Size sprite, Wim Watching, induction panel, player photo | Order + finish King Size; Wall of Fame photo placed permanently |
| Full Kapsalon Experience | Large sprite, Both Sauces drizzle, Battle Tray | Completion grants Kapsalon Battle Tray equipment |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Leeman's Döner Palace | Menu board rivalry note; Wim's "Mehmet down the street? Good man. No cheese. His loss." | Friendly-rivalry dialogue crosslinks; Leeman's sign reads "NO KAPSALON. Go to Wim for that." |
| De Groene Gids | Munchies pipeline endpoint marker | WARNING: may overcorrect — enhanced HP food effects |
| The Tolerance Hostel | Battle Tray display prop reference | Kitchen conversations + tray shown on shelf |
| FEBO Automat | Comparison dialogue hook | "FEBO is snack. Kapsalon is MEAL." |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A cathedral of cheese where excess is craft and the fork is the only casualty"
- **Color Mood:** Cheese gold and port-city orange over aluminum silver — bright, greasy, joyful; noticeably brighter than Leeman's
- **Lighting:** Bright fluorescent base + the salamander's warm broiler glow as the compositional heart + exterior neon at night
- **Texture:** Bubbling Gouda gloss, dented aluminum, grease sheen on every counter, laminated menu shine

### Environmental Storytelling:
- The Wall of Fame's empty slots are an open challenge visible from the door
- One döner tower (focused) vs. Leeman's three — different philosophy, same district
- The fork dispenser beside the replacement fork cup admits the truth before Wim says it
- The layer-explanation sign converts confusion into evangelism at the threshold

### Character Integration Notes:
- Wim's 128px sprite towers over every scene — warmth at scale, always visible over the counter
- Kemal holds the salamander zone; his bubble-watch frames pair with the glow pulse
- Customer groups render as single blocks; individual featured NPCs (First-Timer, Champion) carry the story beats
- Food Coma slump must read as bliss, not distress — no regrets in this establishment

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Fork Break** — frame 3's two-halves disbelief, the universal kapsalon experience
2. **The Cross-Section Diagram** — five labeled layers of beautiful chaos, instantly shareable
3. **Wall of Fame Induction** — camera flash, photo sliding into place, eternal recognition
4. **The Salamander Glow** — bubbling Gouda in golden light, ASMR bait
5. **The "No Small" Sign** — "There Is No Small. There Is Only 'You Are Not Ready' And 'Regular.'"

### Quote Potential:
- "You want small? There is no small. There is only 'you are not ready' and 'regular.'"
- "The fork breaks because you eat with passion. Get another fork."
- "In the port city, we put cheese on everything. This is the Shamsterdam way. Accept it."
- "The coma is the body's respect for what you've eaten. Accept the coma."
- "Both sauces? You understand. You have achieved understanding."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | kapsalon_interior_main.png | 1920x1080 |
| 2 | kapsalon_exterior_fixtures.png | 1024x1024 |
| 3 | kapsalon_food_items.png | 512x256 |
| 4 | npc_wim_kemal.png | 512x512 |
| 5 | npc_kapsalon_customers.png | 1024x256 |
| 6 | kapsalon_effects.png | 512x256 |
| 7 | kapsalon_ui.png | 512x512 |

**Total Estimated Memory:** ~19 MB in-memory (uncompressed RGBA worst case), within the 34 MB location budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `kapsalon_interior_main.png` (1920x1080)
- [ ] `kapsalon_exterior_fixtures.png` (1024x1024)
- [ ] `kapsalon_food_items.png` (512x256)
- [ ] `npc_wim_kemal.png` (512x512)
- [ ] `npc_kapsalon_customers.png` (1024x256)
- [ ] `kapsalon_effects.png` (512x256)
- [ ] `kapsalon_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + assembly-line layer order guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: fork break trilogy, "No Small" sign, Wall of Fame empty slots, the lying Fork Integrity icon
- [ ] Accessibility visual alternatives included for all audio cues (sizzle-bubble, SNAP, sauce squirt, recovery chime)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (celebrating the absurdity, never mocking the culture)
- [ ] Hidden areas/interactions have discoverable visual cues (Wall of Fame slots, Both Sauces reverence highlight, Battle Tray)
- [ ] Performance optimized (CPU particles, atlas limits respected, static assembly fallback)
- [ ] Touch zone sizing considered (44px minimum for size/sauce/meat options)
- [ ] Colorblind-friendly alternatives available where color codes meaning (sauce container shapes, segmented risk meter)
- [ ] Social media viral potential maximized in composition choices (fork break framing, cross-section diagram)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam late-night district; origin story told as "the port city" in all in-world text |
| Cultural Specificity | ✅ | Dutch-Turkish kapsalon fusion, 2003 barber origin story, Gouda-because-Dutch |
| Satirical Targets Appropriate | ✅ | The eating experience and bro portion hubris — the fusion culture is celebrated |
| Seedy Underbelly Present | ✅ | 1200-calorie 3 AM cardiovascular events, cheese-on-everything philosophy at its conclusion |
| Gameplay Value Established | ✅ | Ordering system, two status effects, fork event, King Size challenge, collectible tray |
| Technical Feasibility | ✅ | Static assembly/cheese fallbacks per profile; overlay-based glow; group blocks |
| Performance Budget | ✅ | 60 FPS, 14 draw calls, 34 MB, 15 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all audio cues, reduced-motion set, 44px touch zones |
| No Crypto Elements | ✅ | Pure cheese-based currency of satisfaction |
| Social Media Integration | ✅ | 5 screenshot moments + 5 quotable lines identified |

**Once these assets ship, Kapsalon Koning becomes the game's monument to glorious excess: a glowing aluminum tray, a doomed plastic fork, and a 6'5" evangelist who believes cheese can fix you — and is not entirely wrong.**
