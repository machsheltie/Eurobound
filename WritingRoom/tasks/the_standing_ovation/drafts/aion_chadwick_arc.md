# Aion — The Chadwick Arc: Camcorder, Napkin, Chain, Tape, Exit

**Round 6 REVISION — Editor Ruling #4 (`aion_chadwick_arc`) applied.** Both mandatory corrections:
1. **5C-2: Chadwick's "That's not an anointing. That's a description." is CUT.** Pilsner's declaration now runs straight into "Nobody fact-checks a legend, Chadwick." — he answers an objection nobody made. Chadwick's backward silent performance follows immediately.
2. **5B VAULT: the claim is now "the footage is never publicly distributed"** (ruling text, verbatim), replacing "the player never sees the footage" everywhere it appeared, including the branch table.

Carried forward unchanged from Phase 5: the in-scene reenactment order-error ("That's not the order." / "Director's cut."), Bradley owning his compromised lines, the PRESS napkin envelope payoff, predictions-not-metrics, the cut German gloss, mechanically distinct Release/Vault flags, and the two-option no-tape D4 exit.

**Reviewer: GLM (state wiring), Kimi (voice/integration).**
Camcorder verified against `design/characters/Chadwick/chadwicksweapons.md`: the "Vintage Camcorder (Chain Attached)" is documented canon. The **seven-character title-generator limit is a PROPOSED device detail**, flagged as such everywhere it appears.

---

## ARC SUMMARY — "DISTRIBUTION DOESN'T EXIST"

Chadwick's whole evening is the gap between *capturing* and *distributing*. He owns a device that records. He does not own a device that converts, edits, uploads, or reaches one viewer. The arc's engine: he treats the tape as an asset whose value compounds daily, because the tape is the one thing in his life that cannot yet be fact-checked. No branch costs a single SOVS. The delusion runs on distribution-free fame.

---

## SCENE 1 — THE PRESS NAPKIN (Act I, Foyer, free)

**Trigger:** Chadwick, filming the foyer, asks Herr Dramatisch for press credentials.

CHADWICK: "I'm going to need press access. I'm media. Internet media. You've probably heard of the channel."

HERR DRAMATISCH: *(beaming, producing a napkin and a rubber stamp from within the cape)* "FINALLY! An American who respects STATIONERY!"

*He stamps the napkin: a single word, in dramatic crimson — **PRESS** — with the theatrical flourish he usually reserves for stamps of TRIUMPH.*

HERR DRAMATISCH: "There. You are now OFFICIALLY accredited by The Standing Ovation. The fee—" *(beat, genuinely disappointed)* "—there is no fee. I would not cheapen the gesture. The gesture is FREE. It is also WORTHLESS. This is called THEATER."

**CHADWICK:** *(filming the napkin)* "Credentials confirmed. Frame that for me. No — with the light. You're losing the light, cape guy."

**Design notes:**
- 0 SOVS. The napkin becomes a **PROPOSED key item: `press_napkin`** — "A house-stamped napkin officially accrediting the bearer as PRESS. Smells faintly of Curtain Call Copper. Legally: a napkin."
- Readers: the envelope beat in 5A, and the Keeper of the Rope's nonviolent resolution (GLM's consolidated sheet §5). Two readers, no fees.

---

## SCENE 2 — THE TITLE GENERATOR (Act I–II, free)

**Setup:** Chadwick opens the camcorder's on-screen title generator to brand his footage. The generator — a period-plausible titling feature, PROPOSED device detail — accepts a maximum of **seven characters**.

He types: **C-H-A-D-W-I-K**

CHADWICK: *(to himself, nodding)* "Chadwik. That's cleaner. Brands better. C-H-A-D-W-I-K."

BRADLEY: "You spelled it wrong."

CHADWICK: "It's a brand decision."

BRADLEY: "It's your name."

CHADWICK: *(closing the menu, definitively)* "Enigma sells."

**Design notes:**
- **CHADWIK** persists as the on-tape title card. In D4, any player who commits to release is committing to releasing footage branded with a misspelled name — he had the option to retype and chose branding.
- Fires once, early, so the payoff has a runway. Never re-typed. Never corrected by anyone whose opinion Chadwick respects (i.e., no one).

---

## SCENE 3 — THE CHAIN-YANK (Act II, D2B only, free)

**Trigger:** Only if the player chose **D2 Branch B (camcorder armed)**. The camera is live when Max reaches the verbatim name exchange (Event 10).

**Beat:** During *"Do I?"*, Chadwick lunges to frame the moment. The camcorder's chain — the documented flail chain — catches on the chair-back/belt hardware, snaps taut, and **wrenches the lens to belt height.**

CHADWICK: *(struggling with the chain, whisper-screaming)* "Not now. NOT NOW. We're capturing history—"

*The tape records exactly: the ceiling of The Standing Ovation. Bradley's rigid playbill. Max's voice, clear as a bell. And Chadwick, off-frame, begging the hardware for one more chance.*

MAX: *(without looking over, mid-exit)* "Tip your server."

**Design notes:**
- `chadwick_tape` (inventory item, per GLM's two-flag architecture — not a flag) is armed only via D2B. In D2A/D2C the camera stays holstered; the chain never yanks.
- The yank never interrupts the verbatim exchange — stage business on top of fixed dialogue.
- §17 compliance: the yank IS the joke. No terminology, no gloss, nothing after "Tip your server."

---

## SCENE 4 — PAYLOAD TABLE (Act III–IV, D2B only)

What the tape actually contains, by D3 branch. Exactly ONE append per branch.

| D3 Branch | Appended to tape | The joke |
|---|---|---|
| **A: Ice Water** | *(nothing — three men drinking water with terrifying discipline)* | The tape's most boring eleven seconds. Chadwick will later describe them as "cinema verité." |
| **B: Drink Through It** | Bradley's drunken "technical clarification" as audio over the belt-height lens staring at nothing | If this tape ever surfaces, Bradley's voice is the story, and it is worse than the picture. |
| **C: Biomechanical Reset** | ONE frame of the chosen disaster (scene-local `reset_method` enum: press/wallsit/wedge — not persistent flags, per GLM's audit) | One perfectly-timed still. The exact frame a real viral clip would loop. |

---

## SCENE 5 — D4: THE EXIT (free, all branches)

Per q8 (Option B, binding): a "post" means Chadwick **commits to releasing the recording** — no instant upload, no new services, no invented locations. The tape stays on the camcorder.

### Branch shape by tape state

**If `chadwick_tape` is in inventory** — the player chooses RELEASE or VAULT (5A/5B). The branches are not flavor variants:

| | RELEASE | VAULT |
|---|---|---|
| Flag | `sinfonia.ovation.footage_release_planned = true` | `sinfonia.ovation.footage_vaulted = true` |
| Future reader | **The Axed Critic's Eager state, anywhere in the district** (GLM §1: he opens by begging for syndication rights to tape nobody has seen — the player did nothing but tell the truth to a camcorder) | **None.** The Critic stays bitter and unemployed. |
| Next-day beat | The escalating metrics-narration fires (predictions only) | Never fires. The footage is never publicly distributed. |
| Delusion fed | The premiere that cannot happen | The leverage that does not exist |
| What the player bought | A future consequence (rumor, not publication — the flag never means upload) | Suppression: Bradley's worst eleven seconds are never publicly distributed |

**If no tape (D2A/D2C)** — the player chooses which record of the evening survives (5C).

### 5A — RELEASE

*Chadwick slides the tape into an unmarked envelope. He considers. He slides the PRESS napkin in after it. He immediately retrieves the napkin.*

CHADWICK: "Credentials stay with the journalist."

*(Envelope into his jacket. He pats the jacket.)*

CHADWICK: "Kubrick sat on 2001 for four years. This is my 2001."

BRADLEY: "You just put it in your jacket."

CHADWICK: "In an ENVELOPE. Distribution is a process. Premières need anticipation. I'm dropping it Friday."

PILSNER: "Dropping it where?"

CHADWICK: "Everywhere. Once the transfer's handled. It's handled. It's being handled. Friday."

- **Flag:** `sinfonia.ovation.footage_release_planned = true` (PROPOSED, persistent — it has real readers outside the scene).
- **The next-day offscreen beat (PROPOSED ambient, release only, fires once per in-game day, max three):** asked how the premiere went, Chadwick does not check the tape — he NARRATES its projected metrics, escalating, about footage nobody including him has watched:
  - First ask: "Projecting sixty views by lunch. It's pacing like a slow burn."
  - Second ask: "Three hundred, conservative ceiling. The algorithm finds the real ones."
  - Third ask: "A million. Roughly. I'm not reading the comments, that's for the next team."
- Every number is a prediction in his mouth. No upload occurs. `footage_posted` is never set.

### 5B — VAULT

CHADWICK: *(weighing the tape in his palm like a warhead)* "You don't release this. You don't EVER release this. This is leverage. This is a retirement plan. Do you know what a guy with MY following could do with eleven seconds of THIS?"

BRADLEY: "Delete it."

CHADWICK: "It goes in the vault."

BRADLEY: "Your sock is not a vault."

CHADWICK: *(taping it into the sock, on camera, which defeats the purpose of a vault)* "The sock is a PROTOCOL."

PILSNER: "Show us."

CHADWICK: "You don't have clearance."

- **Flag:** `sinfonia.ovation.footage_vaulted = true` (PROPOSED, persistent — mutual exclusion with release; prevents any later "you promised us the tape" continuity error).
- **Mechanical/narrative difference honored:** no premiere, no metrics beat, no Critic reader. The vault's suppression is REAL — **the footage is never publicly distributed**, on any branch, by anyone. The payoff is total suppression plus Chadwick's leverage fantasies. Bradley's worst moment becomes an asset Chadwick can neither spend nor show.

### 5C — NO TAPE: THE TWO RECORDS (player choice)

*On the street walk back. Chadwick has no footage. Only one copy of the event exists, and it's him. Two men want to be the copy.*

> **[Let Chadwick perform the encounter.]**
> **[Keep walking. Pilsner delivers the official version.]**

#### 5C-1 — The Reenactment

Chadwick performs it from memory. Full commitment. Chain as prop.

CHADWICK: *(as Max, one eyebrow raised, examining his rings)* "'Apparently somebody here is more progressive than he thought.'"

*(as himself, stunned, gripping the chain)* "'...What?'"

*(as Max)* "'Nothing.'"

*(as himself)* "'WHAT?'"

BRADLEY: "That's not the order."

CHADWICK: "Director's cut."

*(He continues. As Max, to Bradley:)*

CHADWICK: "'Don't ruin it by speaking.'"

BRADLEY: "Yes."

*(A beat. The status handles the review.)*

BRADLEY: "Yes, please."

*(Chadwick takes a bow to an audience of two. The street provides no applause. He waits. The street continues to provide no applause.)*

CHADWICK: "Tough room. Euro audiences are like that."

*(He clicks an imaginary tally light on and off. Nothing records.)*

**Design notes:**
- The wrong order is now in-scene business, flagged by the mandatory exchange — never readable as the original scene.
- Bradley's "Yes." / "Yes, please." are his canon compromised-dialogue options; the status does the performance notes. Chadwick reviewing himself is gone.
- Pilsner's former topper ("He's got you there…") is cut per §17: the punchline is Bradley's second "yes," and the line after it explained the joke.

#### 5C-2 — The Official Version

Pilsner delivers the legend while the bros walk. Bradley corrects the load-bearing errors. Chadwick, denied the stage, performs anyway.

PILSNER: "History will record: the Beer Lord was summoned."

CHADWICK: "We walked to a bar."

PILSNER: "Summoned. The house said my name."

BRADLEY: "They said it once. For money."

PILSNER: "For posterity. And Max anointed a knight of the realm. Nobody fact-checks a legend, Chadwick."

*(Chadwick, denied the reenactment, performs it anyway — silently, mouthing all four parts, walking backward in front of them.)*

BRADLEY: "Pole."

*(The pole does its work. From the ground:)*

CHADWICK: "I got that."

**Design notes:**
- **The anointing exchange is cut (Editor Ruling #4):** Chadwick's "That's not an anointing. That's a description." made him the room's sharpest critic. Pilsner now dismisses the objection nobody made, and the physical ending (the backward pole-walk) lands without a commentary line in front of it.
- A genuine choice, not menu padding: two comedy forms — Chadwick's one-man theater vs. Pilsner's mythmaking with Bradley as reluctant fact-checker. Both free, both escalate, neither humiliates anyone but its performer.
- "I got that." — he claims capture of an unrecorded fall. The camcorder stays holstered; no tape is created post-hoc (the tape architecture stays clean: D2B-only).
- The branches share the walk's final beat with 5A/5B exits; no additional ending follows.

---

## NOTES FOR REVIEWERS

**GLM (state):**
1. Register synced to your architecture: two persistent footage flags, `chadwick_tape`/`receipt_producers_circle`/`relic_claim_ticket` as inventory items, `reset_method` as scene-local enum. Your `rope_resolved` / `palate_respected` first-clear gates are carried in my register.
2. 5A/5B difference table above — confirm the Critic Eager wiring reads off `footage_release_planned` only, and that VAULT triggers nothing.
3. 5C-2 creates no tape and sets no flags; confirm no reader expects one.

**Kimi (integration):**
1. 5C is now a two-option choice; the spine's §11 marker ("REENACTMENT as the full no-tape exit") should read "AION 5C — the two records."
2. The reenactment's misordered exchange is the joke; do not "correct" it to match the fixed scene (ruling `kimi_five_fixes` NOTE).
3. Both 5C branches end on the street; no second Pilsner speech, no Max callback (your polish note 5 stands).
4. **New (overnight):** D4's threshold staging now feeds D5 — per the corrected break, the street exit plays under the marquee *before* departure, so 5C-2's walk must end back at the stage door, not at the hostel. Flagging so integration doesn't splice the old street ending after Jenna's invitation.
