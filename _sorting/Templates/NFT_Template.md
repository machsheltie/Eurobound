# NFT Design Template — Ultimate Brochain Collection

*Use this for every NFT added to the Frat Bro NFT sidequest, in the base game and in all future
expansions. Copy this file, fill every section. Sections may be exceeded but never skipped.*

---

## ⛔ BINDING RULES — read before writing a single word

1. **The artwork is ALWAYS 90s or 00s pop culture. NEVER location-derived.**
   The two axes are separate and must stay separate:
   - **Acquisition ROUTE** = location-specific and venue-flavored (a nightclub bathroom QR, a
     rigged claw machine, an auction catalog, a backstage terminal). This is *where you find it*.
   - **ARTWORK / SUBJECT** = 90s/00s pop culture, always. Never the venue, never the city, never
     local scenery, never the country you're standing in. This is *what it is*.
   A location-derived NFT concept is a **defect**. The joke is that the bros crossed a continent
   and came home with American nostalgia they are convinced is a European art portfolio.
2. **The game NEVER winks.** No line of card copy may acknowledge that the asset is worthless,
   nudge the player, or explain the satire. Every word is written in total, sincere reverence.
   The gap between the solemn framing and a $4 plastic toy is the entire joke; naming the joke
   kills it.
3. **The bros are never scam-aware.** They believe every holding is generational wealth. Whoever
   sold, gifted, or minted it knew exactly what it was worth.
4. **No mascots.** An NFT is an image, a sound, or an object — never a character, never a
   companion, never something with a name that talks, follows, or has an arc.
5. **Never name the property outright in the NFT's title.** The title is an oblique, grandiose
   rebrand. (Ghostbusters → *Who You Gonna Call?*; Beanie Babies → *The Polyester Reserve*.)
   The description may reference the real thing freely — real brands and properties are permitted
   by standing author ruling.
6. **MA-rated satire at full strength.** Do not sanitize, soften, or make it "safe."

---

## 1. Identity

| Field | Value |
|---|---|
| **Display Name** | *(oblique, grandiose rebrand — never the literal product name)* |
| **Mint Number** | `Mint #NN` — two digits evoking the artifact's year (e.g. Ghostbusters → #84) |
| **Item ID** | `item_nft_<snake_case_name>` |
| **City** | Debaucheryville / Sinfonia / Publandia / Shamsterdam / *(expansion city)* |
| **Collection Slot** | e.g. "Sinfonia target 2 of 4" |
| **Media Type** | still image / animated GIF / audio / other |

## 2. Acquisition

| Field | Value |
|---|---|
| **Route** | *(the venue + method: QR mural, rigged claw machine, auction catalog, backstage terminal, showdown reward, gift…)* |
| **Venue** | *(exact location file it lives in)* |
| **Unlock Condition** | *(what the player must do)* |
| **Acquisition Beat** | *(2–5 lines: what actually happens in the scene. The bros misread it. Locals do not.)* |

## 3. The Artwork Itself

*What the player literally sees or hears. Intentionally ugly, low-resolution, low-effort, or
mundane. Specify format crimes — JPEG artifacts, visible Photoshop checkerboard, a thumb in
frame, wrong aspect ratio, 240p, mono audio.*

- **Description of the asset:**
- **Format crime:**
- **File/asset name:** `nft_<name>.png` / `.gif` / `.ogg`

## 4. Card Copy — Legacy Vault

*This is the copy that appears on the wallet card. Follow the established register precisely:*

**Tagline** — 2–5 words, mock-crypto or mock-finance terminology, ends with a period.
> *e.g. "Proof-of-Pellet." / "The original gig-economy disruptor."*

**Description** — Frames a piece of 90s/00s pop culture as an *economic* phenomenon. The
established opening move is `"Before [modern thing], ..."` — positioning the artifact as the
ancestor of something current. Must contain at least one hyper-specific absurd detail
(*net-30 terms*, *typos on their tags*, *a $5 stuffed frog*). Written straight; never funny
on purpose; never self-aware.

**Collector's Thesis** — Crypto-investor logic applied with total conviction. Very often ends on
a valuation contradiction stated as though it were bullish:
> *e.g. "Intrinsic value: $0.04. Market sentiment: Infinite."*
> *e.g. "Zero utility, maximum nostalgia, infinite yield."*

**Estimated Future Value** — absurdly optimistic; may be redacted, still loading, or measured
against something it will never outpace.

**Edition Tag** — e.g. *Edition 1 of 1*, *Limited Drop*, *Pre-2005 Retail Artifact*. Contradictions
between the edition tag and the mint number are permitted and often funnier (a 1-of-1 with a mint
number is canon precedent — do not "fix" these).

## 5. Bros' Reaction

*One line each, or a short exchange. They are certain. They are wrong. Nobody corrects them, and
no narrator confirms anything.*

- **Lord Pilsner:**
- **Chadwick:**
- **Bradley:**

## 6. System Integration

- **Counts toward:** Ultimate Brochain Collection (12 base-game; milestones at 4 / 8 / 12)
- **Wallet tab:** The Legacy Vault *(never Bagholder Assets — that tab is for rug-pull certificates)*
- **Resale value:** €0 everywhere. Cannot be sold, traded, or redeemed. Every vendor declines it.
- **Related files:** *(quest leg file, location file, item file, `design/economy/legacy_vault_cards.md`)*

## 7. Validation Checklist

- [ ] Artwork is 90s/00s pop culture, **not** location-derived
- [ ] Title is an oblique rebrand, not the literal property name
- [ ] Mint number evokes the artifact's year
- [ ] Nothing in any copy field winks, explains, or acknowledges worthlessness
- [ ] Bros are never scam-aware; the seller/minter always knew
- [ ] No mascot, companion, or talking entity introduced
- [ ] Asset is specified as ugly/low-effort with a named format crime
- [ ] Route is location-flavored and the artwork is not
- [ ] Real brands/properties left exactly as named (standing author ruling: brands are exempt)

---

## Reference Specimens — author-authored, study these for voice

> **Who You Gonna Call? (Mint #84)**
> **Tagline:** The original gig-economy disruptor.
> **Description:** Before app-based food delivery, four guys in stained jumpsuits charged
> municipal governments ten grand to trap gods in a Tupperware container. This asset captures
> pure, uncut American optimism: the belief that any cosmic nightmare can be solved with
> unlicensed nuclear reactors and an invoice with net-30 terms.
> **Collector's Thesis:** Generational spectral wealth. The physical containment grid may be
> sparking, but this token is immutable. Zero utility, maximum nostalgia, infinite yield.

> **The Polyester Reserve (Mint #99)**
> **Tagline:** Proof-of-Pellet.
> **Description:** Before JPEG monkeys, entire suburban economies collapsed because a billionaire
> named Ty convince the nation that a $5 stuffed frog was a sovereign wealth fund. Millions of
> college funds were liquidated and converted into acrylic-encased polyester bears with typos on
> their tags. This item represents the exact moment American finance abandoned math and embraced
> soft, bean-filled optimism.
> **Collector's Thesis:** The original shitcoin. Unbacked, mass-produced, and stored in a
> Tupperware bin under a basement stairwell. Intrinsic value: $0.04. Market sentiment: Infinite.
