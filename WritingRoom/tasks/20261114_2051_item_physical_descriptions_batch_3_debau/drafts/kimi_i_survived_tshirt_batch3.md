# Batch 3 draft — `i_survived_tshirt` ("I Survived The Cock-Up T-Shirt")

Primary writer: Kimi. Reviewer: Deepseek (or Aion if he posts first).

Source: `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` (30 SOVS, actual value 5, scam_level medium; player_sees "Tourist trap t-shirt. Locals visibly cringe when they see it."). Vendor context: `design/worlds/debaucheryville/astronomical_cockup_square.md` — merchandise stall folding table; the shirt exists because the bros cried at a 38-second puppet show. Lettering rule (brief): the icon renders with no readable lettering, so the print decorates but cannot carry the read — hence the giant crying face carries the joke at icon size.

---

## 🖼️ Physical description (icon art brief) — `i_survived_tshirt`

| Field | Description |
|-------|-------------|
| **silhouette** | A short-sleeved t-shirt laid flat, front up, shoulders squared, torso slightly wider than it is long. The collar sags out of round with one point flipped up; one sleeve sticks out stiffly while the other lies folded under the hem. The bottom hem dips in a shallow smile where the shirt was worn untucked under a gut. A short clothesline cord runs behind the collar with two wooden clothespins on the shoulders. |
| **scale_cue** | The print eats the whole torso: a crying face the size of a dinner plate under a line of text that runs armpit to armpit. A normal souvenir shirt's graphic sits modestly on the chest; this one covers everything the fabric allows. |
| **materials_and_cheap_cues** | Paper-thin white single-jersey cotton, the kind you can read a hand through. The knit texture is visible at the hem; the collar ribbing is a different, cheaper knit that has already gone bacon-wavy. The print is plastisol heat-transfer with a mirror sheen, sitting on top of the fabric and already cracking along the fold lines. An iron-on size label sticks half-peeled out of the back of the collar. |
| **colours** | Shirt: washed-off white #EDEAE0, never optic white, with armpit zones yellowed to #D9CFA8. Print: royal blue #1F4FA3 for the text, fire-engine red #D42B2B for the underline swoosh and the word "COCK-UP", and a sun-faded gold #CFB53B for the clock's rays. Crying face: flat cartoon peach #E8B48C, tears blue #7FB5D5, mouth black #26221E. Clothespins: raw pine #D9B98A. |
| **contents** | The shirt itself is the object; nothing inside. Through the thin fabric, faint grey ghost lines show the folding-table grid underneath. |
| **decoration** | The print, armpit to armpit: **"I SURVIVED THE"** in small royal-blue capitals; below it **"COCK-UP"** in enormous red capitals, the letters slightly bowed where the transfer was applied over the belly curve; below that a cartoon of the clock tower's gold dial drawn as a weeping face with two huge blue tear drops and a wavy open mouth; under the face, a red swoosh underline with **"DEBAUCHERYVILLE"** in small blue capitals inside it. The red of "COCK-UP" is cracked across every fold; one tear drop has a hairline crack through it. |
| **condition** | Sold new, already dying: collar ribbing wavy from the vendor's iron; a grey scuff across the left shoulder from the table; a faint rectangular price-sticker ghost on the hem where a sticker was peeled off; the transfer's red layer flaking at the "C"; armpits pre-yellowed because the vendor's stock sits in a damp lock-up. One clothespin has left a pinch mark in the shoulder. |
| **garnish_and_addons** | Two wooden clothespins clipped on the shoulders, one of them gripping a scrap of the vendor's handwritten cardboard price tag (a torn brown rectangle with a single thick marker stroke, no readable price). A length of cheap white plastic clothesline droops behind the collar. |
| **palette_anchors** | From `astronomical_cockup_square.md` Technical Specifications: Gothic Gold #CFB53B, Scam Green #7FFF00, Neon Pink #FF1493 (kept to none of the print; the shirt is red/blue/gold so it reads as its own object against the square's signage). New to this item: #EDEAE0, #D9CFA8, #1F4FA3, #D42B2B, #E8B48C, #7FB5D5, #26221E, #D9B98A. |
| **reads_at_icon_size** | 1. A white t-shirt on a line, unmistakably a shirt, not a flag or a towel: collar, sleeves, hem dip. 2. A souvenir of a bad experience, not a band tee: the giant crying gold clock-face with two blue tears reads instantly as "wept-at tourist attraction". 3. Cheap and doomed: the wavy bacon collar, the cracking red print, the yellowed armpits and the clothespins say folding-table merch, not a shop. |
| **must_not_look_like** | A clean screen-printed band or college tee on a hanger. A flag, banner or folded sweater. A photoreal clock face (it is a flat cartoon crying face). Anything a local would wear. A new shirt in good condition. The words carrying the joke at icon size (the crying face does that). |
| **lettering** | Top line: **I SURVIVED THE** — middle: **COCK-UP** — inside the swoosh: **DEBAUCHERYVILLE**. All spelled out here for the art file; at icon size the lettering blurs and only the crying face and the red mass of "COCK-UP" survive. No other text; the price tag is a marker stroke only. |

---

### Continuity notes for the integrator
- Name, price, stats (+1 Bravado / −2 Charm), effects and story untouched — looks only, per rpac.
- "Locals visibly cringe" is an NPC animation trigger, not an icon property; the icon just has to look like something worth cringing at.
- No real place names; DEBAUCHERYVILLE is the parody name and is the only word that could appear on the print besides the survival claim. The word "Europe" appears nowhere.
