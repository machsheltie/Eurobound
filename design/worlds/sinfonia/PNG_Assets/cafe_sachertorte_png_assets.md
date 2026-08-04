# Café Sachertorte - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Café Sachertorte location - a high-end Viennese café where a slice of cake costs 18 Sovs, the waiter's disapproval is complimentary, and tradition is commodified down to the last apricot glaze. It becomes ground zero for Gustav's 340 Sovs rampage during the Fiaker Fiasco sidequest.

**Location ID:** `sinfonia_kaffeehaus_cafe_sachertorte_01`
**Theme:** The commodification of tradition and the tyranny of refinement — café pretension weaponized against tourists
**Zone:** Kaffeehaus Row
**Hours:** 08:00–22:00 (peak pretension 14:00–17:00; pre-opera evening service)
**Primary Function:** Café shop / quest location — Fiaker Fiasco phase 2 (Gustav's cake heist), hidden-charge economy, debt system, post-quest Valued Patron path

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Sachertorte Brown | #3D2314 | Wood tones, menus, chocolate everything |
| Apricot Glaze | #FBCEB1 | Cake accents, warm highlights |
| Cream Marble | #FFFDD0 | Floors, tabletops |
| Café Imperial Gold | #CFB53B | Gilding, frames, trim |
| Mahogany Dark | #4A0000 | Wall paneling, counter |
| Coffee Black | #1C1C1C | Herr Ober's formal wear, espresso |
| Whipped Cream | #FFFAFA | Porcelain, linen, highlights |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/cafe_sachertorte/
├── environment/
│   └── cafe_sachertorte_tileset.png
├── npcs/
│   ├── herr_ober_waiter.png
│   └── cafe_sachertorte_npcs.png
├── objects/
│   ├── cafe_sachertorte_landmarks.png
│   └── cafe_sachertorte_destruction.png
├── effects/
│   └── cafe_sachertorte_effects.png
└── ui/
    └── cafe_sachertorte_ui.png
```

---

## 🎨 Sprite Sheet 1: Interior Tileset
**File:** `cafe_sachertorte_tileset.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #3D2314 (Sachertorte Brown), #FFFDD0 (Cream Marble), #CFB53B (Imperial Gold), #4A0000 (Mahogany)

### Floor Tiles (32x32 each):
- **Marble Floor** (0, 0, 32x32) - Cream marble with subtle veining
- **Marble Floor Worn** (32, 0, 32x32) - High-traffic pattern
- **Carpet Pattern** (64, 0, 32x32) - Deep red Persian-style
- **Carpet Border** (96, 0, 32x32) - Gold-trimmed edge
- **Kitchen Tile** (128, 0, 32x32) - White commercial tile

### Wall Tiles (32x64 each):
- **Mahogany Panel** (0, 32, 32x64) - Dark wood wainscoting
- **Cream Wall Upper** (32, 32, 32x64) - Aged cream plaster
- **Wainscoting Cap** (64, 32, 32x32) - Gilded molding
- **Gilded Frame** (96, 32, 64x64) - For oil paintings

### Furniture (various sizes):
- **Marble Table** (0, 96, 32x32) - Round café table, marble top
- **Bentwood Chair** (32, 96, 24x32) - Thonet-style, dark wood
- **Bentwood Chair Toppled** (56, 96, 32x24) - Post-chaos state
- **Service Counter Section** (0, 128, 64x48) - Dark wood with brass
- **Counter Glass Case** (64, 128, 48x48) - Display portion

### Windows & Doors:
- **Tall Window** (0, 176, 32x80) - Cream curtains, brass rod
- **Window Light Glow** (32, 176, 32x80) - Overlay for sunbeam effect
- **Front Door** (64, 176, 32x64) - Heavy glass, brass handles
- **Patio Door Intact** (96, 176, 32x64) - To outdoor seating
- **Patio Door Damaged** (128, 176, 40x64) - Post-Gustav entry
- **Kitchen Door** (168, 176, 24x48) - Swinging staff door

### Decorative Elements:
- **Oil Painting** (0, 256, 48x64) - Aristocrat portrait
- **Gilded Mirror** (48, 256, 40x56) - Ornate frame
- **Wall Sconce** (88, 256, 16x32) - Warm fabric shade
- **Clock Antique** (104, 256, 24x32) - Pendulum style
- **"Established 1843" Plaque** (128, 256, 32x16) - Brass

### Technical Notes:
- Marble should show EarthBound-style depth through subtle gradient
- Mahogany panels need visible wood grain texture
- All furniture should cast soft shadows

---

## 🎭 Sprite Sheet 2: Herr Ober (Head Waiter)
**File:** `herr_ober_waiter.png`  
**Dimensions:** 384x288 pixels  
**Color Palette:** #1C1C1C (Formal Black), #FFFFFF (White Shirt), #CFB53B (Gold Accents)

### Idle & Service States (48x96 each):
- **Idle** (0, 0, 48x96) - Perfect stillness, hands clasped
- **Service Frame 1** (48, 0, 48x96) - Approaching with tray
- **Service Frame 2** (96, 0, 48x96) - Presenting order
- **Service Frame 3** (144, 0, 48x96) - Placing item precisely

### Judgment Animation (48x96 each):
- **Judgment Frame 1** (192, 0, 48x96) - Eyebrow beginning to raise
- **Judgment Frame 2** (240, 0, 48x96) - Full disapproval, slight head tilt
- **Judgment Frame 3** (288, 0, 48x96) - Return to neutral with sigh

### Chaos Reaction (48x96 each):
- **Horror Frame 1** (0, 96, 48x96) - Turning to see Gustav
- **Horror Frame 2** (48, 96, 48x96) - Hands rising to face
- **Horror Frame 3** (96, 96, 48x96) - Full horror, step backward
- **Horror Frame 4** (144, 96, 48x96) - Mouth open screaming

### Fury Animation (48x96 each):
- **Fury Frame 1** (192, 96, 48x96) - Pointing accusingly
- **Fury Frame 2** (240, 96, 48x96) - Both arms gesturing
- **Fury Frame 3** (288, 96, 48x96) - Red-faced, demanding

### Emotional States:
- **Defeat** (0, 192, 48x96) - Slumped, staring at destruction
- **Reluctant Respect** (48, 192, 48x96) - Post-payment acknowledgment
- **Door Block** (96, 192, 48x96) - Arms crossed, refusing entry

### Detail Elements:
- **Pocket Watch** (144, 192, 12x16) - On chain, for close-up
- **Service Tray** (156, 192, 32x24) - Silver, with items
- **Debt Receipt** (188, 192, 24x32) - Paper with 340 Sovs

### Animation Timing:
- Service: 4fps, single play
- Judgment: 2fps, hold on final frame
- Horror: 6fps, single play
- Fury: 4fps, loop

### Character Notes:
- Face should show permanent exhaustion lines
- Mustache thin and precisely trimmed
- Posture always ramrod straight except in Defeat state
- White apron becomes increasingly rumpled through chaos states

---

## 👥 Sprite Sheet 3: Café Regulars & Staff
**File:** `cafe_sachertorte_npcs.png`  
**Dimensions:** 384x288 pixels  
**Color Palette:** Various formal wear colors, #3D2314 (Wood tones)

### The Intellectual (48x80 each):
- **Reading** (0, 0, 48x80) - Book held, not actually reading
- **Espresso Sip** (48, 0, 48x80) - Tiny cup raised
- **Unchanged During Chaos** (same sprite) - Literally doesn't react

### Chess Master Greta (48x80 each):
- **Waiting** (96, 0, 48x80) - Hand on chin, board ready
- **Playing** (144, 0, 48x80) - Moving piece
- **Checkmate Victory** (192, 0, 48x80) - Slight smirk

### The Poseur (48x80 each):
- **Philosophizing** (240, 0, 48x80) - Dramatic hand gesture
- **Phone Mode** (288, 0, 48x80) - Suddenly professional
- **Filming Chaos** (336, 0, 48x80) - Phone held up

### Tourist Couple (64x80 each):
- **Sitting Nervous** (0, 80, 64x80) - Both uncomfortable
- **Price Checking** (64, 80, 64x80) - Him grimacing at menu
- **Alarmed** (128, 80, 64x80) - Pointing at horse
- **Evacuating** (192, 80, 64x80) - Running, him filming

### Chef Konrad (48x80 each):
- **Cooking** (0, 160, 48x80) - Normal kitchen work
- **Panic** (48, 160, 48x80) - Arms raised, screaming
- **Ladle Brandish** (96, 160, 48x80) - Defensive position
- **Aftermath** (144, 160, 48x80) - Thousand-yard stare

### Sous Chef Anna (48x80 each):
- **Working** (192, 160, 48x80) - Prep work
- **Amused** (240, 160, 48x80) - Slight smile at chaos
- **Quote Delivery** (288, 160, 48x80) - "Better taste than tourists"

### NPC Notes:
- The Intellectual wears tweed, coffee-stained
- Greta dressed simply in black, silver jewelry
- Poseur in black turtleneck, oversized glasses
- Tourists in obvious travel wear, money belts visible
- Kitchen staff in chef whites, Konrad with tall hat

---

## 🏛️ Sprite Sheet 4: Landmarks & Major Props
**File:** `cafe_sachertorte_landmarks.png`  
**Dimensions:** 512x384 pixels  
**Color Palette:** #3D2314 (Sachertorte Brown), #FBCEB1 (Apricot), #CFB53B (Gold)

### The Cake Display Case (96x128 each):
- **Pristine** (0, 0, 96x128) - All cakes perfect, lights on
- **Post-Heist** (96, 0, 96x128) - Sachertorte missing, crumbs
- **Secured** (192, 0, 96x128) - Post-repair with lock, memorial photo

### Individual Cakes (32x24 each):
- **Sachertorte Whole** (0, 128, 32x24) - The star, chocolate gleam
- **Sachertorte Slice** (32, 128, 24x20) - Cross-section visible
- **Opera Cake** (56, 128, 32x24) - Layered stripes
- **Apfelstrudel** (88, 128, 32x20) - Golden, powdered sugar
- **Gugelhupf** (120, 128, 32x24) - Ring shape
- **The Gustav Cookie** (152, 128, 24x20) - Horse-shaped, post-quest

### Crystal Chandelier (80x64 each):
- **Static** (0, 152, 80x64) - Hanging normally
- **Swaying Frame 1** (80, 152, 80x64) - Slight tilt left
- **Swaying Frame 2** (160, 152, 80x64) - Slight tilt right
- **Intact After Near Miss** (240, 152, 80x64) - With relief sparkle

### Wall Décor:
- **Emperor's Letter** (0, 216, 48x64) - Framed, 'aged' paper
- **Trophy Case** (48, 216, 64x80) - Awards stopping at 1999
- **Wall of Shame** (112, 216, 48x64) - Post-quest, Gustav photo
- **No Horses Sign** (160, 216, 32x24) - Post-quest addition

### Service Items:
- **Newspaper Stand** (0, 296, 32x48) - Wooden holder with papers
- **Chess Set** (32, 296, 48x48) - Elaborate, mid-game
- **Menu Stand** (80, 296, 24x40) - Leather-bound menu
- **Silver Tray** (104, 296, 32x24) - With coffee service

---

## 💥 Sprite Sheet 5: Destruction Sequence
**File:** `cafe_sachertorte_destruction.png`  
**Dimensions:** 256x192 pixels  
**Color Palette:** #FFFDD0 (Marble), #3D2314 (Wood), #808080 (Debris)

### Marble Table Destruction (3 states):
- **Intact** (0, 0, 32x32) - Perfect marble-topped table
- **Tipping** (32, 0, 40x32) - Mid-fall, marble sliding
- **Fallen** (72, 0, 48x24) - On side, marble cracked

### Patio Table Destruction (2 states):
- **Intact** (0, 32, 40x40) - Wrought-iron outdoor table
- **Crashed** (40, 32, 48x32) - Toppled, bent legs

### Umbrella Stand (2 states):
- **Upright** (0, 72, 24x48) - Brass, with parasols
- **Toppled** (24, 72, 48x24) - Dented, parasols scattered

### Sachertorte Consumption (3 states):
- **Intact Cake** (0, 120, 32x24) - Whole, gleaming
- **Bitten** (32, 120, 32x24) - Gustav's first bite, 28 Sovs gone
- **Devoured** (64, 120, 32x24) - Empty pedestal, crumbs

### Opera Cake Grab:
- **Slice Present** (96, 120, 24x20) - On display
- **Slice Gone** (120, 120, 24x20) - Empty spot with crumbs

### Debris Elements:
- **Cake Crumbs** (0, 144, 48x16) - Scattered chocolate pieces
- **Shattered Porcelain** (48, 144, 64x32) - Broken plates/cups
- **Bent Umbrella** (112, 144, 32x24) - Damaged parasol

### Animation Notes:
- Table tipping should take 0.3 seconds
- Cake consumption holds on "Bitten" state for dramatic effect
- Debris should scatter with physics feel

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `cafe_sachertorte_effects.png`  
**Dimensions:** 256x128 pixels  
**Color Palette:** #FFFFFF (Steam), #FFFACD (Light), #3D2314 (Chocolate)

### Coffee Steam (16x32 each, 3 frames):
- **Steam Frame 1** (0, 0, 16x32) - Rising from cup
- **Steam Frame 2** (16, 0, 16x32) - Dispersing
- **Steam Frame 3** (32, 0, 16x32) - Fading

### Dust Motes (64x64):
- **Window Light Particles** (48, 0, 64x64) - Floating dust in light beam

### Damage Effects:
- **Impact Burst** (0, 32, 32x32) - Table crash
- **Porcelain Shatter** (32, 32, 48x32) - Breaking china
- **Glass Rattle** (80, 32, 32x24) - Display case shake

### Lighting Effects:
- **Window Light Beam** (0, 64, 32x64) - Angled afternoon sun
- **Chandelier Glow** (32, 64, 48x48) - Warm light emanation
- **Candle Flicker** (80, 64, 16x24) - Evening table candles

### UI Particles:
- **Sovs Word Float** (0, 96, 16x16) - Rising particle for the damage counter. **No currency glyph exists — the word is the symbol.** ⚠️ **CELL TOO SMALL** for `SOVS`: either widen to 48x16, or keep 16x16 and float a plain coin/impact mote with the word carried by the **Price Popup** text bubble instead.
- **Price Popup** (16, 96, 48x24) - "+85 Sovs" style text bubble
- **Damage Counter BG** (64, 96, 120x32) - Running total display

---

## 🖥️ Sprite Sheet 7: UI Elements
**File:** `cafe_sachertorte_ui.png`  
**Dimensions:** 256x192 pixels  
**Color Palette:** #3D2314 (Menu Brown), #CFB53B (Gold), #FFFFFF (Text)

### Menu Interface:
- **Menu Frame** (0, 0, 160x128) - Leather-bound look
- **Menu Tab Beverages** (160, 0, 48x24) - Coffee icon
- **Menu Tab Cakes** (160, 24, 48x24) - Cake icon
- **Price Tag** (160, 48, 32x16) - Gold-trimmed

### Damage Tracking:
- **Damage Counter Background** (0, 128, 120x32) - "Damages: 340 SOVS"
- **Sovs Wordmark** (120, 128, 24x24) - Atlas key `sovs_symbol`. **The symbol is the word — letter `SOVS`, never draw a currency mark.** ⚠️ **CELL TOO SMALL:** four characters will not read at 24x24. Widen to 48x16 (the size allotted in `cafe_sachertorte_sprite_mapping.json`, which requires re-flowing the y=128 row to make room beside **Debt Indicator**), or delete the tile and letter `SOVS` inline in the counter string.
- **Damage Item Entry** (0, 160, 200x24) - Itemized line

### Debt System:
- **Debt Indicator** (144, 128, 64x24) - "Debt: 340 Sovs"
- **Payment Slider** (144, 152, 80x20) - For partial payments
- **Valued Patron Badge** (208, 128, 48x48) - Unlock reward

### Status Icons:
- **Caffeinated** (0, 184, 24x24) - Coffee cup with lightning
- **Sugar Rush** (24, 184, 24x24) - Cake with sparkles
- **Humiliated** (48, 184, 24x24) - Red face icon

---

## 🎬 Animation Specifications

### Herr Ober Judgment:
- **Duration:** 1.5 seconds (hold on final frame)
- **Frames:** 3
- **Pattern:** Frame 1 → 2 → 3, hold frame 3
- **Trigger:** Player orders incorrectly, in English, or under-tips
- **Purpose:** The café's core social weapon — disapproval as ambience
- **Audio Sync:** Faint disappointed exhale on frame 3
- **Mobile Optimization:** None needed

### Herr Ober Horror:
- **Duration:** ~0.67 seconds, single play
- **Frames:** 4
- **Pattern:** Frame 1 → 4, no loop
- **Trigger:** Gustav's entry through the patio door
- **Purpose:** Thirty years of service collapsing in four frames
- **Audio Sync:** German exclamation on frame 1
- **Mobile Optimization:** None needed

### Herr Ober Fury:
- **Duration:** 0.75 second loop
- **Frames:** 3
- **Pattern:** Loop while debt dialogue is active
- **Trigger:** Post-rampage confrontation
- **Purpose:** Drives the 340 Sovs debt-assignment scene
- **Audio Sync:** None (dialogue carries it)
- **Mobile Optimization:** None needed

### Coffee Steam:
- **Duration:** 1.5 second cycle
- **Frames:** 3
- **Pattern:** Rise → disperse → fade, loop
- **Trigger:** Constant on served cups and counter
- **Purpose:** Warm, expensive stillness before the storm
- **Audio Sync:** None
- **Mobile Optimization:** Halve emitter density (8 → 4 sources)

### Marble Table Tipping:
- **Duration:** 0.3 seconds
- **Frames:** 3 (intact → tipping → fallen)
- **Pattern:** Single play, hold fallen state
- **Trigger:** Gustav collision during rampage
- **Purpose:** Each crash increments the damage counter — comedy through accounting
- **Audio Sync:** Crash + cash-register ching on impact frame
- **Mobile Optimization:** None needed

### Sachertorte Consumption:
- **Duration:** ~2 seconds (hold on Bitten for dramatic effect)
- **Frames:** 3 states (intact → bitten → devoured)
- **Pattern:** State advance per bite event
- **Trigger:** Gustav reaching the display case
- **Purpose:** The 28 Sovs bite — the quest's signature crime
- **Audio Sync:** Disturbing eating sounds per bite
- **Mobile Optimization:** None needed

### Chandelier Sway:
- **Duration:** 2 second cycle during chaos
- **Frames:** 3 (static → left → right)
- **Pattern:** Left ↔ right pendulum, settle to "near miss" state
- **Trigger:** Rampage screen shake
- **Purpose:** Sustained will-it-fall tension (it never falls — the relief sparkle is the punchline)
- **Audio Sync:** Crystal tinkle on each direction change
- **Mobile Optimization:** Static frame on low-end devices

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cake display case outline | set at sheet layout | 96x128 | High-contrast frame around the primary interactable |
| Herr Ober outline overlay | set at sheet layout | 48x96 | Key NPC silhouette against dark mahogany |
| Menu stand highlight | set at sheet layout | 24x40 | Enhanced-visibility marker for the order interaction |
| Patio door frame | set at sheet layout | 32x64 | Marks Gustav's entry point / exit route |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chandelier static frame | set at sheet layout | 80x64 | No sway during chaos; state changes only |
| Steam-free cup overlay | set at sheet layout | 16x32 | Removes looping steam particles |
| Dust-mote-free window beam | set at sheet layout | 32x64 | Static light beam without floating particles |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| German exclamation burst | set at sheet layout | 32x24 | Speech-shock glyph over Herr Ober when the horror cry fires |
| Crash/ching burst | set at sheet layout | 32x32 | Impact star + damage numeral for every destruction sound. **No currency glyph** — the word `SOVS` is lettered in the damage popup, not here. ⚠️ 32x32 cannot hold `SOVS` beside the star; widen to 48x32 if the word must appear in the burst itself. |
| Eating-sounds indicator | set at sheet layout | 24x24 | Munch glyph over Gustav during consumption audio |
| Crystal tinkle sparkle | set at sheet layout | 16x16 | Glint marks on chandelier per tinkle |

### Colorblind Considerations:
- Damage popups pair the numeral and the word `SOVS` with impact-star shapes, never color alone
- Status icons (Caffeinated / Sugar Rush / Humiliated) use distinct silhouettes, not just tint
- Menu price tags readable as text; hidden charges italicized, not color-flagged
- Touch zones minimum 44px for menu, display case, and payment interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); cake display case needs ASTC 4x4 — the Sachertorte must gleam
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for landmarks sheet (display case is screenshot-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cafe_environment | tileset, landmarks, destruction | 1024x1024 |
| cafe_characters | Herr Ober, regulars & staff | 1024x512 |
| cafe_effects_ui | effects, UI elements | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full steam (8 sources), dust motes, candle flicker, chandelier sway, all debris particles |
| Medium | 4 steam sources, no dust motes, reduced debris density |
| Low | Static chandelier, no ambient particles, debris as static sprites |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 40 per frame
- **Memory Footprint:** 38 MB maximum
- **Particle Limit:** 30 (steam 8, dust 15 → rampage swaps to crumbs 30 / porcelain 20, never concurrent)

### Performance Notes:
- Rampage particle systems (cake crumbs, shattered porcelain) replace ambient systems rather than stacking on top
- Kitchen zone sprites load on-demand (only visible during Konrad/Anna scenes)
- Post-quest state swaps (secured case, memorial, No Horses sign) are static texture switches, zero runtime cost

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Use AnimatedSprite2D for character states
- CPUParticles2D for steam and debris
- CanvasLayer for damage counter UI overlay
- Location state machine: pre_quest → during_quest → post_quest_unpaid → post_quest_paid drives sprite set swaps

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Herr Ober horror animation | German exclamation | On frame 1 of horror |
| Table destruction | Crash sound + register ching | On impact frame |
| Gustav cake consumption | Disturbing eating sounds | Per bite state change |
| Chandelier sway | Crystal tinkle | On each direction change |
| Judgment animation | Disappointed exhale | On held frame 3 |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Fiaker Fiasco (café phase) | Gustav entry, chaos sprites, evacuation NPCs | Phase start: Gustav entry triggers chaos state |
| Fiaker Fiasco (damage tracking) | Destruction states, price popups, counter UI | Each destruction increments `fiaker_fiasco_damage_sov` (+340 Sovs café total) |
| Fiaker Fiasco (aftermath) | Damaged tileset states, hostile Herr Ober set | Post-quest unpaid: staff hostile, café closed 24h |
| Debt repayment | Debt receipt, payment slider, Valued Patron badge | Debt cleared: commemorative menu, Gustav Cookie, friendly staff |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Opera House Plaza | Gustav sprites shared (incoming chase) | Chase hand-off from plaza terraces |
| Opera Backstage (Bassline Opera House) | Gustav continues (outgoing chase); Herr Ober may appear chasing bros | Patio-door exit toward the alley |
| The Moderato Pub | Retreat point reference (no shared sprites) | Standard door transition |
| Café Existenz | Same district ambience (Kaffeehaus Row) | None |
| All Fiaker Fiasco locations | Damage counter UI reused | Persistent CanvasLayer overlay |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Faded grandeur meets modern pretension"
- **Color Mood:** Warm browns and creams with gold accents
- **Lighting:** Soft, warm interior glow; dramatic afternoon sun
- **Texture:** Aged wood, polished marble, crystal clarity

### Character Design Notes:
- **Herr Ober**: Posture is KEY - ramrod straight degrading to slump
- **Regulars**: Each has defining characteristic (book, chess, phone)
- **Kitchen Staff**: Konrad's tall hat should be memorable
- **Everyone except Intellectual reacts to Gustav**

### Environmental Storytelling:
- Trophy case awards stopping at 1999 = decline hint
- Emperor's letter slightly too pristine = fake
- Worn spots on marble floor = regulars' usual seats
- Post-quest changes tell story (memorial, sign, secured case)

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Gustav examining cakes** with connoisseur expression
2. **Damage counter hitting 340 Sovs** with Herr Ober's fury
3. **The Intellectual unfazed** while chaos surrounds
4. **The Gustav cookie** on post-quest menu

### TikTok Potential:
- "POV: A horse just ate your entire Sachertorte inventory"
- "When the 18 Sovs cake slice hits different"
- "The damage counter going crazy"
- "One man. One horse. 340 Sovs in damages."

### Quote Potential:
- "That horse has better taste than most tourists." - Sous Chef Anna
- "In thirty years of service... a HORSE." - Herr Ober
- "340 Sovs. You will pay this. Now." - Herr Ober
- "I've been coming here for 40 years. This is the most exciting thing that's ever happened." - The Intellectual

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | cafe_sachertorte_tileset.png | 1024x512 |
| 2 | herr_ober_waiter.png | 384x288 |
| 3 | cafe_sachertorte_npcs.png | 384x288 |
| 4 | cafe_sachertorte_landmarks.png | 512x384 |
| 5 | cafe_sachertorte_destruction.png | 256x192 |
| 6 | cafe_sachertorte_effects.png | 256x128 |
| 7 | cafe_sachertorte_ui.png | 256x192 |

**Total Estimated Memory:** ~4 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `cafe_sachertorte_tileset.png` (1024x512)
- [ ] `herr_ober_waiter.png` (384x288)
- [ ] `cafe_sachertorte_npcs.png` (384x288)
- [ ] `cafe_sachertorte_landmarks.png` (512x384)
- [ ] `cafe_sachertorte_destruction.png` (256x192)
- [ ] `cafe_sachertorte_effects.png` (256x128)
- [ ] `cafe_sachertorte_ui.png` (256x192)

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
- **Documentation:** Animation timing reference sheet + quest-state sprite swap guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] Herr Ober's posture consistent across all states
- [ ] Cake display shows correct contents per state
- [ ] Destruction sequences read clearly at game resolution
- [ ] The Intellectual sprite literally unchanged across all states
- [ ] Damage counter UI readable on mobile screens
- [ ] Steam particles loop seamlessly
- [ ] All furniture matches EarthBound oblique style
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Café feels refined yet fragile
- [ ] Chaos sequence reads clearly
- [ ] Emotional arc of Herr Ober is palpable
- [ ] Economic satire elements visible (hidden charges, prices)
- [ ] Post-quest changes tell complete story
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Viennese café culture evoked, never named |
| Cultural Specificity | ✅ | Kaffeehaus tradition, Sachertorte reverence, waiter-as-institution |
| Satirical Targets Appropriate | ✅ | Tourist exploitation, hidden charges, pretension economy — punches up |
| Seedy Underbelly Present | ✅ | Fake Emperor's letter, "American adjustment" surcharge, tourist detection pricing |
| Gameplay Value Established | ✅ | Shop, quest phase 2, debt system, status effects, Valued Patron path |
| Technical Feasibility | ✅ | Seven sheets, atlas plan, LOD tiers documented |
| Mobile Performance Budget | ✅ | 60 FPS, 40 draw calls, 38 MB, 30 particles |
| Accessibility Features | ✅ | Visual cues for all audio events; static motion variants |
| No Crypto Elements | ✅ | None present |
| Social Media Integration | ✅ | Cake heist and damage-counter moments identified |

**Café Sachertorte: Where Vienna's famous 18 Sovs cake slice meets a horse with expensive taste and zero impulse control.**
