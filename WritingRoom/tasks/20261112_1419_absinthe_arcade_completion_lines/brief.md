# Absinthe Arcade completion lines

Requested by the Absinthe Orchestrator (Arcade completion). The author approved the Arcade scope in round v42. Each part below is a separate deliverable section, so the author can approve them one at a time.

## Binding rules
- **The bros (Pilsner, Chadwick, Bradley) are sincere doofuses.** No witty bro quips, no knowing references, and no crimestopping or investigating. The comedy is how wrong they are. The author has rejected "too clever" bros twice. NPCs, examine text and microcopy can be razor-sharp.
- Full MA satire, no narrator, and don't explain the joke. The only ceiling is no nudity.
- No real place names. Real brands, games and songs keep their real names. Money is SOVS ("1 SOV"). All names unique (grep design/).
- Lines are 280 characters max (design/style_guides/writing_limits.md).
- The window cat on the Arcade facade is canon set dressing, never a mascot: no name and no companion behaviour.
- Junk-item rule: an inspect line pays off, short, as dark and dirty as it likes.

## Read first
- .claude/CLAUDE.md
- design/worlds/debaucheryville/absinthearcade.md
- design/worlds/debaucheryville/clawmachinemaintenanceclosetrestroom.md (lines 88-122)
- design/World Design/Debaucheryville/interactions/absinthe_arcade_interactions.json (the "Good Games, Bad Decisions" entry)
- design/World Design/Debaucheryville/npcs/Absinthe_Arcade/absinthe_arcade_npcs.json (ambient_npcs)
- design/worlds/debaucheryville/npcs/Absinthe_Arcade/jakub_tokens_dvorak.md
- design/Quests/debaucheryville/grandpa_provides.md (the approved scenes, round v30)
- WritingRoom/tasks/20261111_1412_jakub_restroom_scene/final.md (Jakub's approved voice)

## Deliverable: drafts/<writer>_arcade_completion.md

1. **Maintenance closet.** One examine line or short exchange each for:
   - the DDR-arrow toilet
   - the CRT mirror (loops "INSERT COIN"; give 2-3 easter-egg read-outs)
   - the used-sock prize chute
   - the sparking wiring
   - the 30-second shame timer (canon line: "You've achieved nothing but shame, player one"; give 2-3 escalating variants)
   - a one-line read-out for each graffiti wall (the graffiti text is canon; don't change it)
2. **Small hooks.**
   - The first-entry cinematic "Good Games, Bad Decisions" (a short beat, 4-8 lines).
   - Fake VIP arrows that loop back to the bar (2-3 lines as the bros follow them, sincerely).
   - The bidet bar stool (one polite chime, plus its examine line).
   - Exterior examines: the street cabinet, the chalkboard, the window cat (set dressing only).
   - The club-flyer panel.
3. **Ambient group barks, 4-6 lines per group.**
   - Twitchy Hackers: they hint the mirror shadow puzzle.
   - EDM Ghosts.
   - Rogue Backpackers.
   - Bathroom Route Speedrunners: they hint the 3-token DDR unlock.
   - Hints come out of the NPC's own obsession, never as a tutorial.
4. **Jakub's reaction when the bros win Sea-Monkeys from the rigged claw.** Author ruling: "Jakub for the first one. Drop the second." Use Jakub's voice from his profile and the restroom final.
5. **Quest Log entries for Grandpa Provides.** One plain, short objective line per step. These are log text, not jokes; match the approved scenes' step order.

Save early, post a summary, then vote done.

## Added 2026-11-12 (author: "Writers' Room drafts both", Eurobound Desk orch-fight-wisp-lines; relayed by the Absinthe Orchestrator)

6. **The Green Fairy Wisp (boss, The Absinthium Taproom).** Canon voice: design/worlds/debaucheryville/the_absinthium_taproom.md:167-185.
   - Her phase 1 line: "You sought me, and now you've found me. Was it worth it?"
   - Her phase 2 line: "Which version of yourself would you prefer?"
   - Write **(a)** her phase 3 line as she drops into "The Reckoning" (room distortion, control reversal, final attack "The Truth"). Give 3 options.
   - Write **(b)** her line as she leaves after the bros survive 6 rounds (the fight counts as "survived"). Give 3 options.
   - She is the cryptic one. The bros' reactions, if any, stay dumb.
7. **Grandpa Provides: the loss.** design/Quests/debaucheryville/grandpa_provides.md:348 has the ruled outcome: the bros wake on the street outside at 1 HP, and the tab and service charge (50 SOVS) are taken from the wallet. If the wallet is short, it is emptied and the rest is waived. "Grandpa Provides" is the title only and is never spoken.
   - Write **(a)** the loss line (whoever speaks it, per the approved scenes).
   - Write **(b)** the "tab stolen" Quest Log objective: one plain line, matching section 5.
8. **Dr. Vaněk's opener check, new line 1** (the_absinthium_taproom.md:34-36). This case is "With the Keychain, No Absinthium Opener". The old line offered to sell the opener for 22 SOVS; that path is DEAD (the opener is earned only, via the Mirror Maze).
   - Write 3 options for a replacement that sends them to the maze.
   - The line for "With Both Openers" is approved. Its "Either way" no longer has a second way: offer one minimal fix to that phrase only, and change nothing else.

**Queue order (author, wr_queue_order = arcade):** this task runs FIRST once OpenRouter is topped up.

## Added 2026-11-13 (author, Eurobound Desk orch-vanek-q1: "Wait for the Writers' Room top-up"; relayed by the Absinthe Orchestrator)

9. **Dr. Vaněk, two more gaps** (game/core/vanek_taproom.gd has empty constants for both; section 8 covers the third). Canon voice: design/worlds/debaucheryville/the_absinthium_taproom.md, his check lines (:34-37), serving lines (:235-238) and stamp speech (:213-214). He is a deadpan "researcher" who treats the bros as test subjects.
   - **(a) Can't afford the Absinthe Lager** (12 SOVS; the wallet is short). Give 3 options. One line each. He does not lend, discount or give it away.
   - **(b) Return visits after the bros are stamped.** Give 4-6 callback lines he can cycle through. Nothing that implies new quests, rewards or mechanics.
   - His "research survey" is NOT in this task (Claude pitches it to the author separately). Don't write it or reference its questions.

## Added 2026-11-13 (Arcade Build Board card t_employee, relayed by the Absinthe Orchestrator)

10. ~~**Jakub reacts to the club flyers.**~~ **STRUCK 2026-11-13: the author's arc_employee ruling "Jakub for the first one. Drop the second." dropped the flyer reaction ('Did you make this on Microsoft Publisher?'). Write nothing for it.** Original text: Besides the flyer panel's examine line (section 2), write Jakub's reaction when a bro picks up or reads a club flyer. Give 2-3 options, in Jakub's voice (profile + restroom final). Section 4's Sea-Monkeys reaction is the card's "you actually won that" beat. Note: "Unfortunately, bro, you actually won" is Jaxson Vane's canon line (bacchanusbeachbeatdown.md:529), so Jakub must not reuse that wording.
