# Battle HUD icon pictures

# Brief: battle-screen icon pictures (status icons + action-type icons)

## The ruling (author, Desk asset-team-plan-battle_hud-q2, verbatim)
"The Writers' Room proposes a picture for each; I approve the list."

## The approved look (`dev/asset_team/plans/battle_hud_icons_plan.md`)
- **One simple 3D object per icon**: the status's joke made physical, on a **round badge**.
- **Border colour** (GDD 309): **green or blue for buffs, red or orange for debuffs**. Neutral statuses: say which and why.
- Drawn at **28 x 28 px** in battle. The object must read as a silhouette at that size: one object, chunky, no scene, **no lettering** (no words can be read at 28 px).
- Canon already fixes two: **Grease Fingers = an oil drip; Embarrassed = a blush that pulses** (GDD 308; Hungover = a sloshing beer mug). Confirm those two and give their colours; don't replace them.
- Animation is a later pass. Name the one motion each icon would loop (one short phrase), but the still picture is the deliverable.

## Audience and rules
Younger Gen X, xennial and millennial women. Each icon is a tiny joke on the bros: cheap, gross, 1997–2005 era objects. Real brands keep their real names, but no logos are readable at 28 px, so use shapes. No real place names; "Europe" is banned. No nudity.

## Where the meanings are
`game/assets/data/skills/status_effects.json` ("status_effects"), `design/mechanics/Battle/status_effects.md`, `game/battle/battle_core.gd` (line 17 and the villain moves; its NEGATIVE list is embarrassed, sloppy, confused, stun, grease_fingers, tourist_trap_victim, food_poisoning, broke_af), and `design/items/general_items/strawberry_shortcake_speedcakes_item.md` for the sugar_rush_hour, gush_locked and crash family. Grep each id; read only the lines you need.

## Format per icon (one table row)
| id | display name | buff/debuff/neutral, border colour | the object (one sentence, shape first) | colours (word + hex) | the loop motion | why it's funny (half a line) |

## Slices (each writer writes drafts/<name>_hud.md within the first 6 tool calls)
- **Kimi:** sugar_rush_hour, gush_locked, crash, cottonmouth, the_shakes, wobbly_windmill_navigation (display name "Windmill Grist"), contact_high, space_cake_timer
- **Deepseek:** space_cake_gamble, canal_confusion, tunnel_confusion, tunnel_vision, sloppy, confused, stun, tourist_trap_victim
- **Mistral:** food_poisoning, broke_af, hardcore_gamer, gains_bro, grease_fingers (confirm: oil drip), embarrassed (confirm: pulsing blush), plus the **four action-type icons**: attack, item, skill, debuff (these overlay the turn-order portraits, GDD 303)
