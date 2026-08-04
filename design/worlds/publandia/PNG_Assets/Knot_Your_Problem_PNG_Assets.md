# Knot Your Problem - Complete PNG Asset Requirements

## 📋 Overview
Knot Your Problem is a late-night pretzel cart run by Eoin Reilly, a man who has optimized every gram of emotional labor out of the transaction and reinvested it all in pretzel quality — this document specifies every sprite needed to render aggressive indifference as a service. The satirical essence in one sentence: drunk bros mistake a food vendor for a therapist, and the vendor's entire visual language says "5 Sovs. Next."

**Location ID:** `publandia_vendor_knot_your_problem_01`
**Theme:** Drunk oversharing meets professional indifference — salty carbs, no sympathy, next customer
**Zone:** The Craic Tax (mobile cart, prime drunk foot traffic)
**Hours:** 6 PM - 4 AM (peak drunk hours only)
**Primary Function:** Street vendor / quick snacks / light HP restoration / emotional void — transaction system, efficiency bonuses, Bravado interactions, the hidden Sodium Conspiracy

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Industrial Steel | #71797E | Cart body, condiment station, all functional surfaces |
| Pretzel Brown | #C4A747 | Pretzels, warmer glow, the only warmth Eoin provides |
| Night Black | #1C1C1C | Background, night sky, Eoin's emotional availability |
| Mustard Yellow | #FFDB58 | Mustard cups, price highlights ("The yellow one") |
| Salt White | #FAF9F6 | Salt crystals, napkins, signage lettering |
| Pub Glow Amber | #FFB347 | Distant pub lights, drunk-traffic direction cues |
| Wet Cobble Slate | #3B4048 | Rain-slick cobblestones, puddle bases |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/knot_your_problem/
├── environment/
│   ├── knot_cart.png
│   └── knot_effects.png
├── npcs/
│   ├── eoin_reilly.png
│   └── knot_customers.png
├── objects/
│   └── knot_pretzels.png
└── ui/
    ├── knot_ui.png
    └── knot_accessibility.png
```

---

## 🛒 Sprite Sheet 1: The Cart & Signage
**File:** `knot_cart.png`
**Dimensions:** 512x384 pixels

### Cart Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Body | (0, 0) | 256x160 | Compact metal cart, industrial steel, surprisingly well-organized, zero decoration |
| Cart Wheels | (0, 160) | 128x32 | Locked wheels — mobile cart, but Eoin has found his spot |
| Cart Work Light | (128, 160) | 64x32 | Single functional lamp — visibility only, no ambiance, that is the point |
| Cash Box Closed | (192, 160) | 32x32 | Dented steel, exact-change slot worn shiny |
| Cash Box Open | (224, 160) | 32x32 | Coins sorted by denomination, obviously |

### The Efficiency Engine:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Warmer Case Stocked | (256, 0) | 128x96 | Glass pretzel warmer, full stock organized by type and size |
| Warmer Case Mid-Rotation | (384, 0) | 128x96 | Rotation system state — fresh stock cycling in, the one thing Eoin cares about |
| Condiment Station | (256, 96) | 128x64 | Three mustards, three salts, self-serve napkins, one pointed gap where ketchup would go |
| Eoin's Station | (384, 96) | 128x64 | Cash box, counter surface, direct sightline to exit (encouraging departure) |

### Condiment Station Detail:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mustard Yellow Bottle | (256, 160) | 32x32 | "The yellow one." Eoin's prescribed remedy for relationship problems |
| Mustard Spicy Bottle | (288, 160) | 32x32 | Brown squeeze bottle, hand-labeled |
| Mustard Honey Bottle | (320, 160) | 32x32 | Amber squeeze bottle, hand-labeled |
| Salt Regular Shaker | (352, 160) | 32x32 | Plain steel shaker |
| Salt Garlic Shaker | (384, 160) | 32x32 | Steel shaker, garlic icon |
| Salt Everything Shaker | (416, 160) | 32x32 | Steel shaker, chaos icon |
| Napkin Dispenser Full | (448, 160) | 32x32 | Self-serve. Don't ask for more |
| Napkin Dispenser Low | (480, 160) | 32x32 | Refilled on Eoin's schedule, not yours |

### Signage (All Five):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign | (0, 192) | 192x48 | "KNOT YOUR PROBLEM" — plain, functional lettering, no flourish |
| Subtitle Sign | (192, 192) | 128x32 | "Pretzels. That's It." |
| Small Print Sign | (320, 192) | 192x32 | "Exact Change Appreciated. Conversation Not." |
| Side Sign | (192, 224) | 128x32 | "I Don't Want To Hear About It" — mounted at drunk eye level |
| Hours Placard | (320, 224) | 128x32 | "6 PM - 4 AM" — peak drunk hours only, and both parties know it |

### Menu Board & Street Context:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Price Menu Board | (0, 256) | 128x128 | All 7 items, prices only, no descriptions needed |
| No Ketchup Marker | (128, 256) | 64x64 | Crossed-out ketchup bottle. Eoin has standards |
| Empty Ketchup Slot | (128, 320) | 64x64 | The pointed gap in the condiment lineup — negative space as editorial |
| Counter Ledge Tile | (192, 256) | 64x64 | Serving edge, worn smooth by eight years of handoffs |
| Exact-Change Tray | (192, 320) | 64x64 | Coin tray positioned to end the interaction faster |
| Wet Cobblestone Tile | (256, 256) | 128x128 | Rain-slick Publandia cobbles, tileable |
| Puddle Reflection | (384, 256) | 64x64 | Pub glow mirrored in standing water |
| Queue Wear Patch | (448, 256) | 64x64 | Pavement worn where the drunk line forms nightly |
| Distant Pub Glow Strip | (384, 320) | 128x64 | Warm amber pub windows down the street — the sodium conspiracy's other half |

### Technical Notes:
- Warmer case states swap on a rotation timer; glass uses a single translucent overlay layer, no shader
- The Empty Ketchup Slot must read as deliberate absence, not missing art — align it in the condiment lineup grid
- Cart Work Light is the primary light source; everything outside its cone falls toward Night Black

---

## 👨 Sprite Sheet 2: Eoin Reilly
**File:** `eoin_reilly.png`
**Dimensions:** 384x256 pixels

### Eoin States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Neutral | (0, 0) | 64x96 | Clean apron, neutral expression, no wasted movement |
| Waiting / Impatient Stare | (64, 0) | 64x96 | Dead-eyed waiting while a story he didn't ask for happens at him |
| Transaction Handoff | (128, 0) | 64x96 | Pretzel extended, palm flat, the interaction's entire emotional peak |
| Rare Approving Nod | (192, 0) | 64x96 | The single nod. Perfect Transaction reward. Blink and you miss it |
| The Exception | (256, 0) | 64x96 | Free pretzel slid across the counter, eyes almost soft — for The Crier only |
| Preparing Usual | (320, 0) | 64x96 | Already making it before the regular reaches the counter. "Usual?" |

### Dialogue Portraits & Close-Ups:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Portrait Neutral | (0, 96) | 64x48 | Default dialogue box face — flat, professional |
| Portrait Deflection | (64, 96) | 64x48 | Mid-"5 Sovs." — the face that ends stories |
| Portrait Nod | (128, 96) | 64x48 | For "Good." — approval at minimum viable warmth |
| Portrait Exception | (192, 96) | 64x48 | For "Pretzel's on me. Go." — humanity, briefly visible |
| Hands Handoff Close-Up | (256, 96) | 64x48 | Practiced grip, wax paper, zero fumble in eight years |
| Apron Detail | (320, 96) | 64x48 | Clean apron texture — pristine, because efficiency leaves no stains |

### Expression Micro-Set:
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Dead-Eyed Waiting | (0, 144) | 48x48 | Story tolerance: zero |
| Impatient Stare | (48, 144) | 48x48 | Browsing-too-long penalty face |
| Nod Frame A | (96, 144) | 48x48 | Chin down — half the entire nod |
| Nod Frame B | (144, 144) | 48x48 | Chin up — the other half |
| Almost-Softening | (192, 144) | 48x48 | The Exception, in the eyes only |
| "Next." Mouth Frame | (240, 144) | 48x48 | One syllable, door closed |
| Cash-Box Hand | (288, 144) | 48x48 | Coins counted by feel |
| Free-Pretzel Slide Hand | (336, 144) | 48x48 | The Exception handoff, no charge, no eye contact |

### Action Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Wipe Counter | (0, 192) | 64x64 | Idle-loop micro-movement, cloth in tight circles |
| Restock Rotation | (64, 192) | 64x64 | Fresh pretzels into the warmer — the only ritual he honors |
| Point to Mustard | (128, 192) | 64x64 | "Mustard's on the left." Doubles as relationship advice |
| Point to Café | (192, 192) | 64x64 | "Two blocks down. Chairs. People. Go." |
| Cash Exchange | (256, 192) | 64x64 | Coin intake, sub-second turnaround |
| Idle Blink | (320, 192) | 64x64 | Two-frame blink. Even his blinks are efficient |

### Technical Notes:
- Eoin's animation budget is deliberately tiny: stillness IS the character — resist the urge to add motion
- The Rare Approving Nod uses Nod Frame A → B → Neutral in under a second; it must never loop
- The Exception state is gated to The Crier encounter; it should feel visually rare because it is

---

## 👥 Sprite Sheet 3: Customer NPCs
**File:** `knot_customers.png`
**Dimensions:** 384x256 pixels

### Customer States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Oversharer Mid-Story | (0, 0) | 64x96 | Arms wide, mid-sentence, oblivious to the wall of indifference |
| Oversharer Deflated | (64, 0) | 64x96 | Holding pretzel, story unfinished, "okay, bye I guess?" |
| Efficient Regular Nod | (128, 0) | 64x96 | Approaches, nods. That's the whole dialogue |
| Efficient Regular Departing | (192, 0) | 64x96 | Transaction complete in 8 seconds, everyone's happy |
| The Crier | (256, 0) | 64x96 | Tears, attempted words, genuinely struggling |
| The Crier With Free Pretzel | (320, 0) | 64x96 | Holding the exception, pointed toward the café |

### Customer States (Continued):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Confused Tourist Asking | (0, 96) | 64x96 | "But like, what's your STORY—" |
| Confused Tourist Processing | (64, 96) | 64x96 | Recalibrating expectations of vendor friendliness |
| Drunk Queue Silhouettes | (128, 96) | 128x96 | Background line of swaying pub refugees, 3 deep |
| Story Speech Bubble | (256, 96) | 64x48 | Rambling text trailing off the bubble's edge |
| "5 Sovs" Cutoff Bubble | (320, 96) | 64x48 | The story bubble severed clean by a price |
| Tear Drops | (256, 144) | 32x32 | The Crier's overlay particles |
| Confusion Marks | (288, 144) | 32x32 | Tourist's floating question marks |
| Respect Marks | (320, 144) | 32x32 | "...harsh but fair, honestly." |
| Camera Phone Prop | (352, 144) | 32x32 | Raised phone, pre-10 Sovs-fee |

### Customer Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Oversharer Portrait | (0, 192) | 64x48 | Wild-eyed, mid-narrative |
| Efficient Regular Portrait | (64, 192) | 64x48 | Serene. Understands the system |
| Crier Portrait | (128, 192) | 64x48 | Red-eyed, grateful |
| Tourist Portrait | (192, 192) | 64x48 | Bright, doomed optimism |
| Walk-Away Backs | (256, 192) | 128x64 | Departing customers, carbed up, emotionally unchanged |

### Technical Notes:
- Queue silhouettes are a single static sprite with a slow sway offset — never individually animated
- The "5 Sovs" Cutoff Bubble must visually interrupt the Story Bubble when spawned (hard replace, no crossfade)
- The Crier's tears use the Tear Drops overlay at 2-3 particles maximum; this is a comedy of restraint

---

## 🥨 Sprite Sheet 4: Pretzels & Condiments
**File:** `knot_pretzels.png`
**Dimensions:** 256x128 pixels

### Menu Items (All Seven):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Classic Pretzel | (0, 0) | 32x32 | Plain, salted, perfect — 3 Sovs, +12 HP |
| Pretzel Bites Bag | (32, 0) | 32x32 | Shareable (if you have friends) — 4 Sovs, +15 HP |
| Cheese Stuffed Pretzel | (64, 0) | 32x32 | Melted cheese visible at the seam — 6 Sovs, +25 HP |
| Jalapeño Stuffed Pretzel | (96, 0) | 32x32 | Green flecks, heat shimmer — 7 Sovs, +22 HP, +Heat resist |
| The Everything Pretzel | (128, 0) | 32x32 | Every topping, visually chaotic — 6 Sovs, +23 HP |
| Cinnamon Sugar Pretzel | (160, 0) | 32x32 | Sweet option — 5 Sovs, +18 HP, +5 SP, judged silently |
| Large Pretzel | (192, 0) | 48x48 | More pretzel, same attitude — 5 Sovs, +20 HP |

### Condiments & Serveware:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Mustard Cup Yellow | (0, 48) | 32x32 | The yellow one. It helps |
| Mustard Cup Spicy | (32, 48) | 32x32 | Brown, hand-poured |
| Mustard Cup Honey | (64, 48) | 32x32 | Amber, drizzle texture |
| Salt Packet Regular | (96, 48) | 32x32 | Plain white packet |
| Salt Packet Garlic | (128, 48) | 32x32 | Garlic icon packet |
| Salt Packet Everything | (160, 48) | 32x32 | Chaos icon packet |
| Napkin Stack | (192, 48) | 32x32 | Free. The only free thing here (usually) |
| Wax Paper Wrap | (224, 48) | 32x32 | Handoff wrapper, cart-branded with nothing |

### Special-State Pretzels:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Bonus Portion Pretzel | (0, 80) | 48x48 | Slightly larger — the no-conversation reward, never announced |
| Free Pretzel On Napkin | (48, 80) | 48x48 | The Exception. On the house. Go to the café |
| Cold Pretzel | (96, 80) | 48x48 | Held for ten minutes of talking. He complained about the pretzel |
| Menu Icon Strip | (144, 80) | 112x32 | Seven 16x16 mini icons for the menu list UI rows |

### Technical Notes:
- All seven menu items share a silhouette family; toppings differentiate at 32x32 — test legibility at mobile scale
- Bonus Portion must be recognizably ~15% larger than Large when side by side, subtle in isolation
- Cold Pretzel desaturates Pretzel Brown toward Industrial Steel — sadness via palette

---

## ✨ Sprite Sheet 5: Effects & Night Street
**File:** `knot_effects.png`
**Dimensions:** 256x256 pixels

### Pretzel Steam & Salt:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Steam Wisp Frame 1 | (0, 0) | 16x32 | Rising curl off fresh stock |
| Steam Wisp Frame 2 | (16, 0) | 16x32 | Curl drift left |
| Steam Wisp Frame 3 | (32, 0) | 16x32 | Curl drift right |
| Steam Wisp Frame 4 | (48, 0) | 16x32 | Dissipating |
| Warmer Steam Fog | (64, 0) | 64x32 | Interior glass haze — quality made visible |
| Salt Sparkle Frame 1 | (128, 0) | 16x16 | Crystal glint under cart light |
| Salt Sparkle Frame 2 | (144, 0) | 16x16 | Glint peak |
| Salt Sparkle Frame 3 | (160, 0) | 16x16 | Glint fade |
| Salt Pour | (176, 0) | 16x32 | Shaker stream, thirst incoming |
| Cash Glint | (192, 0) | 32x32 | Coin flash on exact change |
| Coin Flip | (224, 0) | 32x32 | Change returned, reluctantly |
| Warmer Glow Pulse | (0, 32) | 64x32 | Pretzel Brown ambient light from the case |
| Mustard Squeeze Drip | (64, 32) | 32x32 | Single dollop, no waste |
| Napkin Flutter | (96, 32) | 32x32 | Self-serve grab moment |
| Salt Grain Scatter | (128, 32) | 64x32 | Counter-surface crystals catching light |
| Streetlamp Halo | (192, 32) | 64x32 | Cold civic light vs. warm pub glow |

### Night Street Context:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Night Street Backdrop | (0, 64) | 256x96 | Rain-slick cobblestones, pub-lit street, cart's industrial glow against the amber — Publandia at 2 AM |
| Rain Drizzle Overlay | (0, 160) | 128x32 | Light Irish mist, not a downpour |
| Cobble Shimmer | (128, 160) | 64x32 | Wet-stone highlight pass |
| Pub Light Bokeh | (192, 160) | 64x32 | Soft amber blobs — the source of all customers |
| Cart Light Cone | (0, 192) | 64x64 | Functional white pool around the cart, hard edges |
| Night Breath Puff | (64, 192) | 32x32 | Cold-air breath from queuing drunks |
| Sodium Aura | (96, 192) | 32x32 | Faint salt shimmer on consumed pretzel — the conspiracy, rendered |
| Perfect Transaction Flash | (128, 192) | 64x64 | Clean white ping — efficiency achieved |
| Bravado Sparkle | (192, 192) | 64x64 | +10 Bravado burst for the Perfect Transaction |

### Technical Notes:
- Steam and salt are the ONLY looping particles — the profile demands minimal effects, and Eoin would agree
- Night Street Backdrop is a static painted layer; bokeh and shimmer are alpha overlays, no shaders
- Sodium Aura triggers only when the hidden conspiracy timer is armed (pretzel eaten, 30-minute drink window open)

---

## 🎮 Sprite Sheet 6: UI Elements
**File:** `knot_ui.png`
**Dimensions:** 256x256 pixels

### Menu & Transaction:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu List Panel | (0, 0) | 128x160 | Simple list, 7 rows, prices, zero flavor text — browsing not encouraged |
| Menu Row Highlight | (128, 0) | 96x24 | Selected item bar, Mustard Yellow |
| Price Tag Chips | (128, 24) | 96x24 | 3 Sovs through 8 Sovs denominations |
| Transaction Complete | (128, 48) | 96x48 | "Here. Next." — done indicator |
| Efficiency Bonus Popup | (128, 96) | 96x32 | "+2 HP. Good." — quick-order reward |
| Exact Change Icon | (128, 128) | 32x32 | Coin stack — +1 HP nod of respect |
| Portion Bonus Icon | (160, 128) | 32x32 | Slightly-larger-pretzel indicator |
| Bravado +10 Badge | (192, 128) | 32x32 | Perfect Transaction payout |
| Regular Status Pips | (224, 128) | 32x32 | 10-order wordless counter toward "Regular" |

### Deflection & Gags:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Deflection Response Popup | (0, 160) | 128x48 | Conversation shut down: player text truncated, "5 Sovs. Next." stamped over it |
| Camera Fee Popup | (128, 160) | 96x48 | "Camera costs 10 Sovs." — Accept / Respect buttons |
| Perfect Transaction Timer | (0, 208) | 96x48 | Under-5-seconds countdown bar, no numerals, just shrinking steel |
| Emotionally Unchanged Icon | (96, 208) | 32x32 | Status effect: flat-line heart |
| Carbed Up Icon | (128, 208) | 32x32 | Status effect: pretzel silhouette, slight thirst tick |
| Efficient Customer Icon | (160, 208) | 32x32 | Status effect: Eoin remembers (doesn't care, but remembers) |
| Exact Change UI Coin | (192, 208) | 32x32 | Payment prompt asset |
| No Ketchup UI Icon | (224, 208) | 32x32 | Grayed, crossed out, permanently disabled option |

### Technical Notes:
- Deflection Response Popup hard-cuts any open dialogue advance — it interrupts, that is the joke
- Perfect Transaction Timer starts on cart approach; hitting zero silently disarms the +10 Bravado payout
- Menu rows pad to 44px hitboxes at runtime regardless of sprite height

---

## 🎬 Animation Specifications

### Pretzel Warmer Rotation:
- **Duration:** 4 seconds per cycle, every 45 seconds
- **Frames:** 2 (Warmer Case Stocked → Warmer Case Mid-Rotation → back)
- **Pattern:** Frame 1 (hold 41s) → Frame 2 (4s) → loop
- **Trigger:** Constant timer while location loaded
- **Purpose:** Fresh stock always — the single visible proof that Eoin cares about something
- **Audio Sync:** Pretzel warmer hum, continuous low layer
- **Mobile Optimization:** Low LOD holds Frame 1 permanently

### Pretzel Steam:
- **Duration:** 2 seconds per loop
- **Frames:** 4 (Steam Wisp 1 → 2 → 3 → 4)
- **Pattern:** 1 → 2 → 3 → 4 → respawn, 2-3 concurrent wisps
- **Trigger:** Constant above warmer case; burst on handoff
- **Purpose:** Warmth and quality signaling in a location that offers no other warmth
- **Audio Sync:** None
- **Mobile Optimization:** Single wisp on Medium LOD; static Warmer Steam Fog overlay on Low

### Salt Crystal Sparkle:
- **Duration:** 0.6 seconds
- **Frames:** 3 (Salt Sparkle 1 → 2 → 3)
- **Pattern:** 1 → 2 → 3 → despawn, random counter positions every 4-8 seconds
- **Trigger:** Timer while cart in view
- **Purpose:** Subliminal sodium advertising — the conspiracy starts at the retina
- **Audio Sync:** None
- **Mobile Optimization:** Disabled below High LOD

### Eoin Idle:
- **Duration:** 12 seconds per loop
- **Frames:** 4 (Neutral hold → Idle Blink x2 → Wipe Counter → Neutral)
- **Pattern:** Neutral (8s) → Blink (0.3s) → Wipe Counter (3s) → Neutral → loop
- **Trigger:** Constant when no transaction active
- **Purpose:** Stillness as characterization — a man at peace with his boundaries
- **Audio Sync:** None (silence is the point)
- **Mobile Optimization:** None needed — already minimal by design

### The Handoff:
- **Duration:** 1.2 seconds
- **Frames:** 3 (Neutral → Transaction Handoff → Neutral)
- **Pattern:** Neutral → Handoff (hold 0.8s) → Neutral
- **Trigger:** Purchase confirmed
- **Purpose:** The entire relationship, delivered in wax paper
- **Audio Sync:** Order confirmation beep on frame 2; cash box close on return to Neutral
- **Mobile Optimization:** None needed

### The Single Nod:
- **Duration:** 0.8 seconds, plays once, never loops
- **Frames:** 3 (Nod Frame A → Nod Frame B → Neutral)
- **Pattern:** A (0.3s) → B (0.3s) → Neutral (hold)
- **Trigger:** Perfect Transaction completed, or exact change paid
- **Purpose:** Maximum emotional payout of the entire location — restraint is the reward
- **Audio Sync:** Satisfying quick-exchange sound resolves as the chin comes up
- **Mobile Optimization:** None needed — three frames is already the floor

### The Perfect Transaction (Under 5 Seconds):
- **Duration:** 5.0 seconds maximum, player-paced
- **Frames:** Timer bar + Handoff (3) + Nod (3) + Perfect Transaction Flash (1) + Bravado Sparkle (1)
- **Pattern:** Timer starts on approach → order → pay → Handoff → Flash + Nod + Bravado Sparkle simultaneously → "Next."
- **Trigger:** Order, pay exact change, and leave with zero non-essential words before the timer empties
- **Purpose:** The location's core mastery beat — +10 Bravado, Eoin's single approving nod
- **Audio Sync:** Quick-exchange sound on completion; flat "Next." as the player steps away
- **Mobile Optimization:** Flash and Sparkle merge into one composite frame on Low LOD

### Deflection Cutoff:
- **Duration:** 0.4 seconds
- **Frames:** 2 (Story Speech Bubble → "5 Sovs" Cutoff Bubble)
- **Pattern:** Story bubble grows with player text → hard replace with cutoff bubble, no transition
- **Trigger:** Player selects any conversation/overshare dialogue option
- **Purpose:** The comedy engine — every story dies mid-sentence at the same price point
- **Audio Sync:** Conversation-attempt stinger: dialogue murmur cut off clean by "5 Sovs"
- **Mobile Optimization:** None needed

### The Exception:
- **Duration:** 4 seconds, once per playthrough beat
- **Frames:** 4 (Neutral → The Exception → Point to Café → Neutral)
- **Pattern:** Neutral → Exception slide (2s) → Point to Café (1.5s) → Neutral
- **Trigger:** The Crier encounter reaches its dialogue apex
- **Purpose:** Eoin's hidden humanity — he's not heartless, he has boundaries
- **Audio Sync:** No beep, no cash box — the silence of a free pretzel is the loudest cue here
- **Mobile Optimization:** None needed — this moment ships at full quality on every device

### Cash Box Open/Close:
- **Duration:** 0.5 seconds
- **Frames:** 2 (Cash Box Closed → Open → Closed)
- **Pattern:** Closed → Open (0.25s) → Closed
- **Trigger:** Payment received
- **Purpose:** Transactional punctuation; the metronome of the whole location
- **Audio Sync:** Cash box clink on open; latch on close
- **Mobile Optimization:** None needed

### Night Drizzle & Pub Bokeh:
- **Duration:** Continuous ambient
- **Frames:** Rain Drizzle Overlay scroll + Pub Light Bokeh alpha pulse (6s cycle)
- **Pattern:** Drizzle scrolls at 8px/s; bokeh eases 80%→100%→80% alpha
- **Trigger:** Constant, 6 PM - 4 AM (which is always, here)
- **Purpose:** Publandia night atmosphere — the pubs glow warm so the cart can glow cold
- **Audio Sync:** Background street noise layer
- **Mobile Optimization:** Static drizzle texture, bokeh pulse disabled on Low LOD

### Oversharer Gesture Loop:
- **Duration:** 3 seconds per loop while story active
- **Frames:** 2 (Oversharer Mid-Story ± 4px arm offset)
- **Pattern:** Sway between arm positions until Deflection Cutoff fires → snap to Oversharer Deflated
- **Trigger:** Oversharer NPC ambient scene or "The Overshare" quest
- **Purpose:** Shows what Eoin deals with, 50,000 stories deep
- **Audio Sync:** Story murmur fading into background street noise
- **Mobile Optimization:** Static Mid-Story pose on Low LOD

---

## ♿ Accessibility Sprite Requirements
**File:** `knot_accessibility.png` (supplemental sheet — delivered alongside the 6 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Panel Bold | (0, 0) | 96x64 | Thick-bordered menu list with enlarged item rows and high-contrast pricing |
| Deflection Popup Bold | (96, 0) | 96x48 | Oversized "5 Sovs. Next." with heavy outline — the punchline must land for everyone |
| Eoin Interactive Outline | (192, 0) | 48x64 | White-on-dark outline for the order hotspot at Eoin's station |
| Warmer Case Hotspot Outline | (0, 64) | 64x64 | Outlined glass case examine zone with enlarged stock silhouettes |
| Condiment Station Outline | (64, 64) | 64x64 | Outlined mustard/salt/napkin zone; the ketchup gap outlined in negative |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steam, Static | (128, 64) | 32x32 | Fixed steam curl replacing the 4-frame wisp loop |
| Salt Sparkle, Off | (160, 64) | 32x32 | Matte crystal state — no glint animation |
| Rain, Static Overlay | (192, 64) | 64x32 | Fixed mist texture replacing scrolling drizzle |
| Warmer Glow, Steady | (128, 96) | 64x32 | Constant Pretzel Brown glow — pulse disabled |
| Bokeh, Steady | (192, 96) | 32x32 | Fixed-alpha pub lights, no breathing cycle |
| Timer, Non-Pulsing | (224, 96) | 32x32 | Perfect Transaction bar drains linearly with no flash on completion |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Order Beep Icon | (0, 128) | 32x32 | Confirmation ping burst on order accepted |
| Cash Box Clink Icon | (32, 128) | 32x32 | Coin-on-steel glyph on payment open/close |
| Napkin Grab Rustle Icon | (64, 128) | 32x32 | Paper-flutter glyph on self-serve napkin pull |
| "5 Sovs" Cutoff Stinger Slash | (96, 128) | 48x32 | Dialogue waveform sliced clean through by a 5 Sovs tag — the conversation-attempt kill shot, visualized |
| Quick-Exchange Flash Icon | (144, 128) | 32x32 | Perfect Transaction completion cue — crisp double-tick glyph |
| Warmer Hum Bars | (176, 128) | 32x32 | Gentle amplitude bars for the ambient warmer hum |
| "Next." Pulse | (208, 128) | 32x32 | Single flat pulse ring each time Eoin says it (even to nobody) |
| Order Button Enlarged | (0, 160) | 64x32 | High-visibility order action, padded to 44px+ hitbox at runtime |
| Pay Button Enlarged | (64, 160) | 64x32 | High-visibility payment action, padded to 44px+ hitbox at runtime |
| Leave Button Enlarged | (128, 160) | 64x32 | High-visibility departure — Eoin's favorite button |

### Colorblind Considerations:
- The three mustards (yellow/spicy/honey) carry letter tags (Y / S / H) on cups and bottles — never coded by color alone
- The three salts use distinct packet icons (plain / garlic bulb / chaos star), no color dependency
- Price highlights pair Mustard Yellow with a bold weight change so selection reads without hue
- Status icons (Carbed Up / Emotionally Unchanged / Efficient Customer) are three distinct silhouettes
- All interactive zones — menu rows, order/pay/leave buttons, condiment station, Eoin hotspot — meet the 44px minimum touch target via runtime hitbox padding

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback for legacy devices); Night Street Backdrop and signage kept at ASTC 4x4 so sign text stays legible
- **Android:** ETC2 with alpha across all sheets
- **Fallback:** PNG high quality for the five signs and the Price Menu Board — the jokes are written on them, they must not compress into mush

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| knot_environment | knot_cart, knot_effects | 1024x1024 |
| knot_characters | eoin_reilly, knot_customers | 1024x512 |
| knot_items_ui | knot_pretzels, knot_ui, knot_accessibility | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility — this location never comes close.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full steam (3 wisps), salt sparkle, drizzle scroll, bokeh pulse, warmer rotation |
| Medium | Single steam wisp, no salt sparkle, static drizzle, bokeh pulse retained |
| Low | Static steam fog overlay, no particles, static drizzle, warmer holds stocked frame |

### Performance Targets:
- **Target FPS:** 60 (profile floor of 45 treated as the absolute minimum on lowest-tier devices)
- **Max Draw Calls:** 8 per frame (per profile performance budget — a pretzel cart has no excuse for more)
- **Memory Footprint:** 20 MB maximum (per profile budget; actual sheet load lands well under)
- **Particle Limit:** 12 (steam wisps + salt sparkles + tear drops combined — minimal effects by design)

### Performance Notes:
- Single-NPC focus: Eoin is the only fully animated character; customers cycle one at a time
- Queue silhouettes are one static sprite; never spawn individual queue NPCs
- Night Street Backdrop loads once as a static layer — no parallax, the cart doesn't move and neither does Eoin's expression
- Deflection popup and dialogue portraits share the UI atlas to keep transaction sequences to a single bind

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D for cart/backdrop layers, AnimatedSprite2D for Eoin and customers, CPUParticles2D (not GPU) for steam, salt sparkle, and drizzle
- Perfect Transaction timer runs as a scene-local Timer node armed on cart Area2D entry; UI bar binds to time_left
- Deflection system: any overshare dialogue choice emits `deflected` — cuts active dialogue advance, spawns Cutoff Bubble and Deflection Response Popup in one frame
- State tracking per `knot_your_problem_state` (purchases_total, wordless_streak, perfect_transaction_done, exception_witnessed, camera_fee_paid, sodium_timer_armed)
- The Exception is a one-shot cutscene state gated on The Crier ambient encounter — locked out of replay

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Transaction Handoff frame 2 | Order confirmation beep | On pretzel-extended frame |
| Cash Box Open/Close | Cash box clink + latch | Clink on open, latch on close frame |
| Napkin Flutter | Napkin grab rustle | On self-serve pull |
| Deflection Cutoff | Conversation murmur cut off by "5 Sovs" stinger | Murmur dies exactly on bubble replace |
| Perfect Transaction Flash + Nod | Satisfying quick-exchange sound | Resolves as Nod Frame B lands |
| Warmer Case (constant) | Pretzel warmer hum | Continuous ambient layer, ducked during dialogue |
| Oversharer Gesture Loop | Story fading into background street noise | Murmur volume drops 10% per loop |
| The Exception slide | Silence (all ambient ducked) | Full duck for the 2s slide — no beep, no cash box |
| "Next." Mouth Frame | Flat "Next." voice line | Every transaction close, even with no queue |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Perfect Transaction | Perfect Transaction Timer, Handoff, Nod Frames A/B, Perfect Transaction Flash, Bravado Sparkle, Bravado +10 Badge | Complete a purchase in under 5 seconds with exact change and zero non-essential words; single nod is the trophy |
| The Overshare | Oversharer poses, Story Speech Bubble, "5 Sovs" Cutoff Bubble, Deflection Response Popup, Portrait Deflection, Emotionally Unchanged Icon | Comedy quest, always fails — every dialogue branch terminates in a deflection; failure IS completion |
| Regular Status | Regular Status Pips, Preparing Usual pose, Efficient Regular sprites, Efficient Customer Icon | 10 wordless orders fills the pip counter; Eoin starts the usual before the player reaches the counter |
| The Exception | The Crier states, The Exception pose, Free Pretzel On Napkin, Point to Café, Portrait Exception | Witness-only quest: triggers on The Crier ambient encounter; unlocks "Human After All" achievement |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Craic Tax (zone) | Cart positioned via Queue Wear Patch and Distant Pub Glow Strip — prime drunk traffic placement | Cart is a persistent zone fixture; no interior, walk-up only |
| The Blarney Trap | Walk-Away Backs and Drunk Queue Silhouettes path from the pub's exit — post-pub pretzel need | Pub-exit stumble path feeds the queue during peak hours |
| All Drinking Locations | Sodium Aura + Carbed Up thirst tick — the Sodium Conspiracy (salt → thirst → drinking → pretzels) | +5% Bravado synergy fires if alcohol is consumed within 30 minutes of a pretzel; the circle continues |
| Plot Armor Provisions | Menu Icon Strip scale contrast — snacks vs. meals niche, no shared inventory | Different food economy tier; no direct transition, mutual non-competition |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Industrial efficiency parked in the middle of Publandia's warmest, drunkest street"
- **Color Mood:** Industrial Steel and Night Black holding a hard line against Pub Glow Amber; Pretzel Brown is the only warmth the cart emits, and it's for sale
- **Lighting:** One functional cart light (hard white cone) against rain-slick cobbles and soft amber pub windows — the cart is a pocket of fluorescent honesty in a street full of golden lies
- **Texture:** Brushed steel, spotless glass, worn coin tray, wet stone — everything clean, nothing cozy

### Environmental Storytelling:
- Five signs that together form a complete customer-service philosophy: the name, the inventory, the prices, the boundary, and the payment terms
- The Empty Ketchup Slot — standards, communicated through absence
- The Queue Wear Patch — eight years of drunk feet standing in exactly the same spot
- The condiment station's self-serve napkins beside the "I Don't Want To Hear About It" sign: everything you need, nothing you want
- The sodium conspiracy hides in plain sight: salt sparkles under the cart light while pub glow beckons from the backdrop

### Character Integration Notes:
- Eoin is animated by subtraction: six states, two blink frames, one nod — every added frame dilutes him
- Customers carry all the motion; Eoin is the still point the comedy orbits
- The Exception must be staged with full ambient audio duck and no transaction sprites — the absence of the cash box IS the emotion
- Dialogue portraits stay within a 5% expression range of each other, except Portrait Exception, which gets 10%

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The "I Don't Want To Hear About It" Sign** - A food cart that legislates against your feelings, in plain functional lettering
2. **The Deflection Popup** - Player's heartfelt paragraph hard-cut by "5 Sovs. Next." — endlessly captionable
3. **The Single Nod** - The rarest approval animation in the game, screenshot-raced by completionists
4. **The Exception** - Free pretzel, café directions, ambient silence — the whole internet says "he DOES care"
5. **The Empty Ketchup Slot** - Standards as level design
6. **The 10 Sovs Camera Fee** - Chadwick paying a vendor for the right to make content about him not caring

### Quote Potential:
- "Mustard helps. The yellow one."
- "Napkins are free. Pretzel?"
- "I sell pretzels. That's the story."
- "Café's down the street. This is a pretzel stand."
- "They want me to care. I want them to have a good pretzel. We compromise."
- "Camera costs 10 Sovs."
- "...harsh but fair, honestly."

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | knot_cart.png | 512x384 |
| 2 | eoin_reilly.png | 384x256 |
| 3 | knot_customers.png | 384x256 |
| 4 | knot_pretzels.png | 256x128 |
| 5 | knot_effects.png | 256x256 |
| 6 | knot_ui.png | 256x256 |

**Total Estimated Memory:** ~9 MB (loaded, atlased, mipped — comfortably under the 20 MB profile budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `knot_cart.png` (512x384)
- [ ] `eoin_reilly.png` (384x256)
- [ ] `knot_customers.png` (384x256)
- [ ] `knot_pretzels.png` (256x128)
- [ ] `knot_effects.png` (256x256)
- [ ] `knot_ui.png` (256x256)
- [ ] `knot_accessibility.png` (256x192, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (all five signs on separate text layers — sign copy is load-bearing comedy and will be iterated)
- **Documentation:** Animation timing reference sheet (Perfect Transaction 5s ceiling, 0.8s nod, 0.4s deflection cutoff, warmer rotation cadence)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Industrial Steel #71797E, Pretzel Brown #C4A747, Night Black #1C1C1C, Mustard Yellow #FFDB58)
- [ ] All five signs readable at mobile scale — "I Don't Want To Hear About It" must land as a punchline from queue distance
- [ ] The Empty Ketchup Slot reads as deliberate editorial absence, not missing art
- [ ] The Exception assets (free pretzel, café point, softened portrait) feel visually distinct from every paid transaction
- [ ] Sodium Aura is subtle enough to be a hidden mechanic, present enough to be found
- [ ] Accessibility visual alternatives included for all audio cues (beep, cash box, napkin grab, "5 Sovs" stinger, quick-exchange sound)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (drunk oversharing vs. professional indifference) is clear throughout all assets
- [ ] Hidden interactions discoverable: sodium conspiracy shimmer, camera fee, bonus portion, cold pretzel gag
- [ ] Mobile performance optimized (12-particle cap, 8 draw calls, single-NPC animation, static backdrop)
- [ ] Touch zone sizing considered (44px minimum — menu rows, order/pay/leave buttons, condiment and Eoin hotspots compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (letter-tagged mustards, icon-coded salts, silhouette-distinct status icons)
- [ ] Social media viral potential maximized (deflection popup framing, single-nod capture window, sign compositions)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (Publandia only) | ✅ | Publandia, The Craic Tax zone — no real city names anywhere in assets or signage |
| Cultural Specificity | ✅ | Dublin-style drunk food culture; the 3 AM confession booth that is any food cart |
| Satirical Targets Appropriate | ✅ | Punches at drunk oversharers and parasocial customers, never at service workers' actual struggles |
| Seedy Underbelly Present | ✅ | The Sodium Conspiracy — salt drives thirst drives drinking drives pretzels; the cart is pub-adjacent on purpose |
| Gameplay Value Established | ✅ | HP restoration shop, efficiency bonuses, Bravado economy, 4 quests, 6 achievements |
| Technical Feasibility | ✅ | 6 sheets + 1 supplemental, no shaders, walk-up cart with no interior, mobile optimization documented |
| Mobile Performance Budget | ✅ | 60 FPS target, 8 draw calls, ~9 MB actual vs. 20 MB budget, 12-particle cap |
| Accessibility Features | ✅ | Visual cues for all five critical sounds, static-motion variants, high-contrast set, 44px touch targets |
| No Crypto Elements | ✅ | Absent — Eoin accepts exact change in Sovs and nothing else. PASS |
| Social Media Integration | ✅ | Six screenshot moments and seven quotable lines identified, deflection popup built to be shared |

---

**Knot Your Problem delivers the funniest possible answer to the question nobody asked Eoin: every sprite on these six sheets exists to sell one warm, perfectly salted pretzel and precisely zero units of sympathy. The cart gleams, the steam rises, the pub glow beckons from the backdrop, and the sodium conspiracy quietly reloads the whole street's thirst — while the deflection popup guillotines every drunk confession at the same price point and the single nod waits, three frames long, for the one player efficient enough to earn it. Your night, your drama, your feelings? Rendered, coordinate-mapped, and still knot Eoin's problem.**

**"Napkins are free. Pretzel?"**
