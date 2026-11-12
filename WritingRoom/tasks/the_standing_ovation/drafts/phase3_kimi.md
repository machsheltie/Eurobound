# PHASE 3 — STORY AND GAMEPLAY BREAK (Kimi)

Lane: character, dialogue, stagecraft. Architecture only; no integrated quest scene. Everything new is **PROPOSED** pending editor/author review. This does not claim the consolidator role; that belongs to the actual last speaker.

## 0. Structural position

Adopt GLM's one-evening frame and Aion's conditional-tape amendments, with three corrections:

1. **The fixed Max encounter is a no-choice runway.** Do not interrupt events 3–11 with a menu, a second crowd-work scene, or extra business in every branch. The only conditional physical business is the D2B-armed camcorder chain after “Do I?”; the spoken exchange remains unchanged.
2. **D4 is a real choice only when a tape exists.** In D2A/D2C there is no post/vault menu and no imaginary tape to vault. Chadwick automatically supplies the memory reenactment. This preserves agency by not disguising a branch lock as a decision.
3. **The drink branch needs an exact bill, not “about 24 SOVS.”** Use **two servings of the existing menu item The Encore, 10 SOVS each = 20 SOVS**, both ordered for Bradley. Each arrives with the existing staff ovation. No invented drink, mandatory tip, or drink sent to Max. The two-drink threshold for suppression is a proposed quest-local tuning value; the exact +10 Confidence / −25 Concentration copy never changes.

Result: four primary decisions, three of which have mechanical/state consequences, a completely free entertaining route, and two nonfinancial escalation engines (crowd work and Bradley's physical cover-up).

## 1. Beat order and fixed-event runway

| Stage | Content | Player control / consequence |
|---|---|---|
| 0. Opera District, pre-show | Optional ambient encounters; venue establishes that the revue is excellent and the ropes are decorative | Observation can avoid the rare rope encounter entirely; no combat gates entry |
| 1. Entry / D1 | Standard table vs. Producer's Circle; free Legends Wall is scenery only | Cost, receipt, announcement, two later dialogue variants |
| 2. Revue, first half | Max owns the room; Chelsea and the twins receive a small number of complete, excellent routines; required events 1–2 occur here | No combat and no player-authored performance |
| 3. Revue crowd work / D2 | One short Jenna/Barbara-led interaction while Max controls the room | Pilsner onstage / Chadwick's camcorder / restraint; only the camcorder branch creates a tape |
| 4. Finale | Performer-owned curtain call; APPLAUSE sign lights after the room is already standing | No extra Pilsner mic grab; show ends cleanly |
| 5. Post-show fixed encounter | Required events 3–11, exactly in the order below | No choice menu until Max has moved on; D2B alone arms the belt-height recording |
| 6. Immediate bro aftermath | Dossier §14 PHILLIP pile-on verbatim; status UI; D3 coping | Free water / 20-SOVS drink / free white-knuckle; compromised dialogue in all three |
| 7. Exit / D4 | Tape decision if and only if D2B; otherwise reenactment; optional ambient encounters | Release commitment vs. vault; upload and audience response are delayed, never wireless or instantaneous |

### Required events, locked in sequence

1. Bros attend the spectacular First Daughters revue.
2. Pilsner recognizes the period political celebrities and wildly overvalues that knowledge. “Who is Bush?” supplies the age collision; it does not produce acceptance or a lesson.
3. Max meets the bros after the show.
4. Max names Pilsner **Beer Lord**.
5. Max says **“And Basketball Jersey. You're cute.”** and **“Don't ruin it by speaking.”**
6. Bradley's body reacts visibly before Max comments: the playbill drops to belt level with both hands. No spoken line causes the “Oh.”
7. Verbatim: **“Oh.” / “What?” / “Nothing.” / “What?” / “Apparently somebody here is more progressive than he thought.”**
8. Max nicknames Bradley **Trouser Snake**. The status copy uses the exact supplied values and compromised-dialogue language.
9. Chadwick receives no nickname.
10. Verbatim deliberate exchange: **“What did you say your name was again?” / “Chadwick.” / “Right.” / “You know my name.” / “Do I?”** The two intermediate responses from the established exchange are retained; the three required lines are not paraphrased.
11. Max moves on with their evening: one professional emergency at the bar, then the queens' food argument and garnish theft. No poker/casino material, return visit, counseling, or romantic prize.

The dossier §16 optional ordering is superseded by the brief's numbered events and editor note 11: Chadwick's denial follows Trouser Snake. Max's initial read stays private to Max and the bros. Later public attention can result only from the player's crowd-work, Reset, or publicity choices.

## 2. Decision/state architecture

Working flag aliases below expand to the mandatory namespace `sinfonia.standing_ovation.<flag>` in the final technical table. They are design flags only; `data/quests/flags.json` does not yet exist.

| Decision | Options | Immediate state and cost | Later payload |
|---|---|---|---|
| **D1 — Seating** | **Producer's Circle** / **Wing Position** | Circle: `d1_producer_circle`, 72 SOVS, receipt, pre-show announcement, “Only one name was supplied.” Wing: `d1_wing_position`, 0 SOVS, tactical-sightlines rationalization and failed nine-second attempt to film somebody else's acknowledgment | Circle changes Max's approach to “You heard your name and remained seated”; Wing gets the delegation/doubling-back approach. Beer Lord itself is never purchase-dependent |
| **D2 — Crowd work** | **Send Pilsner** / **Deploy camcorder** / **Stay seated** | A: `d2_pilsner_onstage`, fake-ID/puka-shell humiliation, 0 SOVS; proposed comped `the_understudy` only if approved. B: `d2_camcorder_deployed` + `tape_exists`, Jenna turns the obsolete rig into her prop, then Chadwick keeps rolling for “B-roll.” C: `d2_pilsner_validated`, 0 SOVS, no tape, one correct answer and one delighted Max line | A supplies public humiliation and the comp/retelling. B alone unlocks D4 post/vault. C supplies “That was the correct amount of useless,” followed by Pilsner inventing a consulting career on the walk home |
| **D3 — Bradley copes** | **Water** / **Drink through it** / **White-knuckle** | Water: `aftermath_water`, 0 SOVS, full status. Drink: `aftermath_drinks`, 20 SOVS, `TS_SUPPRESSED` presentation stage + proposed ordinary intoxication; attraction and nickname unchanged. White-knuckle: `aftermath_white_knuckle` + one cosmetic `reset_*` variant, 0 SOVS, full status | All three retain compromised dialogue. If tape exists: drink appends the “technical clarification” audio; white-knuckle appends one physical-disaster frame; water appends nothing. No Reset option is optimal |
| **D4 — Tape, only if `tape_exists`** | **Commit to post** / **Vault** | Post: `footage_release_committed`, 0 SOVS tonight; CHADWIK title card and “Premieres Friday.” Vault: `footage_vaulted`; memory reenactment fires. Without a tape, only `no_tape` + reenactment | After a plausible transfer/upload, set delayed `footage_posted`; next-day metrics/comments and eager-critic publicity variant follow. Vault/no-tape never generate those results. Transfer method is q8, pending |

Additional rulings on state:

- D1 options are mutually exclusive; D2 options are mutually exclusive; exactly one `aftermath_*` is set.
- The Reset is a cosmetic execution choice nested inside D3C, **not** a fifth primary decision and not a puzzle with a correct maneuver.
- `TS_SUPPRESSED` does not swap, clear, or remap the supplied +10/−25 values. It marks reduced immediate physical/social presentation while judgment worsens. Engine implementation beyond scene dialogue is proposed.
- No same-night views, likes, upload, livestream, or audience comments. “Brenda's mom liked it” remains cut as invented marital backstory.
- Minimum quest spend: **0 SOVS**. Maximum planned quest spend before any optional ordinary drinking/ambient activity: **92 SOVS** (72 Circle + 20 drink). No mandatory cover, applause levy, camera license, inscription, certificate, or final bill.

## 3. The single vanity purchase

**Lock the Producer's Circle, with the Legends Wall free and non-purchasable, unless Gemini supplies a new structural objection.**

The Circle earns its place on two genuine payoffs, not on an inflated dependency list:

1. The announcement / Chadwick half-rise / “Only one name was supplied.”
2. Max's conditional “You heard your name and remained seated.”

The central character contrast is larger than the receipt: Pilsner pays to hear **Lord Pilsner**, then prizes Max's unsolicited, more devastating **Beer Lord** more highly. Keep Bradley's pre-purchase arithmetic and the optional receipt; cut Pilsner's spoken third explanation of the 48-SOVS acknowledgment.

The wall's “THE AMERICANS — RETURNING CHAMPIONS, ANNUAL SINCE 1994” does its work for free. No wall purchase, no self-inscribed vandalism, no second prestige system after the climax.

## 4. Six live disputes — positions

1. **CHADWIK: camcorder title generator.** Seven-character field, eight-letter CHADWICK, output CHADWIK; he can retype it and chooses “Enigma sells.” The exact field limitation is a proposed device detail to state once, not an existing canon specification. Aion's handwritten-wall version is withdrawn for good reason.
2. **Critic: fixed drop; publicity changes dialogue/behavior, not respect.** GLM's Circle → retraction telemetry is rejected. A purchase cannot make the critic deferential. If `footage_posted` eventually becomes true, the critic becomes more eager to print because he witnessed/published a fiasco. Keep the drop fixed and resolvable; do not add a conditional drop table for this joke.
3. **Transfer: q8 filed.** Recommendation is existing **Dieter “Decibel” Krause at Bassline**, who already runs sound and sells night equipment, adding a proposed next-day tape-capture/upload service. This reuses an established person/location and avoids inventing a Plaza kiosk or cybercafé. Fallback is an entirely offscreen next-day errand. No transfer location or hardware is canon until answered.
4. **Toast Immortal and every successor mic grab: cut.** A third spotlight invasion is accumulation, not escalation, and endangers the private cover-up. Pilsner already has D2A, D2C, and his D3A silence supervision.
5. **Genuine-win trivia: election-night 2000 broadcast sequence, not the broken film dates and not a fabricated VNS quotation.** Pilsner correctly remembers that Florida was projected for Gore, retracted, projected for Bush, and retracted again, because he stayed up for the whole sequence. Broadcast facts only, no partisan opinion. Do not print GLM's “VNS projects Florida for — hold it — hold it” as if it were a verified archival quote. The twins' “Florida's still counting” is a curtain joke; Pilsner's is tedious lived expertise. Baha Men's “You All Dat” (2001) remains a valid period fallback, but not as an answer to a question specifically about 2000.
6. **Chain-decides-the-frame: adopt only under Aion's D2B causality.** The camera is hot because Chadwick elected B-roll after Jenna's crowd work. After “Do I?”, the chain wrenches the lens to belt height without changing the fixed dialogue. The tape captures Bradley's cover-up, Max's clear audio, Chadwick's needy off-camera voice, and “Tip your server.” D3 changes at most one appended payload. This is what makes D2B and D3 materially change D4 rather than recoloring an identical exit.

## 5. Character and stagecraft guardrails for drafting

- **The revue is not a delivery system for bro humiliation.** Select a few complete performer-owned routines. Keep Chelsea's technical precision, Jenna's aggressive physical confidence, and Barbara's surgical stillness distinct. No concatenation of every audition costume, lyric, and blackout gag.
- **Pilsner's recognition is real; his inferred status is false.** He can be right about Chelsea, the twins, and the broadcast calls while being completely wrong that this makes him a producer, consultant, or historical witness of interest to anybody.
- **Bradley is less articulate, not less intelligent.** Give him one accurate physical read of the choreography, then bad mechanics: denim bunching, leg-day backlog, vasoconstriction, alignment, leverage. No polished discussion of gender, identity, progress, or transformation.
- **The status is inconvenience, not punishment for attraction.** Max is genuinely desirable. Bradley's panic and cover-up are the joke; his attraction is not. No diagnosis, cure, identity label, or moral resolution.
- **Max does not become an insult turret.** Preserve “God, you're serious” / “I am. That's on me” because it lets them be caught off guard. Give them one exit reason, not three successive exits: the cape/chair-routine professional emergency is sufficient. A monitor note can happen during their working room management, not as a second farewell.
- **The queens continue their evening.** “It had olives” / “It had three olives” stays as ambient life. Max never returns to supervise D3 or D4.
- **Chadwick's technology causes a bad decision.** “Dogme 95. No tripod. No rules,” CHADWIK, and announcing a Friday premiere for an undigitized tape all come from relevance hunger. He never becomes a competent contemporary distributor or a perceptive generational straight man.
- **PHILLIP is scoped to the author-written roast.** No surname, expanded home biography, or general civilian-name retrofit.

## 6. Enemy roster / m1 slot map

Names and statistics remain provisional under q4; full current-engine and proposed-full-design entries are a Phase 4 responsibility. Repository search found no design-side collisions for the five working IDs.

| m1 slot | Working enemy | Location and one-line gameplay identity |
|---|---|---|
| Common | **The Axed Critic** (`axed_critic`) | Outside in the venue queue lane; unemployed reviewer writing a real-time pan of the bros in 2000-era entertainment-media register. Owns the period-reference and ego/humiliation requirements without anachronizing a contemporary NPC |
| Status manipulation | **Supernumerary Ambitieux** (`supernumerary_ambitieux`) | Wings-side pre-show queue; nine seasons as a non-speaking courtier, escalating posture/bow corrections and composure damage; digs in defensively as the fight continues |
| Group / reinforcement | **The Second Chair** (`second_chair_bassoonist`) | Alley smoke break; assistant-principal bassoonist whose flat notes call in opinionated reed-section reinforcements; burst the caller down or control the section |
| Rare / unusual | **Keeper of the Rope** (`velvet_rope_paladin`) | Exterior decorative rope; manifests only if a bro touches/crosses the rope that guards nothing. Observation and restraint are literal counterplay |
| Elite / mini-boss | **The Keg-Acolyte** (`dramatisch_keg_acolyte`) | Green Room door between tours; one obsessive cellar-hand, not an order or Dramatisch faction. Siphon attacks build a foam meter; at maximum he salutes the bros' head retention and politely leaves mid-fight |

Mechanics-as-comedy: Keeper + Keg-Acolyte. Ego/social humiliation: Critic + Supernumerary. Period reference: Critic. All are ambient before/after the revue, none are required quest gates, and none fight during the performance.

**Engine correction endorsed:** GLM verified that current `DataRepo` hardcodes Debaucheryville paths and never reads Sinfonia's enemy file; `grant_rewards()` also applies one drop unconditionally and ignores `drop_chance`. Therefore valid current-schema entries are only data specs. Encounter loading, actual drop rolls, party combat, AI, statuses, and animations must all be costed as proposed engine work, not promised as current functionality.

## 7. Drafting and review allocation

GLM's table is accepted with the missing profile/item/post-credits responsibilities made explicit:

| Section | Primary | Reviewer | Path |
|---|---|---|---|
| Quest frame/template, D1/state tables, pre-show street, five full enemy entries and current/proposed engine contract | GLM | Gemini (enemies), Kimi (frame) | `drafts/quest_frame.md`, `drafts/enemies_and_preshow.md` |
| Revue acts, D2 staging, announcer/free wall, **Chelsea/Jenna/Barbara mandatory NPC profiles** | Gemini | Kimi | `drafts/show_acts.md`, `drafts/performer_profiles.md` |
| Fixed post-show dossier scene, PHILLIP aftermath, D3 and status presentation | Kimi | Aion | `drafts/dossier_scene.md` |
| Chadwick arc, chain/CHADWIK/PRESS napkin, D4 delayed fuse + reenactment, next-day/post-credits payoff, related item specs, continuity register and implementation dependencies | Aion | GLM | `drafts/chadwick_arc.md`, `drafts/continuity.md` |
| Integration into mandatory sidequest-template structure | Kimi | all four | `final.md` |

No section should begin until the editor reviews this break.

## 8. Open author dependencies (not silently resolved)

- **q8:** Dieter capture/upload service vs. offscreen errand vs. new Plaza kiosk. Recommendation: Dieter.
- Proposed comped `the_understudy` in D2A and the free PRESS napkin need confirmation; neither may become a hidden fee.
- Producer's Circle price/receipt item, quest flags, status implementation, item specs, and all enemy names/statistics remain proposals through normal review.
- Final enemy names are reviewed only after full entries, per q4.
