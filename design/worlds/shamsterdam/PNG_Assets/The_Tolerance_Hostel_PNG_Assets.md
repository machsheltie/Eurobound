# The Tolerance Hostel - Complete PNG Asset Requirements

## 📋 Overview
The Tolerance Hostel tolerates everything except being comfortable, quiet, or dignified. This document specifies every PNG asset for the hostel: the faded green door with the 60%-functional buzzer, the reception where Yusuf works on his film project, the twelve-bed dorm containing THE BUNK, the galley kitchen that becomes a confessional at 8 AM, the two bathrooms serving forty people, the passive-aggressive note ecosystem, the rotating cast of Nigel and Takeshi and Brittany and Wolf, and the 50 Sovs damage deposit you are never seeing again. Its satirical essence in a sentence: 35 Sovs buys you a bed, and everything else costs extra — especially your sanity.

**Location ID:** `shamsterdam_canalring_tolerance_hostel_01`
**Theme:** Budget travel romanticism versus budget travel reality — "meeting people" means "enduring people"
**Zone:** Canal Ring Promenade, tucked behind more respectable establishments, between a cheese shop and a "coffee" shop
**Hours:** 24-hour reception (theoretically); night staff is one guy who is "around somewhere"
**Primary Function:** Save point / rest hub / social systems node — sleep quality rolls with disruption events, kitchen gossip hint delivery, fridge politics, bulletin board quest hooks, bathroom line mechanics, and the Wi-Fi network that triggers ICQ

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Hostel Beige | #D4C5A9 | Walls, bunk frames, general surfaces |
| Budget Blue | #4169E1 | Signage, lockers, plastic fittings, TripAdvisor sticker |
| Fluorescent Wash | #F5F5DC | Reception lighting, harsh dorm overhead |
| Stain Brown | #8B7355 | THE BUNK, carpet history, kitchen accumulation |
| Notice Yellow | #E8D44D | Passive-aggressive notes, warning tape, sticky notes |
| Night Dorm Blue | #232A3A | Overnight scenes, phone-screen darkness |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/tolerance_hostel/
├── environment/
│   ├── hostel_rooms_a.png
│   ├── hostel_rooms_b.png
│   └── hostel_exterior_fixtures.png
├── objects/
│   └── hostel_objects.png
├── npcs/
│   ├── npc_hostel_staff.png
│   └── npc_hostel_guests.png
├── effects/
│   └── hostel_effects.png
└── ui/
    └── hostel_ui.png
```

---

## 🛏️ Sprite Sheet 1: Rooms A — Reception/Common & The Dorm
**File:** `hostel_rooms_a.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed — only one room sheet resident at a time)
**Color Palette:** #D4C5A9, #F5F5DC, #8B7355, #232A3A

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reception & Common Area | (0, 0) | 1024x1024 | Cramped lobby: check-in desk behind sticker-covered plexiglass, key rack with visible gaps, bulletin board, vending machine, lost-and-found box, Windows 7 computer, three couches telling three different stories of human suffering, TV playing Dutch news to nobody, world map with pins in the wrong countries, Polaroid wall of the "Tolerance Family" |
| 12-Bed Dorm Room | (1024, 0) | 1024x1024 | Three bunk stacks per wall, narrow aisle, lockers too small for luggage, one outlet per four beds, privacy curtains on the four premium bunks, laundry hanging from every possible surface, and THE BUNK in the bottom corner — draft, stain, and all |

### Technical Notes:
- Anchor points (Reception): desk at (256, 640), key rack at (448, 512), bulletin board at (640, 448), vending machine at (128, 704), couch slots at (704, 768) / (896, 800), TV at (832, 512), computer at (448, 768)
- Anchor points (Dorm): bunk slots at (1152, 576) / (1152, 832) / (1472, 576) / (1472, 832) / (1792, 576) / (1792, 832), THE BUNK at (1792, 896), locker row at (1344, 960), outlet at (1280, 704), aisle centre at (1536, 896)
- Both rooms share one 8.39 MB texture and stream together as the ground-floor pair
- THE BUNK is painted with its distinguishing marks baked in — the stain, the visible draft gap in the wall behind it, and the marginally more collapsed mattress. It must be identifiable from the doorway without any UI marker.
- The dorm background ships with a night-grade variant baked into the alpha of a second layer group so the overnight scene does not require a separate texture
- Reception fluorescent is painted at a neutral value; the flicker overlay (Sheet 7) supplies the malfunction

---

## 🍳 Sprite Sheet 2: Rooms B — Communal Kitchen & Bathroom Line
**File:** `hostel_rooms_b.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed)
**Color Palette:** #D4C5A9, #8B7355, #E8D44D, #F5F5DC

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Communal Kitchen | (0, 0) | 1024x1024 | Galley kitchen barely fitting four people, designed for forty: fridge covered in labelled territories, stovetop with two working burners and two decorative ones, sink perpetually full of dishes that are "soaking," microwave with a permanent tomato-sauce explosion on the ceiling above it, spice rack containing salt and restaurant packets, table for six that twelve are using, and the peanut butter |
| Bathroom Line Area | (1024, 0) | 1024x1024 | Two doors, forty guests, one corridor. Queue marks worn into the floor, "5 MINUTE SHOWER LIMIT" sign, territorial toiletry collection claiming an entire sink, drain hair representing six continents, and a mirror with a motivational sticker that reads differently at 3 AM |

### Technical Notes:
- Anchor points (Kitchen): fridge at (128, 512), stovetop at (384, 576), sink at (576, 576), microwave at (768, 448), table at (512, 832), notes wall at (896, 384), peanut butter shelf at (704, 640)
- Anchor points (Bathroom): door A at (1280, 576), door B at (1600, 576), queue origin at (1920, 768), mirror at (1408, 448), sink pair at (1728, 640)
- Kitchen is the only room in the location with warm morning light; the confessional happens here and the grade should make it feel almost pleasant, which is the trap
- The microwave ceiling explosion must be visible in wide shots — it is the kitchen's establishing detail
- Bathroom queue floor marks are painted worn, not drawn as signage; nobody made them, they accumulated

---

## 🚪 Sprite Sheet 3: Exterior & Fixtures
**File:** `hostel_exterior_fixtures.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #D4C5A9, #4169E1, #8B7355, #E8D44D

### Exterior & Reception:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hostel Exterior (Canal House) | (0, 0) | 384x512 | Narrow entrance, faded green door, brass "TOLERANCE" sign from the 1970s, weed smoke from the upper windows, a guy on the stoop who may or may not be a guest |
| Reception Desk + Plexiglass | (384, 0) | 256x192 | COVID addition, never removed, now entirely stickers |
| Key Rack (Missing Keys) | (640, 0) | 128x192 | Visible gaps; some rooms have three-plus copies in circulation |
| Bulletin Board | (768, 0) | 256x384 | Pub crawl flyers from 2019, one yoga class that never happened, real quest hooks hidden among them |
| Vending Machine | (384, 192) | 96x192 | 4 Sovs water, 6 Sovs "emergency toiletries" |
| Communal Computer (Windows 7) | (480, 192) | 128x96 | Keyboard is... sticky |
| Lost & Found / Free Stuff Box | (608, 192) | 128x96 | The distinction stopped mattering years ago |
| TV (2009, Dutch News) | (480, 288) | 128x96 | Nobody is watching. It has never been off. |
| Three Couches | (608, 288) | 160x96 | Three different stories of human suffering |
| World Map with Wrong Pins | (384, 384) | 192x128 | 90% are in the wrong location |
| Polaroid Wall ("Tolerance Family") | (576, 384) | 192x128 | Everyone looks wasted |
| "House Rules" Poster (8 Languages) | (768, 384) | 128x128 | Nobody reads any of them |
| Passive-Aggressive Note Collection | (896, 384) | 128x128 | Wall-mounted archive of accumulated hostility |

### Dorm Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Metal Bunk Bed Unit | (0, 512) | 192x256 | Standard stack, mattresses of varying depression levels |
| THE BUNK (Detail) | (192, 512) | 256x192 | Bottom corner. Mysterious stain. Draft. Everyone knows which one. |
| Privacy Curtain (Premium Bunks) | (448, 512) | 96x192 | Four bunks have these. The hierarchy is visible. |
| Locker Row | (544, 512) | 256x128 | Too small for actual luggage; locks sold separately (8 Sovs) |
| Single Power Outlet | (544, 640) | 64x64 | One per four beds. The adapter wars are real. |
| Adapter War Tangle | (608, 640) | 64x64 | Six devices. One socket. Ongoing diplomacy. |
| Laundry on Every Surface | (672, 640) | 128x64 | Somebody's, everybody's, nobody's |
| Earplugs on Pillow | (800, 512) | 96x64 | Veteran move, visible from the door |
| Reading Light (Half Broken) | (896, 512) | 128x64 | Two states: off, and also off |
| Mattress (Varying Depression) | (800, 576) | 224x96 | Three depression levels for random bunk assignment |
| Dorm Overhead Light | (800, 672) | 128x96 | Always too bright, no dimmer, no mercy |
| Dorm Aisle Floor (Tileable) | (928, 672) | 96x96 | Worn vinyl, seamless all edges |
| Bunk Ladder | (192, 704) | 128x64 | Metal, cold, loud |
| Under-Bunk Luggage | (320, 704) | 128x64 | Because the lockers do not fit it |
| Draft Source (THE BUNK Corner) | (448, 704) | 96x64 | The gap in the wall. Nobody has ever mentioned it. |
| Mysterious Stain | (544, 704) | 128x64 | Detail plate for THE BUNK close-ups |
| Bunk Frame Creak Point | (672, 704) | 128x64 | The specific joint responsible for every movement sound |

### Kitchen & Bathroom Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fridge (Passive-Aggressive Labels) | (0, 768) | 128x256 | Names, dates, threats, escalation |
| Stovetop (2 Working Burners) | (128, 768) | 128x128 | The other two are "decorative" |
| Sink (Perpetually "Soaking") | (256, 768) | 128x128 | Everything is soaking. Everything has always been soaking. |
| Microwave (Ceiling Explosion) | (384, 768) | 128x128 | Permanent tomato sauce overhead, unaddressed |
| Spice Rack | (512, 768) | 128x64 | Salt, and packets stolen from restaurants |
| Communal Peanut Butter Shelf | (512, 832) | 128x64 | It cannot be taken. It cannot be discarded. |
| Kitchen Table for 6 | (640, 768) | 192x128 | Twelve are eating at it |
| Dish Pile | (832, 768) | 96x128 | Soaking |
| Kitchen Wall Notes | (928, 768) | 96x128 | "WASH YOUR DISHES OR WE WASH THEM WITH YOUR TOOTHBRUSH" |
| Bathroom Door x2 | (128, 896) | 128x128 | Two. For forty-plus. |
| Shower Stall (3, One Hot) | (256, 896) | 128x128 | Location of the good one is classified until night three |
| Toilet Stall (1 Lock Works) | (384, 896) | 128x128 | The other two require the "hold and hope" technique |
| Sink Pair (Slow Drain) | (512, 896) | 128x128 | Pack patience |
| "5 MINUTE SHOWER LIMIT" Sign | (640, 896) | 96x64 | Universally ignored |
| Mirror ("TODAY IS A NEW DAY") | (736, 896) | 96x64 | Reads differently at 3 AM |
| Territorial Toiletry Collection | (640, 960) | 96x64 | One person's entire kit, claiming an entire sink |
| Bathroom Queue Floor Marks | (736, 960) | 96x64 | Worn in, not painted on |
| Faded Green Door + Buzzer | (832, 896) | 96x128 | "RING TWICE. WAIT. RING AGAIN. WE ARE COMING." |
| TripAdvisor 3.4 Star Sticker | (928, 896) | 96x64 | "Great location! Interesting people!" |
| Hostelworld "PARTY HOSTEL" Badge | (928, 960) | 96x64 | Not updated since 2015 |

### Technical Notes:
- Dorm Aisle Floor is the only tiled asset; it must seam on all four edges
- THE BUNK, its stain, and its draft source ship as separate elements so the bunk can be assembled at any dorm slot, but the canonical placement is the bottom corner nearest the draft
- Mattress plate contains three depression variants sampled at random per bunk on scene load
- All passive-aggressive notes and signage are baked at 2x internal resolution and flagged for the ASTC 4x4 exception list — the note text is a primary comedy delivery vector

---

## 🔑 Sprite Sheet 4: Objects & Hostel Ephemera
**File:** `hostel_objects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #4169E1, #E8D44D, #8B7355, #D4C5A9

### Keys, Locks & Bedding:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hostel Key (Oversized Keychain) | (0, 0) | 48x64 | Large enough to be embarrassing in public. Deliberately. |
| Locker Lock | (48, 0) | 32x32 | 8 Sovs at reception, roughly 3x market price |
| Passport | (48, 32) | 32x32 | Check-in requirement, deposit hostage |
| Sleep Quality Dice | (80, 0) | 64x64 | The overnight roll, visualised |
| Breakfast Sad Bread | (144, 0) | 64x32 | "It's bread. And whatever's in the jar." |
| Mystery Jar | (144, 32) | 32x32 | "I don't ask about the jar." |
| Eternal Peanut Butter | (176, 32) | 32x32 | Exists outside time. Cannot be taken. Cannot be discarded. |
| Fridge Shelf (Yours) | (208, 0) | 64x64 | Designated, 85% safe, 95% with a threatening label |
| Fridge Shelf (Communal) | (272, 0) | 64x64 | Fair game. Expect loss. |
| Alarm Phone Buzzing F1 | (336, 0) | 32x32 | 5 AM. Every day. |
| Alarm Phone Buzzing F2 | (368, 0) | 32x32 | Still 5 AM. Still buzzing. |
| Wi-Fi Password Note | (336, 32) | 64x32 | "everything" — lowercase, one word |
| Shower Hot Water Indicator | (400, 0) | 48x64 | The good shower's secret, learned after two nights |
| Towel | (448, 0) | 64x64 | 3 Sovs. You were supposed to bring one. |

### The Note Ecosystem:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Passive-Aggressive Note A | (0, 64) | 96x64 | "YOUR MOTHER DOESN'T WORK HERE" |
| Passive-Aggressive Note B | (96, 64) | 96x64 | "WASH YOUR DISHES OR WE WASH THEM WITH YOUR TOOTHBRUSH" |
| Passive-Aggressive Note C | (192, 64) | 96x64 | Fridge label: name + date + escalating threat |
| Bulletin Flyer (Pub Crawl 2019) | (288, 64) | 96x64 | Still up. Still 2019. |
| Bulletin Flyer (Lost Passport) | (384, 64) | 64x64 | "If found, I'm the crying one in room 4." |
| Bulletin Flyer (Taxi Share) | (448, 64) | 64x64 | Legitimate quest hook hiding in plain sight |

### Dorm & Kitchen Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sheet | (0, 128) | 64x64 | "Supposed to have sheet. Check lost and found." |
| Earplugs | (64, 128) | 64x64 | The single best item in the location |
| Paracetamol Strip | (128, 128) | 64x64 | Nigel needs some. Nigel always needs some. |
| Phone Charger (Missing) | (192, 128) | 64x64 | Chadwick's. Formerly Chadwick's. |
| Deposit Receipt (20 Sovs + 50 Sovs) | (256, 128) | 64x64 | A fee, not a deposit |
| Yogurt (Contested) | (320, 128) | 64x64 | Ongoing investigation, no suspects, everyone a suspect |
| Dish Sponge (Aggressive) | (384, 128) | 64x64 | Morning scrubbing, audible from the dorm |
| Bunk Curtain Pull | (448, 128) | 64x64 | Premium bunk interaction handle |

### Icons & Materials:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Key Icon | (0, 192) | 32x32 | Oversized-keychain silhouette |
| Lock Icon | (32, 192) | 32x32 | Padlock silhouette |
| Sleep Quality Icon | (64, 192) | 32x32 | Die-face silhouette |
| Exhausted Status Icon | (96, 192) | 32x32 | Drooping-eyelid silhouette |
| Bravado Chip | (128, 192) | 32x32 | Shared-system chip, local styling |
| Wi-Fi Icon | (160, 192) | 32x32 | Arc silhouette |
| Fridge Safety Icon | (192, 192) | 32x32 | Labelled-shelf silhouette |
| Bathroom Queue Icon | (224, 192) | 32x32 | Stacked-figures silhouette |
| Hostel Floor Tile (Tileable) | (256, 192) | 64x64 | Alternate crop for prop layering |
| Polaroid (Player, Wasted) | (320, 192) | 96x64 | Added to the Tolerance Family wall on the third night |
| Check-Out Slip | (416, 192) | 96x64 | Deposit deductions, itemised, non-negotiable |

### Technical Notes:
- The Hostel Key must be recognisable at 32px as comically oversized; it is carried into other locations as a visible prop
- Sleep Quality Dice is the location's signature UI object and doubles as the save-point confirmation graphic
- Passive-aggressive notes are authored as a pool of six variants; the environment samples three at random per scene load so repeat visits read differently
- Eternal Peanut Butter has no interaction and no inventory entry; examining it returns the same line forever

---

## 🧑‍💻 Sprite Sheet 5: Hostel Staff
**File:** `npc_hostel_staff.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #D4C5A9, #4169E1, #232A3A

### Night Receptionist Yusuf:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Yusuf Night Reception Idle | (0, 0) | 64x96 | Tired, hoodie, laptop open |
| Yusuf On Laptop (Personal Project) | (64, 0) | 64x96 | Film student from Morocco, working for a free bed |
| Yusuf Check-In Process | (128, 0) | 64x96 | "Passport. Deposit. Room 3. Bed... whichever one is empty." |
| Yusuf Key Replacement F1 | (192, 0) | 64x96 | "That's the third one today." |
| Yusuf Key Replacement F2 | (256, 0) | 64x96 | "Twenty Sovs. Yeah, I know you paid deposit. Twenty Sovs." |
| Yusuf Noise Complaint | (320, 0) | 64x96 | "I'll... look into it." *returns to laptop* |
| Yusuf Wi-Fi Explanation | (384, 0) | 64x96 | "Like we tolerate everything. Get it?" |
| Yusuf Breakfast Description | (448, 0) | 64x96 | "I don't ask about the jar." |

### Day Manager Ingrid:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ingrid Day Manager Idle | (0, 96) | 64x96 | Dutch, efficient, perpetually sighing, owns 3% and thinks about it constantly |
| Ingrid Check-Out Clock Check | (64, 96) | 64x96 | "You are... an hour late. This is normal for your room." |
| Ingrid Deposit Conversation F1 | (128, 96) | 64x96 | "Your deposit? There were... issues." |
| Ingrid Deposit Conversation F2 | (192, 96) | 64x96 | "The cleaning fee. You understand." |
| Ingrid Quiet Hours Recitation | (256, 96) | 64x96 | "Or midnight. Or 2 AM." |
| Ingrid Review Comment | (320, 96) | 64x96 | "We have 3.4 stars. This is fine. Everything is fine." |
| Ingrid Silent Judgment Hold | (384, 96) | 64x96 | She remembers every rule violation |
| Ingrid "Come back soon. Or don't." | (448, 96) | 64x96 | "We are always here. The tolerance never ends." |

### Portraits & Maria:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Yusuf Portrait (Dialogue) | (0, 192) | 128x128 | Seen everything. Surprised by nothing. |
| Ingrid Portrait (Dialogue) | (128, 192) | 128x128 | Professional passive-aggression, fully realised |
| Maria Portrait (Dialogue) | (256, 192) | 128x128 | Knows everything that happens in every room. Will never tell. |
| Maria Housekeeping Idle | (384, 192) | 64x96 | Headphones always in |
| Maria Earbud Removal | (448, 192) | 64x96 | The one-earbud conversation posture |
| Reserve / Atlas Padding | (384, 288) | 128x32 | Reserved strip, do not paint |

### Maria & Staff Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Maria Sheet Change | (0, 320) | 64x96 | Efficient, silent, unhurried |
| Maria Working Around You | (64, 320) | 64x96 | Not with you. Around you. |
| Maria Muttering | (128, 320) | 64x96 | Probably commentary. Definitely commentary. |
| Maria Crime Scene Assessment | (192, 320) | 64x96 | Morning room inspection, no visible reaction |
| Yusuf Buzzer Response (Eventual) | (256, 320) | 64x96 | You rang twice, waited, rang again. He is coming. |
| Yusuf Half-Asleep | (320, 320) | 64x96 | 4 AM desk state |
| Ingrid Morning Sigh | (384, 320) | 64x96 | The default state |
| Ingrid Rule Violation Memory | (448, 320) | 64x96 | She has a list. It is not written down. |

### Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Yusuf High-Contrast Silhouette | (0, 416) | 64x96 | Accessibility outline variant |
| Ingrid High-Contrast Silhouette | (64, 416) | 64x96 | Accessibility outline variant |
| Maria High-Contrast Silhouette | (128, 416) | 64x96 | Accessibility outline variant |
| Reception Counter Pose (Yusuf) | (192, 416) | 64x96 | Behind-plexiglass anchor pose |
| Accessibility Reserve Block | (256, 416) | 256x96 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Yusuf's laptop screen is a separate glow element so it can remain lit in the night-grade dorm-adjacent lighting
- Ingrid's frames all share one silhouette with only head angle and shoulder line altered; her range is deliberately narrow
- Maria never faces the camera in any working frame except the portrait; she is authored to work past the player, not with them

---

## 👥 Sprite Sheet 6: Guests
**File:** `npc_hostel_guests.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Mixed backpacker palette, fluorescent and night-blue ambient grades

### The Rotating Cast:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Nigel the Snorer (Awake, Apologetic) | (0, 0) | 64x96 | Manchester. "Sorry mate, was I snoring again?" |
| Nigel Sleeping (Snoring) | (64, 0) | 64x96 | Room 3, Bed 7. Brutal. Nothing to be done, apparently. |
| Takeshi (5 AM Alarm Guy) | (128, 0) | 64x96 | Japanese businessman on a finding-himself trip |
| Takeshi Sleeping Through Alarm | (192, 0) | 64x96 | The alarm is for meditation. He sleeps through meditation. |
| Brittany the Oversharer | (256, 0) | 64x96 | San Diego. Kitchen regular. Morning confessional. |
| Brittany Mid-Story | (320, 0) | 64x96 | She is always mid-story |
| Wolf the Veteran Backpacker | (384, 0) | 64x96 | "Just call me Wolf." Actual name: Gavin. |
| Wolf Gatekeeping Posture | (448, 0) | 64x96 | Six years. This place is too touristy. |
| The Couple Who Forgot | (512, 0) | 128x96 | Beds 5 & 6. Whispering. Not quietly enough. |
| Locker Suspect | (640, 0) | 64x96 | Bed 12. Never gives the same name twice. |
| Locker Suspect (Near Lockers) | (704, 0) | 64x96 | Not that he was looking |
| Bros Trio (Dorm) | (768, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley, pre-composed |
| Sleeping Guests Variety | (960, 0) | 64x96 | Background sleeper, three palette variants |

### Portraits & Group Blocks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Nigel Portrait | (0, 96) | 128x128 | Genuinely apologetic. Will change nothing. |
| Wolf Portrait | (128, 96) | 128x128 | About to gatekeep a place you have not heard of |
| Brittany Portrait | (256, 96) | 128x128 | "You won't BELIEVE what happened last night." |
| Takeshi Portrait | (384, 96) | 128x128 | "Tomorrow I will fix." (He will not fix.) |
| Locker Suspect Portrait | (512, 96) | 128x128 | "Nice watch. Is that new?" |
| Kitchen Morning Block | (640, 96) | 192x96 | Pre-composed 8 AM confessional cluster |
| Bathroom Queue Block | (832, 96) | 128x96 | Pre-composed 7 AM line |
| Common Room Slump Block | (960, 96) | 64x96 | Couch occupancy, pre-composed |

### Ambient:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sleeping Silhouette Row | (640, 192) | 192x64 | Cheap dorm depth for the overnight scene |
| Bathroom Queue Shuffle Strip | (832, 192) | 128x64 | Two 64x64 frames: weight shift left / right |
| Accessibility Reserve | (960, 192) | 64x64 | Reserved for high-contrast marker |
| Portrait Band Padding | (0, 224) | 640x32 | Reserved padding, do not paint |

### Technical Notes:
- Kitchen Morning Block, Bathroom Queue Block, Common Room Slump Block, and Bros Trio all ship pre-composed to protect the 16-draw-call budget
- Sleeping Guests Variety is one sprite palette-modulated three ways; the dorm never authors individual sleepers
- The Couple Who Forgot ships as a single 128x96 block with no separable frames — this is both a performance decision and a content one
- Every guest sprite must have a night-grade-compatible palette; the dorm scene applies a global multiply and no sprite may resist it

---

## ✨ Sprite Sheet 7: Effects — Flicker, Snore & Passive Aggression
**File:** `hostel_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #F5F5DC, #232A3A, #E8D44D, #8B7355

### Light & Sleep:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fluorescent Flicker Frame 1 | (0, 0) | 64x64 | Reception, malfunctioning, permanent |
| Fluorescent Flicker Frame 2 | (64, 0) | 64x64 | Flicker variant |
| Broken Lamp Warm Pool | (128, 0) | 64x64 | "Atmospheric" common-room lighting, i.e. broken |
| Harsh Dorm Overhead | (192, 0) | 64x64 | Always too bright, no dimmer |
| Bathroom Questionable Light | (256, 0) | 64x64 | Greenish. Unflattering. Honest. |
| Snore Visualization Frame 1 | (320, 0) | 64x64 | Character-parented, sawtooth waveform |
| Snore Visualization Frame 2 | (384, 0) | 64x64 | Waveform variant, different NPC signature |
| Phone Screen Glow | (448, 0) | 64x64 | Faces lit from below in the dark |

### Disruption & Ambience:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| 5 AM Alarm Buzz Ring | (0, 64) | 64x64 | Expanding ring from Takeshi's phone |
| Bathroom Steam | (64, 64) | 64x64 | Someone got the hot shower |
| Dust Motes | (128, 64) | 64x64 | Reception and common room |
| Passive-Aggressive Energy Shimmer | (192, 64) | 64x64 | Faint yellow field around the note walls |
| TV Static | (256, 64) | 64x64 | Dutch news, or the absence of it |
| Vending Machine Hum Glow | (320, 64) | 64x64 | 4 Sovs water, illuminated, always on |
| Bunk Creak Impact | (384, 64) | 64x64 | Movement detection, one-shot per shift |
| Fridge Door Light | (448, 64) | 64x64 | Kitchen, night, someone is in the yogurt |

### Grades & Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reception Cold Wash | (0, 128) | 128x128 | Full-scene fluorescent multiply plate |
| Dorm Harsh Wash | (128, 128) | 64x64 | Daytime dorm grade |
| Kitchen Morning Wash | (192, 128) | 64x64 | The only warm light in the building |
| Bathroom Damp Wash | (256, 128) | 64x64 | Humid, green-tinged |
| Common Room Sad Wash | (320, 128) | 64x64 | Broken-lamp grade |
| Snore Glyph | (384, 128) | 32x32 | Mirrors the constant multi-source snoring |
| Alarm Glyph | (416, 128) | 32x32 | Mirrors the 5 AM alarm |
| Toilet Flush Glyph | (448, 128) | 32x32 | Mirrors the every-twenty-minutes overnight flush |
| Creaky Bunk Glyph | (480, 128) | 32x32 | Mirrors bunk movement |
| Muffled EDM Glyph | (128, 192) | 32x32 | Mirrors Shamsterdam being awake outside |
| Dish Scrub Glyph | (160, 192) | 32x32 | Mirrors aggressive morning washing-up |
| Key Jingle Glyph | (192, 192) | 32x32 | Mirrors the oversized keychain |
| Locker Open Glyph | (224, 192) | 32x32 | Mirrors locker metal |
| Shower Gasp Glyph | (256, 192) | 32x32 | Mirrors somebody discovering the water temperature |
| Static Flicker (Reduced Motion) | (288, 192) | 64x64 | Steady fluorescent substitute |
| Static Snore (Reduced Motion) | (352, 192) | 64x64 | Waveform held on frame 1 |
| Static TV (Reduced Motion) | (416, 192) | 64x64 | Frozen screen, no static crawl |
| Reserve | (480, 192) | 32x64 | Reserved cell, do not paint |

### Technical Notes:
- Snore Visualization is character-parented and each sleeping NPC gets a distinct waveform signature — the player learns to identify Nigel by shape alone
- The 5 AM Alarm Buzz Ring must be visible even in the darkest night grade; it is the location's signature running gag and cannot be lost to the multiply plate
- Passive-Aggressive Energy Shimmer is an extremely low-amplitude yellow field, on the edge of perception, applied only near note clusters
- No screen-space shake anywhere; all disruption is communicated by parented overlays and glyphs

---

## 🧭 Sprite Sheet 8: UI Elements
**File:** `hostel_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #4169E1 UI chrome, #D4C5A9 panel fill, #E8D44D warnings

### Check-In & Rooms:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Room Selection UI | (0, 0) | 256x128 | 12-Bed 35 Sovs / 4-Bed "Private" 55 Sovs / Actual Private 85 Sovs / THE BUNK |
| "Fully Booked" Stamp | (256, 0) | 128x64 | Lands on Actual Private. Every time. Always. |
| Deposit Panel | (384, 0) | 128x64 | 20 Sovs key + 50 Sovs damage, neither of which you will see again |
| Check-In Panel | (256, 64) | 256x64 | Passport, deposit, room, "bed... whichever one is empty" |

### Sleep System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sleep Quality Meter | (0, 128) | 128x64 | Restful / Disturbed / What Sleep? / The Snorer Night |
| Sleep Quality Dice Roll UI | (128, 128) | 128x64 | The overnight roll, visible, honest, merciless |
| Disruption Event Popup | (256, 128) | 256x96 | What woke you: alarm / snorer / couple / thief / fire alarm / your own bunkmate |
| Sleep Disruption Table | (0, 192) | 256x96 | Six event types with their probability weights shown |

### Facilities & Social:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bathroom Line Timer | (256, 224) | 128x32 | 5-15 minute countdown, skippable via Bravado check |
| Shower Quality Indicator | (384, 224) | 128x32 | Hot water availability; the good shower is learned after two nights |
| Kitchen Gossip Bubble | (256, 256) | 256x96 | Overheard conversation UI delivering location hints and quest clues |
| Fridge Politics Panel | (0, 288) | 256x96 | Your shelf / communal shelf / unlabelled / labelled-with-threat safety percentages |
| Bulletin Board UI | (0, 384) | 256x96 | Scrollable flyer list with real quest hooks mixed into the noise |
| Wi-Fi Password Note UI | (256, 352) | 128x32 | "everything" |
| ICQ / Mom Message Chip | (384, 352) | 128x32 | Hostel network triggers the check-in with increasing concern |
| Bravado Check Panel | (256, 384) | 256x64 | Line cutting / kitchen story exaggeration / fridge territory dispute |

### Status & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Status Icon Row | (256, 448) | 128x32 | Four 32x32: Exhausted / Rested / Fridge-Safe / Marked |
| High-Contrast Bed Marker | (384, 448) | 64x32 | Bold outline for the bed interaction (save point) |
| Bunk Silhouette Set | (448, 448) | 64x32 | Standard bunk vs. THE BUNK as labelled stepped silhouettes |
| Touch-Zone Guide Overlay | (0, 480) | 256x32 | Dev-only 44px minimum overlay, stripped at build |
| Reserve | (256, 480) | 256x32 | Reserved strip, do not paint |

### Technical Notes:
- The Sleep Quality Dice Roll UI shows the actual roll and the actual modifiers; the system is transparent because the comedy comes from the odds, not from concealment
- Fridge Politics Panel shows explicit percentages (85% / fair game / 50% / 95%) as text, not as a colour bar
- Bulletin Board UI mixes three real quest hooks into roughly a dozen flyers; hooks are distinguished by an interaction affordance, never by colour
- Every room option, flyer, and Bravado choice renders at 44px+ touch height

---

## 🎬 Animation Specifications

### Reception Fluorescent Flicker (Sheet 7):
- **Duration:** 0.3-second burst at irregular intervals averaging every 12 seconds
- **Frames:** 2, played 1-2-1 with a randomised gap
- **Pattern:** Continuous while the reception scene is loaded
- **Trigger:** Constant
- **Purpose:** The first thing you see, malfunctioning, and nobody has ever mentioned it
- **Audio Sync:** Faint ballast buzz on each burst
- **Mobile Optimization:** Low LOD uses the static flicker plate (profile requirement: simplified lighting flicker); disabled in reduced-motion mode

### Snore Cycle (Sheets 6 & 7):
- **Duration:** 3.2 seconds per cycle per sleeper
- **Frames:** 2 waveform frames, per-NPC signature shape
- **Pattern:** Continuous overnight; multiple sleepers run out of phase, deliberately never syncing
- **Trigger:** Overnight dorm scene with any sleeping NPC present
- **Purpose:** Two-plus sources, varying intensity, permanently out of step
- **Audio Sync:** Each waveform shape maps to a distinct snore sample; Nigel's is the loudest and the most recognisable
- **Mobile Optimization:** Low LOD uses the static snore plate (profile requirement: simplified snoring visualization) and caps audible sources at two

### The 5 AM Alarm (Sheets 4, 6, 7, 8):
- **Duration:** 4.0 seconds (0.4s buzz ring expand, 3.2s persistence, 0.4s fade) repeating every 9 minutes until manually dismissed
- **Frames:** 2 phone-buzz frames + expanding ring + Takeshi Sleeping Through Alarm
- **Pattern:** Repeats. He does not wake. Everyone else does.
- **Trigger:** 5 AM game clock, high probability per night
- **Purpose:** The location's defining running gag
- **Audio Sync:** Alarm tone at 0.0s of each repetition; Takeshi's apology plays at 8 AM in the kitchen, not at 5 AM
- **Mobile Optimization:** Ring expand reduced to a static pulse on Low LOD; the sound and the disruption event are never cut

### Sleep Quality Roll (Sheets 4 & 8):
- **Duration:** 2.4 seconds (0.8s dice tumble, 0.4s settle, 1.2s result + disruption popup)
- **Frames:** Sleep Quality Dice + meter fill + Disruption Event Popup
- **Pattern:** One-shot per night slept
- **Trigger:** Sleeping in any bed (also the save point)
- **Purpose:** Save your game, gamble your stats — the tactical tension of the entire location
- **Audio Sync:** Dice rattle 0.0-0.8s; result tone at 1.2s; the disruption's own sound cue at 1.6s
- **Mobile Optimization:** Dice snap to result in reduced-motion mode; the meter still fills

### The Kitchen Confessional (Sheets 6, 7, 8):
- **Duration:** Rolling; gossip bubbles surface every 6-10 seconds while the player remains in the kitchen between 7-10 AM
- **Frames:** Kitchen Morning Block + Kitchen Gossip Bubble + Brittany Mid-Story
- **Pattern:** Continuous ambient dialogue delivery with hint payloads
- **Trigger:** Entering the kitchen in the morning window after any night out
- **Purpose:** The exposition engine — location hints, quest clues, price warnings, and NPC connections all arrive here
- **Audio Sync:** Overlapping morning chatter bed; the current speaker's line rises above it
- **Mobile Optimization:** Kitchen Morning Block reduces to three visible figures on Low LOD (profile requirement: reduced NPC count)

### Bathroom Queue (Sheets 6 & 8):
- **Duration:** 1.6-second shuffle cycle per queued NPC, phase-offset
- **Frames:** 2 (Bathroom Queue Shuffle Strip)
- **Pattern:** Continuous during the 7-9 AM rush
- **Trigger:** Morning bathroom scene
- **Purpose:** Five to fifteen minutes of real waiting, visualised as collective weight-shifting
- **Audio Sync:** Occasional shower gasp from behind a door; a flush every twenty seconds
- **Mobile Optimization:** Queue caps at four visible figures on Low LOD

### THE BUNK Assignment (Sheets 3 & 8):
- **Duration:** 2.0 seconds (0.6s camera settle on the bunk, 1.4s detail hold)
- **Frames:** THE BUNK detail + mysterious stain + draft source
- **Pattern:** One-shot on assignment
- **Trigger:** Selecting or being assigned THE BUNK
- **Purpose:** Everyone knows which one. Now you know which one.
- **Audio Sync:** A faint draft whistle that is present nowhere else in the building
- **Mobile Optimization:** None needed (one-shot)

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Bed Marker | Sheet 8 (384, 448) | 64x32 | Bold outline for the bed interaction, which is also the save point |
| Bunk Silhouette Set | Sheet 8 (448, 448) | 64x32 | Standard bunk vs. THE BUNK as labelled stepped silhouettes |
| Yusuf High-Contrast Silhouette | Sheet 5 (0, 416) | 64x96 | Enhanced-visibility outline of the check-in NPC |
| Ingrid High-Contrast Silhouette | Sheet 5 (64, 416) | 64x96 | Enhanced-visibility outline of the check-out NPC |
| Maria High-Contrast Silhouette | Sheet 5 (128, 416) | 64x96 | Enhanced-visibility outline of the housekeeping NPC |
| Accessibility Reserve Block | Sheet 5 (256, 416) | 256x96 | Overflow space for additional high-contrast variants |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Flicker | Sheet 7 (288, 192) | 64x64 | Steady fluorescent substitute at reception |
| Static Snore | Sheet 7 (352, 192) | 64x64 | Waveform held on frame 1 for all sleepers |
| Static TV | Sheet 7 (416, 192) | 64x64 | Frozen screen with no static crawl |
| Static Alarm Pulse | Sheet 7 (0, 64) | 64x64 | Non-expanding ring; the alarm remains fully legible |
| Snapped Dice Roll | Sheet 8 (128, 128) | 128x64 | Dice show the result immediately without tumbling |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Snore Glyph | Sheet 7 (384, 128) | 32x32 | Mirrors constant multi-source snoring, one glyph per active sleeper |
| Alarm Glyph | Sheet 7 (416, 128) | 32x32 | Mirrors the 5 AM alarm; persists for the full 4-second repetition |
| Toilet Flush Glyph | Sheet 7 (448, 128) | 32x32 | Mirrors the overnight flush every twenty minutes |
| Creaky Bunk Glyph | Sheet 7 (480, 128) | 32x32 | Mirrors bunk movement, including the player's own |
| Muffled EDM Glyph | Sheet 7 (128, 192) | 32x32 | Mirrors the city outside |
| Dish Scrub Glyph | Sheet 7 (160, 192) | 32x32 | Mirrors aggressive morning washing-up |
| Key Jingle Glyph | Sheet 7 (192, 192) | 32x32 | Mirrors the oversized keychain, in and out of the location |
| Locker Open Glyph | Sheet 7 (224, 192) | 32x32 | Mirrors locker metal; doubles as the thief-event tell |
| Shower Gasp Glyph | Sheet 7 (256, 192) | 32x32 | Mirrors somebody discovering the water temperature |

### Colorblind Considerations:
- Sleep quality tiers use four named text labels plus distinct meter segment counts, never a red-to-green gradient
- Fridge safety uses explicit percentage text (85% / fair game / 50% / 95%) plus shelf silhouettes
- Disruption events are identified by named text and a distinct glyph per type, never by colour-coded popups
- THE BUNK is identified by its stain shape, its position, and a text label — not by tint
- Bulletin board quest hooks are distinguished by an interaction affordance icon, never by flyer colour
- Status effects use distinct silhouettes: drooping eyelid (Exhausted), open eye (Rested), labelled shelf (Fridge-Safe), tag (Marked)
- Touch zones minimum 44px for room options, bulletin flyers, Bravado choices, and the bed interaction

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (fallback PVRTC 4BPP); all passive-aggressive notes, bulletin flyers, House Rules poster, TripAdvisor sticker, deposit receipt, check-out slip, and all portraits at ASTC 4x4
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for both room sheets (the night dorm grade and the fluorescent wash both band under lossy compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| hostel_environment | hostel_exterior_fixtures | 1024x1024 |
| hostel_characters | npc_hostel_staff, npc_hostel_guests | 1024x1024 |
| hostel_fx_ui | hostel_objects, hostel_effects, hostel_ui | 1024x1024 |

*(The two room sheets load and unload as paired-room units — only one is resident in normal play. Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Irregular fluorescent flicker, per-NPC snore waveforms out of phase, expanding alarm ring, TV static crawl, dust motes, bathroom steam, full queue and kitchen blocks, tumbling dice |
| Medium | Flicker retained, snore waveforms capped at three sleepers, TV static at half rate, dust motes in reception only |
| Low | Static flicker (profile requirement), static snore visualization (profile requirement), reduced dorm NPC count (profile requirement), static TV, no dust motes, snapped dice |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 38 MB maximum
- **Particle Limit:** 14 (dust motes, bathroom steam, alarm ring motes)

### Performance Notes:
- Paired-room streaming keeps typical resident footprint at ~15.2 MB (one room sheet + all atlases); theoretical all-resident worst case is ~25.2 MB, comfortably inside budget
- Kitchen Morning, Bathroom Queue, Common Room Slump, and Bros Trio all render as pre-composed single blocks
- Sleeping guests share one AnimatedSprite2D texture with per-instance palette modulation and phase offset — one material, N instances
- The dorm night grade is a single multiply quad, not per-sprite tinting
- Passive-aggressive note variants are sampled at scene load, not per-frame

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (room backgrounds, fixtures, notes), AnimatedSprite2D (flicker, snore overlays, alarm ring, TV static, staff), CPUParticles2D (dust motes, bathroom steam — not GPU), CanvasLayer (room selection, sleep roll, gossip bubbles, bulletin board), Area2D (reception desk, each bed, fridge, bulletin board, bathroom doors, vending machine)
- Special systems: sleep quality roll with weighted six-event disruption table, save-point coupling on the bed interaction, kitchen gossip pool with hint payload tagging and rotation, fridge politics ownership model with labelling modifier, bathroom queue timer with Bravado skip, bulletin board hook injection, Wi-Fi network flag triggering ICQ conversations, three-strike noise violation counter with flexible enforcement, "Regular" status at 3+ nights, deposit deduction calculator

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Fluorescent flicker burst | Ballast buzz | Per burst, ~every 12s |
| Snore waveform per sleeper | Distinct snore sample per NPC signature | Continuous, out of phase |
| 5 AM alarm ring | Alarm tone | 0.0s of each 9-minute repetition |
| Bunk creak impact | Frame creak | On any bunk movement, including the player's |
| Dice tumble | Rattle | 0.0-0.8s of sleep roll |
| Sleep result | Result tone, then the disruption's own cue | 1.2s / 1.6s |
| Locker open | Metal scrape | On locker interaction; also the thief-event tell |
| Shower door | Gasp from behind it | Random during the morning rush |
| Overnight ambient | Toilet flush | Every ~20 minutes of night time |
| Key interaction | Oversized keychain jingle | Per use, in and out of the location |
| Morning kitchen | Aggressive dish scrubbing bed | Continuous 7-10 AM |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Sleep Quality / Save Point | Bed interaction, dice roll UI, sleep meter, disruption popup | Sleeping saves the game and rolls the night; tactical tension between safety and rest |
| The Kitchen Confessional | Kitchen Morning Block, gossip bubble, Brittany frames | 7-10 AM hint delivery: location tips, quest clues, price warnings, NPC connections |
| Fridge Politics | Fridge fixture, note variants, fridge politics panel, contested yogurt | Labelling raises safety from 50% to 95%; territory disputes are Bravado checks |
| Bulletin Board Hooks | Bulletin board fixture and UI, three flyer variants | Taxi share, lost camera at Wandelpark, travel documentary interview (Chadwick very interested) |
| THE BUNK | THE BUNK detail, stain, draft source, bunk silhouette set | Worst position in the dorm; surviving a night grants Bravado and costs HP |
| Wolf's "Better Spot" (Couchsurf) | Wolf frames and portrait | Complaining to Wolf unlocks a significantly worse accommodation option and a 15 Sovs "utilities" debt |
| The Locker Suspect | Locker Suspect frames, locker row, locker open glyph | Low-probability overnight theft if no 8 Sovs lock was purchased |
| ICQ / Mom Check-In | Wi-Fi note UI, ICQ chip | Hostel network triggers escalating parental concern messages |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Café de Schaamte | Exhausted status carried into the espresso scene | Hostel war stories over coffee; sleep quality visibly affects the player sprite |
| De Groene Gids | Common room disruption state; "supplies" prop in the dorm | Returning with supplies raises the noise-violation counter |
| Casa Rosé | Kitchen Morning Block gossip payload | Morning-after processing happens at the kitchen table |
| FEBO Automat | Oversized hostel key prop visible on 3 AM returns | Late-night snack acquisition on the walk back |
| Leeman's Döner Palace | Wolf's "tell him Mehmet Wolf sent you" gossip line | Mehmet's Silent Judgment Hold frame plays on that exact line |
| Proeflokaal 't Kansen | Sawdust-Dusted Clothing overlay persists until the next sleep | Kitchen gossip references "the place with the sawdust" |
| The Hemp Museum | Gift Shop Bag prop visible in dorm and kitchen | The Cultural Alibi can be challenged at the kitchen table |
| Venustempel (Museum Mile) | Photo album privacy flag; Sharing the Love stack decay on rest; Tier 5 bathroom-queue event | Venus Temple *interior* photos cannot be shown to Ingrid; fountain exterior photos are unflagged and freely shared. A full night's sleep removes 2 Sharing the Love stacks. At Tier 5 (Shamsterdam Stomach) the dorm bathroom-queue event fires on the next rest — needs a queue-outside-the-bathroom-door ambient composition. |
| The Pancake House | Expectation Adjustment status | "Did they explain before you ordered?" changes the exchange |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Tolerance as a business model — everything is permitted and nothing is comfortable"
- **Color Mood:** Hostel beige and stain brown under fluorescent wash, punctuated by budget blue plastic and notice-yellow hostility — institutional, worn, weirdly warm only in the kitchen
- **Lighting:** Malfunctioning fluorescent at reception, broken "atmospheric" lamps in the common room, merciless overhead in the dorm, greenish damp in the bathrooms, and one genuinely pleasant window of morning light in the kitchen
- **Texture:** Sticker-layered plexiglass, cold bunk metal, sagging mattresses, laminated multilingual signage, accumulated sticky-note paper, worn floor marks

### Environmental Storytelling:
- The key rack has visible gaps, which means several rooms currently have three keys in circulation
- The world map's pins are mostly in the wrong countries and nobody has corrected a single one
- The Polaroid wall is titled "Tolerance Family" and every person in it is wasted
- The microwave's ceiling explosion has been there long enough to have a shape people recognise
- The bathroom queue marks are worn into the floor, not painted on
- THE BUNK's draft comes from a visible gap in the wall behind it that has never been mentioned by anyone
- The peanut butter predates the current staff

### Character Integration Notes:
- Yusuf's default state is working on something that is not hostel business; the laptop glow should be in almost every frame he appears in
- Ingrid has the narrowest expression range of any NPC in the location, and it still communicates more judgment than anyone else's
- Maria never faces the player while working; she is authored to move past them
- Nigel is genuinely sorry every single morning and this must read as sincere, which makes it worse
- Wolf's gatekeeping posture should be immediately recognisable in silhouette from across the common room
- The Couple Who Forgot are always mid-whisper and never acknowledge the room

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **THE BUNK** — bottom corner, stain, visible draft gap, and a sagging mattress, all in one frame
2. **The Passive-Aggressive Note Wall** — an entire ecosystem of escalating hostility in eight languages
3. **The 5 AM Alarm** — Takeshi asleep, the ring expanding, and eleven other people awake
4. **The Sleep Quality Dice** — the actual odds, shown honestly, before you commit to the night
5. **The "Tolerance Family" Polaroid Wall** — everyone wasted, permanently, on the lobby wall

### Quote Potential:
- "The Wi-Fi password is 'everything.' Yeah, lowercase, one word. Like we tolerate everything. Get it?"
- "Breakfast is 7 to 10. It's bread. And whatever's in the jar. I don't ask about the jar."
- "Noise complaint? I'll... look into it."
- "Check-out is 10 AM. You are... an hour late. This is normal for your room."
- "You're leaving review? How nice. We have 3.4 stars. This is fine. Everything is fine."
- "Come back soon. Or don't. We are always here. The tolerance never ends."
- "Sorry mate, was I snoring again? The lads say I'm brutal. Nothing I can do really. Sleep well though?"
- "I am so sorry about alarm. Tomorrow I will fix."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | hostel_rooms_a.png | 2048x1024 |
| 2 | hostel_rooms_b.png | 2048x1024 |
| 3 | hostel_exterior_fixtures.png | 1024x1024 |
| 4 | hostel_objects.png | 512x256 |
| 5 | npc_hostel_staff.png | 512x512 |
| 6 | npc_hostel_guests.png | 1024x256 |
| 7 | hostel_effects.png | 512x256 |
| 8 | hostel_ui.png | 512x512 |

**Total Estimated Memory:** ~15.2 MB typical resident (one room sheet + all atlases); ~25.2 MB theoretical all-resident worst case. Within the 38 MB location budget.

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `hostel_rooms_a.png` (2048x1024)
- [ ] `hostel_rooms_b.png` (2048x1024)
- [ ] `hostel_exterior_fixtures.png` (1024x1024)
- [ ] `hostel_objects.png` (512x256)
- [ ] `npc_hostel_staff.png` (512x512)
- [ ] `npc_hostel_guests.png` (1024x256)
- [ ] `hostel_effects.png` (512x256)
- [ ] `hostel_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + room-pair streaming diagram + full passive-aggressive note copy sheet (six variants, all languages) + snore waveform signature key per NPC

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#D4C5A9, #4169E1, #F5F5DC, #8B7355, #E8D44D, #232A3A)
- [ ] Key gags read clearly: THE BUNK identifiable from the doorway without UI, the gapped key rack, the wrong-country map pins, the microwave ceiling explosion, the worn bathroom queue marks, the draft gap in the wall
- [ ] All note and signage text is legible at gameplay zoom on a 5-inch display
- [ ] The dorm night grade preserves the 5 AM alarm ring's legibility
- [ ] Accessibility visual alternatives included for all audio cues (snore, alarm, flush, bunk creak, EDM, dish scrub, key jingle, locker, shower gasp)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (targets are hostel economics, budget-travel romanticism, and backpacker gatekeeping — not budget travellers or hospitality workers)
- [ ] Staff read as fellow exhausted travellers, not villains
- [ ] Hidden areas/interactions have discoverable visual cues (the good shower, THE BUNK, bulletin board hooks, the labelled fridge shelf)
- [ ] Mobile performance optimized (paired-room streaming, CPU particles, atlas limits respected, static flicker/snore fallbacks, reduced dorm NPC counts)
- [ ] Touch zone sizing considered (44px minimum for room options, flyers, Bravado choices, and the bed)
- [ ] Colorblind-friendly alternatives available where color codes meaning (named sleep tiers, percentage text on fridge safety, glyph-coded disruption events)
- [ ] Social media viral potential maximized in composition choices (THE BUNK framing, note wall readability, alarm-ring staging, dice odds transparency)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam Canal Ring Promenade; guest backstories reference Manchester and San Diego as origins, never Shamsterdam by another name |
| Cultural Specificity | ✅ | Amsterdam hostel culture, cannabis-tourist clientele, canal house architecture, Dutch day-manager directness |
| Satirical Targets Appropriate | ✅ | Budget-travel romanticism, party-hostel economics, backpacker gatekeeping — never budget travellers or hospitality staff themselves |
| Seedy Underbelly Present | ✅ | Selling community while profiting from discomfort; 50 Sovs "deposit" that is a fee; 8 Sovs locks at 3x market; the always-"fully booked" private room |
| Gameplay Value Established | ✅ | Save point coupled to a sleep-quality gamble, six-event disruption table, kitchen hint delivery, fridge politics, bathroom queue, bulletin hooks, ICQ trigger, couchsurf branch |
| Technical Feasibility | ✅ | Paired-room streaming, static flicker/snore fallbacks per profile, reduced dorm NPC counts per profile, pre-composed group blocks |
| Mobile Performance Budget | ✅ | 60 FPS, 16 draw calls, 38 MB, 14 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all nine audio cues, reduced-motion set including a non-expanding alarm ring, named sleep tiers, 44px touch zones |
| No Crypto Elements | ✅ | Pure hostel chaos; the only unrecoverable deposit is the 50 Sovs damage one |
| Social Media Integration | ✅ | 5 screenshot moments + 8 quotable lines identified |

**Once these assets ship, The Tolerance Hostel becomes the game's most honest room: 35 Sovs gets you a bed, a save point, and a dice roll; the notes on the fridge tell you everything about everyone who has slept here; and somewhere in the bottom corner, drafty and stained and known to all, THE BUNK is waiting to see how much Bravado you actually have.**
