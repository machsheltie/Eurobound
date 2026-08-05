# The Strobe Survival Kit - Complete PNG Asset Requirements

## 📋 Overview
The Strobe Survival Kit is a fold-out street stall run like a forward operating base: Antonín, a former sound engineer with visible hearing aids and twenty years of receipts, sells earplugs, glow sticks, and the will to continue to tourists marching into 105-decibel territory. This document specifies every PNG for the military-surplus-meets-rave armory, the decibel warning chart that guilt-trips honestly, and the equipment whose effects are — uniquely for Debaucheryville — exactly what the vendor claims.

**Location ID:** `debaucheryville_vendor_strobe_survival_01`
**Theme:** Harm reduction disguised as tactical commerce — "Equip Yourself. The Night Is Hostile."
**Zone:** Absinthe Arcade, near club entrances
**Hours:** 8 PM - 5 AM (pre-club through post-club; prices +50% after midnight, earplugs exempt)
**Primary Function:** Street vendor / equipment hub — Confusion-reduction gear, SP/HP consumables, theft prevention, next-day status prevention, Tactical Briefing system, Bravado interactions

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Military Green | #4B5320 | Stall structure, surplus crates, Antonín's vest |
| Neon Pink | #FF6EC7 | Glow product accents, rave-side inventory |
| Night Black | #1A1A1A | Street backdrop, shadow zones |
| Warning Orange | #FF4500 | Decibel chart, midnight price notice, alerts |
| Glow Yellow-Green | #CCFF33 | Active glow sticks, LED product light |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/strobe_survival_kit/
├── environment/
│   ├── survival_stall.png
│   └── stall_sections.png
├── objects/
│   └── survival_items.png
├── npcs/
│   ├── antonin.png
│   └── stall_customers.png
├── effects/
│   └── stall_effects.png
└── ui/
    └── stall_ui.png
```

---

## 🏪 Sprite Sheet 1: The Stall
**File:** `survival_stall.png`
**Dimensions:** 512x512 pixels

### Stall Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stall Structure Full | (0, 0) | 384x320 | Fold-out street stall, military surplus meets rave culture |
| Fold-Out Awning | (384, 0) | 128x64 | Olive canvas, pink trim — the two cultures negotiating |
| Stencil Main Sign | (384, 64) | 128x48 | "THE STROBE SURVIVAL KIT" in military stencil font |
| Tagline Board | (384, 112) | 128x32 | "Equip Yourself. The Night Is Hostile." |
| Category Header Strip | (384, 144) | 128x32 | "AUDIO DEFENSE \| VISUAL ENHANCEMENT \| CHEMICAL SUPPORT \| TACTICAL ACCESSORIES" |
| Midnight Price Notice | (384, 176) | 128x32 | "Prices increase after midnight. Plan ahead." |
| Warning Board | (384, 208) | 128x48 | "The club doesn't care about your comfort. We do." |

### The Chart & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Decibel Warning Chart | (384, 256) | 96x128 | Club dB levels — Velvet Curtain 105 dB "permanent damage threshold", underground 110+ "why" |
| Work Light | (480, 256) | 32x32 | Practical clamp lamp |
| Work Light Beam | (480, 288) | 32x64 | No-nonsense light cone |
| Counter Fold-Out | (0, 320) | 256x96 | Transaction surface, cable-tied to the frame |
| Pegboard Wall Left | (256, 320) | 128x96 | Hanging items, everything visible, everything grabbable |
| Pegboard Wall Right | (384, 384) | 128x96 | Second pegboard panel |
| Night Street Strip | (0, 416) | 384x96 | Club district context, distant bass-lit doorways |
| Stall Cash Box | (384, 480) | 64x32 | Olive drab, dented |
| Stock Crate | (448, 480) | 64x32 | "EARPLUGS — RESTOCK WEEKLY" stencil |

### Technical Notes:
- Decibel chart is examine-zoomable; the numbers are the guilt trip and must be legible
- Midnight Price Notice gains a Warning Orange modulate pulse after 00:00
- Street strip parallax-scrolls slightly; distant club doors brighten as night progresses

---

## 🧰 Sprite Sheet 2: Stall Sections
**File:** `stall_sections.png`
**Dimensions:** 512x256 pixels

### The Armory Sections:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Audio Defense Display | (0, 0) | 128x128 | Earplug wall, foam to musician-grade — the primary product |
| Visual Enhancement Display | (128, 0) | 128x128 | Glow sticks, LED gear, strobe shades rack |
| Chemical Support Rack | (256, 0) | 128x128 | Energy shots, caffeine pills, electrolytes, mints |
| Tactical Accessories Board | (384, 0) | 128x128 | Pouches, flashlights, wipes, hair ties, chargers |
| Regret Prevention Corner | (0, 128) | 128x128 | Condoms, aspirin, snack bars, water — no judgment |
| Glow Stick Bin | (128, 128) | 128x128 | Colorful chaos in a surplus ammo crate |

### Section Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Earplug Tier Comparison Card | (256, 128) | 128x64 | Foam / silicone / musician / custom side-by-side |
| Earplug Dispenser | (256, 192) | 64x64 | Gumball-style dispenser, foam grade |
| Decibel Meter Prop | (320, 192) | 64x64 | Live-reading meter aimed at the club district |
| Water Bottle Crate | (384, 128) | 64x64 | "HYDRATION IS SURVIVAL" |
| Snack Bar Box | (448, 128) | 64x64 | 2 AM crash prevention stock |
| Price Flip Cards | (384, 192) | 128x64 | Pre-midnight / post-midnight (+50%) flip pair |

---

## 🎒 Sprite Sheet 3: Survival Inventory
**File:** `survival_items.png`
**Dimensions:** 256x256 pixels

### Audio Defense:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Foam Earplugs (Basic) | (0, 0) | 24x24 | 3 Sovs — "Better than nothing. Barely." |
| Silicone Earplugs | (32, 0) | 24x24 | 8 Sovs — "Now we're talking." |
| Musician-Grade Plugs | (64, 0) | 24x24 | 20 Sovs — "The sound stays, the damage doesn't." |
| Custom Molded (Premium) | (96, 0) | 24x24 | 45 Sovs — "Once you go custom, you never go back." |
| Earplug Carry Case | (128, 0) | 24x24 | Keyring capsule |
| Glow Stick (Dormant) | (160, 0) | 32x16 | Pre-crack state |
| Glow Stick (Active) | (160, 16) | 32x16 | Cracked and glowing |
| Glow Stick Bundle (6) | (192, 0) | 48x32 | "You'll make friends. Or lose them all." |

### Visual & Chemical:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| LED Bracelet | (0, 32) | 32x32 | Rechargeable. Responsible. Still ridiculous |
| Strobe-Resistant Shades | (32, 32) | 32x24 | Yes, wear them inside. It's SURVIVAL |
| Glow Glasses | (64, 32) | 32x24 | Stupid-looking, memorable |
| Energy Shot | (96, 32) | 24x32 | Liquid motivation. The crash is real |
| Caffeine Pills (6) | (128, 32) | 24x24 | Controlled release |
| Electrolyte Packet | (160, 32) | 24x24 | Hydration is survival |
| Breath Mints (Tin) | (192, 32) | 24x24 | For after the kebab. Or during |
| Energy Gum | (224, 32) | 24x24 | Caffeine without the bottle. Sophisticated |

### Tactical & Regret Prevention:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Phone Pouch (Secure) | (0, 64) | 32x32 | -80% pickpocket risk |
| Mini Flashlight | (32, 64) | 24x24 | Club bathrooms are dark for reasons |
| Flashlight (Beam On) | (64, 64) | 32x32 | Navigation mode |
| Wet Wipes (Pack) | (96, 64) | 24x24 | Don't ask what for. Just have them |
| Hair Ties (Set) | (128, 64) | 24x24 | Underrated. Essential |
| Backup Charger | (160, 64) | 32x24 | Phone resurrection |
| Protection Pack | (192, 64) | 24x24 | No judgment. Only preparation |
| Aspirin (Packet) | (224, 64) | 24x24 | Take before bed. Thank me tomorrow |

### Kit & States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Snack Bar | (0, 96) | 24x24 | The club doesn't serve food |
| Water Bottle | (32, 96) | 24x32 | Revolutionary: drinking water |
| Full Survival Kit Bundle | (64, 96) | 64x64 | Complete loadout in a surplus pouch — Bradley's order |
| Glow Stick Color Strip | (128, 96) | 96x16 | Six colors for the bundle |
| LED Bracelet (Lit) | (128, 112) | 32x32 | Active-glow variant |
| Shades (Worn Glyph) | (160, 112) | 32x24 | Equipped indicator art |
| Midnight +50% Tag | (192, 112) | 32x32 | Desperation pricing chip |
| Standard Price Tag | (224, 112) | 32x32 | Pre-midnight chip |

### Demonstration Art:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Earplug In-Ear Demo | (0, 160) | 48x48 | Cutaway insertion diagram, briefing-style |
| Decibel Wave Icon | (48, 160) | 32x32 | Sound pressure visual for the chart |
| Combo Deal Bundle | (80, 160) | 48x48 | Earplugs + electrolytes + shades combo |
| Restock Crate (Open) | (128, 160) | 48x48 | Antonín's restocking animation prop |

---

## 🪖 Sprite Sheet 4: Antonín "Tonda" Dvořák
**File:** `antonin.png`
**Dimensions:** 256x384 pixels

### Operating Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Idle Gruff | (0, 0) | 64x96 | Surplus vest, practical stance, hearing aids visible — always visible |
| Tactical Assessment | (64, 0) | 64x96 | Scanning the player's loadout — "You're going in naked. Tactically naked." |
| Demonstrating Earplug F1 | (128, 0) | 64x96 | Holding plug up |
| Demonstrating Earplug F2 | (192, 0) | 64x96 | Roll-and-compress motion |

### Character Beats:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Demonstrating Earplug F3 | (0, 96) | 64x96 | Insertion mime, deadly serious |
| Pointing at Hearing Aids | (64, 96) | 64x96 | "Twenty years. No earplugs. Don't be me." |
| Disappointed Head Shake | (128, 96) | 64x96 | "Your choice. Your ears." |
| Respect Nod | (192, 96) | 64x96 | Post-purchase — "You're prepared now. Go have SAFE fun." |

### Briefing & Portraits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tactical Briefing Gesture | (0, 192) | 64x96 | Map-table energy over the counter |
| Restocking | (64, 192) | 64x96 | Crate-to-pegboard motion |
| Portrait: Gruff | (128, 192) | 64x96 | Dialogue box default |
| Portrait: Concern | (192, 192) | 64x96 | The warning delivery face |

### Expressions & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stern | (0, 288) | 48x48 | Default counter face |
| Vindicated | (48, 288) | 48x48 | When The Convert returns |
| Rare Warmth | (96, 288) | 48x48 | "I like hearing survival stories." |
| Hearing Aid Close-Up | (144, 288) | 48x48 | THE detail shot — insert for the warning beat |
| Chart Pointer Hand | (192, 288) | 48x48 | Finger on the 105 dB line |

---

## 🧑‍🤝‍🧑 Sprite Sheet 5: Customers & Bros
**File:** `stall_customers.png`
**Dimensions:** 512x192 pixels

### Atmospheric Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Convert | (0, 0) | 64x96 | "It's been EIGHTEEN HOURS." Buying musician-grade, slightly panicked |
| Veteran Clubber | (64, 0) | 64x96 | "Usual kit, Tonda." Efficient, nods, leaves |
| Dismissive Bro | (128, 0) | 64x96 | "I'm FINE." Future convert |
| Concerned Friend | (192, 0) | 64x96 | Buying earplugs for the whole reluctant group |
| Sound Engineer (Off-Duty) | (256, 0) | 64x96 | Discussing -25dB vs -30dB molds with Antonín |
| Tourist Pair (Passing) | (320, 0) | 96x96 | Clubward foot traffic |
| Queue Browser | (416, 0) | 64x96 | Reading the decibel chart, recalculating life |

### The Bros:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner (Hesitating) | (0, 96) | 64x96 | "Earplugs are kind of... uncool, right?" |
| Lord Pilsner (Converted) | (64, 96) | 64x96 | "...give me the musician-grade." |
| Chadwick (Glow Sticks) | (128, 96) | 64x96 | "The glow sticks will look AMAZING on camera." |
| Bradley (Full Kit) | (192, 96) | 64x96 | "I'll take the full survival kit." No hesitation |
| Dismissive Bro (Next Day) | (256, 96) | 64x96 | Ears-ringing squiggles, humbled return |
| Friend Handing Earplugs | (320, 96) | 64x96 | Distribution in progress — "Thank me tomorrow" |
| Convert Grabbing Counter | (384, 96) | 64x96 | Desperation frame for the panic beat |

---

## ✨ Sprite Sheet 6: Effects
**File:** `stall_effects.png`
**Dimensions:** 128x128 pixels

### Glow & Light:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Glow Stick Aura | (0, 0) | 32x32 | Soft radius around active sticks |
| LED Flicker F1 | (32, 0) | 32x32 | Bracelet blink on |
| LED Flicker F2 | (64, 0) | 32x32 | Bracelet blink off |
| Bass Throb Ring F1 | (96, 0) | 32x32 | Distant club bass, visualized at the stall edge |
| Bass Throb Ring F2 | (96, 32) | 32x32 | Ring expanding |
| Crack-Activate Flash | (0, 32) | 32x32 | Glow stick snap moment |
| Ear Ringing Squiggle | (32, 32) | 32x32 | Tinnitus made visible (Dismissive Bro, next day) |
| Hearing Aid Glint | (64, 32) | 16x16 | Catchlight on the warning beat |

### Alerts & Auras:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Price Surge Flash | (0, 64) | 64x32 | Midnight +50% strike |
| Decibel Wave Pulse | (64, 64) | 64x32 | Chart meter spike |
| Guilt Aura (Grey) | (0, 96) | 32x32 | Hovering over the unprotected |
| Safety Check Glyph | (32, 96) | 32x32 | Green tick over protected players |
| Glow Rainbow Strip | (64, 96) | 64x32 | Bin shimmer, six colors |

---

## 🎮 Sprite Sheet 7: UI Elements
**File:** `stall_ui.png`
**Dimensions:** 256x192 pixels

### Shop Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Equipment Browser Frame | (0, 0) | 160x96 | Stencil-font section navigation |
| Tactical Briefing Panel | (160, 0) | 96x96 | Antonín's personalized loadout recommendation |
| Earplug Comparison Card | (0, 96) | 96x48 | Foam → custom, tiers and dB reduction |
| Midnight Price Warning | (96, 96) | 96x48 | "+50% — You should have bought before." |

### Status & Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Strobe Headache Icon | (192, 96) | 32x32 | Unprotected debuff indicator |
| Mood Up Icon | (224, 96) | 32x32 | Glow gear bonus |
| Equipped Loadout Bar | (0, 144) | 128x32 | Current protection at a glance |
| Hearing Preserved Badge | (128, 144) | 48x48 | Achievement — Antonín approves |
| Prepared Clubber Icon | (176, 144) | 32x32 | Status affecting bouncer interactions |
| Ringing Ears Debuff Icon | (208, 144) | 32x32 | Next-day -10% audio interactions |
| Confusion Shield Icon | (192, 128) | 32x32 | Earplug/shades reduction indicator |
| Pickpocket Shield Icon | (224, 128) | 32x32 | Phone pouch active |

---

## 🎬 Animation Specifications

### Earplug Demonstration:
- **Duration:** 4.5 seconds
- **Frames:** Demonstrating F1 (1.5s) → F2 roll-compress (1.5s) → F3 insertion mime (1.5s)
- **Pattern:** One-shot, replayable from the briefing menu
- **Trigger:** First Audio Defense browse, or player asks for the demo
- **Purpose:** Genuine harm-reduction education delivered with military gravity
- **Audio Sync:** Foam squeak on F2, muffled-world audio dip on F3 (the whole mix ducks 8dB for 1 second — the product demo IS the sound design)
- **Performance Optimization:** None needed

### The Hearing Aid Moment:
- **Duration:** 3 seconds
- **Frames:** Pointing at Hearing Aids (2s) + Hearing Aid Close-Up insert (1s) with glint
- **Pattern:** One-shot per conversation branch
- **Trigger:** Player dismisses earplugs, or asks about the hearing aids
- **Purpose:** The emotional core of the stall — twenty years of consequence in one gesture
- **Audio Sync:** Brief audio distortion effect while the close-up holds (per profile comedy audio spec)
- **Performance Optimization:** None needed

### Glow Stick Activation:
- **Duration:** 1 second
- **Frames:** Dormant → Crack-Activate Flash (0.2s) → Active + Aura fade-in (0.8s)
- **Pattern:** One-shot per stick
- **Trigger:** Purchase or use of a glow stick
- **Purpose:** Small, perfect retail dopamine — the one product that delivers instantly
- **Audio Sync:** Snap-crack on the flash frame
- **Performance Optimization:** Aura omitted on Low LOD

### Distant Bass Throb:
- **Duration:** 1.0 second loop
- **Frames:** Ring F1 → F2 at the street edge of the stall
- **Pattern:** Constant, intensifying — one ring per beat, +20% opacity per in-game hour toward midnight
- **Trigger:** Constant ambient
- **Purpose:** The threat preview; the stall is quiet, the war is over there
- **Audio Sync:** Muffled club bass, louder as night progresses (per profile audio transitions)
- **Performance Optimization:** Rings off on Low; bass audio still carries the cue with subtitle glyph

### Midnight Price Surge:
- **Duration:** 2 seconds one-shot, then persistent state
- **Frames:** Price Flip Cards flip (1s) → Price Surge Flash (0.5s) → Midnight tags shown (0.5s)
- **Pattern:** Once per night at 00:00
- **Trigger:** In-game clock hits midnight
- **Purpose:** Desperation pricing, ceremonially announced; earplug tags visibly DON'T flip (Antonín's principles)
- **Audio Sync:** Cash register ka-chunk on the flip
- **Performance Optimization:** None needed

### Antonín Restocking Idle:
- **Duration:** 7 seconds loop
- **Frames:** Idle Gruff (4s) → Restocking (2s) → Idle Gruff return (1s)
- **Pattern:** Loop when no customer engaged
- **Trigger:** Idle timer
- **Purpose:** He is always working; the stall never looks abandoned
- **Audio Sync:** Crate shuffle on restock frames
- **Performance Optimization:** Idle-only on Low

### Ear Ringing Squiggle (Next-Day Debuff):
- **Duration:** 2 seconds loop while debuffed
- **Frames:** Squiggle oscillates over affected character
- **Pattern:** Loops during Ringing Ears status
- **Trigger:** Morning after unprotected clubbing
- **Purpose:** Consequence made visible; also marks the Dismissive Bro's return arc
- **Audio Sync:** Faint high-pitch whine under the mix (with visual glyph as the accessible equivalent)
- **Performance Optimization:** Static squiggle on Low

---

## ♿ Accessibility Sprite Requirements
**File:** `stall_accessibility.png` (supplemental sheet — delivered alongside the 7 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Antonín Interactive Outline | (0, 0) | 64x96 | White-on-dark counter hotspot |
| Decibel Chart, Large-Print | (64, 0) | 128x96 | Oversized dB figures — the warning must be readable by everyone it's warning |
| Browser Frame, Bold | (192, 0) | 64x96 | High-contrast shop border |
| Earplug Tiers, Bold Icons | (0, 96) | 128x32 | Thick-outline tier glyphs with dB numbers |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bass Rings, Off | (128, 96) | 32x32 | Static bass glyph replacing expanding rings |
| LED Flicker, Steady | (160, 96) | 32x32 | Constant-on bracelet replacing the blink |
| Price Flash, Removed | (192, 96) | 64x32 | Flip cards change without the surge flash |
| Squiggle, Static | (0, 128) | 32x32 | Fixed tinnitus glyph replacing oscillation |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Muffle Demo Icon | (0, 176) | 48x48 | Ear + down-arrow glyph during the demo audio duck — the demo's point must land without sound |
| Snap-Crack Icon | (48, 176) | 32x32 | Burst glyph on glow stick activation |
| Bass Beat Tick | (80, 176) | 32x32 | Metronome pip synced to the distant bass |
| Ka-Chunk Icon | (112, 176) | 32x32 | Register glyph on the midnight flip |
| Distortion Icon | (144, 176) | 48x48 | Wavy-lines glyph during the hearing aid audio distortion |
| Tinnitus Whine Glyph | (192, 176) | 32x32 | High-line glyph paired with the ringing debuff |

### Colorblind Considerations:
- Earplug tiers are shape-and-number coded (1-4 pips + dB figures), never color-only
- Guilt Aura vs. Safety Check use distinct shapes (cloud vs. check), not just grey/green
- Pre/post-midnight price tags differ by a "+50%" numeral, not tag color alone
- Counter hotspot and all browser rows exceed the 44px minimum touch target

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) — stall_ui.png and decibel chart regions kept uncompressed (numbers must stay crisp)
- **Fallback:** PNG high quality for chart and briefing panel

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| survival_environment | stall, sections | 1024x1024 |
| survival_characters | antonin, customers | 1024x512 |
| survival_items_ui | items, effects, ui, accessibility | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Bass rings, glow auras, LED blinks, 5 customer NPCs, full restock idle |
| Medium | Glow auras only, 3 customers, idle without restock |
| Low | Static glow decals, 2 customers, no rings, static product displays |

### Performance Targets:
- **Target FPS:** 60 (per location profile performance budget)
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 28 MB maximum
- **Particle Limit:** 10 (glow shimmer + rings combined)

### Performance Notes:
- Simplified glow effects and static displays per profile platform considerations
- The stall is an open street scene with one focal NPC — cheapest location in the Arcade by design
- Item icons batched from one sheet; the entire shop browser is a single draw call

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Street scene: single Node2D stall + parallax night strip; distant-club brightness driven by in-game clock
- Equipment system writes to shared `player_equipment` flags (earplugs_grade, shades_equipped, glow_active, pouch_active) consumed by Velvet Curtain and next-morning status resolution
- Midnight pricing: price table swaps on the clock signal; earplug rows flagged `surge_exempt`
- CPUParticles2D (not GPU) for glow shimmer; bass rings are two alternating Sprite2D scales
- State tracking: `strobe_survival_state` (purchases, briefing_taken, earplugs_owned_grade, convert_arc_stage, friend_helped, achievements)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Earplug demo F3 | Full-mix 8dB duck (muffled world) | 1 second on insertion mime |
| Hearing Aid Close-Up | Brief audio distortion | While insert holds |
| Glow stick activation | Snap-crack | On flash frame |
| Bass Throb rings | Muffled club bass | Ring per beat; volume rises toward midnight |
| Midnight flip | Register ka-chunk | On card flip |
| Purchase confirm | Package rustle + gruff "Good." | On transaction |
| Ringing Ears debuff | Faint high whine | Loops with squiggle |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Achievement track (Preparing → Harm Reducer) | Badge/icon set, kit bundle, friend-handoff sprite | Fires on first purchase, earplug purchase, full kit, unprotected survival, post-damage return, convincing a friend |
| The Convert arc | Dismissive Bro → Next-Day → Convert sprites, Vindicated expression | Three-night NPC state machine; Antonín's "I'll have the silicone ready" pays off |
| Tactical Briefing | Briefing Panel, Briefing Gesture, comparison card | Personalized loadout advice; following it earns a discount |
| Prepared Clubber status | Prepared Clubber icon, Safety Check glyph | Equipped protection changes bouncer interactions at Velvet Curtain |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Velvet Curtain Club | Earplugs/shades reduce Confusion there; bouncers nod at strobe shades | Equipment flags carry through entry |
| Hostel Midnight Checkout | Next-morning status (Ringing Ears / clean) resolved from tonight's loadout | Debuff icons appear at wake-up |
| 24-Hour Internet Café | Coffee counteracts the energy-shot crash | Crash debuff cleared there |
| The Bohemian Trap | Absinthe effects stack with energy management | Status icons co-display |
| Neon & Chrome Boutique | Overlapping strobe-protection market (deliberate rivalry gag) | Referenced in dialogue only |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A military briefing for a night out — played straight, because 110 dB for six hours IS combat"
- **Color Mood:** Military Green discipline invaded by Neon Pink inventory; Warning Orange reserved for things that are actually warnings
- **Lighting:** Practical work lights only — no mood lighting at the one honest stall in the Arcade; the glow sticks provide their own
- **Texture:** Surplus canvas, stenciled crates, pegboard order; everything grabbable, nothing decorative

### Environmental Storytelling:
- The decibel chart does the selling; Antonín just points at it
- Earplug price tags don't flip at midnight — principles, rendered in cardstock
- The stall faces the club district: the customer browses with the threat literally glowing behind them
- Hearing aids visible in every Antonín pose — the stall's founding document, worn on his head

### Character Integration Notes:
- Antonín's poses are economical; he gestures like a man briefing soldiers, not selling trinkets
- The Convert's panic must read as comedy AND vindication — Antonín's Vindicated expression pairs with it
- The Dismissive Bro's three-stage arc (dismissal → ringing → conversion) is the location's thesis in NPC form

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Decibel Chart** - "Velvet Curtain: 105 dB — permanent damage threshold. Underground: 110+ — why"
2. **The Hearing Aid Point** - Antonín's twenty years of consequence in one gesture
3. **Lord Pilsner's Conversion** - "Earplugs are uncool" to "give me the musician-grade" in four dialogue lines
4. **The Midnight Flip** - Every price surges except the earplugs
5. **Bradley's Full Kit** - The one bro who just... listened

### Quote Potential:
- "The club is a battlefield. Would you go to war without armor? This is your armor."
- "You see these? Twenty years in clubs. No earplugs. Don't be me."
- "The DJ is wearing earplugs. The bartenders are wearing earplugs. Why aren't you?"
- "You can't create content if you can't hear the feedback. Earplugs."
- "Revolutionary: drinking water. Try it."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | survival_stall.png | 512x512 |
| 2 | stall_sections.png | 512x256 |
| 3 | survival_items.png | 256x256 |
| 4 | antonin.png | 256x384 |
| 5 | stall_customers.png | 512x192 |
| 6 | stall_effects.png | 128x128 |
| 7 | stall_ui.png | 256x192 |

**Total Estimated Memory:** ~12 MB (well inside the 28 MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `survival_stall.png` (512x512)
- [ ] `stall_sections.png` (512x256)
- [ ] `survival_items.png` (256x256)
- [ ] `antonin.png` (256x384)
- [ ] `stall_customers.png` (512x192)
- [ ] `stall_effects.png` (128x128)
- [ ] `stall_ui.png` (256x192)
- [ ] `stall_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (pre/post-midnight price states in separate groups; Antonín demo frames in sequence)
- **Documentation:** Animation timing reference sheet (demo duck timing, midnight flip, bass ring cadence) + equipment-flag effect map

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Military Green #4B5320, Neon Pink #FF6EC7, Warning Orange #FF4500, Night Black #1A1A1A)
- [ ] Decibel chart figures legible at examine zoom (the guilt trip is data)
- [ ] Hearing aids visible in every single Antonín pose — no exceptions
- [ ] Earplug tags visibly unflipped in the post-midnight state
- [ ] Accessibility visual alternatives included for all audio cues (muffle duck, snap, bass, ka-chunk, distortion, whine)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (military seriousness for club prep, sincerity underneath) is clear throughout all assets
- [ ] Hidden details discoverable: exempt earplug tags, live decibel meter, "restock weekly" earplug crate
- [ ] Performance optimized (single-draw-call browser, capped particles, clock-driven lighting)
- [ ] Touch zone sizing considered (44px minimum — counter and browser rows compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (pip-coded tiers, shape-coded auras)
- [ ] Social media viral potential maximized (chart, hearing-aid point, conversion arc compositions)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville / Absinthe Arcade only; "best clubs in Debaucheryville" per profile dialogue |
| Cultural Specificity | ✅ | Eastern European rave culture and intense club scene |
| Satirical Targets Appropriate | ✅ | Club culture's disregard for hearing health and the "I'll be fine" attitude — not clubbers as people |
| Seedy Underbelly Present | ✅ | Desperation pricing after midnight — emergency supplies marked up +50% (earplugs excepted, which IS the characterization) |
| Gameplay Value Established | ✅ | Equipment effects at Velvet Curtain, next-day status prevention, briefing system, Convert NPC arc, Bravado hooks |
| Technical Feasibility | ✅ | 7 sheets, flag-based equipment system, clock-driven pricing — standard Godot 4.x |
| Performance Budget | ✅ | 60 FPS / 12 draw calls / 28 MB per profile; estimate ~12 MB |
| Accessibility Features | ✅ | The muffle-demo and tinnitus cues have visual equivalents; no audio-only information anywhere at the harm-reduction stall (it would be ironic) |
| No Crypto Elements | ✅ | Pure tactical commerce (profile-confirmed) |
| Social Media Integration | ✅ | Five viral moments identified, quotes sourced from profile dialogue |

**When these assets deploy, The Strobe Survival Kit becomes the one stall in Debaucheryville that tells the truth: a pegboard armory where the decibel chart does the sales pitch, the earplug prices never surge, and a gruff man with visible hearing aids points at his own head and says the most honest sentence in the entire district — "Don't be me."**
