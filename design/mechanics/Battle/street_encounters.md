# Street Encounters (APPROVED: Option A, "EarthBound straight")

> **Status: APPROVED, Option A.** Author, Eurobound Desk `Eurobound-skjd-q2`, 2026-11-16, verbatim:
> "A: EarthBound straight (lose = back to last save, lose some SOVS)". Ledger: `docs/superpowers/NEXT_WORK.md`,
> the 2026-11-16 Eurobound-skjd entry. Full proposal and the EarthBound comparison:
> `docs/superpowers/specs/2026-11-16-Eurobound-skjd-proposal.md` (sections 3, 4 and 5).
>
> This doc records the approved option and nothing more. Every **[author]** item is open and stays
> blank or off in the build until the author rules it. No enemy, place, line or number is added here.

## 1. Where it comes from

- Game loop: "Explore overworld → Trigger visible encounters → EarthBound-style battle → Earn EXP, items, gear → City boss → ..." (`design/game_design_document.md:10`).
- "Encounters: visible enemies; preemptive/back attacks; auto-win vs. very weak foes" (`design/game_design_document.md:16`, `:293`).

## 2. The rules (Option A, points 1-7)

1. **Visible.** Street enemies are on the map, drawn with their overworld sprite. Each enemy doc says where it appears (its "Zone / Encounter Table") and how it moves: stands still, wanders, or walks toward the bros. Which enemy does which is per enemy doc **[author]**.
2. **Contact.** Walking into an enemy starts the fight. Whether other enemies close by join it **[author: yes/no]**.
3. **First strike.** The bros touch an enemy from behind: the bros act first for one round. An enemy touches the bros from behind: the enemy acts first for one round. Otherwise normal Speed order (`battle_numbers_proposal.md:15`). The size of the first strike is listed open in spec section 5 item 3 **[author]**.
4. **Auto-win.** Touching an enemy the bros clearly outclass ends it on the spot: the win screen, its XP, SOVS and drops, no battle. The test compares party level to the enemy's level **[author: the gap]**. Until the XP curve is ruled (`NEXT_WORK.md:919`), auto-win is off.
5. **After a fight or a Run.** A short grace period where enemies on the map cannot start a fight **Ruled 2026-11-18: counted in steps** (walking distance; Eurobound Desk `Eurobound-iqgo-q2`, verbatim: "Count it in steps (walking distance)"). **[author: how many steps]**.
6. **Respawn.** Enemies come back when the bros leave the screen and return.
7. **Losing.** When all three bros are down: back at the last save (a FREE Wi-Fi hotspot or the hostel bed, `NEXT_WORK.md:892`, `:920`), XP and items kept, **half** of the SOVS on hand lost (Eurobound Desk `Eurobound-iqgo-q3`, 2026-11-18, verbatim: "Half, as EarthBound does"). Rounding, an implementation detail of "half" (pending author confirmation): the bros keep the rounded-up half and lose the floor, so 81 SOVS loses 40 and leaves 41. Who pays and how it is shown on screen goes to the Writers' Room for the author's approval.

## 3. What stays the same (spec section 4)

- The battle itself is unchanged: side view, rolling HP at 10 HP/s, Run, 1 HP after a won fight, lasting statuses.
- The street enemies are the ones already named (`design/worlds/debaucheryville/debaucheryville.md:157-170`) plus the living statues (`:9`). Each gets an enemy doc from `design/templates/enemy_template.md` before it is built.
- The bros are never afraid: an enemy that walks away from them is the enemy's doing; the bros never flee or avoid anything on their own.

## 4. Open for the author

From the spec (section 5) and the build (Eurobound-iqgo). Each is on the Eurobound Desk.

| # | Open item | Build state until ruled |
|---|---|---|
| 1 | Auto-win level gap, and which party level is compared (leader, lowest, average) | Off (`AUTO_WIN_LEVEL_GAP = null`, `AUTO_WIN_PARTY_LEVEL = ""`) |
| 2 | Grace period: unit RULED (steps, iqgo-q2); the NUMBER of steps is open | None (`GRACE_LENGTH = null`, `GRACE_UNIT = "steps"`). A fight still never restarts by itself: contact needs a fresh touch |
| 3 | RULED (iqgo-q3): half of SOVS on hand. Rounding (floor lost) awaits confirmation | `LOSS_SOVS_SHARE = 0.5` |
| 4 | Which named enemy appears where, how it moves, enemies per screen | No enemy placed in any location |
| 5 | First-strike size (one round acting first, as point 3 says, or EarthBound's free round) | Off (`FIRST_STRIKE_ROUNDS = null`): normal Speed order |
| 6 | Nearby enemies joining a fight | Not built (one enemy contact = its own fight) |
| 7 | Slice scope, the Green Fairy Wisp's double use, the Taproom loss, Blackout Drunk, day/night enemy sets | Not built |
| 8 | HP after a street loss; a loss before the first save | Interim: HP as every other loss in the game (`ArcadeBattle.LOSS_HP`); with no save, back to the start of the screen lost on |
| 9 | The loss wording and who takes the SOVS | Writers' Room. The battle screen shows the neutral key `BATTLE_LOSS_TEXT_PENDING` in place of the old "GAME OVER" |

## 5. Built (Eurobound-iqgo)

| Piece | File |
|---|---|
| The unruled values (all off) and the pure checks: first strike by facing, auto-win, SOVS lost | `game/battle/street_encounter_rules.gd` |
| The enemy on the map: visible, stands / wanders / walks toward the bros, reports contact | `game/characters/enemies/street_enemy.gd` |
| One per screen: contact starts the existing battle, first strike, auto-win, grace, respawn, loss | `game/worlds/shared/street_encounters.gd` |
| The loss: back to the last save's screen and spot, XP and items kept, SOVS share lost | `game/battle/street_loss.gd`, `SaveSystem.last_save_location()` |
| First strike in the battle order | `BattleCore.set_first_strike()` |
| Test screen (no real location) and tests | `game/tests/fixtures/street/street_encounter_test_screen.tscn`, `game/tests/unit/test_street_encounter_rules.gd`, `game/tests/unit/test_street_encounters.gd` |

"From behind" means in the back half of the one touched, judged on the ground plane by the way each faces (the bros by the leader's last walking direction, the enemy by its own).
