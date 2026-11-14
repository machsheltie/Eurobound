# JRPG item categories, and what Eurobound has in each

**Bead:** Eurobound-q1u7 · **Date:** 2026-11-14 · **For:** the author

## The short version

JRPG items fall into about 35 jobs. Eurobound already has a lot of items, but they are bunched into a few of those jobs.

- **Heavily covered:** food and drink that restore HP, drinks and drugs that give a buff with a catch, quest and door-pass items, collectible sets, and junk that pays off when inspected.
- **Thin:** reviving a downed bro, curing a status, items thrown at enemies, getting out of a fight, restoring Bravado without alcohol, and junk that exists to be sold.
- **Empty:** all wearable gear in the actual game (the gear file is blank and the game has no gear slots yet), one-time permanent stat boosters, crafting materials, and anything that controls how often fights happen.

Part 3 lists the gaps in order. This report names no new items, names or numbers. Those are yours.

## How to read this

- **Part 1** is the map of what items do in JRPGs generally.
- **Part 2** puts Eurobound on that map.
- **Part 3** says which squares are thin or empty.

Three words are used for Eurobound's status in Part 2:

| Word | Meaning |
|---|---|
| **Built** | The item is in the game's data files (`game/assets/data/items/`), so the game can load it. |
| **Written** | It exists in a design doc or a location's item list, but not in the game's data. |
| **Nothing found** | I searched and found neither. |

**One note on our stats.** The game tracks two bars per bro: HP (health; at zero the bro is down) and Bravado (the fuel for signature moves, the role "magic points" play elsewhere). `design/mechanics/Battle/bravado.md` is explicit that running out of Bravado never knocks a bro out: "that's HP's job". The six combat stats are offense, defense, speed, charm, luck and grit (`game/assets/data/party/party_members.json`).

---

## Part 1: What items are for

Example games are listed without long item lists, as asked. Where a row has a link, the claim was checked against that page. Rows without a link rest on general knowledge of those games; see "Limits of this research" at the end.

### A. Consumables (used up when used)

| # | Category | What it's for | Why games include it | Example games |
|---|---|---|---|---|
| A1 | Restore HP | Tops up health, in or out of a fight. Usually comes in small, medium and large sizes. | It is the basic safety net, and the most common thing to spend money on. Sizes give shops something new to sell in each town. | EarthBound (food), Final Fantasy (Potion), Undertale ([healing items](https://strategywiki.org/wiki/UNDERTALE/Healing_Items)) |
| A2 | Restore the skill resource | Refills the bar that powers special moves (MP, SP, PP; for us, Bravado). | Usually kept rarer and dearer than HP items, so the player has to ration special moves across a dungeon. | Persona 5 ([SP items are scarce and restock weekly](https://www.thegamer.com/persona-5-how-to-recover-sp/)), EarthBound, Final Fantasy (Ether) |
| A3 | Restore everything | One rare item that refills both bars, sometimes for the whole party. | A panic button for boss fights. Rarity makes it feel precious. | Final Fantasy (Elixir), Chrono Trigger, EarthBound ([Brain Food Lunch](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)) |
| A4 | Party-wide heal | Heals all party members at once. | Answers enemy attacks that hit everyone. Costs more than single heals. | Dragon Quest, Paper Mario, Persona |
| A5 | Revive | Brings back a downed party member, usually with part of their HP. | Lets a fight continue after a knockout, so one bad turn is not the end. Tiers differ by how much HP comes back. | Final Fantasy (Phoenix Down), Octopath Traveler ([Olive of Life](https://www.thegamer.com/octopath-traveler-2-best-items-to-take-from-npcs/)), Pokemon |
| A6 | Cure a status | Removes one bad condition. Games usually have one cheap cure per condition plus a dear cure-all. | Makes status effects a problem the player can prepare for. Cheap single cures reward knowing the area; the cure-all rewards money. | EarthBound ([remedies](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)), Final Fantasy (Remedy), Pokemon |
| A7 | Temporary buff | Raises a stat or grants a helpful condition for a few turns or minutes. | Lets any character prepare for a hard fight, even one with no buff moves. | Pokemon (X items), EarthBound (Defense Spray), Dragon Quest |
| A8 | Damage item | Thrown or fired at enemies for damage, single target or group. | Gives every character a way to hurt enemies without spending the skill resource, and lets weak hitters contribute. | EarthBound ([Bomb, bottle rockets](https://www.thonky.com/earthbound-walkthrough/items)), Octopath Traveler (soulstones), Final Fantasy |
| A9 | Debuff or disable item | Weakens enemies or puts a condition on them: slowed, stunned, blinded, sickened. | Same as A8, but for control. Often the only way a non-caster can disable an enemy. | EarthBound ([Toothbrush, Dirty Socks](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)), Final Fantasy, Bravely Default |
| A10 | Escape a fight | Guarantees running away. Normally fails against bosses. | An insurance policy when the party is in over its head. | Pokemon (Poke Doll), Breath of Fire, Cassette Beasts ([smoke bomb](https://wiki.cassettebeasts.com/wiki/Item)) |
| A11 | Leave a dungeon or warp | Sends the party to the entrance or to a known town. | Saves a long walk back and lets the player bail out of a dungeon that is going badly. | Pokemon ([Escape Rope](https://bulbapedia.bulbagarden.net/wiki/Escape_Rope)), Dragon Quest ([Chimaera Wing](https://dragon-quest.org/wiki/List_of_items_in_Dragon_Quest_V)), EarthBound (Exit Mouse) |
| A12 | Encounter control | Stops weak enemies from attacking for a while, or draws more of them. | Lets the player skip fights that no longer matter, or farm on purpose. | Dragon Quest ([Holy Water](https://dragon-quest.org/wiki/Holy_water)), Pokemon ([Repel](https://www.dittobase.com/red-blue/items/repel)), Cassette Beasts |
| A13 | Permanent stat booster | Raises one stat by a small amount forever. Rare, usually hidden or a quest reward. | A reward for exploring that never goes out of date, and a way for players to shape a character. | Chrono Trigger ([Tabs](https://strategywiki.org/wiki/Chrono_Trigger/Tabs)), EarthBound (capsules), Octopath Traveler ([Nuts](https://primagames.com/tips/octopath-traveler-2-nut-farming-guide)) |
| A14 | Food with a timed effect | A meal that gives a lasting bonus (more experience, a stat boost) for a set time or number of fights. | Makes restaurants worth visiting and gives each town its own flavour. One meal at a time is the usual rule. | Xenoblade Chronicles 3 ([meals with timed bonuses](https://www.thegamer.com/xenoblade-chronicles-3-cooking-meals-recipes-ingredients-guide/)), Yakuza, Star Ocean ([cooking](https://primagames.com/gaming/how-to-use-item-creation-in-star-ocean-the-second-story-r)) |
| A15 | Mixed-blessing consumable | A benefit with a built-in cost or a gamble: heals but sickens, boosts but confuses, or a random result. | Turns item use into a decision. Often where a game puts its jokes. | EarthBound (Rock Candy raises a random stat), Pokemon (berries that confuse), Yakuza (drinking) |
| A16 | Portable rest | A tent or cottage that restores the whole party at a save point or on the map. | Lets the designer place a long dungeon far from an inn. | Final Fantasy (Tent), Chrono Trigger (Shelter), Bravely Default |
| A17 | Crafting material | Does nothing alone. Combined into gear or better consumables. | Gives enemy drops and exploring a purpose beyond money. | Star Ocean ([item creation](https://primagames.com/gaming/how-to-use-item-creation-in-star-ocean-the-second-story-r)), Like a Dragon ([materials](https://strategywiki.org/wiki/Yakuza:_Like_a_Dragon/Table_of_Contents)), Xenoblade |
| A18 | Sell-only goods | Exists to be sold. No other use. | A way to hand out money with flavour, and a place for item jokes. | EarthBound ([Meteornium](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)), Pokemon (Nugget), Final Fantasy XII (loot) |
| A19 | Shop modifiers | Coupons, vouchers and tickets that change a price or unlock stock. | Small rewards that send the player back to a shop. | Paper Mario, Pokemon, Persona |

### B. Equippables (worn or held)

| # | Category | What it's for | Why games include it | Example games |
|---|---|---|---|---|
| B1 | Weapon | Sets how hard a character hits. Usually one line per character. | The clearest sign of progress: a new town means a better weapon. Also carries character identity. | EarthBound (bat, frying pan, yo-yo), Final Fantasy, Dragon Quest |
| B2 | Body armour | Raises defence. The main protective slot. | Lets the player buy survival instead of grinding for it. | Dragon Quest, Final Fantasy, Like a Dragon ([head, body, legs](https://strategywiki.org/wiki/Yakuza:_Like_a_Dragon/Table_of_Contents)) |
| B3 | Head, arms, legs, feet | Extra armour slots with smaller bonuses, often to speed or luck. | More slots mean more shopping decisions and more small rewards to hand out. | EarthBound (body, arms, other), Bravely Default, Chrono Trigger |
| B4 | Accessory | One or two slots for a special effect instead of plain stats. | Where the interesting choices live, because only a couple fit at once. | Final Fantasy ([accessories](https://strategywiki.org/wiki/Final_Fantasy_VII/Accessories)), Chrono Trigger ([accessories](https://almarsguides.com/retro/walkthroughs/snes/games/chronotrigger/misc/lists/accessories/)), Persona 5 |
| B5 | Status immunity or resistance | Blocks one condition, or rarely all of them. | The gear answer to a boss who relies on one status. Rewards scouting ahead. | Final Fantasy ([Ribbon](https://finalfantasy.fandom.com/wiki/Ribbon_(Final_Fantasy))), Bravely Default ([accessories](https://gamerguides.com/bravely-default/guide/items-and-equipment/armors-and-accessories/accessories)), EarthBound (Franklin Badge) |
| B6 | Stat trade-off gear | A strong bonus paid for with a penalty elsewhere. | Makes gear a choice instead of "biggest number wins". | Bravely Default II ([weight limit](https://goombastomp.com/whats-new-for-the-series-in-the-bravely-default-ii-demo/)), Paper Mario (badges that raise attack and lower defence), Final Fantasy VII (Curse Ring) |
| B7 | Passive-effect gear | Works in the background: slow healing each turn, more money or experience, an automatic buff at the start of a fight. | Lets players build a style around one effect. | Persona 5 ([SP Adhesive](https://twinfinite.net/guides/persona-5-sp-adhesive-how-get-use/)), Undertale ([Temmie Armor](https://undertale.fandom.com/wiki/Temmie_Armor)), Pokemon (held items) |
| B8 | Skill-granting gear | Wearing it unlocks a move or ability. | Makes gear part of the move list, so a find changes how a character plays. | Paper Mario ([badges, limited by Badge Points](https://www.mariowiki.com/Badge_Point)), Final Fantasy IX, Xenoblade (gems) |
| B9 | Set bonus | Wearing matching pieces together gives an extra bonus. | Rewards collecting a full outfit and gives a reason to keep a weaker piece. | Dragon Quest X ([full set bonus](https://dragon-quest.org/wiki/Brigandine)), Dragon Quest XI (outfits), Final Fantasy XI ([sets](https://www.bg-wiki.com/ffxi/Set)) |
| B10 | Cursed gear | Very strong, with a nasty drawback, and often cannot be taken off without paying for help. | High risk for high reward, and a classic trap for careless players. | Dragon Quest ([cursed equipment](https://dragon-quest.org/wiki/Cursed_Equipment)), Final Fantasy, Pokemon (Sticky Barb, Ring Target) |
| B11 | Upgradeable or evolving gear | One piece improved over time at a smith or through the story. | Lets a character keep a signature weapon all game instead of replacing it. | Like a Dragon ([crafting and upgrades](https://www.ggrecon.com/guides/like-a-dragon-infinite-wealth-how-to-craft-and-upgrade-weapons)), Star Ocean, Xenoblade |
| B12 | Character-only gear | Only one party member can use it. | Keeps characters distinct and makes a drop feel personal. | EarthBound, Chrono Trigger, Final Fantasy |
| B13 | Cosmetic gear | Changes looks only, or gives no real stats. | Player expression and jokes at no cost to balance. | Dragon Quest XI ([costumes](https://dragon-quest.org/wiki/Costumes_in_Dragon_Quest_XI)), Xenoblade, Paper Mario (zero-cost badges) |
| B14 | Carrying gear | Raises how much the party can carry. | Only matters in games with a carry limit, where it is a prized upgrade. | Pokemon (bag pockets), Resident Evil-style hybrids, EarthBound (storage service instead) |

### C. Key items, tools and collectibles

| # | Category | What it's for | Why games include it | Example games |
|---|---|---|---|---|
| C1 | Story key | Opens a door, proves something to an NPC, or moves the plot. Cannot be sold or dropped. | The designer's way to gate areas until the player has done something. | EarthBound ([key items](https://strategywiki.org/wiki/EarthBound/Key_Items)), Pokemon, Final Fantasy |
| C2 | Field tool | A reusable item that does something on the map: light, dig, reveal, annoy an NPC. | Adds things to do outside fights and rewards returning to old areas. | Pokemon (rods, Itemfinder), Paper Mario, Golden Sun |
| C3 | Transport | A bike, vehicle or travel pass. | Speeds up crossing ground already cleared. Often a mid-game milestone. | EarthBound (Bicycle), Pokemon, Final Fantasy (airship) |
| C4 | Map or information item | Shows where to go, what an enemy is weak to, or what is nearby. | Reduces getting lost, on the player's terms. | EarthBound (town maps, hint shop), Persona, Dragon Quest |
| C5 | Collectible set | A numbered set gathered across the game for a reward or for bragging rights. | Gives completionists a long goal and ties the whole world together. | EarthBound (Sound Stone melodies), Dragon Quest (mini medals), Pokemon (badges) |
| C6 | Trade-chain item | Useless alone. Swapped with one NPC for the next link in a chain. | A quest told through items; sends the player across the map. | EarthBound ([Contact Lens](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)), Zelda-influenced JRPGs, Pokemon (in-game trades) |
| C7 | Broken item to repair | Does nothing until a character or NPC fixes it into something useful. | A delayed reward and a reason to keep odd finds. | EarthBound ([broken items](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)), Chrono Trigger, Xenoblade |
| C8 | Flavour and joke items | No effect. Exists to be read. | Tone, world-building and jokes. EarthBound is the model here. | EarthBound ([no-effect items](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)), Undertale, Like a Dragon |
| C9 | Special currencies and tokens | A second money used at one place: prize tickets, casino chips, medals. | Makes a mini-game pay out its own rewards without breaking the main economy. | Dragon Quest (casino tokens), Pokemon (Game Corner coins), Like a Dragon |

---

## Part 2: Where Eurobound stands

### The three things that shape everything below

1. **The battle code understands four consumable effects today:** restore HP, restore Bravado, revive, and cure one status (`game/battle/battle_core.gd`, lines 164-170). Intoxicants are handled separately (`game/core/intoxicant.gd`). An item that damages or weakens an enemy has no place in that list yet.
2. **There is no gear in the game.** `game/assets/data/items/equipment.json` is empty, the equipment template says the file "has no ruled schema yet", and a code comment says "no equipment slots exist yet" (`game/core/navigation_roll.gd`, line 16). `design/templates/equipment_template.md` is version 1.0, "pending author review".
3. **Two standing laws change what a "normal" item can be here.** Under `design/narrative/bros_choose_debauchery.md`, no intoxicant gives a free advantage. Under the equipment template's "Era Cringe" rule, every piece of gear pays for its bonus. So categories that are pure upside in other games (A7 buffs, B2 armour) are mixed blessings here by design. That is a house style, not a gap.

Two older idea lists are cited often: `design/items/docs/items.md` and `design/items/docs/equipment.md`. Both use joke stats ("+5 Tourist Vibes") that are not the six real stats, and I found no ruling that says whether their contents are still wanted. They are marked "older list" below.

### A. Consumables

| # | Category | What Eurobound has | Where | Status |
|---|---|---|---|---|
| A1 | Restore HP | Two foods Built. Roughly 30 more foods Written across location item lists, most with a side effect. | `game/assets/data/items/consumables.json` (`lukewarm_kebab`, `questionable_goulash`); `design/worlds/*/items/*.json` (kebab stands, kapsalon, doner, corndog) | **Covered.** The heaviest category by far. |
| A2 | Restore Bravado | Four Built, all alcohol. A few Written. | `consumables.json` (`absinthe_shot`, three brewery beers); `design/worlds/debaucheryville/items/` (energy drink, sauce shot); `candy_smokes` in `key_items.json` is a reusable +2 | **Thin.** About one for every ten HP foods, and nearly all carry an alcohol risk. |
| A3 | Restore everything | One beer heals both bars. A full party heal sits in the older list. | `consumables.json` (`beer_wobbly_windmill_brewery`); `design/items/docs/items.md` | **Thin.** |
| A4 | Party-wide heal | Three in the older list only. The game data has no field for "hits the whole party". | `design/items/docs/items.md` | **Written only.** |
| A5 | Revive | One Built, and it is an enemy drop. Two in the older list. | `consumables.json` (`already_spent_credit`, revives at 10% HP); `design/items/docs/items.md` | **Thin.** No revive that I found can be bought. |
| A6 | Cure a status | One Built (cures Confused, an enemy drop). A handful Written. | `consumables.json` (`revision_sticker`); `design/items/docs/items.md`; `design/worlds/debaucheryville/items/` (hygiene kit, aftercare packet, yogurt) | **Thin.** `design/mechanics/Battle/status_effects.md` lists about 20 conditions, and the location lists add more (Cheese Sweats, Garlic Aura, Food Coma). Most have no item cure. Some are cured by a service (a paid shower) or never (The Herp), which is canon. |
| A7 | Temporary buff | Strong. Vapes, beers and drugs apply named statuses with a crash or a risk. | `consumables.json` (entries with an `intoxicant` block); `design/mechanics/Battle/status_effects.md`; `design/items/general_items/` | **Covered.** Many durations are still marked pending in the data. |
| A8 | Damage item | Three in the older list; one throwable souvenir plate in a location list. None Built. | `design/items/docs/items.md` ("Offensive Items"); `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` | **Thin, and the battle code cannot use one yet.** |
| A9 | Debuff or disable item | One Built as a reusable prize (a chance to Embarrass one enemy, once per fight). Two in the older list. | `key_items.json` (`aa_prize_sit_down_comedy_special`); `design/items/docs/items.md` | **Thin.** |
| A10 | Escape a fight | One in the older list. The game has a Run command, and some fights forbid it. | `design/items/docs/items.md`; `game/battle/battle_core.gd`, line 41 | **Thin.** |
| A11 | Leave a dungeon or warp | No item. Fast travel exists as a paid service in one city. | `design/worlds/sinfonia/items/` (fiaker service) | **Nothing found** as an item. |
| A12 | Encounter control | Nothing. One rental car raises sheep encounters as a quirk. | `design/worlds/publandia/items/paddys_premium_motors_items.json` | **Nothing found.** |
| A13 | Permanent stat booster | No consumable does this. Two permanent items carry small stat changes. | `key_items.json` (`student_id`, `members_card`) | **Nothing found** as a consumable. |
| A14 | Food with a timed effect | Plenty Written: foods that leave a lingering condition, a souvenir that gives luck for five fights. | `design/worlds/shamsterdam/items/`, `design/worlds/sinfonia/items/`, `design/worlds/debaucheryville/items/` | **Covered in docs.** Time is measured five ways (turns, steps, minutes, hours, fights). Bead Eurobound-picf already tracks part of this. |
| A15 | Mixed-blessing consumable | The house style. Nearly every food and drink is one. | `design/templates/consumable_item_template.md` ("No Free Advantage"); `design/mechanics/intoxication_law.md` | **Covered.** Eurobound's strongest ground. |
| A16 | Portable rest | No item. Hostel beds are sold as services at three quality levels. | `design/worlds/debaucheryville/items/hostel_midnight_checkout_items.json`; `design/worlds/shamsterdam/items/the_tolerance_hostel_items.json` | **Nothing found** as an item. |
| A17 | Crafting material | No crafting system. The nearest thing is one shrine that accepts food combinations. | `design/worlds/debaucheryville/items/public_restroom_grease_trap_shrine_items.json` | **Nothing found.** |
| A18 | Sell-only goods | Three Built with a sale value. More junk Written with inspect text. The rules for selling are two placeholder files. | `key_items.json` (`auto_gratuity_receipt`, `fuzzy_dice_of_doubt`, `shell_company_business_card`); `design/items/sinfonia_items/`; `design/economy/itemvalue.md` and `design/economy/shoptypes.md` (each three lines) | **Thin.** Items exist; who buys junk and for how much is unwritten. |
| A19 | Shop modifiers | One Built coupon. | `consumables.json` (`item_questionable_kebab_coupon`) | **Thin.** |

### B. Equippables

Everything in this table is Written at most. Nothing wearable is Built except three cosmetic prizes (B13) and one quest accessory (B5).

| # | Category | What Eurobound has | Where | Status |
|---|---|---|---|---|
| — | The slot layout itself | The template lists eleven slot names. The game has no slots, and the layout has not been ruled. | `design/templates/equipment_template.md`; `game/assets/data/items/equipment.json` | **Empty in the game. This blocks every row below.** |
| B1 | Weapon | One recommended weapon idea per bro, with alternatives. No stats in real terms. | `design/characters/*/…weapons.md`; `design/items/docs/weapon-ideas.md` | **Written as ideas.** |
| B2 | Body armour | Torso and leg pieces in the older list; three defence pieces in one shop list; one souvenir shirt using real stats. | `design/items/docs/equipment.md`; `design/worlds/debaucheryville/items/threads_and_treads_items.json`; `astronomical_cockup_square_items.json` | **Written, mostly in joke stats.** |
| B3 | Head, legs, feet | Present in the older list and scattered through shop lists. | `design/items/docs/equipment.md`; `design/worlds/debaucheryville/items/` | **Written, joke stats.** |
| B4 | Accessory | The largest group in the older list: necklaces, rings, watches, phones. | `design/items/docs/equipment.md` | **Written, joke stats.** |
| B5 | Status immunity or resistance | A few scattered cases (earplugs and shades against club hazards, two older-list immunities). One Built quest accessory suppresses The Herp for the party. | `design/worlds/debaucheryville/items/strobe_survival_kit_items.json`; `design/items/gold_circle_coin_item.md` | **Thin.** No list of which conditions gear may block. |
| B6 | Stat trade-off | A rule, not a list: every piece needs an "Era Cringe" drawback. | `design/templates/equipment_template.md` | **Covered as a rule.** The drawbacks are not yet expressed in the six stats. |
| B7 | Passive-effect gear | A few older-list ideas (a pager, a chain wallet). | `design/items/docs/equipment.md` | **Thin.** |
| B8 | Skill-granting gear | Stated as intent: weapons gain Bravado skills as personal quests advance. | `design/mechanics/Battle/bravado.md` ("Item & Bravado Synergy") | **Written as intent.** |
| B9 | Set bonus | Two docs each describe three sets. Only one set name appears in both. | `design/mechanics/Battle/bravado.md`; `design/items/docs/equipment.md` ("Special Combo Sets") | **Written, and the two lists don't match.** |
| B10 | Cursed gear | A different shape: "permanent items" that can never come off, with "Curse Item" as a type. No strong-but-cursed gear that can be removed at a price. | `design/templates/permanent_item_template.md`; `design/items/vip_wristband_item.md` | **Covered differently.** |
| B11 | Upgradeable gear | The template has an optional upgrade table; weapon docs sketch three-stage paths. | `design/templates/equipment_template.md`; `design/characters/Bradley/bradleysweapons.md` | **Written as intent.** |
| B12 | Character-only gear | An "Equippable By" field in the template; weapons are per bro. | `design/templates/equipment_template.md` | **Written.** |
| B13 | Cosmetic gear | Three Built arcade prizes marked wearable and cosmetic. | `key_items.json` (`aa_prize_fangs_for_nothing`, `aa_prize_sixty_minute_emerald`, `aa_prize_two_grand_tie_dye_tee`) | **Built.** The only wearables in the game data. |
| B14 | Carrying gear | Three items add "inventory slots". I found no ruling that the party has a carry limit for them to raise. | `design/items/docs/equipment.md`; `design/worlds/sinfonia/items/` (tote) | **Written, with nothing to act on.** |

### C. Key items, tools and collectibles

| # | Category | What Eurobound has | Where | Status |
|---|---|---|---|---|
| C1 | Story key | Several Built: door passes, quest objects, a wristband. | `key_items.json` (`members_card`, `sea_monkeys`, `millennium_bug`, `participant_wristband`) | **Covered.** |
| C2 | Field tool | Several Built or Written: a squirt gun for NPC reactions, a sobriety test, a flashlight that reveals hints. | `key_items.json` (`aa_prize_*_hydro_bro_2000`, `aa_prize_sobriety_test_deluxe`); `design/worlds/shamsterdam/items/voetgangerstunnel_items.json` | **Covered, lightly.** |
| C3 | Transport | Rental cars in one city, a carriage service in another. | `design/worlds/publandia/items/paddys_premium_motors_items.json`; `design/worlds/sinfonia/items/` | **Written, city by city.** |
| C4 | Map or information item | A map item that improves tunnel navigation odds. | `design/worlds/shamsterdam/voetgangerstunnel.md`, line 135 | **Thin.** One case. |
| C5 | Collectible set | Very strong: brewery beers, openers and stamps (16 each), NFTs, claw-machine plushies, arcade prizes. | `design/items/brewery_tour/`; `design/items/*_nft_item.md`; `key_items.json` (`aa_claw_*`, `aa_prize_*`) | **Covered.** The second-heaviest category. |
| C6 | Trade-chain item | Nothing found in the item data. | — | **Nothing found.** |
| C7 | Broken item to repair | One Built quest item is a broken handheld. I did not confirm it gets repaired. | `key_items.json` (`item_broken_symbol_game_boy`) | **Thin.** |
| C8 | Flavour and joke items | Strong, and backed by a ruling that junk pays off when inspected. | `.claude/CLAUDE.md`; `design/items/sinfonia_items/`; `key_items.json` (`aa_junk_*`) | **Covered.** |
| C9 | Special currencies and tokens | Arcade tickets, crypto coins, location currencies. | `key_items.json` (`ticket_price` fields); `design/economy/shitcoin_master_pool.md` | **Covered.** |

---

## Part 3: What this means

### Where Eurobound is already rich

Food, drink and drugs with a catch; collectible sets; quest passes; junk with jokes. These are the EarthBound-flavoured categories, and they are where the writing has gone. Nothing below suggests cutting any of it.

### The gaps, in order of how much they hold up

1. **Gear does not exist in the game.** No slots, no data format, a template awaiting your review. Every wearable idea written so far (about 20 in location lists, about 55 in the older list) is waiting on this. It is also the largest pile of work that cannot start: weapons, armour, accessories, sets and immunities all depend on which slots exist and which of the six stats gear may touch.

2. **Staying alive in a fight leans on one kind of item.** HP food is everywhere. The other survival tools are thin: one revive (a drop, not for sale), one status cure (also a drop), and Bravado comes back almost only through alcohol, which has a risk attached by law. A player who runs out of Bravado or has a bro go down has very few items to reach for.

3. **About 20 conditions, almost no cures.** Other JRPGs pair most conditions with a cheap cure. Here, most have none as an item. Some of that is deliberate (The Herp, the paid shower). What is missing is a decision, condition by condition, on which are meant to be curable by an item, which by a service, and which just run out.

4. **Nothing to throw at the enemy.** Damage and debuff items are a staple of EarthBound in particular. Eurobound has a few in an older list and one reusable prize, and the battle code has no way to use a damage item yet.

5. **The older lists need a verdict.** `design/items/docs/items.md` and `design/items/docs/equipment.md` hold most of the revive, cure, escape, damage and gear ideas in this report. They use stats that no longer exist. Whether they are a backlog to convert or history to retire changes how empty several rows above are.

### Smaller gaps

- **Junk has no market.** Sell-only items exist, but the two economy files that would say who buys them and what rarity means are placeholders.
- **No permanent stat boosters** as a findable reward. In other games these are the standard prize for exploring off the path.
- **No crafting materials.** This may be a choice. Many JRPGs skip crafting entirely; EarthBound does.
- **No encounter control or dungeon exit items.** Whether these matter depends on how fights start in Eurobound and how long its dungeons run, which I did not find stated in the item docs.
- **Set bonuses are described twice with different sets** (`bravado.md` and `equipment.md`).
- **Carrying gear with no carry limit.** Three items raise an inventory limit that I could not find ruled anywhere.
- **Effect lengths use five different clocks** (turns, steps, real minutes, in-game hours, fights). Partly tracked in Eurobound-picf.

### Questions this raises for you (not answered here)

- Which gear slots does a bro have?
- Is a category meant to be empty on purpose (crafting, encounter control, clean Bravado restores)?
- Are the two older lists a backlog or retired?

---

## Doc defects filed while reading

| Bead | What |
|---|---|
| Eurobound-028j | `design/templates/consumable_item_template.md` says the game's consumable data has four fields. It now has many more (revive, status cure, price, stack size, intoxicant). Anyone using the template would list fields as "missing" that already exist. |
| Eurobound-81un | Three docs disagree on what cures a hangover (`status_effects.md` line 35, `bravado.md` line 23, `items.md` line 13). Needs your ruling. |

---

## Limits of this research

- **Some pages blocked automated reading** (TV Tropes, Bulbapedia, StrategyWiki, Fandom wikis). For those I relied on search-result summaries of the page, and the link is given so you can check it.
- **Rows without a link** in Part 1 rest on general knowledge of those games, not on a page read today. The categories themselves are well established; the specific example could be off in a detail.
- **Search summaries mixed sequels at times** (Octopath Traveler and its sequel; several Like a Dragon titles). I cite the series, not one entry, where that happened.
- **Eurobound counts are approximate.** Location item lists use about 40 different type labels, so "roughly 30 foods" and "about 20 gear pieces" come from a script tally, not a hand count.
- **I did not read every location doc.** Items that live only in a location's prose, and not in its item list, are not counted.

## Sources

General taxonomy and multi-game lists
- [Standard RPG Items (TV Tropes)](https://tvtropes.org/pmwiki/pmwiki.php/Main/StandardRPGItems)
- [Item (Cassette Beasts wiki)](https://wiki.cassettebeasts.com/wiki/Item)

EarthBound
- [EarthBound item lists (Almar's Guides)](https://almarsguides.com/retro/walkthroughs/snes/games/Earthbound/Misc/Lists/Items/)
- [EarthBound items (Thonky)](https://www.thonky.com/earthbound-walkthrough/items)
- [EarthBound key items (StrategyWiki)](https://strategywiki.org/wiki/EarthBound/Key_Items)
- [EarthBound item properties table (Data Crystal)](https://datacrystal.tcrf.net/wiki/EarthBound/Item_Properties_Table)

Final Fantasy
- [Final Fantasy VII items (StrategyWiki)](https://www.strategywiki.org/wiki/Final_Fantasy_VII/Items)
- [Final Fantasy VII accessories (StrategyWiki)](https://strategywiki.org/wiki/Final_Fantasy_VII/Accessories)
- [Final Fantasy IX items (StrategyWiki)](https://strategywiki.org/wiki/Final_Fantasy_IX/Items)
- [Ribbon (Final Fantasy Wiki)](https://finalfantasy.fandom.com/wiki/Ribbon_(Final_Fantasy))
- [Sets (BG Wiki, Final Fantasy XI)](https://www.bg-wiki.com/ffxi/Set)

Dragon Quest
- [Cursed Equipment (Dragon Quest Wiki)](https://dragon-quest.org/wiki/Cursed_Equipment)
- [Holy water (Dragon Quest Wiki)](https://dragon-quest.org/wiki/Holy_water)
- [List of items in Dragon Quest V (Dragon Quest Wiki)](https://dragon-quest.org/wiki/List_of_items_in_Dragon_Quest_V)
- [Brigandine set (Dragon Quest Wiki)](https://dragon-quest.org/wiki/Brigandine)
- [Costumes in Dragon Quest XI (Dragon Quest Wiki)](https://dragon-quest.org/wiki/Costumes_in_Dragon_Quest_XI)

Pokemon
- [Escape Rope (Bulbapedia)](https://bulbapedia.bulbagarden.net/wiki/Escape_Rope)
- [Repel (Dittobase)](https://www.dittobase.com/red-blue/items/repel)
- [List of items by pocket, Sword and Shield (Bulbapedia)](https://bulbapedia.bulbagarden.net/wiki/List_of_items_by_pocket_in_Pok%C3%A9mon_Sword_and_Shield)

Persona
- [How to recover SP in Persona 5 Royal (TheGamer)](https://www.thegamer.com/persona-5-how-to-recover-sp/)
- [SP Adhesive (Twinfinite)](https://twinfinite.net/guides/persona-5-sp-adhesive-how-get-use/)

Chrono Trigger
- [Tabs (StrategyWiki)](https://strategywiki.org/wiki/Chrono_Trigger/Tabs)
- [Accessories (Almar's Guides)](https://almarsguides.com/retro/walkthroughs/snes/games/chronotrigger/misc/lists/accessories/)

Paper Mario
- [Badge Point (Super Mario Wiki)](https://www.mariowiki.com/Badge_Point)
- [List of badges in Paper Mario (Super Mario Wiki)](https://www.mariowiki.com/List_of_badges_in_Paper_Mario)

Xenoblade
- [Xenoblade Chronicles 3 cooking and meals (TheGamer)](https://www.thegamer.com/xenoblade-chronicles-3-cooking-meals-recipes-ingredients-guide/)
- [Xenoblade Chronicles 3 cooking guide (GameSpot)](https://gamespot.com/articles/xenoblade-chronicles-3-cooking-guide/1100-6506065/)

Octopath Traveler
- [Nut farming guide (Prima Games)](https://primagames.com/tips/octopath-traveler-2-nut-farming-guide)
- [Best items to take from NPCs (TheGamer)](https://www.thegamer.com/octopath-traveler-2-best-items-to-take-from-npcs/)

Bravely Default
- [Accessories (Gamer Guides)](https://gamerguides.com/bravely-default/guide/items-and-equipment/armors-and-accessories/accessories)
- [What's new in the Bravely Default II demo: weight limit (Goomba Stomp)](https://goombastomp.com/whats-new-for-the-series-in-the-bravely-default-ii-demo/)

Star Ocean
- [Item creation in Star Ocean The Second Story R (Prima Games)](https://primagames.com/gaming/how-to-use-item-creation-in-star-ocean-the-second-story-r)

Yakuza / Like a Dragon
- [Yakuza: Like a Dragon table of contents: gear and material categories (StrategyWiki)](https://strategywiki.org/wiki/Yakuza:_Like_a_Dragon/Table_of_Contents)
- [Crafting and upgrading weapons in Infinite Wealth (GGRecon)](https://www.ggrecon.com/guides/like-a-dragon-infinite-wealth-how-to-craft-and-upgrade-weapons)

Undertale
- [Healing items (StrategyWiki)](https://strategywiki.org/wiki/UNDERTALE/Healing_Items)
- [Temmie Armor (Undertale Wiki)](https://undertale.fandom.com/wiki/Temmie_Armor)
