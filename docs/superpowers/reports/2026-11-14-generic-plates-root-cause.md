# Why the plates come out cosy (2026-11-14)

## Causes, ranked

**1. The writing describes real, respectable venues.**
- The Windmill was "Brouwerij de Molen", a real brewery. Bottoms Down was "'t Kansen", renamed "name only" (NEXT_WORK.md:113-116). The visual sections still describe the real places.
- Bottoms Down: "no obvious signage", lettering "barely visible" (bottoms_down.md:48-51), "hasn't changed because it doesn't need to" (:110).
- Its PNG spec: "warm, close, unhurried" (:639), the tradition "played entirely straight" (:752).
- Windmill tasting room: "warm candlelight" (:89).
- All three still carry "Sensitivity… not Dutch heritage" (bottoms:117, windmill:122, hostel:112), a field the author removed on 2026-08-03 (template:195).
- The jokes sit in unpaintable parentheses ("lawyers insisted").
- **Authorship:** commit 15d8051f logs the PNG specs as agent work, "captured here unreviewed". Git can't name the main docs' writer, but they copy the retired template word for word.

**2. The palettes are cosy and binding.** Amber, oak and Candlelit Cream (bottoms_down.md:102). The brief says "the palette is binding" (TEAM_BRIEF:31), so a candlelit tavern is what the rules ask for.

**3. Boilerplate and lighting rules push towards a postcard.**
- The brief asks for "warm practical light" (TEAM_BRIEF:20) and a blue daytime sky (PAINT_JOB:18).
- The first Bottoms Down prompt asked for "warm golden late-afternoon light… bare and austere".
- The one passing fix (Tolerance v2) used a ban list, "flat overcast grey daylight" and about 15 seedy props.
- Prompts aren't logged; this came from transcripts.

**4. The references carry the look forward.**
- The first Bottoms Down painter uploaded `pancake_ext_day.jpg` and the old `hostel_ext_day.jpg` with "Match… exactly in… palette".
- The contact sheet's Shamsterdam row is all golden-hour postcards.
- Fix rounds edit the failed plate ("keep this exact layout").

**5. The model beautifies certain words.** One prompt said "grimy… not a cute cottage", and QC still saw a "mossy sagging storybook cottage" (qc_log:7). Trigger words: "1624", "ancient", "tavern", "candlelight", "sagging", and agent-added "half-timbered". Old plus crooked reads as a fairy tale. Modern trash props break it.

**6. Seediness is only checked after painting.** The QC log has no A1 (plan) entries. The first L3 checks on the Windmill and Bottoms Down came after merging (qc_log:3,5).

**7. Rule conflicts force blank signs.**
- The five-language sign (windmill:83) runs into the no-Dutch rule and L4's exact-text rule. The result was "deliberately illegible" plates, which QC failed as "blurred slabs" (qc_log:12).
- Quiet doc signage plus "no invented text" takes away loud signage.

## Fixes

- **Docs [AUTHOR]:** rewrite Visual Design for the renamed real-venue docs so the building shows the gag in paintable objects. Cut the "played straight" and stale Sensitivity lines.
- **Template [AUTHOR]:** add a required field: "What the building exaggerates, readable at thumbnail".
- **Palette [AUTHOR]:** allow a grime or vice accent, or rule that the palette sets hue but never candle-warm light.
- **Plan template:** turn each parenthetical joke into a prop. Require 5 or more modern, seedy props. State the light. Ban beautifier words unless the doc names them.
- **Prompts:** seedy props first, style boilerplate last. Add a standing ban list (golden hour, sunbeams, flower boxes, trees, candle-window glow). Allow overcast days (PAINT_JOB:18). Log every prompt.
- **Style refs:** Arcade plates only, for brushwork, never palette. No Shamsterdam plates as references.
- **QC order:** run a blind A1 with an L3 seediness check before painting, then L3 on the first day thumbnail before other work. An L3 fail means a fresh generation, never an edit.
- **Conflicts [AUTHOR]:** for the five-language sign, choose English only, English plus pictograms, or four real non-Dutch languages. Decide whether plans may propose louder signage.
