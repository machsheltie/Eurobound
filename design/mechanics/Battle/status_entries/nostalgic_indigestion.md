# Status Effect Entry: "Nostalgic Indigestion"

*"PENDING (author). The source glosses it as: remembering when food didn't cost this much"*

> **Draft entry, 2026-11-17 (Eurobound-tcip).** Filled from `design/templates/status_effect_template.md` using the ported source line ONLY. Every value not already in canon is **PENDING**; every point that needs the author is marked **RULING** and is asked on the Eurobound Desk (`Eurobound-tcip-q2`). Do not copy this entry into `design/mechanics/Battle/status_effects.md` until the RULING points are answered.

**Source, verbatim** (`design/quests/debaucheryville/club_flyers.md:422-425`, ported by the author's ruling Eurobound-nda-q6, 2026-11-13):

> ### Late-Night Kebab Stand
> - **Menu items** reference Y2K culture: "Millennium Bug Wrap," "Y2K-bab Special"
> - **Kebab guy** asks if they're "those guys from the Matrix" (they're wearing knockoff leather)
> - **Status effect:** "Nostalgic Indigestion" - remembering when food didn't cost this much

Author, Eurobound-tcip (bead page, 2026-11-13), verbatim: "Keep both; run the intoxication-law review and interview me for the numbers".

## 📋 Status Identity
- **Display Name**: "Nostalgic Indigestion" (unique: the only hit in the repo is the source line. Close but distinct: "Nostalgically Self-Aware", `brewerytourdebaucheryville.md:444`.)
- **Status ID**: `nostalgic_indigestion` (PENDING: `status_effects.json` schema is pending, Eurobound-70z)
- **Polarity**: PENDING with **RULING R1** (the name reads Negative; the source gives no effect).
- **Category**: Food (source: a kebab stand; no drink or drug in the source).
- **Scope**: **RULING R1**.
- **Applies To**: **RULING R1**.

---

## 🎭 The Gap

| Question | Answer |
|----------|--------|
| **What the bros think it is** | PENDING (author): the source gives no bro line. |
| **What it actually does** | **RULING R1**: the source gives no effect, only the gloss "remembering when food didn't cost this much". |
| **Why it's funny** | Internal: the bros' stomachs are as stuck in the past as their slang; the gloss ties the ache to prices. |

---

## 📊 Effects

| Effect | Value | Notes |
|--------|-------|-------|
| Any stat, battle or overworld effect | **RULING R1** | None in the source. |

### Duration
- **Length**: **RULING R2**
- **Ends When**: **RULING R2**

### Sources
| Source | Type | File |
|--------|------|------|
| The Late-Night Kebab Stand during the Club Flyers quest. What triggers it (any purchase, the two Y2K menu items, the visit, the Path A "Guerrilla marketing" stop) is **RULING R3**. | Food / environmental | `design/quests/debaucheryville/club_flyers.md:132, :422-425` |

The two menu items the source names ("Millennium Bug Wrap," "Y2K-bab Special") are not on the stand's own menu (`design/worlds/debaucheryville/Late-Night Kebab Stand.md:89-130`, eight items). Whether they are added there is part of **RULING R3**.

### Cures
| Cure | Notes |
|------|-------|
| **RULING R2** | None in the source. |

### Stacking & Interaction Rules
| Rule | Value |
|------|-------|
| **Reapplied while active** | PENDING (source silent). |
| **Escalates into** | None in the source. |
| **Follow-up status** | None in the source. |
| **Immunity granted / blocked** | **RULING R4** (Y2K Archaeologist, below). |

| Existing Status | What Happens |
|-----------------|--------------|
| "Y2K Archaeologist" permanent buff | "+1 Nostalgia Resistance (immune to status effects caused by outdated references)" (`design/quests/debaucheryville/brewerytourdebaucheryville.md:409`). Does it make a bro immune to Nostalgic Indigestion? **RULING R4.** |
| Food Poisoning | Existing street-food status: "-2 HP per turn in battle, 50% chance to lose turn", 5-8 battles, "Sketchy street food" (`design/mechanics/Battle/status_effects.md:80-84`). Overlap check for R1. |
| Grease Fingers | Existing fast-food status: "-2 Accuracy, can't use tech items" (`status_effects.md:51-55`). Overlap check for R1. |
| Hungover | Cured by "greasy food" (`status_effects.md:38`); the stand's menu cures it too (`Late-Night Kebab Stand.md:99`). Whether eating there both cures Hungover and gives Nostalgic Indigestion follows from R3. |
| The stand's own menu statuses | Greaseburp, Socially Rejected, Meat Doubt, Bloated/Embarrassed/Confused, Dysentery (Light), Insomniac Clarity, Greasy Coma (`Late-Night Kebab Stand.md:93-130`). Interactions PENDING with R1 and R3. |

---

## 🍺 Intoxication Review

Not intoxicating: the source is food. The bead (Eurobound-tcip) asked for the review on both mechanics, so it is written out below.

### Alcohol Ladder Position (alcohol only)
- **Step**: None (not alcohol).

### No Free Advantage (`design/narrative/bros_choose_debauchery.md`)
Not an intoxicant, so the rule does not bind it directly. If the author gives it a benefit (R1), it needs a cost to match the house rule.

### 10-Point Design Review (`design/mechanics/intoxication_law.md` §8)
| # | Point | Answer |
|---|-------|--------|
| 1 | Source item or drink | The Late-Night Kebab Stand, Club Flyers quest (`club_flyers.md:422-425`). Food, not a drink. Exact trigger: **RULING R3**. |
| 2 | Immediate effect | None in the source; only the gloss "remembering when food didn't cost this much". **RULING R1.** |
| 3 | Escalation conditions | None in the source. PENDING. |
| 4 | Visible player-facing cues | None in the source. PENDING (art/UI); the stand's PNG spec of record is `design/worlds/debaucheryville/PNG_Assets/Late_Night_Kebab_Stand_Complete_PNG_Asset_Requirements.md`. |
| 5 | Effect on player control | None in the source. Depends on R1. |
| 6 | Duration and recovery | None in the source. **RULING R2.** |
| 7 | Comedic consequence | From the source: Y2K-themed kebabs and a vendor who takes them for "those guys from the Matrix" leave the bros with indigestion over what food used to cost. Bro lines and the description line: PENDING (author). |
| 8 | Interaction with other established statuses | Y2K Archaeologist immunity: **RULING R4**. Overlap with Food Poisoning and Grease Fingers, and the Hungover cure: table above, settled by R1 and R3. |
| 9 | Technical implementation dependencies | Proposed engineering work: a status row in `status_effects.json` (empty; schema pending, Eurobound-70z); a trigger at the stand (location id `debaucheryville_velvet_alley_kebab_01`, PNG spec :5) tied to the Club Flyers quest; field and battle handling through `game/core/field_status.gd` and `game/battle/battle_core.gd` once R1 sets the scope. |
| 10 | Requires further author approval? | Yes: R1 effects, polarity, scope and who it hits; R2 length and cure; R3 trigger (and the two Y2K menu items); R4 Y2K Archaeologist immunity. The description line is PENDING content. All four are on the Eurobound Desk as `Eurobound-tcip-q2`. |

---

## 🎨 Visual & Audio Cues

| Cue | Description |
|-----|-------------|
| **Status Icon** | PENDING |
| **Sprite / Particle Effect** | PENDING |
| **Screen Effect** | None in the source |
| **Sound** | PENDING |

---

## 🧾 Master List Entry

Not added yet. Goes into `design/mechanics/Battle/status_effects.md` once R1–R4 are answered:

```
"Nostalgic Indigestion"
    • RULING R1
    • Duration: RULING R2
    • Source: Late-Night Kebab Stand, Club Flyers quest (RULING R3)
    • Cure: RULING R2
    • Special: RULING R4
    • Description: "PENDING (author)"
```

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Master list grepped; no existing status already does this | ☐ depends on R1 (Food Poisoning and Grease Fingers are the nearest) |
| Name and ID unique across the game | ☑ |
| Effects use engine stat names or named mechanics (or marked PROPOSED) | ☐ RULING R1 |
| Duration, sources, cures and stacking rules all stated | ☐ RULING R2–R4 |
| Loss of control is bounded, readable and recoverable | ☐ depends on R1 |
| Intoxication review complete (if intoxicating) | ☑ (not intoxicating; written out anyway) |
| Description line is funny, short, and never explains the joke | ☐ PENDING (author) |
| No real city or place names in the description | ☑ |
| Every unruled value marked PROPOSED | ☑ (marked PENDING / RULING; nothing proposed) |
| Author ruling recorded for a new status | ☑ kept by Eurobound-nda-q6 and Eurobound-tcip; effects ☐ |

---

## 🚫 Warnings & Restrictions

### Content
- [x] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke
- [x] Full-strength MA satire; no softened name
- [x] No moralizing
- [x] The bros are never afraid, disgusted or self-aware about it
- [x] Funny, unique name; no real place names
- [x] No mascots

### Money
- [ ] If R1 gives it a price effect, write it in SOVS

---

## 📝 Development Notes

- Engine dependencies: review point 9. `status_effects.json` schema is pending (Eurobound-70z).
- Open questions for the author: R1–R4, Eurobound Desk `Eurobound-tcip-q2`.

---

## 🔧 Development Status

- **Status**: Drafted (review done; effects PENDING)
- **Entry Location**: `design/mechanics/Battle/status_effects.md` → section set by R1
- **Registered In**: `game/assets/data/skills/status_effects.json` No (schema pending, Eurobound-70z)

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Draft entry and review from the ported source line (Eurobound-tcip) | game-designer agent |
