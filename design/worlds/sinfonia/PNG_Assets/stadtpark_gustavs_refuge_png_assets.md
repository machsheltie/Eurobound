# Stadtpark (Gustav's Refuge) - Complete PNG Asset Requirements

*Artist Reference Document for Fiaker Fiasco's Emotional Finale*

## 📋 Overview
The Stadtpark at night is a moonlit sanctuary turned dramatic stage — ancient trees, Victorian lampposts, a gilded Johann Strauss statue, and at the center a single exhausted white horse making his last stand. This document specifies every sprite sheet for the Fiaker Fiasco finale, where a bag of American candy, a runaway Austrian horse, and 2,340 Sovs in property damage somehow become the most emotionally resonant moment in the entire game.

**Location ID:** `sinfonia_stadtpark_gustavs_refuge_01`
**Theme:** Emotional resolution amid absurdity — freedom versus responsibility, with high Viennese art (Strauss, eternally gilded) watching Americans negotiate with candy
**Zone:** Imperial Park District
**Hours:** Always accessible (24 hours); quest finale plays at night
**Primary Function:** Public park / quest resolution — Fiaker Fiasco phase-4 finale with four resolution paths (Return / Retire / Escape / Bail), Skittles trust mechanic, damage settlement negotiation

**Priority**: HIGH (Quest Resolution, Emotional Climax, Multiple Endings)  
**Total Sheets Required**: 10  
**Performance Optimization**: Target 60 FPS on min-spec hardware

### Key Visual Themes
- **Moonlit Drama**: Cool blue moonlight contrasting warm lamplight
- **Romantic Park Aesthetic**: Victorian elegance, manicured nature
- **Emotional Weight**: The horse should look genuinely tired, defiant, sympathetic
- **Satirical Backdrop**: Johann Strauss watches cultural chaos unfold

---

## 🎨 Color Palette

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

## 📁 File Structure
```
assets/sprites/locations/sinfonia/stadtpark_gustavs_refuge/
├── environment/
│   ├── stadtpark_tileset.png
│   ├── johann_strauss_statue.png
│   └── ornamental_pond.png
├── npcs/
│   ├── npc_gustav_horse.png
│   ├── npc_hans_jurgen_stadtpark.png
│   ├── npc_pigeon_lady.png
│   ├── aggressive_swans.png
│   └── stadtpark_ambient_npcs.png
├── objects/
│   └── item_skittles.png
└── effects/
    └── stadtpark_effects.png
```

---

## 🌳 Sprite Sheet 1: Park Tileset
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

### Retired Horse Stalls (Row 9) — POST-GAME STATE ONLY
Hidden during the main quest; revealed at the north pasture fence once the Fiaker Fiasco epilogue has played.
- **Stall Door Left (Gustav)**: Weathered timber stall door (64×64), open upper half
- **Stall Door Right (Klaus)**: Matching door (64×64), open upper half
- **Nameplate — GUSTAV**: Brass plate (48×16), plain engraved serif, polished
- **Nameplate — KING KLAUS**: Brass plate (48×16), **identical polish and finish**, engraved `KING KLAUS` — legible at default zoom without the examine prompt
- **Pasture Fence Section**: Post-and-rail (64×32), tiles horizontally
- **Examine Glint**: Small specular highlight (16×16) on both plates, marks them interactive

**Art direction — the plates carry an entire running gag, so:**
- Both plates must read as *maintained*: bright brass, no verdigris, clean edges. A neglected plate reads as forgotten; a polished one reads as deliberate, which is the joke.
- The two plates are visually identical in every respect except the engraved text. No decorative crown, no flourish, no size difference on Klaus's — the humour dies the instant the art winks.
- `KING KLAUS` must be readable at 1× without zooming. If the text will not fit legibly at 48×16, widen the plate rather than shrinking the type.
- Gustav's plate is plain `GUSTAV`. Resist any urge to embellish it for balance.

---

## 🎻 Sprite Sheet 2: Johann Strauss Monument
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

## 💧 Sprite Sheet 3: Ornamental Pond Tileset
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

## 🐴 Sprite Sheet 4: Gustav the Horse (Quest Finale State)
**Filename**: `npc_gustav_horse.png`  
**Dimensions**: 512 × 384 pixels  
**Sprite Size**: 64 × 64 pixels (larger character for drama)

### Character Design
- **Breed**: Lipizzan (white/grey coat) — Spanish Riding School reject
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

## 🎩 Sprite Sheet 5: Hans-Jürgen (Stadtpark State)
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

## 🕊️ Sprite Sheet 6: Pigeon Lady (Park Appearance)
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

## 🦢 Sprite Sheet 7: Aggressive Swans
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

## 👥 Sprite Sheet 8: Ambient NPCs
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

## 🌈 Sprite Sheet 9: Skittles Item
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

## ✨ Sprite Sheet 10: Effects and Particles
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

## 🎬 Animation Specifications

### General Animation Guidelines (all sheets)
- **Idle Loops**: 2-4 frames, 0.5-1 FPS
- **Emotional Animations**: 2-4 frames, 1-2 FPS
- **Action Animations**: 4-6 frames, 3-8 FPS
- **Gustav Focus**: Larger sprite, more frames for emotional range

### Gustav Defiant Stand:
- **Duration:** 4 second cycle
- **Frames:** 2
- **Pattern:** Slow loop with breath steam particle overlay
- **Trigger:** Scene opening; default finale idle
- **Purpose:** The last-stand image — exhausted dignity under a moonbeam
- **Audio Sync:** Slow breathing layer; distant city hush
- **Performance Optimization:** None needed

### Gustav Trust Sequence (Ears Perk → Cautious Approach → Eating Skittles → Nuzzle):
- **Duration:** ~0.5s / 2.0s / 1.3s / 1.5s respectively
- **Frames:** 2 / 4 / 4 / 3
- **Pattern:** State advance per Skittles-mechanic phase (attention → approach → eats from hand → trust earned)
- **Trigger:** Player Skittles offering phases 1–4 (or Papageno ally alternative)
- **Purpose:** The entire emotional arc of the quest, rendered in a horse's ears
- **Audio Sync:** Bag crinkle on offer; soft crunch on eating; gentle string swell on nuzzle
- **Performance Optimization:** None needed — this is the scene the game is protecting

### Gustav Bolting (Path C):
- **Duration:** 0.75 second cycle
- **Frames:** 6
- **Pattern:** Full gallop loop, cape streaming, exits into darkness
- **Trigger:** No Skittles + aggressive approach
- **Purpose:** The failure ending — beautiful and gone
- **Audio Sync:** Galloping hoofbeats fading out
- **Performance Optimization:** None needed (one-shot exit)

### Gustav Trot Into Moonlight (Path B):
- **Duration:** 1.5 second cycle
- **Frames:** 6
- **Pattern:** Majestic loop toward the moonbeam, head high
- **Trigger:** Skittles trust + freedom dialogue
- **Purpose:** The liberation ending; screenshot bait by design
- **Audio Sync:** Single warm waltz phrase (Strauss watching approvingly)
- **Performance Optimization:** None needed

### Hans-Jürgen Emotional Arc (Pleading → Crying → Relief or Goodbye):
- **Duration:** 2.0s / 2.0s / 2.0s / 1.5s per state
- **Frames:** 4 / 2 / 4 / 3
- **Pattern:** Dialogue-driven state advance; Relief (Path A) and Goodbye (Path B) are mutually exclusive
- **Trigger:** Resolution-path selection
- **Purpose:** A drunk carriage driver becomes the most sincere man in Sinfonia
- **Audio Sync:** Muffled sobs on Crying; relieved laugh on Reunion
- **Performance Optimization:** None needed

### Swan Attack:
- **Duration:** ~0.8 seconds
- **Frames:** 4
- **Pattern:** Alert → attack burst, returns to swimming
- **Trigger:** Player enters swan zone at pond edge
- **Purpose:** Deceptive peace gag; the park's actual apex predators
- **Audio Sync:** Hiss on wings-spread frame
- **Performance Optimization:** Cap at 2 concurrent attacking swans

### Ambient Loops (Leaves / Lamplight / Moonbeam / Statue Shimmer):
- **Duration:** Leaves ~1.5s drift; lamplight and moonbeam 2-frame subtle pulses at 0.5 FPS; statue shimmer 4s cycle
- **Frames:** 6 / 2 / 2 / 2
- **Pattern:** Constant gentle loops
- **Trigger:** Constant (night state)
- **Purpose:** Moonlit sanctuary atmosphere; nothing moves fast except emotions
- **Audio Sync:** Cricket chorus, distant city layer
- **Performance Optimization:** Leaves reduced to 8 concurrent; moonbeam static on low-end

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gustav outline overlay | set at sheet layout | 64×64 | High-contrast silhouette of the white horse against moonlit grass |
| Skittles offering highlight | set at sheet layout | 32×32 | Bold ring on the interactable candy hand-off zone |
| Swan zone warning outline | set at sheet layout | 48×32 | Enhanced visibility boundary of the pond's hidden danger area |
| Path/lamppost edge markers | set at sheet layout | 32×96 | Contrast-boosted walkway edges for the dark night scene |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static autumn leaves | set at sheet layout | 16×16 | Ground scatter only, no drifting particles |
| Steady lamplight | set at sheet layout | 64×64 | Non-pulsing glow variant |
| Static moonbeam | set at sheet layout | 96×128 | Fixed light shaft, no shimmer |
| Reduced bolting shake | set at sheet layout | full scene | Path C camera shake replaced by fade |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Breath indicator | set at sheet layout | 32×32 | Steam puffs double as the visual for Gustav's breathing audio |
| Bag crinkle sparkle | set at sheet layout | 16×16 | Rainbow glint when the Skittles bag audio plays |
| Swan hiss burst | set at sheet layout | 24×24 | Jagged warning glyph on attack hiss |
| String swell glow | set at sheet layout | 48×48 | Soft radiance on Gustav during the nuzzle music cue |

### Colorblind Considerations:
- Skittles read by shape and in-palm count, and the bag by its lettering, not color alone
- Resolution-path lighting shifts (warm/cool/dark) are paired with distinct character poses per path
- Touch zones minimum 44px for Skittles offering, Gustav approach, and dialogue choices

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) Gustav's sheet stays uncompressed — his expressions carry the finale
- **Fallback:** PNG high-quality for Gustav and the Strauss statue (screenshot critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| stadtpark_environment | park tileset, statue, pond | 1024x1024 |
| stadtpark_characters | Gustav, Hans-Jürgen, Pigeon Lady, swans, ambient NPCs | 1024x1024 |
| stadtpark_effects_items | effects, Skittles | 512x512 |

*(Maximum 4 atlases at 1024px per original spec; max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full leaf drift, breath steam, moonbeam shimmer, 8 lamp pools, statue shimmer |
| Medium | 8 leaves, breath steam kept (emotionally load-bearing), static moonbeam, 4 lamp pools |
| Low | Static ambience, breath steam only, static lighting |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** Under 45
- **Memory Footprint:** Under 45 MB
- **Particle Limit:** 60 (leaves + steam + fountain + feathers combined)

### Performance Notes:
- Night scene is light on geometry; budget goes to Gustav's frame count — protect it
- Resolution-path lighting variants are preset swaps, not runtime shader work
- Ambient NPCs (philosopher, couple, tourist) are low-FPS loops; never exceed 2 FPS

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap for park grounds; AnimatedSprite2D for Gustav/Hans-Jürgen emotional states
- CPUParticles2D (not GPU) for leaves, breath steam, fountain spray, pigeon feathers
- Quest-phase state machine: pre_quest → quest_active → post_quest_a/b/c/d selects sprite sets and lighting presets
- Skittles mechanic runs a 4-phase trust-counter gating Gustav's row transitions

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Gustav breathing (rows 0–1) | Slow breath layer | Steam puff per exhale frame |
| Skittles offering | Bag crinkle | On bag-open state |
| Eating Skittles | Soft crunch | Per eating frame 2 |
| Nuzzle | Gentle string swell | On nuzzle frame 1 |
| Bolting (Path C) | Galloping hoofbeats, fading | Loop start, fade with exit |
| Swan attack | Hiss | On wings-spread frame |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Fiaker Fiasco phase-4 (finale) | Gustav all rows, Hans-Jürgen all rows, Skittles states | Entry from opera side-door; resolution selects Path A/B/C/D |
| Path A — Gustav Returns | Nuzzle, Relief/Reunion, resigned return hand-off | Debt −500 Sovs (insurance), unlocks Fiaker fast travel |
| Path B — Gustav Retires | Trot Into Moonlight, Accepting Goodbye | Gustav becomes permanent park NPC with daily buff |
| Path C — Gustav Escapes | Bolting, Hans-Jürgen Crying | Debt +1,000 Sovs, permanent guilt marker |
| Path D — Bros Bail | Scene unchanged, cold lighting preset | Quest fails, debt +500 Sovs, Coward status |
| Papageno ally alternative | Papageno sprite (from opera house) | Approach possible without Skittles |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bassline Opera House | Quest entry point; Hans-Jürgen base sprite (more disheveled); Director may pursue in fury state; Papageno if ally path | Opera side-door path, night transition |
| Opera House Plaza | Pigeon Lady base sprite (same character); Gustav returns to Fiaker queue on Path A | Post-quest state hand-off |
| Café Sachertorte | Debt connection (damage total includes 340 Sovs café) | Damage counter UI carries over |
| The Moderato Pub | Hans-Jürgen post-quest sad-drunk state (Path C) | NPC relocation, no shared sprites |
| Crown & Cask | Easter egg payoff only — the `KING KLAUS` stall nameplate is an insult aimed at König Klaus. No shared sprites; the two Klauses must never appear in one scene | None — the gag is the ambiguity, resolving it kills it |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Moonlit sanctuary turned dramatic stage" — ancient trees casting long shadows, Victorian lampposts creating pools of golden light, and at the center, a single white horse making his last stand. This is where absurdist comedy meets genuine emotion.
- **Color Mood:** Cool blue moonlight against warm gold lamplight; the palette argues freedom versus responsibility before the dialogue does
- **Lighting:** Night ambient with lamppost pools and a moonbeam reserved for Gustav (see Lighting Requirements below); each resolution path gets its own grade
- **Texture:** Manicured hedges and gravel against trampled flowerbeds — order interrupted by one determined horse

### Environmental Storytelling:
- Trampled flowerbed tiles trace Gustav's exact route into the park
- The gilded Strauss statue gleams over the whole negotiation, serenely indifferent — high art as unhelpful witness
- Sleeping tourist, oblivious couple, and 1 Sov philosopher establish that Sinfonia's absurdity continues even at the emotional climax
- Sleeping swans near the pond edge: deceptively peaceful, genuinely dangerous

### Character Integration Notes:
- Gustav is the emotional core: larger sprite, more frames, expressions conveying 16 years of service — he is a character, not a cartoon horse
- Hans-Jürgen's dishevelment must visibly exceed his opera-house state; the halter prop stays in hand until the resolution
- Pigeon Lady renders identically to her Plaza appearance — continuity is the joke

---

## 💡 Lighting Requirements

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

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Gustav's Defiant Stand**: Moonlit horse with cape, steam breath
2. **Skittles Diplomacy**: American candy held out to Austrian horse
3. **Hans-Jürgen's Breakdown**: Emotional German man and his horse
4. **The Nuzzle**: Reunion moment (Path A)
5. **Trotting Into Moonlight**: Freedom scene (Path B)
6. **Strauss Watching**: Statue backdrop to chaos

### Quote Potential:
- "Taste the Rainbow" bag held toward horse
- Pigeon Lady surrounded by birds at night
- Philosopher offering wisdom for 1 Sov
- Sleeping tourist undisturbed by everything

---

## 📋 Required PNG Files (10 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | stadtpark_tileset.png | 1024x768 |
| 2 | johann_strauss_statue.png | 128x192 |
| 3 | ornamental_pond.png | 256x256 |
| 4 | npc_gustav_horse.png | 512x384 |
| 5 | npc_hans_jurgen_stadtpark.png | 288x384 |
| 6 | npc_pigeon_lady.png | 192x192 |
| 7 | aggressive_swans.png | 192x128 |
| 8 | stadtpark_ambient_npcs.png | 288x256 |
| 9 | item_skittles.png | 128x64 |
| 10 | stadtpark_effects.png | 256x256 |

**Total Estimated Memory:** ~5.5 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `stadtpark_tileset.png` (1024x768)
- [ ] `johann_strauss_statue.png` (128x192)
- [ ] `ornamental_pond.png` (256x256)
- [ ] `npc_gustav_horse.png` (512x384)
- [ ] `npc_hans_jurgen_stadtpark.png` (288x384)
- [ ] `npc_pigeon_lady.png` (192x192)
- [ ] `aggressive_swans.png` (192x128)
- [ ] `stadtpark_ambient_npcs.png` (288x256)
- [ ] `item_skittles.png` (128x64)
- [ ] `stadtpark_effects.png` (256x256)

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
- **Documentation:** Animation timing reference sheet + resolution-path lighting preset guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Gustav's exhaustion and hope both read at gameplay zoom
- [ ] Skittles bag immediately recognizable as American candy
- [ ] Pigeon Lady matches her Plaza sprite exactly
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Absurdist comedy and genuine emotion coexist without undercutting each other
- [ ] All four resolution-path lighting grades are distinct
- [ ] Swan danger zone has discoverable visual cues
- [ ] Performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Stadtpark/Strauss evoke Vienna without naming it |
| Cultural Specificity | ✅ | Viennese park culture, Waltz King monument, Fiaker horse tradition |
| Satirical Targets Appropriate | ✅ | American candy diplomacy, tourist obliviousness, 1 Sov wisdom — punches up |
| Seedy Underbelly Present | ✅ | Night park underclass (philosopher's bottle), vicious swans, guilt economies |
| Gameplay Value Established | ✅ | Quest resolution with four endings, trust mechanic, permanent unlocks |
| Technical Feasibility | ✅ | 10 sheets, atlas plan, LOD tiers documented |
| Performance Budget | ✅ | 60 FPS, <45 draw calls, <45 MB, 60 particles |
| Accessibility Features | ✅ | Visual audio cues, static motion variants, shape-based Skittles reads |
| No Crypto Elements | ✅ | None present |
| Social Media Integration | ✅ | Six screenshot moments identified; Path B built as shareable |

**Stadtpark: Where a bag of American candy, a runaway Austrian horse, and 2,340 Sovs in property damage somehow become the most emotionally resonant moment in the entire game.**
