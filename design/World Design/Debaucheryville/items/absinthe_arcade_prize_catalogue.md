# Absinthe Arcade Prize Redemption Catalogue

*"Thirteen prizes. Every one of them a legend. Some of them cost more than the flight." - Lord Pilsner, at the counter*

**Status:** DRAFT. Every ticket price, payout and effect below is **PROPOSED — needs author ruling**.
**Binding source:** author ruling 2026-11-09 (`docs/superpowers/NEXT_WORK.md`, "Arcade fights pay TICKETS, not SOVS").
**Where:** the Prize Redemption counter built into the Absinthe Arcade bar (the cracked absinthe bottle).
**Currency:** prizes are bought with **tickets only**. Tickets are never bought, sold or converted to SOVS. Cabinet tokens cost 1 SOVS each (Frogger 2 tokens, Street Fighter 3, Kebab Kombat 4, per the same ruling).

---

## Ticket scale — PROPOSED — needs author ruling

| Source | Entry cost | Ticket payout per win | Notes |
|---|---|---|---|
| Frogger: Existential Edition | 2 tokens (2 SOVS) | 5-15 | Per villain: Hatchback 5 per car, Sinking Fund 8, Croc Monsieur 15 (villain profiles) |
| Street Fighter: Identity Crisis | 3 tokens (3 SOVS) | 4-15 | Per villain: Palette Swap 4 per Swap, Jarmila 8, Vratislav 15 |
| Kebab Kombat | 4 tokens (4 SOVS) | 5-20 | Ladder: Condiment Clan Ninja 5 per ninja (Mystery Brown 10), Count Continue 8, Shish Kahn 20. One full climb is roughly 40 tickets for 12 tokens |
| DDR dance-off (three-pad) | PROPOSED — needs author ruling | 0-30 by score | Proposed on the decisions page: 2 tokens per song |

| Prize tier | Price range |
|---|---|
| Junk | 15-120 tickets |
| "Better" | 800-2500 tickets |

**The math the counter does not post:** the Chug E. Cheese Plush at 2500 tickets is about 60 full Kebab Kombat ladder climbs, roughly 720 SOVS in tokens, for a toy worth 3 SOVS. That is the design.

---

## Prize list

| # | Name | Item ID | Tier | Price (tickets) | In-game description | Proposed effect | Actual value |
|---|---|---|---|---|---|---|---|
| 1 | Paraffin Pucker | `item_aa_prize_paraffin_pucker` | Junk | 15 | Red wax lips that taste like a birthday candle somebody else blew out. Lord Pilsner wore them for a full lap of the bar and logged every turned cheek as "a near miss." | None (key trinket) | 0 SOVS |
| 2 | Fangs for Nothing | `item_aa_prize_fangs_for_nothing` | Junk | 20 | Glow-in-the-dark vampire teeth one size too large for any human jaw. Bradley has worn them through two drinks and a pickup line and describes the night as "dangerous." | Cosmetic: while equipped, the wearer's battle shouts are lisped ("Thmaaaash!"). No stats. | 0 SOVS |
| 3 | Sixty-Minute Emerald | `item_aa_prize_sixty_minute_emerald` | Junk | 25 | A gold-tone ring with a green glass stone the size of a cocktail olive. After an hour the finger underneath matches the stone, which Chadwick says is how you know it's real. | Cosmetic status **Jade Knuckle** after 60 in-game minutes worn. No stat change. Chadwick cites it as proof of authenticity in dialogue. | 0 SOVS |
| 4 | Five-Finger Lint Discount | `item_aa_prize_five_finger_lint_discount` | Junk | 35 | A sticky rubber hand on a three-foot leash, already furred with bar-floor hair, a ticket stub and one curly hair nobody will claim. Bradley slaps it on the bar whenever he wants another round and calls this "ordering." | None (key trinket) | 0 SOVS |
| 5 | Pinky Promise Prison | `item_aa_prize_pinky_promise_prison` | Junk | 40 | A woven paper tube that tightens the harder you pull. Chadwick and Bradley got their fingers stuck in opposite ends and have been asking the bartender for the couples' discount. | None (key trinket) | 0 SOVS |
| 6 | Neon Wrist Guillotine | `item_aa_prize_neon_wrist_guillotine` | Junk | 60 | A strip of spring steel in a hot-pink fabric sleeve that snaps around the wrist on impact and through the sleeve by Thursday. Bradley stacks it under his other bracelets and calls the set his "armor." | None (key trinket) | 0 SOVS |
| 7 | Fuchsia Foot of Fortune | `item_aa_prize_fuchsia_foot_of_fortune` | Junk | 90 | A rabbit's foot dyed a pink no living rabbit ever reached, on a keychain that clearly did nothing for the rabbit. Chadwick clipped it to his chain wallet and rubs it before every claw-machine attempt. | None. The claw stays rigged. | 0 SOVS |
| 8 | Sobriety Test Deluxe | `item_aa_prize_sobriety_test_deluxe` | Junk | 120 | A palm-sized plastic maze with three silver balls and one hole, unsolvable after the second absinthe. Lord Pilsner has been working on it since eleven and says he is "one tilt away." | Usable from inventory. Always fails while the user is Drunk or Confused (tilt rattle, no result). Solvable sober, for no reward. | 0 SOVS |
| 9 | Sit-Down Comedy Special | `item_aa_prize_sit_down_comedy_special` | "Better" | 800 | A pink rubber whoopee cushion priced like a used scooter. Bradley calls it "the strongest weapon in the building" and has deployed it on every bar stool, including the bidet. | Battle item, once per battle, never consumed: 35% chance to inflict **Embarrassed** on one enemy. On a miss, the bros claim it hit. | 1 SOVS |
| 10 | Flamingo Hydro Bro 2000 | `item_aa_prize_flamingo_hydro_bro_2000` | "Better" | 1200 | A flamingo-pink pump-action squirt gun that holds one shot glass of liquid and leaks a second. Chadwick filled it with absinthe and calls it his "concealed carry." | Field interaction: squirt an NPC for a one-line reaction. No battle use. | 2 SOVS |
| 11 | Highlighter Hydro Bro 2000 | `item_aa_prize_highlighter_hydro_bro_2000` | "Better" | 1200 | The same squirt gun in highlighter yellow, won separately because Lord Pilsner refused to share a weapons platform with Chadwick. It holds beer. It does not hold it well. | Same as Flamingo Hydro Bro 2000. | 2 SOVS |
| 12 | Two-Grand Tie-Dye Tee | `item_aa_prize_two_grand_tie_dye_tee` | "Better" | 2000 | A one-size-fits-nobody tie-dye shirt printed slightly crooked with I ♥ ABSINTHE ARCADE. Bradley wears it over his jersey and calls it his "championship belt." | Equippable cosmetic, 0 stats. | 3 SOVS |
| 13 | Chug E. Cheese Plush | `item_aa_prize_chug_e_cheese_plush` | "Better" | 2500 | A cross-eyed plush pizza rat in a chef's hat, stuffed with what feels like aquarium gravel and smelling like a ball pit. Lord Pilsner handed over two and a half thousand tickets for it and calls it "the crown jewels." | None. Inventory key item only. | 3 SOVS |

**Rules for every prize (PROPOSED — needs author ruling):** non-stackable except junk tier (stack 9); cannot be sold to any vendor; can be dropped; no resale value in SOVS.

**Chug E. Cheese Plush constraint (CLAUDE.md: no mascots):** it is an inventory item. It never speaks, never joins battles, never has a sprite following the party and never gets reaction dialogue of its own. "Chug E. Cheese" is the in-world pizza-arcade brand on its tag, not a companion.

---

## Open questions for the author

1. Ticket payouts per cabinet and the DDR dance-off entry cost and payout (all PROPOSED above).
2. Every prize price and every proposed effect.
3. Do junk prizes stack, and can prizes be dropped?
4. Is the existing equipment entry "Slap Bracelet (Leopard Print)" (`design/Inventory/equipment.md`) meant to be the same object as the Neon Wrist Guillotine? Kept separate here.
5. Does the Two-Grand Tie-Dye Tee keep its name if its price moves off 2000 tickets?
