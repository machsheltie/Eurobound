# Signature Beer: Windmill Grist

- **Item ID**: `beer_wobbly_windmill_brewery`
- **Brewed By**: The Wobbly Windmill Brewery (engine id: ⚠ AUTHOR-REVIEW (engine sync): — not minted; world-doc Location ID is `shamsterdam_countryside_wobbly_windmill_brewery_01`), Shamsterdam
- **Unlocked**: challenge completion at this brewery (defeat the Yeast Golem); not sold, and the opener gates only the stamp [author round v34, Set A; author on bead Eurobound-8gg, 2026-11-12; source: design/worlds/shamsterdam/wobbly_windmill_brewery.md L39-43, L191-195]

## Stat Block
| Field | Value |
|---|---|
| **Style** | Amber ale, brewed from grain the windmill grinds upstairs. Not a witbier: the Mad Monarch owns wheat beer (author round v24) [source: design/worlds/shamsterdam/wobbly_windmill_brewery.md L242-243; docs/superpowers/NEXT_WORK.md L510-513] |
| **ABV** | 11%, the tasting-flight finale [author round v34, e3_grist Set A; source: wobbly_windmill_brewery.md L211] |
| **Effects** | +40 HP, +20 Bravado, +15% Speed for 3 turns [author round v34, Set A; source: wobbly_windmill_brewery.md L245-249] |
| **Risk** | Navigation penalty: -20% Navigation for 5 turns [author round v34, Set A; source: wobbly_windmill_brewery.md L250]. Intoxication-law 10-point review below; ⚠ AUTHOR-REVIEW: its pending points need rulings before engine sync. |
| **Price** | Not sold [author round v34, Set A] |
| **Special** | The room keeps spinning even after you leave. [source: design/worlds/shamsterdam/wobbly_windmill_brewery.md L251] |

## Flavor Text
> "The brewmaster calls it 'liquid heritage.' You call it 'why is the floor moving.'" [source: design/worlds/shamsterdam/wobbly_windmill_brewery.md L253]

## PNG Assets
- `beer_wobbly_windmill_brewery_bottle.png` — 48x64, amber ale with windmill stirrer [size: author round v34, asset spec `design/worlds/shamsterdam/PNG_Assets/wobbly_windmill_brewery_png_assets.md` L282; renamed from the source's beer-name stem `windmill_grist_bottle.png` to the full brewery-stem convention]
- `beer_wobbly_windmill_brewery_icon.png` — 32x32, menu icon with spin indicator [source: design/legacy/brewery_passport_book_complete.md L497; renamed from `windmill_grist_icon.png`]

## Intoxication Law Review (design/mechanics/intoxication_law.md §8)
Status: drafted 2026-11-12 (Eurobound-r1c). The review proposes; the author rules. Items marked ⚠ PENDING have no number or decision in the docs and are not filled in here.

1. **Source**: Windmill Grist, 11%, the finale of the tasting flight at The Wobbly Windmill Brewery; x3 from the Yeast Golem, +2 from the Couchsurf host [source: design/worlds/shamsterdam/wobbly_windmill_brewery.md L192, L211, L359]. Alcoholic: yes (round v37 drink_tag; engine flag `"alcohol": true`, 10 clock minutes when bought or drunk). Not sold; the opener gates only the stamp (author round v34, Set A; confirmed on bead Eurobound-8gg, 2026-11-12, and the purchase lines swept).
2. **Immediate effect**: +40 HP, +20 Bravado, +15% Speed for 3 turns; -20% Navigation for 5 turns (round v34, Set A).
3. **Escalation**: In the brewery, each flight beer fills the Spin Meter and the visuals ramp to full spin at Windmill Grist; a maxed flight plus Spin Meter can make a bro throw up (Bravado loss) [source: wobbly_windmill_brewery.md L214-217, L257; design/worlds/shamsterdam/PNG_Assets/wobbly_windmill_brewery_png_assets.md L369-376]. ⚠ PENDING: whether a second Grist stacks the Navigation penalty or its duration, and whether it counts toward Buzzed → Beer Goggles → Shitfaced → Catastrophe (no approved thresholds, intoxication_law.md Appendix A).
4. **Player-facing cues**: Inside the brewery, the Spin Meter's vignette and rotation (vignette-only on Low LOD, off in reduced-motion mode) [wobbly_windmill_brewery_png_assets.md L372, L376]. "The room keeps spinning even after you leave" [wobbly_windmill_brewery.md L251]. ⚠ PENDING: no cue is specified for the Navigation debuff once the party is outside (Tunnel Confusion uses question marks over the head, voetgangerstunnel.md L427).
5. **Player control**: Navigation is Shamsterdam's overworld direction check: the player picks a direction and a probability roll decides where the party actually ends up [source: design/worlds/shamsterdam/voetgangerstunnel.md L120-136]. -20% means more wrong turns: bounded, readable loss of movement control, with the Speed buff getting the party there faster.
6. **Duration and recovery**: Speed buff 3 turns, Navigation penalty 5 turns, so the benefit runs out first. ⚠ PENDING: "turns" is a battle unit and Navigation is an overworld stat (other Navigation effects run on clock time, e.g. Tunnel Confusion, 2 hours or until a successful navigation, voetgangerstunnel.md L424-426); what 5 turns means outside battle, and any cure besides waiting, are not given.
7. **Comedic consequence**: The bro thinks he has drunk fifteen years of Hendrik's life and earned the speed; he gets lost faster. Hendrik: "this is 15 years of my LIFE in a glass. I hope you are worthy." [wobbly_windmill_brewery.md L272]; flavor: "You call it 'why is the floor moving.'" [L253]
8. **Status interactions**: Navigation odds already move with Sober (+20%), Contact High (-15%), Space Cake Gamble (-30%), Canal Confusion (-25%) and a map item (+15%) [voetgangerstunnel.md L131-135]; Tunnel Confusion is -15% Navigation across Shamsterdam [L424-426]. Listing (The Hoisted Pint) also drifts overworld walking [the_hoisted_pint.md L242-243]. Canal Courage cuts Bravado loss while intoxicated [npc_brewmaster_hendrik.md L322]. ⚠ PENDING: whether Grist's -20% stacks additively with those, and whether drinking it cancels the Sober bonus.
9. **Technical dependencies**: Proposed engineering work: Navigation exists only in design data (`design/worlds/shamsterdam/items/voetgangerstunnel_items.json`), and the engine's status list is empty (`game/assets/data/skills/status_effects.json`). It needs a Navigation stat feeding the overworld direction roll, a status timer that works outside battle, a turn-limited Speed buff, the Spin Meter shader with Low-LOD and reduced-motion fallbacks, and `"alcohol": true` on the consumable entry.
10. **Further author approval**: Numbers ruled (round v34, Set A). Still needed: the PENDING points in 3, 4, 6 and 8, and sign-off on this review before engine sync.

## Notes
- Brewed by — The Wobbly Windmill Brewery, windmill-ground grain [source: design/legacy/brewery_passport_book_complete.md L198].
- Brewmaster Hendrik on the final beer: "The final beer, the Windmill Grist... this is 15 years of my LIFE in a glass. I hope you are worthy." [source: wobbly_windmill_brewery.md L272].
- The Yeast Golem is made of dust from this very mill [source: wobbly_windmill_brewery.md L144].
- Passport row: slot 1, signature beer Windmill Grist [source: design/items/brewery_passport_book_item.md L196].
- Alternate in the legacy passport doc, not used: "Brewed with grain ground by the very windmill that's making you dizzy. The circular notes are intentional." [source: design/legacy/brewery_passport_book_complete.md L197]
- Author, round v34 (2026-11-11), on the name: "the name needs work. This is too high brow and official.... Remember, this is *satire* and *parody*. It isn't supposed to read as serious". ⚠ AUTHOR-REVIEW: rename pending (Writers' Room punch-up).
