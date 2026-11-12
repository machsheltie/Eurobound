# GLM — The Standing Ovation Intoxication Specification

**The ten-point design review required by `design/mechanics/intoxication_law.md` §8, applied to this quest.** Companion to Kimi's corrected break (`drafts/kimi_overnight_break.md` §4 supplies the narrative/state contract; this file supplies the mechanic). Editorial rulings applied: `overnight_intoxication_law` (REVISE → this document), `overnight_catastrophe`, `overnight_xanax`, `keg_acolyte_dispute`-style restraint. **Tier names are final author canon: Buzzed → Beer Goggles → Shitfaced → Catastrophe. No numerical thresholds are defined or proposed anywhere in this document.**

**Epistemic labels, same discipline as the enemies file:** SHIPPED = exists in `game/` today. QUEST-AUTHORED = staged by this quest's scenes within existing capabilities. PROPOSED = new engineering, listed in §9.

---

## POINT 1 — SOURCE

**Shitfaced-by-design sources, in narrative order:**

1. **The Producer's Circle pour (D1A).** 24 SOVS of pours on the receipt — the evening's documented alcohol floor.
2. **Venue menu drinks during the show.** The Encore and Copper Statute exist at canon prices; the party drinks through Act II. No count, no ABV — none is documented for the venue and none is invented.
3. **D3B's three Encores**, if the player bought them (30 SOVS) — the coping round.
4. **The Green Room toast** — the unmarked bottle (V1, §9 of the break). Unlabeled provenance is a joke, not a stat block.
5. **The afterparty.** Same bottle; no count is ever shown.

**What is NOT a source:** the Dramatisch Dunkel drop (a consumable reward with an HP value — an item, not an evening), and the Encores' +30 HP — the drink menu's healing value is commerce, not the intoxication system. D3B bypasses the item system entirely (glm_mechanics_state §3, exploit fix); the intoxication system likewise never routes through `use_item()`.

## POINT 2 — IMMEDIATE EFFECTS

Per tier, one behavior each — no tier grants combat, Charm, HP, gold, or Bravado advantage. The law is explicit: no uncomplicated benefits.

- **Buzzed:** dialogue options tilt toward boasting (quest-authored option text). No perception change.
- **Beer Goggles:** the perception layer switches on (Point 4) and *identity* judgment degrades — the bros' classifications inflate ("stage earpiece → Secret Service"). Existing Beer Goggles **combat** effects (−Accuracy, +Friendly Fire, from Mid-Life Crisis) are untouched and unrelated in code.
- **Shitfaced:** dialogue options degrade further and the select/deliver gap opens — what the player selects is not what the bro delivers (the existing quest-authored substitution capability, glm_mechanics_state §3.3's table, now generalized to the evening instead of D3B only).
- **Catastrophe:** exactly one scripted substitution event in this quest (Point 5). No second event exists on any branch.

**TROUSER SNAKE interaction (q9: B, ruling `overnight_xanax`):** alcohol **dulls** the status from Beer Goggles upward — the banner dims, the compromise lines lose volume; **it never ends the status and never blocks the morning-performer-route or pill outcomes.** "Dulled" is presentation only: no engine change, no duration change, expiry still governed by the status's own text.

## POINT 3 — ESCALATION CONDITIONS

**Quest-authored, not metered.** Tier advancement fires at authored beats, never at a drink count:

- Buzzed → set at the first Act II heckle (Chelsea's first applause reset).
- → Beer Goggles → set at the twins' place-switch (the first perception gloss).
- → Shitfaced → set at Barbara's instrumental hold.
- → Catastrophe → set **only** at the afterparty, immediately before the single override (Point 5).

Consequence: a player who declines every drink opportunity still rides the authored curve — the bros' evening is drinking *by premise* (bible/03: the bros choose debauchery; nobody drags them). This is the design decision this spec ratifies: **the intoxication system in this quest dramatizes the bros' night; it does not simulate the player's pours.** The player's only intoxication-relevant *decision* with mechanical teeth is D3B's 30 SOVS (dulls harder — the banner dims further), and the pill/performer TROUSER SNAKE outcomes.

**Never descends.** No coffee, food, or water interaction lowers a tier mid-evening. The tiers clear in one place only (Point 6).

## POINT 4 — VISIBLE PLAYER-FACING CUES

1. **Tier label** — the status-tray chip reads BUZZED / BEER GOGGLES / SHITFACED. CATASTROPHE is deliberately *not* shown as a chip; the player experiences it as the override, not as a label they could brace against. (Ruling `overnight_catastrophe`: the system makes clear a Catastrophe decision has occurred — via the substitution banner, not via a pre-warning.)
2. **Dialogue options** mutate per tier (Point 2). This is the primary legibility channel and is QUEST-AUTHORED on shipped capability.
3. **Sprite behavior:** idle sway on the bros at Shitfaced; Pilsner's table-climb pose at the override. Sprite work is PROPOSED asset work (Dependency 11), not a code claim.
4. **The perception gloss (Beer Goggles visual):** ONE device — the campaign-news treatment. Bunting at the stage edge, the `LIVE — ELECTION NIGHT 2000` lower-third, the earpiece-as-Secret-Service read, the afterparty `BREAKING` chyron. **Reuses the existing Beer Goggles overlay rendering approach** from `design/Quests/debaucheryville/nothingisgettingthrough.md` and the Mid-Life Crisis debuff's visual language. **Explicit non-claim:** neither of those is a party-wide intoxication system in code; the debuff is an enemy-targeted combat effect and the Debaucheryville overlay is that quest's scripted presentation. This quest's gloss is QUEST-AUTHORED per-gloss, not a reusable tier-driven system. Per ruling `overnight_rerun_audit`: the gloss escalates once and then the fantasy is carried by behavior — no third overlay.
5. **Sound:** none proposed. No slurred-voice processing; the gag is that the bros hear themselves perfectly.

**Accessibility:** no camera wobble, no screen distortion, no control-lag motion effect is required by this spec — the legibility work is carried by text, chip, and pose. If asset work later adds motion, the existing static-icon / reduced-motion fallback pattern applies and stays mandatory (bible/02 §7).

## POINT 5 — EFFECT ON PLAYER CONTROL

- **Buzzed through Shitfaced:** full ordinary control. Menus are never removed at the bros' expense of the player's — degraded *content*, never degraded *input*.
- **The one Catastrophe override — "Assume the presidency":**
  - Trigger: the afterparty toast beat, player at the afterparty with the evening's tiers intact.
  - The player selects the restrained option (`[Let somebody else toast.]`).
  - The interface substitutes it — banner: **PILSNER IS MAKING AN EXECUTIVE DECISION.** / Selected automatically: **"Assume the presidency."**
  - The ceremony plays: coffee table, playbill hand on "preserve, protect and defend the open tab," Jenna's "So help you God," Executive Order 1: FOUR MORE BEERS. Short — a handful of boxes, no movement loss, no repeated auto-choices, no intimacy content anywhere in the override.
  - **Control returns immediately** after the ceremony. D6 (Bradley's choice) follows with both options fully live and never auto-substituted.
  - Bounded duration, single occurrence per quest, deterministic — no roll, no random generator of forced choices (ruling language honored).
- **What is never overridden:** D5, D6, the TROUSER SNAKE compromise sets (they are quest-authored content, not control loss), and the fixed Max runway (zero-menu by contract, not by intoxication).
- **No softlock path exists:** the override fires inside a linear afterparty beat; if the player saves after V3 and reloads, the afterparty resumes with the override still pending — the substitution is not consumed by a save/load that precedes it.

## POINT 6 — DURATION AND RECOVERY

- **The evening tier state:** set at Point 3's beats; **persists across every scene transition and save/load for the rest of the evening**; clears **only** on the next in-game morning transition (the V3 cut to black → morning frame is the only clear point). Ending any dialogue scene never clears it (editor `overnight_xanax` correction 3, generalized to the tier state).
- **Serialization:** the tier value travels inside the quest's evening chain (break §8, row 5) — a mid-chain save reloads at the correct tier. Absent key = Buzzed default; no migration needed on `SAVE_VERSION 2`.
- **TROUSER SNAKE:** governed by its own canon text (remainer of the evening), alcohol-dulled from Beer Goggles up (Point 2), never defeated by tier.
- **`flintstone_xanax_active`:** set the moment Bradley consumes the pill (consumption IS the trigger; the item is `usable: true`, zero-heal — glm_s5_synch_findings S4). Contract: **read by D6 staging, morning Bradley staging, and TROUSER SNAKE recurrence/performance suppression; cleared by the next in-game morning transition; never cleared by scene exit, dialogue end, hostel arrival, or the decline path** (the decline player who bought and ate the pill still carries it to their own next morning — the author's joke does not require the afterparty). Save/load-safe as a plain flag on `SAVE_VERSION 2`.
- **Morning:** one transition clears tier state, dulling presentation, and (per its own key) the Xanax suppression. Nothing intoxication-related crosses into the next day except the morning *consequences* (soreness animations, sweatshirt, buttons, decree).

## POINT 7 — COMEDIC CONSEQUENCE

One sentence per tier, because the break carries the scenes:

- Buzzed: the bros believe volume is charisma (the room chants FOUR MORE YEARS because the queens *made it* a chant; Pilsner believes he started it).
- Beer Goggles: an advertised drag revue becomes, in their minds, a private presidential-family hookup — the quest's central lie (ruling `overnight_rerun_audit`: the misunderstanding is political *identity*).
- Shitfaced: the select/deliver gap — the player watches Bradley fail to say "water."
- Catastrophe: Pilsner founds a government on an open tab, and the fridge decree survives until morning as physical evidence.

The law's shape is preserved: each tier's "benefit" is the bros' *experience* of benefit; the player's experience is watching the bill come due in the morning.

## POINT 8 — INTERACTION WITH OTHER ESTABLISHED STATUSES

| Status | Interaction |
|---|---|
| **TROUSER SNAKE** | Dulled by tiers ≥ Beer Goggles (presentation only); defeated only by the pill or the performer route; pill additionally blocks recurrence + performance until morning. |
| **Mid-Life Crisis Beer Goggles (combat)** | Shares a *name and visual language*, nothing else. No code linkage proposed. A quest evening at tier Beer Goggles does NOT apply the combat debuff outside battle, and the debuff's −Accuracy/+Friendly Fire never fires during the revue (no combat occurs during the show). |
| **Embarrassed / Hungover** | Untouched by tiers. Morning consequences are animations and dialogue, NOT statuses — ruling `presidential_soreness` prohibits a zero-stat morning status, and this spec extends that prohibition to the whole morning: no HUNGOVER chip in this quest's morning scene. |
| **Bravado** | No tier grants or drains Bravado. The Keg-Acolyte lockout (editor `keg_acolyte_dispute`) is an encounter-local applause rule, unrelated to intoxication — noted here only to close the door on conflation. |
| **The D3B "suppressed" presentation** | Subsumed: D3B's dimmed banner is the dulling at its strongest local expression. No separate flag (audit: scene-local, glm_mechanics_state §2.4). |

## POINT 9 — TECHNICAL IMPLEMENTATION DEPENDENCIES

All PROPOSED engineering; nothing below is claimed to exist in the shipped build:

| # | Dependency | Notes |
|---|---|---|
| 11 | Quest-scoped evening-tier state variable, serialized with the evening chain | Enum of 4 tiers; absent = Buzzed; `SAVE_VERSION 2` absorbs it. The only new *state* the system needs. |
| 12 | Tier-conditional dialogue option substitution | Generalizes the shipped replacement capability (already used by TROUSER SNAKE staging) from one status to tier-gated option sets. QUEST-AUTHORED content, PROPOSED plumbing. |
| 13 | The one-shot auto-select banner | The "PILSNER IS MAKING AN EXECUTIVE DECISION." UI moment — replaces the selected option and runs the ceremony. One scene, one firing. |
| 14 | Overlay/gloss control hooks | Per-gloss scripted presentation reusing the Debaucheryville overlay's *rendering approach*. No tier-driven system claimed. |
| 15 | The morning transition as the single clear point | V3 cut to black → morning frame performs all clears (tier state; `flintstone_xanax_active` per its own key). |
| 16 | Sprite sway/climb poses; static-icon accessibility fallback | Asset work; spec requires the text/chip legibility channel to function with motion disabled. |

**Explicitly NOT required:** an alcohol meter, drink-count tracking, ABV data, party-wide buff system, movement impairment, camera effects, or any new status entries. Every system this quest needs is one enum, one banner, one clear point, and staged content.

## POINT 10 — APPROVAL STATUS

| Element | Status |
|---|---|
| Tier names Buzzed → Beer Goggles → Shitfaced → Catastrophe | **CANON** (author, 2026-11-09) |
| The escalation concept + bounded loss of agency | **CANON** (bible/02 §3; editor `overnight_catastrophe` approves the afterparty override with changes — implemented at Point 5) |
| TROUSER SNAKE dull/defeat hierarchy | **CANON** (q9: B; editor `overnight_xanax`) |
| Flintstone Xanax effect + until-morning block | **CANON** (author directive; editor `overnight_xanax`: implemented exactly, no roll, no substitution) |
| MoonCum696969 pricing/spendability | **CANON** (q10: A; editor `mooncum_economy`) |
| All thresholds | **NONE DEFINED — intentional.** Tier advancement is authored-beat-driven by design; if the author later wants a metered system, that is a separate global-system decision. |
| Points 2–6, 9 mechanics | **PROPOSED** — production candidate pending editorial review; not implementation-authorized. |
| Dependencies 11–16 | **PROPOSED engineering list** for the implementation plan. |

**Open items for the moderator's register:** none new. The spec consumes every open intoxication question from glm_mechanics_state §9.1 (resolved by the author's law + Appendix A); that entry should be marked superseded, not deleted.
