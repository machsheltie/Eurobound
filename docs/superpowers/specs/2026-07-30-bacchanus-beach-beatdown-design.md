# Design Spec: The Bacchanus Beach Beatdown (Debaucheryville Sidequest)

**Date:** 2026-07-30
**Status:** Approved by author (interview + section-by-section review)
**Scope:** One new sidequest, three prize/consolation items, one new status effect, four NPC profiles, two full location suites, one new template, three file edits.

---

## 1. Premise

The bros stumble onto **The Bacchanus Beach Beatdown** — a trashy reality-TV trivia gauntlet
(inspired by MTV summer specials / The Challenge) filmed on **Fauxst Beach**, a fake beach of
trucked-in sand on **The Bohemian Riviera**, the beach-bar strip along **The Bacchanus** river
(Vltava parody: Bacchus + anus). Contestants are strapped into port-o-potties rigged to a
pneumatic catapult. Three wrong answers = launched into the river. The trivia is conducted
entirely in Czech-parody; the bilingual sign-up PA never mentions this because the bros never
ask. Contestant #4 is a 22-year-old local polyglot genius with the body of a Greek god who
wasn't even trying to enter.

The show is a **Cirque du Shady production** ("Shady Productions" — Ringmaster Vance "Vape"
Vallaro's TV venture, a folding table with a fax machine behind the big top), which is why
Hamstradamus is the prize-giver and why the whole thing feels like a rigged carnival game
with camera cranes.

This quest is the trivia show only. The all-night party scene on the Bohemian Riviera
**seeds** the future "Herp" questline (Gold Circle Coin) but does not include it.

## 2. Quest Structure

- **Quest ID:** `debaucheryville_sidequest_bacchanus_beach_beatdown_01`
- **File:** `Design/Quests/Location Specific/Debaucheryville/bacchanusbeachbeatdown.md`
  (must satisfy every section of `Templates/sidequest_template.md`)
- **Quest giver:** Petra the Production Assistant, sign-up table on Fauxst Beach.
  She is scrupulously honest; every scam beat is technically disclosed. Release forms are
  pure Czech-parody legalese; the bros sign unread.

### Flow
1. **Hook:** Bros cringe at college-age vacationers on the Bohemian Riviera, spot the EMTV-style
   crew, and all three sign up to prove they've still got it.
2. **Bro Select:** Player picks ONE bro to answer for. The other two play on autopilot —
   confidently, catastrophically wrong. They accumulate strikes automatically and are launched
   at staggered comic intervals (~Q4 and ~Q7, one mid-sentence). Minimum 2/3 bros are always
   launched; the quest cannot end without at least two airborne port-o-potties.
3. **Phase 1 — The Gauntlet:** 9 questions in Czech-parody, 3 strikes = launched.
   Player decodes via cognates, props, host gestures, crowd reactions. The selected bro
   shouts a confidently wrong answer first each round; the player then picks the real answer.
4. **Janek's "choke":** Janek deliberately throws exactly one answer out of boredom.
   Surviving bro: "LOOK! Janek is CHOKING under the pressure, baby!" (He is not.)
5. **Phase 2 — Sudden Death:** Survive with <3 strikes → head-to-head buzzer duel vs Janek.
   Winnable only because Janek genuinely doesn't care — he pauses mid-buzzer to wave at his
   crew team gliding down the Bacchanus. Timing/reflex skill window; hard but fair.
6. **Chadwick's cheat (Chadwick only):** Visible "Go Live" option during any question.
   ICQ chat feeds answers at ~70% reliability (trolls). Each use fills Jaxson's suspicion
   meter; 3 uses = disqualification → immediate launch, no consolation prize
   ("Unfortunately, bro."). Lord Pilsner and Bradley have no cheat path.

### Outcomes
- **WIN:** Hamstradamus (wizard hat + beach-appropriate speedo) pins the sheriff badge on the
  winning bro, hands over the stein, delivers a cursed Y2K prophecy. Post-credits scene A.
- **LOSS:** Launch sequence → river splash → walk of shame past vacationers heckling in
  Czech-parody (bros translate the heckles as praise: "Nice try!" "Good effort, champions!")
  → **Port-O-Cologne** status effect + **Hamagotchi** consolation trinket for "second place."
  Post-credits scene B.

## 3. NPCs (each gets full `Templates/NPC_Profile_Template.md` treatment)

| NPC | ID | Notes |
|---|---|---|
| **Jaxson Vane** | `debaucheryville_npc_jaxson_vane_01` | Host. Local D-lister, real name Jaromír Vaněk, legally rebranded as an "imported American" action-sports host; accent slips when the catapult jams. Three rival energy-drink sponsors (drinks from three cans simultaneously). Oakleys indoors. Catchphrase "Unfortunately, bro." delivered arctic-cold at the lever pull. Bros think he's a kindred spirit; he sees launchable content. |
| **Janek Sýkora** | `debaucheryville_npc_janek_sykora_01` | 22, elite national crew team rower who was just walking by (magazine-ad hair, designer swim trunks). Four languages, genius, Greek-god build. Sýkora = "titmouse" in Czech; locals find that hilarious, the bros never learn it. Doesn't want the prize; answers out of politeness; calls the bros "the sirs" (never learns their names). |
| **Petra the Production Assistant** | `debaucheryville_npc_petra_production_assistant_01` | Bilingual sign-up PA, quest giver of record. Never lies once — everything is technically disclosed. Smaller profile but full template. |
| **Hamstradamus** | (Cirque du Shady) | FINALLY gets his NPC profile file. Covers his Cirque prophecy-tent role AND his Beatdown prize-giver appearance: normal hamstery self, wizard hat, beach-appropriate speedo. Cursed Y2K prophecy with every prize. |

NPC profile locations: new folder `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/`
for Jaxson, Janek, Petra; Hamstradamus in `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/`.

## 4. Locations (each gets the full mandatory suite from `Templates/location_validation_template.md`)

### A. The Bohemian Riviera (with Fauxst Beach) — NEW
One explorable zone: the beach-bar strip along the Bacchanus embankment + Fauxst Beach
(trucked-in sand, inflatable palm trees, space heaters, lifeguard tower over wadeable water)
+ the Beatdown filming setup (catapult row, port-o-potties, EMTV camera cranes) + the
all-night party scene (Herp questline seed). Satirical core: a landlocked country charging
beach-resort prices for a river embankment; MTV-style "summer specials" filmed wherever's cheapest.

### B. The Cirque du Shady — NEW (the missing parent location)
Stitches together existing sub-locations WITHOUT modifying their files: Hamstradamus's prophecy
tent, The Participation Trophy (Yolanda), Mystery Meat Cart (Chef Chuckles), Bobo the Crypto
Clown's performance circle, knife-throwing act, rigged games, ICQ backroom, Ringmaster Vance
"Vape" Vallaro's tent. New element: **Shady Productions** (the TV venture linking Cirque → beach).

Each location produces 9 files (profile .md, PNG_Assets .md, core/npcs/interactions/environment/
items/sprite_mapping/location_nodes JSONs) placed in the existing per-type subfolders under
`Design/World Design/Debaucheryville/` (matching the Astronomical Cock-Up Square pattern;
create `core/` and `environment/` subfolders as needed).

## 5. Items & Status Effect

### Summer Vacation Trivia Champ Badge (WIN — flagship, full permanent-item file)
- Cheap plastic gold kids' sheriff star: **"SUMMER VACATION TRIVIA CHAMP 2003"** in flaking
  glitter print. 2003 because Shady Productions bought a pallet of defective badges decades
  ago and no one has ever beaten the local contestant — until now.
- **Deception:** actually a ~0.008-Sov party-favor badge that makes no sense as a trivia prize;
  the winning bro believes it's a wearable Mensa card / law-enforcement-grade credential.
- **Hybrid mechanics:** permanently pinned to the winning bro's sprite (degrades: paint flakes,
  pin rusts from river spray) AND grants passives:
  - Bravado +3 ("the law of the beach")
  - Charm +1 vs Tourists / −1 vs Locals
  - **Aggressive Guessing:** 10% proc on taking damage — bro shouts a confidently incorrect
    fact, inflicting existing *Embarrassed* status on enemies for 1 turn
  - **Deputy of Denial:** immune to the first *Embarrassed* applied to him each battle
- Unlocks "Trivia Champion of Europe" dialogue game-wide; NPC reaction table (bouncers, kids
  who recognize party-store merch, a deeply unimpressed real cop).
- File: `Design/Inventory/items/trivia_champ_badge_item.md` (uses the new permanent template).

### The Souvenir Stein (WIN — "practical" prize, compact file)
- Hollow yellowing plastic stein from the same 2003 pallet. **Take a Swig** (cooldown):
  restores 5 HP, small chance of brief *Nausea* from swallowing foil glitter.
- File: `Design/Inventory/items/summer_vacay_stein_item.md`.

### Hamagotchi™ Virtual Hamster Pal (LOSS — consolation trinket, compact file)
- Knockoff Tamagotchi with Hamstradamus branding, waterlogged, screen permanently showing a
  tiny hamster ghost. Buttons do nothing. Bros treasure it ("it's VINTAGE tech, bro").
- File: `Design/Inventory/items/hamagotchi_consolation_item.md`.

### Port-O-Cologne (LOSS status effect)
- Applied by launch/splash. −Charm with everyone, fly particles, NPCs step back, vendor
  "smell tax," romance dialogue locked while active.
- Cure: paid shower at hostel or spa. Swimming in the Bacchanus to rinse off REFRESHES the
  duration (it's the Bacchanus).
- Added to `Design/Mechanics/Battle/status_effects.md`.

## 6. New Template

`Templates/permanent_item_template.md` — generalized from `Design/Inventory/items/vip_wristband_item.md`:
Identity / The Deception / Economic Details / Visual Specs incl. degradation / Stats & Effects
incl. "What It Does NOT Do" / Gameplay Integration (permanent visibility, sprite) / NPC Reactions /
Quest Integration / Key Story Moments / Mobile Optimization / Validation Checklist / Dev Notes.

## 7. World-File Edits

1. `Design/World Design/Debaucheryville/debaucheryville.md` — add **"The Bacchanus Riverfront"**
   district to STREETS & DISTRICTS (river + Bohemian Riviera strip + Fauxst Beach).
2. `Design/World Design/Debaucheryville/debaucheryville_locations_index.md` — add tags for
   `bohemian_riviera` and `cirque_du_shady`.
3. `Design/Mechanics/Battle/status_effects.md` — add Port-O-Cologne.

## 8. Non-Negotiable Tone Rules (from templates and existing docs)

- Bros are NEVER self-aware; players laugh AT them; scams obvious to players.
- Satire targets tourists/frat-bro psychology and scam economies, never Czech people;
  vendors/NPCs are savvy entrepreneurs, not villains.
- No crypto elements in any of this content (none established at these locations).
- Y2K-era cringe flavor (ICQ, EMTV, 2003 merch); world names only (Debaucheryville, never Prague).
- Post-credits scenes deliver the delusion-vs-reality payoff for BOTH outcomes.

## 9. Deliverable Checklist (~30 files)

1. `Templates/permanent_item_template.md` (new)
2. `Design/Quests/Location Specific/Debaucheryville/bacchanusbeachbeatdown.md` (new)
3. `Design/Inventory/items/trivia_champ_badge_item.md` (new)
4. `Design/Inventory/items/summer_vacay_stein_item.md` (new)
5. `Design/Inventory/items/hamagotchi_consolation_item.md` (new)
6. `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/jaxson_vane.md` (new)
7. `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/janek_sykora.md` (new)
8. `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/petra_production_assistant.md` (new)
9. `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/hamstradamus.md` (new)
10–18. Bohemian Riviera location suite (9 files: .md profile, PNG assets .md, 7 JSONs)
19–27. Cirque du Shady location suite (9 files)
28. Edit `debaucheryville.md` (new district section)
29. Edit `debaucheryville_locations_index.md` (new tags)
30. Edit `status_effects.md` (Port-O-Cologne)
