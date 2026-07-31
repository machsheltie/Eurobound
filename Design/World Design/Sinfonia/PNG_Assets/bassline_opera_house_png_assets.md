# The Bassline Opera House - Complete PNG Asset Requirements

*Artist Reference Document for Sinfonia's Crown Jewel*

**Location ID**: `sinfonia_bassline_opera_house_01`  
**Priority**: HIGH (Multi-Zone Venue, Story Hub, Boss Arena, Fiaker Fiasco Phase 3)  
**Total Sheets Required**: 12  
**Mobile Optimization**: Target 60 FPS on iPhone 8+

---

## Art Direction Summary

### Visual Identity
The Bassline Opera House embodies **faded grandeur meeting modern decadence**—a 400-year-old baroque masterpiece that transforms into an EDM venue at night. Think Vienna State Opera crossed with a Berlin techno club. The building should feel *simultaneously prestigious and slightly seedy*.

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Opera House Gold | #CFB53B | Trim, chandeliers, gilding |
| Baroque Cream | #FFF8DC | Walls, marble accents |
| Velvet Red | #8B0000 | Curtains, carpets, seating |
| Marble White | #FFFAFA | Floors, columns |
| Backstage Black | #1C1C1C | Wings, work areas |
| Bassline Neon | #FF00FF / #00FFFF | Night transformation |

---

## SHEET 1: Lobby Tileset
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

## SHEET 2: Backstage Tileset
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

## SHEET 3: Starry Night Backdrop
**Filename**: `bassline_opera_backdrop_starry.png`  
**Dimensions**: 512 × 256 pixels

### Three States Required
1. **Pristine**: Deep blue/black, hand-painted stars, moon, clouds
2. **Cape Catching**: Gustav's cape snagged on rigging rope
3. **Torn**: Dramatic diagonal tear, canvas edges visible, stars misaligned

*Art Note*: The tear is a KEY DESTRUCTION moment—8 months of work destroyed. Make it dramatic but comedic.

---

## SHEET 4: Regisseur Heinrich Hoffmann
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

## SHEET 5: Stagehead Otto
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

## SHEET 6: Prima Donna Adelheid
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

## SHEET 7: Papageno (Franz)
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

## SHEET 8: Lobby Staff (Shared Sheet)
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

## SHEET 9: Maestro Vice von Strauss (Boss)
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

## SHEET 10: Destructible Props
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

## SHEET 11: Effects & Particles
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

## SHEET 12: UI Elements
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

## Lighting Requirements

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

## Social Media Viral Moments

### Key Screenshot Opportunities
1. **Gustav on stage** during "Der Hölle Rache"—horse interrupting opera
2. **Damage counter hitting €2,000**—with destruction visible
3. **Director's breakdown**—sitting on floor, thousand-yard stare
4. **Papageno befriending Gustav**—bird-man and horse bonding
5. **Otto sipping coffee**—completely unfazed during chaos

### Quotable Visual Moments
- Director: "I studied at the Conservatory..." (breakdown pose)
- Otto: "*sips coffee*" (deadpan during destruction)
- Prima Donna: "I sang at La Scala!" (outrage pose)
- Papageno: "Follow the bird-man!" (guiding pose)

---

## Technical Specifications

### File Format Requirements
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **Resolution**: 72 DPI (screen optimized)
- **Compression**: Lossless
- **Naming Convention**: `snake_case_descriptive.png`

### Mobile Optimization Targets
- **Texture Atlases**: Maximum 5 at 1024px
- **Draw Calls**: Under 50 for full location
- **Memory**: Under 50MB for all zones loaded
- **Particles**: Maximum 80 simultaneous
- **Target FPS**: 60 on iPhone 8+

### Animation Guidelines
- **Idle Loops**: 2-4 frames, 1-2 FPS
- **Action Animations**: 3-6 frames, 4-8 FPS
- **Destruction Sequences**: 3-4 frames, 6-8 FPS
- **Boss Attacks**: 4-8 frames, 4-6 FPS

---

## Cross-Reference: Related Assets

### From Opera House Plaza
- Gustav sprite (now with café feathers on cape)
- Hans-Jürgen sprite (may appear at resolution)
- Damage counter UI (shared system)

### To Stadtpark
- Gustav sprite continues (even more disheveled)
- Papageno sprite (if ally path chosen)
- Director may pursue (fury state)

---

**END OF ASSET REQUIREMENTS**

*The Bassline Opera House: Where 400 years of cultural excellence meets one horse in a cape, one method-acting bird-man, and €2,000 in Magic Flute production costs.*
