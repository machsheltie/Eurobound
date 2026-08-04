# City Progression Order & Backtracking — CANON

**Status:** Canon — author rulings 2026-08-01 and 2026-08-03. **This was previously undocumented**, which is why cross-city timing kept being guessed at. Record additions here rather than in location files.

---

## 🚨 THE ORDER

> **Publandia → Debaucheryville → Sinfonia → Shamsterdam**

That is the **first-playthrough** sequence. It is not a cage.

---

## 🔄 BACKTRACKING IS SUPPORTED — READ THIS BEFORE ASSUMING ANYTHING

> **"Like many RPGs, players can return to other cities after their first playthrough, and so ending up in Shamsterdam does not mean it's the end of the road — players can go back, and at times I may add content that does actually require going back when we talk about the main storyline. So nothing is off-limits as far as getting the Coin or the Herp. Nobody is automatically assumed clean and free and clear. There is no order on when each couchsurfer has to be gotten to."**
> — Author, 2026-08-03

**Cities remain open. The player can return to any city at any time.** Main-storyline content may itself require going back.

### What this means for every author

| ❌ Never write | ✅ Because |
|---|---|
| "The party is clean in this city" | A returning player may arrive infected |
| "The Coin is unobtainable here, so State 3/4 can't happen" | They can go get it and come back |
| "This is the last city, so this state is terminal" | Nothing is terminal; they can leave and return |
| "By this point the party will have X" | No progression gate guarantees anything |
| "This host must be attempted before/after Y" | There is no couchsurf ordering |

**The single rule: every location, host, and scene must support every state, at all times.** No per-city special cases, no unreachable states, no assumed party condition.

---

## `the_herp` — all three states are reachable everywhere

Both the infection and the cure are **optional sidequests** (`Design/design_optionality_principle.md`), and backtracking makes both reachable from anywhere at any time.

| State | How reached |
|---|---|
| **No Herp** | Never attended the Bacchanus Beach party (Debaucheryville) |
| **Herp active** | Attended the party; has not obtained the Gold Circle Coin |
| **Herp suppressed** | Holds the Coin (Haute Couture Haberdashery, Sinfonia), equipped by any bro |

- Caught at the beach party: scripted, guaranteed, party-wide, immediate and permanent — **but only if the player attends.**
- Suppressed, never cured. The status stays in the list permanently, greyed, tagged SUPPRESSED.
- **A player may decline the Coin forever** and be refused by every couchsurf host for the rest of the game. That is an intended playstyle, not a failure — see `nothingisgettingthrough.md` → "The Permanently Infected Playthrough".
- **Publandia being first does not make it a clean city.** A returning player can arrive there in any of the three states.

---

## Binding rules for contributors

1. **`the_herp` is the game's ONE and ONLY STD.** No location, quest, or NPC may introduce a second. A second infection makes STDs ambient background instead of THE event and undercuts the Coin's payoff. *(Author ruling 2026-08-01 — one was drafted for Roodelicht Row and cut.)*
2. **Never assume a Herp state anywhere, in any city, at any point.** Branch, or do not reference it.
3. **Never write a temporary suppressant**, reduced-severity state, cream, potion, vendor cure, or cooldown. There is none, by design — the Coin must feel Excalibur-tier.
4. **Never gate content on progression order** without checking here first. Backtracking defeats most such assumptions.
5. **Couchsurf hosts have no required order** and every host supports all four Chronicles states at all times (`Design/Quests/couchsurfingchronicles.md` → "THE FOUR STATES").

---

## Correction log

- `shamsterdam.md` once carried a "To Sinfonia" cross-city section implying Sinfonia came after Shamsterdam. Wrong; rewritten to "From Sinfonia".
- Earlier drafts of this file left Publandia's position unconfirmed and treated Debaucheryville as first. Publandia is first.
- Earlier routing notes claimed States 3/4 were unreachable in Publandia and that Shamsterdam's State 2 was terminal. **Both wrong** — backtracking makes every state reachable in every city.

**Cross-references:** `Design/design_optionality_principle.md`, `Design/Quests/couchsurfingchronicles.md`, `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`, `Design/Inventory/items/gold_circle_coin_item.md`.
