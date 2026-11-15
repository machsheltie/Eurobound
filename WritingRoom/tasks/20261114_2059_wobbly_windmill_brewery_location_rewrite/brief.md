# Wobbly Windmill Brewery location rewrite loud seedy

# Brief: The Wobbly Windmill Brewery, full rewrite of the location files (loud, seedy, specific)

## Rulings (verbatim)
- vuqj-q1: "Writers' Room rewrites the visual sections of every renamed real-venue doc before its building is painted"
- orch-location-rewrite-throughput: "Full rewrites, one building at a time (slow, most thorough)"
- vuqj-q4 (the machinery sign): "English plus pictograms (a hand with a red cross, a gear, a skull): every language, no words"
- vuqj-q3: "Palette sets the colours, but never candle-warm or golden-hour light; lighting is set per plan"
- Interactables rule (`design/style_guides/location_interactables_rule.md`, binding 2026-11-14): four layers (background shell / placed props / interactive objects / pickups). Anything game logic could refer to is declared in the location file. Any NEW behaviour is a [QUESTION FOR AUTHOR].
- The approved model for this job is Bottoms Down: read `design/worlds/shamsterdam/bottoms_down.md` Visual Design and "Interactables & Props (four-layer rule)" for the bar we're matching.

## Audience (author, 2026-11-14)
"I have told it several times the game is for younger Gen X/xennial/millenial women". Every sign, prop and patron has to land for her. The bros are the punchline, laughed AT.

## Why (bead Eurobound-xnpg)
The Wobbly Windmill Brewery was a real, respectable brewery, renamed. Its visual sections still describe the respectable place: "warm candlelight" in the tasting room (`wobbly_windmill_brewery.md:89`), the stale "Sensitivity... not Dutch heritage" line (:122), and a five-language DO NOT TOUCH MACHINERY sign (:83). The image tools paint that as a cosy heritage windmill. The fix is the writing: an over-the-top, seedy, specific tourist-trap brewery inside a windmill that a painter can't make charming.

## Files in scope (read; draft replacements in drafts/; never edit them)
- `design/worlds/shamsterdam/wobbly_windmill_brewery.md` (485 lines): the location.
- `design/worlds/shamsterdam/npcs/wobbly_windmill_brewery/npc_brewmaster_hendrik.md` (454 lines): the brewmaster.
- `design/worlds/shamsterdam/PNG_Assets/wobbly_windmill_brewery_png_assets.md` (614 lines): the art spec.

## Ruled facts: keep exactly
- The name **The Wobbly Windmill Brewery**; the brewery-tour role (Shamsterdam brewery, any order); the opener and stamp; the two-stamp gate with Kees at Bottoms Down; **Windmill Grist** (never sold); the **Yeast Golem** boss; the tasting flight and Spin Meter; the Brewmaster's Speech; the Selfie Spot challenge; "Canal Courage" passive progress.
- **Names:** Brewmaster **Hendrik** and the apprentice **Bram** keep their names (ucpf q42: "Keep the locals' Dutch first names; only titles, nicknames and places change"). **Hendrik the seagull** at The Salty Swallow is author-kept (q73: "Keep it: the seagull beat depends on the name"). **Polder Pilsner is now Landfill Lager** (ucpf rename): use the new name.
- Every number, price, hour, id, slug, filename, sprite id and flag stays.

## What to change
Everything descriptive: exterior, signage, each floor's interior, the blade level, satirical design, patrons, the bros' reactions, audio, and the PNG doc's palette, scene layouts and props to match. Make it:
- **Loud.** The windmill is a tourist trap that brags. Screaming signage in English (pictograms where a sign needs every language), merch everywhere, hazard tape, a turnstile, a queue rope.
- **Seedy and specific.** Spills with a history, a gift shop selling the same thing three ways, the selfie spot's grime, broken machinery held with zip ties, at least 5 modern seedy props per scene.
- **Old, never charming.** Age reads as grime, damage and stubbornness. Banned painter-bait words: "charming", "cozy", "quaint", "storybook", "fairy-tale", "rustic", "heritage", "faded", "barely visible", "warm candlelight", "golden hour", "half-timbered", "ancient".
- **Fill the required line** in Visual Design: **"What this building exaggerates (readable at thumbnail size)"**, one sentence a QC reviewer can check against a 231 px thumbnail.
- **Cut** the "played straight" and Sensitivity lines.
- **No Dutch words or real nationality** in player-facing text. **"Europe" is banned** (Euromemeia). Internal notes may name the real inspiration.

## Hard limits
- No new mechanics, numbers, prices, quests, rewards or items. A new NPC name counts as new content: propose 2-3 names marked [PROPOSED].
- Bros: sincere doofuses (writer_role.md; bible 00 and 01 §3a). Never witty, scared, disgusted, self-aware or scam-aware. Run the stand-up test on every bro line.
- MA. No nudity. Money is SOVS.

## Slices (one writer at a time; small reads; write within your first 6 tool calls)
- **A: Kimi.** `wobbly_windmill_brewery.md` lines 1-147 (identity, Visual Design, Satirical Design), 259-336 (NPCs, patrons, bro reactions) and 361-379 (Audio), plus a new "Interactables & Props (four-layer rule)" section. Draft: `drafts/kimi_windmill_location.md`.
- **B: Deepseek.** `npc_brewmaster_hendrik.md`: appearance, personality, connections, recurring appearances, to match Kimi's draft. Dialogue stays verbatim except for rule breaks (list each). Draft: `drafts/deepseek_hendrik.md`.
- **C: Mistral.** `wobbly_windmill_brewery_png_assets.md`: overview, palette (hues only), and the scene/exterior/signage/patron sheets, matched to Kimi's draft. Technical sections stay, except candle and golden-hour wording. Draft: `drafts/mistral_windmill_png.md`.
- **D: Aion.** Exterior signs: the main sign, the machinery sign (English + pictograms per vuqj-q4), and a gift-shop or queue sign. 3 options each, with a pick. Read only Kimi's draft. Draft: `drafts/aion_windmill_signs.md`.
- **Final: Kimi** integrates in three passes. The author approves on the Desk before anything goes into `design/`.
