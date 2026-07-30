# The Cirque du Shady

*A semi-permanent traveling circus that has not traveled since 1997*

## Location Identity
- **Location ID**: `debaucheryville_circus_cirque_du_shady_01`
- **Display Name**: The Cirque du Shady
- **Satirical Subtitle**: "A semi-permanent traveling circus that has not traveled since 1997"
- **World Location**: Debaucheryville
- **Area Zone**: Circus Grounds (edge of Old Town)
- **Location Type**: Quest Hub / Attraction Cluster / Production Company HQ

**What this file is**: the parent grounds document that stitches the Cirque's existing, separately-profiled attractions into one navigable location. Where a zone already has its own file (the prize booth, the mystery meat cart, the prophecy tent, Bobo's performance spot), this document links to it, quotes its established facts, and adds nothing that contradicts it. Everything else on these grounds — the gate, the big top exterior, Ringmaster Vance's tent, the Shady Productions office, the knife-throwing act, the rigged game alley, and the ICQ backroom — is new content authored here for the first time.

---

## Access & Requirements

### Entry Conditions
- **Time Restrictions**: Grounds open 14:00–01:00 daily. Individual attractions keep their own posted hours where established elsewhere (the prize booth: "whenever the circus is open"); this document sets that operating window.
- **Stat Requirements**: None to enter the grounds
- **Item Requirements**: None to enter; individual attractions have their own currency requirements (Circus Tickets at the prize booth, Kebab Coins at the mystery meat cart) per their own files
- **Previous Location Requirements**: None — accessible from Old Town on arrival in Debaucheryville
- **Special Conditions**: On Beatdown filming days, Hamstradamus is physically absent from `prophecy_tent` (relocated to Fauxst Beach as prize-giver, per `hamstradamus.md`), and the riverside gear path out of `shady_productions_office` sees active foot traffic moving production equipment toward the Bohemian Riviera

### Exit Conditions
- **Normal Exit**: Main gate (west, to Old Town Streets) or the riverside gear path out of `shady_productions_office` (east, to The Bohemian Riviera)
- **Completion Requirements**: None — this is a hub, not a gated quest location
- **Failure States**: N/A
- **Progressive Unlocks**:
  - `beatdown_aware` — set on first examination of the Shady Productions folding table or fax machine, or on hearing Vance mention "the show"
  - `vance_met` — set on first dialogue with Ringmaster Vance
  - `cirque_visited` — set on first entry to the grounds via either gate
  - Individual attraction unlocks (Yolanda's "Frequent Loser" status, Chef Chuckles' Respect, Bobo's "backstory breakdown" dialogue) remain governed entirely by their own files and are not re-specified here

---

## Visual Design

### The Grounds Layout
```
┌──────────────────────────────────────────────────────────────────────────┐
│                    ← MAIN GATE (from Old Town Streets)                     │
│               🎫 Ticket Booth — "Admission €5. Everything Else Extra."      │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│     [PROPHECY TENT]                 [GAME ALLEY]          [PRIZE BOOTH]     │
│      turban, crystal ball        rigged milk bottles,     Yolanda's counter │
│      (heart of the main path)     ring toss, coin toss ─► (ticket redemption)│
│                                                                              │
│                       ┌─────────── BIG TOP ───────────┐                     │
│                       │  faded red-and-cream canvas    │                     │
│  [MEAT CART PITCH]    │  dome, tent stakes sunk in      │   [PERFORMANCE     │
│   Chef Chuckles'      │  concrete since 1997            │    CIRCLE]         │
│   cart, steam &       │  ⛺ Vance's Tent   🚪 ICQ         │  Bobo's balloon-   │
│   neon rotisserie     │    (vape haze)     Backroom      │  animal pitch +    │
│   (beside Vance's      │     (flap)       (canvas flap)  │  knife-throwing act│
│   tent, per canon)     └────────────────┬────────────────┘                    │
│                                          │                                    │
│                       ┌── SHADY PRODUCTIONS OFFICE ──┐                       │
│                       │  folding table · fax machine   │                      │
│                       │      (behind the big top)      │                      │
│                       └────────────────┬────────────────┘                     │
│                                        │                                      │
└─────────────────────────────────────── ┼──────────────────────────────────────┘
                        riverside gear path → THE BOHEMIAN RIVIERA
                                (Shady Productions / Fauxst Beach)
```

### Zone Directory
| Zone Tag | Contents | Canonical Source |
|----------|----------|-------------------|
| `main_gate` | Ticket booth, entrance signage | New — this document |
| `big_top` | Main tent exterior, Ringmaster Vance's tent flap, ICQ backroom flap | New — this document (Vance's existing canon per `debaucheryville.md` / `game_design_document.md`) |
| `prophecy_tent` | Hamstradamus, Prophecy Roulette | `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/hamstradamus.md` — **not modified** |
| `game_alley` | Rigged carnival games, ticket source | New — this document |
| `prize_booth` | The Participation Trophy, Yolanda | `Design/World Design/Debaucheryville/the_participation_trophy.md` — **not modified** |
| `meat_cart_pitch` | Mystery Meat Cart, Chef Chuckles | `Design/World Design/Debaucheryville/mysterymeatcart.md` — **not modified** |
| `performance_circle` | Bobo "The Blockchain" Bitsworth, knife-throwing act | Bobo: see NPCs section below (`crypto_clown.md`) — **not modified**. Knife-throwing act: new — this document |
| `shady_productions_office` | Folding table + fax machine; produces The Bacchanus Beach Beatdown | New — this document (production role cross-referenced from `bacchanusbeachbeatdown.md` and `bohemian_riviera.md`) |
| `icq_backroom` | ICQ terminal hotspot; Darkweb Dossier "hack-through" pop-ins | New — this document (characters per `debaucheryville.md`) |

### Exterior Description
- **Approach**: Old Town cobblestones give way to trampled grass and sawdust well before the gate itself is visible — the smell (fried sugar, machine oil, something floral gone slightly wrong) arrives first
- **Entrance**: A single wooden ticket booth flanked by a rope line that has never once needed to hold back a real crowd. A hand-painted arch overhead reads "THE CIRQUE DU SHADY" in a font trying hard to look hand-lettered by someone with real showmanship
- **Signage**: Main arch: "THE CIRQUE DU SHADY — EST. [date scratched out and re-painted three times, current reading illegible]." Ticket booth: "ADMISSION €5. EVERYTHING ELSE EXTRA." Small taped-on addendum, clearly added later: "(THIS INCLUDES THE BATHROOM.)"
- **Atmosphere**: A distorted calliope loop bleeds through everything; vape clouds drift from the direction of Vance's tent regardless of wind; the whole grounds smell faintly of fry oil and canvas mildew
- **Environmental Context**: Sits at the edge of Old Town, with the big top itself visible from streets away — a faded red-and-cream dome that has clearly not moved, in any literal sense, in a very long time. The riverside gear path on the grounds' far side connects directly to the Bohemian Riviera's embankment path, the same route documented in `bohemian_riviera.md`'s Connected Locations section

### Interior Visuals — Zone by Zone

#### `main_gate`
- The ticket booth: warped plywood, a single barred window, a hand-cranked ticket dispenser that jams on purpose (per the attendant, "builds anticipation")
- A corkboard beside the booth, papered in overlapping flyers — Prophecy Roulette hours, a faded Vanishing Elephant "Bubbles" poster (missing-pet-style, except the elephant is still, technically, on the premises), and one current Shady Productions casting flyer, curling at the corners

#### `big_top`
- The dome itself: faded red-and-cream canvas panels, several visibly re-stitched, a support pole with rust rings marking where wheels used to attach before the tent stopped traveling
- **Vance's Tent**: a smaller canvas structure abutting the big top's side, its flap perpetually fogged from the inside; a hand-lettered sign reads "RINGMASTER — BY APPOINTMENT (NO APPOINTMENTS NEEDED)"
- **ICQ Backroom**: a second, unmarked canvas flap on the big top's opposite side, propped open a crack; a single CRT monitor glow is visible from outside after dark
- Faint elephant-adjacent sounds and hay smell drift from within the big top itself — Bubbles's enclosure is inside, ambient dressing only (see Gameplay Mechanics)

#### `game_alley`
- A row of rigged carnival games — milk bottles filled with concrete, oversized rings against undersized bottle necks, a coin-pusher tilted three degrees off level — running parallel to the path toward the prize booth
- Barker patter is constant and interchangeable game to game; ticket payouts feed directly into the prize booth's ticket economy documented in `the_participation_trophy.md`

#### `shady_productions_office`
- One folding card table, one office chair with a wheel missing, and a fax machine that predates the current millennium by a comfortable margin, humming behind the big top's canvas wall
- The fax machine periodically spits a **Casting-Call Flyer** — the same flyer, every time, reading "WANTED: ATHLETIC-INTELLECTUAL HYBRID. CARGO SHORTS PREFERRED. NO EXPERIENCE NECESSARY." A stack of identical printed flyers, un-collated, covers most of the table
- A shrink-wrapped merchandise pallet stamped **2003** is visible at the tent-flap edge of the office — the same pallet documented at Fauxst Beach in `bohemian_riviera.md`, evidently the overflow storage location
- A hand-lettered sign taped to the fax machine: "SHADY PRODUCTIONS — HOME OF THE BACCHANUS BEACH BEATDOWN — SEASON 22"

#### `performance_circle`
- An open ring of trampled grass ringed by mismatched folding chairs, shared by Bobo's balloon-animal pitch and the knife-throwing act on a rotating schedule neither performer has ever formally agreed to
- A wooden target board, permanently scarred, leans against a support post when not in active use

#### `prophecy_tent`, `prize_booth`, `meat_cart_pitch`
- Interior visuals for these three zones are fully specified in their own files (`hamstradamus.md`, `the_participation_trophy.md`, `mysterymeatcart.md`) and are not restated or altered here — see the Zone Directory above for exact paths

### Technical Specifications
- **Color Palette**: Faded Big-Top Red `#B22222`, Canvas Cream `#F5F0DC`, Neon Marquee `#FF6EC7`, Vape-Cloud Gray `#C0C0C8`
- **Lighting Setup**: Afternoon — flat, dusty daylight filtered through canvas seams; Night — the neon marquee over the main gate and scattered string bulbs along `game_alley`, everything else lit by whatever spills from tent flaps
- **Particle Systems**: Vape cloud drift (Vance's tent, ambient and dialogue-triggered), calliope-adjacent dust motes, fax-machine paper-feed flutter, distant hay/dust from the big top interior
- **Animation Elements**: Marquee flicker (main gate), Vance's vape-cloud speech FX, Prophecy Tent Glow (purple-gold pulse through the tent seams, full spec in `Cirque_du_Shady_PNG_Assets.md` — Hamstradamus's own performer animation states remain in `hamstradamus.md` and are not restated here), fax machine paper-spit cycle
- **Mobile Optimization**: Grounds crowd rendered as simplified sprites at distance, full detail near active attractions; vape-cloud particle density reducible; each stitched sub-location keeps the mobile-optimization notes already specified in its own file

---

## Satirical Design

### Theme & Vibe
**Core Concept**: The Cirque du Shady is Debaucheryville's carnival grift economy running at full vertical integration — a full-stack scam ecosystem where every attraction feeds the next one. Game Alley manufactures tickets that are worth less than the games cost to play; the Prize Booth converts those tickets into garbage; the Mystery Meat Cart and Prophecy Tent extract cash directly; the Performance Circle solicits tips for acts that are, depending on the act, either a Ponzi-adjacent balloon pitch or a genuine prophet nobody believes; and behind it all, the Shady Productions office quietly recruits the marks who fall hardest — for television.

**The Irony**: Nothing here hides what it is. The ticket booth's sign says "everything else extra" out loud. The fax machine's casting flyer is visible to anyone who reads it. Ringmaster Vance will, without prompting, describe his loot crates as "a bit of a gamble, honestly." The grift isn't concealment — it's that total, cheerful transparency changes nothing about what a bro chooses to believe he's walking into.

### Cultural Targets
- **Primary Satirical Focus**: The traveling-circus-as-scam-ecosystem — carnival grift economics stacked end to end, from rigged games through garbage prizes through reality-TV recruitment
- **Secondary Targets**: "Semi-permanent" branding that quietly admits permanence; the fax machine as a symbol of an operation that has not updated a single piece of its infrastructure since the prize pallet's stamped year; showmen who oversell themselves in exactly the register their marks want to hear
- **Cultural Specificity**: Traveling-circus grift culture, tourist-district carnival economics, low-budget reality-TV production infrastructure — world names only throughout (Debaucheryville, The Bacchanus, The Bohemian Riviera)
- **Humor Approach**: Affectionate mockery of a scam machine that is, structurally, completely honest about being one; every performer here (Vance, Chef Chuckles, Yolanda) is a savvy entrepreneur playing it straight, never a villain
- **Sensitivity Considerations**: Satire targets carnival grift economics and reality-TV recruitment psychology, never Czech people or circus performers as a class; the NPCs profiled elsewhere on these grounds are explicitly written as savvy, not exploited — this document does not alter that framing

### Seedy Underbelly Elements
- **Primary Vice**: Converting foot traffic into money by any attraction available, then converting the most gullible foot traffic into unpaid television talent
- **City-Specific Comedy Operations**: The full grounds-wide pipeline — ticket games feed the prize booth, the prize booth feeds ironic pride, the prophecy tent feeds paid mysticism, and the Shady Productions office quietly feeds Fauxst Beach
- **Buffoon Exploitation**: Bros who wander past the Shady Productions fax machine and read "WANTED: ATHLETIC-INTELLECTUAL HYBRID" as a message written specifically to them
- **Comedy of Errors**: The same casting flyer has been feeding out of the same fax machine for who knows how many seasons, and every bro who reads it experiences it as a personal summons
- **Consequence System**: Money spent at every attraction on these grounds is, without exception, money spent on something worth less than what was paid — consistent with every stitched sub-location's own economics

### Buffoon Delusion Scenarios
**What bros THINK is happening**: They have discovered the real, functioning nerve center of an international entertainment operation — a circus that's secretly a media empire, and they, specifically, are the kind of guys a media empire would want.

**What is ACTUALLY happening**: A rigged game alley, a garbage-prize booth, a food cart of questionable provenance, a prophet nobody believes despite being always right, a failed street performer busking for tips, a knife act older than most of the tourists, and a fax machine that has printed the same flyer for twenty-two seasons, all operating under one canvas dome that has not moved since before most of them could drive.

**Obvious signs they ignore**:
- The ticket booth's sign says "everything else extra" in plain English before they've paid for anything
- The Shady Productions casting flyer is identical every time it prints
- The prize pallet visible at the office's edge is stamped `2003`
- Ringmaster Vance describes his own loot crates as "a bit of a gamble, honestly," unprompted
- The fax machine has clearly not been serviced since before some of the bros were born

**How locals play along**: Nobody here corrects a bro's read on the situation, because correcting it has never once changed a purchase decision. Vance treats every walk-up as a potential talent discovery. Yolanda counts tickets with the same flat honesty regardless of how the counting is received. It's funnier this way, and it's also just Tuesday.

---

## Gameplay Mechanics

### Primary Functions
- **Core Purpose**: Central quest hub and attraction cluster tying together the Cirque's independently-profiled sub-locations, plus the production-company front door for The Bacchanus Beach Beatdown
- **Secondary Functions**: Rigged-game ticket sink (`game_alley` → `prize_booth`), ambient performance district (`performance_circle`), ICQ hotspot access (`icq_backroom`), light environmental storytelling for the "Vanishing Elephant" quest hook

### Interactive Elements by Zone
- **`main_gate`**: Ticket booth transaction, corkboard flyer examine points (Bubbles poster, Shady Productions casting flyer)
- **`big_top`**: Exterior examine only in this document; Vance's tent hosts his loot-crate voucher pitch (fulfillment happens at `prize_booth` — see Economic Integration below); the ICQ backroom flap leads to `icq_backroom`
- **`prophecy_tent`**: Prophecy Roulette (5 coins, random buff/debuff) — full mechanics in `hamstradamus.md`, not restated here
- **`game_alley`**: Rigged carnival games (milk bottles, ring toss, coin pusher) — average yield 5–15 tickets per €3 game, feeding directly into `prize_booth`'s documented ticket-tier economy
- **`prize_booth`**: Ticket redemption — full mechanics in `the_participation_trophy.md`, not restated here
- **`meat_cart_pitch`**: Full menu and Digestive Daredevil mechanics in `mysterymeatcart.md`, not restated here
- **`performance_circle`**: Bobo's balloon-animal pitch (see NPCs section below); the knife-throwing act's interactive dodge minigame (player takes the assistant's spot)
- **`shady_productions_office`**: Casting-flyer examine point; `beatdown_aware` trigger; no transactions occur here — this is a production front, not a vendor
- **`icq_backroom`**: ICQ terminal; random "hack-through" pop-ins from Darkweb Dossier characters

### Economic Integration
Grounds admission is a flat, plainly-advertised rip-off — everything past the gate costs extra, and the sign says so:

| Item/Service | Price | Reality |
|--------------|-------|---------|
| Grounds admission | €5 | Grants access to further paid attractions, nothing else |
| Rigged carnival game (`game_alley`) | €3 avg. | 5-15 tickets, statistically worse than the prize costs |
| Vance's Shady Loot Crate Voucher | Variable, per Vance's own pitch | "A bit of a gamble, honestly" — his words. Per canon (`game_design_document.md`), the crates themselves are offered "from the prize booth" — Vance hawks and sells the voucher from his tent, and the bro walks it over to `prize_booth` for fulfillment |
| Knife-throwing act dodge round | Free to attempt, tip solicited after | Tip jar sits beside the target board |

Vance's loot-crate line is a two-zone transaction by design: the pitch happens at `big_top` (his tent), the redemption happens at `prize_booth`, where Yolanda hands over the crate with the same flat professionalism she brings to every other prize — visibly unthrilled to be doing Vance's fulfillment on top of her own ticket counter. No crate contents, pricing, or Yolanda dialogue are specified in this document; that redemption-counter mechanic belongs to a future items/shop pass and to `the_participation_trophy.md` itself, not this stitching file — it is noted here only so the two zones don't contradict each other. Individual attraction economics (ticket tiers, menu prices, Prophecy Roulette cost) remain fully specified in their own files and are referenced, not restated, here.

### Quest Integration
- **`debaucheryville_sidequest_bacchanus_beach_beatdown_01`**: `shady_productions_office` is the production's home base — the folding table and fax machine referenced directly in `bacchanusbeachbeatdown.md`'s Cross-References section ("Shady Productions is Ringmaster Vance 'Vape' Vallaro's television venture, operated from a folding table with a fax machine behind the big top"). The actual sign-up and quest content live entirely at Fauxst Beach on the Bohemian Riviera; this office is flavor, foreshadowing, and the `beatdown_aware` state trigger, not a second quest-start point
- **Prophecy Roulette**: Ambient event at `prophecy_tent`, fully specified in `hamstradamus.md`
- **The Vanishing Elephant ("Bubbles")**: Sidequest hook per `debaucheryville.md` / `game_design_document.md` — recover the elephant before he's sold to a questionable nightclub. Bubbles's enclosure is ambient dressing inside `big_top` in this document; the quest itself is a hook only, not designed here (consistent with how `night_party_zone` is treated as a hook in `bohemian_riviera.md`)
- **ICQ Scammer Sting** (cross-referenced in `bacchanusbeachbeatdown.md`): `icq_backroom` shares the same ICQ substrate and at least one handle (`Tony420`) with that questline's cast

---

## NPCs

| NPC | Zone | Role | Full Profile |
|-----|------|------|----------------|
| Ringmaster Vance "Vape" Vallaro | `big_top` (his tent) | Circus proprietor; owner of Shady Productions | New — profiled below, no prior file existed |
| Hamstradamus | `prophecy_tent` | Prophecy Roulette / doom-prophet performer | `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/hamstradamus.md` |
| Yolanda Kovarik | `prize_booth` | Prize redemption attendant | `Design/World Design/Debaucheryville/the_participation_trophy.md` |
| Chef Chuckles | `meat_cart_pitch` | Mystery Meat Cart vendor | `Design/World Design/Debaucheryville/mysterymeatcart.md` |
| Bobo "The Blockchain" Bitsworth | `performance_circle` | Failed street performer, balloon-animal pitch | `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/crypto_clown.md` |
| Blanka (knife-throwing assistant) | `performance_circle` | Target-board assistant; hands the role to the player for the dodge minigame | New — profiled below |

### Ringmaster Vance "Vape" Vallaro
- **Location Zone**: `big_top` (personal tent, adjoining the main dome)
- **Role**: Circus proprietor and Shady Productions owner-operator; the single point of contact tying every attraction on these grounds together
- **Appearance**: Ringmaster coat gone slightly threadbare at the cuffs, top hat at a showman's angle, a vape pen never more than a hand's reach away
- **Personality**: Speaks in unbroken sales patter with a vape cloud punctuating roughly every third sentence; genuinely proud of the operation, in the specific way of a man who has never once questioned whether pride was earned
- **Key Dialogue**: *"Loot crate? Sure. Sure, why not. It's — *(exhale)* — it's a bit of a gamble, honestly. Aren't we all? Walk your voucher over to the booth, Yolanda will sort you out."* / *"Semi-permanent. That's the word. We COULD move. We just — *(exhale)* — haven't needed to."*
- **Services/Function**: Hawks shady loot crates from his tent — existing canon, per `game_design_document.md` ("offers shady 'loot crates' from the prize booth"). Vance pitches and sells the voucher here; fulfillment happens at `prize_booth`, per canon, not at his tent (see Economic Integration above). No crate contents or pricing are specified in this document — that mechanic belongs to a future items/shop pass, not this stitching file
- **Cross-Reference**: Owner of Shady Productions, which operates The Bacchanus Beach Beatdown from `shady_productions_office` per `bacchanusbeachbeatdown.md`

### Blanka (Knife-Throwing Assistant)
- **Location Zone**: `performance_circle`, target board
- **Role**: Normally stands as the knife-thrower's live target; on interactive rounds, she steps aside and coaches the player through the dodge minigame instead
- **Appearance**: Sequined leotard gone matte with age, a professional's stillness, completely unbothered by the job description
- **Personality**: Dry, competent, has done this literally thousands of times and finds the tourists who volunteer for her spot far more alarming than the knives ever were
- **Key Dialogue**: *"You want my job? Fine. Stand there. Don't flinch — flinching is how you get hit. I flinch never."* / *"Eight thousand throws. Zero misses. He's better than the fax machine, and that's the highest compliment I hand out."*
- **Services/Function**: Gatekeeps the interactive knife-throwing dodge round; the throwing act itself is a fixture of `performance_circle`'s rotating schedule alongside Bobo's pitch

---

## Audio Design

### Environmental Audio
- **Ambient Soundscape**: Distorted calliope loop (grounds-wide base layer), Vance's vape exhale (proximity-triggered near `big_top`), distant hamster techno (bleeding faintly from `prophecy_tent`'s direction whenever Hamstradamus's dance-loop idle is active), fax-machine paper-feed hum from `shady_productions_office`, barker patter from `game_alley`
- **Music Style**: Warped, slightly-too-slow carnival calliope, consistent with the "hasn't traveled since 1997" framing
- **Audio Transitions**: Calliope volume drops noticeably inside `prophecy_tent` and `shady_productions_office` — both quieter, more contemplative zones by design
- **Interactive Audio**: Ticket-dispenser jam-and-release (`main_gate`), knife-throw whistle-and-thunk (`performance_circle`), fax-machine paper-spit chug (`shady_productions_office`)

### Comedy Audio Integration
- **Satirical Stingers**: A sad calliope note when a rigged game is lost; the fax machine's chug landing exactly on a beat when a bro reads the casting flyer aloud
- **Character Voice Direction**: Vance's dialogue is voiced with an audible exhale built into the pacing, not layered on after — every sentence has a vape-cloud-shaped pause in it
- **Environmental Comedy**: The distant hamster techno never resolves into anything a player can place — it's there, then a food-cart hiss cuts it off, every time
- **Social Media Audio**: The ticket booth's dispenser jam-and-clunk-and-eventually-dispense cycle is a natural short-clip capture

---

## Time-of-Day Variations

### Afternoon (14:00–18:00)
- Moderate crowd; all attractions active; Bubbles-adjacent hay smell strongest during big top feeding time
- Grounds at their most family-tourist-friendly appearance before the evening crowd shifts the tone

### Evening–Night (18:00–01:00)
- Peak crowd density; neon marquee active over `main_gate`; string lights along `game_alley`
- `icq_backroom` hotspot most active after dark — this is when Darkweb Dossier "hack-through" pop-ins are most likely to trigger
- Calliope volume and vape-cloud density both increase slightly, per Vance's own showmanship instincts

### Beatdown Filming Days (variable, per `bacchanusbeachbeatdown.md` production schedule)
- Hamstradamus is absent from `prophecy_tent`, relocated to Fauxst Beach as prize-giver (see `hamstradamus.md` — "on Beatdown filming days he is physically relocated to Fauxst Beach and is absent from the tent")
- `shady_productions_office` sees visibly increased foot traffic moving gear along the riverside path toward the Bohemian Riviera
- The casting-call fax runs more frequently, though it never prints anything but the same flyer

---

## Connected Locations

### Directly Adjacent
- **Old Town Streets**: Landward exit via `main_gate`
- **Riverside Embankment Path**: Runs from `shady_productions_office` to the Bohemian Riviera's embankment path

### Quest-Connected
- **The Bohemian Riviera**: Connected via the Shady Productions gear path — the same route documented in `bohemian_riviera.md`'s Connected Locations section: "Connected via the Shady Productions gear path along the riverbank — Ringmaster Vance 'Vape' Vallaro's television venture operates the Beatdown from a folding table with a fax machine behind the big top; Hamstradamus travels this exact route on filming days between the prophecy tent and `prize_podium`." This document keeps that connection reciprocal — the gear path terminates at `shady_productions_office` on this end.

### Sub-Location Files (stitched, not modified)
- `Design/World Design/Debaucheryville/the_participation_trophy.md` (`prize_booth`)
- `Design/World Design/Debaucheryville/mysterymeatcart.md` (`meat_cart_pitch`)
- `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/hamstradamus.md` (`prophecy_tent`)
- Bobo's profile (`performance_circle`) — see NPC table above for the exact file path

---

## Implementation Specifications

### Technical Requirements
- **Asset List**: Grounds tileset, main gate/marquee, big top exterior + Vance's tent + ICQ backroom flap, Shady Productions office props (folding table, fax machine, casting flyer, prize pallet), game alley rig, performance circle target board, Vance and Blanka NPC sprites — full list in the companion PNG Assets document
- **Animation Requirements**: Marquee flicker, vape-cloud text-reveal (Vance's dialogue), Prophecy Tent Glow (full spec in `Cirque_du_Shady_PNG_Assets.md`), fax-machine paper spit, ticket-dispenser jam cycle, knife-throw whistle-and-thunk
- **Performance Budget**: Target 45-60 FPS; max 30-45 draw calls (grounds-wide, crowd-density dependent); memory budget 55-70MB across the full stitched grounds (individual sub-locations retain their own already-specified budgets)
- **Platform Considerations**: Vape-cloud particle density reducible on mobile; grounds crowd LOD steps down aggressively past `game_alley` mid-ground

### State Tracking
```
cirque_du_shady_state:
  - cirque_visited: boolean
  - beatdown_aware: boolean
  - vance_met: boolean
  - filming_day_active: boolean
  - icq_backroom_hackthrough_seen: boolean
  - return_visit_count: integer
```

---

## Quality Assurance Checklist

### Pre-Implementation Review
- [x] **World consistency verified** — uses "Debaucheryville," "The Bacchanus," and "The Bohemian Riviera" exclusively; no real-world city names appear anywhere in this document
- [x] **Cultural specificity confirmed** — traveling-circus grift economy, not generic European carnival
- [x] **Satirical targets appropriate** — carnival grift economics and reality-TV recruitment psychology, never Czech people or performers as a class
- [x] **Gameplay value established** — central attraction-cluster quest hub, tying five previously-standalone sub-locations into one navigable parent
- [x] **Technical feasibility confirmed** — stitched-zone approach achievable within stated performance budget
- [x] **Bobo's existing backstory is referenced by file pointer only — no new elements introduced beyond that pointer**
- [x] **Seedy underbelly present** — grounds-wide grift pipeline, from rigged games through garbage prizes through unpaid TV recruitment
- [x] **Zero contradictions with existing sub-location canon** — the_participation_trophy.md, mysterymeatcart.md, hamstradamus.md, and Bobo's profile are referenced by file and ID only; no detail in this document restates or alters their established facts
- [x] **Zone tag names exact and stable** — `main_gate`, `big_top`, `prophecy_tent`, `game_alley`, `prize_booth`, `meat_cart_pitch`, `performance_circle`, `shady_productions_office`, `icq_backroom`

### Post-Implementation Testing
- [ ] All nine zone tags resolve to distinct, navigable areas
- [ ] Sub-location transitions (`prophecy_tent`, `prize_booth`, `meat_cart_pitch`, `performance_circle`'s Bobo pitch) hand off correctly to their own files' mechanics
- [ ] `beatdown_aware` and `vance_met` state triggers fire correctly
- [ ] Filming-day Hamstradamus absence from `prophecy_tent` reads correctly against `hamstradamus.md`'s own schedule table
- [ ] Riverside gear path connects bidirectionally with `bohemian_riviera.md`'s embankment path

---

## Development Notes

- This document's entire purpose is to stitch, not to re-author. Every fact about Yolanda, Chef Chuckles, Hamstradamus, and Bobo lives in their own files; this document links to them by exact file path and quotes only what's needed for grounds-level navigation. Any future edit to this file that restates their mechanics in more detail than a pointer risks drifting out of sync with the source files — don't.
- Zone tag IDs (`main_gate`, `big_top`, `prophecy_tent`, `game_alley`, `prize_booth`, `meat_cart_pitch`, `performance_circle`, `shady_productions_office`, `icq_backroom`) are load-bearing for a downstream task that builds directly on this file — do not rename them in a later revision without updating dependents.
- Vance's loot-crate contents, pricing, and the knife-throwing dodge minigame's full mechanical spec are intentionally left as hooks in this document, consistent with how `bohemian_riviera.md` treats its `night_party_zone` — grounds dressing and unlock conditions only, deferred to a future pass.
- The Vanishing Elephant ("Bubbles") sidequest is referenced as a hook per existing GDD canon and is not designed in this document.

---

## Final Validation

**The Cirque du Shady is the parent grounds document the Cirque's sub-locations have needed since the prize booth, the mystery meat cart, the prophecy tent, and Bobo's performance circle were each profiled independently. It adds a main gate that says exactly what it is, a big top that hasn't moved since 1997, a Ringmaster who sells gambles and calls them gambles, an ICQ backroom that occasionally lets the wrong people in, and a production office where a folding table and a twenty-year-old fax machine quietly produce a reality show that will, on a beach downriver, launch at least two out of every three people who sign up for it. Every sub-location keeps its own established facts untouched; this file only tells you how to walk between them.**
