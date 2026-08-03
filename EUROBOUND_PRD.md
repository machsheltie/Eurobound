# EUROBOUND — Product Requirements Document & Game Bible

**Version 1.0 · July 2026 · Living document**
**Working title:** Eurobound
**One-liner:** An EarthBound-style satirical JRPG where three aging frat bros take one last hurrah across Europe's seediest nightlife — convinced they're legends, while the game, the NPCs, and the player quietly know better.

> **How to use this document.** This is the single source of truth. Where the design folders (`Design/`, `Production/`, `UX-UI/`, etc.) disagree with each other, **§2 Canon Decision Ledger** resolves the conflict and this document wins. Detailed flavor content (venue docs, quest docs, dialogue) stays in the existing folders; this Bible defines the systems, numbers, structure, pipeline, and scope that turn those documents into a shippable game.

---

## Table of Contents

1. [Vision, Pillars & Tone](#1-vision-pillars--tone)
2. [Canon Decision Ledger](#2-canon-decision-ledger)
3. [Product Definition](#3-product-definition)
4. [World & Story](#4-world--story)
5. [The Party — Canonical Character Kits](#5-the-party--canonical-character-kits)
6. [Combat Bible](#6-combat-bible)
7. [Progression — Clout, Levels & Skill Trees](#7-progression--clout-levels--skill-trees)
8. [Social & Reputation Systems](#8-social--reputation-systems)
9. [Economy, Items & Equipment](#9-economy-items--equipment)
10. [Quest & Content Inventory](#10-quest--content-inventory)
11. [Interactables, ICQ & the Save System](#11-interactables-icq--the-save-system)
12. [UX / UI & Accessibility](#12-ux--ui--accessibility)
13. [Art Bible](#13-art-bible)
14. [Audio Bible](#14-audio-bible)
15. [Technical Architecture](#15-technical-architecture)
16. [Production Plan & Skills Package](#16-production-plan--skills-package)
17. [Compliance, Legal & Store Strategy](#17-compliance-legal--store-strategy)
18. [Risk Register](#18-risk-register)
19. [Appendices](#19-appendices)

---

## 1. Vision, Pillars & Tone

### 1.1 The premise

Lord Pilsner, Chadwick, and Bradley — three aging American frat relics pushing 40 — set out on "EuroBouncin'," a final bender across three heightened caricatures of European nightlife cities: **Publandia** (Dublin), **Debaucheryville** (Prague), and **Sinfonia** (Vienna). They believe this trip will confirm they are still legends. Every pub, club, kebab stand, and NPC in the game politely disagrees.

*"This isn't about saving the world — it's about surviving it with your ego intact."*

### 1.2 Why EarthBound

Eurobound is a direct homage to EarthBound/Mother 2 — the name is the thesis. EarthBound's craft is the template on every axis:

- **Oblique-projection pixel towns** with diagonal streets, flat saturated color, and chunky readable sprites.
- **Visible enemies on the map** — no random battles.
- **Front-view battles**: static front-facing enemy sprites over psychedelic animated backgrounds; the party is represented by a row of stat boxes, not sprites.
- **The rolling HP odometer** — mortal blows can be outrun.
- **Mundane objects as legendary gear** (EarthBound's Cracked Bat and Fry Pan → our Ceremonial Beer Paddle and Vintage Ring Light Mace).
- **Mechanical humor**: status effects, item descriptions, and enemy names are jokes that also function (EarthBound's Homesickness → our Hungover, Embarrassed, and Regret Rash).
- **"Accurately inaccurate" satire**: EarthBound's Eagleland is an affectionate fever-dream of America; Eurobound's cities are an affectionate fever-dream of European nightlife. We love the thing we mock. The iconography is right; the details are joyfully wrong. (*Yes, we know the pretzels are more German — lean into the satire.*)

### 1.3 Design pillars

1. **The player is in on the joke.** The trio believes; the NPCs, the reward names, and the status effects quietly don't. **There is no narrator** — no voice of any kind that frames, explains, or apologizes for the satire (author ruling 2026-08-03). Satire targets everything: the bros' delusion, the locals, the cities, the cultures, the vices. Everything gets parodied, nothing gets hand-wrung over — "it's offensive" is not a design consideration in this game.
2. **Comedy through tragedy, with real teeth.** Every gag has mechanics. "Mid-Life Crisis" is an actual Ultimate. Getting Embarrassed actually drains Bravado. Rewards are real even when the fiction is humiliating ("promoted to Bathroom Attendant" still pays out).
3. **Perfect EarthBound DNA, modern execution.** SNES-era look and battle structure, delivered with modern UX and autosave. Target platform: Steam/desktop, Godot 4.4 (author ruling 2026-08-03; mobile-first is void).
4. **The seedy underbelly is shown, glorified, and ridiculed.** Drugs, sex workers, red-light districts, benders, hookups — everything the bros came to Europe for is on screen and on the table. The one hard line: no explicit nudity (sex happens, it's never shown). This is an MA game for adults. The underworld isn't a threat lurking behind velvet curtains — it's the playground, presented in all its glory, and the joke is the bros looking dumb in the middle of it.
5. **Playable Idiot Logic.** Flaws are mechanics: Flirt always backfires. Bradley won't detour without a gym nearby. Chadwick's buffs fail when his stream chat turns on him. The party's greatest enemy is itself.

### 1.4 The emotional core

Eurobound is about three men who will never notice the party ended years ago — and the game never notices for them. There are no "Reality Check" encounters, no Perspective status, no Mirror Chad, no alternate ending where the truth lands. **The mask never slips.** The bros never learn, the game never winks, and nothing on screen explains the joke. Sincerity is the joke: the deadpan commitment holds from title screen to credits, and the comedy comes from the player seeing what the bros never will.

---

## 2. Canon Decision Ledger

The design folders were written across multiple drafting passes and contain contradictions. The following decisions are **final canon**. Files listed in the "Cleanup" column should be edited to match (tracked in Appendix 19.4).

| # | Topic | Conflict in docs | **CANON DECISION** | Rationale |
|---|---|---|---|---|
| C1 | **Protagonist POV** | Player-as-rival-roaster (Production doc, legacy pitch) vs player-controls-the-trio (README, GAMEPLAN, Synopsis, all character docs) | **Player controls the trio: Lord Pilsner, Chadwick, Bradley.** The world does the roasting. | Owner's stated vision; matches 90% of written content. The "roast" energy lives in the narrator, NPCs, and enemy design. |
| C2 | **Engine** | Godot 4.x (Production, all prototype code) vs Phaser.js (legacy pitch, one Dev Skills section) vs Unity (considered) | **Godot 4.6+.** Delete/ignore all Phaser references. | See §15.1. Best 2D pipeline, zero fees, existing GDScript code, Foundation-maintained mobile store plugins (2026). Unity's AI tooling doesn't outweigh this for a solo pixel-art game. |
| C3 | **Party roles** | `party.md` + character docs (Pilsner=Leader, Bradley=Tank, Chadwick=Support) vs `combatsystem.md` (Bradley=glass cannon, Pilsner=tank) | **Pilsner = Inspiring Commander (balanced leader/buffer). Bradley = Tank/Berserker Protector. Chadwick = Chaotic Support/debuffer.** | Three docs agree vs one; matches personalities (Bradley "catches his breath then charges"). Bradley's berserk-at-low-HP covers the DPS role dynamically. |
| C4 | **Ultimates** | Two sets of names across files | **Pilsner: Mid-Life Crisis · Chadwick: Viral Meltdown · Bradley: Bouncer Breaker.** (`Fratocalypse Now`, `Going Viral`, `Final Round's On Me` are retired or repurposed as skill-tree nodes.) | Confirmed by party.md, bravado.md, AND the musical Ultimate Choruses in `musicalbeats.md`. |
| C5 | **Spell ownership** | `bravado.md` vs `skilltrees_cloutspells.md` assign Battle Cry of the Mascot / Flash of the Red Solo Cup / Charm of the Bro Code to different bros | **Skill trees are canon:** Pilsner gets *Battle Cry of the Mascot* and *Flash of the Red Solo Cup* (Toastmaster / Barroom Tactics); Chadwick gets *Charm of the Bro Code* (PR Spin). | The skill-tree doc is the most complete progression spec; character quest docs match it. |
| C6 | **Currency** | "Cover Charges" vs "Bar Tabs" vs "gold" (code) vs "€" (menus) vs "beer tokens/shame coins" | **One currency: SOVS.** Never euros, never the € glyph, never koruna (author ruling 2026-08-03; supersedes the €-as-display-glyph rule). "Cover Charge" stays as a recurring money-sink event (doors literally tax you). "Gold" in prototype code is renamed `sovs`. Shitcoin/crypto satire per the Round 5 economy spec. | Author-locked currency canon; grounded-but-fake currency keeps the satire while cutting real-world baggage. |
| C7 | **XP** | Consistent | **XP = "Clout."** Clout accumulates (never spent) and gates both levels and skill tiers. See §7. | Resolves the earn-vs-spend ambiguity in the skill tree doc. |
| C8 | **Boss placement** | Count Velvet Absinthe at "Shadow Exchange" vs "Absinthe Cathedral" | **Shadow Exchange.** "Absinthe Cathedral" is cut (it exists nowhere else). | Matches the city doc and the `unlock_premium_stock()` hook already in code. |
| C9 | **NFT roster** | 4+ candidate NFT sources in Debaucheryville for a 3-per-city hunt; NFT #2 has three names | **12 collectible NFTs, 4 per city — `fratbronft.md` is canon (author ruling; supersedes this row's old 9-count).** Milestones 4/8/12. Publandia's 4th is a sanctioned open slot awaiting the author. Extra discovery points remain alternate acquisition routes, not extra NFTs. "Velvet Wristband JPEG" is an alias to delete. | Matches the author's quest doc and the Round 5 Legacy Vault (12 cards). |
| C10 | **Breweries** | 4/city (brewery doc, tracker code) vs 2–3/city (sidequests.md) | **4 per city, 12 total.** | Matches the fully-designed Debaucheryville set and `brewery_tracker.gd`'s default data. |
| C11 | **City names in-game** | Docs mix "Dublin/Publandia," "Prague/Debaucheryville" | **Only parody names appear in-game.** Real city names may appear in marketing copy as "inspired by." | Trademark/sensitivity hygiene; EarthBound's own approach (Onett, Twoson). |
| C12 | **Status naming** | "Hungover" vs "Hangover"; two versions of Hydrated for Once, Embarrassed | **Master status list in §6.6 is canon.** Status is "Hungover." Embarrassed = merged spec (stat penalty + Bravado drain + no Ultimates). Hydrated for Once = Hungover immunity + 1 HP regen/turn. | statuseffects.md has the best numbers; merges add the Bravado hooks other systems need. |
| C13 | **Scope statement** | Designer Persona says "30–60 minute experience" vs content docs describing 10+ hours | **V1.0 target: 8–12 hours** (Undertale-scale). The "30–60 minute" figure is reassigned to the **vertical slice/demo**. | Research: every successful solo EarthBound-like shipped 6–25 hrs; the written content supports ~10. |
| C14 | **Orientation** | Never decided | **Landscape.** | Preserves EarthBound battle composition and oblique overworld sightlines; two-handed virtual-stick play. Portrait revisit only if slice playtests demand it. |
| C15 | **Battle menu** | Attack/Skill/Item/Defend/Flee vs mockup's Fight/Skills/Items/Run | **Bash / Brag / Items / Chicken Out** — four slots as in the mockup, flavored. "Brag" opens Bravado skills; Defend lives inside Bash submenu as "Brace" (see §6.2). | Four large touch targets beat five; flavored verbs carry tone into the UI. |
| C16 | **Distribution** | iOS-only vs HTML5/itch vs Android | **Steam/desktop premium.** Mobile is no longer the target (author ruling 2026-08-03). Price point: author decision, open. itch.io/HTML5 may remain as a press/playtest channel. | Matches the approved folder-restructure spec ("Godot 4.4, targeting Steam"). |
| C17 | **Voice acting** | "voices" requested; character voice.md files empty | **No full VO.** Per-character text-blip "voices" (Undertale-style pitched beeps) + a handful of recorded gag barks and the sung Victory Stingers. See §14.4. | Genre-authentic, radically cheaper, avoids AI-voice licensing risk; stingers deliver the "voice" fantasy where it counts. |
| C18 | **Bottle Opener Keychain geography** | References Munich/Belgium/Oktoberfest | Rewrite to the three shipped cities. "12 Different Breweries" now literally refers to the game's 12 breweries. | Berlin/Ibiza/Munich remain listed as **post-1.0 expansion hooks** only. |
| C19 | **Raunch ceiling** | Darkweb ICQ logs (fentanyl gummies, organ trade) far edgier than the rest | **There is no raunch ceiling. The ONLY ceiling in this game: no nudity. Beyond that, anything goes.** MA / adults-only, full-strength satire (author ruling 2026-08-03; binding rule §0a-2: sanitizing, softening, or de-subversifying is a highest-severity defect). No `SATIRE_MODE=SAFE`, no `line_safe` strings, no safe build — sanitization mechanisms are banned outright and may never be rebuilt. The pre-sanitization darkweb/vice content (Tony420's pharmacological inventory, the ICQ logs) is canon at full strength. | The 16+ ceiling and Satire Swap system were an unauthorized sanitization pass in direct violation of the author's express orders. The satire ships intact or not at all. |
| C20 | **`Legacy_Pitch_Document.md`** | Contains identifying details about a real person | **Never ships, never public.** Move out of any public repo/press kit; keep locally if desired. All characters remain "recognizable archetypes, legally safe" (the repo's own success metric). | Defamation/likeness risk. The finished game must stand alone as archetype satire. |

---

## 3. Product Definition

| Field | Value |
|---|---|
| **Genre** | Satirical retro JRPG (EarthBound-like) |
| **Platforms** | iOS 16+ (iPhone), Android 10+ (Galaxy-class); landscape |
| **Engine** | Godot 4.6+, Compatibility (GL) renderer |
| **Price** | **$4.99 premium.** No ads. No IAP at launch. (Optional post-launch: "Deluxe Roast Pack" cosmetic DLC, one-time purchase.) |
| **Rating target** | Apple **16+** · ESRB **Teen/M17+ boundary — design to Teen where possible** · PEGI 16 · IARC questionnaire answered as *infrequent* mature themes |
| **Session design** | Meaningful loop completes in **≤ 10 minutes**; autosave continuous; quest log restates context on relaunch |
| **V1.0 content** | 3 cities · 12 brewery micro-dungeons · 3 city bosses + 3 rival showdowns + final sequence · 3 personal quest chains · 10 global sidequest lines · 9 NFTs · 8–12 hours |
| **Vertical slice** | Publandia core loop, 30–60 minutes (see §16.3) |
| **Audience** | 25–45, played SNES-era RPGs or their descendants (Undertale, Stardew), enjoys satire; secondary: mobile premium-RPG buyers |
| **Comparable titles** | EarthBound, Undertale, Citizen Sleeper (tone-adjacent), Stardew mobile (premium mobile model) |

**What "done" means for V1.0:** a player who has never read these documents laughs in the first 10 minutes, understands battle by the second encounter, finishes Publandia in 2–3 hours, and describes the game to a friend as *"EarthBound but you play as the guys everyone dreads at the hostel."*

---

## 4. World & Story

### 4.1 Structure

Sequential city-worlds, each with a surface tourist layer and a **Seedy Underbelly** layer, connected by a stylized rail-travel interstitial (train montage = act break + laundry list of what the bros claim happened vs. what we saw).

> **Shamsterdam is canon (author's city — this PRD predates it).** A fourth city with ~70 content files (venues incl. Casa Rose Erotic Theater, the Condomerie, coffeeshops, canal district; currently staged in the folder-restructure `_sorting/`). Its place in the act structure, boss, and quest skeleton await author direction — the three-act table below is the pre-Shamsterdam draft.

```
PUBLANDIA (Dublin)          DEBAUCHERYVILLE (Prague)      SINFONIA (Vienna)
"Beer & Brotherhood"        "Neon Nights & Shady          "Culture & Nightlife" —
                             Delights — it was cheaper     opera glitz over black-tie
                             at 3 a.m."                    backrooms
(+ SHAMSTERDAM — placement and order per author; act labels dead per author ruling)
```

Every city delivers the same guaranteed skeleton (content quotas are production law):

- 1 base-of-operations pub/inn (The Bottomless Tap · Hostel "Midnight Checkout" · The Moderato Pub)
- 4–5 districts, 6–10 enterable venues, 2 of them dungeon-scale
- 4 brewery micro-dungeons (Brewery Tour)
- 1 **city boss** (awards trinket/weapon + access unlock)
- 4 hidden NFT acquisitions (with redundant routes; 12 total per `fratbronft.md` — the Rival Trio appears once in the whole game, in the NFT sidequest only, NOT per city)
- 6–10 Wi-Fi/ICQ hotspots (save + flavor + hints)
- 3 restroom graffiti shrines (Public Restroom Graffiti quest — 9 total)
- 1–2 couchsurf spots, 1 karaoke/performance venue, city-specific status effects & reputation ladder

### 4.2 The story spine — AUTHOR-CONTROLLED (`mainquest.md` is written WITH the author, never without)

**Standing rule (author, 2026-08-03):** No story decision is made by anyone but the author. The previous agent's invented plot ("The Last Hurrah": 39th-birthday cold open, chain-email hook, Holy Keg MacGuffin, Influencer Syndicate villain arc, all act beats) is **dead in its entirety** — it was written without author input and does not resemble the author's game. Gaps in the story are filled by interviewing the author, never by invention.

**The story core (author-dictated):**
- **Lord Pilsner has just gotten a divorce.** That's the trigger: three former college frat bros, all pushing 40, set out on one last big hurrah across Europe, convinced they've still got it — still hot, still able to do everything they did in their 20s without consequence. In reality: thinning, graying hair; beer guts; bodies that cannot hold up to that level of partying.
- **Chadwick and Bradley leave their wives at home** — and cheat on them across the trip.
- **Lord Pilsner secretly lives with his mom.** Post-divorce he moved back home; he told the guys he got his own place. He also has a recently acquired girlfriend who doesn't know he lives with mom — and he cheats on her throughout the trip too.
- **The Holy Keg is NOT the plot.** It stays exactly what the author wrote: Lord Pilsner's small personal side quest (`party.md`). It is never a MacGuffin, never the game's spine.
- **City bosses stand as written in the author's design docs** (The Craic Baron, Count Velvet Absinthe, Maestro Vice von Strauss). They are city content — wired into no quest spine, carrying no Keg fragments.
- **The Rival Trio appears exactly ONCE in the entire game**, in the Frat Bro NFT side quest (the Influencer Syndicate theft route). No per-city showdowns; the Syndicate is NFT-hunt flavor, not an antagonist faction.

**Bradley's wedding ring (author-dictated quest — replaces the dead pawn beat):** Bradley is still married. One night his wedding ring vanishes — one of their hookups took it, and she extorts him: pay up, or "What are you gonna do — tell your wife what happened to your wedding ring? Do I need to call her?" **The player decides:**
1. **Pay up** — cough up the money, get the ring back.
2. **Refuse** — Bradley has to call his wife and admit he "lost" his wedding ring. He is in the doghouse for the rest of the trip: every subsequent call to "Dear" makes it unmistakably clear, escalating until the end of the game when, as the bros get ready to fly home, she informs him she has **sold his DeLorean to pay for a replacement ring**.

**Act structure: DEAD (author ruling 2026-08-03).** All of the previous agent's act beats are killed — they existed only to serve the plot that agent invented, which is not and will not be the author's story. City order, opening scene, act framing, and Shamsterdam's placement are the author's to dictate. **Finale:** also awaiting the author's design ("The Legend" perspective-boss is dead); the author will design the ending after the rest of the story is settled.

**Endings.**
1. **"Still Got It" survives in concept** (author ruling 2026-08-03): the bros declare the trip the greatest of all time; the delusion survives, fully intact. The author will rewrite it to be utterly ridiculous once the rest of the story is settled — the Keg-tap staging is dead with the Keg plot. Nothing about this ending is written until the author writes it.
2. **NFT epilogue gag** (12/12 NFTs, per `fratbronft.md`, author-dictated rework 2026-08-03): post-credits stinger — Chadwick and Bradley's champagne-fueled "Crypto Kings of Europe" press conference, **CryptoBro69 at the podium doing the talking**, seconds before the market crash bankrupts them instantly. Police haul CryptoBro69 away mid-sentence; arms thrown skyward as they drag him off: **"DIAMOND HANDS FOREVER!"**

*The "Fistø Ending" (sincere mask-slip alternate ending) is killed by author ruling 2026-08-03. There is one ending: the delusion survives. Fistø exists only as the philosopher-janitor in the Public Restroom Graffiti quest — no ending arc, no sincere beat.*

### 4.3 City summaries (detail lives in `Design/Locations/`)

**Publandia** — author-dictated 2026-08-03: home to a dungeon housing minor boss **The Schnitzel King** (revived from the author's original pitch boss roster; dungeon concept in development with the author). Districts: Cobblestone Market Street, Temple Bar Alley, Brewery District, Liffey Walk, Kebab Alley (1 a.m.+). Key venues: The Bottomless Tap ("Infinite refills, infinite regret"), The Stoutworks Brewery, Trinity of Pints, Back Alley Betting Shop, The Back Room, The Lightweight Hostel, Dodgy Off-License, Café NORA. Boss: **The Craic Baron** (Surge Pricing, Round on Me, Hen Party Swarm, Sticky Floor). Enemies: Hen Party Swarm, Stag Do Berserker, Spill Sprite, Barkeep's Mop. Status flavor: Craic'd Up, The Fear, Fair Play. *Production status: mid-fidelity — needs per-venue docs to Debaucheryville standard.*

**Debaucheryville** — the flagship, fully designed (15 venue docs). Districts: Old Town Square, Clocktower Plaza, Absinthe Arcade district, Hostel Row, Kebab Alley/Underground Vice Corridor. Venues: Velvet Curtain Club (+VIP stall), Shadow Exchange, Cyberspace Kavarna, Internet History Museum → Meme Black Market, Cirque du Shady + Mystery Meat Cart, Mr. Chadz Kebabs, Absinthe Arcade, four breweries (The Absinthium Taproom, Three-Crown Keg Haus, The Tap Dat Vault, Ye Olde B.R.E.W. Lab). Boss: **Count Velvet Absinthe** (Green Fairy Confusion, Tourist Trap, Currency Scam, Strobe Mirage). Vendors: Mr. Chadz, Chef Chuckles, Donny.exe, MemeLord.exe, Mrs. Rata, The UV Man, Token Goblin.

**Shamsterdam** — the author's fourth city (content staged in the folder restructure). Author-dictated 2026-08-03: minor villain **The Weed Wraith** (revived from the author's original pitch boss roster). Full city summary to be written with the author when the staged files land.

**Sinfonia** — districts: Imperial Square, MusikGasse, Kaffeehaus Row, Trainspotting Square. Venues: The Bassline Opera House (day opera / night EDM arena), Mozart's Last Rave (crypt-club, undead DJ), Café Existenz, The Black-Tie Backroom, Baroness' Ballroom, Airbnb Palais, The Moderato Pub. Boss: **Maestro Vice von Strauss** (Crescendo Crush, Waltz of Weakness, Encore of Excess, Standing Ovation; tempo-synced fight). Signature systems: rhythm-timed combat bonuses, Masquerade Mode, etiquette checks, Art Authentication. *Production status: mid-fidelity — needs per-venue docs.*

### 4.4 Named NPC canon

Playable-adjacent and recurring: **Fistø** (philosopher-janitor, Public Restroom Graffiti quest ONLY — no ending arc; author ruling 2026-08-03), **Maestro Beerschi** (Selfie with a Local Legend), **Hamstradamus** (prophetic hamster, cryptic foreshadowing), **Slick Greg**, **Dmitri "The Router"**, **CyberGoth Katka**, **Vape Witch Vanessa**, **Backpack Girl Who Never Left** (gives the broken Game Boy used in Sinfonia), **Suspicious Twins Polina & Paulina**, **Ringmaster Vance "Vape" Vallaro**.

ICQ cast (Darkweb Dossier crossover): **Tony420**, **NarcGreg**, **CryptoBro69**, **Miss Morphine** (deliberately unresolved: person/bot/spyware — keep the ambiguity, it's the best joke in the cast), **richfield69**, **CryptoMamiXXX**, **Hamstradamus.eth**, **404_Bratnado.exe** (unlockable), minor trolls (TrollaLad420, Y2KBugZilla, NumaNumaNate, RedRoomRandy). Phone contacts: **Mom** — **Lord Pilsner's mom** (author-dictated rework, 2026-08-03): post-divorce, Pilsner secretly lives with her while telling everyone he got his own place. Free SP restore on first call per city stays, but the first call home plays over speakerphone as maximum embarrassment — she mothers her "little boy" like he's eight (is he getting enough sleep, brushing his teeth, eating well, not staying out too late; she bought him new trousers and needs him to try them on when he gets home) and exposes exactly how pathetic post-divorce life at mom's is, in front of the guys (Failure to Launch / Howard's-mom energy). Every later call lands at least one fresh dig. Nobody in any scene ever frames it as a lesson. Also: Bestie, Random Forum Troll, Shadow Tipster — and Bradley's calls to **"Dear"** (doghouse escalation per the wedding-ring quest, §4.2). **Hot Kroger Guy** (cameo — stays, author ruling 2026-08-03) gets one author-dictated scripted call: he found Lord Pilsner's girlfriend's phone left unlocked in her cart at Kroger, found Pilsner in her contacts, and calls to ask if Pilsner knows how to reach "this really pretty girl" so he can return her phone… and ask her on a date. "Does she have a boyfriend?" Pilsner — mid-trip, actively cheating on her — gets to sweat the inevitability of his girlfriend meeting Hot Kroger Guy face to face to get her phone back, and there is nothing he can do about it from Europe.

---

## 5. The Party — Canonical Character Kits

Shared stat block: **HP, Bravado (BP), Attack, Defense, Speed, Luck, Guts.** Guts = crit resistance and "shrug it off" checks (resisting Embarrassed, staying up at 1 HP with a *"Bro refuses to acknowledge the L!"* proc, EarthBound-style). Charm is a **social stat** used out of combat and by a few skills (see §6.5) — it lives on the sheet but has no base-damage role.

### 5.1 Base stats & growth (Level 1 → Level 30 cap)

| | HP | BP | ATK | DEF | SPD | LCK | GUT | Growth personality |
|---|---|---|---|---|---|---|---|---|
| **Lord Pilsner** | 45 | 22 | 11 | 10 | 8 | 7 | 10 | Even growth; ATK scales +1/turn *within* battles ("Drunk Boxing Leader" — stronger and more reckless as the fight runs long: +5% damage dealt AND taken per round after round 2, cap +25%) |
| **Chadwick** | 36 | 30 | 8 | 8 | 11 | 11 | 6 | Best BP pool & regen (+2 BP/turn baseline); fragile; Luck-leaning |
| **Bradley** | 60 | 16 | 13 | 13 | 6 | 5 | 12 | Tank curve; **Berserker Protector**: below 50% HP +15% ATK, below 25% HP +30% ATK and taunts are free actions |

Per-level gains (average): HP +6/+5/+8, BP +3/+4/+2, primary stats +1 to +1.5 weighted to personality. Full curve table generated in `data/balance/level_curve.json` (see §15.5); these anchors are canon: **Level 10 ≈ end of Publandia, Level 19 ≈ end of Debaucheryville, Level 27 ≈ Maestro, 28–30 = The Legend + postgame.**

### 5.2 Lord Pilsner — "The Legend in His Own Mind"

- **Role:** Inspiring Commander — balanced attacker + party buffer. **Bravado Style: Keg-Fu.**
- **Weapon line:** Ceremonial Beer Paddle → Weathered Pledge Paddle → Restored Chapter Paddle → Legendary President's Gavel (personal-quest reward: **Beer Paddle Mk II** sidegrade with party-buff-on-crit).
- **Special:** *Pint-Sized Rally* (8 BP) — party ATK +20% for 3 turns; 25% chance enemies gain *Secondhand Embarrassment* (−10% accuracy).
- **Ultimate:** ***Mid-Life Crisis*** (all remaining BP, min 20) — tears off shirt, screams about his prime: AoE damage = 2.5× ATK, party +15% crit for 3 turns, self gains **Reckless** (defense −25%, 2 turns). Upgrades: *Deluxe* (summons hallucinated pledges for 1 round — 3 extra weak hits), *Vintage* (enemies gain **Beer Goggles**: −accuracy, 10% friendly-fire).
- **Trees (§7):** Toastmaster (support), Barroom Tactics (control), Tall Tales (reality-bending RNG).
- **Overworld ability:** *Negotiate* — reroll one shop price or talk past one door per city district (always at some dignity cost).
- **Personal quest:** *The Holy Keg* — his chain becomes the main quest's B-plot; the final revelation is that the "legendary party" the Keg came from was one he wasn't actually invited to.
- **Flaw-as-mechanic:** *Wrong Legend* — when Pilsner delivers quest exposition, 20% chance the journal records his (wrong) version; correcting it via any NPC yields bonus Clout ("Fact-Checked!" +10).
- **Look:** frosted tips, puka shells, cargo shorts, Sidekick on belt. **Text-blip voice:** low, over-warm brass tone.

### 5.3 Chadwick — "The Influencer Nobody Asked For"

- **Role:** Chaotic Support — buffs allies with hype, debuffs enemies with cringe. **Bravado Style: Bro-Mancy.**
- **Weapon line:** Vintage Ring Light Mace → Flickering Ring Light → LED Content Creator Array → Professional Broadcast Halo (personal-quest reward: **Halo of Clout**). Ring light illuminates dark areas — the party's only genuinely useful tool, a running joke.
- **Special:** *Selfie Smite* (6 BP) — flash blind (single enemy, −25% accuracy 2 turns); 10% chance Chadwick trips while posting (loses next minor action).
- **Ultimate:** ***Viral Meltdown*** (all BP, min 20) — livestreams the battle screaming at haters: all enemies −20% accuracy and −15% ATK (Morale) 3 turns; allies gain **Audience Hype** (+3 BP regen/turn, 3 turns). Upgrades: *Global Trend* (affects reinforcements, +1 turn), *Brand Deal* (25% bonus "Sponsored Swag" item drop on victory).
- **Trees:** Cloutcraft (buffs/RNG), PR Spin (debuffs/silences), Live Service (economy/summon gags).
- **Overworld ability:** *The Algorithm* — reveals hidden interactables and secret social events on the current screen (30-second cooldown, phone-raise animation).
- **Personal quest:** *The Stolen Clip* — hunt the roommate who took credit for his one real viral moment (2009, dorm prank, local news). Ends in a live stream duel where winning honestly gets him fewer views than losing hilariously would have.
- **Flaw-as-mechanic:** *Chat Is Turning* — Chadwick's buff skills have a 10% "0 Viewers" backfire (buff becomes 1-turn Embarrassed on him). His ICQ followers leave sarcastic tips mid-quest.
- **Look:** backward trucker hat, popped collar, chain wallet, Nokia N-Gage. **Text-blip voice:** fast, high, autotuned warble.

### 5.4 Bradley — "The Muscle with a Dad Bod"

- **Role:** Tank / Crowd Controller, Berserker Protector. **Bravado Style: Frat-Sorcery.**
- **Weapon line:** Broken Pool Cue Staff → Weighted Fighting Stick → Legendary Pub Champion's Rod (personal-quest reward: **Staff of the Stag**). Pool tables act as power-up stations (+10% ATK for that battle, once per venue).
- **Special:** *Protein Slam* (7 BP) — restores 25% max HP and burps a stun cloud (30% stun chance, adjacent enemies, 1 turn).
- **Ultimate:** ***Bouncer Breaker*** (all BP, min 20) — stuns all enemies 1 turn + heavy single-target (3× ATK). Upgrades: *XXL* (grabs an enemy and uses it as the weapon — AoE splash 50%), *House Rules* (target gains **Thrown Out** — misses its next reinforcement/entrance). 
- **Trees:** Brawl Science (damage), Security Professional (taunt/control), Recovery & Reps (sustain).
- **Overworld ability:** *Move It* — breaks cracked obstacles, shoves furniture, intimidates one guard-type NPC per district.
- **Personal quest:** *Brawler's Crown* — win a (consensual, barroom-rules) fight in every pub; final "all bouncers allowed" arena; passive reward **Crowd Favorite** (+2 Guts while taunted). The pawned-wedding-ring beat in Act 2 belongs to him.
- **Flaw-as-mechanic:** *Gym Brain* — refuses party fast-travel if an undiscovered gym/protein vendor is on the current map (marker appears; visiting it clears the block and gives a small buff — the detour is always mechanically worth it, which is the joke).
- **Look:** Livestrong bracelet, oversized jersey, baggy jeans, two pagers. **Text-blip voice:** slow, deep thuds.

### 5.5 Party-wide rules

- All three are always in the party (no swapping in V1.0); any bro at 0 HP is **"Passed Out"** and revived to 1 HP after battle (EarthBound-style defeat only when all three drop — see §6.7).
- **Flirt** is a universal battle/overworld action that **always backfires** — its only outputs are comedy, region-specific fail states, occasional accidental quest triggers, and a guaranteed −1 dignity narrator line. It costs nothing and heals nothing. Players will press it anyway. That's the design.
- Equipment slots (canon, resolves the slot/category mismatch): **Weapon · Torso · Legs · Footwear · Accessory ×2** — necklaces, rings, watches, hats, and cellphones are ALL "Accessory"; exactly one equipped **Cellphone** is additionally required in Accessory slot 1 (it's the save/ICQ device and its model grants perks — see §9.4).

---

## 6. Combat Bible

The battle system is the product's spine. It is EarthBound's chassis — front-view, menu-driven, rolling HP — with Bravado, ego dynamics, and Combos layered on top.

### 6.1 Presentation

- **Front view.** Enemies are static front-facing sprites (1–2 frame idle wobble max) composited over a **two-layer psychedelic background** (palette-cycled + sine-distorted shader — see §13.6). The party is represented by three **odometer boxes** (HP / BP) along the bottom, EarthBound-style. No party battle sprites: this is the single biggest scope saver in the genre and it is genre-authentic.
- **Encounters are visible on the map.** Touching an enemy starts battle; approaching from behind = preemptive round; getting tailed = enemy free round. Enemies 5+ levels below the party resolve as **instant auto-win** ("You won without embarrassing yourselves. Barely.").
- **SMAAAASH!!** crits use the full banner + screen shake + strong haptic.
- Enemy names are absurd noun phrases in the EarthBound tradition: *Hen Party Swarm, Stag Do Berserker, Spill Sprite, Barkeep's Mop, The Expat Who Never Left, Silent Bouncer, Backpack Bard, Pickpocket Pair, Green Fairy Wisp, Crypto Clown, Rigged Carnival Game, Knife-Throwing Assistant, Masked Patron, Pastry Golem, Critic's Quill, Dance Duelists, The Maestro's Harried Assistant…*

### 6.2 Turn flow & action economy

State machine: `INTRO → ROUND_START → [per combatant: SELECT → RESOLVE → ANIMATE] → ROUND_END → (VICTORY | DEFEAT | ESCAPE)`.

- **Initiative:** turn order by Speed, modified by Bravado band (High +2 SPD, Low −2 SPD) and environment (Sinfonia venues can lock turn order to the music's beat grid).
- **Per bro, per turn:** 1 **Main Action** + 1 **Minor Action**.
  - Main: **Bash** (basic attack; submenu holds **Brace** = defend, halve damage + 2 BP regen), **Brag** (Bravado skills/spells), **Combo** (if available).
  - Minor: **Item**, **Taunt**, **Bravado Flex** (+3 BP, +5% next-attack damage, small chance a watching NPC heckles), **Flirt** (see §5.5).
- **Interrupts:** specific skills fire off-turn (Bradley's *"Bro, Do You Even Lift?"* counter-taunt; Sidekick phone's *Ping* 5% interrupt).
- Battle menu = 4 large touch targets: **Bash / Brag / Items / Chicken Out** (C15). Chicken Out = flee: success = `own SPD avg / (own avg + enemy avg)`, +20% if any bro is Embarrassed (shame is aerodynamic). Bail-Out Card = guaranteed escape.

### 6.3 The rolling HP meter

HP damage doesn't subtract instantly — the odometer **ticks down at 2.5% of that bro's max HP per second** (tunable). A mortal blow can be outrun by healing or by winning first. Instant-kill effects and defeat-at-0 still apply when the meter *reaches* 0, not when damage is dealt. This is mandatory, load-bearing, EarthBound DNA — it converts turn-based combat into real-time triage tension, and it's why battles stay exciting at 5 minutes a session.

### 6.4 Damage model (canonical formulas)

```
Physical damage  = (ATK × SkillMult + BravadoMod − TargetDEF) × Variance × CritMult × EnvMult
BravadoMod       = +15% of base damage at High Bravado band, −10% at Low, −20% at Zero
Variance         = 0.9 – 1.1 uniform
CritMult         = 2.0 ("SMAAAASH!!")   CritChance = 4% + LCK × 0.5% + skill bonuses − target GUT × 0.4%
EnvMult          = regional: beer-tagged moves ×1.5 in Publandia; vice-tagged ×1.5 in Debaucheryville
                   (with 15% "lost control" self-mishap); rhythm-tagged ×1.5 in Sinfonia when
                   beat-timed (tap timing bonus)
Accuracy         = 92% base − target evasion (SPD-derived) − attacker accuracy debuffs
```

(The docs' regional ×2 multipliers are reduced to ×1.5 — ×2 broke balance math at every level band tested on paper. Tune from 1.5.)

### 6.5 Bravado — the resource (BP)

Confidence as mana. Per-bro pool (§5.1).

- **Spend:** skills (4–10 BP), Ultimates (all BP, minimum 20 — Ultimates are only available at High band).
- **Gain:** Bravado Flex (+3), Brace (+2), landing crits (+4), kills (+3), NPC crowd cheers (+1–3/round based on Reputation), winning drinking/rhythm minigames (out of battle, sets starting band), Chadwick auras.
- **Drain:** being missed-at (whiff = −2 to attacker), public embarrassment events, **Sobriety Creep** — outside battle, each in-game hour without a drink/social win drains 2 BP (day-night system, §11.3).
- **Bands:** High = >70% pool (Ultimates unlocked, +crit, +SPD; sprite glows, crowd murmurs) · Mid = 30–70% · Low = <30% (−damage, −SPD; slouched sprites) · **Zero = "Dad on a Bender"** — the bro collapses into a sulk: skips turns until healed to Mid by items/allies; if all three hit Zero simultaneously, forced comedic retreat (treated as defeat-lite: wake at base, small € loss, unique narrator scene).
- Combined-Bravado gates for Combos: **High ≥ 150 total (80% success) · Mid 90–149 (60%) · Low < 90 (40%)** — matching the doc's bands with the >150 anchor.

### 6.6 Master status list (canon — resolves all drift)

**Positive:** Liquid Confidence (+3 Charm-checks, +2 BP/turn, −1 accuracy step; 3–5 turns) · Gains Bro (+20% ATK, 2 turns) · Hydrated for Once (immune Hungover, +1 HP regen/turn, until next alcohol) · Manic (+3 SPD, −2 accuracy steps, **two Main Actions**, 2 turns → then Crash) · Heart Palpitations (+1 turn priority, −1 HP/turn, 3 turns) · Hardcore Gamer (+2 SPD, +5% crit, −1 HP/turn, 2 turns) · Inspired (+Charm, +crit) · Audience Hype (+3 BP regen) · Protected / Heroic (Bros Before Heroes) · Insomniac Clarity · Scam Aware · VIP Status / Club Stamped · Fair Play · Untouchable, Entertained, Extreme (item-granted, per §9).

**Negative:** **Hungover** (−20% all stats, −1 HP/turn, 25% skip turn; 3–5 turns; cures: time, Advil, greasy food, Sextuple Espresso) · Sloppy (−3 accuracy steps, 15% friendly fire; 1–2 turns) · **Embarrassed** (−20% ATK, −2 BP/turn, Ultimates & Taunt locked; 2–3 turns; scaling by Clout tier per §7.3) · Grease Fingers (−2 accuracy steps, tech items locked, 4 turns or washed) · Beer Goggles (−accuracy, 10% friendly fire) · Reckless (−25% DEF) · Crash (−3 all stat steps, 75% skip, 3 turns) · Confused/Green Fairy Confusion (random targeting) · Cringe / Cringe Lock (combo lockout) · Thirsty (regen halved) · Regret Rash (−Luck, 3 battles) · Meat Doubt, Greasy Coma, DigiDysentery (menu buttons inverted 2 min), Dysentery (Light), Socially Rejected, Bloated, Pixel PTSD, Mentally Unwell, Blue Screen, Signal Loss, Off-Tempo (−SPD next turn), Party Foul (−BP), Tourist Trapped (shop prices ×2 until rest or 3 areas), Broke AF, Lost AF, Reputation Ruined, Wrist Rash (flavor).

**Special:** **Blackout Drunk** (Liquid Confidence + Sloppy + memory loss: battle ends, wake in random location minus random items — used ONCE as scripted story beat in Act 2, then available as a rare organic outcome of stacking alcohol) · **Existential Crisis** (all abilities become *Question Life Choices* [does nothing]; 2 turns or ally uses **Snap Out of It**). *(The "Perspective" status is killed by author ruling 2026-08-03 — no sincerity/moralizing mechanics, ever.)*

Rules: same status doesn't stack, reapplication refreshes duration; one cleanse tier (Advil cures any one negative status + small HP; specific cures listed per status win over generic). "Accuracy steps" = −8% each. Full machine-readable table: `data/balance/status_effects.json`.

### 6.7 Combos (canonical set — one version per combo)

Unlock gates by Clout tier (§7.3). Trigger: both/all participants select **Combo** on the same round with the required Bravado band. Success rolls the band percentage; failure fires the Backfire. Failed combos permanently unlock small **"Never Again"** passives (+2% resist to that backfire's status). **Snap Out of It** (any third bro's minor action) clears combo-lockout states.

| Combo | Bros | Effect (success) | Backfire |
|---|---|---|---|
| **Beeramid Blast** | Pilsner+Bradley | 2.5× AoE, all enemies stunned 1 turn (2 in Sinfonia), both +2 BP | Collapse: both take 10% maxHP, Pilsner Embarrassed |
| **Like & Subscribe** | Chadwick+Bradley | Bradley's hit ×2; 25% **Viral Crit** (×3 total); party +2 BP regen 2 turns; fake chat overlay | "0 Viewers": both −6 BP, Chadwick Embarrassed |
| **Wingman Protocol** | Chadwick+Pilsner | Charm one humanoid enemy 2 turns (acts for you); fails automatically vs robots/animals | Rejection: both −5 BP, gain **Rejected** (−10% ATK 2 turns) |
| **Double Chug** | Pilsner+Bradley | Both gain Liquid Confidence | Both puke: **Sloppy** + party-wide 1-turn stun (in Publandia the crowd cheers: +2 BP anyway) |
| **Bros Before Heroes** | Bradley+ally<25%HP | Bradley intercepts all damage for that ally 2 turns; ally **Protected** (+50% damage, status immune); Bradley pays 25% current HP, gains **Heroic** (+1 GUT permanent, once/battle) | — (always works; the cost is the joke: "No man left behind — except defense stats") |
| **Alpha Sigma Slam** | all three | 3× AoE + full party BP restore; at ≥150 combined BP becomes **Alpha Sigma Thunder**: also grants **Legendary** (+1 all stat steps rest of battle) | 12%: chant devolves — self-stun + psychic cringe damage (doubled if anyone Embarrassed) |
| **Spotlight Clash** | any two Ultimates same turn | — (always a failure state) | Both cancel, massive BP loss, enemies act free; third bro's Snap Out of It breaks it |
| Regional: **Tavern Takeover / Casino Royale / Symphony of Bros** | all three + venue | Set-piece finishers with NPC participants; unlocked at Regional Mastery 400+ (§7.4) | Venue-specific (guards, enrage, collapse) |
| Equipment: **Legendary Douchebags / Connection Failed / LinkedIn Lament** | full sets (§9.4) | As specced in equipment docs | — |

Competitive combos (*Who Flexed Harder?*, *Toast vs. Post*, *Who's The Alpha?*) are **in-party gamble actions**: opposed rolls trade Bravado between bros with audience-overlay gags; net-neutral resources, morale texture. The **Dynamic Ego/Spotlight meter** tracks kills+crits per bro; the leader gets +5% damage ("showing off"), the trailing bro −1 BP regen ("sulking") — placate via Taunt-praise minor action. Numbers deliberately small: it's a texture system, not a rotation.

### 6.8 Enemy design & AI (fills `enemyai.md`)

Roster targets: **10–12 regular enemies + 1 boss per city**, plus ONE rival-trio fight in the entire game (NFT sidequest only — author ruling 2026-08-03). Every enemy = 1 static sprite + palette-swap variant budget.

AI is data-driven weighted-random with gates (EarthBound-simple, LimboAI behavior trees):
- Each enemy: 2–4 moves with weights + conditions (`hp<50%`, `target_has_status`, `round>2`).
- **Archetypes:** Swarmer (multi-unit, weak, Hen Party Swarm), Bruiser (Stag Do Berserker), Debuffer (Spill Sprite → Grease Fingers), Leech (steals SOVS: Pickpocket Pair), Cringe-caster (attacks Bravado not HP: Backpack Bard's ukulele solo), Gimmick (Rigged Carnival Game only damageable after its "rules" are Bragged at).
- **Reality Check enemies are killed by author ruling 2026-08-03** — no moralizing enemy types, ever. Enemy direction (author): EarthBound-style enemies drawn from the satirized/parodied cities and each city's TRUE seedy underbelly — late-night partying, sex workers, hookups, drugs, drinking, heavy nightlife — played straight, no hand-wringing or pearl-clutching. The audience is Folklore / South Park / GTA players. Specific new rosters get proposed to the author for approval before becoming canon.
- Bosses: 2–3 phases, phase scripts + telegraphed "big move" rounds; **bosses drop status immunity but keep vulnerability windows** (e.g., Craic Baron's Sticky Floor round leaves him Distracted for 1 turn).

### 6.9 Victory, defeat & rewards

- **Victory:** Clout + € + drop table roll; regional **Victory Stinger** sung couplet (§14.3); "promotion" flavor titles on notable wins (bouncer fight → *Bathroom Attendant*: Nightstick, Glowsticks ×2, Half Bottle of Advil, +300 €, +150 Clout — the canonical worked example).
- **Defeat (all three at 0 HP):** wake at base pub; keep Clout and items; lose 10% € ("the tab found you"); mandatory Hungover; unique narrator roast per city. No lost progress — mobile-friendly, and shame IS the death penalty.
- Balance targets (from Production docs, kept): normal fights **3–5 rounds**, bosses **6–8**, baseline survivability = 2–3 mistakes before wipe.

---

## 7. Progression — Clout, Levels & Skill Trees

### 7.1 Clout

**Clout = XP.** It only accumulates (C7). It simultaneously drives level (stat growth, §5.1) and unlocks **Bro Ladder tiers**:

| Tier | Clout | Unlocks |
|---|---|---|
| **Pledge** | 0–99 | Tree tier 1 (the 100-node row unlocks AT 100) |
| **Active** | 100–299 | Tier-1 nodes; basic combos |
| **Alumni** | 300–599 | Tier-2 nodes (250-row), Beeramid Blast, Like & Subscribe, Wingman Protocol |
| **Legacy** | 600–999 | Tier-3 nodes (400-row) + 700-row, Alpha Sigma Slam/Thunder, Bros Before Heroes, competitive combos |
| **Living Legend** | 1000+ | 1000-row capstones, Legendary Douchebags, **Midlife Crisis Mode** (all three at LL: +20% power, 25% per attack to "throw out their back" [1-turn self-stun], +BP drain), NPC reaction ladder maxes out ("BOW BEFORE THE LEGENDS" / "Security! SECURITY!") |

Earn rates budgeted so a completionist hits ~1000 Clout at Sinfonia's midpoint and a mainliner hits Legacy by Maestro. Skill nodes **unlock at thresholds — no spending** (C7). Embarrassment scales with tier (the price of legend): Pledge = −1 BP/turn while Embarrassed; Living Legend = −3 BP/turn, party-wide *Secondhand Embarrassment* (−1 BP/turn all bros), combos locked 2 turns.

### 7.2 Skill trees (canonical, per `skilltrees_cloutspells.md`)

Three branches per bro, five nodes per branch (100/250/400/700/1000). Full node effects live in `data/balance/skills.json`; headline capstones:

- **Pilsner:** Toastmaster → *Final Call* (700: single-use battle rez — "Last call, bros!") → *Mythic Keg Summon* (1000). Barroom Tactics → *Pub Takeover* (1000: the entire bar joins the fight). Tall Tales → *Rewrite History* (1000: retcon one failed action per battle into success).
- **Chadwick:** Cloutcraft → *Algorithm Manipulation* (700: control RNG 3 turns) → *Global Phenomenon* (1000: abilities hit twice). PR Spin → *Cancel Culture* (100, 1-turn silence) → *Complete Character Destruction* (1000: remove one non-boss enemy via cancellation). Live Service → *Parasocial Army* (1000: summon imaginary fans).
- **Bradley:** Brawl Science → *One-Punch Chad* (1000: instant-KO attempt — yes, the name stays; Chadwick objects in a banter line, which is why it stays). Security Professional → *Club Ownership* (1000: battlefield control). Recovery & Reps → *Immortal Bro* (1000: cannot die 5 turns).

Personal-quest spell unlocks (independent of trees): Pilsner *Final Keg Stand*, Chadwick *Algorithm Blessing*, Bradley *Final Roundhouse Slam*.

### 7.3 Regional Mastery

Per-city Clout counters (earned in that region) unlock at 400/700/1000: Publandia crowd-participation → *Local Legend* (NPCs buy drinks = free BP) → *Honorary Publandian* (beer-tag ×1.5 → ×2); Debaucheryville jackpot mechanics → *High Roller* → *Chaos Lord* (random beneficial procs); Sinfonia timing bonuses → *Beat Master* → *Symphony Conductor* (once per battle, dictate one enemy's action).

### 7.4 Mobile progression UX

Clout unlock toasts with satirical copy; the skill tree is visualized as a **frat house** (basement → roof); ego meter physically inflates; favorite spells pinnable to the Brag wheel; auto-suggest available combos with a "COMBO READY" pip.

---

## 8. Social & Reputation Systems

### 8.1 Collective reputation

One shared meter per city — the world rates the trio as a unit (**"Those Three American Idiots"**). Five states per city, event-driven transitions (not points): Publandia **Drinking Ladder** (Clueless Tourists → Pub Crawl Rookies → Beer Garden Regulars → Honorary Drinking Buddies → Legendary Lightweights), Debaucheryville **Vice Hierarchy** (Obvious Marks → Useful Idiots → Vice Apprentices → Chaos Catalysts → Lords of Misrule), Sinfonia **Sophistication Spectrum** (Cultural Barbarians → Eager Students → Adequate Appreciators → Refined Gentlemen → Honorary Viennese).

Mechanical hooks per state (as designed): shop price modifiers (+50%/+100% at the bottom, discounts at the top), venue/dialogue gating, combat crowd behavior (BP regen ±1–3/round), NPC assists, regional set-piece combos at state 5. **Reputation destroyers** are scripted instant events (ordering an "Irish Car Bomb" = reset to state 1; moralizing in Debaucheryville = exile from fun districts; cultural vandalism in Sinfonia = immediate exile). Cross-city spillover: prior-city fame = +1 starting state; combined titles (*Cultured Drunks*, *International Incidents Waiting to Happen*) are cosmetic epithets with one dialogue branch each.

Implementation: each ladder = an int 1–5 in `GameState.reputation`, transitions fired by the event-flag system (§15.4). UI shows the state name + "The locals seem..." descriptor — never a progress bar.

### 8.2 Street Rep & dialogue

**Street Rep** = a small global modifier (0–10) raised by witty dialogue choices; grants vendor discounts (−2%/point, cap −15%) and unique dialogue. Dialogue system spec (fills `dialoguesystem.md`): Dialogic 2 timelines; 2–3 choice branches max; choice consequences limited to flags, €, BP, Street Rep, and item grants (the effect grammar of §15.5 — no freeform effects). Quoting discovered graffiti to matching NPCs unlocks hidden responses/discounts (graffiti quest hook).

### 8.3 Social combat & minigames

Some encounters resolve verbally: a 3-round exchange where each bro has one social verb — Pilsner **Storytelling** (Charm + Tall Tales tier vs. credibility), Chadwick **Influence Flexing** (Luck-weighted), Bradley **Intimidation** (GUT + ATK-weighted). Resolution = opposed roll `d100 + stat×5 + rep-state×5`; win = quest progress/€/BP, loss = Embarrassed + comedy (never a hard fail — social combat losses always open a worse-but-funnier alternate path).

Minigames (one input pattern each, reused): **drinking contests** = tap-timing meter (refusing a round = Party Foul, −BP); **rhythm checks** (Sinfonia, karaoke, Tap Dat Vault) = 4-lane beat taps; **pouring/claw/scam games** (Debaucheryville) = timing-stop wheels, visibly rigged (the rig is the joke; Scam Aware status reveals the true window); **T9 texting minigame** (Nokia N-Gage perk) = word-entry speed gag.

---

## 9. Economy, Items & Equipment

### 9.1 Currency & flow (fills `Design/Economy/`)

**Euros (€)** only (C6). Sources: battle rewards (level×8–15 € per fight), quest payouts, selling gear, Shadow Exchange conversions. Sinks: shops, **Cover Charges** (district doors, 5–50 €, waived at high reputation — the money-sink event that keeps the old currency name alive as a joke), bribes, brewery tour fees, taxi vouchers, scams (mechanically: money you "chose" to lose), Bail-Out Cards, verification fees (Shadow Exchange, 10 €).

Target curve: the party should feel broke in the first third of each city and comfortable at the end — then arrival in the next city (new prices, new scams) resets the squeeze. Wallet at city end: ~800 € (Publandia) / ~2,000 € (Debaucheryville) / ~4,500 € (Sinfonia). Prices in `data/balance/economy.json`; anchor prices: pint 4 €, kebab 5–9 € (per the written menus), gear 30–400 €, XP Ring from eBaum's World 50 € (as written).

**Crypto Coins**: worthless gag currency from scams; only the Meme Black Market and one Tony420 trade accept them. **NFTs**: quest collectibles, not currency (§10.3).

### 9.2 Consumables (canon list = `items.md`, priced)

Rarity ladder: **Common / Uncommon / Rare / Legendary / Mythic**. Highlights (full table → `data/items/consumables.json`): Muscle Milk (Chalky Vanilla) 8 € · Advil (Half Empty Bottle) 12 € · Chug of the Gods 15 € (party heal, 15% Sloppy) · Aquafina (Room Temperature) 3 € (cures Hungover → Hydrated for Once) · Bail-Out Card 40 € · Four Loko (Original Recipe) [Legendary, 120 €] (revive +75% HP, Manic; **cannot use while Sober** — "Sober" simply = not under any alcohol status) · Sextuple Espresso [Mythic, 200 €] (full party HP, Heart Palpitations; also THE Hungover hard-cure) · BAWLS Guarana 25 € · Stale Beer Nuts 5 € · Axe Body Spray (Concentrated Blast) 18 € (AoE + Overwhelmed) · Roast Card (Savage) 30 € (damage scales with target's current Bravado/morale) · Fake ID (Laminated at Kinko's) 60 € ("Works 60% of the time, every time") · Hair Gel (Industrial Strength), Glow Sticks (Rave Quality), Portable DVD Player (7-inch Screen) [Legendary], Monster Energy (Original Formula) [Mythic revive-all], Duct Tape (Half Roll), Disposable Camera (12 Shots Left), Bluetooth Earpiece (Blinking LED) · regional: Absinthe Shot (Prague Special), Guinness (Room Temperature) (grants *Philosophical*), Sachertorte Slice (grants *Refined*), the four brewery beers (Absinthe Lager, Iron Gut Tripel, Vape Stout, Blockchain Bock — each a strong buff with its designed drawback), Legendary Hangover (per-city trophy consumable: "You don't remember last night, but everyone else does.").

### 9.3 Equipment

Slots per §5.5. All equipment stats **map to the core 7 + Charm**; the ~50 joke stats in `equipment.md` (Dad Energy, Tourist Vibes, Douchebag Aura…) are **flavor lines displayed on the item card**, not mechanics — EXCEPT where a joke stat names a real hook (…+3 Item Slots = real inventory slots; −2 Speed = real; theft-chance, ICQ-compatible = real). Rule: **numbers shown in white are mechanical; gold italic "stats" are vibes.** This one presentational rule resolves the stat chaos while keeping every joke.

Sets (all four now defined): **The Full Frat Bro** (Bradley), **The Influencer** (Chadwick: Trucker Hat + Deep-V + Ring Light accessory + N-Gage → *Influencer Deluxe*: Viral Crit chance doubled), **The Alumni** (Pilsner: Class Ring + blazer torso + pleated khakis + loafers → *Old Glory*: +2 BP regen, Embarrassed resist), **Cringe Business Casual** (any bro: Bluetooth Earpiece + Polo + Khakis + money clip → *LinkedIn Lament* combo), plus **Tech Bro Wannabe** and **Suburban Dad Regression** as flavor sets. Relics (Pager: 911-text BP surge 1/dungeon; T-Mobile Sidekick: *Ping* 5% interrupt) keep their designed effects.

### 9.4 Cellphones

One equipped cellphone required (Accessory 1). Models are progression sidegrades: **Nokia N-Gage** (ICQ compatible, immune Signal Loss, T9 minigame) · **BlackBerry Pearl** (Business Mode: +2 Negotiation one battle) · **Palm Treo 650** (−1 accuracy, stylus missing — a trap item with the best flavor text) · **Windows Mobile PDA** (+3 "Business Cred" [vibes], random Blue Screen) · **T-Mobile Sidekick** (Pilsner's default; Ping relic). The phone is the diegetic ICQ/save device (§11).

### 9.5 Shops (fills `shoptypes.md` / `blackmarket.md`)

Types: General store (Hair of the Dog, Midnight Munchies) · Equipment (Sole Mates, Threads & Treads, Neon & Chrome, Haute Couture Haberdashery, The Cultured Corner) · Food vendors (stat food; Mr. Chadz, Chef Chuckles, Donny.exe, carts) · **Black market** (Shadow Exchange: rate-board minigame, barter window, Notoriety risk meter, post-boss premium stock — already prototyped in code; Meme Black Market: meme summons + MemeMastery meter) · Circus Prize Booth (token economy). Shop prices modulated by reputation state, Street Rep, Tourist Trapped, and 3 A.M. price drops.

---

## 10. Quest & Content Inventory

Scope tiers: **[CORE]** ships in V1.0 or the game doesn't ship · **[FULL]** ships in V1.0 target scope · **[STRETCH]** post-launch/update material. This is the complete inventory of everything designed in `Design/Quests/` with its verdict.

### 10.1 Main quest [CORE]
"The Last Hurrah" per §4.2: 3 city arcs, 3 rival showdowns, 3 city bosses, The Legend finale, 2 endings + NFT epilogue.

### 10.2 Personal quest chains [FULL]
- **Pilsner — The Holy Keg** (merged into main quest B-plot; rewards Beer Paddle Mk II, *Legend of Me* upgrade, hidden keg-tap vendor key).
- **Bradley — Brawler's Crown** (pub champions → college rival rematch → all-bouncers arena; Staff of the Stag, Bouncer Breaker XXL, *Crowd Favorite*).
- **Chadwick — The Stolen Clip** (stolen video hunt → influencer gauntlet → live stream duel; Halo of Clout, *Global Trend*, out-of-combat BP-regen emote).

### 10.3 Global sidequest lines
| Quest | Tier | Notes |
|---|---|---|
| **Brewery Tour** (12 breweries, bottle-opener-gated) | [CORE] | Debaucheryville's four fully designed; author Publandia/Sinfonia sets to the same template. Rewards: regional beers, per-city Legendary Hangover, *Continental Beer Master*, Brewmaster Selfie collectibles. |
| **Public Restroom Graffiti** (9 shrines) | [CORE] | Fistø appears here ONLY as the philosopher-janitor — comedy, no ending arc, no alternate-ending flag (author ruling 2026-08-03). Titles: *Street Philosopher*, *The Greasy Prophet*, *Joysticks & Shame*; Dry Marker of Revelation. |
| **Frat Bro NFT Hunt** (9 NFTs) | [CORE] | Milestones 3/6/9: badge → *Wallet of Shame* (+1 Charm, "forever marking you as that guy") → crypto-crash epilogue. NFTs are JOKES + collectibles — zero blockchain anything (§17.2). |
| **The Great Döner Debate** | [FULL] | Three vendors, Tony420 ICQ poll, *World's Pickiest Drunk* (already has a structured JSON passive — the effect-schema template). |
| **Darkweb Dossier ICQ events** | [FULL] | Ambient content system: per-city ad batches + chat logs; raunch ceiling per C19. |
| **The Couchsurfing Chronicles** | [FULL] | 1–2 spots/city; Morning After Album; *Slept Around, Found Out*; Regret Rash roulette. |
| **Meme Black Market + MemeMastery** | [FULL] | Debaucheryville anchor content; 3:33 A.M. gate; *Shitposter Supreme*; 404_Bratnado.exe. |
| **Underground Karaoke League** (Sinfonia) | [FULL] | Rhythm minigame reuse; Golden Mic (+Charm). |
| **Lockpick Lullaby, ICQ Scammer Sting, Club Flyers, NFT city hunts** | [FULL] | Debaucheryville local quests as designed. |
| **Vinyl Hunt** (battle-track remixes) | [STRETCH] | Requires alt music stems; design is one line. |
| **Street Performer Trials / Taxi Driver Confessionals / Selfie with a Local Legend / Wi-Fi Roulette** | [STRETCH] | Stubs; cheap to add post-launch as event content. |

### 10.4 Content debt (must be authored — currently placeholders)
Publandia + Sinfonia venue docs to Debaucheryville fidelity · Publandia/Sinfonia brewery quartets · Publandia/Sinfonia local quest folders · NPC backstories doc · all dialogue (budget: ~25,000 words of NPC/system text for V1.0 — EarthBound-density, Google Sheets → JSON pipeline per Production docs) · enemy roster stats · bulletin board copy (~10 boards/city).

---

## 11. Interactables, ICQ & the Save System

### 11.1 The phone is the platform

The equipped cellphone (§9.4) hosts: **ICQ** (story chats, Darkweb Dossier events, scam popups — "Uh-oh! You've got a message!"), **quest log** (restates context on relaunch — mobile session requirement), **Morning After Album** (couchsurf/selfie gallery), **Napstur** (iPawd perk: random stat-boosting tracks), contacts (Mom = free SP/BP restore, first call per city — the Homesickness homage).

### 11.2 Save system (fills `save_load.md`)

- **Diegetic layer:** Wi-Fi hotspots ("FREE Wi-Fi" signs, 6–10/city) are full-service save points: save, heal-once flavor, ICQ event trigger, rumor hint.
- **Real layer (mandatory):** **continuous autosave** — on map change, battle end, dialogue branch, purchase, and `NOTIFICATION_APPLICATION_PAUSED`/backgrounding. Mobile OSes kill backgrounded apps; the diegetic hotspot is a *skin*, never the actual persistence gate.
- Three manual slots + rotating autosave slot + backup snapshot (corruption recovery: checksum, fall back to snapshot). Cloud: iCloud/Play Games Services via the Foundation-maintained plugins. Save schema versioned from day one (§15.6).

### 11.3 World clock (fills `daynightcycle.md`)

In-game clock runs 1 game-hour ≈ 1 real-minute while exploring (paused in battle/dialogue/menus), **plus scripted jumps** ("that night…"). Drives: pub crowds, venue hours (Tap Dat Vault midnight-only; Kebab Alley 1 A.M.+; 3:33 A.M. Meme Black Market kiosk; 3 A.M. price drops; Dead Hours), Sobriety Creep, hotspot ICQ schedules (Tony420 online 3–6 A.M.). A **"Wait/Pre-game until…"** bench action lets players skip to any hour — never make a mobile player wall-clock wait. All the docs' conflicting time gates (3:00/3:33/1–3 A.M.) stand as written; the bench action makes them friction-free.

### 11.4 Interactable object systems

- **Bulletin boards** [FULL]: pixel posters, satirical ads ("Got Soap?"), rumor hints; per-city *Poster Collector* title.
- **Graffiti** [CORE]: status-gated reveals (some only visible while Hungover), lore drops, quote-collection for §8.2 dialogue unlocks; system doc = the de facto mechanics already written in the restroom files.
- **Vending machines** [FULL]: simple item dispensers + 2 scripted specials (gutted Kavarna machine; CryptoDoner access point).
- **Wi-Fi hotspots** [CORE]: §11.2.
- **Cellphones-in-world** [STRETCH]: ringing payphones/lost phones as one-off gags.

---

## 12. UX / UI & Accessibility

### 12.1 Global layout

Landscape (C14). Safe-area aware on notched devices (`DisplayServer.get_display_safe_area()`); all interactive elements ≥ 48 px touch targets, thumb-zone mapped (primary actions bottom corners; standard vs Max-size layouts auto-adjust; one-handed and two-handed layout toggle).

- **Overworld:** floating virtual joystick (appears where the left thumb lands, invisible at rest) + contextual tap (tap NPC = talk, tap chest = open, tap self = menu). Interact button bottom-right mirrors context icon. Full MFi/Bluetooth gamepad support.
- **Battle:** per the mockup evolved — top: turn-order portrait strip; center: enemies over shader background; bottom: 3 rolling odometer boxes + the 4-button grid (**Bash / Brag / Items / Chicken Out**); status chips animate on the strip, long-press a chip = cure shortcut into inventory. Gesture shortcuts: swipe-repeat last action; two-finger tap = Brace-all.
- **Menus:** nine-slice retro panels, bitmap font at 2–3× integer scale, ≤ 25 characters per UI label (localization rule).

### 12.2 Microinteraction "juice" standard (kept from Production docs)

120 ms button bounce · 12–20 particle hit-sparks · SMAAAASH banner + screen shake + strong haptic on crit · rolling HP tween 1–2 s · haptic map (crit = strong, pickup = light, cure = double-pulse, boss intro = long rumble) with a global toggle honoring OS settings.

### 12.3 Accessibility (App Store table stakes, per `UX & Accessibility Guide.md`)

VoiceOver/TalkBack strings + battle-log announcements; focus order locked before alpha · dynamic text scaling (font token system, max line lengths) · high-contrast palette toggle (tested via Sim Daltonism/Coblis + greyscale pass; automated colorblind-simulation screenshot check in CI) · dyslexia-friendly font toggle · Reduced Motion mode (kills shakes, particles, background oscillation — battle backgrounds fall back to slow palette cycle only) · battle animation speed Normal/Fast/Off · chat-speed toggle + long-press fast-scroll · **musical interludes toggle** (the sung stingers are skippable) · first-launch accessibility onboarding screen (text size, contrast, haptics, motion).

### 12.4 First 10 minutes

Priority-one QA target (per Dev Skills doc). Cold open (birthday bar tutorial) must: teach movement in 30 s, first battle by minute 3 (scripted, unloseable, teaches Bash/rolling HP), first laugh before the first battle, first save hotspot by minute 8, and land in Publandia proper by minute 10 with Bravado, Brag, and one combo taught.

---

## 13. Art Bible

*(The owner is the artist. This section defines constraints so every asset lands in one coherent game.)*

### 13.1 Core visual identity

EarthBound's language, Eurobound's palette: **flat, bright, saturated color; minimal dithering; thick dark outlines on characters, no outlines on ground tiles; oblique projection** (east–west lines horizontal; verticals recede northeast; north-south walls drawn short). Night is the default state of the world — the palette must do "neon nightlife" without going grimdark: deep blue-purple ambient bases with saturated neon accents per city (Publandia: warm pub amber/green · Debaucheryville: magenta/cyan neon · Sinfonia: gold/ivory/velvet red).

### 13.2 Technical specs

| Spec | Value |
|---|---|
| Base resolution | **320×180 design viewport**, aspect-expanded to fill 19.5:9–20:9 devices (no letterbox); integer world scale, UI may scale fractionally |
| Tile size | **16×16** (metatile at 32 where convenient) |
| Character sprites | ~16×24 to 24×32; enemies 32–96 px battle sprites |
| Walk cycles | 4 directions × 4 frames (16 frames/character); side view mirrored |
| Idle | 8 frames @ 12 fps for hero idles (per style guide); NPCs 2-frame |
| Battle enemy sprites | **1–2 frames, front-facing** (the EarthBound scope-saver) |
| Palette | Fixed master palette (~48 colors) + per-city 16-color accent locks; 1:1 pixel ratio, no mixed-resolution art |
| Filter | Nearest-neighbor everywhere; snap 2D transforms; mipmaps/filter OFF on import |

### 13.3 Asset budget (V1.0, the honest count)

- **Party:** 3 heroes × (16 walk + 8 idle + ~8 emote/cutscene) ≈ 100 frames + 3 portrait sets (≈6 expressions each).
- **NPCs:** ~20 unique bodies + palette swaps → ~60 distinct-looking NPCs; 12 major NPCs get portraits.
- **Enemies:** ~36 regular (1–2 frames each) + 7 bosses (larger, 2–4 frames) + rival trio set.
- **Tilesets:** 3 city exteriors (~250 tiles each incl. oblique diagonals — budget extra: oblique transitions can't pure-autotile), ~12 interior themes (~120 tiles each), 12 brewery-dungeon variants (heavy reuse of 3 base dungeon sets + palette/prop swaps).
- **Battle backgrounds:** 8–10 grayscale index textures + palettes (shader does the rest — §13.6).
- **UI:** nine-slice set, icon font (~120 icons: items, statuses, phone UI), ICQ skin, bitmap fonts ×2 (dialogue + numerals).
- **Marketing:** icon, store screenshots (per-device sets), 30 s preview storyboard.

Rough total: **~2,500–3,500 hand-authored sprites/tiles.** At artist pace of 15–25 finished assets/week alongside everything else, art alone is ~6–9 months of the schedule — this is the long pole; guard it with the reuse rules (palette swaps, modular tiles, prop sheet for satire gags).

### 13.4 Pipeline

**Aseprite** (characters/enemies/tiles/FX; tilemap mode; CLI export in build script) → PNG (power-of-two sheets, pixel snap, no filter/mipmaps) → Godot. **Photoshop** for UI composition/promo per the "Figma-Free Zone" policy (Zeplin for specs if any collaborator joins). Naming: `chr_pilsner_walk_n_01.png`, `ui_btn_bash@2x.png` per existing convention. Godot TileMapLayer + Terrains for autotiling (+ **Better Terrain** addon), bespoke placement for oblique diagonals. AI tools (Retro Diffusion, PixelLab) permitted for *ideation and variant drafts only* — every shipped frame is hand-finished; keep provenance notes for store/Steam disclosure hygiene (§17.4).

### 13.5 Animation & FX

Frame animation for characters; AnimationPlayer/Tween for UI and battle FX; particles from a reusable library (hit sparks, star bursts, beer foam, confetti, vape clouds, € loss motes). Enemy "animations" in battle = tween wiggle/flash/scale on the static sprite (EarthBound-authentic).

### 13.6 The battle background shader

Two stacked layers, each = grayscale index texture + palette LUT, animated by **palette cycling + horizontal/vertical/interleaved sine oscillation** — the documented EarthBound technique; a ready reference implementation exists on godotshaders.com ("Earthbound-like battle background shader w/ scroll effect and palette cycling"). Trivial GPU cost on phones. Each enemy family maps to a background pair + palette (data-driven).

---

## 14. Audio Bible

### 14.1 The sound

EarthBound's soundtrack is **sample-based lo-fi (SNES SPC700), not chiptune** — 8 voices of crunchy compressed samples. That collage-y, warped-Muzak sound is the target, bent toward Eurobound's satire: pub reels that lose the run of themselves, sleazy synthwave for Debaucheryville, pompous waltzes that keep getting bass-dropped for Sinfonia ("pompous brass → drunken tuba" per the leitmotif doc).

### 14.2 Toolchain

**C700 VST** (free SPC700 emulation — the authentic 64KB grunge) inside **REAPER** (already the chosen DAW; loop points, mastering) · **Furnace** or **OpenMPT** for tracker-style writing · **MuseScore** for the Sinfonia orchestral arrangements before lo-fi-ization · **jsfxr / ChipTone** for SFX · Audacity for edits. Format: AAC (iOS)/OGG (Android), ~10 MB in-memory music cap, one streamed music track + two SFX banks, loop-point trimming in REAPER. If composing becomes the bottleneck: commission a composer for 6–8 anchor tracks and self-produce ambient/jingles (the Undertale/Chained Echoes pattern). **Avoid Suno/Udio output for shipped music until the 2026 licensed-model commercial terms settle** (Sony litigation pending as of this writing).

### 14.3 Music map (V1.0 ≈ 22–28 cues)

Per city: overworld day + night variants (layered stems, crossfade), battle, boss, seedy-underbelly interior, base-pub theme (= the leitmotif home). Global: title, tutorial bar, rival trio theme (recurs, degrading each city), final boss 2-parter (The Legend's theme = the three leitmotifs played *perfectly*, then falling apart), endings, jingles (victory, level-up, discovery, Legendary Hangover). **Leitmotifs:** one melodic phrase per bro, instrument-swapped by city and state, inverted/warped under debuffs; hidden as proximity cues in environmental SFX. **Adaptive layers:** combat crossfades by state (normal / low-HP / Inspired); VIP areas muffle the club track through a wall (event-cue ducking); comedic stingers for crits, cures, and plot twists.

**Victory Stingers & Ultimate Choruses** (`musicalbeats.md` — the "Galavant softener" system): short sung couplets on victory (Publandia: "*Raise your glass, you sorry ass — the pub crawl kings are here!*" · Debaucheryville: "*What happens here, stays regretted forever!*" · Sinfonia: "*Another night, another wrong note hit!*") and per-Ultimate chorus tags. One vocalist session (or the owner + pitch correction as a bit) covers all ~12 lines. Global toggle per accessibility spec.

### 14.4 "Voices"

Per C17: **text-blip voices** — each speaker gets a pitched/filtered blip set (Pilsner low brass, Chadwick autotuned chirp, Bradley sub-thud, Tony420 modem noises, Miss Morphine wind-chime static). ICQ messages use the classic "Uh-oh!" soundbite. Recorded human audio is limited to the sung stingers + ≤ 10 gag barks. This is genre-correct, dodges VO cost/licensing entirely, and makes every character instantly audible.

### 14.5 Mobile audio compliance

Pre-title **"Tap to Start"** (iOS audio unlock) — the tap plays a gag SFX (bottle-cap pop) that segues into the title theme. Lifecycle: pause/duck on calls & notifications, resume cleanly; background = hard mute + save.

---

## 15. Technical Architecture

### 15.1 Engine decision — Godot 4.6+ (C2)

Godot over Unity for this project, decided on 2026 facts:

- **2D-first engine:** true 2D coordinate system and physics, TileMapLayer with terrains, near-instant GDScript iteration; a solo dev ships faster in it for exactly this genre.
- **Mobile is no longer Godot's weak spot:** the Godot Foundation now maintains the core store plugins (StoreKit 2, Google Play Billing, Play Games Services) and 4.5/4.6 shipped the mobile-focused work (shader baker = no load stutter, accessibility/screen-reader support, repeatable builds).
- **MIT license, zero fees, terms can't change under you.** Unity's Runtime Fee was cancelled (2024) and Personal is free to $200K revenue — Unity is *fine* — but its remaining advantages (3D, console porting, Unity AI assistants) don't serve a 2D pixel JRPG, and its editor iteration loop is slower. Unity's AI workflows generate generic assets fastest; this game's value is hand-authored specificity by an artist-owner.
- **Existing momentum:** all prototype code is Godot 4 GDScript; the salvageable scripts (below) carry forward.
- Renderer: **Compatibility (GL)** — best battery/perf for 2D mobile. Display: `canvas_items` stretch, `expand` aspect, nearest filtering, snapped 2D transforms.
- If a Switch/console port ever matters: W4 Games / porting partners (~$10–50K) — a later decision, not a reason to switch engines now.

Addon baseline: **Dialogic 2** (dialogue/cutscenes — pin the version; pre-1.0 saves can break), **Phantom Camera** (2D camera follow/tween/shake), **LimboAI** or Beehave (enemy behavior trees), **Better Terrain** (autotiling), **GUT or GdUnit4** (tests for combat math and save migration).

### 15.2 Repo restructure

The current `Assets/Godot/` tree was never a real project (no `project.godot`; hand-typed scenes, most invalid; four competing script roots). Create the actual game at `game/` in this repo:

```
game/
  project.godot            # input map: interact, cancel, menu; autoloads; display settings
  autoload/                # singletons (§15.3)
  scenes/
    overworld/{publandia,debaucheryville,sinfonia}/
    battle/  ui/  vendors/  templates/
  scripts/                 # or co-located with scenes; ONE convention, lowercase
  data/                    # JSON (§15.5): items, enemies, skills, dialogue, quests,
                           # locations, balance, easter_eggs
  assets/{sprites,tiles,audio,fonts,shaders}/
docs/                      # the Design/ folders remain the writers' room
```

**Salvage list** (port with path fixes; everything else regenerate in-editor): `economy_controller.gd` (rename gold→euros), the five **shadow_exchange** scripts (the reference implementation of the intended architecture: signal-driven Area2D interactables + duck-typed controller forwarding), `brewery_tracker.gd`, `dialogue_controller.gd` (superseded by Dialogic 2 eventually, useful for the slice). **All `.tscn` files are regenerate-from-scratch** — they're Godot 3/4 chimeras with undeclared resources. Delete: duplicate ICQ dialogue script, `brewery_tracker.tres`, root `package-lock.json` (empty npm accident). Fix the `deboucheryville` typo at the data layer with a migration map.

### 15.3 Autoload singletons (the backbone)

`GameState` (quest flags, graffiti_found, reputation, street_rep, world clock, ego meter) · `EconomyController` (euros, rates, premium stock — exists) · `PartyState` (stats, statuses, BP, equipment, inventory) · `QuestLog` · `DialogueRunner` (Dialogic wrapper + `push_system_line`, `set_flag_true` — the interface ShadowExchangeRoot already calls) · `ICQController` (message queue, popup scene, hotspot events) · `TimeManager` (§11.3 — grease-trap gate already calls it) · `SaveManager` (§11.2) · `AudioDirector` (layers, ducking, stingers) · `BattleDirector` (encounter setup/teardown) · `MemeMastery` + achievement/title registry · `Haptics` (GDExtension wrapper). Player scene exposes the interaction raycast that calls `interact()` on Area2D interactables — the contract every prototype script already assumes.

### 15.4 Event flags (fills `event_flags.md`)

Single namespaced string-flag registry in GameState: `city.venue.event` (e.g. `dv.velvet.vip_stall_qr`, `global.fisto_thread_complete`, `pub.keychain_purchased`). Rules: flags are write-once booleans unless prefixed `counter.`; every quest doc's implied flags get registered in `data/quests/flags.json`; save schema stores the flat dictionary. Scene-local caches subscribe via signal `flag_changed(flag)`.

### 15.5 Data-driven design & the effect grammar

Everything balanceable is JSON in `data/`, edited via Google Sheets → CSV → JSON where useful (the documented workflow). **One structured effect grammar** replaces every freeform "effect" string, extending the shape that already exists in `worlds_pickiest_drunk_passive.json`:

```json
{ "effects": [
  { "op": "stat_mod", "stat": "atk", "amount_pct": 20, "duration_turns": 2 },
  { "op": "apply_status", "status": "hungover", "chance": 0.25 },
  { "op": "grant_item", "id": "nft_pixelated_kebab_monkey" },
  { "op": "euros", "amount": -25 },
  { "op": "set_flag", "flag": "dv.couchsurf.vanessa_done" }
] }
```

snake_case keys everywhere; canonical ID registry (fixes `deboucheryville`, `absynthium` drift); one dialogue format (Dialogic timelines; the couchsurfing JSON and the GDScript `dialogue_tree` both migrate); one vendor schema (numeric `price_eur`). Strings externalized from day one with the `line_en` / `line_safe` **Satire Swap** columns (§17.3) and localization metadata (Has Pun / Needs Fallback / Cultural Risk).

### 15.6 Save schema

Versioned JSON (`schema_version` int + migration functions), one file per slot in `user://saves/`: party (stats/level/clout/equipment/inventory/statuses), euros, flags dict, reputation states, clock, brewery/graffiti/NFT/meme progress, settings. Checksum + backup snapshot per §11.2. GUT tests: every released schema version must load-migrate forward.

### 15.7 Performance budget

Baseline device: **iPhone 11 / Galaxy S10-class** (2026 revision of the docs' iPhone 8 target). 60 fps target, no dips below 30 · ≤ 350 MB peak memory · battery ≤ 8%/15 min overworld, ≤ 10%/15 min battle · cold load ≤ 5 s, scene change ≤ 2 s · sprite atlases ≤ 2048², unload per city · profile on physical devices monthly, not simulator. Crash reporting: Sentry or Firebase Crashlytics. CI: GitHub Actions running GUT tests + export smoke builds; Fastlane for iOS lane (build, screenshots, TestFlight upload).

---

## 16. Production Plan & Skills Package

### 16.1 Honest scope math

The August-2025 "14–19 days to demo" schedule is void. Calibration from shipped comparables: Undertale (≈32 months, solo + contract artist, 6–8 h game) · Chained Echoes (7 years solo, 30 h) · Omori (6.5 years, small team). Eurobound at 8–12 h, solo artist-developer with strong existing design docs and heavy asset-reuse discipline:

| Phase | Duration | Exit criteria |
|---|---|---|
| **0 · Foundation** | 6–8 weeks | Real Godot project; walkable oblique test map with autotiles; battle state machine with rolling HP vs 2 enemy types; save/load; touch controls feel good ON DEVICE; art style locked via one polished screen ("visual style bible screenshot") |
| **1 · Vertical slice** | 3–4 months | 30–60 min of Publandia: tutorial bar → 2 districts → 3 venues → 1 brewery dungeon → Rival Trio fight. All systems present in v1 form (Bravado, one combo, statuses, shop, ICQ save, reputation state 1→2, one stinger). **This is the go/no-go artifact** — playtest with 10+ strangers; "funny to people who don't know the backstory" is a formal exit criterion |
| **2 · Publandia complete** | 3 months | City 1 content-complete incl. Craic Baron; content pipeline measured (venues/week, dialogue/week) — re-forecast the rest of the schedule from THIS number |
| **3 · Debaucheryville** | 3–4 months | Fastest city per docs-completeness; all 15 venues, 4 breweries, boss, Meme Black Market |
| **4 · Sinfonia + finale** | 3–4 months | Rhythm systems, Masquerade, Maestro, The Legend, both endings |
| **5 · Beta, polish, ports** | 2–3 months | Full-game balance pass (5% increments, 3-tier playtester satisfaction ≥80%), accessibility audit, IARC/Apple questionnaires, TestFlight/Play beta, localization pass (if any), store assets |
| **Total** | **~18–24 months** part-time-plus; ~12–14 months if full-time | |

Scope-cut order if behind (pre-agreed, per the docs' Red-status rule): Sinfonia venue count → STRETCH quests → couchsurf/karaoke lines → musical stingers → **never cut:** rolling HP, Bravado, the city structure (four cities — Shamsterdam included, author ruling 2026-08-03), the graffiti quest.

### 16.2 The total skills package (what this project actually requires of one person)

**Already strong (owner):** pixel/2D art, graphic design, UI composition, satire writing.
**Learn to intermediate level:** GDScript + Godot scene/signal architecture (the make-or-break skill — 4–6 weeks of focused learning; the battle system and save system are the two hard programs) · TileMapLayer/autotiling · JSON data modeling · Aseprite animation workflow · basic REAPER/C700 music production OR the budget to commission ~8 tracks ($150–400/track indie rate) · jsfxr SFX · Git (already in use) · Xcode/TestFlight + Play Console publishing · store-listing ASO basics.
**Outsource candidates (highest leverage first):** composer for anchor tracks · a code review/pairing pass on BattleDirector + SaveManager from an experienced Godot dev (fixed-scope contract) · cultural sensitivity readers per city (the review template already exists) · QA playtesters.
**AI-assist posture:** AI coding assistants for GDScript (high leverage, no disclosure burden), AI as art ideation only (§13.4), no AI music until licensing settles, no AI VO needed (text blips).

### 16.3 Process rules (carried from Production docs)

Vertical slices before content breadth · test touch-feel on device before adding content · dialogue in Sheets → JSON, locked per-city before final art pass · weekly triage vs last 7 days of commits · severity × player-impact bug matrix; "critical first 10 minutes" is priority zero · Green/Yellow/Red daily milestone tracking, Red = cut scope immediately · pre-merge checklist incl. context-echo check and the colorblind screenshot check · in-universe "Hotfix Notes" for players.

---

## 17. Compliance, Legal & Store Strategy

### 17.1 Ratings reality (2026)

Apple's rating tiers changed in late 2025 (now 4+/9+/13+/16+/18+). Eurobound's content — frequent comedic alcohol themes, mild sexual innuendo, infrequent *simulated* gambling parody — targets **16+** (13+ is achievable only by muting the premise; don't). Google Play/IARC: answer for **ESRB Teen–M17+/PEGI 16**. Design rules that keep us there: casino/claw minigames pay out only absurd items and never touch real money or odds-based purchases (no loot boxes, no IAP at all at launch = the whole gacha-disclosure regime is moot) · vice depicted with comedic consequences, never instructional or glorified · innuendo, never explicit · C19 raunch ceiling enforced in string review.

### 17.2 The NFT/crypto joke, done legally

Apple: crypto/NFTs may never function as unlock mechanisms or purchases; **parody is fine**. Our NFTs are collectible JPEG-flavored quest items with zero blockchain anything — the entire joke is that they're worthless. Keep the word "NFT" out of the App Store metadata anyway (reviewer keyword hygiene).

### 17.3 Satire compliance system (already designed — keep it)

`line_en` / `line_safe` dual-string table with `SATIRE_MODE=SAFE` build flag; pre-tested safe build in TestFlight; Satire Safety Changelog; cultural sensitivity review per city using the existing template + in-region readers; metadata rules (no alcohol/drug terms in title, subtitle, first two description lines; colorful "story-safe" screenshots). Rejection Recovery Protocol as documented — with the itch.io/HTML5 "uncensored edition" as the pre-built PR-spin contingency.

### 17.4 Legal hygiene

- **`Marketing/Legacy_Pitch_Document.md` must not ship or be public** (C20). Characters are archetypes; "recognizable but legally safe" is the standing success metric. No real person's photo, name, itinerary, or identifying details anywhere in game or marketing.
- **Brands:** invented sound-alikes only (the EarthBound "Mach Pizza" strategy): Napstur, iPawd, ICQ-style chat (rename to "IBC — I Seek Bros" if counsel prefers), Funcoland/eBaum's/LimeWire-style *references* reviewed case-by-case — nostalgia-brand namechecks in dialogue are higher-risk in the EU than the US; prefer parody names with the same silhouette. No real logos, no brands in icon/title/keywords.
- **Music:** no samples of copyrighted recordings (emulate EarthBound's collage *spirit*, not its sampling strategy). Fonts: OFL/verified licenses only (Press Start 2P, m5x7-class).
- Analytics: privacy-first (drop-off, difficulty spikes, UI abandonment), App Tracking Transparency compliant, no behavioral ad tracking; the "player behavioral profiling for easter eggs" feature stays **on-device only**.

### 17.5 Store & launch strategy

$4.99 premium (C16), Small Business Program 15% commission tier. Playbook (as documented): localized metadata for key EU languages · press kit 2–3 months pre-launch with embargoed codes (retro/RPG and comedy-game press; the origin story is a *great* pitch angle, told on your terms) · Coming Soon page + notify · launch-week push in 72 h · promo codes · post-launch A/B screenshots · seasonal event updates tied to European festivals (Oktoberfest event = the Publandia pretzel joke's revenge) · QoL update within 2–4 weeks. itch.io demo build = wishlist/press funnel and platform-rejection insurance.

---

## 18. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Art volume** (the long pole) | High | Schedule | §13.3 budget + reuse rules; slice measures true asset velocity; scope-cut order pre-agreed |
| **Solo GDScript learning curve** | Medium | Schedule/quality | Phase 0 is exactly this; contract review of the two hard systems; AI pair-coding |
| **Comedy doesn't land with strangers** | Medium | Product | Slice exit criterion; jokes tested in playtests, not assumed; the docs' satire QA checklist |
| **Apple content rejection** | Low–Med | Launch | 16+ targeting, Satire Swap safe build ready, metadata hygiene, itch contingency |
| **Trademark complaint (nostalgia brands)** | Medium | Legal | Sound-alike rename pass before launch (one afternoon of find-replace, do it early) |
| **Scope creep from rich design docs** | High | Schedule | This PRD's [CORE]/[FULL]/[STRETCH] tiers are law; new ideas enter as STRETCH by default |
| **Burnout (revenge-fuel is a sprint fuel, not a marathon fuel)** | Medium | Everything | 18–24 mo pacing, phase gates that produce shippable artifacts (slice → demo → city releases on itch), community/devlog for sustained feedback energy |
| **Dialogic 2 pre-1.0 save breaks** | Medium | Tech | Pin addon versions; save-schema migration tests |
| **Music production stalls** | Medium | Polish | Commission fallback budgeted from the start |

---

## 19. Appendices

### 19.1 Glossary (canonical vocabulary)

**Bravado (BP)** MP-analog, confidence-as-mana · **Clout** XP · **SOVS** currency · **Cover Charge** door-tax money sink · **Bro Ladder** Clout tiers (Pledge/Active/Alumni/Legacy/Living Legend) · **Brag** the skill menu · **Chicken Out** flee · **SMAAAASH!!** crit · **Dad on a Bender** zero-Bravado collapse · **Snap Out of It** ally recovery action · **Seedy Underbelly** each city's night layer, shown in full · **Playable Idiot Logic** flaws-as-mechanics pillar. *(Struck by author ruling 2026-08-03: "Reality Check / Perspective," "The Legend," "Satire Swap.")*

### 19.2 The nine restroom graffiti shrines
Publandia: Stoutworks Brewery (yeast golem miniboss) · The Back Room · Kebab Alley ("Stomach of Steel"). Debaucheryville: Grease Trap Shrine (3 A.M., Fistø's Mecca) · Claw Machine Maintenance Closet ("He moaned 'SMAAAASH' in bed. I ghosted mid-combo.") · Velvet Curtain VIP Stall (NFT QR + "DO NOT LOOK AT THE BABY"). Sinfonia: Mozart's Last Rave (Resurrected DJ ghost ally) · Café Existenz ("Even Nietzsche sat down to pee sometimes.") · Bassline Opera House backstage.

### 19.3 The nine NFTs
Publandia: Temple Bar Receipt JPG (rival showdown) + QR mural + poker-pot find. Debaucheryville: Pixelated Kebab Monkey, VIP Wristband PNG, Beer Pong Saint Relic (multi-route per C9). Sinfonia: Mask Selfie GIF (rival showdown) + auction QR catalog + backstage terminal. Special unlock-only: Funcoland Futures NFT #1999 (MemeMastery) and Meatspin NFT (free, cursed) sit OUTSIDE the 9-count as gag items.

### 19.4 Repo cleanup checklist (docs debt)
1. Strip scaffolding artifacts ("[CONTENT FROM PLAN ABOVE]", "[UPDATED with…]") from all files. 2. De-contaminate `sinfonia.md` (remove the duplicated Debaucheryville block). 3. Merge the three combat drafts in `combatsystem.md` to §6's canon. 4. Update `party.md`/`bravado.md` to C3–C5. 5. Single names: The Absinthium Taproom, Hungover, Beeramid Blast, Like & Subscribe, Alpha Sigma Slam/Thunder. 6. Rewrite Bottle Opener Keychain geography (C18). 7. Complete `debaucheryville_locations_index.md` (add the 10 missing venues). 8. Fill placeholder files by pointing them at this PRD's sections (don't duplicate content). 9. Quarantine `Legacy_Pitch_Document.md` (C20). 10. Delete `package-lock.json`, duplicate ICQ script, `brewery_tracker.tres`. 11. Register all quest flags in `data/quests/flags.json`. 12. Fix `deboucheryville` typo via ID migration map.

### 19.5 Source documents
This Bible synthesizes: `Design/` (Synopsis, Game Design Spec Sheet, all Gameplay/Battle/Progression/Social docs, Systems, Inventory, Economy, Characters, Narratives, Quests, Locations incl. all 15 Debaucheryville venue docs, Interactables), `Production/` (Schedule, Tools & Asset Pipeline, Dev Skills & Workflows), `UX-UI/` (UX & Accessibility Guide, battle mockup), `Marketing/` (Compliance, Playbook, Cultural Sensitivity Template), `Audio-Visual/musicalbeats.md`, `Items/`, `GAMEPLAN.md`, `README.md`, the Godot prototype (`Assets/Godot/`), and July-2026 external research on engine status, EarthBound technique, comparable-title scope, mobile UX norms, store policy, and AI-asset licensing.

---

*The bros think this document is about them becoming legends. It's actually the instruction manual for the joke. Don't tell them.*
