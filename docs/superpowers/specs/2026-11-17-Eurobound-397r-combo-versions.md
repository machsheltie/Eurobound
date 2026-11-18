# Three-Bro Combo and Viral Moment: The Versions Side by Side (Eurobound-397r)

> **Status: COMPARISON ONLY, waiting on the author** (Eurobound Desk `Eurobound-397r-q1`).
> Nothing here merges, rewrites or recommends. Every quote is verbatim from
> `design/mechanics/Battle/battle_system.md` (not edited). Where a field is missing in a version, it says "(not stated)".
> Rulings checked: `docs/superpowers/NEXT_WORK.md:943` (rl4c, combos starter set), `:948` (g0jr-q3),
> `:927` (40ym, Ultimates), `:919` (028k direction), `:569` (Embarrassed). Spec: `docs/superpowers/specs/2026-11-16-eurobound-rl4c-numbers-proposal.md`.
> Proposal (not ruled): `docs/superpowers/specs/2026-11-17-Eurobound-028k-progression-numbers-proposal.md` §6 and §8.

## 1. The three-bro combo

battle_system.md states it three times under one name (Alpha Sigma Slam: :65-68, :137-143, :202) and once under another
(Alpha Sigma Thunder: :333-337). The two Slam entries at :137 and :202 agree with each other; :65-68 has its own backfire.

| Field | Alpha Sigma Slam, Party Dynamics (:65-68) | Alpha Sigma Slam, Combo Codex (:137-143) and Combo Bible (:202) | Alpha Sigma Thunder (:333-337) |
|---|---|---|---|
| Who | "(All Three)" (:65) | "(All Three)" (:137); "All Three" (:202) | "(All Three)" (:333) |
| Trigger / setup | "They sync into a frat chant without realizing." (:66) | "They sync a frat chant by accident, slamming the ground in rhythm." (:138); "Accidental synchronized frat chant." (:202) | "All three accidentally sync a frat chant during combat Requirements: All three alive, combined Bravado >150" (:334) |
| Cost | (not stated) | (not stated) | (not stated) |
| Effect | "Party-wide Bravado restored to full, enemies take big morale-shattering damage." (:67) | "Huge AoE damage + all Bravado bars restored." (:139); "Huge AoE + all Bravado restored." (:202) | "Devastating AoE to all enemies" (:335); "Full Bravado restoration for party" (:336); "\"Legendary\" status (+1 to all stats for rest of battle)" (:337) |
| Backfire | "If one bro is Embarrassed, chant falls apart → they take psychic damage from cringe." (:68) | "10% chance of chant devolving into argument → self-stun." (:140); "10% chance devolves into argument → self-stun." (:202) | "15% chance chant devolves into argument → self-inflicted damage" (:337) |
| Other | (none) | Audience: "Choir effect kicks in — the venue crowd sings: “Once in their lives, the bros actually coordinated!”" (:141). Spotlight: "Spotlight splits evenly (rare miracle)." (:142). Flair: "Amplified indoors (clubs, taverns); echo shakes walls. Outdoors it draws random bystander mobs." (:143) | (none) |

### What each version runs into in the approved rulings

**All versions**
- rl4c (`NEXT_WORK.md:943`): "one success roll on the participants combined Bravado tier (High 80%, Mid 60%, Low 40%); a failed roll is the backfire". A fixed backfire chance (Slam 10%, Thunder 15%) is a second, separate roll; rl4c has none.
- rl4c: "no Bravado cost". No version states a cost, so none conflicts here.
- rl4c spec §5 (`2026-11-16-eurobound-rl4c-numbers-proposal.md:71-72`) left the three-bro combo out of the starter set: "needs \"combined Bravado > 150\" (:334), off the current scale (the bros' maxes add up to 46), and full Bravado restore, which needs its own numbers." Every version restores all Bravado.
- 028k proposal §6 (`2026-11-17-Eurobound-028k-progression-numbers-proposal.md:231`, not ruled) places "Alpha Sigma Slam (:137)" at the Legacy (600) rung; §8 (`:274-276`) lists the duplicate and says "One of each pair needs striking before numbers."

**Alpha Sigma Slam, :65-68**
- rl4c (`NEXT_WORK.md:943`): "Embarrassed bros cannot start or join". Its only backfire ("If one bro is Embarrassed") cannot fire under that ruling. (The rl4c spec cites :68 as the source of the Embarrassed lock, `2026-11-16-eurobound-rl4c-numbers-proposal.md:33`.)
- "psychic damage": the ruled backfire types are self-damage, Bravado drain and Embarrassed (battle_system.md:25-28; rl4c sizes 5 HP, 3 Bravado, Embarrassed 2 turns). No psychic damage type exists.

**Alpha Sigma Slam, :137-143 / :202**
- "self-stun": not one of the three ruled backfire types (battle_system.md:25-28, rl4c sizes). A Stun status is used by Beeramid (rl4c, "Stun 1 turn").
- "10% chance": separate fixed roll; see "All versions".

**Alpha Sigma Thunder, :333-337**
- "combined Bravado >150": the bros' Bravado maxes add up to 46 (rl4c spec :72). rl4c rolls success by combined Bravado tier instead of a flat threshold.
- "\"Legendary\" status (+1 to all stats for rest of battle)": no `legendary` status in `game/assets/data/skills/status_effects.json` (the closest ids are `legendary_hungover` and other hangover statuses, unrelated).
- "self-inflicted damage": fits the ruled self-damage backfire (5 HP). "15% chance": separate fixed roll; see "All versions".

## 2. Viral Moment against Like & Subscribe

Like & Subscribe is approved and built (rl4c, `NEXT_WORK.md:943`; backfire confirmed g0jr-q3, `:948`;
`game/assets/data/skills/combos.json` `like_and_subscribe`). Viral Moment (:328-332) uses the same pair and the same setup.

| Field | Like & Subscribe, Party Dynamics (:61-64) | Like & Subscribe, Codex (:127-136) and Bible (:201) | Viral Moment (:328-332) | Like & Subscribe as ruled (rl4c, `NEXT_WORK.md:943`, `:948`) |
|---|---|---|---|---|
| Who | "(Chadwick + Bradley)" (:61) | "(Chadwick + Bradley)" (:127); "Chadwick + Bradley" (:201) | "(Chadwick + Bradley)" (:328) | Chadwick + Bradley |
| Trigger / setup | "Chad streams Bradley’s attack live." (:62) | "Chad livestreams Bradley’s attack." (:128); "Chad livestreams Bradley’s attack." (:201) | "Chad livestreams Bradley's Ultimate Move Requirements: Bradley using special ability, Chad has Ring Light Mace equipped" (:329) | Combo main action; "open from the start" |
| Cost | (not stated) | (not stated) | (not stated) | "no Bravado cost" |
| Effect | "Double Bradley’s damage + crit chance; viral success = random Bravado regen across party." (:63) | "Bradley’s next hit deals double damage, 25% chance of “viral crit” (massive multiplier)." (:129); "Bradley’s hit = 2× DMG; 25% chance “viral crit.”" (:201) | "Bradley's attack damage doubled" (:330); "25% chance of \"Viral Crit\" (4x damage)" (:331); "Party-wide Bravado regeneration" (:332) | "x2, 25% viral x4 with no SMAAAASH and 1-3 Bravado to each bro" |
| Backfire | "If no one tunes in → attack fizzles, Bradley loses 3 Bravado (“No viewers, bro”)." (:64) | "RNG flop → “0 viewers.” Bradley loses Bravado in humiliation." (:130); "RNG flop: “0 viewers” → Bradley loses Bravado." (:201) | "\"0 Viewers\" → Bradley loses Bravado, Chad gains \"Embarrassed\"" (:332) | "backfire Bradley -3" (g0jr-q3: "Bradley pays on a Like & Subscribe backfire") |
| Other | (none) | Audience overlay, spotlight, regional flair (:131-136) | "Chat Overlay: Fake comments appear: \"YOOO BRADLEY!\" or \"cringe bro delete this\"" (:332) | (none) |

### What Viral Moment runs into in the approved rulings

- **Same pair, same setup, same multipliers as the ruled Like & Subscribe.** The ruled ×4 viral size was taken from Viral Moment: the rl4c spec cites "Viral crit size: **4× damage** | battle_system.md:331 (Viral Moment)" (`2026-11-16-eurobound-rl4c-numbers-proposal.md:21`), and the ruled Like & Subscribe gives each bro 1-3 Bravado on a viral hit, which matches Viral Moment's "Party-wide Bravado regeneration".
- **Backfire.** Viral Moment adds "Chad gains \"Embarrassed\"". The ruled Like & Subscribe backfire costs Bradley 3 Bravado and nothing else (g0jr-q3, `NEXT_WORK.md:948`).
- **Trigger on Bradley's Ultimate.** The canon Ultimates are ruled (40ym, `NEXT_WORK.md:927`: Bradley's is Fratocalypse Now, battle_system.md:283, "Channels entire Bravado bar into a screen-wide nuke"); no numbers are ruled for them. Embarrassed locks Ultimates (`NEXT_WORK.md:569`), and 028k proposal §6 opens Ultimates at Legacy (600), not ruled.
- **"Ring Light Mace" requirement.** Chadwick's starting weapon is the "Vintage Ring Light Mace" (`design/characters/Chadwick/chadwick.md:5`, `design/mechanics/Battle/party.md:44`). No ruling ties any combo to equipped gear yet.
- **028k proposal §6** (`:231`, not ruled) places Viral Moment at Legacy, "also needs the Ring Light Mace equipped", "rides on Bradley's Ultimate"; §8 (`:274-276`) lists "Like & Subscribe and Viral Moment (:328)" as a duplicate pair.
- **Name neighbours (for the author's awareness, not a conflict):** Chadwick's canon Ultimate is "Going Viral" (battle_system.md:291, ruled 40ym); the ruled Like & Subscribe has a "viral" hit; battle_system.md:433 uses "viral moment" in lower case for Chad's Distraction Post.

## 3. Already settled (not reopened)

- Beeramid (:56-60, :117-126, :200) and Beeramid Blast (:320-327): merged by rl4c under the name Beeramid, with the :320-324 numbers (`NEXT_WORK.md:943`; rl4c spec :87-88).
- Like & Subscribe backfire payer: Bradley (g0jr-q3, `NEXT_WORK.md:948`); battle_system.md:64 now says Bradley.

## 4. If the author rules

battle_system.md marks the losing entries superseded (no rewrite of the winners beyond what the author says), the ledger
records the ruling, and the 028k §6 combo table follows the surviving names. Any numbers for the surviving three-bro combo
are a separate round.
