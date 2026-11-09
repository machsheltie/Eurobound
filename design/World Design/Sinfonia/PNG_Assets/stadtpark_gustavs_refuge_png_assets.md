# Stadtpark (Gustav's Refuge) - Complete PNG Asset Requirements

*Artist Reference Document for Fiaker Fiasco's Emotional Finale*

**Location ID**: `sinfonia_stadtpark_gustavs_refuge_01`  
**Priority**: HIGH (Quest Resolution, Emotional Climax, Multiple Endings)  
**Total Sheets Required**: 10  
**Mobile Optimization**: Target 60 FPS on iPhone 8+

---

## Art Direction Summary

### Visual Identity
The Stadtpark at night is a **moonlit sanctuary turned dramatic stage**—ancient trees casting long shadows, Victorian lampposts creating pools of golden light, and at the center, a single white horse making his last stand. This is where absurdist comedy meets genuine emotion.

### Key Visual Themes
- **Moonlit Drama**: Cool blue moonlight contrasting warm lamplight
- **Romantic Park Aesthetic**: Victorian elegance, manicured nature
- **Emotional Weight**: The horse should look genuinely tired, defiant, sympathetic
- **Satirical Backdrop**: Johann Strauss watches cultural chaos unfold

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Moonlit Night Blue | #2C3E50 | Sky, shadows, ambient |
| Lamp Light Gold | #F4D03F | Lamppost glow, warm highlights |
| Grass Dark Green | #1E4D2B | Lawn, vegetation base |
| Path Gravel Grey | #7F8C8D | Walking paths |
| Gustav White | #F5F5F5 | Horse coat (moonlit) |
| Statue Gold | #FFD700 | Johann Strauss gilding |
| Skittles Rainbow | Various | Key item highlights |

---

## SHEET 1: Park Tileset
**Filename**: `stadtpark_tileset.png`  
**Dimensions**: 1024 × 768 pixels  
**Tile Size**: 32 × 32 pixels

### Ground Tiles (Row 0)
- **Grass Dark**: Base lawn tile, slightly blue-tinged (moonlight)
- **Grass Light**: Moonlit highlights on grass
- **Grass Moonlit**: Directly illuminated grass
- **Gravel Path**: Main walking surface, neutral grey
- **Gravel Path Edge**: Transition to grass
- **Flower Bed Intact**: Colorful flowers, ornamental
- **Flower Bed Trampled**: Gustav's destruction path (crushed flowers, hoofprints)
- **Water Pond**: Reflective water surface

### Vegetation (Rows 1-3)
- **Oak Tree Base**: Trunk section (64×96)
- **Oak Tree Canopy**: Full leafy crown (96×96)
- **Hedge Section**: Manicured hedge (64×32)
- **Hedge Corner**: Corner piece for garden borders
- **Rose Bush**: Decorative roses
- **Autumn Leaves (Ground)**: Scattered leaves on path

### Furniture (Row 4-6)
- **Bench Cast Iron**: Victorian-style park bench (64×32)
- **Lamppost**: Three-tile-high ornate lamppost with glow area
- **Drinking Fountain**: Small stone fountain
- **Trash Bin**: Period-appropriate waste receptacle
- **Park Sign**: "STADTPARK" wooden sign

### Buildings (Rows 7-8)
- **Restroom Building**: Small utility building (96×64), locked
- **Ranger Station**: Similar style, with schedule on door
- **Bandstand Base**: White pavilion foundation (128×64)
- **Bandstand Roof**: Ornate white roof structure (128×64)

---

## SHEET 2: Johann Strauss Monument
**Filename**: `johann_strauss_statue.png`  
**Dimensions**: 128 × 192 pixels

### Design Requirements
- **Pose**: Famous "Waltz King" pose, violin raised mid-performance
- **Material**: Golden bronze gilding (should gleam in moonlight)
- **Base**: White marble pedestal, worn from decades of tourist touches
- **Expression**: Serene, eternal, oblivious to horse drama below
- **Scale**: Imposing, approximately 3x character height

### Animation
- Subtle golden shimmer (2 frames, 0.5 FPS)
- Moonlight reflection points

*Art Note*: The statue provides ironic cultural contrast—high Viennese art watching American tourists negotiate with candy.

---

## SHEET 3: Ornamental Pond Tileset
**Filename**: `ornamental_pond.png`  
**Dimensions**: 256 × 256 pixels

### Pond Components
- **Center Water**: Deep blue-green, reflective
- **Edge Tiles**: North, South, East, West transitions
- **Corner Tiles**: NE, NW, SE, SW for smooth pond outline
- **Fountain Center**: Animated water spray (4 frames)
- **Lily Pads**: Small decorative elements

### Swan Zone
- Sleeping swans should be visible near edge
- Area should feel deceptively peaceful
- Hidden danger aesthetic

---

## SHEET 4: Gustav the Horse (Quest Finale State)
**Filename**: `npc_gustav_horse.png`  
**Dimensions**: 512 × 384 pixels  
**Sprite Size**: 64 × 64 pixels (larger character for drama)

### Character Design
- **Breed**: Lipizzan (white/grey coat)
- **Age**: Visible age—16 years of carriage service shows
- **Condition**: Exhausted but defiant
- **Costume**: Tattered opera cape still attached, café feathers in mane
- **Eyes**: Intelligent, tired, hopeful

### Animation States (9 rows)

**Row 0: Defiant Stand** (2 frames, 0.5 FPS)
- Weight shifted, head high
- Cape flowing slightly in breeze
- Steam from breath (particle overlay)

**Row 1: Heavy Breathing** (4 frames, 2 FPS)
- Flanks heaving visibly
- Steam puffs with each exhale
- Exhaustion evident

**Row 2: Ears Perk** (2 frames, 4 FPS)
- Reaction to Skittles/Papageno
- Interest sparked
- Hope emerging

**Row 3: Backing Away** (4 frames, 3 FPS)
- Response to Hans-Jürgen initially
- Defensive posture
- Not aggressive, just wary

**Row 4: Cautious Approach** (4 frames, 2 FPS)
- Moving toward Skittles
- Each step deliberate
- Trust building

**Row 5: Eating Skittles** (4 frames, 3 FPS)
- Head lowered to hand
- Obvious enjoyment
- Key emotional moment

**Row 6: Nuzzle** (3 frames, 2 FPS)
- Gentle nuzzle against Hans-Jürgen
- Forgiveness expressed
- Heartwarming

**Row 7: Bolting** (6 frames, 8 FPS)
- Full gallop escape
- Cape streaming
- Used for Path C (escape ending)

**Row 8: Trot Into Moonlight** (6 frames, 4 FPS)
- Majestic departure
- Head high, free
- Used for Path B (retirement ending)

*Art Note*: Gustav is the emotional core. His expressions must convey 16 years of service, current exhaustion, and the hope for something better. He's not a cartoon horse—he's a character.

---

## SHEET 5: Hans-Jürgen (Stadtpark State)
**Filename**: `npc_hans_jurgen_stadtpark.png`  
**Dimensions**: 288 × 384 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Updates from Previous Phases
- Even more disheveled than Opera House
- Lederhosen fully askew
- Visible panic sweat
- Carrying Gustav's halter (prop)
- Emotional range: desperate → guilty → accepting/relieved

### Animation States (6 rows)

**Row 0: Running Desperate** (6 frames, 6 FPS)
- Full sprint, out of breath
- Arms pumping, halter in hand

**Row 1: Out of Breath** (2 frames, 1 FPS)
- Hands on knees
- Gasping

**Row 2: Pleading** (4 frames, 2 FPS)
- Arms outstretched toward Gustav
- Desperation in posture

**Row 3: Crying** (2 frames, 1 FPS)
- Head bowed
- Shoulders shaking
- Actual tears if possible

**Row 4: Relief/Reunion** (4 frames, 2 FPS)
- Path A ending
- Arms open, joy

**Row 5: Accepting Goodbye** (3 frames, 2 FPS)
- Path B ending
- Bittersweet wave
- Letting go

---

## SHEET 6: Pigeon Lady (Park Appearance)
**Filename**: `npc_pigeon_lady.png`  
**Dimensions**: 192 × 192 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- Same cryptic elderly woman from Plaza
- Surrounded by pigeons even at night (how?)
- Knowing smile
- Mystic but grounded

### Animation States (3 rows)

**Row 0: Standing with Pigeons** (2 frames)
- Default idle
- Pigeons around feet (5-6 birds)

**Row 1: Cryptic Gesture** (3 frames)
- Vague hand wave
- Indicating Gustav
- Mysterious wisdom pose

**Row 2: Listening to Gustav** (2 frames)
- Tilted head
- As if hearing something others can't

---

## SHEET 7: Aggressive Swans
**Filename**: `aggressive_swans.png`  
**Dimensions**: 192 × 128 pixels  
**Sprite Size**: 48 × 32 pixels

### Swan States (4 rows)

**Row 0: Sleeping** (2 frames, peaceful)
**Row 1: Alert** (2 frames, neck raised)
**Row 2: Attacking** (4 frames, hissing, wings spread)
**Row 3: Swimming** (4 frames, elegant movement)

*Art Note*: These swans look beautiful but are MEAN. The attack animation should be genuinely intimidating.

---

## SHEET 8: Ambient NPCs
**Filename**: `stadtpark_ambient_npcs.png`  
**Dimensions**: 288 × 256 pixels

### Homeless Philosopher (Rows 0-1)
- Academic robes, worn
- Surrounded by books
- Empty bottle nearby
- **Sitting**: 2 frames
- **Gesturing Wisdom**: 3 frames
- **Drinking**: 2 frames

### Making Out Couple (Row 2)
- Two figures on bench, intertwined
- Completely oblivious
- Single animation: slight movement
- 64×48 sprite (double width)

### Sleeping Tourist (Row 3)
- Sprawled on bench
- Guidebook as pillow
- Camera around neck
- Does not wake (2 frame breathing)

---

## SHEET 9: Skittles Item
**Filename**: `item_skittles.png`  
**Dimensions**: 128 × 64 pixels

### States
- **Bag Closed**: Crinkly American candy bag (32×32)
- **Bag Open**: Top opened, visible candy (32×32)
- **Handful**: Colorful pile in palm (32×32)
- **Single Skittle**: Each color (16×16 each)
  - Red, Orange, Yellow, Green, Purple

*Art Note*: The Skittles should be immediately recognizable as American candy. The bag should say "SKITTLES" and "TASTE THE RAINBOW."

---

## SHEET 10: Effects and Particles
**Filename**: `stadtpark_effects.png`  
**Dimensions**: 256 × 256 pixels

### Effects
- **Breath Steam**: White puffs from Gustav (32×32, 4 frames)
- **Autumn Leaf Fall**: Various colors drifting (16×16, 6 frames)
- **Lamplight Glow**: Golden circular gradient (64×64, 2 frames subtle pulse)
- **Moonbeam**: Dramatic light shaft on Gustav (96×128, 2 frames)
- **Fountain Spray**: Water particles (64×48, 4 frames)
- **Pigeon Feathers**: Small floating feathers (16×16, 4 frames)

---

## Lighting Requirements

### Nighttime Lighting
- **Ambient**: Cool blue (#2C3E50), 30% intensity
- **Moonlight**: Soft white-blue (#C0C0FF), 40% global
- **Lamppost Pools**: Warm gold (#F4D03F), 70%, 60px radius, 8 points
- **Gustav Spotlight**: Subtle moonbeam effect on central lawn

### Resolution Scene Lighting
- **Path A (Return)**: Warmer tones, golden highlights
- **Path B (Retire)**: Cool moonlight, silver-blue, bittersweet
- **Path C (Escape)**: Dramatic shadows, horse disappears into darkness
- **Path D (Bail)**: Unchanged, cold, guilty

---

## Social Media Viral Moments

### Key Screenshot Opportunities
1. **Gustav's Defiant Stand**: Moonlit horse with cape, steam breath
2. **Skittles Diplomacy**: American candy held out to Austrian horse
3. **Hans-Jürgen's Breakdown**: Emotional German man and his horse
4. **The Nuzzle**: Reunion moment (Path A)
5. **Trotting Into Moonlight**: Freedom scene (Path B)
6. **Strauss Watching**: Statue backdrop to chaos

### Quote-Worthy Visual Moments
- "Taste the Rainbow" bag held toward horse
- Pigeon Lady surrounded by birds at night
- Philosopher offering wisdom for €1
- Sleeping tourist undisturbed by everything

---

## Technical Specifications

### File Format
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **Resolution**: 72 DPI
- **Compression**: Lossless
- **Naming**: snake_case

### Mobile Optimization
- **Texture Atlases**: Maximum 4 at 1024px
- **Draw Calls**: Under 45
- **Memory**: Under 45MB
- **Particles**: Maximum 60
- **Target FPS**: 60

### Animation Guidelines
- **Idle Loops**: 2-4 frames, 0.5-1 FPS
- **Emotional Animations**: 2-4 frames, 1-2 FPS
- **Action Animations**: 4-6 frames, 3-8 FPS
- **Gustav Focus**: Larger sprite, more frames for emotional range

---

## Cross-Reference: Related Assets

### From Previous Phases
- Hans-Jürgen base sprite (more disheveled)
- Pigeon Lady base sprite (same character)
- Papageno sprite (if ally path)
- Director sprite (if pursuing)

### New for This Location
- Gustav in final state (cape, feathers, exhausted)
- Park environment (night lighting)
- Skittles item (key quest object)
- Resolution-specific effects

---

**END OF ASSET REQUIREMENTS**

*Stadtpark: Where a bag of American candy, a runaway Austrian horse, and €2,340 in property damage somehow become the most emotionally resonant moment in the entire game.*
