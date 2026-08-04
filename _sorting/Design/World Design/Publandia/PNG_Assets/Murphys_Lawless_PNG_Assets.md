# Murphy's Lawless - Complete PNG Asset Requirements

## 📋 Overview
Murphy's Lawless is the corner shop where Murphy's Law is both the name and the business model — a Dublin-style late-night side-street off-license where everything that can go wrong will, and Murphy will ring it up on a 1987 register while insisting the card machine is broken. This document specifies every PNG asset required to render the shop, Rory Murphy, his nocturnal clientele, the full cursed inventory, and the side-effect economy that turns 3 AM desperation into gameplay.

**Location ID:** `publandia_seedy_murphys_lawless_01`
**Theme:** Late-night desperation purchasing — "If It Can Go Wrong, We Sell It"
**Zone:** Side street off The Craic Tax (Seedy Underbelly), Publandia
**Hours:** 10 AM - 5 AM (closes for exactly 5 hours, no one knows why)
**Primary Function:** Shop / side-effect generator / "Frequent Sufferer" progression hub / back-room unlockable + quest hooks ("Murphy's Miracle", "The Back Room", "Quality Control", "The Card Machine")

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Flickering Neon | #FF6B6B | Main sign, window glow, night exterior |
| Refrigerator White | #F0FFFF | Fridge interiors, fluorescent spill, cold light |
| Grime Brown | #5D4037 | Floors, shelving, decades of wall residue |
| Suspicious Yellow | #FFD93D | Price tags, warning labels, MurphyBoost branding |
| Mist Gray | #9FA8B2 | Rain and street mist outside the barred windows |
| Register Brass | #B08D57 | 1987 cash register, door hardware, bell |
| EXTREME Red | #D32F2F | MurphyBoost EXTREME, Cardiac Concern icon, risk highlights |
| Back Room Green | #2E7D32 | Back room quality-stock glow, no-side-effect seals |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/murphys_lawless/
├── environment/
│   ├── murphys_exterior.png
│   └── murphys_interior.png
├── npcs/
│   ├── murphy_seamus.png
│   └── murphys_customers.png
├── objects/
│   ├── murphys_products_drinks.png
│   └── murphys_products_sundry.png
├── effects/
│   └── murphys_effects.png
└── ui/
    ├── murphys_ui.png
    └── murphys_accessibility.png
```

---

## 🏪 Sprite Sheet 1: Exterior — The Glow of Poor Decisions
**File:** `murphys_exterior.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Flickering Neon #FF6B6B against Mist Gray #9FA8B2 — neon vs. mist is the whole exterior mood

### Storefront Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Storefront Facade | (0, 0) | 256x256 | Narrow shopfront wedged between legitimate businesses; hand-painted name, apostrophe questionable |
| Neighbor Building Left | (256, 0) | 64x256 | Respectable, dark, closed — everything Murphy's isn't |
| Neighbor Building Right | (320, 0) | 64x256 | Also closed. Everything is closed. That's the point |
| Wet Cobblestone Ground | (384, 0) | 128x64 | Rain-slick side-street tile, neon reflections |
| Mist Overlay Strip | (384, 64) | 128x64 | Drifting Publandia night mist, semi-transparent |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon Sign Full Lit | (384, 128) | 128x32 | "MURPHY'S LAWLESS" all tubes on (rare) |
| Neon Sign Half-Dead | (384, 160) | 128x32 | "MURPH'S LAWLE" — the working-letters state |
| Neon Sign Off Frame | (384, 192) | 128x32 | Dark tubes for flicker cycle |
| Questionable Apostrophe | (384, 224) | 32x32 | Close-up: the apostrophe hangs at a legally ambiguous angle |
| OPEN Sign Always On | (416, 224) | 32x32 | Burns eternal — it has never been off |
| "OFF-LICENSE & SUNDRIES" | (448, 224) | 64x32 | Subtitle sign; sundries undefined |

### Windows & Door:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Barred Window Left | (0, 256) | 96x96 | Security bars, rain-streaked glass, neon glow bleeding through the mist |
| Barred Window Right | (96, 256) | 96x96 | "COLD BEER • HOT DEALS • QUESTIONABLE DECISIONS" decal visible |
| Door Closed | (192, 256) | 64x96 | Creaky door, brass bell above |
| Door Stuck (Mid-Push) | (256, 256) | 64x96 | Flexing under force, refusing — the comedy frame |
| Door Open | (320, 256) | 64x96 | Finally. Bell mid-swing |
| "PUSH HARDER" Sign | (384, 256) | 64x32 | "IF THE DOOR STICKS, PUSH HARDER" (door always sticks) |
| "Card machine broken (always)" | (384, 288) | 64x32 | Handwritten, taped crooked, suspiciously permanent |
| Window Slogan Decal | (448, 256) | 64x64 | Standalone slogan overlay for interior-side rendering |
| Hours Sign | (448, 320) | 64x32 | "10 AM - 5 AM. THE FIVE HOURS ARE PRIVATE." |

### Street Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rain Puddles | (0, 352) | 128x32 | Reflective puddles catching neon red |
| Side Street Cobble Tile | (128, 352) | 128x32 | Tileable wet cobblestone |
| Litter Details | (256, 352) | 128x32 | Empty MurphyBoost cans, chip papers — prior customers' testimony |
| Distant Craic Tax Glow | (384, 352) | 128x32 | Warm bar-light glow up the street, where the customers come from |

### Technical Notes:
- Neon flicker cycles between the three sign frames via alpha/frame swap — never all-on for more than 4 seconds
- Mist Overlay scrolls at 4 px/sec using a single repeating strip; disabled at Low LOD
- Rain outside the barred window rendered as CPUParticles2D capped at 20 drops

---

## 🛒 Sprite Sheet 2: Interior — The Chaos Emporium
**File:** `murphys_interior.png`
**Dimensions:** 512x512 pixels

### Room Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Tile | (0, 0) | 128x128 | Sticky linoleum, tileable, decades of spill history |
| Back Wall | (128, 0) | 128x128 | Grime Brown, shelf shadows, one suspicious stain |
| Ceiling + Fixture Mounts | (256, 0) | 128x64 | Tile with fluorescent mounting points |
| Fluorescent Tube Steady | (256, 64) | 128x32 | The one that works |
| Fluorescent Tube Dying | (256, 96) | 128x32 | The one that flickers (see Animation Specs) |
| Reinforced-Glass Counter | (384, 0) | 128x128 | Murphy's domain — scratched perspex, cash slot, he's learned |

### Aisles & Cold Section:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Aisle Shelf Left | (0, 128) | 128x192 | Narrow, cramped, stocked by Murphy's incomprehensible logic |
| Aisle Shelf Right | (128, 128) | 128x192 | Best/worst items hidden in unlikely places |
| Cold Section Fridge Bank | (256, 128) | 128x192 | Two fridges of varying temperature reliability |
| Fridge Door Open | (384, 128) | 64x128 | Swung wide, interior light spilling |
| Back-of-Fridge Darkness | (448, 128) | 64x64 | Where mysteries live — depth the light doesn't reach |
| Fridge Condensation Glass | (448, 192) | 64x64 | Fogged door overlay with drip trails |
| Mystery Back-of-Fridge Silhouette | (384, 256) | 64x64 | Unidentifiable shape. Examine at your own risk |
| Fridge Interior Light Glow | (448, 256) | 64x64 | Refrigerator White radial glow |

### The Counter (Murphy's Domain):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cash Register 1987 | (0, 320) | 64x64 | Brass-toned relic; still works, somehow |
| Register Drawer Open | (64, 320) | 64x64 | Cash only, remember |
| Card Machine (Dusty, Functional) | (128, 320) | 64x64 | Not broken. Never was. Quest evidence |
| "No Refunds" Laminated Sign | (192, 320) | 64x32 | Prominent, laminated, serious |
| "STAFF ONLY" Door Sign | (192, 352) | 64x32 | The rumor made bolted-on metal |
| Counter Cigarette Wall | (256, 320) | 128x64 | Cigarettes, lighters, the "special" items (ask, or don't) |
| Phone Charger Display | (384, 320) | 64x64 | Chargers that might work, carousel of fraying hope |
| Lighter Display | (448, 320) | 64x64 | Impulse rack at the cash slot |

### The Back Room (Unlockable):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Room Door Closed | (0, 384) | 64x96 | "STAFF ONLY" — nobody's been back there and returned the same |
| Back Room Door Ajar | (64, 384) | 64x96 | Post-unlock state, green glow leaking |
| Back Room Interior | (128, 384) | 256x128 | The revelation: clean shelves, actual quality, reasonable prices |
| Back Room Quality Shelf | (384, 384) | 128x64 | Name-brand stock, no-side-effect items, rare consumables |
| Back Room Glow | (384, 448) | 128x64 | Back Room Green ambience — trust rendered as light |
| Sticky Floor Patch | (0, 480) | 64x32 | Decal for high-traffic zones |
| Dust Strip | (64, 480) | 64x32 | Shelf-edge dust overlay for the '08 wine corner |

### Technical Notes:
- Aisle shelves are deliberately placed to force a winding path — collision follows the sprite, not a grid
- Back Room Interior loads only on unlock (`back_room_unlocked` state) — never resident before then
- Fridge glow and condensation are separate layers so the death-rattle shudder can move the fridge without moving the light

---

## 👴 Sprite Sheet 3: Rory Murphy — The Nocturnal Observer
**File:** `murphy_seamus.png`
**Dimensions:** 384x384 pixels

### Murphy States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Counter Idle (Watching) | (0, 0) | 96x128 | Behind reinforced glass, watching, waiting. Always watching |
| Greeting Nod | (96, 0) | 96x128 | "Evening. Or morning. Whatever this is." |
| Subtle Warning Lean | (192, 0) | 96x128 | Sober-player-only pose — slight forward tilt, eyebrow at work |
| Ringing Up | (288, 0) | 96x128 | Working the 1987 register by muscle memory |
| Knowing Hmm | (0, 128) | 96x128 | Head tilt at your basket. He says nothing. The "hmm" says everything |
| Frequent Sufferer Warmth | (96, 128) | 96x128 | Concerning warmth — the smile of a man who's watched you suffer five times |
| Restocking | (192, 128) | 96x128 | Placing items by incomprehensible logic |
| Neither Confirms Nor Denies | (288, 128) | 96x128 | The back-room shrug, palms half-raised |

### Murphy Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Apron That's Seen Things | (0, 256) | 64x64 | Stain archaeology, 23 years deep |
| Face Close-Up | (64, 256) | 64x64 | 60s, permanent stubble, amused-by-humanity eyes |
| Hands on Counter | (128, 256) | 64x32 | Folded, patient, waiting for your decision |
| Hands at Register | (128, 288) | 64x32 | Mid-keystroke on brass keys |

### Murphy Expressions:
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Acceptance | (192, 256) | 48x48 | Default — provides without judgment |
| Amusement | (240, 256) | 48x48 | "Bold. I respect bold." |
| Quiet Concern | (288, 256) | 48x48 | Reserved for EXTREME purchases |
| Concerning Warmth | (336, 256) | 48x48 | Frequent Sufferer recognition |
| Judgment-Free Stare | (320, 320) | 48x48 | Business is business |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Default | (0, 320) | 64x48 | Standard dialogue box |
| Portrait Warning | (64, 320) | 64x48 | "Keep water nearby. Trust me." |
| Portrait Amused | (128, 320) | 64x48 | Purchase-observation lines |
| Portrait Warmth | (192, 320) | 64x48 | "Welcome to the club. There's no card. There should be." |
| Portrait Hmm | (256, 320) | 64x48 | Paired with the knowing "hmm" audio sting |

### Technical Notes:
- Subtle Warning Lean plays ONLY when `player_sober == true` — drunk players get Counter Idle. The pose difference IS the warning system
- Frequent Sufferer Warmth replaces Greeting Nod permanently once the status is earned
- Restraint is the direction: Murphy never emotes above a 3/10. The shop does the screaming

---

## 👥 Sprite Sheet 4: The 3 AM Clientele
**File:** `murphys_customers.png`
**Dimensions:** 256x256 pixels

### Customer NPCs:
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| The 3 AM Regular | (0, 0) | 64x96 | Beeline stride, sealed items only, zero browsing |
| The Desperate Tourist | (64, 0) | 64x96 | Panic browsing, wide eyes, everything else is closed |
| The MurphyBoost Enthusiast | (128, 0) | 64x96 | Third can of EXTREME, base pose (vibration frame 1) |
| The Morning Returner | (192, 0) | 64x96 | Haunted, gray-faced, here for the headache cure |

### Secondary Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Enthusiast Vibration Frame 2 | (0, 96) | 64x96 | 1px offset jitter — "the jitters aren't a bug, they're a FEATURE" |
| Enthusiast Vibration Frame 3 | (64, 96) | 64x96 | 2px offset jitter, eyes slightly wider |
| Customer Side-Effect Pose | (128, 96) | 64x96 | Generic regret stance for any NPC mid-consequence |
| Tourist Arms-Full | (192, 96) | 64x96 | "I'll take it all." Carrying too much, committing to regret |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Regular Portrait | (0, 192) | 64x48 | "You're new here, aren't you?" |
| Tourist Portrait | (64, 192) | 64x48 | Mid-panic |
| Enthusiast Portrait | (128, 192) | 64x48 | Pupils like dinner plates |
| Returner Portrait | (192, 192) | 64x48 | Thousand-yard stare, Murphy's Lawless edition |

### Technical Notes:
- Enthusiast vibrates via 3-frame cycle at 12 fps — the only fast animation in the shop, which is the joke
- Max 2 customer NPCs on screen at once (performance budget + the shop is never busy, only occupied)
- Morning Returner spawns only during morning hours; hostile-adjacent idle, never actually hostile

---

## 🍺 Sprite Sheet 5: The Cold Section & Drinks
**File:** `murphys_products_drinks.png`
**Dimensions:** 256x192 pixels

### Name Brands & Murphy's Select:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Name-Brand Lager Six-Pack | (0, 0) | 48x48 | Premium, legitimate, +30% markup — safety costs |
| Legitimate Irish Whiskey | (48, 0) | 32x48 | Actual label, actual whiskey |
| Sealed Wine | (80, 0) | 32x48 | Boring. Safe. Correct |
| Craft Beer (Cold) | (112, 0) | 32x48 | Condensation included |
| Name-Brand Energy Drink | (144, 0) | 32x48 | The 10%-risk option |
| Murphy's Budget Lager Six-Pack | (176, 0) | 48x48 | -20% price, 25% Regret. "It'll do what beer does. Mostly." |
| "Imported" Whiskey | (224, 0) | 32x48 | Imported from where? Quotation marks load-bearing |

### The Gamble Shelf:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Mystery Wine (Sealed Since '08) | (0, 48) | 32x64 | Dust-coated bottle, label sun-faded illegible. Could be great. Could be vinegar |
| Murphy's Strong Tall Can | (32, 48) | 32x64 | Ominously tall. 3 Sovs. "Bad Decision" buff included |
| MurphyBoost™ Original | (64, 48) | 32x64 | Suspicious Yellow can with lightning bolt drawn slightly wrong |
| MurphyBoost™ EXTREME | (96, 48) | 32x64 | EXTREME Red, 60% Cardiac Concern, no waiver (there should be) |
| "Medicinal" Energy Tonic | (128, 48) | 32x64 | Apothecary-shaped bottle, medical claims in tiny print |
| Fridge Shelf Dressing Row | (160, 48) | 96x64 | Mixed bottle/can filler for cold-section shelves |

### Label Close-Ups (Examine Gags):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| MurphyBoost Label Close-Up | (0, 112) | 64x48 | "NOW WITH MORE" — more what is never stated |
| EXTREME Warning Label | (64, 112) | 64x48 | "SIGN THE WAIVER (THERE IS NO WAIVER)" |
| Mystery Wine Dust Layer | (128, 112) | 32x48 | Separate overlay proving it's been there since '08 |
| Cold/Warm Beer State Pair | (160, 112) | 64x48 | With/without condensation — temperature reliability varies |
| Empty Cans Props | (224, 112) | 32x48 | Crushed MurphyBoost cans for street/floor dressing |

### Shelf Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Handwritten Price Tags | (0, 160) | 128x32 | Suspicious Yellow tags, prices in Murphy's scrawl |
| Shelf Talker "MURPHY RECOMMENDS?" | (128, 160) | 128x32 | The question mark is doing tremendous work |

### Technical Notes:
- Risk-tier products carry a subtle hatched border baked into the sprite (see Colorblind Considerations)
- Mystery Wine renders bottle + dust overlay as two layers so examining can "wipe" the dust
- All drink sprites drop into both shelf slots and the inventory UI at native size

---

## 🥜 Sprite Sheet 6: Sundries, "Medicine" & Counterfeits
**File:** `murphys_products_sundry.png`
**Dimensions:** 256x192 pixels

### Snacks:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Sealed Crisps | (0, 0) | 32x32 | The only 0%-risk item in the building |
| Open-Section Crisps | (32, 0) | 32x32 | Bag clipped shut with a clothes peg. 20% Stale |
| Mystery Meat Roll | (64, 0) | 32x32 | Heat-lamp sheen. The mystery is included |
| Day-Old Sandwich | (96, 0) | 32x32 | "It's been here a while. But it's still here." |
| Murphy's Mixed Nuts | (128, 0) | 32x32 | One nut always weird |
| The Weird Nut Close-Up | (160, 0) | 32x32 | Examine payoff: it is not any known nut |
| Water Bottle (2 Sovs) | (192, 0) | 32x32 | "Worth it." — Murphy, correctly |
| Generic Cigarette Pack | (224, 0) | 32x32 | Counter-wall stock |

### "Medicinal" Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| "Headache Cure" | (0, 32) | 32x48 | Cures Hungover, 30% Drowsy. The quotation marks again |
| "Stomach Settler" | (32, 32) | 32x48 | Solves one problem, files a new one |
| "Energy Supplement" | (64, 32) | 32x48 | +All stats, then a double-penalty crash |
| Murphy's Miracle Tonic | (96, 32) | 32x48 | Cures most statuses, applies a different one. Quest item ("Murphy's Miracle") |
| Miracle Tonic Label Close-Up | (128, 32) | 64x48 | Ingredients list: "PROPRIETARY. TRUST MURPHY." |
| Back Room Quality Crate | (192, 32) | 64x48 | Sealed crate glimpsed through the ajar door pre-unlock |

### Counterfeit Merchandise:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| "Guooi" Sunglasses | (0, 80) | 32x24 | Designer, if the designer was drunk. -Durability |
| Misspelled Band Shirt | (32, 80) | 48x48 | "Vintage." The band name is confidently wrong |
| Plastic Lucky Charm | (80, 80) | 32x32 | +Luck (it's plastic, it does nothing) |
| Fraying Phone Charger | (112, 80) | 32x32 | 50% chance of working, 100% chance of fraying |
| Guooi Logo Close-Up | (144, 80) | 48x24 | Two O's too many, kerning criminal |
| Band Shirt Typo Close-Up | (192, 80) | 64x48 | Examine payoff for +Embarrassment when noticed |

### Back Room Stock (Unlockable):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Room Shelf Spread | (0, 128) | 96x64 | Name brands at reasonable prices — revolutionary |
| No-Side-Effect Seal Icon | (96, 128) | 32x32 | Back Room Green checkmark seal on trustworthy stock |
| Rare Consumable A | (128, 128) | 32x48 | Unavailable anywhere else in Publandia |
| Rare Consumable B | (160, 128) | 32x48 | Murphy's personal recommendation (trustworthy) |
| Recommendation Tag | (192, 128) | 64x32 | "MURPHY ACTUALLY RECOMMENDS" — no question mark this time |
| Reasonable Price Tag | (96, 160) | 32x32 | Shockingly fair. Regulars only |
| "REGULARS ONLY" Strip | (192, 160) | 64x32 | Shelf-edge banner for the back room |

### Technical Notes:
- Counterfeit items carry a faint wobble in the linework — the fakeness must read at sprite scale
- Weird Nut and Band Shirt Typo close-ups are examine-triggered popups, loaded with the sheet (no extra file)
- Back room rows stay dormant in the atlas until `back_room_unlocked`

---

## ✨ Sprite Sheet 7: Effects & Status Icons
**File:** `murphys_effects.png`
**Dimensions:** 256x128 pixels

### Light & Flicker Frames:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Neon Flicker Frame 1 | (0, 0) | 64x16 | Full glow |
| Neon Flicker Frame 2 | (64, 0) | 64x16 | Letters dropping out |
| Neon Flicker Frame 3 | (128, 0) | 64x16 | Near-dark, one letter fighting on |
| Neon Buzz-Pop Flash | (192, 0) | 64x16 | Single bright pop frame, paired with electrical-pop audio |
| Fluorescent Flicker Frame 1 | (0, 16) | 64x16 | On |
| Fluorescent Flicker Frame 2 | (64, 16) | 64x16 | Half-lit stutter |
| Fluorescent Flicker Frame 3 | (128, 16) | 64x16 | Off blink |
| Fridge Light Stutter | (192, 16) | 64x16 | Interior light hesitation frame |

### Ambient Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Condensation Drip Frame 1 | (0, 32) | 16x16 | Bead forming |
| Condensation Drip Frame 2 | (16, 32) | 16x16 | Bead sliding |
| Condensation Drip Frame 3 | (32, 32) | 16x16 | Drop released |
| Fridge Death-Rattle Frame 1 | (48, 32) | 32x16 | 1px shudder offset |
| Fridge Death-Rattle Frame 2 | (80, 32) | 32x16 | Counter-shudder + rattle lines |
| Dust Motes | (112, 32) | 32x32 | Floating in the fluorescent beam |
| Door Stick Shake Lines | (144, 32) | 32x32 | Impact lines for the mid-push frame |
| Ominous Side-Effect Aura | (176, 32) | 32x32 | Sickly glow that precedes consequences |
| Purchase Sparkle (Ironic) | (208, 32) | 32x32 | Cheerful sparkle on checkout — the optimism before |
| Cold Air Wisp | (240, 32) | 16x32 | Fridge-door-open vapor |
| Neon Reflection Puddle | (0, 48) | 64x16 | Red shimmer overlay for exterior puddles |
| Register Ding Flash | (64, 48) | 48x16 | Brass glint on the 1987 register's ding |

### Side-Effect Status Icons (32x32 each):
| Icon | Position | Size | Description |
|------|----------|------|-------------|
| Regret | (0, 64) | 32x32 | Drooping pint glass, introspective raincloud |
| Jitters | (32, 64) | 32x32 | Vibrating can with motion lines |
| Cardiac Concern | (64, 64) | 32x32 | Heart with worried eyebrows, flashes in HUD |
| Questionable | (96, 64) | 32x32 | Meat roll with a question mark — effect: ??? |
| Stale | (128, 64) | 32x32 | Cracked crisp, gray tone |
| Drowsy | (160, 64) | 32x32 | Half-closed eyelids, sinking Z |
| Bad Decision | (192, 64) | 32x32 | Confident thumbs-up with tiny warning triangle |
| Iron Stomach Achievement | (224, 64) | 32x32 | Riveted iron gut badge — 10 items, zero effects |

### Progression & Trigger Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Frequent Sufferer Badge | (0, 96) | 32x32 | Five tally marks over a queasy face — earned through pain |
| Crash Incoming Icon | (32, 96) | 32x32 | Countdown cloud for delayed energy-drink crashes |
| Side-Effect Trigger Burst Frame 1 | (64, 96) | 32x32 | Aura ignition |
| Side-Effect Trigger Burst Frame 2 | (96, 96) | 32x32 | Full sickly flash |
| Side-Effect Trigger Burst Frame 3 | (128, 96) | 32x32 | Settle into status icon |
| Jitters Shake Overlay | (160, 96) | 32x32 | Screen-space shiver lines for Jitters status |
| Heart Flash Frame 1 | (192, 96) | 32x32 | Cardiac Concern HUD pulse, bright |
| Heart Flash Frame 2 | (224, 96) | 32x32 | Cardiac Concern HUD pulse, dim |

### Technical Notes:
- Every status icon pairs shape + posture, never color alone (see Colorblind Considerations)
- Trigger Burst is the single scariest visual in the shop — 3 frames, then it's over, and the icon just... stays
- All flicker frames drive alpha-toggle timers; motion-reduced mode swaps to steady frames on the accessibility sheet

---

## 🎮 Sprite Sheet 8: UI Elements
**File:** `murphys_ui.png`
**Dimensions:** 256x256 pixels

### Shop Inventory:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shop Inventory Frame | (0, 0) | 192x128 | Grimy shelf-styled browse window, category rows |
| Risk % Display (Sober) | (192, 0) | 64x32 | "RISK: 40%" — plain, honest, visible only when sober |
| Risk % Display (Drunk) | (192, 32) | 64x32 | "RISK: ¯\\_?_/¯" — smeared, unreadable, hidden by design |
| Risk Pip Row | (192, 64) | 64x32 | 5-pip risk meter, hatch-pattern coded per tier |
| Category Tabs | (192, 96) | 64x32 | Beer / Boost / Snacks / "Medicine" / Merch |

### Transaction Popups:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Purchase Confirm Popup | (0, 128) | 96x64 | "NO REFUNDS. STILL SURE?" with laminated-sign styling |
| Side-Effect Trigger Popup | (96, 128) | 96x64 | "SOMETHING IS HAPPENING" — status icon slot + ominous border |
| Item Detail Card | (192, 128) | 64x64 | Sprite, price, Murphy's one-line commentary |

### Progression UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Room Unlock Banner | (0, 192) | 128x64 | "THE BACK ROOM IS OPEN TO YOU" in Back Room Green |
| Cash Only Icon | (128, 192) | 32x32 | Coin stack — the preferred, "honest" currency |
| Card "Broken" Icon | (160, 192) | 32x32 | Card with bandage. It is not broken. Quest evidence |
| Frequent Sufferer Progress Pips | (128, 224) | 64x32 | 5 tally pips filling per side effect survived |
| Buy Button | (192, 192) | 64x32 | "REGRET IT" (the buy verb, 44px+ touch target with padding) |
| Cancel Button | (192, 224) | 64x32 | "WISE" (the flee verb) |

### Technical Notes:
- Risk display swaps sober/drunk sprite based on player intoxication state — no numeric fallback while drunk, that's the mechanic
- Purchase Confirm always renders the No Refunds styling; there is no version without it
- All tappable UI elements ship with transparent padding to guarantee 44px minimum touch targets at 1x

---

## 🎬 Animation Specifications

### Door Stick-and-Release (The Commitment):
- **Duration:** 1.8 seconds total
- **Frames:** 4 (Closed → Stuck Mid-Push (hold 0.8s) → Stuck deeper flex → Open + bell swing)
- **Pattern:** Frame 1 → 2 (hold) → 3 → 4, one-shot per entry
- **Trigger:** Player enters the shop (every single time — the door always sticks)
- **Purpose:** The comedy beat that announces every customer; commitment mechanic made physical
- **Audio Sync:** Wood strain on the stick, bell jingle exactly on frame 4
- **Mobile Optimization:** Shake lines dropped at Low LOD; timing untouched (the joke is sacred)

### Neon Sign Flicker:
- **Duration:** 6-second loop with randomized 0-2s jitter
- **Frames:** 3 (Full Lit → Half-Dead → Off) + Buzz-Pop Flash insert
- **Pattern:** Full (4s) → Half-Dead (1.2s) → Off (0.3s) → Pop Flash (0.1s) → Full
- **Trigger:** Constant while exterior is on screen
- **Purpose:** "MURPHY'S LAWLESS" degrading to "MURPH'S LAWLE" — the sign itself obeys Murphy's Law
- **Audio Sync:** Electrical pop on the Pop Flash frame
- **Mobile Optimization:** Half-Dead held as static frame at Low LOD; reduced-motion uses accessibility steady frame

### Fluorescent Flicker (The Dying Tube):
- **Duration:** Random intervals, 20-50 seconds between events; each event 0.4s
- **Frames:** 3 (On → Half-Lit → Off → On)
- **Pattern:** Quick stutter, single event, alpha toggle
- **Trigger:** Timer, interior only
- **Purpose:** Keeps the interior slightly unreliable, like everything else in stock
- **Audio Sync:** Fluorescent buzz rises just before each stutter
- **Mobile Optimization:** Event frequency halved at Medium LOD; disabled at Low and in reduced-motion mode

### Refrigerator Death-Rattle:
- **Duration:** 1.2 seconds per rattle, every 25-40 seconds
- **Frames:** 2 (shudder offset → counter-shudder), 6 alternations
- **Pattern:** 1 → 2 → 1 → 2 → 1 → 2 → rest
- **Trigger:** Timer, weighted to trigger when the player approaches the cold section
- **Purpose:** The refrigerator is dying and has been for years; the hum is the shop's heartbeat
- **Audio Sync:** Hum pitch drops then recovers across the rattle — the death-rattle audio gag
- **Mobile Optimization:** Rattle becomes audio-only at Low LOD (sprite stays still)

### Murphy Counter Idle (Watching):
- **Duration:** 12-second loop
- **Frames:** 4 (Watching (8s) → slow blink → head turn toward player (2s) → return)
- **Pattern:** Loop with gaze tracking the player's aisle position on the head-turn beat
- **Trigger:** Constant while Murphy is unengaged
- **Purpose:** Murphy notices everything; the player should feel gently observed at all times
- **Audio Sync:** Occasional sigh on the return beat (30% chance per loop)
- **Mobile Optimization:** Gaze tracking dropped at Low LOD; blink retained

### Enthusiast Vibration:
- **Duration:** 0.25-second loop (continuous)
- **Frames:** 3 (base → 1px offset → 2px offset)
- **Pattern:** 1 → 2 → 3 → 2 → loop at 12 fps
- **Trigger:** Constant while The MurphyBoost Enthusiast is on screen
- **Purpose:** Three cans of EXTREME rendered as pure frame data; warning and aspiration simultaneously
- **Audio Sync:** None (the silence makes it worse)
- **Mobile Optimization:** Drops to 2-frame 6 fps at Low LOD; static base frame in reduced-motion mode

### Side-Effect Trigger:
- **Duration:** 1.0 second, one-shot
- **Frames:** 3 burst frames + status icon settle
- **Pattern:** Aura ignition → sickly flash → settle → status icon persists in HUD
- **Trigger:** Consumption roll fails (risk % check on item use)
- **Purpose:** The moment of consequence — brief, ominous, then quietly permanent
- **Audio Sync:** Ominous side-effect sting starts on frame 1; Murphy's knowing "hmm" 0.5s after settle if in shop
- **Mobile Optimization:** Flash frame brightness capped at Low LOD; single-frame version in reduced-motion mode

### Condensation Drip:
- **Duration:** 2.5 seconds per drip, staggered across fridge doors
- **Frames:** 3 (bead → slide → release)
- **Pattern:** One-shot per spawn point, max 3 concurrent
- **Trigger:** Constant near cold section
- **Purpose:** The fridges sweat; temperature reliability is visibly variable
- **Audio Sync:** None
- **Mobile Optimization:** Disabled at Low LOD

---

## ♿ Accessibility Sprite Requirements
**File:** `murphys_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Inventory Frame, Bold | (0, 0) | 96x64 | Thick-bordered browse window, enlarged product rows and price text |
| Purchase Confirm, Bold | (96, 0) | 96x48 | Oversized "NO REFUNDS. STILL SURE?" with heavy outline |
| Murphy Counter Hotspot Outline | (192, 0) | 48x64 | White-on-dark outline for Murphy's talk/shop interaction zone |
| Cold Section Hotspot Outline | (0, 64) | 64x64 | Outlined fridge examine zone, back-of-fridge mystery included |
| Back Room Door Outline | (64, 64) | 64x64 | High-visibility "STAFF ONLY" door hotspot with lock-state indicator |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon Sign, Steady | (128, 64) | 64x16 | Constant half-glow "MURPHY'S LAWLESS" — flicker cycle disabled |
| Fluorescent, Steady | (128, 80) | 64x16 | Constant tube light, stutter events off |
| Fridge, No Shudder | (128, 96) | 64x32 | Static fridge bank frame — death-rattle becomes audio/caption only |
| Side-Effect Burst, Single-Frame | (192, 64) | 32x32 | One dimmed frame replacing the 3-frame flash |
| Door Shake Lines, Off | (192, 96) | 32x32 | Stuck-door frame without impact lines |
| Enthusiast, Static | (224, 64) | 32x64 | Non-vibrating pose with jitter implied by linework only |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Bell + Stick Icon | (0, 128) | 32x32 | Strained-door glyph then bell burst — covers the stick-first entry every time |
| Fridge Hum Waves | (32, 128) | 32x32 | Uneven wave lines over the cold section; wobbles during death-rattle |
| Fluorescent Buzz Zigzag | (64, 128) | 32x32 | Zigzag glyph above the dying tube when the buzz rises |
| Neon Pop Spark | (96, 128) | 32x32 | Spark glyph at the sign on each electrical pop |
| Purchase Beep Icon | (128, 128) | 32x32 | Register blip glyph on checkout confirmation |
| Ominous Trigger Vignette | (160, 128) | 48x32 | Screen-edge sickly darkening replacing the side-effect sting audio |
| Murphy's "Hmm" Bubble | (208, 128) | 32x32 | Small "hmm." bubble at Murphy — the knowing judgment, visualized |
| Sigh Wisp | (240, 128) | 16x32 | Faint breath wisp for Murphy's occasional sigh |

### Colorblind Considerations:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Risk-Tier Hatch Legend | (0, 160) | 128x32 | Risk pips coded by hatch density (solid/diagonal/cross-hatch), never color alone — the percentage numeral always renders beside the pips when sober |
| Large Touch Target Overlay | (128, 160) | 64x32 | Debug/QA overlay proving 44px minimum zones on buy, cancel, tabs, and hotspots |
| Status Icon Text Labels | (192, 160) | 64x32 | Text label strip ("REGRET", "JITTERS", etc.) attachable under every status icon |

- Risk percentages communicate via numeral + hatch pattern + pip count — three channels, zero color dependency
- Status icons are shape-distinct silhouettes (drooping glass vs. vibrating can vs. worried heart) before any color is applied
- MurphyBoost Original vs. EXTREME differ by can shape and label typography, not just yellow vs. red
- All interactive elements (buy, cancel, tabs, Murphy, fridges, back room door) meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback for legacy devices); murphys_ui.png and murphy_seamus.png at ASTC 4x4 — text and portraits must stay crisp
- **Android:** ETC2 with alpha for all sheets
- **Fallback:** Lossless PNG for murphys_ui.png (risk percentages and sign text are gameplay-critical reading)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| murphys_environment | murphys_exterior, murphys_interior | 1024x1024 |
| murphys_characters | murphy_seamus, murphys_customers | 1024x512 |
| murphys_products | murphys_products_drinks, murphys_products_sundry | 512x512 |
| murphys_fx_ui | murphys_effects, murphys_ui, murphys_accessibility | 1024x512 |

*(All atlases well under the 2048x2048 mobile GPU compatibility ceiling.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full flicker cycles, death-rattle shudder, condensation drips, mist scroll, gaze tracking, all rain particles |
| Medium | Fluorescent events halved, drips at 1 concurrent, rain at 10 drops, mist static |
| Low | Steady lighting frames, static fridge (audio-only rattle), no drips, rain at 5 drops, Enthusiast at 6 fps |

### Performance Targets:
- **Target FPS:** 60 (profile floor of 60 FPS treated as the never-drop-below line on minimum-spec devices)
- **Max Draw Calls:** 12 per frame (per the location performance budget)
- **Memory Footprint:** 30 MB maximum (location budget); asset payload ~16 MB leaves headroom for audio and state
- **Particle Limit:** 20 (rain, dust motes, and cold-air wisps share the pool)

### Performance Notes:
- Simplified shelving meshes on mobile — aisle shelves collapse to 2 sprites + collision, per the profile's platform note
- Reduced flicker on mobile: neon and fluorescent share one timer to avoid duplicate per-frame work
- Back Room Interior streams in on unlock only; never resident during normal shopping
- Max 2 customer NPCs concurrent; the Enthusiast's 12 fps vibration is the frame-rate budget's single indulgence

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap for floor/cobble tiles; single-scene interior (no parallax — the shop is too cramped for depth, which is correct)
- CPUParticles2D (not GPU) for rain (20 cap), dust motes, and cold-air wisps
- Neon, fluorescent, and fridge-light flicker driven by alpha-toggle timers — all flicker timers disabled in reduced-motion mode, swapping to the accessibility sheet's steady frames
- Area2D examine points: Mystery Wine ('08 dust wipe), back-of-fridge silhouette, weird nut, Guooi logo, band shirt typo, card machine (dusty, functional — sets `card_machine_examined` for "The Card Machine")
- Shop state per `murphys_lawless_state`: side_effects_suffered (0-5+), frequent_sufferer, back_room_unlocked, iron_stomach_progress, card_machine_examined, purchases_total, player_sober (drives risk display + Murphy's warning pose)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Door Stick-and-Release (1.8s) | Wood strain, then door bell | Strain on the stuck hold; bell exactly on the open frame — sticks first, every time |
| Fridge bank / Death-Rattle | Refrigerator hum (constant, uneven) | Hum loops always; pitch drops and recovers across each 1.2s rattle |
| Fluorescent Flicker event | Fluorescent buzz | Buzz swells 0.2s before the stutter, cuts on the off-frame |
| Neon Buzz-Pop Flash | Neon sign electrical pop | Pop lands on the single flash frame, every flicker cycle |
| Purchase Confirm → Buy | Purchase beep | Beep on confirm tap; register ding flash follows on the 1987 register |
| Side-Effect Trigger Burst | Ominous side-effect sting | Sting starts on burst frame 1, resolves as the status icon settles |
| Portrait Hmm / Knowing Hmm pose | Murphy's knowing "hmm" | On pose entry — 0.5s after any side effect triggers in-shop |
| Murphy Counter Idle | Murphy's occasional sigh | On the idle loop's return beat, 30% chance |
| Exterior ambience | Distant traffic | Constant low bed, quieter late night, harsh at morning transition |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Murphy's Miracle | Murphy's Miracle Tonic, Miracle Tonic Label Close-Up, Side-Effect Trigger Burst, status icon set | Investigating what's actually in the tonic; each test dose rolls the "cures one, applies another" gag via the trigger popup |
| The Back Room | Back Room Door Closed/Ajar, Back Room Interior, Quality Shelf, No-Side-Effect Seal, Unlock Banner, Frequent Sufferer Badge | Unlock via Frequent Sufferer status or quest completion; door swaps to Ajar, interior streams in, banner fires once |
| Quality Control | Murphy Restocking pose, unlabeled Rare Consumable sprites, Side-Effect Trigger Popup, Customer Side-Effect Pose | Murphy "tests" new products — you're the test; each sample rolls effects live with Murphy's Knowing Hmm on failure |
| The Card Machine | Card Machine (Dusty, Functional), "Card machine broken (always)" sign, Card "Broken" Icon, Portrait Default | Examining the machine vs. the sign exposes the lie; Murphy's "Cash is honest. Card is... traceable." dialogue branch |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Craic Tax | Distant Craic Tax Glow strip on the exterior sheet; bar-to-Murphy's stumble is the shop's main artery | Warm bar glow up the street; customers (and bros) flow downhill from last orders to Murphy's neon |
| The Bunk & Blunder | Hostel guests resupply here — Desperate Tourist and Tourist Arms-Full poses double as hostel-guest spawns | Late-night walk transition; guests exit with Murphy's bags as inventory props |
| Paddy's Book | MurphyBoost Original/EXTREME sprites feed the gambling-energy pipeline | Enthusiast NPC pathing between locations; EXTREME purchase flagged for Paddy's Book all-nighter dialogue |
| The Blarney Trap | Seamus (Blarney) knows Murphy — old Dublin connection; Portrait Default reused in cross-referenced dialogue | Name-drop dialogue triggers; no shared scene, just two old operators who neither confirm nor deny |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "The glow of poor decisions, the hum of dying refrigerators"
- **Color Mood:** Flickering Neon red bleeding into street mist; Refrigerator White as the only clean light in the building; Grime Brown swallowing everything below waist height; Suspicious Yellow shouting prices nobody should pay
- **Lighting:** Harsh fluorescent (one tube dying), neon spill through barred windows, fridge glow as the cold section's siren call; outside, rain and mist eat the streetlight — Dublin-style late-night side-street economics rendered in two light sources and a prayer
- **Texture:** Sticky lino, scratched reinforced perspex, dust strata on the '08 wine, laminate on the one sign Murphy means

### Environmental Storytelling:
- The apostrophe on the hand-painted sign hangs at an angle that has clearly been "fixed" several times
- "Card machine broken (always)" taped beside a card machine that is visibly dusty and visibly functional — the lie is on display
- The OPEN sign has never been off; the door has never not stuck; the "No Refunds" sign is the only laminated thing in the shop — Murphy's priorities, documented
- The back-of-fridge darkness and the sealed-since-'08 Mystery Wine tell the inventory philosophy without a word: availability over quality, always
- The back room, glimpsed green and clean through an ajar door, is the shop's one honest secret

### Character Integration Notes:
- Murphy never judges and never exceeds a 3/10 emote — acceptance is the performance; the Frequent Sufferer Warmth pose should be exactly warm enough to be concerning
- The Subtle Warning Lean must be missable: sober players catch it, drunk players get nothing, and that asymmetry is the entire warning system
- Customers are a consequence timeline: Regular (learned), Tourist (learning), Enthusiast (refusing to learn), Morning Returner (learned too late)

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Half-Dead Neon** - "MURPH'S LAWLE" glowing through the mist, apostrophe dangling — instantly recognizable shop-sign comedy
2. **"Card machine broken (always)"** - The handwritten lie taped next to a working card machine, laminated "No Refunds" sign in frame
3. **The Risk Display Gag** - Side-by-side sober "RISK: 60%" vs. drunk "RISK: ¯\\_?_/¯" screenshots — the mechanic explains itself
4. **The Mystery Wine** - A dust-caked bottle, sealed since '08, price tag: 6 Sovs — the gamble in still-life
5. **The MurphyBoost Enthusiast** - Visibly vibrating NPC mid-testimonial, third EXTREME can in hand
6. **The Back Room Reveal** - Green-lit shelves of reasonable prices after an entire shop of chaos — the twist that quality existed all along

### Quote Potential:
- "Looking for something specific, or just browsing the desperation?"
- "The mystery wine? Someone left it here in '08. Still sealed. Could be great. Could be vinegar. Only one way to know."
- "Taking the EXTREME? Sign the waiver. I'm joking. There's no waiver. There probably should be."
- "That's a combination. Energy drinks and whiskey. Bold. I respect bold."
- "You feel ALIVE, you know? The jitters aren't a bug, they're a FEATURE."
- "The constant? Poor decisions at 3 AM. That's eternal. That's human."
- "Frequent sufferer now. Welcome to the club. There's no card. There should be."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | murphys_exterior.png | 512x384 |
| 2 | murphys_interior.png | 512x512 |
| 3 | murphy_seamus.png | 384x384 |
| 4 | murphys_customers.png | 256x256 |
| 5 | murphys_products_drinks.png | 256x192 |
| 6 | murphys_products_sundry.png | 256x192 |
| 7 | murphys_effects.png | 256x128 |
| 8 | murphys_ui.png | 256x256 |

**Total Estimated Memory:** ~16 MB (in-memory with atlas padding and mipmaps; comfortably inside the location's 30 MB budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `murphys_exterior.png` (512x384)
- [ ] `murphys_interior.png` (512x512)
- [ ] `murphy_seamus.png` (384x384)
- [ ] `murphys_customers.png` (256x256)
- [ ] `murphys_products_drinks.png` (256x192)
- [ ] `murphys_products_sundry.png` (256x192)
- [ ] `murphys_effects.png` (256x128)
- [ ] `murphys_ui.png` (256x256)
- [ ] `murphys_accessibility.png` (256x192, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (Mystery Wine dust overlay, fridge glow/condensation, and neon sign letter groups on separate layers — the sign's dead letters will change per polish pass)
- **Documentation:** Animation timing reference sheet (1.8s door beat, neon/fluorescent flicker intervals, death-rattle cadence, side-effect trigger sequence)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Flickering Neon #FF6B6B, Suspicious Yellow #FFD93D, Grime Brown #5D4037, Back Room Green #2E7D32)
- [ ] The questionable apostrophe reads as deliberately, comedically wrong at sprite scale — not as an art error
- [ ] "Card machine broken (always)" sign and the dusty-but-functional card machine both read clearly; the contradiction is quest evidence and must survive compression
- [ ] Mystery Wine's '08 dust layer wipes cleanly on examine; the bottle underneath stays illegible
- [ ] "Guooi" logo close-up is legibly misspelled — the extra O's must be unmistakable
- [ ] Accessibility visual alternatives included for all audio cues (door bell + stick, fridge hum, fluorescent buzz, neon pop, purchase beep, ominous sting, Murphy's "hmm", sigh)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (3 AM desperation economics, side effects as features) is clear throughout all assets
- [ ] Hidden interactions discoverable: back-of-fridge silhouette, weird nut, band shirt typo, card machine examine, back room glow through the ajar door
- [ ] Mobile performance optimized (12 draw calls, 20-particle pool, alpha-toggle flicker, back room streamed on unlock)
- [ ] Touch zone sizing considered (44px minimum — buy/cancel buttons, category tabs, all examine hotspots compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (hatch-pattern risk pips, numeral + pip redundancy, shape-distinct status icons, text label strip)
- [ ] Social media viral potential maximized (half-dead neon framing, sober/drunk risk display comparison, Enthusiast vibration loop GIF-ability)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only; Dublin flavor expressed through style, never named on-screen |
| Cultural Specificity | ✅ | Dublin-style late-night off-license economy, Temple Bar-adjacent survival retail |
| Satirical Targets Appropriate | ✅ | Punches at desperate tourists, bros, and 3 AM decision-making — Murphy provides, buyers choose; poverty is never the joke |
| Seedy Underbelly Present | ✅ | Questionable products at exploitative prices, counterfeit merch, the "broken" card machine, the rumored back room |
| Gameplay Value Established | ✅ | Shop + risk/side-effect system, sober/drunk information asymmetry, Frequent Sufferer progression, back room unlock, 4 quest hooks |
| Technical Feasibility | ✅ | Single-scene interior, alpha-toggle flicker, streamed back room, CPUParticles2D — all documented above |
| Mobile Performance Budget | ✅ | 60 FPS target (45 floor), 12 draw calls, 30 MB budget with ~16 MB asset payload, 20-particle cap |
| Accessibility Features | ✅ | Visual cues for all 8 audio events, steady-light variants, single-frame trigger, hatch-coded risk, 44px targets |
| No Crypto Elements | ✅ | PASS — Murphy is cash-only for entirely different, entirely suspicious reasons |
| Social Media Integration | ✅ | Six screenshot moments and seven quotable lines identified |

---

**Murphy's Lawless delivers the comedy of consequence as retail. Every asset serves the same arc: the neon lies about the shop's name, the sign lies about the card machine, the labels lie about the products — and the only honest things in the building are the "No Refunds" sign, the risk percentages you can only read sober, and the door that sticks every single time. Murphy watches it all from behind reinforced glass with 23 years of acceptance, the refrigerators rattle out their death songs, and the bros walk out into the mist carrying twelve suspiciously cheap beers and the seeds of tomorrow's status effects. The shop doesn't punish you. It just provides. That's the service.**

**"Looking for something specific, or just browsing the desperation?"**
