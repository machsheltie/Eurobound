# Character QC gate (author, 2026-11-13: "some of the shit they do is a bit dicey. We need qc for sure")

Nothing from the character pipeline reaches the author (the Desk), Tripo (credits) or the Orchestrator (frames) until an independent reviewer passes it. The producing agent never reviews its own work. Each reviewer is a fresh Sonnet subagent that gets the images and this checklist, nothing about how they were made, and replies in JSON.

## Gates

| Gate | When | Reviewer compares | Must pass |
|---|---|---|---|
| G1 Source | Before a portrait goes on the Desk | Portrait vs the model sheet and doc lines quoted in the brief | Checklist A |
| G2 Tripo input | Before spending Tripo credits | Tripo source vs the Desk-approved portrait | Checklist A, plus "only the requested change differs" |
| G3 Model | After the Tripo build and rig | Rest render S/E/N plus a large face crop vs the approved portrait | Checklist B |
| G4 Frames | Before frames go to the Orchestrator | Contact sheet of 8-dir idle/walk plus a game-size crop | Checklist C; blind critic face score >= 7 |

## Checklist A (2D source)
1. Every word on the image is spelled exactly as in the brief, letter by letter (hat patches, jerseys, badges, sashes, name tags). Garbled or extra text fails.
2. Anatomy: five fingers per hand, two of each limb, no fused or missing parts, both feet and shoes visible.
3. One figure, head to toe, facing the viewer, arms clear of the torso, hands empty unless the brief says otherwise.
4. Every outfit item in the brief is present and the right colour; nothing is added that the brief or sheet doesn't have.
5. Face detail to Pilsner's bar: open eyes with lids, irises and catchlights; defined nose and nostrils; mouth and teeth; skin texture; stubble where due. Not airbrushed.
6. Expression matches the brief (the bros are sincere doofuses: never smug, never clever).
7. Nothing in it sanitises the character or contradicts the doc and the author's rulings in the brief.

## Checklist B (3D model)
1. The face is not the back of the head; the front and back views are not mixed up.
2. There are no merged limbs, fused hands and thighs, or webbing between the arms and torso.
3. All lettering reads correctly in the large crop (re-project with `project_ref.py` if not).
4. The face keeps the portrait's features and expression; it isn't generic or smoothed over.
5. Props that must not be there are culled; props that must be there are present.

## Checklist C (look-B frames)
1. Feet are planted on the floor line, at the same scale as the other characters (height_m from the config).
2. No frame stretches, tears or drags clothing (hands, shorts, lanyards).
3. The head isn't pitched up or down in the side and back views, and the sunglasses and lenses are complete.
4. Every walk frame reads as a stride; the idle reads as breathing, not frozen.
5. At game size the face still reads: eyes, mouth and expression are visible.
6. All 8 directions are present, frame counts are correct, and there are no empty frames.

## Log
Append every reviewer reply, pass or fail, to `tools/char3d/qc_log.jsonl` with a `date` field, and cite the passing line when posting on the Desk or sending frames. The review team (Absinthe Orchestrator, Eurobound-2boh) audits the log and spot-checks.

## Reference-locked review (author protocol 2026-11-14)
G3 and G4 also follow the review rules in `dev/asset_team/QC.md`, "Reference-locked review for every 3D asset". That means standard renders, region-by-region comparison against the approved portrait, repairs to failing regions only, and exactly one outcome: APPROVED, REVISION REQUIRED or BLOCKED. Source: `design/style_guides/reference_locked_texturing_protocol.md` steps 9-11. The Chadwick trial (the author's Desk answer on nhxz-q1) is the first asset reviewed this way.

## Reviewer reply
`{"item": "<id>", "gate": "G1|G2|G3|G4", "pass": true|false, "fails": ["<checklist item number>: <concrete issue and where>", ...]}`. A fail goes back to the producer; after two failed fixes it goes to the author on the Desk.
