# Hostel "Midnight Checkout" - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Hostel "Midnight Checkout" - where sleep is theoretical, privacy is fictional, and someone is ALWAYS in your bed.

**Location ID:** `debaucheryville_hostel_midnight_checkout_01`  
**Theme:** Universal hostel experience - beautiful chaos of 40 strangers, passive-aggressive kitchen politics, bunk bed confessions at 3 AM  
**Zone:** Hostel Row, Budget Accommodation District (Debaucheryville)  
**Hours:** 24/7 reception (theoretically - receptionist presence varies)  
**Primary Function:** Rest point, stat restoration, confession system, roommate events, Hostel Bonds

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Budget Beige | #D4C4A8 | Facade, walls, main surfaces |
| Hostel Blue | #4169E1 | Signage accents, UI panels, bunk frames |
| Institutional Green | #8FBC8F | Background walls, corridors |
| Warning Red / Neon | #FF6347 | Neon sign, warning notes, alarm effects |
| Faded Wood | #8B4513 | Ornate doorframe, worn furniture |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/hostel_midnight_checkout/
├── environment/
│   ├── hostel_exterior.png
│   ├── reception_lobby.png
│   ├── common_room.png
│   ├── kitchen_full.png
│   ├── dorm_rooms_combined.png
│   └── bunk_bed_detail.png
├── npcs/
│   ├── hostel_staff_sprites.png
│   └── hostel_guest_sprites.png
├── effects/
│   ├── hostel_effects.png
│   └── confession_scene.png
└── ui/
    └── hostel_ui.png
```

---

## 🏨 Sprite Sheet 1: Hostel Exterior
**File:** `hostel_exterior.png`  
**Dimensions:** 384x384 pixels  
**Color Palette:** #D4C4A8 (budget beige), #FF6347 (neon red), #8B4513 (faded wood)

### Facade Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Building Base | (0, 0) | 384x256 | 19th-century converted building |
| Ornate Doorframe | (0, 256) | 96x128 | Faded grandeur entrance |
| Window + AC | (96, 256) | 64x64 | Random AC unit placement |
| Window No AC | (160, 256) | 64x64 | Basic window |
| Peeling Paint | (224, 256) | 64x64 | Character-building texture |

### Neon Sign (192x48 each):
| State | Position | Description |
|-------|----------|-------------|
| Full On | (0, 320) | All letters lit |
| Two Letters Out | (192, 320) | Flickering state |

**Visual Notes:** Faded grandeur, peeling paint "in character-building shades," plastic signage contrasting ornate doorframe

---

## 🛎️ Sprite Sheet 2: Reception Lobby
**File:** `reception_lobby.png`  
**Dimensions:** 512x384 pixels  

### Reception Desk:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter | (0, 0) | 192x96 | Understaffed chaos |
| Clipboard System | (192, 0) | 64x48 | Paper-based tracking |
| Key Hooks | (256, 0) | 96x64 | Half-empty always |
| Bell | (352, 0) | 32x32 | May summon staff |

### Lobby Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Worn Couch | (0, 96) | 128x64 | Seen better decades |
| Mismatched Chairs | (128, 96) | 96x64 | No two alike |
| Notice Board | (224, 96) | 96x96 | Tour offers, complaints |

---

## 🛋️ Sprite Sheet 3: Common Room
**File:** `common_room.png`  
**Dimensions:** 512x384 pixels  

### Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mismatched Sofa | (0, 0) | 128x72 | Territorial seating |
| Bean Bag | (128, 0) | 64x56 | First-come claimed |
| Cheap Table | (192, 0) | 80x48 | Wobbly |
| SINGLE Working Outlet | (272, 0) | 32x32 | THE contested resource |

### Wi-Fi Corner:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corner Setup | (0, 72) | 96x80 | The reliable signal spot |
| Occupied Sign | (96, 72) | 48x24 | Usually applies |

---

## 🍳 Sprite Sheet 4: Kitchen
**File:** `kitchen_full.png`  
**Dimensions:** 384x384 pixels  

### Appliances:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stove (1 Burner) | (0, 0) | 96x80 | ONE working, contested |
| Microwave 2007 | (96, 0) | 48x40 | Ancient, functional |
| Fridge Chaos | (144, 0) | 64x128 | Labels ignored |

### The Note Wall (CRITICAL):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Board Base | (0, 128) | 128x96 | Passive-aggressive gallery |
| Notes Layer 1 | (128, 128) | 128x96 | First wave |
| Notes Layer 2 | (256, 128) | 128x96 | Escalation |

### Individual Notes:
| Note | Position | Size | Text |
|------|----------|------|------|
| Label Food | (0, 224) | 64x32 | "LABEL YOUR FOOD" |
| Not Yours | (64, 224) | 48x32 | "THIS IS NOT YOURS" |
| Cheese | (112, 224) | 64x32 | "WHO TOOK MY CHEESE" |
| Dishes | (176, 224) | 56x32 | "We need to talk..." |

---

## 🛏️ Sprite Sheet 5: Dorm Rooms Combined
**File:** `dorm_rooms_combined.png`  
**Dimensions:** 1024x512 pixels  

### Room Layouts:
| Room | Position | Size | Chaos Level |
|------|----------|------|-------------|
| 12-Bed Dorm | (0, 0) | 512x384 | Maximum |
| 8-Bed Dorm | (512, 0) | 384x384 | High |
| 6-Bed Dorm | (0, 384) | 384x128 | Moderate |
| 4-Bed Dorm | (384, 384) | 256x128 | Manageable |

**Dorm Visual Notes:**
- 60% functional ladders visible
- Lockers requiring "exact key technique"
- Mix of curtained/uncurtained bunks
- Personal items scattered
- Varying mattress quality visible

---

## 🛏️ Sprite Sheet 6: Bunk Bed Detail
**File:** `bunk_bed_detail.png`  
**Dimensions:** 256x256 pixels  

### Bunk Frame:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Metal Frame | (0, 0) | 96x160 | Various ages, distinctive sounds |
| Ladder Functional | (96, 0) | 32x80 | 60% of bunks |
| Ladder Broken | (128, 0) | 32x80 | 40% of bunks |

### Mattress States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Standard | (0, 160) | 80x24 | Thin but acceptable |
| Saggy | (80, 160) | 80x24 | Unique topography |
| Lumpy | (160, 160) | 80x24 | Character building |

### Privacy Curtain:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Open | (160, 0) | 48x80 | No privacy |
| Closed | (208, 0) | 48x80 | 40% of bunks |

### Personal Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Bunk Light Off | (0, 184) | 24x16 | Individual reading light |
| Bunk Light On | (24, 184) | 24x16 | Lit state |
| Backpack | (48, 184) | 32x40 | Personal storage |
| Phone Charging | (80, 184) | 16x24 | Universal sight |
| Earplugs | (96, 184) | 16x12 | Essential equipment |

---

## 👨‍💼 Sprite Sheet 7: Staff NPCs
**File:** `hostel_staff_sprites.png`  
**Dimensions:** 256x192 pixels  

### Radek (64x96 each):
| State | Position | Description |
|-------|----------|-------------|
| Idle | (0, 0) | Perpetual stubble, thousand-yard stare |
| Checking In | (64, 0) | Processing clipboard |
| Thousand-Yard Stare | (128, 0) | Seen 10,000 travelers |
| Handing Key | (192, 0) | Service mode |

**Radek Visual Notes:** Late 20s Czech, hostel t-shirt, film student who stayed 4 years, helpful but exhausted

### Lenka (64x96 each):
| State | Position | Description |
|-------|----------|-------------|
| Alert | (0, 96) | Nocturnal energy |
| Coffee Dependent | (64, 96) | Always holding cup |
| Philosophical | (128, 96) | 3 AM wisdom mode |

**Lenka Visual Notes:** Early 30s, former traveler who got stuck, curious about guests

---

## 🎒 Sprite Sheet 8: Guest NPCs
**File:** `hostel_guest_sprites.png`  
**Dimensions:** 512x384 pixels  

### Gap Year Gary (Australian):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Friendly | (0, 0) | 64x96 | Overly enthusiastic |
| Confessing | (64, 0) | 64x96 | "Can't go home" |

### Heartbreak Hannah (German):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Journaling | (128, 0) | 64x96 | Processing emotions |
| Emotional | (192, 0) | 64x96 | 3 AM moment |

### Philosophy Phil (American):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Contemplative | (256, 0) | 64x96 | Kerouac visible |
| Deep Conversation | (320, 0) | 64x96 | Finding himself |

### Local Lukáš (Czech Pretending):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Pretending | (384, 0) | 64x96 | Too knowledgeable |
| Revealed | (448, 0) | 64x96 | Caught being local |

### Three-Week Resident:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Territorial | (0, 96) | 64x96 | That's MY outlet |
| Advising | (64, 96) | 64x96 | Unsolicited tips |

### Generic Backpackers:
| Type | Position | Size | Description |
|------|----------|------|-------------|
| Type 1 | (128, 96) | 64x96 | Rotating guest |
| Type 2 | (192, 96) | 64x96 | Different nationality |
| Type 3 | (256, 96) | 64x96 | Various states |
| Snoring Guest | (320, 96) | 64x96 | THE source |
| Party Returner | (384, 96) | 64x96 | 3 AM drunk arrival |

---

## 🎮 Sprite Sheet 9: UI Elements
**File:** `hostel_ui.png`  
**Dimensions:** 384x256 pixels  

### Room Selection:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Panel | (0, 0) | 256x192 | Booking interface |
| 12-Bed Option | (0, 192) | 64x32 | 12 Sovs - Maximum chaos |
| 8-Bed Option | (64, 192) | 64x32 | 16 Sovs - Still chaos |
| 6-Bed Option | (128, 192) | 64x32 | 20 Sovs - Compromise |
| 4-Bed Option | (192, 192) | 64x32 | 28 Sovs - Given up |
| Private Option | (256, 192) | 64x32 | 45 Sovs - Why hostel? |

### Sleep Quality System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Meter Frame | (256, 0) | 128x64 | Quality display |
| Excellent | (256, 64) | 32x32 | +10% stats |
| Good | (288, 64) | 32x32 | Full restore |
| Fair | (320, 64) | 32x32 | 80% restore |
| Poor | (352, 64) | 32x32 | Groggy status |
| None | (256, 96) | 32x32 | Exhausted |

### Status Icons:
| Icon | Position | Size | Description |
|------|----------|------|-------------|
| Groggy | (288, 96) | 32x32 | Poor sleep result |
| Exhausted | (320, 96) | 32x32 | No sleep result |
| Hostel Bond | (352, 96) | 48x48 | Friendship formed |
| Earplugs | (256, 128) | 32x32 | +1 Sleep Tier |

---

## ✨ Sprite Sheet 10: Animation Effects
**File:** `hostel_effects.png`  
**Dimensions:** 256x192 pixels  

### Bunk Creak (64x64 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Frame 1 | (0, 0) | Initial position |
| Frame 2 | (64, 0) | Slight shift |
| Frame 3 | (128, 0) | Return |

### Snore Waves (96x32 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Wave 1 | (0, 64) | Small ripple |
| Wave 2 | (96, 64) | Growing |
| Wave 3 | (0, 96) | Crescendo |
| Wave 4 | (96, 96) | Maximum |

### Other Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Alarm Warfare | (0, 128) | 128x64 | Multiple phones |
| Sleep Interrupt | (128, 128) | 64x64 | Wake-up moment |

---

## 💬 Sprite Sheet 11: Confession Scene
**File:** `confession_scene.png`  
**Dimensions:** 256x192 pixels  

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bunk Setup | (0, 0) | 256x192 | 3 AM conversation scene |
| Dialogue Frame | (0, 144) | 256x48 | Text overlay |

---

## 🎬 Animation Specifications

### Neon Sign Flicker:
- **Pattern:** Full On → Two Letters Out → Full On
- **Timing:** Random 2-5 seconds between flickers
- **Flicker Duration:** 0.3 seconds

### Bunk Bed Creak:
- **Pattern:** Frame 1 → 2 → 3 → 2 → 1
- **FPS:** 6
- **Trigger:** Guest movement or random
- **Audio Sync:** Metal creak sound

### Snore Visualization:
- **Pattern:** Wave 1 → 2 → 3 → 4 (loop)
- **FPS:** 2
- **Visual:** Size scales with volume
- **Trigger:** Snoring roommate event

### Alarm Cascade:
- **Trigger:** Phone Alarm Warfare event
- **Duration:** 30 seconds minimum
- **Visual:** Multiple phone icons flashing

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Working Outlet Highlight | (304, 0) | 32x32 | High-contrast outline for THE contested outlet (common_room.png) |
| Bed Assignment Marker | (192, 128) | 32x32 | Bold numbered marker for player's assigned bunk |
| Reception Bell Outline | (352, 32) | 32x32 | Enhanced visibility interaction target |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon Sign Steady | (0, 320) | 192x48 | Always-on sign state, flicker disabled (hostel_exterior.png) |
| Static Snore Indicator | (192, 64) | 64x32 | Single-frame snore icon replacing animated waves |
| Alarm Static Icon | (192, 128) | 64x64 | Non-flashing alarm warfare indicator |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Snore Waves | (0, 64) | 96x32 | Already-visual cue for snoring roommate (hostel_effects.png) |
| Creak Indicator | (192, 0) | 32x32 | Shake-lines icon when bunk creak audio plays |
| Alarm Flash Frame | (0, 128) | 128x64 | Visual substitute for phone alarm audio |
| Door/Key Indicator | (352, 96) | 32x32 | Key-turn icon for lock audio cue |

### Colorblind Considerations:
- Sleep quality tiers use distinct icon shapes AND text labels (Excellent-None), never color alone
- Roommate event popups use symbols (Zzz, phone, speech bubble) plus text
- Room price options display Sov amounts as text, not color-coded tiers
- Touch zones minimum 44px for booking options, bell, outlet, and bunk interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); note wall text kept higher quality for readability
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for UI panels and passive-aggressive notes (text-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| hostel_environment | exterior, lobby, common room, kitchen | 2048x1024 |
| hostel_dorms | dorm_rooms_combined, bunk_bed_detail | 2048x1024 |
| hostel_characters | staff sprites, guest sprites | 1024x512 |
| hostel_effects_ui | effects, confession scene, UI | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full rotating guest cast animated, dust motes, all roommate event effects |
| Medium | Reduced guest animation rates, simplified snore/creak effects |
| Low | Static background guests, no particles, event popups only |

### Performance Targets:
- **Target FPS:** 60 (multi-room location with crowd rendering)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 38 MB maximum
- **Particle Limit:** 15 (dust motes, laundry steam, kitchen smoke combined)

### Performance Notes:
- Simplified crowd systems: background guests rendered as static sprites beyond 3 active NPCs
- Dorm rooms load on demand per floor; only the occupied dorm is fully animated
- Snore/alarm effects limited to the player's current room

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Multi-room layout: separate scene per floor with shared TileMap resources
- Roommate events: random event controller with weighted trigger table
- Confession scene: dialogue overlay system with dimmed background layer
- Sleep quality: state machine feeding stat restoration modifiers on wake

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Neon sign flicker | Electrical buzz | On flicker frame |
| Bunk creak frames | Metal creak sound | Frame 2 of creak cycle |
| Snore waves | Snoring loop | Wave size scales with volume |
| Alarm warfare | Overlapping phone alarms | On each phone icon flash |
| Reception bell | Bell ding | On player interaction |
| Key hooks | Key jangle | On check-in completion |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Bunk Bed Confessions | confession_scene.png, guest NPC states | 3 AM random event or roommate approach |
| Kitchen Encounters | Note wall layers, individual notes | Peak-hour resource conflicts |
| Gary's Message Home | Gap Year Gary confessing state | Confession unlock chain |
| Hannah's Ex Decision | Heartbreak Hannah emotional state | Confession unlock chain |
| ICQ / Darkweb Dossier | Wi-Fi corner setup | Terminal access in common room |
| Notice Board Quests | Notice board sprite | Tour offers, lost item hooks |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Velvet Curtain Club | Party Returner guest sprite | 3 AM drunk arrival event |
| Shadow Exchange | Staff dialogue references | No visual transition; narrative link |
| 24-Hour Internet Café | Wi-Fi corner (alternative access) | Shared ICQ UI elements |
| Late-Night Kebab Stand | Kitchen defeat dialogue | Post-kitchen-failure exit prompt |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Faded grandeur meets budget renovation - beautiful chaos, affectionately rendered"
- **Color Mood:** Budget beige and institutional green softened by warm bunk lights; neon red accents for the perpetually half-lit sign
- **Lighting:** Harsh fluorescents in common areas, dim dorm corridors, individual bunk reading lights as intimate pools
- **Texture:** Peeling paint in "character-building shades," worn upholstery, industrial sheets, decades of traveler wear

### Environmental Storytelling:
- The passive-aggressive note wall chronicles escalating kitchen warfare without a word of dialogue
- The single working outlet, visibly guarded, tells the story of territorial common-room politics
- 60% functional ladders and mattresses of unique topography signal budget entropy
- Ornate 19th-century doorframe against plastic signage: grandeur surrendered to backpacker economics

### Character Integration Notes:
- Radek reads as helpful-but-exhausted: perpetual stubble, thousand-yard stare, hostel t-shirt
- Lenka carries nocturnal energy: alert posture, ever-present coffee cup
- Guest NPCs are affectionate archetypes, not mockeries - each distinct at 64x96 silhouette read
- Rotating generic backpackers keep dorms feeling alive without heavy animation budgets

---

## 📋 Required PNG Files (11 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | hostel_exterior.png | 384x384 |
| 2 | reception_lobby.png | 512x384 |
| 3 | common_room.png | 512x384 |
| 4 | kitchen_full.png | 384x384 |
| 5 | dorm_rooms_combined.png | 1024x512 |
| 6 | bunk_bed_detail.png | 256x256 |
| 7 | hostel_staff_sprites.png | 256x192 |
| 8 | hostel_guest_sprites.png | 512x384 |
| 9 | hostel_ui.png | 384x256 |
| 10 | hostel_effects.png | 256x192 |
| 11 | confession_scene.png | 256x192 |

**Total Estimated Memory:** ~38 MB (in-memory budget including atlas overhead)

---

## 📦 File Delivery Checklist

### Required PNG Files (11 Total):
- [ ] `hostel_exterior.png` (384x384)
- [ ] `reception_lobby.png` (512x384)
- [ ] `common_room.png` (512x384)
- [ ] `kitchen_full.png` (384x384)
- [ ] `dorm_rooms_combined.png` (1024x512)
- [ ] `bunk_bed_detail.png` (256x256)
- [ ] `hostel_staff_sprites.png` (256x192)
- [ ] `hostel_guest_sprites.png` (512x384)
- [ ] `hostel_ui.png` (384x256)
- [ ] `hostel_effects.png` (256x192)
- [ ] `confession_scene.png` (256x192)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha |
| Color Space | sRGB |
| DPI | 72 |
| Naming | snake_case |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups (note wall notes on separate layers)
- **Documentation:** Animation timing reference sheet (creak, snore, alarm cascade cycles)

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Passive-Aggressive Note Wall** - Kitchen warfare gallery
2. **12-Bed Dorm Chaos** - Maximum hostel experience
3. **Radek's Thousand-Yard Stare** - Seen everything
4. **3 AM Confession Scene** - Deep bunk bed conversations
5. **Single Working Outlet** - THE contested resource
6. **Snore Visualization** - Sleep quality enemy

### Quote Potential:
- "12 Sovs/Night. Your Dignity Costs Extra."
- "Quiet hours are 11 to 7. This is theoretical."
- "Someone is always snoring. This is hostel law."
- "The hostel is democracy. Everyone gets equal chaos."
- "Check-in anytime, checkout never."

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 11 PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Passive-aggressive note wall text is readable at gameplay zoom
- [ ] Radek's thousand-yard stare reads clearly at 64x96
- [ ] Single working outlet is visually distinct as THE contested resource
- [ ] All guest NPC archetypes are distinguishable by silhouette
- [ ] Accessibility visual alternatives included for all audio cues (snore, creak, alarm)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Hostel satire is affectionate toward backpacker culture, not mocking travelers
- [ ] Neon sign flicker and note wall create discoverable visual interest
- [ ] Mobile performance optimized (static background guests, on-demand dorm loading)
- [ ] Touch zone sizing considered (44px minimum for booking UI and interactions)
- [ ] Sleep quality tiers readable without color (shapes + labels)
- [ ] Social media viral potential maximized (note wall, 12-bed chaos compositions)

---

## 🏆 Location Validation Status

| Requirement | Status |
|-------------|--------|
| World Consistency | ✅ PASS |
| Cultural Specificity | ✅ PASS |
| Satirical Targets | ✅ PASS |
| Seedy Underbelly | ✅ PASS |
| Gameplay Value | ✅ PASS |
| Technical Feasibility | ✅ PASS |
| Mobile Performance | ✅ PASS (60 FPS, 16 draws, 38MB) |
| Accessibility | ✅ PASS |
| No Crypto Elements | ✅ PASS |
| Social Media | ✅ PASS |

**Hostel "Midnight Checkout" becomes the essential rest hub where sleep quality affects stats, roommate events create chaos, bunk bed confessions unlock quests, kitchen encounters test social skills, and Radek has seen everything and judges nothing. 12 Sovs buys a bed, 11 strangers, one working shower, and stories you'll tell forever!**
