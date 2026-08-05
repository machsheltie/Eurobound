# The Bassline Opera House - Complete PNG Asset Requirements

*Artist Reference Document for Sinfonia's Crown Jewel*

## 📋 Overview
The Bassline Opera House is a 400-year-old baroque masterpiece that transforms into an EDM venue at night — Sinfonia's crown jewel, where four centuries of cultural excellence meet one horse in a cape, one method-acting bird-man, and 2,000 Sovs in Magic Flute production costs. This document specifies every sprite sheet the location needs across its six zones: grand lobby, auditorium, backstage, dressing rooms, orchestra pit boss arena, and **the divas' apartment above the house** (Saturday-only couchsurf interior).

**Location ID:** `sinfonia_bassline_opera_house_01`
**Theme:** Cultural institution pretension — opera snobbery and artistic exploitation, with a dual identity (traditional opera by day, underground Bassline EDM by night)
**Zone:** Imperial Square District
**Hours:** Lobby 10:00–23:00; rehearsals 10:00–17:00; performances 19:00–22:00; Bassline 23:00–04:00; **DIE, FLEDERMAUS! Saturdays 19:00–22:00, apartment 01:30–late (Saturday only)**
**Primary Function:** Multi-zone venue / story hub / boss arena — Fiaker Fiasco phase 3 (backstage chaos), Maestro Vice von Strauss city-boss fight, Waltz of the Bros rhythm battle, **"The Ladies of the House" couchsurf (`sinfonia_couchsurf_opera_divas_01`)**, gift shop and box office economy

**Priority**: HIGH (Multi-Zone Venue, Story Hub, Boss Arena, Fiaker Fiasco Phase 3, Couchsurf Interior)  
**Total Sheets Required**: 18  
**Performance Optimization**: Target 60 FPS on min-spec hardware

> **⚠️ Binding art direction for Sheets 13–18 — the stage/off-stage gag.**
> Madame Fortissima and Prima Donna Adelheid are drag performers headlining **DIE, FLEDERMAUS!**, and their off-stage identities (**Wolfram Kranzler**, 58; **Lorenz Brandtner**, 44) are printed on the programme, engraved on the dressing-room door plates, and applauded nightly by twelve hundred people. **The transformation must be legible in the art with no dialogue explaining it** — a player who mutes the game must be able to look at the stage sheet and the off-stage sheet side by side and understand instantly that these are the same two people.
> The legibility comes from **silhouette, scale, posture and palette**, never from a cheap gag. Prohibited in every frame on every one of these sheets: five o'clock shadow, comedy stubble, smeared lipstick, "man in a dress" staging, wink-to-camera expressions, or any framing that treats either performer as a punchline. **They must read as great performers; the audience gives them an ovation and the player has to believe it.** Wig lace at the hairline, the adam's apple, the shave kit and the size 47 shoes are rendered plainly and unremarked because these characters do not hide them — not because the art is nudging anybody. Full canon: `opera_divas_couchsurf_direction.md`, `npcs/Bassline_Opera_House/npc_madame_fortissima.md`, `npc_prima_donna_adelheid.md`.

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
| Imperial Oxblood | #6E0F1A | Fortissima's gown, apartment upholstery |
| Jet & Silver | #101014 / #C0C4CC | Adelheid's DIE, FLEDERMAUS! look |
| Cardigan Grey | #7A7A72 | Kranzler off-stage; the deliberate anti-glamour |
| Mirror Bulb Warm | #FFE9B8 | Makeup-station bulbs, apartment morning light |
| Jägermeister Green | #1B3A22 | Nightcap bottle and tray staging |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/bassline_opera_house/
├── environment/
│   ├── bassline_opera_lobby_tileset.png
│   ├── bassline_opera_backstage_tileset.png
│   ├── bassline_opera_backdrop_starry.png
│   └── divas_apartment_interior.png
├── npcs/
│   ├── npc_regisseur_hoffmann.png
│   ├── npc_stagehead_otto.png
│   ├── npc_prima_donna_adelheid.png
│   ├── npc_prima_donna_adelheid_dragshow.png
│   ├── npc_lorenz_brandtner_offstage.png
│   ├── madame_fortissima.png
│   ├── madame_fortissima_dragshow.png
│   ├── npc_wolfram_kranzler_offstage.png
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

### Coat Check Hilde (Rows 4-5)
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
- **Damage Popup**: 3 frames, rising "N SOVS" amount — letter the word, there is no currency glyph
- **Chandelier Sparkle**: 4 frames, crystal glints
- **Dust Cloud**: 4 frames, prop destruction aftermath
- **Stage Light Beam**: 2 frames, spotlight effect

---

## 🖥️ Sprite Sheet 12: UI Elements
**Filename**: `opera_house_ui.png`  
**Dimensions**: 256 × 192 pixels

### UI Components
- **Damage Counter Frame**: Ornate gold frame (128×48)
- **Sovs Wordmark**: The word `SOVS` lettered in the house's gold display face (96×32) — **the symbol is the word; there is no Sov glyph.** ⚠️ Cell widened from 32×32 to 96×32: four legible characters do not fit in 32px. Atlas key is `sovs_symbol`.
- **Debt Indicator**: "OUTSTANDING" bar (100×32)
- **Choice Panel**: Dialogue choice frame, baroque style (200×80)
- **Papageno Icon**: For ally indicator (48×48)
- **Status Icons**: Cultured Presence, Artistic Guilt, etc. (24×24 each)

---

## 🌟 Sprite Sheet 13: Madame Fortissima — Diva (Backstage & Lobby)
**Filename**: `madame_fortissima.png`
**Dimensions**: 384 × 384 pixels
**Sprite Size**: 96 × 128 pixels (4 columns × 3 rows = 12 cells)
**Color Palette**: Imperial Oxblood #6E0F1A + Opera House Gold #CFB53B over Baroque Cream #FFF8DC

> **📌 Reconciliation note.** `bassline_opera_house.md`'s PNG Asset Requirements Summary lists `madame_fortissima.png - 96x128 - Principal soprano`, and that sheet was **absent from this document** until this pass. It is now specified here. **The 96×128 figure in that summary is the sprite cell size, not the sheet size** — the sheet is 384 × 384. This follows the precedent already set by `boss_maestro_von_strauss.png`, listed in the same summary as 256×384 and specified in this document at 512×640. **This document is authoritative for all sheet dimensions.** The NPC profile's `fortissima_diva` sprite state maps here.

### Character Design
- **Age**: 58. Broad-shouldered, magnificently upholstered, excellent core strength from three decades under a heavy costume
- **Height**: Tall; in the heels, extremely tall. She ducks under the dressing-room doorframe without thinking about it — build the frame so the duck reads
- **The wig**: A tower. Powdered, pinned, forty years out of period on purpose. **Lace front visible at the hairline in every conversational frame.**
- **The makeup**: Full stage paint built to be read from the back of the upper gallery, which at four feet is a landscape
- **Accessories**: Opera-length gloves, a lorgnette she uses correctly, a stage fan she conducts rooms with
- **The adam's apple**: rendered, unhidden, unremarked. She stopped bothering in 2009.

### Cell Layout
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle — Hold Court | (0, 0) | 96x128 | Weight on the back foot, fan working, playing to a house that is not there. Default frame. |
| Wig Adjust | (96, 0) | 96x128 | Two fingers to the lace at the temple, entirely unselfconscious |
| Lorgnette Raise | (192, 0) | 96x128 | Inspecting whoever just spoke |
| Compliment Graded | (288, 0) | 96x128 | **The fan closes.** This is how the player learns a compliment landed. |
| Fan Working A | (0, 128) | 96x128 | Idle loop frame A |
| Fan Working B | (96, 128) | 96x128 | Idle loop frame B |
| Backstage Turn — Wig Off, Gown On | (192, 128) | 96x128 | Post-curtain dressing-room state; **the transitional silhouette between Sheets 14 and 16** |
| Walk A | (288, 128) | 96x128 | Unhurried; enters every room as though it had been waiting |
| Walk B | (0, 256) | 96x128 | Second walk frame |
| Greeting Sweep | (96, 256) | 96x128 | "I have performed for KINGS! For EMPERORS!" — arms out |
| Invitation Beckon | (192, 256) | 96x128 | The backstage invitation upstairs; one flight of stairs, no ceremony |
| Signed Programme Handoff | (288, 256) | 96x128 | 10 Sovs; she signs both names and the examine text carries the second signature |

### Character Notes
- Every gesture is **blocked** — she is playing to a house even in a corridor. No frame should read as casual except the Backstage Turn.
- Deflects compliments by escalating them; the Compliment Graded frame is the one moment she drops to conversational and is briefly, completely sincere.
- She touches shoulders, arms and faces constantly, warmly, entirely without agenda. Build the Greeting Sweep so contact reads as hospitality, never as advance.

---

## 🎪 Sprite Sheet 14: Madame Fortissima — DIE, FLEDERMAUS! (Stage)
**Filename**: `madame_fortissima_dragshow.png`
**Dimensions**: 512 × 640 pixels
**Sprite Size**: 128 × 160 pixels (4 columns × 4 rows = 16 cells)
**Color Palette**: Imperial Oxblood #6E0F1A + Opera House Gold #CFB53B, Velvet Red #8B0000 curtain behind

### Character Design
- **The gown**: Imperial gold and oxblood, boned, corseted, with a train that requires a dresser and gets one. **It is genuinely beautiful costume work and the shop that built it is proud of it** — render it that way. The oversized cell exists to hold the train.
- **Footwear**: Size 47, custom, four inches, and she does the entire second act in them
- **Scale**: This is the *big* silhouette. Sheet 16 is the same person at half the volume — the contrast is the whole gag.

### Stage & Performance (Row 0)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stage Entrance A | (0, 0) | 128x160 | Arms out, gown at full spread, held for four beats |
| Stage Entrance B | (128, 0) | 128x160 | Train settling behind her |
| Aria Hold | (256, 0) | 128x160 | Sustained note, chest open, lorgnette hand down |
| Fan Conduct | (384, 0) | 128x160 | Conducting the room with the stage fan |

### Act Two & Bows (Row 1)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Duet Stance (with Adelheid) | (0, 160) | 128x160 | Two-hander blocking anchor; pairs with Sheet 15 row 1 |
| Gown Sweep A | (128, 160) | 128x160 | Crossing the stage, train trailing |
| Gown Sweep B | (256, 160) | 128x160 | Second sweep frame |
| Bow, Deep | (384, 160) | 128x160 | Full company bow, wig still on |

### The Curtain Call (Row 2) — **the location's central visual gag**
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Curtain Call — Arms Wide, Wig On | (0, 320) | 128x160 | Twelve hundred people already on their feet |
| Curtain Call — Wig Lifted | (128, 320) | 128x160 | Hands to the tower, lift beginning |
| **Curtain Call — Wig Held Out at Arm's Length** | (256, 320) | 128x160 | **A TRIUMPH FRAME, NOT A REVEAL FRAME. She is bowing.** Held like a trophy. If this frame plays as a gag the scene is broken. |
| Curtain Call — Wig-Off Bow | (384, 320) | 128x160 | Wig cap, grey at the temples visible, gown still full, still enormous, still winning |

### Backstage & The Nightcap (Row 3) — gown on, wig off
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marquee Approach / Lobby In Costume | (0, 480) | 128x160 | Post-curtain lobby hold, standing where the chandelier light is best (deliberately) |
| Backstage Pass Handoff | (128, 480) | 128x160 | Free, if she likes you; 60 Sovs at the box office |
| Nightcap Pour | (256, 480) | 128x160 | Apartment, ~01:40. Pouring at volume, tray on the sideboard behind her. **No lingering framing on the tray.** |
| Prost Count — Glass Raised | (384, 480) | 128x160 | "Drei — zwei — eins — PROST!" Joyous. Best part of her week and it must look like it. |

### Character Notes
- **The last frame before the Nightcap fade to black is Fortissima laughing** at something Chadwick said, hand on his shoulder — composite from Prost Count + a laugh pose; **no menacing staging, no slow-motion, no ominous cut.**
- Wig lace stays visible at conversational distance in every non-stage frame. It is not a mistake and must not be cleaned up.
- The curtain-call ovation is a genuine ovation. Crowd art behind these frames must be enthusiastic, not smirking.

---

## 🖤 Sprite Sheet 15: Prima Donna Adelheid — DIE, FLEDERMAUS! (Stage & Backstage)
**Filename**: `npc_prima_donna_adelheid_dragshow.png`
**Dimensions**: 384 × 320 pixels
**Sprite Size**: 48 × 80 pixels (8 columns × 4 rows = 32 cells; 30 specified, 2 reserved)
**Color Palette**: Jet & Silver #101014 / #C0C4CC over Backstage Black #1C1C1C

> Dimensions and cell size deliberately match her existing repertory sheet `npc_prima_donna_adelheid.png` (384×320, 48×80) so the two can be swapped by state without a rig change. Her `adelheid_dragshow` sprite state maps here.

### Character Design
- **Where Fortissima is scale, Adelheid is line.** Sharper, cleaner, more controlled silhouette in every frame.
- **The look**: Sharper, wittier and considerably more expensive than the Queen of the Night — jet, silver, and a train she uses as a weapon in the Act Two patter number
- **The wig**: Sleek, black, waved. Lace front visible at any conversational distance.
- **Accessories**: A cigarette holder used exclusively as a prop; a hand mic she does not need and deploys anyway
- **Rendered plainly and unremarked**: wig lace, adam's apple, and the shave kit on her makeup station

### Stage — The Patter Number (Row 0)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Drag Stage Idle | (0, 0) | 48x80 | Upright, hands still, entirely composed |
| Patter Number A | (48, 0) | 48x80 | "SHE'S SO FAST." — frame A |
| Patter Number B | (96, 0) | 48x80 | Frame B |
| Patter Number C | (144, 0) | 48x80 | Frame C |
| Cigarette Holder Pose | (192, 0) | 48x80 | Prop only; never lit |
| Hand Mic Deploy | (240, 0) | 48x80 | Does not need it; uses it |
| Train Whip A | (288, 0) | 48x80 | Act Two, the train as a weapon |
| Train Whip B | (336, 0) | 48x80 | Follow-through |

### Curtain Call & Signature Beats (Row 1)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Duet Stance (with Fortissima) | (0, 80) | 48x80 | Pairs with Sheet 14 row 1 |
| Deep Bow | (48, 80) | 48x80 | **She does not remove the wig.** She simply bows. |
| Gesture to Fortissima | (96, 80) | 48x80 | Hands the ovation across; the house goes up a level |
| Ovation Hold | (144, 80) | 48x80 | Wig on, entirely composed, twelve hundred people standing |
| The Eyebrow A | (192, 80) | 48x80 | Two-frame state. Ends most conversations in this building. |
| The Eyebrow B | (240, 80) | 48x80 | Raised roughly two millimetres. **Will be used constantly — this is the most-reused pair on the sheet.** |
| Correction Mid-Sentence | (288, 80) | 48x80 | Reflexive, never hostile, already moving on |
| List Produce | (336, 80) | 48x80 | The itemised invoice out of a sleeve, already broken down |

### Apartment — Wig Off, Corset On (Row 2)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Backstage Turn | (0, 160) | 48x80 | Out of the wig within ninety seconds of the curtain |
| Sideboard Turn — Back to Room | (48, 160) | 48x80 | **The nine seconds. No cut, no lingering, no framing device.** Camera treats it as a person making drinks. |
| Sideboard Work A | (96, 160) | 48x80 | Frame A |
| Sideboard Work B | (144, 160) | 48x80 | Frame B |
| Tray Carry | (192, 160) | 48x80 | Bringing the lacquered tray to the room |
| Glass Handoff — Eye Contact | (240, 160) | 48x80 | Hands each tall glass over personally, in order. **Not flirtation; the bros read it as flirtation.** |
| Hand Adjust | (288, 160) | 48x80 | "Hold it properly. Not like that." Adjusting Pilsner's grip. |
| Corset Removal, Hall A | (336, 160) | 48x80 | Mid-conversation, entirely unceremonious, one in the morning |

### Apartment & Nightcap Close (Row 3)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corset Removal, Hall B | (0, 240) | 48x80 | Follow-through |
| Corset Handoff | (48, 240) | 48x80 | Hands the corset to Lord Pilsner to hold. He is thrilled. |
| Walk A | (96, 240) | 48x80 | Efficient stride |
| Walk B | (144, 240) | 48x80 | Second walk frame |
| Prost — Glass Raised | (192, 240) | 48x80 | Small glass, hers |
| Laughing | (240, 240) | 48x80 | **The last frame before the fade to black** — glass down, already laughing at something Fortissima said |
| *(reserved)* | (288, 240) | 48x80 | Held for a second eyebrow variant if playtesting wants one |
| *(reserved)* | (336, 240) | 48x80 | Held for a Fiaker Fiasco crossover pose in drag costume |

### Character Notes
- **Never sultry, coy, seductive, arch or knowing in any frame.** She is not flirting; she has never flirted. Every "flirtatious" read in the scene is the bros' invention and the art must not endorse it.
- Her stillness reads as impatience and is not. Do not add fidget frames.
- She corrects, itemises, and keeps the room moving. Posture in every frame: someone at work, doing it well, on time.

---

## ☕ Sprite Sheet 16: Wolfram Kranzler — Off-Stage
**Filename**: `npc_wolfram_kranzler_offstage.png`
**Dimensions**: 288 × 256 pixels
**Sprite Size**: 48 × 64 pixels (6 columns × 4 rows = 24 cells)
**Color Palette**: Cardigan Grey #7A7A72 over Baroque Cream #FFF8DC, warm Mirror Bulb #FFE9B8 key light

> Dimensions and cell size deliberately match `npc_stagehead_otto.png` (288×256, 48×64) — the ordinary-person rig. **That is the joke, in geometry:** Sheet 14 is 128×160, this is 48×64, and it is the same human being four hours later. Her `kranzler_offstage` sprite state maps here.

### Character Design
- **Age**: 58. Grey at the temples, glasses on a chain, **a cardigan of profound ordinariness over the corset he has not yet got out of**
- **Posture**: Sits differently. Talks at half the volume. Makes tea. Nothing is blocked; nothing is played to a house.
- **Prohibited**: stubble gag, smeared paint, any frame that stages the change as a *reveal*. The paint is simply off and the cardigan is simply on.
- **Voice note for the VO director, carried here because it affects lip-sync frames**: the speaking voice does not change between states. Same voice, two volumes.

### Apartment Idle & The Crossword (Row 0)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cardigan Idle A | (0, 0) | 48x64 | Default off-stage frame |
| Cardigan Idle B | (48, 0) | 48x64 | Idle loop frame B |
| Crossword Absorbed A | (96, 0) | 48x64 | Kitchen table, 3 a.m., three Americans unconscious on the furniture |
| Crossword Absorbed B | (144, 0) | 48x64 | Frame B; he finishes it |
| Page Turn | (192, 0) | 48x64 | Morning-after; **does not look up** |
| Glasses Up / Look Over | (240, 0) | 48x64 | "It was MEMORABLE. For me." — warm, not cruel |

### Hospitality (Row 1)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tea Make A | (0, 64) | 48x64 | Feeds people. Waters people. This is why the couchsurf exists. |
| Tea Make B | (48, 64) | 48x64 | Frame B |
| Coffee Pour for Guests | (96, 64) | 48x64 | "There is coffee. There is bread." |
| Bread on Table | (144, 64) | 48x64 | "Eat the bread." |
| Quiet Beat | (192, 64) | 48x64 | Goes very still before saying anything kind, as though checking it is safe to |
| Speaks Kindly | (240, 64) | 48x64 | The line lands warm at the end, not the start |

### Movement & The Apartment (Row 2)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seated at Kitchen Table | (0, 128) | 48x64 | Pen in hand, ink, correct |
| Seated, Pen Down | (48, 128) | 48x64 | Crossword complete |
| Stand from Table | (96, 128) | 48x64 | Unhurried |
| Walk A | (144, 128) | 48x64 | Off-stage gait — nothing blocked, nothing performed |
| Walk B | (192, 128) | 48x64 | Second walk frame |
| Hall — Indicating the Door | (240, 128) | 48x64 | The four pairs of size 47 heels are in shot behind him |

### Morning-After & Branch States (Row 3)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cardigan Over Un-Removed Corset | (0, 192) | 48x64 | The in-between state; hospitality outranked getting changed |
| Reading Glasses On/Off | (48, 192) | 48x64 | Two-position frame |
| Hand on Shoulder | (96, 192) | 48x64 | Warm, constant, entirely without agenda |
| Bucket Placement | (144, 192) | 48x64 | Deadpan. "There is a bucket by the tall one and he should be grateful for it and for me." |
| Morning Greeting | (192, 192) | 48x64 | Does not look up as he says it |
| **Decline-Branch Idle** | (240, 192) | 48x64 | **Nightcap declined.** Identical staging, nobody in makeup, no bucket, no debris. "Sensible. Boring. But sensible." **This branch is fully supported and gates nothing.** |

---

## 📋 Sprite Sheet 17: Lorenz Brandtner — Off-Stage
**Filename**: `npc_lorenz_brandtner_offstage.png`
**Dimensions**: 288 × 256 pixels
**Sprite Size**: 48 × 64 pixels (6 columns × 4 rows = 24 cells; 23 specified, 1 reserved)
**Color Palette**: Cardigan Grey #7A7A72 / faded dressing-gown neutrals over Baroque Cream #FFF8DC

> Matches Sheet 16's rig exactly so the two off-stage NPCs share animation timing. Her `brandtner_offstage` sprite state maps here. Where Sheet 15 is *line*, this is line **relaxed** — same clean silhouette, none of the tension.

### Character Design
- **Age**: 44. Sharp-featured, tired around the eyes, **considerably funnier than the stage persona — the jokes get better as the layers come off**
- **Dress**: A dressing gown of some age. Bare feet. Reading glasses.
- **Timing**: out of the wig within ninety seconds of the curtain, out of the corset within twenty minutes of the door
- **Prohibited**: the same list as Sheet 16. No stubble gag, no smear, no reveal staging.

### Morning Idle & Invoices (Row 0)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dressing Gown Idle A | (0, 0) | 48x64 | Coffee, glasses, bare feet, far end of the room |
| Dressing Gown Idle B | (48, 0) | 48x64 | Idle loop frame B |
| Bare Feet Shift | (96, 0) | 48x64 | Weight change; the only fidget she gets |
| Coffee Sip | (144, 0) | 48x64 | Unhurried |
| Reading Glasses On | (192, 0) | 48x64 | Work begins |
| Invoice Review | (240, 0) | 48x64 | Going through paper; three invoices track her disposition |

### The Morning After (Row 1)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Table Slide — 80 Sovs Invoice | (0, 64) | 48x64 | Slides the sheet across **without looking up.** No negotiation, no Charm check. |
| Page Turn | (48, 64) | 48x64 | "The kind that happened." Dry and unbothered, never sinister. |
| The Eyebrow, Off-Stage A | (96, 64) | 48x64 | Same two millimetres, no makeup |
| The Eyebrow, Off-Stage B | (144, 64) | 48x64 | Frame B |
| Hand Flat on Table | (192, 64) | 48x64 | She does this before saying anything she actually means |
| The Lift Story | (240, 64) | 48x64 | **Genuine admiration.** "You did, actually. It was extraordinary." The warmest frame she has. |

### Movement & Apartment (Row 2)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Laughing | (0, 128) | 48x64 | Off-stage laugh; the jokes are better here |
| Walk A | (48, 128) | 48x64 | Bare feet, efficient |
| Walk B | (96, 128) | 48x64 | Second walk frame |
| Standing Composed | (144, 128) | 48x64 | Stillness that reads as impatience and is not |
| Points to Front Stairs | (192, 128) | 48x64 | "Front stairs, not the back — the crew are loading in" |
| Unsent Letter — Holding | (240, 128) | 48x64 | Four pages. Examine-only. Not takeable — she notices. |

### Transitional & Branch States (Row 3)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seated, Far End of Room | (0, 192) | 48x64 | Her fixed morning-after position |
| Coffee Pour | (48, 192) | 48x64 | For herself; the guests get Wolfram's pot |
| Corset Off, Gown On | (96, 192) | 48x64 | **The transitional frame** — pairs with Sheet 15's Corset Removal Hall A/B to complete the change on screen with no dialogue |
| Glasses Removed | (144, 192) | 48x64 | End of paperwork |
| **Decline-Branch Idle** | (192, 192) | 48x64 | **Nightcap declined.** Same room, same gown, no makeup on anybody, **coffee table intact so no 80 Sovs invoice frame fires.** Fully supported branch. |
| *(reserved)* | (240, 192) | 48x64 | Held for the eleven-minute horse account, if it gets its own seated pose |

---

## 🛋️ Sprite Sheet 18: The Divas' Apartment (Couchsurf Interior)
**Filename**: `divas_apartment_interior.png`
**Dimensions**: 1024 × 768 pixels
**Tile Size**: 32 × 32 pixels (structure band); object cells as tabled
**Color Palette**: Imperial Oxblood #6E0F1A + Baroque Cream #FFF8DC + Opera House Gold #CFB53B, keyed by Mirror Bulb Warm #FFE9B8

The afterparty and morning-after location. One flight of internal stairs above the backstage corridor — **the same door Otto uses for the smoke-break area, which is why the whole crew has always known.** A real home belonging to two working professionals: good furniture bought over thirty years, two full makeup stations, a hall of shoes, and a kitchen table with a completed crossword on it. **It must not read as a lair, a trap, or a set.** It reads as somewhere people live.

### Structure Tiles — Row 1 (32x32 each)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Parquet Floor | (0, 0) | 32x32 | Herringbone, waxed, decades old |
| Parquet Floor — Worn Path | (32, 0) | 32x32 | Door to kitchen to chaise; thirty years of the same route |
| Persian Rug — Centre | (64, 0) | 32x32 | Good rug, real, worn |
| Persian Rug — Edge | (96, 0) | 32x32 | Border tile |
| Hall Runner | (128, 0) | 32x32 | Leads to the shoes |
| Kitchen Tile | (160, 0) | 32x32 | Small kitchen, well used |
| Wallpaper — Damask, Night | (192, 0) | 32x32 | Lamp-lit state |
| Wallpaper — Damask, Morning | (224, 0) | 32x32 | Daylight state |
| Dado Rail | (256, 0) | 32x32 | Period trim |
| Cornice | (288, 0) | 32x32 | Plaster, chipped in one corner |
| Skirting | (320, 0) | 32x32 | Scuffed at heel height |
| Stair Head — Internal Stair | (352, 0) | 32x32 | Arrives from the backstage corridor |
| Radiator | (384, 0) | 32x32 | Cast iron, painted over |
| Bare Board — Hall | (416, 0) | 32x32 | Unrugged hall floor |

### Structure Tiles — Row 2 (32x32 each)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ceiling Plaster | (0, 32) | 32x32 | Flat fill |
| Ceiling Rose | (32, 32) | 32x32 | Chandelier mount |
| Door Frame Top | (64, 32) | 32x32 | Header tile |
| Threshold | (96, 32) | 32x32 | Room-to-room |
| Kitchen Splashback | (128, 32) | 32x32 | Tiled, 1970s, unrepentant |
| Floorboard Gap | (160, 32) | 32x32 | Detail tile |
| Rug Fringe | (192, 32) | 32x32 | Rug termination |
| Chandelier Chain | (224, 32) | 32x32 | Vertical run |
| Picture Rail | (256, 32) | 32x32 | Hung with framed posters |
| Damp Stain | (288, 32) | 32x32 | One wall, upper corner, unaddressed since 1997 |
| Bookshelf Fill | (320, 32) | 32x32 | Scores and librettos |
| Sheet-Music Stack | (352, 32) | 32x32 | Stacked flat |
| Framed Poster | (384, 32) | 32x32 | Eleven years of DIE, FLEDERMAUS! posters, one per season |
| Hook Rail | (416, 32) | 32x32 | Coats, furs, one dressing gown |

### Doors, Windows & Standing Fixtures (64x96 each)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Apartment Door — Closed | (448, 0) | 64x96 | From the internal stair |
| Apartment Door — Open | (512, 0) | 64x96 | Entry state |
| Hall Arch | (576, 0) | 64x96 | Living room to hall |
| Sash Window — Night, Shuttered | (640, 0) | 64x96 | 01:40 state |
| Sash Window — Morning, Shutters Open | (704, 0) | 64x96 | Late-morning state |
| Sash Window — Morning Light Shaft | (768, 0) | 64x96 | Overlay; the shaft lands across the chaise |
| Full-Length Mirror | (832, 0) | 64x96 | "There was a mirror involved and considerable discussion of 'blending'." |
| Wig Block Stand, Tall | (896, 0) | 64x96 | Floor-standing, occupied |
| Costume Rail — Gowns | (960, 0) | 64x96 | Working wardrobe, protected in bags |

### Furniture (Band B)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chaise Longue — Empty | (0, 96) | 128x96 | Hers, and she would rather not revisit it before eleven |
| Chaise Longue — Three Bros Draped | (128, 96) | 128x96 | Morning-after composite; individually, badly |
| Kitchen Table + Two Chairs | (256, 96) | 128x96 | The crossword table |
| Sideboard — Lacquered | (384, 96) | 128x96 | Where the tray is made |
| Coffee Table — Intact | (512, 96) | 96x64 | 80 Sovs |
| Coffee Table — Destroyed | (608, 96) | 96x64 | Post-lift. Comedic wreckage, not violent wreckage. |
| Armchair — The Good Chair | (704, 96) | 64x96 | Fortissima's |
| Armchair — The Other Good Chair | (768, 96) | 64x96 | Adelheid's |
| Bookcase — Scores & Librettos | (832, 96) | 96x96 | Thirty-one seasons of paper |
| Standard Lamp | (928, 96) | 32x96 | The 03:00 light source |
| Floor Cushion Pile | (960, 96) | 64x64 | Overflow seating |
| Bucket | (512, 160) | 32x32 | By the tall one |
| Blanket, Folded | (544, 160) | 32x32 | She puts blankets on people |
| Blanket, Thrown Over a Bro | (576, 160) | 64x32 | Applied at some point in the night by somebody kind |
| Slippers Pair | (640, 160) | 32x32 | Size 47 |
| Newspaper, Folded | (672, 160) | 32x32 | Crossword source |
| Post Pile | (960, 160) | 64x32 | Includes about two of Helga's letters a year; it is a whole thing |

### The Makeup Stations (Band C) — **the sign the bros compliment as "a really nice vanity setup"**
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Makeup Station 1 (Fortissima) — Unlit | (0, 192) | 128x128 | Six-foot lit mirror, two chairs, thirty-one years of professional kit |
| Makeup Station 1 — Bulbs Lit | (128, 192) | 128x128 | Working state |
| Makeup Station 2 (Adelheid) — Unlit | (256, 192) | 128x128 | Hers, identical to Fortissima's |
| Makeup Station 2 — Bulbs Lit | (384, 192) | 128x128 | Working state |
| Makeup Kit — Open | (512, 192) | 64x64 | Professional, enormous, immaculate |
| Makeup Kit — Closed | (576, 192) | 64x64 | Cased |
| **Shave Kit** | (640, 192) | 64x64 | Badger brush, cut-throat, strop. Immaculate. **Chadwick has assumed it is a paintbrush set.** Rendered plainly; no emphasis, no highlight. |
| Wig Block — Fortissima's Tower | (704, 192) | 64x64 | Name written on the base in marker, older than the wig |
| Wig Block — Adelheid's Sleek Black | (768, 192) | 64x64 | Waved, lace visible |
| Wig Block — Empty | (832, 192) | 64x64 | Styrofoam head, bare |
| Powder & Palette Cluster | (896, 192) | 64x64 | Stage paint, gallery-readable |
| Mirror Bulb — On/Off Pair | (960, 192) | 64x64 | Tileable bulb strip source |
| Makeup Chair — Empty | (512, 256) | 64x64 | Two per station |
| Makeup Chair — Occupied Silhouette | (576, 256) | 64x64 | Background dressing anchor |
| Remover Pad Drift | (640, 256) | 64x32 | Used, dropped, ordinary |
| Hairpin Scatter | (640, 288) | 64x32 | Everywhere, permanently |
| Lipstick Row | (704, 256) | 64x32 | Racked |
| Brush Roll | (704, 288) | 64x32 | Rolled, professional |
| Perfume Cluster | (768, 256) | 64x64 | Good bottles, mostly empty |
| Corset on a Chair Back | (832, 256) | 64x64 | Removed in the hall at one in the morning, mid-conversation |
| Opera Gloves, Discarded | (896, 256) | 64x32 | Elbow length |
| Lorgnette | (896, 288) | 64x32 | On the sideboard, used correctly |
| Fan, Closed | (960, 256) | 64x32 | The compliment-graded fan |
| Fan, Open | (960, 288) | 64x32 | Working state |

### The Nightcap (Band D)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lacquered Tray — Empty | (0, 320) | 96x64 | Black lacquer, good |
| Lacquered Tray — Laid | (96, 320) | 96x64 | **Two small glasses, three tall ones.** The composition is the whole joke and it is never pointed at. |
| Lacquered Tray — Carried | (192, 320) | 96x64 | Adelheid's carry anchor |
| Jägermeister Bottle — Full | (288, 320) | 32x64 | Of no distinction whatsoever |
| Jägermeister Bottle — Half | (320, 320) | 32x64 | Later state |
| Energy Drink Cans — Six, Unopened | (352, 320) | 64x64 | Bought for this, every Saturday, for eleven years |
| Energy Drink Cans — Opened, Scattered | (416, 320) | 64x64 | Morning state |
| Small Glass — Full | (480, 320) | 32x32 | The ladies' |
| Small Glass — Empty | (480, 352) | 32x32 | Drunk |
| Tall Glass — Full | (512, 320) | 32x32 | The guests' |
| Tall Glass — Empty | (512, 352) | 32x32 | Drunk faster |
| Ice Bucket & Tongs | (544, 320) | 64x64 | Household kit |
| Sideboard Surface — Mid-Pour | (608, 320) | 128x64 | **The nine-second state.** Neutral lighting, ordinary staging, no shadow gag, no rack focus, no green key light. It is a person making drinks. |
| Sideboard Surface — Tray Assembled | (736, 320) | 128x64 | Ready to carry |
| Bar Towel | (864, 320) | 32x32 | Over the shoulder |
| Bottle Opener | (864, 352) | 32x32 | Household |
| Chandelier — Apartment, Night | (896, 320) | 64x64 | Small, domestic, gold |
| Chandelier — Apartment, Morning | (960, 320) | 64x64 | Unlit; daylight does the work |
| Record Player — Playing | (0, 384) | 64x64 | Not opera |
| Record Sleeve Stack | (64, 384) | 64x64 | Leaning on the bookcase |
| Karaoke Setup | (128, 384) | 96x64 | "You were charming and you were terrible at karaoke" |
| Camera on Tripod | (224, 384) | 64x64 | Hers. "I am not a MONSTER, I am a DOCUMENTARIAN." |
| Photograph — Face Down | (288, 384) | 32x32 | In a drawer, and they will remain in a drawer |
| Photograph — Face Up | (288, 416) | 32x32 | **Deliberately unreadable at gameplay zoom.** The contents are never shown, ever. |
| Ashtray, Unused | (320, 384) | 32x32 | Prop only |
| Coaster Set | (320, 416) | 32x32 | Because it is her floor |
| Sheet Music Drift | (352, 384) | 64x64 | Across every horizontal surface |
| The Unsent Letter — Four Pages | (416, 384) | 64x64 | Examinable. Not takeable — she notices. |
| Crossword — In Progress | (480, 384) | 32x32 | 3 a.m. state |
| Crossword — Completed in Ink | (480, 416) | 32x32 | Morning state, correct |
| Crossword — 1997, Kept | (512, 384) | 32x32 | Third examine; kept because of a particular clue |
| Pen | (512, 416) | 32x32 | Ink |
| Invoice Stack | (544, 384) | 64x64 | The three-invoice warmth track |
| Invoice — The 80 Sovs Coffee Table | (608, 384) | 64x32 | Single sheet, itemised, correct |
| Invoice — Slid Across Table | (608, 416) | 64x32 | In-motion frame |
| Bread Basket | (672, 384) | 64x64 | "Eat the bread." |
| Coffee Pot & Three Cups | (736, 384) | 96x64 | None of the cups match |
| Water Glasses, Three | (832, 384) | 64x64 | Set out before anybody woke up |
| Aspirin Strip | (896, 384) | 32x32 | Also set out before anybody woke up |
| Sunglasses, Indoors | (896, 416) | 32x32 | Pilsner's |
| Programme in a Jacket | (928, 384) | 64x64 | Bradley's copy. He has read her entry twice. |

### Morning After — The Pillow & Aftermath (Band E)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pillow — Clean | (0, 448) | 64x64 | Night state, and the **decline-branch morning state** |
| **Pillow — Full Face of Makeup Print** | (64, 448) | 64x64 | **The headline prop.** A complete, well-applied stage face transferred to the linen — brow, lash, lip, contour, all of it, in register. It is *their own* makeup, from the other side of the pillow. **Never a smear, never grotesque, never staged as evidence of anything.** It looks like exactly what it is: expensive paint on a pillowcase. |
| Pillow — Makeup Print, Morning-Light Lit | (128, 448) | 64x64 | Same prop under the window shaft; **this is the screenshot frame** |
| Pillowcase Pair, Second Print | (192, 448) | 64x64 | Fainter, on the next pillow along, because there were three of them |
| Cushion — Makeup Transfer | (256, 448) | 64x64 | Chaise cushion, partial |
| Throw Blanket — Tangled | (320, 448) | 96x64 | Somebody was tucked in |
| Bro Sleeping Bundle A | (416, 448) | 96x64 | Lord Pilsner, chaise longue |
| Bro Sleeping Bundle B | (512, 448) | 96x64 | Chadwick, floor, cushion pile |
| Bro Sleeping Bundle C | (608, 448) | 64x64 | Bradley, armchair, upright, dignified, ruined |
| Discarded Shoes, Bros' | (672, 448) | 64x32 | Ordinary trainers; the size contrast with the hall is the gag |
| Discarded Jacket, Bros' | (672, 480) | 64x32 | Programme still in the pocket |
| Bro Face — Full Stage Paint | (736, 448) | 96x96 | Portrait insert. **Very well done.** Applied by them, to each other, with a mirror and considerable discussion of "blending". Not clownish — *competent*, which is funnier. |
| Bro Face — Paint Half-Removed | (832, 448) | 96x96 | Mid-cleanup; "Full Face" status wearing off |
| Bro Face — No Paint | (928, 448) | 96x96 | **Decline branch.** Ordinary hangover face. |
| Coffee Table Debris Field | (0, 512) | 96x64 | Comedic, not violent |
| Splinter Scatter | (96, 512) | 64x64 | 80 Sovs worth |
| Chaise — Cushion Displaced | (160, 512) | 128x64 | Post-lift |
| Rug — Rucked | (288, 512) | 96x64 | The landing was, apparently, stuck |
| Bucket — In Use | (384, 512) | 32x64 | Grateful for it and for her |
| Bucket — Clean | (416, 512) | 32x64 | **Decline branch** |
| Towel Under the One in the Shorts | (448, 512) | 64x64 | Placed pre-emptively, by a professional |
| Empty Cans, Morning Count | (512, 512) | 64x64 | Six |
| Glass, Tipped | (576, 512) | 32x32 | Nobody dropped it; it is just tipped |
| Glass, Upright & Empty | (576, 544) | 32x32 | Adelheid's, on a coaster |
| Makeup Wipes Packet | (608, 512) | 32x32 | Offered, unprompted |
| Hand Mirror, Face-Down | (608, 544) | 32x32 | The instrument of the blending discussion |
| Slipper, One | (640, 512) | 32x32 | The other is elsewhere and stays elsewhere |
| Sock, Nobody's | (640, 544) | 32x32 | Ownership never established; permanent canon |
| Curtain — Drawn | (672, 512) | 64x64 | Night state |

### Lighting States & The Hall (Band F)
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Overlay — Night (01:40) | (0, 576) | 256x192 | Lamp and chandelier warm, deep shadow in corners. **Warm and domestic — no cold key, no green cast, no horror grade.** |
| Overlay — 03:00 Low Lamp | (256, 576) | 256x192 | Standard lamp only; Kranzler at the table with the crossword |
| **Overlay — Morning Light** | (512, 576) | 256x192 | **The morning-after state.** Late-morning sun through an open sash, one hard shaft across the chaise and the pillow, dust in it, everything visible and slightly too bright. Blows out the makeup print at the edges. Warm, kind, and merciless about detail. |
| Hall — Four Pairs of Size 47 Heels | (768, 576) | 128x96 | Custom, four pairs, lined up. Rendered as good shoes, well kept. |
| Hall — Five Pairs | (896, 576) | 128x96 | Adelheid's added; all size 47 and up |
| Hall — Shoes with Bradley In Frame | (768, 672) | 128x96 | **The two-second beat.** He looks. He says nothing. He continues his morning. No reaction frame, no zoom, no sting. |
| Hall — Coat Hooks & Furs | (896, 672) | 64x96 | Hilde holds these during the season |
| Front Door — Out, Front Stairs | (960, 672) | 64x96 | "Front stairs, not the back — the crew are loading in" |

### Environmental Storytelling Notes
- **Nothing in this apartment is a clue and nothing is a trap.** The makeup stations, the wig blocks, the shave kit and the shoes are all present at full size and full clarity because these are two people's ordinary belongings in their own home. The art never highlights, glints, rim-lights or otherwise nudges any of them.
- The eleven framed posters on the picture rail are a season count. A player who reads them learns the show has run eleven years. No character mentions this.
- **Every "morning after" object has a decline-branch counterpart** (clean pillow, clean bucket, intact coffee table, unpainted faces). The decline branch is a fully dressed room, not a stripped one.
- The apartment is **Saturday-only content** and loads with the couchsurf; it never needs to coexist with the boss arena.

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
- **Performance Optimization:** None needed (single NPC)

### Otto's Coffee Sip:
- **Duration:** ~1 second, single play on random interval
- **Frames:** 3
- **Pattern:** Raise → sip → lower, return to idle
- **Trigger:** Timer (random 8–15s), unaffected by chaos state
- **Purpose:** The deadpan constant — destruction rages, Otto sips
- **Audio Sync:** Quiet slurp, deliberately audible in chaos lulls
- **Performance Optimization:** None needed

### Starry Night Backdrop Tear:
- **Duration:** ~0.6 seconds (canvas rip effect, 4 frames at 6-8 FPS)
- **Frames:** 3 backdrop states + 4-frame rip effect overlay
- **Pattern:** Pristine → cape catching → torn (state advance, no loop)
- **Trigger:** Gustav's cape snag scripted event
- **Purpose:** The 400 Sovs, eight-months-of-work destruction centerpiece
- **Audio Sync:** Long fabric-rip sound synced to the diagonal tear; damage popup ching on completion
- **Performance Optimization:** None needed (scripted one-shot)

### Maestro Boss Phase Cycle:
- **Duration:** Attacks 0.7–2.0s each per guidelines (4-8 frames at 4-6 FPS)
- **Frames:** 8 (conducting/chaotic conducting), 6 (crescendo, waltz, DJ, summon), 4 (bass attack, transformation, defeat)
- **Pattern:** Phase-locked rows; transformation plays once between phases
- **Trigger:** Boss AI state machine, tempo-synced to battle music
- **Purpose:** Classical elegance → modern swagger → desperate fusion, each phase a tonal shift
- **Audio Sync:** All attacks beat-matched; Phase 2 bass attack lands exactly on the drop
- **Performance Optimization:** Phase 3 strobe replaced by slow color fade on low-end devices

### Papageno Performing / Feather Bounce:
- **Duration:** ~1 second loop (6 frames at 4-8 FPS)
- **Frames:** 6
- **Pattern:** Dance loop with subtle feather secondary motion
- **Trigger:** Constant while on screen; Guiding Beckon during ally path
- **Purpose:** The one performer who never breaks character, even mid-catastrophe
- **Audio Sync:** Panpipe phrase on performing loop start
- **Performance Optimization:** Feather secondary motion disabled on low-end

### Destruction Effects (Feathers / Gold Flakes / Dust):
- **Duration:** 0.5–0.7 seconds each (4 frames at 6-8 FPS)
- **Frames:** 4 each
- **Pattern:** Single play, spawned per destruction event
- **Trigger:** Prop destruction events
- **Purpose:** Sells impact and cost — every puff of dust is money
- **Audio Sync:** Crash + register ching with rising SOVS damage popup
- **Performance Optimization:** Cap concurrent effect instances at 4 on low-end

### Fortissima's Curtain Call (Sheet 14, Row 2):
- **Duration:** ~2.0 seconds, single play (4 frames at 2 FPS, final frame held)
- **Frames:** 4 (arms wide → wig lifted → wig held out → wig-off bow)
- **Pattern:** State advance, no loop; holds on the wig-off bow until the scene ends
- **Trigger:** End of DIE, FLEDERMAUS!, Saturday performance only
- **Purpose:** **The location's central visual gag, delivered entirely without dialogue.** A triumph, not a reveal.
- **Audio Sync:** Genuine ovation, twelve hundred people, mixed as an ovation. **If it plays as a gag the scene is broken.**
- **Performance Optimization:** Crowd layer pre-rendered; no per-audience-member logic

### The Eyebrow (Sheet 15, Row 1):
- **Duration:** ~0.4 seconds, single play, returns to idle
- **Frames:** 2
- **Pattern:** Rest → raised (two millimetres) → rest
- **Trigger:** Any bro line Adelheid declines to dignify; also the direct-flirtation branch
- **Purpose:** Ends most conversations in this building. **Highest-reuse animation on the diva sheets.**
- **Audio Sync:** None. Silence is the joke.
- **Performance Optimization:** None needed

### The Nightcap Sequence (Sheets 14/15/18):
- **Duration:** ~14 seconds total scripted sequence
- **Frames:** Sideboard turn (2f loop, ~9s) → tray carry (1f) → glass handoff ×3 (2f each) → prost count (1f held) → laugh frame (1f) → fade
- **Pattern:** Fixed scripted sequence, plays once per playthrough, **co-owned by both diva profiles**
- **Trigger:** Accepting the tray in the apartment, ~01:40 Saturday
- **Purpose:** The afterparty's one scripted beat
- **Audio Sync:** Room tone and conversation only. **No sting, no stinger chord, no downbeat on the sideboard turn.** "PROST!" on the raised-glass frame.
- **Performance Optimization:** None needed
- **⚠️ Staging rails (binding):** the camera does not cut away from the sideboard and does not linger on it; there is no slow-motion, no rack focus, no colour shift, and no lingering on the tray. **The last frame before the cut to black is a host laughing.** If any part of this reads as menace it has drifted off spec and must be pulled back to farce.

### The Morning Page Turn (Sheets 16/17):
- **Duration:** ~1 second, single play on dialogue advance
- **Frames:** 2 each (Kranzler page turn; Brandtner page turn / table slide)
- **Pattern:** Plays on each morning-after line; **neither character looks up**
- **Trigger:** Morning-after dialogue nodes
- **Purpose:** Two people going about their Sunday morning while three guests reconstruct a night they cannot remember
- **Audio Sync:** Paper, a cup on a saucer, nothing else
- **Performance Optimization:** None needed

### The Off-Stage Transition (Sheets 14 → 13 → 16, and 15 → 17):
- **Duration:** Not animated as a sequence; delivered as three static states the player encounters in order across the evening
- **Frames:** Stage (128×160 / 48×80 full costume) → backstage turn (wig off, gown on) → off-stage (48×64, cardigan / dressing gown)
- **Pattern:** State swap on zone and time-of-day change; never a morph, never a transformation effect
- **Trigger:** Curtain call → dressing room 23:30 → apartment 01:30
- **Purpose:** **The stage/off-stage gag must be legible from silhouette scale alone.** Sheet 14 is 128×160; Sheet 16 is 48×64. Same person, four hours apart, and the player understands it without one line of dialogue.
- **Audio Sync:** None — and the VO does not change register between states, which must be stated to the VO director
- **Performance Optimization:** State swap is a texture change, not geometry

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Destructible prop outlines | set at sheet layout | per prop | High-contrast silhouettes marking what Gustav can (will) destroy |
| Papageno ally highlight | set at sheet layout | 48×80 | Bold outline for the follow-the-bird-man guidance path |
| Boss telegraph outlines | set at sheet layout | 64×80 | Enhanced-visibility windup silhouettes for all Maestro attacks |
| Hidden panel door marker | set at sheet layout | 32×64 | Discoverable-contrast variant of the lobby's hidden panel |
| Apartment interactable outlines | set at sheet layout | per object | High-contrast silhouettes for the couchsurf examinables: door plates, wig blocks, makeup stations, hall shoes, unsent letter, crossword |
| Makeup-print pillow outline | set at sheet layout | 64×64 | The print must stay readable against pale linen at low-vision contrast settings — it is the morning-after's key visual |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Phase 3 strobe replacement | set at sheet layout | full arena | Slow two-color fade replacing tempo-synced strobe |
| Static chandelier sparkle | set at sheet layout | 64×64 | Non-glinting chandelier variant |
| Reduced Bassline color cycle | set at sheet layout | full arena | Single-hue wash replacing #FF00FF → #00FFFF → #FFFF00 cycling |
| Static makeup-mirror bulbs | set at sheet layout | 64×64 | Non-flickering variant of the makeup-station bulb strip |
| Instant Nightcap cut | set at sheet layout | full screen | Straight cut to black replacing the timed fade, for players who find slow fades disorienting; **scene content is identical either way** |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Beat-drop indicator | set at sheet layout | 32×32 | Pulsing bass glyph telegraphing Phase 2 drops for rhythm play |
| Fabric-rip streak | set at sheet layout | 48×16 | Directional tear glyph accompanying the backdrop rip audio |
| German exclamation burst | set at sheet layout | 32×24 | Speech-shock glyph over Hoffmann and Adelheid outbursts |
| Crash/ching burst | set at sheet layout | 32×32 | Impact star + damage numeral for every destruction sound. **No currency glyph** — the word `SOVS` is lettered in the damage popup, not here. ⚠️ 32×32 cannot hold `SOVS` beside the star; widen to 48×32 if the word must appear in the burst itself. |
| Ovation glyph | set at sheet layout | 48×24 | Applause indicator for the DIE, FLEDERMAUS! curtain call. **Must read as enthusiastic, never as laughter.** |
| "PROST!" glyph | set at sheet layout | 48×24 | Toast burst on the raised-glass frame of the Nightcap |
| Projection marker | set at sheet layout | 24×24 | Volume indicator distinguishing Fortissima's stage projection from Kranzler's conversational register. **Same voice, two volumes** — the glyph size is the only thing that changes between states. |

### Colorblind Considerations:
- Boss phase changes are signaled by costume state (tails / headphones / open shirt), never lighting color alone
- Status icons (Cultured Presence, Artistic Guilt, Star Quality, Full Face) use distinct silhouettes, not just tint
- The "Full Face" cosmetic is signalled by **facial paint pattern**, not hue shift, so it reads on every colour profile
- Touch zones minimum 44px for box office, gift shop, apartment examinables, and dialogue choice panels

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) lobby tileset gilding and boss sheet need uncompressed
- **Fallback:** PNG high quality for the starry backdrop (its hand-painted stars are plot-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| opera_lobby | lobby tileset, lobby staff, UI | 1024x1024 |
| opera_backstage | backstage tileset, backdrop, destructible props | 1024x1024 |
| opera_principals | Hoffmann, Otto, Adelheid, Papageno | 1024x1024 |
| opera_boss | Maestro von Strauss | 1024x1024 |
| opera_effects | effects & particles | 512x512 |
| opera_divas | Fortissima diva + dragshow, Adelheid dragshow, Kranzler offstage, Brandtner offstage | 1024x1024 |
| opera_apartment | divas' apartment interior | 1024x1024 |

*(Seven atlases at 1024px; max atlas size 2048x2048 for broad GPU compatibility. **Peak concurrent atlas count remains five**, per the original spec: `opera_divas` and `opera_apartment` are Saturday-only, load with the couchsurf interior, and unload with it — they never need to coexist with `opera_boss`, which is Bassline-night content. The five diva sheets pack into a single 1024×1024 with room to spare: 512×640 left column, 384×384 + 384×320 right column, 288×256 ×2 below.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full particle set (80), chandelier sparkle, strobe/color cycling, feather secondary motion |
| Medium | 40 particles, no chandelier sparkle, simplified color cycling |
| Low | Static lighting, minimal particles (destruction one-shots only), no shaders |

### Performance Targets:
- **Target FPS:** 60 on min-spec hardware
- **Max Draw Calls:** Under 50 for full location
- **Memory Footprint:** Under 50 MB for all zones loaded
- **Particle Limit:** 80 simultaneous

### Performance Notes:
- Zone loading enabled: lobby, auditorium, backstage, dressing rooms, orchestra pit, and the divas' apartment load independently
- Bassline transformation swaps lighting presets, not geometry — one texture state change at 23:00
- Boss arena caps concurrent add-summon sprites during Encore phase
- **The divas' apartment is a discrete interior reached by the internal stair.** It streams in on transition and unloads on exit, so its two atlases never add to the peak resident set. The apartment's three lighting overlays (night / 03:00 low lamp / morning) are texture swaps on one CanvasModulate, not re-lit geometry.
- Stage → backstage → off-stage diva states are texture swaps on a shared AnimatedSprite2D per character; no rig change, no morph, no shader.

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap per zone; AnimatedSprite2D for all NPC/boss states; CPUParticles2D (not GPU) for feathers, dust, gold flakes
- Location state machine: normal / rehearsal / performance / bassline / fiaker_fiasco_chaos / dragshow_saturday / apartment_nightcap / apartment_morning / post_quest drives sprite and lighting swaps
- Diva persona state is a **separate enum** from location state (`stage` / `backstage` / `offstage`) and drives the Sheet 14 → 13 → 16 and Sheet 15 → 17 texture swaps independently of time of day
- Boss fight uses a tempo-sync controller: attack animation triggers quantized to battle-music BPM
- CanvasLayer for the shared Fiaker Fiasco damage-counter UI

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Backdrop tear | Long fabric rip + damage ching | Synced to diagonal tear frames |
| Prop destruction | Crash + cash-register ching | On impact frame, "N SOVS" popup rises |
| Maestro Phase 2 bass attack | The drop | Beat-matched, hands-raised frame on downbeat |
| Phase 3 strobe | Battle music tempo | Strobe flashes quantized to BPM |
| Hoffmann horror | German exclamation | On horror frame 1 |
| Papageno performing | Panpipe phrase | On loop start |
| Curtain-call wig removal | Genuine ovation, twelve hundred people | Swells on the wig-lifted frame, peaks on the wig-held-out frame. **Mixed as an ovation, not a laugh.** |
| Nightcap sideboard turn | Room tone and conversation only | **No sting, no chord, no downbeat.** Deliberately unscored. |
| Nightcap prost | "Drei — zwei — eins — PROST!" + glass clink | On the raised-glass frame |
| Nightcap fade to black | Music continues under, unaltered, and fades with the picture | **No stinger on the cut.** |
| Morning page turn | Paper, cup on saucer | On each morning-after dialogue advance |
| 80 Sovs invoice slide | Single sheet on wood | On the table-slide frame |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Fiaker Fiasco phase 3 | Backstage tileset damage states, destructible props, backdrop states, Hoffmann/Otto/Adelheid/Papageno sets | Gustav auto-enters via alley; 2,000 Sovs backstage damage tracked to `fiaker_fiasco_damage_sov` |
| Maestro boss fight (main quest) | Boss sheet all phases, arena lighting states | Orchestra pit, Bassline configuration, 23:00–04:00 |
| Waltz of the Bros | Auditorium configuration, patron NPCs | Rival rhythm-battle encounter |
| Prima donna negotiation | Adelheid outrage/dismissive sets, torn costume variant | 500 Sovs demand, negotiable to 200 Sovs at Charm 4 |
| **DIE, FLEDERMAUS! (Saturdays)** | Sheets 13, 14, 15; marquee dressing; auditorium performance configuration; ovation crowd layer | Saturday 19:00–22:00; curtain call fires the wig-removal sequence; backstage passes gate the wings |
| **"The Ladies of the House" couchsurf** (`sinfonia_couchsurf_opera_divas_01`) | Sheets 13–18 in full; apartment lighting overlays; Nightcap prop set; morning-after prop set **and its complete decline-branch counterpart set** | Saturday 01:30+, backstage passes required. Quest doc: `Design/Quests/Location Specific/Sinfonia/couchsurfingchroniclessinfonia.md` |
| Fortissima compliment-grading / hint trade | Sheet 13 Compliment Graded frame (the fan closes) | Prop-room hints and the Backstage Labyrinth shortcut |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Opera House Plaza | Adjacent main entrance; Gustav sprite arrives with café feathers on cape; Hans-Jürgen may appear at resolution; shared damage-counter UI | Main-door transition |
| Café Sachertorte | Incoming quest path via alley | Alley auto-entry during Fiaker Fiasco |
| Stadtpark (Gustav's Refuge) | Outgoing quest path; Gustav continues (even more disheveled); Papageno sprite if ally path; Hoffmann may pursue in fury state | Side-door path to the park |
| The Black-Tie Backroom | Hidden entrance from lobby/backstage (hidden panel, prop corridor) | Concealed-door transition |
| Hidden Baroness Ballroom | Unlocked via boss-reward vault keys | Late-game key transition |
| **The Divas' Apartment** (this document, Sheet 18) | Internal stair off the backstage corridor — **the same door Otto uses for the smoke-break area** | Stair transition, Saturday only, backstage passes required |
| Haute Couture Haberdashery | `item_gold_circle_coin` lifts the party-wide `the_herp` couchsurf interception before any Sinfonia couchsurf, including this one | No shared sprites; state gate only |

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
- The torn starry backdrop remains visibly repaired post-quest — the 2,000 Sovs never quite disappears
- **The marquee is the location's largest piece of environmental storytelling.** "DIE, FLEDERMAUS! — *A Night of Grand Opera, Performed Entirely by the Ladies of the House*", four feet high, on Saturdays, with the party walking under it. It is never framed, highlighted, or lingered on. It is simply legible.
- **The two brass door plates** — W. KRANZLER on Room 1, L. BRANDTNER on Room 2, each with a taped or framed card underneath giving the stage name — are ordinary props at ordinary size, rendered so the player can read them and the bros can lean on them
- **The apartment is a home, not a set.** Eleven framed season posters, a damp stain nobody has dealt with since 1997, mismatched coffee cups, and two full professional makeup stations, all present at full clarity and none of them highlighted

### Character Integration Notes:
- Otto's calm is a rendering rule: his sprite never gains reaction frames, whatever happens in the scene
- Papageno's feathers get subtle secondary animation; he reads as theatrical even at idle
- Boss phases are costume-first: readable at silhouette level before any lighting change
- **The divas are scale-first.** The whole stage/off-stage gag is carried by cell geometry: Fortissima is 128×160 on stage (Sheet 14), 96×128 backstage (Sheet 13), and 48×64 in a cardigan (Sheet 16). Adelheid is 48×80 in jet and silver (Sheet 15) and 48×64 in a dressing gown (Sheet 17). **A player who mutes the game must understand the transformation from the sprites alone.**
- **The divas must read as great performers in every stage frame.** No cheap visual joke is permitted anywhere on Sheets 13–18: no five o'clock shadow, no comedy stubble, no smeared lipstick, no "man in a dress" staging, no wink to camera. The curtain-call wig removal is a **triumph frame**, staged as a bow.
- Wig lace, adam's apples, the shave kit and the size 47 shoes are rendered plainly and never emphasised. **They are visible because these characters do not hide them, not because the art is winking.**
- **The Nightcap never renders as menace.** No shadow gag on the sideboard, no rack focus, no colour shift, no lingering on the tray, no slow-motion. Warm domestic lighting throughout, and the last frame before the cut is a host laughing.
- **The decline branch is fully dressed art, not a stripped room.** Every morning-after prop has a clean counterpart on Sheet 18 and a decline-branch idle on Sheets 16 and 17. A player who says no sees a complete scene.

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

### Divas' Apartment Lighting (Sheet 18 overlays)
- **Night (01:40)**: Small domestic chandelier plus standard lamp, warm gold (#FFD9A0), 65% intensity, deep shadow in the corners. **Warm and domestic — no cold key, no green cast, no horror grade, at any point in the Nightcap.**
- **03:00 Low Lamp**: Standard lamp only (#FFC98A), 35% intensity, one pool of light on the kitchen table where Kranzler is doing the crossword
- **Morning**: Late-morning sun through an open sash (#FFF3D6), 100% intensity, one hard shaft across the chaise and the pillow, visible dust. Blows out the edges of the makeup print. **Warm, kind, and merciless about detail.**
- **Makeup Station Bulbs**: 2 bulb strips at Mirror Bulb Warm (#FFE9B8), 90%, with a static non-flickering accessibility variant
- **Hall**: Unlit in every state. The four pairs of size 47 heels are lit only by spill from the living room, and the art never adds a light to them.

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Gustav on stage** during "Der Hölle Rache"—horse interrupting opera
2. **Damage counter hitting 2,000 Sovs**—with destruction visible
3. **Director's breakdown**—sitting on floor, thousand-yard stare
4. **Papageno befriending Gustav**—bird-man and horse bonding
5. **Otto sipping coffee**—completely unfazed during chaos
6. **The marquee**—"DIE, FLEDERMAUS!" four feet high with three Americans walking under it, one of them reading it out loud, correctly, with the comma
7. **The curtain call**—the wig held out at arm's length, twelve hundred people on their feet
8. **The Nightcap tray**—two small glasses, three tall ones, and a bottle of Jägermeister on black lacquer under a domestic chandelier
9. **The morning after**—three men in full professional stage makeup on a chaise longue, and a 58-year-old in a cardigan doing the crossword behind them
10. **The pillow**—a complete, well-applied stage face printed on white linen, in the morning light shaft
11. **The hall**—four pairs of size 47 heels, with Bradley in frame, deciding not to
12. **The 80 Sovs invoice** sliding across the table, in focus, three ruined men out of focus behind it

### Quote Potential:
- "I studied at the Conservatory..." - Regisseur Hoffmann (breakdown pose)
- "*sips coffee*" - Otto (deadpan during destruction)
- "I sang at La Scala!" - Prima Donna Adelheid (outrage pose)
- "Follow the bird-man!" - Papageno (guiding pose)
- "It is a JÄGERBOMB, my darling, and it is BENEATH ME, and I have one every week." - Madame Fortissima (Nightcap pour pose)
- "I am not a MONSTER, I am a DOCUMENTARIAN." - Madame Fortissima (camera-on-tripod prop in frame)
- "Bro, she did a COSTUME CHANGE. During the BOWING." - Chadwick (curtain-call frame)
- "The kind that happened." - Prima Donna Adelheid (page-turn pose)
- The comma. The entire marquee gag is one comma and the internet will find it.

---

## 📋 Required PNG Files (18 Total)

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
| 13 | madame_fortissima.png | 384x384 |
| 14 | madame_fortissima_dragshow.png | 512x640 |
| 15 | npc_prima_donna_adelheid_dragshow.png | 384x320 |
| 16 | npc_wolfram_kranzler_offstage.png | 288x256 |
| 17 | npc_lorenz_brandtner_offstage.png | 288x256 |
| 18 | divas_apartment_interior.png | 1024x768 |

**Total Estimated Memory:** ~16.1 MB (uncompressed RGBA) — 4,227,072 px × 4 bytes = 16,908,288 bytes. Sheets 1–12 account for ~10.3 MB (unchanged); Sheets 13–18 add ~5.8 MB. **Still well inside the <50 MB all-zones budget**, and the apartment's two atlases are Saturday-only and unload on exit, so resident memory during the boss fight is unchanged.

**Sheet 13 reconciliation:** `madame_fortissima.png` was specified in `bassline_opera_house.md`'s PNG Asset Requirements Summary (`96x128 - Principal soprano`) but was **missing from this document**. It is now Sheet 13. The 96×128 figure is the **sprite cell size**; the sheet is 384×384 (4 × 3 cells). This document is authoritative for sheet dimensions — the same divergence already exists for `boss_maestro_von_strauss.png` (256x384 in that summary, 512×640 here). Flag raised in `npcs/Bassline_Opera_House/npc_madame_fortissima.md` → Development Status is hereby closed.

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
- [ ] `madame_fortissima.png` (384x384) — cells 96x128
- [ ] `madame_fortissima_dragshow.png` (512x640) — cells 128x160
- [ ] `npc_prima_donna_adelheid_dragshow.png` (384x320) — cells 48x80
- [ ] `npc_wolfram_kranzler_offstage.png` (288x256) — cells 48x64
- [ ] `npc_lorenz_brandtner_offstage.png` (288x256) — cells 48x64
- [ ] `divas_apartment_interior.png` (1024x768) — 32x32 structure tiles + tabled object cells

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
- **Documentation:** Animation timing reference sheet + boss tempo-sync cue sheet + **a side-by-side stage/off-stage contact sheet for both divas** (Sheet 14 next to Sheet 16; Sheet 15 next to Sheet 17), used to sign off that the transformation reads without dialogue

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 18 PNG files match exact dimensions specified
- [ ] All cell coordinates on Sheets 13–18 are non-overlapping and within their stated sheet bounds (top-left origin, no sheet exceeds 2048px on either axis)
- [ ] Color palette matches hex codes exactly
- [ ] Backdrop tear reads as dramatic-but-comedic at gameplay zoom
- [ ] Otto's sprite shows zero reaction frames across all states
- [ ] Boss phases readable at silhouette level (costume-first)
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Diva Sheet Sign-Off (Sheets 13–18) — **all boxes must be ticked before these sheets ship**:
- [ ] **The stage/off-stage transformation reads with the sound off and no dialogue on screen.** Verified against the side-by-side contact sheet.
- [ ] Both divas read as **great performers** in every stage frame. The curtain-call ovation is believable.
- [ ] The curtain-call wig removal is staged as a **bow / triumph frame**, never as a reveal frame
- [ ] **Zero cheap visual jokes anywhere on these sheets**: no five o'clock shadow, no comedy stubble, no smeared lipstick, no "man in a dress" staging, no wink to camera
- [ ] Wig lace, adam's apples, the shave kit and the size 47 shoes are rendered plainly, at ordinary size, with **no highlight, glint, rim-light or framing emphasis**
- [ ] The Nightcap sequence contains **no menace staging**: no shadow gag, no rack focus, no colour shift, no slow-motion, no lingering on the tray
- [ ] The last frame before the fade to black is a **host laughing**
- [ ] Morning-after aftermath is **cosmetic and comedic only** — makeup, a hangover, a bucket, a broken coffee table. Nothing on any sheet depicts or implies distress, injury, or fear.
- [ ] **The decline branch is fully dressed**: clean pillow, clean bucket, intact coffee table, unpainted faces, and a decline-branch idle for both off-stage hosts. **No art asset gates content behind the Nightcap.**
- [ ] The photograph prop is **unreadable at gameplay zoom** in every state
- [ ] The marquee and both brass door plates are legible at gameplay zoom and **never highlighted**
- [ ] The apartment reads as a **home**, not a lair or a set

### Quality Checkpoints:
- [ ] Satirical theme (cultural pretension vs. chaos) clear throughout all assets
- [ ] The satire lands on the **tourists**, never on the performers, opera, or drag performance
- [ ] Hidden panel / prop corridor have discoverable visual cues
- [ ] Apartment stair entrance (shared with Otto's smoke-break door) has a discoverable visual cue
- [ ] Performance optimized (CPU particles, atlas limits respected, apartment atlases stream and unload)
- [ ] Touch zone sizing considered (44px minimum for interactive elements, including all apartment examinables)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Vienna State Opera evoked as reference, never named in-world |
| Cultural Specificity | ✅ | Opera-house hierarchy, Magic Flute production culture, EDM night economy, an eleven-year sold-out drag headline show that the whole city knows about |
| Satirical Targets Appropriate | ✅ | Opera snobbery, artistic self-importance, institutional pretension — punches up. **The diva sheets target three American tourists failing to read a four-foot marquee, a standing ovation and two brass door plates; drag performance, opera and the performers themselves are rendered with complete respect and are the most competent thing in the building.** |
| Seedy Underbelly Present | ✅ | Bassline underground nights, hidden gambling-den entrance, scalped prestige |
| Gameplay Value Established | ✅ | Story hub, boss arena, rhythm battle, quest phase 3, shop/box office, Saturday drag show + couchsurf interior |
| Technical Feasibility | ✅ | 18 sheets, 7-atlas plan (peak concurrent 5), zone loading incl. streamed apartment, LOD tiers documented |
| Performance Budget | ✅ | 60 FPS, <50 draw calls, ~16.1 MB of sheets against a <50 MB budget, 80 particles |
| Accessibility Features | ✅ | Visual audio cues (incl. ovation and PROST glyphs), strobe replacement, static makeup bulbs, instant-cut fade option, telegraph outlines, apartment examinable outlines |
| No Crypto Elements | ✅ | None present |
| Social Media Integration | ✅ | Twelve screenshot moments and nine quotable poses identified |
| **Tone Rails Held (Sheets 13–18)** | ✅ | Divas never villainous or predatory; bros never distressed; aftermath cosmetic and comedic only; **decline branch fully dressed and gates nothing**; nothing on any sheet explains the show to the bros |
| **Stage/Off-Stage Legibility** | ✅ | Carried by cell geometry (128×160 → 96×128 → 48×64) and palette, verified by a required side-by-side contact sheet, **with no dialogue involved** |
| **`madame_fortissima.png` Reconciled** | ✅ | Previously specified in `bassline_opera_house.md` and absent here; now Sheet 13 at 384×384 with 96×128 cells, with the summary/document divergence documented and this document declared authoritative |

**The Bassline Opera House: Where 400 years of cultural excellence meets one horse in a cape, one method-acting bird-man, 2,000 Sovs in Magic Flute production costs, and three Americans who read the marquee out loud and understood none of it.**
