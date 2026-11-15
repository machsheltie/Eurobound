# Item physical descriptions batch 2 — Absinthe Arcade and taproom items (Deepseek)

Scope: items 4–7 of the brief. `item_broken_symbol_game_boy` / `aa_broken_symbol_handheld`, `velvet_wristband_vip`, `already_spent_credit`, `cracked_mirror_shard`. Format: the 12-field `## Physical description (icon art brief)` adopted as standing in Desk rpac-q1. Looks only — no name, price, effect or story changes. Reviewer for this section: **Mistral** (canon + gameplay read), with **Aion** on the audience read.

Two open decisions are marked `[QUESTION FOR AUTHOR]` inline (the handheld's symbol, and the wristband's `silhouette` orientation). Everything else is written to be paintable without another ruling.

---

## 4. `item_broken_symbol_game_boy` / `aa_broken_symbol_handheld` — Broken Handheld with Weird Symbols

### [QUESTION FOR AUTHOR] Which symbol pulses on the screen

Canon (`absinthe_arcade_items.json:121`, `key_items.json:315`) says only "unfamiliar musical symbols". The Asset team's ref used a **treble clef**. That is the single most recognisable music symbol on the planet — a shop logo, a tattoo, a phone-app icon. It makes "unfamiliar" false on sight, and the unreadable clue is the point of the item (its future use is `music_symbol_clue` in Sinfonia).

- **Option A (recommended): a medieval neume.** One chunky square lozenge with a single hooked tail, one fainter lozenge behind it, then the pulse repeats. Unfamiliar to players and to anyone who reads music; it also points at Sinfonia's old-music pretension rather than a nursery-school music book.
- **Option B: an invented glyph.** Three filled note-heads stacked on one diagonal beam, belonging to no notation system that exists. Literally unfamiliar to every player, and impossible to mistake for a brand.

If the author keeps the treble clef, it is consistent with what shipped and I will write it as canon-clef; I am flagging it because it argues with the item's own word.

### silhouette

A chunky rectangular handheld, roughly 3:4 width to height and thick enough to read as a brick rather than a slab — a rounded plastic body with one big square dead screen filling the upper half, a plus-shaped directional pad in the lower left, two fat round buttons lower right. One lower corner has a shallow round dent that flattens the corner curve. A short blunt tail of body below the buttons. Reads as a toy console, not a phone.

### scale_cue

The plus-shaped pad and the big square dead screen are the two shapes that survive an empty 128 px frame. The duct tape patch, the dent and the two stickers are third-read extras, not silhouette. At the in-game 24–32 px the read is a brick with a black window.

### materials_and_cheap_cues

Moulded ABS with a smooth soft surface — the plastic is solid and injection-moulded, no texture, no grain. Sun-yellowed grey: the grey is legible underneath the yellow, the way an old arcade cabinet yellows and nothing else does. One flat grey duct-tape patch sits fully inside the body outline with clean straight edges, bubbled at one end. Two flat paper stickers, both creased across the middle, one peeling at a corner. The screen is flat dead glass, matte, no glare, no glow except the one symbol.

### colours

- Body: sun-yellowed grey `#C7C1A8`.
- Body shadow (underside, dent interior): grey `#9A947F`.
- Dead screen: near-black `#101010`.
- Pulsing symbol: toxic green `#39FF14` (anchor).
- Screen cracks: dark plum `#2B1A2E`.
- Duct tape: grey `#8A8A8A` with a hard lighter edge `#B4B4B4`.
- Sticker A: sun-bleached bubblegum pink `#E39AAC`, carrying a crude pixel-invader silhouette in worn grass green `#2E8C1B`.
- Sticker B: small round faded silver `#C0C0C8` with the arcade's angular A/hourglass emblem stamped in worn black `#0A0A0A`.
- Empty battery bay (see `condition`): recessed flat grey `#6E6A5C` interior, no metal contacts painted.

### contents

Nothing — the body is closed except the empty bay listed under `condition`.

### decoration

Two flat stickers and one duct-tape patch. No lettering on any of them: both stickers are pictographic. No brand mark, no logo, no speaker slats, no ornamental trim anywhere on the shell.

### condition

Sun-yellowed all over, worse in the recessed grip areas. Three bold crack lines crossing the screen from one impact. One shallow round dent in a lower corner. Duct tape patch lifted and grey at one end. Sticker A creased and peeling at one corner; sticker B worn nearly blank. **Battery cover missing** — canon (`absinthe_arcade_items.json`, `visual.details`) says the cover is gone, so the visible bottom edge carries an empty square battery bay: a flat recessed rectangle, straight sides, plainly empty, no springs, no wires, nothing loose.

CHANGED (was: "closed back, no battery bay" in the R3 ref): canon's own visual field names a missing battery cover, and it is the only wear on the object a player can see without turning it over. Drawn as one flat recessed rectangle so it cannot fail the A3 no-thin-parts rule.
CHANGED (was: "foreign stickers" unspecified, ref showed tape only): two flat pictographic stickers, so the arcade's own ink and a claw-prize freebie are visible instead of an unexplained patch.

### garnish_and_addons

None. No wrist strap, no carry case, no cartridge, no dangling cord.

### palette_anchors

Inherited from the arcade palette (`design/worlds/debaucheryville/absinthearcade.md:44`): `#39FF14` toxic green, `#0A0A0A`. Inherited from `design/worlds/debaucheryville/core/absinthe_arcade_core.json:125`: `#C9A45D` — not used on this item and deliberately so; the only warm brass in the Arcade is the tokens. New to this item: `#C7C1A8`, `#9A947F`, `#101010`, `#E39AAC`, `#2E8C1B`, `#8A8A8A`, `#6E6A5C`.

### reads_at_icon_size (128 px blind checklist)

- [ ] A thick toy handheld — rounded brick, big black screen, plus pad, two round buttons. Not a phone, not a tablet.
- [ ] One hard green glyph on the dead screen, unmistakably a symbol and not a menu, a health bar or a game.
- [ ] Old: yellowed body, cracked screen, lifted tape, empty battery bay.

### must_not_look_like

- A working console — the screen is dead black with cracks through it, one glyph and nothing else.
- A recognisable branded handheld — no wordmark, no logo, no trademark button-colour pattern, no speaker-grille slats.
- A phone or a tablet — physical plus pad, two round buttons, no touchscreen slab.
- Anything cute — no face, no googly eyes, no character plastic, no decal of an animal.

### lettering

None. Both stickers are pictographic; the screen shows one symbol, not words; the shell carries no brand, model or instruction text.

---

## 5. `velvet_wristband_vip` — Velvet Wristband (VIP Access)

CONFIRM OR CORRECT: keep the burgundy velvet, the two hard sheen bands, the barbed one-way clasp, the hand-trimmed tail, the frayed edge and the grubby worn section. Correct the wear, foil and sheen below. All wear is flat colour areas — no threads, no fuzz, no noise.

### silhouette

A flattened oval loop of wide flat strap, wider than it is thick — it lies on its side at a three-quarter view, permanently creased flat like a band that has not been off a wrist in four days. A chunky solid clasp block sits on the band, and a short blunt tail the full band width sticks out just past it. No buckle, no buckle holes, no jewellery geometry: it reads as an event band, not a bracelet.

### scale_cue

The oval hole and the clasp block are the two reads in an empty frame; the tail past the clasp is the third. At 32 px the loop must still be an oval loop of flat strap with a lump on it.

### materials_and_cheap_cues

Matte crushed velvet with the nap crushed permanently flat in the pinch marks of a thumb and forefinger. The sheen is not nap — it is exactly two hard-edged lighter bands running the length of the strap, each a flat shape with stepped edges. The clasp is chunky solid grey-white plastic with bold sawtooth barbs cast into it: this band cannot come off without scissors, which is the entire point. Gold foil is thin, dull and half gone. A flat glossy residue patch beside the clasp reads as sticky, not wet.

### colours

- Velvet base: burgundy `#7E1E3E`.
- Velvet shadow: `#4A0E22`.
- Sheen band: `#D86E8E` — two bands only, hard edges.
- Ridge highlight: `#B44E6E`.
- Foil: dull gold `#C9A227`, shadow `#8A6E14`, worn through to backing grey `#A89A94`.
- Clasp: cool grey-white `#E0E6EA`.
- Grime: `#5E4A44`; stains: `#3A2E2A`.
- Outline: dark plum `#2B1A2E`.

### contents

None — it is a band.

### decoration

Exactly one small blocky gold foil mark, hard straight edges, no letters: a short bar and a broke-off stub of a second shape, half rubbed back to the woven backing. Nothing else printed, sewn, stamped or embroidered.

### condition

Four days on one wrist, in flat areas: a few lighter bald patches where the velvet nap is worn through, one flat paler strip along a lower edge where it is frayed (a strip, not threads), broad hard-edged brown stains, one darker stain, a sticky residue patch beside the clasp, a crease line down the whole loop from being pressed flat. Foil worn to a stub. Tail cut unevenly and forever slightly too short.

CHANGED (was: sheen described as "two sheen bands" without form): each band is now a hard-edged flat shape with stepped edges. Soft nap or a gradient turns velvet into satin and the band into jewellery.
CHANGED (was: "small blocky illegible pixel shape"): specified as a bar plus a broke-off stub, no letters — the doc calls the foil canonically illegible, so any readable "VIP" would contradict it.

### garnish_and_addons

None. No bead, no charm, no rivet, no fabric tag.

### palette_anchors

Taken from the item's own palette block (`Assets/Graphics/items/velvet-wristband-vip.md:60`): `#7E1E3E`, `#4A0E22`, `#B44E6E`, `#D86E8E`, `#C9A227`, `#8A6E14`, `#5E4A44`, `#3A2E2A`, `#A89A94`, `#E0E6EA`, `#2B1A2E`. Location-side anchors available and not used: `design/worlds/debaucheryville/velvet_curtain_club.md:284` deep burgundy `#800020` and gold `#FFD700`. Both are brighter and richer than these hexes; using them would make a 40-SOVS band look premium. New to this item: none.

### reads_at_icon_size (128 px blind checklist)

- [ ] A wide flat strap in a loop with a lumpy clasp and a stub of tail past it — an event band, never a bracelet, bangle or ring.
- [ ] Burgundy with two hard pale bands along it, not a gradient — flat strap, flat finish.
- [ ] Used: stains, fuzz-flat bald patches, a paler frayed edge strip, a rubbed foil stub.

### must_not_look_like

- Jewellery — no buckle, no clasp holes, no polished shine, no gemstone, no metal band.
- A bangle, cuff, bracelet or scrunchie — flat strap with a tail and a plastic block, not a ring.
- A pet collar, a lanyard or a hospital band — cloth velvet, wide, with a foil mark.
- A clean, fresh, newly-bought band — that variant exists separately; this icon is the four-days-in state.
- A stack of bands — one band, one loop, nothing layered on the wrist (no wrist in frame at all).

### lettering

None. The foil mark is canonically illegible: a bar and a stub, no letters.

---

## 6. `already_spent_credit` — Already-Spent Credit

CONFIRM OR CORRECT: brass, milled rim dots, groove ring, flat grime, one gouge and engraved `CREDIT 00` all fit canon and the joke. Keep all of them. Two additions, one correction.

### silhouette

A single heavy round token, seen almost face-on with a hair of tilt so the rim reads as thickness — a thick bevelled disc, not a coin-thin washer. Milled dots dot the rim all the way round, a shallow groove ring sits inside the rim on each face, and one edge has a bright flattened spot where a machine's coin return has kicked it back a few hundred times. Slight irregularity at one point on the rim: a flat bite out of the circle, metal pushed rather than cut.

### scale_cue

One disc. At 128 px the read is: circular outline, dotted rim, a groove ring, two short words stacked in the middle. Nothing else in frame — no slot, no hand, no machine.

### materials_and_cheap_cues

Brass-plated zinc: brass on the high faces, dull grey zinc showing through at the rim's worn flats and inside the stamped letters. The lettering is stamped and recessed, not printed — you can see the flat bottom of each groove. Grime is flat: green verdigris bloomed into the groove ring, brown smear across one side, both hard-edged, no speckle, no fuzz.

### colours

- Brass face: `#C9A45D` (anchor).
- Brass highlight: `#E7D7B7` (anchor).
- Brass shadow: `#8A6E14`.
- Bare zinc wear: `#A89A94`.
- Verdigris: `#0B6B50` (anchor).
- Brown grime: `#3A2E2A`.
- Stamped lettering: `#2A2118` in the grooves, with bare metal flecks `#E7D7B7` on the worn stroke tops.
- Rim UV paint remnant: toxic green `#39FF14` (anchor), two flecks in the groove only.

### contents

Nothing — it is a token.

### decoration

Front face: `CREDIT 00` only. Back face: the Absinthe Arcade's angular A/hourglass emblem, stamped, worn nearly smooth — the same emblem as every other token in the building, which is the joke the bros cannot see. Rim: milled dots and the shallow groove ring.

CHANGED (was: no reverse face): canon (`absinthe_arcade_items.json`, the arcade token) gives the Arcade an angular A/hourglass emblem, so this token is visibly the same currency as the one that still works.
CHANGED (was: no rim paint): the canon token rim glows green under UV, so two flecks of green remain in the groove — the only thing on this token still doing its job.

### condition

Spent many times over: rim flattening, one pushed-in bite, brass worn off the highest dots and the groove edge to bare zinc, verdigris in the groove, a hard-edged brown smear, lettering grooves choked with grime with only the raised strokes still catching light, one flat gouge across the rim.

### garnish_and_addons

None. No hole, no ring, no chain, no keyring loop. It is a token, not a pendant.

### palette_anchors

Inherited from `design/worlds/debaucheryville/core/absinthe_arcade_core.json:125-128`: `#C9A45D`, `#E7D7B7`, `#0B6B50`. Inherited from `design/worlds/debaucheryville/absinthearcade.md:44`: `#39FF14`. New to this item: `#8A6E14` (brass shadow), `#A89A94` (bare zinc), `#2A2118` (stamped-letter grime).

### reads_at_icon_size (128 px blind checklist)

- [ ] A chunky round token, dotted rim, groove ring — the same family as every other arcade token at a glance.
- [ ] `CREDIT 00` legible as two short stacked words in the centre, and as words, not a decorative mark.
- [ ] Worn brass with green grime: an object that has been through a slot, not a mint coin.

### must_not_look_like

- A poker chip or a casino chip — no centre inlay disc, no card suits, no edge stripes.
- A generic currency coin — no portrait, no wreath, no numerals other than `00`.
- A medallion, pendant or charm — no loop, no hole, no ribbon.
- A chocolate coin — this is scuffed metal with grime in the grooves, and the lettering is recessed.
- A new token — brass is worn to grey at every high point.

### lettering

Stamped, recessed, uppercase, compressed heavy sans (Impact-adjacent) in `#2A2118` with bare-metal flecks on the stroke tops. Two lines, stacked and centred:
- `CREDIT`
- `00`
No other words on either face. The reverse carries the emblem and no lettering.

---

## 7. `cracked_mirror_shard` — Cracked Mirror Shard

CONFIRM OR CORRECT: only the name is canon (Mirror Chad drop, `the_absinthium_taproom.md:403`). Keep the long pointed shard, the jagged 14-point outline, the flat silvery reflection bands, the bold cracks from one impact point, the grime and the flat fingerprint smudge. Keep the coffee ring deleted. One colour correction.

### silhouette

One long pointed shard, roughly 1:2 width to height, jagged all the way round on a 14-point outline, tapering to a genuinely sharp point at the top and a broken blunt corner at the base. Thick: two raw edges show real slab thickness so it cannot be read as paper or foil. It stands more than it lies.

### scale_cue

The pointed wedge plus the burst of bold cracks fanning from the impact point are the two reads in an empty frame. This ships as a 24×24 in-game PNG, so the shape must still be a spike at 24 px: one wedge, one crack star, no interior detail.

### materials_and_cheap_cues

Mirror glass on a steel backing: the front face is one flat silvery surface carrying flat bands of reflection, and the raw broken edges show the steel as a solid grey band with a lighter chipped line. Nothing transparent, nothing faceted, no gradient — this is a splinter off a cheap mirror that was already mounted on something.

### colours

- Mist silver face: `#C0C0C0` (anchor).
- Bright reflection band: `#F2F2F2`.
- Second face tone (dull band): `#8F8F8F`.
- Reflected absinthe glow, one narrow band across the lower third: `#7FFF00` (anchor).
- Raw edge steel: `#4A4A4A`, chipped lighter line `#B4B4B4`.
- Cracks: dark plum `#2B1A2E`, bold and hard-edged, fanning from one impact point near the upper third.
- Grime: `#3A2E2A` along one raw edge and in the fingerprint smudge.
- Deep void black in the deepest crack: `#0D0D0D` (anchor).

CHANGED (was: "warm peach-orange reflected colour in the lower-right corner"): a peach patch reads as reflected skin, and the ref notes are explicit that nothing of Mirror Chad's look may appear. Corrected to the taproom's own absinthe green, which is what the room actually throws back at the glass.
CHANGED (was: "flat brown grime and a coffee ring", ring deleted in R2): CONFIRMED deleted. A coffee ring makes it a shard off a table, not off a wall in a room full of mirrors.

### contents

Nothing — it is a piece of glass.

### decoration

None. No etching, no frame, no bevel, no foil backing, no lettering. The two hard silver bands and the crack star are the whole surface.

### condition

Cracked from one impact point, four bold lines running to the edges without reaching them. Point chipped at the tip with a pale chip line. One raw edge ground-in with grey grime. One flat fingerprint smudge in the dull band. No dust speckle, no shatter crumbs, no fractal fine cracking.

### garnish_and_addons

None. No blood, no thread, no tape, no tag.

### palette_anchors

Inherited from `design/worlds/debaucheryville/the_absinthium_taproom.md:108`: `#7FFF00` absinthe green, `#0D0D0D` void black, `#C0C0C0` mist silver. New to this item: `#F2F2F2`, `#8F8F8F`, `#4A4A4A`, `#2B1A2E` (crack plum), `#B4B4B4`.

### reads_at_icon_size (128 px blind checklist)

- [ ] A sharp pointed piece of broken glass, thick edges — not a gem, not a blade, not paper.
- [ ] Silvered front with a hard bright band, and bold dark cracks in a star from one point.
- [ ] Cold and proprietary-of-the-taproom: mist silver, one green band, no warm colour anywhere.

### must_not_look_like

- A crystal, gem or diamond — no facets, no translucency, no sparkle, no glow.
- A knife blade or a dagger — no handle, no grind lines, no point-forward symmetry.
- Any reflection of a person — no face, no eye, no silhouette, no skin tone anywhere on it.
- A window pane or a hand mirror — one shard, no frame, no mount.
- A magic crystal powering anything — no rune, no rune-adjacent scratch, no symbol.

### lettering

None.


---

**Header correction:** the intro above names two inline `[QUESTION FOR AUTHOR]` items. Only one exists — the handheld's symbol (§4). The wristband (§5) has no open question: the clasp, tail, foil and wear are all settled from the item's own doc and palette block.
