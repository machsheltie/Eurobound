# Bicycle Warfare Accessories - Complete PNG Asset Requirements

## 📋 Overview
Bicycle Warfare Accessories ("Fietsbel & Meer") is the narrow shop wedged between the tourist bike rentals near Central Station that sells bells like ammunition — a military surplus store for people about to lose a war they don't know they've entered. This document specifies every PNG asset for the shop: the exterior with its warning signage, the interior with the five-tier Bell Wall arsenal and danger-zone war room maps, Werner and Koen, the five atmospheric customer archetypes, all eleven purchasable accessories, effects, and UI. Its satirical essence in a sentence: selling +Confidence to tourists who need +Skill.

**Location ID:** `shamsterdam_central_bicycle_warfare_01`
**Theme:** Tourist cycling overconfidence vs. Dutch bike-lane reality; accessory-as-solution thinking treated with military seriousness
**Zone:** Near Central Station, tourist bicycle rental district
**Hours:** 8 AM - 8 PM (tourist cycling hours, carnage window)
**Primary Function:** Accessory vendor / survival equipment shop — bell tier purchase system, bell test mechanic, "Equipped" +Confidence buff, danger map, cycling achievement track integration

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Warning Orange | #FF6600 | Signage, danger accents, Tier 4 displays |
| Chrome Bell | #C0C0C0 | Bell metal, shine highlights |
| Tactical Gray | #4A4A4A | Walls, floor, military surplus mood |
| Blood Red | #8B0000 | RED danger zones on maps, warning text |
| Route Green | #2D6A4F | GREEN safe zones on maps |
| Retail Glare | #FFF8DC | Harsh retail lighting wash |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/bicycle_warfare_accessories/
├── environment/
│   ├── bicycle_warfare_exterior.png
│   └── bicycle_warfare_interior.png
├── npcs/
│   ├── npc_werner_koen.png
│   └── npc_bwa_customers.png
├── objects/
│   └── bwa_items.png
├── effects/
│   └── bwa_effects.png
└── ui/
    └── bwa_ui.png
```

---

## 🏪 Sprite Sheet 1: Shop Exterior & Street
**File:** `bicycle_warfare_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** Tactical Gray #4A4A4A base, Warning Orange #FF6600 signage, Chrome #C0C0C0 window display

### Storefront:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shop Facade Base | (0, 0) | 384x384 | Narrow storefront between rentals, gray brick, tactical trim |
| Window Bell Display | (384, 0) | 256x256 | Hundreds of bells displayed like ammunition racks |
| Shop Door | (384, 256) | 96x128 | Heavy door, "PREPARE" decal |
| Door (Open State) | (480, 256) | 96x128 | Interior glow variant for entry transition |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign | (640, 0) | 320x64 | "BICYCLE WARFARE ACCESSORIES" stenciled military font |
| Tagline Sign | (640, 64) | 320x32 | "Because They Won't Hear You Coming — Make Them" |
| Secondary Sign | (640, 96) | 256x32 | "Bells • Lights • Mirrors • Prayers" |
| Warning Sign | (640, 128) | 192x64 | "The bike path is not your friend. Prepare accordingly." |
| Honest Addition Sign | (640, 192) | 192x32 | "Bells are mandatory. Survival is optional." |

### Street Context:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Adjacent Rental Shops | (0, 384) | 512x128 | Bike rental frontage strip — customer source, confused tourists emerging |
| Bike Path Glimpse | (512, 384) | 512x128 | The battlefield: bike lane with motion-blurred Dutch cyclists |

### Technical Notes:
- Bike Path Glimpse scrolls horizontally (parallax layer) — cyclists pass at 3x tourist speed
- Window Bell Display gets chrome shine sparkle overlay from effects sheet
- Signage must remain legible at 50% mobile scale — minimum 10px cap height

---

## 🔔 Sprite Sheet 2: Interior Tileset & The Bell Wall
**File:** `bicycle_warfare_interior.png`
**Dimensions:** 1024x1024 pixels

### Structural Tiles (32x32):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Tactical Gray | (0, 0) | 32x32 | Base retail floor |
| Floor Worn Path | (32, 0) | 32x32 | Darker path from counter to bell wall |
| Wall Panel Gray | (64, 0) | 32x32 | Base wall |
| Wall Pegboard | (96, 0) | 32x32 | Bell mounting surface |
| Ceiling Tile | (128, 0) | 32x32 | Standard ceiling |
| Harsh Light Fixture | (160, 0) | 64x32 | Retail glare source, bells reflect it |
| Wall Corner | (224, 0) | 32x32 | Interior corner |
| Entry Mat | (256, 0) | 64x32 | "WELCOME TO THE WAR" doormat |

### The Bell Wall Arsenal (Tier Displays):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tier 1 Display — The Pacifists | (0, 64) | 192x128 | Polite classic ding bells, €5-8 tags, gentle presentation |
| Tier 2 Display — The Compromisers | (192, 64) | 192x128 | DING-DING bells, €10-15, hopeful arrangement |
| Tier 3 Display — The Asserters | (384, 64) | 192x128 | Dual-tone bells, €15-20, serious mounting brackets |
| Tier 4 Display — The Dominators | (576, 64) | 192x128 | Air horns and sirens, €20-25, caged like ordnance |
| Tier 5 Display — The Delusional | (768, 64) | 192x128 | "Smart bells," GPS units, €30+, glowing app icons |

### Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Counter | (0, 192) | 256x128 | Where strategy is discussed and fates are sealed |
| Testing Area | (256, 192) | 256x128 | Try-before-you-buy station, soundproofing foam (decorative) |
| Helmet Corner | (512, 192) | 128x128 | Helmets separated, hand-written "for beginners" sign |
| Accessory Rack | (640, 192) | 128x128 | Mirrors, lights, ponchos on hooks |
| Bell Crate Stack | (768, 192) | 128x128 | Ammunition-style wooden crates of bell stock |

### The Map Section (War Room):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tourist Route Map | (0, 320) | 384x256 | Color-coded danger levels: GREEN parks → RED station area; pattern overlays per zone |
| The "Don't" List | (384, 320) | 192x256 | Areas to avoid — the list is most of central Shamsterdam |
| Local Route Map | (576, 320) | 192x256 | Where Dutch people actually bike; deliberately unreadable symbols |
| Danger Zone Legend | (768, 320) | 192x128 | Color/pattern coding explanation card |

### Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Warning Posters | (768, 448) | 64x96 | "FEAR IS WISDOM" and tram-vs-bike diagram |
| Werner's Newspaper Clippings | (832, 448) | 64x96 | Framed collision headlines behind counter |
| Rain Cloud Barometer | (896, 448) | 64x64 | Always predicts rain ("Not if. When.") |

### Technical Notes:
- Bell Wall tier displays are separate sprites so individual tiers can highlight during selection
- Map danger zones must carry hatching patterns in addition to color (colorblind rule)
- Counter and Testing Area are interaction hotspots — 44px minimum touch zones

---

## 👥 Sprite Sheet 3: Werner & Koen
**File:** `npc_werner_koen.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 pixels

### Vendor Werner (bike path veteran, thousand-yard stare):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Werner Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Lean cyclist build, arms crossed, watching the door |
| Werner "Good Luck" 1-2 | (128, 0) / (192, 0) | 64x96 each | Solemn nod to under-equipped customer — he means it |
| Werner Assessing 1-3 | (0, 96) / (64, 96) / (128, 96) | 64x96 each | Looks customer up and down, prescribes equipment |
| Werner Demonstrating 1-3 | (0, 192) / (64, 192) / (128, 192) | 64x96 each | Bell technique demo — squeeze, ring, meaningful stare |

### Assistant Koen (casual competence, baffled by tourists):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Koen Idle 1-2 | (0, 288) / (64, 288) | 64x96 each | Relaxed lean, too comfortable to understand fear |
| Koen Demo Ding 1-2 | (128, 288) / (192, 288) | 64x96 each | "You just... squeeze it. Like this. *ding*" |
| Koen Watching Worried 1-2 | (0, 384) / (64, 384) | 64x96 each | Watching a tourist wobble away — "Should I call someone? In advance?" |

### Technical Notes:
- Werner's stare should never fully blink during Assessing — characterization detail
- Both NPCs are counter fixtures; no walk cycles required

---

## 🧳 Sprite Sheet 4: Customer NPCs
**File:** `npc_bwa_customers.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 pixels

### Customer Archetypes:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Over-Preparer Idle 1-3 | (0, 0) / (64, 0) / (128, 0) | 64x96 each | Every accessory bought, still terrified, fidget loop |
| Under-Preparer Idle 1-3 | (0, 96) / (64, 96) / (128, 96) | 64x96 each | Pure confidence, dismissive wave: "I'll just be careful" |
| Returning Customer 1-3 | (0, 192) / (64, 192) / (128, 192) | 64x96 each | Shaken, holding slightly bent bell, pointing at Tier 4 |
| Local Gift Buyer 1-2 | (0, 288) / (64, 288) | 64x96 each | Amused Dutch local buying rainbow bell for niece |
| Survivor Idle 1-2 | (0, 384) / (64, 384) | 64x96 each | Haunted eyes, end-of-trip pride |
| Survivor Trophy Hold | (128, 384) | 64x96 | Raising souvenir bell like a medal |

### Technical Notes:
- Customers rotate — max 2 concurrent in shop (draw call budget)
- Returning Customer only spawns after any bro completes one bike sequence

---

## 🛎️ Sprite Sheet 5: Item Sprites
**File:** `bwa_items.png`
**Dimensions:** 256x256 pixels

### Products (full inventory table coverage):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Classic Ding Bell (Tier 1) | (0, 0) | 32x32 | €5 — polite, ignored by all |
| Assertive Bell (Tier 2) | (32, 0) | 32x32 | €12 — noticed by some |
| Serious Dual-Tone (Tier 3) | (64, 0) | 32x32 | €15-20 — actual communication |
| Tactical Air Horn (Tier 4) | (96, 0) | 48x32 | €22 — psychological warfare |
| Smart Bell App (Tier 5) | (144, 0) | 32x32 | €35 — tech delusion, tiny glowing screen |
| Bike Mirror | (176, 0) | 32x32 | €8 — see death coming |
| Front Light | (208, 0) | 32x24 | €10 — legally mandatory, practically useful |
| Rear Light | (0, 32) | 32x24 | €10 — red, always red, not negotiable |
| Bike Helmet | (32, 32) | 48x48 | €25 — +Protection, -Shamsterdam Cred |
| Rain Poncho | (80, 32) | 48x48 | €8 — it WILL rain |
| Survival Map | (128, 32) | 48x64 | €5 — knowledge and terror |
| Combination Package | (176, 32) | 64x64 | €40 — tourist survival bundle box |

### Price Tags & Tier Markers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tier Tags 1-5 | (0, 96) to (128, 96), 32px steps | 32x16 each | Roman-numeral tier chips for wall displays |
| Sale Sticker | (160, 96) | 32x16 | Never actually a sale |

### Technical Notes:
- All items also render on the equipped bike sprite (Technical Integration) — keep silhouettes readable at 50%
- Air Horn is the only non-square bell item; UI grid must accommodate 48px width

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `bwa_effects.png`
**Dimensions:** 256x256 pixels

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Small Ring Wave 1-3 | (0, 0) / (32, 0) / (64, 0) | 32x32 each | Tier 1-2 test ring: modest concentric wave |
| Big Ring Wave 1-3 | (96, 0) / (144, 0) / (192, 0) | 48x48 each | Tier 3 dual-tone: bolder double wave |
| Horn Blast Cone 1-4 | (0, 64) / (64, 64) / (128, 64) / (192, 64) | 64x64 each | Tier 4 test: expanding shock cone, window rattle lines |
| Chrome Shine Sparkle 1-4 | (0, 128) / (16, 128) / (32, 128) / (48, 128) | 16x16 each | Bell wall glint under retail lighting |
| Confidence Buff Aura 1-3 | (64, 128) / (112, 128) / (160, 128) | 48x64 each | Orange glow around customer on purchase — false security made visible |
| Dust Motes 1-2 | (0, 192) / (32, 192) | 32x32 each | Determined atmosphere particles |
| Neighbor Reaction "!?" | (64, 192) | 32x32 | Popup over adjacent shops during horn test |

### Technical Notes:
- Ring waves scale with bell tier — the comedy build of the bell test escalation
- Confidence Aura uses additive blend; capped at 1 instance
- All particles via CPUParticles2D, max 20 concurrent

---

## 🗺️ Sprite Sheet 7: UI Elements
**File:** `bwa_ui.png`
**Dimensions:** 512x384 pixels

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bell Tier Selection Panel | (0, 0) | 256x192 | Five-tier volume comparison with waveform bars |
| Danger Map UI | (256, 0) | 256x192 | "Where not to go" interactive map with pattern-coded zones |
| Equipment Inventory Panel | (0, 192) | 192x128 | What you've got vs. what you need |
| Bike Equipped Status | (192, 192) | 128x64 | Items rendered on bike silhouette |
| Confidence Buff Icon | (320, 192) | 32x32 | +Confidence status (false security) |
| Cycling Survival Badge | (352, 192) | 64x64 | "You made it" achievement art |
| Bravado Delta Chips | (192, 256) | 32x32 each, x192-x288 (3 chips) | +Bravado / -Bravado / neutral indicators |

### Technical Notes:
- Tier selection waveform bars double as the colorblind-safe volume indicator
- All interactive UI zones minimum 44px

---

## 🎬 Animation Specifications

### Bell Test Ding (Sheets 2, 6):
- **Duration:** 0.4 seconds per ring (3 frames at ~8 FPS), single play
- **Frames:** 3 (ring wave)
- **Pattern:** Squeeze → wave frame 1 → 2 → 3 → fade
- **Trigger:** Player tests bell at Testing Area
- **Purpose:** Comedy escalation — each tier louder than expected
- **Audio Sync:** Distinct bell tone per tier, onset locked to wave frame 1
- **Mobile Optimization:** None needed

### Horn Blast Test (Sheet 6):
- **Duration:** 0.8 seconds (4 frames at 5 FPS), single play + 0.4s neighbor "!?" popup
- **Frames:** 4 blast cone + 1 reaction
- **Pattern:** Cone expands frames 1→4; "!?" appears over adjacent shops at frame 3
- **Trigger:** Player tests Tier 4 air horn
- **Purpose:** Peak of the bell test comedy build; shop neighbors react
- **Audio Sync:** Air horn blast at frame 1, muffled neighbor complaint at frame 4
- **Mobile Optimization:** Drop window-rattle lines on Low LOD

### Werner Assessment (Sheet 3):
- **Duration:** 1.5 seconds (3 frames at 2 FPS), plays once per consultation
- **Frames:** 3
- **Pattern:** Head tilt down → up → prescription stare, hold on frame 3
- **Trigger:** Player initiates purchase consultation
- **Purpose:** The Werner Method — assess, prescribe, hope
- **Audio Sync:** Low "hmm" on frame 2
- **Mobile Optimization:** None needed

### Customer Decision Anxiety (Sheet 4):
- **Duration:** 2 second fidget loop (3 frames at 1.5 FPS)
- **Frames:** 3 per archetype
- **Pattern:** Loop while customer NPC active
- **Trigger:** Constant on spawned customers
- **Purpose:** Ambient tension; everyone in here is scared or should be
- **Audio Sync:** None
- **Mobile Optimization:** Static frame 1 on Low LOD

### Bell Wall Shimmer (Sheets 2, 6):
- **Duration:** 3-second interval, 0.5-second sparkle (4 frames at 8 FPS)
- **Frames:** 4
- **Pattern:** Random bell position on wall → sparkle → wait
- **Trigger:** Constant ambient
- **Purpose:** The arsenal gleams; harsh retail lighting on chrome
- **Audio Sync:** None
- **Mobile Optimization:** Disabled on Low LOD

### Confidence Buff Aura (Sheet 6):
- **Duration:** 1 second (3 frames at 3 FPS), single play then icon persists
- **Frames:** 3
- **Pattern:** Aura blooms → settles → transfers to status icon
- **Trigger:** Any purchase completed
- **Purpose:** Visualizes +Confidence (not +Survival)
- **Audio Sync:** Cash register "ka-ching" at frame 1
- **Mobile Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter/Testing Area outlines | Sheet 7, (352, 256) | 64x64 | Bold-outline hotspot markers for the two interaction zones |
| Bell tier high-contrast chips | Sheet 7, (416, 256) | 32x32 x2 (x416, x448) | Numbered I-V chips replacing color-tier coding |
| NPC interaction highlight | Sheet 7, (416, 288) | 64x96 | Outline variant marking Werner/Koen as interactive |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static shine variant | Sheet 6, (96, 192) | 16x16 | Non-animated glint dot replacing sparkle loop |
| Steady confidence icon | Sheet 7, (320, 224) | 32x32 | Non-pulsing buff icon variant |
| Reduced horn blast | Sheet 6, (128, 192) | 64x64 | Single static cone frame, no expansion strobe |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bell volume waveform icons | Sheet 7, (0, 320) | 48x32 x5 (x0-x240, 48px steps) | Per-tier waveform size mirrors of the test audio — the volume joke survives muting |
| Neighbor reaction popup | Sheet 6, (64, 192) | 32x32 | Visual mirror of off-screen complaint audio |
| Ka-ching visual chip | Sheet 7, (256, 320) | 32x32 | Coin burst mirroring register audio |

### Colorblind Considerations:
- Danger map zones use hatching patterns (GREEN solid / YELLOW dots / ORANGE stripes / RED crosshatch), never color alone
- Bell tiers carry Roman numeral chips I-V in addition to display color
- Touch zones minimum 44px for counter, testing area, tier selection, and all purchase buttons

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC (fallback PVRTC 4BPP); map section and signage need higher quality (readable text)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for Tourist Route Map (danger-zone text must be legible)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| bwa_environment | exterior, interior/bell wall | 2048x1024 |
| bwa_characters | Werner/Koen, customers | 1024x512 |
| bwa_effects | items, effects, UI | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full shine sparkles, all customer fidget loops, parallax bike path, horn rattle lines |
| Medium | Reduced sparkle frequency, 1 ambient customer, static bike path |
| Low | Simplified bell variety (per profile), static map, no shine effects, static customers |

### Performance Targets:
- **Target FPS:** 45 (per location profile performance budget)
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 30 MB maximum
- **Particle Limit:** 20

### Performance Notes:
- Profile-mandated: simplified bell variety, static map, reduced shine effects on low-end devices
- Single-room interior — load exterior/interior as separate scenes to stay under draw call cap
- Bike path parallax is the only scrolling layer; disable below Medium LOD

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (interior), AnimatedSprite2D (NPCs, ring waves), CPUParticles2D (dust, sparkles — not GPU), CanvasLayer (tier selection / map UI), ParallaxBackground (bike path glimpse)
- Special systems: bell tier test resolver (tier → wave sprite + audio + neighbor reaction), "Equipped" status compositor (items drawn onto bike sprite), Werner internal rating tracker (Tourist Type / Survival Prediction), Bravado hooks on purchase dialogue choices

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Ring wave frames (per tier) | Tier-specific bell tone (escalating volume) | Onset at wave frame 1 |
| Horn blast cone | Air horn + muffled neighbor complaint | Horn frame 1, complaint frame 4 |
| Confidence aura | Cash register ka-ching | Frame 1 |
| Werner Assessing | Low "hmm" | Frame 2 |
| Bike path glimpse | Passing cyclist whoosh + tram bell (distant, the real threat) | On cyclist sprite crossing screen center |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Cycling Achievement Track — "Equipped" | Any bell item, confidence icon | First purchase |
| Cycling Achievement Track — "Over-Prepared" | Combination Package, inventory panel | Full kit purchase |
| Cycling Achievement Track — "Aggressor" | Tactical Air Horn, blast cone | Tier 4 selection |
| Cycling Achievement Track — "Veteran" | Returning Customer slot logic, survival badge | Player returns post-ride |
| Bike Path Combat (external system) | All item sprites on bike equipped status | Bell/horn/mirror/light/helmet ability icons |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Shamsterdam Bike Rental | Adjacent Rental Shops strip | Natural customer flow; shared street facade |
| Central Station | Danger map RED zone marker | Map highlights on quest reference |
| Canal Bridges (Canal Ring Promenade) | Danger map ORANGE zone marker | Bell-heavy chokepoint callout |
| Park zone ("Vondelpark" in profile — see validation) | Danger map GREEN zone marker | Beginner-area map reference |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A military surplus store that sells bicycle bells with complete sincerity"
- **Color Mood:** Tactical gray oppression cut by warning orange and chrome gleam — retail as war room
- **Lighting:** Harsh flat retail glare; every bell reflects it like polished brass ammunition
- **Texture:** Clean, organized, dead serious — the absurdity comes from the sincerity, not from clutter

### Environmental Storytelling:
- Bells organized by volume like escalating ordnance tells the whole tier system at a glance
- Helmet Corner physically separated with a hand-written "for beginners" sign — Dutch judgment in furniture form
- Framed collision headlines behind Werner's counter explain why he opened the shop without a word of dialogue
- The "Don't" List covering most of central Shamsterdam is the punchline hung on a wall

### Character Integration Notes:
- Werner is a counter fixture; his stillness contrasts with fidgeting customers
- Koen drifts between counter and testing area — the only relaxed body in the room
- Max two atmospheric customers rendered at once; archetypes rotate per visit

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Bell Wall Arsenal** - Five tiers of bells displayed like weaponry; instantly readable satire
2. **The Danger Map** - "The list is most of central Shamsterdam" — shareable map humor
3. **Horn Test Neighbor Reaction** - "!?" popping over adjacent shops mid-blast
4. **Werner's Good Luck Nod** - The solemn send-off to an under-equipped tourist

### Quote Potential:
- "The bell is your only warning. Use it wisely. They won't listen."
- "Thirty years I've lived in Shamsterdam. Twenty years on bikes. I've never stopped being afraid. Fear is wisdom."
- "I don't sell bells. I sell warnings. The bell is just the delivery mechanism."
- "Bells are mandatory. Survival is optional."
- "Wait, you've never biked in a city? But... how do you get places?"

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | bicycle_warfare_exterior.png | 1024x512 |
| 2 | bicycle_warfare_interior.png | 1024x1024 |
| 3 | npc_werner_koen.png | 512x512 |
| 4 | npc_bwa_customers.png | 512x512 |
| 5 | bwa_items.png | 256x256 |
| 6 | bwa_effects.png | 256x256 |
| 7 | bwa_ui.png | 512x384 |

**Total Estimated Memory:** ~9 MB raw RGBA texture data; ~30 MB maximum total footprint (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `bicycle_warfare_exterior.png` (1024x512)
- [ ] `bicycle_warfare_interior.png` (1024x1024)
- [ ] `npc_werner_koen.png` (512x512)
- [ ] `npc_bwa_customers.png` (512x512)
- [ ] `bwa_items.png` (256x256)
- [ ] `bwa_effects.png` (256x256)
- [ ] `bwa_ui.png` (512x384)

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
- **Documentation:** Animation timing reference sheet + bell tier audio/waveform mapping table

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: five-tier arsenal escalation, "for beginners" helmet corner, "Don't" List coverage, Werner's thousand-yard stare
- [ ] Accessibility visual alternatives included for all audio cues (bell tones, horn blast, register)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (military sincerity applied to bell retail)
- [ ] Hidden areas/interactions have discoverable visual cues (testing area foam, tier highlight states)
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (map hatching, tier numerals)
- [ ] Social media viral potential maximized in composition choices (bell wall as hero shot)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ❌ | Profile's danger map lists real place names ("Vondelpark", "Dam Square", also "Amsterdam" in flavor copy) — this spec substitutes generic zone labels, but source profile needs in-world renames |
| Cultural Specificity | ✅ | Dutch bike culture supremacy vs. tourist unpreparedness |
| Satirical Targets Appropriate | ✅ | Tourist overconfidence and accessory-as-solution thinking; Dutch cyclists respected as apex predators |
| Seedy Underbelly Present | ✅ | Selling confidence to people who need skills; +Confidence not +Survival |
| Gameplay Value Established | ✅ | Bell tier purchases, test mechanic, equipped status, achievement track, bike combat hooks |
| Technical Feasibility | ✅ | Single-room shop, CPU particles, one parallax layer documented |
| Mobile Performance Budget | ✅ | 45 FPS, 12 draw calls, 30 MB per profile budget |
| Accessibility Features | ✅ | Waveform volume mirrors, map hatching, reduced-motion variants, 44px zones |
| No Crypto Elements | ✅ | Pure analog cycling equipment (Tier 5 "smart bell" is satire of tech, no blockchain) |
| Social Media Integration | ✅ | 4 screenshot moments + quote bank identified |

**Once these assets are delivered, Bicycle Warfare Accessories becomes the player's first taste of Shamsterdam's true combat system: a dead-serious armory for a war fought in bike lanes, where every purchase buys confidence and the bike path collects the difference.**
