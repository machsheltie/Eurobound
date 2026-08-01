# The Bassline Opera House - Complete PNG Asset Requirements

*Artist Reference Document for Sinfonia's Crown Jewel*

## 📋 Overview
The Bassline Opera House is a 400-year-old baroque masterpiece that transforms into an EDM venue at night — Sinfonia's crown jewel, where four centuries of cultural excellence meet one horse in a cape, one method-acting bird-man, and €2,000 in Magic Flute production costs. This document specifies every sprite sheet the location needs across its five zones: grand lobby, auditorium, backstage, dressing rooms, and orchestra pit boss arena.

**Location ID:** `sinfonia_bassline_opera_house_01`
**Theme:** Cultural institution pretension — opera snobbery and artistic exploitation, with a dual identity (traditional opera by day, underground Bassline EDM by night)
**Zone:** Imperial Square District
**Hours:** Lobby 10:00–23:00; rehearsals 10:00–17:00; performances 19:00–22:00; Bassline 23:00–04:00
**Primary Function:** Multi-zone venue / story hub / boss arena — Fiaker Fiasco phase 3 (backstage chaos), Maestro Vice von Strauss city-boss fight, Waltz of the Bros rhythm battle, gift shop and box office economy

**Priority**: HIGH (Multi-Zone Venue, Story Hub, Boss Arena, Fiaker Fiasco Phase 3)  
**Total Sheets Required**: 12  
**Mobile Optimization**: Target 60 FPS on iPhone 8+

---

## 🎨 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Opera House Gold | #CFB53B | Trim, chandeliers, gilding |
| Baroque Cream | #FFF8DC | Walls, marble accents |
| Velvet Red | #8B0000 | Curtains, carpets, seating |
| Marble White | #FFFAFA | Floors, columns |
| Gilded Bronze | #CD7F32 | Statues, fixtures, aged metalwork |
| Backstage Black | #1C1C1C | Wings, work areas |
| Bassline Neon | #FF00FF / #00FFFF | Night transformation |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/bassline_opera_house/
├── environment/
│   ├── bassline_opera_lobby_tileset.png
│   ├── bassline_opera_backstage_tileset.png
│   └── bassline_opera_backdrop_starry.png
├── npcs/
│   ├── npc_regisseur_hoffmann.png
│   ├── npc_stagehead_otto.png
│   ├── npc_prima_donna_adelheid.png
│   ├── npc_papageno_franz.png
│   ├── npc_lobby_staff_sheet.png
│   └── boss_maestro_von_strauss.png
├── objects/
│   └── destructible_props_sheet.png
├── effects/
│   └── opera_house_effects.png
└── ui/
    └── opera_house_ui.png
```

---

## 🏛️ Sprite Sheet 1: Lobby Tileset
**Filename**: `bassline_opera_lobby_tileset.png`  
**Dimensions**: 1024 × 768 pixels  
**Tile Size**: 32 × 32 pixels

### Contents
- **Floor Tiles**: Marble white/grey, music note mosaic, red carpet
- **Wall Tiles**: Baroque cream, gold trim, columns (base/shaft/capital)
- **Furniture**: Velvet bench, box office window, coat check, gift shop
- **Grand Staircase**: Three-section ascending stairs with red carpet
- **Decorative**: Chandeliers (small/large), Mozart/Beethoven portraits, busts
- **Doors**: Main entrance, auditorium entrance, hidden panel

*Art Note*: Staircase should feel imposing. Worn carpet shows centuries of use.

---

## 🎭 Sprite Sheet 2: Backstage Tileset
**Filename**: `bassline_opera_backstage_tileset.png`  
**Dimensions**: 1024 × 512 pixels

### Contents
- **Floor Tiles**: Stage wood (tape marks), concrete, catwalk metal
- **Wall Tiles**: Flat black, painted brick, pipe grid, fire doors
- **Prop Racks**: Intact and damaged versions (64×96 each)
- **Costume Racks**: Intact and destroyed versions (64×96 each)
- **Set Pieces**: Paper trees, mechanical snake, temple columns
- **Work Areas**: Makeup tables, sewing stations, coffee area
- **Rigging**: Sandbags, fly rail controls, catwalk sections

---

## 🌌 Sprite Sheet 3: Starry Night Backdrop
**Filename**: `bassline_opera_backdrop_starry.png`  
**Dimensions**: 512 × 256 pixels

### Three States Required
1. **Pristine**: Deep blue/black, hand-painted stars, moon, clouds
2. **Cape Catching**: Gustav's cape snagged on rigging rope
3. **Torn**: Dramatic diagonal tear, canvas edges visible, stars misaligned

*Art Note*: The tear is a KEY DESTRUCTION moment—8 months of work destroyed. Make it dramatic but comedic.

---

## 📢 Sprite Sheet 4: Regisseur Heinrich Hoffmann
**Filename**: `npc_regisseur_hoffmann.png`  
**Dimensions**: 384 × 384 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Age**: 50s, prematurely grey
- **Build**: Thin, nervous energy
- **Clothing**: Black turtleneck, director's notebook always in hand
- **Accessories**: Reading glasses on chain

### Animations (6 rows)
1. **Idle Directing**: 6 frames, arms conducting, notebook waving
2. **Horror**: 4 frames, freeze → glasses slip → mouth drops → hands to face
3. **Breakdown**: 2 frames, sitting on floor, head in hands
4. **Fury**: 4 frames, red face, pointing, German screaming posture
5. **Defeat**: 2 frames, cross-legged, thousand-yard stare
6. **Walk**: 4 frames, purposeful stride

---

## ☕ Sprite Sheet 5: Stagehead Otto
**Filename**: `npc_stagehead_otto.png`  
**Dimensions**: 288 × 256 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Age**: 60s, weathered face
- **Build**: Stocky, practical
- **Clothing**: All black stage crew, tool belt, headset around neck
- **Key Prop**: Coffee cup—ALWAYS VISIBLE, never put down
- **Expression**: Permanently unimpressed, seen-everything energy

### Animations (4 rows)
1. **Idle with Coffee**: 2 frames, slight steam from cup
2. **Coffee Sip**: 3 frames, slow deliberate sip mid-chaos
3. **Point Direction**: 2 frames, gestures with coffee hand
4. **Walk**: 4 frames, unhurried even during disaster

*Art Note*: Otto NEVER reacts to chaos. His sprite remains calm while destruction happens around him. The coffee cup is his eternal companion.

---

## 👑 Sprite Sheet 6: Prima Donna Adelheid
**Filename**: `npc_prima_donna_adelheid.png`  
**Dimensions**: 384 × 320 pixels  
**Sprite Size**: 48 × 80 pixels (taller for dramatic costume)

### Character Design
- **Age**: 40s, "ageless" theatrical beauty
- **Build**: Imposing presence, fills the frame
- **Costume**: Queen of the Night gown—black with silver stars
- **Face**: Dramatic stage makeup even during rehearsal
- **Expression**: Perpetual theatrical intensity

### Animations (4 rows × 2 costume variants = 8 rows total)
**Costume Intact (Rows 0-3)**:
1. **Singing**: 4 frames, arms raised, dramatic pose
2. **Interrupted**: 3 frames, shock mid-note, hands to chest
3. **Outrage**: 4 frames, pointing, dramatic gestures
4. **Dismissive**: 2 frames, hand wave, turn away

**Costume Torn (Rows 4-7)**: Same animations but gown shows damage

---

## 🪶 Sprite Sheet 7: Papageno (Franz)
**Filename**: `npc_papageno_franz.png`  
**Dimensions**: 384 × 320 pixels  
**Sprite Size**: 48 × 80 pixels

### Character Design
- **Costume**: Full Papageno bird suit—green feathers, cape, beak mask
- **Build**: Hidden by costume, cheerful movement
- **Key Props**: Panpipes, feather cape, bird seeds in pouch
- **Face**: Visible through costume eyeholes, cheerful expression

### Animations (4 rows)
1. **Performing**: 6 frames, dancing, playing pipes
2. **Excited Hop**: 4 frames, jumping with joy, feathers ruffling
3. **Guiding Beckon**: 4 frames, waving "follow me" gesture
4. **Offering Seeds**: 4 frames, holding out seeds to Gustav

*Art Note*: Papageno NEVER breaks character. His animations should feel theatrical even in chaos. Feathers should have subtle animation/bounce.

---

## 👥 Sprite Sheet 8: Lobby Staff (Shared Sheet)
**Filename**: `npc_lobby_staff_sheet.png`  
**Dimensions**: 384 × 384 pixels  
**Sprite Size**: 48 × 64 pixels

### Box Office Attendant (Rows 0-1)
- **Look**: 50s, prim, reading glasses, behind brass cage window
- **Animations**: Idle (2f), Judging tourists (2f), Refusing sale (3f)

### Opera Usher Gerhardt (Rows 2-3)
- **Look**: 60s, thin, red usher jacket, white gloves, permanent disapproval
- **Animations**: Standing guard (2f), Blocking entry (2f), Disapproving stare (3f)

### Coat Check Helga (Rows 4-5)
- **Look**: 40s, friendly but observant, simple black dress
- **Animations**: Idle (2f), Gossiping/leaning in (3f)

---

## 🎼 Sprite Sheet 9: Maestro Vice von Strauss (Boss)
**Filename**: `boss_maestro_von_strauss.png`  
**Dimensions**: 512 × 640 pixels  
**Sprite Size**: 64 × 80 pixels (larger boss sprite)

### Character Design
- **Age**: 50s, silver-fox handsome, smug
- **Build**: Commanding, theatrical presence
- **Costume Phase 1**: Full conductor's tails, pristine white shirt
- **Costume Phase 2**: Jacket removed, DJ headphones appearing
- **Costume Phase 3**: Shirt open, sweat glistening, chaos mode

### Phase 1 - Classical Corruption (Rows 0-2)
1. **Conducting**: 8 frames, elegant baton movements
2. **Crescendo Attack**: 6 frames, dramatic upward thrust
3. **Waltz Debuff**: 6 frames, sweeping hypnotic motion

### Phase 2 - The Drop (Rows 3-5)
1. **DJing**: 6 frames, working controller, headphones on
2. **Bass Attack**: 4 frames, hands raised, beat drop pose
3. **Transformation**: 4 frames, putting on headphones, smirking

### Phase 3 - Encore (Rows 6-8)
1. **Chaotic Conducting**: 8 frames, wild baton + DJ moves
2. **Encore Summon**: 6 frames, calling reinforcements dramatically
3. **Defeat**: 4 frames, staggering, falling, disbelief

*Art Note*: Each phase should feel like a tonal shift. Phase 1 is classical elegance, Phase 2 is modern swagger, Phase 3 is desperate fusion.

---

## 💥 Sprite Sheet 10: Destructible Props
**Filename**: `destructible_props_sheet.png`  
**Dimensions**: 512 × 384 pixels

### Props with Destruction States

**Papageno Bird Head** (64×64)
- Intact: Colorful, feathered, expressive
- Falling: Mid-air, feathers scattering
- Destroyed: Crushed, feathers everywhere

**Magic Flute Prop** (48×24)
- Intact: Gold-painted wood, ornate
- Bending: Stress visible
- Snapped: Two pieces, gold paint flaking

**Queen of the Night Gown** (48×80)
- Pristine: Black with silver stars, flowing
- Caught: Tangled on Gustav's feathers
- Torn: Ripped seam, stars askew

**Paper Tree** (64×128)
- Standing: Whimsical papier-mâché
- Tipping: 45-degree angle
- Fallen: Crushed, crumpled paper visible

**Mechanical Snake** (96×64)
- Operational: Coiled, motors visible, painted scales
- Kicked: Mid-destruction impact
- Destroyed: Bent segments, sparking wires, exposed motors

---

## ✨ Sprite Sheet 11: Effects & Particles
**Filename**: `opera_house_effects.png`  
**Dimensions**: 256 × 256 pixels

### Effect Animations
- **Feathers Scattering**: 4 frames, various colors floating
- **Gold Paint Flakes**: 4 frames, glittering particles
- **Fabric Tear**: 3 frames, ripping motion
- **Canvas Rip**: 4 frames, backdrop tearing effect
- **Damage Popup**: 3 frames, €euro amount rising
- **Chandelier Sparkle**: 4 frames, crystal glints
- **Dust Cloud**: 4 frames, prop destruction aftermath
- **Stage Light Beam**: 2 frames, spotlight effect

---

## 🖥️ Sprite Sheet 12: UI Elements
**Filename**: `opera_house_ui.png`  
**Dimensions**: 256 × 192 pixels

### UI Components
- **Damage Counter Frame**: Ornate gold frame (128×48)
- **Euro Symbol**: Stylized € (32×32)
- **Debt Indicator**: "OUTSTANDING" bar (100×32)
- **Choice Panel**: Dialogue choice frame, baroque style (200×80)
- **Papageno Icon**: For ally indicator (48×48)
- **Status Icons**: Cultured Presence, Artistic Guilt, etc. (24×24 each)

---

## 🎬 Animation Specifications

### General Animation Guidelines (all sheets)
- **Idle Loops**: 2-4 frames, 1-2 FPS
- **Action Animations**: 3-6 frames, 4-8 FPS
- **Destruction Sequences**: 3-4 frames, 6-8 FPS
- **Boss Attacks**: 4-8 frames, 4-6 FPS

### Hoffmann's Descent (Idle → Horror → Breakdown → Defeat):
- **Duration:** Horror ~0.7s single play; Breakdown and Defeat hold at 1 FPS
- **Frames:** 4 / 2 / 2 per state
- **Pattern:** Quest-state driven progression, no automatic loop back
- **Trigger:** Gustav destruction events during Fiaker Fiasco phase 3
- **Purpose:** A director's career-long faith in art dying in real time; the quest's emotional comedy spine
- **Audio Sync:** German exclamation on Horror frame 1; silence on Defeat
- **Mobile Optimization:** None needed (single NPC)

### Otto's Coffee Sip:
- **Duration:** ~1 second, single play on random interval
- **Frames:** 3
- **Pattern:** Raise → sip → lower, return to idle
- **Trigger:** Timer (random 8–15s), unaffected by chaos state
- **Purpose:** The deadpan constant — destruction rages, Otto sips
- **Audio Sync:** Quiet slurp, deliberately audible in chaos lulls
- **Mobile Optimization:** None needed

### Starry Night Backdrop Tear:
- **Duration:** ~0.6 seconds (canvas rip effect, 4 frames at 6-8 FPS)
- **Frames:** 3 backdrop states + 4-frame rip effect overlay
- **Pattern:** Pristine → cape catching → torn (state advance, no loop)
- **Trigger:** Gustav's cape snag scripted event
- **Purpose:** The €400, eight-months-of-work destruction centerpiece
- **Audio Sync:** Long fabric-rip sound synced to the diagonal tear; damage popup ching on completion
- **Mobile Optimization:** None needed (scripted one-shot)

### Maestro Boss Phase Cycle:
- **Duration:** Attacks 0.7–2.0s each per guidelines (4-8 frames at 4-6 FPS)
- **Frames:** 8 (conducting/chaotic conducting), 6 (crescendo, waltz, DJ, summon), 4 (bass attack, transformation, defeat)
- **Pattern:** Phase-locked rows; transformation plays once between phases
- **Trigger:** Boss AI state machine, tempo-synced to battle music
- **Purpose:** Classical elegance → modern swagger → desperate fusion, each phase a tonal shift
- **Audio Sync:** All attacks beat-matched; Phase 2 bass attack lands exactly on the drop
- **Mobile Optimization:** Phase 3 strobe replaced by slow color fade on low-end devices

### Papageno Performing / Feather Bounce:
- **Duration:** ~1 second loop (6 frames at 4-8 FPS)
- **Frames:** 6
- **Pattern:** Dance loop with subtle feather secondary motion
- **Trigger:** Constant while on screen; Guiding Beckon during ally path
- **Purpose:** The one performer who never breaks character, even mid-catastrophe
- **Audio Sync:** Panpipe phrase on performing loop start
- **Mobile Optimization:** Feather secondary motion disabled on low-end

### Destruction Effects (Feathers / Gold Flakes / Dust):
- **Duration:** 0.5–0.7 seconds each (4 frames at 6-8 FPS)
- **Frames:** 4 each
- **Pattern:** Single play, spawned per destruction event
- **Trigger:** Prop destruction events
- **Purpose:** Sells impact and cost — every puff of dust is money
- **Audio Sync:** Crash + register ching with rising € damage popup
- **Mobile Optimization:** Cap concurrent effect instances at 4 on low-end

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Destructible prop outlines | set at sheet layout | per prop | High-contrast silhouettes marking what Gustav can (will) destroy |
| Papageno ally highlight | set at sheet layout | 48×80 | Bold outline for the follow-the-bird-man guidance path |
| Boss telegraph outlines | set at sheet layout | 64×80 | Enhanced-visibility windup silhouettes for all Maestro attacks |
| Hidden panel door marker | set at sheet layout | 32×64 | Discoverable-contrast variant of the lobby's hidden panel |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Phase 3 strobe replacement | set at sheet layout | full arena | Slow two-color fade replacing tempo-synced strobe |
| Static chandelier sparkle | set at sheet layout | 64×64 | Non-glinting chandelier variant |
| Reduced Bassline color cycle | set at sheet layout | full arena | Single-hue wash replacing #FF00FF → #00FFFF → #FFFF00 cycling |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Beat-drop indicator | set at sheet layout | 32×32 | Pulsing bass glyph telegraphing Phase 2 drops for rhythm play |
| Fabric-rip streak | set at sheet layout | 48×16 | Directional tear glyph accompanying the backdrop rip audio |
| German exclamation burst | set at sheet layout | 32×24 | Speech-shock glyph over Hoffmann and Adelheid outbursts |
| Crash/ching burst | set at sheet layout | 32×32 | Impact star + € glyph for every destruction sound |

### Colorblind Considerations:
- Boss phase changes are signaled by costume state (tails / headphones / open shirt), never lighting color alone
- Status icons (Cultured Presence, Artistic Guilt) use distinct silhouettes, not just tint
- Touch zones minimum 44px for box office, gift shop, and dialogue choice panels

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); lobby tileset gilding and boss sheet need ASTC 4x4
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for the starry backdrop (its hand-painted stars are plot-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| opera_lobby | lobby tileset, lobby staff, UI | 1024x1024 |
| opera_backstage | backstage tileset, backdrop, destructible props | 1024x1024 |
| opera_principals | Hoffmann, Otto, Adelheid, Papageno | 1024x1024 |
| opera_boss | Maestro von Strauss | 1024x1024 |
| opera_effects | effects & particles | 512x512 |

*(Maximum 5 atlases at 1024px per original spec; max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full particle set (80), chandelier sparkle, strobe/color cycling, feather secondary motion |
| Medium | 40 particles, no chandelier sparkle, simplified color cycling |
| Low | Static lighting, minimal particles (destruction one-shots only), no shaders |

### Performance Targets:
- **Target FPS:** 60 on iPhone 8+
- **Max Draw Calls:** Under 50 for full location
- **Memory Footprint:** Under 50 MB for all zones loaded
- **Particle Limit:** 80 simultaneous

### Performance Notes:
- Zone loading enabled: lobby, auditorium, backstage, dressing rooms, and orchestra pit load independently
- Bassline transformation swaps lighting presets, not geometry — one texture state change at 23:00
- Boss arena caps concurrent add-summon sprites during Encore phase

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap per zone; AnimatedSprite2D for all NPC/boss states; CPUParticles2D (not GPU) for feathers, dust, gold flakes
- Location state machine: normal / rehearsal / performance / bassline / fiaker_fiasco_chaos / post_quest drives sprite and lighting swaps
- Boss fight uses a tempo-sync controller: attack animation triggers quantized to battle-music BPM
- CanvasLayer for the shared Fiaker Fiasco damage-counter UI

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Backdrop tear | Long fabric rip + damage ching | Synced to diagonal tear frames |
| Prop destruction | Crash + cash-register ching | On impact frame, € popup rises |
| Maestro Phase 2 bass attack | The drop | Beat-matched, hands-raised frame on downbeat |
| Phase 3 strobe | Battle music tempo | Strobe flashes quantized to BPM |
| Hoffmann horror | German exclamation | On horror frame 1 |
| Papageno performing | Panpipe phrase | On loop start |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Fiaker Fiasco phase 3 | Backstage tileset damage states, destructible props, backdrop states, Hoffmann/Otto/Adelheid/Papageno sets | Gustav auto-enters via alley; €2,000 backstage damage tracked to `fiaker_fiasco_damage_euro` |
| Maestro boss fight (main quest) | Boss sheet all phases, arena lighting states | Orchestra pit, Bassline configuration, 23:00–04:00 |
| Waltz of the Bros | Auditorium configuration, patron NPCs | Rival rhythm-battle encounter |
| Prima donna negotiation | Adelheid outrage/dismissive sets, torn costume variant | €500 demand, negotiable to €200 at Charm 4 |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Opera House Plaza | Adjacent main entrance; Gustav sprite arrives with café feathers on cape; Hans-Jürgen may appear at resolution; shared damage-counter UI | Main-door transition |
| Café Sachertorte | Incoming quest path via alley | Alley auto-entry during Fiaker Fiasco |
| Stadtpark (Gustav's Refuge) | Outgoing quest path; Gustav continues (even more disheveled); Papageno sprite if ally path; Hoffmann may pursue in fury state | Side-door path to the park |
| The Black-Tie Backroom | Hidden entrance from lobby/backstage (hidden panel, prop corridor) | Concealed-door transition |
| Hidden Baroness Ballroom | Unlocked via boss-reward vault keys | Late-game key transition |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Faded grandeur meeting modern decadence" — a 400-year-old baroque masterpiece that transforms into an EDM venue at night. Think Vienna State Opera crossed with a Berlin techno club. The building should feel *simultaneously prestigious and slightly seedy*.
- **Color Mood:** Gold, cream, and velvet red by day; magenta/cyan neon bleeding through the gilding by night
- **Lighting:** Warm cream daytime, golden evening glow, indigo Bassline nights; harsh work lights backstage (see Lighting Requirements below)
- **Texture:** Worn carpet showing centuries of use, gold leaf slightly flaking, stage wood scarred with tape marks — prestige under maintenance

### Environmental Storytelling:
- The hidden lobby panel and prop-corridor door: the institution's respectable face conceals the gambling den behind it
- Backstage chaos (coffee area, sewing stations, damaged racks) shows the unglamorous labor propping up the gilded front
- The torn starry backdrop remains visibly repaired post-quest — the €2,000 never quite disappears

### Character Integration Notes:
- Otto's calm is a rendering rule: his sprite never gains reaction frames, whatever happens in the scene
- Papageno's feathers get subtle secondary animation; he reads as theatrical even at idle
- Boss phases are costume-first: readable at silhouette level before any lighting change

---

## 💡 Lighting Requirements

### Lobby Lighting
- **Daytime**: Warm cream (#FFFACD), 80% intensity
- **Evening**: Golden glow (#FFD700), 90% intensity
- **Bassline Night**: Purple (#4B0082), 60% intensity
- **Chandelier Points**: 5 point lights with crystal sparkle

### Backstage Lighting
- **Work Lights**: Harsh white (#F0F0F0), 70%
- **Stage Spill**: Orange (#FFA500), 50% from wings
- **Exit Signs**: Red (#FF0000), 80% glow

### Boss Arena Lighting
- **Phase 1**: Classical warm gold
- **Phase 2**: EDM color cycling (#FF00FF → #00FFFF → #FFFF00)
- **Phase 3**: Strobe effect, tempo-synced

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Gustav on stage** during "Der Hölle Rache"—horse interrupting opera
2. **Damage counter hitting €2,000**—with destruction visible
3. **Director's breakdown**—sitting on floor, thousand-yard stare
4. **Papageno befriending Gustav**—bird-man and horse bonding
5. **Otto sipping coffee**—completely unfazed during chaos

### Quote Potential:
- "I studied at the Conservatory..." - Regisseur Hoffmann (breakdown pose)
- "*sips coffee*" - Otto (deadpan during destruction)
- "I sang at La Scala!" - Prima Donna Adelheid (outrage pose)
- "Follow the bird-man!" - Papageno (guiding pose)

---

## 📋 Required PNG Files (12 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | bassline_opera_lobby_tileset.png | 1024x768 |
| 2 | bassline_opera_backstage_tileset.png | 1024x512 |
| 3 | bassline_opera_backdrop_starry.png | 512x256 |
| 4 | npc_regisseur_hoffmann.png | 384x384 |
| 5 | npc_stagehead_otto.png | 288x256 |
| 6 | npc_prima_donna_adelheid.png | 384x320 |
| 7 | npc_papageno_franz.png | 384x320 |
| 8 | npc_lobby_staff_sheet.png | 384x384 |
| 9 | boss_maestro_von_strauss.png | 512x640 |
| 10 | destructible_props_sheet.png | 512x384 |
| 11 | opera_house_effects.png | 256x256 |
| 12 | opera_house_ui.png | 256x192 |

**Total Estimated Memory:** ~10.5 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `bassline_opera_lobby_tileset.png` (1024x768)
- [ ] `bassline_opera_backstage_tileset.png` (1024x512)
- [ ] `bassline_opera_backdrop_starry.png` (512x256)
- [ ] `npc_regisseur_hoffmann.png` (384x384)
- [ ] `npc_stagehead_otto.png` (288x256)
- [ ] `npc_prima_donna_adelheid.png` (384x320)
- [ ] `npc_papageno_franz.png` (384x320)
- [ ] `npc_lobby_staff_sheet.png` (384x384)
- [ ] `boss_maestro_von_strauss.png` (512x640)
- [ ] `destructible_props_sheet.png` (512x384)
- [ ] `opera_house_effects.png` (256x256)
- [ ] `opera_house_ui.png` (256x192)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase (`snake_case_descriptive.png`) |
| Layer Organization | Preserve layers in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet + boss tempo-sync cue sheet

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Backdrop tear reads as dramatic-but-comedic at gameplay zoom
- [ ] Otto's sprite shows zero reaction frames across all states
- [ ] Boss phases readable at silhouette level (costume-first)
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (cultural pretension vs. chaos) clear throughout all assets
- [ ] Hidden panel / prop corridor have discoverable visual cues
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Vienna State Opera evoked as reference, never named in-world |
| Cultural Specificity | ✅ | Opera-house hierarchy, Magic Flute production culture, EDM night economy |
| Satirical Targets Appropriate | ✅ | Opera snobbery, artistic self-importance, institutional pretension — punches up |
| Seedy Underbelly Present | ✅ | Bassline underground nights, hidden gambling-den entrance, scalped prestige |
| Gameplay Value Established | ✅ | Story hub, boss arena, rhythm battle, quest phase 3, shop/box office |
| Technical Feasibility | ✅ | 12 sheets, 5-atlas plan, zone loading, LOD tiers documented |
| Mobile Performance Budget | ✅ | 60 FPS, <50 draw calls, <50 MB, 80 particles |
| Accessibility Features | ✅ | Visual audio cues, strobe replacement, telegraph outlines |
| No Crypto Elements | ✅ | None present |
| Social Media Integration | ✅ | Five screenshot moments and quotable poses identified |

**The Bassline Opera House: Where 400 years of cultural excellence meets one horse in a cape, one method-acting bird-man, and €2,000 in Magic Flute production costs.**
