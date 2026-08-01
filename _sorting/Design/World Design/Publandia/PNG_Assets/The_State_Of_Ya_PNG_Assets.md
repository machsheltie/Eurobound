# The State of Ya - Complete PNG Asset Requirements

## 📋 Overview
A corner general store where Maeve Brennan diagnoses your entire night with one glance, tells you exactly what she sees, and sells you exactly what you need to survive it — Irish brutal honesty running a supply chain for bad decisions. This document specifies every sprite for the judgement emporium at the heart of The Craic Tax: the aisles, the assessments, the twenty items of redemption and escalation, and the rarest sprite in Publandia — Maeve's genuine smile.

**Location ID:** `publandia_shop_state_of_ya_01`
**Theme:** Morning-after shame meets Irish mammy energy — judgement delivered with genuine care underneath
**Zone:** The Craic Tax (maximum exposure to poor decisions)
**Hours:** 07:00-23:00 (morning shame through evening setup)
**Primary Function:** Central item shop / hangover supplies / utility & "offensive" items / State Assessment system / Known Disaster progression

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Pharmacy White | #F5F5F5 | Shelving, healing aisle, harsh reality |
| Shame Green | #90EE90 | Signage accents, price tags |
| Dublin Gray | #808080 | Exterior, floor, overcast light |
| Judgement Purple | #8B008B | Assessment UI, Maeve's cardigan trim |
| Fluorescent Glare | #FFFFF0 | Overhead lighting that reveals all |
| Chalkboard Slate | #36454F | Shame Special board, hand lettering |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/state_of_ya/
├── environment/
│   ├── state_exterior.png
│   ├── shop_interior.png
│   └── aisle_details.png
├── npcs/
│   ├── maeve.png
│   └── state_customers.png
├── objects/
│   └── shop_stock.png
├── effects/
│   └── state_effects.png (packed into state_of_ya_ui.png)
└── ui/
    └── state_of_ya_ui.png
```

---

## 🏪 Sprite Sheet 1: Exterior Storefront
**File:** `state_exterior.png`
**Dimensions:** 384x256 pixels

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corner Shop Base | (0, 0) | 256x192 | Traditional Dublin storefront, large windows |
| Window Display | (0, 192) | 128x64 | Hangover cures front and center, seasonal shame supplies |
| Main Sign | (256, 0) | 128x48 | "THE STATE OF YA" in bold, judgmental lettering |
| Subtitle Board | (256, 48) | 128x32 | "We've Seen Worse. Probably." |
| Window Sign | (256, 80) | 128x32 | "HANGOVER SUPPLIES • QUESTIONABLE CHOICES • NO JUDGEMENT*" |
| Asterisk Plaque | (256, 112) | 64x24 | "*judgement included" — small, essential |
| Door Sign | (320, 112) | 64x24 | "Come In, We Already Know" |
| Door Open | (256, 136) | 64x96 | Bell-rigged, herald of another disaster |
| Door Closed | (320, 136) | 64x96 | Same, closed state |
| Chalkboard Special | (128, 192) | 96x64 | "Today's Shame Special: 2-for-1 Aspirin & Dignity" |
| Craic Tax Pavement | (224, 232) | 160x24 | Street tile strip, last night's confetti in the gutter |

### Technical Notes:
- Chalkboard text plate is a separate layer — the Shame Special is designed to rotate in future content passes
- The asterisk plaque must be legible on examine; the whole shop is in that footnote

---

## 🏬 Sprite Sheet 2: Shop Interior — The Judgement Emporium
**File:** `shop_interior.png`
**Dimensions:** 512x384 pixels

### Room Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Linoleum | (0, 0) | 256x128 | Dublin Gray, mopped nightly, scuffed daily |
| Back Wall & Shelving | (0, 128) | 256x128 | Pharmacy White shelf runs |
| Entry Zone (The Assessment) | (256, 0) | 128x96 | Doormat sightline — where one glance tells Maeve everything |
| Fluorescent Fixture Row | (384, 0) | 128x32 | Harsh tubes, reveals all |
| Fluorescent (Healing Soft) | (384, 32) | 128x32 | Slightly softer variant over the Healing Aisle (mercy) |
| Maeve's Counter | (0, 256) | 192x96 | Her domain — register, reading glasses on chain, unavoidable truth |
| Behind-Counter Shelf | (192, 256) | 128x64 | The good stuff, Known Disasters only |
| Register & Bell | (320, 256) | 64x64 | Beeping register, counter bell |
| Window Light Beam | (384, 64) | 128x96 | Gray morning light on the shame brigade |
| Aisle Base Unit | (256, 96) | 128x128 | Generic gondola shelf — tiled four times for the four aisles |
| Aisle End Caps | (384, 160) | 128x96 | Two 64x96 end displays: energy drinks, wet wipes tower |
| Basket Stack | (192, 320) | 64x64 | Wire baskets — optimists take one, realists take two |
| Newspaper Rack | (256, 224) | 64x32 | "PUBLANDIA HERALD: CRAIC TAX CLAIMS MORE VICTIMS" |
| Group Discount Sign | (320, 320) | 96x32 | "GROUP DISCOUNT — Because I've a Heart" |
| Recommendation Glow Shelf | (416, 320) | 96x64 | Subtle highlight variant of shelf section — Maeve's pick |

### Technical Notes:
- Aisle Base Unit tiles into all four aisles; aisle identity comes from Sheet 3 detail overlays
- Recommendation Glow Shelf swaps in over whichever aisle Maeve's assessment points to

---

## 🧴 Sprite Sheet 3: Aisle Details
**File:** `aisle_details.png`
**Dimensions:** 512x256 pixels

### The Four Aisles (128x128 overlays):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Healing Aisle (The Redemption) | (0, 0) | 128x128 | Hangover cures, pain relief, stomach settlers, hydration — softest light in the shop |
| Support Aisle (The Enablement) | (128, 0) | 128x128 | Energy drinks, dubious luck charms, more dubious courage supplements |
| Offensive Aisle (The Escalation) | (256, 0) | 128x128 | Stink bombs, noise makers, "defensive" items — raised-eyebrow stock |
| Utility Aisle (The Practicality) | (384, 0) | 128x128 | Emergency solutions, last resorts, "just in case" supplies |

### Aisle Signage & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Aisle Number Signs 1-4 | (0, 128) | 128x32 | Four 32x32 hanging signs — "Aspirin's aisle 1" must be literal |
| Shelf Price Tags | (128, 128) | 64x32 | Shame Green tag strip |
| Raised Eyebrow Notice | (192, 128) | 64x32 | Offensive aisle: "SOLD AS-IS. I'M NOT ASKING." |
| Behind-Counter Detail | (256, 128) | 128x64 | Maeve's Personal Remedy jar, "Didn't Happen" Kit box, Reset case |
| Grandmother's Recipe Frame | (384, 128) | 64x64 | Handwritten, framed, ingredients illegible on purpose |
| Ice Chest | (0, 160) | 96x64 | Cold drinks, forehead-adjacent uses |
| Mop & Warning Cone | (96, 160) | 64x96 | "CAUTION: REGRET" floor cone |
| Stock Boxes | (160, 160) | 96x64 | Backroom overflow — supply chain management |
| Reading Glasses & Chain | (256, 192) | 32x32 | Counter prop, examine point |
| Photo of the Regulars | (288, 192) | 64x48 | Taped to register — "my favorite recurring tragedies" |
| Sigh Cloud Prop | (352, 192) | 32x32 | Maeve's frequent sigh, visualized |

---

## 👓 Sprite Sheet 4: Maeve Brennan
**File:** `maeve.png`
**Dimensions:** 384x256 pixels

### Maeve States (64x96 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Neutral Assessment | (0, 0) | 64x96 | Behind counter, glasses lowered, reading you |
| The Glance Up | (64, 0) | 64x96 | Door bell rings, one look, full diagnosis |
| Unimpressed | (128, 0) | 64x96 | Standard reaction — arms folded, verdict loading |
| Recommending | (192, 0) | 64x96 | Pointing at the exact aisle: "Aisle 3. Go." |
| Concerned | (256, 0) | 64x96 | You've genuinely worried her — rarer than anger |
| Eye Roll | (320, 0) | 64x96 | Mid-roll frame for Denial Cases |
| Rare Kindness | (0, 96) | 64x96 | "Here. On the house." — softened posture |
| Rare Smile | (64, 96) | 64x96 | The achievement sprite — genuine laugh, +25 Bravado |

### Maeve Expressions (48x48 each):
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Perpetually Unsurprised | (128, 96) | 48x48 | Default — 18 years of everything |
| "Sweet Suffering Jaysus" | (176, 96) | 48x48 | Hungover + dehydrated combo detected |
| Suspicious | (224, 96) | 48x48 | "You're looking well. What are you planning?" |
| Reluctant Fondness | (272, 96) | 48x48 | Known Disaster greeting |
| Genuine Warmth | (320, 96) | 48x48 | "You did good. I don't say that often." |

### Dialogue Portraits (64x48 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Assessment | (0, 192) | 64x48 | Glasses down, seeing everything |
| Portrait Deadpan | (64, 192) | 64x48 | The delivery that carries the shop |
| Portrait Concerned | (128, 192) | 64x48 | Care leaking through |
| Portrait Smile | (192, 192) | 64x48 | Miracle Worker unlock |
| Counter Hands | (256, 144) | 64x32 | Bagging, tallying, no wasted motion |
| Glasses Glint | (256, 192) | 32x32 | Assessment "hmm" accent frame |

---

## 👥 Sprite Sheet 5: Customer NPCs
**File:** `state_customers.png`
**Dimensions:** 384x192 pixels

### The Clientele:
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| Morning Shame Brigade | (0, 0) | 192x96 | Three tourists in matching "PUBLANDIA" shirts, destroyed, bulk-buying aspirin |
| The Evening Prep | (192, 0) | 64x96 | Optimistic, stocking up, no idea what's coming |
| The Denial Case | (256, 0) | 64x96 | Sunglasses indoors, aggressive normalcy, shaking hands |
| The Local Regular | (320, 0) | 64x96 | Made peace with Maeve's ways — 15-second transaction |

### Customer Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Matching Shirts Detail | (0, 96) | 64x48 | "PUBLANDIA" tourist merch close-up |
| Shame Basket (Full) | (64, 96) | 48x48 | Aspirin, all of it |
| Prep Basket (Optimistic) | (112, 96) | 48x48 | Energy drinks, doomed confidence |
| Denial Sunglasses | (160, 96) | 32x24 | Indoor-inappropriate |
| Shaking Hands Overlay | (192, 96) | 32x32 | Two-frame tremor for the Denial Case |
| Customer Portraits Strip | (224, 96) | 160x48 | Brigade / Prep / Denial / Regular, 40x48 each |
| Whisper Huddle Overlay | (0, 144) | 64x48 | Brigade avoiding eye contact |

---

## 🛒 Sprite Sheet 6: Shop Stock
**File:** `shop_stock.png`
**Dimensions:** 256x192 pixels

### Healing Items (24x24 grid, y=0):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Aspirin Packet | (0, 0) | 24x24 | "Two with water. Not with more drink." |
| Paracetamol | (24, 0) | 24x24 | Don't mix. She KNOWS you will |
| Greasy Breakfast Roll | (48, 0) | 32x24 | Grease salvation, wrapped |
| Hair of the Dog Pint (Canned) | (80, 0) | 24x32 | A postponement, not a cure |
| Electrolyte Powder | (104, 0) | 24x24 | Should've had this BEFORE bed |
| Stomach Settler | (128, 0) | 24x24 | Ginger-based, actual medicine |
| Industrial Antacid | (152, 0) | 24x24 | "What did you EAT?" |
| Full Recovery Kit | (176, 0) | 32x32 | Everything you shouldn't have needed |

### Support Items (y=32):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Energy Drink (Brand) | (0, 32) | 24x32 | Legitimate caffeine |
| Discount Energy Drink | (24, 32) | 24x32 | Cheaper, worse, your choice — jitters risk |
| Lucky Rabbit's Foot | (48, 32) | 24x24 | Wasn't lucky for the rabbit |
| Plastic Four-Leaf Clover | (72, 32) | 24x24 | Fake. Luck's about belief anyway |
| "Confidence" Mints | (96, 32) | 24x24 | They're just mints |
| Eye Drops | (120, 32) | 24x24 | Look less guilty |

### Offensive Items (y=64):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Stink Bomb | (0, 64) | 24x24 | Area denial. She's not asking why |
| Noise Maker | (24, 64) | 24x24 | Attention: attracting or escaping |
| Brass Knuckles | (48, 64) | 32x24 | "...self-defense purposes, I assume." |
| "Liquid Courage" Flask | (80, 64) | 24x32 | Pre-filled. For emergencies |
| Pocket Sand | (104, 64) | 24x24 | She just stocks shelves |
| Air Horn | (128, 64) | 24x32 | ACTUAL emergencies. She'll know |

### Utility Items (y=96):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Grease-Proof Napkins | (0, 96) | 24x24 | For the inevitable. Not if. When |
| Fake ID | (24, 96) | 32x24 | This transaction isn't happening |
| Emergency Taxi Voucher | (56, 96) | 32x24 | Instant escape, one use |
| Phone Charger (Works) | (88, 96) | 24x24 | Unlike Murphy's, this one ACTUALLY works |
| Wet Wipes (Pack) | (112, 96) | 24x24 | For "everything" |
| Indoor Sunglasses | (136, 96) | 32x24 | Pretend you're fine |
| Industrial Breath Mints | (168, 96) | 24x24 | Stranger-grade only |
| Emergency Sewing Kit | (192, 96) | 24x24 | Button, seam, dignity — covers two |

### Behind Counter (Known Disaster Only, y=128):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Maeve's Personal Remedy | (0, 128) | 32x32 | Grandmother's recipe, cures ANY status |
| The "Didn't Happen" Kit | (32, 128) | 32x32 | Plausible deniability supplies |
| Emergency Complete Reset | (64, 128) | 32x32 | For when you've REALLY done it |
| Shelf Facing Strips | (96, 128) | 96x32 | Tiled product-row filler for aisle shelves |
| Plastic Bag (Rustling) | (192, 128) | 32x32 | Transaction complete prop |
| Item Category Glyphs | (0, 160) | 128x32 | Cross / bolt / fist / wrench — four 32x32 aisle icons |

### Technical Notes:
- Aisle assignment is icon-coded (cross/bolt/fist/wrench) matching aisle number signs — never color alone
- Fake ID and "Didn't Happen" Kit sprites appear in inventory with a "no comment" overlay stamp

---

## 🎮 Sprite Sheet 7: UI & Effects
**File:** `state_of_ya_ui.png`
**Dimensions:** 256x256 pixels

### Shop UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shop Menu Frame | (0, 0) | 160x192 | Full inventory interface, aisle-tabbed, receipt styling |
| Assessment Popup | (160, 0) | 96x64 | Maeve's verdict banner: state name + comment line |
| State Meter | (160, 64) | 96x32 | How you look to Maeve — six recognized states |
| Recommendation Highlight | (160, 96) | 96x48 | Shelf glow frame + "SHE'S ALWAYS RIGHT" pointer |
| Known Disaster Badge | (160, 144) | 48x48 | Reluctant fondness, earned in five visits |
| "Your Usual?" Button | (208, 144) | 48x48 | Known Disaster quick-buy |
| Behind Counter Panel | (0, 192) | 128x64 | Special access UI, three-slot display |
| Survivor's Discount Tag | (128, 192) | 64x32 | 10% off, no ceremony |
| Group Discount Popup | (128, 224) | 64x32 | Morning Shame Brigade rate |

### Effects & Status Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Bell Ring Burst | (192, 192) | 32x32 | The herald of another disaster |
| Fluorescent Hum Lines | (224, 192) | 32x32 | Ambient buzz cue |
| "Assessed" Status Icon | (192, 224) | 32x32 | She has seen you |
| "Well-Supplied" Icon | (224, 224) | 32x32 | Left with appropriate items |
| Register Beep Flash | (160, 224) | 32x32 | Per-item scan blip |

### Technical Notes:
- Assessment Popup pulls state text from the six-state table (`hungover / pre-night / mid-crisis / post-rejection / suspiciously fine / returning disaster`)
- No ambient music per profile — visual effects carry the atmosphere, so hum lines and bell burst must land

---

## 🎬 Animation Specifications

### The Glance Up:
- **Duration:** 2 seconds
- **Frames:** Neutral → Glance Up (0.5s hold) → verdict expression → Assessment Popup
- **Trigger:** Player crosses the entry threshold (door bell)
- **Purpose:** The location's signature beat — diagnosed before you speak
- **Audio Sync:** Door bell on entry; the "look at the state of ya" sting lands with the popup
- **Mobile Optimization:** None needed

### The Recommendation Point:
- **Duration:** 1.5 seconds
- **Frames:** Recommending state → aisle sign flash → Recommendation Glow Shelf swap
- **Trigger:** Assessment completes, or "I don't know what I need" dialogue option
- **Purpose:** "You need [EXACT ITEM]. Aisle [NUMBER]. Go." — she's always right
- **Audio Sync:** Recommendation ping on the glow swap
- **Mobile Optimization:** Glow becomes static outline on Low LOD

### The Eye Roll:
- **Duration:** 1 second
- **Frames:** 3 (start → apex → return to Unimpressed)
- **Trigger:** Denial Case dialogue, obvious lies, Chadwick filming
- **Purpose:** Judgement as microexpression — the roll is subtle, the meaning is not
- **Audio Sync:** Maeve's sigh, frequent
- **Mobile Optimization:** None needed

### The Rare Smile:
- **Duration:** 2.5 seconds
- **Frames:** Reluctant Fondness → genuine break → Rare Smile hold → recompose
- **Trigger:** "The Rare Laugh" quest success / Maeve Approved moments
- **Purpose:** Rarest sprite in the shop; +25 Bravado made visible
- **Audio Sync:** Slight audio warmth shift — ambient softens for the hold
- **Mobile Optimization:** None needed — it's the achievement

### Fluorescent Reveal:
- **Duration:** Continuous; hum with 0.5s soft pulse every 8s
- **Frames:** 2 alpha states, Healing Aisle uses the softer fixture
- **Trigger:** Constant in interior
- **Purpose:** Harsh light that reveals all, mercy over the Redemption aisle
- **Audio Sync:** Fluorescent hum, register beeps intermittent
- **Mobile Optimization:** Static fixture in reduced-motion mode and Low LOD

### 15-Second Regular Transaction:
- **Duration:** 15 seconds, choreographed
- **Frames:** Regular enters → nod exchange → Counter Hands bagging → bag rustle → exit
- **Trigger:** Ambient event, roughly every third visit
- **Purpose:** Mutual respect as environmental storytelling — the adjusted customer
- **Audio Sync:** "Morning, Maeve." / "You look rough." / "I know." beat-matched to frames
- **Mobile Optimization:** Trimmed to 8s on Low LOD

---

## ♿ Accessibility Sprite Requirements
**File:** `state_accessibility.png` (supplemental sheet — delivered alongside the 7 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shop Menu, Bold | (0, 0) | 96x64 | Thick-bordered inventory with enlarged aisle tabs + icons |
| Assessment Popup, Bold | (96, 0) | 96x48 | Heavy-outline verdict banner, state name enlarged |
| Maeve Interaction Outline | (192, 0) | 48x64 | White-on-dark counter hotspot |
| Aisle Sign Outlines | (0, 64) | 128x32 | Four high-contrast hanging signs with number + icon |
| Behind Counter Outline | (128, 64) | 64x64 | Unlocked-access highlight, Known Disaster gate state shown |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fluorescent, Steady | (192, 64) | 64x32 | Pulse-free fixture state |
| Recommendation, Static | (0, 96) | 96x48 | Fixed outline replacing shelf glow swap |
| Tremor, Off | (96, 96) | 32x32 | Denial Case without shaking-hands overlay |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bell Burst Icon | (128, 96) | 32x32 | Entry bell (mirrors UI sheet, enlarged) |
| Assessment Sting Glyph | (160, 96) | 32x32 | "The state of ya" sting visualization |
| Sigh Wisp | (192, 96) | 32x32 | Maeve's frequent sigh cue |
| Register Beep Blip | (0, 144) | 32x32 | Per-item scan feedback |
| Bag Rustle Lines | (32, 144) | 32x32 | Transaction-complete cue |
| Recommendation Ping Ring | (64, 144) | 32x32 | Glow-swap sound made visible |
| Warmth Shift Frame | (96, 144) | 48x32 | Soft border tint during rare-kindness audio softening |

### Colorblind Considerations:
- Aisles coded by number + icon (cross/bolt/fist/wrench), never Shame Green alone
- State Meter uses six labeled segments, not a color gradient
- Recommendation highlight pairs glow with a pointer arrow; all menu rows, aisle hotspots, and the counter meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (signage and chalkboard text at ASTC 4x4 — the jokes are in the lettering)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for Maeve portraits and the Assessment Popup

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| stateofya_environment | exterior, interior, aisle_details | 1024x1024 |
| stateofya_characters | maeve, state_customers | 512x512 |
| stateofya_items_ui | shop_stock, ui | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | All 4 customer NPC types cycling, fluorescent pulse, full transaction choreography |
| Medium | 2 customers max, static fixtures, trimmed transactions |
| Low | Maeve + 1 customer, no pulse, no ambient events |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 30 MB maximum
- **Particle Limit:** 6 (this shop barely needs effects — reality doesn't need accompaniment)

### Performance Notes:
- Aisle Base Unit is one texture tiled four times; aisle identity is a single overlay each
- Ambient customer events are scheduled, never simultaneous — one NPC scene at a time

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Single-room interior; exterior/interior via simple fade
- Assessment system reads player status effects on entry (Hungover, Dehydrated, Low Bravado, Post-Combat, time-of-day) → selects one of six states → drives Maeve state, popup, and Recommendation Glow shelf target
- CPUParticles2D not required — fluorescent pulse and glow swaps are alpha/material toggles, disabled in reduced-motion mode
- Area2D examine points: asterisk plaque, chalkboard, Grandmother's Recipe Frame, Photo of the Regulars, newspaper rack
- State tracking per `state_of_ya_state` (visits_count, known_disaster, usual_items[], fake_id_bought, made_maeve_laugh, full_circle_pending)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Door open | Shop bell | On door-open frame — announces your arrival |
| Assessment Popup | "Look at the state of ya" sting | With popup slide-in |
| Eye Roll | Maeve's sigh | On apex frame |
| Recommendation Glow swap | Recommendation ping | On swap |
| Register scans | Beep per item | Per Register Beep Flash |
| Transaction complete | Plastic bag rustle | On bag handoff |
| Rare Kindness / Rare Smile | Ambient softening | Fades in over the hold, out on recompose |
| Fake ID purchase | Nothing. Silence. | The transaction isn't happening |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Maeve's Approval | Genuine Warmth expression, "Maeve Approved" state | Impress her genuinely — very rare trigger conditions |
| The Usual | Known Disaster Badge, "Your Usual?" button, Behind Counter Panel | Fifth visit unlocks the shortcut and the good stuff |
| Full Circle | Prep Basket + Shame Basket, Evening Prep + Brigade NPCs | Buy evening prep, return next morning for recovery — same items, no surprise from Maeve |
| The Rare Laugh | Rare Smile animation, Portrait Smile | Make her genuinely laugh; +25 Bravado, Miracle Worker achievement |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bunk & Blunder | Morning route — wake there, shuffle here; Brigade NPCs share the path | Standard street transition, morning light variant |
| The Craic Tax | Host zone; pavement confetti tile, newspaper headline | Same street network |
| Murphy's Lawless | Phone Charger (Works) is a direct competitive jab — "I have standards" | Dialogue-only rivalry |
| All Pubs | Source of every condition Maeve treats; evening prep flows outward | Item buffs and cures carry via status system |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A pharmacy-bright confessional — the one room in Publandia where the lighting refuses to lie"
- **Color Mood:** Pharmacy White and Fluorescent Glare stripping away pretense; Judgement Purple reserved for Maeve and her verdicts; Shame Green pricing the damage
- **Lighting:** Harsh fluorescent everywhere except the Healing Aisle's half-step of mercy
- **Texture:** Mopped linoleum, wire baskets, laminated signage, one handwritten recipe in a frame

### Environmental Storytelling:
- "NO JUDGEMENT*" with "*judgement included" underneath — the shop's contract with the customer
- The chalkboard Shame Special rotates; the shame does not
- Behind-counter shelf visible but ungated only to Known Disasters — trust as store layout
- The Photo of the Regulars taped to the register: 18 years of reluctant fondness in one prop

### Character Integration Notes:
- Maeve's deadpan does the comedy; her sprites must never mug — the eye roll is three frames, not a cartoon
- Rare Smile is deliberately the best-drawn sprite on her sheet; players earn it
- Customer NPCs are the shop's clock: Brigade at morning, Prep at evening, Denial at all hours

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Assessment Popup** - "Sweet suffering Jaysus. The STATE of ya." over your visibly wrecked character
2. **The Asterisk** - "NO JUDGEMENT*" / "*judgement included" in one frame
3. **The Shame Special Chalkboard** - "2-for-1 Aspirin & Dignity"
4. **The Morning Shame Brigade** - Three matching "PUBLANDIA" shirts whisper-buying all the aspirin
5. **The Rare Smile** - Screenshot proof you made Maeve Brennan laugh
6. **The Fake ID Transaction** - "I don't see this. This isn't happening. €25."

### Quote Potential:
- "Jaysus, Mary, and Joseph. The state of ya. What happened last night?"
- "You look like something the cat dragged in, played with, and rejected."
- "You're GREEN. You're SWAYING. You're about as fine as my ex-husband's excuses. €15."
- "People think I'm harsh. I'm not harsh. I'm ACCURATE. Harsh would be lying."
- "The aesthetic is a woman who'll break your phone. How's THAT for content?"
- "Discount for the only one with sense. €28."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | state_exterior.png | 384x256 |
| 2 | shop_interior.png | 512x384 |
| 3 | aisle_details.png | 512x256 |
| 4 | maeve.png | 384x256 |
| 5 | state_customers.png | 384x192 |
| 6 | shop_stock.png | 256x192 |
| 7 | state_of_ya_ui.png | 256x256 |

**Total Estimated Memory:** ~14 MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `state_exterior.png` (384x256)
- [ ] `shop_interior.png` (512x384)
- [ ] `aisle_details.png` (512x256)
- [ ] `maeve.png` (384x256)
- [ ] `state_customers.png` (384x192)
- [ ] `shop_stock.png` (256x192)
- [ ] `state_of_ya_ui.png` (256x256)
- [ ] `state_accessibility.png` (256x192, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (chalkboard text and shelf stock rows on separate layers — the Shame Special and inventory are designed to rotate)
- **Documentation:** Animation timing reference sheet (2s glance, 1s eye roll, 2.5s rare smile, 15s regular transaction)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Pharmacy White #F5F5F5, Shame Green #90EE90, Dublin Gray #808080, Judgement Purple #8B008B)
- [ ] "*judgement included" asterisk plaque legible on examine
- [ ] Aisle number signs match dialogue references exactly ("Aspirin's aisle 1" must be true)
- [ ] Rare Smile reads as genuinely warm — the payoff sprite gets the polish budget
- [ ] Accessibility visual alternatives included for all audio cues (bell, sting, sigh, beep, rustle, ping)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (brutal honesty wrapped in genuine care) is clear throughout all assets
- [ ] Easter eggs discoverable: Grandmother's Recipe Frame, Photo of the Regulars, newspaper headline, the silent Fake ID sale
- [ ] Mobile performance optimized (tiled aisle unit, scheduled ambient events, 6-particle cap)
- [ ] Touch zone sizing considered (44px minimum — menu rows, aisle hotspots, counter compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (numbered + icon-coded aisles, labeled state meter)
- [ ] Social media viral potential maximized (assessment popup framing, asterisk composition)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia and The Craic Tax only; "Dublin Gray" is a palette name, not a place reference in-game |
| Cultural Specificity | ✅ | "The state of ya" as Irish concern-disguised-as-criticism; Irish mammy energy |
| Satirical Targets Appropriate | ✅ | Tourist self-delusion and morning-after shame — tough love, never mockery of locals |
| Seedy Underbelly Present | ✅ | Enabling the cycle for profit; Fake ID and "Didn't Happen" Kit under the counter |
| Gameplay Value Established | ✅ | Central item shop, 25+ items, assessment system, Known Disaster progression |
| Technical Feasibility | ✅ | Single room, toggle-based effects, 7 sheets, mobile optimization documented |
| Mobile Performance Budget | ✅ | 60 FPS, 12 draw calls, 30MB |
| Accessibility Features | ✅ | Visual cues for all audio, steady-light and static-highlight variants, labeled states |
| No Crypto Elements | ✅ | Absent from source and spec |
| Social Media Integration | ✅ | Six viral moments identified, quote bank sourced from profile |

**The State of Ya delivers the most honest room in Publandia: fluorescent light, a woman who is never wrong, and shelves stocked for exactly what you're about to do to yourself. Every asset serves the same loop — assessed, exposed, understood, supplied — and the rarest reward in the shop isn't behind the counter. It's the smile.**

**"Look at Yourself. Now Buy Something for It."**
