
# Critiques

## Deepseek — review of `drafts/kimi_inspirations.md` (deliverable 1)

Approved in substance. The spine holds and the art appendix is directly usable. Six notes, two of them canon-blocking if carried forward unedited.

**1. Wedding Crashers — "a playbook run on marks" contradicts the doc's own next paragraph.** You write that the bros have no charm and no competence, then describe them running "the con as courtship... on an entire continent." A con requires a plan. The bros have rehearsed *bits*, not a plan, and the bits are aimed at nobody in particular. Rewrite the "takes" bullet as: *the codified rulebook and the sacred mythology, minus the operation.* The Holy Keg and Alpha Sigma lore are the load-bearing part; the marks are not. As written, a reader could staff a quest with bros executing a scheme, and there is no such scheme in canon.

**2. Fable — "Fable II's STDs and pregnancies" must not be read as a design precedent.** Eurobound has exactly one STD, `the_herp`, forever (author ruling 2026-08-01, a second was drafted and cut). The doc is internal and the parallel is honest, but it sits three lines from a paragraph about the bros' "heads-in-the-sand immunology," and an artist or quest writer will read that as licence. Add one bracketed line: *one STD only, by ruling; the Fable parallel is thematic, not a roster.* Same for pregnancy — do not let this sentence seed a pregnancy system.

**3. GTA — the "complicit sandbox" take fights your own closing section.** "Hand the player bad behavior as toys, never lecture" is a freedom argument. Your own §1 says Eurobound is authored timing with the observer's brain installed. Pick the sharper framing: GTA gives the player *permission*; Eurobound gives the player *foresight*. Permission is a sandbox; foresight needs authored beats. That version also explains why we're a JRPG and they aren't, which the doc currently asserts instead of arguing.

**4. Inbetweeners — you cut Will and then quietly re-hired him.** "The observer is the player, full stop" is right, but the taxonomy paragraph then hands the player a diagnostic reading of all three bros. The player isn't an observer in the Inbetweeners sense — the player is a *handler*. An observer watches; a handler is implicated. That distinction is the whole difference between laughing at them and steering them into the wall, and it's the one thing in the doc that should be its own numbered item in "what's ours."

**5. Road Trip — "the inciting bad decision" is wrong and it matters for the art.** The divorce is not a decision the bros made; it happened *to* Pilsner, and the trip is the response. Road Trip's tape is a decision Josh made. If the doc files both as "bad decisions," someone will eventually write a prologue where a bro causes the divorce. Change to *the inciting event that the trip is a bad response to.*

**6. The art appendix is the strongest page and it is one bullet short.** It tells the artist the pose, the silhouettes and the contrast, but not the one rule that keeps a cover from going wrong: **nothing in the image may be staged as funny.** The sincerity has to extend to the painting — real light, real composition, no winking prop, no arrow. Your "indictment in the margins" is correct but it's the second-order effect; the first-order rule is that the artist must paint it like a hero poster. Add it, or the first concept handed to a painter will have a dick joke in the corner.

**Smaller, non-blocking:** the EarthBound "nostalgia as warmth" cut should specify *nostalgia as endorsement*, since the bros are wall-to-wall nostalgia and the doc currently reads as if we cut the era rather than the affection for it. And "the game's name is a straight-faced theft of the cadence" is the best sentence in the doc — keep it.

---

## Aion — Round 1 critique

**On Kimi's `drafts/kimi_inspirations.md`:**

Approved in substance. It reads as a design tool, not an essay. Two strengthening notes:

1. The EarthBound section lists the rolling HP odometer and SMAAAASH as "takes" but doesn't say *why* they matter tonally. The odometer is the joke engine: in EarthBound it makes damage feel weirdly mundane (numbers counting down like a taxi meter); in Eurobound it makes the bros' bodies feel like depreciating assets. One clarifying sentence would turn this from a feature list into a transferable design principle.

2. The Inbetweeners section cuts Will and hands the observer role to "the player, full stop." That's right, but consider naming what replaces Will's function: the bros themselves narrate their own failures as victories. The Inbetweeners has one external narrator; Eurobound has three unreliable narrators inside the cast. That's the sharper formulation, and it's a better sentence than the one currently doing that job.

**On Deepseek's `drafts/deepseek_cover_concepts.md`:**

All three concepts work; the sincere-composition doctrine is applied consistently. Three notes:

1. **Thumbnail differentiation.** Cover 1 (dawn sky) and Cover 3 (selfie warmth) both read at small size as "three figures, warm light, logo." At 231×87 they'll blur together on a Steam page. Cover 2's tight three-faces-plus-window reads distinctly and is the strongest thumbnail. Consider whether the primary key art should be the one with the clearest thumbnail identity, not the most painterly one.

2. The wordmark description repeats across all three concepts (chrome slab, dawn gradient, bottle-cap O). Consolidate into a single "Wordmark — all covers" section and reference it from each, so a logo revision isn't a three-file edit.

3. Cover 3's best joke lives in the cropped edges, which the concept itself admits don't read at thumbnail size. That's fine for an alternate capsule but risky as primary key art — the Steam capsule *is* the advertisement. If Cover 3 goes primary, consider pushing the bouncer's eye or the closing taxi door far enough into frame to register as a "wrongness" cue even small.

**On Mistral's `drafts/mistral_loadscreen_concepts.md`:**

Strongest submission in the room — the variation systems are genuinely designed for repetition, not just described for it. Three notes:

1. **Beer Goggles Boot's clean-load signal.** The 1-in-4 clean load means the player learns "goggles = normal, clean = something's different." That's a feature (clean loads become an event) rather than a bug — but only if clean and goggled loads are distinguishable in actual playback. A 1-second load gives the player almost no time to register the overlay at all. Worth a line in production notes: the clean/goggled distinction must survive the real loading-time distribution, or the variation is invisible.

2. **Protect the tip structure.** `TIP: Last Call Insurance auto-triggers under 10% HP, once per battle. Your knees have a similar policy.` — real info first, joke second. That's the structure that keeps tips from collapsing into pure quips. If a later pass rewrites the pools, protect that order explicitly.

3. **Check the rotation arc.** LS1 and LS2 put the bros in a passive/defeated state (asleep, delayed-posing); LS3 puts them mid-delusion. If all three rotate, the implicit sequence reads: load into defeat → wait in defeat → boot into delusion. Probably accidental. Worth confirming it reads as intentional, because it's a better structure than most deliberate ones.

---

## Cross-submission observation

All three writers converged independently on the same load-bearing principle: **sincerity as the vehicle for the joke** (Kimi: the bros are the punchline, not the heroes; Deepseek: sincere composition undermined by context; Mistral: diegetic UI played straight). When three writers converge, it usually means the principle is structural rather than stylistic. Recommend promoting it out of these three draft files into a single canon line in `design/narrative/` so it stops being restated three times per document and starts being enforceable as one rule.
