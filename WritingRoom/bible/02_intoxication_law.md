# EUROBOUND — ADULT INTOXICATION & CONSEQUENCE DESIGN LAW

_Author directive, given to the moderator on 2026-11-09 (worked out with the editor). Binding on every task. Relayed verbatim._

AUTHOR DIRECTIVE — BINDING CREATIVE DIRECTION

Eurobound is a mature, adult satirical JRPG in the tradition of games that allow protagonists to behave recklessly, foolishly, selfishly, and spectacularly badly.

Do not sanitize alcohol, drug use, sex, or intoxicated behavior into moral lessons.

The protagonists are aging former party bros who believe the consequences of their decisions still operate according to the rules of their twenties.

They are wrong.

Their decisions should create comedic, mechanical, social, physical, and occasionally lasting consequences.

1. No obligatory moral lectures

Writers should not interrupt fictional intoxication sequences with warnings, explanatory narration, redemption speeches, or public-service-announcement dialogue.

Characters may make terrible decisions without receiving a lecture about them.

The humor comes from the decisions and consequences.

2. Alcohol is a progressive gameplay system

Audit the existing Eurobound alcohol and Beer Goggles documentation before defining new thresholds.

Build on approved mechanics rather than replacing them.

The intended progression includes:

* Early confidence and impaired judgment.
* Increasingly absurd Beer Goggles perceptions and choices.
* Compromised speech and social interaction.
* Temporary visual or movement impairment.
* At extreme intoxication, brief scripted moments when the player loses control of a character's decision.
* Delayed consequences, including morning-after discoveries and altered NPC interactions.

Exact thresholds and durations remain subject to systems-design review.

3. Loss of player agency is a legitimate mechanic

At severe intoxication, the game may temporarily:

* Replace a sensible dialogue choice with a stupid one.
* Remove the sensible choice entirely.
* Cause a character to interrupt a conversation.
* Trigger an impulsive, embarrassing action.
* Produce temporarily unreliable movement.
* Present deliberately distorted information.
* Lock the player into a short, character-specific disaster.

These events must be understandable, limited in duration, and used for comedic payoff rather than constant frustration.

Do not permanently damage save files or create unpredictable softlocks.

4. Drugs may have absurd, character-specific effects

Tony420 is an established ICQ dealer who takes cryptocurrency payments.

His existing canonical characterization, inventory, and crypto payment mechanics must be respected.

The author has established two product names:

* Flintstone Xanax
* Flintstone Fentanyl

The proposed TROUSER SNAKE interaction involving Flintstone Xanax has a specific author-directed fictional effect:

It eliminates TROUSER SNAKE and prevents Bradley from regaining sexual performance capability until the next in-game morning.

This is a deliberately exaggerated, fictional item consequence.

It is not a medical simulation.

This mechanic creates a delayed payoff if Bradley later has a consensual intimate opportunity with Jenna Talia or Barbara Bushed: he can discover that the cure worked far too well.

The writers must preserve this causal joke instead of replacing it with generic intoxication dialogue.

Do not automatically assign the same effect to Flintstone Fentanyl. Its distinct gameplay behavior requires separate design and authorization.

5. Choices should create delayed comedic consequences

An apparently effective short-term solution may create a worse long-term problem.

Characters may misunderstand what their actions accomplished.

The player should occasionally recognize a terrible consequence before the protagonists do.

The outcome should be funny because of established character flaws, not because the writers arbitrarily punish the player.

6. Protect the mature tone

Do not transform the game into a wholesome lesson about self-improvement.

Do not overexplain innuendo, sexual jokes, drug jokes, or pop-cultural references.

Do not treat player discomfort with an absurd character decision as evidence that the writing must be softened.

Do not replace outrageous consequences with polite, consequence-free dialogue.

The satire should remain sharp, sexually irreverent, politically pointed where appropriate, and deeply character-specific.

7. Keep the game playable

Temporary movement impairment must remain readable and accessible.

Provide accessibility alternatives for strong camera wobble, screen distortion, or motion effects.

Scripted loss-of-control events should have bounded durations and predictable recovery.

Maintain consistent save/load behavior and prevent permanent control loss.

Do not invent mechanical features that the current Godot implementation cannot support without identifying them as proposed engineering work.

8. Mandatory design review

Before integrating an intoxication-related mechanic, identify:

1. Its source item or drink.
2. Its immediate effect.
3. Its escalation conditions.
4. Its visible player-facing cues.
5. Its effect on player control.
6. Its duration and recovery.
7. Its comedic consequence.
8. Its interaction with other established statuses.
9. Its technical implementation dependencies.
10. Whether it requires further author approval.

Final principle:

Eurobound does not punish the bros for drinking or taking drugs because the game has a moral position to deliver.

Eurobound allows the bros to make appallingly confident decisions and then discovers that their bodies, reputations, and circumstances have other plans.

The bros think they're invincible. The gameplay knows better.

---

## Appendix A — The alcohol escalation system (shared by the author 2026-11-09; the editor's proposal)

_Relayed verbatim from what the author shared. The tiers are illustrative: "not yet approved numerical thresholds". **Author ruling 2026-11-09: the tier names are Buzzed / Beer Goggles / Shitfaced / Catastrophe.** The dialogue mock-up's "Drunk" and "Wasted" labels map to Shitfaced and Catastrophe._

> Yes. Let's make that a standing Eurobound game-design rule. 😈
> You're building an adults-only satirical JRPG about three aging frat bros who still believe they possess the alcohol tolerance, sexual stamina, and general invincibility of their early twenties.
> The joke is that their bodies have stopped honoring that agreement.
> […]
> Eurobound should be able to depict drinking, recreational drugs, terrible decisions, sexual embarrassment, and spectacular consequences without becoming a public-service announcement.
>
> The system I'd establish
> Rather than treating alcohol and drugs as ordinary consumables that simply add or subtract stats, I want them to interact with player agency, character behavior, perception, and delayed consequences.
>
> Proposed alcohol escalation
> 1 Buzzed · 2 Beer Goggles · 3 Shitfaced · 4 Catastrophe
> Illustrative tiers, not yet approved numerical thresholds.
>
> 1. Buzzed: Exaggerated confidence, altered dialogue, increasingly ambitious boasts.
> 2. Beer Goggles: Perception becomes less reliable. Attraction and social judgments become hilariously questionable. Existing Beer Goggles combat effects remain intact.
> 3. Shitfaced: Movement becomes unreliable, animations get sloppy, and some dialogue choices become unavailable or distorted.
> 4. Catastrophe: A short scripted loss-of-control event can force a character-specific terrible decision, creating consequences that survive into the next morning.
>
> I'd make the loss of agency intentional game design, not arbitrary punishment. When a player keeps drinking, the interface communicates that they're getting less control, and the resulting disaster is funnier because they can see it coming.
>
> Dialogue impairment prototype — Pilsner encounters an important-looking stranger.
> - Buzzed: Politely decline / Order another round / Ask for directions
> - Beer Goggles: You look familiar / Another round, gorgeous / I know a senator
> - Drunk: I'm fine. Watch this. / Tell everyone my secret / Where's the microphone?
> - Wasted: Challenge the chandelier to a duel / Announce you're running for president / Propose to the coat-check attendant
>
> PILSNER IS MAKING AN EXECUTIVE DECISION.
> Selected automatically: "Announce you're running for president."
> Pilsner climbs onto a table. Chadwick starts filming.

**Canon anchor:** today Beer Goggles exists only as the debuff from Lord Pilsner's Ultimate "Mid-Life Crisis" (Vintage upgrade): "−Accuracy, +Friendly Fire chance" (`design/characters/LordPilsner/lordpilsner.md` l.32). Tier 2 keeps those combat effects and adds the perception layer. The Debaucheryville quest `nothingisgettingthrough.md` already renders Beer Goggles as a literal overlay; reuse it.
