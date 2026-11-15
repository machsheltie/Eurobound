# Closet props physical descriptions

# Brief: Arcade claw-closet props, physical descriptions (rpac, for the Closet reference set)

## Rulings
- Author: "Our agents need to devise descriptions for all items/assets that are vague/lack one so the asset team can successfully generate them." The format is the 12-field "🖼️ Physical description (icon art brief)" (Desk rpac-q1, adopted). These are props and decals, so `scale_cue` means "how big it is on the wall" and `contents` is "none".
- Blacklight switch (Desk bcnr-q8), verbatim: "A blacklight switch on the closet wall; examine it to flip it on and off".
- Sparking wiring (Desk bcnr-q9), verbatim: "Sparks, and a bro gets zapped (a joke line) if you walk too close; no game". The zap lines are done; this is only the look.
- Audience: younger Gen X, xennial and millennial women. MA. No nudity: the pixel-art graffiti is already canon, so don't add more. "Europe" is banned.

## The room (read only these)
`design/worlds/debaucheryville/clawmachinemaintenanceclosetrestroom.md` lines 1-60 and 85-130 ("Chaotic retro grime meets early 2000s LAN party afterglow"). Palette: `design/worlds/debaucheryville/PNG_Assets/Claw_Machine_Maintenance_Closet_Complete_PNG_Asset_Requirements.md` lines 95-110 and 310-340 (fluorescent #00FF41, Spark Yellow #FFFF00, LED pink #FF69B4, UV purple #9400D3). Plan: `docs/superpowers/plans/2026-11-14-arcade-rework-plan.md` §1g, rows C4, C8, C9 and C11.

## Five props (one writer; drafts/mistral_closet.md, all five within the first 5 tool calls)
1. **Blacklight wall switch.** No doc describes the fixture. A cheap switch plate on the closet wall, and the state difference (off / on) so a player can see which. Also how the bulb or tube it controls looks, if it's visible.
2. **C4 sparking-wiring decal.** The docs only say it "snakes across walls". Give the wire runs (how many, how they're fixed or not), the insulation colours, the bare copper, the junction (the PNG doc names a "Wire Junction ... spark source"), tape and repairs. Sparks are Spark Yellow #FFFF00 (existing).
3. **C9 joystick-with-lips graffiti.** "Pixel-art arcade joystick with lips", which glows only while a bro is Embarrassed (code gate `closet_props.gd:88-91`). Docs only say "lipstick marks". Describe the hidden state (or faint) and the glowing state, plus the colours. Keep it in the pixel-graffiti style of the other closet graffiti.
4. **C8 Tekken haiku (confirm only).** The text is final (`game/core/closet_props.gd`):
   "She said "PERFECT" twice. / when the combo was over / she meant the combo". Read-out: "Highlighter ink. Underlined twice." The Asset team did it in #FF69B4. Confirm that colour or give one, and say how the double underline and the handwriting look. Don't change a word.
5. **C11 Broken Prize Tag** (`design/worlds/debaucheryville/items/claw_machine_maintenance_closet_restroom_items.json`, `cmr_broken_prize_tag`: a lore item; "Records a claw-machine maintenance joke."; got by examining the claw-arm chandelier). Item icon plus world prop. If the tag's printed words aren't canon, mark them `[QUESTION FOR AUTHOR]` with 2 options rather than deciding.
