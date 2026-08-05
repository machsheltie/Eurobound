# The Quiet Man - Complete PNG Asset Requirements

## 📋 Overview
An underground fight club maintaining, with total commitment, the legal fiction that it is a pub quiz — punches are "emphatic answers," knockouts are "definitive wins," and the crowd chants "TRI-VI-A!" while blood hits sawdust. This document specifies every sprite for the basement beneath a "closed" pub off the Quay of Last Resort, from the discretion-test door to Big Donnacha's 47-question undefeated streak.

**Location ID:** `publandia_seedy_quiet_man_01`
**Theme:** Fight Club with a quiz-night alibi — euphemism as institution, tourist toughness meeting reality
**Zone:** Basement below a "closed" pub off the Quay of Last Resort (Seedy Underbelly)
**Hours:** 21:00-04:00 (when "trivia" happens)
**Primary Function:** Combat challenge venue / Contender-to-Champion progression / Rumor Trading Post / betting crossover with Paddy's Book

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Blood Red | #8B0000 | Accents, fight card, enthusiasm spillage |
| Sawdust Brown | #D2691E | Pit floor, rope, absorption medium |
| Basement Gray | #505050 | Walls, shadows, everything outside the spotlight |
| Spotlight Yellow | #FFD700 | The single pit spotlight, MC station glow |
| Abandoned Green | #2F4F4F | Exterior "closed" pub, damp street |
| Recovery White | #F5F5F5 | Brigid's supplies, bandages, ice |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/quiet_man/
├── environment/
│   ├── closed_pub_exterior.png
│   ├── pit_arena.png
│   └── gallery_backrooms.png
├── npcs/
│   ├── quiet_man_staff.png
│   ├── fighters.png
│   └── crowd.png
├── effects/
│   └── fight_effects.png
└── ui/
    └── quiet_man_ui.png
```

---

## 🚪 Sprite Sheet 1: Closed Pub Exterior
**File:** `closed_pub_exterior.png`
**Dimensions:** 384x256 pixels

### The Deception:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Abandoned Pub Front | (0, 0) | 256x192 | Lights off, boarded charm, plausible deniability |
| Faded Pub Sign | (256, 0) | 128x48 | Original name weathered to illegibility |
| "CLOSED" Sign | (256, 48) | 96x48 | "CLOSED UNTIL FURTHER NOTICE" — permanent |
| Cellar Door Shut | (256, 96) | 64x64 | Street-level, unremarkable |
| Cellar Door Cracked | (320, 96) | 64x64 | The Tell — slight light under the door |
| Light Leak Strip | (256, 160) | 96x16 | Warm glow escaping the frame |
| Quay Street Tile | (0, 192) | 128x64 | Damp cobbles, away from tourist routes |
| Dumpster & Crates | (128, 192) | 128x64 | Alley dressing |
| Muffled-Cheer Ripple | (256, 176) | 64x32 | Visual audio cue — faint sound lines at the door |
| Donal at the Door | (320, 160) | 64x96 | Bouncer stationed, cap low, judging quickly |

### Technical Notes:
- Exterior must read as genuinely skippable — the Tell (light leak + ripple) only renders after the rumor is heard at The Blarney Trap or Paddy's Book
- Donal's exterior sprite doubles as the entry-question interaction node

---

## 🥊 Sprite Sheet 2: The Pit Arena
**File:** `pit_arena.png`
**Dimensions:** 512x512 pixels

### Arena Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sawdust Floor Tile | (0, 0) | 128x128 | Fresh sawdust — absorbs blood, tiles seamlessly |
| Sawdust Floor Stained | (128, 0) | 128x128 | Post-round variant, enthusiasm spillage visible |
| Rope Boundary Straight | (256, 0) | 128x32 | Rough circle segment, tileable |
| Rope Boundary Corner | (256, 32) | 64x64 | Curve segment |
| Rope Post | (320, 32) | 32x64 | Anchor stakes |
| Basement Wall | (0, 128) | 256x128 | Low ceiling, exposed beams, damp stone |
| Ceiling Beams | (256, 96) | 256x64 | Overhead framing, single cable run |
| Spotlight Rig | (256, 160) | 96x96 | The one light that matters |
| Spotlight Pool | (352, 160) | 128x128 | Floor ellipse, Spotlight Yellow falloff |
| Descent Stairs | (0, 256) | 96x192 | Narrow, steep, deliberately uncomfortable |
| Stair Shadow Gradient | (96, 256) | 64x192 | Darkens toward street level — the point of commitment |

### The MC Station (Question Corner):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| MC Podium | (160, 256) | 96x96 | Ciaran's domain — quiz-show veneer on fight announcing |
| Microphone Stand | (256, 288) | 32x64 | Broadcaster prop |
| Question Cards | (288, 288) | 32x32 | Barely used, part of the fiction |
| Category Board | (320, 288) | 96x64 | "GEOGRAPHY / HISTORY / LITERATURE / SCIENCE / SPORTS / SUDDEN DEATH" |
| House Rules Plaque | (416, 288) | 96x64 | Posted, ignored by house |
| Chalk Tally Wall | (160, 352) | 96x96 | 47 marks under "SEAMUS" |
| Beer Crate Seating | (256, 352) | 96x64 | Ringside luxury |
| Champion Wall | (352, 352) | 160x160 | Winners display, one enormous framed photo |
| Sawdust Bucket | (256, 416) | 48x48 | Refill between "rounds" |
| Mop & Bucket | (304, 416) | 48x64 | For the enthusiasm |

### Technical Notes:
- Stained sawdust tile swaps in per-fight via TileMap layer toggle — cartoonish, never graphic (gore-reduction option swaps to plain scuffed tile)
- Spotlight Pool is the only high-brightness element; everything else sits in Basement Gray

---

## 🏥 Sprite Sheet 3: Gallery & Back Rooms
**File:** `gallery_backrooms.png`
**Dimensions:** 512x384 pixels

### The Viewing Gallery (The Stands):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rickety Platform Tier 1 | (0, 0) | 256x96 | Standing-room scaffold, lower level |
| Rickety Platform Tier 2 | (0, 96) | 256x96 | Upper level, worse railings |
| Support Scaffolding | (256, 0) | 64x192 | Load-bearing optimism |
| Betting Corner | (320, 0) | 96x96 | Where wagers move — Paddy's Book connection |
| Gallery Rail | (320, 96) | 128x32 | Lean-and-shout surface |
| Hanging Bulb String | (320, 128) | 128x32 | Dim gallery lighting |

### The Recovery Room (The Medic):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Recovery Cot | (0, 192) | 128x64 | Where losers wake up |
| Supply Shelf | (128, 192) | 96x64 | Ice, bandages, painkillers — pride not stocked |
| Brigid's Station | (224, 192) | 96x96 | Stool, basin, always-ready ice bucket |
| Privacy Curtain | (320, 192) | 64x96 | Half-drawn, no real privacy |
| Fighter Prep Bench | (0, 256) | 128x64 | Pre-bout wraps and doubt |

### The Rumor Trading Post:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sinéad's Table | (128, 256) | 128x96 | Side-area desk, ledger open |
| Notebook Stack | (256, 288) | 48x48 | Everyone's business, indexed |
| Rumor Board | (304, 288) | 112x96 | Pinned scraps — rotating stock, prices chalked |
| Secrets Lockbox | (416, 288) | 64x64 | The 50 Sovs tier lives here |
| Oil Lamp | (416, 192) | 48x64 | Trading post's conspiratorial glow |
| Coin Tin | (464, 192) | 48x48 | Information economy, cash only |

### Technical Notes:
- Betting Corner and Rumor Board are separate Area2D nodes — betting routes to Paddy's Book odds data, rumors to the info-shop inventory
- Gallery platforms hold crowd clumps from Sheet 6; max two clumps per tier on mobile

---

## 🎙️ Sprite Sheet 4: Staff NPCs
**File:** `quiet_man_staff.png`
**Dimensions:** 384x256 pixels

### The Management (64x96 each):
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| Ciaran MC Idle | (0, 0) | 64x96 | Cheap suit, microphone welded to hand |
| Ciaran Announcing A | (64, 0) | 64x96 | Arm skyward — "A DEFINITIVE ANSWER!" |
| Ciaran Announcing B | (128, 0) | 64x96 | Leaning into crowd, milking it |
| Ciaran Announcing C | (192, 0) | 64x96 | Mock-scholarly gesture at Category Board |
| Donal Bouncer | (256, 0) | 64x96 | Former fighter, visible damage, quiet authority |
| Donal Judging | (320, 0) | 64x96 | The 1952 question pose — arms folded |

### Support Staff (64x96 each):
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| Brigid Nurse | (0, 96) | 64x96 | Practical clothes, ice pack in hand |
| Brigid Patching | (64, 96) | 64x96 | Working on a loser: "Hold still." |
| Brigid Head Shake | (128, 96) | 64x96 | The disappointed KO response |
| Sinéad Broker | (192, 96) | 64x96 | Always writing, never sharing her own |
| Sinéad Trading | (256, 96) | 64x96 | Sliding a folded rumor across the table |

### Dialogue Portraits (64x48 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Ciaran Portrait | (0, 192) | 64x48 | Broadcaster grin |
| Donal Portrait | (64, 192) | 64x48 | "That's not it, friend." |
| Brigid Portrait | (128, 192) | 64x48 | Tired competence |
| Sinéad Portrait | (192, 192) | 64x48 | Businesslike, ledger-adjacent |
| Ciaran Portrait Hype | (256, 192) | 64x48 | Full quiz-show voltage |

---

## 🥋 Sprite Sheet 5: Fighters
**File:** `fighters.png`
**Dimensions:** 384x256 pixels

### The Roster:
| Fighter | Position | Size | Description |
|---------|----------|------|-------------|
| "Tourism Bureau" Terry | (0, 0) | 64x96 | Sloppy stance, misplaced enthusiasm — tutorial opponent |
| "The Accountant" Niamh | (64, 0) | 64x96 | Precise guard, calculated: kickboxer in office wear |
| "Quarry" Jimmy | (128, 0) | 64x96 | Brawler bulk, takes hits to give hits |
| "Big" Donnacha O'Malley | (192, 0) | 80x112 | The Champion — complete fighter, 47-0, reads you already |
| Generic Fighter A | (272, 0) | 64x96 | Undercard filler, local |
| Generic Fighter B | (336, 0) | 48x96 | Undercard filler, wiry |

### Fight States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fighter Down | (0, 112) | 96x48 | Knockout pose — "the floor here is very comfortable actually" |
| Recovery Wake | (96, 112) | 64x96 | Coming to on the cot, regret loading |
| Guard Stance Overlay | (160, 112) | 64x96 | Generic combat-ready pose layer |
| Victory Arms | (224, 112) | 64x96 | Winner's raise under the spotlight |
| Champion Belt Worn | (288, 112) | 64x96 | Big Donnacha with the belt — and the player variant after |

### Fighter Portraits (64x48 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Terry Portrait | (0, 208) | 64x48 | "I've done this before! Twice!" |
| Niamh Portrait | (64, 208) | 64x48 | "I've calculated your odds." |
| Jimmy Portrait | (128, 208) | 64x48 | "This is PERSONAL now." |
| Donnacha Portrait | (192, 208) | 64x48 | "You want to be forty-eight?" |

---

## 👥 Sprite Sheet 6: The Crowd
**File:** `crowd.png`
**Dimensions:** 512x192 pixels

### Crowd States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crowd Cheering | (0, 0) | 256x96 | Fists up, mid-"TRI-VI-A!" chant |
| Crowd Booing | (256, 0) | 256x96 | Turned backs, thumbs down — the Boring debuff made visible |
| Crowd Neutral | (0, 96) | 256x96 | Between rounds murmur, bottles clinking |
| Chant Frames 1-2 | (256, 96) | 128x64 | Two 64x64 mouth/arm overlay frames for chant sync |
| Bet Slip Wavers | (384, 96) | 64x64 | Gallery gamblers overlay |
| Bottle Raise Overlay | (448, 96) | 64x64 | Free-drinks-for-the-winner salute |
| Silhouette Row (Front) | (256, 160) | 256x32 | Foreground dark heads framing the pit camera |

### Technical Notes:
- Crowd is three swappable 256x96 base states + overlay frames — never individually animated NPCs
- Crowd Meter value drives base-state swap thresholds (cheer ≥70%, neutral 30-70%, boo <30%)

---

## 💥 Sprite Sheet 7: Fight Effects
**File:** `fight_effects.png`
**Dimensions:** 256x128 pixels

### Combat Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Sawdust Kick 1-3 | (0, 0) | 96x32 | Three 32x32 scuff bursts |
| Impact Stars | (96, 0) | 32x32 | Cartoonish hit feedback — keeps violence unserious |
| Sweat Spray | (128, 0) | 32x32 | Big-swing follow-through |
| Blood Fleck (Cartoon) | (160, 0) | 32x32 | "Enthusiasm spillage" — removed in gore-reduction mode |
| KO Spiral | (192, 0) | 32x32 | Orbiting birds-adjacent spiral for Knocked Senseless |
| Improvised Weapon Glint | (224, 0) | 32x32 | "Science" category pickup flash |

### Atmosphere:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Spotlight Dust | (0, 32) | 64x64 | Motes in the pit beam |
| Cigarette Haze Band | (64, 32) | 128x32 | Grandfathered ventilation, drifting layer |
| Bulb Flicker Frames | (64, 64) | 64x32 | Two 32x32 gallery-bulb states |
| Crowd Roar Ripple | (128, 64) | 64x32 | Radiating sound lines from the stands |
| Chant Text Burst | (192, 32) | 64x32 | "TRI-VI-A!" pop-up lettering |
| Bell Ding Flash | (192, 64) | 32x32 | Round start/end |
| Ice Pack Steam | (224, 64) | 32x32 | Recovery Room detail |
| Money Change Hands | (0, 96) | 64x32 | Betting corner flurry |
| Rumor Whisper Wisp | (64, 96) | 32x32 | Trading post exchange effect |

---

## 🎮 Sprite Sheet 8: UI Elements
**File:** `quiet_man_ui.png`
**Dimensions:** 512x256 pixels

### Fight UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Trivia Question Frame | (0, 0) | 256x128 | Quiz-show-styled fight announcement: category, "contestants," odds |
| Crowd Meter | (256, 0) | 128x32 | Audience engagement bar, chant icon at full |
| Fight Card | (256, 32) | 128x96 | Tonight's bout listing, chalkboard styling |
| Category Icons | (384, 0) | 128x64 | Six 42x32 glyphs: globe, scroll, book, flask, gloves, skull |
| Victory Fanfare Panel | (384, 64) | 128x64 | "CORRECT ANSWER!" win display |
| KO Display | (0, 128) | 128x64 | "DEFINITIVE ANSWER!" knockout announcement |
| Recovery Timer | (128, 128) | 96x32 | Heal time remaining, ice-pack icon |
| Entry Question Prompt | (128, 160) | 128x64 | "Who won the 1952 Best Picture Oscar?" input frame |

### Status & Progression:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Contender Badge | (256, 128) | 48x48 | Three wins, taken seriously |
| Champion Belt Item | (304, 128) | 64x32 | Equipment sprite, gaudy and earned |
| Humbled Icon | (368, 128) | 32x32 | Loss status — respected for trying |
| Knocked Senseless Icon | (400, 128) | 32x32 | KO confusion, spiral motif |
| Fight Ready Icon | (432, 128) | 32x32 | Signed up, waiting |
| Crowd Favorite Icon | (464, 128) | 32x32 | Full-meter buff |
| Rumor Menu | (256, 160) | 160x96 | Trading post interface — rotating stock, price column |
| Rumor Slip Item | (416, 160) | 48x32 | Purchased information, folded |
| Quiz Champion Title Card | (0, 192) | 128x64 | Belt + title unlock splash |

### Technical Notes:
- Trivia Question Frame reuses quiz-show framing for every bout — the fiction is enforced at UI level
- Category icons are shape-distinct for colorblind safety; category never coded by color alone

---

## 🎬 Animation Specifications

### The Entry Ritual:
- **Duration:** 6 seconds (dialogue-paced)
- **Frames:** Donal Judging hold → question prompt → correct: door swing + light flood / wrong: fold-and-turn
- **Trigger:** Interacting with Donal at the cellar door (post-rumor)
- **Purpose:** The discretion test — the location's handshake
- **Audio Sync:** "Who Wants to Be a Millionaire"-style question sting under the prompt; muffled crowd swells when the door opens
- **Performance Optimization:** None needed

### Ciaran Announcement Loop:
- **Duration:** 5 seconds per announcement
- **Frames:** Announcing A → B → C, mic gestures cycling
- **Trigger:** Fight start, round transitions, knockout
- **Purpose:** Quiz-show energy pasted over violence — the core joke, delivered constantly
- **Audio Sync:** Quiz "correct!" chime after every knockout; broadcaster lines on each pose
- **Performance Optimization:** Two-pose cycle on Low LOD

### Crowd Chant:
- **Duration:** 2-second loop while Crowd Meter ≥70%
- **Frames:** Cheering base + Chant Frames 1-2 alternating, Chant Text Burst on beat
- **Trigger:** High crowd meter, exciting moves, fight climax
- **Purpose:** "TRI-VI-A!" over punches — the fiction made audible and visible
- **Audio Sync:** Chant audio locked to overlay frame swaps
- **Performance Optimization:** Text burst only, static crowd on Low LOD

### Knockout Sequence:
- **Duration:** 3 seconds
- **Frames:** Impact Stars → KO Spiral attach → Fighter Down settle → Ciaran announcement
- **Trigger:** Fight-ending blow (either direction)
- **Purpose:** Cartoonish, decisive, never graphic
- **Audio Sync:** Meaty thud → beat of silence → quiz "correct!" chime → crowd roar
- **Performance Optimization:** Spiral becomes static icon

### Recovery Wake-Up:
- **Duration:** 4 seconds
- **Frames:** Black fade-in → Recovery Wake sprite → Brigid Patching → Head Shake (KO loss only)
- **Trigger:** Player defeat
- **Purpose:** Consequence with warmth — Brigid's competence softens the loss loop
- **Audio Sync:** Recovery Room groans ambient; "Hold still" line on patch frame
- **Performance Optimization:** None needed

### Bulb Flicker & Haze:
- **Duration:** Continuous; flicker at random 20-40s intervals
- **Frames:** 2 bulb states; haze band drifts on 12s loop
- **Trigger:** Constant in basement
- **Purpose:** Grandfathered-ventilation atmosphere
- **Audio Sync:** None
- **Performance Optimization:** Haze static, flicker off in reduced-motion mode

---

## ♿ Accessibility Sprite Requirements
**File:** `quiet_man_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Trivia Frame, Bold | (0, 0) | 96x64 | Thick-bordered announcement with enlarged category text |
| Crowd Meter, Bold | (96, 0) | 96x32 | Segmented high-contrast bar with state labels |
| Donal Interaction Outline | (192, 0) | 48x64 | White-on-dark cellar-door hotspot |
| Rumor Menu, Bold | (0, 64) | 96x64 | Heavy dividers, price column enlarged |
| Pit Boundary, Bold | (96, 64) | 96x32 | High-contrast rope ring for fight readability |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bulb, Steady | (192, 64) | 32x32 | Flicker disabled state |
| Haze, Static | (0, 96) | 64x32 | Fixed light-haze band, no drift |
| Crowd, Calm | (64, 96) | 64x48 | Single neutral crowd state, no chant alternation |
| KO, No Spiral | (128, 96) | 32x32 | Static "dazed" icon replacing orbiting spiral |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Punch Thud Burst | (0, 144) | 32x32 | Impact glyph on every landed hit |
| Quiz Chime Icon | (32, 144) | 32x32 | "Correct!" glyph after knockouts |
| Chant Caption | (64, 144) | 64x32 | "TRI-VI-A!" caption bubble locked to chant audio |
| Bell Icon | (128, 144) | 32x32 | Round start/end flash |
| Muffled Cheer Ripple | (160, 144) | 32x32 | Exterior door sound cue (mirrors Sheet 1) |
| Groan Bubble | (192, 144) | 32x32 | Recovery Room ambience cue |

### Colorblind Considerations:
- Fight categories carry six distinct icon shapes — never color-coded alone
- Crowd Meter uses segmentation + labels, not red/green fill alone
- Gore-reduction mode is independent of colorblind settings; stained sawdust never carries gameplay meaning
- Entry prompt, rumor rows, fight card and all hotspots meet the 44px minimum touch target

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import)
- **Fallback:** PNG high quality for portraits and the Trivia Question Frame

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| quietman_environment | exterior, pit_arena, gallery_backrooms | 1024x1024 |
| quietman_characters | staff, fighters, crowd | 1024x512 |
| quietman_fx_ui | fight_effects, ui | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full crowd states + overlays, all fight particles, haze drift, flicker |
| Medium | Two crowd states, halved particles, static haze |
| Low | Single crowd silhouette row, impact stars only, no haze, no flicker |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 15 per frame
- **Memory Footprint:** 40 MB maximum
- **Particle Limit:** 16 (sawdust + sweat + dust combined)

### Performance Notes:
- Crowd is three base quads + overlays — never per-NPC animation
- Recovery Room and Rumor Post load as sub-scenes on demand
- Fight camera frames the pit only; gallery tiers cull outside combat

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Uses the base game combat system with Pit environment modifiers; category rules (grapple unlock, weapon pickups, boxing-only) applied as combat-scene flags
- CPUParticles2D (not GPU) for sawdust kicks, sweat, spotlight dust; bulb flicker via alpha toggle timer, disabled in reduced-motion mode
- Crowd Meter is a float driving crowd base-state swap + Crowd Favorite / Boring buff application mid-fight
- Area2D nodes: Donal entry (password gate, requires `heard_quiet_man_rumor`), fight sign-up (Bravado 30+ check), Betting Corner, Rumor Board, Recovery cot
- State tracking per `quiet_man_state` (fights_won, fights_lost, contender, champion_defeated, rumors_bought[], humbled_active, knocked_senseless_until)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Entry question prompt | Millionaire-style question sting | Under the full prompt display |
| Cellar door opens | Muffled crowd → full roar | Crossfade over the 1s door swing |
| Landed hits | Meaty thuds | Per Impact Stars frame |
| Knockout | Thud → silence beat → quiz "correct!" chime | Chime exactly 0.8s after the fall |
| Chant overlay frames | "TRI-VI-A!" crowd chant | Locked to frame swaps |
| Round transitions | Bell ding | On Bell Ding Flash |
| Brigid Patching | "Hold still. This'll hurt..." | On patch frame |
| Rumor purchase | Coin tin + whisper wisp | On slip handoff |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Quiz Champion | Big Donnacha (all states), Champion Belt, Quiz Champion Title Card, Chalk Tally Wall | Boss fight unlocks at 5 wins; tally gains a 48th mark either way |
| Information Economy | Rumor Menu, Rumor Board, Sinéad Trading, Rumor Slip | Rotating stock feeds main-quest hints (Craic Baron's Weakness, Stoutworks Secret) |
| The Undercard | Fight Card, Ciaran states, Generic Fighters A/B | Scheduling quest — player arranges bouts for Ciaran |
| Country vs. City | Jimmy, Niamh, faction crowd reactions | Rivalry quest; crowd base state biases by chosen side |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Paddy's Book | Betting Corner, shared fighter roster sprites, bet slip overlay | Fighters appear at both; Quiet Man bouts bettable at Paddy's |
| The Blarney Trap | Rumor source (Declan, night bartender); Backroom connects to Rumor Trading Post | Rumor flag `heard_quiet_man_rumor` enables the Tell |
| The Stoutworks Brewery | "Stoutworks Secret" rumor slip hints at dungeon hidden room | Rumor purchase sets Stoutworks secret-room flag |
| The Craic Tax | "Rival Trio Location" rumor; rivals may appear in the gallery | Rumor-driven encounter placement |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "One spotlight, one lie everybody agreed to — a quiz night rendered in blood red and sawdust"
- **Color Mood:** Basement Gray swallowing everything except the Spotlight Yellow pit; Blood Red used sparingly so it always lands
- **Lighting:** Single dramatic pit spotlight, dim bulb strings in the gallery, oil-lamp conspiratorial glow at the Rumor Post
- **Texture:** Damp stone, fresh-then-stained sawdust, rickety scaffold timber, one immaculate microphone

### Environmental Storytelling:
- The Category Board and barely-used Question Cards maintain the fiction in props
- Chalk Tally Wall: 47 marks under "SEAMUS" — the boss fight advertised before anyone says a word
- House Rules Plaque posted and visibly ignored; the one real rule ("Literature: no groin shots") honored in fight logic
- Abandoned above, alive below: the exterior's whole job is to look like nothing

### Character Integration Notes:
- Ciaran never breaks the bit — every pose is quiz-show, never fight-promoter
- Big Donnacha at 80x112 must dwarf the roster without cartoon exaggeration; stillness is his menace
- Brigid's frames carry the location's only genuine care — play her straight
- The crowd is a single organism: three moods, one voice

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Entry Question** - A bouncer asking the 1952 Best Picture Oscar winner outside a "closed" pub
2. **"TRI-VI-A!" Chant Burst** - The chant text popping over a mid-air haymaker
3. **The Category Board** - "GEOGRAPHY: ground fighting allowed" played completely straight
4. **The Chalk Tally** - 47 marks under SEAMUS, one space suspiciously blank
5. **The KO Announcement** - "A DEFINITIVE ANSWER!" over a flattened tourist
6. **Recovery Room Wake-Up** - Brigid's disappointed head shake, ice at the ready

### Quote Potential:
- "It's Not Fighting If You Call It Trivia"
- "A man of culture. Down the stairs. Mind your step and your teeth."
- "Every fight is just a question with a physical answer. Who's tougher? Let's find out!"
- "Forty-seven questions answered correctly. You want to be forty-eight?"
- "You've got heart. Terrible technique, but heart."
- "I'm doing this for the CONTENT— why is he punching me while I'm TALKING?"

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | closed_pub_exterior.png | 384x256 |
| 2 | pit_arena.png | 512x512 |
| 3 | gallery_backrooms.png | 512x384 |
| 4 | quiet_man_staff.png | 384x256 |
| 5 | fighters.png | 384x256 |
| 6 | crowd.png | 512x192 |
| 7 | fight_effects.png | 256x128 |
| 8 | quiet_man_ui.png | 512x256 |

**Total Estimated Memory:** ~18 MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `closed_pub_exterior.png` (384x256)
- [ ] `pit_arena.png` (512x512)
- [ ] `gallery_backrooms.png` (512x384)
- [ ] `quiet_man_staff.png` (384x256)
- [ ] `fighters.png` (384x256)
- [ ] `crowd.png` (512x192)
- [ ] `fight_effects.png` (256x128)
- [ ] `quiet_man_ui.png` (512x256)
- [ ] `quiet_man_accessibility.png` (256x192, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (stained/clean sawdust and blood flecks on separate layers for the gore-reduction toggle)
- **Documentation:** Animation timing reference sheet (entry ritual, chant loop, KO sequence, recovery wake-up)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Blood Red #8B0000, Sawdust Brown #D2691E, Basement Gray #505050, Spotlight Yellow #FFD700)
- [ ] Category Board and House Rules Plaque readable on examine — the fiction lives in the text
- [ ] Chalk Tally Wall's 47 marks countable at examine zoom
- [ ] Violence reads cartoonish at every frame; gore-reduction layer swap verified
- [ ] Accessibility visual alternatives included for all audio cues (thuds, chime, chant, bell, groans)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (euphemism as institution) is clear throughout all assets
- [ ] Easter eggs discoverable: the Tell light-leak, the one honored rule, blank 48th tally space, Sinéad's own unshared notebook
- [ ] Performance optimized (crowd quads, 16-particle cap, on-demand back rooms)
- [ ] Touch zone sizing considered (44px minimum — entry prompt, rumor rows, fight card compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (icon-shaped categories, segmented meter)
- [ ] Social media viral potential maximized (chant burst framing, KO announcement composition)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia, Quay of Last Resort only ("Quarry" Jimmy keeps the profile's county gag generic) |
| Cultural Specificity | ✅ | Irish fighting reputation subverted via The Quiet Man (1952) film irony |
| Satirical Targets Appropriate | ✅ | Violence tourism and tourist overconfidence — locals go easy on tourists, the joke lands on the bros |
| Seedy Underbelly Present | ✅ | Unlicensed fighting, rumor economy, betting crossover |
| Gameplay Value Established | ✅ | Full combat venue, Contender/Champion progression, information shop |
| Technical Feasibility | ✅ | Reuses base combat system; 8 sheets, mobile optimization documented |
| Performance Budget | ✅ | 60 FPS, 15 draw calls, 40MB |
| Accessibility Features | ✅ | Visual cues for all audio, calm-crowd/steady-bulb variants, gore reduction |
| No Crypto Elements | ✅ | Absent from source and spec |
| Social Media Integration | ✅ | Six viral moments identified, quote bank sourced from profile |

**The Quiet Man delivers organized violence wearing a pub quiz's name tag, and every asset keeps the bit alive: the question cards nobody reads, the category board nobody questions, the chant that turns a beating into a tiebreaker. The player descends the stairs a tourist and wakes up on Brigid's cot a contestant.**

**"And THAT is how you answer a question about HISTORY! With your FISTS!"**
