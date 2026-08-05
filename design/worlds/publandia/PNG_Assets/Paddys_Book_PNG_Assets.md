# Paddy's Book - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Paddy's Book — an unlicensed back-alley gambling den where the odds are handmade, the house rules are load-bearing, and every bet is a sure thing (for Paddy). The satire targets the gambling industry's fundamental unfairness — the house edge dressed up as hospitality — never the people it empties out. Behind a dumpster, under a green bulb, Paddy Malone runs the same math his father and grandfather ran: warmth in, wallets out.

**Location ID:** `publandia_seedy_paddys_book_01`
**Theme:** The house always wins, presented as grandfatherly customer service — gambling industry predation satirized as small-business charm
**Zone:** Back alley off The Craic Tax (Seedy Underbelly)
**Hours:** 18:00–05:00 (opens when legitimate businesses close)
**Primary Function:** Gambling hub / quest location — dice mini-games, brawl betting, Tourist Battle Royale combat, debt system, loan mechanic, "Cleaned Out" consequence loop, four quests and an achievement track

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Smoky Gray | #696969 | Smoke layers, haze, alley stone, ambient murk |
| Money Green | #228B22 | Felt, cash, betting UI accents, the green bulb tell |
| Underground Brown | #3D2314 | Floorboards, desk, ceiling beams, cellar walls |
| Danger Red | #8B0000 | Debt UI, house-rules popups, brawl pit accents |
| Brass Rail | #B5A642 | Fixtures, rails, watch, lamp hardware |
| Chalk White | #F5F5F5 | Odds board lettering, slate marks, betting slips |
| Nicotine Amber | #C9A15A | Bulb light cones, stained walls, lamp glow |
| Stout Black | #1A1208 | Shadows, corners, Tiny's suit, night alley |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/paddys_book/
├── environment/
│   ├── paddys_book_environment_tileset.png
│   └── paddys_book_odds_board.png
├── npcs/
│   ├── paddy_malone.png
│   ├── paddys_book_staff.png
│   ├── paddys_book_regulars.png
│   └── paddys_book_fighters.png
├── effects/
│   └── paddys_book_effects.png
└── ui/
    └── paddys_book_ui.png
```

---

## 🏚️ Sprite Sheet 1: Environment Tileset (Alley to Brawl Pit)
**File:** `paddys_book_environment_tileset.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #696969 (Smoky Gray), #3D2314 (Underground Brown), #1A1208 (Stout Black), #B5A642 (Brass Rail), #228B22 (Money Green — bulb only)

### Alley Exterior (y=0 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Damp Brick Wall Tile | (0, 0) | 32x64 | Wet-sheen brick, mortar going dark |
| Mossy Brick Variant | (32, 0) | 32x64 | Green creep in the grout, never cleaned |
| Cobblestone Tile | (64, 0) | 32x32 | Uneven alley ground |
| Cobblestone Puddle | (96, 0) | 32x32 | Reflects the green bulb when it's on |
| Dumpster | (128, 0) | 96x64 | The landmark that hides the door |
| Dumpster Lid Open | (224, 0) | 96x64 | Variant; someone's been looking for slips |
| Unmarked Door Closed | (320, 0) | 48x80 | Plausible deniability in door form — no sign, no handle plate |
| Unmarked Door Ajar | (368, 0) | 48x80 | Sliver of amber light and smoke escaping |
| Green Bulb OFF | (416, 0) | 16x24 | Dead bulb above the door; open hours over |
| Green Bulb ON | (432, 0) | 16x24 | The tell — lit means open, only if you know to look |
| Green Bulb Glow Halo | (448, 0) | 48x48 | Soft additive halo overlay, deliberately subtle |
| Drainpipe | (496, 0) | 16x80 | Drips on a timer |
| Fire Escape Section | (512, 0) | 64x80 | Rusted, decorative, definitely not fire-rated |
| Rear-of-Craic-Tax Wall Sign | (576, 0) | 64x48 | Faded delivery signage — this alley belongs to legitimate businesses, officially |
| Rain-Slick Overlay | (640, 0) | 64x64 | Wet ground shine (rain before midnight pays 1:3) |
| Alley Shadow Overlay | (704, 0) | 96x80 | Deep shadow wedge for the door recess |

### Entry Checkpoint — Tiny's Domain (y=80 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Checkpoint Wall Tile | (0, 80) | 32x64 | Bare interior brick, single coat of old paint |
| Inner Door | (32, 80) | 48x80 | The point of no return |
| Tiny's Stool | (80, 80) | 32x48 | Reinforced; Tiny is 6'8" |
| Coat Check Rack | (112, 80) | 64x64 | Coats, one suspicious umbrella |
| Weapon Check Bin | (176, 80) | 48x48 | "Theoretically" enforced — half empty |
| House Rules Poster | (224, 80) | 48x64 | Posted and ignored by the house; dusty, one corner peeling |
| Funds-Check Tray | (272, 80) | 32x24 | Where you prove the 50 Sovs minimum |
| Point-of-No-Return Floor Line | (304, 80) | 64x16 | Worn stripe on the boards |
| Bare Bulb Fixture | (368, 80) | 16x32 | Checkpoint's single light source |

### Main Floor — The Pit (y=160 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floorboard Tile | (0, 160) | 32x32 | Dark, worn smooth by pacing gamblers |
| Stained Floorboard | (32, 160) | 32x32 | Spilled stout, spilled hope |
| Low Ceiling Beam | (64, 160) | 96x24 | Head-height beam; tall patrons duck, Tiny folds |
| Smoke-Stained Wall Tile | (160, 160) | 32x64 | Grandfathered ventilation in visible form |
| Betting Station Booth Empty | (192, 160) | 80x64 | Edge-of-room station, chalk slate and rail |
| Betting Station Busy | (272, 160) | 80x64 | Variant with slips, chips, elbow marks |
| Standing Table | (352, 160) | 32x48 | Standing room mostly — keeps people moving |
| The One Good Chair | (384, 160) | 24x32 | Few chairs by design; this one wobbles |
| Wall of "Winners" Photos | (408, 160) | 64x48 | Staged photos of shills holding cash |
| Hanging Bulb + Cord | (472, 160) | 16x48 | One per betting station, dim by policy |
| Chalkboard Drink Prices | (488, 160) | 32x32 | Drinks cheap; losing customers drink more |

### Dice Corner (y=256 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Circular Dice Pit | (0, 256) | 128x96 | Sunken ring where dice fights happen |
| Pit Rail Section | (128, 256) | 64x24 | Brass-topped, polished by gripping hands |
| Spectator Rail Crowd Base | (192, 256) | 96x48 | Packed silhouettes leaning over the rail |
| Dice Table Felt | (288, 256) | 64x48 | Money Green felt, worn pale at the throw line |
| Chalk Score Slate | (352, 256) | 32x32 | High-Low tallies, house column suspiciously long |
| Fingers' Dice Cup | (384, 256) | 16x24 | Leather cup, sleight-of-hand certified |

### The Book Station — Paddy's Desk (y=352 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Paddy's Desk | (0, 352) | 96x64 | Heavy oak, older than the building |
| Open Ledger ("The Book") | (96, 352) | 32x24 | Three generations of arithmetic |
| Cash Box | (128, 352) | 24x24 | Brass, always fuller at closing |
| Green-Shade Desk Lamp | (152, 352) | 24x32 | Only warm pool of light in the room |
| Desk Stool | (176, 352) | 24x32 | For marks accepting loan terms |
| Back Shelf — Bottles & Trophies | (200, 352) | 64x48 | Hurling trophy (Tiny's), unlabeled bottles |
| Odds Board Mounting Frame | (264, 352) | 80x64 | Wall frame the animated board slots into |
| Marker/IOU Spike | (344, 352) | 16x32 | Impaled paper reputations |

### The Brawl Pit — Converted Cellar (y=432 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cellar Stairs Down | (0, 432) | 64x96 | Stone steps into organized disagreement |
| Brawl Pit Floor Section | (64, 432) | 128x96 | Packed dirt over old cellar flags |
| Spectator Ring Section | (192, 432) | 96x48 | Crowd tier around the pit |
| Rope-and-Post Section | (288, 432) | 48x48 | The "ring" — rope, posts, optimism |
| Fight Spotlight Rig | (336, 432) | 48x64 | Single hard spotlight over the pit |
| Corner Stool & Bucket | (384, 432) | 32x32 | Fighter's corner essentials |
| Ring Bell | (416, 432) | 24x24 | Rung by whoever's closest |
| Dark Stain Overlay | (440, 432) | 48x32 | Unspecified. Nobody asks. |

### Recovery Corner (y=560 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sagging Armchair | (0, 560) | 48x48 | Where the cleaned-out land |
| Side Table with Stiff Drink | (48, 560) | 32x40 | On the house — the cheapest thing Paddy buys |
| Sympathy Bottle | (80, 560) | 16x32 | Unlabeled, effective |
| Dim Lamp | (96, 560) | 24x40 | Low light for low moments |
| Loan-Pitch Rug | (120, 560) | 64x32 | Where Maureen stands when she mentions Paddy could help |
| Wall of IOUs | (184, 560) | 64x48 | Pinned markers; the Debt Ghost's is oldest |
| Handkerchief Box | (248, 560) | 16x16 | Maureen restocks it nightly |

### State & Ambience Overlays (y=640 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Smoke Haze Room Overlay | (0, 640) | 256x128 | Full-room low-alpha haze layer |
| Police Raid Red Wash | (256, 640) | 128x128 | 50:1 event overlay — flashing wash (static variant provided) |
| Closing-Time Dark Overlay | (384, 640) | 128x128 | 5 AM dimming state |
| High-Contrast Door Outline | (512, 640) | 48x80 | Accessibility: unmarked door silhouette |
| High-Contrast Bulb Marker | (560, 640) | 32x32 | Accessibility: green bulb finder ring |
| High-Contrast Betting Station Outline | (592, 640) | 80x64 | Accessibility: interactable frame |
| High-Contrast Desk Outline | (672, 640) | 96x64 | Accessibility: Paddy's desk frame |
| High-Contrast Dice Pit Outline | (768, 640) | 128x96 | Accessibility: dice corner frame |
| Exit Route Arrow Markers | (896, 640) | 48x48 | Accessibility: leave-while-you-can wayfinding |

### Composite Backdrops (y=768 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Alley Exterior Backdrop | (0, 768) | 384x256 | Assembled night alley — dumpster, door, bulb position |
| Main Floor Backdrop | (384, 768) | 512x256 | Assembled pit interior with beam shadows |
| Static Smoke Frame | (896, 768) | 128x128 | Motion-sensitivity: single non-drifting haze frame |

### Technical Notes:
- Green bulb ON/OFF is a two-frame swap plus optional halo overlay; halo alpha ≤ 40% — the tell must stay subtle but findable
- Smoke haze renders at 30% alpha over environment, under NPCs' heads (low ceiling gag: smoke sits at sprite shoulder height)
- Police raid wash strobes at 2 Hz max; reduced-motion swaps to static red tint
- Backdrops are single-draw parallax-free planes; keep the den claustrophobic

---

## 🎩 Sprite Sheet 2: Paddy Malone (The Proprietor)
**File:** `paddy_malone.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #3D2314 (Waistcoat Brown), #B5A642 (Watch & Chain), #F5F5F5 (Shirt), #228B22 (Tie)

### Grandfather Warmth & The Book (64x96 frames, y=0 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle Warm A | (0, 0) | 64x96 | Hands folded, eyes twinkling, doing math |
| Idle Warm B | (64, 0) | 64x96 | Breathing frame, smile a half-pixel wider |
| Dealing 1 — Slip Taken | (128, 0) | 64x96 | Accepts your bet like a gift |
| Dealing 2 — Ledger Entry | (192, 0) | 64x96 | One elegant pen stroke; your fate recorded |
| Dealing 3 — Cash to Box | (256, 0) | 64x96 | Money vanishes with practiced tenderness |
| Odds-Calling 1 — Arm Raised | (320, 0) | 64x96 | Calling tonight's action to the floor |
| Odds-Calling 2 — Board Point | (384, 0) | 64x96 | Gesturing at Big Mick vs. Quarry Jimmy |
| Odds-Calling 3 — Cupped Shout | (448, 0) | 64x96 | "Two-to-one! Getting generous in my old age!" |

### House Rules & The Loan (y=96 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| House Rules 1 — Finger Raised | (0, 96) | 64x96 | "Now, we play Publandia rules here" |
| House Rules 2 — Hand on Heart | (64, 96) | 64x96 | Solemn invocation; the house decides disputes |
| House Rules 3 — Apologetic Shrug | (128, 96) | 64x96 | Rules are rules (he wrote them ten seconds ago) |
| Loan Lean-In 1 — Elbows on Desk | (192, 96) | 64x96 | "I hate to see you walk out with nothing" |
| Loan Lean-In 2 — Hand on Shoulder | (256, 96) | 64x96 | Predatory warmth at maximum wattage |
| Loan Contract Presentation | (320, 96) | 64x96 | Paper slides across; 50% per day, among friends |
| Welcome Arms Open | (384, 96) | 64x96 | "New faces, new friends, new opportunities" |
| Counting Cash | (448, 96) | 64x96 | End-of-night ritual, reverent |

### The Mask Slips (y=192 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Winner Congratulation | (0, 192) | 64x96 | Applauds your win; eyes calculating the clawback |
| Rare Payout Wince | (64, 192) | 64x96 | Physical pain, professionally suppressed |
| Whale-Watching Delight | (128, 192) | 64x96 | Watching The Whale lose happily — pure joy |
| Dispute Decision | (192, 192) | 64x96 | "House says... re-roll. Fair, right?" |
| Malone Clause Declaration | (256, 192) | 64x96 | Invoking the clause "for your protection, really" |
| Sizing-Up-the-Mark Squint | (320, 192) | 64x96 | Half-second appraisal of a new tourist |
| Closing-Time Tally | (384, 192) | 64x96 | Ledger closed, watch checked, satisfied |
| Warmth-to-Calculation Transition | (448, 192) | 64x96 | The tween frame where grandda becomes bookmaker |

### Detail Elements (y=288 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Expensive Watch Close-Up | (0, 288) | 48x48 | Funded by your losses; brass and pride |
| Watch Glint Frame 1 | (48, 288) | 48x48 | Light catches the face |
| Watch Glint Frame 2 | (96, 288) | 48x48 | Glint travels the band |
| Ledger Close-Up | (144, 288) | 48x48 | Columns: names, sums, sighs |
| Marker Chit | (192, 288) | 32x32 | "Essentially your reputation," collateral form |
| Paddy Dialogue Bust | (224, 288) | 96x96 | Portrait for dialogue boxes, warm as fresh bread |
| Whiskey Glass | (320, 288) | 16x24 | Paddy's own — never more than one |
| Reading Glasses | (336, 288) | 24x16 | Worn only when the numbers get serious |

### Technical Notes:
- The watch appears in EVERY body frame (left wrist, 2–3 lit pixels) — continuity is the joke
- Warmth-to-Calculation transition frame is reused between any Warm state and any Business state
- Dialogue bust must keep the smile ambiguous: readable as kindly OR predatory depending on context text

---

## 🚪 Sprite Sheet 3: The Staff (Tiny, Fingers, Maureen)
**File:** `paddys_book_staff.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #1A1208 (Tiny's Suit), #8B0000 (Fingers' Waistcoat), #696969 (Maureen's Shawl), #F5F5F5 (Accents)

### Tiny the Bouncer — 6'8" of Professional Politeness (80x112 frames, y=0 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door-Block Idle | (0, 0) | 80x112 | Fills the frame; fills the doorway; that's the job |
| Password Check | (80, 0) | 80x112 | Leaning down to hear the whisper — a long way down |
| Fund Check | (160, 0) | 80x112 | Palm out: "Minimum's 50 Sovs to play. Show me." |
| Approval Nod | (240, 0) | 80x112 | Single nod; door opens behind him |
| Refusal Head-Shake | (320, 0) | 80x112 | Slow, almost sympathetic |
| Knuckle Crack 1 | (400, 0) | 80x112 | Fingers interlaced, raised |

### Tiny Continued (y=112 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knuckle Crack 2 | (0, 112) | 80x112 | The crack; disputes end here |
| Dispute-Settle Loom | (80, 112) | 80x112 | "Paddy's right. Always." |
| Gentle-Voice Chat | (160, 112) | 80x112 | Soft expression on an enormous frame — the contrast gag |
| Escort-Out Carry | (240, 112) | 80x112 | Patron under one arm like a baguette |
| "Leaving? Smart." Nod | (320, 112) | 80x112 | Approval reserved for the rare wise exit |
| Stool Sit | (400, 112) | 80x112 | Off-duty posture, still blocking the door |

### Fingers O'Brien — Dice Master (64x96 frames, y=224 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Showman Idle | (0, 224) | 64x96 | Abnormally long fingers drumming the felt |
| Dice Flourish 1 — Wind-Up | (64, 224) | 64x96 | Cup raised high, all eyes drawn up |
| Dice Flourish 2 — Release Arc | (128, 224) | 64x96 | Dice mid-air, theatrical rainbow |
| Dice Flourish 3 — Landed Reveal | (192, 224) | 64x96 | Ta-da hands over the result |
| Sleight-of-Hand Palm 1 | (256, 224) | 64x96 | Die tucked behind ring finger — 2-frame tell |
| Sleight-of-Hand Palm 2 | (320, 224) | 64x96 | The swap; visible only on close inspection |
| "OH! So Close!" | (384, 224) | 64x96 | Commiserating with the mark he just fleeced |
| Long-Finger Wiggle | (448, 224) | 64x96 | Idle flourish; ex-magician muscle memory |

### Maureen the Consoler (64x96 frames, y=320 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Maternal Idle | (0, 320) | 64x96 | Shawl, warmth, patience |
| Sympathy Drink Offer | (64, 320) | 64x96 | "Here, have a drink. On the house." |
| Shoulder Pat | (128, 320) | 64x96 | Genuine comfort, sincerely delivered |
| Calculating Eyes Tell | (192, 320) | 64x96 | Warm face, cold eyes — 2-pixel iris shift |
| Loan-Assist Ledger Check | (256, 320) | 64x96 | Checking what you're good for |
| Handkerchief Offer | (320, 320) | 64x96 | For the tears; she keeps a box |
| Interest Explanation | (384, 320) | 64x96 | "The interest isn't that bad. If you pay quick." |
| Collection-Day Stare | (448, 320) | 64x96 | The soft touch's other setting |

### Staff Props & Busts (y=416 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Maureen's Drink Tray | (0, 416) | 32x24 | Two sympathy glasses, always ready |
| Coat-Check Tokens | (32, 416) | 24x16 | Brass numbers 1–12; 7 is missing |
| Tiny's Torch | (56, 416) | 16x32 | For checking faces in the alley |
| Fingers' Cup & Dice | (72, 416) | 24x24 | The tools of honest work, dishonestly used |
| Sympathy Drink Glass | (96, 416) | 16x24 | Recovery corner standard issue |
| Tiny Dialogue Bust | (112, 416) | 96x96 | Gentle eyes, mountainous shoulders |
| Fingers Dialogue Bust | (208, 416) | 96x96 | Grin with too many angles |
| Maureen Dialogue Bust | (304, 416) | 96x96 | Kindly; do not sign anything |

### Technical Notes:
- Tiny is deliberately 16px taller than every other NPC sheet frame; he clips the low ceiling beam when standing under it (intentional collision gag)
- Fingers' palm-swap frames must be pixel-subtle: the swapped die differs by ONE pip-cluster pixel — feeds The Ringer Revealed quest inspection mechanic
- Maureen's Calculating Eyes frame is a direct swap of Maternal Idle with only the eyes changed

---

## 👥 Sprite Sheet 4: The Regulars (Shark, Whale, Ghost, Ringer)
**File:** `paddys_book_regulars.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #696969 (Shark's Coat), #B5A642 (Whale's Excess), #1A1208 (Ghost's Pallor), #8B0000 (Ringer accents)

### The Local Shark (64x96 frames, y=0 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Observing Idle | (0, 0) | 64x96 | Watching the table, not the dice |
| Precise Small Bet | (64, 0) | 64x96 | One chip, placed like surgery |
| Quiet Pocketing | (128, 0) | 64x96 | 20 Sovs a night, every night, no fuss |
| "Don't Tell Anyone" Whisper | (192, 0) | 64x96 | Leaning to the player, hand shielding mouth |
| Nursing the Same Pint | (256, 0) | 64x96 | Two hours, one pint, zero mistakes |
| Background Gambler A | (320, 0) | 64x96 | Crowd filler — hunched over slate |
| Background Gambler B | (384, 0) | 64x96 | Crowd filler — mid-groan |
| Background Gambler C | (448, 0) | 64x96 | Crowd filler — praying to dice |

### The Whale (y=96 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Money Throw 1 | (0, 96) | 64x96 | Fistful of notes leaving the hand |
| Money Throw 2 — Notes Airborne | (64, 96) | 64x96 | Confetti of currency |
| Celebrating a Loss | (128, 96) | 64x96 | Arms up, delighted — "I'm here for the EXPERIENCE!" |
| Buying Rounds | (192, 96) | 64x96 | Beloved by staff, statistically |
| "500 Sovs on the Australian!" Point | (256, 96) | 64x96 | Committing to the ringer, loudly |
| Adored by Staff | (320, 96) | 64x96 | Basking; Paddy's ideal customer |
| Staff-Adoration Sparkle Overlay | (384, 96) | 32x32 | Little hearts-and-Sov glints around him |
| Banknote Flutter Strip | (416, 96) | 48x32 | 3-frame falling notes for his aura |

### The Debt Ghost (y=192 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corner Linger | (0, 192) | 64x96 | Haunting the recovery corner he graduated from |
| Task Shuffle | (64, 192) | 64x96 | Sweeping; "working it off" month six |
| Haunted Stare | (128, 192) | 64x96 | A thousand-yard look at the dice corner |
| Warning Delivery Lean | (192, 192) | 64x96 | "Don't take the loan. Whatever you do." |
| Flinch as Paddy Passes | (256, 192) | 64x96 | Involuntary; Paddy waves warmly |
| Sigh Slump | (320, 192) | 64x96 | Shoulders drop two full pixels |

### The Ringer (y=288 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "G'day Mate!" Wave | (0, 288) | 64x96 | Tourist disguise at full brightness |
| Tourist Costume Idle | (64, 288) | 64x96 | Bucket hat, camera, brand-new "old" backpack |
| Suspicious Shadowboxing | (128, 288) | 64x96 | Footwork far too clean for a "first time" |
| Post-Reveal Pro Stance | (192, 288) | 64x96 | Hat off, guard up, entirely different person |
| Wink at Paddy | (256, 288) | 64x96 | The tell that closes The Ringer Revealed |
| Under-Table Payment | (320, 288) | 64x96 | Real wages, collected discreetly |

### Technical Notes:
- The Ringer's tourist frames share silhouette with Tourist Battle Royale combatants (Sheet 5) so he blends in the lineup — reveal frames break the silhouette
- Debt Ghost renders at 90% opacity always; he's not supernatural, just faded
- Whale's banknote flutter strip is reused by the effects money-scatter system

---

## 🥊 Sprite Sheet 5: Brawl Fighters & Crowd
**File:** `paddys_book_fighters.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #8B0000 (Fight accents), #696969 (Crowd mass), #1A1208 (Pit shadow), #F5F5F5 (Chalk)

### Headliners — Big Mick vs. Quarry Jimmy (80x112 frames, y=0 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Big Mick Idle | (0, 0) | 80x112 | Docker's build, taped fists, 2:1 favorite |
| Big Mick Guard | (80, 0) | 80x112 | High guard, patient |
| Big Mick Haymaker | (160, 0) | 80x112 | The punch the odds are priced on |
| Big Mick Victory | (240, 0) | 80x112 | Arm raised, unbothered |
| Big Mick KO'd | (320, 0) | 80x112 | Sprawled; 3:2 bettors weep |
| Quarry Jimmy Idle | (400, 0) | 80x112 | Stone-cutter's shoulders, 3:2 underdog |
| Quarry Jimmy Guard | (480, 0) | 80x112 | Low crouch, granite patience |
| Quarry Jimmy Body Shot | (560, 0) | 80x112 | Digs like he's quarrying |
| Quarry Jimmy Victory | (640, 0) | 80x112 | Modest nod; he's done this before |
| Quarry Jimmy KO'd | (720, 0) | 80x112 | Down but somehow still frowning |

### The Brewery Gorilla & Mystery Opponent (y=112 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Brewery Gorilla Loom Idle | (0, 112) | 96x128 | 5:1 — a man shaped like his nickname |
| Brewery Gorilla Wind-Up | (96, 112) | 96x128 | Keg-lifting muscles, weaponized |
| Brewery Gorilla Barrel Swing | (192, 112) | 96x128 | Wide arc; spectators lean back as one |
| Brewery Gorilla Victory Roar | (288, 112) | 96x128 | The 1:8 outcome nobody bet against |
| "???" Opponent Silhouette | (384, 112) | 64x128 | Unannounced challenger — black shape, question marks |
| Tale-of-the-Tape Chalkboard | (448, 112) | 96x96 | Fighter stats, half of them invented |

### Tourist Battle Royale Combatants (64x96 frames, y=240 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "American Mike" Idle | (0, 240) | 64x96 | 3:1 — actually decent, college wrestling stance |
| "American Mike" Swing | (64, 240) | 64x96 | Committed, telegraphed, effective enough |
| "British Barry" Overconfident | (128, 240) | 64x96 | 5:1 — chin up, guard down |
| "British Barry" Quick KO | (192, 240) | 64x96 | The fastest sprite state change in the game |
| "The Australian" Stance | (256, 240) | 64x96 | 2:1 — ringers are often "Australian" |
| "The Australian" Suspicious Skill | (320, 240) | 64x96 | Combination work no tourist has |
| "German Tourist" Windmill | (384, 240) | 64x96 | 4:1 wildcard, technique unknown to science |
| "German Tourist" Surprise Hit | (448, 240) | 64x96 | Could genuinely surprise |
| "Mystery Entrant" Hooded | (512, 240) | 64x96 | 8:1 — hood up, weight perfectly balanced |
| "Mystery Entrant" Reveal | (576, 240) | 64x96 | Hood drops: it's the Ringer. It's always the Ringer. |

### Crowd Reaction Strips (128x80 strips, y=336 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crowd Cheer Strip | (0, 336) | 128x80 | Arms up, pints sloshing — 2-frame alternation |
| Crowd Groan Strip | (128, 336) | 128x80 | Collective deflation on a favorite falling |
| Crowd Surge Strip | (256, 336) | 128x80 | Everyone leans in on a knockdown |
| Arms-Raised Betting Strip | (384, 336) | 128x80 | Waving slips at odds changes |
| Silent Tension Strip | (512, 336) | 128x80 | The stillness before a decisive roll |
| Shill Celebration | (640, 336) | 64x80 | Lone "winner" cashing out loudly, on schedule |

### Fight Props (y=416 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Towel Throw | (0, 416) | 32x32 | Mid-air surrender |
| Spit Bucket | (32, 416) | 24x24 | Veteran of a thousand rounds |
| Winner's Purse Bag | (56, 416) | 32x32 | Pot minus 30% house cut |
| Chalk Tally Board | (88, 416) | 48x48 | Round-by-round scoring, house arithmetic |
| Referee Armband | (136, 416) | 16x16 | Worn by Tiny when he remembers |
| Stretcher Plank | (152, 416) | 96x32 | For British Barry, mostly |

### Technical Notes:
- Big Mick and Quarry Jimmy get full 5-state sets — they headline the odds board and The Inside Bet quest cutscene
- Fight loops alternate Guard/Attack states at 0.4s per swap; impact bursts come from the effects sheet, never baked into fighter frames
- Crowd strips tile horizontally around the pit; cap at 4 strip instances on screen (reduced crowd density per profile)

---

## 📊 Sprite Sheet 6: The Odds Board (Animated Multi-State)
**File:** `paddys_book_odds_board.png`
**Dimensions:** 512x1024 pixels
**Color Palette:** #1A1208 (Board Slate), #F5F5F5 (Chalk White), #228B22 (Money Green trim), #8B0000 (Locked bets)

### Board Base (full render, all text legible at mobile scale):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Odds Board Base | (0, 0) | 384x512 | Full board: "PADDY'S BOOK — TONIGHT'S ACTION" header; BRAWLS: "Big Mick vs. Quarry Jimmy......... 2:1 / 3:2", "The Brewery Gorilla vs. ???....... 5:1 / 1:8", "Tourist Battle Royale............. Various"; DICE FIGHTS: "High-Low Championship............. Entry 20 Sovs", "Liar's Dice Tournament............ Entry 50 Sovs", "Paddy's Special (ask)............. 100 Sovs min"; PROPOSITIONS: "Rain before midnight.............. 1:3", "Hen party vomit (Craic Tax)....... 1:2", "Tourist asks for 'Publandia Bomb'. 1:1", "Police raid tonight............... 50:1"; footer: "HOUSE RULES: THE HOUSE IS ALWAYS RIGHT" |

### Header & Modifier Plates (right column):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Header Plate | (384, 0) | 128x32 | "PADDY'S BOOK — TONIGHT'S ACTION" as separate slat |
| Section Divider Slat | (384, 32) | 128x16 | Double-line chalk divider |
| Odds-Shift Arrow UP | (384, 48) | 24x24 | Solid triangle — odds lengthening (colorblind-safe shape cue) |
| Odds-Shift Arrow DOWN | (408, 48) | 24x24 | Inverted outline triangle — odds shortening (distinct shape, not just color) |
| Chalk Hand "Updating" | (432, 48) | 48x48 | Disembodied cuff rewriting a line |
| High-Roller Adjustment Slat | (384, 120) | 128x24 | "ODDS SUBJECT TO WINNING TOO MUCH" — appears at High Roller status |
| "Dice Recalibrating" Sign | (384, 144) | 128x48 | Technical-difficulties plate for house-rules stalls |

### Flippable Digit Tiles (16x24 each, y=520 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Digit 0 | (0, 520) | 16x24 | Split-flap style chalk digit |
| Digit 1 | (16, 520) | 16x24 | — |
| Digit 2 | (32, 520) | 16x24 | — |
| Digit 3 | (48, 520) | 16x24 | — |
| Digit 4 | (64, 520) | 16x24 | — |
| Digit 5 | (80, 520) | 16x24 | — |
| Digit 6 | (96, 520) | 16x24 | — |
| Digit 7 | (112, 520) | 16x24 | — |
| Digit 8 | (128, 520) | 16x24 | — |
| Digit 9 | (144, 520) | 16x24 | — |
| Colon Tile | (160, 520) | 16x24 | For 2:1, 3:2, 50:1 |
| Slash Tile | (176, 520) | 16x24 | For dual-odds lines (2:1 / 3:2) |
| Blank Tile | (192, 520) | 16x24 | Empty slot / wiped line |
| Half-Flip Frame A | (208, 520) | 16x24 | Mid-rotation blur, top half |
| Half-Flip Frame B | (224, 520) | 16x24 | Mid-rotation blur, bottom half |

### Individual Line Slats (320x24 each, swappable rows):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Slat: Big Mick vs. Quarry Jimmy 2:1 / 3:2 | (0, 552) | 320x24 | Headline bout line — cross-referenced at The Quiet Man |
| Slat: The Brewery Gorilla vs. ??? 5:1 / 1:8 | (0, 576) | 320x24 | Mystery opponent line |
| Slat: Tourist Battle Royale — Various | (0, 600) | 320x24 | Odds cycle live during entry period |
| Slat: High-Low Championship — Entry 20 Sovs | (0, 624) | 320x24 | Dice fights section |
| Slat: Liar's Dice Tournament — Entry 50 Sovs | (0, 648) | 320x24 | — |
| Slat: Paddy's Special (ask) — 100 Sovs min | (0, 672) | 320x24 | The "ask" is doing heavy lifting |
| Slat: Rain before midnight — 1:3 | (0, 696) | 320x24 | Free money for the house |
| Slat: Hen party vomit (Craic Tax) — 1:2 | (0, 720) | 320x24 | Saturday night special — settled by Craic Tax scouts |
| Slat: Tourist asks for "Publandia Bomb" — 1:1 | (0, 744) | 320x24 | Daily occurrence; Paddy scouts bars |
| Slat: Police raid tonight — 50:1 | (0, 768) | 320x24 | Longest odds on the board; Paddy has an understanding |
| Footer Slat: HOUSE RULES: THE HOUSE IS ALWAYS RIGHT | (0, 792) | 320x32 | Bolder chalk, double-underlined, non-negotiable |

### Reduced-Motion Variant:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Odds Board (simplified) | (0, 832) | 384x192 | Single-frame board, no flip animation, current odds only |

### Technical Notes:
- Digit flips run as 3-frame sequences (current → half-flip A → half-flip B → new digit) at 0.1s per frame with staggered per-digit start (0.05s offset) for the cascade effect
- Board text uses 8px chalk pixel font minimum; validate legibility at 1x mobile scale — this board is the room's information anchor
- Slats overlay the base board rows so individual lines update without redrawing the full board (1 draw call for board + slat batch)

---

## ✨ Sprite Sheet 7: Effects & Particles
**File:** `paddys_book_effects.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #696969 (Smoke), #C9A15A (Light), #228B22 (Money), #F5F5F5 (Bursts)

### Atmosphere Layers (y=0 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Smoke Layer A | (0, 0) | 256x128 | Seamless drift loop, slow, 30% alpha |
| Smoke Layer B | (256, 0) | 256x128 | Counter-drift loop for parallax depth |

### Light & Dust (y=128 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Single-Bulb Light Cone | (0, 128) | 64x96 | Nicotine-amber cone under each hanging bulb |
| Brawl Spotlight Cone | (64, 128) | 96x128 | Hard-edged pit spotlight |
| Dust Motes Frame 1 | (160, 128) | 64x64 | Particles suspended in beam |
| Dust Motes Frame 2 | (224, 128) | 64x64 | Drift offset frame |
| Green Bulb Pulse 1 | (288, 128) | 32x32 | Exterior tell, faint |
| Green Bulb Pulse 2 | (320, 128) | 32x32 | Peak glow |
| Green Bulb Pulse 3 | (352, 128) | 32x32 | Decay — full cycle stays subtle |
| Desk Lamp Glow | (384, 128) | 48x48 | Warm pool over the ledger |

### Dice & Impact (y=256 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dice Roll Blur 1 | (0, 256) | 32x32 | Tumble streak, launch |
| Dice Roll Blur 2 | (32, 256) | 32x32 | Mid-air chaos |
| Dice Roll Blur 3 | (64, 256) | 32x32 | Deceleration wobble |
| Dice Roll Blur 4 | (96, 256) | 32x32 | Final tumble |
| Dice Settle Bounce | (128, 256) | 32x32 | Last hop before the verdict |
| Impact Burst Small | (160, 256) | 32x32 | Jab connect |
| Impact Burst Medium | (192, 256) | 48x48 | Solid hit |
| Impact Burst Large | (240, 256) | 64x64 | Haymaker / Gorilla swing |
| Sweat Flick | (304, 256) | 16x16 | Fight seasoning |
| Loss Thud Dust Puff | (320, 256) | 32x32 | Visual for the loss thud (common) |
| Win Fanfare Sparkle | (352, 256) | 48x48 | Visual for the win fanfare (rare, by design) |

### Money & Chips (y=320 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Money Note Flutter 1 | (0, 320) | 48x32 | Note leaving a hand |
| Money Note Flutter 2 | (48, 320) | 48x32 | Mid-air tumble |
| Money Note Flutter 3 | (96, 320) | 48x32 | Landing (in Paddy's half of the table) |
| Chip Scatter 1 | (144, 320) | 48x32 | Chips spilling on win |
| Chip Scatter 2 | (192, 320) | 48x32 | Chips raked away on loss |
| Coin Glint 1 | (240, 320) | 16x16 | Visual for chip-clink audio |
| Coin Glint 2 | (256, 320) | 16x16 | — |
| Coin Glint 3 | (272, 320) | 16x16 | — |
| Cash-to-Paddy Vacuum Trail | (288, 320) | 96x32 | Stylized note-stream toward the desk; the house edge, visualized |

### Comedy & Audio-Cue Visuals (y=384 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sad Trombone Icon | (0, 384) | 48x48 | Appears over player on Cleaned Out — Paddy's choice, he thinks it's funny |
| Descending Note 1 | (48, 384) | 32x32 | "Wah" — eye level |
| Descending Note 2 | (80, 384) | 32x32 | "Wah" — waist level |
| Descending Note 3 | (112, 384) | 32x32 | "Waaah" — hits the floor and flattens |
| Empty-Pockets Pull-Out Overlay | (144, 384) | 64x64 | Pocket linings out; universal ruin symbol |
| Loan-Offer Jingle Sparkle | (208, 384) | 32x32 | Sickly-sweet glint when the pitch begins |
| House-Rules Announcement Flash | (240, 384) | 64x48 | Gavel-and-shamrock burst on rule invocations |
| Crowd Murmur Wisps | (304, 384) | 64x32 | Ambient chatter visual (speech squiggles) |
| Odds-Call Speech Glyph | (368, 384) | 32x32 | Megaphone glyph over Paddy during odds calling |
| Fight-Sound Star Burst | (400, 384) | 32x32 | Generic visual for off-screen brawl audio |

### Technical Notes:
- All particles via CPUParticles2D; smoke layers are scrolling TextureRects, NOT particles (2 draw calls total for atmosphere)
- Sad trombone sequence: icon appears, notes spawn at 0.4s intervals descending 8px each — total gag reads in under 2 seconds
- Cash-to-Paddy vacuum trail triggers only on losses ≥ 50 Sovs (comedy escalates with stakes)
- Green bulb pulse cycle is 4 seconds — slow enough to miss if you're not looking, which is the point

---

## 🎰 Sprite Sheet 8: UI, Items & Betting Interfaces
**File:** `paddys_book_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #228B22 (Money Green), #8B0000 (Danger Red), #F5F5F5 (Chalk White), #1A1208 (Panels)

### The Loaded Dice Set (y=0 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Die Face 1 | (0, 0) | 24x24 | Ivory-yellowed, chipped corner |
| Die Face 2 | (24, 0) | 24x24 | — |
| Die Face 3 | (48, 0) | 24x24 | — |
| Die Face 4 | (72, 0) | 24x24 | — |
| Die Face 5 | (96, 0) | 24x24 | — |
| Die Face 6 | (120, 0) | 24x24 | Comes up 55% of the time when the house needs it |
| Loaded Die Tell Face | (144, 0) | 24x24 | Pip cluster ONE pixel off-center — the tell for The Ringer Revealed, visible only on close inspection |
| Dice Pair Resting | (168, 0) | 48x32 | Table-state pair |
| Inspect-Zoom Die | (216, 0) | 64x64 | Magnified die for the inspection interaction; off-center pip weight readable here |
| Dice Cup Icon | (280, 0) | 32x32 | UI shorthand for dice games |

### Slips, Badges & Status Icons (y=64 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Betting Slip Blank | (0, 64) | 64x48 | Chalk-lined stub, "PADDY'S" letterhead |
| Betting Slip Filled | (64, 64) | 64x48 | Your wager, Paddy's penmanship |
| Betting Slip VOID Stamp | (128, 64) | 64x48 | Red VOID — house rules were invoked |
| High Roller Badge | (192, 64) | 48x48 | Brass shamrock — respect and worse odds |
| Cleaned Out Icon | (240, 64) | 32x32 | Empty pocket silhouette + downward wah-note shape |
| In Debt to Paddy Icon | (272, 64) | 32x32 | Marker chit with red string — Paddy's property now |
| On a Roll Icon | (304, 64) | 32x32 | Flaming die + solid up-arrow (shape-coded, not color-only) |
| Chasing Losses Icon | (336, 64) | 32x32 | Spiral drain + outline down-arrow (distinct shape from On a Roll) |

### The Loan & The Debt (y=128 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Loan Contract | (0, 128) | 96x64 | Readable gag text: "TERMS: 50% INTEREST PER DAY. YES, PER DAY. SIGN HERE, FRIEND." |
| Loan Contract Signed | (96, 128) | 96x64 | Your signature, already regretted |
| Debt Counter UI | (192, 128) | 128x32 | "OWED TO PADDY: ___ SOVS" — persistent HUD bar while In Debt |
| Interest Tick Popup | (320, 128) | 48x24 | "+50%" daily tick, red, accompanied by jingle visual |
| Marker Chit UI | (368, 128) | 32x32 | Inventory item: your reputation, in paper form |

### Betting Interfaces (y=192 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Odds/Betting Interface Panel | (0, 192) | 256x192 | Dice & proposition betting: stake selector, odds line, payout preview (house edge not shown, obviously) |
| Brawl Betting UI Panel | (256, 192) | 256x192 | Fighter cards with portraits, live odds with shift arrows, bet-lock timer |

### Popups & Buttons (y=384 row):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| House-Rules-Change Popup | (0, 384) | 192x128 | "⚖ MALONE CLAUSE INVOKED — For your protection, really." Red-sealed scroll frame |
| Bet Increase Button (+) | (192, 384) | 48x48 | 48px — exceeds 44px touch minimum |
| Bet Decrease Button (−) | (240, 384) | 48x48 | Distinct shape (recessed vs. raised) |
| Confirm Bet Button | (288, 384) | 64x48 | "ON." — Money Green with chalk border |
| Walk Away Button | (352, 384) | 64x48 | Always available; the smartest button in the game |
| Password Whisper Prompt | (416, 384) | 64x48 | Speech bubble with ear icon — "Seamus sent me" entry cue at the door |
| Achievement Toast Frame | (416, 432) | 96x32 | For the track: Player → Hopeful → Educated → Experienced |

### Technical Notes:
- All interactive UI elements ≥ 44x44 px touch zones; betting panels reserve 48px rows per option
- Loan contract gag text must be legible without zoom on a 6" screen — the terms ARE the joke
- Loaded-die tell: normal die faces and the tell face differ by exactly one pixel of pip offset; inspect-zoom die makes it findable, table-scale dice make it missable
- VOID stamp overlays the filled slip as a separate sprite (slip reused across states)

---

## 🎬 Animation Specifications

### Odds Board Digit Flip:
- **Duration:** 0.3 seconds per digit (0.1s per frame), 0.05s stagger between digits in a line
- **Frames:** 4 (current → half-flip A → half-flip B → new)
- **Pattern:** Cascade left-to-right across the updated slat
- **Trigger:** Odds change events (bets placed, fight developments, Paddy's whim)
- **Purpose:** The room's heartbeat — the board never stops moving because the take never stops moving
- **Audio Sync:** Split-flap clatter, one tick per digit flip
- **Performance Optimization:** Low LOD swaps to static board variant (0, 832 on Sheet 6), instant text swap

### Dice Roll (Fingers' Flourish):
- **Duration:** 1.2 seconds (wind-up 0.3s, air 0.5s, settle 0.4s)
- **Frames:** 3 character frames + 4 blur frames + settle bounce
- **Pattern:** Flourish 1 → 2 → 3 synced with blur 1→4 → settle bounce → face result
- **Trigger:** Every dice game round (constant ambient rolls at other tables at half rate)
- **Purpose:** Constant dice motion is the den's ambient pulse; Fingers' version is theater
- **Audio Sync:** Dice rattle through blur frames; clack on settle bounce; result silence beat
- **Performance Optimization:** Ambient background rolls drop to result-only (no blur frames)

### Paddy Odds-Calling Loop:
- **Duration:** 2.4 seconds loop
- **Frames:** 3 (arm raised → board point → cupped shout)
- **Pattern:** 1 → 2 → 3 → 1, 0.8s per frame
- **Trigger:** Timer loop while at desk with no active player interaction
- **Purpose:** Paddy performing the odds is the room's carnival barker track
- **Audio Sync:** Muffled odds-calling vocal bark on frame 3; odds-call speech glyph displays concurrently
- **Performance Optimization:** None needed

### House Rules Invocation:
- **Duration:** 2.5 seconds (hold final frame until player responds)
- **Frames:** 3 (finger raised → hand on heart → apologetic shrug)
- **Pattern:** Single play, hold shrug during popup
- **Trigger:** Player winning too much; disputed rolls; Malone Clause events
- **Purpose:** The core satirical mechanic — rules materialize exactly when the house needs them
- **Audio Sync:** "House rules" announcement sting on frame 1; gavel-and-shamrock flash fires with it
- **Performance Optimization:** None needed

### Loan Pitch Lean-In:
- **Duration:** 3 seconds (0.75s per frame, hold presentation)
- **Frames:** 4 (idle warm → lean-in 1 → lean-in 2 → contract presentation)
- **Pattern:** Single play into held contract frame
- **Trigger:** Player hits 0 Sovs (Cleaned Out) or accepts Maureen's referral
- **Purpose:** Predation at its most tender — the slower the lean, the worse the terms
- **Audio Sync:** Loan offer jingle begins on lean-in 1; jingle sparkle visual accompanies
- **Performance Optimization:** None needed

### Sad Trombone (Cleaned Out):
- **Duration:** 1.8 seconds
- **Frames:** Icon + 3 descending notes (0.4s spawn intervals)
- **Pattern:** Trombone icon appears over player → notes descend 8px per step → final note flattens on floor
- **Trigger:** Player balance hits 0 Sovs at Paddy's
- **Purpose:** Paddy chose this sound himself; the humiliation is part of the service
- **Audio Sync:** Sad trombone "wah wah waaah" — one note per visual note spawn
- **Performance Optimization:** None needed (it's four sprites; the gag is sacred)

### Tiny Knuckle-Crack Dispute Settlement:
- **Duration:** 1.0 second (0.5s per frame, hold crack)
- **Frames:** 2 (interlace raise → crack)
- **Pattern:** Single play, hold, return to loom
- **Trigger:** Player selects "Argue" on any dispute
- **Purpose:** Argument resolution, Publandia style — the crack IS the verdict
- **Audio Sync:** Knuckle pop (surprisingly loud) on frame 2; fight-sound star burst visual
- **Performance Optimization:** None needed

### Brawl Fight Loop (Big Mick vs. Quarry Jimmy):
- **Duration:** 0.8 seconds per exchange (0.4s per state swap)
- **Frames:** 2 per fighter (guard ↔ attack), impact bursts overlaid on connects
- **Pattern:** Alternating exchanges; scripted outcome states (victory/KO) on fight resolution
- **Trigger:** Brawl pit fight events; The Inside Bet quest sequence
- **Purpose:** Legible bout rhythm players can (think they can) read for betting
- **Audio Sync:** Meat-thud impact per burst; crowd cheer/groan strips swap per momentum shift; bell on start/end
- **Performance Optimization:** Impact bursts capped at 1 concurrent; crowd strips at 2 instances

### Smoke Drift:
- **Duration:** 12 second scroll loop (Layer A), 17 seconds (Layer B, counter-direction)
- **Frames:** 2 scrolling layers
- **Pattern:** Continuous UV scroll, no keyframes
- **Trigger:** Constant while indoors
- **Purpose:** Grandfathered ventilation as visual identity; the room breathes smoke
- **Audio Sync:** None
- **Performance Optimization:** Single layer at low LOD; static smoke frame for reduced motion

### Green Bulb Pulse:
- **Duration:** 4 second cycle
- **Frames:** 3 (faint → peak → decay)
- **Pattern:** Slow sine loop
- **Trigger:** Constant during open hours (18:00–05:00); OFF sprite otherwise
- **Purpose:** The tell — findable if you've heard the rumor, invisible if you haven't
- **Audio Sync:** None (silence is the tell's whole job)
- **Performance Optimization:** 2-frame version at low LOD

### Money/Chip Scatter:
- **Duration:** 0.9 seconds
- **Frames:** 3 flutter + 2 chip scatter, physics-lite arcs
- **Pattern:** Burst on payout events; vacuum-trail variant on big losses
- **Trigger:** Bet resolution ≥ 20 Sovs; Whale ambient throws every 8–12s
- **Purpose:** Money in motion, almost always toward the desk
- **Audio Sync:** Chips clinking (coin glints flash per clink); note rustle
- **Performance Optimization:** Halve particle count; Whale ambient throws every 20s

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Unmarked Door Outline | (512, 640) on environment sheet | 48x80 | High-contrast silhouette of the hidden entrance |
| Green Bulb Finder Marker | (560, 640) on environment sheet | 32x32 | Ring marker making the tell findable without color perception |
| Betting Station Outline | (592, 640) on environment sheet | 80x64 | Interactable frame for all betting stations |
| Paddy's Desk Outline | (672, 640) on environment sheet | 96x64 | The book station, high-visibility frame |
| Dice Pit Outline | (768, 640) on environment sheet | 128x96 | Dice corner interaction boundary |
| Exit Route Arrows | (896, 640) on environment sheet | 48x48 | Wayfinding to the alley — leaving is always an option |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Odds Board | (0, 832) on odds board sheet | 384x192 | No digit flipping; instant text swaps on update |
| Static Smoke Frame | (896, 768) on environment sheet | 128x128 | Non-drifting haze; replaces both scroll layers |
| Static Red Tint (raid) | (256, 640) on environment sheet | 128x128 | Police-raid wash held static — no strobing, ever, in reduced-motion mode |
| Impact Burst Single-Frame | (192, 256) on effects sheet | 48x48 | Fights show held medium burst instead of rapid flashing bursts |
| Green Bulb Steady ON | (432, 0) on environment sheet | 16x24 | Pulse cycle disabled; bulb holds lit state |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dice Rattle Visual | (0, 256) on effects sheet | 32x32 | Roll blur frames double as the constant-dice-audio visual |
| Chip Clink Glints | (240, 320) on effects sheet | 16x16 | One glint flash per clink |
| Crowd Murmur Wisps | (304, 384) on effects sheet | 64x32 | Ambient chatter squiggles; density tracks murmur volume |
| Crowd Cheer/Groan Strips | (0, 336) / (128, 336) on fighters sheet | 128x80 | Cheer and groan audio always paired with strip swap |
| Fight-Sound Star Burst | (400, 384) on effects sheet | 32x32 | Off-screen brawl audio gets an on-screen burst near the cellar stairs |
| Odds-Call Speech Glyph | (368, 384) on effects sheet | 32x32 | Megaphone glyph whenever Paddy's odds-calling vocal plays |
| Win Fanfare Sparkle | (352, 256) on effects sheet | 48x48 | Rare win audio, always with sparkle |
| Loss Thud Dust Puff | (320, 256) on effects sheet | 32x32 | Common loss audio, always with puff |
| House-Rules Announcement Flash | (240, 384) on effects sheet | 64x48 | Gavel-and-shamrock burst with the sting |
| Loan-Offer Jingle Sparkle | (208, 384) on effects sheet | 32x32 | Sickly glint synced to jingle |
| Sad Trombone Note Trail | (48, 384) on effects sheet | 32x32 ×3 | Descending notes render the trombone visually, beat for beat |

### Colorblind Considerations:
- Odds movement uses paired shape cues: solid triangle UP vs. outline inverted triangle DOWN — never color alone
- Win/loss feedback pairs green/red with distinct shapes: sparkle burst (win) vs. flat dust puff (loss)
- On a Roll (flaming die + solid up-arrow) and Chasing Losses (spiral + outline down-arrow) are silhouette-distinct at 32px
- Green bulb tell has the high-contrast finder-ring alternative; the puddle reflection provides a second non-hue cue (brightness)
- Betting slip states use stamp/overlay changes (VOID), not tint changes
- All betting UI touch zones minimum 44px; +/− buttons are 48px and shape-differentiated (raised vs. recessed)

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) odds board sheet stays uncompressed — chalk text must stay legible
- **Fallback:** PNG high quality for `paddys_book_odds_board.png` and `paddys_book_ui.png` (text-critical assets)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| paddys_book_environment | environment tileset, odds board | 2048x1024 |
| paddys_book_characters | Paddy, staff, regulars, fighters | 2048x1024 |
| paddys_book_effects_ui | effects, UI elements | 1024x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Both smoke layers, dust motes, full digit-flip cascades, 4 crowd strips, all ambient dice rolls, money/chip particles |
| Medium | One smoke layer, no dust motes, digit flips without stagger, 2 crowd strips, ambient rolls at half rate |
| Low | Static smoke frame, static odds board, 1 crowd strip, result-only dice, no ambient money particles |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 38 MB maximum
- **Particle Limit:** 24 (dust 8, money/chips 8, fight bursts 8 — fight bursts swap in for dust during brawls, never stack)

### Performance Notes:
- Simplified smoke (per profile): smoke is 2 scrolling TextureRects, not particles — 2 draw calls flat at High, 1 at Medium, 0 at Low
- Reduced crowd density (per profile): crowd strips are batched quads; the room reads "packed" through silhouette bases, not individual NPCs
- Static odds board option (per profile): low-end devices swap the animated board for the static variant with instant text updates
- Brawl pit sprites load on-demand when the player descends the cellar stairs; alley exterior unloads once inside
- The 16-draw-call ceiling is strict: environment backdrop (1), tiles batch (1), smoke (2), odds board + slats (2), NPC batch (3), fighters (2), effects (2), UI canvas (3) = 16

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for all character states; AtlasTexture regions per the coordinate tables above
- CPUParticles2D (not GPU) for dust, money, chips, fight bursts
- Odds board as a scene: static base Sprite2D + slat Sprite2D children + digit AnimatedSprite2D pool (15 digit instances max)
- CanvasLayer for debt counter, status icons, betting panels
- Location state machine: `closed → open → player_flush → player_cleaned_out → player_in_debt` drives NPC dialogue sets, loan-pitch triggers, and door/bulb states
- Door state: green bulb ON/OFF keyed to in-game clock (18:00–05:00); password prompt gates the inner door node

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Dice roll blur frames | Dice rattle (constant ambient) | Rattle spans blur 1–4; clack on settle bounce |
| Coin glint flashes | Chips clinking | One glint per clink event |
| Crowd strips (cheer/groan) | Crowd murmur → cheers | Murmur constant; strip swap on cheer/groan trigger |
| Impact bursts | Fight sounds from brawl pit | Burst spawns on the hit frame |
| Odds-call speech glyph + Paddy frame 3 | Paddy's odds calling | Vocal bark on cupped-shout frame |
| Win fanfare sparkle | Win fanfare (rare) | Sparkle and fanfare fire together on payout |
| Loss thud dust puff | Loss thud (common) | Puff on the same frame as the thud |
| House-rules flash + Paddy finger raise | "House rules" announcement sting | Sting on invocation frame 1 |
| Loan jingle sparkle + lean-in 1 | Loan offer jingle | Jingle begins as the lean begins |
| Sad trombone icon + note trail | Sad trombone | One "wah" per descending note spawn |
| Odds board digit flips | Split-flap clatter | One tick per digit flip |
| Tiny knuckle crack frame 2 | Knuckle pop | On the crack frame |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Cleaning the Debt | Debt counter UI, marker chit, Debt Ghost task-shuffle frames, Paddy dealing states | Player performs tasks for Paddy; debt counter decrements; Debt Ghost comments per milestone |
| The Inside Bet | Big Mick / Quarry Jimmy full fight sets, tale-of-the-tape board, betting slip, brawl betting UI | Fixed-fight intel changes displayed odds arrows; moral choice branches use victory/KO states |
| Whale Watching | The Whale full set, staff-adoration overlay, money flutter strip, Paddy whale-watching delight | Player helps land the big fish; Whale ambient throw rate escalates per phase |
| The Ringer Revealed | Ringer disguise + reveal frames, Mystery Entrant frames, loaded die tell face, inspect-zoom die, Fingers palm-swap frames | Inspection interaction exposes the one-pixel pip tell; wink-at-Paddy frame confirms; exploit/expose branch |
| Debt System (systemic) | Loan contract, signed variant, interest tick popup, In Debt icon, Cleaned Out icon | Cleaned Out triggers trombone + loan pitch; default spawns collector encounters at The Blarney Trap |
| Achievement Track | Achievement toast frame, High Roller badge | Player → Hopeful → Educated → Experienced → Wise/Marked → Survivor → Known |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Blarney Trap | Rumor dialogue points players here; Paddy's debt collectors (Tiny loom frame reused) appear there if you owe; loan offer follows you there after Cleaned Out | Standard door transition; collector encounter overlay |
| The Quiet Man | Fighter crossover — Big Mick and Quarry Jimmy sprites shared for cross-venue bouts and cross-betting; odds board headline slat referenced in Quiet Man dialogue | Fighter sprites loaded from this sheet at both venues |
| Shenanigans | Mickey and Paddy are professional acquaintances (different scams, same marks) — Paddy dialogue bust appears in Shenanigans cutscene | Bust reuse only; no environment sharing |
| The Craic Tax | Scouts direct high-spending tourists here; hen-party-vomit proposition slat (0, 720 on odds board) is settled by Craic Tax scout reports; alley sits behind Craic Tax businesses | Alley entrance accessible from Craic Tax back street; scout NPC hand-off |
| Door password system | Password whisper prompt (416, 384 on UI sheet) — "Seamus sent me" entry cue; password rumor text sourced from The Blarney Trap and Craic Broker NPCs | Whisper bubble interaction at unmarked door |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Grandfatherly warmth over industrial-grade extraction"
- **Color Mood:** Smoke gray and underground brown swallowing everything except the money green — cash and felt are the only saturated things in the room, which is the thesis
- **Lighting:** Single bare bulbs in amber cones; one green bulb outside; one hard spotlight over the brawl pit; Paddy's desk lamp is the warmest light in the building, and it shines on the ledger
- **Texture:** Damp brick, smoke-stained plaster, worn felt, hand-polished brass — everything aged except Paddy's watch

### Environmental Storytelling:
- The House Rules poster is dusty and peeling because nobody — least of all the house — has ever consulted it
- The Wall of "Winners" photos features the same three faces in different hats (they're shills; observant players can spot the repeat)
- The marker spike on Paddy's desk and the Wall of IOUs in the recovery corner bookend the debt pipeline visually
- Few chairs, low ceilings, dim light: the room is engineered to keep you standing, betting, and unable to think clearly — hostile architecture as satire
- The satire aims up: every rigged element (loaded pip, shill photos, house-rules stamp) indicts the operation, never the punters it empties — per the profile's sensitivity note, the industry is the joke, addiction never is

### Character Integration Notes:
- Paddy renders warm in every frame; only the transition frame and the watch glint betray the machinery underneath
- Tiny's gentle face on a doorway-filling body is a contrast gag — never draw him menacing, the SIZE is the menace
- The Ringer must be findable in the Battle Royale lineup by silhouette-reading players (his stance is a half-pixel too balanced)
- Debt Ghost at 90% opacity, always at the edge of frames — the room's memento mori

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The full odds board** — "Hen party vomit....... 1:2" and "Police raid tonight....... 50:1" on one legible chalk board is a shareable image by itself
2. **The sad trombone descending over a cleaned-out player** while Paddy's loan contract slides into frame
3. **The Mystery Entrant hood-drop reveal** mid-Battle-Royale with the Whale's "500 Sovs on the Australian!" still on screen
4. **The loan contract close-up** — "50% INTEREST PER DAY. YES, PER DAY. SIGN HERE, FRIEND."

### TikTok Potential:
- "POV: you found the green lightbulb" (door discovery reveal)
- "The house rules changing in real time" (Malone Clause popup speedrun)
- "Betting on rain in Publandia" (free money for the house)
- "When the 'Australian' tourist starts throwing combinations"

### Quote Potential:
- "The house always wins. That's not greed — that's math." — Paddy Malone
- "I'm not a criminal. I'm a mathematician who accepts cash." — Paddy Malone
- "I'm not LOSING, I'm INVESTING in the NARRATIVE." — Chadwick
- "Don't take the loan. Whatever you do. I've been 'working it off' for six months." — The Debt Ghost
- "I'll wait outside." — Bradley
- "Paddy's right. Always." — Tiny, settling a dispute

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | paddys_book_environment_tileset.png | 1024x1024 |
| 2 | paddy_malone.png | 512x384 |
| 3 | paddys_book_staff.png | 512x512 |
| 4 | paddys_book_regulars.png | 512x384 |
| 5 | paddys_book_fighters.png | 1024x512 |
| 6 | paddys_book_odds_board.png | 512x1024 |
| 7 | paddys_book_effects.png | 512x512 |
| 8 | paddys_book_ui.png | 512x512 |

**Total Estimated Memory:** ~12.5 MB (uncompressed RGBA at 4 bytes/pixel: 4 + 0.75 + 1 + 0.75 + 2 + 2 + 1 + 1 MB) — comfortably inside the 38 MB location budget with runtime overhead

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `paddys_book_environment_tileset.png` (1024x1024)
- [ ] `paddy_malone.png` (512x384)
- [ ] `paddys_book_staff.png` (512x512)
- [ ] `paddys_book_regulars.png` (512x384)
- [ ] `paddys_book_fighters.png` (1024x512)
- [ ] `paddys_book_odds_board.png` (512x1024)
- [ ] `paddys_book_effects.png` (512x512)
- [ ] `paddys_book_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + odds board slat/digit assembly guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Odds board text legible at 1x mobile scale — every line from headline to footer readable without zoom
- [ ] Green bulb tell subtle but findable: ≤ 40% halo alpha, discoverable via rumor knowledge or high-contrast finder marker
- [ ] Loaded-dice tell visible ONLY on close inspection: one pixel of pip offset at table scale, readable at inspect-zoom scale
- [ ] Paddy's watch present in every body frame (left wrist continuity)
- [ ] Fingers' palm-swap differs by exactly one pip-cluster pixel across the two frames
- [ ] The Ringer's tourist silhouette matches Battle Royale combatant proportions; reveal frames break it
- [ ] Loan contract terms legible on a 6" screen
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets — the house is the joke, not the gamblers
- [ ] Hidden areas/interactions have discoverable visual cues (bulb, door recess shadow, whisper prompt)
- [ ] Performance optimized (CPU particles, 16 draw calls, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum; betting buttons 48px)
- [ ] Colorblind-friendly alternatives available where color codes meaning (arrows, shapes, stamps)
- [ ] Social media viral potential maximized in composition choices (board framing, trombone staging)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only; the city's pub-and-bookmaker culture evoked, never named. NOTE: the source profile slips twice ("very Dublin back alley", "always works in Dublin") — this spec uses no real city names and the profile lines should be corrected upstream |
| Cultural Specificity | ✅ | Bookmaking-as-inheritance, proposition betting on everything including the weather, the hurler-turned-bouncer, the sympathetic loan pitch |
| Satirical Targets Appropriate | ✅ | Gambling industry's engineered edge, thrill-seeking tourists, "authentic underground experience" romance — punches up at the operation, never at addicts (per profile sensitivity note) |
| Seedy Underbelly Present | ✅ | Unlicensed gambling, loaded dice, fixed fights, 50%-per-day loan sharking, debt servitude (the Debt Ghost) |
| Gameplay Value Established | ✅ | Three dice games, proposition betting, brawl betting, Tourist Battle Royale combat, debt system, four quests, achievement track, Bravado economy |
| Technical Feasibility | ✅ | Eight sheets, three atlases, LOD tiers, on-demand brawl pit loading documented |
| Performance Budget | ✅ | 60 FPS, 16 draw calls, 38 MB, 24 particles (per profile budget) |
| Accessibility Features | ✅ | Visual cues for all 12+ audio events; static odds board, static smoke, no-strobe raid variant; shape-coded odds movement |
| No Crypto Elements | ✅ | None present — Paddy accepts cash. Only cash. |
| Social Media Integration | ✅ | Odds board, sad trombone, ringer reveal, and loan contract moments identified |

**Paddy's Book: where the green bulb is the only honest thing in the building, the odds board never stops flipping, and the warmest smile in Publandia costs 50% a day.**
