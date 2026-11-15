# Handoff: ABSINTHE ORCHESTRATOR (2026-11-15)

**Window name: Absinthe Orchestrator.** This window can be cleared once you've read this. Per the author's note (bead Eurobound-jpkw), new work goes to a fresh window, one task each.

## What this window owned
- The Absinthe Arcade build (hall, Taproom, restroom, claw closet), plus merging and committing for the teams.
- Relaying Eurobound Desk answers to the windows that asked (claim `relayed: true`, SendMessage the answer verbatim).
- Bead-page sync (`Tools/orchestrator/sync_check.py`) and the QC review team (Eurobound-2boh).

## Done in the last stretch (all on main, pushed)
- Arcade data: VIP arrows at the bar front, scratched service note dropped (6580d794).
- 3D look-B characters in the hall: Jakub (53def99e), Cara (f13a76cf), Tomáš (plain, plus a ringed set swapped in by `ring_on()`), Ashleigh, Kenleigh, Brynleigh (f1031023, e1ea2cca), the Accounts Receivable twins at 2.1 m (0cd1cdfc). Jakub asleep in the restroom as a 3D render (e5336d25). `HallNpc.use_look_b()` loads any hall character's look-B frames.
- Lord Pilsner's turn-order portrait v3 (3c968686).
- Claw-closet wiring zap barks: the approved 4-line pool per bro, with a cooldown (78ac0a81).
- "Europe" banned from player-facing text; it is Euromemeia/Euromemeian. The talk box is now half the screen wide (6b2b6b31).
- Committed for other teams: Sprite tools and frames, the Writers' Room task records and docs (c7f9024a).

## Open: needs the author (Eurobound Desk)
- **ANSWERED 2026-11-15: Eurobound-8c3z-q1, "Research 2-3 approaches (fixed sprites, real-time 3D in the room, painted HD sprites) and show me in-game mock shots of each before anything else is made".** That is the next task: give it to a fresh window. Mock all three in the Arcade hall with the same characters, then post them on the Desk side by side. Nothing else character-related gets made first. Earlier note on this item: **Eurobound-8c3z-q1: how to fix the characters** (pixel art still present, smudged and deformed in game). This is the top priority. Bead Eurobound-8c3z holds the diagnosis:
  - The look-B frames are drawn at about 1/3 size with LINEAR filtering and no mipmaps.
  - Tripo deformities passed reviews that never judged the characters in game.
- `sprite-dev-g3-whitney-bradley`, the Chadwick cards and `sprite-dev-pilsner-g4-retro`: these block the last pixel-art characters.
- Eurobound-3ho-q14 answered ("Approve all..."): eurobound-2b puts the Backpack Girl final on bead 3ho; then wire it (Arcade completion arc).
- asset-team-qc-arcade-hall-31a: the fix round is running in the Asset team. After it passes, wire 3.1a (scene gd:230-239). 3.1b (bidet, Sea-Monkeys card, VIP arrows, nest) follows.

## Open: for the next window
- **Do not ship new character art** until the author picks an option on 8c3z-q1 and has seen it in game.
- Eurobound-04t2: the Beads team's agent will move `dialogue_box.gd` to shared code and switch off the Dialogue Manager add-on. You review and merge. Conditions:
  - class_name and API stay unchanged;
  - no hand edits to project.godot;
  - the full GUT suite passes.
- Keep out of `status_effects.json`, `consumables.json` and `tools/validate_data.py` until the Beads team says its data agent has landed.
- Not built yet:
  - the NAP/DON'T NAP prompt (approved in `design/narrative/opening_step1.md`);
  - the closet blacklight wall switch (bcnr-q8; needs the switch art from the Closet reference set);
  - the wiring spark FX (art).
- Beads opened here:
  - Eurobound-jt8q: the Europe sweep (Writers' Room has it);
  - Eurobound-rpac: item physical descriptions;
  - Eurobound-v2vg: commit_paths can't stage new files under tools/ vs Tools/;
  - Eurobound-m4sc: gitignore the banned `tripo_client.py`;
  - Eurobound-jpkw: one task per window, then handoff;
  - Eurobound-8c3z: the character rethink.
- Desk relay: this window ran the "Eurobound Desk relay fallback" and "eurobound-ad" check crons. They stop when this window is cleared. Jpkw asks where relaying lives next.

## Gotchas
- New files under `tools/char3d/` need `git hash-object -w` plus `update-index --cacheinfo` under the `Tools/` spelling until v2vg is fixed.
- The repo is public: no absolute local paths in tracked files.
- Run GUT with `python -I Tools/orchestrator/gut.py --import` after any checkout or merge.
