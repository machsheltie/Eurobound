# Item physical descriptions, batch 3 (PROPOSED)

Bead Eurobound-rpac. The 12-field format (Desk rpac-q1). Drafts compiled by the moderator: Kimi (tee, snow globe), Deepseek (rhinestone shirt, thong), Mistral (VIP wristband). On approval, each section goes into the item's own .md (a short new .md where an item has none).

---

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

---

# Batch 3 draft — `clock_snow_globe` ("Clock Snow Globe")

Primary writer: Kimi. Reviewer: Mistral (or Aion if he posts first).

Sources: `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` (25 SOVS, actual value 3, scam_level medium; use_action "shake", audio_on_use "tiny_sad_clock_chime", sellback 1 SOV; player_sees "Shake it and feel the disappointment all over again."). Clock description from `design/worlds/debaucheryville/astronomical_cockup_square.md` — "The Clock Tower Detail" section only: Gothic tower, blue-and-gold astronomical dial with zodiac symbols, skeleton Death at the corner with hourglass and bell rope, golden mechanical rooster in a small window above Death, two apostle windows. Palette anchors from the same doc's Technical Specifications. Snow globes sit on the merchandise stall's folding table next to the plates and temp tattoos.

---

## 🖼️ Physical description (icon art brief) — `clock_snow_globe`

| Field | Description |
|-------|-------------|
| **silhouette** | A small glass snow globe: a round dome about two-thirds of the object's height, seated on a squat hexagonal resin base with a stepped foot. The dome is slightly egg-shaped, taller than wide, with a visible thick glass rim where it meets the base. A tiny tower shape stands dead centre inside. Nothing elegant: the proportions are squat and bottom-heavy, souvenir-shelf, not mantelpiece. |
| **scale_cue** | The base is as tall as the tower inside the dome, and the tower's dial is the size of a fingernail — the base is oversized because that's where the moulded "scene" and the lettering band live, which is how souvenir globes are actually built. |
| **materials_and_cheap_cues** | Dome: thin blown glass with a visible vertical seam and a slight wobble in the curve, never crystal; a greasy fingerprint haze on one side. Liquid: water gone faintly cloudy, with one slow air bubble the size of a pea stuck at the top that never quite leaves. Base: cast polyresin painted to imitate carved stone, with a mould seam around the foot and a felt pad already peeling at one corner. Snow: white plastic flakes plus coarse gold glitter that clumps. |
| **colours** | Glass: faint blue-green cast #CFE3E2 at the rim. Liquid: murky pale aqua #AECFC9. Tower: Gothic grey #6E6A66 with gold dial #CFB53B and blue dial field #2E4A7A; rooster gold #D4A017; skeleton bone white #E8E4D8. Snow: flat white #F5F5F0; glitter clumps antique gold #B8912F. Base: fake-stone tan #A08C6E with a dry-brushed gold band #CFB53B; felt pad dark brown #4A3B2C. Price sticker: white #F2EEE4. |
| **contents** | Inside the dome: a miniature of the square's clock tower, simplified to a spire, one blue-and-gold dial with two stubby hands, two tiny apostle windows (shut), a bone-white skeleton blob at the corner holding a speck of an hourglass, and a gold rooster comma in the window above it. The tower leans about three degrees off vertical. The "snow" is mostly settled on the tower's shoulders and the dome floor, with a few flakes and one clump of gold glitter still suspended. |
| **decoration** | The base is moulded in relief with a tiny square scene: a crowd of six faceless tourist bumps with raised phone rectangles, and a banner band around the foot carrying the lettering (below). The relief is soft and lumpy — the mould was worn out three production runs ago. Dry-brushed gold paint catches only the high points, so the "carving" reads as smudged. |
| **condition** | New but already tired: the cloudy water (it was filled with tap water, not distilled); the permanent top bubble; the felt pad peeling; a crescent scratch on the dome; the gold dry-brush already worn off the highest bumps; a white price sticker on the felt with a single printed stroke. One dead flake of glitter is stuck permanently to the inside of the glass above the waterline. |
| **garnish_and_addons** | None — it is the garnish. The price sticker is the only add-on. |
| **palette_anchors** | From `astronomical_cockup_square.md` Technical Specifications: Gothic Gold #CFB53B, Stone Gray #708090 (shifted darker to #6E6A66 for the miniature so it separates from the glass), Cobblestone Brown #8B7355 (echoed in the base's #A08C6E). New to this item: #CFE3E2, #AECFC9, #2E4A7A, #D4A017, #E8E4D8, #F5F5F0, #B8912F, #4A3B2C, #F2EEE4. |
| **reads_at_icon_size** | 1. A snow globe, instantly: round dome on a squat decorated base, white flakes inside. 2. A clock-tower souvenir, not a Christmas globe: the grey spire with a single gold-and-blue dial and the gold rooster dot read as "that clock" even with no lettering. 3. Sad and cheap: cloudy water, the stuck bubble, the leaning tower and the clumped glitter say 3-SOV gift shop, and the snow sitting mostly settled hints at the underwhelming chime. |
| **must_not_look_like** | A Christmas or winter-holiday globe (no Santa, no tree, no red). A crystal or high-end souvenir. A snowman scene. A functioning, pristine keepsake — the water is cloudy and the tower leans. A paperweight with no base relief. Readable lettering at icon size (the band is a smudge of gold at that scale). |
| **lettering** | On the base band: **ASTRONOMICAL COCK-UP** on the front and **DEBAUCHERYVILLE** on the back, moulded in relief and dry-brushed gold. Spelled out here for the art file; at icon size the band reads as a gold smear only, and no read depends on it. |

---

### Continuity notes for the integrator
- Name, price, effects (shake / tiny sad chime / 1 SOV sellback) and story untouched — looks only, per rpac.
- The "tiny_sad_clock_chime" is audio; the icon just has to look like it would make one.
- The tower miniature must stay faithful to the clock description (skeleton + rooster + blue-gold dial) but simplified to blobs at this scale — no new lore, no extra figures.
- No real place names anywhere; "Europe" nowhere.

---

# Batch 3 draft — Deepseek

Items: (3) Rhinestone Shirt of Shame (Bedazzled), (4) `item_leopard_print_thong`.

Reviewer for both: **Kimi** (voice/character) with **Mistral** on the thong's icon-scale question (see the flag at the bottom). Looks only: no name, price, stat, effect or story change. No real place names, no "Europe", no lettering carried by the icon.

---

## 🖼️ Physical description (icon art brief) — Rhinestone Shirt of Shame (Bedazzled)

Source of the item and its numbers: `design/items/docs/equipment.md:240-243` (+4 Attention Seeking, +1 Disco Ball Effect, −3 Taste; "Blinds enemies and bystanders with its gaudy magnificence"; "Each rhinestone tells a story of questionable life choices"). An existing icon prompt sheet already exists at `Assets/Graphics/items/rhinestone-shirt-of-shame.md` (black slim-fit button-down, swirling stone design, roughly a third of the stones missing, pale yellowed glue dots, sweat patch, flapping cuffs, curled collar point). **This table keeps that sheet's look and its 16-colour palette intact** and specifies what the sheet leaves soft: what the swirl is, how the missing third scatters, and what the wear is. No contradiction with the existing sheet.

| Field | Description |
|-------|-------------|
| **silhouette** | A long-sleeved button-down shirt hanging flat, front up, no body in it and no hanger: squared shoulders, a straight hem, both sleeves hanging to mid-thigh length so the cuffs flap loose and unbuttoned, one cuff turned back and one not. The collar is splayed wide open with the top three buttons undone, opening a deep V that reaches the top of the stone pattern. One collar point curls up and holds. A single diagonal band of stone clusters runs from the left hip up across the chest and over the right shoulder, so the sparkle crosses the body the wrong way and reads at a glance as a sash. |
| **scale_cue** | The stones are big enough to count: roughly 20 across the chest at icon resolution, each one 1–2px with a single brighter centre pixel, so the bald patches read as missing stones instead of wear. A second scale tell is the open collar: a good three buttons' worth of gap, wide enough that the shirt is clearly cut slim and cheap, not a roomy work shirt. |
| **materials_and_cheap_cues** | Slick polyester-blend poplin with a hard, unfriendly sheen: two flat highlight bands, no soft folds. The cloth is thin enough that the button placket shows as a raised ridge under the stones. Flat faceted acrylic rhinestones in glued rows, not sewn, not foil-backed glass, not crystals — each one set slightly proud of the cloth so its shadow falls on the fabric. The glue is a visible pale slug around every stone. The buttons are thin, cheap, four-hole, sewn on with a thread that does not match. The sleeve cuffs are fused, not turned and stitched. |
| **colours** | Cloth: near-black #16161A with a mid #2E2E36 where it turns and a hard sheen #4A4A56 along the top of each fold. Outline #2B1A2E. Stones: silver-white #F4F8FA, cyan #3EC6D8, magenta #D83EC0, each with a pure white centre pixel #FFFFFF and a shadow pixel #C4CAD4. Missing stones: a bald glue dot #C9BE8E with its shadow #9E9268, roughly a third of the pattern, scattered. Sweat: #3E3A44 under one arm, spreading into the cloth. Dried drink stain: amber-brown #8A6A2F. Frayed thread at the cuff and at the empty bottom buttonhole: grey #8A8A93. Cast shadow: #6E5F72. |
| **contents** | None — it is a shirt. No body inside it, no hanger through the neck, nothing in the breast pocket, because it has no breast pocket. |
| **decoration** | One glued stone pattern, no other trim: a swirl that was designed as a dragon and no longer is one, because the missing third took the head, one wing and most of the tail. What survives is a fat comma of stone clusters across the chest ending in a hook over the right shoulder. The stones are set in rows that kink where the pattern crosses the button placket, and one row of about nine stones has clearly been re-glued by hand, sitting a full stone-width off line with a smear of excess glue under it. No motif is legible, no shape repeats, nothing spells anything. |
| **condition** | Worn at least once, probably all night, and not washed: a third of the stones gone with bald glue dots left behind; the re-glued crooked row; a dark sweat patch under the right arm bleeding through to the outside; an amber drink stain down the left side that has dried and set; the bottom button missing with a short grey thread tail and a stretched-out buttonhole; the hem's stitching come undone for about the width of a thumb; both cuffs unbuttoned and grubby at the edges; one collar point permanently curled; one plastic tag barb still lodged in the collar seam with the tag itself ripped away. |
| **garnish_and_addons** | The single plastic tag barb in the collar seam, and nothing else. No hangtag, no price sticker, no tissue, no spare button bag, no bow. |
| **palette_anchors** | Reuses the existing icon sheet's palette unchanged (`Assets/Graphics/items/rhinestone-shirt-of-shame.md` §4): #2B1A2E, #16161A, #2E2E36, #4A4A56, #F4F8FA, #C4CAD4, #3EC6D8, #D83EC0, #FFFFFF, #C9BE8E, #9E9268, #3E3A44, #6E5F72, plus #FF00FF chroma key. New to this item, and they take the sheet to its 16-colour limit: #8A6A2F (dried drink stain), #8A8A93 (frayed thread). Location anchors that must **not** appear on the garment: Neon & Chrome #FF1493 / #C0C0C0 / #4B0082 / #00BFFF (`design/worlds/debaucheryville/neon_and_chrome_boutique.md:88`) and Velvet Curtain #FFD700 / #800020 (`velvet_curtain_club.md:284-285`). The shirt is black and silver; the club is the light source, not the garment. |
| **reads_at_icon_size** | 1. A black long-sleeved button-down hanging flat: collar, placket, two flapping cuffs, straight hem. Not a jacket, not a dress, not a tee. 2. A sparkle sash crossing the body the wrong way, bright and clustered, with obvious bald gaps punched through it: bedazzled, and half of it has fallen off. 3. Cheap and already ruined: hard plastic sheen, a sweat patch, a drink stain, an empty bottom buttonhole and a thread tail. |
| **must_not_look_like** | A plain black shirt (the stone sash and the bald patches are the object). A clean, new, fully-stoned shirt (a third of the stones must be missing). A sequinned jacket, jumpsuit or Elvis costume (glued acrylic stones on poplin, not sequins, not a collar-to-cuff covered suit). A leather or satin club shirt. A printed graphic tee. A recognisable rhinestone motif — no skull, no heart, no star, no animal head, no flames, no team logo, no text. A shirt with a body in it: no torso, no arms, no hands, no neck, no mannequin. A costume-shop Halloween item. Club neon on the fabric. |
| **lettering** | None. The pattern is not a word, not initials, not a monogram, and not a brand; the tag barb holds no tag, so there is no printed text anywhere on the item. If the generator produces anything readable on the stones or the collar, it is a defect. |

**Continuity notes — shirt**
- The existing prompt sheet's "flat pure-magenta #FF00FF chroma-key field" and 16-colour cap are respected: this brief adds two hexes and stops.
- "Slim-fit" is kept from the sheet. It is the shirt's cut, not a comment on who is in it — the icon shows an empty shirt, so no body is described or implied.
- The +1 Disco Ball Effect proc frame (96x96, radiating cyan/magenta spokes) is already specced on the sheet and is unaffected by this brief.

---

## 🖼️ Physical description (icon art brief) — `item_leopard_print_thong`

Source: `design/items/leopard_print_thong_item.md` (92% polyester / 8% spandex, machine-repeated rosettes misaligned at the seam, flat elastic already relaxed on day one, one loose thread at the left hip, care label washed past legibility, no brand, no size, no country of manufacture; three-state sun-fade ramp). The doc's look is vague on exactly two things this table settles: **how it is laid out** and **what the print and the label actually look like**.

**Object only. Laid flat, folded once, no body, no wearer, no nudity.**

| Field | Description |
|-------|-------------|
| **silhouette** | Laid flat and folded once across the pouch, front up: a horizontal elastic waistband across the top, a soft rounded triangle of fabric hanging below it where the pouch has collapsed in on itself, and one narrow strap arcing up and to the right from the fold, so the whole thing reads as a squashed keyhole. The fold line cuts a straight crease across the lower third. Nothing is stretched, nothing is filled out — it is an empty garment lying on a surface, and the strap loops loosely rather than hanging taut. |
| **scale_cue** | The waistband is the widest thing in frame and the strap is barely a fifth of that, thin as a shoelace: a garment the size of a folded hand towel, not a pair of trunks. The elastic has visible slack in it — two soft ripples along the band where it no longer pulls — and the strap lies in a wide open loop rather than a tight one, which is what a garment does when there is nothing inside it. |
| **materials_and_cheap_cues** | Thin shiny polyester-spandex jersey with a flat synthetic sheen and no depth: it reflects as a single hard highlight, not as soft fabric. The print is screen-printed onto the cloth, so the rosettes sit on the surface and fade with it rather than being woven in. The waistband is bare flat elastic, stitched down with one narrow row of cheap straight stitching that puckers. The strap has a single overlocked edge, visible as a slightly darker ridge. No lining and no gusset: the print shows through from the inside of the pouch, reversed and paler, which is how you can tell the fabric is one layer and very thin. |
| **colours** | Ground: sandy tan #C9A46A. Rosettes: a broken dark-brown ring #4A3520 around a pale cream centre #EDE0C4, with a true brown-black #2B1E12 where the ring is thickest. Rosette gaps: a lighter tan #DDBE86 where the print stops short. Waistband: a duller, greyer tan #A89070, one shade off the ground because it is a different dye lot. Strap edge: #8A7452. Loose thread at the left hip: off-white #C8C4B8. Sand grains in the seam: #E8D4A0. Crease shadow: #6E5A3C. Care label: dead white #EFEDE6, washed to a flat blank. |
| **contents** | None — it is an empty garment. The strap loop is open, the pouch is collapsed, and the inside of the fabric is visible at the fold showing the print reversed. |
| **decoration** | The print only: machine-repeated leopard rosettes, each a dark ring with a broken, chipped edge and a pale centre, stamped in a repeat about one rosette wide. The repeat is misaligned exactly where it meets the side seam, so the rings step half a rosette out of line and the pattern jogs visibly down one side. At the waistband the print is cut off mid-rosette, leaving a row of brown half-moons against the elastic. Nothing else: no bow, no logo, no motif, no piping, no contrast trim. |
| **condition** | Worn, unwashed and beach-processed: fine sand caught in the waistband stitch line and in the fold crease; the elastic already slack on day one, with two soft ripples and one spot where it has twisted inside its casing; the loose thread at the left hip that hangs and does not pull any further; the top band sun-faded so the tan has gone chalky and the rosettes have softened toward vague brown spots while the lower fold is still bright; a small pilled patch where the strap rubs; the crease across the fold set hard enough to hold itself; the care label washed to a blank with only its stitched border left. |
| **garnish_and_addons** | The loose thread at the left hip and a scatter of sand grains. No price tag, no hangtag, no hanger, no cardboard, no packaging, no sticker, no pin. |
| **palette_anchors** | From `design/worlds/debaucheryville/bohemian_riviera.md:119`: Sand #E8D4A0 (the grains in the seam, the only riviera colour on the object). New to this item: #C9A46A (ground tan), #4A3520 (rosette ring), #2B1E12 (ring core), #EDE0C4 (rosette centre), #DDBE86 (print gap), #A89070 (waistband), #8A7452 (strap edge), #C8C4B8 (thread), #6E5A3C (crease shadow), #EFEDE6 (label). The riviera's own accents — EMTV Magenta #FF1493, Inflatable-Palm Green #32CD32, Space Heater Orange #FF7F32 — must not appear anywhere on the item, or it starts reading as a beach prop instead of a garment from a wire rack. |
| **reads_at_icon_size** | 1. A small folded leopard-print garment: tan ground, brown rings, a bright horizontal elastic band, one thin strap loop. 2. Empty and cheap, not packaged: the strap hangs in an open loop, the cloth is creased flat, the elastic is rippled and slack. 3. Used: sand in the seam, a loose thread, a bleached top band against a still-bright fold, and a label with no writing on it at all. |
| **must_not_look_like** | A woman's bikini bottom or briefs (this has a collapsed front pouch and exactly one narrow back strap — the keyhole silhouette and the single strap are the tell). A bandana, scarf, washcloth or cleaning rag (it has a waistband and a strap; those two parts carry it). A sock, a glove, a hair scrunchie. A leopard-print handbag or pouch (no zip, no clasp, no gusset, no strap handle). A mannequin, hips, legs or any body part wearing it. A clean new item in cellophane with a folded card inside. Anything with a printed brand, size, care symbol or country of origin. Anything with a bow, a charm or a novelty print (no novelty slogans, no joke text). |
| **lettering** | None. The care label is a washed-out blank rectangle: no brand, no size, no fibre content, no care symbols, no country of manufacture, no digits, no glyphs that could be mistaken for a brand. Do not render fake-illegible lettering on it — the label is a shape and a border stitch, and the inside of it is empty. Nothing else on the item prints any word. |

**Continuity notes — thong**
- **The three-state fade ramp is canon and this brief describes state 1 only** (`leopard_print_thong_item.md`, "Degradation Over Time"). State 2: the top band sun-faded across the elastic, rosettes softening toward vague spots. State 3: fully bleached to pale ochre #C9AE7A, rosettes abstract, hip thread grey, elastic surrendered. Same silhouette, same layout, same blank label in all three.
- **The original owner is never established**, and the look must not hint at one: no hair, no lipstick, no jewellery, no perfume stain, no second colour of thread, nothing gendered beyond the garment's own cut. Sand and salt only.
- The item doc's `Sprite Requirements` still say the icon base is **8×4 px**. That predates the icon-art briefs and is a sprite-spec number, so I am not touching it — but a folded garment with a print, a slack elastic band and a blank label cannot read at 8×4. **Flagged for the Asset team / Desk, not decided here** (see the question at the bottom of this file).
- Never rendered on-body beyond the existing 2-pixel waistband sliver; this icon is the inventory object only.

---

## Flags for the moderator (not decided here)

1. **`item_leopard_print_thong` icon base size.** The item doc's `Sprite Requirements` say **8×4 pixels** (`leopard_print_thong_item.md`, "Performance & Assets"). That is a pre-brief number and I have not touched it, but no folded garment with a print, a slack elastic band and a blank label survives 8×4 — at that size the object is a tan rectangle. The other four items in this batch are 64×64 masters. **Recommend the Desk confirm the thong's inventory icon is drawn at the icon standard (64×64 / 128×128 master) and that 8×4 was only ever the in-world waistband sliver.** If the answer is "8×4 stands", the Asset team needs a second, simpler description, and I will write it.
2. **Rhinestone shirt hex count.** My table adds two hexes (#8A6A2F, #8A8A93) to the existing sheet's 13 working colours plus chroma key, which lands exactly on the sheet's own 16-colour cap. If the Asset team wants headroom, drop #8A8A93 first (the thread reads as grey at icon size either way).

## Rulings respected
- Looks only. No item's name, price, stats, effects, rarity, source or story is changed by either table.
- No real place names, no "Europe" / "European" / "Euro-" in either table or in any lettering field. Both lettering fields are **None**.
- No body, no nudity: the shirt is empty and hanging; the thong is folded and empty.
- The thong's binding rule is preserved: nothing in either description establishes, hints at or narrows its previous owner.

---

# Batch 3 draft — `vip_all_access_wristband` ("VIP All-Access Wristband")

Primary writer: Mistral. Reviewer: Kimi (voice) — Deepseek already flagged the lettering/read conflict in `critiques.md`; this draft resolves it the way he specified: `lettering` spells out the printed Bohemian exactly, `reads_at_icon_size` carries the joke with no text at all.

Sources: `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` (`actual_text.bohemian: "Je mi 7!"`, `english: "I'm 7!"` — the physical band prints the Bohemian; the English is the gloss and is never printed), `design/items/vip_wristband_item.md` (thin party-supply plastic, ~1.5 cm wide, cheap plastic snap clasp, per-bro sprite colours #CC0000 / #0000CC / #6600CC, text black on coloured background, "legible on close inspection/zoom"), `dev/asset_team/prompts/vip_all_access_wristband_prompt.md` (existing asset: sunny yellow stock party band with a pattern band of balloons/stars/confetti standing in for the slogan, white snap peg clasp, slightly open loop, clasp at back right). Looks only — name, 30 SOVS price, stats, quest hooks and story untouched. No real place names; the word "Europe" appears nowhere. The icon renders with no readable lettering, so the read must come from shape and colour alone.

---

## 🖼️ Physical description (icon art brief) — `vip_all_access_wristband`

| Field | Description |
-------|-------------|
| **silhouette** | A single thin plastic strip laid as a slightly open loop, seen from a three-quarter front view: the band's near wall rises as a shallow arch, the far wall is a thinner lower arc visible through the gap, and the loop opening is a narrow horizontal lens off-centre to the right. At one end (back right) a small white snap clasp closes the loop: a round peg snapped into a hole, seated slightly crooked so one side of the clasp sits a pixel proud of the other. The strip is narrow and long relative to its height — roughly 1:8 width to loop diameter — never a chunky club band, never a fabric strap. |
| **scale_cue** | The loop's inner opening is about half the loop's outer width, so the band reads as a ring with a real hole, not a solid disc. The clasp adds a small square-ish bump on one side of the loop — the only break in the otherwise even elliptical outline. A strip this narrow, looped, with a peg-and-hole closure, is a party-supply wristband, not a bracelet, keyring or cable tie (the cable tie would have a ratchet head; the keyring a split ring; neither has a printed pattern band). |
| **materials_and_cheap_cues** | Thin glossy injection-moulded plastic, the party-supply-store kind: bright, slightly wrong gloss, never matte, never silicone-rubber, never fabric or velvet. A hard-edged white highlight streak runs along the top edge of the near wall. One edge of the strip curls up a fraction, and the loop is slightly lumpy and warped, as if the plastic was demoulded badly. A mould seam line runs along the outer edge of the band. No woven texture, no stitching, no metal. |
| **colours** | Band (the neutral stock icon, before the per-bro sprite tint): sunny yellow plastic ramp #B87C1C (shade), #E8B430 (mid), #F6D840 (light) — never orange, never red. Printed pattern band along the length: chunky abstract balloons, stars and confetti blocks in red #C0302A, blue #2E5ED0, green #3E9A4E on the yellow ground. Clasp and gloss streaks: cream-white #C9BFA6, #F4EEDC. Outline: dark plum-brown #2B1A2E. Cast shadow: #6E5F72. Per-bro sprite overlay colours (character sprites only, not this icon): red #CC0000, blue #0000CC, purple #6600CC. |
| **contents** | The band is empty — it is an open loop of plastic, nothing inside it, no wrist, no hand. |
| **decoration** | A wide printed pattern band running the full length of the strip between its two edges: chunky childish shapes only — round balloons, five-point stars, confetti blocks — in red, blue and green, evenly spaced, slightly misregistered as if printed on a wobbly party-supply roller. No letters, no words, no numbers, no faces anywhere on the band; the pattern band stands in for the slogan at icon size. The clasp peg is a plain white dot. |
| **condition** | Sold new, already cheap: one curled edge, one warped lump in the loop, the crooked clasp peg, a faint scuff on the outer edge, a tiny stress-whitening mark where the plastic was snapped closed. Not dirty, not faded — the degradation states (fading text, curling edges, crust) are the on-sprite day-based variants, not this icon. |
| **garnish_and_addons** | None. No hangtag, no price sticker, no spare clasp, no packaging — the Shady Wristband Guy sells them loose out of his coat pockets. |
| **palette_anchors** | From the existing asset prompt `dev/asset_team/prompts/vip_all_access_wristband_prompt.md` (yellow ramp #B87C1C / #E8B430 / #F6D840, cream #C9BFA6 / #F4EEDC, motif red #C0302A, blue #2E5ED0, green #3E9A4E, outline #2B1A2E, shadow #6E5F72) — 10 colours, inside the strict 16-colour sprite cap with headroom. Per-bro sprite tints from `vip_wristband_item.md` (#CC0000 / #0000CC / #6600CC) are the character-sprite overlay, not this icon, and are not added to this palette. Square palette anchors (#CFB53B Gothic Gold etc.) deliberately not used: the band is its own object against the square's stone/gold. |
| **reads_at_icon_size** | 1. A small bright loop of thin glossy plastic with a hole in the middle and a white peg clasp: a wristband, not a ring, disc or rubber band. 2. Cheerful and childish, not exclusive: the sunny yellow ground with red/blue/green balloons, stars and confetti blocks reads as a kid's party band from shape and colour alone, with no text needed — never dark, never metallic, never premium-looking. 3. Cheap party-supply plastic: narrow strip, crooked snap clasp, curled edge, hard gloss highlight, warped loop. |
| **must_not_look_like** | A chunky fabric or velvet event wristband (the Velvet Wristband equipment item is a different object — thicker, burgundy, barbed clasp). A silicone rubber LIVESTRONG-style band (too thick, no pattern band). A metal or woven bracelet, a keyring, a cable tie, a rubber band. Anything dark, metallic, gold or premium — no foil, no foil stamp, no embossed "VIP" block. Anything with readable letters, numbers or a logo at any size — the pattern band must stay abstract shapes. A wrist or hand wearing it. Three bands at once (the icon is the single stock band; the per-bro colours live on the character sprites). |
| **lettering** | Printed on the band, spelled out exactly as canon gives it: **Je mi 7!** — black playful font on the coloured band, legible only on close inspection/zoom per `vip_wristband_item.md` (the English "I'm 7!" is the gloss and is never printed). At icon size the words must NOT carry the read: they blur into the printed pattern band, and the balloon/star/confetti shapes are what survives. |

---

### Continuity notes for the integrator
- Name, 30 SOVS price (90 for three), stats (+2 Bravado etc.), quest hooks and the Velvet Curtain Club payoff untouched — looks only, per rpac.
- The lettering/read conflict flagged in `critiques.md` is resolved as Deepseek specified: `lettering` carries **Je mi 7!** verbatim (Bohemian only), and `reads_at_icon_size` carries the joke with zero dependence on text.
- The existing asset prompt already matches this layout (yellow stock band, confetti pattern band, white snap clasp, open loop, clasp back right); this table pins the same decisions in the standing 12-field format so the Asset team can regenerate or QC against it.
- No real place names; "Europe"/"European" appear nowhere. DEBAUCHERYVILLE is never printed on this object — the band carries only the birthday slogan.

