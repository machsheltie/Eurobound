# GLM — Phase 6 Synch Findings (on Kimi's break + spine + the register)

Findings register only. Each item: the rule it implements, the finding, the exact fix. Kimi applies the Kimi-file fixes; the glm_mechanics_state fixes are mine. Nothing here is a rewrite; all are targeted edits.

## S1 — break §4 reads as implementation claims, not design targets

**Rule:** editor `overnight_intoxication_law`: "the old Beer Goggles combat effect and the new intoxication tier are related concepts, not proof that the full tiered system already exists in code."
**Finding:** break §4.8 states "alcohol can dull TROUSER SNAKE without defeating it. The pill defeats it" as flat present-tense fact; §4.5 states "D5 and D6 are never overridden" the same way; §4.6 "must serialize" likewise. Correct content, wrong epistemic register — same defect the editor flagged in my enemies file (§10 "full-design-only" labels).
**Fix (exact wording):**
- §4.8 → "**DESIGN TARGET:** alcohol can **dull** TROUSER SNAKE without defeating it (q9: B); the pill and the performer route **defeat** it (author-approved)."
- §4.5 → "**DESIGN TARGET:** ordinary choices remain available through Shitfaced; D5 and D6 are never overridden."
- §4.6 → "**DESIGN TARGET:** the evening state persists across scene transitions and save/load and clears only on the next in-game morning."

## S2 — editorial cut #3 not applied in V5

**Rule:** `overnight_comedy_density` mandatory cut 3 ("extra dialogue explaining the significance of the physical consequences").
**Finding:** V5: `Barbara hands him the borrowed sweatshirt: "Keep it." No anatomy dialogue and no medical explanation.` — the second sentence is an audit note shipped as scene text. Same failure class §17.1 targets.
**Fix:** end the beat at `"Keep it."`

## S3 — "You want the purple one" is player-imperative microcopy

**Rule:** Comedy Directive §8 (microcopy), §17.5 (never translate a reference).
**Finding:** `flintstone_vitamins` inspection text: "Grape. Shaped like a dinosaur. You want the purple one." — sentence 3 reads as instruction TO THE PLAYER. The same words are Barbara's V5 line. Double delivery, second one instructive.
**Fix (recommended):** inspection text → `"Grape. Shaped like a dinosaur."` Two words cut; nobody in fiction tells the player what to take; V5 keeps Barbara's line as the single delivery. Alternative: keep the text, cut Barbara's line. Don't keep both.

## S4 — `flintstone_vitamins` usability and registration are unspecified

**Rule:** `overnight_xanax` correction 2 (reliable across save/load), correction 4 (real opportunity to obtain AND consume before D5).
**Findings:**
1. §8 items table: "Consumable" with `heal_hp: 0`/`heal_bravado: 0` — but no `usable: true` statement. Shipped `use_item()` consumes what it accepts; an unspecified/zero consumable is destroyed on use with no contract, or is dead inventory. The pill must be explicitly `usable: true` and its consumption IS the trigger that sets the until-morning state.
2. §8 has no registration row for the pill (the buttons have their table; the pill doesn't land in the §2.2-style registration list).
3. The expiry contract must name the persistence key and its clear condition (next in-game morning), not "reliably" as an adjective.
**Fixes:**
- §8 items table row: `Consumable; usable: true; heal_hp: 0; heal_bravado: 0; quest effect only — consumption sets the until-morning state`.
- Add registration row: `flintstone_vitamins` | consumables.json | usable, zero-heal consumable | read by D6 staging, morning Bradley staging, and the until-morning suppression reader.
- Expiry contract one-liner: `sinfonia.ovation.flintstone_xanax_active` set on use; read by D6/morning staging; **cleared by the next in-game morning transition, never by scene exit or dialogue end.**

## S5 — §6 branch table says alcohol rows "expire" — a defeat word (§17.7 report, exact fixes)

**Rule:** canon status text "persists for the remainder of the evening unless suppressed by substantial alcohol"; q9: B; editor `overnight_xanax`: alcohol never defeats it.
**Finding:** §6 rows put alcohol outcomes in a box reading **"expires at evening's end"** (decline row; accept/no-vitamin/stay row). "Expires" = the status ends on its own = the prohibited defeat outcome, stated as the table default. Also contradicts §4.8's own dull/defeat language one section up.
**Fixes (exact lines):**
- Both affected cells: "expires at evening's end" → **"dulled; never defeated (q9: B); status text expiry (end of evening)"**
- Line under the table: "D3B alcohol never independently clears the status" → **"D3B alcohol dulls only (q9: B); it never clears the status; expiry follows the status text, never a defeat condition."**

## S6 — venue-hours math: last pour 00:45 vs. a 00:50 toast; decline geography

**Rule:** venue hours canon 16:00–01:00, last pour 00:45 (`the_standing_ovation.md`); editor `overnight_timing`.
**Findings:**
1. §1 clock: Green Room toast at 00:35–00:55 lands after last pour. A beer toast at 00:50 breaks canon hours. Also "By 01:00 Everyone leaves" reads like the venue is open until 01:00 for stragglers; the exit should be ≤00:55.
2. The decline path never touches the 00:35 stage door, but §6's decline row and §7's header don't say where the decline ending happens relative to the door (it's: street ending at D4 → hostel; the door only exists on the accept path).
**Fixes:**
- §1 exit row: "**By 00:55** the party and performers clear the venue (canon hours 16:00–01:00, last pour 00:45)."
- Toast: either stage V1 ≤00:45, or keep the 00:50 toast and add Chelsea's flat line — **"It's last pour." / PILSNER: "We've been here since eleven."** — one line, no explanation. (Recommended: the joke; the constraint becomes a beat instead of a chore.)
- §6 decline row + §7 header: add "decline = complete street ending at D4 → hostel; the stage door at 00:35 exists only on the accept path."

## S7 — `inauguration_held` reader retention is soft, and the decree placement is late

**Rule:** `overnight_catastrophe` ("consequence appears in the next morning's environment or dialogue"); §14-grade edge cases: save/load anywhere must not orphan the reader.
**Finding:** reader column says "retained at least until the morning scene has read it" — soft, and the decree/sash placement currently sits at V4/V5 while the save can happen at V3.
**Fixes:**
- Place the fridge decree and pillowcase sash at **V4** (the morning scene's first beat), so any save point ≥V3 still renders them.
- Reader column → "Fridge decree and sash at V4; retained through the apartment morning scene; cleared by the morning scene's exit."

## S8 — one flag, two jobs: `afterparty_completed`

**Rule:** the editor's own flags principle (a flag registers only with an out-of-scene reader; two jobs = desync risk, the exact disease flagged in glm_mechanics_state §2).
**Finding:** `afterparty_completed` gates BOTH the morning scene's availability AND next-day callbacks outside the apartment. One boolean doing scene-routing and callback-flagging.
**Fix (either, Kimi picks):**
- (a) Add `sinfonia.ovation.morning_available` set at V3; `afterparty_completed` becomes callbacks-only. Two flags, one job each.
- (b) Keep one flag and write the reader list explicitly in §8 ("morning scene availability; decline exclusion; next-day callbacks") — which §8 already has — and accept the coupling, recorded as accepted risk.
Recommendation: (b) — the flag count discipline the editor imposed is worth more than the desync risk on a single linear morning.

## S9 — glm_mechanics_state §2.3 lacks the ICQ window row

**Rule:** `overnight_xanax` correction 4 (the pill route must be real and reachable before D5); `remaining_continuity_errors` #2 (count must include all flags).
**Finding:** §2.3's per-decision map covers D1A–D4; no row tells the implementer the ICQ window is reachable on ALL THREE D3 outcomes (not only the paid D3B) and what its engine contract is.
**Fix (mine, this round):** add §2.3 row —
> **ICQ window (after TROUSER SNAKE lands, before D5):** reachable after any D3 outcome; requires MoonCum balance + `has_inspected_first_crypto_trash` (AD-04 prerequisite); purchase = crypto debit (−50 MoonCum696969), no gold, no item grant at purchase; `add_item("flintstone_vitamins")`; consumption on use sets `flintstone_xanax_active` (until next in-game morning).

**Also mine:** glm_mechanics_state §2 flag table gains the five overnight rows (Kimi's break §8) under a subsection labeled per ruling `glm_mechanics_state` update 5, and the §9 "open author decisions" list loses item 1 (the intoxication question is resolved by the author's law + Appendix A; the spec file this round records it).

## S10 — non-blocking note, no fix: the evening-tier state has no home in §2.3 either

The evening tier (Buzzed→Beer Goggles→Shitfaced→Catastrophe) is quest-scoped serialized state per the break §4.10, but §2.3's map doesn't name where it increments (staged Act II beats + afterparty override). One sentence needed in the spec this round; no break edit required.
