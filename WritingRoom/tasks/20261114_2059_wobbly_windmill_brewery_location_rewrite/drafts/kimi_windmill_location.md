# Kimi — Slice A: Wobbly Windmill Brewery location rewrite
**Scope:** `wobbly_windmill_brewery.md` lines 1–147 (identity, Visual Design, Satirical Design), 259–336 (NPCs, patrons, bro reactions), 361–379 (Audio), plus new "Interactables & Props (four-layer rule)" section.
**Reviewer:** Aion (primary — bro lines, delusion check). Deepseek to spot-check Hendrik/Tessa/Bram dialogue so his NPC rewrite matches.
**Ruled facts kept verbatim:** all IDs, hours, prices, opener/stamp mechanics, Hendrik's Opener Check dialogue, Yeast Golem, tasting flight + Spin Meter, Brewmaster's Speech, Selfie Spot, Windmill Grist (never sold), Canal Courage progress. All numbers untouched.
**Sign wording:** the main sign, machinery sign (English + pictograms per vuqj-q4) and queue/gift-shop sign are Aion's slice D. Placeholder wording below is marked [AION SIGN SHEET]; final text comes from `drafts/aion_windmill_signs.md`.

**Integration flags (out-of-slice lines the final pass must fix or escalate):**
- System Integration (~l.338–360): "Dutch drinking culture", "extremely organized German apartment" — real nationality words, must be rewritten in integration.
- Gameplay Mechanics (~l.148–258): Bradley's "We should use fire." is a competent tactical call from a bro (sane-one risk). Flag for integration: propose swapping to a doofus version.
- QA checklist + Marketing (~l.420+): "Dutch windmill heritage", "Dutch windmill tourism" — rewrite in integration.
- Pre-existing mismatch: PNG sprite `eva_tour_guide.png` vs. NPC "Tour Guide Tessa". Filenames stay (ruled). Note only.

---

## Replacement: header tagline (line 3)

*Where 350 years of stubborn wood learned to brag — queue rope, turnstile, screaming signage, and a tasting flight that spins the room twice*

## Replacement: Location Identity (lines 5–13)

- **Location ID**: shamsterdam_countryside_wobbly_windmill_brewery_01
- **Display Name**: The Wobbly Windmill Brewery
- **English Translation**: "The Windmill Brewery"
- **Satirical Subtitle**: "Respect The Grain. Fear The Spin."
- **World Location**: Shamsterdam
- **Area Zone**: Shamsterdam Countryside (short train ride from central)
- **Location Type**: Brewery Tour Location #1 / Working Windmill / Mini-Dungeon

## Access & Requirements (lines 15–55)

Keep every mechanic, price, opener spec and line of Hendrik's Opener Check dialogue exactly as-is. Two descriptive touch-ups only:

- **Special Conditions**: Must take short "scenic" train ride from central Shamsterdam (8 SOVS round trip, views are... fields)
- **Entrance** (in Visual Design below): the accessibility ramp is "a legal requirement, and there is a sign taking credit for it."

---

## Replacement: Visual Design (lines 57–122)

- **What this building exaggerates (readable at thumbnail size)**: A windmill wearing a tourist trap — a backlit "WOBBLY WINDMILL" sign wider than the door, queue rope and turnstile on the path, hazard tape and zip-tied gears visible through every window, merch stacked in every sightline.

### Exterior Description
- **Approach**: Flat countryside, windmill visible from the train platform — audible before that. Blade whoosh, a gear that rattles on every third pass, and retail radio leaking out of a building with no neighbours to complain to. Tourists are already photographing it from the platform, which is the last free angle.
- **Structure**: Actual working windmill (circa 1680), converted to brewery (circa 2008), Instagram magnet (circa always). The cap and sails are the real thing; everything below the balcony line is signage, merch racks and hazard tape. The wood is old the way a bar floor is old: dark, swollen, and holding.
- **Entrance**: Heavy wooden door at the windmill base, "BREWERY" carved above it and a backlit plastic sign above THAT, because carving doesn't glow. Modern accessibility ramp (a legal requirement, and there is a sign taking credit for it). A turnstile just inside the door. It counts you.
- **The Queue**: A switchback of retractable-belt queue poles on the path, deployed every day regardless of demand. A laminated standing sign planted two metres from the door: "WAIT FROM HERE: 45 MIN." [AION SIGN SHEET — queue/gift-shop sign option]
- **Signage**:
  - Main sign [AION SIGN SHEET — main sign]. Placeholder: backlit plastic, letters a foot high, two flickering — "THE WOBBLY WINDMILL BREWERY — EST. 1680 / 2008 / FOREVER."
  - Below it, a peeling laminated sandwich board: "CRAFT BEER TOURS — TASTING FLIGHTS — GIFT SHOP."
  - Warning placard, bolted, hazard-yellow: "WINDMILL OPERATIONAL — BLADES ROTATE — WATCH HEAD."
  - Smaller sign under that: "The spinning is intentional. The dizziness is not our fault."
  - A plywood photo cutout of a beer mug with three face holes, paint worn off at the chin rests.
  - A vending machine against the wall: motion-sickness pills, phone cables, earplugs. The earplug slot is empty and has been for some time.
- **Atmosphere**: Grain dust on everything, including you. The bin by the door overflows with tasting cups. The whoosh is genuinely impressive and the gift shop is genuinely visible through every window.
- **Environmental Context**: Other tourists waiting for the same train back, comparing tasting notes, holding onto the platform bench.

### Interior Visuals — Ground Floor (Welcome/Shop)
- **Layout**: Round room (it's a windmill), reception desk dead ahead, gift shop cramming every surface, queue rope switchbacking between the door and the till even when the room is empty. Especially when the room is empty.
- **Lighting**: Grey daylight through small windows, two caged utility bulbs on a sagging cord, and one buzzing amber neon "GRAIN" sign over the till that exists because the merch needed a mood.
- **Furniture & Props**:
  - Turnstile at the door (it counts you; a small digital counter on the till displays the number like a high score).
  - Reception desk built from reclaimed barrel wood (claimed), card reader taped over with a handwritten note: "CASH ONLY. READER IS BROKEN. YES, STILL."
  - A CCTV dome in the rafters, blinking red, aimed at the merch.
  - An empty hand-sanitizer pump bolted to the desk, label peeling.
  - Display cases of bottled products (available in gift shop, also reception, also bar, everywhere).
  - "Windmill History" panels (5% about windmill, 95% about beer), laminated, corners lifting.
  - Coat hooks (for the tasting flight aftermath).
  - A support pole covered in stickers from every tour operator that has ever existed, layered like geology.
- **The Gift Shop Section**:
  - The same windmill mug in three sizes, each size labelled a different "edition."
  - "Wobbly Windmill" branded glasses, 18 SOVS (the beer is 6 SOVS).
  - Miniature windmill souvenirs, 25 SOVS (made overseas, painted here — the paint is still tacky on the bottom row).
  - Brewmaster's book: "Respect The Grain" 35 SOVS (self-published, unreadable, a display copy furred with grain dust).
  - T-shirts: "I SURVIVED THE SPIN" 30 SOVS (they know).
  - A laminated placard at the till: "NO REFUNDS. THE SPINNING IS ON THE WEBSITE."
  - The "Survivor Pack" display by the till: motion-sickness pills (3 SOVS), water (2 SOVS), both (5 SOVS). It is the most-stocked shelf in the building.

### Interior Visuals — First Floor (Brewing Operations)
- **Layout**: Circular, dominated by the massive central grinding mechanism connected to the windmill, with a ring of hazard tape on the floor marking how close the lawyers will allow.
- **Key Feature**: THE GRINDING FLOOR — the windmill actually works, grain actually grinds, floor actually vibrates. One gear guard is held on with zip ties. The zip ties are the newest thing in the building.
- **Lighting**: Dusty grey daylight, a single hard spotlight on the brewing vats, flour haze doing the rest. Nothing glows warmly. The vats glow industrially.
- **Furniture & Props**:
  - Central millstone mechanism (moving when wind blows).
  - Copper brewing vats positioned around the circle, each with a drip pan underneath, each drip pan with a history.
  - Grain storage bins (open-topped, safety concern, one with a scoop handle sticking out like a flag).
  - Massive wooden gears (original, terrifying, functional — the zip-tied guard rattles on every third pass).
  - Windows showing blade rotation outside (disorienting).
  - The machinery sign [AION SIGN SHEET — machinery sign per vuqj-q4: English text plus pictograms — a hand with a red cross, a gear, a skull — so it reads in every language and needs no words but the English header]. Placeholder header: "DO NOT TOUCH MACHINERY."
  - A chalkboard nailed to a post: "DAYS SINCE LAST GOLEM: 0." The zero is chalked with unusual confidence.
  - A fire extinguisher furred with flour, inspection tag dangling.
  - A coin-op earplug dispenser mounted by the stairs, empty, its knob painted shut.
- **The Vibration**: Floor vibrates when grinding, beer in glasses ripples, tourists grab rails. The rails are the most-touched surfaces in the building and feel like it.
- **Yeast Golem Arena**: Center of grinding floor, spawns from grain dust accumulation. The hazard-tape ring has a gap worn in it exactly where the golem rises. Nobody has re-taped it. The tape knows.

### Interior Visuals — Second Floor (Tasting Room)
- **Layout**: Upper windmill level, smaller, tighter, the spinning feeling stronger up here. Barrel tables in a circle around the central shaft, each one covered in a logo-printed plastic tablecloth that is sticky in a way that predates tonight.
- **Lighting**: Grey window light and a fluorescent tube over the chalkboard (one flickering). A row of electric tea lights in plastic cups sits unlit on the shelf — fire code bought them, nobody has turned them on since the grand opening, and the switch is behind the merch. No warm light anywhere; the beer is the warmest colour in the room.
- **Furniture & Props**:
  - Barrel tables (actual barrels, actual rings of spills, one ring with its own brass plaque: "SPILL OF 2019 — LEST WE FORGET").
  - Tasting flight boards (5 beers, escalating ABV, escalating mistake).
  - Brewmaster's "throne" (fancy chair at head table, one armrest re-attached with a strap).
  - Chalkboard with today's offerings and pretentious descriptions ("notes of barnyard, verticality, consequence").
  - Laminated menus, sticky, fanned in a basket that says "PLEASE RETURN."
  - A wall-mounted motion-bag dispenser: "COMPLIMENTARY — TAKE ONE." It is refilled hourly. It is always empty.
  - A phone-charging locker, door zip-tied shut, sign: "OUT OF ORDER."
  - Railings with grip tape worn smooth at hand height.
  - Windows showing countryside (helpful for reorientation).
- **The Spin Effect**: At this height, the rotation is more noticeable. Or is that the beer? A laminated card on every table says: "IT IS BOTH."
- **Selfie Spot**: Window overlooking blades, timing matters, many tourists fail this photo. The glass is smeared with forehead and phone prints at exact standing height. A squeegee hangs from the rail on a chain. The chain is the cleanest thing up here.

### Interior Visuals — Blade Level (Post-Boss)
- **Access**: Unlocked after Yeast Golem defeat.
- **Layout**: Cramped platform just below where blades connect.
- **Danger Level**: Theoretical (rails exist, lawyers insisted, the rail bolts are checked weekly and the checklist is taped to the door, signed in advance through next month).
- **Purpose**: Brewmaster selfie spot — photo with spinning blades behind you.
- **Props**: A floor stencil reading "STAND HERE," scuffed to a smear. An official photo rig (camera on a clamp) zip-tied to the rail, "OUT OF ORDER." A hook labelled "PHONE LANYARDS." The hook is empty. A pictogram wind-warning placard: a hat leaving a head.
- **Wind Factor**: SIGNIFICANT. Hair will be destroyed. Photos will be "dramatic." The lost-and-found bin below the platform contains eleven hats and one toupee. [PROPOSED prop detail — no mechanic; if the toupee is too much, cut it and keep ten hats.]

### Technical Specifications
- **Color Palette**: Primary: Grain Gold (#DAA520), Accent: Copper (#B87333), Background: Windmill Wood (#8B4513), Flour White (#FFFAF0) [hex values untouched, ruled; hue direction is Mistral's PNG pass]
- **Lighting Setup**: Grey daylight, buzzing caged bulbs, hard spotlight on vats, fluorescent flicker (tasting room), neon merch glow (ground floor). No candle-warm or golden-hour light anywhere (vuqj-q3); the only warm hue is the beer itself and the amber neon.
- **Particle Systems**: Grain dust (constant), flour haze, beer foam sparkle.
- **Animation Elements**: Grinding mechanism rotation (with the rattling guard), blade shadows through windows, floor vibration effect, liquid ripple in glasses, turnstile counter tick-up.
- **Performance Optimization**: Simplified grinding animation, reduced dust particles, static blade shadows on older devices.

---

## Replacement: Satirical Design (lines 124–150)

### Theme & Vibe
**Core Concept**: A 350-year-old windmill that still genuinely works, wrapped in the loudest possible tourist machine: queue rope, turnstile, merch stacked to the beams, and a tasting flight sequenced so the building and the beer spin you in opposite directions. The brewmaster preaches grain-reverence in a room with a till in it. Nothing here is fake — the mill grinds, the beer is strong, the dizziness is real — and that is the trick: authenticity with a card reader taped to it. CASH ONLY. The gap between Hendrik's sermon and the Survivor Pack display by the door is the whole building.

### Cultural Targets
- **Primary Satirical Focus**: "Authentic" experience tourism — paying premium to be processed, queued, spun and sold the mug on the way out.
- **Secondary Targets**: Craft beer sermon culture, the brewmaster-as-lifestyle-guru, windmill fetishization, gift shops that sell the same mug three ways.
- **Cultural Specificity**: Shamsterdam windmill tourism meets the craft beer explosion: a real working machine monetized within an inch of its sails.
- **Humor Approach**: The gap between the brewmaster's reverence and the tourist's survival instinct, staged in a building that has productized the survival instinct (motion bags, Survivor Packs, grip-taped rails).
- **Satire Strength**: The house is never the butt of the joke. The mill works. The beer delivers. The target is the tourist who pays 25 SOVS to be queued, counted, spun and upsold — and leaves five-star reviews about how real it felt.

### Seedy Underbelly Elements
- **Primary Vice**: Charging 40 SOVS for a tasting flight in a building engineered to maximize disorientation, with the remedy sold back to you at the till as a bundle.
- **City-Specific Comedy Operations**: The windmill genuinely works, the dizziness genuinely accumulates, the liability waivers are comprehensive, the motion-bag dispenser is refilled hourly and is always empty.
- **Buffoon Exploitation**: Bros think they're having an artisanal experience; they're being queued, counted, spun and sold the same mug in three sizes.
- **Comedy of Errors**: Each beer makes the spinning more noticeable, each floor makes it worse, and every remedy is for sale at the bottom.
- **Consequence System**: "Windmill Grist" consumable has navigation penalty — the spinning follows you.

### Buffoon Delusion Scenarios
**What bros THINK is happening**: Exclusive craft brewery experience in a historic windmill, the kind of place that knows a VIP when one turns up.

**What is ACTUALLY happening**: Being queued, counted by a turnstile, spun by a building and a flight simultaneously, and sold the cure at the till.

**How impaired are they**: Increasingly impaired as the tasting flight progresses; the spinning building does not help, and the building is not trying to help.

**Obvious signs they ignore**:
- The queue rope is deployed for a party of three.
- The turnstile counts them.
- The building is SPINNING.
- The tasting flight goes from 5% to 11% ABV.
- Other tourists holding onto tables.
- The Brewmaster's "Respect The Grain" speech is 40 minutes.
- The motion-bag dispenser is refilled hourly and always empty.
- The gift shop prices suggest they need to recoup something.
- The "DAYS SINCE LAST GOLEM" board says 0.
- The Yeast Golem is MADE OF DUST from this very mill.

**How locals play along**: Hendrik treats everything with deadly seriousness, Tessa catches people for a living, Bram sells the same mug three ways and has stopped noticing the whoosh entirely.

---

## Replacement: NPCs & Vendors (lines 259–336)

### Brewery Staff

**Brewmaster Hendrik**
- **Role**: Tour guide, lecture giver, grain philosopher
- **Appearance**: Barrel-chested, brewmaster's apron over a branded polo, beard that could filter beer. The apron has a name tape. The name tape says HENDRIK, in case the throne was ambiguous.
- **Background**: Third-generation windmill operator, converted to brewing in 2008, takes this VERY seriously
- **Demeanor**: Passionate beyond reason, treats grain like family, disappointed in everyone who doesn't get it. Delivers the same sermon to four people as to forty; the turnstile counts them either way.
- **Dialogue**:
  - "Welcome to The Wobbly Windmill Brewery. For 350 years, this windmill has served the people. For 15 years, it has served the GRAIN."
  - "You feel the floor moving? That is HISTORY. That is the grain becoming BEER. Respect it."
  - "The tasting flight is not a race. It is a JOURNEY. Each beer builds on the last. Do not disrespect the order."
  - "The windmill turns, the grain grinds, the beer brews. This is the cycle. You are now PART of the cycle."
  - "The final beer, the Windmill Grist... this is 15 years of my LIFE in a glass. I hope you are worthy."
  - *after combat* "You have defeated the Golem. It is made of our grain, our yeast, our SOUL. You have earned your place."
  - *new, merch-adjacent* "The book is my philosophy. The mug is a mug. Both are for sale."
  - *new, at the turnstile* "Three hundred today. The grain does not care how many. I care. I care every time."

**Tour Guide Tessa**
- **Role**: Manages tour flow, handles panicking tourists, damage control
- **Appearance**: Young woman, brewery polo, practical shoes (for catching people), a lanyard with a whistle she has never needed to blow because her voice carries over the whoosh.
- **Background**: University student, summer job, has developed excellent reflexes
- **Demeanor**: Cheerfully competent, skilled at redirecting dizzy tourists. Can tell a faller from a leaner at twenty paces and is already moving.
- **Dialogue**:
  - "The tour is about two hours. Yes, the building spins the entire time. There are railings."
  - "If you feel unsteady, please hold the railing. If you feel very unsteady, please tell me. I am trained."
  - "The tasting flight is optional. I mean, it's included in the price, but you can skip— nobody skips."
  - "Hendrik's speech is... comprehensive. There are chairs. The chairs are stable. Mostly stable."
  - "The gift shop has motion sickness remedies. Yes, we sell a lot of them. No, I don't find that funny anymore."
  - *new* "The queue rope is for your safety. The switchback is for the gift shop."
  - *new* "I catch people. That's the job. You're thinking 'surely not that often.' Hold my lanyard."

**Gift Shop Attendant Bram**
- **Role**: Retail, merchandise pushing, post-tour upsell
- **Appearance**: Young man, slightly bored, been here two years, knows the speech by heart, has stopped hearing the whoosh the way you stop hearing a fridge.
- **Position**: Ground floor, unavoidable on entry AND exit
- **Dialogue**:
  - "Welcome to— you're doing the tour first? Okay. See you in two hours. I'll be here. I'm always here."
  - *on exit* "How was the tour? The spinning? Yes. Would you like a branded glass? The flight was in branded glasses. You could buy those glasses."
  - "The book is thirty-five SOVS. Hendrik wrote it. I've read it. I mean, I had to. We all had to. It's... comprehensive."
  - "Motion sickness pills? Three SOVS. Water? Two SOVS. Both? Five SOVS. We call it the 'Survivor Pack.'"
  - *new* "The mug comes in three sizes. They're the same mug. The big one is called the Heritage Edition."
  - *new* "The turnstile counts you in. It doesn't count you out. Hendrik says the out-count is between you and the grain."

### Visitor NPCs (Atmospheric)

**The Beer Blogger (Big-City Paper)**
- **Composition**: Solo, notebook, taking this as seriously as Hendrik
- **Behavior**: Writing tasting notes, nodding during lecture, actually respecting the grain
- **Function**: Shows what the "correct" response looks like, makes bros feel inadequate
- **Dialogue**: "The mouthfeel at 350 years of history... remarkable. You can taste the tradition. You can also taste the till, but that's the terroir now."

**The Bachelor Party (Local)**
- **Composition**: Local group who came for the ABV, staying for the chaos
- **Behavior**: Further along in the flight, significantly more affected, supporting each other literally, one wearing the "I SURVIVED THE SPIN" shirt he bought forty minutes ago, over his other shirt.
- **Function**: Preview of bros in 45 minutes
- **Dialogue**: "The room is— no, HE'S spinning. Wait. Are WE spinning? Johannes, are we spinning?"

**The Instagram Couple**
- **Composition**: Here for the windmill photo, suffering through the tour
- **Behavior**: Already took 300 photos, haven't tried the beer, waiting for selfie spot. She has wiped a circle in the selfie-window grime with a wet wipe. The circle is the size of a phone.
- **Function**: The photo is the point; the brewery is a backdrop with a queue
- **Dialogue** (her): "The AESTHETIC though. Is this authentic? This feels authentic."
- **Dialogue** (him): "Can we skip to the picture part? ...there's more?"

**The Repeat Visitor (Unexplained)**
- **Composition**: Solo older man, been here "many times," knows Hendrik personally
- **Behavior**: Drinks full flight without visible effect, nods through lecture, leaves mysteriously
- **Function**: Suggests some people actually love this, true believers exist
- **Dialogue**: "First time? Ah. Enjoy. Respect the grain."

### Original NPC Dialogue
**Hendrik's Greatest Hits** (during tasting):
- "The first beer teaches you humility. The second teaches you character. The third teaches you why we have railings."
- "My grandfather ground grain in this mill. My father ground grain. I grind grain AND brew beer. Progress."
- "The Yeast Golem was not planned. It emerged from our commitment to natural processes. We are... proud? We are proud."
- "If you do not finish the flight, the grain dies in vain. This is not pressure. This is FACT."
- *new* "The turnstile counted 10,000 guests this year. I remember each one who finished the flight. Both lists exist. Only one is on the wall."

**The Bros' Brewery Reactions:**
- **Lord Pilsner**: "A WINDMILL. A real WINDMILL. This is ICONIC. This is— why is it moving."
- **Lord Pilsner** (queue): "Forty-five minutes is the VIP wait. The regular wait is, like, a day. We look like fast-track guys. The rope knows."
- **Lord Pilsner** (turnstile): "It counted me. That's how they track the VIPs. For the toast at the end."
- **Lord Pilsner** (tasting): "I respect the grain. I RESPECT it. I just also need to sit down."
- **Chadwick** (first floor): "The grinder is GRINDING. Real grain. Real CONTENT."
- **Chadwick** (machinery sign): "The skull means it's famous machinery. You only put a skull on the good stuff."
- **Chadwick** (post-golem): "I fought bread. I have footage of fighting BREAD. This trip is INSANE."
- **Bradley** (tasting): "Actually, this is really good. The spinning adds... something."
- **Bradley** (grinding floor): "The floor's doing the work for you. Vibration training. Gyms charge extra for this."
- **Bradley** (Survivor Pack): "Five SOVS for pills AND water. That's a bundle. We'd be losing money NOT buying it."

---

## Replacement: Audio Design (lines 361–379)

### Environmental Audio (Original Atmosphere)
- **Ambient Soundscape**:
  - Windmill blade whooshing (constant, rhythmic)
  - Grinding mechanism rumbling (first floor), with the rattling zip-tied guard audible on every third pass
  - Wood creaking (the building is old and loud about it)
  - Liquid sloshing (brewing vats)
  - Wind through gaps (blade level)
  - Retail radio (ground floor, local pop station, volume set for a building with no neighbours)
  - The turnstile's click and counter beep (ground floor, irregular)
  - The till, and the receipt printer (ground floor, constant)
  - Fluorescent buzz (tasting room), neon hum (ground floor)
  - Hendrik's voice (echoing through floors)
- **Music Style**: Retail radio downstairs; nothing upstairs but the building and the sermon
- **Audio Transitions**: Louder grinding on first floor, wind at blade level, quieter in tasting room — except the fluorescent buzz, which follows you
- **Interactive Audio**: Beer pouring, toast clinking, camera shutter (selfie spot), turnstile click, queue rope's retractable-belt zip

### Comedy Audio Integration
- **Satirical Stingers**: Room-spin audio effect increasing through the tasting flight; the turnstile beep when a bro walks in like a VIP; the receipt printer running long after the purchase should be over
- **Character Voice Direction**: Hendrik's reverent baritone at retail volume, Tessa's trained-projection efficiency, Bram's flat till-read
- **Environmental Comedy**: Bachelor party stumbling sounds, the blogger's approving murmurs, the queue rope's belt zipping in and out for a party of three
- **Boss Audio**: Yeast Golem rising (bread baking sounds, reversed and slowed)

---

## New section: Interactables & Props (four-layer rule)

Per `design/style_guides/location_interactables_rule.md` (binding, 2026-11-14). Four buckets. Only behaviour the files already rule is stated as fact; anything the rewrite implies but no file rules is tagged [QUESTION FOR AUTHOR] and is not a mechanic. Insert after Audio Design, before Implementation Specifications (mirrors Bottoms Down).

### Interactive objects

| Object | What it does | Quests / flags / items it touches |
|---|---|---|
| **Reception Desk (interaction point)** | Purchase the tour (25 SOVS), receive tasting token; Hendrik's opener check at the threshold (Blarney Trap keychain/opener gate — openers earned, never sold). | Brewery Tour quest; tour flow per Gameplay Mechanics. |
| **Bram's Gift Shop (interaction point)** | Buy merchandise at the ruled prices (glasses 18, mini windmill 25, book 35, shirt 30, Survivor Pack 5, pills 3, water 2 — numbers untouched). Post-tour upsell dialogue per Bram. | Gift-shop inventory; Brewmaster-approval discount (5%) per the Speech reward. |
| **The Grinding Floor (boss trigger)** | Yeast Golem encounter at the center of the first floor, phases and rewards exactly per Gameplay Mechanics. | Windmill Grist x3; "Yeast Slayer" title; Tasting Room + Blade Level unlocks. |
| **Tasting Flight Board (second floor)** | Runs the ruled five-beer flight, Spin Meter accumulation, stop-any-time Bravado check. | Flight table per Gameplay Mechanics; Spin Meter; Canal Courage progress. |
| **The Brewmaster's Speech (Hendrik interaction)** | The ruled 40-minute endurance challenge (2 minutes skippable); leave-early Bravado check. | +Brewmaster Approval; gift-shop discount (5%). |
| **The Selfie Spot (blade level)** | Ruled timing mini-game: blade position, success/failure photos, wind difficulty option. | "Perfect Windmill Shot" / "Unfortunate Windmill Shot"; +Bravado / +Embarrassed. |
| **Blade-Level Door** | Locked. Unlocks after Yeast Golem defeat (ruled). | Blade-level access; Brewmaster selfie. |
| **The Golem Chalkboard** | Examine: "DAYS SINCE LAST GOLEM: 0." The zero is chalked with unusual confidence. | [QUESTION FOR AUTHOR: does the number reset to 0 after each golem defeat and count up on later visits? New room-state behaviour — not assumed.] |
| **The Turnstile** | Examine: "It counts you. The counter on the till says so. Nobody knows what happens at 10,000." | [QUESTION FOR AUTHOR: counter ticks up on entry as a scripted beat? Ambient only until ruled.] |
| **The Motion-Bag Dispenser** | Examine: "COMPLIMENTARY — TAKE ONE. Refilled hourly. Always empty." | None (the remedy is sold, not given — the Survivor Pack is at Bram's till, ruled). |
| **The Spill Plaque** | Examine: "SPILL OF 2019 — LEST WE FORGET. The ring is still sticky. Out of respect." | None. |
| **The Machinery Sign** | Examine: English header plus pictograms — a hand with a red cross, a gear, a skull (vuqj-q4). | None. |
| **The Hat Bin (blade level)** | Examine: "Eleven hats and one toupee, lost to the wind. Claims are processed monthly. There are no claims." | None. |
| **The Phone Lanyard Hook (blade level)** | Examine: "PHONE LANYARDS. The hook is empty. The hook was always going to be empty." | None. |
| **The Queue Rope** | Collision: yes. Examine: "WAIT FROM HERE: 45 MIN. The rope is deployed for a party of three." | None. |

### Pickups

| Pickup | How obtained (ruled) | Quests / flags / items it touches |
|---|---|---|
| **Wobbly Windmill Brewery bottle opener** | Earned, never sold — defeat the Yeast Golem only (ruled). | Bottle Opener Keychain; brewery-tour opener gate elsewhere; the two-stamp gate with Kees at Bottoms Down. |
| **"Windmill Grist" stamp** | Added to the Bottle Opener Keychain per System Integration (ruled). | Brewery Tour progress (1 of 4); Canal Courage passive. |
| **Windmill Grist (consumable)** | Yeast Golem defeat, x3 (ruled). Never sold. | Full effect table per Gameplay Mechanics (numbers untouched, ruled Eurobound-eb8). |

### Notable placed props (separate assets, no interaction)

- **The Brewmaster's Throne** — second floor, strap-repaired armrest. Collision: yes. No interaction declared.
- **Barrel tables + logo tablecloths** — second floor. Collision: yes.
- **Copper brewing vats + drip pans** — first floor. Collision: yes.
- **Grain storage bins (one with scoop)** — first floor. Collision: yes.
- **The official photo rig (OUT OF ORDER)** — blade level, zip-tied to rail.
- **The plywood photo cutout (three face holes)** — exterior path.
- **The vending machine (pills/cables/earplugs)** — exterior wall.
- **The squeegee on a chain** — selfie spot window.
- **Exterior sign assemblies** — backlit main sign (FX: two letters flicker), sandwich board, hazard-yellow blade placard, queue standing sign. Separate assets per the rule's sign-assembly example; final wording from Aion's sign sheet.
- **The CCTV dome; the sanitizer pump; the earplug dispenser; the charging locker** — NPC-anchor-scale props, defined in the PNG doc (Mistral's slice).

### Background-only dressing (bake it)

- Windmill shell: cap, sails, balcony, weather-dark wood below the balcony line.
- The grinding mechanism body and wooden gears (the zip-tied guard is dressing on the mesh; the rattle is an FX layer, not an object).
- Hazard-tape ring on the grinding floor (painted texture; the worn gap is baked).
- Queue poles and retractable belts (the rope's examine trigger above is separate from the mesh).
- Turnstile body (the examine trigger is separate from the mesh).
- Caged bulbs, sagging cords, fluorescent tube, neon "GRAIN" sign assembly (FX: buzz/flicker loop).
- Merch racks, mug pyramids, shirt displays, Survivor Pack shelf, book display (the gift-shop interaction is a till trigger, not the racks).
- "Windmill History" panels, laminated menus, table cards ("IT IS BOTH."), sticker pole, coat hooks.
- Fire extinguisher, motion-bag dispenser body, hand-sanitizer pump, CCTV dome (interior dressing).
- Blade-level rails, bolts, checklist, wind-warning pictogram placard.
- Front entrance door: handled as the map transition; the carved "BREWERY" and sign faces are dressing on it.

---

## Cut list (for the integration pass)

- l.3 tagline ("Where Dutch tradition meets tourist disorientation...") — replaced.
- l.89 "Warm candlelight (electric, fire code)" — banned wording, replaced with fluorescent/unlit tea lights.
- l.83 five-language machinery sign — replaced per vuqj-q4 (English + pictograms).
- l.122 "Sensitivity Considerations" line — cut (ruling).
- l.129 "genuine Dutch heritage weaponized for tourism" — replaced; "Dutch" out of player-facing text.
- All "Dutch" / "German" instances in NPC and patron blocks — replaced with Local / Big-City-Paper.
- System Integration "Dutch drinking culture" + "German apartment" — flagged for integration rewrite.
- QA/Marketing "Dutch windmill heritage/tourism" — flagged for integration rewrite.
