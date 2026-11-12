# Doner of Illusions™ × Tony420 — APPROVED (author, desk 2026-11-11 19:06)

Author: the Doner of Illusions × Tony420 lore is approved. Built from Gemini's polished exchange and bond inspect line (`drafts/gemini_doner_tony_lore.md` §2), with the five changed lines from the cart-associate revision (`../20261111_1027_tony420_tablet_staging/drafts/kimi_cart_associate.md`: the goon works the cart as Tony's silent "associate"; no tablet, video call or voice changer here, since the tablet reveal belongs to the Great Döner Debate). Trigger, flag and item definitions are Kimi's (`drafts/kimi_doner_tony_lore.md` §1 and §4).

Fills the hook in `design/worlds/debaucheryville/mysterymeatcart.md` (Doner of Illusions™, "unlocks unique ICQ lore if consumed during Tony420 interaction"). Engine data under `game/` is not touched by this approval.

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

No gate on `tony420_unlocked` (Tony hijacks unprompted; the flag is set by his first hijack, an approved engine change not yet built). No gate on `has_inspected_first_crypto_trash` (no airdrop, no Bagholder Assets deposit happens here). No Döner Debate progress required — if the quest is active, the exchange plays as written and the poll stays where it was.

**Retryability:** if the player closes ICQ before the exchange ends, the flag is unset, the item is already eaten, and the event can be re-armed by buying another Doner of Illusions™ and repeating the steps. Nothing is permanently missable.

---

## 2. THE EXCHANGE — 24 lines

*The eater's sprite holds the wrap at half-mast. The ICQ window does not change shape. Tony's avatar is the canon pixelated Oakleys-indoors photo.*

```
Tony420: yo why does ur wallet smell like cumin
Bradley: Meat money, baby. We're liquid.
Tony420: u did not just eat a clown doner on my hotspot
Chadwick: Absinthe and lamb, bro. Pre-workout pairing.
Tony420: ok u get the tour. ur hallucinating anyway
Tony420: see that meat tower. thats the federal reserve
Lord Pilsner: We knew Europe had a central bank.
Tony420: i made kbab. coin backed by real meat. physical protein
Tony420: one kbab gets u one serving. thats a peg
Bradley: Asset-backed. Like my truck.
Tony420: vendors didnt sign shit. i collateralised the spit
Tony420: clown holds the reserve. chadz holds the float. wim is foreign reserves
Chadwick: Diversified portfolio.
Tony420: heres the genius part. the meat shrinks when u eat it
Tony420: supply burns all night. remints at dawn. deflationary
Bradley: My net worth has a lunch rush.
Tony420: peg broke once. guy ate the collateral. whole district devalued
Lord Pilsner: A run on the bank. We triggered a run on the bank.
Tony420: he did 2 years. not for the meat. for the fries
Tony420: anyway u never saw me. witness protection
*A huge man in a suit and a grease-stained apron is shaving the rotisserie behind the cart. He has not looked up once.*
Tony420: thats my associate. dont look at him. look at the meat
Chadwick: Guy's an international ghost.
*The ICQ avatar unpixelates for exactly one frame: Oakleys, indoors. Then it smears back.*
Tony420: blur is 4 security. not the face. the oakleys
Tony420: u didnt see anything. ur seeing gummy bears
*The associate tears a receipt off the till and holds it out at arm's length.*
Tony420: keep the receipt. its a bond
```

### Staging (the cart associate)

- The associate is already working the cart when the exchange begins; he does not make an entrance, speak, react or receive a name. His only action beyond shaving meat is handing over `council_bond_receipt`, which replaces the abstract receipt grant with the permitted goon handover.
- The Oakleys flash is a one-frame swap of the existing ICQ avatar sprite, not video and not a face reveal. It remains a single static image, with no strobe.
- The approved lore, trigger, one-shot flag, normal Doner effects, item ID and Gemini-polished **DÖNER COUNCIL BOND (1 MEAT)** inspect copy are unchanged.
- No line identifies the associate as a goon, explains witness protection, or comments on the joke. The Döner Debate remains the first blurred/voice-changed Tony420 appearance and the first tablet entrance.

---

## 3. THE ITEM — one, earned

**`council_bond_receipt`** — display name **DÖNER COUNCIL BOND (1 MEAT)**

Grease-stained receipt paper, printed on the cart's own till roll. `consumables.json`, `usable: false`, no sell value, no stats, no combat effect. Granted once with `debaucheryville.mystery_cart.doner_tony_lore_seen`, handed over by Tony's cart associate (see §2 staging). Its only reader is inventory Inspect.

**Inspect microcopy:**

> "Redeemable for one (1) serving of the underlying asset at dawn, when the spit grows back. Bearer assumes all gravy risk, trans-fat liability, and bacterial arbitrage. Not legal tender. In some backchannels it is legal tender."

**Why it earns its slot:** the item is the lore in the player's pocket — the peg, the dawn re-mint, and Tony's existing "box meat is legal tender in some backchannels" line (`icq_group_sauce_apostates.json`) all land in four sentences. The receipt is physically from the cart the player just ate at, which ties the bond to the food instead of making it a generic crypto gag.

**Sprite:** one 16×16 till-roll scrap, grease translucency at one corner, a dot-matrix `1 MEAT` and a perforated edge that is not actually perforated.
