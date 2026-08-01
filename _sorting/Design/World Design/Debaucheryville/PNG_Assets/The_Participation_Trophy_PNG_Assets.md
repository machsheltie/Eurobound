# The Participation Trophy - Complete PNG Asset Requirements

## 📋 Overview
The Participation Trophy is the prize redemption booth where the Cirque du Shady's rigged-game economy comes to die: the player converts €25 of failure into 85 tickets, and Yolanda converts 85 tickets into a half-smoked cigar. This document specifies every PNG for the peeling booth, the four-tier prize wall (Grand Prizes: display only, don't ask), the full garbage catalog, and Yolanda's dead-eyed professionalism — including the rarest sprite in the location, her almost-smile.

**Location ID:** `debaucheryville_circus_participation_trophy_01`
**Theme:** Carnival prize economics and "everyone's a winner" hollow victories — "You Tried! Here's Proof!"
**Zone:** The Cirque du Shady (circus grounds)
**Hours:** Whenever the circus is open (varies, check Cirque du Shady hours)
**Primary Function:** Prize redemption booth — ticket sink, garbage-tier item vendor, Frequent Loser progression, Bravado interactions, four side quests

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Faded Carnival Red | #CD5C5C | Booth stripes, peeling paint |
| Depressing Yellow | #F0E68C | Banner, prize tags, harsh lighting |
| Worn Canvas | #D2B48C | Booth fabric, background |
| Regret Purple | #9370DB | Shadow tones, tier accents |
| Ticket Orange | #E8A33D | Tickets, redemption UI |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/participation_trophy/
├── environment/
│   ├── trophy_booth.png
│   └── prize_wall.png
├── objects/
│   └── prize_items.png
├── npcs/
│   ├── yolanda.png
│   └── circus_npcs.png
├── effects/
│   └── trophy_effects.png
└── ui/
    └── trophy_ui.png
```

---

## 🎪 Sprite Sheet 1: The Booth
**File:** `trophy_booth.png`
**Dimensions:** 512x512 pixels

### Booth Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Booth Structure Full | (0, 0) | 384x320 | Weathered carnival booth, questionable structural integrity |
| Counter Front | (0, 320) | 256x96 | Where dreams become garbage |
| "Smile! You 'Won'!" Sign | (256, 320) | 96x32 | Counter placard, quotation marks load-bearing |
| Ticket Counting Station | (256, 352) | 96x64 | Worn counting tray, Yolanda's domain |

### Signage Suite:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Door (Warehouse of Sadness) | (384, 0) | 96x128 | Where Yolanda retreats to sigh |
| Faded Main Sign | (384, 128) | 128x48 | "THE PARTICIPATION TROPHY" in faded carnival letters |
| "EVERYONE'S A WINNER!" Banner | (384, 176) | 128x48 | Technically true, spiritually false |
| Redeem Arrow Sign | (384, 224) | 128x32 | "REDEEM YOUR TICKETS HERE" — arrow pointing to sadness |
| Fine-Print Sign | (384, 256) | 128x32 | "All Prizes Are Final. No Refunds. No Complaints. No Hope." |
| Handwritten Sign | (384, 288) | 128x32 | "Yes, these are the GOOD prizes" |

### Booth Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Peeling Paint Decals | (384, 320) | 64x64 | Overlay flakes for the structure |
| Sad Bunting | (384, 384) | 128x32 | Once-festive triangles, now beige |
| Back Storage Interior | (384, 416) | 128x96 | Boxes labeled by disappointment tier, source of the smell |
| Harsh Booth Light Cone | (0, 416) | 128x96 | Unflattering for prizes AND customers |
| Storage Boxes | (128, 416) | 128x96 | "PARTICIPATION — BULK" stenciled crates |
| Counter Bell | (256, 416) | 32x32 | Ding for service; Yolanda hears, chooses her pace |
| Tip Jar (Empty) | (288, 416) | 32x32 | Has never contained a tip |
| Yolanda's Stool | (256, 448) | 32x64 | Seven years of sitting |
| Sigh Retreat Curtain | (320, 416) | 64x96 | Between counter and warehouse |

---

## 🏆 Sprite Sheet 2: The Prize Wall
**File:** `prize_wall.png`
**Dimensions:** 512x512 pixels

### The Illusion, Shelved:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grand Prize Shelf (Top) | (0, 0) | 512x128 | Never actually won, display only |
| "Good" Tier Shelf | (0, 128) | 512x96 | Technically obtainable, practically impossible |
| Consolation Shelf | (0, 224) | 512x96 | What you're actually getting |
| Participation Floor Bins | (0, 320) | 512x96 | The real inventory, at ankle height |

### Grand Prize Close-Ups (Display Only):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Legendary Golden Hamster | (0, 416) | 48x48 | Not real gold. Painted. Badly. 10,000 tickets |
| "Winner" Championship Belt | (48, 416) | 64x48 | On display since 2003 |
| Lifetime Circus Pass | (112, 416) | 48x48 | Theoretically exists |
| Ringmaster's Actual Cane | (160, 416) | 32x64 | 15,000 tickets; Vance would notice |
| "Just Ran Out" Card | (192, 416) | 96x32 | Management's contingency sign |
| Ticket Cost Tag Strip | (288, 416) | 192x32 | 10 / 100 / 500 / 1,000 / 10,000 shelf tags |

### Wall Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Display Glass Glare | (192, 448) | 96x64 | Grand-shelf case reflection overlay |
| Dust Overlay Tile | (288, 448) | 64x64 | Accumulated years, tileable |
| Cobweb Corner | (352, 448) | 64x64 | Grand shelf corner detail |
| Broken Spotlight | (416, 448) | 64x64 | Aimed at the Golden Hamster, dead bulb |

### Technical Notes:
- Grand shelf items never enter inventory — display-only regions with examine text
- Dust and cobweb overlays only on the top two shelves; the participation bins see heavy turnover
- Shelf tags must be legible at examine zoom: the math IS the content

---

## 🗑️ Sprite Sheet 3: Prize Catalog
**File:** `prize_items.png`
**Dimensions:** 256x256 pixels

### Participation Tier (10-50 Tickets):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Half-Smoked Cigar | (0, 0) | 24x24 | The classic. Previous owner had somewhere to be |
| Plastic Kazoo | (32, 0) | 24x16 | Makes noise. That's it. That's the prize |
| Single Playing Card (7 of Clubs) | (64, 0) | 16x24 | The rest of the set is somewhere else. Forever |
| Broken Glow Stick | (96, 0) | 24x24 | It worked once. That time has passed |
| Deflated Balloon Animal | (128, 0) | 32x24 | Was a dog. Or a giraffe. Hard to tell now |
| Mystery Sticker | (160, 0) | 16x16 | Might be lucky. Probably isn't |
| Used Glitter Hat | (192, 0) | 32x32 | Someone had a good time in this once. The glitter remembers |
| Knockoff Sunglasses | (224, 0) | 32x16 | They say "Rayban" if you don't look closely |

### Consolation & "Good" Tier:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mystery Meat Corndog | (0, 32) | 24x32 | The mystery is IF meat |
| Plastic Trophy (Participation) | (32, 32) | 32x48 | "First Place in Showing Up." Your name isn't on it |
| Questionable Stuffed Animal | (64, 32) | 32x32 | The eyes follow you. That's just how it was made. Probably |
| Circus Souvenir Mug | (96, 32) | 32x32 | Drink from where the clowns drink |
| The Big Stuffed Bear | (128, 32) | 48x48 | Actually decent. How did you get this many tickets? Concerning |
| Cirque du Shady T-Shirt | (176, 32) | 32x32 | "Circus Survivor" — is that a brag? Unclear |
| Glowing Novelty Sword | (208, 32) | 32x48 | Looks cool. In the dark. If you squint |

### Premium Garbage (Frequent Loser Only):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ringmaster's Cane (Replica) | (0, 80) | 24x48 | Don't let Vance see you with this |
| Hamstradamus Bobblehead | (32, 80) | 32x32 | The real one would be offended. Don't show him |
| Vintage Circus Poster | (64, 80) | 32x48 | From back when this place had dignity. Allegedly |
| Yolanda's Recommendation Box | (96, 80) | 32x32 | Unmarked box — random but actually decent item |
| The "Good" Mystery Meat | (128, 80) | 24x32 | From a better batch. Don't ask what "better" means |

### Tickets & States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ticket (Single) | (160, 80) | 24x16 | Pure loss, converted to paper |
| Ticket Strip | (184, 80) | 48x16 | A fan of five |
| Ticket Pile | (184, 96) | 48x32 | The 85-ticket moment |
| Prize Bag | (0, 128) | 32x32 | "CONGRATULATIONS" printed crooked |
| Corndog (Bitten) | (32, 128) | 24x32 | Commitment made |
| Corndog (Regretted) | (64, 128) | 24x32 | Nausea roll failed |
| Kazoo Sound Lines | (96, 128) | 32x16 | Annoying nearby NPCs, visualized |
| Sticker (Applied) | (128, 128) | 16x16 | Random +1 spent |
| Glitter Shed Pile | (160, 128) | 32x16 | The hat gives back |
| Balloon (Fully Flat) | (192, 128) | 32x24 | Final form |
| Sword Glow (Night) | (224, 128) | 32x48 | +15 Style, after dark, squinting |

---

## 👩 Sprite Sheet 4: Yolanda Kovarik
**File:** `yolanda.png`
**Dimensions:** 256x384 pixels

### Counter Service Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Yolanda Neutral | (0, 0) | 64x96 | Professional neutrality hiding existential weariness |
| Counting Tickets | (64, 0) | 64x96 | "...I see." |
| Presenting Prize | (128, 0) | 64x96 | Cigar handoff with dead-eyed ceremony |
| Gesturing at Bottom Shelf | (192, 0) | 64x96 | "Anything down there." |

### Character Beats:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| The Sigh (Mid-Retreat) | (0, 96) | 64x96 | Turning toward the curtain |
| Almost-Smile | (64, 96) | 64x96 | Rarest achievement, rarest sprite |
| Corndog Under-Counter | (128, 96) | 64x96 | Putting the good batch back — "Nothing." |
| Frequent Loser Recognition | (192, 96) | 64x96 | "I remember faces. Yours is... dedicated." |

### Dialogue Portraits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Portrait: Neutral | (0, 192) | 64x96 | Standard dialogue box |
| Portrait: Deadpan | (64, 192) | 64x96 | "Living the dream." |
| Portrait: Almost-Smile | (128, 192) | 64x96 | Miracle Worker achievement portrait |
| Portrait: The Math Stare | (192, 192) | 64x96 | "I can. I won't enjoy it. Neither will you." |

### Expressions & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dead-Eyed Service | (0, 288) | 48x48 | Default |
| Dry Wit | (48, 288) | 48x48 | Delivering a corndog description |
| Rare Humanity | (96, 288) | 48x48 | "Between us... the corndog's not bad" |
| Judging Silently | (144, 288) | 48x48 | Out loud: nothing |
| Ticket Count Hands Close-Up | (192, 288) | 64x48 | Counting tray insert shot |

---

## 🤹 Sprite Sheet 5: Circus NPCs & Bros
**File:** `circus_npcs.png`
**Dimensions:** 512x192 pixels

### Nearby Circus Cast:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Game Barker Ludvík | (0, 0) | 64x96 | The rigged-games feeder — "EVERYONE'S a winner! ...eventually!" |
| Barker Mid-Pitch | (64, 0) | 64x96 | Arms wide, tickets fanned |
| Recent "Winner" | (128, 0) | 64x96 | Thousand-yard stare at a broken glow stick |
| The Proud Idiot | (192, 0) | 64x96 | Displaying haul with genuine, unironic joy |
| Hamstradamus Cameo | (256, 0) | 48x48 | The prophetic hamster passes by |
| Hamstradamus Prophecy Pose | (304, 0) | 48x48 | "The corndog is acceptable today... relatively..." |
| Passing Family | (352, 0) | 96x96 | Parents steering children away from the booth |
| Queue Loser (Generic) | (448, 0) | 64x96 | Ambient line filler, tickets in hand |

### The Bros:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner (85 Tickets) | (0, 96) | 64x96 | "We CRUSHED those games!" |
| Lord Pilsner (Bulk Deal) | (64, 96) | 64x96 | Pocketing seventeen mystery stickers |
| Chadwick (Glitter Hat) | (128, 96) | 64x96 | "The AESTHETIC of disappointment!" |
| Bradley (Counting Again) | (192, 96) | 64x96 | "Eighty-five." |
| Bros Walk-of-Shame | (256, 96) | 128x96 | Trio leaving with garbage, group composition |
| Kid With Kazoo | (384, 96) | 48x96 | Best thing he's ever received. He's five. He doesn't know yet |
| Ticket Booth Runner | (448, 96) | 64x96 | Staff shuttling ticket rolls from the games |

---

## ✨ Sprite Sheet 6: Effects
**File:** `trophy_effects.png`
**Dimensions:** 128x128 pixels

### Atmosphere Particles:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Dust Mote F1 | (0, 0) | 32x32 | Drifting in the harsh light cone |
| Dust Mote F2 | (32, 0) | 32x32 | Drift variant |
| Glitter Fleck F1 | (64, 0) | 16x16 | Shed from the Used Glitter Hat |
| Glitter Fleck F2 | (80, 0) | 16x16 | Sparkle variant |
| Hollow Confetti F1 | (96, 0) | 32x32 | Two sad pieces of confetti on redemption |
| Hollow Confetti F2 | (96, 32) | 32x32 | Falling, already regretting |

### Comedy Beats:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Sad Trombone Note Glyph | (0, 32) | 32x32 | Subtle stinger visual |
| Record Scratch Flash | (32, 32) | 64x32 | The Math Moment freeze-frame |
| Math Realization Flash | (0, 64) | 64x64 | Full-screen white blink before the popup |
| "Winner" Sparkle (Ironic) | (64, 64) | 32x32 | Single limp sparkle on prize handoff |
| Corndog Steam | (96, 64) | 16x32 | Rising from the good batch |
| Kazoo Note | (112, 64) | 16x16 | Floating annoyance |
| Nausea Swirl | (64, 96) | 32x32 | 30% chance made visible |
| Fly F1 | (96, 96) | 16x16 | Circling the back storage |
| Fly F2 | (112, 96) | 16x16 | Loop partner |
| Bobblehead Wobble Lines | (96, 112) | 32x16 | Budget prophecy in motion |

---

## 🎮 Sprite Sheet 7: UI Elements
**File:** `trophy_ui.png`
**Dimensions:** 256x256 pixels

### Redemption Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ticket Counter UI | (0, 0) | 128x64 | "TICKETS: ##" in carnival lettering |
| Prize Tier Menu Frame | (128, 0) | 128x160 | Four-tier shopping interface, bottom tier pre-highlighted |
| Redemption Confirm | (0, 64) | 128x64 | "Congratulations. You participated." |

### Status & Badges:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Frequent Loser Badge | (0, 128) | 48x48 | 10 redemptions — Yolanda acknowledges your existence |
| Carnival Debt Icon | (48, 128) | 32x32 | Always active — you spent more than it's worth |
| Participation Pride Icon | (80, 128) | 32x32 | Committed to the bit (+Bravado) |
| Ticket Icon (Small) | (112, 128) | 16x16 | Currency chip for menus |

### The Math:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Math Realization Popup | (0, 176) | 128x80 | "You spent €25. Your tickets are worth €4.25." |
| Prize Comparison Panel | (128, 160) | 128x96 | Tickets vs. direct gold price, side by side |

---

## 🎬 Animation Specifications

### Yolanda's Prize Presentation:
- **Duration:** 4 seconds
- **Frames:** Counting Tickets (1.5s) → Gesturing at Bottom Shelf (1s) → Presenting Prize (1.5s)
- **Pattern:** One-shot per redemption
- **Trigger:** Player confirms a prize
- **Purpose:** The ceremony of receiving garbage, played completely straight
- **Audio Sync:** Ticket shuffle during count, hollow "congratulations" fanfare on handoff, single ironic sparkle
- **Mobile Optimization:** None needed

### Ticket Counting:
- **Duration:** 2 seconds loop while tallying
- **Frames:** Ticket Count Hands close-up alternating with counter tray
- **Pattern:** Loops until total displayed
- **Trigger:** Player presents tickets
- **Purpose:** The pause where hope does math
- **Audio Sync:** Paper-flick tick per counted batch
- **Mobile Optimization:** Skip close-up, show total directly on Low LOD

### The Math Moment:
- **Duration:** 1.5 seconds
- **Frames:** Record Scratch Flash (0.3s) → Math Realization Flash (0.2s) → popup slides in (1s)
- **Pattern:** One-shot, once per playthrough (first time player requests or triggers the math)
- **Trigger:** Player selects "do the math" dialogue option
- **Purpose:** The speedrun through the stages of grief
- **Audio Sync:** Record scratch exactly on the freeze-frame
- **Mobile Optimization:** None needed

### Yolanda's Sigh Retreat:
- **Duration:** 5 seconds
- **Frames:** Neutral → The Sigh (2s) → walks through curtain (2s) → curtain sway (1s)
- **Pattern:** One-shot, random idle event every 90-180s when no customer waiting
- **Trigger:** Idle timer
- **Purpose:** Seven years of this, in one repeating gesture
- **Audio Sync:** One audible sigh at the pose apex
- **Mobile Optimization:** Sigh pose only, no walk, on Low

### Hollow Confetti:
- **Duration:** 1.2 seconds
- **Frames:** 2 confetti pieces, F1 → F2, falling
- **Pattern:** Exactly two pieces per redemption — the budget ran out
- **Trigger:** Redemption confirm
- **Purpose:** Celebration, technically
- **Audio Sync:** Faint party-horn wheeze
- **Mobile Optimization:** None needed (it is already the reduced version — that is the joke)

### Hamstradamus Pass-By:
- **Duration:** 6 seconds
- **Frames:** Cameo scuttle across foreground → Prophecy Pose (2s) → exit
- **Pattern:** Random event, roughly every 5 minutes on the grounds
- **Trigger:** Random timer while player is at the booth
- **Purpose:** Meta-commentary cameo; occasionally hints at corndog Nausea odds
- **Audio Sync:** Tiny mystical chime on the Prophecy Pose
- **Mobile Optimization:** Event disabled on Low LOD

### Bobblehead Wobble:
- **Duration:** 2 seconds decay
- **Frames:** Bobblehead + wobble lines, amplitude tween to rest
- **Pattern:** On tap / on shelf bump
- **Trigger:** Player interacts with the Hamstradamus Bobblehead
- **Purpose:** Budget prophecy; occasionally "speaks" (text bubble)
- **Audio Sync:** Spring boing at wobble start
- **Mobile Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements
**File:** `trophy_accessibility.png` (supplemental sheet — delivered alongside the 7 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Yolanda Interactive Outline | (0, 0) | 64x96 | White-on-dark counter hotspot |
| Fine-Print Sign, Large-Print | (64, 0) | 128x48 | "No Refunds. No Complaints. No Hope." readable without zoom |
| Tier Menu, Bold Frame | (64, 48) | 128x64 | High-contrast redemption interface border |
| Shelf Tags, Enlarged | (192, 0) | 64x96 | Ticket costs in oversized digits — the math must be readable |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dust, Static | (0, 96) | 32x32 | Fixed mote decal replacing drift particles |
| Flash, Removed Card | (32, 96) | 64x32 | Math Moment plays without white flashes — popup slides only |
| Glitter, Off | (96, 96) | 32x32 | Static glitter patch replacing shed particles |
| Wobble, Single Frame | (128, 96) | 32x32 | Bobblehead tilts once, no oscillation |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sigh Puff | (0, 160) | 32x32 | Breath glyph over Yolanda on each sigh |
| Hollow Fanfare Icon | (32, 160) | 48x32 | Drooping trumpet on the "congratulations" |
| Record Scratch Icon | (80, 160) | 32x32 | Zigzag glyph on the Math Moment |
| Counting Tick Marks | (112, 160) | 48x32 | Tally strokes appearing per counted batch |
| Party-Horn Wheeze Icon | (160, 160) | 32x32 | Deflating horn on confetti drop |
| Prophecy Chime Icon | (192, 160) | 32x32 | Sparkle glyph on Hamstradamus pose |

### Colorblind Considerations:
- Prize tiers are position-coded (shelf height) and tag-coded (ticket digits), never color-only
- Nausea risk on corndogs shown by the swirl icon, not a green tint alone
- Frequent Loser badge uses a distinct laurel-of-tickets silhouette
- Counter interaction zone and all tier menu rows exceed the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 — trophy_ui.png at ASTC 4x4 (math text must stay crisp)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for signage regions (all the jokes are text)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| trophy_environment | booth, prize wall | 1024x1024 |
| trophy_characters | yolanda, circus npcs | 1024x512 |
| trophy_items_ui | prize items, effects, ui, accessibility | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Dust motes, glitter, flies, Hamstradamus event, full presentation sequences |
| Medium | Dust only, no flies, presentation without close-up inserts |
| Low | No particles, no Hamstradamus event, direct total display, sigh pose without walk |

### Performance Targets:
- **Target FPS:** 45 (per location profile performance budget)
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 28 MB maximum
- **Particle Limit:** 10 (dust, glitter, flies combined)

### Performance Notes:
- Simplified prize wall on small screens: tier shelves collapse into the menu UI, booth stays focal (per profile: focus on transaction)
- Premium Garbage assets load only after Frequent Loser status
- Grand shelf is a single static region — it never changes because nothing up there is ever won

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Booth as single scene; prize wall regions bound to a data-driven catalog resource (tickets/gold/effects per item)
- Ticket economy reads the shared `cirque_tickets` counter fed by the rigged games; direct-purchase path bypasses it
- Redemption flow as a short AnimationPlayer sequence with the Math Moment as an interrupt branch
- CPUParticles2D (not GPU) for dust, glitter, flies
- State tracking: `participation_trophy_state` (prizes_redeemed, frequent_loser, math_realized, almost_smile_earned, participation_set_owned, corndogs_survived)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Ticket counting | Paper-flick ticks | Per counted batch |
| Prize handoff | Hollow "congratulations" fanfare | On Presenting Prize frame |
| Hollow Confetti | Party-horn wheeze | On confetti spawn |
| Math Moment | Record scratch | On freeze-frame flash |
| Yolanda's sigh | Single sigh sample | At pose apex |
| Kazoo (in inventory use) | Kazoo blat | With Kazoo Sound Lines |
| Hamstradamus Prophecy Pose | Tiny mystical chime | On pose hold |
| Booth ambient | Off-key distant carnival music, quieter at counter | Constant; ducks -4dB in dialogue |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Grand Prize Myth | Grand shelf items, "Just Ran Out" card, dust/cobweb overlays | Investigation of whether anyone has EVER won; examine text chain across the display items |
| Yolanda's Favorite | Frequent Loser badge, Recommendation Box, Rare Humanity expression | 10 redemptions unlock her genuine recommendation |
| Corndog Connoisseur | Corndog states, Nausea Swirl, corndog steam | Eat 5 Mystery Meat Corndogs without Nausea (luck-based) |
| Ironic Champion | All 6 participation-tier item sprites, Participation Pride icon | Collect every participation prize, display with pride (+15 Bravado) |
| Made Yolanda Almost Smile | Almost-Smile pose + portrait | Rarest achievement; sprite reserved exclusively for it |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Cirque du Shady Games | Ticket sprites and counter shared; Barker feeds players here | Walk across grounds, carnival audio continuous |
| Hamstradamus Tent | Cameo sprite reused from tent asset lineage; prophecies reference prizes | Cameo pass-by event |
| Ringmaster Vance (boss) | Cane Replica item — "Don't let Vance see you with this" reaction hook | Dialogue flag if replica equipped near Vance |
| Shadow Exchange | Selected prizes barterable there (at insulting rates) | Item sprites shown in Shadow Exchange barter UI |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Childhood disappointment, concentrated, under harsh lighting"
- **Color Mood:** Faded Carnival Red and Depressing Yellow — festivity with the saturation drained by seven years of sun
- **Lighting:** One harsh booth cone, unflattering for prizes AND customers; the Grand shelf spotlight is broken, of course
- **Texture:** Peeling paint, worn canvas, dust strata by shelf height (thickest at the top, where nothing is ever touched)

### Environmental Storytelling:
- Dust gradient tells the whole economy: pristine participation bins, archaeological Grand shelf
- The Championship Belt has been there since 2003 — its tag is sun-bleached around a darker rectangle where a previous tag was
- The tip jar is empty and always has been
- The handwritten "Yes, these are the GOOD prizes" is the only recent-looking signage

### Character Integration Notes:
- Yolanda's poses are minimal-motion by design — she expends exactly the energy required, never more
- The Almost-Smile must be barely distinguishable from Neutral; players should argue about whether it happened
- The Kid With Kazoo is played 100% sincere — he is the one person the booth hasn't beaten, and the composition should protect that

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The 85-Ticket Verdict** - Ticket pile on the counter, Yolanda gesturing at the bottom shelf
2. **The Math Realization Popup** - "€25 spent. Tickets worth €4.25."
3. **The Grand Prize Shelf** - Badly painted Golden Hamster under a broken spotlight, since forever
4. **The Bros' Walk-of-Shame** - Trio exiting with a glitter hat, seventeen stickers, and dignity nowhere
5. **The Almost-Smile** - Blink and you miss the rarest sprite in the circus

### Quote Potential:
- "The mystery isn't what meat. The mystery is IF meat. Enjoy."
- "85 tickets. Consolation tier starts at 100. You're in participation territory."
- "...four cigars?" / "Living the dream."
- "It says 'Winner' but it doesn't say what you won. Interpret as needed."
- "That's a bulk deal. We just got a BULK DEAL."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | trophy_booth.png | 512x512 |
| 2 | prize_wall.png | 512x512 |
| 3 | prize_items.png | 256x256 |
| 4 | yolanda.png | 256x384 |
| 5 | circus_npcs.png | 512x192 |
| 6 | trophy_effects.png | 128x128 |
| 7 | trophy_ui.png | 256x256 |

**Total Estimated Memory:** ~13 MB (well inside the 28 MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `trophy_booth.png` (512x512)
- [ ] `prize_wall.png` (512x512)
- [ ] `prize_items.png` (256x256)
- [ ] `yolanda.png` (256x384)
- [ ] `circus_npcs.png` (512x192)
- [ ] `trophy_effects.png` (128x128)
- [ ] `trophy_ui.png` (256x256)
- [ ] `trophy_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (prize tiers grouped by shelf; Yolanda poses grouped by scene beat)
- **Documentation:** Animation timing reference sheet (presentation sequence, Math Moment, sigh retreat) + prize catalog data map (sprite region → tickets/gold/effects)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Faded Carnival Red #CD5C5C, Depressing Yellow #F0E68C, Worn Canvas #D2B48C, Regret Purple #9370DB)
- [ ] All signage text readable on examine (fine-print sign, handwritten sign, shelf tags — the jokes are text)
- [ ] Almost-Smile differs from Neutral by deliberately minimal pixels
- [ ] Golden Hamster paint reads as badly applied gold paint, not gold
- [ ] Accessibility visual alternatives included for all audio cues (sigh, fanfare, scratch, ticks, wheeze, chime)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (systemic disappointment, deadpan-distributed) is clear throughout all assets
- [ ] Hidden details discoverable: empty tip jar, 2003 belt tag ghost, dust gradient economy, sincere kazoo kid
- [ ] Mobile performance optimized (collapsed prize wall on small screens, gated Premium Garbage, CPU particles)
- [ ] Touch zone sizing considered (44px minimum — counter and tier rows compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (shelf/tag coding, swirl icons)
- [ ] Social media viral potential maximized (math popup, walk-of-shame, grand shelf compositions)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville / Cirque du Shady only |
| Cultural Specificity | ✅ | Eastern European carnival seediness, tourist trap prize economics |
| Satirical Targets Appropriate | ✅ | The rigged system and participation-trophy culture — explicitly not the workers or customers |
| Seedy Underbelly Present | ✅ | Money and time converted into certified garbage, by design |
| Gameplay Value Established | ✅ | Ticket sink, item catalog with real (bad) stats, 4 quests, Frequent Loser progression, Bravado hooks |
| Technical Feasibility | ✅ | 7 sheets, data-driven catalog, one presentation timeline — standard Godot 4.x |
| Mobile Performance Budget | ✅ | 45 FPS / 12 draw calls / 28 MB per profile; estimate ~13 MB |
| Accessibility Features | ✅ | Flash-free Math Moment path, glyphs for every stinger, oversized math text |
| No Crypto Elements | ✅ | Tickets are paper and regret only (profile-confirmed) |
| Social Media Integration | ✅ | Five viral moments identified, quotes sourced from profile dialogue |

**With these assets delivered, The Participation Trophy becomes the emotional exhaust pipe of the entire circus: every rigged game upstream ends here, at a counter where a woman with seven years of practice hands you a half-smoked cigar, two pieces of confetti fall, a hollow fanfare plays, and the sign reminds you — technically, spiritually falsely — that everyone's a winner.**
