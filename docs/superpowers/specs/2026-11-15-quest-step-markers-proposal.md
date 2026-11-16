# Quest step markers: proposal for the two quest files

Bead: Eurobound-wn1f. Desk card: Eurobound-wn1f-q2. Status: **approved and built.** Author answers: wn1f-q2 "Approve as proposed"; wn1f-q3 "A for all four" (Cock-Up 1 and 7a, VIP 1 and 5 all take reading A). Built 2026-11-16 in the two quest files and `game/assets/data/world_data/quest_flags.json`; tests in `game/tests/unit/test_quest_data.gd`.

Author ruling this answers (Desk Eurobound-wn1f-q1, 2026-11-15): "Run quests from data: an agent proposes the missing step markers for both and brings them to me for approval".

## What you are approving

The Quest Log ticks a step when a **marker** (a flag) is switched on. Neither quest file says which marker belongs to which step, so neither quest shows in the log (`game/core/quest_data.gd:67-69`).

For each step below: what the player does, the moment it "counts as done", and whether a marker for that moment already exists or a NEW one is needed. Every step, its order and its content come from your quest docs. Nothing is added, merged or reordered.

Four steps have two possible readings (Cock-Up 1 and 7a, VIP 1 and 5). They are marked **YOUR CALL** and no reading is picked for you.

## Quest 1: The Astronomical Cock-Up (8 steps)

| # | Step | Counts as done when… | Marker |
|---|------|----------------------|--------|
| 1 | The Gathering | **YOUR CALL.** A: the moment the quest starts (the bros enter the square and see the crowd). B: when the bros' opening talk about the crowd ends (Bradley: "...Historical ones.") | A: existing. B: NEW |
| 2 | Scam Gauntlet | the bros have paid all three scammers: the viewing spot, the "Monk" blessing, and the clock wine | NEW |
| 3 | The Show | the 38-second clock show finishes | NEW |
| 4 | Emotional Response | the bros finish crying over the clock (the scene where Lord Pilsner decides on the tattoo) | NEW |
| 5 | Path Choice | the player picks "Full Clock Experience" or "Secret Show Seekers" | NEW |
| 6a | Full Clock Experience (path A) | the bros have bought the plates, the T-shirts, the extra clock wine and the temporary tattoos, and Lord Pilsner finds the tattoo shop | NEW |
| 7a | The Tattoo (path A) | Lord Pilsner has the duck tattoo. **YOUR CALL** on timing for path B, see below | existing |
| 6b | Secret Show Seekers (path B) | 3 AM comes, still nothing, and the bros conclude they are not "spiritually ready yet" | existing |

Finishing the quest needs no change: the file already has its completion markers for both paths.

**Step 7a, YOUR CALL.** On path B your doc says "Lord Pilsner still gets the tattoo during the wait" (before midnight). The tattoo marker that exists today is switched on only when the whole quest finishes.
- Reading A: keep it that way. On path B the tattoo step ticks at the very end, together with the 3 AM step. No marker changes.
- Reading B: the tattoo step ticks the moment the tattoo is done, so on path B it ticks hours before the quest ends. This needs the existing tattoo marker taken out of the "quest finished" lists, because today any marker in those lists finishes the whole quest.

### Small print (Quest 1)

All ids start with `debaucheryville.astronomical_cockup_square.` unless shown in full.

| # | Marker id | Existing or NEW | Source |
|---|-----------|-----------------|--------|
| 1 A | `…astronomical_cockup_started` | existing | `game/assets/data/quests/astronomical_cockup.json:256`; registry `game/assets/data/world_data/quest_flags.json:449`; start moment `design/quests/debaucheryville/astronomical_cockup.md:39` |
| 1 B | `…cockup_crowd_noticed` | NEW | set after the opening exchange, `astronomical_cockup.md:42-52` |
| 2 | `…cockup_scam_gauntlet_done` | NEW | set after the third scam, "Three bottles." / "60 SOVS per bottle", `astronomical_cockup.md:104-108`; the three required scams are `astronomical_cockup.json:42-44` |
| 3 | `…clock_show_witnessed` | NEW in the registry | "Windows close. 38 seconds total.", `astronomical_cockup.md:124-126`. The square's own file already uses this name for this moment (`design/worlds/debaucheryville/interactions/astronomical_cockup_square_interactions.json:65`), but it is not in the flag registry |
| 4 | `…crying_triggered` | NEW in the registry | end of "The Bros' Reaction", `astronomical_cockup.md:136-156`. The square's file already uses this name (`astronomical_cockup_square_interactions.json:106`), not in the registry |
| 5 | `…cockup_path_chosen` | NEW | "Binary Path Choice", `astronomical_cockup.md:160`; `astronomical_cockup.json:68-76` |
| 6a | `…cockup_full_clock_experience_done` | NEW | the five items of "Execution", `astronomical_cockup.md:166-170`; `astronomical_cockup.json:83-87` |
| 7a | `debaucheryville.euro_ink_4_less.duck_tattoo_acquired` | existing | `astronomical_cockup.json:257-258`; registry `quest_flags.json:613`; "Is done. Very beautiful.", `astronomical_cockup.md:186-188` |
| 6b | `…secret_show_sucker` | existing | named on the step itself, `astronomical_cockup.json:127`, and set at path B's end, `:258`; registry `quest_flags.json:531`; `astronomical_cockup.md:220-222` |

Why three existing markers were not used:
- **Step 4, `post_clock_vulnerability`** (`quest_flags.json:1137`): the crying scene switches it on, but it switches itself off after 30 game minutes, so the step would un-tick.
- **Step 5, `cockup_path_a_chosen` / `cockup_path_b_chosen`** (`quest_flags.json:477`, `:492`): they sit in the "quest finished" lists (`astronomical_cockup.json:257-258`), and the log treats any marker in those lists as "quest finished" (`game/core/quest_data.gd:47-51`). Using them at the choice would finish the quest at step 5. The Duck Reveal scene also reads the path A marker as "Complete Path A (get the tattoo)" (`astronomical_cockup.md:316`).
- **Step 6a, `tattoo_decision_made`** (`design/worlds/debaucheryville/core/astronomical_cockup_square_core.json:94`): it opens the alley to the tattoo shop; no file says when it is set, and it is not in the registry.

## Quest 2: The VIP Experience (7 steps)

| # | Step | Counts as done when… | Marker |
|---|------|----------------------|--------|
| 1 | The Approach | **YOUR CALL.** A: the moment the quest starts (Shady Wristband Guy approaches). B: when his pitch ends ("Only 30 SOVS each") and Lord Pilsner answers | A: existing. B: NEW |
| 2 | The Transaction | the bros buy the three wristbands for 90 SOVS | existing |
| 3 | Wristband Application | the bros put the wristbands on | NEW |
| 4 | Velvet Curtain Approach | the bros reach the club and see there is no line ("word got out we were coming. They cleared it.") | NEW |
| 5 | Bouncer Encounter | **YOUR CALL.** A: after the two bouncers' Bohemian exchange (the children's menu joke), before "ID." B: after the bouncer reads it out in English ("Your bracelet says... 'I am seven.'") and the long pause | NEW (either reading) |
| 6 | The Revelation, Ignored | the bouncer says it is from a children's birthday party and Bradley reframes it ("A THEMED birthday party. For VIPs. Seven is probably a tier.") | NEW |
| 7 | Entry Granted | the bros walk into the club (the bouncers' "Američané." plays in the same moment) | existing |

**The quest counts as finished when** the bros walk into the club. The marker for that already exists but sits under a heading the log does not read (`on_club_entry`). Proposal: list that same marker under `on_complete` as well. No new marker.

### Small print (Quest 2)

| # | Marker id | Existing or NEW | Source |
|---|-----------|-----------------|--------|
| 1 A | `debaucheryville.astronomical_cockup_square.vip_wristband_quest_started` | existing | `game/assets/data/quests/vip_wristbands.json:287`; registry `quest_flags.json:574`; `design/quests/debaucheryville/vip_wristbands.md:39-44` |
| 1 B | `debaucheryville.astronomical_cockup_square.wristband_pitch_heard` | NEW | set after `vip_wristbands.md:53-55` |
| 2 | `debaucheryville.astronomical_cockup_square.wristbands_purchased` | existing | `vip_wristbands.json:288`; registry `quest_flags.json:587`; `vip_wristbands.md:81` |
| 3 | `debaucheryville.astronomical_cockup_square.vip_wristbands_all_bros` | NEW in the registry | "Bros carefully put on wristbands", `vip_wristbands.md:84`. The step already names this change (`vip_wristbands.json:66`) and the club's files wait on it (`design/worlds/debaucheryville/core/velvet_curtain_club_core.json:20`), but it is not in the registry |
| 4 | `debaucheryville.velvet_curtain_club.wristband_approach_seen` | NEW | "There is no line." to "They cleared it.", `vip_wristbands.md:107-111`; `vip_wristbands.json:73-77` |
| 5 | `debaucheryville.velvet_curtain_club.bouncer_read_wristband` | NEW | reading A: `vip_wristbands.md:123-135`; reading B: `vip_wristbands.md:145-147`. The doc runs steps 5 and 6 as one scene (`:115-163`); the file splits them at "bouncer reads the wristband" / "bouncer explains" (`vip_wristbands.json:82`, `:96`) and calls the English read-out the "explanation" (`:148`) |
| 6 | `debaucheryville.velvet_curtain_club.birthday_wristband_explained` | NEW | `vip_wristbands.md:151-153`; `vip_wristbands.json:101-104` |
| 7 | `debaucheryville.velvet_curtain_club.vip_wristband_quest_complete` | existing | `vip_wristbands.json:289`; registry `quest_flags.json:668`; "They enter", `vip_wristbands.md:163` |
| finish | the same marker as step 7, listed under `quest_flags.on_complete` | existing | `vip_wristbands.json:289`; the log reads only `on_complete*` (`game/core/quest_data.gd:47-53`) |

Why two existing markers were not used:
- **Step 3, `wristbands_visible_on_sprites`** (`quest_flags.json:600`): the registry says it is switched on when the quest completes, not when the bros put the wristbands on.
- **Steps 5 and 6, `bouncer_encounter_survived`** (`quest_flags.json:655`): it is switched on when the bros get into the club, the same moment as step 7, so it cannot tell steps 5, 6 and 7 apart.

## Count

| Quest | Steps | Existing marker | NEW marker | Depends on your call |
|-------|-------|-----------------|------------|----------------------|
| The Astronomical Cock-Up | 8 | 2 (7a, 6b) | 5 (2, 3, 4, 5, 6a) | 1 (step 1: existing under A, NEW under B) |
| The VIP Experience | 7 | 2 (2, 7) | 4 (3, 4, 5, 6) | 1 (step 1: existing under A, NEW under B) |

## Not decided here

- **The branch.** A path A player never does step 6b, and a path B player never does step 6a. How the log shows the path not taken is still open on Eurobound-wn1f.
- **Step wording in the log.** Until the Writers' Room supplies a line per step, the log shows the step's name ("Scam Gauntlet").
- **Starting the quests.** Nothing in the game switches on either quest's start marker yet (Eurobound-ou0t).

## After approval (for the agent who implements it)

1. Add each approved NEW id to `game/assets/data/world_data/quest_flags.json` in the registry's form: `type: bool`, `default: false`, `category: quest`, `write_once: true`, `set_by` in the words of the "Counts as done when…" column, the quest's `quest_id`, `doc` = the quest-doc line in the Source column, `status: ruled`.
2. Add `"done_when": ["<id>"]` to each of the 15 stages in the two quest files, and `"on_complete"` to `vip_wristbands.json` `quest_flags`.
3. If the author picks reading B for Cock-Up step 7a, move `duck_tattoo_acquired` out of `on_complete_a` / `on_complete_b` in the same change.
4. Done means `QuestData.load_dir()["incomplete"]` is empty, `Tools/validate_data.py` passes, and both quests appear in the Quest Log.
