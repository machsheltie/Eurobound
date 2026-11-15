# Closet props — physical descriptions (icon art briefs)

Mistral, Round 1 (Phase 4). Five props for the Claw Machine Maintenance Closet Restroom (Debaucheryville, Absinthe Arcade hidden area), in the 12-field "🖼️ Physical description (icon art brief)" format (Desk rpac-q1). Props/decals: `scale_cue` = how big it is on the wall; `contents` = "none".

Palette anchors (all from `design/worlds/debaucheryville/PNG_Assets/Claw_Machine_Maintenance_Closet_Complete_PNG_Asset_Requirements.md` 🎨 Color Palette): Fluorescent Green #00FF41, Retro/LED Pink #FF69B4, Grime Brown #3C2415, Shadow Black #1C1C1C, Metal Grey #808080, UV Purple #9400D3, Spark Yellow #FFFF00, Neon Cyan #00FFFF, Magenta #FF00FF, Door Brown #8B4513, Token Gold #FFD700.

Room facts used below (from `game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.gd`): tiles are 0.28 m; wall height 14 tiles (~3.9 m); wiring hotspot on the right wall at (4.75, 5.5); joystick hotspot left wall at (-3.1, 2.4); haiku on free left wall at (-3.8, 6.0); chandelier hangs from the ceiling over the room's back half. Examine-line canon from `game/core/closet_props.gd`.

---

## 1. Blacklight wall switch (examine toggles it on/off — Desk bcnr-q8)

| Field | Description |
|-------|-------------|
| **silhouette** | A single-gang toggle switch plate, roughly 1:1.6 (width:height), mounted high on the left wall near the door, with one dark tube fixture visible on the back wall above the graffiti. |
| **scale_cue** | The plate reads as a small beige rectangle about 0.35 x 0.55 tiles (10 x 15 cm) on the wall; the tube reads as a thin horizontal bar about 6 tiles long. |
| **materials_and_cheap_cues** | Yellowed ivory plastic plate with a visible mould seam down the middle, one Phillips screw at the top (the bottom screw is missing and the hole is stripped), toggle lever slightly crooked in its slot. The tube is cheap blacklight glass in a dented metal-grey channel bracket, held by one bracket and one length of tape. |
| **colours** | Plate: aged off-white #E8E0C8 with grime-brown #3C2415 smudges around the screw holes. Toggle: same plastic, darker where handled. Tube off: dark violet-grey glass #2A2A3A with UV Purple #9400D3 edge shading. Tube on: glowing UV Purple #9400D3 with a pale lavender core #C77DFF. |
| **contents** | none |
| **decoration** | A strip of masking tape above the plate with a hand-scrawled label in marker; the marker is faded to a ghost outline. |
| **condition** | Plate cracked at the missing-screw corner; toggle yellowed and stiff. Tube: one end blackened where the starter died, flickers on startup. |
| **garnish_and_addons** | The controlled blacklight tube itself, mounted on the back wall, plus the tape label. Nothing else on the plate. |
| **palette_anchors** | UV Purple #9400D3, Grime Brown #3C2415, Metal Grey #808080 from the closet palette; aged off-white #E8E0C8 and lavender core #C77DFF are new to this prop. |
| **reads_at_icon_size** | (1) a beige toggle plate with one screw, (2) the violet glow state when on, (3) the tube bar above it. |
| **must_not_look_like** | A modern smart-home rocker, a clean white new plate, or a light switch that only changes the room's normal light — the ON state must visibly flood the wall with purple. |
| **lettering** | None readable; the tape label is illegible marker scribble (icon renders without readable text). |

**State difference (off / on):** OFF — plate dark, toggle down, tube dark violet-grey, graffiti invisible under the normal fluorescent green. ON — toggle up, tube floods the back and left walls with UV Purple #9400D3 wash, and the highlighter graffiti (SMAAAASH quote, cheat codes, pixel art, haiku) lights up in its UV inks. The switch is the only thing that changes; the fluorescent marquee light stays on and flickering either way.

---

## 2. C4 sparking-wiring decal (right wall; sparks + zap bark when a bro walks close — Desk bcnr-q9)

| Field | Description |
|-------|-------------|
| **silhouette** | Three cable runs snaking across the right wall in loose S-curves and one diagonal drop, converging on a single junction box mid-wall; the whole decal spans roughly 5 tiles wide x 3 tiles tall (1.4 x 0.85 m). |
| **scale_cue** | Reads as a tangle of cables about as wide as the sock chute, with one bright junction at its heart; at wall scale the runs are 2-3 px thick lines with a chunky junction block. |
| **materials_and_cheap_cues** | Old cloth/rubber insulated cable, not conduit: two runs are stapled to the wall, one run hangs free with a sagging loop, and one repair is a wrap of grey duct tape plus a band of black electrical tape that has unpeeled at one end. The junction is a rusted metal-grey box with its cover hanging open on one screw. |
| **colours** | Insulation: faded red #B03030, cracked yellow #C8B040, and one black sheath #1C1C1C split open along its length. Bare copper at the split and at the junction terminals: #B87333. Staples: Metal Grey #808080. Duct tape: dull grey #909090. Electrical tape: black #1C1C1C. Sparks: Spark Yellow #FFFF00 with a white-hot #FFFFFF core. Junction box: Metal Grey #808080 with rust #7A4A2A streaks. |
| **contents** | none |
| **decoration** | None painted on; the decoration is the damage — the split sheath and the open junction cover. |
| **condition** | Insulation cracked and frayed at three points, copper dull and green-tinged at the junction; one run's staple has torn out, so that end dangles. Sparks emit from the open junction (and occasionally from the split sheath) every 2-5 s, and when a bro walks within ~1.2 tiles. |
| **garnish_and_addons** | The spark FX burst itself (Spark Yellow #FFFF00 star-burst with an arc lick between two terminals), plus the bro's zap bark overhead — visual only, no game. |
| **palette_anchors** | Spark Yellow #FFFF00, Metal Grey #808080, Shadow Black #1C1C1C, Grime Brown #3C2415 from the closet palette; insulation red/yellow, copper #B87333 and rust #7A4A2A are new to this decal. |
| **reads_at_icon_size** | (1) snaking multi-coloured cables on a grimy wall, (2) one chunky junction where they meet, (3) a yellow spark burst at that junction. |
| **must_not_look_like** | Neat cable trays or a tidy breaker panel — nothing here is fixed properly; must not read as safe, and must not look like a single straight wire. |
| **lettering** | none |

---

## 3. C9 joystick-with-lips graffiti (glows only while a bro is Embarrassed — code gate `closet_props.gd:146-149`)

| Field | Description |
|-------|-------------|
| **silhouette** | A pixel-art arcade joystick — round ball top on a thin stick, on a square base — with a pair of full lips overlaid across the ball; roughly square, about 1.2 x 1.2 tiles (34 x 34 cm) on the left wall beside the other graffiti. |
| **scale_cue** | About the size of the pixel-boobs tag next to it: a chunky 48x48-px-style pixel drawing, ~1 tile wide on the wall. |
| **materials_and_cheap_cues** | Highlighter/marker on bare grime-brown wall, drawn in the same flat pixel style as the approved pixel-graffiti decal (`REF/decals/aa_closet_decal_pixel_graffiti.png`): hard pixel edges, no shading, four colours max. Lipstick marks smeared over the ball, glossy against the matte marker. |
| **colours** | Hidden/faint state: dull smudged pink #B05080 at low opacity, barely above the grime — reads as lipstick smears only. Glowing state (Embarrassed): ball and base in LED Pink #FF69B4, lips in Magenta #FF00FF, outline in Shadow Black #1C1C1C, with a UV Purple #9400D3 emission halo around the whole drawing. |
| **contents** | none |
| **decoration** | The drawing itself: ball top with a highlight pixel, stick, four-screw base plate, lips with a darker mouth line. |
| **condition** | Faint state looks half-wiped, as if someone tried to scrub it. Glowing state is crisp — the marker ink fluoresces under the room light once the Embarrassed gate opens. |
| **garnish_and_addons** | The emission glow overlay in the glowing state only (UV Purple #9400D3 halo, pink core); no glow when hidden. |
| **palette_anchors** | LED Pink #FF69B4, Magenta #FF00FF, UV Purple #9400D3, Shadow Black #1C1C1C, Grime Brown #3C2415 — all from the closet palette's UV-reactive graffiti inks. |
| **reads_at_icon_size** | (1) a pixel joystick, (2) lips on it, (3) the pink/purple glow when Embarrassed. |
| **must_not_look_like** | A clean vector illustration or a photo — must stay flat pixel graffiti like its neighbours; in the hidden state it must NOT be invisible, just faint. |
| **lettering** | none |

**State difference:** hidden/faint — dull lipstick smears, no readable joystick, no emission. glowing (any bro Embarrassed) — full pixel joystick-with-lips in LED Pink #FF69B4 / Magenta #FF00FF with the UV Purple #9400D3 halo, emission mask on.

---

## 4. C8 Tekken haiku decal (confirm only — text is final, do not change a word)

Text (`game/core/closet_props.gd:60-63`, author-approved):

> She said "PERFECT" twice.
> when the combo was over
> she meant the combo

Read-out: "Highlighter ink. Underlined twice."

| Field | Description |
|-------|-------------|
| **silhouette** | Three lines of hand-scrawled text in a rough block about 3 tiles wide x 1.2 tiles tall (0.85 x 0.34 m) on the free left wall, with two underline strokes beneath the last line. |
| **scale_cue** | Reads as one pink highlighter scrawl about as wide as the CRT mirror; at wall scale each text line is ~0.35 tiles tall. |
| **materials_and_cheap_cues** | Highlighter ink on bare grime-brown wall — strokes are uneven in width, bleed slightly at the edges, and the second underline pass is offset from the first. Handwriting is hasty, tall-narrow marker letters, same hand as the other closet graffiti. |
| **colours** | **Confirmed: LED Pink #FF69B4** (Retro Pink from the closet palette — matches the Asset team's choice and the other pink graffiti). Underlines: same #FF69B4, second pass slightly offset and fainter. |
| **contents** | none |
| **decoration** | The double underline: two hand-drawn strokes under the whole haiku, the second one shorter, wobbly, and half the opacity — visibly "underlined twice", not once thick. |
| **condition** | Fresh-looking highlighter, slightly glossy; edges feathered where the wall is damp. |
| **garnish_and_addons** | none |
| **palette_anchors** | LED Pink #FF69B4 and Grime Brown #3C2415, both from the closet palette; no new hexes. |
| **reads_at_icon_size** | (1) three lines of pink scrawl, (2) the double underline, (3) highlighter-glossy uneven strokes. |
| **must_not_look_like** | A clean font print, a single underline, or a different ink colour — the pink must match the pixel-boobs decal beside it. |
| **lettering** | Exactly, three lines: `She said "PERFECT" twice.` / `when the combo was over` / `she meant the combo` — then two underline strokes. No other words. |

---

## 5. C11 Broken Prize Tag (item icon 256x256 + world prop hanging from the claw-arm chandelier; pickup from examining the claw arm — `cmr_broken_prize_tag`)

| Field | Description |
|-------|-------------|
| **silhouette** | A small rectangular cardboard tag, ~1:1.4 (width:height), with a punched hole at the top and a torn lower corner; world prop dangles from the claw arm by a short loop of string; icon is the tag face-on. |
| **scale_cue** | World prop: about 0.5 x 0.7 tiles (14 x 20 cm) hanging at claw height. Icon: the tag fills the 256x256 frame with 16 px safe area. |
| **materials_and_cheap_cues** | Thin printed cardboard, edges fuzzy and softened by damp; hole punched off-centre and reinforced with a worn metal eyelet; string is a grey twist-tie. Print is cheap dot-matrix/thermal style, slightly crooked on the card. |
| **colours** | Card: manila #D8C49A with Grime Brown #3C2415 stains and a damp dark patch at the torn corner. Eyelet: Metal Grey #808080. String: #909090. Print: Shadow Black #1C1C1C. Accent stripe across the top: LED Pink #FF69B4 (faded to #B05080 where stained). |
| **contents** | none |
| **decoration** | A pink stripe across the top edge, the eyelet, and the printed words (see lettering); a barcode-ish block of black bars at the bottom that is really just scribble. |
| **condition** | Torn lower corner with a fresh-looking rip, damp stain, crooked print, one corner creased where the claw clamped it. World prop swings gently with the chandelier's idle twitch. |
| **garnish_and_addons** | The twist-tie loop hooking it onto the claw arm (world prop only); icon has none. |
| **palette_anchors** | LED Pink #FF69B4, Grime Brown #3C2415, Metal Grey #808080, Shadow Black #1C1C1C from the closet palette; manila #D8C49A and stain tones are new to this item. |
| **reads_at_icon_size** | (1) a manila tag with a hole and torn corner, (2) dark printed words, (3) the pink stripe. |
| **must_not_look_like** | A shiny new prize ticket, a wristband, or anything laminated — it must read as the broken, discarded tag from a claw machine, not a collectible. |
| **lettering** | `[QUESTION FOR AUTHOR]` — the tag's printed words are not canon anywhere (items JSON says only "Records a claw-machine maintenance joke."). Two options: **A)** `PRIZE: 1x DIGNITY — CLAIMED` / **B)** `NOT A PRIZE — MAINTENANCE JOKE` (small print: `see management`). |

---

## Reviewer

Reviewer for this section: Kimi (character/dialogue + integration consistency). Notes requested on: palette-anchor citations, the [QUESTION FOR AUTHOR] options in prop 5, and whether the state descriptions match the code gates (`closet_props.gd:146-149`, bcnr-q8/q9).
