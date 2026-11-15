# Rest points and rest rules: proposal (Debaucheryville)

**Status:** PROPOSED. Nothing here is canon until the author rules on Eurobound Desk card `Eurobound-8snp-q1`.
**Bead:** Eurobound-8snp. **Date:** 2026-11-15.
**What this is:** a list of every place the Debaucheryville docs already let the bros sleep, the rest rules already ruled, and the rules proposed to fill the holes. No game data, design doc or code was changed. No bed, host, price or number was invented.

## The short version

- The docs already have **9 rest spots**: 1 hostel (5 room types) and 8 hosts who offer a crash spot.
- **8 rest rules are already ruled.** **8 more are proposed** below.
- **7 numbers or decisions** are left blank for the author (section 5).
- The engine can already run a rest (`game/core/game_clock.gd:64`, `game/core/rest_events.gd`). Nothing in the game calls it, and the hostel is not in the engine data at all.

## 1. Every rest spot in the docs

Paths are under `design/worlds/debaucheryville/` unless they start with `design/quests/`. "Chronicles" is `design/quests/debaucheryville/couchsurfingchroniclesdebaucheryville.md`.

### 1a. The hostel (paid beds)

Hostel "Midnight Checkout", Hostel Row. The doc calls it "Primary Accommodation / Rest Point" (`hostel_midnight_checkout.md:12`) and "Primary rest point for Debaucheryville" (`:321`). Gate: reception. "Check-in: Anytime (if reception is staffed)" (`:104`); staff are Receptionist Radek (`:231`) and a Day Receptionist (`npcs/Hostel_Midnight_Checkout/hostel_midnight_checkout_npcs.json:26`). Rest verb in the location JSON: `hmc_sleep`, "Attempt to Sleep", needs `hostel_checked_in` (`interactions/hostel_midnight_checkout_interactions.json:21-30`).

| Room (doc wording) | Price | Sleep Quality (doc) | Source |
|---|---|---|---|
| 12-Bed Mixed Dorm, "The Full Experience" | 12 SOVS | Poor | `hostel_midnight_checkout.md:151` |
| 8-Bed Mixed Dorm, "Slightly Less Chaos" | 16 SOVS | Fair | `:152` |
| 6-Bed Mixed Dorm, "The Compromise" | 20 SOVS | Decent | `:153` |
| 4-Bed Private-ish, "We've Given Up on Budget" | 28 SOVS | Good | `:154` |
| Private Room, "Why Are We at a Hostel?" | 45 SOVS | Excellent | `:155` |

What the doc says a night does (`:165-170`): "Excellent Sleep: Full HP/Bravado restoration, +10% stats next day"; "Good Sleep: Full HP/Bravado restoration"; "Fair Sleep: 80% HP/Bravado restoration"; "Poor Sleep: 60% HP/Bravado restoration, "Groggy" status (2 hours)"; "No Sleep: 40% HP restoration, "Exhausted" status (affects all actions)". It also lists eight random roommate events with chances (`:173-182`) and "Status Effects: Clear negative statuses (mostly), risk new ones (roommate dependent)" (`:323`).

**Engine:** not known. No hostel location, bed or booking exists in `game/assets/data`. The only mentions are two flag notes: "Hostel rest while Gush-Locked" and "Any hostel rest while Sugar Rush Hour is active" (`game/assets/data/world_data/quest_flags.json:984`, `:1291`).

### 1b. Hosts (crash spots)

All hosts are optional. Each one gates her or his own spot, and the Herp four-state routing can refuse the bros (Chronicles `:485-500`).

| # | Host and where you meet | Where the bros sleep (doc wording) | Cost / result in the doc | Source | Engine |
|---|---|---|---|---|---|
| 1 | QUEEN Riviéra Renata, night party at the Bohemian Riviera | "Lord Pilsner cocooned in a sleeping bag" on Fauxst Beach | "No SOVS loss, no gag trinket, no stat payout"; `the_herp`; leopard-print thong | Chronicles `:25-50`; `design/quests/debaucheryville/nothingisgettingthrough.md:94`, `:138` | Not in the couchsurf data file |
| 2 | Vape Witch Vanessa, Velvet Curtain Club | "the couch" (State 4: "Sixty SOVS. Floor, not the couch") | "+Bravado restored (if you answer her crystal quiz correctly) or Confused status"; Charged Quartz Vape Tip | Chronicles `:58-72`, `:83`, `:120` | Data only: `couchsurfing_chronicles_debaucheryville.json:3` |
| 3 | Backpack Girl Who Never Left, Absinthe Arcade | "the floor"; "One night, one bro (she picks)", "Free", "Zero sleep" | "-10 Bravado (you didn't sleep)"; Ballad of the Bros | Chronicles `:129-142`, `:153`; `npcs/Absinthe_Arcade/backpack_girl_who_never_left.md:156` | Data only: same file `:22` |
| 4 | CryptoBro69's "Ex", Shadow Exchange | "Wake on futon under buzzing CRTs and LED strips, she's gone" | "Hungover status"; "Lose 25 SOVS"; scratched Millennium Bug | Chronicles `:204-218`; `shadowexchange.md:133-134` | Data only: same file `:32` |
| 5 | Suspicious Twins (Polina & Paulina), Cirque du Shady | "Their flat (couchsurf interior)"; "A place to crash (paired)", "Free" | "Embarrassed status applied"; Twin Token | Chronicles `:295-308`; `npcs/Cirque_du_Shady/suspicious_twins_polina_paulina.md:127`, `:184` | Data only (Polina's id): same file `:42` |
| 6 | Miss Morphine, ICQ pop-up | "You wake up in a neon-lit room full of Y2K tech, VHS tapes, and expired party pills" | "Buff: Inspired (+Charm/Crit)"; discarded USB | Chronicles `:394-408`; `npcs/_unassigned/miss_morphine.md:117` | Data only: same file `:52` |
| 7 | "The Philosopher", The Absinthium Taproom | Not said. "a regular who's been here so long they might be part of the furniture" | "Rest partially restores HP/Bravado (50%)"; "Existentially Rested" status: +5 INT, -5 Bravado (2 hours) | `the_absinthium_taproom.md:277-283` | Not known |
| 8 | "CryptoBro69 Himself", Ye Olde B.R.E.W. Lab, after the boss | "Wake on RGB gaming chair surrounded by dead monitors" | "Gain Blockchain Bock x2, Hungover status, -15 SOVS" | `ye_olde_brew_lab.md:251-256` | Data only: `game/assets/data/locations/debaucheryville/debaucheryville_interactions.json:2110-2122` |

"Data only" means a JSON record exists and no scene or script uses it (bead Eurobound-j1h6).

### 1c. Sleeping in the docs that is not a bro rest spot

Listed so nobody builds one by mistake.

- **The Green Fairy statue's arms** (Arcade restroom): Jakub sleeps there, not the bros. "Jakub 'Tokens' Dvorak sleeps in her arms from 01:00 until morning" (`location_nodes/absinthe_arcade_restroom_location_nodes.json:34`).
- **Tram Stop #17 bench:** the interaction is "Sit with Jiří" (`interactions/tram_stop_17_interactions.json:326-334`). Sitting, not sleeping.
- **Donát's mattress** (Euro Ink 4 Less back room): "Donát's living quarters. Mattress on floor... He lives here." (`location_nodes/euro_ink_4_less_location_nodes.json:141`).
- **The street outside the Arcade:** after losing to Accounts Receivable "the bros wake on the street outside at 1 HP" (`villains/absinthe_arcade/accounts_receivable.md:199`). That is a defeat, not a rest.
- **Cirque du Shady grounds:** `couchsurf_integration` says `"available": false` (`environment/cirque_du_shady_environment.json:47-50`). The Twins' flat is the spot, not the circus.

## 2. What is already ruled

1. **A rest jumps the clock to the next 10:00.** "'Morning' is the next rest, which jumps the clock to 10:00" (`docs/superpowers/NEXT_WORK.md:670`). Built: `game/core/game_clock.gd:64`. No minute cost for a rest is ruled, and none is needed.
2. **Venues throw the bros out at closing.** Same line (`NEXT_WORK.md:670`). Time moves only when the bros act (`:667`).
3. **The game saves only at hotspots and beds, in 3 slots. No autosave.** "No autosave for now: hotspots and beds only"; slots: "3" (`NEXT_WORK.md:892`, Desk x2ws-q1 and q2; this replaces `:700`).
4. **A rest ends these statuses:** the four Legendary Hangovers, "the cure item and sleep still end it at any time" (`NEXT_WORK.md:887`; `design/quests/debaucheryville/brewerytourdebaucheryville.md:352`); Cottonmouth, "until the bro drinks or rests" (`NEXT_WORK.md:912`); a Space Cake Timer that has not landed, "rest clears an unlanded timer", and Contact High and Space Cake Gamble (`NEXT_WORK.md:863`); The Munchies, "ends at rest" (`NEXT_WORK.md:907`); Canal Courage Hungover, cured by "sleep" (`NEXT_WORK.md:849`). In data, Sugar Rush Hour, The Shakes and Wobbly Windmill also end on rest (`game/assets/data/skills/status_effects.json:9`, `:162`, `:187`, `:209`).
5. **Rest events run before the status is removed.** The Speedcakes deep clean and the Mango Munchies Tax fire at a rest (`docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md:76`, `:288`; approved, `NEXT_WORK.md:828`). What the deep clean throws away and what the tax takes are still open, so today only a flag is set (`game/core/rest_events.gd:44-52`).
6. **Sober comes back at a rest** (Shamsterdam Navigation, Eurobound-eb8; `game/core/navigation_roll.gd:154`).
7. **Couchsurf nights follow the author's standing rule.** "one girl means one bro sleeps with her, and it is never polite, good sex. The bros are doofuses and wake up to hilarious and/or horrifying results: robbed, she's gone, an STD, beaten up for sleeping with someone's girl" (`NEXT_WORK.md:736`). Each host has four Herp states and "Payload is granted once" (Chronicles `:489-500`).
8. **Rest never comes with a lesson.** "No obligatory moral lectures" (`design/mechanics/intoxication_law.md:18`); "Intoxicants do not provide uncomplicated, consequence-free advantages" (`design/narrative/bros_choose_debauchery.md:16`). Bradley's TROUSER SNAKE loss lasts "until the next in-game morning" (`intoxication_law.md:72`).

Also written, not checked as a ruling: the coin roster reshuffles on "hostel/hotel rest" (`docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md:89`).

## 3. Proposed rules

9. **The rest spots for Debaucheryville are the ones in section 1, and no others.** The hostel and the hosts the author keeps (see gap G1).
   *Why:* they are the only places the docs let the bros sleep.
   *Rejected:* sleeping anywhere (benches, the street). It would make closing time and the hostel price mean nothing. *Rejected:* hostel only. The host mornings are already written as the next morning.
10. **Every rest spot runs the same rest.** Rest events, status endings, Sober back, clock to 10:00 (rules 1, 4, 5, 6). A host night counts as a rest; the morning scene plays first, and the watch reads 10:00 when the player has control again.
   *Why:* the ledger says morning is the next rest, and every host entry is a morning scene.
   *Rejected:* host nights as scenes that leave the clock alone. The bros would wake up "the next morning" at 01:00.
   *Note:* some scenes name an hour ("6am", "07:00 sharp", Chronicles `:122-124`, `:133`). Those lines stay as written; only the watch afterwards says 10:00.
11. **The bros can rest at any hour.** A rest always wakes them at the next 10:00.
   *Why:* the hostel doc says "Check-in: Anytime" (`hostel_midnight_checkout.md:104`).
   *Rejected:* night only. It needs a new rule and a refusal line nobody has written.
12. **The hostel is pay first.** The bros book a room type at reception, pay its price in SOVS, then use the bed. Not enough SOVS means no bed. Hosts cost exactly what their entry says.
   *Why:* "Registration: Name, passport, nights staying, payment" (`hostel_midnight_checkout.md:143`).
   *Rejected:* a tab paid in the morning. No doc gives the hostel a tab.
13. **What a rest restores depends on where the bros slept.** At the hostel, the room type sets it, using the doc's sleep-quality list once the author confirms the numbers (N2). At a host, the night restores only what that host's entry says, and nothing where the entry is silent until the author says otherwise (N4).
   *Why:* it is what the docs already say, and it keeps the 45 SOVS room worth buying.
   *Rejected:* every rest fully refills HP and Bravado. It would make the room types pointless and turn a free host night into a free heal, which Backpack Girl's "-10 Bravado (you didn't sleep)" contradicts.
14. **Saving is offered at the hostel bed, before the bros sleep. Host spots do not save.**
   *Why:* the ruling says "beds"; a couch, a futon and a beach are scripted scenes, and a Wi-Fi hotspot covers saving elsewhere.
   *Rejected:* every rest spot saves. It would put a save prompt inside the host scenes.
15. **The first rest point built is the hostel's 12-Bed Mixed Dorm at 12 SOVS, with no roommate events and no random sleep roll.** The other rooms, the roommate events and the Bunk Bed Confessions come later, each after its numbers are ruled.
   *Why:* it is the cheapest bed and the hostel's own subtitle ("12 SOVS/Night. Your Dignity Costs Extra.", `hostel_midnight_checkout.md:9`), and it needs the fewest unruled numbers.
   *Rejected:* building the whole sleep system at once. Its eight event chances and five outcome tiers have never been ruled.
16. **Statuses with no rest rule stay as they are.** Gush-Locked and a waiting Crash are not ended by a rest until the author rules (`status_effects.json:58`, `:122`, `:129`).
   *Why:* the data already says "pending author" for both.
   *Rejected:* a rest clears everything. It would wipe a Crash the author ruled must wait for a fight (64vo-q2, `NEXT_WORK.md:875`).

## 4. Where the docs disagree with a ruling or with each other

- **Autosave.** The hostel doc says "Save Point: Auto-save on check-in and checkout" (`hostel_midnight_checkout.md:324`). The newer ruling says no autosave (rule 3). The ruling wins; the doc line is stale.
- **Hostel prices.** Three versions: the room table 12 / 16 / 20 / 28 / 45 SOVS (`hostel_midnight_checkout.md:151-155`); "12-35 SOVS/night" (`:18`); and the items JSON with three bookings at 12, 35 and 45 SOVS (`items/hostel_midnight_checkout_items.json:5-27`). See N1.
- **How many hosts.** The Chronicles premise says "1-2 opportunities to crash with NPCs per city" (Chronicles `:6`). The docs give Debaucheryville 8.

## 5. Numbers and decisions for the author

None of these is filled in.

- **N1. Hostel prices.** Which list is right: five rooms (12 / 16 / 20 / 28 / 45 SOVS) or three bookings (12 / 35 / 45 SOVS)?
- **N2. What each hostel room restores.** The doc's figures (100% plus "+10% stats next day", 100%, 80%, 60%, 40% HP) were never ruled. Confirm or change. "Decent" (the 6-bed room) has no line in the outcome list: number for the author.
- **N3. Roommate event chances** (`hostel_midnight_checkout.md:173-182`): never ruled. Number for the author, needed only when the events are built.
- **N4. What a host night restores when her entry says nothing** (Renata, the "Ex", the Twins, Miss Morphine, CryptoBro69 Himself): number for the author.
- **N5. "Groggy" (2 hours), "Exhausted" and "Existentially Rested" (2 hours)** are named in the location docs and are not in the status master list or the status data. Keep them, and with what numbers: for the author.
- **N6. Does a rest clear the drunk tier** (Buzzed, Beer Goggles, Shitfaced)? No ruling found.
- **N7. What the Speedcakes deep clean throws away and what the Munchies Tax takes at a rest.** Already open on Eurobound-5kf4; listed here because the first bed will fire them.

## 6. Gaps for the author

- **G1. Two hosts are only in location docs.** "The Philosopher" and "CryptoBro69 Himself" have no entry in the Chronicles doc and no four-state routing. Are they hosts, or leftovers?
- **G2. Two index notes name no host.** The locations index gives The Tap Dat Vault "couchsurf reward selfie" and Three Crown Keg Haus "couchsurf/quest access" (`debaucheryville_locations_index.md:11-12`). No doc says who or where.
- **G3. No hotel.** The status master list ends "Tourist Trap Victim" with "Rest at hotel or visit 3 different areas" (`design/mechanics/Battle/status_effects.md:63`). The Debaucheryville docs have a hostel and no hotel.
- **G4. The hostel is not in the game.** No location, screen or data. The first bed needs it.
- **G5. The engine's couchsurf file is behind the docs.** It has 5 hosts, lists the Twins under Polina only, and has no Renata (`game/assets/data/world_data/events/couchsurfing/couchsurfing_chronicles_debaucheryville.json`). Tracked by Eurobound-j1h6.
- **G6. `design/mechanics/Systems/daynightcycle.md` is a three-line placeholder.** Once the rules above are ruled, they belong there and in the ledger.

## 7. After the author rules

Record the ruling in `docs/superpowers/NEXT_WORK.md`, then file a build bead for the first rest point (rule 15). That closes Eurobound-8snp.
