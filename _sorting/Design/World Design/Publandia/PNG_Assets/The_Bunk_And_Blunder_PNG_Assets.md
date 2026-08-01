# The Bunk & Blunder - Complete PNG Asset Requirements

## 📋 Overview
The Bunk & Blunder is Publandia's premier budget hostel, where €15 buys a bed, a story, and a fundamental reassessment of your life choices — this document specifies every PNG needed to render sleep as theoretical, privacy as fictional, and your roommates' life choices as ambient audio. The satire targets hostel culture and budget travel delusions: the bros think they're saving money for experiences; the hostel IS the experience, just not the one they wanted.

**Location ID:** `publandia_lodging_bunk_blunder_01`
**Theme:** Budget travel delusion meets random roommate chaos — "Where Dreams Go to Die (Usually Around 3 AM)"
**Zone:** Off Cobblestone Market Street (budget district), near The Craic Tax but far enough for plausible deniability
**Hours:** 24/7 reception (someone's always awake, unfortunately)
**Primary Function:** Rest point / social hazard zone / morning shame generator — random roommate rest-quality system, "Embarrassed" status engine, Shower Gauntlet mini-challenge, four quest hooks

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Institutional Beige | #D2B48C | Walls, reception, primary surfaces |
| Exhaustion Gray | #808080 | Colm, bedding, morning light, dark circles |
| Mystery Stain Brown | #8B4513 | Carpet, ceiling stains, backgrounds best not examined |
| Hope Green (Faded) | #90EE90 | Signage optimism, notice board pleas, key cards |
| Fluorescent White | #F5F5F0 | Harsh overhead lighting, shower tile |
| 3 AM Blue | #2F4F6F | Night dorm scenes, phone-glow shadows |
| Phone Glow Cyan | #7FDBFF | Screen light in dark dorms, Wi-Fi UI |
| Shame Red | #CD5C5C | Embarrassed popup, chaos warnings, cold-water gauge |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/the_bunk_and_blunder/
├── environment/
│   ├── hostel_exterior.png
│   ├── reception_interior.png
│   ├── common_room.png
│   ├── dorms_and_privates.png
│   └── shower_block.png
├── npcs/
│   ├── colm_obrien.png
│   └── hostel_residents.png
├── ui/
│   └── bunk_blunder_ui_effects.png
└── accessibility/
    └── bunk_blunder_accessibility.png
```

---

## 🏚️ Sprite Sheet 1: Hostel Exterior
**File:** `hostel_exterior.png`
**Dimensions:** 512x384 pixels

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Facade Main | (0, 0) | 256x256 | Converted Georgian townhouse, paint peeling artistically — "character" since 1987 |
| Sash Windows (3 states) | (256, 0) | 192x64 | Three 64x64 windows: lit, dark, condensation-fogged |
| Chimney Row | (448, 0) | 64x64 | Georgian chimney pots, one leaning |
| Main Sign | (256, 64) | 192x48 | "THE BUNK & BLUNDER" in cheerful letters (ironic) |
| Star Rating Plaque | (448, 64) | 64x48 | "★★★" — self-awarded, mounting screws visible |
| Subtitle Sign | (256, 112) | 192x32 | "Budget Beds, Priceless Memories" (also ironic) |
| Asterisk Fine Print | (448, 112) | 64x32 | "*hot water not guaranteed" in tiny honest type |
| Window Amenities Sign | (256, 144) | 128x48 | "FREE WI-FI • HOT SHOWERS* • LOCKERS" |
| Chalkboard | (384, 144) | 64x96 | "Tonight's Vibe: CHAOTIC" — the chalk has never been touched |
| Entry Door Closed | (448, 144) | 64x96 | Georgian door, brass gone dull |
| Stone Steps & Railing | (256, 192) | 128x64 | Worn steps, wobbling ironwork |

### Street Life:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Entry Door Open | (0, 256) | 64x96 | Interior beige glow, faint fluorescent hum implied |
| Exhausted Traveler Entering | (64, 256) | 64x96 | Backpack, hope, no idea |
| Traumatized Traveler Leaving | (128, 256) | 64x96 | Same person, 8 hours later, avoiding eye contact |
| Cobblestone Street Tile | (192, 256) | 128x64 | Market Street budget-district cobbles |
| Cobblestone Wet Variant | (320, 256) | 128x64 | Publandia default weather state |
| Streetlamp | (448, 256) | 64x128 | Georgian lamp, flickers in sympathy |
| Craic Tax Glow (Distant) | (192, 320) | 128x64 | Neon haze from the bar district — where guests come FROM |
| Puddle Reflections | (320, 320) | 64x64 | Reflects the ★★★ plaque, unkindly |
| Backpack Pile | (384, 320) | 64x64 | Abandoned outside at check-in queue peak |

### Technical Notes:
- Facade renders day/night via modulate tint; window states swap on time-of-day
- The chalkboard is a single static sprite by design — the joke is that it never changes
- Rain streaks handled by the effects sheet, not baked into facade

---

## 🛎️ Sprite Sheet 2: Reception — The Warning Zone
**File:** `reception_interior.png`
**Dimensions:** 512x384 pixels

### Room Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reception Backdrop | (0, 0) | 256x192 | Beige walls, The Smell rendered as subtle color grade |
| Reception Desk | (0, 192) | 192x96 | Scratched counter, bell nobody rings, Colm's domain |
| Desk Clutter | (192, 192) | 64x48 | Coffee mug strata, eight years deep |
| Key Card Stack | (192, 240) | 64x48 | Faded Hope Green cards, shuffled like tarot |

### The Wall of Forgotten Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Forgotten Items Wall | (256, 0) | 192x128 | Shelving of abandoned property — impressive collection |
| House Rules Sign | (448, 0) | 64x96 | Dense text, comprehensively ignored, slightly askew |
| The Traffic Cone | (448, 96) | 64x64 | From room 6. No one's claimed it. No one wants to claim it |
| Key Card Dispenser (Functional) | (256, 128) | 64x64 | Green light, working — enjoy it while it lasts |
| Key Card Dispenser (Jammed) | (320, 128) | 64x64 | Red light, card half-emerged — the other 50% |
| Lost Umbrella Cluster | (384, 128) | 64x64 | Forgotten-wall detail, all broken the same way |

### Fixtures & Flow:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fluorescent Tube Fixture | (256, 192) | 128x32 | Harsh institutional lighting bar |
| Worn Floor Tile | (256, 224) | 128x32 | Path to desk polished by ten thousand check-ins |
| Cleaner-vs-Humanity Haze | (384, 192) | 128x64 | Faint overlay: industrial cleaner losing the war |
| Breakfast Station | (0, 288) | 128x96 | Continental spread — toast and sadness |
| Coffee Machine (Real) | (128, 288) | 64x96 | The one honest thing in the building |
| Wi-Fi Password Chalk Note | (192, 288) | 96x48 | "BunkBlunder2024 — Capital B's. It works sometimes." |
| Luggage Heap | (192, 336) | 96x48 | Pre-check-in purgatory pile |
| Doorway to Dorms | (288, 288) | 64x96 | Abandon hope threshold |
| Doorway to Common Room | (352, 288) | 64x96 | Where strangers become stories |
| Reception Bell | (416, 288) | 32x32 | Dusty. Colm sees you anyway |
| "NO REFUNDS" Sign | (448, 288) | 64x32 | The most enforced rule in the building |
| Forgotten Single Shoe | (416, 320) | 32x32 | Just the one. Always just the one |
| Room 6 Door Tag | (448, 320) | 64x32 | Provenance of the cone. Ask no questions |
| Check-Out Sign | (416, 352) | 96x32 | "CHECK-OUT 10 AM" — nobody makes check-out |

### Technical Notes:
- Dispenser sprite swap is random per booking (50% jam rate drives dialogue beat)
- The Traffic Cone is an Area2D examine point and a "Lost and Found" quest object
- Haze overlay at 10% alpha, additive — present but deniable, like The Smell

---

## 🛋️ Sprite Sheet 3: Common Room — The Mixing Pot
**File:** `common_room.png`
**Dimensions:** 512x384 pixels

### Room & Furniture (Multiple Decades, Zero Coordination):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Common Room Backdrop | (0, 0) | 256x192 | Mismatched wallpaper eras meeting in one corner |
| Sofa, 1970s Floral | (0, 192) | 128x64 | Sagging in the shape of a thousand travelers |
| Armchair, 1980s Vinyl | (128, 192) | 64x64 | Cracked, repaired with tape, cracked again |
| Beanbag, 2000s Deflated | (192, 192) | 64x64 | More bag than bean |
| Coffee Table, Ringed | (0, 256) | 96x64 | Cup rings decades deep, geological record |
| Plastic Chair | (96, 256) | 64x64 | The overflow seating, the honest seating |
| Tasseled Lamp | (160, 256) | 64x64 | Someone's grandmother's, presumably |
| Microwave, Crusted | (224, 256) | 32x32 | Interior best left unlit |
| Kettle | (224, 288) | 32x32 | Limescale load-bearing at this point |

### The One Working Outlet & Kitchen:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The One Working Outlet | (256, 0) | 64x64 | Shrine-lit, socket worn smooth by pilgrimage |
| Daisy-Chained Power Strip | (320, 0) | 128x64 | Strip into strip into strip — dangerously loaded, gently smoking potential |
| Fridge of Mystery | (448, 0) | 64x128 | Labeled leftovers, none claimed, some sentient |
| Kitchen Area Base | (256, 64) | 192x128 | Biohazard-adjacent counters and hob |
| Sink Dish Mountain | (448, 128) | 64x64 | Structural. Do not remove the base plate |

### Notice Board & Events:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Notice Board | (256, 192) | 128x128 | Cork chaos — quest hook surface |
| Desperate Pleas Close-Ups | (384, 192) | 128x64 | "LOST: charger, dignity", "SEEKING: quiet roommate (impossible)" |
| Tour Advertisements | (384, 256) | 128x64 | "AUTHENTIC PUBLANDIA WALKING TOUR" — laminated optimism |
| Kitchen Disaster Frames | (0, 320) | 128x64 | Two 64x64 frames: small fire, smaller regret |
| Power Strip Failure Frame | (128, 320) | 64x64 | Blackout state — darkness, chaos, bonding |
| Rain Window | (192, 320) | 64x64 | Rain against common room glass, Publandia standard |
| Impromptu Party Props | (256, 320) | 96x64 | Cans, someone's speaker, questionable playlist implied |
| 3 AM Deep Chat Corner | (352, 320) | 96x64 | Two silhouettes, low lamp, unexpected depth |
| Mug Cluster | (448, 320) | 64x64 | Communal mugs, each one a former favorite |

### Technical Notes:
- Notice board is an Area2D quest surface — pleas layer swaps as side quests open/close
- Power strip failure frame swaps the room to 3 AM Blue palette + blackout vignette (effects sheet)
- Kitchen fire frames capped at 2 — the disaster is an event card, not a particle budget

---

## 🛏️ Sprite Sheet 4: Dorms & "Privates" — The Sardine Experience
**File:** `dorms_and_privates.png`
**Dimensions:** 1024x512 pixels

### Room Bases:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| 12-Bed Dorm Base | (0, 0) | 384x256 | Maximum density, maximum chaos — a social experiment |
| 8-Bed Dorm Base | (384, 0) | 320x256 | Standard misery configuration |
| 4-Bed Dorm Base | (704, 0) | 256x256 | The compromise |
| Locker Closed | (960, 0) | 64x64 | Dented steel, trust no one |
| Locker Open | (960, 64) | 64x64 | Empty except previous occupant's optimism |
| Locker Padlocked | (960, 128) | 64x64 | Player-secured state |
| "BRING YOUR OWN LOCK" Sign | (960, 192) | 64x64 | The hostel provides nothing but the hole |

### "Private" Rooms (Relative Term):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Private" Double | (0, 256) | 256x192 | The surrender option — walls don't reach the ceiling |
| "Private" Single | (256, 256) | 256x192 | Actual privacy, marginal dignity |
| Wall-Gap Detail | (512, 256) | 128x64 | The gap where wall meets not-ceiling; sound lines pouring over |

### Bunk Beds (Questionable Structural Integrity):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bunk Bed, Empty | (640, 256) | 96x128 | Visible weld wobble, ladder of faith |
| Bunk Bed, Top Occupied | (736, 256) | 96x128 | Sagging mattress silhouette from below |
| Bunk Bed, Both Occupied | (832, 256) | 96x128 | Full sardine state |
| Bunk 4B — Derek's | (928, 256) | 96x128 | Nameplate worn smooth, permanent occupancy aura, earplugs on the post |
| Ladder Detail | (512, 320) | 64x64 | The loose rung. THE loose rung |
| Bed Occupancy Icons | (576, 320) | 64x64 | Four 32x32 states: empty / reserved / occupied / Derek |

### Dorm Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dorm Doorways (Rooms 2/4/6) | (512, 384) | 192x64 | Three numbered doors — room 2 (the couple), room 4, room 6 (cone origin) |
| Ceiling Fan, Wobbling | (704, 384) | 64x64 | Rotation optional, wobble guaranteed |
| Dorm Fluorescent Bar | (768, 384) | 128x32 | Overhead tube, one bulb dead (see effects) |
| Mystery Stain, Ceiling | (768, 416) | 64x32 | Directly above bunk 7. Unexplained |
| Mystery Stain, Floor | (832, 416) | 64x32 | Adjacent to lockers. Also unexplained |
| Rain-Streaked Dorm Window | (896, 384) | 128x128 | Rain against glass — the free ambience nobody asked for |
| Top/Bottom Preference Tags | (512, 448) | 128x64 | Seasoned Traveler bunk-request UI props |
| Bedsheet, Suspicious | (640, 448) | 128x64 | Officially clean. Emotionally unclean |
| Alarm Clock, 4 AM | (768, 448) | 64x64 | The Early Riser's weapon of choice |
| Flip-Flop Pair | (832, 448) | 64x64 | Shower armor, dorm-side staging |
| Curtain Divider | (0, 448) | 128x64 | Privacy theater for bottom bunks |
| Reading Light Cone | (128, 448) | 64x64 | The polite roommate's compromise |
| Derek's Spare Earplugs | (192, 448) | 64x64 | "Here, take my spare pair." — quest/gift object |
| Suitcase Explosion | (256, 448) | 128x64 | Contents deployed across three bunk radii |
| Plastic Bags, Mid-Rustle | (384, 448) | 128x64 | The 5 AM packing soundscape, visualized |

### Technical Notes:
- Room bases are swapped per booking tier; bunk sprites instanced over base at fixed anchor rows
- Wall-Gap Detail composites onto both private rooms — the sound lines are the point
- Bunk 4B always renders occupied; Derek is not procedurally generated, Derek is a constant

---

## 🚿 Sprite Sheet 5: Shower Block — The Gauntlet
**File:** `shower_block.png`
**Dimensions:** 512x384 pixels

### The Block:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shower Block Base | (0, 0) | 256x192 | Tiled room, drain of despair centered |
| Stall 1 — Working, HOT | (256, 0) | 64x128 | Steam rising, today's winner (rotates) |
| Stall 2 — Working, Cold | (320, 0) | 64x128 | Functional. Technically |
| Stall 3 — Broken | (384, 0) | 64x128 | Bag over the showerhead like a crime scene |
| Stall 4 — Broken | (448, 0) | 64x128 | "OUT OF ORDER" sign older than some guests |
| Hot Water Rotation Sign | (256, 128) | 128x64 | Chalk: "TODAY'S HOT SHOWER: #__" — number slot swappable |
| "FLIP-FLOPS MANDATORY" Sign | (384, 128) | 128x64 | The floor has seen things |

### Floor & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Tile (Has Seen Things) | (0, 192) | 128x64 | Grout tone unreproducible in nature |
| Drain Close-Up | (128, 192) | 64x64 | Examine at your own risk |
| Fogged Mirror | (192, 192) | 64x64 | Mercifully fogged |
| 5-Minute Timer Dial | (256, 192) | 64x64 | Enforced by water temperature collapse |
| Temperature Collapse Gauge | (320, 192) | 64x64 | Needle plunging from red to Shame Red to blue |
| Queue Bench | (384, 192) | 128x64 | Where morning regret compounds |

### The Queue:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Towel Rack, Overloaded | (0, 256) | 128x64 | Load rating exceeded in 1994 |
| Abandoned Toiletry Shelf | (128, 256) | 128x64 | 2-in-1 bottles, all empty, all kept |
| Steam Bank Overlay | (256, 256) | 128x64 | Hot-stall glory cloud |
| Cold Yelp Splash Frame | (384, 256) | 64x64 | The moment of temperature betrayal |
| Shower Curtain, Insufficient | (448, 256) | 64x128 | Covers 70% of the job requirement |
| Queue Position Markers | (0, 320) | 128x64 | Floor numbers 1-8 — the math doesn't work |
| Puddle Trail | (128, 320) | 128x64 | Stall-to-bench evidence line |
| Wet Footprints | (256, 320) | 96x64 | Flip-flop tread, as mandated |
| "SHOWER FAIRLY" Plea Sign | (352, 320) | 96x64 | Handwritten, laminated, ignored |

### Technical Notes:
- Hot stall position randomizes daily; rotation sign number slot updates to match (Seasoned Travelers get the tell)
- Steam overlay only renders on the current hot stall — steam IS the information
- Timer dial and gauge drive the Shower Gauntlet mini-challenge UI (sheet 8)

---

## 😶 Sprite Sheet 6: Colm O'Brien
**File:** `colm_obrien.png`
**Dimensions:** 384x384 pixels

### Colm States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle Behind Desk | (0, 0) | 96x128 | Permanent exhaustion, coffee IV implied |
| Handing Key Card | (96, 0) | 96x128 | The Colm Method: key, luck, no questions |
| Wishing Luck | (192, 0) | 96x128 | Flat palm raise — you'll need it |
| Directing to Showers | (288, 0) | 96x128 | "Number 3 has hot water today." |
| Beyond Judgment | (0, 128) | 96x128 | Past surprise, approaching transcendence |
| Coffee Sip | (96, 128) | 96x128 | Eyes closed, brief peace |
| Late-Night Philosophy Lean | (192, 128) | 96x128 | Elbows on desk, 3 AM crucible talk |
| Seasoned-Traveler Nod | (288, 128) | 96x128 | He remembers your name now. This is enormous |

### Colm Expressions:
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Exhausted Default | (0, 256) | 48x48 | Eight years deep |
| Past Surprise | (48, 256) | 48x48 | You cannot shock this man |
| Almost Amused | (96, 256) | 48x48 | The closest he gets |
| Pre-Coffee | (144, 256) | 48x48 | Do not approach |
| "Please Don't Try" | (192, 256) | 48x48 | For guests who announce plans |

### Colm Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Coffee Mug (IV-Adjacent) | (240, 256) | 48x48 | Never empty, never full |
| Key Card Fan | (288, 256) | 48x48 | Dealt like fate |
| "COLM" Name Tag | (336, 256) | 48x48 | Crooked since the gap year that never ended |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Default | (0, 304) | 64x48 | Exhausted monotone, rendered |
| Portrait Deadpan | (64, 304) | 64x48 | For dignity inquiries |
| Portrait Philosophy | (128, 304) | 64x48 | "This place is a crucible." |
| Portrait Morning-After | (192, 304) | 64x48 | "You'll hear about it. Everyone heard about it." |
| Portrait Name-Remembered | (256, 304) | 64x48 | Seasoned Traveler reward warmth (trace amounts) |
| Hands Sliding Key Card | (320, 304) | 64x48 | The check-in ritual close-up |

### Micro-Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Eye Bags Detail | (0, 352) | 32x32 | Load-bearing |
| Stubble Detail | (32, 352) | 32x32 | Day four, always day four |

### Technical Notes:
- Colm's whole performance is restraint — no exaggerated frames; the monotone is visual too
- Portrait Deadpan pairs with the dignity line; hold it a beat longer than comfortable
- Seasoned-Traveler Nod unlocks only at `nights_stayed >= 5`

---

## 👥 Sprite Sheet 7: Hostel Residents & Roommate System
**File:** `hostel_residents.png`
**Dimensions:** 512x512 pixels

### Resident NPCs (Standing):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Derek, Awake | (0, 0) | 64x96 | Three months of "finding himself," knows everything about Dublin |
| Derek, Advice-Giving | (64, 0) | 64x96 | Unsolicited wisdom mid-delivery |
| Brigitte, With System | (128, 0) | 64x96 | German efficiency, clipboard, color-coded doom |
| Brigitte, Unraveling | (192, 0) | 64x96 | Three days in — the schedule is dead |
| Gary, Journaling | (256, 0) | 64x96 | Gap year profundity, pen mid-epiphany |
| Gary, Profound Gesture | (320, 0) | 64x96 | Explaining what the Quay REPRESENTS |
| Mysterious Older Traveler | (384, 0) | 64x96 | 50s, enigmatic, stayed here in '92 under a different name |
| The Witness | (448, 0) | 64x96 | Awkward eye contact, deciding whether to mention it |

### Player & Situational Poses:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Embarrassed Player — Realization | (0, 96) | 64x96 | "...everyone heard me come in last night" |
| Embarrassed Player — Face Cover | (64, 96) | 64x96 | Full-hand shame shield |
| Witness Eye-Contact Two-Shot | (128, 96) | 128x96 | Player + Witness locked in mutual "cool cool cool" |
| Party Returnee Stumble | (256, 96) | 64x96 | 3 AM entry, loud, apologetic |
| Sleepwalker Wandering | (320, 96) | 64x96 | Arms out, trajectory: your bunk |
| The Couple (Bunk Silhouette) | (384, 96) | 128x96 | They think they're being quiet. They're not |

### Sleepers (Horizontal):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Derek Snoring in 4B | (0, 192) | 128x64 | Legendary output, sound lines shaking the frame |
| Snoring NPC, Generic | (128, 192) | 96x64 | Horizontal noise maker, dorm filler |
| Restless Sleeper Frames | (224, 192) | 128x64 | Two 64x64 toss-and-turn frames |
| Crier Under Blanket | (352, 192) | 96x64 | Quiet sobbing lump, existential crisis in progress |
| Phone Addict Glow Silhouette | (448, 192) | 64x64 | Face lit cyan, thumbs going |

### Group Scenes:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shower Queue Lineup | (0, 256) | 256x96 | Four figures in towels and despair, positions 1-4 |
| Morning Shame Shuffle Frames | (256, 256) | 192x96 | Three 64x96 frames — head down, exit trajectory, no eye contact |
| Mysterious Traveler Vanish | (448, 256) | 64x96 | Half-faded — appears, shares wisdom, is gone |

### Roommate Type Icons (Reveal System, 48x48 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Silent Type | (0, 352) | 48x48 | Closed eyes + single Z — the +20% unicorn |
| The Snorer | (48, 352) | 48x48 | Triple jagged Z — industrial grade, -30% |
| The Phone Addict | (96, 352) | 48x48 | Glowing screen icon, -15% |
| The Early Riser | (144, 352) | 48x48 | 5 AM alarm bell, -25% |
| The Party Returnee | (192, 352) | 48x48 | Tilted bottle + stars, -40% |
| The Crier | (240, 352) | 48x48 | Teardrop, -10% (+sympathy) |
| The Talker | (288, 352) | 48x48 | Overflowing speech bubble, -20% OR +info |
| The Witness | (336, 352) | 48x48 | Wide eye icon — Embarrassed risk |
| The Sleepwalker | (384, 352) | 48x48 | Walking Z-trail figure, -20% (+story) |
| The Couple | (432, 352) | 48x48 | Two overlapping hearts, ostensibly quiet, -35% |

### Roommate System Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Roommate Risk Frames | (0, 400) | 144x48 | Three 48x48 icon borders: diagonal-stripe (safe) / dotted (risky) / zigzag (chaos) — pattern-coded, never color-only |
| Derek's Earplug Offer Hand | (144, 400) | 64x48 | The gift frame — "Earplugs and low expectations." |
| Gary's Journal Prop | (208, 400) | 48x48 | "VOLUME III: THE QUAY" |
| Brigitte's Schedule, Annotated | (256, 400) | 96x48 | The PLAN, crossed out in escalating despair |
| Traveler's '92 Token | (352, 400) | 48x48 | Cryptic keepsake — quest hint object |
| Awkward Silence Bubble | (400, 400) | 64x48 | "..." — deployed after every Witness encounter |
| Existential Sigh Wisp | (464, 400) | 48x48 | The dorm's sixth ambient sound, visualized |

### Technical Notes:
- Roommate icons pair 1:1 with the 10-type random generation table; icon + risk frame render on the Roommate Reveal panel
- Rotating residents draw from this sheet per night seed; Derek is exempt from rotation (see: constant)
- Shower Queue Lineup crops per-figure for queue-position UI reuse

---

## 🎮 Sprite Sheet 8: UI & Effects
**File:** `bunk_blunder_ui_effects.png`
**Dimensions:** 512x512 pixels

### Booking & Rest UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Room Selection Panel | (0, 0) | 256x192 | Five room rows: 12/8/4-bed, "private" double/single — price, privacy, chaos level per row |
| Rest Quality Meter | (256, 0) | 128x64 | 20%-90% band, pattern-hatched segments + numeral readout |
| Embarrassed Status Popup | (384, 0) | 128x64 | Shame Red banner: "EMBARRASSED (-10 Bravado, 4 hrs)" |
| Roommate Reveal Panel | (256, 64) | 192x128 | Icon slots for tonight's random draw — the horror lottery card |
| Shower Queue Timer | (448, 64) | 64x128 | Vertical hot-water countdown, position number window |
| Wi-Fi Login Screen | (0, 192) | 192x128 | "BunkWiFiGuest" — connection: unreliable; speed: theoretical |
| Sleep Quality Result Card | (192, 192) | 192x128 | Morning summary: restoration %, roommate recap, incident log |
| Seasoned Traveler Badge | (384, 192) | 64x64 | Five-night veteran crest — earplugs rampant on a field of beige |
| Key Card State Icons | (448, 192) | 64x64 | Two 32x64 icons: card-works / card-dead |
| "NO REFUNDS" Confirm Stamp | (384, 256) | 128x64 | Slams onto booking confirmation, ink still wet |

### Atmosphere Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dust in Fluorescent Beam | (0, 320) | 96x64 | Motes drifting through harsh light |
| Shower Steam Puffs | (96, 320) | 96x64 | Three 32x64 frames, hot stall only |
| Broken Bulb Flicker Frames | (192, 320) | 96x64 | Three 32x64 frames: off / dim / on — the one bulb, always the one |
| 3 AM Thud Shockwave Rings | (288, 320) | 96x64 | Radiating rings from ceiling — the mystery, visualized, never explained |
| Phone Screen Glow | (384, 320) | 64x64 | Cyan cone in dark dorm |
| Mysterious Floating Particles | (448, 320) | 64x64 | Origin unknown, best not investigated |

### Event Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Snore Zzz Chain Frames | (0, 384) | 128x64 | Multi-frequency: big Z, small z, jagged Z — the dorm chorus |
| Alarm Radiating Rings | (128, 384) | 64x64 | The distant phone alarm that never stops |
| Bunk Creak Jolt Lines | (192, 384) | 64x64 | Frame shake lines on any bunk movement |
| Power Strip Spark | (256, 384) | 64x64 | The daisy chain's warning shot |
| Blackout Vignette | (320, 384) | 64x64 | Power failure darkness overlay (9-slice) |
| Rain-on-Window Streaks | (384, 384) | 64x64 | Tileable streak overlay for all windows |
| Cold Shower Shiver Lines | (448, 384) | 64x64 | "Shocked Awake" status visual |

### Morning Effects & Status Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Morning Light Shaft | (0, 448) | 128x64 | Gray Publandia dawn through dorm window — judgment illumination |
| "Oh No" Realization Drop | (128, 448) | 64x64 | The shadow that falls over the player at memory-return |
| Craic Tax Afterglow Haze | (192, 448) | 128x64 | Door-frame aura on impaired 2 AM arrivals from the bar district |
| Status Icon Set | (320, 448) | 128x64 | Four 32x32 icons + labels: Sleep Deprived / Shocked Awake / Hostel Bonded / Embarrassed |
| Free Night Voucher | (448, 448) | 64x64 | Hostel Hero reward — the highest honor Colm can bestow |

### Technical Notes:
- Rest Quality Meter segments carry hatch patterns AND numerals — value never reads by color alone
- Roommate Reveal composites icons + risk frames from sheet 7 at runtime
- All effect frames sized for CPUParticles2D texture slots or simple AnimatedSprite2D loops

---

## 🎬 Animation Specifications

### Snoring Cycle (Derek Grade):
- **Duration:** 4 seconds loop
- **Frames:** 4
- **Pattern:** Inhale rise (1) → peak Zzz burst (2) → rattle hold (3) → collapse exhale (4) → loop
- **Trigger:** Constant while any Snorer-type occupies a bunk; Derek's 4B instance never stops
- **Purpose:** The dorm's dominant ambient comedy — sleep quality made visible
- **Audio Sync:** Multi-frequency snore layers; big Z frames sync to bass snore, small z to the whistle
- **Mobile Optimization:** Static Zzz sprite with 2-frame alpha pulse on low-end devices

### Broken Bulb Flicker:
- **Duration:** Random intervals, 8-30 seconds between events; each flicker 0.4 seconds
- **Frames:** 3 (off / dim / on)
- **Pattern:** on → dim → off → dim → on (quick stutter)
- **Trigger:** Timer, constant in dorm and shower block scenes
- **Purpose:** The one permanently broken bulb — institutional decay on a loop
- **Audio Sync:** Faint fluorescent buzz drop-out on the off frame
- **Mobile Optimization:** Alpha toggle only, no glow shader; disabled entirely in reduced-motion mode

### Shower Queue Shuffle:
- **Duration:** 2 seconds per position advance
- **Frames:** 3
- **Pattern:** Weight shift left → step forward → settle sigh → hold until next advance
- **Trigger:** Queue position change during the Shower Gauntlet
- **Purpose:** Makes the queue feel geological; each advance is a tiny hollow victory
- **Audio Sync:** Flip-flop slap on the step frame; distant shower running throughout
- **Mobile Optimization:** Snap-to-position with no tween below medium LOD

### Morning Shame Shuffle:
- **Duration:** 3 seconds, plays once on morning exit while Embarrassed
- **Frames:** 3
- **Pattern:** Head drop → shoulder hunch walk → door escape (no loop, mercifully)
- **Trigger:** Player exits dorm with "Embarrassed" status active
- **Purpose:** The walk of shame as a game verb — witnesses watching optional but likely
- **Audio Sync:** The quiet "oh no" morning shame sound on frame 1; awkward silence after
- **Mobile Optimization:** None needed (single short one-shot)

### Embarrassment Reaction:
- **Duration:** 1.5 seconds
- **Frames:** 2 (Realization → Face Cover)
- **Pattern:** Realization hold (1s) → face cover snap (0.5s) → hold until popup dismissed
- **Trigger:** "Embarrassed" status acquisition (witnessed regrettable act)
- **Purpose:** Status feedback beat; pairs with the Shame Red popup
- **Audio Sync:** Awkward-silence stinger cuts all ambient for 1 second — the cruelest sound is nothing
- **Mobile Optimization:** None needed

### Colm Idle Cycle:
- **Duration:** 12 seconds loop
- **Frames:** Idle (6s) → coffee sip (2s) → beyond-judgment stare (3s) → micro-sigh return (1s)
- **Pattern:** Sequential, weighted toward Idle
- **Trigger:** Constant at reception
- **Purpose:** Eight years of this, communicated in twelve seconds
- **Audio Sync:** Coffee sip slurp, barely audible; nothing else — Colm generates no drama
- **Mobile Optimization:** Drop coffee sip beat; hold Idle/stare alternation

### Phone Glow Pulse (Dark Dorm):
- **Duration:** 6 seconds loop
- **Frames:** 2
- **Pattern:** Glow bright (typing) → dim (reading) → loop
- **Trigger:** Phone Addict roommate present, night scene
- **Purpose:** The cyan lighthouse of inconsiderate scrolling
- **Audio Sync:** Soft keyboard tap cluster on bright frame
- **Mobile Optimization:** Static glow cone, no pulse

### The 3 AM Thud:
- **Duration:** 1 second, once per night, 03:00 game time
- **Frames:** 3 (ring expand)
- **Pattern:** Ring 1 → ring 2 → ring 3 → gone; never repeated, never explained
- **Trigger:** Timer, every night, guaranteed
- **Purpose:** The hostel's signature mystery — players will theorize, the game will never answer
- **Audio Sync:** Single deep thud; all snoring pauses for exactly 2 seconds after, then resumes
- **Mobile Optimization:** Single-frame flash version

### Shower Steam Rise:
- **Duration:** 3 seconds loop
- **Frames:** 3
- **Pattern:** Puff spawn → drift up → dissipate, staggered spawning
- **Trigger:** Hot stall active (the one, the only)
- **Purpose:** Marks today's hot shower — steam is the tell Seasoned Travelers read
- **Audio Sync:** Shower running loop while active
- **Mobile Optimization:** Single static steam bank sprite (also the reduced-motion variant)

### Dust in Fluorescent Light:
- **Duration:** Continuous drift
- **Frames:** CPUParticles2D, 8 particles max
- **Pattern:** Slow downward drift with lateral wander inside beam cone
- **Trigger:** Constant in reception and dorm scenes
- **Purpose:** Institutional atmosphere — the light is harsh AND dirty
- **Audio Sync:** None
- **Mobile Optimization:** 4 particles at medium LOD, static overlay at low

---

## ♿ Accessibility Sprite Requirements
**File:** `bunk_blunder_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Room Selection Panel, Bold | (0, 0) | 96x64 | Thick-bordered booking rows, enlarged price/chaos text |
| Embarrassed Popup, Bold | (96, 0) | 96x64 | Oversized status banner, heavy outline, icon + text |
| Reception Desk Hotspot Outline | (192, 0) | 64x64 | White-on-dark outline for Colm's interaction zone |
| Bunk Selection Outline | (0, 64) | 64x64 | High-visibility bunk pick highlight (Seasoned Traveler perk) |
| Shower Timer, Bold | (64, 64) | 64x64 | Enlarged countdown numerals with thick ring |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Broken Bulb, Steady | (128, 64) | 64x64 | Constant dim tube — flicker stutter disabled |
| Steam, Static | (192, 64) | 64x64 | Fixed steam bank replacing rising puff particles |
| Phone Glow, Steady | (0, 128) | 32x32 | Non-pulsing glow cone state |
| Rain, Static Overlay | (32, 128) | 32x32 | Fixed streak texture replacing animated window rain |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Snore Zzz, Multi-Frequency | (64, 128) | 32x32 | Stacked big-Z/small-z glyph — bass snore vs. whistle, both readable |
| Distant Phone Alarm Bell | (96, 128) | 32x32 | Persistent small bell with radiating arcs — it's always going, somewhere |
| Bunk Creak Lines | (128, 128) | 32x32 | Jolt lines glyph on any bunk movement |
| Plastic Bag Rustle Glyph | (160, 128) | 32x32 | Crinkle burst for the 5 AM packing ritual |
| 3 AM Thud Burst | (192, 128) | 32x32 | Single heavy impact star — the nightly mystery must land without sound |
| Key Card Beep Flash | (224, 128) | 32x32 | Green check flash (works) / red X flash (jammed) — shape-coded both ways |
| Shower Timer Tick Rings | (0, 160) | 32x32 | Shrinking ring per elapsed minute of the 5-minute limit |
| "Oh No" Morning Shame Glyph | (32, 160) | 32x32 | Small deflation glyph replacing the quiet realization sound |
| Shower Running Waves | (64, 160) | 32x32 | Water-line glyph while any stall is active |
| Hushed Conversation Dots | (96, 160) | 32x32 | Low-opacity speech dots for whispered dorm talk |
| Snoring Crescendo Stack | (128, 160) | 32x32 | Z-stack growing glyph for the synchronized-snoring stinger |
| Awkward Silence Ellipsis | (160, 160) | 32x32 | "..." burst when ambient cuts after embarrassment |
| Temperature Yelp Spike | (192, 160) | 32x32 | Jagged spike glyph on hot-water collapse |
| Alarm Acknowledged Check | (224, 160) | 32x32 | Confirmation tick when an alarm is finally silenced |

### Colorblind Considerations:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rest Quality Meter, Patterned | (0, 192) | 128x32 | Hatch/dot/solid segment fills + numeral — restoration % never color-only |
| Roommate Risk Shape Tags | (128, 192) | 96x32 | Circle (safe) / triangle (risky) / octagon (chaos) shape tags for reveal panel |
| Hot Shower Marker, Numbered | (224, 192) | 32x32 | Stall number badge — hot stall identified by numeral, not steam tint |
| Room Chaos Level Pips | (0, 224) | 128x32 | Pip-count chaos rating (1-5 pips) for booking rows |
| Key Card State Icons, Shaped | (128, 224) | 64x32 | Embossed check/X shapes independent of green/red |
| Touch Target Padding Guide | (192, 224) | 64x32 | 44px minimum hit-zone template for all interactive elements |

- Rest quality and roommate risk are double-coded everywhere: pattern + shape + numeral, color as garnish only
- All booking rows, roommate icons, shower queue slots, and examine hotspots meet the 44px minimum touch target
- Every critical sound in the audio design has a sprite above — the hostel must be fully survivable with the sound off

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback for legacy devices); Roommate Reveal panel and dialogue portraits at ASTC 4x4 — text must stay crisp
- **Android:** ETC2 with alpha
- **Fallback:** Lossless PNG for UI sheet and accessibility sheet (readable text is non-negotiable)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| bunk_blunder_environment | exterior, reception, common room, shower block | 2048x2048 |
| bunk_blunder_dorms | dorms_and_privates (loaded on booking only) | 1024x1024 |
| bunk_blunder_characters | colm_obrien, hostel_residents | 1024x1024 |
| bunk_blunder_ui_fx | ui_effects, accessibility | 1024x1024 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full dorm crowd sprites, all snore/steam/dust particles, flicker + glow effects |
| Medium | Dorm crowd capped at 6 visible sleepers, dust at 4 particles, static steam bank |
| Low | Static snoring indicators (per profile), no particles, alpha-toggle flicker only, single ambient sleeper sprite per dorm |

### Performance Targets:
- **Target FPS:** 60 (12-bed dorm night scene is the stress case; the profile's 45 FPS figure is the never-dip-below floor for that scene on minimum-spec devices)
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 32 MB maximum
- **Particle Limit:** 12 (8 dust + 3 steam + 1 spark reserve)

### Performance Notes:
- Simplified dorm crowd: bunk occupants render as sheet-7 horizontal sprites, never full NPC scenes — the atmosphere is audio-focused by design, so sprites carry less load
- Dorm atlas loads on booking, unloads on checkout; only one dorm base resident in memory at a time
- Snoring is 4 frames on one AnimatedSprite2D per sleeper, shared frames across instances
- The 3 AM thud is one-shot; rings despawn after 1 second
- Rain streaks are a single tileable overlay reused across every window in the building

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- CPUParticles2D (not GPU) for dust, steam, and floating particles; broken-bulb flicker via alpha toggle timer, disabled in reduced-motion mode
- **Random roommate generation:** on booking confirm, roll N-1 roommates from the 10-type table (Silent Type, Snorer, Phone Addict, Early Riser, Party Returnee, Crier, Talker, Witness, Sleepwalker, Couple); apply cumulative rest modifiers to a 50% base, clamp to 20%-90% restoration; Roommate Reveal panel composites sheet-7 icons + risk frames from the roll
- **The Embarrassed status system:** trigger checks on drunk entry (balance check), late calls, bathroom incidents, sleep-talking, wrong-bed events, and food-status snoring; applies -10 Bravado for 4 hours, swaps in Witness dialogue branches, and feeds the reputation-spread flag read by The Blarney Trap
- **The Shower Gauntlet:** morning queue mini-challenge — random position 1-8, shared hot-water timer depleting per user, success grants clean buff, failure applies "Shocked Awake" (shiver-lines effect), skip applies -Charisma until a bath is found elsewhere
- Area2D examine points: the traffic cone, House Rules sign, notice board, fridge of mystery, wall-gap detail, bunk 4B, "Reserved" queue markers
- State tracking per `bunk_blunder_state` (nights_stayed, seasoned_traveler, current_room_type, roommate_roll[], embarrassed_until, witness_npc_id, hot_stall_today, derek_befriended, cone_quest_stage)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Snore Zzz Chain (4-frame cycle) | Multi-frequency snoring layers | Bass snore on big-Z frame, whistle on small-z frame |
| Alarm Radiating Rings | Distant phone alarm (always) | Continuous low loop; rings pulse on each ring tone |
| Steam Puffs / hot stall | Shower running | Loop while hot stall occupied |
| Hushed Conversation Dots | Whispered dorm conversations | Random night intervals, ducks under snoring |
| Bunk Creak Jolt Lines | Bunk bed creaking | On any bunk enter/exit/toss frame |
| Plastic Bags Mid-Rustle | Plastic bag rustling | 5 AM Early Riser packing sequence |
| 3 AM Thud Shockwave Rings | The mysterious 3 AM thud | 03:00 nightly; all snoring pauses 2s after |
| Key Card State Icons | Key card beep (accept/reject tones) | On dispenser/door interaction frame |
| Shower Queue Timer | Shower timer countdown ticks | Tick per minute; temperature-collapse sting at 5:00 |
| Morning Shame Shuffle frame 1 | The quiet "oh no" realization | On head-drop frame; awkward silence follows |
| Snoring Crescendo Stack | Synchronized snoring stinger | When 3+ Snorer-types align phase |
| Embarrassment Reaction | Awkward-silence stinger (all ambient cuts) | 1s silence on face-cover frame |
| Cold Yelp Splash Frame | Shower temperature yelp | On hot-water collapse mid-shower |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Roommate Situation | Roommate icons, Brigitte Unraveling, Derek Advice-Giving, Roommate Reveal panel | Help or sabotage a roommate — icon roll seeds the target; outcomes adjust rest modifiers and Bravado |
| Lost and Found | The Traffic Cone, Forgotten Items Wall, Room 6 Door Tag, Notice Board pleas | Track down an item "borrowed" by a former guest; the cone is the tutorial red herring nobody claims |
| The Witness Protection | The Witness, Eye-Contact Two-Shot, Awkward Silence Bubble, Embarrassed popup | Prevent the embarrassing story from spreading before it reaches The Blarney Trap |
| Hostel Hero | Kitchen Disaster frames, Power Strip Failure, Blackout Vignette, Free Night Voucher | Help during crisis (fire alarm, blackout, breakdown) — +30 Bravado, free night, "Legend" track |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Blarney Trap | Colm's recommendation dialogue portraits; Embarrassed reputation flag surfaces in Trap gossip | Story-spread notification ping if Witness Protection failed |
| The Craic Tax | Craic Tax Afterglow Haze on 2 AM arrivals; Party Returnee sprite is usually inbound from there | Stumble-in door transition with haze aura, balance-check camera sway |
| Murphy's Lawless | Desperate-supply-run props (earplugs, flip-flops, padlocks) reference its shelf sprites | Standard street transition; "back in 10 min" note on reception desk |
| Café NORA | Sleep Quality Result Card offers "recover properly?" link on sub-40% nights | Morning-light crossfade toward actual coffee and dignity |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Georgian grandeur gone to seed — a townhouse that peaked in 1830 and has been apologizing since 1987"
- **Color Mood:** Institutional Beige and Exhaustion Gray doing the heavy lifting; faded Hope Green signage promising what Mystery Stain Brown delivers; 3 AM Blue and Phone Glow Cyan own the night scenes
- **Lighting:** Harsh fluorescent everywhere, one permanently broken flickering bulb, gray Publandia daylight through rain-streaked sash windows, phone-glow as the dorm's only warm(ish) light
- **Texture:** Peeling paint, worn linoleum paths, cup-ring geology, grout tones unreproducible in nature, bedding that is officially clean

### Environmental Storytelling:
- The self-awarded ★★★ plaque with visible mounting screws, directly above the honest asterisk: "*hot water not guaranteed"
- The chalkboard reading "Tonight's Vibe: CHAOTIC" — untouched chalk proving it has never needed updating
- The Wall of Forgotten Items with its unclaimed traffic cone from room 6: a museum of nights nobody remembers
- The one working outlet, shrine-lit, with its dangerously daisy-chained power strip — backpacker infrastructure in one image
- Walls that don't reach the ceiling in the "private" rooms: the wall-gap detail with sound lines pouring over IS the satire of paying extra for privacy
- Bunk 4B: nameplate worn smooth, earplugs on the post — Derek as permanent fixture, load-bearing resident

### Character Integration Notes:
- Colm is the anti-Seamus: same exhaustion genus, zero drama — every frame is restraint, monotone rendered visually; the Seasoned-Traveler Nod must feel like a knighthood
- Residents rotate nightly except Derek, who is a constant, like gravity or the 3 AM thud
- The Witness two-shot composition should hold uncomfortable framing — too much space between them, both aware of it
- Sleepers are horizontal comedy: the snore cycle carries the dorm, so those 4 frames get polish priority

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Roommate Reveal Panel** - Tonight's random draw of ten possible horrors, shareable as a personality test ("I got 2 Snorers and a Couple, pray for me")
2. **The Traffic Cone on the Forgotten Items Wall** - Unclaimed, unexplained, from room 6 — the game's most meme-able prop
3. **"Tonight's Vibe: CHAOTIC"** - The chalkboard that has never needed changing
4. **The ★★★ Self-Awarded Plaque + Asterisk Sign** - Both signs in one frame is the whole review economy satirized
5. **The 3 AM Thud** - Shockwave rings, every snore stopping for two seconds, no explanation ever — players WILL post theories
6. **The Wall-Gap "Private" Room** - Sound lines pouring over the wall that doesn't reach the ceiling
7. **The One Working Outlet** - Shrine lighting, daisy-chained power strip, seven devices, one socket

### Quote Potential:
- "You're the third person to ask about their dignity this morning. I haven't seen it."
- "Someone left a traffic cone in room 6. No one's claimed it. No one wants to claim it."
- "Room type? Grand. That's €18. Key card. Room 4. Good luck."
- "Breakfast is 7-9. Continental means toast and sadness. Coffee's real though."
- "The couple in room 2 thinks they're quiet. They're not. Nobody's told them. Nobody will."
- "The snoring guy in 4B? That's Derek. He's been here two weeks. I think he's finding himself. Loudly."
- "The 12-bed dorm is a social experiment. The 4-bed is a compromise. The private room is surrender."
- "I had a SCHEDULE. A PLAN. This place has destroyed both. In three days."
- "So... last night... you, uh... don't worry, I won't... yeah. Cool. Cool cool cool."
- "Check-out is 10 AM. Nobody makes check-out. I've stopped mentioning it."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | hostel_exterior.png | 512x384 |
| 2 | reception_interior.png | 512x384 |
| 3 | common_room.png | 512x384 |
| 4 | dorms_and_privates.png | 1024x512 |
| 5 | shower_block.png | 512x384 |
| 6 | colm_obrien.png | 384x384 |
| 7 | hostel_residents.png | 512x512 |
| 8 | bunk_blunder_ui_effects.png | 512x512 |

**Total Estimated Memory:** ~22 MB (within the 32 MB location budget with atlas overhead and the on-demand dorm atlas unloaded outside bookings)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `hostel_exterior.png` (512x384)
- [ ] `reception_interior.png` (512x384)
- [ ] `common_room.png` (512x384)
- [ ] `dorms_and_privates.png` (1024x512)
- [ ] `shower_block.png` (512x384)
- [ ] `colm_obrien.png` (384x384)
- [ ] `hostel_residents.png` (512x512)
- [ ] `bunk_blunder_ui_effects.png` (512x512)
- [ ] `bunk_blunder_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (Forgotten Items Wall items and Notice Board pleas on separate layers — both surfaces are designed to accumulate)
- **Documentation:** Animation timing reference sheet (snore cycle phasing, flicker intervals, 3 AM thud timing, shower queue advance)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Institutional Beige #D2B48C, Exhaustion Gray #808080, Mystery Stain Brown #8B4513, Hope Green #90EE90)
- [ ] The Traffic Cone reads instantly as absurd on the Forgotten Items Wall — it is the location's museum piece
- [ ] The one hot shower is identifiable by steam + rotation sign number + accessibility numeral badge, all three agreeing
- [ ] The wall-gap detail on "private" rooms reads clearly — sound lines over the not-ceiling ARE the joke
- [ ] Bunk 4B carries Derek's permanence: worn nameplate, earplugs on post, occupied at all times
- [ ] ★★★ plaque screws and "*hot water not guaranteed" fine print legible on examine
- [ ] Accessibility visual alternatives included for all audio cues (snore frequencies, phone alarm, creak, rustle, thud, beep, timer, "oh no")
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (budget travel delusion vs. shared-misery reality) is clear throughout all assets
- [ ] Easter eggs discoverable: room 6 door tag, single forgotten shoe, "SHOWER FAIRLY" plea, Brigitte's annotated schedule, the '92 token
- [ ] Mobile performance optimized (12-particle cap, static snoring indicators at low LOD, on-demand dorm atlas, alpha-toggle flicker)
- [ ] Touch zone sizing considered (44px minimum — booking rows, roommate icons, queue slots, examine hotspots compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (patterned rest meter, shape-tagged risk frames, numbered hot stall, pip-count chaos levels)
- [ ] Social media viral potential maximized (Roommate Reveal card framing, cone composition, 3 AM thud mystery staging)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only; Cobblestone Market Street, Craic Tax proximity — no real-world city named |
| Cultural Specificity | ✅ | Dublin hostel scene / international party-hostel culture, satirized with specificity |
| Satirical Targets Appropriate | ✅ | Punches at hostel experience, budget-travel delusion, and the bros — never at poverty or staff |
| Seedy Underbelly Present | ✅ | False economy (cheap stay, expensive consequences) plus Craic Tax aftermath flow-through |
| Gameplay Value Established | ✅ | Rest system, roommate roulette, Embarrassed status, Shower Gauntlet, 4 quests, achievement track |
| Technical Feasibility | ✅ | 8 sheets, simple scene swaps, on-demand dorm atlas, CPU particles only |
| Mobile Performance Budget | ✅ | 60 FPS target (45 floor on min-spec dorm scene), 12 draw calls, 32 MB, 12-particle cap |
| Accessibility Features | ✅ | 14 visual audio cues, motion-sensitivity variants, pattern/shape-coded meters, 44px targets |
| No Crypto Elements | ✅ | PASS — nothing in this hostel appreciates in value, least of all the guests |
| Social Media Integration | ✅ | 7 screenshot moments, 10 profile-sourced quotes, Roommate Reveal built to be shared |

---

**The Bunk & Blunder delivers the full budget-travel comedy arc in sprite form: the cheerful signage that lies, the traffic cone nobody claims, the one hot shower everyone hunts, the walls that stop short of the ceiling, and Derek in 4B snoring through it all like a foghorn of self-discovery. Every asset serves the same joke told at different volumes — you didn't book a bed, you booked an audience. Colm hands over the key card, wishes you luck, and asks no questions, because after eight years he already knows the answer: you'll leave with less dignity, more story, and a booking for tomorrow night.**

**"You're the third person to ask about their dignity this morning. I haven't seen it."**
