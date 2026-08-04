The Couchsurfing Chronicles
Premise: Meet hostel/bar NPCs who offer a “crash spot.”
Optional interiors where the bros “crash” with NPCs met in bars.
Player must navigate awkward morning-after conversations to get stat boosts (Charisma) or hilariously bad debuffs (Hangover).
1-2 opportunities to crash with NPCs per city

Gameplay: Dialogue mini-scenes the morning after.
Sometimes boost Charisma (“bonding story”).
Sometimes inflict Hangover/Embarrassed debuffs (awkward regrets).
Improvement Layer: Each NPC has unique comic flavor:

“Expat Who Never Left” → overlong rant, gives “Passport Pillow” (+1 Luck).

“Silent Bouncer Poet” → leaves you a cryptic poem (flavor collectible).

“Backpack Bard” → tries to jam at 7am, inflicts -SP but drops music sheet quest item.

Meta Layer (25% Enhancement)
📸 “Morning After Album”

Each unique Couchsurf event adds a “memory photo” to your Crash Gallery (viewable in hostel lobby).

Completing all Couchsurf NPCs across all cities unlocks the title: “Slept Around, Found Out”

Effect: +5% XP from battles only while Hungover 🤣

😬 “One-Night Stand Roulette”

Hidden mechanic: After 3+ Couchsurfings in a single city, you risk triggering a “STI Surprise”

(No graphic content. Instead, you get a status debuff called Regret Rash → reduces Luck for 3 battles, applies minor shame dialogue overlays like “It itches… your dignity.”)

🐸 ICQ Gag Crossover

One random Couchsurf per city unlocks a delayed ICQ pop-up the next day, like:

💬 Missed Call: “Hey, are you the one who clogged the sink?”
💬 New Message: “I’m keeping your hoodie. You don’t get to ghost me.”
💬 Anonymous Tip: “She’s married. Just FYI.”

---

# ADDENDUM — The Scripted Entry, The Herp, and The Gold Circle Coin

*(Added by `debaucheryville_sidequest_nothing_is_getting_through_01`. Everything above still stands unchanged.)*

## The Scripted Chronicles Entry: QUEEN Riviéra Renata

- **NPC ID:** `debaucheryville_npc_queen_riviera_renata_01`
- **Official Profile:** `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/queen_riviera_renata.md`
- **Owning Quest:** `debaucheryville_sidequest_nothing_is_getting_through_01` — `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`

One Chronicles entry cannot be player-initiated. The scripted outbreak event `night_event_outbreak_01` at the Bohemian Riviera's `night_party_zone` logs QUEEN Riviéra Renata's entry automatically and applies the permanent status effect `the_herp` to all three bros. Within the party it cannot be declined or avoided — **but attending the party is itself optional**, and a player who skips it never logs the entry and never catches the Herp.

**Consequence for the meta layer:** QUEEN Riviéra Renata is a **required host** for completion, and her entry can only be logged by attending the beach party — which also applies `the_herp`, permanently. So **full Chronicles completion REQUIRES catching The Herp**, and the unlock title — **"Slept Around, Found Out"** — is literal and load-bearing. Nobody completes it clean.

**But the whole chain is optional.** The Riviera, the trivia and the party are all player choices. A player who skips the party simply never completes the Chronicles and never earns the title. That is a supported playthrough, not a failure state, and it is never signposted as a mistake. See `Design/design_optionality_principle.md`.

**This is NOT the "One-Night Stand Roulette" mechanic.** That system, its 3+ couchsurfing trigger, and the `Regret Rash` debuff are unchanged and unaffected. `the_herp` is a separate, scripted, permanent status that does not roll, does not expire, and is never cured — only suppressed. The two can coexist.

## 🔀 THE FOUR STATES — every couchsurf host must have lines for all of them

**Author ruling (2026-08-03). This is the single source for the rule; the LINES live in each host's Chronicles entry, never duplicated into NPC profiles (profiles cross-reference).**

There is **no fixed couchsurf order.** Once a city has been visited the player can return to it at any time, so a host may be attempted in any Herp state, in any order, at any point in the game. Every host therefore needs **four authored variants**:

| # | State | Condition | What plays |
|---|---|---|---|
| **1** | **CLEAR** | Party has never caught `the_herp` | Normal engagement. She sleeps with them. Standard morning-after micro-scene and full payload. |
| **2** | **INFECTED** | `the_herp` active, `item_gold_circle_coin` NOT equipped | **Roasted and refused, hilariously.** She is visibly, unmistakably disgusted. In her own voice — no generic refusal exists. No payload awarded. Sets `<npc>_refused_while_infected = true`. |
| **3** | **SUPPRESSED — CLEAN** | Coin equipped, and she has NOT previously refused them | Plays **exactly as State 1, as if they had never been infected.** No callback, no reference, no acknowledgement. Full payload. |
| **4** | **SUPPRESSED — CALLBACK** | Coin equipped, and `<npc>_refused_while_infected = true` | One **sting callback line** — she says her piece about the last time, the bros absorb none of it — **then the couchsurf resolves normally.** Never a second refusal, never blocks the entry. |

### Binding rules
- **The flag is per-NPC**, not party-wide: `<npc>_refused_while_infected`. A host they never attempted while infected plays State 3, not State 4.
- **State 2 must be characterized and funny, never preachy.** She is disgusted and says so in her own established voice. Nobody lectures; nobody is cruel *about* the bros' feelings, because the bros have none to hurt. The joke is entirely on them.
- **Payload is awarded once.** First-time rewards (stat change, gag item, flavour collectible, ICQ payload, Passport entry) only if that entry was never completed before. A player who completed her pre-infection gets the scene, not duplicate rewards.
- **State 2 is a supported long-term playstyle**, not a dead end — a player may decline the Coin permanently and see State 2 for every host for the rest of the game. Those lines therefore carry real weight; write them well and write them varied. See `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md` → "The Permanently Infected Playthrough".
- **Renata is the sole exception** — she is the source of the infection, is only ever encountered via the scripted outbreak, and has no four-state treatment.

### Chronicles completion
Completion requires **every host, including Renata**. Renata's entry can only be logged by attending the beach party, which also infects the party — so completion is **gated behind catching the Herp**.

State 2 awards no payload, so an infected party cannot complete anyone while unsuppressed. **Full completion therefore requires obtaining the Coin.**

That makes declining the Coin a deliberate trade, and both sides of it are legitimate:
- **Take the Coin** → Chronicles completable, "Slept Around, Found Out" earnable.
- **Refuse the Coin** → forgo completion and the title, and instead watch the bros get refused by every host in every city for the rest of the game. Supported, intended, and for many players the better joke.

## The Six Official Profiles

The Debaucheryville couchsurf NPCs now have full standalone profiles. Their meet locations, morning scenes, results, ICQ integrations, and satire angles are unchanged; the profiles add the Herp-rejection scene and the post-cure callback line.

| Chronicles NPC | NPC ID | Official Profile (under `Design/Character Profiles/DebaucheryvilleNPCs/`) |
|---|---|---|
| QUEEN Riviéra Renata *(scripted)* | `debaucheryville_npc_queen_riviera_renata_01` | `Bohemian Riviera/queen_riviera_renata.md` |
| Vape Witch Vanessa | `debaucheryville_npc_vape_witch_vanessa_01` | `Velvet Curtain Club/vape_witch_vanessa.md` |
| Backpack Girl Who Never Left | `debaucheryville_npc_backpack_girl_01` | `Absinthe Arcade/backpack_girl_who_never_left.md` |
| CryptoBro69's "Ex" | `debaucheryville_npc_cryptobro69s_ex_01` | `Shadow Exchange/cryptobro69s_ex.md` |
| Suspicious Twins (Polina & Paulina) | `debaucheryville_npc_polina_01`, `debaucheryville_npc_paulina_01` | `Cirque Du Shady/suspicious_twins_polina_paulina.md` |
| Miss Morphine | `debaucheryville_npc_miss_morphine_01` | `miss_morphine.md` |

Debaucheryville detail lives in `Design/Quests/Location Specific/Debaucheryville/couchsurfingchroniclesdebaucheryville.md`. Status spec: `Design/Mechanics/Battle/status_effects.md` (`the_herp`). Item spec: `Design/Inventory/items/gold_circle_coin_item.md`.

**Standing rules, unchanged:** no graphic content — implication, cutaway, and morning-after wreckage only. Nobody relocates. Miss Morphine's is-she-real ambiguity is never resolved.