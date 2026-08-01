# Haute Couture Haberdashery - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Haute Couture Haberdashery — the Imperial Square tailoring house where the mirrors are positioned to catch your worst angle, the lighting is calibrated to make your current clothes look worse, and the head tailor tells you the complete truth about the price twice so nobody can later claim they were unclear. It is an equipment shop, a four-tier client-status ladder, the "HOUSE OF NEEDLES" of Hamstradamus's prophecy, and the home of a sealed vitrine containing one object that is not for sale at any number.

**Location ID:** `sinfonia_imperialsquare_haute_couture_01`
**Theme:** Luxury retail psychology — a genuinely excellent shop whose purchase experience is engineered to make you feel you don't deserve it until you pay
**Zone:** Imperial Square, Grand Entrance District
**Hours:** 10 AM - 7 PM (fashion keeps civilized hours; the shop is empty of staff after 7:01 PM, which is what makes PATH B possible)
**Primary Function:** Equipment shop / formal wear & accessories — Assessment Protocol, fitting-room mechanic, Valued Client tiers, "Nothing Is Getting Through" quest hub (both paths), three selfie variants

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Velvet Black | #1A1A1A | Alcove walls, vitrine velvet, garment boxes, night interiors |
| Gold Thread | #CFB53B | Signage lettering, beading, cufflinks, trim, the Coin |
| Cream Marble | #FFF8E7 | Showroom floors, walls, panelling, main light key |
| Judgment Gray | #808080 | Fitting-room lighting cast, Night Porter's tunic, unflattering shadow ramp |
| Presentation Burgundy | #6B0F1A | The presentation sleeve, ticket book, private-room carpet (derived — not in profile, added for the PATH A handover prop) |
| Champagne Pale | #EFE3B8 | Coupe contents, bubble particles, warm chandelier bloom (derived accent) |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/haute_couture_haberdashery/
├── environment/
│   ├── haute_couture_tileset.png
│   └── haute_couture_landmarks.png
├── npcs/
│   ├── monsieur_aiguille.png
│   ├── night_porter.png
│   └── haute_couture_npcs.png
├── objects/
│   └── haute_couture_equipment.png
├── effects/
│   └── haute_couture_effects.png
└── ui/
    └── haute_couture_ui.png
```

---

## 🏛️ Sprite Sheet 1: Temple of Textiles Tileset
**File:** `haute_couture_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #FFF8E7 (Cream Marble), #1A1A1A (Velvet Black), #CFB53B (Gold Thread), #808080 (Judgment Gray)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cream Marble | (0, 0) | 32x32 | Showroom base |
| Marble Gold-Vein | (32, 0) | 32x32 | Feature variant |
| Marble Inlay Medallion | (64, 0) | 32x32 | Centre-of-room ornament |
| Showroom Border Tile | (96, 0) | 32x32 | Perimeter run |
| Fitting Room Parquet | (128, 0) | 32x32 | Warmer, quieter underfoot |
| Alcove Black Velvet Floor | (160, 0) | 32x32 | Accessories alcove |
| Workshop Boards | (192, 0) | 32x32 | Behind the glass wall |
| Imperial Square Paving | (224, 0) | 32x32 | Exterior street |
| Private Room Carpet | (256, 0) | 32x32 | Valued Client, burgundy |
| Carpet Gold Edge | (288, 0) | 32x32 | Runner border |

### Wall Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Showroom Cream Panel | (0, 32) | 32x64 | Standard interior wall |
| Panel With Gold Beading | (32, 32) | 32x64 | Feature wall |
| Mirror Wall Segment | (64, 32) | 32x64 | Showroom reflective run |
| Fitting Room Mirror Full | (96, 32) | 32x64 | Floor-to-ceiling, no escape |
| Velvet Black Alcove Wall | (128, 32) | 32x64 | Accessories alcove |
| Workshop Brick Whitewash | (160, 32) | 32x64 | Behind the glass |
| Glass Wall Mullion | (192, 32) | 16x64 | Workshop framing |
| Glass Wall Pane | (208, 32) | 32x64 | Semi-transparent, tailors visible |
| Exterior Stone Ashlar | (240, 32) | 32x64 | Façade masonry |
| Wainscot Cap Strip | (272, 32) | 32x16 | Panel top rail |
| Cornice Gilt Strip | (272, 48) | 32x16 | Ceiling trim |
| Skirting Board | (272, 64) | 32x16 | Floor trim |

### Doors & Passages:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glass Entry Door With Brass Handle | (0, 96) | 48x80 | The judgmental bell hangs here |
| Door Bell Fixture | (48, 96) | 16x24 | Two tones: disappointed / welcoming |
| Showroom Arch | (64, 96) | 64x96 | Main floor threshold |
| Fitting Room Curtain Closed | (128, 96) | 32x80 | Public assessment zone |
| Fitting Room Curtain Open | (160, 96) | 32x80 | Occupied state |
| Private Fitting Door | (192, 96) | 32x80 | Valued Client only |
| Workshop Glass Door | (224, 96) | 32x80 | "We can alter ANYTHING" |
| Service Door | (256, 96) | 32x80 | The Night Porter's entrance and exit |
| Torch Hook By Service Door | (288, 96) | 16x24 | Empty during the day, examinable forever |
| Step At Service Door | (288, 120) | 32x16 | "everyone minds the step except me" |

### Exterior Façade & Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Storefront Base | (0, 192) | 192x128 | Ashlar stone, gold-lettered fascia |
| Display Window Left | (192, 192) | 96x128 | Mannequins posed dramatically |
| Display Window Right | (288, 192) | 96x128 | Changed weekly (Thursdays) |
| Main Sign "Haute Couture Haberdashery — Bespoke Excellence Since 1822" | (384, 192) | 256x40 | Primary fascia |
| Window Decal "By Appointment Preferred. Walk-Ins Tolerated." | (384, 232) | 256x32 | Gold on glass |
| Brass Plate Hours "10 AM – 7 PM" | (384, 264) | 96x24 | Fashion keeps civilized hours |
| Awning, Black With Gold Piping | (480, 264) | 160x32 | Exterior shade |
| Pavement Planters | (640, 192) | 64x64 | Clipped, symmetrical |
| Brass Boot Scraper | (704, 192) | 32x24 | Wipe your feet |
| Closed Sign (7 PM) | (736, 192) | 64x32 | Turned by Aiguille personally |
| Window Change Placard (Thursdays) | (640, 256) | 96x24 | He does the mannequins himself |
| Night Façade Overlay (Dark, Moonlit) | (800, 192) | 192x128 | PATH B exterior state |

### Furniture & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Velvet Waiting Bench | (0, 320) | 96x48 | For those waiting to be judged |
| Velvet Stool | (96, 320) | 32x40 | Fitting-room seat |
| Champagne Trolley | (128, 320) | 48x48 | Two grades, one visible |
| Accessory Velvet Pillow | (176, 320) | 32x24 | Where the profit margin lives |
| Display Plinth Empty | (208, 320) | 32x48 | Showroom mannequin base |
| Display Plinth Labeled "3" | (240, 320) | 32x48 | Post-quest state; never attributed |
| Cash Counter | (272, 320) | 96x48 | Where the ticket is written |
| Ticket Book & Pen | (368, 320) | 32x24 | The true price, stated twice |
| Rack Of Suits | (400, 320) | 96x64 | Showroom stock |
| Bolt-Of-Cloth Shelf | (496, 320) | 96x64 | Handled with reverence |
| Pincushion & Chalk Tray | (592, 320) | 32x24 | Workshop hours only |
| Tailor's Dummy | (624, 320) | 32x64 | Aiguille's own suit lives here overnight |
| Sewing Machine, Industrial | (656, 320) | 48x48 | Visible through glass |
| Steam Press | (704, 320) | 48x48 | Workshop |
| Fabric Bolt Stack | (752, 320) | 64x48 | Midnight worsted among them |
| Walnut Chair | (816, 320) | 32x48 | "Somebody has moved the walnut chair again." |
| Office Carpet Patch | (848, 320) | 64x32 | "one carpet, and the carpet is in the office" |

### Backdrop / Parallax Layers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Imperial Square Backdrop Far | (0, 384) | 512x128 | Slow parallax |
| Imperial Square Backdrop Near | (512, 384) | 384x128 | Fast parallax |
| Chandelier Light Gradient Overlay | (896, 384) | 128x128 | Interior additive key |

### Technical Notes:
- Fitting Room Mirror Full and Mirror Wall Segment both need a matching low-alpha reflection layer authored on a separate PSD group — the reflection is a runtime-composited sprite, not baked art
- The Judgment Gray ramp is applied *only* inside fitting rooms; the showroom uses a warm cream ramp, and the difference must be visible in a side-by-side crop
- Night Façade Overlay is a full-tint replacement, not an additive pass — PATH B needs the gold lettering to go cold
- Display Plinth Empty and Display Plinth Labeled "3" are pixel-identical apart from the numeral; the joke is that nothing else changed
- Regions x912–1024 (y320–384) and x304–384 (y96–192) are reserved padding

---

## 💎 Sprite Sheet 2: Mirrors, Vitrine & Display Landmarks
**File:** `haute_couture_landmarks.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #CFB53B (Gold Thread), #1A1A1A (Velvet Black), #FFF8E7 (Cream Marble), #6B0F1A (Presentation Burgundy)

### Mirrors & Fitting Rooms:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Three-Way Mirror (Selfie Spot) | (0, 0) | 128x160 | Every angle, no escape |
| Fitting Room Interior, Public | (128, 0) | 96x160 | Assessment zone |
| Fitting Room Interior, Private | (224, 0) | 96x160 | Valued Client — slightly less humiliating |
| Interrogation Lighting Overlay | (320, 0) | 96x160 | Reveals every flaw (intentional) |
| Summon Bell | (416, 0) | 24x32 | He was already watching |
| Mirror Reflection Ghost Layer | (440, 0) | 72x160 | Runtime-composited player reflection |

### The Locked Vitrine — *Objets d'Héritage*:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Vitrine Sealed, Coin Present | (0, 160) | 64x96 | Own spotlight, black velvet, own key |
| Vitrine Open, Key Turned | (64, 160) | 64x96 | PATH A only — he opens it himself |
| Vitrine Empty, Placard Retained | (128, 160) | 64x96 | Post-quest, both paths, permanently |
| Gold Circle Coin, Seal Unbroken | (192, 160) | 32x32 | `item_gold_circle_coin` — gold foil, molded 1990 |
| Hand-Set Placard | (192, 192) | 96x32 | "It Is Not For Sale. It Is For Aspiration." |
| Burgundy Presentation Sleeve | (192, 224) | 48x32 | Keepable, worthless, French care instruction |
| The Separate Key | (240, 224) | 24x24 | "It does not touch them." |
| Black Velvet Bed | (264, 224) | 24x32 | The Coin's resting shape, still impressed |
| Vitrine Spotlight Pool | (288, 160) | 64x96 | Stays lit after the case empties |

### Showroom Displays:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mannequin, Opera Occasion | (352, 160) | 48x96 | Organised by occasion |
| Mannequin, Ball Occasion | (400, 160) | 48x96 | Ball |
| Mannequin, Formal Dining | (448, 160) | 48x96 | Formal Dining |
| Mannequin, "Being Seen" | (352, 256) | 48x96 | The fourth occasion |
| Spotlit Display Case, Museum-Style | (400, 256) | 64x64 | Each piece lit like an artifact |
| Occasion Placard Set | (464, 256) | 48x32 | Category labels |
| Accessories Alcove Pillow Row | (464, 288) | 48x32 | Velvet, add-on sales |
| Champagne Coupe Service | (400, 320) | 64x32 | You'll need it when you see prices |
| No Price Tags Detail | (464, 320) | 48x24 | If you have to ask |

### The Alteration Workshop (Visible):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glass Wall View, Tailors At Work | (0, 256) | 192x96 | Subtle pressure: see how much work goes into this |
| Tailor At Machine, Silhouette A | (192, 256) | 48x96 | Background craft |
| Tailor At Machine, Silhouette B | (240, 256) | 48x96 | Background craft |
| Hem In Progress Detail | (288, 256) | 32x32 | Close-up prop |
| Chalk Marks On Cloth | (288, 288) | 32x32 | Aiguille's hand |
| Aiguille's Own Suit On Form | (320, 256) | 32x96 | Changed daily; the shop's best argument |

### Trim & Reflection Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marble Floor Reflection Strip | (0, 352) | 192x32 | Multiply-blend floor sheen |
| Chandelier Crystal Row | (192, 352) | 160x32 | Tileable overhead |
| Gold Thread Trim Strip | (352, 352) | 160x32 | Universal edging |

### Technical Notes:
- **The vitrine spotlight never turns off.** Post-quest the case is empty, the velvet keeps the Coin's impression, the placard stays, and the light stays on. This is authored art, not a runtime toggle
- Vitrine Sealed / Open / Empty must register as one object at three moments — identical framing, identical spotlight geometry
- The Three-Way Mirror is the selfie spot: composition must accommodate three reflected player poses plus the "old clothes in the corner" prop for the Transformation variant
- Mannequin sprites are reused as the PATH B pose reference; the bro mannequin poses on Sheet 5 must silhouette-match these four at plinth scale

---

## 🪡 Sprite Sheet 3: Monsieur Aiguille — The Head Tailor
**File:** `monsieur_aiguille.png`
**Dimensions:** 384x288 pixels
**Color Palette:** #1A1A1A (Three-piece suit), #FFF8E7 (Linen/marble key), #CFB53B (Watch chain, pin), #6B0F1A (Sleeve, ticket book)

### Assessment & Craft States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| idle_assess | (0, 0) | 48x96 | Hands lightly clasped, watching the door (35%) |
| assessing_gaze A | (48, 0) | 48x96 | The two-second look, frame 1 — *concerned*, never contemptuous |
| assessing_gaze B | (96, 0) | 48x96 | Frame 2, complete. Applied to everyone |
| circling A | (144, 0) | 48x96 | "The shoulders..." |
| circling B | (192, 0) | 48x96 | "...the posture..." |
| circling C | (240, 0) | 48x96 | "...the fabric choices..." |
| measuring | (288, 0) | 48x96 | Tape off the neck, measurement taken |
| chalk_mark | (336, 0) | 48x96 | The mark made; waistcoat chalk |

### Service & Transaction States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| fabric_handle | (0, 96) | 48x96 | Both hands, entirely absorbed — the one emotional subject |
| slight_approval | (48, 96) | 48x96 | The rare genuine nod ("A man of focus. This way.") |
| ellipsis_hold | (96, 96) | 48x96 | The pause before the honest word; the client fills it |
| ticket_write | (144, 96) | 48x96 | Restating the true price at normal volume |
| champagne_offer | (192, 96) | 48x96 | Well-dressed arrival: "You clearly understand quality." |
| sigh_comply | (240, 96) | 48x96 | Rush tailoring, +50%; he sighs, and complies |
| consultation | (288, 96) | 48x96 | €100 wardrobe advice, gesturing at synergies |
| lock_check | (336, 96) | 48x96 | Two fingers on the vitrine lock, 7 PM, every night, every game state |

### The Vitrine & Quest States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| vitrine_unlock A | (0, 192) | 48x96 | The separate key, turned |
| vitrine_unlock B | (48, 192) | 48x96 | **The two-handed lift** — different register from everything else he does |
| vitrine_unlock C | (96, 192) | 48x96 | Seating the Coin in the sleeve before he will let go |
| errand_brief | (144, 192) | 48x96 | The 1994 hem; enormous, entirely sincere weight |
| named_greeting | (192, 192) | 48x96 | PATH A, warm, uses their names — the actual reward |
| valued_clients_pause | (240, 192) | 48x96 | PATH B: "Ah. The Valued Clients." One second too long |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Measuring Tape Detail, Worn Soft | (288, 192) | 48x24 | Numbers gone at the eighty-centimetre mark |
| Tailor's Chalk & Pincushion | (288, 216) | 48x24 | Waistcoat pocket; left wrist in workshop hours |
| Reading Glasses (Hems Only) | (288, 240) | 48x24 | Used for nothing else |
| Three-Piece Suit Fabric Detail | (288, 264) | 48x24 | Made by him, altered by him |
| Two-Handed Lift Close-Up | (336, 192) | 48x48 | Hero framing for the screenshot moment |
| Assessing Eyes Close-Up | (336, 240) | 48x48 | Reads as a specialist reading your chart |

### Animation Timing:
- idle_assess: 2fps, loop, minimal movement — he stands the way he would like everyone to stand
- assessing_gaze: 2 frames over 2.0 seconds, single play, fires on every first entry of a new outfit state
- circling A→B→C: 3fps, single play, one frame per named fragment, synced to dialogue
- measuring → chalk_mark: 4fps, single play
- ticket_write: 3fps, 2.0s single play; the restated price lands mid-write
- vitrine_unlock A→B→C: 2fps, single play, 4.5s total — deliberately slower than every other animation in the shop
- lock_check: 1.0s single play, fires at 7 PM in every game state

### Character Notes:
- **He must never sneer.** The whole character collapses if he plays as a snob. The face reads *concerned*: a problem he intends to solve and is confident he can
- Zero excess movement in any frame. He is precise and upright; the measuring tape is always around his neck, including at the vitrine and at close
- The two-handed lift is the only frame in the sheet where he is not selling. It must be visibly different in register — slower posture, lowered shoulders, full attention on the object
- No frame may wink at the audience or land a verdict on anyone
- The ellipsis_hold frame carries the character: a real held beat with nothing happening in it

---

## 🔦 Sprite Sheet 4: The Night Porter
**File:** `night_porter.png`
**Dimensions:** 256x288 pixels
**Color Palette:** #808080 (Grey uniform tunic), #1A1A1A (Night marble shadow), #CFB53B (Torch beam warm core), #FFF8E7 (Moonlit marble)

### The Round (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| walk_round A | (0, 0) | 64x96 | Contact frame; torch at waist height, keys silent |
| walk_round B | (64, 0) | 64x96 | Passing frame |
| walk_round C | (128, 0) | 64x96 | Opposite contact |
| walk_round D | (192, 0) | 64x96 | Passing frame |

### Key Beats (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| torch_sweep_plinth | (0, 96) | 64x96 | Once per circuit; torch up to exactly plinth height, no slowing |
| the_count | (64, 96) | 64x96 | "The mannequins are two." Mid-stride, walk cycle uninterrupted, face shows **nothing** |
| torch_hook | (128, 96) | 64x96 | End of shift; torch onto its hook |
| thermos | (192, 96) | 64x96 | Service door, 6:50 PM, filled at home |

### Callbacks & Ambient (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| pose_compliment | (0, 192) | 64x96 | "You hold a pose well, sir. Most men move." Warm, in motion, never stopping |
| day_passing | (64, 192) | 64x96 | Coming in as the day staff leave |
| talk_to_room | (128, 192) | 64x96 | An ambient round line, delivered to nobody, still walking |

### Props & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Torch On Its Hook | (192, 192) | 32x48 | Examinable forever; rubber collar worn smooth on one side |
| Thermos | (224, 192) | 32x48 | He has never once bought a coffee in Imperial Square |
| Key Ring, Carried Silent | (192, 240) | 32x48 | Carried so they do not sound |
| Soft-Soled Shoes Detail | (224, 240) | 32x48 | Worn flat, silent on marble |

### Animation Timing:
- walk_round A→B→C→D: 4fps, continuous loop, **pace never varies** — this loop is the stealth sequence's clock
- torch_sweep_plinth: 1.5s, single play, once per circuit, on schedule, regardless of what is on the plinths
- the_count: delivered over 1.8s with the walk cycle running underneath at unchanged speed; no pause before, during, or after
- torch_hook: 1.2s, single play, end of shift
- pose_compliment: 1.0s, delivered in passing; the walk never stops

### Character Notes:
- Seventy, tired, dignified, and entirely unremarkable — the least dramatic thing in a marble showroom at midnight
- **Never spooky, never comedic-doddering, never a jump-scare silhouette.** He is not a security threat and he is not a joke
- His face must be legible for exactly one frame during the plinth sweep and must show nothing whatsoever
- He never stops walking. In any scene. Under any circumstances
- The warm smile exists only in `pose_compliment` and `day_passing` — the player never sees it during the sequence
- The torch is the single most important prop in the questline's marquee beat: heavy, old, rubber-collared, beam swept at waist height except once per circuit

---

## 👔 Sprite Sheet 5: Staff, Customers & The Party
**File:** `haute_couture_npcs.png`
**Dimensions:** 384x288 pixels
**Color Palette:** #1A1A1A (Staff blacks), #CFB53B (Livery gold), #FFF8E7 (Marble key), tourist earth tones

### Staff & Customers (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shop Assistant Idle | (0, 0) | 48x96 | Impeccably dressed, moving silently, always nearby |
| Assistant With Champagne Tray | (48, 0) | 48x96 | "Champagne while you decide?" |
| Assistant Suggesting Cufflinks | (96, 0) | 48x96 | "They really complete the look." |
| Assistant Redirecting Vitrine Inquiry | (144, 0) | 48x96 | The vitrine is off their script entirely |
| Aristocrat Customer | (192, 0) | 48x96 | Does not acknowledge your existence |
| Nervous Tourist | (240, 0) | 48x96 | "Is this... is this too much?" |
| Decisive Regular | (288, 0) | 48x96 | Hands over card without looking at price |
| Valued Client, Named | (336, 0) | 48x96 | Champagne in hand; they learned his name |

### The Bros (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner, Tourist Clothes | (0, 96) | 48x96 | Assessed in two seconds, found wanting |
| Lord Pilsner, Opera Cape | (48, 96) | 48x96 | "I feel like a DIFFERENT PERSON." |
| Lord Pilsner, Stage-Whisper Heist | (96, 96) | 48x96 | Audible from the street, six feet from Aiguille |
| Chadwick, Conductor's Tuxedo | (144, 96) | 48x96 | "How do I look?!" |
| Chadwick Making A Face | (192, 96) | 48x96 | "We are ROBBING this man." |
| Bradley At The Monocles | (240, 96) | 48x96 | A man of focus |
| Bro Mannequin Pose A | (288, 96) | 48x96 | PATH B — mid-gesture, held |
| Bro Mannequin Pose B | (336, 96) | 48x96 | Cape hem visibly trembling |

### Scene Composites:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bro Mannequin Pose C | (0, 192) | 48x96 | The third plinth |
| Mannequin Beat, Eleven-Second Hold | (48, 192) | 144x96 | Three men in opera capes on display plinths — framed for portrait capture |
| Assessment Protocol Reaction, Party | (192, 192) | 96x96 | Three tourists in the doorway under the gaze |
| Post-Purchase Party, Elevated | (288, 192) | 96x96 | €800 of merchandise; "we're CLIENTELE" |

### Character Notes:
- The three mannequin poses must silhouette-match the Sheet 2 showroom mannequins at plinth scale — the gag only works if the count is genuinely ambiguous from a distance
- Exactly one cape hem trembles. Never two. It is on Pose B
- The Assessment Protocol reaction sprite plays completely straight and is never modified for the quest — including while a Groin Blurt is going off
- Assistants never look at the vitrine. Not once, in any frame

---

## 🧥 Sprite Sheet 6: Formal Wear, Accessories & Transaction Props
**File:** `haute_couture_equipment.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #1A1A1A (Blacks), #CFB53B (Gold Thread), #FFF8E7 (Linen/silk), #6B0F1A (Presentation Burgundy)

### Premium Collection & Garments:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Emperor's Ensemble | (0, 0) | 64x96 | €750, +8 Charm +5 Style — automatic respect from all Sinfonia NPCs |
| Prima Donna Gown | (64, 0) | 64x96 | €600, +6 Charm +4 Performance |
| Conductor's Tuxedo | (128, 0) | 48x64 | €300, +5 Charm +3 Performance, +15% rhythm-timed damage |
| Opera Cape | (176, 0) | 48x64 | €200. It has been €200 all season |
| Virtuoso's Vest | (224, 0) | 48x64 | €350, +4 Performance +3 Charm |
| Aristocrat's Walking Stick | (272, 0) | 32x64 | €250, weapon, 1.2x damage, chance to Embarrass |
| The Phantom's Mask | (304, 0) | 48x48 | €400, +4 Mystery +3 Charm |
| The Phantom's Mask, Worn | (304, 48) | 48x48 | Masquerade state |
| Black-Tie Attire Set | (352, 0) | 48x64 | Gates one of three routes into The Black-Tie Backroom |
| Midnight Worsted Bolt, 13 Metres | (400, 0) | 64x48 | PATH A errand payload |
| Bolt Tied For Carrying | (400, 48) | 64x48 | Shoulder-carry configuration |
| Midnight Worsted On Shoulders | (464, 0) | 48x64 | "You will bring it back to me on your shoulders." |
| Tuxedo Tails Detail | (128, 64) | 48x32 | Close-up |
| Cape Clasp Detail | (176, 64) | 48x32 | Close-up |
| Vest Embroidery Detail | (224, 64) | 48x32 | Close-up |
| Walking Stick Head | (272, 64) | 32x32 | Close-up |
| Black-Tie Bow Detail | (352, 64) | 48x32 | Close-up |
| Shoulder-Carry Strap | (464, 64) | 48x32 | Errand rig |

### Accessories & Small Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Formal Gloves | (0, 96) | 32x32 | €75, +2 Charm, halves Embarrassed duration |
| Ballroom Shoes | (32, 96) | 32x32 | €150, +3 Dance +2 Speed |
| Cultural Critic's Monocle | (64, 96) | 32x32 | €175, +3 INT, forgery detection |
| Maestro's Cufflinks | (96, 96) | 32x32 | €125, +10% rhythm timing window |
| Opera Glasses | (128, 96) | 32x32 | €100, +2 Perception |
| Ivory Fan | (160, 96) | 32x32 | €90, +2 Style, fans away one status per battle |
| Pearl Cufflinks | (192, 96) | 32x32 | €80, +5% shop discounts |
| Silk Pocket Square | (224, 96) | 24x24 | €50, prevents Disheveled |
| Velvet Bow Tie | (248, 96) | 24x24 | €60, required for some formal venues |
| Valued Client Badge | (272, 96) | 32x32 | Status indicator |
| Champagne Coupe | (304, 96) | 32x32 | Standard grade |
| Better Champagne Coupe | (336, 96) | 32x32 | Valued Client grade |
| Gold Circle Coin | (368, 96) | 32x32 | `item_gold_circle_coin` — cannot be sold, dropped, or traded |
| Burgundy Presentation Sleeve | (400, 96) | 48x32 | Keepable, worthless, untranslated French |
| Vitrine Key | (448, 96) | 24x32 | Kept apart from every other key in the shop |
| Measuring Tape Item | (472, 96) | 40x32 | Examinable; numbers gone at 80cm |

### Presentation & Packaging:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cape On Rack | (0, 128) | 48x64 | Showroom display state |
| Tuxedo On Rack | (48, 128) | 48x64 | Showroom display state |
| Gown On Form | (96, 128) | 48x64 | Showroom display state |
| Ensemble On Form | (144, 128) | 48x64 | Premium display, spotlit |
| Vest On Hanger | (192, 128) | 48x64 | Showroom display state |
| Accessories On Velvet Pillow | (240, 128) | 48x32 | Alcove presentation |
| Cufflinks On Velvet Pillow | (240, 160) | 48x32 | Alcove presentation |
| Alteration Ticket | (288, 128) | 48x32 | +€50, return later |
| Perfect-Fit Tag (+1) | (288, 160) | 48x32 | Genuinely worth it |
| Garment Box, Black With Gold | (336, 128) | 64x64 | Purchase packaging |
| Garment Bag | (400, 128) | 48x64 | Carry state |
| Receipt, €800 | (448, 128) | 64x64 | "That's not a receipt, that's a RÉSUMÉ." |

### Transaction & Tier Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Price Card, Blank Reverse | (0, 192) | 48x32 | Prices not visible on the floor |
| Price Card "€200" | (48, 192) | 48x32 | The cape, all season |
| Price Card "€750" | (96, 192) | 48x32 | The Emperor's Ensemble |
| Ticket Book Open | (144, 192) | 64x32 | Where the true price is written |
| Assessment Protocol Icon | (208, 192) | 32x32 | Fires on first entry per outfit state |
| Tier Plate: Client | (240, 192) | 64x32 | €0, standard treatment |
| Tier Plate: Valued Client | (304, 192) | 64x32 | €500, private room, 10% off |
| Tier Plate: Distinguished Client | (368, 192) | 64x32 | €1000, 15% off, reserved items |
| Tier Plate: Patron of Fashion | (432, 192) | 64x32 | €2000, 20% off, custom orders |
| Outfit Comparison Stat Card | (0, 224) | 128x32 | Fitting-room stat delta |
| Synergy Reveal Card | (128, 224) | 96x32 | €100 consultation output |
| Champagne Bottle, Two Grades | (224, 224) | 32x32 | Both visible; only one offered |
| Caption Plate "Investment Piece" | (256, 224) | 80x32 | Standard selfie |
| Caption Plate "The Old Me Is Dead" | (336, 224) | 88x32 | Requires €300+ in one visit |
| Caption Plate "They Know My Name Now" | (424, 224) | 88x32 | Requires Patron of Fashion |

### Technical Notes:
- The Opera Cape must be the most silhouette-legible garment on the sheet at 48x64 — it is the shop's icon and the "Cape Confidant" achievement art
- The Gold Circle Coin is 32x32 and reads as gold foil with an unbroken seal; it must **never** be rendered with a sparkle, glow, or rarity frame. Its power is that it looks like a piece of 1990 novelty latex, because it is
- Price cards ship in blank-reverse and revealed pairs; the floor state is always blank
- Tier plates are text-differentiated, not colour-differentiated (see Accessibility)

---

## ✨ Sprite Sheet 7: Shimmer, Champagne & Torchlight
**File:** `haute_couture_effects.png`
**Dimensions:** 256x192 pixels
**Color Palette:** #CFB53B (Gold Thread), #EFE3B8 (Champagne Pale), #FFF8E7 (Marble key), #808080 (Night wash)

### Fabric & Light:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fabric Shimmer Sweep A | (0, 0) | 64x48 | Silk highlight travelling |
| Fabric Shimmer Sweep B | (64, 0) | 64x48 | Second phase |
| Gold Thread Glint | (128, 0) | 32x32 | Trim sparkle, single pop |
| Dust Motes In Chandelier Beam | (160, 0) | 48x48 | Slow drift |
| Chandelier Light Bloom | (208, 0) | 48x48 | Additive overhead |
| Spotlight Cone, Museum Display | (128, 32) | 32x64 | Per-piece display light |
| Vitrine Spotlight Halo | (0, 48) | 64x48 | Never turns off |
| Champagne Bubble Column A | (64, 48) | 32x48 | Coupe rise, frame A |
| Champagne Bubble Column B | (96, 48) | 32x48 | Frame B |
| Cork Pop Burst | (160, 48) | 48x48 | Valued Client unlock |
| Mirror Reflection Sheen | (208, 48) | 48x48 | Multiply pass over mirror art |

### Night & Stealth (PATH B):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Torch Beam, Waist Height | (0, 96) | 64x48 | The default sweep |
| Torch Beam, Plinth Sweep | (64, 96) | 64x48 | Once per circuit, exact plinth height |
| Moonlight Marble Wash | (128, 96) | 64x48 | Cool overlay, showroom at midnight |
| Cape Hem Tremble Overlay | (192, 96) | 32x48 | Applied to exactly one bro |
| Held-Pose Stillness Marker | (224, 96) | 32x48 | Player-facing hold indicator |

### Audio Glyphs & Comedy Stings:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Price Reveal Sting Glyph | (0, 144) | 32x32 | Subtle musical emphasis, visualised |
| Assessing Gaze Glyph | (32, 144) | 32x32 | The two-second look, marked |
| Door Chime Glyph, Disappointed | (112, 144) | 32x24 | Casual-attire arrival |
| Door Chime Glyph, Welcoming | (144, 144) | 32x24 | Well-dressed arrival |
| Register Chime Ring | (176, 144) | 32x24 | Refined chime |
| Footstep Ring, Soft-Soled | (208, 144) | 24x24 | The Night Porter's primary positional cue |
| Torch Rubber-Collar Glyph | (232, 144) | 24x24 | The other primary positional cue |
| Sigh Glyph | (0, 176)† | 24x24 | *(see note)* |
| Confidence Posture Aura | (0, 176) | 64x16 | Post-purchase: "You're already standing differently." |
| Champagne Fizz Glyph | (64, 168) | 48x24 | Pour audio marker |
| Curtain Rustle Glyph | (112, 168) | 32x24 | Fitting-room audio marker |
| Fabric Handle Glyph | (144, 168) | 32x24 | Reverence audio marker |
| Thermos Pour Glyph | (176, 168) | 32x24 | Service-door ambient marker |
| Bell Summon Glyph | (208, 168) | 48x24 | Fitting-room bell |

† Sigh Glyph ships inside the Assessing Gaze Glyph cell as a second variant frame at (32,144); no separate coordinate is allocated.

### Technical Notes:
- All particles are CPUParticles2D. Champagne bubbles cap at 6 per coupe, 2 coupes maximum on screen
- The Torch Beam sprites are the only light cones in the shop authored as additive *masked* quads — they must not bloom onto the mannequin poses, or the held-pose gag loses its edge
- Cape Hem Tremble is a 2-frame ±1px shear applied at runtime to one designated sprite; it is never baked
- Mirror Reflection Sheen and Marble Floor Reflection Strip (Sheet 2) must use the same opacity curve so the showroom reads as one polished surface

---

## 🖥️ Sprite Sheet 8: Fitting Interface, Client Tiers & Stealth HUD
**File:** `haute_couture_ui.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #1A1A1A (Panel), #CFB53B (Frame/Text), #FFF8E7 (Field), #6B0F1A (Confirm accent)

### Fitting Room Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fitting Panel Frame | (0, 0) | 160x96 | Mirror preview + stat comparison |
| Stat Comparison Row | (160, 0) | 96x24 | Current vs. proposed |
| Stat Delta Chip Positive | (160, 24) | 48x24 | Upward arrow, doubled border |
| Stat Delta Chip Negative | (208, 24) | 48x24 | Downward arrow, jagged border |
| Tailor Commentary Bubble | (160, 48) | 96x48 | "It is an observation of progress." |

### Assessment & Purchase:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Assessment Protocol Banner | (0, 96) | 128x32 | Fires on first entry per outfit state |
| Outfit Quality Meter | (128, 96) | 128x32 | Drives staff treatment tier |
| Price Reveal Plate | (0, 128) | 96x32 | The true number, stated once here and once aloud |
| Purchase Confirm Button | (96, 128) | 80x32 | 44px+ touch rect |
| Decline Button | (176, 128) | 80x32 | "Perhaps another time. When you're... ready." |

### Client Tier Track:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tier Track Bar | (0, 160) | 160x24 | €0 → €2000 rail |
| Tier Pip | (160, 160) | 24x24 | Milestone marker, filled/empty |
| Discount Badge | (184, 160) | 24x24 | 10% / 15% / 20% |
| Valued Client Badge Large | (208, 160) | 48x48 | €500 unlock hero art |
| Spend Counter Plate | (0, 184) | 96x24 | Running total |
| Private Room Unlock Banner | (96, 184) | 112x24 | Less public judgment |

### Quest & Stealth ("Nothing Is Getting Through"):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Vitrine Inquiry Prompt | (0, 208) | 96x24 | Redirected to Monsieur Aiguille |
| Errand Objective Card | (96, 208) | 112x24 | PATH A: midnight worsted, 13 metres, in formal wear, in daylight |
| Pose-Hold Timer Ring, 11 Seconds | (208, 208) | 48x48 | PATH B marquee beat; screenshot button stays live throughout |
| Patrol Clock Bar | (0, 232) | 96x24 | Fixed pattern; never reacts, never speeds up |
| Groin Blurt Fail Warning | (96, 232) | 112x24 | The sequence's actual fail-state generator |

### Technical Notes:
- **The Night Porter is not a detection mechanic.** There is no cone, no alert state, and no fail-on-sight UI. The Patrol Clock Bar displays a fixed loop; the only fail warning in the sequence is the Groin Blurt indicator
- The screenshot/selfie button must remain interactive for the full duration of the Pose-Hold Timer Ring
- Stat delta chips are border-coded (doubled = positive, jagged = negative) as well as arrow-coded
- Tier plates and the tier track use text and pip count, never hue, to distinguish the four levels

---

## 🎬 Animation Specifications

### The Assessment Protocol:
- **Duration:** 2.0 seconds, single play
- **Frames:** 2 (assessing_gaze A → B), then hold on B for 0.8s before dialogue
- **Pattern:** Snap to A, ease to B, hold. No return to idle until the line completes
- **Trigger:** Any first entry in a new outfit state — applied to everyone, every time, never softened for any quest
- **Purpose:** The shop's defining beat: a complete diagnosis delivered in two seconds by someone who thinks he is helping
- **Audio Sync:** Door chime (disappointed or welcoming tone, per outfit quality) 0.3s before frame 1; the greeting line begins on the hold
- **Mobile Optimization:** None needed

### The Circling:
- **Duration:** 3.0 seconds, single play
- **Frames:** 3 (circling A → B → C), one per named fragment
- **Pattern:** Sequential, each frame held 1.0s, locked to "The shoulders... the posture... the fabric choices..."
- **Trigger:** Party assessment on first visit; consultation purchase
- **Purpose:** A man naming what he sees, in fragments, while you fill the pauses
- **Audio Sync:** One dialogue fragment per frame; the ellipses are real held beats with no audio in them
- **Mobile Optimization:** None needed

### Ticket Write & Price Restatement:
- **Duration:** 2.0 seconds, single play
- **Frames:** 3 (approach counter → write → look up)
- **Pattern:** Continuous write; the restated price lands on frame 2
- **Trigger:** Any purchase confirmation
- **Purpose:** The complete truth of the transaction, delivered at entirely normal volume, while the buyers celebrate a robbery
- **Audio Sync:** Refined register chime on frame 1; "It has been €200 all season" spoken flat across frame 2 — no smirk, no emphasis on any word
- **Mobile Optimization:** None needed

### The Vitrine Unlock (PATH A):
- **Duration:** 4.5 seconds, single play
- **Frames:** 3 (separate key → two-handed lift → seating in sleeve)
- **Pattern:** Deliberately the slowest animation in the location; hold 1.5s on the lift
- **Trigger:** PATH A errand completed at Valued Client tier
- **Purpose:** The most sincere thirty seconds in the questline, played completely straight
- **Audio Sync:** Lock turn on frame 1; **no music sting, no comedy scoring, no undercut anywhere in this animation.** Room tone only
- **Mobile Optimization:** None needed — this is the content

### Lock Check:
- **Duration:** 1.0 second, single play
- **Frames:** 1 (lock_check) with a 2-frame finger contact
- **Pattern:** Two fingers on the vitrine's lock, on his way past
- **Trigger:** 7 PM close, every night, in every state of the game — including after the case is empty
- **Purpose:** He never stopped checking. He never says why
- **Audio Sync:** Soft glass tap
- **Mobile Optimization:** None needed

### The Round (Night Porter Patrol Loop):
- **Duration:** Continuous; full circuit configurable, pace fixed
- **Frames:** 4 (walk_round A → B → C → D) at 4fps
- **Pattern:** Unvarying loop. Never accelerates, never reacts, never breaks
- **Trigger:** PATH B after-hours sequence begins
- **Purpose:** The stealth sequence's clock — the player plans around a fixed pattern, not a detection cone
- **Audio Sync:** Soft-soled footsteps and the torch's rubber collar mixed as the scene's **primary positional cue**; ambient round lines fire from other rooms at intervals
- **Mobile Optimization:** None needed — the loop is 4 frames

### The Plinth Sweep:
- **Duration:** 1.5 seconds, single play, once per circuit
- **Frames:** 1 (torch_sweep_plinth) with the beam cone animating across
- **Pattern:** Torch rises to exactly plinth height, passes across all three faces in sequence, does not slow
- **Trigger:** Scheduled once per patrol circuit, regardless of what is on the plinths
- **Purpose:** The marquee beat's camera move, performed by a prop
- **Audio Sync:** Footsteps continue unbroken underneath. No music change
- **Mobile Optimization:** None needed

### The Count:
- **Duration:** 1.8 seconds, delivered over the running walk cycle
- **Frames:** 0 additional — `the_count` frame swaps in for 1 walk-cycle frame and out again
- **Pattern:** Mid-stride, conversational, no pause before or after, walk cycle uninterrupted
- **Trigger:** Plinth sweep resolves with three bros held in pose
- **Purpose:** "The mannequins are two. There are two mannequins."
- **Audio Sync:** **No music sting. No camera push. No reaction cut to a bro.** The line ships verbatim, in one breath, at conversational volume. The repetition is a man confirming his own count
- **Mobile Optimization:** None needed

### Fabric Shimmer:
- **Duration:** 2.0 second cycle
- **Frames:** 2 (shimmer sweep A ↔ B)
- **Pattern:** Slow travelling highlight across silk surfaces; emitters offset so no two garments shimmer together
- **Trigger:** Constant on premium garments and mannequins
- **Purpose:** The clothes ARE excellent, and the art has to say so before the stat card does
- **Audio Sync:** None
- **Mobile Optimization:** Premium garments only on Medium; disabled on Low

### Champagne Pour:
- **Duration:** 1.5 seconds, single play + 3.0s bubble loop
- **Frames:** 2 bubble columns (A ↔ B) plus cork pop burst on tier unlock
- **Pattern:** Pour, then continuous bubble rise while held
- **Trigger:** Well-dressed entry, Valued Client unlock, or fitting-room wait
- **Purpose:** You'll need it when you see the prices
- **Audio Sync:** Fizz on pour; cork pop on the Valued Client unlock only
- **Mobile Optimization:** Bubble count 6 → 3 on Medium; static coupe on Low

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Monsieur Aiguille outline | set at sheet layout | 48x96 | Primary vendor silhouette, thick rim |
| Vitrine outline | set at sheet layout | 64x96 | Quest-critical interactable |
| Three-way mirror outline | set at sheet layout | 128x160 | Selfie spot frame |
| Fitting room curtain outline | set at sheet layout | 32x80 | Entry point marker |
| Display plinth outline | set at sheet layout | 32x48 | PATH B pose targets |
| Night Porter outline | set at sheet layout | 64x96 | Readable against dark marble |
| Equipment icon outlines (all 21) | set at sheet layout | varies | White-rim variants for shop legibility |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static fabric shimmer | set at sheet layout | 64x48 | Single held highlight, no sweep |
| Static champagne coupe | set at sheet layout | 32x32 | No bubble rise |
| Tremble-free cape hem | set at sheet layout | 32x48 | Trembling conveyed by a static wobble-line glyph |
| Non-scrolling backdrop frame | set at sheet layout | 512x128 | Parallax disabled variant |
| Fixed torch beam | set at sheet layout | 64x48 | Sweep replaced by a discrete two-position cut |
| Static dust motes | set at sheet layout | 48x48 | No drift |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door chime glyph, disappointed | (112, 144) | 32x24 | Casual-attire arrival tone |
| Door chime glyph, welcoming | (144, 144) | 32x24 | Well-dressed arrival tone |
| Register chime ring | (176, 144) | 32x24 | Every completed purchase |
| Price reveal sting glyph | (0, 144) | 32x32 | Every price reveal |
| Champagne fizz glyph | (64, 168) | 48x24 | Every pour |
| Curtain rustle glyph | (112, 168) | 32x24 | Fitting-room entry/exit |
| Bell summon glyph | (208, 168) | 48x24 | Fitting-room bell |
| Footstep ring, soft-soled | (208, 144) | 24x24 | **Night Porter proximity — the stealth sequence's primary cue must have a visual equivalent** |
| Torch rubber-collar glyph | (232, 144) | 24x24 | Torch handling, positional |
| Thermos pour glyph | (176, 168) | 32x24 | Service-door ambient |
| Fabric handle glyph | (144, 168) | 32x24 | Aiguille's reverence beat |

### Colorblind Considerations:
- Stat delta chips are border-coded (doubled = positive, jagged = negative) and arrow-coded, never hue alone
- Client tiers are distinguished by name text and pip count (0–3 filled), never by colour
- Door chime tone is communicated by glyph *shape* (downturned vs. upturned arc), not by tint
- The Assessment Protocol banner carries an explicit icon rather than a colour state
- Torch beam and moonlight wash are separated by shape (hard cone vs. soft flood) so the stealth sequence is readable in monochrome
- Touch zones minimum 44px for purchase/decline, fitting-room entry, the vitrine, and the pose-hold input

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 for environment and characters; ASTC 4x4 for `haute_couture_equipment.png` and `haute_couture_ui.png` — garment silhouettes and the Coin must stay legible at inventory scale. PVRTC 4BPP fallback.
- **Android:** ETC2 with alpha across all sheets
- **Fallback:** PNG high quality for `haute_couture_landmarks.png` — the vitrine spotlight gradient and mirror sheen band under compression

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| haute_couture_environment | tileset, landmarks | 2048x1024 |
| haute_couture_characters | Aiguille, Night Porter, staff & party | 1024x512 |
| haute_couture_items_fx | equipment, effects, UI | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full fabric shimmer on all garments, chandelier dust motes, champagne bubbles (6/coupe), mirror reflection compositing, spotlight cones, parallax backdrop, torch beam sweep |
| Medium | Shimmer on premium garments only, halved dust density, 3 bubbles/coupe, simplified single-plane mirror reflection, spotlight cones retained |
| Low | No shimmer, no dust, static coupe, mirror reflection replaced with a flat tint pass, parallax off. **Vitrine spotlight and torch beam are retained at all LOD levels — they are quest-critical staging** |

### Performance Targets:
- **Target FPS:** 40 (per location profile: "40 FPS target")
- **Max Draw Calls:** 15 per frame (per location profile)
- **Memory Footprint:** 40 MB maximum (per location profile)
- **Particle Limit:** 20 (dust 8, champagne 6, shimmer 6 — the PATH B night scene disables dust and champagne entirely and spends the whole budget on nothing, because the sequence is silent and still)

### Performance Notes:
- Mirror reflection is a single duplicated, flipped, alpha-reduced sprite of the player — not a viewport render. Two mirror surfaces maximum on screen
- The Alteration Workshop behind the glass wall uses two looping silhouette sprites, not full NPCs
- The PATH B night scene is a distinct scene state, not a separate scene: it swaps the façade overlay, kills daytime NPCs, and loads exactly one additional character sheet (`night_porter.png`)
- Showroom customer NPCs cap at 3 concurrent sprites
- Equipment preview in the fitting room composites one garment sprite over the player base — no per-item character redraws

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- `TileMap` for floors/walls; `ParallaxBackground` with two `ParallaxLayer` nodes for the Imperial Square backdrop
- `AnimatedSprite2D` for Monsieur Aiguille (all 22 states) and the Night Porter (patrol loop + beats)
- `Sprite2D` pool (max 3) for assistants and customers; 2 looping silhouettes behind the workshop glass
- `CPUParticles2D` (not GPU) for dust motes, champagne bubbles, fabric shimmer emitters
- `CanvasLayer` for the fitting interface, tier track, and PATH B stealth HUD
- `Light2D` (or additive quad, per platform tier) for the vitrine spotlight and the museum display cones; the torch beam is an additive masked quad parented to the Night Porter
- Shop state machine: `entered → assessed → browsing → fitting → purchase_confirmed → tier_evaluated` — the Assessment Protocol fires on transition into `assessed` for every new outfit state
- Vitrine state machine: `sealed → (PATH A) unlocked → empty_placard_retained` / `sealed → (PATH B) empty_placard_retained`. Both terminal states keep the spotlight and the placard, permanently, on every subsequent visit
- Aiguille schedule driver: 9–10 AM workshop, 10 AM–2 PM showroom, 2–5 PM fitting rooms, 5–7 PM showroom, 7 PM close + `lock_check`. He does not exist in the scene after 7 PM under any circumstances
- Night Porter patrol: a fixed-timeline `PathFollow2D` clock. **No detection cone, no alert state, no fail-on-sight.** The Groin Blurt system is the sequence's only fail-state generator

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Glass entry door opening | Door chime (disappointed / welcoming per outfit tier) | 0.3s before assessing_gaze frame 1 |
| circling A/B/C | "The shoulders... the posture... the fabric choices..." | One fragment per frame; ellipses are silent held beats |
| ticket_write frame 2 | "It has been €200 all season" — flat, normal volume | Mid-write |
| Price reveal plate | Subtle musical sting | On plate appear |
| Purchase confirm | Refined register chime | On button release |
| Valued Client unlock | Champagne cork pop | On tier badge swap |
| Fitting room curtain | Curtain rustle | On open/close |
| Summon bell | Bell, single strike | On press; Aiguille is already on his way |
| vitrine_unlock frames 1–3 | Lock turn, then room tone only | **No scoring anywhere in this cue** |
| Night Porter walk cycle | Soft-soled footsteps + torch rubber collar | Continuous; primary positional cue, mixed forward |
| the_count | Line delivered conversationally over unbroken footsteps | No sting, no push, no cut |
| pose_compliment | Warm pleasantry at passing-hello volume | Never followed by anything |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| "Dress for Success" | Conductor's Tuxedo, Opera Cape, Phantom's Mask, Black-Tie Attire, garment bag | Acquire formal wear for masquerade infiltration |
| "The Emperor's Ensemble" | Emperor's Ensemble sprite + on-form display, Patron tier plate | Premium quest unlocking the highest-tier item |
| "Fashion Critic" | Aiguille consultation frame, synergy reveal card, aristocrat/tourist/regular NPCs | He asks you to assess others' outfits |
| "Patron of Fashion" | Tier track bar, all four tier plates, spend counter, caption "They Know My Name Now" | Reach maximum client status |
| **"Nothing Is Getting Through" — PATH A** | Vitrine sealed → open → empty, separate key, two-handed lift, presentation sleeve, Gold Circle Coin, errand objective card, midnight worsted bolt + shoulder-carry, named_greeting frame | Valued Client (€500, existing tier) + the errand in formal wear, in daylight; then the handover ceremony |
| **"Nothing Is Getting Through" — PATH B** | Night façade overlay, service door + torch hook + step, all four patrol frames, plinth sweep, the_count, three bro mannequin poses, eleven-second hold composite, pose-hold timer ring, patrol clock bar, Groin Blurt warning, plinth labeled "3", valued_clients_pause, pose_compliment | After-hours infiltration (shop closes 7 PM) in formal wear purchased from this shop |
| Selfie Spot — Standard | Three-way mirror, caption "Investment Piece" | Any visit in new equipment |
| Selfie Spot — "The Transformation" | Three-way mirror, old clothes prop in corner, caption "The Old Me Is Dead" | Spend €300+ in one visit |
| Selfie Spot — "Distinguished Client" | Private fitting room, better champagne coupe, caption "They Know My Name Now" | Patron of Fashion status |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Imperial Square | Shared district paving, ashlar façade, backdrop strips; the storefront is visible from the square | Standard street transition |
| Baroness' Ballroom | Formal attire required for entry — equipment sprites carry over as worn-state overlays | None (equipment check on entry) |
| The Black-Tie Backroom | Black-Tie Attire Set sold here; one of three routes in | None (inventory gate) |
| The Bassline Opera House | Opera Cape and Conductor's Tuxedo for day attendance; Maestro's Cufflinks widen rhythm timing | None (equipment carry-over) |
| Crown & Cask | Formal attire improves seating rank at the banquet benches | None (equipment check on entry) |
| Debaucheryville — "Nothing Is Getting Through" | Three bros arrive carrying `the_herp`; the Gold Circle Coin is the objective; the shop is the prophecy's "HOUSE OF NEEDLES" | Cross-city quest handoff; scene text and branch logic live in `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md` |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Intimidating elegance, engineered — a genuinely excellent shop that has been designed to make you feel you don't deserve it until you pay"
- **Color Mood:** Cream marble and gold thread against velvet black; warm chandelier grandeur in the showroom, a cold grey interrogation ramp in the fitting rooms
- **Lighting:** Chandelier glamour overhead, museum spotlights per display piece, one permanent spotlight on the vitrine, and a fitting-room key light angled to find every flaw. At night: moonlight on marble, one torch, nothing else
- **Texture:** Polished marble, silk with a travelling highlight, black velvet that eats light, gold beading, and one grey uniform tunic pressed by hand

### Environmental Storytelling:
- Prices are not visible anywhere on the showroom floor — the price cards ship blank-side-out, and the true number only ever appears on the ticket
- Staff outfits are visibly nicer than anything the player is wearing until very late in the tier ladder
- The fitting-room light ramp is measurably colder than the showroom's; the shop is telling you something with lux values
- The vitrine sits at the back of the alcove with its own spotlight, its own velvet, and a hand-set placard, and it is in Aiguille's sightline from most of the showroom, which is not an accident and is never mentioned
- Post-quest the case is empty and every other detail is untouched: the light, the velvet with the Coin's impression still in it, the placard. He refused to remove it
- The two display plinths have been quietly re-labeled "3." Nobody claims it and nothing resolves it
- A torch hangs on a hook by the service door in every scene, at every hour, on both paths

### Character Integration Notes:
- **Monsieur Aiguille is never a snob.** Every frame must read as a specialist reading your chart, who likes you, and who is about to tell you. If a frame looks contemptuous, it is wrong
- His only register change in the entire sheet is the two-handed vitrine lift — that frame must be visibly a different man doing a different thing
- **The Night Porter is never spooky, never doddering, and never a joke.** He is the most clear-eyed person in his scene and the least dramatic thing in the room. His age and his knees are never the punchline
- Nothing in the Night Porter's performance — posture, timing, or the one legible face frame — may hint that he knows. The moment it looks knowing, the beat is dead
- The bros are the only sprites permitted loose posture and broad gesture; everyone employed here stands correctly
- Assistants never look at the vitrine in any frame

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The mannequin beat** — three men in opera capes frozen mid-gesture on display plinths in a moonlit marble showroom, one cape hem visibly trembling, a torch beam crossing their faces in sequence. Framed for portrait capture, readable at thumbnail size with zero text, screenshot button live for the full eleven seconds
2. **The two-handed lift** — a tailor in a three-piece suit raising a piece of 1990 novelty latex out of a spotlit vitrine with total reverence, while a man in cargo shorts says "It's a coin"
3. **The ticket** — Aiguille writing at the counter, restating the true price at normal volume, while three men celebrate a robbery six feet behind him
4. **The assessing gaze**, held, in the doorway, on a party in beachwear
5. **The plinths, later**, quietly re-labeled "3"
6. **The empty vitrine** with its spotlight still on and its placard still there

### Quote Potential:
- "It is not for sale. It is for aspiration." - the vitrine placard
- "That is a statement about you. It is not a statement about the case." - Monsieur Aiguille
- "Welcome to Haute Couture. I see we have... work to do." - Monsieur Aiguille
- "The cape is €200. It has been €200 all season. I should not like the gentleman to feel he had underpaid." - Monsieur Aiguille
- "It is an observation of progress." - Monsieur Aiguille
- "It was not a small hem." - Monsieur Aiguille
- "They spent five hundred euro to be told their own names. Do not laugh. Everyone here did." - Monsieur Aiguille
- "The mannequins are two. There are two mannequins." - The Night Porter
- "You hold a pose well, sir. Most men move." - The Night Porter
- "Two hundred euro for a cape. Well. It is a very good cape." - The Night Porter, ambient round line
- "EIGHT HUNDRED EUROS, boys — for ALL of it. That's not a receipt, that's a RÉSUMÉ." - Chadwick

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | haute_couture_tileset.png | 1024x512 |
| 2 | haute_couture_landmarks.png | 512x384 |
| 3 | monsieur_aiguille.png | 384x288 |
| 4 | night_porter.png | 256x288 |
| 5 | haute_couture_npcs.png | 384x288 |
| 6 | haute_couture_equipment.png | 512x256 |
| 7 | haute_couture_effects.png | 256x192 |
| 8 | haute_couture_ui.png | 256x256 |

**Total Estimated Memory:** ~5 MB (1,261,568 px uncompressed RGBA); ~1.4 MB after ETC2/ASTC compression — comfortably inside the 40 MB profile budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `haute_couture_tileset.png` (1024x512)
- [ ] `haute_couture_landmarks.png` (512x384)
- [ ] `monsieur_aiguille.png` (384x288)
- [ ] `night_porter.png` (256x288)
- [ ] `haute_couture_npcs.png` (384x288)
- [ ] `haute_couture_equipment.png` (512x256)
- [ ] `haute_couture_effects.png` (256x192)
- [ ] `haute_couture_ui.png` (256x256)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve layers in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet + parallax layer guide (two strips, 0.25x / 0.6x) + vitrine state-flow diagram (sealed → PATH A / PATH B → empty, placard retained) + Night Porter patrol timing chart

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (including the two derived accents, flagged in the palette table)
- [ ] **No frame of Monsieur Aiguille sneers.** Every expression reads as concerned, never contemptuous
- [ ] The two-handed vitrine lift is visibly a different register from every other Aiguille frame
- [ ] The measuring tape is around his neck in all 22 frames, including the vitrine frames
- [ ] **The Night Porter's face shows nothing whatsoever** in his one legible frame during the plinth sweep
- [ ] The Night Porter is never rendered as spooky, doddering, or comedic
- [ ] The three bro mannequin poses silhouette-match the Sheet 2 showroom mannequins at plinth scale
- [ ] Exactly one cape hem trembles (Pose B), never two
- [ ] Vitrine Sealed / Open / Empty share identical framing and spotlight geometry
- [ ] The empty vitrine retains spotlight, velvet impression, and placard
- [ ] The Gold Circle Coin has no sparkle, glow, or rarity frame
- [ ] Display Plinth Empty and Display Plinth Labeled "3" are pixel-identical apart from the numeral
- [ ] Fitting-room grey ramp is measurably colder than the showroom cream ramp in a side-by-side crop
- [ ] Accessibility visual alternatives included for all audio cues — including the Night Porter's footstep and torch cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (luxury retail psychology, honest transaction misread as a heist) is clear throughout
- [ ] The vitrine reads as sacred without any comedy scoring, wink, or undercut
- [ ] The eleven-second hold is framed for portrait capture and readable at thumbnail size with zero text
- [ ] The stealth sequence contains no detection-cone or alert-state art — the Night Porter is a clock, not a guard mechanic
- [ ] Mobile performance optimized (CPU particles, 15-draw-call ceiling, three atlas binds, no viewport mirror renders)
- [ ] Touch zone sizing considered (44px minimum for purchase/decline, fitting room, vitrine, pose-hold input)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia and Imperial Square only; Sinfonian haute-tailoring and old-imperial concert-hall dress influence, no real place named |
| Cultural Specificity | ✅ | Sinfonian haute-tailoring tradition, Imperial Square gatekeeping, formal-wear etiquette, bespoke house since 1822 |
| Satirical Targets Appropriate | ✅ | Luxury retail psychology and the bros mistaking an honest transaction for a heist; Aiguille is a genuine craftsman who charges the marked price and protects his staff, never a caricature; the Night Porter is written with complete respect |
| Seedy Underbelly Present | ✅ | The profile's "Buffoon Exploitation" section: a shop that assesses arrivals instantly, guides them toward "transformative" pieces, and is engineered so they spend more than planned. Plus PATH B: after-hours infiltration and theft from the vitrine |
| Gameplay Value Established | ✅ | 16-item equipment shop, fitting-room stat-comparison mechanic, four-tier client ladder, three special services, Assessment Protocol, two-path quest hub, three selfie variants, seven achievements |
| Technical Feasibility | ✅ | Eight sheets, three atlases, three LOD tiers, scene-state (not scene-swap) night mode, CPU particles only |
| Mobile Performance Budget | ✅ | 40 FPS / 15 draw calls / 40 MB taken verbatim from the profile's stated budget. Flagged: 40 FPS is below the 60 FPS engine default — confirm deliberate low-end target |
| Accessibility Features | ✅ | Visual glyphs for all eleven audio cues including the Night Porter's footstep and torch cues; static/reduced-motion variants for shimmer, champagne, cape tremble, torch sweep, parallax; shape-first UI coding |
| No Crypto Elements | ✅ | None present. Confirmed absent in the location profile ("No crypto elements — Pure fashion snobbery") and in both NPC profiles' explicit crypto checks |
| Social Media Integration | ✅ | Three documented selfie variants with unlock conditions, six screenshot moments, eleven quotable lines, one portrait-framed marquee beat with a live screenshot button |

**Haute Couture Haberdashery: a shop that will tell you the complete truth about the price twice, improve you exactly as promised, and let you walk out believing you robbed it — where the only thing in the building that cannot be altered sits under a spotlight that never goes off.**
