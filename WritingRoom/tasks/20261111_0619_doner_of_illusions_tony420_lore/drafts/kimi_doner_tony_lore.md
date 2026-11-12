# Doner of Illusions™ × Tony420 — the ICQ lore, defined

**Kimi draft, round 1. Primary writer: Kimi. Requested reviewer: Gemini (microcopy teeth, Tony voice, explained-joke audit).**
**Status: PROPOSED. Fills the existing hook** `"unlocks_unique_lore_if_consumed_during_tony420_interaction"` (`debaucheryville_interactions.json` → `debaucheryville_cirque_mystery_cart_01` → menu item `doner_of_illusions`; same string in `debaucheryville_locations.json` and `mysterymeatcart.md`). No canon file is edited by this document.

**Author rulings applied (2026-11-11):** Tony420 is the person (`debaucheryville_npc_tony420_01`); crypto only, every shitcoin at its own SOVS rate; never seen in person — a goon holds a tablet playing a blurred, voice-changed video; lowercase default, shouted words and full stops allowed; Flintstone Fentanyl is his only Flintstone product besides the Xanax quest pill; nobody is self-aware; the bros are never afraid or disgusted.

---

## 1. THE TRIGGER — what "consumed during a Tony420 interaction" means

**Definition:** the Doner of Illusions™ is used from the item menu **while the ICQ window is open on a live Tony420 thread**. That is the whole condition. Eating it at the cart with no ICQ window open, or while the window is open on Hamstradamus or CryptoBro69, changes nothing: the item applies its canon effects (+10 SP, −5 Int, 25% Confused for 2 battles) and no lore fires.

**Player-facing surface, in three steps:**

1. Player buys the Doner of Illusions™ (7 SOVS) at the Mystery Meat Cart.
2. At any signed **FREE Wi-Fi** hotspot, Lord Pilsner whips out his phone; Tony420 hijacks the connection. The intended route uses the Cirque's own `icq_backroom` zone (ICQ terminal hotspot, Darkweb Dossier hack-through pop-ins, `cirque_du_shady.md`), so the whole thing happens on the circus grounds. The ICQ window is open on `Tony420`.
3. With that window still open, the player uses the Doner of Illusions™ on any bro. The ICQ "Uh-oh!" arrives and the lore exchange below replaces the thread. Normal food effects still apply to the eater.

**The eater is Confused/hallucinating.** The exchange fires whether or not the 25% Confused roll landed — the absinthe-glaze hallucination is the item's premise, and Confused is only its combat expression. Requiring the roll would hide the lore from 75% of the players who did the thing right. No roll, no new intoxication tier, no Beer Goggles reuse: this is food, not alcohol, so `intoxication_law.md`'s 10-point review is not engaged. There is no loss of player control beyond the scripted replies the bros type.

**Systems used, all existing:** the ICQ pop-up (`icq_popup.gd` / `show_icq_message`, the same two-way event shape as `icq_great_doner_debate_dialogue.gd`), FREE Wi-Fi hijack, item consumption, the existing Doner of Illusions™ effects. Nothing else.

**One new flag, with its reader:**

| Flag | Set when | Read by | Cleared |
|---|---|---|---|
| `debaucheryville.mystery_cart.doner_tony_lore_seen` | The lore exchange completes | The trigger itself: one-shot per save, so the event never repeats and never displaces later Tony420 hijacks. Also read by the junk-item grant, which fires once | Never |

No gate on `tony420_unlocked` (nothing in canon sets it; Tony hijacks unprompted). No gate on `has_inspected_first_crypto_trash` (no airdrop, no Bagholder Assets deposit happens here). No Döner Debate progress required — if the quest is active, the exchange plays as written and the poll stays where it was.

**Retryability:** if the player closes ICQ before the exchange ends, the flag is unset, the item is already eaten, and the event can be re-armed by buying another Doner of Illusions™ and repeating the steps. Nothing is permanently missable.

---

## 2. THE LORE — what the player actually learns

Three facts, all new, all consistent with the rulings:

1. **Tony420 is admin of the Döner Council because he invented $KBAB.** KebabSwap (`shitcoin_master_pool.md` #8: "collateralised by physical protein… redeemable* for one serving") was Tony's own product, built as a settlement rail for meat. That is why a drug dealer runs a kebab group chat, and why Mr. Chadz's burner says "Meat-backed, they said. My meat. Nobody asked me." The vendors never agreed to back anything; Tony collateralised their rotisseries.
2. **The peg broke.** $KBAB is redeemable for meat only while the meat is *there*. A vertical spit is shaved down all night and rebuilt in the morning, so the underlying asset depreciates on a dinner cycle and re-mints at dawn. Tony treats this as a supply schedule.
3. **His "witness protection" is a pair of Oakleys.** The goon's tablet plays a blurred, voice-changed video, exactly as ruled — and the blur exists to hide that Tony is wearing the same Oakleys as his ICQ avatar, not to hide his face from the law. He calls it witness protection because he thinks that is what the blur is for.

---

## 3. THE EXCHANGE — 24 lines

*The eater's sprite holds the wrap at half-mast. The ICQ window does not change shape. Tony's avatar is the canon pixelated Oakleys-indoors photo.*

```
Tony420: yo why does ur wallet smell like cumin
Bradley: Meat money, baby. We're liquid.
Tony420: u did not just eat a clown doner on my hotspot
Chadwick: It's called pairing, bro. Absinthe and protein.
Tony420: ok u get the tour. ur hallucinating anyway
Tony420: see that meat tower. thats the federal reserve
Lord Pilsner: We knew Europe had a central bank.
Tony420: i made kbab. coin backed by real meat. physical protein
Tony420: one kbab gets u one serving. thats a peg
Bradley: Asset-backed. Like my truck.
Tony420: vendors didnt sign anything. i collateralised the spit
Tony420: clown holds the reserve. chadz holds the float. wim is foreign reserves
Chadwick: Diversified.
Tony420: heres the genius part. the meat shrinks when u eat it
Tony420: supply burns all night. remints at dawn. deflationary
Bradley: My portfolio has a lunch rush.
Tony420: peg broke once. guy ate the collateral. whole district devalued
Lord Pilsner: A run on the bank. We triggered a run on the bank.
Tony420: he did 2 years. not for the meat. for the fries
Tony420: anyway im on video now. witness protection
*A goon steps into frame beside the cart and holds up a tablet. Heavy blur. Voice pitched down to a foghorn.*
Tony420: (video) dont look at the tablet. look at the meat
Chadwick: That's a body double. Guy's a ghost.
*The blur clears for exactly one frame: Oakleys, indoors. Then it smears back.*
Tony420: blur is 4 security. not the face. the oakleys
Tony420: u didnt see anything. ur seeing gummy bears
Tony420: keep the receipt. its a bond
```

**Line-by-line discipline:** Tony never explains the joke, never admits the peg was a scam, and never notices the bros are hallucinating-adjacent — he is giving a sales tour and the food is a marketing opportunity. The bros are thrilled to be insiders. Nobody is frightened by the goon or disgusted by the meat. The "2 years / not for the meat / for the fries" beat is the only unexplained aside and stays unexplained.

**The tablet-goon payoff:** the goon is real and visible in the overworld for this beat only; the video is blurred and voice-changed exactly as ruled; Tony is never seen in person. The single clear frame of Oakleys is a video artifact, not a face reveal — the player learns the avatar is current, not that Tony is identifiable.

---

## 4. THE JUNK ITEM — one, earned

**`council_bond_receipt`** — display name **DÖNER COUNCIL BOND (1 MEAT)**

Grease-stained receipt paper, printed on the cart's own till roll. `consumables.json`, `usable: false`, no sell value, no stats, no combat effect. Granted once with `debaucheryville.mystery_cart.doner_tony_lore_seen`. Its only reader is inventory Inspect.

**Inspect microcopy:**

> "Redeemable for one (1) serving of the underlying asset, at dawn, when the asset grows back. Bearer assumes all gravy risk. Not legal tender. In some backchannels it is legal tender."

**Why it earns its slot:** the item is the lore in the player's pocket — the peg, the dawn re-mint, and Tony's existing "box meat is legal tender in some backchannels" line (`icq_group_sauce_apostates.json`) all land in four sentences. The receipt is physically from the cart the player just ate at, which ties the bond to the food instead of making it a generic crypto gag.

**Sprite:** one 16×16 till-roll scrap, grease translucency at one corner, a dot-matrix `1 MEAT` and a perforated edge that is not actually perforated.

---

## 5. IMPLEMENTATION NOTES

- **No new mechanics.** One boolean flag (§1), one inert item (§4), one scripted ICQ event reusing the existing two-way pop-up. No wallet writes, no coin creation, no status changes beyond the item's canon effects.
- **Save/load:** the flag commits when the exchange completes. Saving mid-exchange resumes the ICQ thread without replaying or double-granting; saving after completion leaves only the flag and the receipt.
- **Ordering with other Tony content:** one-shot means this never competes with AD-01/04/07/11 airdrops, the Couchsurfing pitches, the Döner Debate verdict poll, or the Standing Ovation Xanax delivery. If another Tony event is queued on the same connection, the lore takes precedence once and the queued event fires on the next connection.
- **Text rendering:** `kbab` in Tony's lines should render as `$KBAB` only if the ICQ label passes `$` through unmodified (the airdrop spec already requires `!!!1`, emoji and merge fields to survive). No auto-capitalisation or spell-correction on his body text.
- **Audio:** the standard "Uh-oh! You've got a message!" only. The tablet's voice-change is a pitched-down modem-blip variant of Tony's existing text blips, not new VO.
- **Accessibility:** the one-frame Oakleys flash is a single static sprite swap, not a strobe; it must not trip the cart's existing strobe-reduction setting.

---

## 6. SELF-AUDIT (house §17 + the no-explanation directive)

- No narrator, no editorialising ICQ chrome, no "little did they know."
- Every Tony line is either a sales claim or a threat about looking at the tablet. None diagnoses the bros or the satire.
- "Deflationary" is Tony misusing a term with total confidence; the bros accept it. Nobody translates it for the player.
- The last line ("keep the receipt. its a bond") hands off to the item instead of topping the previous joke.
- Cut from earlier passes: a Chef Chuckles reply explaining the reserve joke; a Pilsner line about the gold standard; a second clear-frame gag. All three explained or repeated a landed beat.

## 7. OPEN ITEMS FOR THE AUTHOR

1. **New permanent lore:** Tony as $KBAB's creator, the vendor-collateralisation, and the dawn re-mint schedule are proposed additions to his backstory and to KebabSwap's pool entry, not yet canon.
2. **The goon** is an unnamed, non-speaking extra. If the author wants him registered (NPC ID, sprite), that is a separate template task; this document does not create him as a character.
3. **The "2 years for the fries" line** implies an off-screen incarceration in the Döner Council's history. Left deliberately unattributed; if the author wants it tied to a named vendor, that is his call.
