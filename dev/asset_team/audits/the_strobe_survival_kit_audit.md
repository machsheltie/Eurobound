# Audit: The Strobe Survival Kit

**Files read (8-file set, city debaucheryville, all under design/worlds/debaucheryville/; file stem is strobe_survival_kit, no "the_"):**
- Main md: the_strobe_survival_kit.md (whole)
- core/strobe_survival_kit_core.json
- environment/strobe_survival_kit_environment.json
- interactions/strobe_survival_kit_interactions.json
- items/strobe_survival_kit_items.json
- location_nodes/strobe_survival_kit_location_nodes.json
- npcs/Strobe_Survival_Kit/strobe_survival_kit_npcs.json (only file in folder)
- PNG_Assets/Strobe_Survival_Kit_Complete_PNG_Asset_Requirements.md
- sprite_mapping/strobe_survival_kit_sprite_mapping.json
- events/: no folder exists in this city, nothing matches. MISSING files: none.
- Also: dev/asset_team/reviews/the_strobe_survival_kit_ext_review.jpg (only exterior review exists; no interior plate).

## Q1, how well does it represent the location? Score 3/5
Doc: "military surplus aesthetic meets rave culture", "Organized chaos", pegboards, "bins of glow sticks, earplug dispensers", decibel chart ("terrifying"), "last stop before the front lines". Painted: riveted olive crate wall, stencil sign, tagline, four category panels, orange warning and price plates; open night state has awnings, lit pegboard cells and a few glow sticks. Text accurate. The chaos and rave half is missing: no bins, no dispensers, no decibel chart or meter in view, and the closed day state reads as a shipping container.

## Q2, interior and exterior requirements? Score 2/5
Palette md/PNG: #4B5320, #FF6EC7, #1A1A1A, #FF4500. Olive and black right; orange only on hazard stripes and plates; pink only in tiny sticks, so the accent is absent (PNG sheet: "olive canvas, pink trim, the two cultures negotiating"). Missing nodes: ssk_decibel_display (live club readout), ssk_support_shelf (Chemical Support), Regret Prevention Corner, Antonín at ssk_operator, Price Flip Cards, Restock Crate. Interior: md says stall only; json lists interior nodes (see conflict 2). Over the top: no.

## Verdict: REDO exterior. Interior only if conflict 2 is ruled for it.

## Redo plan
**Hook:** Clubbing as a war zone, briefed by a former sound engineer who lost his own hearing.
**Palette:** #4B5320 tarps and crates; #FF6EC7 glow bins and LED strings; #1A1A1A alley; #FF4500 hazard, price warning, decibel red zone. Json alternative: olive, amber, LED cyan, stencil white.
**Exterior:** Node ssk_stall. Fold-out stall, pegboards, overflowing glow-stick bins, earplug dispensers, pink-trimmed olive awning, Decibel Warning Chart ("Velvet Curtain Club 105 dB, permanent damage threshold"; "Underground 110+, why") with a meter aimed at the club, price flip cards, Midnight Price Notice that pulses orange after 00:00, stencil sign, tagline, four category headers, warning plate.
**Interior:** Stall counter only unless ruled otherwise: Audio Defense, Visual Enhancement, Chemical Support, support shelf, Antonín Counter (ssk_operator) with chart-pointer prop, Restock Crate.
**NPC stations:** Antonín "Tonda" Pískal at ssk_operator (md: visible hearing aids, surplus vest; json: hearing protection and clipboard); up to 4 pre-club shoppers and 4 post-club casualties near shelf, display, counter.
**Satire beats made visible:** decibel chart as guilt trip; "yes, wear them inside" shades; Regret Prevention Corner (condoms, aspirin, snacks, water); desperation price flip, earplugs exempt.
**Conflicts, approval needed:**
1. Palette: md pink/orange vs json amber, LED cyan, stencil white.
2. Md says street stall only; json gives nodes (ssk_audio_defense to ssk_exit) as a walk-through "interior". Is there an interior plate?
3. Subtitle: md "Earplugs, Glow Sticks, and the Will to Continue." vs json "Equip Yourself. The Night Is Hostile." (md sign tagline).
4. Json has no Tactical Accessories or Regret Prevention node; md has five sections.
5. Items: json 5 items (Musician Earplugs 15, Shades 20, Glow Bundle 5); md about 25 with Musician 20, Shades 15, Bundle 8.
6. Hearing aids (md) vs hearing protection (json) for Antonín's look.
**Not in the file, needs approval:** sandbag or barricade staging (old plan had it; only "front lines" phrasing supports it); whether the midnight price board shows a number (md says +50%).
