# Status Effect Entry: "Foam Fighter"

*"PENDING (author): no in-game description line exists in the source."*

> **Draft entry, 2026-11-17 (Eurobound-tcip).** Filled from `design/templates/status_effect_template.md` using the ported source line ONLY. Every value not already in canon is **PENDING**; every point that needs the author is marked **RULING** and is asked on the Eurobound Desk (`Eurobound-tcip-q1`). Do not copy this entry into `design/mechanics/Battle/status_effects.md` until the RULING points are answered.
>
> **Template note.** Foam Fighter is a *passive title*, and `design/templates/` has no title template. This entry uses `status_effect_template.md`, the closest fit: the title's whole payload is a permanent passive effect pair (a buff and a drawback) earned by drinking, and this template carries the intoxication review the law requires. Titles as a system (where they show, whether they are equipped, whether they are statuses at all) have no design doc; that is filed separately (see Development Notes).

**Source, verbatim** (`design/quests/debaucheryville/brewerytourdebaucheryville.md:460`, ported by the author's ruling Eurobound-nda-q6, 2026-11-13):

> **Hidden Bonus:** If you drink all 4 brewery beers in one game day, you gain a passive title "Foam Fighter" (+5% to all HP-restoring item effects, but random Confusion chance in battle).

Author, Eurobound-tcip (bead page, 2026-11-13), verbatim: "Keep both; run the intoxication-law review and interview me for the numbers".

## 📋 Status Identity
- **Display Name**: "Foam Fighter" (unique: the only hits in the repo are this file and the source line)
- **Status ID**: `foam_fighter` (PENDING: `status_effects.json` schema is pending, Eurobound-70z)
- **Polarity**: Neutral-Situational (the source pairs a buff with a drawback). Final placement PENDING with the RULING points.
- **Category**: Scripted-Permanent (source: "passive title"). Whether it is ever lost: **RULING R2**.
- **Scope**: Both. The heal bonus covers "all HP-restoring item effects" (battle and overworld); the Confusion chance is "in battle".
- **Applies To**: **RULING R3** (the source says "you"; the alcohol ladder is per bro, ledger Eurobound-f3tq-q4 "Per bro").

---

## 🎭 The Gap

| Question | Answer |
|----------|--------|
| **What the bros think it is** | PENDING (author): the source gives no bro line. |
| **What it actually does** | +5% to all HP-restoring item effects (source). A random chance in battle to become Confused (source); in the engine, Confused makes single-target actions land on a random target from everyone on the field except the user (`game/battle/battle_core.gd:1014-1025`; ruling ef4_confused_stun, `game/battle/battle_rulings.gd:27-28`). Chance, timing and length: **RULING R1**. |
| **Why it's funny** | Internal: the name sells a hardened drinker; the payload is a small heal bonus paid for by randomly hitting the wrong person. |

---

## 📊 Effects

| Effect | Value | Notes |
|--------|-------|-------|
| HP restored by items | +5% | Canon (source). Rounding of the result (e.g. +15 HP → 15.75): PENDING (engineering, follow the existing rounding rule when one is ruled). Applies to "all HP-restoring item effects", so beers, food and consumables alike. |
| Confused chance in battle | **RULING R1** | Source: "random Confusion chance in battle". No number, no roll timing (battle start, each turn or each action), no length. |
| Confused length | **RULING R1** | Carried field Confusion lasts 2 battle turns (round v44 `b_confusion_battle = 2turns`, `game/core/field_status.gd:101-104`); whether Foam Fighter's uses that is not ruled. |

### Duration
- **Length**: Permanent per the source's "passive title". **RULING R2**: is the title kept forever, and does the Confusion chance ever end (rest, sobering up, a later day)?
- **Ends When**: **RULING R2**.

### Sources
| Source | Type | File |
|--------|------|------|
| Drink all four Debaucheryville brewery signature beers in one game day: Absinthe Lager, Iron Gut Tripel, Vape Stout, Blockchain Bock | Scripted (drink count) | `design/quests/debaucheryville/brewerytourdebaucheryville.md:22-24, :460`; beers in `design/items/brewery_tour/beer_absinthium_taproom_item.md`, `beer_three_crown_keg_haus_item.md`, `beer_tap_dat_vault_item.md`, `beer_ye_olde_brew_lab_item.md` |

"One game day": **RULING R4**. The Tap Dat Vault opens only at midnight (`brewerytourdebaucheryville.md:173`), so where the game day starts decides whether its Vape Stout can share a day with the other three. Each beer joins the permanent item pool on first completion of its brewery (`brewerytourdebaucheryville.md:335`), so the four can also be drunk from inventory.

### Cures
| Cure | Notes |
|------|-------|
| **RULING R2** | None in the source. |

### Stacking & Interaction Rules
| Rule | Value |
|------|-------|
| **Reapplied while active** | PENDING (source silent: a second four-beer day). |
| **Escalates into** | None in the source. |
| **Follow-up status** | None in the source. |
| **Immunity granted / blocked** | **RULING R6** (below). |

| Existing Status | What Happens |
|-----------------|--------------|
| The Neon Nightmare (Debaucheryville Legendary Hangover) | Gives "Confusion immunity during the battle" (`brewerytourdebaucheryville.md:344-345`). If it blocks Foam Fighter's roll, the drawback vanishes for that battle and only the +5% remains. **RULING R6.** |
| "Neon Photogenic" badge | "+5% resistance to 'Confused' status, permanently" (`brewerytourdebaucheryville.md:383`). Does it reduce Foam Fighter's chance? **RULING R6.** |
| Reality Anchor | 10% chance to block Confused outright (`game/core/field_status.gd:94`); the engine already applies it to any `confused` application on a party member (`game/battle/battle_core.gd:1113`). It would cut Foam Fighter's chance unless ruled otherwise. **RULING R6.** |
| Absinthe Lager's own Confusion | 30% chance to apply Confusion to the user on drinking (`brewerytourdebaucheryville.md:90`; item doc calls it "Green Fairy Confusion", `beer_absinthium_taproom_item.md:12`). The two rolls are independent unless ruled otherwise. |
| Sloppy | Also redirects single-target actions (`battle_core.gd:1014`); no new rule needed. |
| Alcohol ladder (Buzzed → Beer Goggles → Shitfaced → Catastrophe) | The four beers count toward the ladder; the title itself is not a ladder step. Tier thresholds are not ruled (Eurobound-p0j). |

---

## 🍺 Intoxication Review

### Alcohol Ladder Position (alcohol only)
- **Step**: None. Foam Fighter is earned by drinking but is not a tier. The four beers move the drinker up the ladder; other brewery beers count "1 drink toward Buzzed → Beer Goggles → Shitfaced → Catastrophe, with no ABV weighting" (Eurobound-eb8, as recorded in `design/items/brewery_tour/beer_bottoms_down_item.md:29`). The Debaucheryville four do not state it in their own docs, and the thresholds wait on Eurobound-p0j.

### No Free Advantage (`design/narrative/bros_choose_debauchery.md`)
"Intoxicants do not provide uncomplicated, consequence-free advantages." The source pairs the +5% heal bonus with a random Confusion chance in battle. The bonus is permanent; whether the drawback is big enough to pay for it depends on numbers the source does not give. **RULING R5: does Foam Fighter pass the no-free-advantage test as written?** Note R6: if any immunity blocks the roll, the title is a free advantage in that battle.

### 10-Point Design Review (`design/mechanics/intoxication_law.md` §8)
| # | Point | Answer |
|---|-------|--------|
| 1 | Source item or drink | The four Debaucheryville brewery signature beers, all drunk in one game day (`brewerytourdebaucheryville.md:460`). "One game day": **RULING R4**. Whether one bro must drink all four, or the party between them: **RULING R3**. |
| 2 | Immediate effect | Passive title "Foam Fighter": +5% to all HP-restoring item effects (canon); random Confusion chance in battle (chance, when it rolls, how long: **RULING R1**). |
| 3 | Escalation conditions | None in the source. A repeat four-beer day: PENDING. The beers themselves escalate the ladder (thresholds: Eurobound-p0j). |
| 4 | Visible player-facing cues | None in the source. PENDING (art/UI): the Confused spiral icon and indicator already have specs (`design/worlds/debaucheryville/PNG_Assets/Absinthium_Taproom_Complete_PNG_Asset_Requirements.md:341, :381`); the brewery tour styles achievement notices "like ICQ message popups" (`brewerytourdebaucheryville.md:320`). How a title is shown at all has no design (see Development Notes). |
| 5 | Effect on player control | In battle only, when the Confusion roll hits: the bro's single-target actions go to a random target, allies included (engine, ruled ef4_confused_stun). Bounded by Confused's length (**RULING R1**); readable through the existing Confused icon and battle line "%s is Confused and goes for %s." (`battle_core.gd:1025`). No field control loss. |
| 6 | Duration and recovery | Title: permanent per the source ("passive title"). Whether it or its Confusion chance ever ends: **RULING R2**. Each Confused proc recovers after its length (**RULING R1**). |
| 7 | Comedic consequence | From the source: the reward for a one-day four-brewery bender is a bro who heals slightly better and then, at random, attacks his own friends. Bro lines and the title's description line: PENDING (author). |
| 8 | Interaction with other established statuses | Neon Nightmare Confusion immunity, Neon Photogenic +5% Confused resistance, Reality Anchor 10% block: **RULING R6**. Absinthe Lager self-Confusion and Sloppy: independent (table above). Ladder: Eurobound-p0j. |
| 9 | Technical implementation dependencies | Proposed engineering work, none of it built: (a) a per-bro log of which of the four beer ids were drunk on each `GameClock.day` (`game/core/game_clock.gd:38`); (b) a title store and display (no Titles section in the approved menu, ledger `NEXT_WORK.md:699`); (c) a heal multiplier on item healing (`battle_core.gd:300` heals `heal_hp` flat; the field item path needs the same hook); (d) a battle roll that applies the existing `confused` status (`battle_core.gd:20`); (e) a `status_effects.json` schema (empty; Eurobound-70z). |
| 10 | Requires further author approval? | Yes: R1 Confusion chance, roll timing and length; R2 permanence and any cure; R3 who earns it; R4 what "one game day" means; R5 the no-free-advantage verdict; R6 which immunities and resistances block it. Bro lines and the description line are PENDING content. All six RULING points are on the Eurobound Desk as `Eurobound-tcip-q1`. |

---

## 🎨 Visual & Audio Cues

| Cue | Description |
|-----|-------------|
| **Status Icon** | PENDING. Confused procs reuse the existing Confused icon (Absinthium PNG spec :381). A title icon is not specced. |
| **Sprite / Particle Effect** | PENDING. Confused procs can reuse the Confusion spiral (Absinthium PNG spec :341). |
| **Screen Effect** | None in the source. |
| **Sound** | PENDING. |

---

## 🧾 Master List Entry

Not added yet. Goes into `design/mechanics/Battle/status_effects.md` (or a titles registry, if the author rules one) once R1–R6 are answered:

```
"Foam Fighter"
    • +5% to all HP-restoring item effects, random Confusion chance in battle (RULING R1)
    • Duration: passive title (RULING R2)
    • Source: drinking all 4 Debaucheryville brewery beers in one game day (RULING R3, R4)
    • Cure: RULING R2
    • Special: RULING R6
    • Description: "PENDING (author)"
```

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Master list grepped; no existing status already does this | ☑ (no title or status pairs a heal bonus with a Confusion chance) |
| Name and ID unique across the game | ☑ |
| Effects use engine stat names or named mechanics (or marked PROPOSED) | ☑ (item healing; engine `confused`) |
| Duration, sources, cures and stacking rules all stated | ☐ RULING R2–R6 |
| Loss of control is bounded, readable and recoverable | ☐ bounded once R1 sets the length |
| Intoxication review complete (if intoxicating) | ☑ (10 points written; six need the author) |
| Description line is funny, short, and never explains the joke | ☐ PENDING (author) |
| No real city or place names in the description | ☑ |
| Every unruled value marked PROPOSED | ☑ (marked PENDING / RULING; nothing proposed) |
| Author ruling recorded for a new status | ☑ kept by Eurobound-nda-q6 and Eurobound-tcip; numbers ☐ |

---

## 🚫 Warnings & Restrictions

### Content
- [x] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke
- [x] Full-strength MA satire; no softened name or effect
- [x] No moralizing: the Confusion chance is a consequence, not a lesson
- [x] The bros are never afraid, disgusted or self-aware about it
- [x] Funny, unique name; no real place names
- [x] No mascots

### Money
- [x] No price effect

---

## 📝 Development Notes

- Engine dependencies: item 9 of the review. `status_effects.json` schema is pending (Eurobound-70z); intoxication tiers are unimplemented (Eurobound-p0j).
- Titles have no system, template or registry, though many quests award them ("Web 1.0 Pioneer" and "Y2K Villain" in `club_flyers.md:206, :306`; "Truffle Collector", "Stroopwafel Connoisseur", "Curator of the Cursed Web" and others). Filed as its own bead (Eurobound-tcip, discovered-from).
- Open questions for the author: R1–R6, Eurobound Desk `Eurobound-tcip-q1`.

---

## 🔧 Development Status

- **Status**: Drafted (review done; numbers PENDING)
- **Entry Location**: `design/mechanics/Battle/status_effects.md` → Neutral-Situational, after the RULING points (or a titles registry, if ruled)
- **Registered In**: `game/assets/data/skills/status_effects.json` No (schema pending, Eurobound-70z)

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Draft entry and intoxication-law review from the ported source line (Eurobound-tcip) | game-designer agent |
