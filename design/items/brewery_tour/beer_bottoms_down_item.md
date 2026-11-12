# Signature Beer: Oude Genever

- **Item ID**: `beer_bottoms_down`
- **Brewed By**: Bottoms Down (engine id: ⚠ AUTHOR-REVIEW (engine sync): — not minted; world-doc Location ID is `shamsterdam_oldtown_bottoms_down_01`), Shamsterdam
- **Unlocked**: challenge completion at this brewery (the Jenever Taste Test gauntlet; x5 on success, x2 on failure); purchasable there afterward [source: design/worlds/shamsterdam/bottoms_down.md L175-187, L29-31]

## Stat Block
| Field | Value |
|---|---|
| **Style** | Aged Dutch jenever, zeer oud classification; the beer-style vocabulary exemption applies to the tour's signature drink [source: design/legacy/brewery_passport_book_complete.md L201] |
| **ABV** | 35%, the menu's Oude Jenever [author round v34, e3_genever "same_menu": one item, menu numbers; source: bottoms_down.md L217-219] |
| **Effects** | +25 Bravado [author round v34, menu numbers; source: bottoms_down.md L217-219] |
| **Risk** | "The Shakes": -15% Accuracy for 3 turns [author ruling 2026-11-12, Eurobound-r1c: "-15% accuracy for 3 turns"; matches bottoms_down.md L233, L240. The legacy passport's -20% (design/legacy/brewery_passport_book_complete.md L204) is superseded]. Sprite vibrates, reticle unstable; cure: time, food or sleep; stacks in duration [source: bottoms_down.md L238-244]. Intoxication-law 10-point review below; ⚠ AUTHOR-REVIEW: its pending points need rulings before engine sync. |
| **Price** | 6 SOVS [author round v34, menu numbers; source: bottoms_down.md L217-219] |
| **Special** | Cannot be consumed during combat (hands shaking). The glass is filled to surface tension and must be sipped from the bar, bowing; lifting it spills. [source: design/worlds/shamsterdam/bottoms_down.md L234, L77-80, L196-201] |

## Flavor Text
> "Four hundred years of tradition in one glass. Your ancestors are watching. They're disappointed but not surprised." [source: design/worlds/shamsterdam/bottoms_down.md L236]

## PNG Assets
- `beer_bottoms_down_bottle.png` — 32x48, traditional tulip, overfilled [size: author round v34, asset spec `design/worlds/shamsterdam/PNG_Assets/bottoms_down_png_assets.md` L190; renamed from the source's `oude_genever_glass.png` to the full brewery-stem convention]
- `beer_bottoms_down_icon.png` — 32x32, menu icon with surface tension [source: design/legacy/brewery_passport_book_complete.md L499; renamed from `oude_genever_icon.png`]

## Intoxication Law Review (design/mechanics/intoxication_law.md §8)
Status: drafted 2026-11-12 (Eurobound-r1c). The review proposes; the author rules. Items marked ⚠ PENDING have no number or decision in the docs and are not filled in here.

1. **Source**: Oude Genever, 35%, served by Kees at Bottoms Down; one item with the menu's Oude Jenever (round v34, "same_menu"). The Shakes is also inflicted by Zeer Oude Jenever (x2), Korenwijn, gauntlet failure and the Couchsurf morning [source: design/worlds/shamsterdam/bottoms_down.md L218-220, L185, L239, L367]; those sources are outside this review. Alcoholic: yes (round v37 drink_tag; engine flag `"alcohol": true`, 10 clock minutes when bought or drunk).
2. **Immediate effect**: +25 Bravado (round v34, menu numbers); The Shakes, -15% Accuracy for 3 turns (author ruling 2026-11-12).
3. **Escalation**: Further jenever servings stack the duration, not the magnitude [source: bottoms_down.md L241]; Zeer Oude Jenever applies The Shakes x2 [L219]; gauntlet failures accumulate Shakes stacks [source: design/worlds/shamsterdam/PNG_Assets/bottoms_down_png_assets.md L482]. ⚠ PENDING: turns added per extra serving, any duration cap, and whether it counts toward Buzzed → Beer Goggles → Shitfaced → Catastrophe (the tiers have no approved thresholds, intoxication_law.md Appendix A).
4. **Player-facing cues**: Sprite vibration by a 2px offset-frame swap (no screen shake), an unstable combat reticle, a status bar with stack indicator and an explicit "-15% Accuracy" text readout, the trembling-hand icon, and a tremolo audio bed [source: bottoms_down_png_assets.md L272-278, L351-353, L381, L404-405, L424; bottoms_down.md L242, L386]. Bros' line: "I'm fine. Everything's fine. Why is my hand doing that." [bottoms_down.md L244]
5. **Player control**: Attacks miss more often for 3 turns. Oude Genever cannot be drunk in combat; authored, not a bug [source: bottoms_down.md L234; design/worlds/shamsterdam/npcs/bottoms_down/npc_kees.md L466]. No dialogue or movement takeover is specified.
6. **Duration and recovery**: 3 turns; cured by time, food or sleep [bottoms_down.md L240, L243]. Frietomat and the Stroopwafel Cart reduce the duration and De Zilte Waarheid gives "mild improvement" [source: design/worlds/shamsterdam/frietomat.md L271; stroopwafel_cart.md L254; de_zilte_waarheid.md L298]. Reduced-motion mode swaps the tremor for the bar and the text readout [bottoms_down_png_assets.md L533]. ⚠ PENDING: how much each food cuts, and how a turn-counted status runs on the overworld (the Couchsurf morning applies it outside battle, bottoms_down.md L367).
7. **Comedic consequence**: The bro thinks he is proving his constitution and earning the bartender's respect; he gets +25 Bravado and hands that will not hold a weapon still. Kees: "Your hands will shake. This is the drink. Not you." [npc_kees.md L191]
8. **Status interactions**: Stacks with Listing (The Hoisted Pint) [source: design/worlds/shamsterdam/the_hoisted_pint.md L246]; Postponed Hangover does not block it [the_mad_monarchs_wit_tea_party.md L239]; Canal Courage cuts Bravado loss while intoxicated [npc_kees.md L356]. ⚠ PENDING: whether it stacks with Beer Goggles, the other combat accuracy penalty (−Accuracy, design/characters/LordPilsner/lordpilsner.md L33; Tier 2 keeps it, intoxication_law.md Appendix A).
9. **Technical dependencies**: Proposed engineering work: the engine's status list is empty (`game/assets/data/skills/status_effects.json`), so it needs a status with duration stacking, an accuracy modifier in the battle hit roll, a combat-use lock on the item, the offset-frame sprite swap and reticle wobble, and the reduced-motion presentation. The consumable entry needs `"alcohol": true`.
10. **Further author approval**: Magnitude ruled (2026-11-12). Still needed: the PENDING points in 3, 6 and 8, and sign-off on this review before engine sync.

## Notes
- Brewed by — Bottoms Down, 400-year-old recipe [source: design/legacy/brewery_passport_book_complete.md L208]. Bartender Kees serves it.
- Passport row: slot 2, signature beer Oude Genever [source: design/items/brewery_passport_book_item.md L197].
- One item (author round v34, e3_genever "same_menu"): the signature "Oude Genever" and the menu's "Oude Jenever" are the same drink, priced and statted from the menu. The menu's separate "Zeer Oude Jenever" (12 SOVS, +40 Bravado) is untouched.
- Alternate in the legacy passport doc, not used: "Aged for years. Served for centuries. The sawdust exists for a reason." [source: design/legacy/brewery_passport_book_complete.md L207]
- Author, round v34 (2026-11-11), on the name: "the name needs work. This is too high brow and official.... Remember, this is *satire* and *parody*. It isn't supposed to read as serious". ⚠ AUTHOR-REVIEW: rename pending (Writers' Room punch-up).
