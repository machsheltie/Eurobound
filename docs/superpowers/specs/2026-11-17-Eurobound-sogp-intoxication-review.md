# Intoxication-Law Review: Chug & Shrug, Hop-Chi Heal, Final Round's On Me (Eurobound-sogp)

> **Status: REVIEW, waiting on the author** (Eurobound Desk `Eurobound-sogp-q1`).
> Binding law: `design/mechanics/intoxication_law.md` §8 (the 10-point review) and `design/narrative/bros_choose_debauchery.md`
> ("Intoxicants do not provide uncomplicated, consequence-free advantages. Any apparent benefit should be temporary, deceptive,
> compromised, or accompanied by an entertaining drawback.").
> Model: `design/mechanics/Battle/status_entries/foam_fighter.md` (Eurobound-tcip).
> Nothing in `game/` or `design/` was changed. **No number, drawback, line or mechanic is proposed here.** Every value not
> already in canon is **PENDING**; every point that needs the author is marked **RULING** and is asked on the Desk.

Audience: younger Gen X, xennial and millennial women. All three moves are Lord Pilsner's; the joke the law asks for is the
gap between what he thinks the beer is doing for him and what it actually does.

## 0. Where these moves sit

| Move | Rung (028k proposal, not yet approved) | Source |
|---|---|---|
| Chug & Shrug | Alumni (300 Clout), "first self-heal" | `docs/superpowers/specs/2026-11-17-Eurobound-028k-progression-numbers-proposal.md:197` |
| Final Round's On Me (Ultimate) | Legacy (600 Clout) | same file `:198` |
| Hop-Chi Heal | Living Legend (1,000 Clout) | same file `:199` |

None is in the Debaucheryville slice (028k §5: nobody reaches Legacy there; Alumni comes at the boss). This review runs
before each move's numbers round, as 028k §8 (`:277-280`) asks.

`design/mechanics/Progression/skilltrees_cloutspells.md` does not name any of the three moves (grep: no hit for Chug,
Hop-Chi or Final Round). Its only related line is a rung reward, "1000 Clout: 'Honorary Irishman' - All beer-based abilities
double effectiveness" (`:105`); that doc is not approved as written (`NEXT_WORK.md:919`), so it is noted under point 8 and
not ruled on here.

## Shared ground (all three moves)

| Fact | Source |
|---|---|
| Ladder tiers are Buzzed → Beer Goggles → Shitfaced → Catastrophe, **per bro** | `intoxication_law.md:145`; ledger f3tq-q4 "Per bro" (`NEXT_WORK.md:950`) |
| Tier mapping: "Buzzed = slightly worse options, Beer Goggles = judgment overrides, Shitfaced = guaranteed embarrassment, Catastrophe stays the worst" | f3tq-q1 (`NEXT_WORK.md:950`) |
| Ladder thresholds and decay are not ruled; the ladder is not built | Eurobound-p0j (deferred); `NEXT_WORK.md:950` |
| Drunk events "never fire in battle" | `docs/superpowers/proposals/2026-11-13-drunk-judgment-and-folklore-proposal.md:90` (shape approved, f3tq-q3) |
| Drink tag: "every alcoholic drink and beer ... counts as 'a drink' for the clock's 10 minutes" | Round v37 (`NEXT_WORK.md:713`) |
| Bravado is fed by drinking: it drains through "Sobriety creep (time passage without drinks)" and regens from "Winning drinking games/minigames" | `design/mechanics/Battle/bravado.md:14`, `:18` |
| Bravado bands: Zero = "Bravado moves unavailable"; Low (≤25% of max) = "Ultimates locked out"; Mid; High (flavor only) | `docs/superpowers/specs/2026-08-06-bravado-consolidation-design.md:71-76` |
| Embarrassed (ruled): −20% ATK, −2 Bravado a turn, locks Bravado-cost moves, Ultimates and Taunt; 2 turns | `bravado.md:21`; v27, v28, g0jr-q3 |
| Pilsner today (v26): HP 45, max Bravado 12 | `game/assets/data/party/party_members.json`; 028k §1 |
| Hungover (approved): all stats −2, 25% skip chance; cured by time, Advil or greasy food; battle length unruled (3-5 flagged) | `game/assets/data/skills/status_effects.json` `hungover` (vdrt-q2); Eurobound-81un |
| Sloppy (approved): −3 accuracy steps; length unruled (1-2 flagged) | `status_effects.json` `sloppy` (vdrt-q2) |
| Liquid Confidence (approved): +3 Charm, −1 accuracy step; length unruled (3-5 flagged) | `status_effects.json` `liquid_confidence` (vdrt-q2) |
| Stun: "loses the next turn and doesn't stack" | `game/battle/battle_rulings.gd:27` (ef4_confused_stun) |
| Engine skills today: one enemy hit (with an optional `inflict` status roll) or a buff on another bro (`target: "other_bro"`). No heal, no Bravado restore, no self or party target, no all-enemies target, no Ultimate effect | `game/battle/battle_core.gd:245-250`, `:461-494`; `game/assets/data/skills/party_abilities.json` |

**Shared RULING X1: do these moves count as drinks on Pilsner's ladder?** Each one is built on a beer in battle. If a
move counts as a drink, it moves Pilsner up his own ladder (per bro, f3tq-q4) and, by the v37 drink tag, may also move the
clock. If it does not, the move is a Keg-Fu technique that only *looks* like drinking, and the law's review applies only
in part. The source lines do not say.

---

## 1. Chug & Shrug (Lord Pilsner)

**Source, verbatim** (`design/mechanics/Battle/battle_system.md:264`, Lord Pilsner's Core Abilities):

> • Chug & Shrug — Heals HP and restores partial Bravado.

No other doc gives it a different effect (catalog `docs/catalog/status_effects_and_abilities.md:20` copies the line).

### What the bro thinks vs what he gets (`bros_choose_debauchery.md:24`)
- **Thinks:** a beer fixes everything; he shrugs off the hit.
- **Actually gets, per the source:** HP and some Bravado back. **Nothing else.** As written there is no gap, so there is no joke
  and no drawback.

### No Free Advantage
As written, Chug & Shrug **fails** the test: a heal plus a Bravado restore with no drawback, no chance of failure and no
cost stated. **RULING C3: what is the catch** (or is it not an intoxicant move, X1)? Existing canon that the author may
choose to point at, listed as facts, not as proposals:
- Chug of the Gods, Pilsner's older skill-tree heal: "heal self/allies; small chance 'Sloppy' debuff −Accuracy 1 turn"
  (`design/characters/LordPilsner/lordpilsner.md:20`). That tree is not approved (028k §1).
- Double Chug's failure: "puke → AoE stun allies" (`battle_system.md:204`; `:77`, `:157`).
- Sloppy and Hungover already have approved effects (Shared ground).

### 10-Point Design Review (`intoxication_law.md` §8)
| # | Point | Answer |
|---|---|---|
| 1 | Source item or drink | Unnamed. "Chug" names the act; no beer, item or inventory cost is given. **RULING C1:** is a real beer drunk, and does it come from inventory (an item cost) or from nowhere (a Bravado move)? Counts as a drink: **X1**. |
| 2 | Immediate effect | "Heals HP and restores partial Bravado" (canon). Who it heals: **RULING C2** (028k calls it a "self-heal", `:197`; the source does not say self, one ally or the party). Amounts, Bravado cost (if any), cooldown: PENDING numbers round. |
| 3 | Escalation conditions | None in the source. If it counts as a drink (X1), each use climbs Pilsner's ladder (thresholds: Eurobound-p0j). Whether repeat uses in one battle change anything: PENDING. |
| 4 | Visible player-facing cues | None in the source. PENDING (art, animation, battle line; `battle_text` is a Writers' Room line). |
| 5 | Effect on player control | None in the source. Any loss of control comes only from the drawback the author picks (C3); it must be bounded and readable (law §7). |
| 6 | Duration and recovery | Instant heal and restore (source). Any drawback's length and cure: with **C3**. |
| 7 | Comedic consequence | **None in the source**, which is the problem C3 must fix. The name promises a shrug-off; the consequence is unwritten. Bro lines: PENDING (author / Writers' Room). |
| 8 | Interaction with other established statuses | Embarrassed locks Bravado-cost moves: if Chug & Shrug has a Bravado cost, an Embarrassed Pilsner cannot use it. Hungover: does the chug touch it (hair of the dog), or does it stack? **RULING C4.** Cottonmouth locks *spoken* skills (`battle_core.gd:233-234`); a chug is not spoken unless ruled. Sloppy / Liquid Confidence: only if C3 uses them. Ladder: X1, Eurobound-p0j. |
| 9 | Technical implementation dependencies | Proposed engineering work, none built: a skill-side HP heal and Bravado restore (items have `heal_hp` / `heal_bravado`, `battle_core.gd:300-301`; skills do not); a self or party target (skills reach only enemies or `other_bro`, `:245-250`); a ladder hook if X1 says it counts (ladder unbuilt, p0j); the drawback status roll on the user (today `inflict` rolls only on a hit enemy, `:484-489`). |
| 10 | Requires further author approval? | Yes: X1, C1, C2, C3, C4, and every number. |

---

## 2. Hop-Chi Heal (Lord Pilsner, Keg-Fu)

**Source, verbatim** (`design/mechanics/Battle/battle_system.md:297`, Lord Pilsner — Keg-Fu):

> • Hop-Chi Heal — Restores % HP based on missing Bravado (the drunker, the stronger).

Catalog copy: `docs/catalog/status_effects_and_abilities.md:28`. No other source.

### The conflict inside the line
The parenthetical treats **missing** Bravado as being **drunker**. Canon Bravado runs the other way: it drains through
"Sobriety creep (time passage without drinks)" and regens from "Winning drinking games/minigames" (`bravado.md:14`, `:18`),
so a bro low on Bravado is, by that doc, the *soberer* one. The ladder (Buzzed → Catastrophe) is a separate, per-bro track.
**RULING H1: what does Hop-Chi scale on?**
- missing Bravado only (the parenthetical is a joke, not a rule; the move is then not an intoxicant move),
- Pilsner's ladder tier (the move is a drunk-boxing heal, and the law applies in full),
- or both.

### What the bro thinks vs what he gets
- **Thinks:** the drunker he is, the more ancient beer chi flows through him.
- **Actually gets:** depends on H1. The source gives no drawback.

### No Free Advantage
- If H1 = ladder tier: the heal *rewards* being drunk. That is exactly an intoxicant giving an advantage, so it needs a catch
  (**RULING H3**).
- If H1 = missing Bravado: the "cost" is being low on Bravado, which already locks Ultimates at ≤25% (consolidation §3).
  Whether that counts as the drawback, or the move needs its own: **RULING H3**.
- Edge the numbers round must face: Zero Bravado makes "Bravado moves unavailable" (consolidation `:73`). If Hop-Chi costs
  Bravado, it can never be used at its strongest point (0 Bravado); at Pilsner's max of 12, its peak is at 1 Bravado.
  Whether it costs Bravado at all: **RULING H2**.

### 10-Point Design Review
| # | Point | Answer |
|---|---|---|
| 1 | Source item or drink | None named; it is a Keg-Fu spell (`battle_system.md:293-299`). Whether he drinks anything: with **H1** and **X1**. |
| 2 | Immediate effect | Restores a % of HP that grows with missing Bravado (canon). Whose Bravado and whose HP (Pilsner's own, the target's, the party's): **RULING H2**. The % curve, cap and cost: PENDING numbers round. |
| 3 | Escalation conditions | The heal escalates as Bravado falls (canon); or as the ladder climbs (H1). Beyond that, none in the source. |
| 4 | Visible player-facing cues | None in the source. The Bravado bar already shows how much is missing. If H1 uses the ladder, the tier needs a battle cue, and no battle cue for ladder tiers exists (p0j). PENDING. |
| 5 | Effect on player control | None in the source. The player picks when to cast. Any control loss comes only from a drawback (H3). |
| 6 | Duration and recovery | Instant heal (source). Any drawback's length and cure: with **H3**. |
| 7 | Comedic consequence | From the source: Pilsner heals best when he is at his most pathetic. The joke needs the drawback to land; PENDING with H3. Bro lines: PENDING (author / Writers' Room). |
| 8 | Interaction with other established statuses | Embarrassed drains 2 Bravado a turn, which would *raise* Hop-Chi's heal, but also locks Bravado-cost moves, so whether he can cast it while Embarrassed depends on H2's cost. Bravado Flex (+3) lowers the heal. Low band (≤25%) locks Pilsner's Ultimate: his two heals compete for the same Bravado. Hungover (all stats −2): no stated interaction; if H1 uses the ladder, does a Hungover bro count as drunk? **RULING H4.** |
| 9 | Technical implementation dependencies | Proposed engineering work: a skill heal scaled by `max_bravado - bravado` (the engine tracks both, `battle_core.gd:632-633`), or by ladder tier (unbuilt, p0j); self or party target (skills reach only enemies or `other_bro`). |
| 10 | Requires further author approval? | Yes: X1, H1, H2, H3, H4, and every number. |

---

## 3. Final Round's On Me (Lord Pilsner's Ultimate)

**Source, verbatim** (`design/mechanics/Battle/battle_system.md:299`; ruled canon by Eurobound-40ym, `NEXT_WORK.md:927`, "No
upgrades or numbers are ruled for the canon Ultimates yet"):

> • Final Round’s On Me (Ultimate) — Slams entire keg, restoring allies’ Bravado + HP, while stunning enemies in AOE “beer flood.”

The same words are in `design/characters/LordPilsner/lordpilsner.md:7`, `:29` and `bravado.md:52`.

### What the bro thinks vs what he gets
- **Thinks:** the hero buys the whole bar a round and wins the fight.
- **Actually gets, per the source:** HP and Bravado for the allies and a stun on every enemy. **No catch.**

### No Free Advantage
As written it **fails**: party heal, party Bravado and an all-enemy stun with no drawback. The other two canon Ultimates
both carry one: Fratocalypse Now, "If it fails? Bradley passes out → Hangover debuff next turn" (`battle_system.md:283`);
Going Viral, "2–4x ... depending on RNG" (`:291`). **RULING F3: what is Final Round's catch?** (Facts the author may point
at: Fratocalypse's fail-into-Hangover pattern; the approved Hungover status, Shared ground.)

### 10-Point Design Review
| # | Point | Answer |
|---|---|---|
| 1 | Source item or drink | "Entire keg" (canon). **RULING F1:** does Pilsner *drink* the keg (it hits his ladder hard) or *slam it down* so it bursts into the "beer flood"? Do the allies drink from it (their own ladders, per bro)? Is the keg an inventory item the party must carry, or free? Counts as drinks: **X1**. |
| 2 | Immediate effect | Allies regain Bravado and HP; enemies in the area are stunned (canon). Whether "allies" includes Pilsner: **RULING F2**. Stun is "loses the next turn and doesn't stack" (ef4); whether every enemy is stunned or each rolls a chance: **RULING F4**. Amounts, Bravado cost: PENDING numbers round. |
| 3 | Escalation conditions | None in the source. If F1 says Pilsner drinks a whole keg, one cast is many drinks at once (how many: with X1 and p0j). |
| 4 | Visible player-facing cues | "AOE 'beer flood'" (canon): a full-field beer effect. Animation, screen effect and battle line: PENDING. A full-screen flood needs the law §7 reduced-motion alternative if it shakes or distorts the screen. |
| 5 | Effect on player control | On the enemy side, a stun (bounded: one lost turn, no stacking). On the party side, none in the source; any loss comes from F3. |
| 6 | Duration and recovery | Heal and restore are instant; stun is one turn (ef4). Any drawback's length and cure: with **F3**. Ultimate is locked at Zero or Low Bravado and while Embarrassed (consolidation §4; ruled Embarrassed). |
| 7 | Comedic consequence | From the source: his big moment is buying a round nobody asked for and drowning the room in it. The consequence that makes it a Eurobound joke (F3) and bro lines: PENDING. |
| 8 | Interaction with other established statuses | Embarrassed locks it (ruled). Low band locks it (consolidation §4). It restores allies' Bravado, so it can lift an ally back out of Low or Zero. Does the flood touch statuses: cure or extend Hungover, cause Sloppy, end Embarrassed? Source silent: **RULING F5**. Enemies already stunned: stun doesn't stack (ef4). 028k's Legacy Embarrassed (−3 a turn, proposed) is the rung this opens on. "Honorary Irishman" doubling "beer-based abilities" (`skilltrees_cloutspells.md:105`) is unapproved; not ruled here. |
| 9 | Technical implementation dependencies | Proposed engineering work: Ultimates have a gate (`is_ultimate`, consolidation §4) but no effect in data (Eurobound-g0jr); party-wide heal and Bravado restore; all-enemies status apply (today `inflict` reaches one hit target, `battle_core.gd:484-489`); keg item cost if F1 says so; ladder hook if X1 says so (p0j); a reduced-motion alternative for the flood. |
| 10 | Requires further author approval? | Yes: X1, F1, F2, F3, F4, F5, and every number. |

---

## 4. Shotgun Flex and Shotgun Ritual (Bradley): the reading check

The bead asks whether "shotgun" means shotgunning a beer. What the docs say:

| Move | Line, verbatim | Drinking? |
|---|---|---|
| Shotgun Flex | `battle_system.md:227`: "Shotgun Flex — Burns 1/3 Bravado bar for guaranteed crit." | No source says so. No other doc names it. |
| Shotgun Ritual | `battle_system.md:282`: "Shotgun Ritual — Sacrifices 25% Bravado for guaranteed crit + AOE splash." | Not in this line. |
| Shotgun Ritual | `bravado.md:59`: "Shotgun Ritual — Drinks and hurls can; big damage but self-Bravado drain." | **Yes.** |

So Shotgun Ritual has **two different effect lines** in two current docs, and one of them says Bradley drinks. The 028k
table uses the battle_system.md line (`:219`). **RULING S1:** (a) is Shotgun Flex a beer shotgun? (b) Which Shotgun Ritual
line is canon, and is Ritual a drinking move? Any move ruled a drinking move gets the same 10-point review before its
numbers round. Both already carry a cost (Bravado burned), which the review would weigh against the no-free-advantage test.

---

## 5. All RULING points (asked on the Desk as `Eurobound-sogp-q1`)

| Id | Question |
|---|---|
| X1 | Do these moves count as drinks on Pilsner's own ladder (and the clock's drink tag), or are they techniques that only look like drinking? |
| C1 | Chug & Shrug: is a real beer drunk, and from inventory or from nowhere? |
| C2 | Chug & Shrug: who it heals (self, one ally, the party). |
| C3 | Chug & Shrug: its catch. As written it fails no-free-advantage. |
| C4 | Chug & Shrug and Hungover: does it touch it, or stack? |
| H1 | Hop-Chi Heal: scales on missing Bravado, ladder tier, or both? (The parenthetical contradicts `bravado.md:14`.) |
| H2 | Hop-Chi Heal: whose Bravado, whose HP, and does it cost Bravado (if so it can't be cast at 0, its peak)? |
| H3 | Hop-Chi Heal: its catch, or does low Bravado (Ultimate lockout) already pay for it? |
| H4 | Hop-Chi Heal: does a Hungover bro count as drunk for it (only if H1 uses the ladder)? |
| F1 | Final Round's On Me: drinks the keg, or slams it into a flood? Do allies drink? Is the keg an item cost? |
| F2 | Final Round's On Me: does "allies" include Pilsner? |
| F3 | Final Round's On Me: its catch. As written it fails no-free-advantage; the other two Ultimates both carry one. |
| F4 | Final Round's On Me: every enemy stunned, or a chance each? |
| F5 | Final Round's On Me: does the beer flood touch any status (Hungover, Sloppy, Embarrassed)? |
| S1 | Shotgun Flex: beer shotgun or not? Shotgun Ritual: which of its two lines is canon, and is it drinking? |

Every number (heal amounts, Bravado restored, Bravado costs, % curve, stun chance, cooldowns) waits for each move's own
numbers round, after these answers. Bro lines and battle text are PENDING (author / Writers' Room).

## 6. Filed from this review

- Engine skills cannot heal, restore Bravado, target self or the party, hit all enemies, or run an Ultimate effect
  (`battle_core.gd:245-250`, `:461-494`). Filed as its own bead (discovered-from Eurobound-sogp).
- Liquid Confidence's stale Taunt bonus in `bravado.md:22` is already filed (Eurobound-i3jo); not refiled.

## Revision History

| Date | Change | Author |
|---|---|---|
| 2026-11-17 | 10-point reviews for the three moves and the Shotgun reading check (Eurobound-sogp) | game-designer agent |
