# ICQ Airdrops

**Status:** Design, Round 5. Derived from `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §4 (author-locked) under the Round 5 plan, Lane E.
**Owns:** airdrop delivery channel, sender roster, payload rules, bro reaction beat, the airdrop message set.
**Related docs:** `design/economy/economy_system.md` (flags, seed, rug logic), `design/economy/wallet_ui.md` (Bagholder Assets tab and its reveal), `design/economy/shitcoin_master_pool.md` (the coin pool airdrops draw from).

---

## 0. Voice Contract

Airdrops are **passive and comedy-only.** They have no mechanical effect of any kind — no stat, no currency, no quest hook, no hidden accumulation that pays off later. They exist so that worthless tokens keep arriving unbidden and the party keeps taking it as validation.

Two voices, never mixed:

- **The senders are working.** Tony420 and company know exactly what a $SPANK token is worth. Their copy is confident, competent scam-marketing — urgency, scarcity, insider access, capitalization abuse. They are not confused; they are selling.
- **The bros are winning.** Every airdrop is inbound institutional interest. Somebody out there sees what they are building. They never wonder why. They never check. They never ask what the coin does.

**Nothing winks.** The ICQ window does not editorialize. There is no narrator line after an airdrop. No NPC ever says "you know that's spam, right?" Not once, not as a joke, not from a minor character.

---

## 1. Delivery

### 1.1 Channel

Airdrops arrive through the **in-game ICQ window** — the same pop-up used for existing Darkweb Dossier crossover messages, with the same presentation: sender handle, pixelated avatar, message body in the ICQ chrome.

Accompanied by the vintage **"Uh-oh!"** sound — the existing `"Uh-oh! You've got a message!"` soundbite already established for ICQ pop-ups. No new sound, no variant, no sting. The joke works because it is the *same* noise that has always meant "someone wants something from you."

### 1.2 Placement

Existing canon anchors ICQ pop-ups to signed **"FREE Wi-Fi"** hotspots, which double as save points. Airdrops should follow that canon: a hotspot connection may deliver an airdrop instead of, or alongside, a normal ICQ chat.

Frequency: sparse. An airdrop is an occasional event, not a per-hotspot tax. Repeated firing turns a running gag into a chore.

### 1.3 Ordering constraint (integration, binding)

**Airdrops must not fire before `has_inspected_first_crypto_trash` is true.**

Reason: an airdrop deposits into **Bagholder Assets**, and before the reveal that tab does not exist (`wallet_ui.md` §3.1) — it does not render, and there is no stub to hold anything. Firing an airdrop earlier would either leak the hidden tab or drop an item into a container the game has not built.

This is a consequence of the hidden-tab rule rather than an author ruling; see §5 Open Items.

### 1.4 Payload

Each airdrop deposits a quantity of a **0-value junk coin** into Bagholder Assets. It renders there exactly like every other item in that tab: flat grey, plain quantity and denomination, value `$0.00`, no commentary.

- Quantities are always large. Six figures is normal. Large numbers are the entire perceived value.
- Payload coins are drawn from the master pool (`shitcoin_master_pool.md`). Airdrops do **not** introduce coins that exist nowhere else.
- Airdropped coins are **not spendable.** No back-alley vendor accepts them, no kiosk exchanges them, they are not a free ticket into the 35/65. They are junk that has arrived.
- No accept/decline prompt. The player is not consulted. That is what an airdrop is.

### 1.5 The bro reaction beat (~3 seconds)

Immediately after the message, one party line, roughly three seconds on screen, in normal dialogue presentation. It **misinterprets the airdrop as institutional validation.**

Canonical line, **author-locked, verbatim** — use exactly as written wherever the $SPANK 100,000 airdrop is delivered:

```
Chadwick, we just got airdropped 100k SpankTokens! We're institutional investors now, bro!
```

Rules for all other reaction lines:

- Read the airdrop as **evidence of arrival** — the market noticed them, a fund is positioning, they are on a list.
- Never suspicious, never sarcastic, never a punchline about spam.
- No party member ever plays sceptic. There is no straight man in the party for this bit.
- One line only. No back-and-forth, no follow-up, no callback later in the scene.

---

## 2. Senders

### 2.1 Canonical (author-specified)

| Handle | Register |
|---|---|
| **Tony420** | Established cyber-dealer. All-lowercase, no punctuation, no capitals, chronically online at 3 AM. Sells absolutely anything. Treats an airdrop as a free sample that obligates you. |
| **CryptoBro69** | NFT evangelist, already canon as the "Pixelated Kebab Monkey" shill. Speaks in thesis. Capitalizes Concepts. Believes his own pitch harder than the bros do, which is why he is the most dangerous man in the game. |
| **SpamBot99** | Automated. Corporate template language with the seams showing — unresolved merge fields, mismatched pluralization, a footer that does not belong. Never answers, never varies its tone, never stops. |

### 2.2 Permitted additional senders (existing Darkweb Dossier canon)

Consistent with §4's allowance for senders drawn from Darkweb Dossier canon:

| Handle | Register |
|---|---|
| **CryptoMamiXXX** | Established. Sells adjacent nonsense with total commitment. Warm, familiar, transactional. |
| **richfield69** | Established. Late-night, needy, four-thousand-days-idle energy. When he airdrops, it reads like an apology he is trying to expense. |

**NarcGreg does not airdrop.** He is canonically the recipient of this material, not a distributor. Using him as a sender contradicts his established function.

No new senders are invented in this document.

---

## 3. Airdrop Message Set

Twelve messages. All payload coins are author-seed or existing-canon coins; once the master pool is final, payloads may be re-pointed to any pool coin — the messages are the asset, the coin is a slot.

Format per entry: **sender**, **payload**, **message body** (as it appears in the ICQ window), **reaction** (the ~3-second party line).

Reaction lines marked DRAFT are subject to author veto at review. The canonical line in #1 is author-locked and byte-exact.

---

**AD-01 — Tony420 — payload: 100,000 $SPANK**

```
Tony420:
yo bro sent u 100k $SPANK off the top no charge
dont sell it. dont even look at it. just hold
u kno what u got
```

> **Reaction (AUTHOR-LOCKED, VERBATIM):**
> `Chadwick, we just got airdropped 100k SpankTokens! We're institutional investors now, bro!`

---

**AD-02 — SpamBot99 — payload: 500,000 RugPullInu**

```
SpamBot99:
DEAR [WALLET_HOLDER_NAME],
CONGRATULATION! YOU HAVE BEEN SELECT FOR 500,000 RUGPULLINU
REASON FOR AWARD: LOYALTY
NO ACTION IS REQUIRE. NO ACTION IS POSSIBLE.
--
This message is intended only for [WALLET_HOLDER_NAME].
```

> **Reaction (DRAFT):** "They picked us for loyalty. We haven't even done anything yet."

---

**AD-03 — CryptoBro69 — payload: 12,000 GigaChadX**

```
CryptoBro69:
Sending you a Position. Not a Gift. A Position.
GigaChadX is not a coin, it is a Posture.
Most wallets are not built to hold Posture.
Yours was flagged as Ready.
```

> **Reaction (DRAFT):** "Our wallet got flagged as Ready. Do you know what that means?"

---

**AD-04 — Tony420 — payload: 8,400,000 MoonCum696969**

```
Tony420:
dumping 8.4 mil mooncum into ur wallet
its backed by beanie babies and ketamine
supply is capped bc the guy who can mint more is in prison
HODL!!!1
```

> **Reaction (DRAFT):** "Capped supply, Chadwick. Capped. There will never be more of this."

---

**AD-05 — SpamBot99 — payload: 1 ThongCoin**

```
SpamBot99:
YOUR AIRDROP OF 1,000,000 THONGCOIN HAS BEEN PROCESSED.
AMOUNT DELIVERED: 1 THONGCOIN
DIFFERENCE: NETWORK
THANK YOU FOR YOUR CONTINUE PARTNERSHIP.
```

> **Reaction (DRAFT):** "One. That's the rarest one, then. That's just math."

---

**AD-06 — CryptoMamiXXX — payload: 250,000 SafeMoon-X**

```
CryptoMamiXXX:
hey you 😘
sending 250k SafeMoon-X to the wallets i actually believe in
short list. very short list.
dont make me look stupid
```

> **Reaction (DRAFT):** "She has a short list. We're on the short list."

---

**AD-07 — Tony420 — payload: 66,600 TractorCoin**

```
Tony420:
tractorcoin. agricultural sector. real world assets bro
every token is backed by like. a field
which field is not disclosed for tax reasons
sending u 66,600 to get in early
```

> **Reaction (DRAFT):** "Real world assets. Land, Chadwick. We own part of a field."

---

**AD-08 — CryptoBro69 — payload: 3 GigaChadX**

```
CryptoBro69:
Correcting an earlier oversight.
You were under-allocated. That has been resolved.
I am not able to say by whom.
The allocation is small because the allocation is Early.
```

> **Reaction (DRAFT):** "Somebody upstairs noticed we were under-allocated."

---

**AD-09 — SpamBot99 — payload: 4,000,000 RugPullInu**

```
SpamBot99:
FINAL NOTICE (1 OF 9)
YOUR 4,000,000 RUGPULLINU IS DELIVERED AND CANNOT BE RETURN.
TO STOP RECEIVING THIS AIRDROP, REPLY "STOP".
REPLYING "STOP" WILL NOT STOP THIS AIRDROP.
```

> **Reaction (DRAFT):** "You can't even give these back. That's how scarce they are."

---

**AD-10 — richfield69 — payload: 777,000 ThongCoin**

```
richfield69:
sent u 777k thongcoin
consider it square between us
also if u see cryptomami tell her i changed
tell her about the coin first tho
```

> **Reaction (DRAFT):** "He settled a debt with us. In assets. Like adults do."

---

**AD-11 — Tony420 — payload: 2,000,000 SafeMoon-X**

```
Tony420:
whoever this wallet belongs 2, congrats
u were the 1000th connection on this hotspot
2 mil safemoon-x deposited automatic
no i cant tell u who paid for it
```

> **Reaction (DRAFT):** "An anonymous benefactor. We have an anonymous benefactor."

---

**AD-12 — CryptoBro69 — payload: 100,000 $SPANK**

```
CryptoBro69:
Topping up your $SPANK.
Not because you need it. Because the Thesis needs it.
A position this size begins to look like Conviction.
Conviction is what the market prices in last.
```

> **Reaction (DRAFT):** "We're being priced in, bro. We're being priced in."

---

## 4. Engine Requirements

### 4.1 Existing hook

The ICQ pop-up already exists at `game/Scripts/ui/icq_popup.gd` with:

```
show_icq_message(sender: String, text: String, avatar_path: String)
```

Airdrops **reuse this call**. Do not build a second pop-up, a distinct "airdrop window", or any bespoke chrome. The visual identicalness to ordinary spam is the point.

### 4.2 Airdrop record

```
id             : String        # AD-01 .. AD-12
sender         : String        # handle; maps to existing avatar asset
body           : String        # message text, preserved exactly incl. casing and typos
payload_coin   : String        # coin_id from the master pool
payload_amount : int
reaction_line  : String
one_shot       : bool = true   # each airdrop fires at most once per save
```

**Do not spell-correct, capitalize, or auto-format `body`.** The typos, the missing punctuation, the `!!!1`, and the unresolved `[WALLET_HOLDER_NAME]` merge fields are authored copy. Any text pipeline that "cleans" these breaks the joke.

### 4.3 Flags and gating

| Flag | Use |
|---|---|
| `has_inspected_first_crypto_trash` | **Hard gate.** No airdrop may fire while false (§1.3). |
| `airdrops_delivered` | `Array[String]` of fired airdrop IDs; enforces `one_shot` |
| `bagholder_assets` | Receives the payload deposit |

Flag definitions are canonical in `design/economy/economy_system.md` §8.2.

### 4.4 Delivery rules

- Trigger surface: Wi-Fi hotspot connection. Airdrop delivery must not block or replace saving.
- Selection: pick uniformly at random from airdrops not yet in `airdrops_delivered`. When the set is exhausted, airdrops simply stop. No looping, no procedural generation, no "you have 47 new messages" escalation.
- Rate limit: at most one airdrop per hotspot connection, with a cooldown of several hotspot visits between deliveries. Exact spacing is tuning.
- Deposit is silent — no item-get jingle, no toast, no inventory-full warning. The pop-up and the reaction line are the whole event.
- Airdrops have **zero** interaction with the 35/65 roll, the active roster, roster rotation, or `economy_seed`. They are a closed loop.

### 4.5 Text rendering

Message bodies contain emoji, `!!!1`, bracketed merge fields, and inconsistent casing. Verify the ICQ label renderer passes all of these through unmodified before locking the font and text pipeline.

---

## 5. Open Items / Escalations

1. **Airdrop gating on `has_inspected_first_crypto_trash` (§1.3).** Derived from the binding hidden-tab rule rather than stated by the author. It is the only ordering that preserves the Tab 2 reveal. Flagged for author confirmation; if the author wants airdrops firing pre-reveal, the reveal trigger itself would need to widen to include "first airdrop received."
2. **Reaction lines AD-02 through AD-12 are DRAFT.** Register is locked by §1.5; specific lines are subject to author veto.
3. **Payload coin assignment.** Messages currently use author-seed and existing-canon coins only, to avoid pre-empting Lane C's master pool. Once the pool is final, payloads may be re-pointed; the message bodies stay as written.
4. **Speaker attribution.** The author-locked reaction line addresses Chadwick, so the speaker is one of the other two. Unassigned in source — same open item as `economy_system.md` §9.1.

## 6. Cross-References

- Flags, seed, rug logic, kiosk system → `design/economy/economy_system.md`
- Bagholder Assets presentation and reveal → `design/economy/wallet_ui.md` §3
- Coin pool and certificate/QR content → `design/economy/shitcoin_master_pool.md`
- Existing ICQ canon → `_sorting/Design/Quests/darkwebdossiercrossoverevents.md` (read-only reference this round)
- Source spec → `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §4
