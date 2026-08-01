# The Bohemian Riviera

*A beach resort experience for a country with no beach, no resort, and no shame*

## Location Identity
- **Location ID**: `debaucheryville_riverfront_bohemian_riviera_01`
- **Display Name**: The Bohemian Riviera
- **Satirical Subtitle**: "A beach resort experience for a country with no beach, no resort, and no shame"
- **World Location**: Debaucheryville
- **Area Zone**: The Bacchanus Riverfront
- **Location Type**: Quest Hub / Party District / Reality-TV Set

---

## Access & Requirements

### Entry Conditions
- **Time Restrictions**: Accessible 24/7. Beatdown filming days run on a rotating production schedule (see Time-of-Day Variations) and determine whether `catapult_row` is actively staffed; the rig itself is permanent set dressing between tapings and remains visible at all hours.
- **Stat Requirements**: None
- **Item Requirements**: None to enter
- **Previous Location Requirements**: None — accessible immediately on arrival in Debaucheryville, no prior quest gate
- **Special Conditions**: Entering the `fauxst_beach` zone on any active filming day auto-triggers Petra's sign-up dialogue at `signup_table`; this is the entry point for `debaucheryville_sidequest_bacchanus_beach_beatdown_01`

### Exit Conditions
- **Normal Exit**: Old Town streets (landward), riverside gear path to The Cirque du Shady (downriver)
- **Completion Requirements**: None to leave; the Beatdown can be declined, delayed, or completed on any visit
- **Failure States**: N/A in the traditional sense — per quest design, a minimum of two of the three bros are always launched into The Bacchanus regardless of player skill; this is the broadcast format, not a difficulty setting
- **Progressive Unlocks**:
  - Completing the Beatdown (WIN, LOSS, or DISQUALIFICATION) permanently unlocks the `night_party_zone` all-night party scene
  - `port_o_cologne` status becomes obtainable (any launch) and curable (riverbank shower vendor) from first completion onward
  - The aired episode begins looping on `bar_strip` bar TVs approximately one in-game day after quest resolution
  - Riverbank port-o-potty monuments (fished out by the boat-hook retrieval man) become permanent, navigable landmarks along the embankment after first completion
  - `Astronomical Cock-Up Square` and `Velvet Curtain Club` gain Beatdown-outcome-specific NPC callback dialogue once the quest resolves
  - Unlocking `night_party_zone` also arms the scripted outbreak event `night_event_outbreak_01`, the origin point of `debaucheryville_sidequest_nothing_is_getting_through_01` (see Quest Integration)

---

## Visual Design

### The Riviera Layout
```
┌──────────────────────────────────────────────────────────────────────┐
│                       THE BACCHANUS (river, murk-green)                │
│   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  │
│        [Lifeguard Tower — Standa]      [Shower Vendor Cart — Zdenka]   │
│                                          ~drifting port-o-potty~        │
│   ┌───────────────────── CATAPULT ROW ─────────────────────┐          │
│   │   🚽════🚽════🚽   <EMTV crane camera arcs overhead>     │          │
│   │   pneumatic arm, 3 units, hazard tape between tapings    │          │
│   └────────────────────────────────────────────────────────┘          │
│           │                                        │                   │
│   [SIGN-UP TABLE — Petra]                  [PRIZE PODIUM — Hamstradamus]│
│    clipboard, release forms                 folding table, banner       │
│           │                                        │                   │
│   ═══════════════════ FAUXST BEACH (trucked-in sand) ═══════════════   │
│   🌴 inflatable palm    🔥 space heater    🌴 inflatable palm          │
│         ⚠ "NO DIVING (SERIOUSLY, IT'S 40cm)"  ⚠                        │
│              [boat-hook retrieval station, Rosťa]                       │
│                                                                          │
├──────────────────────────── BAR STRIP ─────────────────────────────────┤
│   [Žá Žá Beach Klub]      [The Tan Line]       [Kokos Loco]            │
│   shipping container       tanning-bed neon      plastic tiki huts      │
│                                                                          │
│              ░░░░░░ NIGHT PARTY ZONE (after dark) ░░░░░░               │
│         string lights, sound system, unlocks after Beatdown resolves   │
└──────────────────────────────────────────────────────────────────────┘
       ← To Old Town Streets                    To The Cirque du Shady →
                                            (Shady Productions gear path)
```

### Exterior Description
- **Approach**: A cobblestone Old Town street narrows, dips, and then opens directly onto a raked ribbon of imported sand laid over embankment concrete — the transition is instant and slightly absurd, like walking into a diorama. The Bacchanus itself is visible the entire time: a slow, murky river doing its level best to look like a coastline.
- **Entrance**: No gate, no threshold — the sand simply starts. A sun-faded wooden signpost reads "THE BOHEMIAN RIVIERA" in beach-vacation script font, with a smaller, laminated card zip-tied underneath listing the sand's delivery manifest number, "for insurance purposes."
- **Signage**: Official: "THE BOHEMIAN RIVIERA — Debaucheryville's #1 Beach Destination" (there is no #2). Production: a sagging vinyl banner over the catapult reading **"BEATDOWN — LÉTO — SEZÓNA 22."** Safety: the "NO DIVING (SERIOUSLY, IT'S 40cm)" sign, hand-lettered, zip-tied to the lifeguard tower ladder.
- **Atmosphere**: Beach-resort ambition performed at full volume on a landlocked river — Eurodance bleeding from three separate bar sound systems that never quite sync, the occasional EMTV crane swinging into frame, gulls that are almost certainly just pigeons that have been on the sand long enough to develop an accent.
- **Environmental Context**: Bordered by Old Town's tourist sprawl to the west and a quieter riverside path east toward The Cirque du Shady, used by Shady Productions to move gear (and, on filming days, Hamstradamus) between the two venues.

### Interior Visuals — Zone by Zone

#### `fauxst_beach`
- Trucked-in sand, several inches deep, raked daily over embankment concrete; a delivery receipt for "40 TONS — RIVERSIDE FILL — NOT FOR HUMAN CONSUMPTION" is visibly stapled to the signpost and never removed
- Inflatable palm trees (four, slightly under-inflated, permanently listing at the same 15-degree angle regardless of wind)
- Space heaters positioned at "cozy" intervals along the loungers, running at full blast in the middle of summer because the rental company delivered the wrong equipment once, in Season 3, and nobody has ever un-booked them
- The lifeguard tower: a genuine, structurally sound tower positioned over water that is somewhere between 40 and 60 centimeters deep depending on who you ask and how the liability paperwork reads that week
- The "NO DIVING (SERIOUSLY, IT'S 40cm)" sign — the depth on the sign and the depth Standa the lifeguard will admit to under direct questioning do not match, and nobody involved considers this a problem worth resolving
- Loose beach chairs, none matching, several clearly borrowed from the bar strip and never returned

#### `bar_strip`
Three named beach bars line the embankment behind Fauxst Beach, each committing to a different flavor of landlocked-resort delusion:
- **Žá Žá Beach Klub** — a repainted shipping container strung with fairy lights and sold to vacationers as "VIP beach access," despite opening directly onto the same public sand as everyone else.
- **The Tan Line** — a sports-bar shell wallpapered in tanning-bed neon, playing beach volleyball highlights on a loop from a coastline none of its patrons have ever visited.
- **Kokos Loco** — a tiki-hut facade selling piña coladas in coconut shells that are, on close inspection, imported plastic molded to look tropical.

#### `catapult_row`
- The three-unit pneumatic catapult rig, permanent between tapings, roped off with hazard tape and a four-language "DO NOT ENTER — FILMING EQUIPMENT" sign when idle
- Three port-o-potties strapped to the arm; the center unit's door latch is visibly broken and swings open under its own weight
- EMTV camera crane, parked at rest position when not filming, still faintly humming
- A shrink-wrapped prize pallet stamped **2003**, half-opened, visible in the background — badges, steins, and Hamagotchis in identical bulk, never pointed at by anyone on staff
- Ground beneath the arm shows a permanent damp stain and a faint, specific smell that predates the current filming season

#### `signup_table`
- Petra's folding table: clipboard with coiled-cord pen, headset, laminated disclosure checklist she no longer needs but keeps anyway
- Three release forms, four pages each, single-spaced, entirely in Czech-parody legalese, fanned out and ready
- A small hand-lettered sign reading "SIGN-UP HERE" in six languages, none of which are the language the trivia is actually asked in

#### `prize_podium`
- A folding card table dragged out post-taping, draped in a Shady Productions banner folded so many times the logo has a permanent crease through it
- A small trapdoor in the table's base for Hamstradamus's entrance
- Leftover confetti from prior tapings, never fully swept, ground into the sand

#### `night_party_zone`
- Locked until the Beatdown resolves (win, loss, or disqualification) at least once
- String lights strung between the bar strip's awnings and the lifeguard tower, a sound system that migrates nightly between whichever bar is paying for the generator, and a crowd that arrives from nowhere in particular and stays until sunrise
- **This zone is a hook only** — the all-night party scene here is the seed for a future questline (working name "Herp") and is deliberately left undesigned beyond ambient dressing and unlock conditions in this document
- **Hook now claimed**: that questline shipped as `debaucheryville_sidequest_nothing_is_getting_through_01`, and this zone is where its scripted outbreak event `night_event_outbreak_01` is staged. The line above still governs this file — only the event hook is registered here (see Quest Integration); the scene's beats, dialogue, and NPC design live in the quest and profile files

### Technical Specifications
- **Color Palette**:
  - Sand: `#E8D4A0`
  - The Bacchanus (murk-green): `#5E7350`
  - EMTV Magenta (production branding, crane, signage): `#FF1493`
  - Catapult Steel: `#708090`
  - Inflatable-Palm Green: `#32CD32`
  - Accent — Space Heater Orange: `#FF7F32`
  - Accent — Night Party String-Light Amber: `#FFC966`
- **Lighting Setup**:
  - Day: harsh, flat beach-resort brightness, heat shimmer off the sand
  - Golden Hour: dramatic orange wash across the river, silhouettes of loungers and inflatable palms, the hour every bro believes he looks like a magazine cover
  - Night: string-light pools over `night_party_zone`, EMTV magenta glow from any bar TV playing the looping episode, lifeguard tower spotlight sweeping the water on a slow automatic cycle
- **Particle Systems**: Catapult launch splash (river impact), space-heater heat shimmer, confetti (post-win), fly-swarm particles (`port_o_cologne` status), string-light glow bloom (night)
- **Animation Elements**: Catapult launch arc (three independently-triggerable units, staggered fire), Hamstradamus's speedo strut, Jaxson's triple-can sip, Janek's buzzer-wave, inflatable palm idle sway, EMTV crane idle rotation
- **Mobile Optimization**: Vacationer crowd rendered as simplified sprites at distance, full detail on approach; catapult launch sequence pre-rendered per unit; bar-strip TV loop is a single shared low-res asset reused across all three bars, not rendered per-venue

---

## Satirical Design

### Theme & Vibe
**Core Concept**: A landlocked country's beach resort, built entirely out of confidence and trucked-in sand, hosting a reality-TV catapult show that runs on the same energy as an MTV summer special — filmed wherever the permits are cheapest, staffed by people who have long since stopped pretending the water is clean.

**The Irony**: Everyone involved in running the Bohemian Riviera — Petra, Jaxson, the bartenders, the shower vendor — is completely honest about what it is. Nothing here is a scam in the traditional sense. The sand's delivery receipt is stapled in plain view. The lifeguard will tell you the real depth if you ask him directly. The comedy isn't deception; it's that total, cheerful disclosure changes nothing about what the vacationers choose to believe they're experiencing.

### Cultural Targets
- **Primary Satirical Focus**: Reality-TV exploitation formats — the MTV summer-special economy where humiliation is the product and the release form is the only honest document on set
- **Secondary Targets**: Landlocked "beach resort" cosplay (trucked-in sand, inflatable palms, space heaters in July, a lifeguard tower over ankle-deep water); aging bros measuring themselves against college-age vacationers on a curve only they can see; sponsorship desperation (a host contractually drinking from three competing energy-drink cans at once); beach-resort pricing applied to a river embankment
- **Cultural Specificity**: The monolingual tourist's total confidence in a language he has never attempted; MTV/reality-TV era nostalgia (2003-vintage prize pallets, VHS-style aired episodes, EMTV camera cranes) collapsing directly into present-day influencer behavior (Chadwick's livestreamed sign-up, ICQ chat as a cheat channel)
- **Humor Approach**: Affectionate mockery of tourist delusion and reality-TV machinery; the locals running the show (Petra, Jaxson, the vendors) are savvy entrepreneurs playing it completely straight, never villains
- **Sensitivity Considerations**: Satire targets tourist psychology and reality-TV formats, never Czech people; no crypto elements; framed throughout as a summer vacation trip, not the other seasonal college-travel cliché; world names only — Debaucheryville, The Bacchanus

### Seedy Underbelly Elements
- **Primary Vice**: Manufactured humiliation as broadcast product, sold back to the humiliated as "fame"
- **City-Specific Comedy Operations**: The Beatdown production ecosystem — sign-up, catapult, prize podium, and the bar-strip TV loop that turns every outcome into a permanent local celebrity (for better or worse)
- **Buffoon Exploitation**: Bros are the ideal contestant — desperate to be "scouted," constitutionally unable to hear a disclosure, willing to sign anything for a camera they think is pointed at them
- **Comedy of Errors**: A minimum of two of three bros are launched every single taping, non-negotiably; the selected bro's own confidently-wrong shout is always one of the four selectable answers, meaning players must actively decline to be their own character
- **Consequence System**: Every prize is 2003-vintage carnival-grade merchandise; every launch is fished out with a boat hook and stood upright as a landmark; the episode airs on a loop and follows the bros into every bar on the strip

### Buffoon Delusion Scenarios
**What bros THINK is happening**:
> They have been scouted. An international television production walked the entire strip, looked at nine hundred college-age vacationers, and picked the three guys in cargo shorts specifically. This is the comeback moment.

**What is ACTUALLY happening**:
> Shady Productions runs a cheap catapult show on a fake beach and needs bodies. The bros were standing near the sign-up table. The fourth contestant, Janek, is a national-team rower who got waved over because the show needed someone who could actually answer a question.

**How impaired are they**:
> Not drunk — sober enough to sign four-page legal documents. Emotionally compromised enough to believe a monitor showing them the beach behind them is a camera.

**Obvious signs they ignore**:
- Petra discloses every single mechanic — the toilet, the catapult, the river, the water quality — in full, unprompted, twice
- The center port-o-potty's door latch is visibly broken
- The 2003-stamped prize pallet is in plain view before anyone has won anything
- The "camera" Chadwick flexes at is a monitor showing the beach behind him
- Two of the three bros are launched on a hard, non-negotiable schedule regardless of performance

**How locals play along**:
> Nobody corrects anything because total, cheerful honesty doesn't change what the bros hear. Vendors, hosts, and production staff treat every taping as season one, every time. Jaxson never once contradicts a bro's read on the situation. It's funnier this way, and it's also just Tuesday.

---

## Gameplay Mechanics

### Primary Functions
- **Core Purpose**: Quest hub for `debaucheryville_sidequest_bacchanus_beach_beatdown_01` — the Bacchanus Beach Beatdown catapult-trivia show
- **Secondary Functions**: Bar-hop / social district (three named beach bars), photo-opportunity zone (golden-hour posing), `port_o_cologne` status acquisition and cure loop, night-party unlock as future-questline seed

### Interactive Elements
- **`signup_table`**: Petra's dialogue tree, release-form signing, Bro Select path choice (Lord Pilsner / Chadwick / Bradley)
- **`catapult_row`**: `minigame_beatdown_trivia_gauntlet` (nine questions, three strikes, Czech-parody decode), staggered non-selected-bro launches
- **`prize_podium`**: `minigame_beatdown_sudden_death` resolution, Hamstradamus's WIN-branch prophecy and badge-pin ceremony
- **`fauxst_beach`**: Ambient examine points (delivery receipt, "NO DIVING" sign, lifeguard tower), boat-hook retrieval station (post-quest landmark)
- **`bar_strip`**: Three bars, each with light flavor interactions; bar TVs begin looping the aired episode ~1 day after quest completion
- **`night_party_zone`**: Locked until Beatdown resolution; ambient-only content in this document (see Time-of-Day Variations)

### Economic Integration
Landlocked beach-resort pricing — a river embankment charging full Mediterranean rates because the vacationers have no basis for comparison:

| Item/Service | Price | Reality |
|--------------|-------|---------|
| Beach lounger rental | €15/day | Sand is trucked in; chair is real |
| "River View" upgrade | €25 | The view is of the opposite riverbank |
| Space heater proximity seating | €5 | It is already 30°C |
| Riverbank shower (`port_o_cologne` cure) | €50 (€40 "if you go now") | Price rises the longer you stand there dripping |
| Piña colada in a coconut, Kokos Loco | €12 | Coconut shell is imported plastic |
| VIP cabana, Žá Žá Beach Klub | €80 | Cabana is a repainted shipping container |
| Beatdown sign-up | Free (release form signature) | Full contestant slot on a broadcast episode |

### Quest Integration
- **Quest Hub Role**: Origin point for `debaucheryville_sidequest_bacchanus_beach_beatdown_01`, triggered on entry to `fauxst_beach` on any filming day
- **Outbreak Event Hook — `night_event_outbreak_01`**: Origin point for `debaucheryville_sidequest_nothing_is_getting_through_01` ("Nothing Is Getting Through"), staged at `night_party_zone` during Night Rave hours once that zone is unlocked. Scripted and guaranteed — all three bros wake with `the_herp`, all three diagnose poison ivy, and the questline leaves for Sinfonia from here
- **Renata's Presence**: QUEEN Riviéra Renata, a Bohemian Riviera institution, is at the party that night; locals name-drop her in passing background dialogue ("Renata's here somewhere tonight—") and the bros never connect it. Her full design — appearance, dialogue, and her side of the morning exit — lives in `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/queen_riviera_renata.md`; the scene itself lives in `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`. Neither is duplicated in this file
- **Repeat Visit Value**: Petra discloses the same complete script to every new sign-up group; Jaxson hosts every taping as "season one"; the bar-strip TV loop and riverbank port-o-potty monuments persist and accumulate after first completion
- **Cross-Location Dependencies**: Beatdown-outcome dialogue at `Astronomical Cock-Up Square` (Shady Wristband Guy callback) and `Velvet Curtain Club` (bouncer badge-flash / half-step-back scenes)

---

## NPCs

### Jaxson Vane (Reality-TV Host)
- **Location Zone**: `catapult_row` / `prize_podium`
- **Role**: Hosts the trivia gauntlet and Sudden Death, tracks the selected bro's strike counter, pulls the lever
- **Summary**: Local broadcaster Jaromír Vaněk rebranded as an "imported American" extreme-sports host; drinks from three competing energy-drink sponsors in one rehearsed triple-sip; never watches a launch. Signature line: *"Unfortunately, bro."*
- **Full Profile**: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/jaxson_vane.md`

### Janek Sýkora (Contestant Four)
- **Location Zone**: `catapult_row` / `prize_podium`
- **Role**: Unbeatable trivia wall and Sudden Death buzzer opponent; the quest's only genuine skill gate
- **Summary**: A 22-year-old national crew-team rower recruited off the street mid-training-row; answers all nine questions correctly except one scripted thrown answer at Q6; his crew team gliding past on The Bacchanus is his only tell (1.5-second buzzer window). Calls the bros "the sirs" because nobody has introduced them.
- **Full Profile**: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/janek_sykora.md`

### Petra (Production Assistant)
- **Location Zone**: `signup_table`
- **Role**: Quest giver; runs sign-up, full disclosure, and release-form collection
- **Summary**: Discloses every material fact of the show, every time, unprompted — the toilet, the catapult, the river, the water quality, the waiver — and offers to read the four-page Czech-parody release forms aloud in English (never accepted). Never lies, in any line, in any branch.
- **Full Profile**: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/petra_production_assistant.md`

### Hamstradamus (Filming-Day Prize-Giver)
- **Location Zone**: `prize_podium` (filming days only; otherwise resident at The Cirque du Shady prophecy tent)
- **Role**: WIN-branch prize-giver — speedo-strut entrance, badge-pin ceremony, canon-locked English prophecy
- **Summary**: A turbaned, booming-voiced circus hamster who is, structurally, always correct. On Beatdown filming days he wears a midnight-blue wizard hat and a beach-appropriate speedo instead of his usual turban.
- **Full Profile**: `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/hamstradamus.md`

### Rosťa — Boat-Hook Retrieval Man *(new, location NPC)*
- **Location Zone**: `fauxst_beach`, riverbank retrieval station
- **Role**: Ambient service NPC; fishes launched port-o-potties out of The Bacchanus and stands them upright along the embankment as informal landmarks
- **Appearance**: Weathered, permanently damp, a boat hook that never leaves his hand, waders rolled down to the knee because the water rarely justifies rolling them up
- **Personality**: Utterly unbothered — this has been his entire job for eleven seasons and he has developed a professional rhythm around it; treats each retrieval with the same mild competence a mail carrier brings to a route
- **Key Dialogue**: *"Three today. Personal best is five. I keep a chart."* / *"You get used to the smell. You do not get used to the door latch."*
- **Services/Function**: Purely environmental-storytelling and flavor barks; retrieved units become permanent riverbank landmarks after quest completion (locals give directions using them; a vendor sets up next to one; someone's laundry appears on one by Day 6)

### Standa — Fauxst Beach Lifeguard *(new, location NPC)*
- **Location Zone**: `fauxst_beach`, lifeguard tower
- **Role**: Ambient service NPC; staffs the tower over the 40–60cm water
- **Appearance**: Genuine lifeguard kit — whistle, rescue buoy, red trunks — undercut by a well-worn paperback he is never quite willing to put down
- **Personality**: Professionally attentive, personally bored; the job has exactly two duties, and one of them (watching for actual drowning risk in ankle-deep water) has never once been needed
- **Key Dialogue**: *"The sign says forty. I'd call it closer to sixty, if you're asking me directly, which you are."* / *"I've blown this whistle twice. Both times, catapult."*
- **Services/Function**: Flavor dialogue and comedic depth-discrepancy easter egg; whistle-blow bark triggers on any catapult launch witnessed from the tower

### Zdenka — Riverbank Shower Vendor *(new, location NPC)*
- **Location Zone**: `fauxst_beach`, riverbank, adjacent to the lifeguard tower
- **Role**: Vendor NPC; sells the `port_o_cologne` status cure
- **Appearance**: A folding cart with a hose rigged to a repurposed water tank, a hand-lettered price sign, sun-bleached apron
- **Personality**: Brisk, transactional, entirely unsentimental about the fly particles trailing behind every customer
- **Key Dialogue**: *"Fifty euro for the shower. Forty if you go now. It goes up the longer you stand there."* — quoted verbatim from the Beatdown quest doc's NPC callback
- **Services/Function**: Direct `port_o_cologne` cure hook, available to any bro (or party member) who has been launched and waded ashore; price escalates the longer the affected party dawdles at her cart

### College-Vacationer Crowd *(ambient NPC group)*
- **Location Zone**: All zones, ambient density highest at `bar_strip` and `fauxst_beach`
- **Role**: Ambient crowd — sign-up witnesses, Beatdown spectators, heckle-line deliverers during the Walk of Shame
- **Summary**: Nine hundred (give or take) college-age vacationers the bros believe they were specifically scouted over; deliver Czech-parody heckle lines the bros confidently mistranslate as praise; film everything on flip phones; chant crowd responses (e.g., the "pět… pět… pět…" beer-volume chant) without being asked
- **Function**: Density and reaction-shot dressing during tapings; heckle-line delivery on LOSS branch walk-of-shame; no unique names or persistent dialogue trees required beyond barked lines already specified in the quest doc

---

## Audio Design

### Environmental Audio
- **Ambient Soundscape (day)**: Distant Eurodance bleeding from three unsynced bar sound systems, vacationer chatter, cobblestone-to-sand footstep transition, river lapping against the embankment
- **Catapult Launch Audio**: The signature *THUNK-hisssss-splash* — pneumatic release, air hiss, and the specific wet, hollow, resonant river-impact note the sound designer has been asked to make "wetter" every season; this note is reused unchanged as the show's de facto theme music
- **Jaxson's Mic Feedback**: A short, sharp feedback squeal whenever the crane camera swings past his podium mark too fast — a rig quirk nobody has fixed in twenty-two seasons
- **Night Audio (`night_party_zone`)**: Sound system migrating nightly between bars, crowd noise cresting toward dawn — ambient dressing only, no unique mix required for this seed content

### Interactive Audio
- **Sign-up beat**: Pen-click on clipboard, headset static, page-turn on the release forms
- **Trivia gauntlet**: Twelve-second countdown tick, correct-answer chime, strike buzzer, crowd chant (the "pět… pět… pět…" beer-chant is audible and central to the metric-trap question)
- **Sudden Death**: Oar catch-and-release audio cue, mixed above crowd noise, ramping for two full seconds before Janek's crew team passes — the only skill-gate tell in the questline, audio-only by design
- **Prize podium**: Speedo-strut fanfare sting, badge-pin click, stein-leak drip loop

### Comedy Audio Stingers
- **Mid-Sentence Launch (Q7)**: Speech audio clips hard mid-syllable, then continues faintly over the water at falling volume for ~1 second before cutting — do not fade
- **Aired Episode (bar TVs)**: Short, looping CRT-filtered edit (~20s) with the "HOSTÉ" lower-third graphic, reused across every bar on the strip
- **Jaxson's accent slip**: A single clean syllable of Czech leaking through during genuine equipment malfunction — rare, never overused

---

## Time-of-Day Variations

### Day Filming (10:00–17:00, active tapings only)
- Full production crew active at `catapult_row` and `signup_table`
- Maximum vacationer crowd density, EMTV crane live and swinging
- Space heaters running at full blast regardless of ambient temperature
- Trivia gauntlet and Sudden Death resolve during this window

### Golden-Hour Posing (18:00–20:00)
- Filming wraps for the day; production crew breaks down but leaves the catapult roped off
- Vacationer crowd shifts from spectator mode to photo-op mode — flexing at the monitor Chadwick made famous, sunset selfies against the inflatable palms
- Bar strip terraces fill; drink prices tick up on the (unwritten) golden-hour markup
- Best lighting for screenshots; worst lighting for anyone actually trying to read the "NO DIVING" sign

### Night Rave (22:00–04:00, post-Beatdown-completion only)
- `night_party_zone` unlocks and activates — string lights, migrating sound system, crowd that arrives from nowhere and stays until sunrise
- Bar-strip TVs loop the aired Beatdown episode at low volume under the music once the episode has begun airing
- **This is the seed for the future "Herp" questline — hook only, not designed in this document.** No new mechanics, NPCs, or narrative beats beyond ambient party dressing are specified here.
- On the questline's scripted party night, `night_event_outbreak_01` fires during this window (see Quest Integration). The ambient dressing above is unchanged and no new location mechanics are authored for it here.
- Riverbank retrieval station (Rosťa) goes quiet; port-o-potty monuments are lit by the string lights and function as informal seating

---

## Connected Locations

### Directly Adjacent
- **Old Town Streets**: Landward exit, general exploration and vendor-cluster access (Astronomical Cock-Up Square, etc.)
- **Riverside Embankment Path**: Runs the length of the strip past all bar-strip venues and the retrieval station

### Quest-Connected
- **The Cirque du Shady**: Connected via the Shady Productions gear path along the riverbank — Ringmaster Vance "Vape" Vallaro's television venture operates the Beatdown from a folding table with a fax machine behind the big top; Hamstradamus travels this exact route on filming days between the prophecy tent and `prize_podium`
- **Astronomical Cock-Up Square**: Beatdown-outcome callback dialogue via the Shady Wristband Guy, who recognizes "the toilet men... from the television"
- **Velvet Curtain Club**: Beatdown-outcome callback at the door — badge-flash scene (WIN) or the bouncer's half-step-back-and-let-them-in-anyway scene (LOSS)

---

## Implementation Specifications

### Technical Requirements
- **Asset List**: Beach tileset (sand, water, inflatable palms), catapult + port-o-potty rig with launch animation frames, bar-strip facades ×3, NPC sprites (Jaxson, Janek, Petra, Hamstradamus beach variant, Rosťa, Standa, Zdenka), vacationer crowd sprites, parallax river background
- **Animation Requirements**: Three independently-triggerable catapult launch units (staggered fire — Launch One as interruption, Launch Two mid-syllable), Jaxson's triple-can sip, Janek's 1.5-second buzzer-wave, Hamstradamus's speedo strut and badge pin
- **Performance Budget**: Target 45-60 FPS; max 25-45 draw calls (crowd-density dependent); memory budget 55-65MB (larger than a single-room location due to six active zones); particle limit — splash (1 per launch), heat shimmer (2 emitters), fly swarm (`port_o_cologne`, 10 max), string lights (night, ambient glow only)
- **Platform Considerations**: Bar-strip TV loop asset shared across all three venues rather than rendered per-venue; crowd LOD steps down aggressively past `bar_strip` mid-ground

### State Tracking
```
bohemian_riviera_state:
  - visited: boolean
  - beatdown_complete: boolean
  - selected_bro: string (enum: lord_pilsner / chadwick / bradley / none)
  - bros_launched_count: integer (0-3)
  - night_party_seen: boolean
  - outbreak_seen: boolean (night_event_outbreak_01 — "Nothing Is Getting Through")
  - filming_day_active: boolean
  - episode_airing: boolean (true ~1 in-game day after beatdown_complete)
  - port_o_cologne_active: boolean
  - return_visit_count: integer
```

---

## Quality Assurance Checklist

### Pre-Implementation Review
- [x] **World consistency verified** — uses "Debaucheryville" and "The Bacchanus" exclusively; no real-world city or river names appear anywhere in this document
- [x] **Cultural specificity confirmed** — landlocked beach-resort satire, reality-TV format satire, tourist psychology satire, not generic European
- [x] **Satirical targets appropriate** — reality-TV exploitation formats and tourist/bro psychology, never Czech people
- [x] **Gameplay value established** — quest hub for the Beatdown, bar-strip social district, night-party unlock seed
- [x] **Technical feasibility confirmed** — staggered catapult launches, crowd density, bar-strip TV loop all achievable within stated performance budget
- [x] **No crypto elements** — none present
- [x] **Seedy underbelly present** — reality-TV humiliation-as-product economy, landlocked beach-resort pricing
- [x] **Summer vacation framing maintained throughout** — the other seasonal college-travel cliché is never used

### Post-Implementation Testing
- [ ] All six zone tags (`fauxst_beach`, `bar_strip`, `catapult_row`, `signup_table`, `prize_podium`, `night_party_zone`) resolve to distinct, navigable areas
- [ ] Beatdown quest trigger fires correctly on `fauxst_beach` entry during active filming days
- [ ] Catapult launch stagger timing (Q4 interruption, Q7 mid-syllable) reads correctly
- [ ] `night_party_zone` remains locked until `beatdown_complete` is true
- [ ] `port_o_cologne` cure loop functions at Zdenka's riverbank cart
- [ ] Bar-strip TV loop begins ~1 day after quest completion, not before
- [ ] Time-of-day variations (day filming / golden-hour posing / night rave) transition correctly
- [ ] Cross-location callback dialogue fires at Astronomical Cock-Up Square and Velvet Curtain Club post-resolution

---

## Social Media Viral Potential

### Screenshot Moments
1. **The triple catapult row, loaded** — three port-o-potties on the pneumatic arm, inflatable palms, space heaters, lifeguard tower, EMTV crane, all in one establishing frame
2. **Golden-hour flex at the monitor** — Chadwick (or any bro) flexing at the "camera" that is visibly showing the beach behind him
3. **Hamstradamus pinning the badge** — the crooked star, the crying grown man, the beach-appropriate speedo
4. **The walk of shame** — soaked bros, fly particles, heckle/mistranslation text bubbles stacked in one frame

### Quote Potential
- "NO DIVING (SERIOUSLY, IT'S 40cm)"
- "Fifty euro for the shower. Forty if you go now."
- "Three today. Personal best is five. I keep a chart."
- "Unfortunately, bro."

---

## Development Notes

- The three named bar-strip venues (Žá Žá Beach Klub, The Tan Line, Kokos Loco) are location flavor only in this document — no shop inventory or NPC rosters are authored for them here; that is deferred to their own future location passes if the plan calls for it.
- `night_party_zone` is deliberately underspecified per the brief: it exists as an unlock condition and ambient dressing only. Do not add Herp-questline mechanics, NPCs, or narrative beats to this file in a later pass — that belongs to its own future task.
- That future task is now `debaucheryville_sidequest_nothing_is_getting_through_01`, and the note above still holds: this file carries the outbreak **hook** only (event id, quest id, staging zone, and a pointer to Renata's profile). Mechanics, scene beats, and NPC design remain out of this document by design — add them to the quest file or the profile, never here.
- Rosťa, Standa, and Zdenka are new location NPCs authored here to absorb the minor characters the quest doc references but does not itself formally profile (the boat-hook retrieval man, the Fauxst Beach lifeguard, and the riverbank shower/`port_o_cologne` vendor). Their dialogue draws directly from `bacchanusbeachbeatdown.md` where the quest doc already quotes them verbatim (Zdenka's price line) and extrapolates lightly elsewhere, consistent with quest-doc canon (Rosťa's "entire job," Standa's tower staffing and "used the whistle twice").
- The 40cm vs. 60cm water-depth discrepancy between the safety sign and Standa's own admission is an intentional bit, not an error to reconcile — it mirrors the quest doc's established pattern of total honesty changing nothing about what tourists choose to hear.
- Zone tag IDs (`fauxst_beach`, `bar_strip`, `catapult_row`, `signup_table`, `prize_podium`, `night_party_zone`) are load-bearing for the downstream JSON data pass — do not rename them in a later revision without updating dependent files.

---

## Final Validation

**The Bohemian Riviera is Debaucheryville's monument to landlocked confidence — a beach resort built entirely from trucked-in sand, sponsor-can triple-sips, and a catapult rig that has launched a minimum of two out of every three contestants for twenty-two consecutive seasons. Every mechanic that humiliates the bros is disclosed to them, in full, by an honest woman with a clipboard, and it changes nothing about what they choose to believe happened. The strip's three beach bars, its filming setup, and its after-dark party scene together form a complete quest hub — and the after-dark scene, deliberately, is only a promise of more to come.**
