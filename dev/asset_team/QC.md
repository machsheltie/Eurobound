# Asset QC gates (author, 2026-11-13: "You'd better get the review team after the sprite team and asset development teams too as some of the shit they do is a bit dicey. We need qc for sure")

> **Coverage (author, 2026-11-14: "be sure ALL types of assets/sprites are being reviewed by our blind agents"; bead Eurobound-lrg5):** every asset type, its gate, and the checklists for types not covered below (K key art, N NFT, U UI, V VFX, E enemy battle, P dialogue portraits, T tilesets and kits, S audio, C 2D cut-outs, plus the A2+ decomposition check) are in `dev/qc/QC_COVERAGE.md`. Assets accepted before a gate existed are queued in `dev/qc/retro_queue.md`.

Nothing the Asset Development Team makes reaches the author (the Desk), Tripo (credits), the Asset Board as "done", or the game until an independent reviewer passes it.

- **Who reviews:** a fresh Sonnet subagent that has never seen the job. It gets only the files named in its gate, this checklist and the author's rulings quoted in the brief. It never gets the producer's reasoning or earlier attempts. The producing agent never reviews its own work.
- **What a fail means:** a fail goes back to the producer. After two failed fixes, the item goes to the author on the Desk with the attempts side by side.
- **One exception (owner ruling, 2026-11-13):** if the only remaining fail is mechanical lettering, meaning text that must match the doc exactly, the producer may make one more fix. It must be done by local re-lettering only (for example Pillow), with no regeneration, and followed by a fresh blind review of the whole gate. Log it as "fix-3 (owner-approved, mechanical)". If that review fails anything, the item goes to the Desk. Judgment calls (look, parody, palette, layout) never get a third fix. The same exception covers a mechanical colour match to a colour the doc names exactly (for example a palette swap to "highlighter yellow"): one deterministic recolour of the texture, with no regeneration and a fresh review of the whole gate. An item gets this extra fix only once, whatever the cause.
- **Who owns it:** the review team is owned by the Absinthe Orchestrator (bead Eurobound-2boh). It keeps these checklists, reads the QC log and re-runs its own blind review on any item it doubts. The character equivalent is `Tools/char3d/QC.md`.

## Gates

| Gate | When | Reviewer gets | Must pass |
|---|---|---|---|
| A1 Plan | Before a plan goes on the Desk | `plans/<id>_plan.md` + the building's main `.md` + its PNG spec + `style_refs/existing_exteriors_contact.jpg` / `existing_interiors_contact.jpg` | Checklist P |
| A1.5 Seediness thumbnail | The first day plate, before any night relight, elevation or lettering work | One 512 px thumbnail + the plan's "what the building exaggerates" line | Checklist L items 1 and 3 only. A fail here means a FRESH generation, never an edit of the failed plate |
| A2 Plate | Before plates go on the Desk or the board | The review sheet + the author-approved plan (with the author's notes) + the palette lines | Checklist L |
| A3 Tripo input | Before spending Tripo credits (icons, props, kits) | The Tripo source image + the approved reference or spec | Checklist T |
| A4 Model / icon | After the Tripo build and render | Render(s) + the approved reference | Checklist M |
| A5 In game | When the asset is wired into a scene | Fixed shots via `Tools/critic_loop` | Blind critic score >= 7 on every shot |

## Why plates came out cosy, and the standing fixes (QC owner, 2026-11-14)
Root cause: `docs/superpowers/reports/2026-11-14-generic-plates-root-cause.md`. These rules apply to every location from now on:
- **A1 is mandatory before any painting.** No plate is generated without a passing A1 line in `qc_log.jsonl`.
- **Every plan turns each bracketed or dialogue-only joke into a paintable prop.** It lists five or more modern, seedy props (trash, signage, damage, vice), states the lighting, and names the one thing the building exaggerates, readable at thumbnail size.
- **Prompts put the seedy props first and the style boilerplate last.** They carry the standing ban list: golden hour, sunbeams, flower boxes, potted plants, trees, moss, candle-lit windows, half-timbering, storybook lean. They also avoid the words "ancient", "quaint", "charming", "cosy", "tavern", "candlelight", "historic" and "traditional" unless the doc names them. Overcast or harsh light is allowed. Save every prompt in `dev/asset_team/prompts/<id>_<n>.txt`.
- **Style references:** only Absinthe Arcade plates, uploaded for brushwork, never for palette. Never use a Shamsterdam plate or any failed plate as a reference.
- **A seediness fail at A1.5 or A2 means a fresh generation,** never an edit of the failed plate.

## Checklist P (plan)
1. It lists all nine files for the location (main `.md`, `core/`, `environment/`, `interactions/`, `items/`, `location_nodes/`, `npcs/<Location>/`, `PNG_Assets/`, `sprite_mapping/`, plus `events/`), each marked read or MISSING.
2. Every palette hex is quoted from the doc's Color Palette and assigned a place. No invented colours.
3. Each of its 3-5 satire beats cites a real doc line. The beats are over the top, scandalous and seedy, and the building itself tells the joke. A respectable, tidy or historical-streetscape plan fails ("I don't want respectable Prague").
4. All signs and text are doc text only. Anything not in the files is listed as a question, not decided.
5. It differs visibly from the existing-plates contact sheets: storeys, roofline, window rhythm, shopfront, staging; for interiors, floor material, plan and light. A plan that repeats the cream stucco block, the stepped gable with canal railing, or the glossy checkerboard floor (unless the doc names it) fails.
6. No real place names. Real brands keep their real names. No nudity.
7. Every joke the doc keeps in brackets, dialogue or "lawyers insisted" asides is turned into a paintable object. The plan lists five or more modern, seedy props, states the lighting (no golden hour, no candle-warm glow unless the doc names it), and names the one exaggeration readable at thumbnail size.

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

## Reference-locked review for every 3D asset (author protocol 2026-11-14, steps 9-11; bead Eurobound-nhxz.8)
Binding source: `design/style_guides/reference_locked_texturing_protocol.md`. It applies to gates A3 and A4, and to G3 and G4 in `Tools/char3d/QC.md`.
1. **Standard renders.** Use one render set per asset:
   - the reference view (the camera matched to the approved art);
   - front, side and back views;
   - neutral lighting and the intended game lighting;
   - fixed camera, exposure and colour management across attempts, so that rounds can be compared.
2. **Region-by-region comparison.** Pair each material region in the render with the same region in the approved art. Until `tools/paint_zones` (SAM) exists, the reviewer names the regions by hand. Judge each region for colour, surface character, markings, texture scale, finish, boundaries and seams, and placement. Use numerical colour difference only where the regions and lighting line up.
3. **Correction.** Repair only the failing regions. Never regenerate regions that already pass. Repeated failure goes to the Desk with a precise issue report (the two-fix rule above).
4. **Outcome:** exactly one of **APPROVED**, **REVISION REQUIRED** or **BLOCKED**.
   - APPROVED needs all of: reference fidelity, UV and texture validation, correct PBR behaviour, and an acceptable look at in-game scale.
   - If a protocol step couldn't run (a tool missing or not yet approved, e.g. Desk nhxz-q2 / q3), the report names the step and the fallback used. It never claims the full workflow ran.
5. **Non-negotiables the reviewer checks:**
   - the approved art outranks any generated interpretation;
   - a correct silhouette with wrong materials is not complete;
   - no generic photoreal substitutes for painterly or distinctive surfaces;
   - no unjustified upscaling;
   - observed details and invented ones are labelled.
6. **Reviewer reply** adds `"outcome": "APPROVED|REVISION REQUIRED|BLOCKED"` and `"regions": [{"region", "verdict", "issue"}]` to the usual JSON.

## Checklist M (3D model / icon render)
1. The silhouette and proportions match the reference. There is no mesh soup, no fused parts and no missing pieces.
2. Lettering reads correctly in a large crop.
3. Icons: the approved look B (`Tools/item3d/README.md`), fixed ortho scale 0.95, the subject centred with a margin, and it reads at 128 px.
4. Buildings and props: the graybox passed before ornament (`3d_asset_rules.md`, "Architecture before detail"), and kit modules are reused, not regenerated.

## Reviewer reply
`{"item": "<id>", "gate": "A1|A2|A3|A4|A5", "pass": true|false, "fails": ["<checklist item>: <concrete issue and where>", ...]}`

Append every reply, pass or fail, to `dev/asset_team/reviews/qc_log.jsonl` with the item id and the date. The Desk card for an item cites its passing gate line.
