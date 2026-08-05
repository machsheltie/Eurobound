# The Moderato Pub - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for The Moderato Pub — the Viennese-style beer hall on MusikGasse where musicians have argued about tempo since 1848, nothing has ever been resolved, and nobody wants it to be. It satirizes musical pedantry: subjective preference defended as objective truth, at volume, nightly. Critically, this is the ONE Sinfonia location that isn't exploiting the player — the safe haven, base of operations, save point, and quest hub where the bros are adopted as lovable idiots (and the regulars quietly bet on their opinions). Every asset must radiate warmth: the visual promise that here, and only here, Sinfonia will not chew you up.

**Location ID:** `sinfonia_musikgasse_moderato_pub_01`
**Theme:** Musical pedantry as endless holy war — pub culture gatekeeping and "authentic experience" tourism, all rendered harmless and warm
**Zone:** MusikGasse, Street Performer District
**Hours:** 11:00–03:00 (musicians keep flexible hours; the tempo debate itself never stops)
**Primary Function:** Base of operations / safe zone — save point, full rest (backroom couchsurfing), party management, quest hub (bulletin board + 4 quest givers), pub shop (drinks/food), Tempo Debate mini-game, brewery tour stamp ("Win a Tempo Debate"), Regular status progression

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Beer Amber | #FFBF00 | Beer, taps, warm highlights, stamp ink base |
| Wood Brown | #5D432C | Tables, bar, wainscoting, bass-clef table legs |
| Cream Wall | #FFF8DC | Interior walls, exterior plaster |
| Musical Black | #1A1A1A | Metronomes, notation, chalkboard grounds, signage text |
| Copper Accent | #B87333 | Bottle opener, stamp accents, tap hardware, lantern trim |
| Hop Green | #7BA05B | Beer garden vines, window box foliage |
| Warm Lamplight | #FFE4A1 | Window glow, candle light, hearth, string lights |
| Chalk White | #F5F5F5 | Chalkboard writing, foam, sheet music paper |
| Red Ink | #C0392B | Sheet-music corrections, "TRAITOR!" accents, Allegro trim |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/moderato_pub/
├── environment/
│   ├── moderato_pub_exterior.png
│   └── moderato_pub_tileset.png
├── npcs/
│   ├── herr_takt_bartender.png
│   ├── tempo_faction_leaders.png
│   └── moderato_pub_npcs.png
├── objects/
│   └── moderato_pub_items.png
├── effects/
│   └── moderato_pub_effects.png
└── ui/
    └── moderato_pub_ui.png
```

---

## 🏠 Sprite Sheet 1: Exterior & Beer Garden
**File:** `moderato_pub_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #FFF8DC (Cream Wall), #5D432C (Wood Brown), #7BA05B (Hop Green), #FFE4A1 (Warm Lamplight)

### Façade & Beer Garden Backdrops:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pub Façade | (0, 0) | 512x384 | Corner wirtshaus on MusikGasse: painted trim, warm windows, wooden gable |
| Beer Garden Backdrop | (512, 0) | 384x384 | Courtyard: flagstones, trellis, hop vines, string lights strung overhead |
| Window Box Day | (896, 0) | 64x32 | Flowers in bloom, cream sill |
| Window Box Evening | (896, 32) | 64x32 | Same flowers, lamplight tint |
| Painted Main Sign | (896, 64) | 96x64 | Beer stein + musical notes, hand-painted swing sign |
| Tempo Chalkboard | (896, 128) | 64x96 | A-frame board: "Tonight's Tempo: CONTESTED" in chalk |
| Est. 1847 Sign | (896, 224) | 96x32 | "The Moderato — Est. 1847 — Tempo Wars Since 1848" brass plate |

### Doors, Windows & Street:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Front Door Closed | (0, 384) | 64x96 | Heavy wooden door, brass handle |
| Front Door Open | (64, 384) | 64x96 | Warm light and argument noise spilling out |
| Window Glow Overlay | (128, 384) | 64x96 | Warm interior light for evening façade |
| Gesturing Silhouettes A | (192, 384) | 64x96 | Patron shadows in window, arms mid-debate |
| Gesturing Silhouettes B | (256, 384) | 64x96 | Second frame — arms swapped, one stein raised |
| String Lights Lit | (320, 384) | 256x32 | Beer garden strand, warm bulbs |
| String Lights Static | (320, 416) | 256x32 | Reduced-motion variant, no twinkle |
| Hop Vine Segment | (576, 384) | 64x96 | Climbing vine, cone clusters |
| Hop Vine Corner | (640, 384) | 64x96 | Trellis corner piece |
| Exterior Lantern | (704, 384) | 32x96 | Copper-trimmed wall lantern |
| Cobblestone Tile A | (736, 384) | 32x32 | MusikGasse street tile |
| Cobblestone Tile B | (768, 384) | 32x32 | Worn variant (street performer pitch) |
| Cobblestone Tile C | (800, 384) | 32x32 | Drain/edge variant |
| Garden Table | (832, 384) | 64x64 | Wooden courtyard table with stein rings |
| Garden Bench | (896, 384) | 64x32 | Matching bench, initials carved as note heads |

### Technical Notes:
- Façade rendered for day AND evening via Window Glow / lantern overlays — no duplicate building sprite
- Silhouette frames alternate at slow interval so the pub visibly argues from the street
- Beer garden backdrop is a single pre-rendered plate; string lights are the only animated exterior layer

---

## 🍺 Sprite Sheet 2: Interior Tileset & Décor
**File:** `moderato_pub_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #5D432C (Wood Brown), #FFF8DC (Cream Wall), #FFBF00 (Beer Amber), #1A1A1A (Musical Black), #C0392B (Red Ink)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wood Plank | (0, 0) | 32x32 | Main hall flooring, warm grain |
| Wood Plank Worn | (32, 0) | 32x32 | High-traffic path to the bar |
| Hearth Stone | (64, 0) | 32x32 | Around the fireplace |
| Backroom Floor | (96, 0) | 32x32 | Plainer boards, cot area |
| Snug Rug | (128, 0) | 32x32 | Deep red rug tile, quieter tone |
| Garden Flagstone | (160, 0) | 32x32 | Beer garden walk-on tile |
| Beer Spill Overlay | (192, 0) | 32x32 | Amber stain decal (debate casualty) |
| Stage Boards | (224, 0) | 32x32 | Scuffed performance flooring |

### Wall Tiles (32x64 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cream Plaster | (0, 32) | 32x64 | Standard interior wall |
| Plaster w/ Photo Shadows | (32, 32) | 32x64 | Ghost rectangles where memorabilia rotated |
| Wood Wainscot | (64, 32) | 32x64 | Lower paneling, main hall |
| Snug Paneling | (96, 32) | 32x64 | Full-height dark wood, cozy |
| Backroom Wall | (128, 32) | 32x64 | Bare plaster, gig posters |
| Window Wall Segment | (160, 32) | 32x64 | Interior-side window with curtain |

### Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Communal Table | (0, 96) | 128x48 | Long Austrian-style table, stein rings |
| Communal Bench | (128, 96) | 128x24 | Matching bench, seats a faction |
| Bass-Clef Table Leg | (256, 96) | 16x48 | Carved leg detail — the signature gag, readable in close-up |
| Snug Round Table | (272, 96) | 48x48 | Smaller, for quiet quest conversations |
| Chair | (320, 96) | 32x48 | Simple wirtshaus chair |
| Stage Platform | (352, 96) | 160x64 | Raised stage for performances and arguments about performances |
| Spotlight Rig | (512, 96) | 64x32 | Stage lighting bar |
| Bar Counter Section | (576, 96) | 128x64 | Wood bar with brass rail, tileable |
| Tap Array | (704, 96) | 96x48 | Five taps, handles shaped like note durations (whole to sixteenth) |
| Back-Bar Metronome Shelf | (800, 96) | 128x64 | Shelf of metronomes, every one set to a different tempo |
| Cot Made | (928, 96) | 64x32 | Backroom cot, folded blanket |
| Cot Rumpled | (928, 128) | 64x32 | Recently slept in (full rest state) |

### Décor Gags:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Baton Dartboard | (0, 160) | 48x48 | Dartboard with conductor batons stuck in it, bullseye = fermata |
| Memorabilia Wall A | (96, 160) | 128x96 | Signed photos of "famous" musicians nobody's heard of |
| Memorabilia Wall B | (224, 160) | 128x96 | More unknowns, one frame hung pointedly crooked |
| Tempo of the Day Chalkboard | (352, 160) | 64x96 | Interior board; today's tempo (matches nobody's preference) |
| Corrected Sheet Music | (416, 160) | 48x64 | Framed score covered in red-ink corrections from rival patrons |
| No Allegro After Midnight Sign | (464, 160) | 64x32 | Brass sign, visibly ignored |
| Instrument Stein Shelf | (528, 160) | 96x32 | Display row of instrument-shaped steins |
| Metronome Andante | (624, 160) | 32x48 | Pendulum left, slow tick |
| Metronome Moderato | (656, 160) | 32x48 | Pendulum center |
| Metronome Allegro | (688, 160) | 32x48 | Pendulum right, fast tick |
| Fireplace Hearth | (720, 160) | 96x96 | Main hall hearth, ember glow |
| Bulletin Board Prop | (816, 160) | 96x128 | Physical quest board, pinned notices |
| Upright Piano | (912, 160) | 96x96 | House-band corner piano, stein on lid |

### Doors, Windows & Room Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Snug Door | (0, 288) | 32x64 | To the quiet side room |
| Backroom Door | (32, 288) | 32x64 | "Regulars Only" (unlocks with status) |
| Garden Door | (64, 288) | 32x64 | To the courtyard |
| Front Door Interior | (96, 288) | 32x64 | Inside face of entrance |
| Window Day | (128, 288) | 32x64 | Natural light state |
| Window Night | (160, 288) | 32x64 | MusikGasse lamplight state |
| Table Candle | (192, 288) | 16x32 | Evening table light |
| Wall Lantern | (208, 288) | 16x32 | Copper interior lantern |
| Coat Rack w/ Cases | (224, 288) | 32x64 | Instrument cases hung like coats |
| Keg Stack | (256, 288) | 64x64 | Behind-bar barrels, chalk tempo markings |
| Snug Armchair | (320, 288) | 48x48 | Worn, beloved |
| Snug Fireplace | (368, 288) | 64x64 | Smaller hearth, fewer opinions per square meter |
| Mic Stand | (432, 288) | 16x48 | Stage prop (Underground Karaoke League intel) |
| Accordion Prop | (448, 288) | 32x32 | Kurt's, visibly missing parts |
| Tuba Prop | (480, 288) | 32x48 | Street performer's, leaning on stage |

### Technical Notes:
- Tileset covers all four rooms (main hall, snug, beer garden interior edge, backroom) — no separate room sheets
- Metronome trio are the only constantly animated tileset elements; each ticks at its own rate (deliberate polyrhythm)
- Cot Made → Cot Rumpled is a static swap on rest, zero runtime cost

---

## 🎩 Sprite Sheet 3: Herr Takt (Bartender)
**File:** `herr_takt_bartender.png`
**Dimensions:** 512x288 pixels
**Color Palette:** #5D432C (Vest Brown), #FFF8DC (Shirt Cream), #B87333 (Copper), #1A1A1A (Mustache/Earring)

### Bar Service States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle | (0, 0) | 48x96 | Sturdy build, towel over shoulder, patiently amused |
| Pour Frame 1 | (48, 0) | 48x96 | Stein under tap, handle pulled |
| Pour Frame 2 | (96, 0) | 48x96 | Amber stream flowing, perfect angle |
| Pour Frame 3 | (144, 0) | 48x96 | Foam settled, admiring the head |
| Stein Slide | (192, 0) | 48x96 | Sending a stein down the bar |
| Glass Polish A | (240, 0) | 48x96 | Idle loop, polishing |
| Glass Polish B | (288, 0) | 48x96 | Polish continues, eyebrow raised at debate |
| Listening Amused | (336, 0) | 48x96 | Leaning on bar, secretly has no opinion |
| Save-Point Nod | (384, 0) | 48x96 | Calm nod to player — save confirmed |

### Mediating, Stamp & Morning States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mediating Frame 1 | (0, 96) | 48x96 | Palms down toward Allegro table |
| Mediating Frame 2 | (48, 96) | 48x96 | Palms down toward Adagio table |
| Mediating Frame 3 | (96, 96) | 48x96 | Both palms down, eyes closed, breathing |
| Stamp Ceremony 1 | (144, 96) | 48x96 | Producing the stamp with gravity |
| Stamp Ceremony 2 | (192, 96) | 48x96 | Stamp raised, metronome ticking |
| Stamp Ceremony 3 | (240, 96) | 48x96 | Stamp lands — "Welcome to the debate, forever." |
| Stamp Speech Pose | (288, 96) | 48x96 | Mid-speech: "You probably changed no minds! But you PARTICIPATED!" |
| Coffee Delivery 1 | (336, 96) | 48x96 | Morning: carrying coffee toward backroom |
| Coffee Delivery 2 | (384, 96) | 48x96 | Offering the cup, knowing smile |

### Social States & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Morning Check-In | (0, 192) | 48x96 | Leaning into backroom doorway with coffee pot |
| Regular Greeting | (48, 192) | 48x96 | Remembers your order — small salute |
| Round Announcement | (96, 192) | 48x96 | Arms wide: "Another round for the Allegro table! And the Adagio table!" |
| Metronome Earring Detail | (144, 192) | 16x16 | Close-up: tiny metronome earring, pendulum visible — dialogue portrait accent |
| Stamp Tool | (160, 192) | 24x24 | Brewery stamp, copper and bronze |
| Coffee Tray | (184, 192) | 32x24 | Pot + cup, morning service |
| Trophy Stein | (216, 192) | 24x32 | Temporary debate-winner stein (selfie prop) |

### Technical Notes:
- Mustache is impressive and load-bearing to the silhouette — must read at 48x96
- Metronome earring detail overlays the idle sprite in dialogue close-ups; its tiny pendulum is the only part of Herr Takt that ever picks a tempo
- Save-Point Nod pairs with the save sparkle effect (Sheet 7) — Herr Takt IS the save point's human face

---

## 🎭 Sprite Sheet 4: Faction Leaders
**File:** `tempo_faction_leaders.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #C0392B (Allegro Red trim), #1A1A1A (Adagio Black), #FFBF00 (Moderato Amber), #FFF8DC (Cream)

### Frau Schnell — Allegro Leader (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle (Vibrating) | (0, 0) | 48x96 | Never fully still — heel tapping double-time |
| Rapid Gesture 1 | (48, 0) | 48x96 | Arms up, mid-torrent of words |
| Rapid Gesture 2 | (96, 0) | 48x96 | Chopping hand, other arm swinging |
| Rapid Gesture 3 | (144, 0) | 48x96 | Both hands blurring, leaning over table |
| "TRAITOR!" Point | (192, 0) | 48x96 | Full-extension accusatory finger |
| Speed Drinking | (240, 0) | 48x96 | Stein vertical, done in one |
| Debate Victory | (288, 0) | 48x96 | Fist pumped, already arguing next topic |
| Motion Blur Overlay | (336, 0) | 48x96 | Optional speed-smear layered on gestures |

### Herr Langsam — Adagio Leader (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle (Statuesque) | (0, 96) | 48x96 | Utterly composed, eyes half-closed |
| Slow Gesture 1 | (48, 96) | 48x96 | One arm beginning to rise, glacially |
| Slow Gesture 2 | (96, 96) | 48x96 | Arm at apex, single finger extended |
| Slow Gesture 3 | (144, 96) | 48x96 | Arm descending — the point has been made |
| Mid-Pause Contemplation | (192, 96) | 48x96 | Frozen between words, room waits |
| Glacial Sip | (240, 96) | 48x96 | Stein tilted one degree |
| "...disappointing..." | (288, 96) | 48x96 | Slow head shake, profound sorrow |
| Pocket Watch Check | (336, 96) | 48x96 | Checking the time, in no hurry to read it |

### Die Mitte — Moderato Mediator (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Exhausted Idle | (0, 192) | 48x96 | Perpetually tired eyes, hopeful posture anyway |
| Pleading 1 | (48, 192) | 48x96 | Hands clasped: "Can't we agree that SOME pieces..." |
| Pleading 2 | (96, 192) | 48x96 | Hands open to both tables — no one agrees |
| Head in Hands | (144, 192) | 48x96 | Defeat, elbows on table |
| Tears of Joy | (192, 192) | 48x96 | "FINALLY! Someone who UNDERSTANDS!" — Lord Pilsner variant trigger |
| Grateful Round-Buyer | (240, 192) | 48x96 | Buying the wise abstainer a drink |
| Table Collapse | (288, 192) | 48x96 | Face down on communal table, 3 AM state |

### Faction Emblems (colorblind-safe shapes, 32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Allegro Emblem | (0, 288) | 32x32 | Double eighth-note "wings" on upward arrow — shape-coded, not color-coded |
| Adagio Emblem | (32, 288) | 32x32 | Long whole-note bar on horizontal band |
| Moderato Emblem | (64, 288) | 32x32 | Balanced quarter note on level scale |
| Presto Emblem | (96, 288) | 32x32 | Jagged sixteenth-note run, lightning silhouette |
| Lento Emblem | (128, 288) | 32x32 | Drooping fermata over resting note |

### Technical Notes:
- Frau Schnell animates at the sheet's fastest rate, Herr Langsam at its slowest — their frame timing IS the joke (see Animation Specifications)
- Die Mitte's Tears of Joy is a scripted one-shot tied to the bros' "medium tempo" dialogue beat
- Emblems appear on clothing, flags (Sheet 8), and debate UI so faction identity never relies on color alone

---

## 🎤 Sprite Sheet 5: Quest Givers, Performers & Patrons
**File:** `moderato_pub_npcs.png`
**Dimensions:** 1024x384 pixels
**Color Palette:** Varied street-musician wear over #5D432C / #FFF8DC base tones

### Quest Givers (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kurt Idle | (0, 0) | 48x96 | Accordion strapped on, one bellows fold visibly torn |
| Kurt Playing 1 | (48, 0) | 48x96 | Bellows extended, wheezing note |
| Kurt Playing 2 | (96, 0) | 48x96 | Bellows compressed, pained expression |
| Kurt Despair | (144, 0) | 48x96 | Holding broken part: "Specific parts! From SPECIFIC shops!" |
| Kurt Quest Gesture | (192, 0) | 48x96 | Pointing toward MusikGasse, list in hand |
| Bruckmann Idle | (240, 0) | 48x96 | Retired maestro, cane, immaculate old coat |
| Bruckmann Conducting 1 | (288, 0) | 48x96 | Cane raised as baton, conducting a memory |
| Bruckmann Conducting 2 | (336, 0) | 48x96 | Downbeat — thirty years of authority in one gesture |
| Bruckmann Intel Lean | (384, 0) | 48x96 | Conspiratorial: "I trained Vice von Strauss. I know his... flaws." |
| Die Stimme Idle | (432, 0) | 48x96 | Scarf-shadowed face, corner seat, untouched drink |
| Die Stimme Beckon | (480, 0) | 48x96 | Two fingers, minimal motion |
| Die Stimme Point | (528, 0) | 48x96 | "First, you must PROVE you can sing." |
| Die Stimme Vanish | (576, 0) | 48x96 | Half-turned toward the snug, already leaving |
| Tourist Slumped | (624, 0) | 48x96 | Exhausted Tourist: dead-eyed over a Lento Lager |
| Tourist Map Fumble | (672, 0) | 48x96 | Map unfolding wrong in every direction |
| Tourist Plea | (720, 0) | 48x96 | "Does anything in this city make SENSE?" |
| Tourist Relief | (768, 0) | 48x96 | Quest complete — first genuine smile in days |

### Street Performers & House Band (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Violinist Idle | (0, 96) | 48x96 | Street Performer 1: violin lowered, scanning for a pitch |
| Violinist Playing 1 | (48, 96) | 48x96 | Bow up-stroke, eyes closed |
| Violinist Playing 2 | (96, 96) | 48x96 | Bow down-stroke, transported |
| Violinist Hat Pass | (144, 96) | 48x96 | Hat extended, hopeful |
| Tubist Idle | (192, 96) | 48x96 | Street Performer 2: tuba resting on hip |
| Tubist Oompah 1 | (240, 96) | 48x96 | Cheeks inflated, full commitment |
| Tubist Oompah 2 | (288, 96) | 48x96 | Release, brass bell gleam |
| Tubist Winded | (336, 96) | 48x96 | Bent over, tuba as support |
| House Pianist | (384, 96) | 48x96 | Seated at upright, playing whatever tempo starts the least fights |

### Faction Patrons (48x96 unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Allegro Patron A Idle | (0, 192) | 48x96 | Emblem armband, foot tapping fast |
| Allegro Patron A Gesture 1 | (48, 192) | 48x96 | Debate frame: fist pounds table |
| Allegro Patron A Gesture 2 | (96, 192) | 48x96 | Debate frame: leaping up from bench |
| Allegro Patron B Idle | (144, 192) | 48x96 | Second body type, same fervor |
| Allegro Patron B Gesture | (192, 192) | 48x96 | Stein raised mid-shout |
| Adagio Patron A Idle | (240, 192) | 48x96 | Emblem sash, monumental stillness |
| Adagio Patron A Gesture 1 | (288, 192) | 48x96 | Debate frame: slow palm raised for silence |
| Adagio Patron A Gesture 2 | (336, 192) | 48x96 | Debate frame: measured single nod |
| Adagio Patron B Idle | (384, 192) | 48x96 | Second body type, eyes closed in patience |
| Adagio Patron B Gesture | (432, 192) | 48x96 | Deliberate finger wag, one per sentence |
| Presto Extremist | (480, 192) | 48x96 | Jittering constantly, banned-from-competitions energy |
| Lento Purist | (528, 192) | 48x96 | So still it's arguably a prop; blinks once per scene |
| Sleeping Musician | (576, 192) | 96x48 | Horizontal on cot, instrument cuddled |
| Passed-Out Patron | (672, 192) | 96x48 | Face down on communal table, stein upright and guarded |
| Toast Cluster | (768, 192) | 128x96 | Three patrons, steins meeting overhead — clink moment |

### Crowd & Scene Strips (96x64 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gasping Crowd A | (0, 288) | 96x64 | Pre-rendered crowd row, collective dramatic gasp |
| Gasping Crowd B | (96, 288) | 96x64 | Second frame — hands to mouths, one monocle mid-drop |
| Betting Regulars | (192, 288) | 96x64 | Two locals whispering, coins on table — betting on the bros' opinions |
| Morning Breakfast Patrons | (288, 288) | 96x64 | Bleary survivors, coffee, debate already resumed |

### Technical Notes:
- Faction patrons ship with idle + debate gesture frames; background crowd uses the pre-rendered Gasping Crowd strips per profile mobile spec
- Betting Regulars sprite is the pub's single sly edge — keep it warm, not sinister; the coins are small change
- Die Stimme is always rendered one shade darker than ambient lighting, never fully lit

---

## 🍻 Sprite Sheet 6: Drinks, Food & Items
**File:** `moderato_pub_items.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFBF00 (Beer Amber), #B87333 (Copper), #FFF8DC (Cream), #F5F5F5 (Foam)

### Drinks Menu (32x48 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Moderato Märzen | (0, 0) | 32x48 | Balanced amber, medium foam — "The compromise beer" |
| Allegro Ale | (32, 0) | 32x48 | Pale, lively bubbles racing upward |
| Adagio Stout | (64, 0) | 32x48 | Near-black, foam settling in geological time |
| Presto Pilsner | (96, 0) | 32x48 | Overfizzing, foam escaping — "Dangerously fast" |
| Lento Lager | (128, 0) | 32x48 | Flat, still, possibly not fermented yet |
| The Fermata | (160, 0) | 32x48 | Golden with fermata symbol etched in the glass |
| Tempo Tantrum | (192, 0) | 32x48 | Signature amber ale, perfectly balanced pour |
| Tempo Tantrum Unlocked Glow | (224, 0) | 32x48 | Post-stamp menu variant with amber aura |
| Trophy Stein | (256, 0) | 32x48 | Debate-winner's temporary trophy |
| Tuba Stein | (288, 0) | 32x48 | Instrument-shaped stein: drink from the bell |
| Violin Stein | (320, 0) | 32x48 | F-hole handle detail |
| Trumpet Stein | (352, 0) | 32x48 | Three-valve lid |
| Empty Stein | (384, 0) | 32x48 | Post-debate state, foam rings |

### Food Menu:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tempo Schnitzel | (0, 48) | 48x32 | Golden schnitzel, lemon — "Served at YOUR pace" |
| Allegro Wurst | (48, 48) | 48x32 | Speed sausage, motion-line garnish |
| Adagio Apfelstrudel | (96, 48) | 48x32 | Powdered sugar, meant to be savored |
| Metronome Pretzels | (144, 48) | 32x32 | Pretzels twisted into metronome silhouettes |
| Fermata Feast | (176, 48) | 64x48 | Full platter — schnitzel, wurst, strudel, pretzels |
| Regular's Breakfast | (240, 48) | 64x48 | Morning spread with coffee (couchsurfing wake-up) |

### Bottle Opener & Quest Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bottle Opener Static | (0, 96) | 32x48 | Aged bronze metronome, opener as pendulum arm |
| Opener Pendulum Left | (32, 96) | 32x48 | Pendulum swung left (idle hang animation) |
| Opener Pendulum Center | (64, 96) | 32x48 | Pendulum at rest |
| Opener Pendulum Right | (96, 96) | 32x48 | Pendulum swung right |
| Inscription Detail | (128, 96) | 48x16 | "Tempo Is Everything" engraving close-up |
| Golden Mic | (176, 96) | 32x48 | Karaoke championship reward, +5 Charm gleam |
| Baton Dart | (208, 96) | 24x8 | Single conductor baton, dart-ready |
| Baton Bundle | (240, 96) | 32x32 | Three batons, dartboard ammo |
| Morning Coffee Mug | (272, 96) | 24x24 | Bradley's abstention fuel |
| Accordion Parts | (296, 96) | 48x32 | Bellows fold + reed block (Kurt's Instrument Repair fetch items) |

### Metronome Collection & Bar Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Metronome Largo | (0, 144) | 24x40 | Slowest of the collection |
| Metronome Adagio | (24, 144) | 24x40 | Slow |
| Metronome Moderato | (48, 144) | 24x40 | The house tempo |
| Metronome Allegro | (72, 144) | 24x40 | Fast |
| Metronome Presto | (96, 144) | 24x40 | Blur-fast, slightly scorched |
| Pendulum Left Overlay | (120, 144) | 24x40 | Shared pendulum frame for collection animation |
| Pendulum Center Overlay | (144, 144) | 24x40 | Shared center frame |
| Pendulum Right Overlay | (168, 144) | 24x40 | Shared right frame |
| Food Chalkboard Menu | (192, 144) | 64x96 | Wall menu with prices in chalk, corrections in other chalk |
| Note-Duration Tap Handles | (256, 144) | 96x32 | Detail strip of the five tap handles (whole note → sixteenth) |

### Technical Notes:
- Metronome collection animates via three shared pendulum overlays at five different speeds — one sprite set, five tempos
- Bottle opener pendulum swing plays only in inventory inspection ("actually swings slightly when hanging")
- All six drinks must be distinguishable in silhouette/foam behavior, not hue alone (colorblind rule)

---

## ✨ Sprite Sheet 7: Effects & Particles
**File:** `moderato_pub_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #F5F5F5 (Foam/Chalk), #FFE4A1 (Lamplight), #FFBF00 (Amber), #1A1A1A (Notation)

### Bar & Ambient Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pour Stream 1 | (0, 0) | 16x32 | Amber stream leaving tap |
| Pour Stream 2 | (16, 0) | 16x32 | Full flow, slight splash |
| Pour Stream 3 | (32, 0) | 16x32 | Tapering off |
| Foam Rise A | (48, 0) | 32x32 | Head forming in stein |
| Foam Rise B | (80, 0) | 32x32 | Head settled, one drip |
| Toast Clink Spark | (112, 0) | 32x32 | Star burst where steins meet |
| Dart Thunk Star | (144, 0) | 32x32 | Impact burst on dartboard |
| Baton In Flight A | (176, 0) | 32x16 | Spinning baton, frame 1 |
| Baton In Flight B | (176, 16) | 32x16 | Spinning baton, frame 2 |
| Kitchen Steam 1 | (208, 0) | 16x32 | Rising from pass-through |
| Kitchen Steam 2 | (224, 0) | 16x32 | Dispersing |
| Kitchen Steam 3 | (240, 0) | 16x32 | Fading |
| Candle Flicker 1 | (256, 0) | 16x24 | Flame lean left |
| Candle Flicker 2 | (272, 0) | 16x24 | Flame upright |
| Candle Flicker 3 | (288, 0) | 16x24 | Flame lean right |
| Dust Motes | (304, 0) | 64x64 | Window-beam particles, day scenes |
| Floating Notes | (368, 0) | 48x48 | Gentle eighth notes from house band |
| Angry Note Burst | (416, 0) | 48x48 | Jagged clashing notes over debate table |
| Polka Victory Confetti | (464, 0) | 48x48 | Triumphant burst — debate won |

### Debate, Rest & Character Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tick Pulse Ring A | (0, 64) | 32x32 | Expanding ring off a metronome tick |
| Tick Pulse Ring B | (32, 64) | 32x32 | Ring dissipating |
| Debate Stinger Flash | (64, 64) | 48x32 | Musical stinger visual — staff lines flare on point scored |
| Dramatic Gasp Lines | (112, 64) | 32x32 | Shock lines over gasping crowd |
| Die Mitte Sweat Drop | (144, 64) | 16x16 | Mediation under pressure |
| Sleep Zzz | (160, 64) | 24x24 | Backroom rest indicator |
| Dream Swirl | (192, 64) | 64x64 | Musical Dreams sequence — notes orbiting a sleeping bro |
| Wake-Up Shimmer | (256, 64) | 64x32 | Gentle strings visual: soft light ripple at morning |
| Stage Spotlight Cone | (320, 64) | 64x96 | Performance/argument illumination |
| Hearth Glow | (384, 64) | 64x64 | Warm radial fireplace light |
| String Light Twinkle A | (448, 64) | 32x32 | Garden bulb bright phase |
| String Light Twinkle B | (480, 64) | 32x32 | Garden bulb dim phase |

### Stamp, Save & Status Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp Ink Splash 1 | (0, 160) | 48x48 | Impact ring, amber ink |
| Stamp Ink Splash 2 | (48, 160) | 48x48 | Copper flecks scatter |
| Stamp Ink Splash 3 | (96, 160) | 48x48 | Settled stamp glow |
| Save Sparkle A | (144, 160) | 32x32 | Save-point twinkle, metronome-shaped glint |
| Save Sparkle B | (176, 160) | 32x32 | Second frame |
| Auto-Save Swirl | (208, 160) | 32x32 | Entry auto-save indicator |
| Argument Cloud | (240, 160) | 64x48 | Scuffle-style cloud with clefs and fists |
| Frau Schnell Speed Lines | (304, 160) | 48x48 | Horizontal velocity streaks |
| Herr Langsam Slow Trail | (352, 160) | 48x48 | Afterimage echoes of one deliberate gesture |
| Free Drink Sparkle | (400, 160) | 32x32 | Reward glint on a comped stein |

### Technical Notes:
- Tick pulse rings double as the visual audio cue for every metronome — one ring per audible tick, always
- Angry Note Burst and Floating Notes are mutually exclusive per table: a table argues or enjoys music, never both
- Stamp ink splash sequence locks to the three-tick stamp animation (Sheet 8 + Animation Specifications)

---

## 🖥️ Sprite Sheet 8: UI, Debate Interface & Brewery Tour
**File:** `moderato_pub_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #5D432C (Frame Brown), #FFBF00 (Amber), #F5F5F5 (Chalk Text), #1A1A1A (Notation)

### Tempo Debate Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Debate Frame | (0, 0) | 256x160 | Main interface: topic banner ("Should Für Elise be Andante or Moderato?"), response area, staff-line borders |
| Allegro Position Button | (256, 0) | 96x48 | Choice button with Allegro wing emblem (≥44px touch zone) |
| Adagio Position Button | (256, 48) | 96x48 | Choice button with whole-note-bar emblem |
| Moderato Position Button | (256, 96) | 96x48 | Choice button with balanced-note emblem |
| Abstain Button | (352, 0) | 96x48 | Rest-symbol emblem — abstaining is respected |
| Ridiculous Position Button | (352, 48) | 96x48 | Upside-down clef emblem — biggest laugh path |
| Point Scored Banner | (352, 96) | 96x48 | Stinger banner sliding in on a won exchange |
| Reaction Portrait: Approval | (448, 0) | 48x48 | Faction face frame — nodding warmth |
| Reaction Portrait: Outrage | (448, 48) | 48x48 | "TRAITOR!" red-ink flare |
| Reaction Portrait: Laughter | (448, 96) | 48x48 | Everyone-buys-you-a-drink face |

### Quest Hub & Faction UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bulletin Board UI | (0, 160) | 192x192 | Quest hub screen: cork texture, pinned mission notes, string connections |
| Quest Note: Karaoke League | (192, 160) | 48x48 | Underground Karaoke League pin (mic doodle) |
| Quest Note: Performer Trials | (240, 160) | 48x48 | Street Performer Trials pin (territory map doodle) |
| Quest Note: Tempo Diplomat | (288, 160) | 48x48 | Peace-broker pin (dove holding baton, doomed) |
| Quest Note Hover State | (336, 160) | 48x48 | Selected note lifts with shadow |
| Regular Badge | (384, 160) | 48x48 | Stein-and-stool crest, earned after 3 visits |
| Regular Progress Pips | (432, 160) | 64x16 | Five-point tracker toward Regular status |
| Allegro Faction Flag | (192, 208) | 64x32 | Pennant, double-eighth wing emblem — shape-distinct |
| Adagio Faction Flag | (256, 208) | 64x32 | Rectangle, long whole-note bar emblem |
| Moderato Faction Flag | (320, 208) | 64x32 | Square, balanced quarter-note emblem |
| Presto Faction Flag | (384, 208) | 64x32 | Jagged pennant, sixteenth-run emblem |
| Lento Faction Flag | (448, 208) | 64x32 | Drooping banner, fermata emblem |

### Buff & Status Icons (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Allegro Morning Buff | (192, 240) | 32x32 | +10% Speed: winged boot on eighth note |
| Adagio Morning Buff | (224, 240) | 32x32 | +10% Defense: shield on whole note |
| Moderato Morning Buff | (256, 240) | 32x32 | +5% both: balanced scale icon |
| Moderate Mood Buff | (288, 240) | 32x32 | Tempo Tantrum effect — level meter icon |
| Jittery Status | (320, 240) | 32x32 | Presto Pilsner side effect — vibrating outline |
| Fermata Pause Icon | (352, 240) | 32x32 | Debuffs-on-hold indicator |
| Golden Mic Icon | (384, 240) | 32x32 | Inventory/equip icon, +5 Charm |
| Rest Available Icon | (416, 240) | 32x32 | Cot icon on backroom door prompt |

### Brewery Stamp & System UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Brewery Stamp Full Art | (192, 272) | 96x96 | Frozen pendulum mid-swing, stein at rest below; "Tempo Settled (Temporarily)" arc text; warm amber + copper ink |
| Stamp Anim Tick 1 | (288, 272) | 64x64 | Stamp hovers, metronome tick one |
| Stamp Anim Tick 2 | (352, 272) | 64x64 | Stamp rises, tick two |
| Stamp Anim Tick 3 / Land | (416, 272) | 64x64 | Stamp slams on the third tick |
| Stamp Inked Result | (288, 336) | 64x64 | Passport page result with ink splash settled |
| Save Indicator A | (352, 336) | 32x48 | Metronome save icon, pendulum left |
| Save Indicator B | (384, 336) | 32x48 | Pendulum right — two-frame save-point marker over the bar |
| Party Management Tab | (416, 336) | 32x32 | Marching-band-file icon |
| Quest Log Tab | (448, 336) | 32x32 | Setlist icon |

### Shop & Misc UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Frame | (0, 352) | 160x128 | Shop interface: chalkboard-styled drinks/food panel |
| Price Tag | (160, 352) | 32x16 | Chalk price chip |
| Regular Discount Tag | (160, 368) | 32x16 | "-15%" chip, Regular status only |
| Golden Mic Trophy Large | (160, 384) | 48x64 | Championship reward showcase art |
| Selfie Spot Icon | (208, 400) | 32x32 | Camera prompt at the main bar |
| Achievement Toast | (240, 400) | 128x32 | Banner: "Presto President", "Tempo Warrior", etc. |
| Debate Topic Ticker | (240, 432) | 192x24 | Scrolling strip of tonight's contested topics |

### Technical Notes:
- Every interactive UI element ≥44x44px effective touch zone (48x48 buttons and notes exceed it; flags and pips are display-only)
- Faction identity is triple-coded: emblem shape + flag silhouette + label text — color is decoration, never information
- Stamp animation frames align 1:1 with three audible metronome ticks; the landing frame and ink splash (Sheet 7) share the third tick

---

## 🎬 Animation Specifications

### Herr Takt Beer Pour:
- **Duration:** 1.2 seconds, single play
- **Frames:** 3 (pour 1 → 2 → 3) + pour stream/foam effects
- **Pattern:** Frame advance with effect overlay, hold on settled foam
- **Trigger:** Any drink purchase
- **Purpose:** The pub's heartbeat — every order is served with unhurried craft
- **Audio Sync:** Pour sound starts frame 1, tapers frame 3; faint foam fizz on hold
- **Performance Optimization:** Profile-mandated simplified bar animation — 2 frames, no stream particle on low-end

### Herr Takt Mediating:
- **Duration:** 2.4 seconds loop
- **Frames:** 3 (palms to Allegro → palms to Adagio → both, eyes closed)
- **Pattern:** 1 → 2 → 3 → loop while debate heat is high
- **Trigger:** Debate volume threshold / scripted debate scenes
- **Purpose:** The only neutral party in the room, conducting calm
- **Audio Sync:** Argument snippets duck slightly on frame 3
- **Performance Optimization:** Hold frame 3 as static on Low LOD

### Herr Takt Coffee Delivery (Morning):
- **Duration:** 3.0 seconds, single play
- **Frames:** 2 (carry → offer) plus Morning Check-In pose
- **Pattern:** Carry 1.5s → offer, hold with wake-up shimmer
- **Trigger:** Player wakes after backroom rest
- **Purpose:** The couchsurfing payoff — someone actually looking after you in Sinfonia
- **Audio Sync:** Gentle wake-up strings begin on carry; cup-set clink on offer
- **Performance Optimization:** None needed (scripted scene, nothing else animating)

### Metronome Collection (Competing Tempos):
- **Duration:** Five simultaneous cycles: 2.0s (Largo), 1.5s (Adagio), 1.0s (Moderato), 0.67s (Allegro), 0.4s (Presto)
- **Frames:** 3 shared pendulum overlays (left → center → right → center)
- **Pattern:** Continuous loops, deliberately never in phase
- **Trigger:** Constant while bar is on screen
- **Purpose:** The pub's signature comedy texture — five tempos ticking at once, agreeing on nothing
- **Audio Sync:** One tick per pendulum extreme, each metronome at its own rate; tick pulse ring (Sheet 7) fires per audible tick
- **Performance Optimization:** Low LOD freezes all pendulums at center (static variant); Medium runs Moderato only

### Frau Schnell Rapid Gestures:
- **Duration:** 0.6 second loop
- **Frames:** 3 gestures + optional blur overlay
- **Pattern:** 1 → 2 → 3 loop at 5 fps — fastest NPC in the room
- **Trigger:** Debate active or player conversation
- **Purpose:** Her frame rate is her personality: "Life is SHORT! Music should be FAST!"
- **Audio Sync:** Rapid speech bed, no pauses; blur overlay pulses with syllable peaks
- **Performance Optimization:** Drop blur overlay; 2-frame version at Low LOD

### Herr Langsam Deliberate Gesture:
- **Duration:** 4.8 seconds per cycle
- **Frames:** 3 (arm rising → apex → descending)
- **Pattern:** 1.6s per frame — slowest NPC in the game, intentionally
- **Trigger:** Debate active or player conversation
- **Purpose:** The Adagio argument made flesh; the room waits, and that's the joke
- **Audio Sync:** "...Why... the... rush?" — one word per frame; slow trail effect on the descent
- **Performance Optimization:** None needed (it's already nearly static)

### Die Mitte Tears of Joy:
- **Duration:** 2.0 seconds, single play, hold final frame
- **Frames:** 3 (exhausted idle → pleading → tears of joy)
- **Pattern:** Scripted advance during the bros' "medium tempo" beat
- **Trigger:** Lord Pilsner's accidental Moderato endorsement
- **Purpose:** "FINALLY! Someone who UNDERSTANDS!" — the pub's biggest heart moment
- **Audio Sync:** Dramatic gasp (crowd strip swaps) on frame 2; triumphant string swell on frame 3
- **Performance Optimization:** None needed

### Baton Dart Throw:
- **Duration:** 0.5 seconds flight + thunk hold
- **Frames:** 2 flight frames + thunk star
- **Pattern:** Flight A ↔ B (spin) → impact star, baton stays in board
- **Trigger:** Optional dartboard mini-interaction / ambient patron throws
- **Purpose:** Conductor batons as darts — authority repurposed as pub game
- **Audio Sync:** Whoosh on release, dartboard thunk exactly on impact frame
- **Performance Optimization:** Skip flight frames; baton appears in board with thunk star only

### Tempo Debate Point Scored:
- **Duration:** 0.8 seconds
- **Frames:** Stinger flash (1) + banner slide (interface)
- **Pattern:** Flash on staff lines → banner in → out
- **Trigger:** Winning dialogue exchange in Tempo Debate mini-game
- **Purpose:** Scores social combat like real combat — with orchestration
- **Audio Sync:** Musical stinger on flash frame; dramatic gasp lines over reacting faction
- **Performance Optimization:** Banner only, no flash, at Low LOD

### Debate Victory (Polka Burst):
- **Duration:** 2.5 seconds, single play
- **Frames:** Confetti burst (1) + toast cluster + free drink sparkle
- **Pattern:** Confetti → steins raise → sparkle on comped drink
- **Trigger:** Debate won (stamp-eligible moment)
- **Purpose:** Victory feels communal — even the losers toast you
- **Audio Sync:** Triumphant polka burst starts with confetti; toast clink on stein contact
- **Performance Optimization:** Confetti capped at 12 particles

### Brewery Stamp Ceremony:
- **Duration:** 2.0 seconds (three ticks at Moderato: 0.5s apart, land on third, 0.5s ink settle)
- **Frames:** 3 stamp frames + 3 ink splash frames + inked result
- **Pattern:** Tick 1 (hover) → tick 2 (rise) → tick 3 (SLAM + splash 1) → splash 2 → 3 → result
- **Trigger:** Winning a Tempo Debate with the bottle opener in inventory
- **Purpose:** "Tempo Settled (Temporarily)" — the stamp lands on the beat, because of course it does
- **Audio Sync:** Metronome ticks on frames 1–3; stamp lands exactly on the third tick, per profile; Herr Takt's speech follows
- **Performance Optimization:** None needed (scripted, exclusive scene)

### Musical Dreams (Backroom Rest):
- **Duration:** 4.0 second loop during sleep fade
- **Frames:** Dream swirl (1, rotating) + Zzz (2 alternating)
- **Pattern:** Swirl rotates continuously, Zzz pulses every 1.0s
- **Trigger:** Sleeping in backroom (Regular status)
- **Purpose:** Tempo-themed dream buffs telegraphed visually before the morning reveal
- **Audio Sync:** Muffled tavern music slows/detunes beneath; gentle wake-up strings end the loop
- **Performance Optimization:** Static swirl frame, Zzz only

### Candle & String Light Ambience:
- **Duration:** Candle 0.9s cycle; string lights 2.0s cycle
- **Frames:** 3 (candle), 2 (twinkle)
- **Pattern:** Continuous loops, offset per instance
- **Trigger:** Evening interior / beer garden at night
- **Purpose:** The warmth budget — this location sells safety through light
- **Audio Sync:** None
- **Performance Optimization:** Static candle + String Lights Static variant at Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bar counter outline | set at sheet layout | 128x64 | High-contrast frame on the primary interactable (shop/save) |
| Herr Takt silhouette | set at sheet layout | 48x96 | Bright-edge outline against dark back-bar |
| Bulletin board highlight | set at sheet layout | 96x128 | Enhanced-visibility marker for the quest hub |
| Backroom door outline | set at sheet layout | 32x64 | Marks the rest/couchsurfing entrance |
| Debate table glow ring | set at sheet layout | 128x48 | Identifies which communal table hosts the active debate |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static crowd strips | (0, 288) / (96, 288) Sheet 5 | 96x64 | Pre-rendered patrons frozen mid-gesture — replaces the constantly gesturing crowd |
| Metronomes frozen center | (144, 144) Sheet 6 overlay | 24x40 | All five pendulums held at center; tick rings disabled |
| String Lights Static | (320, 416) Sheet 1 | 256x32 | No twinkle cycle in beer garden |
| Static candle frame | (272, 0) Sheet 7 | 16x24 | Upright flame, no flicker |
| Frau Schnell reduced set | (0, 0) Sheet 4 | 48x96 | Idle-only; blur overlay and 5 fps loop disabled |
| Dream swirl static | (192, 64) Sheet 7 | 64x64 | Non-rotating dream frame with pulsing Zzz removed |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pour glyph | set at sheet layout | 24x24 | Tap-and-stream icon over bar whenever pour audio plays |
| Toast clink spark | (112, 0) Sheet 7 | 32x32 | Fires on every toast clink sound |
| Dart thunk star | (144, 0) Sheet 7 | 32x32 | Impact star on every dartboard thunk |
| Tick pulse rings | (0, 64) Sheet 7 | 32x32 | One ring per metronome tick — five rates, five visual sources |
| Dramatic gasp lines | (112, 64) Sheet 7 | 32x32 | Appears over crowd for every gasp audio event |
| Stinger flash | (64, 64) Sheet 7 | 48x32 | Staff-line flare for every debate-point musical stinger |
| Polka burst confetti | (464, 0) Sheet 7 | 48x48 | Visual stand-in for the victory polka |
| Wake-up shimmer | (256, 64) Sheet 7 | 64x32 | Light ripple synced to gentle wake-up strings |
| Stamp tick counter | set at sheet layout | 48x16 | "1 · 2 · 3" pips filling with each stamp-ceremony metronome tick |
| Speech-burst glyphs | set at sheet layout | 24x24 | Shout indicator over off-screen argument audio |

### Colorblind Considerations:
- Faction identity is NEVER color-only: each faction owns a distinct emblem shape (Allegro wings, Adagio bar, Moderato balance, Presto jag, Lento fermata), a distinct flag silhouette (pennant / rectangle / square / jagged / drooping), and text labels in all debate UI
- Drinks differ by silhouette and foam behavior (overfizz, flat, fermata etch), not hue alone
- Buff icons use distinct pictograms (boot / shield / scale), not tint swaps
- Debate reaction portraits pair expression with border pattern (dots = approval, zigzag = outrage, waves = laughter)
- Touch zones minimum 44px for bar, bulletin board, debate buttons, backroom door, and shop rows

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) UI sheet and stamp art need uncompressed — chalk text and stamp inscription must stay legible
- **Fallback:** PNG high quality for `moderato_pub_ui.png` (debate text) and the stamp full art

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| moderato_environment | exterior, interior tileset | 1024x1024 |
| moderato_characters | Herr Takt, faction leaders, NPCs | 2048x1024 |
| moderato_items_fx_ui | items, effects, UI | 1024x1024 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | All five metronomes ticking, full crowd gesture frames, candle flicker, string twinkle, dust motes, all debate effects |
| Medium | Moderato metronome only, faction leaders animate but patrons use static crowd strips, no dust motes, confetti capped |
| Low | Pre-rendered static crowd everywhere, all pendulums frozen center, simplified 2-frame pour, no ambient particles, effects limited to UI-critical cues (stinger, stamp, save sparkle) |

### Performance Targets:
- **Target FPS:** 60 (per location profile — cozy atmosphere priority over frame rate)
- **Max Draw Calls:** 16 per frame (per location profile)
- **Memory Footprint:** 40 MB maximum (per location profile)
- **Particle Limit:** 20 (steam 3, dust 8, notes 6, confetti burst 12 — bursts replace ambient, never stack)

### Performance Notes:
- Per profile: background patrons are STATIC (crowd strips), bar animations are SIMPLIFIED, and the crowd is PRE-RENDERED — the animation budget is spent on Herr Takt and the three faction leaders, who carry the comedy
- Beer garden and backroom load on-demand (door-gated sub-scenes); snug shares the interior tileset with a palette-warmed light overlay
- Metronome collection animates through 3 shared overlay frames scheduled at 5 rates — one texture region, five tempos, one draw call
- Debate mini-game is UI-layer only; world animation drops to idle set while the interface is open

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for Herr Takt and faction leaders; static Sprite2D for crowd strips
- CPUParticles2D (not GPU) for steam, dust, notes, confetti
- CanvasLayer for debate interface, bulletin board UI, and achievement toasts
- Base-of-operations hooks: save/load API on bar interaction (manual save + entry auto-save), full-rest state machine on backroom (Regular status gate → sleep fade → dream loop → coffee delivery scene → buff grant), party management / quest log / achievement tracker panels opened from the UI tabs
- Regular status tracker (0–5 points) drives sprite/state unlocks: backroom door, discount tags, Regular badge, behind-bar selfie variant
- Timer-scheduled pendulum overlays for the five-tempo metronome collection (see Performance Notes)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Pour animation | Pour sound + foam fizz | Starts frame 1, tapers frame 3 |
| Toast cluster / clink spark | Toast clink | On stein-contact frame |
| Baton dart | Dartboard thunk | Exactly on impact frame |
| Metronome pendulums (x5) | Competing metronome ticks | One tick per pendulum extreme, five independent rates |
| Gasping crowd strips | Dramatic gasp | On strip swap A → B |
| Debate stinger flash | Musical stinger (point scored) | On flash frame |
| Polka confetti burst | Triumphant polka burst | Burst and downbeat together |
| Wake-up shimmer / coffee delivery | Gentle wake-up strings | Strings begin on carry frame, resolve on cup-set clink |
| Stamp ceremony frames 1–3 | Metronome ticks x3 | Stamp lands exactly on the third tick |
| Frau Schnell gestures | Rapid no-pause speech bed | Loop-synced, blur pulses on syllable peaks |
| Herr Langsam gesture | "...Why... the... rush?" | One word per 1.6s frame |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Underground Karaoke League | Die Stimme states, mic stand, Golden Mic icon + trophy, quest note pin | Die Stimme grants tournament access from the snug; Golden Mic (+5 Charm) awarded on championship |
| Street Performer Trials | Violinist/tubist sets, hat pass, quest note pin, MusikGasse door transition | Performers claim territories; buff item rewards delivered at the bar |
| Instrument Repair (Kurt) | Kurt despair/quest frames, accordion prop, accordion parts item | Fetch parts from MusikGasse shops; repaired-accordion playing frames on completion |
| Opera House Intel (Bruckmann) | Bruckmann conducting/intel frames, snug table | Reconnaissance dialogue before The Bassline Opera House boss; Vice von Strauss weakness hints |
| Tempo Diplomat | Die Mitte full set, argument cloud, all faction flags | Impossible peace-brokering attempt; "The Moderate Voice" achievement path |
| The Golden Mic | Golden Mic trophy large, achievement toast | Championship reward showcase + equip icon |
| Rotating Tourist Quests | Exhausted Tourist states, map fumble | Randomized "help me find..." missions; relief frame on turn-in |
| Brewery Tour: "Win a Tempo Debate" | Debate interface, bottle opener, stamp full art + animation, ink splash, Herr Takt stamp ceremony | Bottle opener in inventory + debate victory → stamp ceremony scene → Tempo Tantrum unlocked on menu |
| Achievements (First Round, Local Regular, Tempo Warrior, Presto President, Musical Dreams, Fermata Champion, The Moderate Voice, Tempo Diplomat) | Achievement toast banner + relevant scene sprites | Toast fires on trigger; Presto President uses Chadwick + Presto flag combo |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bassline Opera House | Bruckmann intel scene; weakness-hint UI carries into boss fight | Standard door transition; intel journal entry persists |
| Mozart's Last Rave | Rumor dialogue at bar points to cemetery entrance (no shared sprites) | None — dialogue only |
| Café Existenz | Intellectual-musician crossover patrons (shared silhouette language) | Same-district ambience |
| MusikGasse | Direct street access; violinist/tubist sprites reused as exterior buskers; cobblestone tiles shared | Door transition with street-performance audio crossfade |
| The Dancing Stein | Tempo-overlap gag: competing house tempos referenced in Debate Topic Ticker | None — text ticker only |
| Brewery Tour (system-wide) | Bottle opener, stamp, passport page UI shared with all brewery locations | Stamp ceremony scene overlay |
| All Sinfonia locations | Save/rest/party management here is the recovery point after any Sinfonia failure | Entry auto-save swirl on every arrival |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "The one warm room in a city of scams" — safe-haven warmth is the design keynote; every other Sinfonia location exploits the player, so this one must visibly, instantly promise it won't
- **Color Mood:** Beer amber and lamplight gold over deep wood brown — honey tones, zero cold highlights indoors
- **Lighting:** Warm tavern glow as the default state; stage spotlights for drama, hearth and candles for evening, natural window light by day, string lights in the garden — light always says "stay"
- **Texture:** Worn-smooth wood, chalk dust, foam, brass polished by decades of hands — aged but loved, never decayed

### Environmental Storytelling:
- The metronome shelf (five tempos, never in phase) tells the whole 178-year argument without a word of dialogue
- Red-ink corrections on framed sheet music = patrons who cannot let anything go, even décor
- "No Allegro After Midnight" sign hangs directly above the loudest Allegro table
- Memorabilia wall of signed photos of musicians nobody's heard of = the pub's gentle self-delusion
- Bass-clef table legs and note-duration tap handles reward players who look closely
- Cot Rumpled and coffee delivery frames show the pub takes care of its people — the satire has a soft center

### Character Integration Notes:
- Herr Takt anchors every scene from behind the bar; he is the visual promise of safety and the literal save point
- Faction leaders are personality-through-framerate: Schnell at 5 fps, Langsam at 0.6 fps, Die Mitte sagging between them
- Crowd is pre-rendered warmth, not detail — silhouettes mid-gesture, steins up, forever arguing
- Die Stimme renders one shade darker than ambient light in all states; the mystery is a lighting rule, not a sprite

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The metronome shelf ticking at five tempos at once** — instantly loopable, instantly understood by every musician online
2. **Die Mitte's tears of joy at Lord Pilsner's "medium tempo"** — the accidental-diplomacy meme frame
3. **The baton dartboard mid-thunk** — conductor authority as pub game
4. **"Tonight's Tempo: CONTESTED" chalkboard** — the exterior establishing shot that sells the whole location
5. **Stamp landing on the third metronome tick** — satisfying rhythm-synced payoff clip

### TikTok Potential:
- "POV: you said music should be 'medium' in the wrong pub"
- "Frau Schnell vs. Herr Langsam: the same argument at two frame rates"
- "I don't remember picking a side but I'm faction president now"
- "The one place in this game that ISN'T scamming you"

### Quote Potential:
- "The secret handshake is buying a round." — Herr Takt
- "FINALLY! Someone who UNDERSTANDS!" / "TRAITOR!" — Die Mitte and Frau Schnell, same second
- "Life is SHORT! Music should be FAST! Why are you still standing there?! SIT! DRINK! FASTER!" — Frau Schnell
- "...Why... the... rush?" — Herr Langsam
- "I don't remember picking a side but apparently I'm PRESIDENT of the Presto Extremists now?" — Chadwick
- "You argued! You defended! You probably changed no minds! But you PARTICIPATED!" — Herr Takt's stamp speech

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | moderato_pub_exterior.png | 1024x512 |
| 2 | moderato_pub_tileset.png | 1024x512 |
| 3 | herr_takt_bartender.png | 512x288 |
| 4 | tempo_faction_leaders.png | 512x384 |
| 5 | moderato_pub_npcs.png | 1024x384 |
| 6 | moderato_pub_items.png | 512x256 |
| 7 | moderato_pub_effects.png | 512x256 |
| 8 | moderato_pub_ui.png | 512x512 |

**Total Estimated Memory:** ~9.2 MB (uncompressed RGBA, ~4 bytes/pixel — well inside the 40 MB location budget with atlas overhead)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `moderato_pub_exterior.png` (1024x512)
- [ ] `moderato_pub_tileset.png` (1024x512)
- [ ] `herr_takt_bartender.png` (512x288)
- [ ] `tempo_faction_leaders.png` (512x384)
- [ ] `moderato_pub_npcs.png` (1024x384)
- [ ] `moderato_pub_items.png` (512x256)
- [ ] `moderato_pub_effects.png` (512x256)
- [ ] `moderato_pub_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + metronome tempo-scheduling table (five rates, shared overlays) + stamp-ceremony tick alignment guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] All five metronomes read as different tempos at a glance (pendulum angles + tick rings)
- [ ] Bass-clef table legs and note-duration tap handles legible at game resolution
- [ ] "Tonight's Tempo: CONTESTED" and "No Allegro After Midnight" chalk/brass text readable on mobile screens
- [ ] Frau Schnell and Herr Langsam frame counts support their contrasting animation rates
- [ ] Die Mitte's tears-of-joy frame lands emotionally at 48x96
- [ ] Stamp full art shows frozen pendulum + resting stein with legible arc inscription
- [ ] Faction emblems distinguishable in grayscale (colorblind check)
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (pedantry treated with total seriousness)
- [ ] Safe-haven warmth reads instantly — this must FEEL like the one non-exploitative room in Sinfonia
- [ ] Hidden areas/interactions have discoverable visual cues (backroom door, snug, selfie spot, dartboard)
- [ ] Performance optimized (CPU particles, atlas limits respected, static crowd honored)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (faction shapes, drink silhouettes)
- [ ] Social media viral potential maximized in composition choices (metronome shelf, debate reactions, stamp beat-sync)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia / MusikGasse only; Viennese wirtshaus evoked, never named |
| Cultural Specificity | ✅ | Viennese beer hall tradition + classical-music pedantry (tempo wars since 1848) |
| Satirical Targets Appropriate | ✅ | Debate culture and expertise gatekeeping — never music itself, never the locals as victims; bros are lovable idiots, not marks |
| Seedy Underbelly Present | ❌ | Absent BY DESIGN per the profile's Safe Haven section — this is deliberately the one Sinfonia location that doesn't exploit you; the sole mild edge is regulars quietly betting on the bros' opinions (Betting Regulars sprite, Sheet 5) |
| Gameplay Value Established | ✅ | Base of operations: save point, full rest, party management, quest hub, shop, debate mini-game, brewery stamp, Regular progression |
| Technical Feasibility | ✅ | Eight sheets, three-atlas plan, LOD tiers, shared-overlay metronome scheduling documented |
| Performance Budget | ✅ | 60 FPS, 16 draw calls, 40 MB, 20 particles — per location profile |
| Accessibility Features | ✅ | Visual cues for every audio event (ticks, clinks, thunks, gasps, stingers, polka, strings, stamp ticks); static motion variants; shape-coded factions |
| No Crypto Elements | ✅ | None present — pure musical comedy |
| Social Media Integration | ✅ | Metronome shelf, Die Mitte meme frame, stamp beat-sync, faction-president moments identified |

**The Moderato Pub: the one room in Sinfonia where the beer is honest, the arguments are eternal, the stamp lands on the beat, and — for exactly as long as you can hear five metronomes disagreeing — you are finally, genuinely safe.**
