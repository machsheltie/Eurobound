# Café Sachertorte - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Café Sachertorte location - a high-end Viennese café that becomes ground zero for Gustav's €340 rampage during the Fiaker Fiasco sidequest.

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
- **Debt Receipt** (188, 192, 24x32) - Paper with €340

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

### Chess Master Helena (48x80 each):
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

### Chef Klaus (48x80 each):
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
- Helena dressed simply in black, silver jewelry
- Poseur in black turtleneck, oversized glasses
- Tourists in obvious travel wear, money belts visible
- Kitchen staff in chef whites, Klaus with tall hat

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
- **Bitten** (32, 120, 32x24) - Gustav's first bite, €28 gone
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
- **Euro Symbol Float** (0, 96, 16x16) - For damage counter
- **Price Popup** (16, 96, 48x24) - "+€85" style text bubble
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
- **Damage Counter Background** (0, 128, 120x32) - "Damages: €"
- **Euro Symbol Large** (120, 128, 24x24) - For totals
- **Damage Item Entry** (0, 160, 200x24) - Itemized line

### Debt System:
- **Debt Indicator** (144, 128, 64x24) - "Debt: €340"
- **Payment Slider** (144, 152, 80x20) - For partial payments
- **Valued Patron Badge** (208, 128, 48x48) - Unlock reward

### Status Icons:
- **Caffeinated** (0, 184, 24x24) - Coffee cup with lightning
- **Sugar Rush** (24, 184, 24x24) - Cake with sparkles
- **Humiliated** (48, 184, 24x24) - Red face icon

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Use AnimatedSprite2D for character states
- CPUParticles2D for steam and debris
- CanvasLayer for damage counter UI overlay

### Audio Sync Points:
- Herr Ober horror animation syncs with German exclamation
- Table destruction syncs with crash sound + register ching
- Gustav cake consumption syncs with disturbing eating sounds
- Chandelier sway syncs with crystal tinkle

### Quest Integration:
- **Phase Start**: Gustav entry triggers chaos sprites
- **Damage Tracking**: Each destruction increments counter
- **Aftermath**: Switch to damaged state sprites
- **Post-Quest**: Secured/memorial sprites load

### Cross-Location Dependencies:
- Gustav sprites shared with Opera House Plaza/Backstage
- Damage counter UI reused across all Fiaker Fiasco locations
- Herr Ober may appear in Opera Backstage (chasing bros)

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme**: "Faded grandeur meets modern pretension"
- **Color Mood**: Warm browns and creams with gold accents
- **Lighting**: Soft, warm interior glow; dramatic afternoon sun
- **Texture**: Aged wood, polished marble, crystal clarity

### Character Design Notes:
- **Herr Ober**: Posture is KEY - ramrod straight degrading to slump
- **Regulars**: Each has defining characteristic (book, chess, phone)
- **Kitchen Staff**: Klaus's tall hat should be memorable
- **Everyone except Intellectual reacts to Gustav**

### Environmental Storytelling:
- Trophy case awards stopping at 1999 = decline hint
- Emperor's letter slightly too pristine = fake
- Worn spots on marble floor = regulars' usual seats
- Post-quest changes tell story (memorial, sign, secured case)

---

## 📦 File Delivery Checklist

### Required PNG Files (7 Total):
- [ ] `cafe_sachertorte_tileset.png` (1024x512)
- [ ] `herr_ober_waiter.png` (384x288)
- [ ] `cafe_sachertorte_npcs.png` (384x288)
- [ ] `cafe_sachertorte_landmarks.png` (512x384)
- [ ] `cafe_sachertorte_destruction.png` (256x192)
- [ ] `cafe_sachertorte_effects.png` (256x128)
- [ ] `cafe_sachertorte_ui.png` (256x192)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG
- **Naming Convention:** snake_case, all lowercase

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Gustav examining cakes** with connoisseur expression
2. **Damage counter hitting €340** with Herr Ober's fury
3. **The Intellectual unfazed** while chaos surrounds
4. **The Gustav cookie** on post-quest menu

### TikTok Potential:
- "POV: A horse just ate your entire Sachertorte inventory"
- "When the €18 cake slice hits different"
- "The damage counter going crazy"
- "One man. One horse. €340 in damages."

### Quotable Content:
- "That horse has better taste than most tourists." - Sous Chef Anna
- "In thirty years of service... a HORSE." - Herr Ober
- "€340. You will pay this. Now." - Herr Ober
- "I've been coming here for 40 years. This is the most exciting thing that's ever happened." - The Intellectual

---

## ✅ Final Validation

### Before Submitting Assets:
- [ ] Herr Ober's posture consistent across all states
- [ ] Cake display shows correct contents per state
- [ ] Destruction sequences read clearly at game resolution
- [ ] The Intellectual sprite literally unchanged across all states
- [ ] Damage counter UI readable on mobile screens
- [ ] Steam particles loop seamlessly
- [ ] All furniture matches EarthBound oblique style

### Quality Checkpoints:
- [ ] Café feels refined yet fragile
- [ ] Chaos sequence reads clearly
- [ ] Emotional arc of Herr Ober is palpable
- [ ] Economic satire elements visible (hidden charges, prices)
- [ ] Post-quest changes tell complete story
- [ ] Mobile performance optimized

**Café Sachertorte: Where Vienna's famous €18 cake slice meets a horse with expensive taste and zero impulse control.**
