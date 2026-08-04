# Baroness' Ballroom - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Baroness' Ballroom - Sinfonia's secret masquerade venue where everyone wears a mask, nobody uses their real name, and the only thing more elaborate than the lies is the chandelier. It is the city's social combat arena: reputation is HP, the waltz is a weapon, and three American bros were identified within 30 seconds of arrival.

**Location ID:** `sinfonia_hidden_baroness_ballroom_01`
**Theme:** High-society anonymity theater — masks that layer more pretense instead of removing it
**Zone:** Hidden location (accessed via Opera House, Cemetery, and Café routes)
**Hours:** Masquerade nights only (Friday & Saturday, 10 PM - 4 AM)
**Primary Function:** Social combat zone / dance duel arena / rumor trading hub — Masquerade Identity system, Whisper Gallery trades, Baroness audience, Lady Geheimnis couchsurf

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Midnight Purple | #4B0082 | Primary walls, drapery, Baroness accents |
| Masquerade Gold | #CFB53B | Gilding, masks, chandelier, trim |
| Ballroom Cream | #FFF8DC | Marble, background surfaces |
| Mystery Black | #1C1C1C | Der Schatten, shadows, formal wear |
| Candle Warm | #FFD9A0 | Candlelight glow, sconce halos |
| Scandal Crimson | #8B0000 | Carpet runner, humiliation UI, crowd reaction accents |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/baroness_ballroom/
├── environment/
│   ├── baroness_ballroom_tileset.png
│   └── baroness_ballroom_landmarks.png
├── npcs/
│   ├── baroness_of_masks.png
│   ├── baroness_ballroom_court_npcs.png
│   ├── baroness_ballroom_crowd.png
│   └── baroness_ballroom_bros.png
├── effects/
│   └── baroness_ballroom_effects.png
└── ui/
    └── baroness_ballroom_ui.png
```

---

## 🏛️ Sprite Sheet 1: Ballroom Tileset
**File:** `baroness_ballroom_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #FFF8DC (Ballroom Cream), #4B0082 (Midnight Purple), #CFB53B (Masquerade Gold), #1C1C1C (Mystery Black)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Checkered Marble A | (0, 0) | 32x32 | Cream square of the dance-floor checker |
| Checkered Marble B | (32, 0) | 32x32 | Black square of the dance-floor checker |
| Polished Marble Plain | (64, 0) | 32x32 | Perimeter flooring, soft reflections |
| Crimson Carpet | (96, 0) | 32x32 | Staircase and dais runner |
| Carpet Gold Border | (128, 0) | 32x32 | Trim edge for runner |
| Salon Parquet | (160, 0) | 32x32 | Private salon herringbone wood |
| Gallery Stone | (192, 0) | 32x32 | Whisper Gallery curved corridor floor |
| Dais Platform Tile | (224, 0) | 32x32 | Elevated purple-veined marble |

### Wall Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ballroom Wall Cream | (0, 32) | 32x64 | Aged cream plaster with gold pinstripe |
| Gilded Panel Wall | (32, 32) | 32x64 | Ornate boiserie panel |
| Gallery Curved Wall | (64, 32) | 32x64 | Acoustic curve segment (whisper-carrying) |
| Salon Wall Purple | (96, 32) | 32x64 | Midnight purple damask |
| Mirror Wall Panel | (128, 32) | 32x64 | Strategically angled — never shows full faces |
| Velvet Drape Panel | (160, 32) | 32x64 | Heavy purple drapery segment |
| Wainscot Cap | (192, 32) | 32x32 | Gilded molding strip |

### Grand Staircase:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stair Section | (0, 96) | 64x64 | Marble steps, descending sweep |
| Stair Balustrade | (64, 96) | 32x64 | Gold-leaf railing |
| Carpet Runner Stairs | (96, 96) | 32x64 | Crimson runner overlay |
| Landing Marble | (128, 96) | 64x32 | Announcement platform surface |

### Doors & Entrances:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ornate Double Door L | (0, 160) | 32x64 | Grand entrance, left leaf |
| Ornate Double Door R | (32, 160) | 32x64 | Grand entrance, right leaf |
| Opera Route Curtain | (64, 160) | 32x64 | Behind the Maestro's box — prestige entry |
| Cemetery Route Stone Door | (96, 160) | 32x64 | Underground passage from Mozart's Last Rave |
| Café Route Bookcase Door | (128, 160) | 32x64 | Secret door from Café Existenz back room |
| Salon Door | (160, 160) | 32x64 | Private salon access |
| Secret Exit Panel | (192, 160) | 32x64 | One of three exits, wall-flush |

### Platforms & Stations:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Herald Platform | (0, 224) | 96x64 | Announcement stage with lectern |
| Baroness Dais Base | (96, 224) | 128x64 | Elevated authority platform |
| Orchestra Platform | (224, 224) | 128x64 | Raised stage for the waltz orchestra |
| Mirror Station | (352, 224) | 48x64 | Mask-adjustment vanity (surveillance disguised as vanity) |
| Refreshment Table | (400, 224) | 64x48 | Eavesdropping-positioned service station |

### Windows & Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tall Window Night | (0, 288) | 32x80 | Dark glass, candle reflections |
| Velvet Drape Tied | (32, 288) | 32x80 | Gold-corded purple drape |
| Wall Sconce | (64, 288) | 16x32 | Candle sconce, warm halo |
| Masked Ancestor Portrait | (80, 288) | 48x64 | Every painted ancestor also wears a mask |
| Floor Candelabra | (128, 288) | 24x64 | Freestanding gold candelabra |
| Whisper Gallery Arch | (152, 288) | 64x80 | Curved acoustic archway |

### Columns & Macro Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marble Column | (0, 384) | 32x96 | Fluted, gilt capital |
| Column Pair Garlanded | (32, 384) | 64x96 | Masquerade-night garland dressing |
| Checkered Floor Macro | (96, 384) | 128x128 | Pre-composed 4x4 dance floor block |

### Technical Notes:
- Mirror panels use a darkened reflection shader region — reflections must never resolve a full face
- Checker macro tile is the dance-duel arena base; keep contrast readable under spotlight overlay
- All three entrance doors share one frame size for interchangeable route logic

---

## 👑 Sprite Sheet 2: Landmarks & Major Props
**File:** `baroness_ballroom_landmarks.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #CFB53B (Masquerade Gold), #FFF8DC (Cream), #4B0082 (Midnight Purple)

### The Chandelier (more elaborate than the lies):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chandelier Static | (0, 0) | 128x96 | Massive crystal centerpiece, candle-lit |
| Chandelier Sway L | (128, 0) | 128x96 | Slight tilt left, crystal shimmer |
| Chandelier Sway R | (256, 0) | 128x96 | Slight tilt right |
| Announce Platform Dressed | (384, 0) | 96x96 | Herald's stage with banners |

### Authority & Performance:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Baroness Dais Dressed | (0, 96) | 160x112 | Draped dais with throne silhouette |
| Throne Chair | (160, 96) | 48x64 | The Baroness' seat, standalone |
| Orchestra Ensemble | (208, 96) | 160x112 | Musicians with instruments (waltzes hiding modern beats) |
| Food Service Domed | (368, 96) | 64x48 | Covered dishes — even the food is masked |
| Food Dome Lifted | (432, 96) | 64x48 | Dramatic reveal state |

### Salons & Stations:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mirror Station Ornate | (0, 208) | 64x96 | Full vanity with candle flanks |
| Refreshment Fountain | (64, 208) | 96x96 | Champagne fountain (lies about alcohol content) |
| Salon Fireplace | (160, 208) | 96x80 | Private salon hearth |
| Baroness Salon Divan | (256, 208) | 96x64 | Inner Circle seating |
| Whisper Gallery Bench | (352, 208) | 64x48 | Rumor-trading seat |

### Social Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Name Card Stand | (0, 304) | 32x48 | Masquerade identities only — no real names |
| Seating Chart | (32, 304) | 48x64 | Actually a social hierarchy diagram |
| Spotlight Floor Decal | (80, 304) | 96x96 | Dance-duel spotlight ring |
| Dance Floor Medallion | (176, 304) | 128x128 | Center inlay, duel start point |
| Buffet Cover Row | (304, 304) | 96x32 | Line of decorative covers |

### Entrance Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Velvet Rope | (0, 432) | 64x32 | Dais approach barrier — crossing uninvited = social death |
| Herald Trumpet Banner | (64, 432) | 48x80 | Hanging announcement banner |

### Technical Notes:
- Chandelier sway is ambient (slow pendulum), not chaos-driven — it is the room's heartbeat
- Spotlight decal renders under dancers, medallion under spotlight; keep both z-ordered below character layer
- Refreshment fountain has a 2-frame pour loop handled by UV scroll, no extra frames needed

---

## 🎭 Sprite Sheet 3: The Baroness & Der Schatten
**File:** `baroness_of_masks.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #4B0082 (Midnight Purple), #CFB53B (Gold), #1C1C1C (Mystery Black)

### The Baroness of Masks (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Court Idle | (0, 0) | 64x96 | Elaborate gown, ageless stillness |
| Gesture of Welcome | (64, 0) | 64x96 | One raised hand — the room quiets |
| Amused | (128, 0) | 64x96 | Head tilt, "seventeen counts tonight" energy |
| Probing Question | (192, 0) | 64x96 | Leaning forward, innocent-seeming inquiry |
| Favor Grant | (256, 0) | 64x96 | Extending favor token |
| Displeasure | (320, 0) | 64x96 | Stillness that reads as danger |
| Mask Shift Frame 1 | (384, 0) | 64x96 | Mask color mid-transition (purple) |
| Mask Shift Frame 2 | (448, 0) | 64x96 | Mask color mid-transition (gold) |

### Baroness Special States (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mask Shift Frame 3 | (0, 96) | 64x96 | Mask color mid-transition (black) |
| One Truth Revealed | (64, 96) | 64x96 | Maximum favor — leaning close, hand beside mask |

### Der Schatten — The Baroness' Shadow (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle | (128, 96) | 48x96 | All-black formal wear, featureless mask |
| Dance Frame 1 | (176, 96) | 48x96 | Waltz step, mechanical grace |
| Dance Frame 2 | (224, 96) | 48x96 | Turn |
| Dance Frame 3 | (272, 96) | 48x96 | Extension |
| Dance Frame 4 | (320, 96) | 48x96 | Close |
| Bow | (368, 96) | 48x96 | Silent challenge issued |
| Challenge Point | (416, 96) | 48x96 | Gesture toward the floor — no words, only the dance |

### Duet & Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shifting Mask Close-Up | (0, 192) | 32x32 | Item-scale mask for dialogue portraits |
| Baroness Fan | (32, 192) | 24x32 | Folding fan prop |
| Favor Token | (56, 192) | 24x24 | Gold sigil, reward hand-off |
| Waltz Duet Frame 1 | (96, 192) | 96x96 | Schatten + partner, spotlight duet |
| Waltz Duet Frame 2 | (192, 192) | 96x96 | Duet turn |
| Waltz Duet Frame 3 | (288, 192) | 96x96 | Duet finale pose |

### Salon Audience Poses (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Baroness Seated | (0, 288) | 64x96 | Holding court in salon |
| Baroness Leaning | (64, 288) | 64x96 | Interested — a dangerous sign |
| Baroness Dismissal | (128, 288) | 64x96 | Audience over, gesture toward door |

### Character Notes:
- Witnesses disagree on her appearance: mask shift frames cycle continuously so no screenshot captures the same Baroness twice
- Der Schatten never has an idle fidget — perfect stillness between dance frames
- Baroness silhouette must remain readable at 64x96 against dark salon backgrounds (gold trim carries the read)

---

## 🎺 Sprite Sheet 4: Court NPCs & Dance Duelists
**File:** `baroness_ballroom_court_npcs.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Formal wear variety, #CFB53B (Gold), #1C1C1C (Black)

### The Herald — Herr Ankündiger (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Herald Idle | (0, 0) | 48x96 | Elaborate costume, perpetual judgment |
| Herald Announce | (48, 0) | 48x96 | Booming projection pose |
| Herald Warm (Bribed) | (96, 0) | 48x96 | Delivery adjusted by bribe level |
| Herald Disdain | (144, 0) | 48x96 | "...presenting... *sigh* ...The Count of Cool." |
| Herald Trumpet Raise | (192, 0) | 48x96 | Fanfare cue |

### Lady Geheimnis — The Former Baroness (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Faded Elegance Idle | (240, 0) | 48x96 | Mask permanently affixed, worn finery |
| Reminiscing | (288, 0) | 48x96 | "When she was the Baroness" |
| Warning Gesture | (336, 0) | 48x96 | "Some truths cost everything, dear." |
| Mask Touch | (384, 0) | 48x96 | Hand at the mask that never comes off |

### The Rumor Broker — Der Flüsterer (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shadow Idle | (0, 96) | 48x96 | Face always in shadow |
| Whisper Lean | (48, 96) | 48x96 | Trading position |
| Trade Offer | (96, 96) | 48x96 | Palm-up rumor card exchange |

### Dance Duelists (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Debutante Idle | (144, 96) | 48x96 | First challenge, forgiving posture |
| Debutante Dance A | (192, 96) | 48x96 | Waltz step |
| Debutante Dance B | (240, 96) | 48x96 | Waltz turn |
| The Veteran Idle | (288, 96) | 48x96 | Twenty years on this floor |
| Veteran Dance A | (336, 96) | 48x96 | Tighter form |
| Veteran Dance B | (384, 96) | 48x96 | Tempo-shift step |
| The Champion Idle | (0, 192) | 48x96 | "They call me 'The Waltz.'" |
| Champion Dance A | (48, 192) | 48x96 | Near-perfect form |
| Champion Dance B | (96, 192) | 48x96 | Surprise tempo shift |
| Champion Flourish | (144, 192) | 48x96 | Career-ending finish pose |
| Duelist Defeated | (192, 192) | 48x96 | Shared embarrassment state, any duelist |

### Crowd Reactions:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gasping Pair | (240, 192) | 64x96 | Public failure witnessed |
| Applause Pair | (304, 192) | 64x96 | Duel victory response |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Invitation Check | (0, 288) | 32x32 | Herald inspecting invitation (forgery = 30% detection) |
| Herald Scroll | (32, 288) | 24x32 | Announcement list |
| Bribe Purse | (56, 288) | 24x24 | Intonation adjustment fee |

### Character Notes:
- Each duelist's costume escalates in gold content: Debutante minimal → Champion dripping
- Lady Geheimnis' palette is the Baroness' palette desaturated 40% — visual rhyme, faded glory
- Rumor Broker's face region is pure #1C1C1C in every frame; no eyes ever render

---

## 👥 Sprite Sheet 5: Masked Crowd & Servants
**File:** `baroness_ballroom_crowd.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Formal variety over #4B0082 / #CFB53B / #1C1C1C

### Masked Guests (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Guest — Noble | (0, 0) | 48x80 | Count/Countess template persona |
| Guest — Artist | (48, 0) | 48x80 | Creative-type persona, dramatic scarf |
| Guest — Scholar | (96, 0) | 48x80 | Intellectual persona, pince-nez over mask |
| Guest — Mystery | (144, 0) | 48x80 | No-claims persona, plain domino mask |
| Inner Circle Member | (192, 0) | 48x80 | VIP guest, gold-thread mask |
| Waltz Partner | (240, 0) | 48x80 | Player's assigned dance partner |
| Servant With Tray | (288, 0) | 48x80 | Identical mask — indistinguishable staff |
| Servant Idle | (336, 0) | 48x80 | Same mask, same posture, different pose |
| Ejected Guest | (384, 0) | 64x80 | Being escorted out, mask half-off |

### Background Waltz Loops (96x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Waltz Pair Loop 1 | (0, 80) | 96x96 | Pre-rendered background couple, frame A |
| Waltz Pair Loop 2 | (96, 80) | 96x96 | Frame B |
| Waltz Pair Loop 3 | (192, 80) | 96x96 | Frame C |
| Waltz Pair Loop 4 | (288, 80) | 96x96 | Frame D |
| Fan Flutter Guest | (384, 80) | 48x80 | Standing guest, fan animation anchor |

### Social Encounter Poses:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Conversation Circle | (0, 176) | 128x96 | Three-guest cluster, potential encounter |
| Eavesdropper | (128, 176) | 48x80 | Leaning from refreshment station |
| Snickering Pair | (176, 176) | 96x80 | Crowd reaction to "The Count of Cool" |
| Socially Destroyed Guest | (272, 176) | 48x80 | Mid-destruction, kindness-quest target |
| Kindness Interaction | (320, 176) | 96x80 | Player consoling destroyed guest (Geheimnis trigger) |

### Seated Guests:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seated Guest Row | (0, 272) | 96x64 | Perimeter seating filler |
| Toast Pose Guest | (96, 272) | 48x80 | Raised glass (contents lie about alcohol) |

### NPC Notes:
- All four guest personas share one body rig; masks and one accessory differentiate them
- Servants must be pixel-identical to each other except pose — the indistinguishability is the joke
- Background waltz loops are pre-rendered pairs per mobile optimization (no individual dancer logic)

---

## 🍺 Sprite Sheet 6: Bros in Masquerade
**File:** `baroness_ballroom_bros.png`
**Dimensions:** 384x256 pixels
**Color Palette:** Rented formal wear over #1C1C1C, tourist tells intact

### Masquerade States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pilsner "Count of Cool" | (0, 0) | 48x96 | Entrance pose, cheap mask, maximum confidence |
| Pilsner Baroness Sweat | (48, 0) | 48x96 | "...I'm... cool?" |
| Chadwick Waltz Attempt 1 | (96, 0) | 48x96 | "One two three" — wrong foot forward |
| Chadwick Foot Stomp | (144, 0) | 48x96 | The partner-foot incident |
| Chadwick OW | (192, 0) | 48x96 | "Then why did it hurt ME?!" |
| Bradley Gallery Lean | (240, 0) | 48x96 | Acquiring intelligence, poorly |
| Bradley Intel Note | (288, 0) | 48x96 | "I consider it valuable." |
| Group Ejection | (336, 0) | 48x96 | Unmasked failure state, single-file shame |

### Group & Failure Frames:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Masked Bro Trio | (0, 96) | 144x96 | Group shot — identified in 30 seconds |
| Pilsner "NAILED IT" | (144, 96) | 48x96 | Post-announcement triumph, crowd unconvinced |
| Partner Foot-Hurt | (192, 96) | 48x96 | Dance partner recoiling |
| Humiliated Walk 1 | (240, 96) | 48x96 | Escorted exit, frame A |
| Humiliated Walk 2 | (288, 96) | 48x96 | Escorted exit, frame B |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Count of Cool Mask | (0, 192) | 32x32 | Lord Pilsner's chosen identity prop |
| Crooked Bow Tie | (32, 192) | 24x24 | Chadwick's formal-wear tell |
| Bradley's Notebook | (56, 192) | 24x32 | Intelligence log |

### Technical Notes:
- Bros' waltz frames deliberately desync from the rhythm UI beat — the wrongness is animated, not random
- American posture tells (wide stance, slouch) persist through every masked frame

---

## ✨ Sprite Sheet 7: Effects & Particles
**File:** `baroness_ballroom_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFD9A0 (Candle Warm), #CFB53B (Gold), #FFFFFF (Highlights)

### Candlelight (16x24 each, 3 frames):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Candle Flame 1 | (0, 0) | 16x24 | Tall flicker |
| Candle Flame 2 | (16, 0) | 16x24 | Bend |
| Candle Flame 3 | (32, 0) | 16x24 | Recover |

### Mask & Fabric Shimmer:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mask Sparkle 1 | (48, 0) | 16x16 | Glint on gilded masks |
| Mask Sparkle 2 | (64, 0) | 16x16 | Glint travel |
| Mask Sparkle 3 | (80, 0) | 16x16 | Fade |
| Fabric Shimmer A | (96, 0) | 48x48 | Gown highlight sweep overlay |
| Fabric Shimmer B | (144, 0) | 48x48 | Sweep frame 2 |

### Dance & Social Combat:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Confetti Burst 1 | (192, 0) | 64x64 | Dance victory shower |
| Confetti Burst 2 | (256, 0) | 64x64 | Dispersal |
| Confetti Burst 3 | (320, 0) | 64x64 | Settle |
| Spotlight Cone | (384, 0) | 96x128 | Dance duel follow-spot |
| Cutting Remark Slash | (0, 64) | 48x32 | Social attack impact glyph |
| Perfect Comeback Flash | (48, 64) | 48x48 | Critical hit burst, gold |
| Record Scratch Flash | (96, 64) | 48x48 | Social failure sting visual |

### Ambience & Audio Visuals:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chandelier Glow | (0, 128) | 96x96 | Warm radial light emanation |
| Whisper Trail 1 | (96, 128) | 64x24 | Gallery whisper traveling wisp |
| Whisper Trail 2 | (96, 152) | 64x24 | Wisp mid-travel |
| Whisper Trail 3 | (96, 176) | 64x24 | Wisp arrival curl |
| Crowd Murmur Ring | (160, 128) | 64x64 | Conversation circle ambience pulse |
| Waltz Note Drift | (224, 128) | 32x32 | Floating note glyph (orchestra) |
| Hidden Beat Pulse | (256, 128) | 32x32 | Modern-beat undertone glyph (subtle bass ring) |

### Technical Notes:
- Whisper trails follow spline paths along the gallery curve — CPUParticles2D with path attractor
- Record scratch flash pairs with the comedy audio sting; both fire on Social HP zero events
- Confetti caps at 20 particles on-screen (see performance budget)

---

## 🖥️ Sprite Sheet 8: UI Elements
**File:** `baroness_ballroom_ui.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #4B0082 (Purple), #CFB53B (Gold), #FFFFFF (Text), #8B0000 (Crimson)

### Social Combat UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Social HP Meter | (0, 0) | 192x32 | Evening reputation bar, 100 → 0 |
| Credibility Meter | (192, 0) | 128x32 | Identity performance tracker |
| Dance Rhythm Bar | (320, 0) | 192x64 | Waltz timing UI (3/4 time markers) |
| Interrogation Frame | (0, 32) | 160x64 | Verbal combat dialogue panel |
| Approach Progress | (160, 32) | 128x24 | Baroness gauntlet meter |

### Rumor Trading:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rumor Card Common | (0, 96) | 64x48 | 50 Sovs tier, plain seal |
| Rumor Card Uncommon | (64, 96) | 64x48 | 150 Sovs tier, silver seal |
| Rumor Card Rare | (128, 96) | 64x48 | 400 Sovs tier, gold seal |
| Rumor Card Exclusive | (192, 96) | 64x48 | 1000 Sovs+ tier, Baroness sigil |
| Freshness Indicator | (256, 96) | 24x24 | Rumor decay timer glyph |
| False Rumor Mark | (280, 96) | 24x24 | Detection warning (shape-coded X) |

### Identity System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Identity Card — Count | (0, 144) | 64x48 | Nobility persona card |
| Identity Card — Artist | (64, 144) | 64x48 | Creative persona card |
| Identity Card — Scholar | (128, 144) | 64x48 | Intellectual persona card |
| Identity Card — Mystery | (192, 144) | 64x48 | Blank persona card |
| Identity Card — Custom | (256, 144) | 64x48 | Name-your-own card |

### Items & Status:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Masquerade Mask Basic | (0, 192) | 48x32 | Entry item |
| Masquerade Mask Ornate | (48, 192) | 48x32 | Upgraded item |
| Invitation Card | (96, 192) | 48x32 | Entry requirement (200 Sovs at Black-Tie Backroom) |
| Forged Invitation | (144, 192) | 48x32 | Crafted fake — subtly wrong seal |
| Baroness Favor Icon | (192, 192) | 48x48 | Four-stage favor indicator |
| Inner Circle Badge | (240, 192) | 32x32 | Three-visit unlock |
| Humiliated Stamp | (272, 192) | 64x64 | Failure status (worse than Embarrassed) |
| Baroness Vault Key | (336, 192) | 32x32 | Maestro-defeat reward item |

### Technical Notes:
- Rumor tiers are shape-coded (seal geometry) as well as color-coded for colorblind support
- Forged invitation's wrong seal must be findable in screenshots — community bait
- All touch targets render at minimum 44px in-game scale

---

## 🎬 Animation Specifications

### Chandelier Ambient Sway:
- **Duration:** 4.0 second cycle
- **Frames:** 3 (static → left → right)
- **Pattern:** Slow pendulum loop, ease in/out
- **Trigger:** Constant
- **Purpose:** The room breathes; grandeur with faint unease
- **Audio Sync:** Faint crystal tinkle every second swing apex
- **Mobile Optimization:** Static frame on Low LOD

### Herald Announcement:
- **Duration:** 2.0 seconds (hold on final frame)
- **Frames:** 3 (idle → trumpet raise → announce)
- **Pattern:** Single play, hold announce during name text
- **Trigger:** Player entry / any new arrival
- **Purpose:** First-impression control; intonation makes or breaks reputations
- **Audio Sync:** Trumpet fanfare on frame 2; announcement VO on frame 3 (disdain or warmth variant per bribe level)
- **Mobile Optimization:** None needed

### Waltz Dance Duel Loop:
- **Duration:** 1.8 seconds per bar (3/4 time at ~100 BPM), looping
- **Frames:** 4 per dancer (step → turn → extension → close)
- **Pattern:** Loop synced to rhythm UI; complexity phase adds tempo shifts (Veteran ±10%, Champion ±25%)
- **Trigger:** Dance duel accepted
- **Purpose:** Core rhythm combat readability — beat 1 of each bar is the input window
- **Audio Sync:** Frame 1 lands exactly on downbeat of waltz track
- **Mobile Optimization:** Background waltz pairs drop to 2-frame loops

### Baroness Mask Shift:
- **Duration:** 6.0 second cycle
- **Frames:** 3 mask-shift frames cross-faded over base pose
- **Pattern:** Purple → gold → black → loop, 2s per phase
- **Trigger:** Constant whenever the Baroness is on screen
- **Purpose:** "Impossible to describe consistently" — no two screenshots match
- **Audio Sync:** None
- **Mobile Optimization:** Fix to single mask frame on Low LOD

### Whisper Trail:
- **Duration:** 3.0 seconds per traversal
- **Frames:** 3 wisp sprites along spline
- **Pattern:** Spawn at speaker → travel gallery curve → curl at listener
- **Trigger:** Rumor exchange begins; ambient every 8-12s in gallery
- **Purpose:** Makes the acoustic gimmick visible; guides players to trade hubs
- **Audio Sync:** Whisper SFX pans left-to-right following wisp position
- **Mobile Optimization:** Halve ambient spawn rate

### Confetti Victory Burst:
- **Duration:** 1.2 seconds, single play
- **Frames:** 3
- **Pattern:** Burst → disperse → settle, despawn
- **Trigger:** Dance duel victory
- **Purpose:** Public triumph — the crowd celebrates so the loser suffers more
- **Audio Sync:** Triumphant dance flourish sting on frame 1
- **Mobile Optimization:** 20 → 10 particles

### Unmasked Ejection:
- **Duration:** 2.5 seconds, single play
- **Frames:** 2-frame walk (Humiliated Walk 1-2) looped across exit path + mask half-off state
- **Pattern:** Escort walk to nearest secret exit, screen fade
- **Trigger:** Social HP reaches 0 or identity exposure
- **Purpose:** Failure state with maximum public visibility
- **Audio Sync:** Record scratch on trigger; sad waltz variant during walk
- **Mobile Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Duelist outline overlay | set at sheet layout | 48x96 | High-contrast rim on active dance challenger |
| Baroness dais boundary | set at sheet layout | 128x64 | Bright edge marking the social-death zone |
| Rumor Broker locator | set at sheet layout | 48x96 | Silhouette enhancement in shadowed gallery |
| Secret exit markers | set at sheet layout | 32x64 | High-visibility frames on all three exits |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chandelier static frame | set at sheet layout | 128x96 | No sway loop |
| Sparkle-free mask set | set at sheet layout | 48x80 | Guests without glint particles |
| Static background couples | set at sheet layout | 96x96 | Waltz pairs frozen at frame A |
| Confetti-free victory card | set at sheet layout | 96x64 | Text panel replaces particle burst |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fanfare glyph | set at sheet layout | 32x32 | Trumpet icon over Herald on announcement audio |
| Downbeat flash ring | set at sheet layout | 48x48 | Dance floor pulse on every waltz downbeat |
| Whisper direction arrow | set at sheet layout | 24x24 | Points along gallery when whisper SFX pans |
| Gasp/applause bubbles | set at sheet layout | 32x24 | Crowd reaction glyphs paired with reaction audio |
| Record-scratch burst | set at sheet layout | 48x48 | Jagged star on social failure sting |

### Colorblind Considerations:
- Rumor tiers use distinct seal shapes (circle/diamond/crest/sigil), never color alone
- Social HP (crimson) and Credibility (gold) meters use different fill textures (solid vs. hatched)
- Dance timing windows show shape markers (bar lines) in addition to color zones
- Touch zones minimum 44px for rumor cards, identity selection, and dance inputs

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); Baroness sheet at ASTC 4x4 — the mask shift must not band
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for landmarks sheet (chandelier is screenshot-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| ballroom_environment | tileset, landmarks | 2048x1024 |
| ballroom_characters | Baroness/Schatten, court NPCs, crowd, bros | 1024x1024 |
| ballroom_effects_ui | effects, UI | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full crowd loops, chandelier sway, mask shift cycle, whisper trails, all particles |
| Medium | Half ambient particle rate, 2-frame crowd loops, mask shift at 2 frames |
| Low | Static chandelier, frozen background couples, single mask frame, no ambient particles |

### Performance Targets:
- **Target FPS:** 60 (per location profile budget)
- **Max Draw Calls:** 24 per frame
- **Memory Footprint:** 55 MB maximum
- **Particle Limit:** 24 (candles 8, whisper 4, sparkle 8 → confetti burst swaps in at 20, never concurrent with sparkle)

### Performance Notes:
- Crowd is pre-rendered pair loops per profile mobile spec — no per-dancer skeletons
- Private salons and Baroness salon load on-demand (door-gated scenes)
- Three entrance route exteriors are separate lightweight scenes, never resident with the ballroom

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for Baroness, Schatten, duelists; static Sprite2D pool for pre-rendered crowd pairs
- CPUParticles2D (not GPU) for candles, confetti, whisper trails
- CanvasLayer for Social HP / Credibility / rumor UI
- Location state machine: `entry_check → announced → floor_free → social_encounter → dance_duel → baroness_audience → ejected/exit` drives sprite set swaps
- Masquerade identity choice stored as flag; Herald announce frame + VO variant keyed to it

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Herald trumpet raise | Trumpet fanfare | Frame 2 of announcement |
| Waltz dance frames | Orchestra downbeat | Frame 1 lands on every bar's beat 1 |
| Whisper trail wisp | Panned whisper SFX | Pan position tracks wisp x-coordinate |
| Chandelier sway apex | Crystal tinkle | Every second apex |
| Social HP zero | Record scratch + sad waltz | On trigger frame |
| Confetti burst | Dance flourish sting | Frame 1 |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Mask Etiquette Exam | Invitation card, Herald check pose | Prerequisite completion enables clean entry |
| The Baroness' Favor | Baroness full state set, favor icon, approach progress bar | Multi-stage social quest to maximum favor |
| The Former Baroness | Lady Geheimnis set, kindness interaction pose, socially destroyed guest | Couchsurf trigger + backstory quest |
| Rumor Network | All four rumor card tiers, freshness indicator | Collect all exclusive rumors |
| Dance Champion | All duelist sets, Der Schatten dance frames, confetti | Defeat all duelists including Der Schatten |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bassline Opera House | Opera route curtain door; Maestro's Vault Keys item | Curtain part + muffled-orchestra crossfade |
| The Black-Tie Backroom | Invitation card (purchased there); shared rumor card assets | Standard door, rumor UI persists |
| Café Existenz | Café route bookcase door | Bookcase swing + coffeehouse murmur fade |
| Mozart's Last Rave | Cemetery route stone door (underground passage) | Stone grind + bass-to-waltz audio crossfade |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Anonymous chaos in formal attire — performance art about performance"
- **Color Mood:** Midnight purple and gold under candle warmth; cream marble keeping everything theatrical
- **Lighting:** Chandelier centerpiece, candle pools, strategic shadow bands for intrigue; spotlight isolation during duels
- **Texture:** Velvet, gilt, polished checker marble, mask lacquer

### Environmental Storytelling:
- No mirror ever shows a full face — the room itself maintains the social contract
- Name cards, seating chart, and portraits all masked: the lie is institutional, generations deep
- Lady Geheimnis' faded palette echoing the Baroness' tells the succession story wordlessly
- Refreshment stations angled toward conversation circles — eavesdropping is load-bearing architecture

### Character Integration Notes:
- The Baroness must read as the most saturated object in any frame she occupies
- Der Schatten renders with no outline highlight — a hole in the lighting
- Servants pixel-identical; crowd guests rig-shared with mask/accessory swaps
- Bros keep their tourist posture through every masked frame — identified in 30 seconds, forever

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The "Count of Cool" announcement** — Herald's pained pause rendered in one disdain frame
2. **Chadwick's foot-stomp waltz** against a floor of flawless background couples
3. **The Baroness' shifting mask** — no two screenshots of her match
4. **The Unmasked ejection** — mask half-off, secret exit, maximum shame

### Quote Potential:
- "PRESENTING... *adjusts delivery based on bribe level* ...a guest." - The Herald
- "Your mask is... adequate. But masks are for faces. What mask does your SOUL wear?" - The Baroness
- "I've danced here for twenty years. You have twenty seconds to impress me." - The Veteran
- "I wore the crown of secrets for twelve years. Then I learned the price. Some truths cost everything, dear." - Lady Geheimnis
- "That was MY foot." / "Then why did it hurt ME?!" - Dance Partner & Chadwick

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | baroness_ballroom_tileset.png | 1024x512 |
| 2 | baroness_ballroom_landmarks.png | 512x512 |
| 3 | baroness_of_masks.png | 512x384 |
| 4 | baroness_ballroom_court_npcs.png | 512x384 |
| 5 | baroness_ballroom_crowd.png | 512x384 |
| 6 | baroness_ballroom_bros.png | 384x256 |
| 7 | baroness_ballroom_effects.png | 512x256 |
| 8 | baroness_ballroom_ui.png | 512x256 |

**Total Estimated Memory:** ~7 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `baroness_ballroom_tileset.png` (1024x512)
- [ ] `baroness_ballroom_landmarks.png` (512x512)
- [ ] `baroness_of_masks.png` (512x384)
- [ ] `baroness_ballroom_court_npcs.png` (512x384)
- [ ] `baroness_ballroom_crowd.png` (512x384)
- [ ] `baroness_ballroom_bros.png` (384x256)
- [ ] `baroness_ballroom_effects.png` (512x256)
- [ ] `baroness_ballroom_ui.png` (512x256)

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
- **Documentation:** Animation timing reference sheet + waltz downbeat sync chart + entrance route scene guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] No mirror sprite resolves a readable full face
- [ ] Servant sprites pixel-identical except pose
- [ ] Baroness mask-shift frames cross-fade without banding
- [ ] Bros' tourist posture reads through masks at game resolution
- [ ] Waltz frames land frame 1 on the downbeat marker
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (anonymity theater) is clear throughout all assets
- [ ] Hidden entrances/exits have discoverable visual cues
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Viennese/Habsburg ball culture evoked, never named |
| Cultural Specificity | ✅ | Habsburg masquerade traditions, waltz culture, social-season hierarchy |
| Satirical Targets Appropriate | ✅ | High-society performance and bros who think masks make them suave — punches up |
| Seedy Underbelly Present | ✅ | Rumor economy, blackmail disguised as gossip, reputation as weapon |
| Gameplay Value Established | ✅ | Social combat, dance duels, rumor trading, identity system, couchsurf |
| Technical Feasibility | ✅ | Eight sheets, atlas plan, pre-rendered crowd, LOD tiers documented |
| Mobile Performance Budget | ✅ | 60 FPS, 24 draw calls, 55 MB, 24 particles (per profile budget) |
| Accessibility Features | ✅ | Visual cues for all audio events; static motion variants |
| No Crypto Elements | ✅ | None present — pure social/masquerade satire |
| Social Media Integration | ✅ | Count of Cool, foot-stomp waltz, shifting mask moments identified |

**Baroness' Ballroom: Where masks reveal more than faces ever could, the waltz ends careers, and three bros in rented formal wear were made the evening's entertainment without ever knowing it.**
