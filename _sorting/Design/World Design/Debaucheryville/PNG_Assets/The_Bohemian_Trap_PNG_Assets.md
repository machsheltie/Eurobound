# The Bohemian Trap - Complete PNG Asset Requirements

## 📋 Overview
The Bohemian Trap is an ornate absinthe cart (built 2015, aged artificially) where Emil "The Green Fairy" Novak sells €3 of strong alcohol for €25 with a story attached. This document specifies every PNG needed for the cart theater: the backlit bottle array, the elaborate ritual sequence, the dry-ice mystique, and the "Green Fairy Confusion" status that reverses the player's controls. The trap is literal, the vendor knows it, and the experience is — annoyingly — still kind of fun.

**Location ID:** `debaucheryville_vendor_bohemian_trap_01`
**Theme:** Absinthe mythology commodification — "Drink Like Hemingway. Pay Like a Tourist. Regret Like Everyone."
**Zone:** Absinthe Arcade, Neon Entertainment Quarter
**Hours:** 6 PM - 4 AM (twilight to desperation hours)
**Primary Function:** Street vendor / status-effect dispenser — Absinthe tiers, the purchasable ritual, Green Fairy Confusion with 20% control reversal, Bravado interactions

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Absinthe Green | #7FFF00 | Bottle glow, neon underlighting, vision tint |
| Antique Gold | #CFB53B | Cart trim, Art Nouveau lettering, spoons |
| Night Black | #1A1A1A | Night backdrop, wrought iron details |
| Fog Gray | #A9A9A9 | Dry ice fog, mysterious atmosphere |
| Deep Cart Green | #2E5E2E | Cart body wood, "antique" paint |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/bohemian_trap/
├── environment/
│   ├── bohemian_cart.png
│   └── arcade_night_bg.png
├── objects/
│   └── ritual_props.png
├── npcs/
│   ├── emil.png
│   └── trap_tourists.png
├── effects/
│   └── green_effects.png
└── ui/
    └── trap_ui.png
```

---

## 🛒 Sprite Sheet 1: The Cart
**File:** `bohemian_cart.png`
**Dimensions:** 512x512 pixels

### Cart Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Body Full | (0, 0) | 320x256 | Ornate wooden wagon, Belle Époque fantasy, artificially aged |
| Cart Awning | (320, 0) | 192x96 | Green canvas with gold fringe |
| Art Nouveau Main Sign | (320, 96) | 192x64 | "THE BOHEMIAN TRAP" in swirling lettering |
| "Since... 1997" Board | (320, 160) | 192x32 | "Traditional Recipe Since... 1997" — the ellipsis does heavy lifting |
| ABV Warning (Tiny) | (320, 192) | 96x32 | "70% ABV — Not for the unprepared" in deliberately small type |
| "See the Green Fairy Tonight" Card | (416, 192) | 96x32 | The promise, gold on green |

### Display & Station:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bottle Display (Backlit) | (0, 256) | 256x128 | Absinthe array glowing green, Art Nouveau labels |
| Ritual Station Countertop | (256, 256) | 256x128 | Spoons, sugar, fountain arranged artistically |

### Educational Posters:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Poster: History of Absinthe | (0, 384) | 96x128 | Heavily romanticized |
| Poster: Famous Drinkers | (96, 384) | 96x128 | Hemingway, Van Gogh, Toulouse-Lautrec |
| Poster: The Proper Ritual | (192, 384) | 96x128 | Elaborate, photogenic, unnecessary |
| Poster: Thujone Content | (288, 384) | 96x128 | The "active ingredient" discussion |

### Cart Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wrought Iron Wheel | (384, 384) | 64x64 | Black iron, decorative spokes |
| Cart Lantern | (448, 384) | 32x64 | Gold lantern, green flame tint |
| Green Neon Under-Rail | (384, 448) | 128x32 | Underlighting strip beneath the cart |
| Menu Chalkboard | (384, 480) | 128x32 | Tier prices, "House Special" starred |

### Technical Notes:
- Cart position shifts slightly each night per profile — cart is one Node2D moved by a nightly seed, no extra sprites
- Bottle display glow is a modulate pulse, not extra frames
- Posters are examine-zoomable; text must be legible at 2x

---

## 🥄 Sprite Sheet 2: Ritual Props
**File:** `ritual_props.png`
**Dimensions:** 256x256 pixels

### Glassware & Ritual Kit:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Absinthe Glass (Empty) | (0, 0) | 32x48 | Traditional reservoir glass |
| Absinthe Glass (Poured) | (32, 0) | 32x48 | Clear green measure inside |
| Absinthe Glass (Louched) | (64, 0) | 32x48 | Clouded opalescent green |
| Slotted Spoon | (96, 0) | 48x32 | Genuinely beautiful object, ornate slots |
| Sugar Cube | (144, 0) | 16x16 | Why not just dissolve sugar? TRADITION |
| Sugar Cube (Dissolving) | (160, 0) | 16x16 | Mid-drip erosion |
| Flaming Sugar | (176, 0) | 16x32 | The "modern" variation, briefly lit |
| Absinthe Fountain | (192, 0) | 64x96 | Ornate, Instagram-ready, mostly decorative |

### Drip & Louche Animation:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Water Drip F1 | (96, 32) | 16x16 | Drop forming at fountain tap |
| Water Drip F2 | (112, 32) | 16x16 | Drop falling |
| Water Drip F3 | (128, 32) | 16x16 | Drop hitting sugar |
| Louche Cloud F1 | (0, 96) | 64x64 | First swirl of cloud in the glass |
| Louche Cloud F2 | (64, 96) | 64x64 | Cloud spreading |
| Louche Cloud F3 | (128, 96) | 64x64 | Near-full opalescence |
| Louche Cloud F4 | (192, 96) | 64x64 | "The fairy waking" — full cloud |

### The Absinthe Tiers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bottle: Tourist Green | (0, 160) | 32x64 | €8, "A gentle introduction" |
| Bottle: Bohemian Standard | (32, 160) | 32x64 | €12, "The traditional experience" |
| Bottle: Artist's Choice | (64, 160) | 32x64 | €18, "As Hemingway preferred" |
| Bottle: Green Fairy Special | (96, 160) | 32x64 | €25, Art Nouveau fairy label |
| Bottle: "Vintage" Reserve | (128, 160) | 32x64 | €40, dusty on purpose |
| Shot Flight Tray | (160, 160) | 64x32 | €30, five small glasses of commitment |
| Sugar-Only Dish | (224, 160) | 32x32 | €2, the Disappointer's order |

### Pour Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pour Stream F1 | (160, 192) | 16x32 | Green ribbon from bottle |
| Pour Stream F2 | (176, 192) | 16x32 | Stream tapering off |
| Tip Jar | (192, 192) | 32x32 | "FOR THE FAIRY" label |
| Glass Coaster | (224, 192) | 16x16 | Gold-rimmed presentation coaster |

---

## 🎩 Sprite Sheet 3: Emil "The Green Fairy" Novak
**File:** `emil.png`
**Dimensions:** 512x384 pixels

### Performance Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Idle Theatrical | (0, 0) | 64x128 | Waistcoat, top hat, waxed mustache, performative everything |
| Presenting Bottle | (64, 0) | 64x128 | Bottle held aloft with ceremony |
| Pour F1 | (128, 0) | 64x128 | Bottle tilts |
| Pour F2 | (192, 0) | 64x128 | Stream begins |
| Pour F3 | (256, 0) | 64x128 | Precise measure |
| Pour F4 | (320, 0) | 64x128 | Bottle righted with flourish |
| Flame Flourish | (384, 0) | 64x128 | Lighting the sugar, match held high |
| Watching Reaction | (448, 0) | 64x128 | Post-consumption observation, hands clasped |

### Ritual & Character Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| The Pitch (Arms Wide) | (0, 128) | 64x128 | "Welcome, welcome to The Bohemian Trap!" |
| Sugar Placement | (64, 128) | 64x128 | Cube balanced on spoon, reverent |
| Water Drip Focus | (128, 128) | 64x128 | Leaning in — "We don't rush the fairy" |
| "The Fairy Has Found You!" | (192, 128) | 64x128 | Triumphant declaration pose |
| Rare Honesty Shrug | (256, 128) | 64x128 | "The science is... debated." |
| Off-Duty Emil | (320, 128) | 64x128 | Top hat off, theater degree visible in posture |
| Tip Accept Bow | (384, 128) | 64x128 | Deep theatrical bow |
| Pocket Watch Check | (448, 128) | 64x128 | Costume detail beat between customers |

### Expressions & Portraits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Theatrical Delight | (0, 256) | 48x48 | Full showman |
| Mysterious Squint | (48, 256) | 48x48 | "Some say it opens doors" |
| Disappointment (Sugar-Only) | (96, 256) | 48x48 | Palpable; Emil remembers |
| Honest Weariness | (144, 256) | 48x48 | Off-duty "experience architect" face |
| Showman Grin | (192, 256) | 48x48 | The €25 smile |
| Portrait: Showman | (240, 256) | 64x96 | Dialogue box, in character |
| Portrait: Off-Duty | (304, 256) | 64x96 | Dialogue box, behind the curtain |
| Mustache Twirl F1 | (368, 256) | 48x48 | Idle flourish |
| Mustache Twirl F2 | (416, 256) | 48x48 | Twirl completing |

---

## 🧑‍🤝‍🧑 Sprite Sheet 4: Tourists & Bros
**File:** `trap_tourists.png`
**Dimensions:** 512x192 pixels

### Atmospheric NPCs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Believer | (0, 0) | 64x96 | Staring into middle distance, seeing fairies (none present) |
| Believer Pointing at Lamp | (64, 0) | 64x96 | "That's definitely a fairy" |
| Skeptic's Companion | (128, 0) | 64x96 | "Mark, that's a lamp" energy |
| Instagram Ritualist | (192, 0) | 96x96 | Ring light out, drink getting cold, multiple angles |
| Absinthe Veteran Locals | (288, 0) | 96x96 | Czech pair, amused — "Forty euros. AMAZING." |
| First-Timer (Nervous) | (384, 0) | 64x96 | "I have work Monday" |
| Queue Tourist | (448, 0) | 64x96 | Generic line filler |

### The Bros & Gag Objects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner (Fairy in the Lamp) | (0, 96) | 64x96 | Pointing at the green lamp, converted |
| Chadwick (Recording) | (64, 96) | 64x96 | "This is ASMR. This is POETRY." |
| Bradley (Slightly Left) | (128, 96) | 64x96 | "Perhaps slightly to the left of where I intended" |
| Bro Walking Backward | (192, 96) | 64x96 | Control-reversal victim frame |
| The Lamp (Unlit) | (256, 96) | 32x64 | An ordinary street lamp |
| The Lamp (Green-Lit) | (288, 96) | 32x64 | The "fairy" — same lamp, green glow |
| Tourist Drinking | (320, 96) | 64x96 | Mid-ritual consumption |
| Tourist "Is This It?" | (384, 96) | 64x96 | The deflation moment, tiny glass in hand |
| Photo Pose Pair | (448, 96) | 64x96 | Two tourists posing with the fountain |

---

## 🧚 Sprite Sheet 5: Green Effects
**File:** `green_effects.png`
**Dimensions:** 256x256 pixels

### Atmosphere:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Dry Ice Fog Bank | (0, 0) | 128x64 | Ground fog rolling from under the cart |
| Fog Wisp F1 | (128, 0) | 64x64 | Rising tendril |
| Fog Wisp F2 | (192, 0) | 64x64 | Tendril dissipating |
| Green Sparkle F1 | (0, 64) | 32x32 | "Fairy" glint |
| Green Sparkle F2 | (32, 64) | 32x32 | Glint bloom |
| Green Sparkle F3 | (64, 64) | 32x32 | Glint fade |
| Fairy Particle Hint | (96, 64) | 32x32 | Suggestive shimmer — never a full fairy |
| Fairy Silhouette Tease | (128, 64) | 64x64 | Ambiguous shape in fog; is it? (it is not) |
| Neon Underglow Pool | (192, 64) | 64x32 | Green light wash on cobblestones |
| Green Glass Glint | (192, 96) | 32x32 | Bottle highlight ping |
| Sparkle Burst | (224, 96) | 32x32 | Ritual completion pop |

### Status Effect Overlays:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Green Vision Tint Tile | (0, 96) | 128x128 | Tileable screen tint — scales opacity per Buzzed tier |
| Vignette Corner | (128, 128) | 64x64 | Edge blur corner, mirrored for full frame |
| Control Reversal Arrows | (192, 128) | 64x32 | Crossed left/right arrows glyph |
| Wobble Lines | (192, 160) | 64x32 | Stagger indicator around player feet |
| Louche Swirl Overlay | (128, 192) | 64x64 | Screen-space swirl during Confusion spikes |
| Confusion Stars | (192, 192) | 64x32 | Orbiting green stars |
| Screen Sparkle Edge | (192, 224) | 64x32 | "Occasional sparkle" per Confusion status |
| Green Flash Frame | (0, 224) | 128x32 | Consumption-moment full-width flash strip |

### Technical Notes:
- Vision tint: Light 25% opacity, Standard 40%, Confusion 60% + sparkle edges
- Fairy Silhouette Tease spawns at most once per Confusion duration — the joke dies if overused
- All particles CPUParticles2D; fog capped at 2 emitters on mobile

---

## 🌃 Sprite Sheet 6: Arcade Night Backdrop
**File:** `arcade_night_bg.png`
**Dimensions:** 512x256 pixels

### Background Layers:
| Layer | Position | Size | Description |
|-------|----------|------|-------------|
| Twilight Skyline | (0, 0) | 256x128 | 6 PM opening hours — purple-orange fade |
| Night Skyline | (256, 0) | 256x128 | Full night, neon jumble glowing |
| Cobblestone Street | (0, 128) | 256x64 | Tileable ground strip |
| Club Entrance Glow Row | (256, 128) | 256x64 | Distant club doorways, tourist magnets |

### Street Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon Sign Jumble | (0, 192) | 128x64 | Competing arcade signage, out of focus |
| Distant Tourist Crowd | (128, 192) | 128x64 | Silhouette shuffle layer |
| Street Lamp | (256, 192) | 32x64 | THE lamp (see Sheet 4 for the lit gag version) |
| Puddle Reflection | (288, 192) | 96x32 | Green neon mirrored in a puddle |
| Ground Fog Layer | (288, 224) | 128x32 | Low ambient fog strip |
| Trash Bin | (416, 192) | 32x64 | Arcade street reality |
| Kebab Wrapper Litter | (448, 192) | 64x32 | Foreshadowing the cure |
| Bottle Litter | (448, 224) | 64x32 | Empty tourist-tier bottles |

---

## 🎮 Sprite Sheet 7: UI Elements
**File:** `trap_ui.png`
**Dimensions:** 256x192 pixels

### Menu & Ritual:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Absinthe Menu Frame | (0, 0) | 160x96 | Art Nouveau tier selection panel |
| Ritual Step Tracker | (160, 0) | 96x32 | Nine-step ritual progress pips |
| Skip Ritual Button | (160, 32) | 96x32 | Available, but loses "experience" (and Bravado) |
| Tier Price Tags | (160, 64) | 96x32 | €8 through €40 chip strip |

### Status Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Absinthe Buzzed (Light) | (0, 96) | 32x32 | Faint green swirl icon |
| Absinthe Buzzed (Standard) | (32, 96) | 32x32 | Fuller swirl, blur edge |
| Green Fairy Confusion | (64, 96) | 32x32 | Fairy silhouette in swirl |
| Confidence Up | (96, 96) | 32x32 | +Confidence indicator |
| Accuracy Down | (128, 96) | 32x32 | -Accuracy indicator |
| Control Reversal Warning | (160, 96) | 64x32 | Crossed-arrows alert chip |
| Absinthe Veteran Badge | (224, 96) | 32x32 | 3+ purchases — staff stop explaining |

### Prompts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Was That Worth It?" Prompt | (0, 128) | 192x64 | Three-option reflection panel |
| Photography Op Icon | (192, 128) | 32x32 | Ritual photo moment marker |
| Coffee Cure Hint | (224, 128) | 32x32 | 24-Hour Café pointer when Confused |
| Achievement Toast | (192, 160) | 64x32 | "Green Curious" / "Fairy Touched" toasts |

---

## 🎬 Animation Specifications

### The Full Ritual (Green Fairy Special):
- **Duration:** 24 seconds total (skippable)
- **Frames:** Presenting Bottle (3s) → Pour F1-F4 (4s) → Sugar Placement (3s) → Water Drip F1-F3 loop (8s) → Louche Cloud F1-F4 (4s) → Flame Flourish optional (1s) → presentation flourish (1s)
- **Pattern:** One-shot sequence, step tracker advances per stage
- **Trigger:** Purchasing Green Fairy Special (or any tier with ritual)
- **Purpose:** The elaborate shot-taking IS the product — the animation must feel worth €25 while depicting €3 of alcohol
- **Audio Sync:** Pour sound on F2, sugar clink on placement, water drips at 1 per second (reverent quiet), clouding "whoosh" on Louche F3, flame puff if lit
- **Mobile Optimization:** Drip loop shortens to 4s on Low LOD; louche plays all 4 frames regardless (it is the money shot)

### Water Drip:
- **Duration:** 1.0 second loop within ritual
- **Frames:** 3 (form → fall → hit)
- **Pattern:** Steady, unhurried — "We don't rush the fairy"
- **Trigger:** Ritual step 5
- **Purpose:** ASMR pacing; the Instagram Ritualist NPC exists for this beat
- **Audio Sync:** Drip plink on F3, each cycle
- **Mobile Optimization:** None needed

### Louche Clouding:
- **Duration:** 4 seconds one-shot
- **Frames:** 4 (F1 → F2 → F3 → F4, 1s each)
- **Pattern:** Plays in the glass close-up
- **Trigger:** Ritual step 5 completion
- **Purpose:** "This is the fairy waking" — the visual climax of the con
- **Audio Sync:** Low clouding whoosh starting at F2
- **Mobile Optimization:** None needed

### Dry Ice Fog:
- **Duration:** 6 seconds loop
- **Frames:** Fog bank scroll + 2 wisp frames on offset timers
- **Pattern:** Constant ground roll, wisps rise every 3s
- **Trigger:** Constant while cart is open
- **Purpose:** Mystique on a fog-machine budget — the atmosphere IS dry ice and confidence
- **Audio Sync:** Faint fog hiss, continuous
- **Mobile Optimization:** Fog bank only (no wisps) on Medium; static fog decal on Low

### Green Fairy Confusion (Screen State):
- **Duration:** 60 minutes game-status; visual loop 2 seconds
- **Frames:** Vision tint constant + Confusion Stars orbit + Screen Sparkle Edge pulse (0.5s) + Louche Swirl on reversal events
- **Pattern:** Loops for status duration; Control Reversal Arrows flash 0.4s on each reversed input (20% chance per action)
- **Trigger:** Consuming Green Fairy Special or Shot Flight
- **Purpose:** Being drunk with green lighting, mechanically — comedy through struggle, never debilitation
- **Audio Sync:** Distinctive "wrong way" boing on each reversal event
- **Mobile Optimization:** Stars capped at 3, sparkle edge off on Low; tint always on (it carries the state read)

### Emil Idle:
- **Duration:** 9 seconds loop
- **Frames:** Idle Theatrical (6s) → Mustache Twirl F1-F2 (1.5s) → Pocket Watch Check (1.5s)
- **Pattern:** Loop with twirl/watch alternating
- **Trigger:** Constant when no customer engaged
- **Purpose:** Never breaks character, even unwatched
- **Audio Sync:** None
- **Mobile Optimization:** Twirl only, no watch check, on Low

### The Deflation Beat:
- **Duration:** 2 seconds
- **Frames:** Tourist "Is This It?" hold + slight deflation slump tween
- **Pattern:** One-shot after first sip of any tier
- **Trigger:** Consumption complete, before status applies
- **Purpose:** The "€25 for a thimble" moment — comedy anchor
- **Audio Sync:** Slight deflation note (satirical stinger per profile)
- **Mobile Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements
**File:** `trap_accessibility.png` (supplemental sheet — delivered alongside the 7 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Emil Interactive Outline | (0, 0) | 64x128 | White-on-dark hotspot outline for all poses |
| Menu Frame, Bold | (64, 0) | 128x64 | High-contrast tier selection border |
| ABV Warning, Large-Print | (64, 64) | 128x48 | "70% ABV" readable without examine zoom — the joke sign, made honest |
| Ritual Tracker, Bold Pips | (192, 0) | 64x32 | Thick-outline step indicators |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Vision Tint, Static | (0, 128) | 64x64 | Fixed tint replacing swirl/sparkle overlays (tint stays — it reads state) |
| Confusion Stars, Off | (64, 128) | 32x32 | Single static star badge replacing the orbit |
| Fog, Reduced | (96, 128) | 64x32 | Static ground fog decal replacing rolling banks |
| Louche, Cross-Fade | (160, 128) | 64x64 | Two-frame dissolve replacing the 4-frame swirl |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wrong-Way Boing Icon | (0, 192) | 48x48 | Crossed arrows + burst on every control reversal — the reversal must never be audio-only |
| Drip Plink Icon | (48, 192) | 32x32 | Droplet ring per ritual drip |
| Clouding Whoosh Icon | (80, 192) | 32x32 | Swirl glyph as the louche forms |
| Deflation Note Icon | (112, 192) | 32x32 | Drooping note on the "is this it?" beat |
| Fog Hiss Icon | (144, 192) | 32x32 | Wisp glyph while fog machine runs |
| Glass Clink Icon | (176, 192) | 32x32 | Clink burst on presentation |

### Colorblind Considerations:
- Status tiers are icon-differentiated (swirl density + fairy silhouette), never green-intensity alone
- Control reversal uses the crossed-arrows shape, not a color flash
- Bottle tiers carry distinct label silhouettes (plain / banded / fairy figure / dust), not just label color
- Emil's tap zone (64x128) and all menu tiers exceed the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 — green_effects.png at ASTC 4x4 (screen overlays band easily)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for trap_ui.png and poster text

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| bohemian_environment | cart, arcade backdrop | 1024x1024 |
| bohemian_characters | emil, tourists | 1024x512 |
| bohemian_effects_ui | ritual props, effects, ui, accessibility | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full fog (2 emitters), sparkles, complete ritual timing, 5 tourist NPCs |
| Medium | Fog bank only, sparkle burst on completion only, 3 tourists |
| Low | Static fog decal, static bottle glow, shortened drip loop, 2 tourists, tint-only Confusion |

### Performance Targets:
- **Target FPS:** 45 (per location profile performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 32 MB maximum
- **Particle Limit:** 14 (fog + sparkles combined)

### Performance Notes:
- Ritual close-up assets (glass states, louche frames) loaded on purchase, freed after
- Screen tint is one full-screen ColorRect + tile texture — cheaper than shader vignette on low-end
- Simplified fog effect and static bottle glow per profile platform considerations

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Cart as one scene with nightly position offset (`night_seed`); ParallaxBackground for skyline layers (twilight → night lerp at 9 PM)
- Ritual as an AnimationPlayer timeline with step-tracker signals; skip button jumps to consumption with `experience_skipped` flag
- Control reversal: input remap wrapper active during Confusion, 20% roll per movement action, single-action duration
- CPUParticles2D (not GPU) for fog and sparkles
- State tracking: `bohemian_trap_state` (purchases_count, veteran_status, ritual_completed, sugar_only_ordered, emil_offduty_found, current_status_effect)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Pour F2 | Pour sound | Frame start |
| Sugar Placement | Cube clink | On contact |
| Water Drip F3 | Drip plink | Each cycle |
| Louche Cloud F2-F4 | Clouding whoosh | Starts F2, tails F4 |
| Flame Flourish | Match strike + flame puff | On ignition |
| Consumption | Gulp + Green Flash Frame | Flash on swallow |
| "Is This It?" beat | Slight deflation note | On slump tween |
| Control reversal event | "Wrong way" boing | With arrows flash |
| Ritual quiet | Ambient ducks -6dB | Steps 3-5 (reverent), restores after |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Absinthe Achievement Track | Ritual sequence, veteran badge, sugar-only dish, off-duty Emil | "Green Curious" → "Behind the Curtain" toasts fire on each milestone |
| Behind the Curtain (Emil off-duty) | Off-Duty Emil pose + portrait | Found post-cart hours; real philosophy dialogue unlocks |
| Green Fairy Confusion navigation | Confusion overlays, reversal arrows, coffee cure hint | Status persists across locations until cured (time/coffee/kebab) |
| The Disappointer | Sugar-Only Dish, Emil Disappointment expression | Ordering just the sugar; Emil remembers on all future visits |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Velvet Curtain Club | Confusion/Buzzed status carries into club entry (confidence helps, accuracy doesn't) | Status overlays persist through transition |
| 24-Hour Internet Café | Coffee Cure Hint icon points there; coffee clears Confusion | Tint fade-out on cure |
| Hostel Midnight Checkout | Getting back while Confused — reversal events continue en route | Status overlays persist |
| Shadow Exchange | Absinthe status affects exchange rate negotiation | Status icon shown in negotiation UI |
| Late-Night Kebab | Post-absinthe carb absorption cure path | Tint fade-out on cure |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Belle Époque theater on a 2015 cart — the trap is in the name and nobody reads the name"
- **Color Mood:** Absinthe Green glow against Night Black, trimmed in Antique Gold; everything the color of the promise
- **Lighting:** Green neon underglow, backlit bottles, mysterious fog-diffused shadows; Emil lit like a stage act because he is one
- **Texture:** Artificially aged wood, polished ritual silverware, dry-ice sheen on cobblestones

### Environmental Storytelling:
- "Traditional Recipe Since... 1997" — the sign confesses; the ellipsis is doing theater
- The ABV warning is tiny; the fairy promise is enormous — priorities rendered in font size
- No locals at the cart, ever, except the two amused veterans watching from across the street
- The lamp. Just an ordinary lamp, until someone Confused looks at it

### Character Integration Notes:
- Emil's poses never break character in public; Off-Duty Emil is the only pose allowed honest body language
- The louche close-up must be genuinely beautiful — the satire lands harder when the theater is good
- The Fairy Silhouette Tease must stay ambiguous in silhouette; if it reads as a definite fairy, the joke inverts

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Louche Close-Up** - Genuinely gorgeous clouding shot, ring-light ready
2. **"THE FAIRY IS IN THE LAMP"** - Lord Pilsner pointing at a green lamp
3. **The Control Reversal Walk** - Player physically failing to leave the cart in a straight line
4. **"Since... 1997"** - The sign that confesses
5. **The Sugar-Only Order** - Emil's palpable disappointment over a €2 dish

### Quote Potential:
- "They pay for experience. I provide experience. The alcohol is just the medium."
- "Mark, that's a lamp. The lamp is not a fairy. We've been over this."
- "The fairy does not answer to science. She answers to belief."
- "Is this worth €25? ...you will remember this. You will tell people about this. Is THAT worth €25?"
- "I see... I see GREEN. I see... that's a lamp. But a GREEN lamp. THE FAIRY IS IN THE LAMP."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | bohemian_cart.png | 512x512 |
| 2 | ritual_props.png | 256x256 |
| 3 | emil.png | 512x384 |
| 4 | trap_tourists.png | 512x192 |
| 5 | green_effects.png | 256x256 |
| 6 | arcade_night_bg.png | 512x256 |
| 7 | trap_ui.png | 256x192 |

**Total Estimated Memory:** ~14 MB (well inside the 32 MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `bohemian_cart.png` (512x512)
- [ ] `ritual_props.png` (256x256)
- [ ] `emil.png` (512x384)
- [ ] `trap_tourists.png` (512x192)
- [ ] `green_effects.png` (256x256)
- [ ] `arcade_night_bg.png` (512x256)
- [ ] `trap_ui.png` (256x192)
- [ ] `trap_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (ritual sequence frames grouped in order; status overlays in their own group)
- **Documentation:** Animation timing reference sheet (full 24s ritual breakdown, drip cadence, reversal flash timing)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Absinthe Green #7FFF00, Antique Gold #CFB53B, Night Black #1A1A1A, Fog Gray #A9A9A9)
- [ ] "Since... 1997" and the tiny ABV warning readable on examine
- [ ] Louche Cloud frames read as one continuous clouding when played at 1s per frame
- [ ] The Lamp and Green-Lit Lamp are pixel-identical except for glow (the gag depends on it)
- [ ] Accessibility visual alternatives included for all audio cues (boing, drip, whoosh, deflation note, hiss, clink)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (mythology-priced alcohol, vendor in on the joke) is clear throughout all assets
- [ ] Easter eggs discoverable: the ellipsis sign, absent locals, veteran hecklers, the lamp
- [ ] Mobile performance optimized (on-demand ritual assets, 2-emitter fog cap, ColorRect tint)
- [ ] Touch zone sizing considered (44px minimum — Emil hotspot and menu tiers compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (icon-coded statuses, silhouette-coded bottles)
- [ ] Social media viral potential maximized (louche close-up, lamp gag, reversal walk compositions)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville / Absinthe Arcade only; "Bohemia" survives as mythology branding, not geography |
| Cultural Specificity | ✅ | Absinthe tourism industry and Eastern European tourist trap culture |
| Satirical Targets Appropriate | ✅ | Tourism experience commodification and the tourists buying it — not Czech culture or responsible drinking |
| Seedy Underbelly Present | ✅ | €3 of alcohol sold for €25 with a costume and a fog machine |
| Gameplay Value Established | ✅ | Status effect economy, control reversal mechanic, purchasable ritual, Bravado hooks |
| Technical Feasibility | ✅ | 7 sheets, one AnimationPlayer ritual, input-wrapper reversal — standard Godot 4.x |
| Mobile Performance Budget | ✅ | 45 FPS / 14 draw calls / 32 MB per profile; estimate ~14 MB |
| Accessibility Features | ✅ | Reversal is never audio-only; static tint path; every stinger has a glyph |
| No Crypto Elements | ✅ | Pure traditional grift (profile-confirmed) |
| Social Media Integration | ✅ | Five viral moments identified, quotes sourced from profile dialogue |

**When these assets ship, The Bohemian Trap becomes a complete piece of street theater the player pays to fall for: a beautiful ritual, a gorgeous clouding glass, a fog machine working overtime — and then the walk away from the cart, slightly to the left of where they intended, past a green lamp that is absolutely, definitely, one hundred percent just a lamp.**
