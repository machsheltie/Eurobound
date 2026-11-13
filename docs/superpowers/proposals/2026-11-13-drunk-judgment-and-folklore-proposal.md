# PROPOSAL: Drunk Judgment Tiers, Embarrassment Events and Pilsner Folklore

**Bead:** Eurobound-f3tq. **Status:** PROPOSAL for author approval. Not final design. Nothing here is canon until the author rules.
**Author's words (2026-11-13):** quoted from the bead where used. Every number marked **PROPOSED** is a placeholder range, not a ruling.
**Binding inputs:** `design/mechanics/intoxication_law.md`, `design/narrative/bros_choose_debauchery.md`, `.claude/CLAUDE.md` content rules.
**Voice rule for all player-facing text this proposal implies:** no narrator, no disclaimer, no moral framing. The bros are never afraid, disgusted or self-aware.

---

## 0. What already exists (build on it, do not duplicate)

| Thing | Where | How this proposal uses it |
|-------|-------|---------------------------|
| Alcohol ladder Buzzed / Beer Goggles / Shitfaced / Catastrophe | `intoxication_law.md` App. A (l.145-157) | The four tiers. Names are ruled and unchanged. |
| "PILSNER IS MAKING AN EXECUTIVE DECISION" banner and the dialogue mock-up | App. A (l.167-175) | The override cue and the option-degradation pattern. |
| Beer Goggles overlay | Quest `nothingisgettingthrough.md` (cited by App. A l.177) | Reused as the tier 2 visual. |
| Embarrassed status | `design/mechanics/Battle/status_effects.md` l.45 (-2 Charm, -1 Confidence, no Bravado abilities, 2-3 turns). The ledger (`NEXT_WORK.md` l.569) gives a different battle version (-20% ATK, -2 Bravado a turn). | Reused as the optional status an event leaves behind. **Not redefined.** The two versions disagree; flagged in review point 8. |
| Hungover status | `status_effects.md` l.35 (-2 all stats, -1 HP per turn, 25% skip, 3-5 turns) | The proposed morning cost (Q7). |
| Regional Reputation states, "Public Embarrassment" as a destroyer, "Spectacular failures that become endearing" as a gain | `socialmechanicsandreputationsystem.md` l.52, l.188 | The doc already contains both halves of the author's mixed-consequence idea. Extended, not replaced. |
| "Local Legend" (three existing uses) | Rep doc l.40 (dialogue unlock at "Honorary Drinking Buddies"); `skilltrees_cloutspells.md` l.104 (700 Clout status, "NPCs buy them drinks"); `selfiewithlocallegend.md` (mock famous locals) | Name collision. See section 5. |
| Morning-after / rest hook | `strawberry_shortcake_speedcakes_item.md` l.192 ("Rest/morning-after script", flag PROPOSED), `game_design_document.md` l.179 | The wake-up hook the evidence roll attaches to. Not confirmed built. |
| Bunk & Blunder Traffic Cone | `The_Bunk_And_Blunder_PNG_Assets.md` l.104, l.129, l.686; Colm's wall and rule 7 in `npc_colm_obrien.md` | A separate item per the author's ruling. The Stolen Traffic Cone must not reuse its flags or quest. |
| "Evidentiary Record" | Searched `docs/`, `design/`, `game/`. No such system exists. | Not built on. This proposal deliberately adds no journal or log for evidence (section 4). |
| Status data schema | `game/assets/data/skills/status_effects.json` is empty; see `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md` | New statuses wait on that schema. |

---

## 1. Tier table: what each tier does to player choice

**Scope decision needed (Q1):** the author's wording is Pilsner-centric, but the cab mooning is a group event. This proposal assumes a **per-bro intoxication tier T (0-4)**, so "Pilsner overrides" is Pilsner's expression and the other two bros need an equivalent. Their personality hooks are PROPOSED only, taken from existing canon (Pilsner narcissist; Chadwick films things per App. A; Bradley physical presence per the Social doc).

**Dialogue choice model (PROPOSED):** each authored choice set may carry up to three tagged slots: `sensible`, `bold`, `stupid`. Writers author the `stupid` slot only for sets flagged `judgment_gate`. Sets without the tag are never altered, which keeps quest-critical dialogue safe.

| T | Tier | Author's meaning | Dialogue / UI effect (PROPOSED) | Control |
|---|------|------------------|---------------------------------|---------|
| 0 | Sober | Player makes decisions | All slots shown as authored. | Full. |
| 1 | Buzzed | Slightly worse options | The `sensible` option is reworded as a boast ("Politely decline" becomes "Decline, loudly") and its skill-check modifier drops by 1 step. A `bold` option is added where none exists. No option is removed. | Full. Player picks everything. |
| 2 | Beer Goggles | Pilsner occasionally overrides good judgment | Everything from T1. On a `judgment_gate` set, a **override roll** may replace the player's pick with the `stupid` slot. Chance PROPOSED 10-20% per gate, max 1 override per conversation. Perception layer: attraction and social labels use the Beer Goggles overlay. Existing combat debuff stays intact (App. A l.161). | Player picks; game may overrule it once per conversation. |
| 3 | Shitfaced | Embarrassment event guaranteed; bro initiates; player may be forced to finish | Sensible options removed or distorted on `judgment_gate` sets. Override chance PROPOSED 30-50%. One **guaranteed embarrassment event** per night (section 2). Movement unreliability and sloppy animation per App. A l.162, with a reduced-motion alternative. | Event beats are authored; player input narrows during them. |
| 4 | Catastrophe | Stays the worst tier | Everything from T3, plus: the event comes from the Catastrophe variant pool; a second event per night is allowed; **morning evidence roll** is live (section 4); the wake-up cost applies (Q7). | Longest forced stretch, still bounded. |

**What the concrete UI terms mean**

| Phrase | Meaning (PROPOSED) |
|--------|--------------------|
| "Slightly worse options" | The option set is reworded and the sensible choice's odds drop. Never fewer choices at T1. |
| "Overrides good judgment" | The game picks the `stupid` slot for the player, shows the App. A "PILSNER IS MAKING AN EXECUTIVE DECISION" banner for 1.0-1.5 s (PROPOSED), and auto-selects. The banner is the telegraph; no explanatory text follows it. |
| "Forced to finish" | After a bro initiates, the event plays its authored beats (1-3 PROPOSED). The player cannot cancel, but each beat still needs an input: **advance-only** (press to continue, or hold to confirm). No timing test, no failure state. |
| Bounded duration | Whole event PROPOSED 20-40 s. A timeout auto-advances the last beat, so no event can hold the player. |
| Accessibility | An "auto-complete events" setting plays the event with no input. A reduced-motion setting replaces wobble and distortion. |
| Save/load | The pending-event flag and the current beat index are saved. Loading mid-event restarts that event from beat 1. |

**Tier movement:** how a drink raises T and how T decays (sleep, food, time) is not ruled. See review points 3 and 6.

---

## 2. Embarrassment-event system

### 2.1 Guarantee rule (PROPOSED)

1. The first time a bro reaches T >= 3 since his last sleep, set `pending_embarrassment[bro] = true`.
2. The event fires at the next **safe trigger point**: a scene transition, venue entry, or end of a conversation. It never fires in battle, in a cutscene, or inside a quest-critical beat. If blocked, it waits for the next safe point.
3. Event choice: filter the event table by context tags and minimum tier, then weighted-random. If nothing matches, a **fallback pool** event fires, so the guarantee always holds.
4. No repeats of the same event id for PROPOSED 2-3 in-game nights, except events marked `recurring`.
5. A **group event discharges `pending_embarrassment` for every participant.** This stops one cab ride from producing three separate guaranteed events.
6. Cap: one guaranteed event per bro per night at T3; one extra allowed at T4.

### 2.2 Event table schema

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Unique across the game. |
| `min_tier` | int 3-4 | Catastrophe-only events use 4. |
| `context_tags` | list | Cab, bar, street, venue id. Cab context is an engineering dependency (section 6, point 9). |
| `initiator_base` | per-bro 0-3 | PROPOSED, see 2.3. |
| `group` | bool | Others may join. |
| `recurring` | bool | May repeat; repeat count feeds folklore. |
| `outcomes` | list | Each carries `polarity`, `immediate`, `cost`, `standing_deltas`, optional `deferred_payoff`. See section 3. |
| `leaves_status` | optional | May apply the existing Embarrassed. |

**Example Shitfaced events** (named by the author, not designed here): cab mooning (section 2.4); the Blarney Trap wet-T-shirt contest, bead Eurobound-n7w5, written separately and slotted in when it lands. All other rows are SLOTS: `[event slot 1..n]`.

### 2.3 Initiator selection

**Expression:** `W_i = B_i * T_i`, `P(initiator = i) = W_i / sum(W)`

| Symbol | Type | Range | Description |
|--------|------|-------|-------------|
| B_i | float | 0-3 (PROPOSED) | The event's personality base for bro i, set per event in its table. |
| T_i | int | 0-4 | Bro i's current tier. A sober bro has weight 0 and cannot initiate. |
| W_i | float | 0-12 | Initiator weight. |
| P | float | 0-1 | Probability bro i initiates. |

**Output range:** unbounded above only by the 0-12 product; normalised to 1. If `sum(W) = 0`, no one is drunk enough and no event fires.
**Worked example (placeholder bases):** all `B = 1`. Pilsner T2, Chadwick T1, Bradley T3. W = 2, 1, 3, sum 6. Bradley initiates 50%, Pilsner 33%, Chadwick 17%. More intoxication makes a bro likelier to start it, and the event table's personality bases tilt it further. This satisfies "different bro may initiate depending on intoxication/personality" without a fixed script.

### 2.4 Cab mooning: recurring group event

1. **Trigger:** cab context, at least one bro at T >= 3. Marked `group` and `recurring`.
2. **Initiator:** drawn by 2.3.
3. **Joining:** for each other bro j, `P(join) = clamp(J_j + 0.15 * (T_j - 1), 0, 0.9)`. J_j is a per-bro base, PROPOSED 0.2-0.5. A bro at T0 never joins.
4. **Pilsner's rule (the author's quote):** if the initiator is not Pilsner and Pilsner is at T >= 2, he joins with probability 1. "Lord Pilsner cannot allow another man to dominate the evening's ass-based discourse." The threshold T2 is PROPOSED (Q8).
5. **Scaling:** outcomes are tagged by participant count (1, 2, 3). The Social doc's core philosophy is shared catastrophe ("Those Three American Idiots"), so a three-bro moon hits the shared regional standing; a solo moon is attributed to the bro.
6. **Recurrence:** each performance increments `folklore_count[event_id]`. That count is what raises "Local Legend" standing (section 5). Nothing recites it to the player.

---

## 3. Consequence model

Every outcome is tagged one of three polarities. **No outcome is tagged benefit-only**: a benefit always carries a stated cost (`bros_choose_debauchery.md`: "Any apparent benefit should be temporary, deceptive, compromised, or accompanied by an entertaining drawback").

| Polarity | Meaning | Rule |
|----------|---------|------|
| Punish | Pure loss | Allowed. Must be funny and character-specific, not arbitrary (law point 5). |
| Mixed | Loss in one place, gain in another | The author's mooning example. The cost field names the loss. |
| Weird benefit | Gain with a priced cost | Cost is paid now, later, or both. The cost field may not be empty (validation rule). |

**Author's examples mapped to the model** (costs are PROPOSED slots for the author to confirm, not invented content):

| Author's example | Polarity | Benefit | Cost slot (PROPOSED) |
|------------------|----------|---------|----------------------|
| Cab mooning | Mixed | A bar crowd's standing rises; Local Legend progress | Standing with the mooned NPC falls |
| Idiotic purchase, useful three days later | Weird benefit, delayed | An item that pays off later | SOVS paid now; the payoff is conditional (Q5) |
| Catastrophic pass that works | Weird benefit | The pass succeeds | The success carries a paired cost: slot `[pass-cost]`, default is the T3+ wake-up cost (Q7) |
| Unfamiliar promotional T-shirt becomes a collectible | Weird benefit | A collectible | A slot `[shirt-cost]`; the shirt is a visible worn item with no stat advantage, so the cost is that it displaces whatever slot it occupies (confirm with item template) |
| Traffic cone | Neutral evidence | The player gains an item | The silent mechanic in section 4; no benefit stated at all |

### Delayed-payoff mechanic (PROPOSED)

A **deferred-consequence queue** stores records `{source_event, due_day, payoff_id, cost_paid}`.

| Rule | Value |
|------|-------|
| Delay | Author's example is 3 in-game days. Other payoffs PROPOSED 2-4. |
| Delivery | On the due day's wake-up, or at the first relevant scene after it. |
| Announcement | Through the same ordinary item or standing change as any other source. No "your earlier decision paid off" message. |
| Survival | Stored in the save. If the due condition can never occur (item consumed or quest closed), the record drops silently. No softlock. |
| Cap | PROPOSED max 3 open records, so the queue cannot be farmed. |

---

## 4. Morning-evidence system

**Roll timing:** once per wake-up, on the first frame after the rest transition completes. It rolls only if any bro reached **T4 (Catastrophe)** during the day since the last wake. Author: it "sometimes appears overnight when they hit the fourth level of drunk."

**Chance:** PROPOSED 30-50% flat (Q6).

**Formula**

`evidence_awarded = (max(T_i over the day) == 4) AND (rand() < R)`

| Symbol | Type | Range | Description |
|--------|------|-------|-------------|
| T_i | int | 0-4 | Each bro's highest tier since the last wake. |
| R | float | 0.30-0.50 (PROPOSED) | Evidence chance per eligible wake-up. |
| rand() | float | 0-1 | Uniform roll. |
| evidence_awarded | bool | true/false | Whether one item is drawn. |

**Output range:** at most one item per wake-up (PROPOSED). **Worked example:** Bradley reaches T4 at 02:00; the party rests; R = 0.40; roll 0.27 is below 0.40, so one item is drawn from the pool.

**Pool shape (SLOTS only, no new items invented here)**

| Slot | Content |
|------|---------|
| E1 | **Stolen Traffic Cone** (author-named; separate from the Bunk & Blunder cone). |
| E2 | Wearable collectible slot (the author's promotional T-shirt example). |
| E3 | Junk item slot, regional flavour, funny inspect microcopy per the junk-items rule. |
| E4 | Item that pays off later (ties to the deferred queue). |
| E5-En | Open. Each added item needs its own template and an author ruling. |

Pool rules (PROPOSED): each item is drawn once per save; weights per slot; drawn items leave the pool; an empty pool stops the roll silently.

**Exact silent notification behaviour**

| Aspect | Behaviour |
|--------|-----------|
| Text | "You have added Stolen Traffic Cone to your inventory" (the ruled wording; the bead's mock-up reads `INVENTORY UPDATED / + 1 Traffic Cone`, so the author should confirm which, though the ruling post-dates it). |
| Component | The **same toast any pickup uses**. No special colour, icon, sound, shake or highlight. |
| Timing | Appears once, on the first control frame after the morning fade-in. Default pickup dismissal. |
| Absent | No dialogue, no portrait, no flashback, no quest entry, no journal entry, no map marker, no "new" badge beyond the standard inventory one, no tooltip on the toast. |
| Bros | No bro comments on it, ever. Pilsner "doesn't know either": inspect text and any dialogue must not reference how it was acquired. |
| Inventory entry | The item's normal inspect microcopy is funny and says nothing about its origin. **Confirm** the author's "no tooltip" refers to the toast and not the item's normal inspect text (Q9). |
| Hidden data | An internal debug-only field records the source night. It is never shown, exported to a log, or read by dialogue. |
| Evidentiary Record | None exists, and none is created. A log would explain the item and break "nobody, including the game, ever explains how". |

---

## 5. Reputation and "Local Legend" standing (NEEDS AUTHOR RULING)

**Problem 1: per-NPC standing.** "Loses Reputation with one NPC" implies standing below the regional level. Today reputation is regional, five states per region.

| Option | What it is | Pros | Cons |
|--------|-----------|------|------|
| A. Sparse standing map | `standing[npc_or_crowd_id]` integer, only created when an event's outcome table names it; default 0; regional state untouched | Precise, supports "this crowd loves it, that NPC doesn't" | New numeric system to tune and display |
| B. Flags only | `grudge:<id>` and `fan:<crowd_id>` booleans set by outcomes; dialogue and prices read them; no numbers | Cheapest; matches "NPCs remember previous interactions" (Social doc l.165); easy to test | Coarse; no gradual build |
| C. Regional-state nudges only | Events move the regional state up or down; "one NPC" is a dialogue line, not data | Zero new systems | Cannot express the author's split reaction |

**Recommendation: B for the NPC grudge, plus the `folklore_count` from section 2.4 for the crowd side.** The count gives gradual growth without a second reputation number.

**Problem 2: who owns "Local Legend".** Three docs already use it. The Rep doc makes it a dialogue unlock at Publandia state 4; the Clout tree makes it a status at 700 Clout; the quest uses it for mock-famous NPCs. The author's "his Local Legend status rises" fits the Clout "status" reading, but the author also wrote "Reputation". Options: (1) Local Legend is the existing Clout status and folklore adds Clout; (2) Local Legend is the Reputation dialogue unlock and folklore moves Reputation; (3) the new folklore standing gets its own unique name and Local Legend stays as is. **Recommendation: (3), subject to the author's wish**, because name uniqueness is a standing rule. The author must choose the name.

---

## 6. intoxication_law 10-point review (law section 8)

Reviewed for the whole system. Verdicts: PASS, PASS-FLAG (acceptable with a stated flag), RULING (cannot pass until the author rules).

| # | Point | Answer | Verdict |
|---|-------|--------|---------|
| 1 | Source item or drink | Any alcohol item, each carrying a ladder step per the consumable template. No new source is added. Drugs (Xanax, Fentanyl) are out of scope; Fentanyl needs its own authorisation per law point 4. | PASS |
| 2 | Immediate effect | Section 1 table per tier. | PASS |
| 3 | Escalation conditions | A drink's ladder step raises T. The numeric thresholds and per-drink points are unruled (App. A: "not yet approved numerical thresholds"). | RULING |
| 4 | Visible cues | Tier badge, reworded option text, Beer Goggles overlay (existing), the executive-decision banner (App. A). Status icon art is not specced. | PASS-FLAG |
| 5 | Effect on player control | Bounded: events 20-40 s, advance-only input, auto-complete setting, timeout, one override per conversation at T2, no battle or quest-critical interruption. **Flag:** App. A puts forced decisions at Catastrophe; the ruling moves overrides to Beer Goggles and the guaranteed event to Shitfaced. App. A needs amending (Q2). | PASS-FLAG |
| 6 | Duration and recovery | Events are bounded. Tier decay (sleep, food, time) is not defined; Hungover and Embarrassed already exist. | RULING |
| 7 | Comedic consequence | Mixed outcomes, deferred payoffs, silent evidence. The joke is the gap between what the bro expects and what he gets (Debauchery canon). No lecture, no narrator. | PASS |
| 8 | Interaction with other statuses | Reuses Hungover and Embarrassed (not redefined). **Flag:** Embarrassed has two versions (master list vs ledger l.569). The Mid-Life Crisis Beer Goggles combat debuff is kept intact. The TROUSER SNAKE / Xanax rule is untouched. | PASS-FLAG |
| 9 | Technical dependencies | **PROPOSED engineering, not verified in `game/`:** per-bro intoxication state; dialogue option filter/override hook; scripted event runner with a skip path; deferred-consequence queue; wake-up hook; per-NPC flags; a cab or travel context (I found no cab system in the docs I checked); standard toast reuse. The status schema is empty (see the 2026-11-12 data-shape proposal). | RULING |
| 10 | Requires further author approval | Yes: this whole proposal, every PROPOSED number, new statuses (mechanics change), the standing model, the Local Legend name, and each evidence item. | RULING |

**No Free Advantage check:** every weird benefit in section 3 has a cost field, and the validation rule rejects an empty one. The cone grants no stat. **Content-rule check:** no moralising text, no bro fear or self-awareness, no real place names, no nudity (the Blarney Trap contest is a stage event, not a shown one), all prices in SOVS.

---

## 7. Open questions for the author

| # | Question | Options | Recommendation |
|---|----------|---------|----------------|
| Q1 | Is intoxication tracked per bro or per party? | (a) per bro, (b) Pilsner only with the others as scenery, (c) one party-wide tier | **(a)**. Group events need bros at different tiers. |
| Q2 | App. A currently puts forced decisions at Catastrophe. Amend it? | (a) amend App. A to this mapping, (b) keep App. A as illustration and record this proposal as superseding it, (c) revert the mapping | **(b)**; leaves the law text intact and the ruling traceable. |
| Q3 | Per-NPC standing model | (A) sparse numeric map, (B) flags only, (C) regional nudges only | **(B)** |
| Q4 | Local Legend ownership | (1) the Clout status, (2) the Reputation dialogue unlock, (3) a new unique name | **(3)** |
| Q5 | Does a delayed payoff always pay off? | (a) always, as the author wrote, (b) usually, with a rare dud, (c) set per item | **(a)** for the first items; the dud variant can follow. |
| Q6 | Evidence roll shape | (a) flat 30-50%, (b) flat plus a pity bonus after misses, (c) guaranteed the first Catastrophe night, then rare | **(a)**; (c) invents a story beat. |
| Q7 | Do T3+ nights always end with Hungover on waking? | (a) yes, universal cost, (b) only for T4, (c) never; costs live only in each outcome | **(a)**. It prices every weird benefit once and uses an existing status. |
| Q8 | Pilsner's cab-moon join threshold | (a) always joins at T >= 2, (b) joins with a high chance only, (c) joins at any tier above Sober | **(a)** |
| Q9 | Does "no tooltip" cover the item's normal inspect microcopy? | (a) only the notification, (b) the item has no description at all | **(a)**; the junk-items ruling asks for funny microcopy. |
| Q10 | Embarrassment cadence | (a) one guaranteed per night at T3, extra at T4, (b) one per tier entry, (c) one per bro per day | **(a)** |

**New cross-system entities for `design/registry/entities.yaml`** (not written; the registry file was not checked): `intoxication_tier` (0-4 per bro), `folklore_count`, `grudge:<id>` and `fan:<id>` flags, deferred-consequence queue, `Stolen Traffic Cone`. Do you want me to add them after approval?
