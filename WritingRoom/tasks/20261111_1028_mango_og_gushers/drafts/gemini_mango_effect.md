# PROPOSED EFFECT DESIGN: MANGO OG GUSHERS™

> **Status:** PROPOSED item effect design for MANGO OG GUSHERS™ (sibling product to STRAWBERRY SHORTCAKE SPEEDCAKES™).
> **Author Mandate:** Desk request 0tunrztx34zkyuq97j5l ("A + room drafts the effect").
> **Design References:** `design/items/general_items/strawberry_shortcake_speedcakes_item.md`, `design/mechanics/intoxication_law.md`, `design/narrative/bros_choose_debauchery.md`.

---

## 🎭 The Deception (The Three Questions)

| Question | Detail |
|---|---|
| **What does the bro THINK he's getting?** | A "calibrating, terpene-enhanced creative flow-state" that unlocks effortless European chill, deep philosophical gravitas, and smooth social swagger without any calories. |
| **What does he ACTUALLY get?** | "Gush-Locked" (a heavy, paralyzing couch-lock stone where his brain floats away, his mouth turns into bone-dry sand, and he fixates on trivial nonsense while completely unable to execute basic physical momentum). |
| **The Comedy Gap (Gameplay Consequence)** | Instead of sophisticated European cool, the bro experiences profound inertia. In the overworld, he gets glued to arbitrary scenery pondering deep absurdities. In combat, his attacks become completely toothless slow-motion "bonding gestures" that pacify enemies instead of damaging them, leaving him ravenous and broke afterwards. |

---

## 💨 Proposed Status: "Gush-Locked"

A distinct, stoned mirror image of Speedcakes' "Sugar Rush Hour". Where Speedcakes causes manic hyperactivity, frantic cleaning, and stolen Bravado, Mango OG Gushers causes heavy inertia, over-philosophizing, pacification, and catastrophic munchies.

### Immediate In-Battle Mechanics
- **Status Name:** "Gush-Locked" (Unique in repo; distinct from generic Sleep or Paralyze).
- **Primary Modifiers:** +Defense (he is too limp/numb to care about hits), −Speed, −Accuracy.
- **Battle Pacification ("Contact High / Deep Chill"):**
  - Instead of hitting for standard physical damage, the bro's regular attacks turn into sluggish, uncoordinated attempts to vibe with or deeply appreciate the target.
  - Deals drastically reduced physical damage (TBD balancing pass).
  - Inflicts a chance of **"Pacified" / "Mellowed"** on the target enemy (enemy skips next turn or deals reduced damage because the bro's overwhelming lethargy and unblinking stare are socially disarming).
  - **No Free Bravado:** Unlike Speedcakes (which siphons enemy Bravado), Mango OG Gushers drains the bro's own Bravado over time as he realizes nothing matters.

### Overworld Loss of Control
- **"The Stare" / Scenery Fixation:**
  - At bounded intervals while walking the overworld, the bro abruptly stops moving for 2–3 seconds to inspect an absurd environmental detail (a peeling flyer, a discarded doner wrapper, a blinking streetlamp) while muttering an unprompted "epiphany" box.
  - Movement temporarily locks, then releases immediately without softlocking.
- **Hostel Rest Morning-After Consequence:**
  - If resting at a hostel while Gush-Locked, the party wakes up to the **"Munchies Tax"**: a random edible/consumable food item in the inventory has vanished, or a small handful of SOVS are gone from the bro ordering room service/delivery in a blackout stupor.

### The Comedown ("Cottonmouth Crash")
- When "Gush-Locked" expires:
  - Immediately transitions into **"Cottonmouth"** (or feeds into existing "Crash"): -1 to all stats, dialogue choices scrambled with thirsty demands for liquid, unable to use spoken Bravado abilities until drinking a beverage consumable.

---

## 📝 Battle Text Lines (2 Short Lines)

| # | Line | Status |
|---|------|--------|
| 1 | `[BRO] slowly touches [ENEMY]'s shoulder and whispers, "We don't need to fight, man. Look at your elbows." [ENEMY] is completely baffled.` | PROPOSED |
| 2 | `[BRO] takes a massive swing at [ENEMY], forgets why his arm is up, and just leaves it there. [ENEMY] lowers their weapon out of second-hand awkwardness.` | PROPOSED |

---

## 🔍 Alternative Inspect Microcopy (1 Short Line)

> Author standard: short, biting, junk-rewarding microcopy with teeth.

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | `"0% fruit juice. 100% legal panic."` | PROPOSED |

*(Alternative backup: `"Smells like mango candy and three missed court dates."`)*

---

## 🍺 10-Point Intoxication Law Review (`design/mechanics/intoxication_law.md` §8)

1. **Source item or drink:** MANGO OG GUSHERS™, bought from Tony420 over ICQ (paid in VapeSwap $HUFF, dead drop delivery).
2. **Immediate effect:** Inflicts status **"Gush-Locked"** (+Defense, −Speed, −Accuracy, physical attacks convert to lethargic pacification hits).
3. **Escalation conditions:** Hitting the vape again extends duration and stacks the impending Cottonmouth/Crash. Mixing with alcohol accelerates Beer Goggles straight into Shitfaced (cross-fading bypasses Buzzed).
4. **Visible player-facing cues:** Bro's sprite develops droopy half-lidded eyes, text scroll slows down to a crawl with trailing ellipses ("bro..."), a tropical smoke cloud particle follows the bro.
5. **Effect on player control:** Bounded overworld stops where the bro locks up to stare at scenery for 2 seconds. In battle, player still commands actions, but basic attacks become sluggish pacifying attempts.
6. **Duration and recovery:** Bounded turn duration in combat / step count in overworld; recovery triggers "Cottonmouth Crash" or clears after consuming a drink/resting.
7. **Comedic consequence:** The bro thinks he's displaying magnetic zen maturity; he is actually standing motionless in front of an alley dumpster talking about geometry, and wakes up having eaten the party's trail rations.
8. **Interaction with other established statuses:**
   - **Alcohol ladder:** Cross-fade effect skips a tier upward.
   - **Hungover:** Temporarily masks the penalty, but doubles the subsequent Cottonmouth thirst.
   - **Sugar Rush Hour:** Cancels out Speedcakes into a catastrophic confused twitching state.
9. **Technical implementation dependencies:** Requires custom combat attack resolution (physical attack converts to damage reduction + enemy turn-skip debuff chance) and overworld micro-pause script hook.
10. **Requires further author approval?** Yes. Status name ("Gush-Locked"), pacification attack conversion, overworld stop mechanic, and balancing numbers remain PROPOSED pending author review.
