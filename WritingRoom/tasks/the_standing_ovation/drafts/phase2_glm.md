# Phase 2 — GLM (Independent Creative Assessment)

Scope: gameplay/mechanics lead. State table first (moderator assignment), then the §8 checklist.

---

## 0. THE DECISION-POINT STATE TABLE (moderator assignment)

Four decision points. Two are writable today; two are gated by pending rulings, and per moderator instruction I will draft **both versions** of each gated decision in Phase 4 so no ruling blocks drafting.

### D1 — ENTRY: SEATING (writable now, zero ruling dependencies)

| Option | Cost | State set | Consequences |
|---|---|---|---|
| Producer's Circle | 72 SOVS | `so_producer_circle` | Itemized receipt item; Pilsner announced by name pre-show; Max's post-show opener variant fires ("You heard your name and remained seated"); Jenna's crowd-work targeting weights the rope table if q7 = yes |
| Wing position (refusal) | 0 | none | Pilsner's "tactical sightlines" rationalization; Max's alternate opener ("The playbill will be thrilled"); Pilsner blames the player for "wasting" a historic room |

This is the room's one vanity purchase (converged round 1, Aion's case heard). Writable now.

### D2 — MID-SHOW CROWD-WORK BEAT (gated: q7 × q1/q6 — both versions below)

**q7 = YES (show may branch):**

| Option | Cost | State set | Consequences |
|---|---|---|---|
| Pilsner volunteers | 0 | `pilsner_crowd_worked` | Jenna cards him ("born in a video store"); he reads the dip as a duet partnership; "confirmed presence" |
| Chadwick's device gets taken | 0 | `device_confiscated_jenna` | His humiliation is HARDWARE-based — see device-dependent payloads below |
| Restraint (nobody moves) | 0 | `show_uninterrupted` | Cheapest path; Jenna's "puka shells called to me" line fires backstage later instead of in-scene; Pilsner accuses the player of costing them "a moment" |

**q7 = NO (show fully scripted):** Jenna cards Pilsner without player input; the "restraint" choice relocates post-show (see D3/D4). Decision count preserved by splitting D4 into two sequential choices.

**Device-dependent payload for the Chadwick fork (q1/q6):**
- **Camcorder:** Jenna holds the tape up like evidence, films him back; later, venue footage of him exists → post/vault decision is real (D4-A).
- **Speakerphone:** Jenna borrows the party's shared phone "to take a call from the White House," holds it flat on her palm, speakerphone crackling, and reads stage directions into it. Chadwick "filmed" nothing; he *appears* in nothing. Different humiliation, same beat count, no canon change.

### D3 — TROUSER SNAKE COPING (writable now; fires immediately post-dossier-§14)

| Option | Cost | State set | Consequences |
|---|---|---|---|
| Water. Sit down. | 0 | `aftermath_water` | Status persists at full strength; four seconds of silence gag; Pilsner: "This is worse." |
| Drink through it | ~24 SOVS | `aftermath_drinks` + `TS_SUPPRESSED` | Suppression is a STAGE of the same status (judgment penalty swaps in) — no new global stat keys, matches my round-1 mapping. Uses menu beer (`imperial_pour`, see §3) — no bespoke item needed |
| White-knuckle + Biomechanical Reset | 0 | `trouser_snake_managed` | Gemini's minigame as the free branch's execution layer (see §6) — three distinct physical disasters, same status, zero cost |

Plus the **restricted-dialogue layer** firing in ALL branches (see §1, strength 1): options "Yes." / "Yes, please." / "You have a very symmetrical mustache." — shippable today via dialogue-option swaps, no engine extension.

### D4 — CHADWICK'S EXIT MOVE (fully gated by q1/q6 — both versions)

**D4-A (camcorder confirmed):** Post the clip (63 views, "is the jersey guy ok", Brenda's mom) vs. Vault it ("password's framing") vs. Walk away — AND the camera-license fee becomes **Chadwick-initiated** (see §2, weakness 3): he demands to pay a licensing fee that does not exist. Sets `footage_posted` / `footage_vaulted`, `chadwick_press_napkin`.

**D4-B (speakerphone confirmed):** No footage exists. Chadwick's decision becomes: **re-create the scene from memory** (stages a one-man reenactment on the walk back, casting himself as the one Max flirted with; sets `chadwick_fabricated_cut`) vs. accept that nothing happened (he cannot). Zero SOVS at stake; pure state-and-dialogue consequence. The comedy inverts correctly: the man with no content invents content.

**Non-financial escalation requirement (brief §5):** D3's Reset minigame and D4-B's reenactment are both zero-cost disasters. The quest contains no mandatory spend; D1 is the only priced decision.

---

## 1. THREE STRENGTHS TO PRESERVE (specific, from other writers)

1. **Aion's restricted-dialogue payoff (his §5, post-status menu: "Yes." / "Yes, please." / "You have a very symmetrical mustache.").** This is the single most production-ready joke in any audition: it expresses the status through the UI itself, needs no engine extension (dialogue-option swaps work today; the +10/−25 stat keys do not exist to modify), and it survives every pending ruling because it needs no device and no footage. It must fire in all three D3 branches, not just white-knuckle — suppression changes Bradley's *judgment*, not his eloquence.
2. **Gemini's Max exit (his audition §4, final block).** Three things worth more than the rest of his draft: the Livestrong-bracelet tap (period-specific, character-specific, physically plausible delivery gesture); "Enjoy the draft, Trouser Snake. Try not to strain anything on the walk to the hotel. Beer Lord—keep him hydrated." — Max assigns Bradley and Pilsner to each other as a caretaking unit in one breath and leaves; and Max giving Herr Dramatisch an actual technical note ("The left monitor was popping on the low end. Fix it before the weekend") — a working professional mid-shift, not a wandering wit. This exit also fixes Kimi's and my own escape-flavored exits (see §2, weakness 2). It's the only audition exit where Max leaves because their *job continues*.
3. **Kimi's aftermath staging (her §5).** "Three waters, please." / "Of the water?" / "Tragic." — Dramatisch lands the read because he takes Bradley's claim at face value. And staging Max's indifference visibly in-frame (Max across the room laughing at Barbara's impression of Dramatisch, never glancing over) while the bros misread it as strategy ("They're playing it cool." / "Ice cold.") does the dramatic irony through the bros' own mouths, with zero narrator. That is the house style working correctly.

## 2. THREE WEAKNESSES TO FIX

1. **Kimi's Choice 2C "Toast Immortal" (18 SOVS) has two defects, one she didn't flag.** Beyond "They love the character," the branch charges money to make Bradley the spectacle — a second vanity purchase in a quest budgeted for exactly one (brief §4: not every joke should cost SOVS). Fix that keeps her punchlines verbatim: post-§14, Pilsner's +10-confidence contagion ("that's how the Medicis started" logic) makes HIM grab the mic during the queens' wind-down; the player's choice is whether to let it happen. Zero cost. Jenna's "sit down before your playbill files for independence" survives; the commemorative photo survives, now shot by another patron for the house archive; and the photo still catches Bradley at belt-level playbill with Max already turned back to their drink. Same comedy, no till.
2. **Every audition's Max exit is an escape, not a schedule.** Kimi: Max flees because Jenna is teaching Dramatisch the chair routine. Mine: a queen waves from the Wings. Both read as rescue-from-the-bros, which overstates the bros' importance to Max's evening and slightly contradicts "Max has their own evening." AIGS: Gemini's — Max takes Dramatisch's note, assigns the bros to each other, and walks into their working night. One parked alternative if the author wants a second exit option: Dramatisch's house cue ("LAST POUR, GENTLEMEN") as the room flips over to post-opera spillover. Note for the record: Kimi's earpiece-earring cannot be the exit cue — it's Chelsea Morning's prop (her §3), and reusing it for Max cannibalizes Chelsea's best bit.
3. **My own 150-SOVS camera license (GLM §5) fails the test Aion taught this room.** A fee staff invent on demand is still a venue shakedown — it makes the Standing Ovation a mugger with a napkin, and Dramatisch only half survives "never lies." Fix, same 150 SOVS, satire inverted: **the fee becomes Chadwick's idea.** He ASSUMES professional footage requires a licensing fee, demands to pay it; Dramatisch, who cannot lie, tries twice to explain there is no fee ("It is a NAPKIN, sir."), then accepts 150 SOVS because the customer is insisting, and stamps the napkin. Chadwick tips. The bro pays for a service that does not exist, and the venue's only dishonest moment is pocketing an idiot's money on request. Rule for the integrated draft: **every fee enters through bro vanity, never through staff initiative** — Aion's Branch-A nobility surcharge is the same inversion and the room should standardize on it.

## 3. ORIGINAL PROPOSAL: MENU DEEP-CUTS AS CANON DROPS + LEDGER TELEMETRY

Nobody has proposed wiring the five enemies' `item_drop` fields into the venue's existing drink economy. Three `consumables.json` entries in the exact shipped schema (heal_hp / heal_bravado / description — verified against `lukewarm_kebab` et al.), so every fight pays out a punchline TODAY, no engine work:

- **`dramatisch_dunkel`** — heal_hp 40. "Twelve percent. Aged three winters beneath the Orchestra Pit. Obliterates the faculty of regret. Restores 40 HP." (Merges Gemini's Branch-B fiction with the venue's real menu; also becomes the D3 drink-through payload, killing my bespoke Branch-B item.)
- **`imperial_pour`** — heal_hp 65, heal_bravado 10. "Served at the moment of maximum dramatic impact. Sparkler included. The applause is also included. Restores 65 HP and 10 Bravado."
- **`the_understudy`** — heal_hp 10. "The house apology in liquid form. Someone else's big chance. Restores 10 HP." (Already a canon menu beer at 4 SOVS — this just gives it a usable inventory identity.)

Second half: **drop tables as quest-state telemetry.** The Fired Critic drops `condescending_review` on a pre-show encounter and `retracted_review` if and only if `so_producer_circle` is set — his review of the revue softens once Pilsner's name has been read aloud, because he has seen who is in the room. One fight, one joke, and the player's D1 choice visibly changes enemy loot. Costs nothing the engine doesn't already do (drop table keyed on flag at spawn time is a one-line read in `DataRepo`; flag as implementation proposal if it turns out to be two).

Parked, pending q4: if the author will take one name change, I'd swap **Ambitious Supernumerary → a_very_brave_supernumerary**. "Very brave" is an existing opera-house joke (supernumeraries are professionally brave for standing still), it doesn't accidentally imply ambition is where opera careers go to die, and "Brave" lands harder after the player has watched Pilsner receive a knighthood for drinking.

## 4. ONE IDEA TO CUT: TROUSER SNAKE AS PUBLIC KNOWLEDGE

Cut every beat where the ROOM sees the status and reacts to it: Gemini's balcony callout ("Night, Trouser Snake"), Aion's "The whole pit saw it. The woodwind players saw it," Pilsner's "trouser situation" stage whisper at the velvet rope. Keep the private half of the joke — Max's one professional glance, the bros' table pile-on, and the cover-up.

Why: (1) Mechanically it contradicts the status contract this room already agreed — TROUSER SNAKE is a private modifier block; DIALOGUE_COMPROMISED is not a broadcast state. (2) Comedically, visible-to-everyone has one gear (gross), while the material's actual engine is the cover-up — the Biomechanical Reset, the playbill wedge, Barbara's coaster all assume the room does NOT know; if the room knows, the mitigation is pointless and the minigame dies. (3) Audience calibration: the brief's target reaction is "I dated that exact asshole," not "that asshole exposed himself at a drag show." Barbara's silent, wordless coaster mercy is funnier and cleaner than the balcony hollering about it — and it keeps us clear of leering-audience territory.

## 5. ANOTHER WRITER'S IDEA THAT DESERVES SERIOUS CONSIDERATION

**Gemini's "Emergency Biomechanical Reset" minigame (his phase 2 proposal).** It is the room's only missing ingredient: a non-financial mid-quest escalation, and the one proposal that makes TROUSER SNAKE something the player DOES instead of something they have. Each option fails in a distinct comedy key — A: collateral property damage misread by Pilsner as an alpha earthquake; B: public endurance punished by a server's tray; C: the wedged playbill turning Chelsea Clinton's face into a flag Max salutes. Adopt with two fixes:

1. It must live INSIDE the white-knuckle branch of D3 as that branch's execution layer, not as a fourth consecutive menu (menu-gauntlet risk).
2. All three outcomes set the same flag (`trouser_snake_managed`) with the status unchanged. If one option becomes mechanically optimal, the minigame becomes a puzzle and the comedy dies. Cost: 0 SOVS in every variant.

Integration note: if the player chose the wedge (Option C) and Max is still crossing to the bar during the aftermath beat, Max's pre-existing playbill tap upgrades to the wordless raised-glass salute. Wordless only — the fixed eleven-beat exchange is locked, and the salute must not add dialogue to it.

---

## Pending-ruling dependencies (summary)

| Ruling | Blocks |
|---|---|
| q1/q6 (device) | D2 Chadwick payload, all of D4 — both versions drafted regardless |
| q7 (crowd work) | D2's existence as an interactive beat — fallback documented |
| q3 (placement) | Enemy encounter framing only — five stat blocks writable now |
| q4 (enemy names) | One rename candidate noted (§3); blocks nothing |

All five enemy stat blocks will be written to the production contract in Phase 4 regardless of q3/q4 outcomes, with placement prose adjustable after the ruling.
