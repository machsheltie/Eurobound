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

One Chronicles entry is no longer optional. The scripted outbreak event `night_event_outbreak_01` at the Bohemian Riviera's `night_party_zone` logs a Chronicles entry automatically, on every playthrough, for every player. It cannot be declined, missed, or avoided, and it applies the permanent status effect `the_herp` to all three bros.

**Consequence for the meta layer:** since that entry is mandatory and the status it applies is permanent, **full Chronicles completion now REQUIRES catching The Herp.** The unlock title above — **"Slept Around, Found Out"** — becomes literal and load-bearing. Nobody reaches it clean.

**This is NOT the "One-Night Stand Roulette" mechanic.** That system, its 3+ couchsurfing trigger, and the `Regret Rash` debuff are unchanged and unaffected. `the_herp` is a separate, scripted, permanent status that does not roll, does not expire, and is never cured — only suppressed. The two can coexist.

## The Rejection Hook

While `the_herp` is active on the party, **every Couchsurf attempt in every city is intercepted.** The invitation still appears and the bros still accept; the morning-after micro-scene is simply replaced by that NPC's **characterized Herp-rejection scene**, authored in her own official profile in her own established voice. No generic refusal exists. No stat boost, gag item, or ICQ payload from the normal entry is awarded on an intercepted attempt.

The interception lifts **party-wide** the moment `item_gold_circle_coin` is equipped by any one bro. Every intercepted NPC can then be re-attempted, and each has her own **post-cure callback line** — none of which lets the bros off the hook. **Chronicles completion therefore stays fully achievable**; it is gated behind the Herp, not blocked by it.

**Resolution and payload (binding):** the post-cure callback plays as a **sting beat only.** She says her piece, the bros absorb none of it, and **the couchsurf then resolves normally** — the NPC's standard morning-after micro-scene and outcome run exactly as authored above. The callback is never a second refusal and never blocks the entry. **The first-time payload** (stat change, gag item, flavor collectible, ICQ payload, Passport entry) **is granted only if that entry was never completed pre-infection.** Players who completed an NPC before the outbreak get the callback and the scene, but no duplicate rewards.

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