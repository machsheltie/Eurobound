# Item physical descriptions batch 2 Asset team blocked icons

# Brief: item physical descriptions, batch 2 (the Asset team's blocked icons)

## The rulings (author, 2026-11-14, verbatim)
- "The writing room should be giving all items physical descriptions that go into detail complete with colors"
- "Our agents need to devise descriptions for all items/assets that are vague/lack one so the asset team can successfully generate them. They should be in the items Md files"

Bead Eurobound-rpac. Tracker: `design/items/docs/physical_descriptions_tracker.md`. Batch 1 (Kokos Loco Bucket) is on the Desk as rpac-q1 and sets the format. This batch uses that **proposed** format; if the author changes the format, we reformat, not rewrite.

## Audience (author, 2026-11-14)
"I have told it several times the game is for younger Gen X/xennial/millenial women". Every object is a joke on the bros or the tourist trap, and has to land for her at a glance: cheap, used, dubious, specific. Never cute, never appetising, never premium.

## What a description is, and is not
- **Looks only:** shape and silhouette, size (and how size reads with nothing else in the frame), materials and how you can tell they are cheap, every colour as a plain word plus a hex code, markings, **every word of lettering spelled out exactly** (or "none"), wear and damage.
- **Never** change what an item is, its name, numbers, effects, price, or story. If a look choice would change what it is, write it as a `[QUESTION FOR AUTHOR]` instead of deciding it.
- Real brands keep their real names. No real place names. MA is fine; no nudity.
- Plain paintable words only. If a painter can't paint the word ("vibe", "evocative", "tropical feel"), cut it.

## Format per item (the 12 fields proposed in rpac-q1)
`## Physical description (icon art brief)`, then: silhouette, scale_cue, materials_and_cheap_cues, colours (word + hex), contents (if it holds anything), decoration, condition, garnish_and_addons (say "none" when there are none), palette_anchors (hexes taken from the owning location's palette, with the file and line, versus new ones), reads_at_icon_size (3 checks at 128 px), must_not_look_like, lettering (spell out every word, or "none").
About 90 to 160 words for the description fields, plus the lists.

## Items and slices (one writer per item; each writes drafts/<name>_batch2.md)

**Mistral: the Cirque du Shady items** (`design/worlds/debaucheryville/items/cirque_du_shady_items.json`)
1. `item_shady_loot_crate_voucher` (about line 85). No look and no printed text. Write both; spell out the printed text.
2. `item_used_glitter_hat` (about line 31; also `design/worlds/debaucheryville/the_participation_trophy.md:169`). **The author has ruled its look (Desk asset-team-desc-used_glitter_hat), verbatim:** "A glitter party crown (the bros' 'basically a crown')", note: "It should look like the 80s my little pony princess pony crowns lmao. With glitter. And streamers." So: a cheap plastic 80s-toy-style princess party crown, glitter, streamers. **No My Little Pony branding, logo or characters.** Make it used and grubby, matching its own line "Glitter hides the stains. Mostly." Give exact colours.
3. `item_beatdown_casting_flyer` (about line 110). The text is already exact; keep it word for word. Describe the paper, print, colours, layout and wear.

**Deepseek: Absinthe Arcade and taproom items**
4. `item_broken_symbol_game_boy` / `aa_broken_symbol_handheld` (`design/worlds/debaucheryville/items/absinthe_arcade_items.json`; `game/assets/data/items/key_items.json` about line 310). Three refs failed: the sticker look, WHICH symbol, the body tone and the battery bay are all thin. Settle each from canon; if canon names no symbol, propose one as a `[QUESTION FOR AUTHOR]` with 2 options.
5. `velvet_wristband_vip` (`Assets/Graphics/items/velvet-wristband-vip.md`). The wear, foil and sheen are vague.
6. `already_spent_credit` (`game/assets/data/items/consumables.json` about line 85). CONFIRM OR CORRECT: the icon is finished, and agents picked the token's material and colour.
7. `cracked_mirror_shard` (a Mirror Chad drop: `design/worlds/debaucheryville/the_absinthium_taproom.md:403`; `game/assets/data/enemies/debaucheryville_arcade_battle.json` about line 1064). CONFIRM OR CORRECT: only the name is canon; agents picked the shape and cracks.

**Aion: finished icons to confirm or correct**
8. `item_tan_line_neon_shooter` (`design/worlds/debaucheryville/items/bohemian_riviera_items.json`; venue at `bohemian_riviera.md:91`). Agents picked the colour from "tanning-bed neon" only.
9. `hamagotchi_consolation` (`design/items/hamagotchi_consolation_item.md`). Agents picked the shell colour.
10. `green_fairy_essence` (a boss consumable: `design/worlds/debaucheryville/the_absinthium_taproom.md:404`; `game/assets/data/enemies/debaucheryville_arcade_battle.json` about line 1075). Only the name is canon; agents picked the flask.
11. `mango_og_gushers` (`design/items/general_items/mango_og_gushers_item.md`). The box layout is marked PROPOSED.

**For the CONFIRM OR CORRECT items (6-11):** read the icon prompt the Asset team used, `dev/asset_team/icon_refs/<id>_prompt.md`. Keep every pick that fits canon and the joke, and write it into the description. Mark each detail you change as `CHANGED (was: ...)`, with one line of why. Don't change a finished icon for taste alone. Change only what is wrong for canon, the joke or the audience.

## Rules for writers
- Write your file within your first 6 tool calls. Read only the files named for your items, plus the matching `_prompt.md` files.
- No bro lines in this task.
