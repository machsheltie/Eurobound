# Trinity of Pints - Complete PNG Asset Requirements

## 📋 Overview
A pub cosplaying as a prestigious university — plastic ivy, stock-photo alumni, faux-Latin mottos, and Dean Declan Murphy grading your pint-finishing technique with the gravitas of a tenure committee. This document specifies every sprite for Publandia's School of Liquid Arts, where drinking challenges are "courses," failure is "academic probation," and the diploma is fake but printed that morning with genuine ceremony.

**Location ID:** `publandia_pub_trinity_pints_01`
**Theme:** Gimmick-pub tourism and academic pretension — tourists who want to feel CULTURED while getting hammered
**Zone:** Adjacent to Cobblestone Market Street (the "academic quarter")
**Hours:** 11:00-01:00 ("class hours")
**Primary Function:** Drinking challenge venue / course-and-GPA system / graduation ceremony / Brewery Passport stamp stop

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Academic Green | #355E3B | Banners, robes, exterior trim |
| Scholarly Gold | #CFB53B | Crests, medallions, faux-Latin lettering |
| Old Parchment | #F5DEB3 | Diplomas, walls, course catalog |
| Wood Brown | #8B4513 | Long tables, bookshelves, podium |
| Plastic Ivy Green | #4CBB17 | The Amazon-sourced ivy, slightly too bright |
| Navy Seal Blue | #191970 | Trinity stamp ink, department flags |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/trinity_of_pints/
├── environment/
│   ├── trinity_exterior.png
│   ├── great_hall.png
│   └── campus_rooms.png
├── npcs/
│   ├── trinity_faculty.png
│   └── trinity_students.png
├── objects/
│   └── academic_props.png
├── effects/
│   └── (packed into trinity_effects_ui.png)
└── ui/
    └── trinity_effects_ui.png
```

---

## 🏛️ Sprite Sheet 1: Exterior — The Faux Georgian Facade
**File:** `trinity_exterior.png`
**Dimensions:** 384x384 pixels

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Georgian Facade | (0, 0) | 256x256 | Trinity College mimicry, but... off. Proportions 5% wrong on purpose |
| Ornate Iron Gates | (256, 0) | 128x160 | "TRINITY OF PINTS" worked into faux-Latin scroll ironwork |
| Plastic Ivy Overlay | (0, 256) | 128x64 | Slightly-too-bright ivy, visible zip ties on examine |
| Main Sign | (128, 256) | 128x48 | "TRINITY OF PINTS — Est. MCMXCVII" (1997, not as old as it looks) |
| Motto Banner | (128, 304) | 128x32 | "In Vino Veritas, In Cervisia Felicitas" |
| Enrollment Sign | (256, 160) | 128x48 | "NOW ACCEPTING STUDENTS — No Prerequisites Required" |
| Course Board | (256, 208) | 96x96 | Daily "lecture" schedule, chalk hand |
| Warning Plaque (Small) | (352, 208) | 32x32 | "Academic standards may vary" |
| Lamppost & Bell Housing | (256, 304) | 64x80 | The recorded "academic bells" speaker, visible if examined |
| Cobble Approach Tile | (320, 304) | 64x64 | Street tile toward Market Street |
| Drunk Student Silhouette | (0, 320) | 64x64 | Gravitas undermined — one visible through the window |

### Technical Notes:
- The facade's deliberate wrongness (window spacing, column count) is a background gag — subtle, not broken
- Bell Housing examine point reveals the speaker; bells play at random via audio timer

---

## 🍺 Sprite Sheet 2: The Great Hall
**File:** `great_hall.png`
**Dimensions:** 512x384 pixels

### Main Pub Area:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Great Hall Base | (0, 0) | 256x192 | Hogwarts/Oxford dining-hall pastiche with visible taps |
| Long Table Section | (0, 192) | 192x64 | Wooden tables, tileable end-to-end |
| Head Table | (192, 192) | 128x64 | Where "Professors" preside in party-store robes |
| Stained Glass Window (LED) | (256, 0) | 96x128 | Faux stained glass, pint-glass saint motif |
| Department Banners | (352, 0) | 128x128 | Four 32x128 flags: BEER, SHOT, GAME, SONG departments |
| Challenge Stage | (256, 128) | 128x64 | Scattered drinking-challenge platform |
| Chalkboard Formulas | (384, 128) | 128x64 | "Drinking game rules" as equations |
| Enrollment Desk | (0, 256) | 128x96 | Registration: pay tuition, receive laminated Student ID |
| Trophy Case | (128, 256) | 96x96 | Empty bottles and stained diplomas, proudly lit |
| Fake Alumni Portraits | (224, 256) | 128x64 | Stock photos in robes, gilt frames |
| Course Catalog Stand | (352, 256) | 64x96 | The drinking challenge menu, lectern-mounted |
| Candle Sconce (LED) | (416, 256) | 32x64 | Faux candlelight fixture |
| Beer Tap Row | (320, 320) | 128x64 | The truth behind the gravitas |
| Academic Bell (Prop) | (448, 256) | 64x64 | Decorative — the real one is a speaker |

### Technical Notes:
- Department banners are individually placeable — lecture halls reuse them
- Fake Alumni Portraits are an examine chain; each gives one absurd stock-photo bio line

---

## 📚 Sprite Sheet 3: Campus Rooms — Library, Lecture Hall & Quad
**File:** `campus_rooms.png`
**Dimensions:** 512x384 pixels

### The Library (Back Room):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Library Base | (0, 0) | 192x160 | Quieter drinking area for "studying" |
| Hollow Bookshelf Wall | (192, 0) | 128x128 | IKEA prop books, spine titles increasingly absurd |
| Flask Compartment Open | (320, 0) | 64x64 | Hidden flask inside a fake book — discoverable |
| Research Materials Shelf | (320, 64) | 64x64 | Cocktail recipe books, heavily annotated |
| Reading Lamp & Armchair | (384, 0) | 128x128 | Day-drinking with pretense station |

### The Lecture Hall (Challenge Room):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lecture Hall Base | (0, 160) | 192x128 | Stadium seating around central challenge area |
| Challenge Floor Circle | (192, 128) | 96x96 | Where courses are "examined" |
| Rules Chalkboard | (288, 128) | 96x64 | Course-specific "formulas" |
| Stadium Bench Tier | (288, 192) | 128x32 | Tileable seating row |
| Darts Setup | (384, 128) | 64x96 | GAME 215: Applied Darts Theory station |
| Blind Taste Rig | (416, 224) | 96x64 | BEER 201 flight with covered labels |

### The Quad (Beer Garden):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Quad Lawn Base | (0, 288) | 192x96 | Outdoor seating, "lawn games" |
| Graduation Podium | (192, 288) | 96x96 | Ceremony focal point, crest-fronted |
| Graduation Backdrop | (288, 288) | 128x96 | Fake banners + ivy wall + Trinity crest — selfie spot |
| Lawn Game Set | (416, 288) | 96x48 | Drinking-game ring toss |
| String Lights | (416, 336) | 96x48 | Quad evening dressing |
| Confetti Ground Layer | (192, 224) | 96x64 | Post-ceremony scatter overlay |

### Technical Notes:
- Graduation ceremony assembles: Podium + Backdrop + confetti burst (UI sheet) + Dean Graduating pose
- Flask Compartment is a repeatable examine gag with escalating flavor text

---

## 🎓 Sprite Sheet 4: Faculty
**File:** `trinity_faculty.png`
**Dimensions:** 384x256 pixels

### The Administration (64x96 each):
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| Dean Declan Idle | (0, 0) | 64x96 | Full academic regalia — robe, cap, medallion, perpetual seriousness |
| Dean Lecturing A | (64, 0) | 64x96 | Finger raised, thesis-defense energy |
| Dean Lecturing B | (128, 0) | 64x96 | Gesturing at chalkboard formulas |
| Dean Grading | (192, 0) | 64x96 | Clipboard scrutiny of your pint technique |
| Dean Conferring | (256, 0) | 64x96 | Diploma extended, ceremony mode |
| Dean Toasting | (320, 0) | 64x96 | Commencement toast raise |

### The Faculty (64x96 each):
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| Prof. Siobhan (Spirits) | (0, 96) | 64x96 | Tweed, reading glasses, glass perpetually in hand |
| Prof. Cian (Games) | (64, 96) | 64x96 | Sports casual under academic robe, darts at the ready |
| Prof. Aisling (Music) | (128, 96) | 64x96 | Folk aesthetic, bodhrán slung |
| Siobhan Nosing Glass | (192, 96) | 64x96 | "Smell first. Now taste." demonstration pose |
| Cian Throwing | (256, 96) | 64x96 | State champion '08 form |
| Aisling Playing | (320, 96) | 64x96 | Bodhrán rhythm-game conductor |

### Dialogue Portraits (64x48 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Dean Portrait | (0, 192) | 64x48 | Scholarly gravitas |
| Dean Portrait (Private) | (64, 192) | 64x48 | The rare mask-slip — twelve adjunct years behind the eyes |
| Siobhan Portrait | (128, 192) | 64x48 | Warm but exacting |
| Cian Portrait | (192, 192) | 64x48 | Competitive encouragement |
| Aisling Portrait | (256, 192) | 64x48 | "Beautiful! Terrible, but beautiful!" |
| Medallion Detail | (320, 192) | 32x32 | Dean's chain of office close-up |
| Party-Store Tag | (352, 192) | 32x32 | Still attached to a faculty robe — examine gag |

---

## 🧑‍🎓 Sprite Sheet 5: Student NPCs
**File:** `trinity_students.png`
**Dimensions:** 384x192 pixels

### The Student Body:
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| The Repeat Student | (0, 0) | 64x96 | Fifth attempt at BEER 101, commitment issues |
| The Overachiever | (64, 0) | 64x96 | Taking notes, asking about extra credit, double-major ambitions |
| The Legacy Admission | (128, 0) | 64x96 | Expecting preferential treatment, getting none |
| The Study Group | (192, 0) | 192x96 | Bachelorette party, matching shirts: "SARAH'S GETTING MARRIED" |

### Student Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Notebook & Pen | (0, 96) | 32x32 | Overachiever prop |
| Matching Shirt Detail | (32, 96) | 48x32 | Study Group merch close-up |
| Failed Exam Slip | (80, 96) | 32x32 | Repeat Student's F, laminated by now |
| Coordinated Cheer Overlay | (112, 96) | 96x48 | Study Group arms-up frame |
| Student Portraits Strip | (208, 96) | 160x48 | Repeat / Overachiever / Legacy / Group rep, 40x48 each |
| Drunk "Academic" Gesture | (0, 128) | 64x64 | Student attempting scholarly discussion, swaying |

---

## 📜 Sprite Sheet 6: Academic Props & Items
**File:** `academic_props.png`
**Dimensions:** 256x256 pixels

### Enrollment & Graduation:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Student ID Card | (0, 0) | 64x48 | Laminated that minute, your name in Comic Serif |
| Diploma (Rolled) | (64, 0) | 48x48 | Ribbon-tied scroll |
| Diploma (Open) | (112, 0) | 96x64 | "BACHELOR OF BEVERAGE SCIENCES (B.B.S.)" full certificate text |
| Graduation Cap (Prop) | (208, 0) | 48x48 | Mortarboard, selfie-ready |
| Academic Robe (Wearable) | (0, 48) | 64x96 | Player equip prop for ceremony/selfie |
| Valedictorian Medal | (64, 64) | 48x48 | Highest GPA of the night |
| Course Credit Chit | (112, 64) | 32x32 | Per-course completion token |
| Freshman Beanie | (144, 64) | 32x32 | Enrollment starter gag |

### The Bar & Courses:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Branded Pint Glass ("Textbook") | (176, 64) | 32x48 | Free with tuition |
| Academic Amber Bottle | (208, 48) | 32x64 | Irish Red with honey notes, Stoutworks contract brew |
| Academic Amber Pint | (240, 48) | 16x48 | Poured, deceptively scholarly |
| Whiskey Trio (SHOT 110) | (0, 144) | 72x32 | Three 24x32 identification shots |
| Beer Flight (BEER 201) | (72, 144) | 96x32 | Five blind-test glasses |
| Guinness Pour Stages | (168, 144) | 88x32 | BEER 301 — settle, surge, sacrament (three 24x32 + head detail) |
| Bodhrán & Tipper | (0, 176) | 48x48 | SONG 220 rhythm instrument |
| Dart Set | (48, 176) | 32x32 | GAME 215 equipment |
| Thesis Gauntlet Tray | (80, 176) | 96x48 | THESIS 401 multi-stage: drink, game, toast, song props combined |
| Stamp: Trinity of Pints | (176, 176) | 64x64 | Square academic seal — open book + pint glass, laurel border, "Cum Laude in Lager," deep navy ink |
| Hollow Book (Closed/Open) | (0, 224) | 64x32 | Two 32x32 states for library gag |
| Latin Motto Scroll | (64, 224) | 64x32 | Mostly incorrect Latin, framed anyway |
| GPA Report Card | (128, 224) | 48x32 | Gentleman's C rendered official |
| Tuition Receipt | (176, 240) | 32x16 | €10 — "covers tuition, materials, and distinguished faculty" |
| Diploma Print Stack | (208, 224) | 48x32 | This morning's batch, ink drying |

### Technical Notes:
- Diploma (Open) text must be legible at examine zoom — the full B.B.S. certificate is the payoff
- Stamp matches Brewery Passport ink spec: Navy Seal Blue #191970

---

## 🎮 Sprite Sheet 7: Effects & UI
**File:** `trinity_effects_ui.png`
**Dimensions:** 512x256 pixels

### Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Graduation Confetti Burst | (0, 0) | 96x96 | Ceremony payoff particles |
| Candle Flicker Frames 1-2 | (96, 0) | 64x32 | Two 32x32 LED-candle states |
| Dust Motes | (96, 32) | 32x32 | Library atmosphere |
| Cork Pop Burst | (128, 32) | 32x32 | Celebration accent |
| Stained Glass Light Pool | (160, 0) | 96x64 | Colored floor cast |
| Scholar's Focus Sparkle | (256, 0) | 32x32 | +INT buff activation |
| Bell Toll Ripple | (288, 0) | 32x32 | Random "academic bells" visual |

### Course & Ceremony UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Course Catalog Menu | (0, 96) | 160x160 | Freshman → Senior Thesis listing, prerequisite lines |
| GPA Tracker | (160, 96) | 96x48 | Academic standing dial: Dean's List → Expulsion Risk |
| Grade Stamps A/B/C/F | (256, 96) | 128x32 | Four 32x32 result seals |
| Course Complete Badge | (256, 128) | 48x48 | Credit earned |
| Graduation Ceremony Banner | (160, 144) | 96x48 | "COMMENCEMENT" header panel |
| Balance Check Meter | (304, 128) | 64x32 | Podium walk intoxication wobble gauge |
| Valedictorian Splash | (320, 0) | 128x64 | Highest-GPA-of-the-night celebration card |
| Academic Probation Notice | (320, 64) | 96x32 | Remedial coursework required |
| Scholar's Focus Icon | (368, 128) | 32x32 | +3 INT, 30 min |
| Pretentious Debuff Icon | (400, 128) | 32x32 | Dialogue becomes insufferable |
| Enrolled Status Icon | (432, 128) | 32x32 | Part of the bit |
| Graduate Status Icon | (464, 128) | 32x32 | Permanent alumni standing |
| Selfie Frame: Academic | (160, 192) | 96x64 | Podium + backdrop overlay, robe/cap/diploma prop slots |
| Alumni Discount Tag | (256, 192) | 64x32 | €5 graduate tuition |
| Toast-Off Prompt | (320, 192) | 96x32 | PUB 115 crowd-approval meter |
| Rhythm Bar (SONG 220) | (416, 192) | 96x32 | Note-hit track for drinking songs |
| Dean's List Crest | (416, 160) | 48x32 | 20% discount, VIP seating marker |

### Technical Notes:
- GPA Tracker is a dial with four labeled bands — standing changes are also announced via grade stamps
- Balance Check Meter wobble amplitude scales with intoxication stat during the podium walk

---

## 🎬 Animation Specifications

### Dean's Grading Ritual:
- **Duration:** 3 seconds
- **Frames:** Grading pose → clipboard mark → grade stamp slam onto UI
- **Trigger:** Any course completion
- **Purpose:** Every pint judged like a thesis defense — the core joke, systematized
- **Audio Sync:** Pen scratch, then official stamp thunk on the seal frame
- **Mobile Optimization:** None needed

### Graduation Ceremony:
- **Duration:** 12 seconds, choreographed
- **Frames:** Dean Conferring at podium → player balance-check walk (wobble meter live) → diploma handoff → Dean Toasting → Confetti Burst → selfie prompt
- **Trigger:** Senior Thesis complete or credit threshold reached
- **Purpose:** The full pomp — everyone graduates eventually, everyone feels something anyway
- **Audio Sync:** "Pomp and Circumstance" parody swells from podium step; cork pop + stamp on diploma handoff; crowd cheer on confetti
- **Mobile Optimization:** Confetti count halved; ceremony skippable after first viewing

### The Balance Check Walk:
- **Duration:** 4 seconds within ceremony
- **Frames:** Player walk cycle with wobble offset driven by intoxication
- **Trigger:** Ceremony step 2
- **Purpose:** The GPA was drinking all along
- **Audio Sync:** Crowd "oooh" on heavy wobbles
- **Mobile Optimization:** Wobble becomes UI meter only in reduced-motion mode

### Candle & Stained Glass Ambience:
- **Duration:** Continuous; candle 0.8s flicker alternation, light pool 20s slow drift
- **Trigger:** Constant in Great Hall and Library
- **Purpose:** Faux-collegiate mood lighting doing its LED best
- **Audio Sync:** None
- **Mobile Optimization:** Static candles, fixed light pool on Low LOD

### Random Academic Bells:
- **Duration:** 2-second toll ripple
- **Frames:** Bell Toll Ripple x3 fading
- **Trigger:** Random 90-180s timer ("plays randomly" per the recorded-bells gag)
- **Purpose:** Marks "course times" with zero actual schedule
- **Audio Sync:** Recorded bell audio — deliberately slightly canned
- **Mobile Optimization:** Visual ripple only if audio muted; off in reduced-motion

### Rhythm Course (SONG 220):
- **Duration:** Course-length; note track scrolls at 120 BPM
- **Frames:** Aisling Playing pose + Rhythm Bar note hits
- **Trigger:** SONG 220 / Traditional Music Studies enrollment
- **Purpose:** 80% accuracy target, 40% lyric retention guaranteed
- **Audio Sync:** Note-hit flashes locked to bodhrán beats
- **Mobile Optimization:** Note density reduced on Low LOD

---

## ♿ Accessibility Sprite Requirements
**File:** `trinity_accessibility.png` (supplemental sheet — delivered alongside the 7 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Course Catalog, Bold | (0, 0) | 96x96 | Thick-bordered listing, enlarged course codes and tier dividers |
| GPA Tracker, Bold | (96, 0) | 96x48 | Four labeled bands with pattern fills |
| Grade Stamps, Bold | (96, 48) | 128x32 | A/B/C/F with heavy outlines and letterforms |
| Enrollment Desk Outline | (0, 96) | 64x64 | White-on-dark interaction hotspot |
| Podium Outline | (64, 96) | 64x64 | Ceremony trigger highlight |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Candles, Steady | (128, 96) | 32x32 | Flicker-free LED state |
| Confetti, Static | (160, 96) | 64x64 | Single settled-confetti frame replacing burst |
| Wobble, Meter-Only | (224, 96) | 32x32 | Balance conveyed by gauge, camera/character steady |
| Light Pool, Fixed | (0, 160) | 48x32 | Non-drifting stained glass cast |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bell Toll Icon | (48, 160) | 32x32 | Random bells visualized |
| Stamp Thunk Star | (80, 160) | 32x32 | Grade/diploma stamp impact |
| Cork Pop Burst Icon | (112, 160) | 32x32 | Celebration cue |
| Pomp Parody Note | (144, 160) | 32x32 | Ceremony music cue glyph |
| Crowd Cheer Ripple | (176, 160) | 32x32 | Toast-off and ceremony approval |
| Bodhrán Beat Pulse | (208, 160) | 32x32 | Rhythm course beat indicator (independent of audio) |

### Colorblind Considerations:
- GPA bands use pattern fills + text labels, never green-to-red gradient alone
- Grade stamps are letterforms first; seal color is decorative
- Rhythm Bar note hits flash with shape change (circle → star), not color swap alone
- Course rows, enrollment desk, podium, and selfie prompt all meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (diploma text and stamp at ASTC 4x4 — certificate legibility is the joke)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for Dean portraits, diploma, and stamp

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| trinity_environment | exterior, great_hall, campus_rooms | 1024x1024 |
| trinity_characters | faculty, students | 512x512 |
| trinity_props_ui | academic_props, effects_ui | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full Great Hall crowd, confetti burst, candle flicker, drifting light pools |
| Medium | Simplified crowd (Study Group + 2), halved confetti, static light pools |
| Low | Static portraits, no confetti particles (settled frame), faculty + 1 student per room |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 15 per frame
- **Memory Footprint:** 36 MB maximum
- **Particle Limit:** 20 (confetti peak only; ambient runs ≤8)

### Performance Notes:
- Great Hall crowd simplified per profile: static portraits, banner flags unanimated
- Library, Lecture Hall, and Quad load as sub-scenes on demand
- Ceremony is a timeline animation — no physics confetti

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Room graph: Great Hall hub → Library / Lecture Hall / Quad sub-scenes, simple fades
- CPUParticles2D (not GPU) for confetti and dust; candle flicker via 2-frame alpha toggle, disabled in reduced-motion mode
- Course system: each course is a minigame scene returning a grade (A/B/C/F) → GPA float → standing band; Senior Thesis chains four minigame stages
- Ceremony timeline (AnimationPlayer): podium, balance check (reads intoxication stat), diploma, toast, confetti, selfie prompt, stamp application (requires Bottle Opener Keychain flag)
- State tracking per `trinity_state` (enrolled, courses_passed[], gpa, standing, graduated, valedictorian, alumni_discount, stamp_acquired, academic_amber_unlocked)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Grade stamp slam | Official stamp thunk | On seal frame |
| Graduation podium step | "Pomp and Circumstance" parody | Swell starts on Dean Conferring |
| Diploma handoff | Stamp + cork pop combination | Both on handoff frame — the profile's "Diploma Sound" |
| Confetti burst | Crowd cheer | On burst frame |
| Random bells | Recorded toll (slightly canned) | With Bell Toll Ripple |
| SONG 220 note hits | Bodhrán beats | Locked to Rhythm Bar flashes |
| Course completion | Completion fanfare | On Course Complete Badge pop |
| Valedictorian award | Extended fanfare + staff fawning lines | On splash card |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Brewery Tour Sidequest (stamp) | Stamp: Trinity of Pints, Dean Conferring, ceremony sequence | Stamp applied during graduation by Dean Declan; requires Bottle Opener Keychain from The Blarney Trap |
| Senior Thesis (THESIS 401) | Thesis Gauntlet Tray, all four course stations, Graduation Ceremony assets | Multi-stage gauntlet: drink, game, toast, song → graduation trigger |
| Valedictorian Run | GPA Tracker, Valedictorian Splash + Medal, Dean's List Crest | Highest GPA of the session; bonus Bravado + free drinks |
| Academic Probation Arc | Probation Notice, Repeat Student NPC, remedial course flow | Sub-1.5 GPA path; public shame, retakes, redemption |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Blarney Trap | Bottle Opener Keychain gates the stamp; Academic Amber sold there post-graduation; Seamus recommends Trinity | Item/flag link + cross-dialogue |
| The Stoutworks Brewery | Academic Amber contract-brewed there (bottle sprite shared style); academic NPCs reference Stoutworks beer | Item lineage; stamp synergy toward Publandia Legendary Hangover |
| Cobblestone Market Street | Visible from the main street — facade draws the "cultural" crowd | Standard street transition |
| The Confidence Man | "Exam confidence" tonic pitch before courses | Buff carries into course minigames |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Oxford by way of a party store — every prestigious surface exactly one inspection away from collapse"
- **Color Mood:** Academic Green and Scholarly Gold striving for gravitas; Plastic Ivy Green and LED warmth betraying the 1997 of it all
- **Lighting:** Faux candlelight, stained-glass pools, graduation-day brightness in the Quad
- **Texture:** Real wood tables under fake books, laminate over parchment, ivy with visible zip ties

### Environmental Storytelling:
- Est. MCMXCVII carved grandly — 1997 pretending to be 1697
- The trophy case of empty bottles and stained diplomas is the curriculum's honest résumé
- Hollow books, flask compartments, and this morning's diploma print stack: the whole institution disassembles on examine
- "Academic standards may vary" — the smallest sign tells the biggest truth

### Character Integration Notes:
- Dean Declan never breaks character in any sprite; the Private portrait is the sole crack, and it's earned
- Faculty poses must play their departments straight — Siobhan noses a €4 whiskey like it's a first edition
- Students carry the reaction comedy; the Study Group is one choreographed organism
- Bradley's genuine emotion at a fake graduation is the tonal target: absurd AND touching

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Graduation Selfie** - Robe, mortarboard, diploma, fake ivy backdrop — indistinguishable from a real one at thumbnail size
2. **The Diploma Close-Up** - "BACHELOR OF BEVERAGE SCIENCES (B.B.S.)" in full certificate typography
3. **The Trophy Case** - Empty bottles and stained diplomas, museum-lit
4. **The Balance Check Walk** - Wobble meter maxed on the podium approach
5. **The Course Board** - "BEER 301: Advanced Stout Analysis" chalked under today's date
6. **The Party-Store Tag** - Still hanging off a professor's robe

### Quote Potential:
- "Cum Laude in Lager"
- "A UNIVERSITY for DRINKING? This is the greatest country on EARTH."
- "I'm putting this on my LINKEDIN. Bachelor of Beverage Sciences. HR will be IMPRESSED."
- "My doctoral thesis was on the semiotics of Irish identity in post-colonial literature. Now I grade pint-finishing technique. I've never been happier."
- "The diploma is fake. The education is real. Think about it."
- "I'm... proud? I didn't expect to feel genuine emotion at a fake graduation."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | trinity_exterior.png | 384x384 |
| 2 | great_hall.png | 512x384 |
| 3 | campus_rooms.png | 512x384 |
| 4 | trinity_faculty.png | 384x256 |
| 5 | trinity_students.png | 384x192 |
| 6 | academic_props.png | 256x256 |
| 7 | trinity_effects_ui.png | 512x256 |

**Total Estimated Memory:** ~16 MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `trinity_exterior.png` (384x384)
- [ ] `great_hall.png` (512x384)
- [ ] `campus_rooms.png` (512x384)
- [ ] `trinity_faculty.png` (384x256)
- [ ] `trinity_students.png` (384x192)
- [ ] `academic_props.png` (256x256)
- [ ] `trinity_effects_ui.png` (512x256)
- [ ] `trinity_accessibility.png` (256x192, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (diploma text, course board chalk, and banner flags on separate layers — courses and mottos are designed to rotate)
- **Documentation:** Animation timing reference sheet (grading 3s, ceremony 12s timeline, bells 90-180s randomizer) + selfie frame composition guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Academic Green #355E3B, Scholarly Gold #CFB53B, Old Parchment #F5DEB3, Wood Brown #8B4513)
- [ ] Diploma certificate text fully legible at examine zoom
- [ ] Stamp matches passport spec: square seal, laurel border, deep navy ink
- [ ] The facade's "off" proportions read as subtly wrong, never as an art error
- [ ] Accessibility visual alternatives included for all audio cues (bells, stamps, cork, pomp parody, bodhrán)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (drinking dressed as scholarship) is clear throughout all assets
- [ ] Easter eggs discoverable: flask compartment, party-store tag, bell speaker, diploma print stack, zip-tied ivy
- [ ] Mobile performance optimized (static crowd portraits, timeline ceremony, sub-scene rooms)
- [ ] Touch zone sizing considered (44px minimum — course rows, enrollment desk, podium compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (patterned GPA bands, letterform grades, shape-change rhythm hits)
- [ ] Social media viral potential maximized (graduation selfie composition, diploma framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only; Trinity College satirized as "Trinity of Pints" without naming Dublin in-game |
| Cultural Specificity | ✅ | Irish literary-heritage commodification, Trinity College tourism |
| Satirical Targets Appropriate | ✅ | Gimmick pubs, tourist pretension, "college experience" industry — never education itself; locals avoid the place |
| Seedy Underbelly Present | ✅ | €10 "tuition" cover charge for a themed pub; exploiting the desire to feel cultured |
| Gameplay Value Established | ✅ | Ten-course challenge catalog, GPA system, graduation ceremony, stamp stop, Academic Amber unlock |
| Technical Feasibility | ✅ | Hub-and-rooms structure, timeline ceremony, 7 sheets, mobile optimization documented |
| Mobile Performance Budget | ✅ | 60 FPS, 15 draw calls, 36MB |
| Accessibility Features | ✅ | Visual cues for all audio, steady-candle/static-confetti/meter-only variants, labeled GPA bands |
| No Crypto Elements | ✅ | Absent from source and spec |
| Social Media Integration | ✅ | Six viral moments identified, quote bank sourced from profile |

**Trinity of Pints delivers the complete counterfeit college experience: enrollment, coursework, probation, and a graduation that moves people despite everyone knowing better. Every asset commits to the bit as hard as Dean Declan does — because the diploma is fake, the education is real, and the selfie is forever.**

**"In Cervisia Felicitas."**
