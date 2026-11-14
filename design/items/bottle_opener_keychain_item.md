# Item Definition: Bottle Opener Keychain

*"Bottle Opener Keychain (16 Different Breweries)" — for opening beers with maximum jingling and zero class*

## 📋 Item Identity
- **Item ID**: `bottle_opener_keychain`
- **Display Name**: Bottle Opener Keychain
- **Internal Name**: The pre-loaded frat-bro keyring — ONE container item that every earned brewery opener clips onto [source: design/quests/general_quests/brewerytour.md L33-34]
- **Item Type**: Hybrid (Permanent Cosmetic + Quest Container)
- **Rarity**: Common origins (bros treat it as Legendary)
- **Source**: The Blarney Trap, Publandia — GRANTED the instant the bros order the special beer for the first time, together with The Blarney Trap's opener and the Brewery Passport Book [source: design/quests/general_quests/brewerytour.md L27-42]

---

## 🎭 The Deception

### What The Item Actually Is
A new, inexpensive bottle-opener keychain granted at The Blarney Trap, Publandia, as the entry key to the Brewery Tour. At acquisition, the metal is clean, the finish is intact, and the main ring has little or nothing hanging from it beyond its attachment hardware and any approved tour tag. It has no ancient patina, no spring-break souvenirs, no mystery keys, no hometown bar tokens, and no pre-European history.

Each completed brewery adds that brewery’s unique opener. The object gradually changes from a comically optimistic empty ring into a crowded record of the actual trip. Its wear, mismatched metals, weight, and noise are consequences of player progress—not invented backstory.

### What The Bros Believe It Is
At acquisition:

> “This is not an empty keychain. This is sixteen future credentials.”

At base-game completion:

> “Sixteen breweries. Four cities. One résumé that opens bottles.”

The joke is that the bros treat unused keychain hardware like a sacred commission on day one, then become even more insufferable as the collection finally gives them evidence.

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A — never sold. GRANTED on the Publandia special-beer order trigger (author ruling 2026-08-04) [source: design/quests/general_quests/brewerytour.md L27-34] |
| **Actual Value** | A handful of cheap, mismatched giveaway openers — marginal SOVS at most |
| **Resale Value** | 0 SOVS (worthless, and quest-critical besides) |
| **Can Be Sold** | No |
| **Can Be Dropped** | No (permanent quest container) |
| **Can Be Traded** | No |

---

## 🎨 Visual Specifications

### Confirmed Visual Requirements

- The keychain is **newly acquired at The Blarney Trap, Publandia**.
- It begins **new, clean, and nearly empty**.
- It is one shared collection object, not a pre-existing personal keepsake for any one bro.
- It visually accumulates **16 unique base-game brewery openers**: 4 from each of the 4 base-game cities.
- Expansion breweries remain a separate progress set and must not alter the visual or UI meaning of `16/16` base-game completion.
- Any grime, scratches, mismatched finishes, crowding, or loud jingling must appear progressively as openers are earned.

### Physical Appearance — PROPOSED Production Design

The following design is concrete enough for concept generation and sprite production, but its unverified choices require visual-direction approval.

| Attribute | Proposed Description |
|---|---|
| **Primary Ring** | One circular polished stainless-steel split ring, approximately 35 mm in diameter, sturdy but visibly mass-produced; bright cool-silver highlights; no rust, tarnish, dents, or stretched coils at acquisition |
| **Attachment Hardware** | A short three-link steel chain connected to a compact swivel snap hook sized for a belt loop; hardware is clean, symmetrical, and recently manufactured |
| **Tour Identifier** | A small flat enamel tag on the short chain, proposed as a rounded rectangle with deep Publandia green enamel, cream lettering, and a thin warm-gold border; text: `BREWERY TOUR`; no real-world brand or city name |
| **Starting Load** | The ring itself plus approved attachment hardware/tag; zero earned brewery openers before the first brewery reward. The Blarney Trap's opener is granted in the same moment as the keychain, so the art should support an immediate `0 → 1` update rather than depicting the item as preloaded |
| **Earned Openers** | Sixteen visually distinct opener silhouettes and finishes, each defined by its own brewery item document; they attach to the main ring only when earned |
| **Initial Condition** | Factory-clean metal, crisp enamel, clean edges, no patina, no residue, no stickers, no bent parts, and no unexplained keys or souvenirs |
| **Progressive Wear** | Very light contact scratches begin after several openers; minor edge wear and metal-on-metal scuffing appear late in the collection; never imply years of ownership |
| **Full Base-Game Silhouette** | Dense, irregular fan of 16 opener shapes hanging from one ring; crowded and overconfident but still readable as a recently assembled travel collection |
| **Expansion Treatment** | **PROPOSED:** expansion openers attach to a smaller secondary ring or extension link so they are visually grouped apart from the completed 16-opener base-game fan |

### Initial and Progressive Visual States

| State | Trigger | Required Visual Read | Wear / Sound Direction |
|---|---|---|---|
| **State 0 — Newly Acquired** | Keychain obtained; no brewery opener earned yet | Clean main ring, clip, short chain, and approved tour tag; abundant empty space | Pristine; almost silent except for one light metal click |
| **State 1 — First Opener** | First brewery reward | One unique opener hangs freely with plenty of unused ring space | Clean; a small two-piece clink |
| **State 4 — First City Complete** | 4/16 base breweries | Four distinct openers form a readable loose fan; first-city set is visually complete | Faint contact scuffs; short jingle during movement |
| **State 8 — Two Cities Complete** | 8/16 base breweries | Ring looks busy and uneven; shapes overlap without becoming an unreadable metal blob | Noticeable jangle; light edge wear |
| **State 12 — Three Cities Complete** | 12/16 base breweries | **TBD** | **TBD** |
| **State 16 — Base Tour Complete** | 16/16 base breweries | Full, ridiculous fan of sixteen unique openers; tour tag remains barely visible as the organizing anchor | Loud layered jingle; fresh-travel wear only, never antique patina |
| **Expansion State — Separate** | Expansion brewery opener earned | Additional opener appears in the approved expansion grouping without changing the `16/16` base silhouette or count | Separate optional accent/chime; final treatment **TBD** |

### Art-Generation Brief — PROPOSED

**Primary concept prompt:**

> A newly manufactured bottle-opener keychain for a satirical 1990s/early-2000s-inspired retro JRPG, isolated three-quarter view on a transparent background. One bright polished stainless-steel split ring, a short three-link chain, and a compact clean swivel snap hook. Add one small rounded-rectangle enamel brewery-tour tag in deep green, cream, and warm gold, with simple readable “BREWERY TOUR” lettering. The ring is intentionally almost empty, with abundant visible space for future collectible openers. Factory-clean surfaces, crisp edges, controlled specular highlights, chunky readable silhouette, playful mundane-object-as-legendary-treasure presentation. No existing souvenir collection, no old keys, no rust, no tarnish, no grime, no antique patina, no real brands, no real city names, no background scene, no hand holding it.

**Progression-sheet prompt:**

> Create an orthographic item progression sheet of the same bottle-opener keychain as brewery openers are earned. Keep the steel ring, short chain, snap hook, and green enamel tour tag identical in every stage. Add only earned openers between stages. Every opener has a unique silhouette and material treatment; the collection grows from sparse and clean to crowded and loudly mismatched. Wear develops only as light travel scuffs from metal contact. The final sixteen-opener version is dense and ridiculous but each opener remains distinguishable. Transparent background, consistent scale, consistent lighting, no extra keys or charms, no aged or inherited look.

**Negative prompt / exclusions:**

- No rust, verdigris, heavy tarnish, dirt, grease, chipped antique plating, or decades of wear
- No car keys, house keys, USB drives, spring-break charms, hometown tokens, mystery souvenirs, or preloaded opener pile
- No real brewery logos, real alcohol brands, or real place names
- No leather fob, lanyard, pocketknife, weapon silhouette, magical glow, gems, or luxury jewelry treatment
- No illegible microtext beyond the approved tour-tag lettering
- No photographic background, tabletop, hand, pocket, or belt-loop scene in the isolated item master

### Production Deliverables — PROPOSED

| Asset | Proposed Requirement |
|---|---|
| **Concept Master** | Transparent-background source with the State 0 item fully separated into ring, chain/clip, tour tag, and opener attachment layers |
| **Progression Sheet** | Matched views for each visual state; identical camera, scale, and light direction |
| **Inventory Icons** | Clean pixel-art redraws derived from the approved concept, with separate icons per visual state; exact pixel dimensions **TBD by UI pipeline** |
| **Overworld Accessory** | Simplified hip-level silhouette states for sparse, mid, and full collection; only if persistent on-character visibility is approved |
| **Individual Opener Layers** | One layer/sprite per brewery opener so acquisition can update the collection without repainting the whole keychain |
| **Palette Discipline** | Bright cool steel for shared hardware; opener-specific palettes carry brewery identity; follow the binding HD-2D style guides (`design/style_guides/`) for readability rather than photoreal material noise |
| **Transparency / Cropping** | Alpha background; centered object; padding sufficient for the State 16 swing arc; no baked shadow outside an approved icon treatment |

---

## 📊 Stats & Effects

### Direct Stats

```text
Combat Stats:        None beyond Party Prep below
Party Stats:         Party Prep = +1 Bravado per completed city, applied at battle start (v44 ruling)
Bartender Discount:  5% per completed city, max 20% (v44 ruling)
Item Tier:           Tier B "Credentials" (gates opener collection)
Collection Capacity: 16 base-game brewery openers
Expansion Capacity:  Tracked separately; +2 breweries per expansion city per supplied source
```

The earlier `Party Prep +3`, `Bro Credibility +1`, and `Airport Security -1` values are superseded by the author's round v44 ruling above (Party Prep = +1 Bravado per completed city at battle start; bartender discount 5% per completed city, max 20%). `Bro Credibility` and `Airport Security` remain unsupported.

### Passive Effects

| Effect | Status | Description |
|---|---|---|
| **Brewery Tour Access** | **CONFIRMED** | The Brewery Tour sidequest is unavailable until the party has acquired the keychain at The Blarney Trap, Publandia |
| **Tier B "Credentials"** | **CONFIRMED (v44)** | Gates opener collection |
| **Bartender Discount** | **CONFIRMED (v44)** | 5% per completed city, max 20% |
| **Party Prep** | **CONFIRMED (v44)** | +1 Bravado per completed city at battle start |
| **Opener Collection Tracking** | **CONFIRMED FUNCTION / PROPOSED IMPLEMENTATION** | Adds one brewery-specific opener to the collection when that brewery’s completion condition is met; UI displays base progress out of 16 |
| **Regional Beer Unlock** | **CONFIRMED QUEST EFFECT** | Finding/completing a brewery unlocks its regional beer as a consumable; this reward belongs to the Brewery Tour loop, not an item stat bonus |
| **Progressive Appearance** | **USER-DIRECTED; IMPLEMENTATION PROPOSED** | Visual state updates as openers are earned so the keychain changes from nearly empty to crowded |
| **Progressive Jingle** | **PROPOSED COSMETIC** | Sparse states produce isolated clicks; later states produce a fuller jangle. Audio must be event-based and must not become a constant intrusive loop |

### What It Does NOT Do

- It does not arrive old, tarnished, overloaded, or full of pre-trip memories.
- It does not contain openers from breweries the player has not completed.
- Expansion breweries do not change the base-game `16/16` achievement requirement.
- It does not grant exclusive local brews, cultural respect, secret-area access, or dialogue gates unless those mechanics receive a separate author ruling. Its bartender discount is capped at 5% per completed city, max 20%.
- It does not provide combat, travel, or security modifiers beyond Party Prep (+1 Bravado per completed city at battle start).

---

## 🎯 Gameplay Integration

### Permanent Hybrid Change

**Confirmed:** possession of the newly acquired Publandia keychain gates access to the Brewery Tour, and brewery discoveries add their openers to the collection.

**Confirmed (author round v44):** Tier B "Credentials" gates opener collection; bartender discount is 5% per completed city, max 20%; Party Prep is +1 Bravado per completed city at battle start.

**PROPOSED implementation:** once acquired, the item stays in the party’s permanent key-item inventory and cannot be discarded. Its collection UI exposes two separate progress groups:

```text
BASE TOUR       0/16 → 16/16
EXPANSION TOURS separate 0/2 group per expansion city
```

The base completion flag must read only the sixteen base-game opener records. Expansion records may share the same item screen but cannot be included in the denominator or required for the base reward.

### Sprite Implementation — PROPOSED

- **Inventory visibility**: Always shown in the Key Items / Brewery Tour collection UI after acquisition.
- **Overworld visibility**: Optional hip/belt-loop overlay; requires author and animation approval because the supplied sources do not establish which bro wears the shared party item.
- **Layer**: If approved, accessory overlay at waist/hip level, behind the forward arm and in front of torso/leg layers as pose requires.
- **State switching**: Use sparse (`0–3`), first-city (`4–7`), two-city (`8–11`), three-city (`12–15`), and full (`16`) silhouette tiers for overworld readability; preserve exact per-opener detail in the item/collection screen.
- **Animation**: Two-frame delayed sway on walk cycles; settle frame on idle; no perpetual motion while standing.
- **Audio**: Trigger short clink/jingle samples on movement starts, stops, sprints, falls, or inspection events. Scale layer count by collection tier; do not run a constant loop beneath dialogue or music.
- **Expansion rendering**: Expansion openers use a separate attachment group or UI tab, subject to visual-direction approval.

### Peak Frat Bro Cringe

- They display an almost empty ring like an accreditation badge immediately after acquiring it.
- Every new opener becomes evidence that they are “basically in the industry.”
- The collection starts quiet enough to ignore and ends loud enough that they mistake nuisance for prestige.
- They can identify every opener’s brewery but still cannot identify whose turn it is to buy the next round.
- The full collection weighs down the approved wearer’s cargo shorts only after the player has actually earned enough metal to justify the gag.

---

## 🗣️ NPC Reactions

### When NPCs Notice The Keychain
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| European Bartenders | Offer better prices and exclusive local brews because "you clearly know your beer" | "We're basically locals now" |
| Gatekept Pub NPCs | Won't talk to you without "proper beer credentials" | *bros just flash the keychain like a badge* |
| Debaucheryville Locals | ⚠ AUTHOR-REVIEW: "Ah, you have the One True Pils opener! You understand REAL beer, not American water!" | "We're basically beer sommeliers now" |
| Prostoberg Locals | ⚠ AUTHOR-REVIEW: Beer-festival NPCs treat you like family instead of tourists | "We've been adopted" |
| Abbeyvale Monks | ⚠ AUTHOR-REVIEW: The Brothers of Our Lady of Perpetual Hops actually let you into their secret brewery areas | "We're basically monks now" *(they are not)* |
| Publandia Pub Crawl Guides | Offer you the "locals only" route | "VIP treatment, obviously" |

### Callback Dialogue Throughout Game
**Chadwick** (admiring the collection):
> "Bro, remember when we got this one at that sketchy beach bar?"

**Bradley** (reminiscing):
> "Dude, that's where you hooked up with that girl with the fake ID!"

**Lord Pilsner** (declaring intent):
> "Gentlemen, our European adventure demands we add to this legendary collection!"

---

## 🔗 Quest Integration

### Source Quest
- **Quest Family**: Brewery Tour (16 breweries, 4 cities × 4) [source: design/quests/general_quests/brewerytour.md L12]
- **Quest Giver**: Seamus, owner of The Blarney Trap
- **Location**: The Blarney Trap, Publandia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| The entire Brewery Tour sidequest | The one-time trigger: ordering the special beer at The Blarney Trap, Publandia [source: design/quests/general_quests/brewerytour.md L27-31] |
| Each brewery's stamp, brewmaster selfie, opener, and signature beer | Completing that brewery's challenge while carrying the keychain [source: design/quests/general_quests/brewerytour.md L45-58] |
| Better bartender pricing and exclusive local brews | Simply possessing the keychain, anywhere in Europe |

### Achievement
None directly on this item — see `brewery_passport_book_item.md` for "Continental Beer Master" and "Photogenic Drinker." The "Key Collector" achievement (own-all-openers) was ruled DEAD as redundant under the earned-opener model, 2026-08-05 [source: docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md, Salvage 28 ruling].

---

## 🎬 Key Story Moments

### The Trigger (Acquisition)
*At The Blarney Trap, Publandia, the bros order the special beer for the first time — the one-time event that opens the entire tour.* [source: design/quests/general_quests/brewerytour.md L27-31]

The keychain, The Blarney Trap's opener, and the Brewery Passport Book change hands together in that single moment. Before this order, no brewery anywhere will hand over a stamp, sell a signature beer, or part with an opener — the tour does not exist for the player until this fires. [source: design/quests/general_quests/brewerytour.md L40-42]

---

## 🖥️ Performance & Assets

### Sprite Requirements — PROPOSED

- **Inventory master**: one modular keychain base plus individual brewery-opener layers.
- **Base visual checkpoints**: the visual states above for concept/reference; production may compress overworld rendering into five tiers (`0–3`, `4–7`, `8–11`, `12–15`, `16`).
- **Individual opener assets**: sixteen base-game opener sprites or layer definitions, one per brewery; expansion openers live in a separate asset group.
- **Silhouette priority**: at small scale, show the ring/clip and total collection mass; do not attempt unreadable inscription detail.
- **UI detail priority**: the inspection/collection screen may show individual opener materials, inscriptions, and brewery identity.
- **Animation**: small sway/settle motion only; no physics simulation required.
- **Audio set**: at most four collection-tier variants (empty click, sparse clink, medium jingle, full jangle), triggered contextually.
- **Accessibility**: keychain audio follows SFX volume and any repeated-sound accessibility control; visual progress must never rely on sound alone.

### Performance Impact

- Prefer a precomposed sprite per overworld tier over rendering sixteen independent physics objects.
- Build the detailed inventory view from cached layers or precomposed milestone images.
- Do not run a persistent ambient jingle loop.
- No particles, dynamic lighting, cloth simulation, or real-time metal physics are required.
- Expansion assets should load with expansion content and should not enlarge the base-game completion array.

### Suggested Data Separation — PROPOSED (bead Eurobound-vyn)

```text
base_brewery_openers:      0..16
base_brewery_complete:     base_brewery_openers == 16
expansion_brewery_sets:    one independent 0..2 record per expansion city
visual_tier_base:          empty | sparse | first_city | two_cities | three_cities | complete
visual_tier_expansion:     separate optional attachment state
```

This is a documentation-level proposal, not a verified save-schema or implementation mandate. It stays a proposal under bead Eurobound-vyn until the author rules on it.

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ✅ |
| Acquisition (grant trigger) documented | ✅ |
| Stats and effects specified | ✅ |
| Visual specifications complete | ✅ |
| NPC reactions documented | ✅ |
| Quest integration clear | ✅ |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |
| 16-brewery count used throughout | ✅ |
| No real-world place or brand names remain | ✅ |

---

## 📝 Development Notes

- **Degradation Over Time section omitted** — the keychain accumulates (openers added across the 16-brewery tour) rather than degrading; a decay table would misrepresent it, per this task's omit-what-doesn't-fit instruction.
- **Per-Character Variants section omitted** — the keychain is ONE shared party item, not per-bro [source: design/quests/general_quests/brewerytour.md L33-34].
- **Distinction From Equipment section omitted** — no equippable counterpart exists for this item.
- **Six real-world references replaced** with author-approved parody stand-ins, per the Gap 21–26 ruling (2026-08-05, batch-reviewed): a Mexican spring-break resort → Blackout Bay; a Florida spring-break beach strip → Hangover Shores; a real chain party bar → Señor Sloppy's; a real German beer-festival city → Prostoberg; a real monastic brewing tradition and its home country → Abbeyvale/the Brothers of Our Lady of Perpetual Hops; a real legendary lager brand and its home country → Lagerovia/The One True Pils. All flagged ⚠ AUTHOR-REVIEW inline above; every one of these is a background-flavor reference only, not a new visitable location. [source: docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md Gap Manifest #21-26 and Rulings]
- Purchase language fully retired: this item is never bought, never a Pint-Off reward — granted once, on the trigger, full stop [source: design/quests/general_quests/brewerytour.md L27-34].

---

## Author copy (round v43, 2026-11-12)

**[CANON — author, round v43, 2026-11-12]** The author's Bottle Opener Keychain copy, fields 1-8, verbatim. Where it disagrees with anything above (opener count included), that is an open conflict for the author, not resolved here.

### 1. Tagline

> *"Sixteen terrible decisions' worth of empty ring, waiting for verifiable proof that we are industry professionals."*

### 2. Description

> A brand-new, factory-clean stainless steel split ring equipped with a short three-link chain, a swivel snap hook for a belt loop, and a deep green-and-gold enamel tag stamped **BREWERY TOUR**. At acquisition in Publandia, it is starkly, embarrassingly empty—devoid of old keys, scuffs, or prior history.
>
> As the bros complete brewery challenges across the continent, each earned bottle opener attaches to the main ring like a mismatched badge of honor. By the end of the base tour, it transforms into a dense, deafening, overconfident fan of sixteen unique metal silhouettes that jingles loudly enough to clear a hostel hallway at three in the morning.

### 3. Collector's Thesis

> "Anyone can buy a souvenir bottle opener at a tourist trap, chat. But an officially issued tour keychain with sixteen modular slot capacity? That’s not a keyring. That’s a mobile accreditation framework. Every opener we add isn't just a piece of stamped steel; it’s a verified node in our continental drinking infrastructure. While the locals look at us like we’re just three guys making a racket in a stairwell, we’re carrying sixteen proofs of stake. On the ring. Forever."

### 4. What the Picture Actually Shows

An inventory icon of modular keychain hardware rendered in crisp, clean pixel art that dynamically updates as milestones are cleared.

* **The Base:** A polished, unmarred stainless steel split ring and a gleaming green enamel "BREWERY TOUR" tag.
* **The Progression:** Starts as a lonely, silent loop with zero openers. Grows progressively cluttered with sixteen bizarrely shaped regional openers—from Celtic harps to microchip-engraved vault keys—clinking together in an increasingly aggressive visual mass.
* **The Flaw:** Even at maximum capacity (16/16), the green enamel tour tag remains perfectly pristine and factory-bright, wedged stubbornly at the front like a nametag worn by someone who arrived an hour early to their own corporate team-building seminar.

### 5. Its 'Format Crime'

> **The Acoustic Terror Index:** The item has no digital compression errors, but its *physical* format crime is purely auditory. Because the developers programmed a dynamic metal-on-metal jingle sound effect that scales directly with the number of attached openers, walking across any quiet indoor tile map after collecting eight or more openers triggers an inescapable, high-decibel cascade of clinking steel that alerts every NPC within three rooms and ruins every stealth sequence in the game.

### 6. How it Hangs in the Inventory / Claw Cabinet

> Clipped proudly and prominently to Chadwick's right belt loop at all times, swinging violently with every exaggerated stride he takes. In the inventory menu, it occupies a dedicated key-item slot where you can manually inspect each dangling piece of metal, though doing so forces Lord Pilsner to read out the inscription of every single opener as if reading from an architectural blueprint.

### 7. Media Type

> `Dynamic Modular Key-Item Container with 16 Progressive Sprite States`

### 8. Each Bro's Reaction Line

* **Lord Pilsner** (flipping the nearly empty ring between his fingers at the Publandia bar):
> "Look at that spacing, gentlemen. Sixteen slots. Zero clutter. We aren't just drinking our way across Euromemeia; we’re curating a physical ledger of institutional hospitality. Pass me that pint."

* **Chadwick** (shaking his hip aggressively so the keychain rattles into his phone microphone during a live stream):
> "Chat, listen to that. *[Single quiet click]* That is the sound of zero leverage. But give us four breweries in Debaucheryville and that ring is going to sound like a toolbox falling down a fire escape. We are scaling rapidly."

* **Bradley** (staring expressionlessly at the ring while leaning against a damp stone wall):
> "It jingles when I walk. That means people know I'm arriving before I get there. That's efficiency."
