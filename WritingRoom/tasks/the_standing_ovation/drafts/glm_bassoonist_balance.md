# GLM — Bassoonist Balance Verification (Editor Ruling #5, fix 06)

**Mandate:** replace Appendix B6's TBD row with a real turn-by-turn verification for the **solo-Pilsner build** against the **Second Chair Bassoonist (34 HP / off 7 / def 3 / speed 4 / luck 4)** and its **Union Break adds — Tympanist on Break (16 / 4 / 2 / 3) and Overworked Oboist (18 / 3 / 2 / 5)** — accounting for each summon, its arrival turn, the Bassoonist's attack rhythm, target selection, and self-inflicted damage. No enemy redesign: cracked reed, Low C prep, union reinforcements all stand.

**Result up front: a valid route exists on the current spec. The row is no longer TBD.** The smallest spec change needed is one anchor sentence (§6 below), which restores Aion's own authored timing rather than altering the enemy.

---

## §1 Conventions (identical to the §8 tables already in final.md)

- **Build:** shipped solo Pilsner — HP 45 / offense 8 / defense 6 / luck 4 / Bravado 12; skills: Bash, Roast Line (×1.8, cost 4 Bravado).
- **Formula:** `damage = (offense×2 − defense) × multiplier ± 2, floor 1; crit = attacker luck × 1%, ×2.` Player attacks do not miss; enemy crits are noise-level (luck ≤ 4) and priced in §7.
- **Turn order:** the §8 convention is player-first per round. Sensitivity check: if the Bassoonist acts first instead, the expected-case kill still lands before his second activation completes, and the worst case (§4) is priced with the summon already out — the verdict is robust to either order.
- **Two cases reported:** the **expected case** (average rolls, reed misses priced at their probability) and the **worst case** (every enemy attack hits, every player roll at minimum). If the worst case wins, the fight is safe by construction.

## §2 One-shot damage values

| Attacker → target | Formula | Range | Avg |
|---|---|---|---|
| Pilsner Bash → Bassoonist (def 3) | (16−3) | 11–15 | 13 |
| Pilsner Roast → Bassoonist (def 3) | 13 × 1.8 | 21–25 | 23 |
| Pilsner Bash → either add (def 2) | (16−2) | 12–16 | 14 |
| Bassoonist regular → Pilsner (def 6) | (14−6) | 6–10 | 8; 25% built-in reed miss, +10% per taunt |
| Bassoonist **Low C** → Pilsner | armor-piercing (14) | 12–16 | 14; then **Sharp** (off −2, 3 turns) |
| Bassoonist after Sharp → Pilsner | (10−6) | 2–6 | 4 |
| Tympanist thump → Pilsner | (8−6), floor | 1–4 | 2 — **30% of the time it hits himself for ~6 instead** (E ≈ 1.8 self-damage/turn) |
| Oboist → Pilsner | (6−6) → floor 1 | 1 | 1; her one **Embarrassed** lecture (no damage, −20% offense + no taunt, 2 turns) is full-design-only |

## §3 Recommended route — burst the summon (expected case)

Aion's authored trigger (Phase 4 draft, carried intent): **"On his second turn, he signals"** — Union Break consumes his turn, so the summon happens at his second activation and not before. Two Pilsner actions arrive before that activation completes.

| Turn | Pilsner | Bassoonist HP | Enemy action | Pilsner HP |
|---|---|---|---|---|
| T1 | **Roast Line** (23) — also the taunt: reed miss now 35% | 34 → 11 | Regular attack: 8 avg × 0.65 hit = **E 5.2** | ~40 |
| T2 | **Bash** (13) | 11 → **dead before his second activation** | — Union Break never fires; **the adds never exist** | ~40 |

**2 turns, ~5 damage taken, no heal, no items.** Both signature moves are denied by the same two turns: no Low C inhale gets to complete, and the union never convenes. The century's representative is fired before he can call the break — on-premise, and exactly the counterplay the kit already advertises for the inhale.

**Bravado:** 4 of 12. **Key-click:** never fires — no items used.

## §4 Worst case (low rolls, no reed misses, no player crits)

Minimum opening: Roast 21 + Bash 11 = 32 < 34. He survives his second activation at ~2 HP and the break fires.

| Turn | Pilsner | Board | Enemy actions | Pilsner HP |
|---|---|---|---|---|
| T1 | Roast (21) | B 13 | B hits 10 (no reed miss) | 35 |
| T2 | Bash (11) | B ~2; **Union Break: Tympanist + Oboist arrive** (consumes his turn) | — | 35 |
| T3 | **Bash Bassoonist** (11 min) — he is the only real threat; correct targeting | B dead. Adds' first actions | Tympanist 2 + Oboist 1 | 32 |
| T4 | Bash Tympanist (12 min) | Ty 4 | Oboist spends her one Embarrassed lecture (no damage); Ty 2 | 30 |
| T5 | Bash Tympanist, offense −20% (~9–13) | Ty dead | Oboist 1; Ty thump 2 or self-hit | ~28 |
| T6 | Bash Oboist (12–16) | 2–6 left | Oboist 1 (zero-effect criticism now) | ~27 |
| T7 | Bash Oboist | **dead** | — | ~27 |

**≤7 turns, ≤19 damage vs 45 HP — wins with no heal in every case.** The adds are 2-and-1 furniture; the Tympanist is the fight's leading scorer against his own side. If the Embarrassed lecture ships inert on the four-button build (it should — same label as `spare_reed`'s cure), the worst case gets *shorter*, not longer.

## §5 Zero-Bravado exit (Bash-only, for the scarcity ledger)

Bash ×3: 13+13+13 = 39 ≥ 34 (summon fires at his T2 as above, adds out), then two-to-three more turns of 14-avg Bashes clear 16 and 18 HP. ~6–7 turns, ~15–20 taken. **Wins, no heal** — the encounter keeps the zero-Bravado exit every slot in this roster carries.

## §6 Spec notes (no redesign; one anchor)

1. **Pin the summon turn.** Neither final.md B3 nor glm_enemies_full §3 states *when* Union Break fires; Aion's authored Phase 4 text does. Add to the B3 kit: **"Union Break fires on his second turn, one use per encounter."** This is a restoration of the concept author's own timing so the verification is reproducible — the sentence the whole denial route (and this row) hangs on. Flag for **Aion to confirm**; it is his enemy.
2. **Label the Oboist's Embarrassed lecture full-design-only**, matching the existing `spare_reed` treatment: on the shipped four-button build it degrades to her zero-effect breath-support criticism. No row values depend on it.

## §7 Residual noise

Bassoonist luck 4 → 4% crit ×2: at most +8 on one hit, ~once in 25 fights. Against a 26-HP worst-case margin, irrelevant. Tympanist self-hit expectation (−1.8/turn on a 16-HP add) is already excluded from the worst case, so it only shortens fights.

---

## The replacement B6 row (existing column format)

| B | Bassoonist + Break adds | 34+16+18 HP | Roast T1 (taunt) → Bash T2 — the kill denies Union Break | 2 expected; ≤7 worst case | ~5 expected; ≤19 worst | Wins, no heal. If low rolls keep him alive at ~2 HP the break fires; the adds hit for 2 and 1, and the Tympanist mostly hits himself. Bash-only route: ≤7 turns, ~20, still no heal |
