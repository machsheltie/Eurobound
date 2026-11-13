# Asset QC gates (author, 2026-11-13: "You'd better get the review team after the sprite team and asset development teams too as some of the shit they do is a bit dicey. We need qc for sure")

Nothing the Asset Development Team makes reaches the author (the Desk), Tripo (credits), the Asset Board as "done", or the game until an independent reviewer passes it.

- **Who reviews:** a fresh Sonnet subagent that has never seen the job. It gets only the files named in its gate, this checklist and the author's rulings quoted in the brief. It never gets the producer's reasoning or earlier attempts. The producing agent never reviews its own work.
- **What a fail means:** a fail goes back to the producer. After two failed fixes, the item goes to the author on the Desk with the attempts side by side.
- **Who owns it:** the review team is owned by the Absinthe Orchestrator (bead Eurobound-2boh). It keeps these checklists, reads the QC log and re-runs its own blind review on any item it doubts. The character equivalent is `Tools/char3d/QC.md`.

## Gates

| Gate | When | Reviewer gets | Must pass |
|---|---|---|---|
| A1 Plan | Before a plan goes on the Desk | `plans/<id>_plan.md` + the building's main `.md` + its PNG spec + `style_refs/existing_exteriors_contact.jpg` / `existing_interiors_contact.jpg` | Checklist P |
| A2 Plate | Before plates go on the Desk or the board | The review sheet + the author-approved plan (with the author's notes) + the palette lines | Checklist L |
| A3 Tripo input | Before spending Tripo credits (icons, props, kits) | The Tripo source image + the approved reference or spec | Checklist T |
| A4 Model / icon | After the Tripo build and render | Render(s) + the approved reference | Checklist M |
| A5 In game | When the asset is wired into a scene | Fixed shots via `Tools/critic_loop` | Blind critic score >= 7 on every shot |

## Checklist P (plan)
1. It lists all nine files for the location (main `.md`, `core/`, `environment/`, `interactions/`, `items/`, `location_nodes/`, `npcs/<Location>/`, `PNG_Assets/`, `sprite_mapping/`, plus `events/`), each marked read or MISSING.
2. Every palette hex is quoted from the doc's Color Palette and assigned a place. No invented colours.
3. Each of its 3-5 satire beats cites a real doc line. The beats are over the top, scandalous and seedy, and the building itself tells the joke. A respectable, tidy or historical-streetscape plan fails ("I don't want respectable Prague").
4. All signs and text are doc text only. Anything not in the files is listed as a question, not decided.
5. It differs visibly from the existing-plates contact sheets: storeys, roofline, window rhythm, shopfront, staging; for interiors, floor material, plan and light. A plan that repeats the cream stucco block, the stepped gable with canal railing, or the glossy checkerboard floor (unless the doc names it) fails.
6. No real place names. Real brands keep their real names. No nudity.

## Checklist L (location plates)
1. Every element of the approved plan, and every note the author added to it, is present. Count windows, signs, props and named sub-areas.
2. The palette is binding: the Primary colour dominates, the Accent draws the eye, the Background sets the ground. The plate's main colours must be the doc's hex values.
3. It reads as over the top and as a parody of its own theme at a glance, not as a generic or respectable building.
4. **Every word on the image, letter by letter.** It must match the doc text exactly. Misspellings, extra invented signage, logos or names fail ("GEGRETS" was a real miss).
5. Camera and format: the fixed tilt camera (about 30-40 degrees down for exteriors, a high three-quarter view for interiors), 16:9, at least 2048 px wide, the building centred and complete.
6. No people or vehicles painted in. Interiors keep straight rows and real open floor.
7. Painterly HD-2D, never photoreal. Night is pixel-registered to day, and an interior's night plate is the exact pixel size of its day plate.
8. Neighbouring buildings are plain and unnamed, with no construction scaffolding or tarps unless the doc says so.
9. It is not a look-alike of anything on the contact sheets.
10. No distress or weathering painted where the author hand-paints it (3D surfaces: `design/style_guides/3d_asset_rules.md`).

## Checklist T (Tripo input)
1. One object, complete, on a clean background, matching the approved reference or spec.
2. The lettering is correct, or there is none (lettering is projected afterwards).
3. Only the requested change differs from the approved reference.

## Checklist M (3D model / icon render)
1. The silhouette and proportions match the reference. There is no mesh soup, no fused parts and no missing pieces.
2. Lettering reads correctly in a large crop.
3. Icons: the approved look B (`Tools/item3d/README.md`), fixed ortho scale 0.95, the subject centred with a margin, and it reads at 128 px.
4. Buildings and props: the graybox passed before ornament (`3d_asset_rules.md`, "Architecture before detail"), and kit modules are reused, not regenerated.

## Reviewer reply
`{"item": "<id>", "gate": "A1|A2|A3|A4|A5", "pass": true|false, "fails": ["<checklist item>: <concrete issue and where>", ...]}`

Append every reply, pass or fail, to `dev/asset_team/reviews/qc_log.jsonl` with the item id and the date. The Desk card for an item cites its passing gate line.
