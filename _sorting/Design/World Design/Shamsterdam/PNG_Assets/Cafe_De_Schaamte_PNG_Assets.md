# Café de Schaamte - Complete PNG Asset Requirements

## 📋 Overview
Café de Schaamte ("Café of Shame") is the canal-side outdoor terrace on the Canal Ring Promenade where €4.50 buys a thimble of espresso and a lifetime supply of Dutch judgment — and where a poorly disguised Sheltie in a SHAMSTERDAM hoodie runs "covert" mission briefings from the corner table. This document specifies every PNG asset for the terrace: the mismatched-furniture environment, the canal/bicycle background layers, Agent Havok's prop-laden table, Barista Willem and Server Margot, Havok and the café regulars, consumables, effects, and the judgment-driven UI. Its satirical essence in a sentence: Americans paying premium prices to be performatively ignored and calling it culture.

**Location ID:** `shamsterdam_canalring_cafe_schaamte_01`
**Theme:** American tourists expecting American service in European establishments; performative European sophistication; Dutch directness vs. tourist obliviousness
**Zone:** Canal Ring Promenade, waterside terrace overlooking main canal
**Hours:** Always accessible (outdoor seating, 24-hour Amsterdam energy; Havok's table mysteriously accessible even when "closed")
**Primary Function:** Outdoor café / quest hub / Agent Havok base of operations — Fabergé Egg Hunt briefing and debrief, café service system with judgment mechanics, consumables, Couchsurf hook, ambient overheard storytelling

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Canal Green | #2E5A4C | Water, awning, terrace accents |
| Espresso Brown | #3C2415 | Coffee, furniture, chalkboard frame |
| Overcast Grey | #B8C4C8 | Sky, cobblestones, ambient light |
| Terrace Cream | #F5F0E6 | Cups, table linens, signage |
| String-Light Amber | #FFD9A0 | Evening lighting |
| Judgment Pink | #FF69B4 | Havok accents, shame/Bravado UI hits |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/cafe_de_schaamte/
├── environment/
│   ├── cafe_terrace_environment.png
│   └── cafe_canal_background.png
├── objects/
│   └── havok_table_props.png
├── npcs/
│   ├── npc_cafe_staff.png
│   └── npc_havok_regulars.png
├── effects/
│   └── cafe_effects.png
└── ui/
    └── cafe_ui.png
```

---

## ☕ Sprite Sheet 1: Terrace Environment
**File:** `cafe_terrace_environment.png`
**Dimensions:** 1024x1024 pixels

### Ground Tiles (32x32):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cobblestone Base | (0, 0) | 32x32 | Canal-side walkway |
| Cobblestone Worn | (32, 0) | 32x32 | Foot-polished variant |
| Cobblestone Bike-Rutted | (64, 0) | 32x32 | Constant bicycle threat evidence |
| Terrace Edge | (96, 0) | 32x32 | Where café spills onto sidewalk |
| Canal Coping Stone | (128, 0) | 32x32 | Water's edge — no railing where you'd want one |

### Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wrought-Iron Table Variants 1-4 | (0, 32) / (96, 32) / (192, 32) / (288, 32) | 96x96 each | Wobbly, mismatched, none level |
| Mismatched Chairs 1-6 | (384, 32) to (544, 32), 32px steps | 32x48 each | Six styles, zero comfort |
| Composed Table Set A / B | (224, 128) / (352, 128) | 128x128 each | Pre-arranged table+chairs clusters for fast terrace layout (12 tables total) |

### Fixtures & Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ancient Espresso Machine | (0, 128) | 128x192 | Older than most American cities; aggressive competence energy |
| Chalkboard Menu | (128, 128) | 96x128 | Prices that make Americans gasp |
| Awning Flutter 1-2 | (0, 320) / (512, 320) | 512x128 each | Ancient fabric awning, two wind frames |
| String Lights | (0, 448) | 512x64 | Evening atmosphere strand |
| Canal Railing | (512, 448) | 256x64 | Where locals lean, smoke, and make disappointed eye contact |
| Geranium Pots 1-3 | (768, 448) / (800, 448) / (832, 448) | 32x48 each | Traditional Dutch cheer vs. ambient judgment |
| Newspaper Stack | (896, 448) | 48x48 | International, weeks old, read incorrectly |
| Communal Ashtray | (944, 448) | 32x32 | Technically illegal, universally ignored |
| Wifi Password Sign | (896, 496) | 64x32 | "FREE WIFI — Password: 'OrderSomethingFirst'" |

### Signage & Detail:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Faded Café Photos 1-3 | (0, 512) / (48, 512) / (96, 512) | 48x48 each | Decades of confused tourists in every era |
| Counter/Bar Front | (144, 512) | 256x128 | Order point, Willem's domain |
| Hand-Painted Sign | (400, 512) | 192x64 | "Café de Schaamte" |
| Sub-Sign | (400, 576) | 192x32 | "Est. 1847 — Judging Tourists Since 1967" |
| Handheld Menu | (592, 512) | 48x96 | Tourist confusion prop |

### Technical Notes:
- Terrace assembles from composed table sets + individual furniture for the cramped 12-table layout
- Chalkboard prices must be legible (price-shock gag depends on it)
- String lights render only in evening/night state

---

## 🚲 Sprite Sheet 2: Canal & Background Layers
**File:** `cafe_canal_background.png`
**Dimensions:** 1024x512 pixels

### Canal:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Water Reflection Strip 1-2 | (0, 0) / (0, 128) | 1024x128 each | Shimmering canal surface, two-frame loop |
| Canal Boat Passing | (0, 256) | 384x192 | Tour boat, wake included |
| Boat Wake Splash 1-2 | (592, 352) / (656, 352) | 64x32 each | Terrace-edge splash |

### Traffic & Fauna:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bicycle Passing 1-4 | (384, 256) / (512, 256) / (640, 256) / (768, 256) | 128x96 each | Background cyclist loop, bell-first |
| Pigeon Idle 1-2 / Pecking 1-2 / Alarmed / Suspicious | (384, 352) to (544, 352), 32px steps | 32x32 each | Six pigeon states — the last one is for Havok's paranoia |

### Background Gags:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tourist Selfie Canal-Fall 1-3 | (0, 448) / (64, 448) / (128, 448) | 64x64 each | The terrace's featured entertainment |
| Coffeeshop Smoke Drift 1-2 | (192, 448) / (256, 448) | 64x64 each | Wisps from the visible Coffeeshop Quarter |
| Roodelicht Distant Glow | (320, 448) | 128x64 | Evening-only red haze on the horizon |

### Technical Notes:
- Water strips scroll slowly with 2-frame crossfade; simplified to static on low-end (profile-mandated)
- Bicycle loop passes every 8 seconds; bell audio precedes sprite entry
- Canal-fall gag triggers randomly (~every 3-5 minutes), max once per scene load

---

## 🕵️ Sprite Sheet 3: Agent Havok's Table & Consumables
**File:** `havok_table_props.png`
**Dimensions:** 512x256 pixels

### The Corner Table:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corner Table Full Composition | (0, 0) | 192x128 | Best canal view, worst street visibility — "covert" |
| Upside-Down Newspaper | (192, 0) | 64x96 | Headline readable to observant players: "BRUNCH CHAOS: LOCAL DOG SUSPECTED" |
| Laminated Mission Dossier | (256, 0) | 48x64 | Clearly an eggs Benedict recipe from Sunday Brunch with Giselle |
| Briefcase | (304, 0) | 64x48 | Half-scratched-off podcast sticker |
| SHAMSTERDAM Hoodie on Chair | (368, 0) | 96x96 | Tags still attached |
| Empty Espresso Cups Cluster | (464, 0) | 48x32 | He's been "maintaining cover" for HOURS |
| Crayon Blueprints | (192, 96) | 64x48 | Fabergé Egg Hunt briefing material |
| Pigeon-Suspicion Eye Icon | (256, 96) | 32x32 | "They could be working for *anyone*" |

### Consumables (menu table coverage):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Espresso Cup (Tiny) | (288, 96) | 32x32 | €4.50 thimble of disappointment; +15 SP |
| Croissant (Day-Old) | (320, 96) | 48x32 | €8.00 of questionable freshness |
| Stroopwafel | (368, 96) | 32x32 | €3.50 — the only judgment-free order |
| Heineken Bottle | (400, 96) | 24x48 | €6.00, -Bravado, locals judge |
| "American Coffee" Mug | (424, 96) | 32x32 | €5.00, +Shame buff |
| "Giselle Special" Mystery Glass | (456, 96) | 32x32 | Item doesn't exist; barista confusion trigger |
| Serving Tray | (0, 128) | 64x32 | Margot's unknowable schedule |
| Check Saucer | (64, 128) | 32x32 | Arrives when it decides to arrive |
| Tip Coins | (96, 128) | 32x32 | Confusion prompt prop |

### Technical Notes:
- Table composition is the quest-hub hotspot; 44px+ interaction zone
- Newspaper headline needs a zoom-readable variant (2x detail in master file layers)

---

## 👥 Sprite Sheet 4: Café Staff
**File:** `npc_cafe_staff.png`
**Dimensions:** 512x384 pixels
**Sprite Size:** 64x96 pixels

### Barista Willem:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Willem Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Mechanical precision at rest |
| Willem Operating Machine 1-3 | (128, 0) / (192, 0) / (256, 0) | 64x96 each | Ancient espresso machine mastery |
| Willem Judging Stare | (320, 0) | 64x96 | "Do not tell me you want it 'iced.'" |
| Willem Sigh 1-4 | (0, 96) / (64, 96) / (128, 96) / (192, 96) | 64x96 each | Measurable on the Richter scale |

### Server Margot:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Margot Idle 1-2 | (256, 96) / (320, 96) | 64x96 each | Bemused detachment baseline |
| Margot Appear/Disappear 1-3 | (0, 192) / (64, 192) / (128, 192) | 64x96 each | Mysterious departure/arrival on unknowable schedule |
| Margot Delivering | (192, 192) | 64x96 | Serves what you need, not what you want |
| Margot Check-Refusal Shrug | (256, 192) | 64x96 | "The check will arrive when it decides" |

### Night Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Willem Night Idle | (0, 288) | 64x96 | String-light palette version |
| Margot Night Idle | (64, 288) | 64x96 | String-light palette version |

### Technical Notes:
- Willem's sigh animation is a Bravado-damage event — pair with sigh cloud effect (Sheet 6)
- Margot's appear/disappear uses alpha fade on frames 1/3

---

## 🐕 Sprite Sheet 5: Agent Havok & Café Regulars
**File:** `npc_havok_regulars.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 pixels (groups noted)

### Agent Havok ("Hans", very Shamsterdam local person):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Havok Disguised Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Sheltie in hoodie + sunglasses, seated |
| Havok Tail Wag 1-2 | (128, 0) / (192, 0) | 64x96 each | Under-table tail betrayal, increases with mission excitement |
| Havok Gesturing Urgently 1-2 | (256, 0) / (320, 0) | 64x96 each | Quest trigger wave from corner table |
| Havok Tells 1-6 | (0, 96) to (320, 96), 64px steps | 64x96 each | Newspaper flip, accent slip, pigeon flinch, tag dangle, ear escaping hood, briefing salute |

### Regulars:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cyclist Who Stopped 1-2 | (0, 192) / (64, 192) | 64x96 each | On phone, espresso untouched, radiating judgment |
| Backpacker "Basically a Local" 1-2 | (128, 192) / (192, 192) | 64x96 each | Correcting pronunciation incorrectly |
| Old Man Reading 1-2 | (256, 192) / (320, 192) | 64x96 each | Same table since 1983, "doesn't speak English" |
| Instagram Table Group 1-2 | (0, 288) / (256, 288) | 256x96 each | Four people, eight phones, zero conversation |
| Locals Leaning at Railing 1-2 | (0, 384) / (64, 384) | 64x96 each | Smoking, disappointed eye contact |
| Judging Local (Eye Contact) | (128, 384) | 64x96 | The stare that damages Bravado |

### Technical Notes:
- Havok tells trigger randomly during briefings (one per dialogue page); tail wag layered under table sprite
- Regulars are fixtures — no walk cycles; Instagram Table swaps frames on photo-taking beat

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `cafe_effects.png`
**Dimensions:** 256x256 pixels

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Espresso Steam 1-4 | (0, 0) / (32, 0) / (64, 0) / (96, 0) | 32x64 each | Machine and cup steam wisps |
| Cigarette/Weed Smoke Wisp 1-3 | (128, 0) / (160, 0) / (192, 0) | 32x64 each | European ambiance + coffeeshop drift |
| Canal Mist | (0, 64) | 128x64 | Morning water haze tile |
| Reflection Shimmer 1-3 | (128, 64) / (160, 64) / (192, 64) | 32x32 each | Water light dancing on tables |
| Willem Sigh Cloud 1-2 | (0, 128) / (48, 128) | 48x48 each | Visible, measurable disappointment |
| Judgment Aura 1-2 | (96, 128) / (144, 128) | 48x64 each | Radiates from locals toward tourist faux pas |
| Bicycle Bell Flash 1-2 | (192, 128) / (224, 128) | 32x32 each | Near-miss warning ping |
| Bravado Loss Puff 1-3 | (0, 192) / (32, 192) / (64, 192) | 32x32 each | Shame hit particles |
| Shame Blush 1-2 | (96, 192) / (128, 192) | 32x32 each | Ordering-error indicator |

### Technical Notes:
- Steam and smoke via CPUParticles2D using these frames as particle textures; reduced counts on low-end (profile-mandated)
- Judgment Aura is subtle — 30% opacity max; the joke is ambient, not literal

---

## 🧾 Sprite Sheet 7: UI Elements
**File:** `cafe_ui.png`
**Dimensions:** 512x384 pixels

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu UI Panel | (256, 0) | 256x96 | Order interface with Dutch item names |
| Service Wait Indicator | (0, 0) | 128x32 | "Server arriving eventually..." (30-90s random) |
| Bravado Judgment Meter | (0, 32) | 96x64 | Café-specific shame tracking |
| Pronunciation Attempt Icons 1-4 | (96, 32) to (192, 32), 32px steps | 32x32 each | Language barrier mini-game results (graceful → catastrophic) |
| Price Shock Popup | (0, 96) | 128x96 | "€8.00 for THIS?" |
| Tip Confusion Prompt | (128, 96) | 128x64 | "Tip? (Europeans don't...)" |
| Espresso Size Comparison | (256, 96) | 96x64 | American expectation vs. thimble reality |
| Mission Briefing Frame | (0, 192) | 256x192 | Havok's crayon-blueprint dialogue skin |
| Havok Quest Marker | (256, 192) | 32x32 | Paw-print-shaped "mysterious contact" icon |
| Time-of-Day Indicator | (288, 192) | 64x32 | Morning/afternoon/evening/late-night service states |

### Technical Notes:
- Briefing frame overlays standard dialogue UI during Fabergé Egg Hunt scenes
- All interactive UI zones minimum 44px

---

## 🎬 Animation Specifications

### Espresso Steam (Sheet 6):
- **Duration:** 2-second wisp cycle (4 frames at 2 FPS), continuous while machine active
- **Frames:** 4
- **Pattern:** Rise → curl → dissipate → loop
- **Trigger:** Constant at machine; burst on each order pulled
- **Purpose:** Terrace's visual heartbeat; signals Willem is working
- **Audio Sync:** Machine hiss peak on frame 1 of each burst
- **Mobile Optimization:** Half particle count on Medium, none ambient on Low

### Awning Flutter (Sheet 1):
- **Duration:** 3-second gentle cycle (2 frames at ~0.7 FPS)
- **Frames:** 2
- **Pattern:** Subtle continuous alternation
- **Trigger:** Constant (canal breeze)
- **Purpose:** Ambient life without motion noise
- **Audio Sync:** None
- **Mobile Optimization:** Static awning on low-end devices (profile-mandated)

### Canal Reflections (Sheets 2, 6):
- **Duration:** 4-second crossfade loop (2 strips)
- **Frames:** 2 strips + 3 shimmer sparkles
- **Pattern:** Slow crossfade, shimmer sparkles at random table positions
- **Trigger:** Constant
- **Purpose:** "Canal water reflections dancing on everything"
- **Audio Sync:** Water lapping bed
- **Mobile Optimization:** Simplified reflections on older devices (profile-mandated)

### Havok Tail Wag (Sheet 5):
- **Duration:** 1-second wag (2 frames at 2 FPS); frequency scales with mission excitement
- **Frames:** 2
- **Pattern:** Idle: rare single wags; briefing: continuous loop
- **Trigger:** Dialogue state (mission excitement variable)
- **Purpose:** The tell that breaks the cover — subtle enough that bros miss it
- **Audio Sync:** None (silence is the joke)
- **Mobile Optimization:** None needed

### Willem's Sigh (Sheets 4, 6):
- **Duration:** 2 seconds (4 body frames at 2 FPS + 2-frame cloud)
- **Frames:** 4 + 2
- **Pattern:** Inhale → shoulders rise → release → cloud drifts; single play
- **Trigger:** Bad order (Heineken, iced espresso, "venti")
- **Purpose:** Bravado-damage feedback with comedic weight
- **Audio Sync:** Seismic sigh sample on frame 3
- **Mobile Optimization:** None needed

### Margot Appear/Disappear (Sheet 4):
- **Duration:** 1.5 seconds (3 frames at 2 FPS with alpha fade)
- **Frames:** 3
- **Pattern:** Fade in → serve/shrug → fade out
- **Trigger:** Random 30-90s after order; check requests ignored
- **Purpose:** "Appears and disappears on unknowable schedule"
- **Audio Sync:** Chair scrape on cobblestone at appearance
- **Mobile Optimization:** None needed

### Bicycle Pass (Sheet 2):
- **Duration:** 8-second background loop (4 frames across traverse)
- **Frames:** 4
- **Pattern:** Enter left → bell flash near pedestrians → exit right
- **Trigger:** Constant loop, varying start offsets
- **Purpose:** Constant bicycle menace, Shamsterdam baseline threat
- **Audio Sync:** Bell ding 0.5s before sprite reaches screen center
- **Mobile Optimization:** Loop paused on Low LOD

### Pigeon Behavior (Sheet 2):
- **Duration:** Idle 2s / peck 1.5s / alarmed 0.5s cycles
- **Frames:** 6 states
- **Pattern:** Idle ↔ peck randomly; alarmed when Havok gestures; "suspicious" frame when Havok stares
- **Trigger:** Random placement near crumbs; Havok dialogue events
- **Purpose:** Havok watches them suspiciously — they gather near his table
- **Audio Sync:** Ominous coo (per profile audio) on suspicious frame
- **Mobile Optimization:** Max 2 pigeons on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter/Havok-table hotspot outlines | Sheet 7, (320, 192) | 64x64 x2 (x320, x384) | Bold-outline markers for the two key interaction zones |
| Canal edge warning outline | Sheet 7, (320, 256) | 64x32 | High-contrast coping-stone edge (no railing hazard) |
| NPC interaction highlight | Sheet 7, (384, 256) | 64x96 | Outline variant marking Willem, Margot, Havok as interactive |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static awning | Sheet 1 (Awning frame 1) | 512x128 | Reduced-motion holds frame 1 |
| Static water strip | Sheet 2 (Reflection strip 1) | 1024x128 | No crossfade, no shimmer |
| Steam-free machine | Sheet 1 (Espresso Machine) | 128x192 | Machine renders without particle bursts |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bicycle bell flash | Sheet 6, (192, 128) | 32x32 x2 | Visual mirror of approach bell — fires before sprite crosses |
| Sigh cloud | Sheet 6, (0, 128) | 48x48 x2 | Visual mirror of Willem's seismic sigh |
| Boat motor ripple icon | Sheet 7, (448, 256) | 32x32 | Wake warning mirroring boat audio (every 45-60s) |
| Machine hiss burst icon | Sheet 7, (480, 256) | 32x32 | Steam-burst chip mirroring espresso audio |

### Colorblind Considerations:
- Judgment/Bravado states use icon + meter position, never color alone
- Menu judgment levels display as eyebrow-icons (0-3) alongside any color coding
- Overheard-conversation subtitles carry speaker icons, not color-coded text
- Touch zones minimum 44px for counter, Havok's table, menu options, and tip prompt

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC (fallback PVRTC 4BPP); chalkboard menu and newspaper headline need higher quality (readable gag text)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for Havok table props (tell-spotting depends on detail)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cafe_environment | terrace, canal background | 2048x1024 |
| cafe_characters | staff, Havok/regulars | 1024x1024 |
| cafe_props_ui | table props, effects, UI | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full reflections, all smoke/steam particles, 6 ambient NPCs, pigeons, bicycle loop |
| Medium | Simplified reflections, half particles, 4 ambient NPCs |
| Low | Static water and awning, no ambient particles, 2 ambient NPCs (profile-mandated reductions) |

### Performance Targets:
- **Target FPS:** 45 (per location profile performance budget)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 38 MB maximum
- **Particle Limit:** 24 (steam, smoke, mist)

### Performance Notes:
- Single outdoor scene — background layers on ParallaxBackground to batch draws
- Time-of-day handled by CanvasModulate tint + string-light toggle, not duplicate art
- Ambient NPC conversation rotation is text-only; no extra sprite cost

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (cobblestones), ParallaxBackground (canal, bikes, distant glow), AnimatedSprite2D (NPCs, steam bursts), CPUParticles2D (steam/smoke/mist — not GPU), CanvasModulate (time-of-day), CanvasLayer (menu/briefing UI)
- Special systems: service-delay randomizer (30-90s), judgment-level resolver per order, tip-confusion branch, Havok appearance gate (2+ Shamsterdam locations visited), overheard-conversation rotator with Dutch subtitles, Couchsurf trigger (Heineken order / price complaint)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Steam burst frames | Espresso machine hiss/grind | Frame 1 of burst |
| Bicycle sprite | Bell ding | 0.5s before screen center |
| Canal boat | Motor pass | Every 45-60 seconds with sprite |
| Willem sigh frame 3 | Richter-scale sigh sample | On frame display |
| Margot appearance | Chair scrape on cobblestones | On fade-in complete |
| Pigeon suspicious frame | Ominous coo | On Havok stare event |
| Evening state | Distant Roodelicht club bass | With glow sprite + string lights |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Fabergé Egg Hunt (primary hub) | Havok table composition, crayon blueprints, dossier, briefing frame | Briefing at corner table; debrief and rewards on return |
| Future Shamsterdam Operations | Havok gesturing frames, quest marker | Post-quest permanent briefing spot |
| Couchsurf — Backpacker | Backpacker sprites, Heineken bottle | Invitation trigger via order/complaint |
| Bravado System | Judgment meter, sigh cloud, blush, loss puffs | Order choices and etiquette failures |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Shamsterdam Museum of Questionable Art | Crayon blueprints (heist target imagery) | Fabergé quest briefing reference |
| The Tolerance Hostel | Backpacker NPC continuity | Couchsurf morning-after scene |
| Canal Ring Promenade | Cobblestone tiles, railing, canal layers | Seamless adjacent-zone walk-off |
| Coffeeshop Quarter | Smoke drift wisps, visible from terrace | Ambient smoke source; Chadwick dialogue hook |
| Roodelicht Row | Distant glow sprite (evening) | Audio+visual evening transition |
| Casa Rosé Erotic Theatre | None shared; next-morning debrief dialogue | Bros process the experience over espresso |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "European café culture as an endurance sport the tourists don't know they've entered"
- **Color Mood:** Overcast grey and canal green, warmed only by espresso brown and evening amber — cozy and withholding at once
- **Lighting:** Natural daylight through ancient awning; string lights and water shimmer at night; everything reflects off the canal
- **Texture:** Worn wrought iron, chipped cream crockery, cobblestone polish — 178 years of use, zero renovations

### Environmental Storytelling:
- Twelve cramped tables force strangers into each other's conversations — the ambient-dialogue system is architectural
- The wifi password sign does the café's entire service philosophy in one prop
- Faded photos show tourists confused in every decade: the judgment is a heritage institution
- Havok's table is a complete comedy scene in still life — every prop contradicts his cover story

### Character Integration Notes:
- Willem never leaves the machine; Margot teleports; the gap between them is the service-timing mechanic
- Havok reads as "local" at silhouette distance and "dog in a hoodie" at close range — layer tells accordingly
- Regulars are furniture with opinions; they animate only to judge

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Havok's Table** - Upside-down newspaper, crayon blueprints, hoodie with tags: one frame, whole joke
2. **The Sigh Cloud** - Willem's measurable disappointment hovering over a tourist
3. **Espresso Size Comparison** - The thimble vs. the American expectation
4. **Selfie Canal-Fall** - Background tourist mid-splash while bros sip espresso
5. **The Wifi Sign** - "Password: 'OrderSomethingFirst'"

### Quote Potential:
- "I have made coffee since before your country had coffee. Do not tell me you want it 'iced.'"
- "You want the check? You will get the check when I decide you are finished."
- "We must speak quietly. The pigeons. They could be working for *anyone*."
- "He just asked for ice in his espresso. ICE. In ESPRESSO."
- "Ja, ja, very authentic, this establishment. I come here every day. To my favorite table. Which is... *looks around* ...this one. Now."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | cafe_terrace_environment.png | 1024x1024 |
| 2 | cafe_canal_background.png | 1024x512 |
| 3 | havok_table_props.png | 512x256 |
| 4 | npc_cafe_staff.png | 512x384 |
| 5 | npc_havok_regulars.png | 512x512 |
| 6 | cafe_effects.png | 256x256 |
| 7 | cafe_ui.png | 512x384 |

**Total Estimated Memory:** ~10 MB raw RGBA texture data; ~38 MB maximum total footprint (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `cafe_terrace_environment.png` (1024x1024)
- [ ] `cafe_canal_background.png` (1024x512)
- [ ] `havok_table_props.png` (512x256)
- [ ] `npc_cafe_staff.png` (512x384)
- [ ] `npc_havok_regulars.png` (512x512)
- [ ] `cafe_effects.png` (256x256)
- [ ] `cafe_ui.png` (512x384)

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
- **Documentation:** Animation timing reference sheet + Havok tell-frequency guide + parallax layer guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: Havok's tells and table props, upside-down headline, wifi sign, espresso size gap
- [ ] Accessibility visual alternatives included for all audio cues (bell, sigh, boat, machine hiss)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (service culture clash, performative sophistication)
- [ ] Hidden areas/interactions have discoverable visual cues (Havok gesture, readable headline, pigeon behavior)
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (judgment icons, meter positions)
- [ ] Social media viral potential maximized in composition choices (Havok table as hero shot)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam/Roodelicht Row in-world; profile's "Amsterdam energy" lines are meta commentary, not asset text |
| Cultural Specificity | ✅ | Dutch directness, European café service norms, tourist exhaustion |
| Satirical Targets Appropriate | ✅ | American service expectations and tourist behavior; café workers rendered competent, not mocked |
| Seedy Underbelly Present | ✅ | €8 croissants, systematic overcharging, communal illegal ashtray, coffeeshop smoke drift |
| Gameplay Value Established | ✅ | Quest hub (Fabergé Egg Hunt), consumables, Bravado mechanics, Couchsurf hook, ambient storytelling |
| Technical Feasibility | ✅ | Single outdoor scene, parallax layers, CanvasModulate time-of-day documented |
| Mobile Performance Budget | ✅ | 45 FPS, 16 draw calls, 38 MB per profile budget |
| Accessibility Features | ✅ | Visual mirrors for bell/sigh/boat/hiss audio, reduced-motion statics, 44px zones |
| No Crypto Elements | ✅ | Pure espresso-and-judgment commerce |
| Social Media Integration | ✅ | 5 screenshot moments + quote bank identified |

**Once these assets are delivered, Café de Schaamte becomes the beating judgmental heart of Shamsterdam: the terrace where every quest begins over a €4.50 thimble, every faux pas is catalogued, and the dog in the hoodie is definitely, definitely a local.**
