# Proposal: The Munchies (effects and length)

**Status: PROPOSED, waiting on the author (Eurobound Desk `Eurobound-0zt0-q1`).** Nothing here is canon until approved. Every number is marked PROPOSED unless it is quoted from canon.
**Bead:** Eurobound-0zt0 (found by Eurobound-vt7k).
**Author answer that ordered this (bead page, 2026-11-13), verbatim:** "Have a systems designer propose effects and length".
**Already ruled, not reopened here:**
- The Space Cake (8 SOVS) starts a 120-minute Space Cake Timer. When it lands the bro gets +40 Bravado and Space Cake Gamble for 90 game-clock minutes (cap 180). Rest ends the Gamble and clears an unlanded timer (`docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md` SC1-SC11, approved on Eurobound Desk vt7k-q2).
- **The Munchies follows when Space Cake Gamble ends by time, not by rest** (same spec, SC13).
- Lengths on the game clock are stored in `default_duration.clock_minutes` (Eurobound Desk zcdf-q1; `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md:82`). A screen change costs 10 minutes, a fight 20, talking nothing; rest jumps to 10:00 (`docs/superpowers/NEXT_WORK.md:667-670`, `:685`).
- Food, drugs and vapes are not "a drink" (`NEXT_WORK.md:713`).

**Binding law:** `design/mechanics/intoxication_law.md` and `design/narrative/bros_choose_debauchery.md`.

Starbaked is the display name of the coffeeshop whose doc is `design/worlds/shamsterdam/de_groene_gids.md` (`:1`, `:7`). This proposal says Starbaked.

---

## 1. What canon already says

| Subject | Canon | Where |
|---|---|---|
| Trigger and effect | "The Munchies: Triggers after Bravado boost wears off, increases food purchase likelihood" | `design/worlds/shamsterdam/de_groene_gids.md:216` |
| Length | "Variable"; "Increases food purchase likelihood — feeds Leeman's, The Kapsalon King, Fritomat" | `design/worlds/shamsterdam/npcs/De_Groene_Gids/npc_budtender_bas.md:250`, `:334` |
| Bravado | The icon is the "Post-Bravado-drop food drive"; the prompt "fires on Bravado drop-off" | `design/worlds/shamsterdam/PNG_Assets/De_Groene_Gids_PNG_Assets.md:356`, `:638` |
| Fritomat | "Munchies / +50% HP restoration / Everything is incredible" | `design/worlds/shamsterdam/frietomat.md:270` |
| Fritomat, the pipeline | "Trigger: Visiting Fritomat after Starbaked within 2 hours. Effect: All food HP restoration +50%. Dialogue: 'This is the best thing I've ever eaten' (it's a 3 SOVS kroket)" | `frietomat.md:174-179` |
| Fritomat, art | Munchies shimmer on the food and a "+50% HP restoration marker"; the shimmer "applies only when arriving from Starbaked within 2 in-game hours" | `design/worlds/shamsterdam/PNG_Assets/frietomat_png_assets.md:214`, `:222`, `:239` |
| Leeman's Döner Palace | "Post-coffeeshop arrival raises Triple Tower order probability in the ordering UI default"; Mehmet's "tourist eyes" | `design/worlds/shamsterdam/PNG_Assets/Leemans_Doner_Palace_PNG_Assets.md:590`; `de_groene_gids.md:254` |
| The Kapsalon King | "Munchies pipeline endpoint (WARNING: may overcorrect)" | `design/worlds/shamsterdam/kapsalon_koning.md:335` |
| The timing | Bas's customers reach the food counters "about ninety minutes later, considerably worse" | `npc_budtender_bas.md:269`, `:276` |
| Stroopwafel Cart, Pancake House | "Enhanced by munchies state"; "munchies help" with the Portion Revelation | `design/worlds/shamsterdam/stroopwafel_cart.md:260`; `the_pancake_house.md:267` |

Nothing in canon gives The Munchies a length in minutes, says how "purchase likelihood" works for a player who chooses his own purchases, or sizes the Bravado drop.

**Two readings this proposal relies on (PROPOSED):**
1. **The Munchies status is the Munchies Pipeline.** Fritomat's "+50% HP" row and its "within 2 hours of Starbaked" trigger describe the same thing. Under the approved timeline a cake bought at Starbaked lands 120 minutes later and the Gamble runs 90 more, so "within 2 hours of Starbaked" can never be true when The Munchies fires. The vendors therefore check **the status**, and the canon "2 hours" becomes the status's own length (M3).
2. **Not the same thing:** the "Munchies Tax" is MANGO OG GUSHERS's approved rest event (`design/items/general_items/mango_og_gushers_item.md:118`). It keeps its own rules and is not touched. The Syrup Trap's "+Munchies risk" (`design/worlds/shamsterdam/shamsterdam_condom_machines.md:153`) has no numbers and becomes a source only when its own doc says so.

---

## 2. The Munchies (every value PROPOSED)

| Id | Rule | PROPOSED value | Anchor / reason |
|---|---|---|---|
| M1 | **Source** | Fires on the bro whose Space Cake Gamble ends **by time**. A Gamble ended by rest fires nothing. However many cakes fed the Gamble, The Munchies fires once | Approved SC13. "Shamsterdam Dream" reaches it the same way, through the timer (SC2) |
| M2 | **Scope / bearer** | `section: "neutral"`, `scope: ["field"]`, bearer = that bro. It is not carried into battle | It is a mixed status: one benefit, two costs. Canon gives it no battle use |
| M3 | **Length** | `clock_minutes: 120`, `ends_on_rest: true` | The canon "within 2 hours" window (`frietomat.md:175`, `frietomat_png_assets.md:222`), reading 1. On the clock: 12 screen changes or 6 fights. Alternatives for the author: 60 or 90 |
| M4 | **The comedown** (separable) | When The Munchies fires, the bro's Bravado **drops by 40**, never below 0: the same 40 the cake gave | "Triggers after Bravado boost wears off"; "Post-Bravado-drop". At today's Bravado maximums (12 / 20 / 14, `game/assets/data/party/party_members.json`) that is Zero Bravado: signature moves and Ultimates lock, basic attacks only (`design/mechanics/Battle/bravado.md:29`). Food is how he gets it back (the Triple Tower gives +15 Bravado, `leemans_doner_palace.md:148`), which is what makes him buy food. Alternatives: half his current Bravado, or no drop |
| M5 | **Food tastes incredible** | Every food item the bro eats restores **+50% HP**, rounded up (a +20 HP kroket gives 30) | Canon number (`frietomat.md:270`, `:176`). Applies to any `subtype: "food"` item he eats from the menu and any vendor meal, in every city, since "all food" is canon and the status travels with him. Bravado from food is not increased |
| M6 | **"Increases food purchase likelihood"** | Each time he buys food, **50% chance he orders double**: two portions, pays for both, eats both on the spot. If the wallet covers only one, he gets one | The player already decides what to buy, so "likelihood" needs a mechanic. This is the Kapsalon King's "may overcorrect", and a bounded, impulsive action of the kind Law §3 allows. The second portion heals too; when his HP is already full it is pure waste, which is the cost. 50% is the same coin the Gamble flips (approved T2) |
| M7 | **Menu default** | At a food vendor, the cursor starts on the most expensive item while a bro has The Munchies | Canon at Leeman's (`Leemans_Doner_Palace_PNG_Assets.md:590`), extended to every food menu. The player can move it; it costs only the inattentive |
| M8 | **Full is full** | The Munchies ends early once the bro has eaten **3 food items** (a double order counts as 2) | Gives canon's "Variable" length (`npc_budtender_bas.md:250`) a meaning and caps the +50% bonus at three items, so it cannot be farmed for two hours |
| M9 | **Stacking** | `stack_rule: "refresh"`. A second Gamble ending while The Munchies is live resets it to 120 minutes and the 3-item count, and applies M4 again. The bonus never grows past +50% | Matches Contact High (approved CH8) |
| M10 | **Cures** | Rest, waiting it out, or eating it off (M8). No item cures it | Rest is the universal reset (`NEXT_WORK.md:670`) |
| M11 | **Cues** | The Munchies status icon on the bro's Status card (`De_Groene_Gids_PNG_Assets.md:356`); Fritomat's shimmer and "+50% HP" marker show while any bro has the status (`frietomat_png_assets.md:214`, `:239`); a doubled order shows two portions landing on the counter. Reduced motion: Fritomat's static marker (`:340`). Mehmet's "tourist eyes" and the Fritomat "best thing I've ever eaten" line already exist. **No new lines are proposed**; anything more comes from a writing round with the author | Law §7 |
| M12 | **Other statuses** | A doubled Fritomat or Stroopwafel order counts as two meals against The Shakes (approved −2 turns / −80 steps a meal, `frietomat.md:271`). The Munchies does not touch Navigation, Sober, or the Munchies Tax. The food tables' "Space Cake Effect" rows read the Gamble, not The Munchies (approved reading, Space Cake spec §1) | One rule per status |

**Not proposed:** any stat change, any battle effect, any price change at the vendors, any new item, any dialogue.

### 2.1 What the bro thinks he gets and what he gets (`bros_choose_debauchery.md:24`)

- **He thinks** the cake finally wore off and he has discovered the best kroket in Europe.
- **He actually gets** his swagger gone, a 3 SOVS kroket that heals like a 5 SOVS one, and a second kroket he did not mean to order.

### 2.2 Worked example (PROPOSED values)

Bradley (30 HP, 14 Bravado) eats a Space Cake. Two hours later it lands: Bravado back to 14, the floor moves, the tunnel does what it does for 90 minutes. Then The Munchies fires:

1. His Bravado goes 14 → 0 (M4). His signature moves lock.
2. At Fritomat the cursor sits on the Satéschotel, 5 SOVS (M7; `frietomat.md:142`). He buys a kroket instead: 3 SOVS, 30 HP instead of 20 (M5).
3. The coin lands wrong on his next purchase: two Berehaps, 8 SOVS, the second one eaten at full HP (M6). That is 3 items; The Munchies ends (M8).

Total: 11 SOVS spent where 7 would have done, and he still has no Bravado until he drinks or flexes it back.

### 2.3 Rejected alternatives

- **Only the +50% HP bonus.** A free advantage from a drug, which `bros_choose_debauchery.md:16` rules out.
- **A hunger timer that drains HP until he eats.** Punishes the player for the cake instead of letting the bro be an idiot at a snack wall, and has no canon behind it.
- **Vendors raise prices on a bro with The Munchies.** Starbaked already owns that joke: Tourist Trapped, +15% for 1 hour (`de_groene_gids.md:213`).
- **Forcing the purchase** (the bro buys food on his own when he passes a vendor). Takes the wallet out of the player's hands with no input; M6 keeps the player's decision to buy and only doubles it.

---

## 3. Proposed data (for `game/assets/data/skills/status_effects.json`, after approval)

```json
"munchies": {
  "display_name": "The Munchies",
  "section": "neutral", "scope": ["field"], "bearer": "bro",
  "default_duration": {"clock_minutes": 120, "ends_on_rest": true, "until_cured": false},
  "stack_rule": "refresh",
  "cured_by": [{"kind": "rest"}],
  "cues": {"icon": null, "idle_anim": null, "particle": null}
},
"space_cake_gamble": { "then": {"status": "munchies", "stacks": false} }
```

The approved shape has no field for M4 (Bravado drop on firing), M5 (food heal bonus), M6 (double-order chance) or M8 (ends after 3 items). As with the Space Cake landing, they would be named constants in code with `_pending` notes that cite this ruling (`game/core/field_status.gd:50-53` is the precedent). If the author wants them as data fields, that is a shape question for another pass.

---

## 4. Intoxication law §8: 10-point review

| # | Point | Answer |
|---|---|---|
| 1 | Source | The end of Space Cake Gamble by time (M1): the Space Cake, 8 SOVS, or "Shamsterdam Dream", both from Starbaked |
| 2 | Immediate effect | Bravado −40 (M4). For up to 120 clock minutes: food heals +50% HP (M5), food orders double half the time (M6), food menus open on the dearest item (M7) |
| 3 | Escalation | None. It refreshes and never deepens (M9). More cakes lengthen the Gamble before it, not The Munchies |
| 4 | Player-facing cues | Status icon; Fritomat shimmer and +50% marker; two portions on the counter for a double order; the Bravado bar emptying. Reduced-motion forms exist (M11) |
| 5 | Player control | The player still chooses whether to buy food and what. Half the time the order doubles, and never past what the wallet holds. No movement or dialogue takeover |
| 6 | Duration and recovery | 120 clock minutes, or 3 food items, or rest. It is a saved `FieldStatus` clock row. It cannot loop: it fires only from a Gamble that ran out, and a Gamble needs a new cake and two more hours |
| 7 | Comedic consequence | The cake wears off and takes his confidence with it; he tries to buy it back one fried thing at a time and keeps getting two |
| 8 | Interactions | M12: doubled meals count twice against The Shakes; no Navigation effect; Sober untouched; Munchies Tax separate; rest after the Gamble skips it entirely (approved SC13) |
| 9 | Technical dependencies (proposed engineering, not built) | `then` firing from a clock row on time expiry only (the Space Cake spec's own dependency, §6 point 9); the Bravado drop on firing; a food-heal multiplier where items are eaten (`game/core/game_state.gd:81-93`, `game/ui/field_menu.gd:200`) and at vendor counters; the double-order roll in the purchase path (`game/core/shop_catalog.gd:158-163`); an eaten-items count on the row; the default-cursor rule in food menus. None of the Shamsterdam food vendors has a scene yet |
| 10 | Further author approval | M1-M12 and the two readings in §1. M4 can be dropped or resized on its own. Any lines come from a writing round, not this spec |

Nothing lectures, warns or explains. The bros wanted the cake, complained it wasn't working, and are now thrilled about a kroket.

## 5. `bros_choose_debauchery.md` check

- **No free advantage (l.16):** the +50% HP is capped at three items and comes with an emptied Bravado bar and doubled orders.
- **No lectures (l.18):** every cue is an icon, a shimmer or a second portion.
- **Willing and delusional (l.28):** nothing stops him going straight back to Starbaked.

## 6. If approved

1. Record the ruling in `docs/superpowers/NEXT_WORK.md`, `de_groene_gids.md` (Status Effect Application), `npc_budtender_bas.md:250` and `frietomat.md:174-179`, `:270`.
2. Write the §3 entry and the `then` on `space_cake_gamble`.
3. File the gameplay-programmer bead for §4 point 9.

## 7. Found work filed (not decided here)

- `frietomat.md:175` and `frietomat_png_assets.md:222`, `:398` trigger the Munchies Pipeline "within 2 hours of Starbaked", which the approved 120 + 90 minute Space Cake timeline can never satisfy. Reading 1 above resolves it if approved; the docs then need the wording changed. Bead: Eurobound-wpb6.
