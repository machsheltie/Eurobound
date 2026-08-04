# Currency — CANON

**Status:** Canon — author ruling (2026-08-01). **Binding game-wide. No exceptions.**

---

## 🚨 THE RULE

> **"Every. Country. Operates. On. Sovs. Not euros. We do not deal with exchanges of currency between areas. The whole game? Sovs."**
> — Author, 2026-08-01

**The entire game uses a single currency: the Sov (Sovereign).**

- Every city. Every country. Every shop, vendor, fine, bribe, tip, reward, and price tag.
- **Euros do not exist in this game.** Neither do pounds, crowns, koruna, guilders (except as defunct novelty props — see below), or any real-world currency.
- **There is no currency exchange.** Not as a mechanic, not as a mini-game, not as flavour text, not as an NPC service. Nobody converts anything. Nobody comments on the rate. It never comes up.

---

## Format

| Context | Form | Example |
|---------|------|---------|
| Prose and dialogue | `N Sovs` (singular `1 Sov`) | "It cost him 40 Sovs." / "That'll be 1 Sov." |
| Signage, menus, UI, price boards | `N SOVS` (singular `1 SOV`) | `Get them while they're hot and heavy- 5 SOVS` |
| Never | `€`, `EUR`, "euro", "euros" | — |

- Whole numbers by default. Avoid decimals; if a price genuinely needs one, round it instead.
- The symbol is the word. There is no Sov glyph.

---

## 🚨 THE 1-SOV FLOOR (binding)

> **"There should be nothing less than 1 Sov as far as money that exchanges hands... the bros should never be presented with the option to buy anything for less than 1 Sov. No other RPG deals in change and we won't be either."**
> — Author, 2026-08-01

**No transaction in the game is ever below 1 Sov.** There is no change, no small coin, no subunit. The Sov is the atom.

| | |
|---|---|
| ❌ **Never** | Any price, fee, fine, tip, bribe, reward, or purchase option the player can act on, priced below 1 Sov. `0.50 Sovs` for a bag is illegal. Round it up to `1 Sov`. |
| ✅ **Allowed** | Sub-1 figures used as **narrative reference only** — what a vendor paid wholesale, what something is "actually worth", a collapsed valuation. The player never transacts at that number. |

**The distinction is whether money changes hands at that figure.**

- *Legal:* "He buys the wristbands for 0.003 Sovs and sells them for 30." The 0.003 is a cost basis the player never pays.
- *Legal:* an NFT "down 99.7% from mint, now worth 0.0003 Sovs" — a valuation gag, not a shop price.
- *Illegal:* "Need a bag? 0.50 Sovs." That is a purchase option. It becomes **1 Sov**.

**When rounding a former sub-1 price, round UP to 1 Sov**, never down to zero and never to "free" — the joke that everything costs something survives, it just costs one Sov.

---

## What This Does NOT Affect

These are unrelated to currency and stay exactly as they are:

- **"Eurobound"** — the game's title.
- **"Euro Ink 4 Less"** — a location name (Debaucheryville).
- **"EuroMeat Pocket™"** and any other item or business whose name contains "Euro" as branding.
- **"European"** as an adjective — the game is set in a parody of Europe and the word is fine.
- Any other proper noun that happens to contain the letters "euro".

The ban is on **euros as money**, not on the word appearing in names.

---

## ⚠️ THE ONE EXCEPTION: Shadow Exchange

**Author ruling (2026-08-01): Shadow Exchange (Debaucheryville) is the single sanctioned money changer in the game.**

`_sorting/Design/World Design/Debaucheryville/shadowexchange.md` — "Underground Money Changer & Black-Market Bazaar", subtitle *"Best Rates If You Don't Ask"* — keeps its split-flap rate board, its currency trays, Mrs. Rata's counter, and its exchange mini-game.

**What makes it legal under this canon:** it does **not** exchange Sovs for regional currencies, because those do not exist. It deals in **defunct, foreign, and novelty currency that nobody else in the game will accept** — obsolete pre-Sovs coinage, dead notes, casino chips, transit tokens, arcade tokens, and whatever else the back-alley economy is pretending has value this week. It is a black-market oddity trading in worthless paper, not a bureau de change.

**Rules:**
- Shadow Exchange is the **only** place currency exchange exists. No other location, NPC, item, or quest may offer it, reference a rate, or convert anything.
- Sovs remain the universal currency everywhere, including inside Shadow Exchange — Sovs are what you pay with and what you walk out holding.
- The rate board is a joke about a market for things that are not money. It must never imply a real Sov-to-other-currency economy.
- Existing engine data (`shop_type: currency_exchange`, `Currency_Exchange` ability, the mini-game, `opens_interface: currency_exchange`) stays valid for this location only.
- Stale exception found and flagged: `game/Assets/Data/npcs/base_profiles/debaucheryville_core.json` contains `"exchange_rates": {"EUR_to_KC": 0.8, "KC_to_EUR": 1.3}` and `"bribe_currency": ["Euro_Bills", ...]`. Both reference abolished currencies and need rewriting to the defunct/novelty framing.

---

## Defunct Currencies as Props

Obsolete real-world currency may appear as a **comedy prop** — a coin-op machine that only takes a currency nobody has used in twenty years, a jar of worthless coins, a tip left in something long demonetised.

**Constraint:** these are collectibles or obstacles, never money the player earns or spends, and never exchangeable. A quest to find obsolete coins for a vintage machine is fine. A quest to *convert* them is not — that is a currency exchange and it does not exist in this game.

Known instance: **"De Guldenvreter"** (Shamsterdam), a guilder-only condom vending machine. See `Design/World Design/Shamsterdam/shamsterdam_condom_machines.md`.

---

## In-World Justification

None is required and none should be given. No NPC explains why everywhere uses Sovs. No signage announces it. It is simply the money, the way money is money. Do not write lore about monetary union — that is boring and this game is not boring.

---

## For Writers and Agents

Before writing any price, cost, fine, reward, or economic figure: **it is in Sovs.** If you are revising an older file that predates this ruling and contains euro figures, convert them as part of your edit. If you find a currency-exchange mechanic anywhere, it is stale and must be removed.

Cross-references: `Design/Economy/itemvalue.md`, `Design/Economy/shoptypes.md`, `Design/Economy/blackmarket.md`, `Templates/location_validation_template.md`.
