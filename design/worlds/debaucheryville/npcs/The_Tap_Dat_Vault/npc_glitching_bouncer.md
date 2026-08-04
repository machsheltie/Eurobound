# NPC Profile: The Glitching Bouncer

*"Vault... *glitch* ...key detected. You kept... the beat."*

## 📋 NPC Identity
- **NPC ID**: `debaucheryville_npc_glitching_bouncer_01`
- **Display Name**: The Glitching Bouncer
- **Internal Name**: The Glitching Bouncer — the Vault's door. No name is on record and he has never been asked for one in a way that produced an answer
- **Role**: Gatekeeper / Bottle-Opener Vendor / Brewery Tour Credential Check
- **Associated Quest**: Brewery Tour — Debaucheryville Slot 2 of 4 (`the_tap_dat_vault` stamp track)
- **Primary Location**: The Tap Dat Vault, Debaucheryville — the vault door, hidden cellar beneath Clocktower Plaza
- **Secondary Appearances**: None. The door is at Clocktower Plaza and it opens at 00:00 and he is behind it

---

## 🎭 Core Concept

### What He's Actually Doing
Standing at a large metal vault door that opens only at exactly 00:00, scanning arrivals for two separate bottle openers, and admitting or refusing them on the result. He speaks in fragments broken by static and glitch artifacts — which, in a venue where the lighting, the NPCs, and the brewing vats are all rhythm-reactive and the DJ zombies sync to 128 BPM, is not treated by anyone present as remarkable. He also sells the Vault's own bottle opener for 20 Sovs to anyone who would rather buy the door than beat it.

### What Bros Believe
That the glitching is an effect — a costume, a voice modulator, part of the venue's cyberpunk theming. That he is a bouncer doing a bit. That getting past him is about attitude, because getting past bouncers is always about attitude.

### The Comedy Gap
Getting past him is about **two specific keychains**, which he tells you, clearly, through the static, in three canonical variants depending on which ones you have. He is the most explicitly-specified door in Debaucheryville — he states the requirement, states the alternative (20 Sovs), and states the price — and the bros keep trying to talk to him, because they have never once encountered a door that meant what it said.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Indeterminate. The glitch obscures the face at irregular intervals |
| Build | Doorman-scale. Wide enough that the vault door behind him reads as the second-widest thing in frame |
| Height | Tall |
| Energy | Static, corrupted, immovable |

### Clothing
- **Dark technical coat**: Matte, absorbs the neon rather than reflecting it, which makes the glitch artifacts on his silhouette read cleanly against it
- **Scanner rig**: A handheld unit on a retractable cable, used for opener checks. Cyan indicator when clear, pink when not
- **Accessories**: Countdown glyphs on the door beside him pulse at 00:00; a stock of Vault bottle openers in a case at his hip, each with a live LED in it
- **Footwear**: Heavy, planted, has not moved

### Distinguishing Features
- Speech breaks into static and glitch artifacts at irregular intervals mid-sentence — never at word boundaries, which is what makes it unsettling
- His sprite corrupts visually at the same instants his speech does; the two are synced
- The scan gesture is identical every time — same arc, same pause, same read
- When the beat drops, the glitching briefly *stops*. Nobody has ever commented on this and it happens every single time

### Sprite Notes
The glitch must be **synced to the venue's 128 BPM**, not random — corruption on the off-beat, clarity on the drop. That sync is the character. Palette per `tap_dat_vault_png_asset_requirements.md`: neon cyan (#00FFFF) and hot pink (#FF1493) glitch artifacts over a deep purple (#4B0082) and cyberpunk black base. The scanner rig's cyan/pink indicator is the readable pass/fail tell at a glance. **Asset gap flagged**: `tap_dat_vault_png_asset_requirements.md` Sprite Sheet 3 (`tapdatvault_npcs.png`) specs the bartender, two DJ zombies, two techno monks, the fridge livestreamer, the Ad Bot, and the Strobe Brewmistress — **but not the Glitching Bouncer**. The location file's own PNG summary lists `bouncer_glitched.png` at 128x192 ("Opener checker"). Use that filename; the pose list needs authoring.

---

## 🧠 Personality

### Archetype
**The Corrupted Doorman** — He is a door policy that has been partially overwritten. What survives is a clear, correct, three-branch credential check and a 20 Sovs sales offer, delivered through interference that never obscures the operative words. He is not menacing and he is not friendly. He is a specification with static in it, and the specification always resolves.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Specification-clear | The requirement, the alternative, and the price all survive the glitch intact. Every time |
| Rhythm-locked | The corruption follows the venue's beat, and clears on the drop |
| Unbribable | There is no attitude, story, or amount other than 20 Sovs that changes the outcome |
| Fragmentary | Speaks in broken clauses. This is not reticence — the words are all there, in pieces |
| Impartial | The check is identical for everyone. He has never scanned two people differently |

### Internal Monologue
> "Publandia... *(static)* ...key. Present. Vault key... absent. Two paths. Rhythm... or twenty. Say... *(glitch)* ...both. Say both, every time, they only hear one. He is going to try... talking. They always... *(static)* ...try talking."

### Motivation
Unrecoverable, in any sense the fiction ever explains. What is observable is that he checks credentials correctly, sells the opener honestly at a fixed price, and has never once been wrong about who is carrying what. Whatever he was before the Vault, the door is what remains, and the door works.

---

## 💬 Dialogue

### Approach/Greeting

**First approach, vault door opening at 00:00**:
> "Door... *(static)* ...is open. Midnight. Only... midnight. You have... *(glitch)* ...until it closes, and it closes... when it closes."

**Approach before midnight (door sealed)**:
> "Not... *(static)* ...yet. Glyphs are counting. Counting... is the only... *(glitch)* ...thing here that does not... need rhythm."

### Bottle Opener Check (canonical, three branches)

**With Blarney Trap Opener, no Vault Opener**:
> *scans* "Publandia... *glitch* ...authorization detected. Vault key... required. Complete rhythm... sequence. Or... *static* ...20 Sovs."

**With both openers**:
> *scans, nods* "Vault... *glitch* ...key detected. You kept... the beat. The brew section... awaits. Don't... *static* ...disappoint."

**Without Blarney Trap Opener**:
> "Authorization... *glitch* ...not found. Publandia... opener... required. Return... *static* ...when equipped."

### Key Interaction Dialogue

*Three Americans have found a vault door in a plaza at midnight. Two of them are trying to talk their way in. One of them has read the requirements.*

**Lord Pilsner**: "Come on, man, we're on the LIST. We're basically on the list."

**The Glitching Bouncer** *(scanner arc, same as always)*:
> "There is no... *(static)* ...list. There are two... keys. You have... *(glitch)* ...one."

**Lord Pilsner**: "But like — energy-wise, vibe-wise, are we in?"

**The Glitching Bouncer**:
> "Vibe is not... *(static)* ...a key."

**Bradley**: "It's twenty Sovs, isn't it. He said twenty Sovs."

**The Glitching Bouncer**:
> "...*(clear, on the drop)* Twenty."

*If the player asks what the glitching is:*
> "What... *(static)* ...glitching."

*If the player asks how to complete the rhythm sequence:*
> "Match... the markers. They scroll. Three... *(glitch)* ...failures and you are outside, and outside... is until tomorrow. Midnight... does not... *(static)* ...negotiate."

*If the player asks why the door only opens at midnight:*
> "It opens... when the glyphs... *(glitch)* ...reach zero. Ask the glyphs. I have... *(static)* ...asked the glyphs."

*If the player asks about the openers:*
> "Chrome. Vault door... shape. Soundwave... cutout. There is a light... *(glitch)* ...inside it. Squeeze it. It keeps... the beat, when you... *(static)* ...cannot."

*If the player mentions Dr. Vaněk or the Absinthium Taproom:*
> "The mirror... place. Slot one. He checks... *(glitch)* ...the same Publandia key. Different... door. Same... *(static)* ...protocol."

### Sales Close — The Tap Dat Vault Bottle Opener (20 Sovs)
*He takes the note, and the opener he hands over has a live LED pulsing in it:*
> "Twenty. Yours. Inhaled... *(glitch)* ...and Survived. It says that... before you have. That is... *(static)* ...the joke, and nobody... has laughed."

### Post-Interaction
> "Brew section... *(glitch)* ...that way. Keep... the beat."

### If Player Declines / Alternative Path

*Declining the 20 Sovs opener and attempting the rhythm puzzle:*
> "Good. Cheaper... *(static)* ...and harder. Most choose... twenty. You did... *(glitch)* ...not."

*Third rhythm-puzzle failure (ejection):*
> "Three. Outside... *(static)* ...now. Not punishment. Just... *(glitch)* ...the count. Come back at... midnight."

*Attempting to bribe him:*
> "Twenty is... *(static)* ...the number. More than twenty is... still twenty. There is no... *(glitch)* ...number above twenty."

*Trying to enter without the Publandia opener repeatedly:*
> "Same... *(static)* ...answer. It will be the same... answer at three... *(glitch)* ...in the morning."

### Callback Dialogue (Return Visits)

*Second visit, credentials in order:*
> "Both keys. Again. Go... *(static)* ...in."

*After the player defeats the Strobe Brewmistress:*
> "You... *(glitch)* ...beat her. She is... *(static)* ...pleased. That is not... a thing she does. Note that... it happened."

*After completing the rhythm puzzle rather than paying:*
> "You did not... *(static)* ...pay. Four percent do not... *(glitch)* ...pay. I keep the... number. Nobody asked me... *(static)* ...to keep the number."

*Late game, all four Debaucheryville stamps:*
> "Four seals. Mirror place, here, the... *(glitch)* ...traditionalists, the algorithm... cellar. You went... *(static)* ...everywhere. Even the ones that were... unpleasant. Especially... *(glitch)* ...those."

*On the beat drop, mid-conversation, at any point:*
> *(entirely clear, no static, one line only)* "There. That's the only part of me that still works right."
> *(the glitching resumes immediately and he does not acknowledge having said it)*

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 00:00 exactly | The vault door | Countdown glyphs reach zero; door opens; credential checks begin |
| 00:00-close | The vault door | Continuous door operation; opener scans; 20 Sovs sales; ejection processing |
| All other hours | The vault door (sealed) | Present but unreachable. The door is only visible when the countdown reaches 00:00 |

**Note:** Access requires first discovering the hidden switch at Clocktower Plaza. The Vault is midnight-only and so, functionally, is he.

### Positioning Notes
- Directly at the large metal vault door — neon graffiti tags, countdown glyphs, bass audible through the metal
- Positioned so the countdown glyphs are always in frame beside him, making the time constraint a permanent visual
- He is the first thing inside and the last thing outside; there is no lobby, no queue rail, no alternative approach
- The bass from the subwoofer vats reaches him through the door, which is why his glitch stays locked to a beat he is technically outside of

---

## 🎒 Inventory / Services

### Services Offered
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| **The Tap Dat Vault Bottle Opener** | 20 Sovs, or free by completing the rhythm puzzle sequence | Vault-door shape with a soundwave pattern cutout, opener integrated into the door handle; brushed chrome with cyan and hot pink neon accents that **actually glow**; inscribed "Inhaled & Survived"; contains a tiny LED that pulses in rhythm when squeezed (battery included) | Required for the Vault's brewing-section access, the Vape Stout purchase, and the Brewery Passport stamp |
| **Credential check** | Free | The reason the Continental Trail has any structure | Scans for the Blarney Trap Bottle Opener (Publandia — quest access) **and** the Tap Dat Vault Bottle Opener (brew section access). Three canonical outcome branches |
| **Ejection processing** | Free, involuntary | Three strikes on the rhythm puzzle | Player is put outside; re-entry available at the next midnight |

**Without the Blarney Trap Opener**: cannot participate in the brewery tour at all.
**Without the Tap Dat Vault Opener**: can enter the vault and explore, but the brewing section remains locked.

### Hidden Details / Easter Eggs
- **The beat-drop clarity**: Every bass drop, his glitching stops for the duration. Standing near him through several drops and doing nothing else eventually produces his one clear line, delivered once per playthrough.
- **Examining the scanner rig**: The cable is retractable and the housing is scuffed on one side only, in an arc, consistent with the identical scan gesture repeated an enormous number of times.
- **Examining the opener case at his hip**: Every opener in it has a live LED. They are all pulsing. They are all pulsing *in sync*, with each other and with the room.
- **Asking his name**: "What... *(static)* ...name." Repeated asking produces the same two words with the static in a different position.
- **The countdown glyphs**: He has, per his own line, asked them. They did not answer. This is the only thing he has ever admitted trying and failing to do.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Strobe Brewmistress | The Vault's boss and its authority. She is "pleased" when the player beats her, which per the bouncer is not a thing she does |
| The Bartender (vape rig) | Downstream of every credential check he passes. The bouncer sends them; the bartender serves them the Vape Stout |
| Dr. Miloš Vaněk (The Absinthium Taproom) | Slot 1 of the same brewery tour, checking the same Publandia key at a different door. "Same protocol." They have never met |
| Keg Haus Bartender (Three-Crown Keg Haus) | Slot 3. Referenced through the Vault's cross-brewery dialogue system rather than directly |
| CryptoBro69 (Ye Olde B.R.E.W. Lab) | Slot 4. Calls the Vault "SICK" and wants to collab. The bouncer has not responded to this |
| Token Goblin (Shadow Exchange) | Sells queue-skip chips described in `shadowexchange.md` as providing "Tap Dat Vault midnight-only venue access." **Reconciliation needed** — see Development Notes |
| Mrs. Rata (Shadow Exchange) | The Exchange sells the Vault's bottle opener on the grey market as an alternative acquisition route |
| The UV Man (Shadow Exchange) | The city's other authentication point. Neither has met the other; both would recognize the other's work instantly |
| DJ Zombies / Techno Monks | Interior fixtures, synced to the same 128 BPM his corruption follows. Nobody inside finds his speech unusual |

### Territory / Social Dynamics
- The vault door is the hardest gate in Debaucheryville: time-locked to a single instant, credential-locked to two separate items, and skill-locked behind a three-strike rhythm puzzle with an alternative purchase price
- Nobody inside the Vault treats his glitching as noteworthy, because everything inside the Vault glitches — the venue normalizes him completely
- His 20 Sovs alternative is the tour's most honest gate: it converts a skill check into a price, states the price, and does not judge the choice
- He is the second of the Debaucheryville brewery tour's four credential checks and the only one that is also a physical door

---

## 🔄 Recurring Appearances

### Within Debaucheryville
- Permanent at the Tap Dat Vault door during its midnight-only window
- Every entry and re-entry to the Vault passes him, making him a repeat-encounter NPC despite a narrow access window
- His bottle opener circulates through the Shadow Exchange's grey market as an alternative acquisition route
- Quoted through the Vault's cross-brewery dialogue system at the other three Debaucheryville brewery locations

### In Other Cities (If Applicable)
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| Publandia | — (referenced only) | He scans for The Blarney Trap Bottle Opener at every check. Publandia is the upstream credential authority for the entire Continental Trail | *(On the Publandia key)* "Every... *(glitch)* ...one of you comes from the same... door. Different city. Same... *(static)* ...keychain. It is a good... system. I did not... design it." |

### Evolution Through Game
- **Pre-switch discovery**: Not encountered. The vault door is not visible
- **First midnight**: Credential check fires; one of three canonical branches
- **After acquiring the Vault opener**: The "both keys" branch becomes his default and stays there
- **After the Strobe Brewmistress**: He reports that she is pleased, which is the only outside information he ever volunteers
- **The beat-drop line**: Once per playthrough, unprompted, requires the player to simply stand there. The single moment anything resembling a person is visible
- He does not change otherwise. The door does not change. That is the point.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| idle_glitching | Default; sprite corrupts on the off-beat, clears on the drop, locked to 128 BPM | 55% |
| glyph_glance | Looks at the countdown glyphs beside the door | 20% |
| scanner_ready | Scanner rig raised to a resting position on its retractable cable | 15% |
| drop_clarity | On every bass drop: corruption ceases entirely for the duration of the drop | 10% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| opener_scan | Any approach; identical arc, identical pause, cyan or pink indicator |
| scan_nod | Both openers detected; the single approving gesture he has |
| opener_sale | 20 Sovs transaction; opener handed over with its LED live |
| ejection | Third rhythm-puzzle failure; player put outside |

### Sprite States
| State | When Used |
|-------|-----------|
| bouncer_idle | Default door presence, glitch cycle running |
| bouncer_scanning | Active credential check |
| bouncer_clear | Bass drop only — no corruption artifacts |
| bouncer_selling | 20 Sovs opener transaction |

---

## 🎯 Quest Integration

### Primary Quest: Brewery Tour — Debaucheryville Slot 2 of 4
- **Quest**: The Tap Dat Vault stamp track (The Tap Dat Seal, "Inhaled & Survived")
- **Role**: Gatekeeper and Vendor
- **Trigger**: Approaching the vault door at 00:00 after discovering the hidden switch at Clocktower Plaza
- **Outcome**: On passing both checks, the brewing section opens — leading to the rhythm-based vapor pressure puzzle, the Glitched Brew Ad Bot mini-mob, the Strobe Brewmistress boss, the Vape Stout, and the stamp

**Stamp unlock conditions (ALL required)**: complete the rhythm-based vapor pressure puzzle; defeat the Strobe Brewmistress; obtain the Vape Stout; present the Debaucheryville Bottle Opener Keychain.

### Quest Gate Function (If Applicable)
**Yes — the hardest gate in the city, and it is triple-locked.**
1. **Time gate**: The door opens at exactly 00:00. He is unreachable at any other hour
2. **Credential gate (hard)**: Without the Blarney Trap Bottle Opener (Publandia), no brewery tour participation at all — he turns the player away entirely
3. **Credential gate (soft)**: Without the Tap Dat Vault Bottle Opener, the player may enter and explore but the brewing section stays locked
4. **Skill gate with a purchase bypass**: The Vault opener is earned via the rhythm puzzle or bought for 20 Sovs. Three rhythm-puzzle failures eject the player until the next midnight

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| The Tap Dat Vault Bottle Opener | Rhythm puzzle completion or 20 Sovs purchase | Yes | Unlocks brewing-section access, Vape Stout purchase, and stamp eligibility. Contains a live LED that pulses in rhythm when squeezed |

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. Mid-glitch at the vault door with the countdown glyphs at 00:00 beside him
2. The scan gesture with the pink fail indicator lit and a bro's face behind it
3. The beat-drop clarity frame — the one moment his sprite is intact
4. The opener case at his hip, every LED pulsing in sync
5. Ejection: the player outside, the door sealed, the glyphs counting again

### Meme Potential
- "Vibe is not... *(static)* ...a key."
- "There is no... number above twenty."
- "What... *(static)* ...glitching."
- "It says that... before you have. That is the joke, and nobody... has laughed."
- "There. That's the only part of me that still works right."
- The glitch-fragment speech pattern is inherently quotable and trivially editable into audio clips

---

## 🗣️ Voice Direction

### Accent
Beneath the corruption: Czech, flat, professional-doorman. The accent must survive the glitch processing — the character is a working bouncer with interference, not a synthesized voice.

### Tone
- **Standard checks**: Procedural and unemotional. He is reading a policy through static
- **Refusals**: Identical to approvals. He has one register and applies it to both outcomes
- **The 20 Sovs line**: Slightly clearer than the surrounding fragments. The price always survives, and that is a joke about doors
- **Beat-drop clarity**: Completely clean. No processing. It should sound like a different, much more tired person

### Key Delivery Notes
- **The glitch must break mid-word, not between words.** Breaking at word boundaries reads as a stutter; breaking mid-word reads as corruption
- **Operative words always survive**: "Publandia," "required," "20 Sovs," "rhythm," "three." The static may take anything else
- The corruption is **synced to the venue's 128 BPM** — VO should be recorded to a click track and processed on the off-beat
- His one clear line is the most important half-second in the profile. Do not process it, do not layer it, and do not repeat it
- Never menacing. He is a door, and doors are not angry

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Full appearance documented | ✅ |
| Personality & motivation clear | ✅ |
| Complete dialogue trees | ✅ |
| Schedule & location specified | ✅ |
| Connections to other NPCs | ✅ |
| Recurring appearances planned | ✅ |
| Animation states defined | ✅ |
| Quest integration documented | ✅ |
| Sprite notes for artists | ✅ |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |
| World consistency (city names) | ✅ |

---

## 📝 Development Notes

- **ASSET GAP — FLAGGED.** `PNG_Assets/tap_dat_vault_png_asset_requirements.md` Sprite Sheet 3 (`tapdatvault_npcs.png`) specs the bartender, two DJ zombies, two techno monks, the fridge livestreamer, the Ad Bot, and the Strobe Brewmistress — **but omits the Glitching Bouncer entirely**. The location file's own PNG summary lists `bouncer_glitched.png` at 128x192 ("Opener checker"). This profile uses that filename. **The bouncer's pose list needs authoring and adding to the PNG_Assets spec.**
- **"The Glitching Bouncer" is the complete identity.** No name exists in any source file and his own dialogue makes the absence deliberate. **Do not invent a name.**
- **The three opener-check dialogue variants are quoted verbatim** from `the_tap_dat_vault.md` and must not be paraphrased in implementation. The 20 Sovs price, the "Inhaled & Survived" inscription, the LED, and the chrome/cyan/pink material spec are all canon-locked.
- **Cross-location reconciliation needed**: `shadowexchange.md` states that Token Goblin's queue-skip chips provide "Tap Dat Vault midnight-only venue access," and the Shadow Exchange sprite sheet corroborates it. `the_tap_dat_vault.md` describes access exclusively via the hidden Clocktower Plaza switch and the midnight window, and **does not mention chips**. This is currently a one-way reference. Either the chip skips a queue this profile does not document, or the reference is stale. **Resolve before implementation.**
- **The beat-drop clarity behavior is a proposed addition**, extrapolated from the location's established "everything is rhythm-reactive" rule (lights pulse, steam bursts, NPC movement syncs to beat). It is cheap, it makes the character, and it costs one clear line. **Flag as proposed, recommend adoption.**
- The glitch sync at 128 BPM matches the DJ Zombies' documented movement sync in the PNG spec's technical notes. Keeping the bouncer on the same clock is what makes him read as *of* the venue rather than as a separate effect.
- Voice acting priority: **medium-high**. Low line count and heavy processing, but the beat-drop line is unprocessed and needs a real performance.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — this profile contains **zero** crypto content; the source location file establishes none
- [x] **NO automatic crypto assumptions** — the door takes 20 Sovs in cash and two physical keychains
- [x] **Coins, kiosks, and certificates come from the master pool** — none used, none invented
- [x] **The bros are never scam-aware** — they hear a fully-stated door policy through static and try to talk their way past it anyway
- [x] **Nothing winks** — his one self-aware-sounding line ("nobody has laughed") is about an inscription, not about the game
- [x] **Focus on city-specific cultural exploitation instead** — vape-culture commercialization, pretentious craft-brewing, and the midnight-only underground venue economy

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior (believing attitude beats a stated requirement, "we're basically on the list"), NOT local culture or ethnicity
- [x] NPC is a savvy operator — an impartial, unbribable door with a transparent alternative price — not a villain or a thug stereotype
- [x] Humor targets commercial vape culture and pretentious brewing, explicitly not nicotine users or legitimate breweries, per the source file's stated sensitivity constraint

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Debaucheryville/npcs/The_Tap_Dat_Vault/npc_glitching_bouncer.md`
- **Registered In**: No — The Tap Dat Vault has **no** `the_tap_dat_vault_npcs.json`. One must be created; it will need the Glitching Bouncer, The Bartender (vape rig), the two DJ Zombies, the two Techno Monks, and the Fridge Livestreamer, with the Strobe Brewmistress and the Glitched Brew Ad Bot registered as boss/mob rather than NPCs.
- **Sprite Sheet**: `bouncer_glitched.png` (128x192, "Opener checker", per `the_tap_dat_vault.md`'s PNG Asset Requirements Summary). **NOT present in `PNG_Assets/tap_dat_vault_png_asset_requirements.md` — asset gap, flagged above.** Related: `tapdatvault_environment_complete.png` (vault door, countdown glyphs), `tapdatvault_particle_effects.png` (hologram glitch patterns, reusable for his corruption artifacts).

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — authored from `the_tap_dat_vault.md` (opener spec, three canonical check variants, midnight access, rhythm puzzle, three-strike ejection, brewery tour integration) and `PNG_Assets/tap_dat_vault_png_asset_requirements.md` (venue palette, 128 BPM sync, glitch effect assets). Flagged the missing bouncer sprite spec, the one-way queue-skip chip reference, and the proposed beat-drop clarity behavior | machsheltie |

---

*Template Version 1.1*
