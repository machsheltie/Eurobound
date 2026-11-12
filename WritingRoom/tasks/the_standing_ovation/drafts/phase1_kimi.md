# Phase 1 — Kimi source review

Status: review only. No creative direction or work split is locked. Audition citations below refer to `room/auditions_text/`; `Max profile` means `design/worlds/sinfonia/npcs/The_Standing_Ovation/max_vex.md`.

## Binding canon for this quest

- The author brief supplies the venue, show title, all 11 fixed events, Max's they/them pronouns, three real decision points, and five new enemies. The encounter dossier supplies the dramatic law: **drag is not the joke; the bros are.** Max is hot, professionally excellent, fallible, socially instigative, and not a counselor, diagnosis machine, romance reward, or morality NPC.
- Max profile is binding for voice and continuity: Max sells nothing, has their own evening, remembers the bros because they are funny rather than important, and later appears independently at a legitimate Black-Tie poker table. No casino/poker material belongs in this quest. Max's reads should feel observed in the moment, not like a stack of prepared comebacks.
- The Standing Ovation is a legitimate brewery/performance venue with excellent beer. Existing spaces: Orchestra Pit, Balcony, Green Room, Wings. Existing hours are 4 PM–1 AM. A 10:30/11 PM revue with aftermath before 1 AM needs no hours exception; Gemini's proposed 2 AM residency is not usable.
- Existing venue items are `beer_standing_ovation` (Curtain Call Copper), `opener_standing_ovation`, and `stamp_standing_ovation`. Openers/stamps are earned, never sold. Do not duplicate them or silently replace the established drinks menu with Dramatisch Dunkel, Black Overture, Imperial Pour, or Cold Shower.
- Bros: appetite without fear or disgust; no shame-based moral turn; no lasting self-awareness. Pilsner = legend/status, Chadwick = audience/obsolete technology and a bad decision caused by relevance hunger, Bradley = concrete physical/mechanical read followed by prideful overcorrection. Brenda is Chadwick's wife; no new marital/family backstory.
- One-phone canon: cellphones were confiscated on arrival; the party shares one speakerphone-only phone. This collides with N-Gage filming/livestreaming in Aion, Gemini, and GLM. Device question sent to author. Chadwick's chain-attached vintage camcorder already exists in `design/characters/Chadwick/chadwicksweapons.md`.
- SOVS only; no real city/place names in player-facing text. Cut/parody Austin, Texas, Chuy's, Arkansas, Stanford, and similar material. Real public political references explicitly required by the brief can remain, but do not add real businesses or licensed songs as production dependencies. All monetary/stat/mechanical additions remain PROPOSED pending approval.
- No narrator or explanatory aside. Stage direction should describe visible action, not deliver the thesis. Battle-log/UI jokes are allowed. All side content is optional and cannot gate main progression.
- The named adult performers need mandatory NPC profiles. Any new items need their proper item treatment. `data/quests/flags.json` does not yet exist, so the final document can supply a namespaced design-side flag table but must not claim engine registration.
- `game/assets/data/enemies/sinfonia_enemies.json` is empty. The only populated example (`debaucheryville_enemies.json`) uses `display_name`, `battle_intro`, `max_hp`, `offense`, `defense`, `speed`, `luck`, `xp_reward`, `gold_reward`, `item_drop`, `drop_chance`. New stats, AI, drops, and mechanics are proposals; five enemies are still required by the mission statement.

## Fixed-event audit

| Audition | Result |
|---|---|
| Aion | All 11 are present in substance. Event 6 is under-staged: Max says “Oh” before any visible waist-level/physical response is supplied; the squats happen only after the required exchange. Put the undeniable physical reaction before “Oh.” |
| Gemini | **Event 10 is missing.** It substitutes Chadwick asking for a handle and Max saying “…Anyway.” The exact “What did you say your name was again?” / “You know my name.” / “Do I?” exchange must be restored. Events 5–8 are otherwise strong and explicit. |
| GLM | All 11 appear, but Beer Lord is delayed until after Trouser Snake, weakening the clean fixed sequence and the Pilsner/Chadwick contrast. Max also gets a tip-pouch/sales function that the canon profile forbids. |
| Kimi | All 11 present and in order. Strongest event-11 staging: Max leaves to deal with Jenna teaching Herr Dramatisch the chair routine, steals Barbara's cherry, and later discusses food with the queens. That is an evening independent of the bros, not a romantic exit. |

## Character/violation pass — exact material

### Aion 3.5

- **Bradley, cut:** “That person was attractive. That's a fact. Facts don't have a gender.” and especially “That's going to sound bad later and I don't care.” This is articulate identity processing plus anticipation of how the line will read later. It resolves the very compatibility failure that should keep making him say stupid physical things. Replace with more bad vasoconstriction/gym science, not insight.
- **Chadwick, rewrite:** “That's called living through it,” delivered “gently,” makes him the emotionally intelligent generational straight man. “Who's watching us is usually the problem” is similarly polished commentary. His job is to make a worse decision because he thinks the footage will make him matter.
- **Pilsner, trim:** “I mean — we're not the show, obviously, there's a show. But we're *of* the show” is an unusually deft self-correction. His wrong declaration should stand without a polished recovery. “I was in a boy band in high school…” and “I was on TRL once… Carson looked at me” are disposable boasts, not biographies to canonize.
- **Max:** no therapist-Max problem. The exit is good. The run of “living exhibit” / “missing a period piece” / “important work” is one rehearsed-sounding insult too many; keep the best observed hit and let Max drink/accept compliments like a person.
- **Bradley, preserve:** the silent gym-quality squat and “Redirecting blood flow,” plus the briny tonic misclassified as a sports drink. Those are physical denial, not romantic-hero writing.

### Gemini

- **Chadwick, rewrite:** “Content architect, cultural scout… Our core demographic is very engaged, very lifestyle-forward” sounds like a current, competent marketing trainee. He needs Friendster/MySpace/hit-counter thinking and a visibly terrible choice. The N-Gage livestream/camera material also conflicts with one-phone canon pending the device ruling.
- **Pilsner, mostly sound:** “In the old kingdoms, laughing was how servants showed joy in the presence of nobility” is exactly the right confident false expertise. “Political framing… institutional memory” is on the articulate edge but still works as borrowed self-importance if shortened.
- **Bradley, preserve:** “The barstool has an ergonomic incline… It's a leverage issue. A mechanical failure of the seat cushion” is an excellent mechanism-based denial. He never becomes a romantic hero in this draft.
- **Max:** “Save the adjectives for your invoice… The left monitor was popping on the low end. Fix it before the weekend” is valuable because Max has professional priorities. Max is not a therapist here. However, the event-10 omission breaks the brief, and the long “catastrophic automated misfire… midwestern biological wiring” direction should become visible sprite acting rather than an essay explaining his body.
- **Canon/content:** the named real venues/schools/businesses and real licensed songs should not ship. The 1997 prom/teen framing is unnecessary; keep all sexual glamour unequivocally in the present-day adult performers and their adult-era political parody.

### GLM 5.3

- **Pilsner, cut or redirect:** reading the playbill's “They, them” as royal plural (“They. Like royalty… We are not amused”) puts too much of the gag on Max's pronouns. The permitted target is Pilsner's obsolete worldview, not the existence of they/them pronouns. Use a title/status misread instead.
- **Pilsner, watch:** “Kid, when I was your age—” followed by arithmetic and a quiet “Enjoy the show” nearly lets reality complete the lesson. He can suffer temporal damage, but must immediately blame the archive, the kid's education, or regional broadcasting rather than accept age as cause.
- **Chadwick, cut:** “Brenda's mom liked it, and she only got a phone last year” invents new marital-family backstory contrary to the brief. The 63-view/top-comment engine is otherwise useful and makes publicity consequential rather than merely witty.
- **Bradley, agency/character risk:** every branch forces him to cross to the Wings after Max, allegedly about choreography, and be escorted back. That turns attraction into compulsory pursuit and strips the player's ability to avoid the humiliation. Keep “I was asking about the choreography” as an optional bad decision, not a fixed toll.
- **Max:** “You must have been somebody in 2000” and the surprised delight when Beer Lord sticks are good evidence Max can be amused rather than omniscient. “Nothing's coming” is a strong non-nickname hit. Remove the velvet tip pouch and “the dwelling would have cost extra”; Max sells nothing, and that line explains the joke.
- **Bradley, preserve:** “Body made a call. I respect the call. It'll drain.” / “To where?” / “Doesn't matter.” Short, physical, sincerely wrong.

### Kimi k3 (my audition — not exempt)

- **Bradley, revise:** “They love the character” after the Toast Immortal implies he knowingly performed a comic persona. He should read the laugh as personal acclaim (“They love me”), not demonstrate author-level awareness of his own shtick.
- **Bradley, watch:** “Drink accepted. That's basically a date… European dating” is usable only as an obviously false one-line rationalization after Max has returned to Chelsea's story. Do not build a reciprocal-romance implication around it.
- **Pilsner:** “I produced tonight” and “That has a touring future” are the right delusions. “We leave a producer, a sex symbol, and a documented media entity” is an appropriately wrong retelling.
- **Chadwick:** “I can get you a MySpace presence,” “I would’ve taken Camera Guy,” and “I own the story” are era- and hunger-specific. The free water branch's “You could die” is generic hostility and can be sharpened or cut.
- **Max:** strongest material is fallibility and independent life: “God, you're serious” / “I am. That's on me”; “You may film. You may not make it my problem”; “Tip your server” into Chadwick's lens; leaving to stop the cape dancing. No therapist-Max or invincible comeback machine.
- **Agency gap in my own draft:** two choice menus are not the brief's three genuine decision points. Seating and the next round need a third, non-spending choice with persistent consequences (the footage/publicity material is the obvious candidate, not a locked direction).

## Material worth preserving

1. **GLM, §3:** the most playable revue language. Chelsea's flat “Good question,” the institutional hearing lighting, Secret Service pyramid, and a jacket reveal that is a second jacket; the twins trading places in blackout; “I'm the pretty one” / “We're identical” / “I'm the pretty one”; “Florida's still counting.” These are short, visual, and performer-owned.
2. **Kimi, §3:** production-friendly stage business: PRIVATE folder containing a mirror; Chelsea's imaginary earpiece earring; tap break along the apron without disturbing a glass; the twins swapping vocal roles and sharing spring water with exaggerated innocence; close-harmony chair choreography; APPLAUSE sign lighting only after the room is already standing.
3. **Aion, §3:** actual vocal/comic identity for the queens, especially “Nobody voted for me, but everybody had notes,” Barbara's dead-still ballad against Jenna's chaos, and Jenna's backstage “The puka shells called to me.” Remove real-place/business references rather than losing the number concepts.
4. **Kimi, §§4–5:** the cleanest complete Max sequence, Bradley's playbill at belt level, “It's the denim. It bunches” / “Leg day” / “That's why it's backed up,” and Max being allowed to laugh despite themself.
5. **Gemini, §§4–5:** Max's monitor-note professionalism and Bradley's ergonomic-stool explanation.
6. **GLM, §6:** post-versus-vault footage as a non-purchase choice with visibly different publicity consequences; “is the jersey guy ok” as the audience's actual interest.
7. **Aion, §4:** the BEER LORD HALL corkboard between two Hawaiian shirts is excellent visible evidence that Pilsner's singular honor is routine. It should not become another mandatory investiture fee.
8. **Aion, §5:** Herr Dramatisch never lies and the service is genuinely delivered. Keep that competence; discard the enormous compulsory itemized bill, not the characterization.

## Conflicts and gaps to resolve in the story break

- None of the auditions satisfies the full agency requirement. Aion has one cosmetic choice and one coping choice plus a forced 216-Sovs bill; Gemini's three branches are three ways to pay; GLM has three motions that converge on the same Wings humiliation and up to ~388 Sovs of purchases; Kimi has only two decision points. The final needs at least three decisions, at least two mechanical/state consequences, a free entertaining route, and one major escalation with no purchase at its root.
- Do not let “excellent show” become a framing sentence followed by three bro scenes. The revue needs a small number of complete, distinct performer-owned numbers, not every audition gag concatenated.
- The adult-performer/adult-era framing must be explicit in staging. Adolescent press-history jokes may be referenced as history, but no sexualized staging should attach to a depiction of a minor.
- The canon Max profile says the full name-forgetting exchange is a casino callback; the newer author brief expressly requires it in this post-show encounter. Follow the brief here. Any later casino appearance should use a shorter proximity greeting rather than repeating the entire exchange, and no poker material enters this quest.
- `bros_character_bible.md` says Pilsner has no established civilian name, while the later owner+ChatGPT Max profile explicitly supplies the roast “PHILLIP.” Treat that later profile as authorization for this one humiliating first-name usage only; no surname or expanded biography.
- TROUSER SNAKE's +10 Confidence / −25 Concentration are canon labels but not global engine stats. Preserve the player-facing copy and compromised dialogue; any internal mapping to Bravado/accuracy or other stats needs a mechanics ruling and must not create a permanent new global system by accident.
- Show scheduling can fit inside current hours; no author exception needed. New prices, statuses, items, NPCs, enemy stats, and persistent flags remain PROPOSED. Author questions sent this round cover Chadwick's recording device and the three performer names.
