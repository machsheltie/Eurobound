# Crown & Cask - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Crown & Cask - the imperial-themed brewery where the beer flows like royal bloodlines, the taproom looks like a throne room, and commoners are welcome as long as they bow to the brewing process. It is Sinfonia Brewery Tour stamp location #3, home of the Coronation Ceremony and a "royal family" that is one guy and his cousins committed so fully to the bit it has become indistinguishable from belief.

**Location ID:** `sinfonia_imperialsquare_crown_cask_01`
**Theme:** Habsburg nostalgia and inherited privilege — imperial aesthetics applied to the mundane act of drinking beer
**Zone:** Imperial Square, Grand Entrance District
**Hours:** 11 AM - 12 AM (royal hours)
**Primary Function:** Brewery / Brewery Tour stamp location — Coronation Ceremony (QTE + dialogue), signature beer shop, throne selfie spot, hidden Usurper quest

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Habsburg Gold | #FFD700 | Crowns, trim, taps, everything with a crown motif |
| Imperial Purple | #4B0082 | Robes, banners, stamp ink |
| Palace Cream | #FFF8DC | Walls, ceiling murals, marble |
| Royal Red | #8B0000 | Bunting, carpets, throne upholstery |
| Habsburg Yellow | #F5C518 | Exterior façade walls |
| Cellar Oak | #5C4033 | Barrels, banquet tables, dark wood |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/crown_and_cask/
├── environment/
│   ├── crown_cask_tileset.png
│   └── crown_cask_landmarks.png
├── npcs/
│   ├── konig_klaus.png
│   └── crown_cask_npcs.png
├── objects/
│   └── crown_cask_drinks.png
├── effects/
│   └── crown_cask_effects.png
└── ui/
    └── crown_cask_ui.png
```

---

## 🏰 Sprite Sheet 1: Palace Brewery Tileset
**File:** `crown_cask_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #F5C518 (Habsburg Yellow), #FFF8DC (Palace Cream), #FFD700 (Gold), #5C4033 (Cellar Oak)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Great Hall Marble | (0, 0) | 32x32 | Cream marble, crown-motif inlay |
| Crown Floor Tile | (32, 0) | 32x32 | Gold crown medallion tile |
| Red Carpet | (64, 0) | 32x32 | Throne approach runner |
| Carpet Gold Edge | (96, 0) | 32x32 | Runner border |
| Cellar Flagstone | (128, 0) | 32x32 | Royal Cellar stonework |
| Courtyard Paving | (160, 0) | 32x32 | Beer garden stone |
| Courtyard Lawn | (192, 0) | 32x32 | Hedge-framed grass |

### Wall Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Palace Cream Wall | (0, 32) | 32x64 | Interior plaster with gilt line |
| Mural Wall Segment | (32, 32) | 32x64 | Cherubs-holding-steins fresco piece |
| Habsburg Yellow Exterior | (64, 32) | 32x64 | Façade wall section |
| Cellar Stone Wall | (96, 32) | 32x64 | Cool barrel-vault masonry |
| Red-Gold Bunting Wall | (128, 32) | 32x64 | Draped celebration segment |
| Wainscot Gilded Cap | (160, 32) | 32x32 | Gold molding strip |

### Vaulted Ceiling & Architecture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Vault Rib Section | (0, 96) | 64x64 | Painted ceiling arch |
| Mural Cherub Panel | (64, 96) | 64x64 | Cherub toasting with stein |
| Column Ornate | (128, 96) | 32x96 | Entrance column, gilt capital |
| Column With Bunting | (160, 96) | 32x96 | Celebration-dressed variant |

### Doors & Passages:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Commoner's Gate | (192, 96) | 32x64 | Regular door with fancy name |
| Grand Entrance Doors | (224, 96) | 64x64 | Column-framed double doors |
| Cellar Stair Descent | (288, 96) | 64x80 | Dramatically lit stone steps |
| Courtyard Archway | (352, 96) | 48x80 | Garden access arch |

### Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Banquet Table Section | (0, 192) | 96x48 | Long oak table, rank-arranged seating |
| Throne Bar Stool | (96, 192) | 24x40 | Throne-shaped, uncomfortable, authentic |
| Servants' Bell | (120, 192) | 16x24 | Staff ignores it ironically |
| Front-Rank Bench | (136, 192) | 64x32 | Regulars' seating near throne |
| Back-Rank Bench | (200, 192) | 64x32 | Newcomers' seating, identical but further |

### Exterior Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Miniature Palace Façade | (0, 256) | 128x96 | Ornate windows, Habsburg-yellow |
| Coat of Arms (Crowned Stein) | (128, 256) | 48x48 | Entrance crest |
| Decorative Guard Post | (176, 256) | 32x64 | Sentry box, purely theatrical |
| Red-Gold Bunting Swag | (208, 256) | 64x24 | Exterior celebration drape |
| Signage "By Royal Appointment (Self-Appointed)" | (272, 256) | 96x32 | Main sign |
| Signage "All Subjects Welcome" | (272, 288) | 96x24 | "Some More Than Others" subline |

### Technical Notes:
- Crown motif appears on floor tiles, glasses, coasters, napkins — commit to the saturation gag
- Front-rank and back-rank benches are pixel-identical; only placement communicates hierarchy
- Cellar tiles use a cooler shadow ramp than the hall (temperature-controlled, dramatically lit)

---

## 👑 Sprite Sheet 2: Landmarks & Major Props
**File:** `crown_cask_landmarks.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #FFD700 (Gold), #8B0000 (Royal Red), #5C4033 (Oak)

### The Throne (Brewmaster's Station):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Throne Empty | (0, 0) | 80x112 | Elevated platform, red upholstery, tap-scepter rack |
| Throne Occupied Frame | (80, 0) | 80x112 | König Klaus seated, holding court |
| Throne With Player | (160, 0) | 80x112 | Selfie-spot state (with permission) |
| Tap Scepter Array | (240, 0) | 96x64 | Taps arranged around throne like scepters |
| Ceremonial Stein | (336, 0) | 32x48 | The knighting vessel |
| Bottle Chandelier | (368, 0) | 96x80 | Repurposed beer-bottle chandelier |

### The Royal Cellar:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Aging Barrel Large | (0, 112) | 64x64 | Oak, crown-branded |
| Barrel Rack Row | (64, 112) | 128x64 | Stacked reserves |
| Crown Jewels Case | (192, 112) | 64x64 | Special reserves under glass, spotlighted |
| Cellar Torch Sconce | (256, 112) | 16x40 | Dramatic torchlight |
| Stamp Ceremony Plinth | (272, 112) | 48x64 | Where the real stamp ceremony happens |

### The Courtyard (Beer Garden):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Beer-Pouring Fountain | (0, 176) | 96x96 | Statues eternally pouring |
| Stein-Shaped Hedge | (96, 176) | 48x64 | Topiary commitment |
| Garden Table Set | (144, 176) | 64x48 | Knighted drinkers' gathering spot |
| Fountain Pour Overlay | (208, 176) | 32x48 | Animated water-beer stream |

### Imperial Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Monarch Portrait 1 | (0, 272) | 48x64 | Previous brewmaster (suspiciously similar face) |
| Monarch Portrait 2 | (48, 272) | 48x64 | Also that face |
| Monarch Portrait 3 | (96, 272) | 48x64 | Still that face |
| Royal Decree Frame | (144, 272) | 40x48 | Actually a beer special |
| Founder's Yeast Shrine | (184, 272) | 48x56 | Great-grandfather's cultures, venerated |
| Dynasty Family Tree | (232, 272) | 64x64 | Seven brewmasters, one gene pool |

### Technical Notes:
- All three monarch portraits share one face template with different wigs — the joke must survive 48x64
- Fountain pour overlay loops via 2-frame UV scroll on the stream region
- Crown Jewels case gets its own spotlight glow from the effects sheet

---

## 🍺 Sprite Sheet 3: König Klaus — The Royal Brewmaster
**File:** `konig_klaus.png`
**Dimensions:** 384x288 pixels
**Color Palette:** #4B0082 (Imperial Purple), #FFD700 (Gold), #FFFFFF (Ermine Trim)

### Court States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Regal Idle | (0, 0) | 48x96 | Fake ermine robe, plastic-but-dignified crown, tap-handle scepter |
| Subjects Approach | (48, 0) | 48x96 | Arms wide: "SUBJECTS! APPROACH!" |
| Dynasty Speech | (96, 0) | 48x96 | Gesturing at portraits: "SEVENTH Royal Brewmaster!" |
| Offended | (144, 0) | 48x96 | "IT IS NOT A THEME! It is a BIRTHRIGHT!" |

### Coronation Ceremony (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Question Pose | (192, 0) | 48x96 | "Do you swear to honor the brew?" |
| Blessing | (240, 0) | 48x96 | Hands raised over kneeling subject |
| Knighting Tap Handle | (288, 0) | 48x96 | Scepter to shoulder, maximum gravity |
| Stamp Press | (336, 0) | 48x96 | Crown seal descending onto passport page |

### Reaction States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Delighted | (0, 96) | 48x96 | "NOW THIS is a proper subject!" |
| Disappointed Pause | (48, 96) | 48x96 | "...'Sure.' Very well." |
| Royal Disappointment | (96, 96) | 48x96 | Ceremony spill witnessed, composure straining |
| "I'll Allow It" | (144, 96) | 48x96 | Bradley's biochemical oath accepted |
| Throne Usurped Fury | (192, 96) | 48x96 | Someone is on the throne WITHOUT permission |
| Anniversary Promise | (240, 96) | 48x96 | "There is a SASH!" |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Plastic Crown | (288, 96) | 24x16 | Dignified despite everything |
| Tap-Handle Scepter | (312, 96) | 16x40 | The realm's true regalia |
| Fake Ermine Robe Hem | (328, 96) | 40x24 | Trim detail for close-ups |

### Ceremony Wide Shot:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knighting Tableau | (0, 192) | 144x96 | Klaus + kneeling participant, composed scene |
| Blessing Tableau | (144, 192) | 144x96 | Stein raised between them |

### Animation Timing:
- Court gestures: 3fps, loop
- Knighting: 4fps, single play, hold on shoulder-tap frame
- Stamp press: 6fps, single play
- Usurped fury: 4fps, loop while player remains on throne

### Character Notes:
- Klaus believes completely; no frame may wink at the audience
- Crown sits slightly crooked in every frame except ceremony frames, where he straightens it
- Robe trim is visibly fake fur — dignity carried by posture, not materials

---

## 🫅 Sprite Sheet 4: Court Staff & Regulars
**File:** `crown_cask_npcs.png`
**Dimensions:** 384x192 pixels
**Color Palette:** Livery gold-purple, #5C4033 (Oak), commoner earth tones

### The Royal Cousins (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cousin Serving | (0, 0) | 48x80 | Matching livery, family resemblance |
| Cousin Ceremony Assist | (48, 0) | 48x80 | Holding ceremonial stein tray |
| Cousin Eye-Roll | (96, 0) | 48x80 | Fired only when Klaus isn't looking |
| Cousin Whisper | (144, 0) | 48x80 | "Just go with it. It makes him happy." |

### Knighted Regulars (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Regular With Pin | (192, 0) | 48x80 | "Knight of the Cask" pin prominent |
| Twelve-Time Knight | (240, 0) | 48x80 | Pin collection across chest |
| Regular Coaching | (288, 0) | 48x80 | "Don't laugh. He hates that." |
| Courtyard Knight Toast | (336, 0) | 48x80 | Beer garden gathering pose |

### Ceremony Participants (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Participant Kneeling | (0, 80) | 48x80 | Optional but "appreciated" |
| Participant Drinking | (48, 80) | 48x80 | Ceremonial stein, mid-timing-minigame |
| Participant Spill | (96, 80) | 48x80 | Royal Disappointment trigger |
| Participant Risen Knight | (144, 80) | 48x80 | Newly dubbed, glowing with unearned nobility |

### Decorative Guards (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Guard At Attention | (192, 80) | 48x80 | Entrance decoration, does nothing |
| Guard Blink | (240, 80) | 48x80 | The only movement he is permitted |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knight Pin | (288, 80) | 16x16 | Crest close-up |
| Livery Crest Patch | (304, 80) | 16x16 | Cousin uniform detail |
| Anniversary Sash | (320, 80) | 24x48 | The promised sash, on display |

### Character Notes:
- All cousins share one face family with Klaus — lineage legitimacy by proximity
- Guards are set dressing that blinks; they must never react to the Usurper event (the punchline is Klaus reacts alone)
- Knight pins scale from one to twelve on the veteran regular

---

## 🍻 Sprite Sheet 5: Royal Beers & Items
**File:** `crown_cask_drinks.png`
**Dimensions:** 256x192 pixels
**Color Palette:** #FFD700 (Golden Ale), #5C4033 (Dark), #FFF8DC (Foam)

### Menu Beers (32x48 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Heir Apparent Ale | (0, 0) | 32x48 | Signature golden ale in crown-shaped glass (glass is yours, +3 Sovs) |
| The Commoner | (32, 0) | 32x48 | 4 Sovs honest lager, apologetic presentation |
| Duke's Dark | (64, 0) | 32x48 | 7 Sovs dark, served with slight bow |
| Princess Pilsner | (96, 0) | 32x48 | 5 Sovs pale, served with curtsey |
| The Usurper (Guest Beer) | (128, 0) | 32x48 | 6 Sovs, discussed in hushed tones |
| King's Reserve | (160, 0) | 32x48 | 15 Sovs, full ceremony service |

### Ceremony & Tour Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crown Bottle Opener | (192, 0) | 32x32 | Miniature Habsburg crown, opener base |
| Velvet Pouch | (224, 0) | 32x32 | Purple, gold-tone drawstring |
| Certificate of Nobility | (192, 32) | 32x24 | Tiny scroll, entirely sincere |
| Ceremonial Stein Filled | (224, 32) | 32x48 | Foam crown mandatory |

### Beer States (32x48 / 32x24):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crown Glass Empty | (0, 48) | 32x48 | Keepsake state |
| Crown Glass Half | (32, 48) | 32x48 | Mid-ceremony |
| Spilled Beer Puddle | (64, 48) | 48x24 | Royal Disappointment evidence |
| Foam Crown Detail | (112, 48) | 24x16 | Perfect pour topper |

### Stamp Assets:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Brewery Stamp Face | (0, 96) | 64x64 | Ornate crown atop beer barrel |
| Stamp Inked Result | (64, 96) | 64x64 | Royal purple with gold-leaf flecks, "Duly Knighted" |
| Stamp Handle | (128, 96) | 32x48 | Gold-crowned press |
| Passport Page Open | (160, 96) | 64x48 | Brewery Tour page ready to receive |

### Technical Notes:
- Heir Apparent Ale glass silhouette must read as a crown at 32x48 — it is the shop's icon
- Stamp face and inked result must match 1:1 so the press animation lands convincingly
- Foam crowns render on every poured beer; a beer without foam is a continuity error

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `crown_cask_effects.png`
**Dimensions:** 256x128 pixels
**Color Palette:** #FFD700 (Gold), #FFF8DC (Foam/Light), #FFFFFF (Sparkle)

### Ceremony Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Trumpet Fanfare Burst | (0, 0) | 48x48 | Tiny heraldic flourish on stamp |
| Crown Descend Glow | (48, 0) | 48x48 | Stamp-press halo |
| Knighting Sparkle | (96, 0) | 32x32 | Shoulder-tap glint |
| Noble Blood Aura | (128, 0) | 48x48 | Post-ceremony buff shimmer |

### Ambience:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dust Motes In Beam | (176, 0) | 48x48 | Cellar and hall light shafts |
| Candle Flicker 1 | (224, 0) | 16x24 | Chandelier candle frame A |
| Candle Flicker 2 | (240, 0) | 16x24 | Frame B |
| Torch Flame 1 | (224, 48) | 16x32 | Cellar torch frame A |
| Torch Flame 2 | (240, 48) | 16x32 | Cellar torch frame B |

### Beer Physics:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Foam Crown Rise 1 | (0, 48) | 24x24 | Pour settling frame A |
| Foam Crown Rise 2 | (24, 48) | 24x24 | Frame B |
| Foam Crown Rise 3 | (48, 48) | 24x24 | Perfect crown formed |
| Fountain Stream Loop A | (72, 48) | 32x48 | Statue pour frame A |
| Fountain Stream Loop B | (104, 48) | 32x48 | Statue pour frame B |
| Spill Splash | (136, 48) | 32x24 | Ceremony failure moment |

### Comedy Stings:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sad Horn Glyph | (0, 80) | 32x32 | Ceremony failure visual sting |
| Extended Fanfare Rays | (32, 80) | 64x32 | Perfect-ceremony celebration burst |
| Throne Spotlight | (96, 80) | 64x48 | Authority pool on the Brewmaster's seat |

### Technical Notes:
- Fanfare burst and sad horn glyph are mutually exclusive per ceremony resolution
- Fountain loop runs at 2fps — stately, never splashy
- Noble Blood aura attaches to player sprite for 45 in-game minutes post-ceremony

---

## 🖥️ Sprite Sheet 7: UI Elements
**File:** `crown_cask_ui.png`
**Dimensions:** 256x192 pixels
**Color Palette:** #4B0082 (Purple), #FFD700 (Gold), #FFF8DC (Cream)

### Coronation Ceremony Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Coronation UI Frame | (0, 0) | 160x96 | Ritual dialogue + QTE panel |
| QTE Approach Meter | (160, 0) | 96x24 | Don't-trip timing bar |
| Drink Timing Ring | (160, 24) | 48x48 | No-spill mini-game dial |
| Answer Chip Best | (160, 72) | 96x24 | "With my liver and heart" tier |
| Answer Chip Acceptable | (0, 96) | 96x24 | "Yes" / "Gold (tip)" tier |
| Answer Chip Failure | (96, 96) | 96x24 | "It's just beer" tier (jagged border) |

### Status & Progression:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Noble Blood Buff Icon | (192, 96) | 32x32 | +2 Charm +2 Style, 45 min |
| Knighted Title Badge | (224, 96) | 32x32 | "Knight/Dame of the Cask" |
| Royal Disappointment Icon | (0, 120) | 32x32 | Spill failure status |
| Retry Prompt Banner | (32, 120) | 96x24 | "Buy another beer to retry" |
| Usurper Alert | (128, 120) | 48x32 | Staff-approaching warning (hidden quest) |

### Brewery Tour Integration:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp Slot UI | (0, 152) | 48x40 | Passport page target zone |
| Tour Progress Pip | (48, 152) | 24x24 | Stamp #3 of Sinfonia tour |
| Bottle Opener Required Icon | (72, 152) | 24x24 | Entry-condition reminder |
| Selfie Prompt Crown | (96, 152) | 32x32 | Throne photo-op indicator |
| Achievement Toast Frame | (128, 152) | 96x32 | "Knighted" / "The Usurper" pop |

### Technical Notes:
- Answer chips are border-coded (smooth/double/jagged) as well as color-coded
- Drink timing ring must be readable one-handed at 44px+ touch scale
- Usurper alert fires only while seated on throne pre-ceremony (hidden quest trigger)

---

## 🎬 Animation Specifications

### The Knighting:
- **Duration:** 2.5 seconds, single play
- **Frames:** 4 (question pose → blessing → tap-handle knighting → hold)
- **Pattern:** Sequential, hold final frame through Klaus's speech
- **Trigger:** Coronation Ceremony questions answered, drink completed
- **Purpose:** The ridiculous ritual everyone does anyway — maximum pomp, tap-handle scepter
- **Audio Sync:** Trumpet sting on knighting contact frame; "Rise, Knight of the Cask!" VO after
- **Performance Optimization:** None needed

### Stamp Press:
- **Duration:** 1.2 seconds, single play
- **Frames:** 3 (crown descends → press → lift revealing ink)
- **Pattern:** Single play with tiny screen-shake on press
- **Trigger:** Ceremony success
- **Purpose:** The Brewery Tour payoff — royal purple, gold-leaf flecks, "Duly Knighted"
- **Audio Sync:** Tiny trumpet fanfare on descend; seal-press thump on press frame
- **Performance Optimization:** Drop screen-shake on Low LOD

### Ceremonial Drink Timing:
- **Duration:** 3.0 seconds active window
- **Frames:** 2 participant states (drinking → risen) + spill branch
- **Pattern:** Timing ring closes; tap inside window = clean drink, outside = spill
- **Trigger:** Ceremony phase 4
- **Purpose:** Easy mini-game with a public failure state
- **Audio Sync:** Gulp on success; splash + sad horn on spill
- **Performance Optimization:** Widen timing window 15% on small screens

### Foam Crown Settle:
- **Duration:** 1.5 seconds, single play
- **Frames:** 3
- **Pattern:** Rise → rise → formed, hold
- **Trigger:** Any beer poured/served
- **Purpose:** Every pour is a tiny coronation
- **Audio Sync:** Pour SFX tail ends as frame 3 lands
- **Performance Optimization:** None needed

### Fountain Pour Loop:
- **Duration:** 1.0 second cycle
- **Frames:** 2
- **Pattern:** A ↔ B stately loop
- **Trigger:** Constant in courtyard
- **Purpose:** Beer-pouring statues — imperial grandeur, absurd subject
- **Audio Sync:** Continuous fountain trickle bed
- **Performance Optimization:** Static frame on Low LOD

### Cousin Eye-Roll:
- **Duration:** 1.0 second, single play
- **Frames:** 2 (serving → eye-roll → back)
- **Pattern:** Fires only when Klaus's facing is away; suppressed otherwise
- **Trigger:** Random 20-40s while Klaus mid-court
- **Purpose:** Varying commitment to the bit, visible to observant players only
- **Audio Sync:** None
- **Performance Optimization:** None needed

### Throne Usurp Confrontation:
- **Duration:** Loop until player stands
- **Frames:** 2 (Klaus fury A/B)
- **Pattern:** Fury loop + Usurper alert UI slide-in
- **Trigger:** Player sits on throne before completing ceremony
- **Purpose:** Hidden quest "The Usurper" — worth it
- **Audio Sync:** Record-scratch on trigger; regal music halts
- **Performance Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Throne outline | set at sheet layout | 80x112 | Primary interactable high-contrast frame |
| König Klaus outline | set at sheet layout | 48x96 | Ceremony authority silhouette |
| Cellar stair marker | set at sheet layout | 64x80 | Tour route visibility |
| Ceremonial stein highlight | set at sheet layout | 32x48 | Drink mini-game target |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static fountain | set at sheet layout | 96x96 | No pour loop |
| Flicker-free candles/torches | set at sheet layout | 16x32 | Steady flame frames |
| Shake-free stamp press | set at sheet layout | 64x64 | Press lands without screen-shake |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fanfare glyph | set at sheet layout | 32x32 | Trumpet icon on every fanfare audio |
| Seal thump ring | set at sheet layout | 32x32 | Impact ring on stamp press sound |
| Sad horn glyph | set at sheet layout | 32x32 | Failure sting visual |
| VO speech burst | set at sheet layout | 24x24 | Klaus proclamation indicator |

### Colorblind Considerations:
- Answer chips border-coded (smooth/double/jagged), never color alone
- Drink timing ring uses a closing shape, not a color shift, for the window
- Noble Blood vs. Royal Disappointment icons have distinct silhouettes (crown vs. tipped stein)
- Touch zones minimum 44px for ceremony inputs, menu, and stamp slot

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) stamp assets kept uncompressed — the "Duly Knighted" ink must stay legible
- **Fallback:** PNG high quality for landmarks sheet (throne is the selfie centerpiece)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| crown_cask_environment | tileset, landmarks | 1024x1024 |
| crown_cask_characters | König Klaus, staff & regulars | 512x512 |
| crown_cask_items_fx | drinks, effects, UI | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Fountain loop, candle/torch flicker, dust motes, foam settles, full ceremony effects |
| Medium | Static fountain, halved dust density, 1-frame flames |
| Low | All ambient static, ceremony effects only (fanfare/stamp retained — they are the content) |

### Performance Targets:
- **Target FPS:** 60 (no budget stated in location profile — engine default applied; flagged for owner review)
- **Max Draw Calls:** 20 per frame
- **Memory Footprint:** 35 MB maximum
- **Particle Limit:** 20 (dust 8, flames 8, ceremony burst 12 — ceremony swaps ambient off, never concurrent)

### Performance Notes:
- Royal Cellar loads on-demand (tour-gated sub-scene)
- Courtyard is a separate lightweight scene sharing the drinks and effects atlases
- Ceremony tableau frames replace live Klaus + participant sprites during the wide shot — one draw call

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for Klaus states; Sprite2D pool for guards, regulars
- CPUParticles2D (not GPU) for dust, ceremony bursts
- CanvasLayer for coronation UI and stamp slot
- Location state machine: `entered → acknowledged_brewmaster → beer_purchased → ceremony_active → knighted / royal_disappointment → stamp_granted` drives Klaus state and UI availability
- Entry condition check: Sinfonia Bottle Opener in inventory required for stamp path; head-nod acknowledgment fires on first Klaus proximity

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Knighting contact frame | Trumpet sting | On shoulder tap |
| Stamp press | Seal thump + tiny fanfare | Descend = fanfare, press = thump |
| Ceremony spill | Splash + sad horn | On spill frame |
| Perfect ceremony | Extended fanfare | On risen-knight frame |
| Throne usurp | Record scratch, music halt | On sit trigger |
| Foam settle | Pour tail-off | Frame 3 |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Full Coronation | Answer chips (best tier), extended fanfare, risen knight | Perfect ceremony performance achievement path |
| Collect the Bloodline | All six beer sprites | Try all Crown & Cask beers |
| The Usurper (hidden) | Throne with player, Klaus fury, Usurper alert | Sit on throne before ceremony; "Worth It" selfie variant |
| Brewery Tour Stamp #3 | Stamp assets, passport page, tour pip | Coronation Ceremony completion grants stamp |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Imperial Square | Shared district exterior ambience, tourist traffic | Standard street transition |
| Haute Couture Haberdashery | Formal attire equipment improves seating rank | None (equipment check on entry) |
| Baroness' Ballroom | Aristocratic culture overlap; Noble Blood buff referenced in social checks | None |
| Brewery Tour (system-wide) | Stamp slot UI, passport page, bottle opener icon shared assets | Persistent tour CanvasLayer |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Total commitment to absurd formality — a palace built around a beer tap"
- **Color Mood:** Habsburg gold and imperial purple on palace cream; royal red carpets pointing at a tap handle
- **Lighting:** Chandelier grandeur in the hall, throne spotlight, torch-lit cellar drama
- **Texture:** Gilt over oak, fake ermine, foam crowns, plastic crown worn with absolute conviction

### Environmental Storytelling:
- Three monarch portraits with one face: the dynasty is one guy and his cousins
- Royal decrees on the walls are beer specials — read closely, the empire is a menu
- Servants' bells at every table that staff ironically ignore
- Rank-arranged banquet seating on identical benches — hierarchy as pure placement

### Character Integration Notes:
- Klaus is never in on the joke; every frame plays the bit straight
- Cousins carry the audience's eye-roll so Klaus never has to break
- Decorative guards must stay indifferent even during the Usurper event — Klaus's solitary fury is the punchline

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Coronation kneel** — plastic crown, tap-handle scepter, total sincerity
2. **The Usurper selfie** — on the throne, staff approaching, "Worth It"
3. **Three identical monarch portraits** in one frame
4. **The stamp press** — "Duly Knighted" in royal purple with gold flecks

### Quote Potential:
- "By the power vested in me by my grandfather, who vested it in himself, I hereby STAMP thee!" - König Klaus
- "IT IS NOT A THEME! It is a BIRTHRIGHT!" - König Klaus
- "Brewed with hops that can trace their lineage back seven generations. The yeast is merely five generations, but we don't discuss that." - Heir Apparent Ale flavor text
- "The Usurper is actually pretty good. Don't tell him I said that." - Royal Cousin
- "Your knighthood is ETERNAL! Return for the anniversary ceremony! There is a SASH!" - König Klaus

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | crown_cask_tileset.png | 1024x512 |
| 2 | crown_cask_landmarks.png | 512x384 |
| 3 | konig_klaus.png | 384x288 |
| 4 | crown_cask_npcs.png | 384x192 |
| 5 | crown_cask_drinks.png | 256x192 |
| 6 | crown_cask_effects.png | 256x128 |
| 7 | crown_cask_ui.png | 256x192 |

**Total Estimated Memory:** ~4 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `crown_cask_tileset.png` (1024x512)
- [ ] `crown_cask_landmarks.png` (512x384)
- [ ] `konig_klaus.png` (384x288)
- [ ] `crown_cask_npcs.png` (384x192)
- [ ] `crown_cask_drinks.png` (256x192)
- [ ] `crown_cask_effects.png` (256x128)
- [ ] `crown_cask_ui.png` (256x192)

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
- **Documentation:** Animation timing reference sheet + ceremony state-flow diagram

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] All three monarch portraits share one recognizable face
- [ ] Klaus's crown crooked in court frames, straightened in ceremony frames
- [ ] Crown-glass silhouette reads as a crown at inventory scale
- [ ] Stamp face and inked result align 1:1 for press animation
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (imperial cosplay, inherited authority) is clear throughout
- [ ] Hidden Usurper interaction has a discoverable visual cue (empty inviting throne)
- [ ] Performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Habsburg/Austrian imperial aesthetics evoked, never named as real places |
| Cultural Specificity | ✅ | Habsburg nostalgia, imperial ceremony, family-recipe dynasty mythology |
| Satirical Targets Appropriate | ✅ | Inherited privilege and imperial cosplay satirized; Klaus is affectionate, not a local stereotype |
| Seedy Underbelly Present | ❌ | Intentionally benign per profile — no vice operation documented beyond the 3 Sovs keepsake-glass upsell and self-appointed authority |
| Gameplay Value Established | ✅ | Brewery Tour stamp, ceremony QTE + dialogue, beer shop with buffs, hidden quest |
| Technical Feasibility | ✅ | Seven sheets, atlas plan, LOD tiers documented |
| Performance Budget | ✅ | 60 FPS default (profile states no budget — flagged), 20 draw calls, 35 MB, 20 particles |
| Accessibility Features | ✅ | Visual cues for all audio events; static motion variants |
| No Crypto Elements | ✅ | None present — pure imperial satire |
| Social Media Integration | ✅ | Coronation kneel, Usurper selfie, identical-portraits moments identified |

**Crown & Cask: Where every drinker is a knight waiting to be dubbed, the scepter pours a solid golden ale, and the only dynasty that matters is seven generations of yeast.**
