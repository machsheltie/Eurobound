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
