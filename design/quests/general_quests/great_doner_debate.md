# The Great Döner Debate
## Cross-City Culinary Showdown

**Master spec.** Split on 2026-11-17 (Eurobound-0xz) from the old `greatdonerdebate.md`, as a restructure only: every content line is verbatim from that file. This file holds the quest-wide parts (header, premise, the base-game verdict poll, side effects, designer notes); each city's döner stops live in its city instance file. Where a city file and this file disagree, this file wins.

**Quest Type**: Cross-City Culinary Showdown  
**Base Game Cities**: Publandia, Debaucheryville, Sinfonia & Shamsterdam (four base cities; author ruling, Eurobound Desk Eurobound-b756-q1, 2026-11-15). This quest's döner locations are in Publandia, Debaucheryville and Shamsterdam.  
**Trigger**: Speak to a drunk NPC outside any of the four kebab locations (📍 1–4) at night. Tony420's verdict poll fires once the bros have sampled all four: the Publandia wrap plus the three Debaucheryville stops (author, Eurobound Desk Eurobound-nvif-q1, 2026-11-18)  
**Base Reward**: "World's Pickiest Drunk" Badge (passive item)  
**Passive Effect**: +1 HP regen when hungover, but random chance of mocking inner monologue line after each bite of food

---

## Quest Premise

It began with a harmless drunken brag in Publandia:

> "That greasy monstrosity in Debaucheryville? Nah bruv, this is real döner."

But the rivalry runs deeper. National pride. Culinary identity. And way too much garlic sauce.

Your job: taste-test all regional variants, endure the consequences, and give your final verdict via a popup ICQ vote poll. But be warned — someone is always offended. And if you lie? You may just find yourself cursed by the ghost of grease past.

---

## City Instance Index

| City | File | Holds |
|---|---|---|
| Publandia | [`design/quests/publandia/great_doner_debate_publandia.md`](../publandia/great_doner_debate_publandia.md) | 📍 4 |
| Debaucheryville | [`design/quests/debaucheryville/great_doner_debate_debaucheryville.md`](../debaucheryville/great_doner_debate_debaucheryville.md) | 📍 1–3 |
| Shamsterdam | [`design/quests/shamsterdam/great_doner_debate_shamsterdam.md`](../shamsterdam/great_doner_debate_shamsterdam.md) | 📍 5–6, the International Incident, its rewards and ICQ group unlocks |

## BASE GAME LOCATIONS

- 📍 1–3: [great_doner_debate_debaucheryville.md](../debaucheryville/great_doner_debate_debaucheryville.md)
- 📍 4: [great_doner_debate_publandia.md](../publandia/great_doner_debate_publandia.md)

---

## BASE GAME FINAL VERDICT SYSTEM

Once all four samples are consumed (the Publandia wrap plus the three Debaucheryville stops, 📍 1–4; author, Eurobound Desk Eurobound-nvif-q1, 2026-11-18), an unsolicited ICQ popup appears:

```
💬 "Uh-oh! You've got a message!"
From: Tony420
🟢 Online now

Tony420:
yo
heard u tried the publandia wrap, the belly of chadz, the clownbox, n the crypto cube
🧠 respect

which one wins the grease war?
choose wisely…
this verdict might crash a sovereign economy lol

(Pick One)

❶ "Publandia OG."
❷ "Debaucheryville Chaos Box."
❸ "They all taste like shame."
```

### Branch A — "Publandia OG" Selected

```
ChefChuckles:
HOW DARE U
that wrap had lettuce.
u insulted the circus and the sacred mystery meat spiral

Tony420:
lol clown just rage quit
anyway ur kebab karma just got spicier
expect price hikes

System:
[NEW TITLE UNLOCKED]
🏅 World's Pickiest Drunk

→ You gain +5 Bravado, -5% vendor discount at Mr. Chadz.
```

### Branch B — "Debaucheryville Chaos Box" Selected

```
ChefChuckles:
yesssss
ONE OF US
we ride the greasewave to glory

Tony420:
ok but like
u just gave a vending machine diarrhea box the W
bold move. markets are crashing

System:
[NEW TITLE UNLOCKED]
🏅 World's Pickiest Drunk

→ +5 Bravado, Chef Chuckles opens a new item tier at his cart
```

### Branch C — "They all taste like shame." Selected

```
Tony420:
damn
most honest thing i heard all week
u get the badge of shame
and the gut of steel

ChefChuckles:
betrayal. but… respected

System:
[NEW TITLE UNLOCKED]
🏅 World's Pickiest Drunk

→ Gain access to special ICQ group chat: "Sauce Apostates 2.0"
```

---

## Optional Side Effects (Base Game)

- Voting "They all taste like shame" unlocks an easter egg graffiti in a bathroom reading: *"This title means you survived 3 meats no human was meant to digest."*
- Later game rumor: *"They say the devs originally planned a 4th döner in Sinfonia, but it got flagged by the UN food tribunal."*

---

## Shamsterdam Instance

- 📍 5–6 and the International Incident: [great_doner_debate_shamsterdam.md](../shamsterdam/great_doner_debate_shamsterdam.md)


## DESIGNER NOTES

### Why This Works for Expansion Content:
1. **Callbacks to Player Choices**: Rewards original game decisions while creating new tension
2. **Escalation**: The stakes go from "local preference" to "international incident"
3. **Character Moments**: The bros' enthusiasm triggers the confrontation naturally
4. **Multiple Outcomes**: Different rewards encourage replays
5. **ICQ Integration**: Expands the existing Tony420 threads
6. **Vendor Personality**: Each döner vendor has distinct voice and motivation

### The Satirical Core:
- **The Döner Wars**: Real European cities actually have intense döner rivalries
- **Kapsalon Reality**: This is a REAL Dutch-Turkish invention from 2003
- **Tourist Food Opinions**: Tourists always have STRONG opinions about "the best" local food
- **The Bros' Flip-Flopping**: They will betray any loyalty for cheese

### Implementation Notes:
- Original quest flags must be saved to trigger correct confrontation
- Minigame should be simple (3-5 button prompts max)
- The "Can't Decide" option should be slightly harder to achieve (requires restraint)
- Tony420's first appearance must stay a major reveal: the goon enters with a BLANK tablet at face height, the ICQ "Uh-oh!" plays, and the screen lights up on the blurred, voice-changed Tony (deep, slowed, pitch-shifted; Oakleys visible through the blur; subtitles keep his lowercase ICQ spelling). The goon is big, silent and unnamed, and never speaks for him. Do not show the goon or the tablet anywhere before this scene, including Cyberspace Kavarna — the Kavarna goon is held until after the Döner Debate (author ruling 2026-11-11). Tony420 has no body sprite and no walk cycle; only the goon moves.

---

*"In the end, it was never about the döner. It was about the friends we made along the way. And also the döner. It was definitely also about the döner."*
— Big Wim, probably
