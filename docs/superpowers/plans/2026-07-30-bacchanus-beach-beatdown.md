# Bacchanus Beach Beatdown Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Author all design/content files for the "Bacchanus Beach Beatdown" Debaucheryville sidequest: 1 new template, 1 sidequest doc, 3 item files, 4 NPC profiles, 2 full location suites, and 3 edits to existing world files.

**Architecture:** Pure content authoring (markdown + JSON) in an existing game-design repo. Every file must conform to the repo's own templates (`Templates/sidequest_template.md`, `Templates/NPC_Profile_Template.md`, `Templates/location_validation_template.md`) and match the voice/structure of exemplar files (`Design/Inventory/items/vip_wristband_item.md`, `Design/World Design/Debaucheryville/astronomical_cockup_square.md`). Validation = section-coverage greps + JSON parsing, no code tests.

**Tech Stack:** Markdown, JSON, git. Validate JSON with PowerShell `ConvertFrom-Json`.

**Source spec:** `docs/superpowers/specs/2026-07-30-bacchanus-beach-beatdown-design.md` — READ IT FIRST for full narrative detail. It is the single source of truth for story content.

## Global Constraints

Every task implicitly includes these. Copy values EXACTLY — cross-file ID mismatches are bugs.

**Canonical IDs & names:**
- Quest ID: `debaucheryville_sidequest_bacchanus_beach_beatdown_01`; Display: "The Bacchanus Beach Beatdown"
- River: **The Bacchanus** (Vltava parody; Bacchus + anus). Beach: **Fauxst Beach**. Bar strip: **The Bohemian Riviera**. District: **The Bacchanus Riverfront**.
- Location IDs: `debaucheryville_riverfront_bohemian_riviera_01` (tag `bohemian_riviera`), `debaucheryville_circus_cirque_du_shady_01` (tag `cirque_du_shady`)
- NPC IDs: `debaucheryville_npc_jaxson_vane_01`, `debaucheryville_npc_janek_sykora_01`, `debaucheryville_npc_petra_production_assistant_01`, `debaucheryville_npc_hamstradamus_01`
- Item IDs: `item_trivia_champ_badge`, `item_summer_vacay_stein`, `item_hamagotchi_consolation`
- Status effect: **Port-O-Cologne** (id `port_o_cologne`)
- Minigame IDs: `minigame_beatdown_trivia_gauntlet`, `minigame_beatdown_sudden_death`
- Show: "The Bacchanus Beach Beatdown," a **Shady Productions** venture (Ringmaster Vance "Vape" Vallaro's TV company — folding table + fax machine behind the Cirque big top). Airs on EMTV ("Euromemeia's #1 Music Televize").
- Badge text: **"SUMMER VACATION TRIVIA CHAMP 2003"** (2003 on purpose: defective merch pallet, never awarded until now). It is a SUMMER VACATION trip, never "spring break."

**The three bros (never "Chad"/"Brody"):** Lord Pilsner (delusional leader, frosted tips, beer paddle), Chadwick (washed influencer, ICQ livestream followers, ring light), Bradley (dad-bod muscle, protein shakes, picks fights).

**Quest mechanics (fixed by author, do not alter):**
- All three bros enter. Player selects ONE to answer for; other two auto-fail with staggered launches (~Q4 and ~Q7, one mid-sentence). Minimum 2/3 bros always launched.
- Phase 1: 9 questions in Czech-parody, 3 strikes = launched. Decode via cognates/props/host gestures/crowd reactions. Selected bro shouts a confidently wrong answer first each round; player picks the real answer.
- Janek deliberately throws exactly ONE answer out of boredom → bros: "LOOK! Janek is CHOKING under the pressure, baby!"
- Phase 2 (survive <3 strikes): sudden-death buzzer duel vs Janek; winnable only because he pauses mid-buzzer to wave at his crew team on the river.
- Chadwick ONLY: visible "Go Live" cheat, ~70% reliable troll ICQ chat, 3 uses fills Jaxson's suspicion meter → disqualification launch, no consolation prize. Pilsner/Bradley have no cheat.
- WIN: Hamstradamus (wizard hat + beach speedo) pins badge, hands stein, gives cursed Y2K prophecy. Post-credits scene A.
- LOSS: launch → splash → walk of shame past vacationers heckling in Czech-parody (bros mistranslate as praise) → Port-O-Cologne debuff + Hamagotchi trinket. Post-credits scene B.

**Tone rules (non-negotiable):** Bros NEVER self-aware; players laugh AT them; scams obvious to players; satire targets tourists/frat-bro psychology and scam economies, never Czech people; NPCs are savvy entrepreneurs, not villains; NO crypto elements anywhere in this content; Y2K-era cringe (ICQ, EMTV, 2003 merch); world names only (Debaucheryville — never Prague/Vltava).

**Formatting:** Match exemplar files' voice — em-dash asides, satirical subtitles in italics under H1, tables for stats, emoji section headers where the template uses them. Windows CRLF is fine; git handles it.

**Commits:** One commit per task, message style `content: <what>` (this repo has no strict convention; keep messages descriptive). End every commit message with:
```
Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016m7EuK9wAMbbWfimUxXwmP
```

---

### Task 1: Permanent Item Template

**Files:**
- Create: `Templates/permanent_item_template.md`
- Read first: `Design/Inventory/items/vip_wristband_item.md` (the exemplar being generalized)

**Interfaces:**
- Produces: the section skeleton Task 2 must follow exactly (same H2 titles, same table shapes).

- [ ] **Step 1: Write the template.** Generalize every section of `vip_wristband_item.md` into bracketed placeholders. Required H2 sections in order: `📋 Item Identity`, `🎭 The Deception` (with `What The Item Actually Is` / `What The Bros Believe It Is` H3s), `💰 Economic Details` (table: Purchase/Actual Value/Resale/Can Be Sold/Dropped/Traded), `🎨 Visual Specifications` (physical appearance table, per-character variants table if applicable, `Degradation Over Time` table), `📊 Stats & Effects` (direct stats code block, passive effects table, `What It Does NOT Do` ❌ list), `🎯 Gameplay Integration` (permanent visibility rules, sprite implementation, distinction-from-equipment table if applicable), `🗣️ NPC Reactions` (reaction table + callback dialogue per bro), `🔗 Quest Integration` (source quest, gates/unlocks table, achievement w/ hidden description), `🎬 Key Story Moments` (2-3 scripted beats), `📱 Mobile Optimization`, `✅ Validation Checklist` (include rows "Comedy value preserved" and "Bros never achieve self-awareness"), `📝 Development Notes`. Top of file: H1 `# Item Definition: [Item Name]`, italic satirical subtitle line, then a short "How to use this template" comment block noting it's for items permanently affixed to a bro (cosmetic-permanent, hybrid, or curse items).
- [ ] **Step 2: Validate section coverage.**
  Run: `grep -c "^## " "Templates/permanent_item_template.md"` — Expected: 12 (the twelve H2 sections above).
- [ ] **Step 3: Commit.** `git add Templates/permanent_item_template.md && git commit` (message: `content: add permanent item template generalized from VIP wristband exemplar` + trailer).

### Task 2: Trivia Champ Badge Item File

**Files:**
- Create: `Design/Inventory/items/trivia_champ_badge_item.md`
- Read first: `Templates/permanent_item_template.md` (Task 1), `Design/Inventory/items/vip_wristband_item.md` (voice), spec §5

**Interfaces:**
- Consumes: Task 1's section skeleton.
- Produces: item `item_trivia_champ_badge` referenced by Tasks 4, 9, 10, 13.

- [ ] **Step 1: Write the file** following the template, filled with (all from spec §5):
  - Identity: ID `item_trivia_champ_badge`, Display "Summer Vacation Trivia Champ Badge", Internal "Defective 2003 Party-Favor Sheriff Star", Type "Permanent Hybrid (Cosmetic + Passive)", Rarity "Common (bros think it's One-Of-A-Kind)", Source "Hamstradamus @ Fauxst Beach prize podium — win The Bacchanus Beach Beatdown".
  - Deception: actually a ~0.008-Sov plastic gold kids' sheriff badge stamped "SUMMER VACATION TRIVIA CHAMP 2003" in flaking glitter (a badge makes zero sense as a trivia prize — bulk mystery merch); winning bro believes it's a wearable Mensa card / law-enforcement-grade credential of intellectual supremacy.
  - Economics: purchase N/A (prize), actual value 0.008 Sovs, resale 0 Sovs, cannot be sold/dropped/traded.
  - Visuals: gold-painted plastic star, bent pin, glitter print; degradation table (Days 1-3 pristine → 4-7 paint flaking → 8+ bare gray plastic, pin rusted from river spray, text reads "SUM ER VAC TION T IVIA CH MP 2 03").
  - Stats code block: `Bravado: +3 ("the law of the beach")`, `Charm (Tourists): +1`, `Charm (Locals): -1 (they watch the show)`.
  - Passives table: **Aggressive Guessing** — 10% on taking damage, bro shouts a confidently incorrect fact ("ACTUALLY, hexagons are INFINITE!"), inflicts existing `Embarrassed` status on enemies 1 turn; **Deputy of Denial** — immune to first `Embarrassed` applied to wearer each battle.
  - Does NOT: grant law-enforcement authority, deputize anyone, prove intelligence, impress anyone who can read, open VIP doors.
  - Gameplay: permanently pinned to winning bro's sprite (chest), visible all animations, degradation visual-only; unlocks "Trivia Champion of Europe" dialogue options game-wide.
  - NPC reactions table incl.: bouncer ("That is... child's toy, yes?" → bro hears "That is a champion's decoration, yes"), kid who recognizes it from the party store, deeply unimpressed real cop, locals who watched the episode.
  - Quest integration: source quest ID, achievement "Beach's Finest" (hidden description: "Answer trivia better than two launched friends and one guy who wasn't trying").
  - Key story moments: the pinning ceremony (Hamstradamus prophecy), first attempt to "flash the badge" at Velvet Curtain Club, post-credits callback.
- [ ] **Step 2: Validate.** Run: `grep -c "^## " "Design/Inventory/items/trivia_champ_badge_item.md"` — Expected: 12. Also `grep -c "item_trivia_champ_badge" ...` ≥ 1 and `grep -c "SPRING BREAK" ...` = 0 (it must say SUMMER VACATION).
- [ ] **Step 3: Commit** (message: `content: add Summer Vacation Trivia Champ Badge permanent item` + trailer).

### Task 3: Stein + Hamagotchi Item Files (compact)

**Files:**
- Create: `Design/Inventory/items/summer_vacay_stein_item.md`
- Create: `Design/Inventory/items/hamagotchi_consolation_item.md`
- Read first: spec §5; use a trimmed version of the Task 1 skeleton (Identity, Deception, Stats & Effects, Quest Integration, NPC Reactions, Validation Checklist — 6 H2 sections each; these are minor items, full 12-section treatment not required).

**Interfaces:**
- Produces: `item_summer_vacay_stein`, `item_hamagotchi_consolation` referenced by Tasks 4, 10, 13.

- [ ] **Step 1: Write the stein file.** ID `item_summer_vacay_stein`, "Souvenir Champion Stein" — hollow yellowing plastic stein from the same 2003 pallet, handed over with the badge on a WIN. Use effect **Take a Swig** (60s cooldown): +5 HP, 20% chance of 10s `Nausea`-style debuff from swallowing a fleck of foil glitter (flavor line: "There wasn't even anything in it. Somehow you swallowed glitter anyway."). Removable inventory item (unlike badge). Bros toast with it constantly; liquid poured in leaks from seam.
- [ ] **Step 2: Write the Hamagotchi file.** ID `item_hamagotchi_consolation`, "Hamagotchi™ Virtual Hamster Pal" — LOSS consolation "second place" prize. Knockoff Tamagotchi with Hamstradamus branding, waterlogged from storage, screen permanently shows a tiny hamster ghost, buttons do nothing. No stats; key item / junk tier; bros treasure it ("it's VINTAGE tech, bro"); examining it near Hamstradamus triggers him to whisper "MY SON." Unlocks one ICQ gag message ("Your Hamagotchi has died. It was already dead. It will die again tomorrow.").
- [ ] **Step 3: Validate.** `grep -c "^## "` each file — Expected: 6 per file. `grep -c "item_summer_vacay_stein"` ≥1 in stein file; `grep -c "item_hamagotchi_consolation"` ≥1 in hamagotchi file.
- [ ] **Step 4: Commit** (message: `content: add stein and Hamagotchi consolation items for Beatdown quest` + trailer).

### Task 4: The Sidequest File

**Files:**
- Create: `Design/Quests/Location Specific/Debaucheryville/bacchanusbeachbeatdown.md`
- Read first: `Templates/sidequest_template.md` (MUST fill EVERY section), spec §1-2 and §5, `Design/Quests/Location Specific/Debaucheryville/vip_wristbands.md` (voice exemplar if it exists — check; otherwise `icqscammersting.md`)

**Interfaces:**
- Consumes: item IDs (Tasks 2-3), NPC IDs, location IDs, status `port_o_cologne` (all fixed in Global Constraints).
- Produces: the quest doc referenced by Tasks 5-13.

- [ ] **Step 1: Write the file** covering every `sidequest_template.md` section:
  - Identity: quest ID; Display "The Bacchanus Beach Beatdown"; Satirical Subtitle "Three strikes and you're airborne"; Quest Giver Petra the Production Assistant @ Fauxst Beach sign-up table; City Debaucheryville; Recommended Level 3-5; Duration ~25 minutes.
  - Core Premise: bros think = they've been scouted as elite athletic-intellectual specimens for international television, their comeback moment. Actually = a trash Shady Productions catapult show that exists to launch tourists into the river for ratings; the trivia is in a language they don't speak and they never asked. Funny because = every fact was disclosed; they signed release forms they couldn't read while flexing for a camera that wasn't on.
  - Satirical targets: reality-TV exploitation formats (The Challenge/MTV summer specials), aging bros vs. college vacationers, language arrogance of monolingual tourists, "beach culture" in a landlocked country; Y2K refs: EMTV, ICQ chat cheat, 2003 merch.
  - Quest Initiation: trigger = enter Fauxst Beach zone after arriving in Debaucheryville; Petra's pitch (technically-honest disclosure dialogue); all three bros' reactions (Pilsner: destiny/"Alpha Sigma material"; Chadwick: content opportunity, "this is my comeback arc"; Bradley: "I've been training my whole life for televised combat trivia").
  - **Binary Path Choice → map to Bro Select** (label as PATH A/B/C by selected bro): Path A Lord Pilsner (hard mode, drunk-confidence flavor answers), Path B Chadwick (identical trivia + exclusive "Go Live" cheat mechanic w/ suspicion meter and disqualification rule), Path C Bradley (hard mode, tries to intimidate the catapult). For each path: what bros think / actually doing / execution steps (sign-up → strap-in → Phase 1 gauntlet → Janek's thrown answer beat → Phase 2 sudden death) / key dialogue / NPC reactions / rewards. Non-selected bros auto-fail at ~Q4 and ~Q7 (one mid-sentence) — write the two staggered launch beats.
  - Minigame spec block: `minigame_beatdown_trivia_gauntlet` (9 questions, 3 strikes; decode via cognates/props/gestures/crowd; include 3 fully-written sample questions in Czech-parody with their visual clue and the bro's confidently-wrong shout) and `minigame_beatdown_sudden_death` (buzzer timing window: Janek waves at crew team for 1.5s — buzz inside the window to win).
  - Rewards WIN: `item_trivia_champ_badge` + `item_summer_vacay_stein`, +3 Bravado, achievement "Beach's Finest". Rewards LOSS: `item_hamagotchi_consolation` + status `port_o_cologne`, walk-of-shame scene (vacationer heckles in Czech-parody + bros' delusional mistranslations — write 4 heckle/mistranslation pairs). Chadwick disqualification: launch, NO consolation prize, Jaxson's "Unfortunately, bro."
  - Environmental integration: catapult row remains on Fauxst Beach after quest; recovered port-o-potties become riverbank "monuments"; NPC callbacks at Velvet Curtain Club and Astronomical Cock-Up Square; easter egg — episode airs on bar TVs along the Bohemian Riviera afterward.
  - Key dialogue moments per bro + 2 sardonic narrator lines.
  - Quest connections: prerequisites none (early-city accessible); unlocks Bohemian Riviera night-party scene (future Herp questline seed — mention only, do not design); cross-refs Cirque du Shady (Shady Productions), Hamstradamus.
  - Mobile UX: 3 screenshot moments (triple catapult row; Hamstradamus in speedo pinning badge; walk of shame), social hooks.
  - **Post-Credits Scene A (WIN)**: months later back home — winning bro wears the badge to a job interview / traffic stop; screenplay format; punchline lands on the badge reading "I'm... wait, this says 2003?" spoken by anyone but the bro.
  - **Post-Credits Scene B (LOSS)**: bros at home re-watching their launch on a taped EMTV VHS, framing it as their "television debut"; Hamagotchi ghost on the shelf; punchline: neighbor kid translates the heckling.
  - Full ✅ Validation Checklist table from template with all rows checked, plus Development Notes (catapult animation, launch physics gag, Czech-parody question rendering, suspicion meter UI).
- [ ] **Step 2: Validate.** `grep -c "^## " file` — Expected ≥ 10; `grep -c "POST-CREDITS" file` ≥ 1; grep each: `item_trivia_champ_badge`, `item_hamagotchi_consolation`, `port_o_cologne`, `debaucheryville_sidequest_bacchanus_beach_beatdown_01` all ≥ 1; `grep -ci "prague\|vltava\|spring break"` = 0.
- [ ] **Step 3: Commit** (message: `content: add Bacchanus Beach Beatdown sidequest (full template)` + trailer).

### Task 5: NPC Profile — Jaxson Vane

**Files:**
- Create: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/jaxson_vane.md`
- Read first: `Templates/NPC_Profile_Template.md` (fill EVERY section), `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/crypto_clown.md` (depth exemplar), spec §3

**Interfaces:**
- Produces: NPC `debaucheryville_npc_jaxson_vane_01` referenced by Tasks 4, 9, 10.

- [ ] **Step 1: Write the profile.** Core facts: host of the Beatdown; local D-lister, real name **Jaromír Vaněk**, legally rebranded as "imported American action-sports host"; accent slips when the catapult jams; three RIVAL energy-drink sponsors (contractually drinks from three cans simultaneously — write the sponsor gag names, e.g. "Rampage!", "Gnarly Juice", "Extreme Bohemian Energy"); extreme-sports Oakleys indoors/at night; catchphrase **"Unfortunately, bro."** delivered arctic-cold at the lever pull. Comedy gap: bros think he's their kindred spirit; he sees launchable content. Include: internal monologue (thinking in Czech, performing in Californian), full dialogue set (greeting, strap-in speech, per-strike lines, lever-pull line, winner-crowning line, callback if bros return), schedule (filming days on Fauxst Beach, off-days doing supermarket openings), connections (employed by Vance/Shady Productions; professional respect for Petra; mild awe of Janek), animation states (lever_pull, triple_can_sip, oakley_adjust, accent_slip), voice direction (Mountain-Dew-commercial American that cracks into Czech vowels under stress), validation checklist all rows.
- [ ] **Step 2: Validate.** `grep -c "^## " file` — Expected ≥ 12 (template has 14 H2 sections; allow ≥12); `grep -c "Unfortunately, bro" file` ≥ 2; `grep -c "debaucheryville_npc_jaxson_vane_01"` ≥ 1.
- [ ] **Step 3: Commit** (message: `content: add NPC profile — Jaxson Vane, Beatdown host` + trailer).

### Task 6: NPC Profile — Janek Sýkora

**Files:**
- Create: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/janek_sykora.md`
- Read first: same template + exemplar as Task 5, spec §3

**Interfaces:**
- Produces: NPC `debaucheryville_npc_janek_sykora_01` referenced by Tasks 4, 9, 10.

- [ ] **Step 1: Write the profile.** Core facts: 22, elite national crew team rower, was walking past Fauxst Beach after a five-mile row (magazine-ad hair, designer swim trunks), recruited on the spot; four languages; genius; Greek-god build; surname Sýkora = "titmouse" in Czech — locals find it hilarious, bros never learn it; doesn't want the prize, answers correctly out of politeness; deliberately throws exactly one answer out of boredom (bros: "HE'S CHOKING!"); in sudden death pauses mid-buzzer to wave at his crew team gliding down the Bacchanus; calls the bros **"the sirs"** — never learns their names. Include: internal monologue (he is thinking about hydrodynamics the entire time), dialogue in flawless polite English + occasional flawless polite Czech/French/German asides, post-loss graciousness ("The sirs flew very bravely."), schedule (dawn rowing, university, walking places while being photographed by strangers), connections (crew team; his grandmother watches the show; zero relationship with fame), animation states (idle_perfect_posture, polite_wave, bored_answer, buzzer_wave), voice direction (calm, kind, devastatingly unbothered), validation checklist.
- [ ] **Step 2: Validate.** `grep -c "^## " file` ≥ 12; `grep -c "the sirs" file` ≥ 2; `grep -c "debaucheryville_npc_janek_sykora_01"` ≥ 1.
- [ ] **Step 3: Commit** (message: `content: add NPC profile — Janek Sykora, the genius contestant` + trailer).

### Task 7: NPC Profile — Petra the Production Assistant

**Files:**
- Create: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/petra_production_assistant.md`
- Read first: same template as Task 5, spec §3

**Interfaces:**
- Produces: NPC `debaucheryville_npc_petra_production_assistant_01`, quest giver of record (Task 4).

- [ ] **Step 1: Write the profile** (full template, but leaner prose than Tasks 5-6). Core facts: bilingual sign-up PA; flawless English to the bros; release forms are pure Czech-parody legalese; **never lies once** — every scam beat is technically disclosed ("The show is conducted in the local language." — Bros: "Bro, obviously, we're IN the local area."). Deadpan clipboard energy; has seen hundreds of tourists sign; keeps a private tally of "seconds until they mention college." Dialogue: recruitment pitch (all-true statements arranged to be misheard), form-signing beat, post-launch checkout ("Please sign here to confirm receipt of one [1] second-place prize."). Connections: Shady Productions employee, coordinates with Jaxson, respects Janek's grandmother (a show superfan). Validation checklist.
- [ ] **Step 2: Validate.** `grep -c "^## " file` ≥ 12; `grep -c "debaucheryville_npc_petra_production_assistant_01"` ≥ 1.
- [ ] **Step 3: Commit** (message: `content: add NPC profile — Petra the Production Assistant` + trailer).

### Task 8: NPC Profile — Hamstradamus

**Files:**
- Create: `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/hamstradamus.md`
- Read first: template (Task 5), `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/crypto_clown.md`, existing Hamstradamus canon: `Design/game_design_document.md` (grep "Hamstradamus"), `Design/World Design/Debaucheryville/debaucheryville.md`

**Interfaces:**
- Produces: NPC `debaucheryville_npc_hamstradamus_01` referenced by Tasks 4, 9-12.

- [ ] **Step 1: Write the profile.** This is his FIRST dedicated file — consolidate existing canon (do not contradict it): prophetic dancing hamster (Hamster Dance homage), cursed Y2K prophecies ("REPENT BEFORE THE CLOCK TICKS 00:00 OR YOUR NOKIA SHALL BECOME A TOASTER."), prophecy tent at the Cirque du Shady, Prophecy Roulette event (5 coins, random buff/debuff), in battle he predicts your doom then trips over his crystal ball, ICQ pop-up presence, successful performer (Bobo the Crypto Clown is insecure about it). NEW canon from spec: **Beatdown prize-giver appearance** — normal hamstery self, **wizard hat + beach-appropriate speedo**; pins the badge; per-outcome prophecy lines (WIN: "HE WHO WEARS THE STAR OF SUMMER SHALL NEVER PAY FULL PRICE FOR ONION RINGS. REPENT." — LOSS: write a matching cursed consolation prophecy); whispers "MY SON" if a bro examines the Hamagotchi near him. Primary location Cirque prophecy tent; secondary appearance Fauxst Beach on filming days. Full dialogue, schedule, connections (Vance employs him; Yolanda stocks his merch; Bobo envies him), animation states (dance_loop, prophecy_trance, crystal_ball_trip, badge_pin, speedo_strut), voice direction (booming prophet voice from a hamster; squeaks when surprised), validation checklist.
- [ ] **Step 2: Validate.** `grep -c "^## " file` ≥ 12; `grep -c "debaucheryville_npc_hamstradamus_01"` ≥ 1; `grep -ci "crypto" file` — Expected: ≤ 2 (only the Bobo-relationship mention; no new crypto content).
- [ ] **Step 3: Commit** (message: `content: add NPC profile — Hamstradamus (first dedicated file)` + trailer).

### Task 9: Bohemian Riviera — Location Profile + PNG Assets

**Files:**
- Create: `Design/World Design/Debaucheryville/bohemian_riviera.md`
- Create: `Design/World Design/Debaucheryville/PNG_Assets/Bohemian_Riviera_PNG_Assets.md`
- Read first: `Templates/location_validation_template.md` (profile template + PNG template inside it), `Design/World Design/Debaucheryville/astronomical_cockup_square.md` (depth exemplar), spec §4A

**Interfaces:**
- Produces: location `debaucheryville_riverfront_bohemian_riviera_01` (tag `bohemian_riviera`), zone names used by Task 10 JSONs: `fauxst_beach`, `bar_strip`, `catapult_row`, `signup_table`, `prize_podium`, `night_party_zone`.

- [ ] **Step 1: Write the location profile** per template, ~cockup-square depth. Identity: ID above, Display "The Bohemian Riviera", Satirical Subtitle "*A beach resort experience for a country with no beach, no resort, and no shame*", Zone "The Bacchanus Riverfront", Type "Quest Hub / Party District / Reality-TV Set". Content: bar strip along the embankment (write 3 named beach bars, e.g. "Žá Žá Beach Klub", "The Tan Line", "Kokos Loco" — each one sentence); **Fauxst Beach** (trucked-in sand with visible receipts, inflatable palm trees, space heaters, lifeguard tower over knee-deep water, "NO DIVING (SERIOUSLY, IT'S 40cm)" sign); Beatdown filming setup (catapult row, port-o-potty queue, EMTV camera cranes, Petra's sign-up table, prize podium); night-party zone (all-night party scene — the future Herp questline seed, mention as hook only); college-vacationer crowd NPCs; ASCII layout map like the cockup file; satirical design section (landlocked beach-resort pricing; MTV-style specials filmed wherever's cheapest); buffoon delusion block; time-of-day variations (day filming / golden-hour posing / night rave); NPCs section summarizing Jaxson, Janek, Petra, Hamstradamus (filming days), vacationer crowd; audio design (catapult *THUNK-hisssss-splash*, distant Eurodance, Jaxson's mic feedback); connected locations (Cirque du Shady via Shady Productions gear path; Old Town streets); state tracking block (`beatdown_complete`, `selected_bro`, `bros_launched_count`, `night_party_seen`); QA checklists.
- [ ] **Step 2: Write the PNG assets doc** per the template's PNG section: color palette table (sand #E8D4A0, Bacchanus murk-green #5E7350, EMTV magenta #FF1493, catapult steel #708090, inflatable-palm green #32CD32), file structure tree, sprite sheets (environment tileset; catapult + port-o-potty objects incl. launch animation frames; NPC sprites Jaxson/Janek/Petra/Hamstradamus-speedo variant; vacationer crowd; parallax river background), animation specs (launch sequence ~3s, splash, Jaxson triple-sip, Janek buzzer-wave 1.5s window), mobile optimization tables, required PNG file list with dimensions, validation status table.
- [ ] **Step 3: Validate.** Both files exist; profile: `grep -c "^## " ` ≥ 9, `grep -ci "prague\|vltava"` = 0; PNG doc: `grep -c "^## "` ≥ 6.
- [ ] **Step 4: Commit** (message: `content: add Bohemian Riviera location profile and PNG asset spec` + trailer).

### Task 10: Bohemian Riviera — 7 JSON Files

**Files:**
- Create: `Design/World Design/Debaucheryville/core/bohemian_riviera_core.json`
- Create: `Design/World Design/Debaucheryville/npcs/Bohemian_Riviera/bohemian_riviera_npcs.json`
- Create: `Design/World Design/Debaucheryville/interactions/bohemian_riviera_interactions.json`
- Create: `Design/World Design/Debaucheryville/environment/bohemian_riviera_environment.json`
- Create: `Design/World Design/Debaucheryville/items/bohemian_riviera_items.json`
- Create: `Design/World Design/Debaucheryville/sprite_mapping/bohemian_riviera_sprite_mapping.json`
- Create: `Design/World Design/Debaucheryville/location_nodes/bohemian_riviera_location_nodes.json`
- Read first: JSON schemas embedded in `Templates/location_validation_template.md`; existing examples in `Design/World Design/Debaucheryville/location_nodes/`, `.../sprite_mapping/`, `.../items/`, `.../interactions/`, `.../npcs/Astronomical_Cockup_Square/` for shape conformity. Task 9's profile is the content source.

**Interfaces:**
- Consumes: zone names from Task 9; NPC IDs, item IDs, minigame IDs from Global Constraints.
- Produces: complete data suite for `bohemian_riviera`.

- [ ] **Step 1: Write all 7 JSONs** following the template schemas exactly. Core: access (always accessible; catapult show only on filming days), exits (to `old_town_streets`, to `cirque_du_shady`), atmosphere, visual theme, satirical_design block, state_tracking (`beatdown_complete: false`, `selected_bro: null`, `bros_launched_count: 0`, `night_party_seen: false`), performance budget. NPCs: full entries for the four named NPCs (dialogue drawn from Tasks 5-8 profiles) + ambient `college_vacationers` group (count 8-12, overheard heckle lines incl. the Czech-parody/mistranslation pairs from Task 4). Interactions: events (`beatdown_signup`, `beatdown_gauntlet`, `janek_thrown_answer`, `sudden_death`, `launch_sequence`, `walk_of_shame`, `prize_ceremony`), the two mini_games (`minigame_beatdown_trivia_gauntlet` w/ 9-question structure + 3 embedded sample questions; `minigame_beatdown_sudden_death` w/ 1.5s buzzer window), interactive objects (port-o-potty examine, release-form examine, "NO DIVING" sign), narrator commentary, return_visit_changes (episode airing on bar TVs). Environment: Eurodance ambient, catapult stingers, `port_o_cologne` in `status_effects.atmospheric_debuffs` context, time-of-day, particles (sand drift, splash, camera flashes), lighting. Items: prize items referencing `item_trivia_champ_badge` / `item_summer_vacay_stein` / `item_hamagotchi_consolation` as quest rewards (`item_category: "quest_items"`, not purchasable) plus 2 purchasable beach-bar consumables (e.g. "Kokos Loco Bucket" — cheap cocktail, applies Liquid Confidence + Sloppy). Sprite mapping: sheets matching Task 9's PNG doc names/coordinates. Location nodes: node entry with features (`entry_point`, `quest_npc: petra_production_assistant`, `mini_game: minigame_beatdown_trivia_gauntlet`, `event_hook: beatdown_launch_sequence`, `selfie_prop: catapult_row`, `npc_group: college_vacationers`, `shop_node: beach_bar`, `hidden_area: night_party_zone`), connections to `old_town_streets` and `cirque_du_shady`, quest_connections to the quest ID.
- [ ] **Step 2: Validate all 7 parse.**
  Run (PowerShell): `Get-ChildItem -Recurse "Design/World Design/Debaucheryville" -Filter "bohemian_riviera*.json" | ForEach-Object { try { Get-Content $_.FullName -Raw | ConvertFrom-Json | Out-Null; "OK  $($_.Name)" } catch { "FAIL $($_.Name): $_" } }`
  Expected: 7 × OK.
- [ ] **Step 3: Commit** (message: `content: add Bohemian Riviera location JSON suite (7 files)` + trailer).

### Task 11: Cirque du Shady — Location Profile + PNG Assets

**Files:**
- Create: `Design/World Design/Debaucheryville/cirque_du_shady.md`
- Create: `Design/World Design/Debaucheryville/PNG_Assets/Cirque_du_Shady_PNG_Assets.md`
- Read first: template + cockup exemplar (as Task 9); EXISTING sub-location canon that must be referenced, not contradicted and not modified: `the_participation_trophy.md` (Yolanda), `mysterymeatcart.md` (Chef Chuckles), `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/crypto_clown.md` (Bobo), plus GDD canon (Ringmaster Vance "Vape" Vallaro, knife-throwing act, Prophecy Roulette, The Vanishing Elephant "Bubbles", ICQ backroom hotspots, rigged games). Spec §4B.

**Interfaces:**
- Produces: location `debaucheryville_circus_cirque_du_shady_01` (tag `cirque_du_shady`); zone names for Task 12: `main_gate`, `big_top`, `prophecy_tent`, `game_alley`, `prize_booth`, `meat_cart_pitch`, `performance_circle`, `shady_productions_office`, `icq_backroom`.

- [ ] **Step 1: Write the parent location profile.** Identity: ID above, Display "The Cirque du Shady", Satirical Subtitle "*A semi-permanent traveling circus that has not traveled since 1997*", Zone "Circus Grounds (edge of Old Town)", Type "Quest Hub / Attraction Cluster / Production Company HQ". The file's job: stitch existing sub-locations into one navigable parent — reference each by its existing file/ID, add NO contradicting details. New content allowed: overall grounds layout (ASCII map), main gate & ticket rip-off, big top exterior, Ringmaster Vance "Vape" Vallaro's tent (he speaks in vape clouds; sells shady loot crates — existing canon), **Shady Productions office** (folding table + fax machine behind the big top; produces The Bacchanus Beach Beatdown; gear path to Fauxst Beach on filming days), knife-throwing act zone, rigged game alley, ICQ backroom hotspot. Satirical design (carnival grift economy; the circus as a full-stack scam ecosystem), buffoon delusions, time-of-day, NPC summary table (Vance, Hamstradamus, Yolanda, Chef Chuckles, Bobo, knife-throwing assistant), audio design (distorted calliope, vape exhale, distant hamster techno), connected locations (Old Town, Bohemian Riviera via Shady Productions), state tracking (`cirque_visited`, `beatdown_aware`, `vance_met`), QA checklists.
- [ ] **Step 2: Write the PNG assets doc** (same structure as Task 9 Step 2): palette (faded big-top red #B22222, canvas cream #F5F0DC, neon marquee #FF6EC7, vape-cloud gray #C0C0C8), sprite sheets (grounds tileset, big top + tents, Vance w/ vape-cloud speech FX, Shady Productions office props incl. fax machine, gate/marquee), animations (marquee flicker, vape-cloud text reveal, Hamstradamus tent glow), mobile optimization, PNG file list, validation table.
- [ ] **Step 3: Validate.** Profile `grep -c "^## "` ≥ 9; `grep -c "Shady Productions"` ≥ 2; `grep -ci "crypto"` ≤ 2 (Bobo reference only); PNG doc `grep -c "^## "` ≥ 6. Confirm zero edits to existing sub-location files: `git status --short` shows only the two new files.
- [ ] **Step 4: Commit** (message: `content: add Cirque du Shady parent location profile and PNG asset spec` + trailer).

### Task 12: Cirque du Shady — 7 JSON Files

**Files:**
- Create: `Design/World Design/Debaucheryville/core/cirque_du_shady_core.json`
- Create: `Design/World Design/Debaucheryville/npcs/Cirque_du_Shady/cirque_du_shady_npcs.json`
- Create: `Design/World Design/Debaucheryville/interactions/cirque_du_shady_interactions.json`
- Create: `Design/World Design/Debaucheryville/environment/cirque_du_shady_environment.json`
- Create: `Design/World Design/Debaucheryville/items/cirque_du_shady_items.json`
- Create: `Design/World Design/Debaucheryville/sprite_mapping/cirque_du_shady_sprite_mapping.json`
- Create: `Design/World Design/Debaucheryville/location_nodes/cirque_du_shady_location_nodes.json`
- Read first: template schemas; Task 11 profile as content source.

**Interfaces:**
- Consumes: Task 11 zone names; NPC/quest IDs from Global Constraints.
- Produces: complete data suite for `cirque_du_shady`.

- [ ] **Step 1: Write all 7 JSONs** (same schema discipline as Task 10). Core: access (circus hours 14:00-02:00), exits (`old_town_streets`, `bohemian_riviera`), state tracking from Task 11. NPCs: Vance (full entry — vape-cloud speech, loot crates), Hamstradamus (`debaucheryville_npc_hamstradamus_01`, prophecy tent), pointer entries for Yolanda/Chef Chuckles/Bobo marked `"defined_in"` referencing their existing files (do not duplicate their dialogue), knife-throwing assistant, ambient `circus_crowd`. Interactions: events (`prophecy_roulette`, `knife_throw_act`, `beatdown_promo` — Vance advertises the show, pointing players to Fauxst Beach), interactive objects (fax machine — spits a casting-call flyer for the Beatdown; rigged game booths), narrator commentary. Environment: distorted calliope audio, vape particles, marquee lighting, time-of-day. Items: prize-booth junk canon (Half-Smoked Cigar, Used Glitter Hat, Mystery Meat Corndog — match existing canon values) + Beatdown casting flyer (key item, free). Sprite mapping: match Task 11 PNG names. Location nodes: features (`entry_point`, `quest_npc: hamstradamus`, `event_hook: prophecy_roulette`, `mini_game: knife_throw_dodge`, `shop_node: prize_booth`, `shop_node: mystery_meat_cart`, `examinable: shady_productions_fax`, `hidden_area: icq_backroom`), connections + quest_connection to the Beatdown quest (role `quest_origin_pointer` via casting flyer).
- [ ] **Step 2: Validate all 7 parse** (same PowerShell loop as Task 10, filter `cirque_du_shady*.json`). Expected: 7 × OK.
- [ ] **Step 3: Commit** (message: `content: add Cirque du Shady location JSON suite (7 files)` + trailer).

### Task 13: World-File Edits (district, index, status effect)

**Files:**
- Modify: `Design/World Design/Debaucheryville/debaucheryville.md` (STREETS & DISTRICTS section, after "Kebab Alley"; and add Cirque cross-ref already exists under BUILDINGS — leave it)
- Modify: `Design/World Design/Debaucheryville/debaucheryville_locations_index.md` (table)
- Modify: `Design/Mechanics/Battle/status_effects.md` (NEGATIVE STATUS EFFECTS section, after "Tourist Trap Victim")

**Interfaces:**
- Consumes: names/tags/IDs from Global Constraints.

- [ ] **Step 1: Add district block to `debaucheryville.md`** after the Kebab Alley block, matching the file's existing plain-list style:
  ```
  The Bacchanus Riverfront
  Fake Beach Resort District
  The Bacchanus river ("40% water" per EU inspectors) and its embankment party strip
      • The Bohemian Riviera: beach-bar strip charging seaside prices in a landlocked country
      • Fauxst Beach: trucked-in sand, inflatable palm trees, space heaters, lifeguard tower over knee-deep water
      • The Bacchanus Beach Beatdown filming site: pneumatic catapult row, port-o-potty queue, EMTV camera cranes
      • All-night beach parties with college-age summer vacationers
      • Launched port-o-potties occasionally wash back ashore as "monuments"
  ```
- [ ] **Step 2: Add two rows to the locations index table** (keep column formatting):
  ```
  | The Bohemian Riviera    | bohemian_riviera        | Beatdown quest hub, beach-bar shops, night party trigger, catapult minigame |
  | The Cirque du Shady     | cirque_du_shady         | Attraction cluster parent, prophecy tent, prize booth, Shady Productions office |
  ```
- [ ] **Step 3: Add Port-O-Cologne to `status_effects.md`** after "Tourist Trap Victim", matching the file's exact entry style:
  ```
  "Port-O-Cologne"
      • -3 Charm with all NPCs, vendors add a "smell tax" (+25% prices), romance dialogue locked, NPCs step away, fly particle effect follows you
      • Duration: Until paid shower at hostel or spa visit
      • Source: Being launched into the Bacchanus in a loaded port-o-potty (Bacchanus Beach Beatdown loss)
      • Special: Swimming in the Bacchanus to "rinse off" REFRESHES the duration
      • Description: "You smell like second place"
  ```
- [ ] **Step 4: Validate.** `grep -c "Bacchanus Riverfront" debaucheryville.md` ≥ 1; `grep -c "bohemian_riviera\|cirque_du_shady" debaucheryville_locations_index.md` = 2 lines; `grep -c "Port-O-Cologne" status_effects.md` ≥ 1.
- [ ] **Step 5: Commit** (message: `content: add Bacchanus Riverfront district, location index tags, Port-O-Cologne status` + trailer).

### Task 14: Cross-Reference Sweep + Final Validation

**Files:** none created; read-only checks + fixes if needed.

- [ ] **Step 1: ID consistency sweep.** For each canonical ID in Global Constraints, grep the whole `Design/` + `Templates/` tree and confirm consistent spelling (no `bacchanus`/`baccanus` drift, no `Sykora` without the intended diacritic form `Sýkora` in display text — ASCII `sykora` allowed only inside IDs/filenames):
  `grep -rn "baccanus" Design/ Templates/ --include=*.md --include=*.json -i` → only "bacchanus" spellings (case-insensitive matches must all contain the `cch`).
- [ ] **Step 2: Banned-term sweep.** `grep -rni "spring break\|prague\|vltava" <all files created/modified by Tasks 1-13>` → 0 hits. `grep -rni "crypto" <new files>` → hits only in Hamstradamus's Bobo-relationship line and Cirque NPC pointer entries.
- [ ] **Step 3: Template compliance spot-check.** Confirm the sidequest file has every H2 from `Templates/sidequest_template.md`; confirm all four NPC files include the "Bros never achieve self-awareness" checklist row.
- [ ] **Step 4: JSON re-parse all 14.** Same PowerShell loop, filter `bohemian_riviera*.json` + `cirque_du_shady*.json`. Expected: 14 × OK.
- [ ] **Step 5: Fix anything found, then final commit** (message: `content: cross-reference fixes for Beatdown content batch` + trailer — skip commit if nothing to fix).
