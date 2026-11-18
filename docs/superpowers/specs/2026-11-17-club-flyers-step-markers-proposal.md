# Club Flyers: step markers proposal

Bead: Eurobound-3ddh. Desk card: Eurobound-3ddh-q1. Status: **waiting on the author.**

Why this needs you: your answer on Eurobound-wn1f-q1 was "Run quests from data: an agent proposes the missing step markers for both and brings them to me for approval". Club Flyers (`design/quests/debaucheryville/club_flyers.md`) is the third quest file. Its doc names no markers, so they come to you the same way before any of them goes into the game.

The quest data is drafted and waiting: `docs/superpowers/specs/2026-11-17-club-flyers-quest-draft.json`. Every line of dialogue in it is copied from the doc by line number. Its step and completion markers are empty until you answer. It is not in `game/assets/data/quests/` yet, because the Quest Log test `test_quest_data_shipped_quest_files_are_all_complete` (`game/tests/unit/test_quest_data.gd:185`) fails on a quest file without markers.

## What you are approving

The Quest Log ticks a step when a **marker** (a flag) is switched on. The steps are the doc's own sections, in the doc's order. Nothing is added, merged or reordered.

| # | Step | Counts as done when… | Marker |
|---|------|----------------------|--------|
| 1 | Quest Initiation | Vanessa's hiring scene ends ("Please don't.", `club_flyers.md:59`). The quest starts at the same moment, as with VIP step 1 (your "A for all four", wn1f-q3) | NEW |
| 2 | The Design Phase | the laptop scene at the hostel ends ("This is coming together. Now we need VISUALS.", `:83`) | NEW |
| 3 | The Flyer Creation | the flyer is finished ("Just the Hotmail.", `:112`) | NEW |
| 4 | Binary Path Choice | the player picks "Web 1.0 Marketing Mastery" or "Alpha Male Vandalism 2001" (`:116-118`, `:216`) | NEW |
| 5a | Web 1.0 Marketing Mastery (path A) | **YOUR CALL.** A: the bros have done all six postering jobs in "Execution" (`:128-133`). B: Vanessa pays the 100 SOVS (`:202`; the doc writes no scene for it) | NEW |
| 5b | Alpha Male Vandalism 2001 (path B) | Hynek's scene at the club ends ("They think it's an art project?", `:300`) | NEW |

**The quest counts as finished** when step 5a or 5b is done. The post-credits scene "The LinkedIn Update" unlocks on "Complete either path" (`:447`), so one extra marker, switched on at the end of either path, unlocks it.

## Small print

All ids start with `debaucheryville.velvet_curtain_club.` (Vanessa's club, where the quest is given; the doc names no hostel for step 2, `:65`).

| # | Marker id | Where it is listed |
|---|-----------|--------------------|
| 1 | `club_flyers_started` | `quest_flags.on_start` and step 1 `done_when` |
| 2 | `club_flyers_design_phase_done` | step 2 |
| 3 | `club_flyers_flyer_created` | step 3 |
| 4 | `club_flyers_path_chosen` | step 4 only. Not in a "quest finished" list: the log treats any marker there as "finished" (`game/core/quest_data.gd:47-51`), the Cock-Up lesson in `2026-11-15-quest-step-markers-proposal.md` |
| 5a | `club_flyers_path_a_done` | step 5a and `quest_flags.on_complete_a` |
| 5b | `club_flyers_path_b_done` | step 5b and `quest_flags.on_complete_b` |
| end | `club_flyers_complete` | both `on_complete_a` and `on_complete_b`; `post_credits_scene.unlock_condition` |

Eight new markers, none existing. One existing flag is related but is not a step marker: `club_flyer_placed` (`game/assets/data/world_data/quest_flags.json`, "NOT BUILT: the bros poster the Arcade with their club flyer") is path A's second job, "Poster Absinthe Arcade entrance" (`:129`). It stays as it is.

## Not decided here

- How the log shows the path not taken (open since Eurobound-wn1f).
- Step wording in the log: until the Writers' Room supplies a line per step, the log shows the step's name.
- Starting the quest: the doc's trigger is "Bros visit Velvet Curtain Club after previous quests" (`:42`) and names no quest (Eurobound-ou0t runs quests).
- Other gaps the draft marks pending: the duration is a range ("30-40 minutes", `:10`); no NPC except Vanessa has a profile id; the reward items have no item docs (Eurobound-gora); Path A's "SOVS reward" has no amount (`:209`).

## After approval (for the agent who implements it)

1. Add each approved id to `game/assets/data/world_data/quest_flags.json`: `type: bool`, `default: false`, `category: quest`, `write_once: true`, `set_by` in the words of the "Counts as done when…" column, `quest_id: debaucheryville_sidequest_club_flyers_01`, `doc` = the `club_flyers.md` line above, `status: ruled`.
2. Fill the draft's `done_when`, `quest_flags` and `post_credits_scene.unlock_condition`, drop those keys from its `_pending`, and move it to `game/assets/data/quests/club_flyers.json`.
3. Add Club Flyers to `APPROVED_STEPS` in `game/tests/unit/test_quest_data.gd`.
4. Done means `python -I Tools/validate_data.py` has 0 FAIL and `python -I Tools/orchestrator/gut.py --select test_quest_data` passes.
