# The Standing Ovation - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for The Standing Ovation — a converted opera-house annex brewery where every pour is a performance, every drink comes with applause, and the beer is aged in barrels that once held the tears of rejected understudies. It satirizes performance culture: the beer is genuinely excellent, the drama is completely unnecessary, and everyone commits anyway because performative appreciation has become indistinguishable from genuine enjoyment. Home of the Bravo Challenge toast mini-game, Sinfonia Brewery Tour stamp #2, and Herr Dramatisch, a brewmaster for whom everything is either MAGNIFICENT or TRAGIC.

**Location ID:** `sinfonia_operadistrict_standing_ovation_01`
**Theme:** Performance culture and theatrical pretension applied to drinking — Viennese opera tradition weaponized against a pint of lager
**Zone:** Opera District, near The Bassline Opera House
**Hours:** 16:00–01:00 (after matinee, before morning rehearsals)
**Primary Function:** Brewery / brewery tour stamp location / toast-performance mini-game (Bravo Challenge) / bar shop with per-beer stage lighting / selfie spot / achievement hub

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Curtain Red | #8B0000 | Curtains, carpet, marquee trim, stamp ink |
| Spotlight Gold | #FFD700 | Spotlights, gilding, applause signs, marquee bulbs |
| Theater Black | #1A1A1A | Walls, shadows, stagehand base tones |
| Foam White | #FFFAF0 | Beer heads, playbill paper, footlight glow |
| Copper Pour | #B87333 | Curtain Call Copper, brew kettle, organ-pipe taps |
| Ruby Highlight | #9B111E | Copper lager highlights, velvet depths |
| Gilded Brass | #B8860B | Rails, opener, frames, tap collars |
| Backstage Grey | #4A4A4A | Green Room concrete, Wings paneling, honesty |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/the_standing_ovation/
├── environment/
│   ├── the_standing_ovation_exterior.png
│   └── the_standing_ovation_tileset.png
├── npcs/
│   ├── herr_dramatisch.png
│   └── the_standing_ovation_npcs.png
├── objects/
│   └── the_standing_ovation_items.png
├── effects/
│   └── the_standing_ovation_effects.png
└── ui/
    └── the_standing_ovation_ui.png
```

---

## 🎭 Sprite Sheet 1: Exterior & Marquee
**File:** `the_standing_ovation_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #8B0000 (Curtain Red), #FFD700 (Spotlight Gold), #1A1A1A (Theater Black), #B8860B (Gilded Brass)

### Façade Sections:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Facade Left Tower | (0, 0) | 192x256 | Opera-annex stonework, dramatic pilasters, gilded cornice |
| Facade Center Arch | (192, 0) | 256x256 | Grand entrance arch, "THE STANDING OVATION" carved lintel |
| Facade Right Tower | (448, 0) | 192x256 | Mirrored tower with theatrical torch sconce |
| Dramatic Light Spill | (960, 0) | 64x256 | Warm gold light column spilling onto the street |

### The Marquee ("NOW POURING:"):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marquee Frame | (640, 0) | 320x128 | Theater marquee, bulb border, fixed "NOW POURING:" header |
| Marquee Letter Board Blank | (640, 128) | 320x64 | Empty track rows for changeable letter tiles |
| Marquee Bulb Overlay F1 | (640, 192) | 320x32 | Bulb chase pattern, odd bulbs lit |
| Marquee Bulb Overlay F2 | (640, 224) | 320x32 | Bulb chase pattern, even bulbs lit |
| Marquee Letters A–M | (0, 256) | 208x24 | Thirteen changeable letter tiles, 16x24 each, gold on black |
| Marquee Letters N–Z | (208, 256) | 208x24 | Thirteen changeable letter tiles, 16x24 each |
| Marquee Numerals & Punctuation | (416, 256) | 192x24 | 0–9, apostrophe, ampersand — 16x24 each (for "CRITICS' CHOICE") |
| Marquee Blank Tile | (608, 256) | 16x24 | Spacer tile, matte black |

### Entrance & Street:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Red Carpet Straight | (0, 288) | 64x96 | Curtain Red runner with gold edging |
| Red Carpet End Flare | (64, 288) | 96x96 | Carpet fanning out at the curb — to a bar |
| Velvet Rope Post | (160, 288) | 16x64 | Brass stanchion (decorative, not exclusive) |
| Velvet Rope Swag | (176, 288) | 64x32 | Draped crimson rope between posts |
| Critics Welcome Sign | (240, 288) | 96x64 | Standing sign: "Critics Welcome — We'll Change Their Minds" |
| Entrance Doors Closed | (336, 288) | 96x96 | Heavy double doors, brass mask knockers |
| Entrance Doors Open Glow | (432, 288) | 96x96 | Doors flung wide, applause-colored light within |
| Exterior Poster Case | (528, 288) | 48x80 | Glass case with parody beer playbill |
| Theatrical Street Lamp | (576, 288) | 32x96 | Lamppost angled like a follow spot |
| Night Window Glow | (608, 288) | 64x64 | Warm interior glow overlay for windows |
| Applause Spill Glyph | (672, 288) | 32x32 | Clap-hands glyph escaping the doors (visual audio cue) |
| Cobblestone Tile | (704, 288) | 32x32 | Opera District street surface |
| Queue Silhouettes | (736, 288) | 96x64 | Post-show crowd waiting behind decorative ropes |

### Night & State Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marquee Night Lit | (0, 384) | 320x128 | Fully lit marquee variant, halo bloom |
| Facade Night Overlay | (320, 384) | 256x128 | Blue-black night grade with gold windows |
| Red Carpet Worn | (576, 384) | 64x96 | Threadbare center line — everyone walks the same dramatic path |
| Repurposed Box Office | (640, 384) | 64x96 | Ticket booth relabeled "BEER OFFICE" |
| Sandwich Board Reviews | (704, 384) | 48x64 | "★★★★★ — The Management" self-review board |

### Technical Notes:
- Letter tiles snap to two 16px-grid track rows on the letter board; longest string "INTERMISSION IPA" (16 tiles incl. space) fits one row
- Bulb overlays alternate for a chase effect; both off = closed state
- Light spill and night overlays are additive-blend layers over the base façade

---

## 🏛️ Sprite Sheet 2: Theatrical Taproom Tileset
**File:** `the_standing_ovation_tileset.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #1A1A1A (Theater Black), #8B0000 (Curtain Red), #B87333 (Copper Pour), #4A4A4A (Backstage Grey)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stage Boards | (0, 0) | 32x32 | Worn oak stage flooring, visible grain |
| Stage Boards Scuffed | (32, 0) | 32x32 | Heel marks from a thousand bows |
| Pit Floor Dark | (64, 0) | 32x32 | Sunken Orchestra Pit flooring, near-black |
| Carpet Red | (96, 0) | 32x32 | House carpet, Curtain Red |
| Carpet Gold Border | (128, 0) | 32x32 | Gold-trimmed carpet edge |
| Balcony Floor | (160, 0) | 32x32 | Polished upper-tier parquet |
| Green Room Concrete | (192, 0) | 32x32 | Plain sealed concrete — the honest floor |
| Wings Floor | (224, 0) | 32x32 | Quiet matte boards, no spotlight marks |
| Pit Step | (256, 0) | 32x32 | Step down into the sunken bar |
| Pit Edge Trim | (288, 0) | 32x32 | Brass nosing on the pit rim |
| Spotlight Floor Mark | (320, 0) | 32x32 | Taped X where the toast spotlight lands |
| Confetti-Littered Floor | (352, 0) | 32x32 | Post-ovation floor state |

### Walls & Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Theater Black Wall | (0, 32) | 32x64 | Matte black house wall |
| Curtain Red Wall | (32, 32) | 32x64 | Draped fabric wall panel |
| Gold Trim Wall | (64, 32) | 32x64 | Black wall with gilded molding |
| Green Room Brick | (96, 32) | 32x64 | Whitewashed brick, exposed pipe |
| Wings Panel Wall | (128, 32) | 32x64 | Quiet grey paneling |
| Wainscot Cap Gilded | (160, 32) | 32x32 | Gold cap molding |
| Gilded Frame Empty | (192, 32) | 64x64 | Ornate frame awaiting self-written praise |
| Playbill Cluster | (256, 32) | 96x64 | Overlapping parody beer playbills |
| Framed Review Small | (352, 32) | 32x48 | "A Triumph." — written by the triumph |
| Framed Review Large | (384, 32) | 48x64 | Full glowing notice, byline: "The Management" |
| Applause Sign Lit | (432, 32) | 64x32 | "APPLAUSE" in gold bulbs (ironic, then not) |
| Applause Sign Unlit | (496, 32) | 64x32 | Dark sign between performances |
| Theatrical Sconce | (560, 32) | 16x32 | Flame-shaped bulb, red shade |
| Dramatic Exit Sign | (576, 32) | 32x24 | "EXIT (DRAMATICALLY)" over the Wings door |
| Costume Display: The Diva Stout | (608, 32) | 48x96 | Beer-ad gown costume on mannequin |
| Costume Display: Fräulein Foam | (656, 32) | 48x96 | Beer-ad dirndl costume from a "famous" campaign |
| Costume Plinth Plaque | (704, 32) | 64x32 | Brass plaque citing fictitious ad awards |

### The Orchestra Pit (Main Bar):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Orchestra Pit Bar Front | (0, 128) | 256x128 | Sunken bar counter built as a stage apron |
| Organ Pipe Taps | (256, 128) | 128x128 | Beer taps arranged as ascending organ pipes, copper and brass |
| Backbar Shelving | (384, 128) | 128x128 | Glassware racks lit like a set piece |
| Pit Bench Curve | (512, 128) | 128x64 | Curved sunken seating facing the "stage" |
| Footlights Strip | (512, 192) | 128x32 | Unlit footlight row along bar edge |
| Footlights Strip Lit | (512, 224) | 128x32 | Warm lit variant for performances |
| Bar Stool | (640, 128) | 24x40 | Velvet-topped stool |
| Cocktail Table | (664, 128) | 40x40 | Small round table, reserved-card prop |
| Tap Handles Row | (704, 128) | 96x32 | Six individual handles (16x32 each), one per menu beer |
| Pour Station | (800, 128) | 64x96 | Stagehand's pouring podium with flourish room |
| Stein Rack | (864, 128) | 64x48 | Hanging ceremonial steins |
| Glass Shelf | (864, 176) | 64x32 | Tulip glasses awaiting their cue |
| Dramatic Menu Lectern | (928, 128) | 48x64 | Menu presented like a conductor's score |

### The Balcony & Stage Lighting:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Balcony Rail Gilded | (0, 256) | 128x48 | Gold balustrade overlooking the pit |
| Balcony Rail Corner | (0, 304) | 48x48 | Corner return piece |
| Balcony Table Tier | (128, 256) | 96x64 | Elevated critics' table with notepads |
| Balcony Box Seat | (224, 256) | 64x80 | Self-appointed critics' box |
| Opera Glasses Prop | (288, 256) | 24x16 | For judging toasts at range |
| Stage Light Rig | (320, 256) | 128x48 | Ceiling truss with lamp heads |
| Spotlight Lamp Unit | (320, 304) | 48x48 | Single follow-spot housing |
| Lighting Gel: Curtain Call Copper | (448, 256) | 64x64 | Warm amber wash with ruby edge — signature pour |
| Lighting Gel: Opening Night Ale | (512, 256) | 64x64 | Bright white premiere wash |
| Lighting Gel: The Understudy | (576, 256) | 64x64 | Dim half-light, apologetic |
| Lighting Gel: Critics' Choice | (640, 256) | 64x64 | Cool discerning gold |
| Lighting Gel: The Encore | (704, 256) | 64x64 | Full gold flood, maximum drama |
| Lighting Gel: Intermission IPA | (768, 256) | 64x64 | House-lights amber |
| House Lights Neutral | (832, 256) | 64x64 | Default no-performance wash |

### The Green Room (Brewery Access):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Copper Brew Kettle | (0, 384) | 96x128 | Actual working kettle — polished but unglamorous |
| Fermentation Tank | (96, 384) | 80x128 | Steel tank with taped-on handwritten label |
| Mash Tun | (176, 384) | 96x96 | Where the real work happens, no spotlight |
| Bottling Bench | (272, 384) | 96x64 | Cluttered, practical, zero flourish |
| Understudy-Tears Barrel Stack | (368, 384) | 96x80 | The famous barrels, chalk-marked "TEARS (ALLEGEDLY)" |
| Clipboard of Actual Science | (464, 384) | 24x32 | Fermentation charts — the least dramatic prop in the building |
| Stamp Ceremony Podium | (496, 384) | 64x96 | Gilded podium with taped spotlight mark — the one theatrical item back here |
| Green Room Mirror | (560, 384) | 64x80 | Bulb-ringed mirror, half the bulbs out |
| Humble Folding Chair | (624, 384) | 32x48 | Deliberately, pointedly untheatrical |
| Fluorescent Light Strip | (656, 384) | 96x16 | Flat institutional lighting |
| Green Room Door | (752, 384) | 32x64 | "PERFORMERS ONLY (EVERYONE IS A PERFORMER)" |
| Tour Rope Guide | (784, 384) | 48x32 | Brewery tour path rope |

### The Wings & Velvet Curtain Exit:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wings Recovery Booth | (0, 544) | 96x96 | Quiet booth where failed toasters recover |
| Consolation Table | (96, 544) | 64x48 | Low table with water and dignity |
| Tissue Box Prop | (160, 544) | 16x16 | For post-boo emotions |
| "Next Time" Sampler | (176, 544) | 48x32 | Embroidered "YOU'LL GET THEM NEXT TIME" |
| Private Tasting Nook | (224, 544) | 96x96 | Curtained alcove for drama-free tastings |
| Dramatic Emergency Exit | (320, 544) | 64x96 | Push-bar door for dramatic departures |
| Velvet Curtain Exit Closed | (384, 544) | 128x192 | Floor-to-ceiling crimson exit curtain (yes, really) |
| Velvet Curtain Parting F1 | (512, 544) | 128x192 | Curtain edges lifting |
| Velvet Curtain Parting F2 | (640, 544) | 128x192 | Full part, street light beyond |
| Curtain Tieback Gold | (768, 544) | 32x64 | Braided gold rope tieback |
| Curtain Valance | (800, 544) | 128x48 | Scalloped top swag |

### Large Set Pieces:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Taproom Backdrop | (0, 768) | 512x256 | Painted opera backdrop behind the bar — clouds, cherubs, hops |
| Balcony Underhang | (512, 768) | 256x128 | Gilded underside of the balcony tier |
| Proscenium Arch Top | (768, 768) | 256x96 | Carved arch crowning the bar-stage |
| House Chandelier | (512, 896) | 128x128 | Crystal chandelier over the pit |
| Proscenium Column Left | (640, 896) | 96x128 | Fluted gold column |
| Proscenium Column Right | (736, 896) | 96x128 | Mirrored column |
| Spotlight Floor Circle | (832, 896) | 96x96 | Baked-in light pool for the selfie spot stage mark |

### Technical Notes:
- Lighting gels are full-screen-tinted 64x64 swatches sampled by a palette-swap CanvasModulate — one gel active at a time, keyed to the beer being poured
- Green Room deliberately uses Backstage Grey and flat lighting: the visual joke is the contrast with the front of house
- Velvet curtain frames double as the location exit animation and the stamp ceremony backdrop

---

## 🎩 Sprite Sheet 3: Herr Dramatisch (Brewmaster)
**File:** `herr_dramatisch.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #1A1A1A (Coat), #8B0000 (Cape Lining), #FFD700 (Buttons, Trim), #FFFAF0 (Shirt)

### Idle & Presence (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle MAGNIFICENT | (0, 0) | 48x96 | Chest out, cape settled, mustache at full attention |
| Idle TRAGIC | (48, 0) | 48x96 | Back of hand hovering near brow, cape drooping |
| Welcome Flourish F1 | (96, 0) | 48x96 | Arms beginning grand opening gesture |
| Welcome Flourish F2 | (144, 0) | 48x96 | Arms wide, cape lifting |
| Welcome Flourish F3 | (192, 0) | 48x96 | Full wingspan — "The stage is SET!" |
| Cape Swirl F1 | (240, 0) | 48x96 | Turn initiated, cape trailing |
| Cape Swirl F2 | (288, 0) | 48x96 | Cape at maximum arc |
| Cape Swirl F3 | (336, 0) | 48x96 | Cape wrapping to rest — the silhouette frame |
| Brewery Tour Gesture | (384, 0) | 48x96 | Presenting the kettle as if unveiling a soprano |
| Holding Court | (432, 0) | 48x96 | One boot on a crate, mid-anecdote |

### Toast Judging (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Listening Intently | (0, 96) | 48x96 | Leaning in, hand cupped to ear |
| Eyebrow Arch | (48, 96) | 48x96 | Single brow raised — the verdict forms |
| Moved To Tears | (96, 96) | 48x96 | Glistening eye, trembling mustache |
| Verdict MAGNIFICENT F1 | (144, 96) | 48x96 | Arms shooting skyward |
| Verdict MAGNIFICENT F2 | (192, 96) | 48x96 | Held triumph, cape flared |
| Verdict TRAGIC F1 | (240, 96) | 48x96 | Head turning away in anguish |
| Verdict TRAGIC F2 | (288, 96) | 48x96 | Full collapse against the bar |
| Verdict ACCEPTABLE | (336, 96) | 48x96 | Grudging nod — the rarest middle ground |
| The Long Pause | (384, 96) | 48x96 | Frozen mid-assessment, crowd holding breath |
| Crowd Poll Gesture | (432, 96) | 48x96 | Arm sweeping to the house — "The crowd has spoken!" |

### Stamp Ceremony (48x96 each unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp Raise F1 | (0, 192) | 48x96 | Stamp lifted from podium |
| Stamp Wind-Up F2 | (48, 192) | 48x96 | Arm cocked behind head |
| Maximum Flourish Apex F3 | (96, 192) | 48x96 | Full extension, cape airborne, one leg raised |
| Stamp Down F4 | (144, 192) | 48x96 | Impact frame, ink burst |
| Stamp Hold & Glare F5 | (192, 192) | 48x96 | Holding the stamp down, meeting the player's eyes |
| Passport Present | (240, 192) | 48x96 | Returning passport with two-handed reverence |
| Post-Stamp Bow | (288, 192) | 48x96 | Deep bow to his own performance |
| Free Copper Presentation | (336, 192) | 48x96 | Offering the Curtain Call Copper, opener reward pose |
| Tragic Collapse | (384, 192) | 48x96 | Back of hand to forehead, full swoon |
| Recovering Composure | (432, 192) | 48x96 | Straightening coat, mustache re-twirled |

### Props & Dialogue Portraits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Prop Brass Stamp | (0, 288) | 24x24 | Handheld stamp, mask motif on grip |
| Prop Passport Open | (24, 288) | 32x24 | Brewery passport open to Sinfonia page |
| Mustache Twirl Overlay F1 | (56, 288) | 24x16 | Fingers at mustache tip |
| Mustache Twirl Overlay F2 | (80, 288) | 24x16 | Full curl achieved |
| Cape Flare Overlay | (104, 288) | 64x64 | Detached cape swoosh for compositing |
| High Contrast Silhouette | (168, 288) | 48x96 | Solid outline — cape and mustache must read in silhouette |
| Portrait MAGNIFICENT | (216, 288) | 96x96 | Dialogue portrait, ecstatic pole |
| Portrait TRAGIC | (312, 288) | 96x96 | Dialogue portrait, devastated pole |
| Portrait ACCEPTABLE | (408, 288) | 96x96 | Dialogue portrait, suspicious neutrality |

### Movement & Reaction (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Green Room Holding Court | (0, 384) | 64x96 | Seated wide on the humble folding chair, still theatrical |
| Walk F1 | (64, 384) | 48x96 | Stride with cape sway left |
| Walk F2 | (112, 384) | 48x96 | Passing pose |
| Walk F3 | (160, 384) | 48x96 | Stride with cape sway right |
| Applauding F1 | (208, 384) | 48x96 | Hands apart, beaming |
| Applauding F2 | (256, 384) | 48x96 | Thunderclap contact frame |
| BRAVO Shout | (304, 384) | 48x96 | Head back, mouth wide, fists clenched in joy |
| Toast Glass Raised | (352, 384) | 48x96 | Ceremonial stein aloft |
| Idle Blink Variant | (400, 384) | 48x96 | MAGNIFICENT idle with rare, dignified blink |

### Technical Notes:
- Cape reads as a single dark mass with #8B0000 lining flashes — silhouette check mandatory at 48px
- MAGNIFICENT and TRAGIC are the only two idle poles; ACCEPTABLE appears exclusively during judging
- Stamp ceremony frames sync to the curtain-rise stamp animation on Sheet 5

---

## 👥 Sprite Sheet 4: Critics, Stagehands & Patrons
**File:** `the_standing_ovation_npcs.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #1A1A1A (Stagehand Black), #8B0000 (House Seats), #FFFAF0 (Notepads), assorted patron wear

### The House Critics (48x80 each unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Critic A Assessing | (0, 0) | 48x80 | Balcony lean, pen hovering over notepad |
| Critic A Scribbling | (48, 0) | 48x80 | Furious note-taking mid-toast |
| Critic A Unimpressed | (96, 0) | 48x80 | "Derivative toast" face |
| Slow Clap F1 | (144, 0) | 48x80 | Hands apart, glacial |
| Slow Clap F2 | (192, 0) | 48x80 | First contact, deliberate |
| Slow Clap F3 | (240, 0) | 48x80 | Accelerating — respect earned |
| Critic Won Over | (288, 0) | 48x80 | "FINALLY! Someone who understands the CRAFT!" |
| Critic Standing Bravo | (336, 0) | 48x80 | On feet, notepad discarded |
| Notepad Prop | (384, 0) | 16x24 | Scored margins, tiny stars |
| Pencil Prop | (400, 0) | 8x16 | Chewed with judgment |
| Critic B Opera Glasses | (416, 0) | 48x80 | Judging the toast at sixty centimeters' range |
| Critic B Lean Forward | (464, 0) | 48x80 | Interest piqued despite herself |

### The Stagehands (Bartenders, 48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stagehand Idle | (0, 80) | 48x96 | All black, perfectly still, professionally invisible |
| Pour Flourish F1 | (48, 80) | 48x96 | Glass presented at arm's length |
| Pour Flourish F2 | (96, 80) | 48x96 | Tap pulled with balletic extension |
| Pour Flourish F3 | (144, 80) | 48x96 | High-pour arc at apex, foam blooming |
| Pour Flourish F4 | (192, 80) | 48x96 | Glass landed, hand withdrawn with grace |
| Small Bow F1 | (240, 80) | 48x96 | Bow initiated — every delivery gets one |
| Small Bow F2 | (288, 80) | 48x96 | Held bow, eyes down |
| Spotlight Operation | (336, 80) | 48x96 | Hands on follow-spot, tracking the toaster |
| Tray Delivery | (384, 80) | 48x96 | Gliding with laden tray at dramatic pace |
| "You're On" Point | (432, 80) | 48x96 | Deadpan point at the player: your cue |

### Applauding Patrons — Escalation Set (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Patron Seated Neutral | (0, 176) | 48x80 | Drinking, pre-judgment |
| Polite Clap F1 | (48, 176) | 48x80 | Fingertip applause, tier 1 |
| Polite Clap F2 | (96, 176) | 48x80 | Measured contact frame |
| Enthusiastic Clap F1 | (144, 176) | 48x80 | Full-hand applause, tier 2, grin |
| Enthusiastic Clap F2 | (192, 176) | 48x80 | Elbows up contact frame |
| Standing Ovation F1 | (240, 176) | 48x80 | Rising from seat, tier 3 |
| Standing Ovation F2 | (288, 176) | 48x80 | On feet, arms overhead |
| Confused Silence | (336, 176) | 48x80 | Mid-blink, glass frozen halfway — Bradley's toast aftermath |
| Boo F1 | (384, 176) | 48x80 | Cupped hands rising |
| Boo F2 | (432, 176) | 48x80 | Full boo, thumbs down |

### Patron Variants & Crowd (48x80 each unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tourist Patron | (0, 256) | 48x80 | Camera ready, unsure when to stand |
| Regular In Scarf | (48, 256) | 48x80 | Dramatic scarf, drinks only during "scenes" |
| Moderato Pub Researcher | (96, 256) | 48x80 | Tempo-faction member taking "research" notes on pour rhythm |
| Opera-Goer (Gown) | (144, 256) | 48x80 | Post-show crossover from The Bassline Opera House |
| Opera-Goer (Tails) | (192, 256) | 48x80 | Still holding programme |
| Failed Toaster Slinking | (240, 256) | 48x80 | Retreating from spotlight toward the Wings |
| Failed Toaster Recovering | (288, 256) | 48x80 | In recovery booth, tissue in hand |
| Filming Patron | (336, 256) | 48x80 | Phone raised — every toast is content |
| Crowd Silhouette Block | (384, 256) | 128x80 | Dark background house rows |

### Crowd Groups & Portraits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crowd Table Group A | (0, 336) | 96x80 | Three patrons mid-conversation |
| Crowd Table Group B | (96, 336) | 96x80 | Toast-watchers turned in unison |
| Balcony Critics Row | (192, 336) | 128x64 | Full critic bench, notepads aligned |
| Wings Recoverer Seated | (320, 336) | 48x80 | Slumped in booth, halfway to acceptance |
| Stagehand HC Silhouette | (368, 336) | 48x96 | High-contrast outline (black-on-black problem solver) |
| Patron HC Outline | (416, 336) | 48x80 | High-contrast patron edge sprite |
| Critic Portrait | (0, 432) | 64x64 | Dialogue portrait, eternal assessment |
| Stagehand Portrait | (64, 432) | 64x64 | Dialogue portrait, professional calm |
| Reaction Icon: Clap | (128, 432) | 32x32 | Overhead bubble glyph |
| Reaction Icon: Boo | (160, 432) | 32x32 | Thumbs-down bubble glyph |
| Reaction Icon: Silence | (192, 432) | 32x32 | "..." bubble glyph |
| Reaction Icon: Bravo | (224, 432) | 32x32 | Star-burst "BRAVO!" glyph |
| Critics' Score Placards | (256, 432) | 96x32 | Held-up score cards, 1 through PERFECTION |

### Technical Notes:
- Stagehands are Theater Black on Theater Black by design; rim-light every edge with #4A4A4A or they vanish — HC silhouette is the fallback
- Applause escalation tiers are the visual readout of the mini-game score: polite → enthusiastic → standing ovation
- Confused Silence must be reusable house-wide (Bradley's fermentation-science toast triggers it on every patron simultaneously)

---

## 🍺 Sprite Sheet 5: Beers, Opener & Stamp
**File:** `the_standing_ovation_items.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #B87333 (Copper Pour), #9B111E (Ruby Highlight), #FFFAF0 (Foam White), #B8860B (Gilded Brass)

### The Beers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Curtain Call Copper | (0, 0) | 32x64 | Signature Vienna copper lager, deep copper with ruby highlights, dense foam |
| Copper With Bow Serve | (32, 0) | 48x64 | Glass plus stagehand glove mid-bow — served with a small bow, always |
| Opening Night Ale | (80, 0) | 32x64 | Bright gold, delivered after a dramatic pause |
| The Understudy | (112, 0) | 32x64 | Slightly smaller head, apologetic tilt, 4 Sovs honesty |
| Critics' Choice | (144, 0) | 32x64 | Amber with a knowing gleam |
| The Encore | (176, 0) | 32x64 | Rich dark pour that earns a staff standing ovation |
| Intermission IPA | (208, 0) | 32x64 | Hazy gold, served with bell warning |
| Intermission Bell | (240, 0) | 24x24 | Brass hand bell, rung before serving |
| Tap Pour Stream F1 | (264, 0) | 16x48 | Stream leaving the organ-pipe tap |
| Tap Pour Stream F2 | (280, 0) | 16x48 | Full flow with foam churn |
| Tap Pour Stream F3 | (296, 0) | 16x48 | Tapering cutoff |
| Foam Head Overlay | (312, 0) | 32x16 | Cresting foam cap for any glass |
| Beer Flight Paddle | (344, 0) | 96x32 | Private-tasting flight, five thimble steins |
| Souvenir Bottle | (440, 0) | 24x56 | Bottled Curtain Call Copper for opener demos |

### Bottle Opener & Stamp:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bottle Opener (Masks & Ribbon) | (0, 64) | 48x32 | Comedy/tragedy masks joined by ribbon; opener notch in the ribbon; brass with crimson enamel, "Bravo!" inscription |
| Opener Inventory Icon | (48, 64) | 32x32 | Simplified icon for inventory grid |
| Opener Applause-Click Glyph | (80, 64) | 24x24 | Tiny clap burst shown on use (visual audio cue for the applause click) |
| Bravissimo Stamp | (104, 64) | 64x64 | Theater masks clinking beer steins, crimson ink, gold accents, "Bravissimo!" |
| Stamp Ink Pad | (168, 64) | 48x32 | Dramatic crimson pad, gold lid |
| Passport Page Stamped | (216, 64) | 64x64 | Sinfonia page bearing the fresh stamp |
| Curtain-Rise Stamp Anim F1 | (280, 64) | 48x48 | Miniature curtain closed over stamp slot |
| Curtain-Rise Stamp Anim F2 | (328, 64) | 48x48 | Curtain rising, spotlight edge entering |
| Curtain-Rise Stamp Anim F3 | (376, 64) | 48x48 | Spotlight hits stamp location |
| Curtain-Rise Stamp Anim F4 | (424, 64) | 48x48 | Stamp lands, ink stars, tiny confetti |

### Décor Items & Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Playbill: "The Marriage of Pilsner" | (0, 128) | 48x64 | Parody beer playbill, ornate border |
| Playbill: "La Bohemian Lager" | (48, 128) | 48x64 | Tragic romance, hops motif |
| Playbill: "Die Zauberbräu" | (96, 128) | 48x64 | Magic-flute parody with tap wand |
| Framed Self-Review | (144, 128) | 64x48 | "★★★★★ — The Management" in a gilded frame |
| Beer Menu Board | (208, 128) | 96x64 | Six beers, prices, tonight's cast list styling |
| Selfie Spot Marker | (304, 128) | 48x48 | Camera glyph on the stage mark |
| Confetti Pile Prop | (352, 128) | 48x24 | Swept-aside confetti from earlier triumphs |
| Handheld Spotlight Prop | (400, 128) | 32x48 | Backup follow-spot by the pour station |

### Status & Stat Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stage Presence Buff Icon | (0, 192) | 24x24 | Comedy mask with +3 Charm sparkle (Curtain Call Copper effect) |
| HP Restore Icon | (24, 192) | 24x24 | Stein heart |
| SP Restore Icon | (48, 192) | 24x24 | Stein star |
| Ceremonial Stein | (72, 192) | 32x40 | The gravitas vessel for challenge drinks |
| Toast Glint | (104, 192) | 24x24 | Raised-glass sparkle |
| Serving Tray | (136, 192) | 48x32 | Black lacquer, silent delivery |

### Technical Notes:
- Curtain Call Copper's ruby highlight is a 2px #9B111E rim inside the glass — must survive 32px width
- Curtain-rise stamp frames play inside the passport UI; timing on Sheet spec below syncs applause audio to F4
- Marquee spells beer names from Sheet 1 letter tiles; menu board here is the static in-house version

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `the_standing_ovation_effects.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FFD700 (Spotlight Gold), #FFFAF0 (Foam White), #8B0000 (Curtain Red), confetti multicolor

### Spotlight System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spotlight Cone Wide | (0, 0) | 128x256 | Primary follow-spot cone, soft gold falloff |
| Spotlight Cone Narrow | (128, 0) | 64x256 | Tight cone for stamp ceremony and selfies |
| Spotlight Dust F1 | (192, 0) | 64x64 | Drifting motes inside the beam |
| Spotlight Dust F2 | (256, 0) | 64x64 | Motes rising |
| Spotlight Dust F3 | (320, 0) | 64x64 | Motes dispersing |
| Spotlight Floor Pool | (384, 0) | 96x48 | Elliptical light pool at cone base |
| Spotlight Sweep F1 | (192, 64) | 96x64 | Beam sweeping the house, left |
| Spotlight Sweep F2 | (288, 64) | 96x64 | Beam center, narrowing |
| Spotlight Sweep F3 | (384, 64) | 96x64 | Beam locked on target |
| Applause Wave Overlay | (192, 128) | 128x64 | Rippling light across the crowd during ovations |
| House Dim Overlay | (320, 128) | 128x128 | Darkens everything outside the spotlight |
| Curtain Ripple Overlay | (448, 128) | 64x128 | Fabric shimmer for curtain surfaces |

### Celebration & Failure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Confetti Burst F1 | (0, 256) | 96x96 | Cannon pop, tight cluster |
| Confetti Burst F2 | (96, 256) | 96x96 | Full spread, gold and crimson |
| Confetti Burst F3 | (192, 256) | 96x96 | Peak scatter |
| Confetti Burst F4 | (288, 256) | 96x96 | Fluttering descent |
| Confetti Fall Loop F1 | (384, 256) | 64x96 | Ambient falling pieces |
| Confetti Fall Loop F2 | (448, 256) | 64x96 | Offset fall cycle |
| Foam Cascade F1 | (0, 352) | 48x64 | Overfoam breaching the glass rim |
| Foam Cascade F2 | (48, 352) | 48x64 | Foam sheeting down the glass |
| Foam Cascade F3 | (96, 352) | 48x64 | Settling lace |
| Curtain Sway F1 | (144, 352) | 64x96 | Exit curtain breathing inward |
| Curtain Sway F2 | (208, 352) | 64x96 | Sway return |
| Dramatic Sting Flash | (272, 352) | 64x64 | Radial gold flash on verdict stings |
| Sad Trombone Glyph | (336, 352) | 32x32 | Drooping trombone notes (visual audio cue, failed toast) |
| Triumphant Brass Glyph | (368, 352) | 32x32 | Ascending fanfare notes (visual audio cue, success) |
| Applause Burst Small | (400, 352) | 48x48 | Sparse clap glyphs — polite tier |
| Applause Burst Large | (448, 352) | 48x48 | Dense clap glyphs — ovation tier |

### Audio Cue Glyphs & Reduced-Motion Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Boo Cloud | (0, 416) | 48x32 | Grey jeer-cloud with down-arrows (visual audio cue) |
| Silence Dots | (48, 416) | 32x16 | "..." for confused silence |
| Spotlight Hum Glyph | (80, 416) | 24x24 | Soft wave rings at cone tip while spot is live |
| Bell Ring Glyph | (104, 416) | 24x24 | Radiating chime arcs for Intermission bell |
| Stamp Applause Glyph | (272, 416) | 24x24 | Clap burst pinned to stamp F4 |
| Glass Clink Sparkle | (296, 416) | 16x16 | Toast contact glint |
| Lighting Wash Gold | (336, 416) | 64x64 | Full-house gold grade (The Encore) |
| Lighting Wash Ruby | (400, 416) | 64x64 | Ruby grade (Curtain Call Copper) |
| Static Spotlight Alt | (0, 448) | 96x48 | Pre-lit pool, no sweep — motion-sensitivity variant |
| Static Confetti Scatter | (96, 448) | 96x48 | Already-fallen confetti, no burst — motion-sensitivity variant |

### Technical Notes:
- House Dim Overlay + cone + floor pool composite the full "spotlight finds you" moment; all additive except the dim layer (multiply)
- Confetti burst REPLACES spotlight dust and fall-loop emitters while active — systems never stack
- Lighting washes are palette-swap grades, not shaders, for low-end devices

---

## 🖥️ Sprite Sheet 7: UI Elements
**File:** `the_standing_ovation_ui.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #1A1A1A (Panels), #FFD700 (Trim), #8B0000 (Accents), #FFFAF0 (Text)

### Toast Speech Interface (Bravo Challenge):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Toast UI Panel | (0, 0) | 256x128 | Script-page styled dialogue panel, stage direction margins |
| Choice Button: Humble Thanks | (256, 0) | 192x32 | Easy — polite applause guaranteed |
| Choice Button: Dramatic Monologue | (256, 32) | 192x32 | Medium — enthusiasm if delivered well |
| Choice Button: Operatic Attempt | (256, 64) | 192x32 | Hard — standing ovation OR complete silence |
| Choice Button: Wing It | (256, 96) | 192x32 | Variable — Charm stat decides everything |
| Difficulty Pips | (448, 0) | 48x16 | One to three mask pips per choice |
| Charm Check Icon | (448, 16) | 24x24 | Mask-and-die glyph for stat-gated options |
| Crowd Mood Preview | (448, 40) | 48x24 | Mini face row forecasting reaction |

### Applause Meter & Status:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Applause Meter Frame | (0, 128) | 128x32 | Proscenium-arch shaped gauge frame |
| Applause Meter Needle | (128, 128) | 16x32 | Gold conductor-baton needle |
| Meter Zone Icons | (144, 128) | 96x24 | Four zone glyphs: silence dots / polite hands / full hands / standing figure — shape-coded, not color-only |
| Applause Meter Fill | (0, 160) | 128x16 | Red-to-gold gradient fill strip |
| Meter Fill HC Variant | (128, 160) | 128x16 | Hatched high-contrast fill, pattern encodes tier |
| Encore! Buff Icon | (256, 128) | 32x32 | Gold laurel over stein, +5 Bravado (1 hour) |
| Booed Off Status Icon | (288, 128) | 32x32 | Cracked mask with down-arrow — temporary ban state |
| Bravo Challenge Banner | (320, 128) | 160x48 | Challenge title card with curtain flourish |

### Results & Flow:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spotlight Vignette UI | (0, 192) | 128x64 | Screen-edge dim overlay when the spotlight finds you |
| Results Card: Success | (128, 192) | 128x64 | "BRAVO!" card, stamp progress, Encore! grant |
| Results Card: Booed | (256, 192) | 128x64 | "Tough Crowd" card with retry terms |
| Stamp Progress Pip | (384, 192) | 24x24 | Brewery tour pip #2 for Sinfonia |
| Retry Round Button | (408, 192) | 96x32 | "Buy a Round to Retry" — the Booed Off exit clause |
| Judgment Countdown Ring | (408, 224) | 32x32 | Timer ring while the crowd deliberates |
| Monologue Timer Bar | (440, 224) | 64x24 | 60-second bar for the Standing Ovation Challenge monologue |

### Technical Notes:
- All buttons render at minimum 44px touch height in-game (32px art scales at 1.5x UI scale minimum)
- Applause meter must be readable at arm's length on a 5.5" screen — needle plus zone icons plus fill redundancy
- Results cards double as the selfie-spot photo frames ("My Moment" / "They Love Me" / "Tough Crowd")

---

## 🎬 Animation Specifications

### Marquee Bulb Chase:
- **Duration:** 0.8 second loop
- **Frames:** 2 (overlay F1 ↔ F2)
- **Pattern:** Alternate, constant while open
- **Trigger:** Location open hours (16:00–01:00)
- **Purpose:** Street-visible theatrical pull toward the entrance
- **Audio Sync:** None (distant applause ambience handled by scene audio)
- **Performance Optimization:** Hold F1 static on low-end devices

### Spotlight Finds Player:
- **Duration:** 1.2 seconds (0.9s sweep, 0.3s lock)
- **Frames:** 3 sweep frames + cone/pool composite
- **Pattern:** Sweep F1 → F2 → F3, then cone + house dim snap on
- **Trigger:** Bravo Challenge start — drink delivered, "You're on."
- **Purpose:** The mini-game's oh-no moment; the room becomes a stage
- **Audio Sync:** Spotlight hum begins at lock (hum glyph appears same frame)
- **Performance Optimization:** Skip sweep; fade static spotlight alt in over 0.4s

### Stagehand Pour Flourish:
- **Duration:** 1.6 seconds, single play
- **Frames:** 4
- **Pattern:** F1 → F2 → F3 (apex hold 0.4s) → F4
- **Trigger:** Any beer ordered
- **Purpose:** Theatrical pour — the everyday act performed as art
- **Audio Sync:** Pour sound on F2; dramatic sting on F3 apex
- **Performance Optimization:** None needed

### Stagehand Small Bow:
- **Duration:** 0.8 seconds (0.3s down, 0.5s hold)
- **Frames:** 2
- **Pattern:** F1 → F2, hold, return to idle
- **Trigger:** Every drink delivery, no exceptions
- **Purpose:** "Served with a small bow, always"
- **Audio Sync:** None
- **Performance Optimization:** None needed

### Applause Escalation (Crowd):
- **Duration:** Polite: 1.0s loop / Enthusiastic: 0.6s loop / Standing Ovation: 0.5s loop
- **Frames:** 2 per tier
- **Pattern:** Tier selected by toast score; loops for 3–6 seconds
- **Trigger:** Crowd judgment result
- **Purpose:** The applause meter made flesh — score readable from the crowd alone
- **Audio Sync:** Applause volume and density scaled to performance tier; clap glyph size matches (small burst / large burst)
- **Performance Optimization:** Animate 6 nearest patrons; crowd blocks hold static frames

### Critics' Slow Clap:
- **Duration:** 3.0 seconds (claps at 0.75s, 0.55s, 0.35s intervals, accelerating)
- **Frames:** 3
- **Pattern:** F1 → F2 → F3, accelerating tempo into standard applause
- **Trigger:** Toast that wins over the House Critics
- **Purpose:** The highest honor: irony collapsing into sincerity
- **Audio Sync:** Single isolated clap per contact frame, then crowd joins
- **Performance Optimization:** None needed

### Booed Off:
- **Duration:** 1.0 second loop (boo), sad trombone 1.5s single play
- **Frames:** 2 boo frames + trombone glyph
- **Pattern:** Boo loop while Results Card: Booed displays
- **Trigger:** Failed toast (Operatic Attempt silence, botched Wing It)
- **Purpose:** Failure state feeding the hidden "Booed Off" achievement
- **Audio Sync:** Sad trombone at trigger; trombone glyph shows for its full duration
- **Performance Optimization:** None needed

### Confetti Burst:
- **Duration:** 1.2 seconds, single play, then 4s fall loop
- **Frames:** 4 burst + 2 fall-loop
- **Pattern:** Burst F1→F4, hand off to fall loop, settle to floor tile state
- **Trigger:** Standing ovation result; "They Love Me" selfie variant
- **Purpose:** Peak triumph moment — the screenshot generator
- **Audio Sync:** Triumphant brass on burst F1 (brass glyph同frame); applause underneath
- **Performance Optimization:** Halve particle count; skip fall loop, jump to static scatter

### Foam Cascade:
- **Duration:** 0.9 second cycle
- **Frames:** 3
- **Pattern:** Breach → sheet → lace, loop while overfoamed
- **Trigger:** The Encore pour; ceremonial drink moment
- **Purpose:** Beer as spectacle — even the foam performs
- **Audio Sync:** Soft fizz on F1
- **Performance Optimization:** Single static foam overlay frame

### Velvet Curtain Exit:
- **Duration:** 1.0 second
- **Frames:** 3 (closed → part F1 → part F2)
- **Pattern:** Single play on exit; reverse on entry
- **Trigger:** Player exits through the velvet curtain (yes, really)
- **Purpose:** Every departure is a final bow
- **Audio Sync:** Fabric whoosh on F1; faint applause swell on F2
- **Performance Optimization:** Crossfade closed → open, skip F1

### Stamp Ceremony (Curtain-Rise Stamp Animation):
- **Duration:** 2.5 seconds total (curtain rise 1.0s, spotlight hit 0.5s, stamp with flourish 1.0s)
- **Frames:** 4 UI frames (Sheet 5) synced to Herr Dramatisch stamp frames F1–F5 (Sheet 3)
- **Pattern:** Anim F1 → F2 (rise) → F3 (spotlight) → F4 (stamp lands) while Dramatisch plays raise → wind-up → maximum flourish → down → hold
- **Trigger:** Bravo Challenge completed, stamp awarded at Green Room podium
- **Purpose:** "This stamp represents TRIUMPH! GLORY! Also, you drank our beer!"
- **Audio Sync:** Applause sound exactly on F4 stamp contact (stamp applause glyph same frame); brass sting on F3 spotlight hit
- **Performance Optimization:** None needed — this is the payoff moment, protect it

### Herr Dramatisch Verdict:
- **Duration:** 1.0 second, hold final frame 1.5s
- **Frames:** 2 per pole (MAGNIFICENT or TRAGIC)
- **Pattern:** F1 → F2, hold; ACCEPTABLE is a single held frame after The Long Pause (1.2s)
- **Trigger:** Toast judgment delivered
- **Purpose:** No middle ground exists; even ACCEPTABLE is performed grudgingly
- **Audio Sync:** Dramatic sting on F2 (sting flash effect same frame)
- **Performance Optimization:** None needed

### Per-Beer Lighting Shift:
- **Duration:** 0.8 second crossfade
- **Frames:** 2 gel states (outgoing/incoming)
- **Pattern:** CanvasModulate lerp between gel swatches
- **Trigger:** Beer selected at the tap — lighting shifts based on what's being poured
- **Purpose:** The room itself reviews your order
- **Audio Sync:** None (pour flourish carries audio)
- **Performance Optimization:** Instant palette swap, no lerp — gels are swatches, not shaders

### Intermission Bell:
- **Duration:** 1.2 seconds (3 pulses at 0.4s)
- **Frames:** 2 (bell tilt ± ) + ring glyph
- **Pattern:** Swing-swing-swing, glyph arcs per pulse
- **Trigger:** Intermission IPA ordered
- **Purpose:** Bell warning before serving, exactly like a theater lobby
- **Audio Sync:** Chime per pulse; bell ring glyph mirrors each chime
- **Performance Optimization:** None needed

### Bottle Opener Applause Click:
- **Duration:** 0.3 seconds
- **Frames:** 1 glyph pop with scale ease
- **Pattern:** Pop in, fade out
- **Trigger:** Opener used on any bottle
- **Purpose:** The tiniest standing ovation in the game
- **Audio Sync:** Tiny applause click sound on pop (glyph IS the visual cue)
- **Performance Optimization:** None needed

### Applause Meter Needle:
- **Duration:** Continuous, 0.2s eased movement per score change
- **Frames:** Needle sprite rotated in code
- **Pattern:** Ease toward current crowd score; zone icons highlight on entry
- **Trigger:** Active during toast delivery and judgment
- **Purpose:** Real-time performance feedback the whole table can read
- **Audio Sync:** Soft tick at each zone boundary (zone icon pulses same moment)
- **Performance Optimization:** Snap movement, no easing

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Herr Dramatisch HC Silhouette | Sheet 3 (168, 288) | 48x96 | Solid outline — cape and mustache read in pure silhouette |
| Stagehand HC Silhouette | Sheet 4 (368, 336) | 48x96 | Rim-lit outline solving black-clothing-on-black-wall |
| Patron HC Outline | Sheet 4 (416, 336) | 48x80 | Edge sprite for crowd readability |
| Meter Fill HC Variant | Sheet 7 (128, 160) | 128x16 | Hatched pattern fill — tier encoded in pattern density, not hue |
| Organ Pipe Taps (bright-edge pass) | Sheet 2 (256, 128) | 128x128 | Tap collars carry #FFD700 edging so the interactable bar reads under dim house lighting |
| Stamp Podium spotlight mark | Sheet 2 (496, 384) | 64x96 | Taped X + podium glow marks the stamp interaction point |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Spotlight Alt | Sheet 6 (0, 448) | 96x48 | Pre-lit pool replaces the sweep — no moving beam |
| Static Confetti Scatter | Sheet 6 (96, 448) | 96x48 | Already-fallen confetti replaces the burst |
| Marquee Bulb Hold | Sheet 1 (640, 192) | 320x32 | F1 held static, no chase |
| Curtain Static Frame | Sheet 2 (384, 544) | 128x192 | Closed curtain without sway overlay |
| Meter Snap Mode | Sheet 7 (128, 128) | 16x32 | Needle snaps between zones instead of sweeping |

### Visual Audio Cues (every audio event has one):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Applause Burst Small / Large | Sheet 6 (400, 352) / (448, 352) | 48x48 each | Clap glyph density mirrors applause intensity — performance score readable with sound off |
| Sad Trombone Glyph | Sheet 6 (336, 352) | 32x32 | Drooping notes on failed toast |
| Triumphant Brass Glyph | Sheet 6 (368, 352) | 32x32 | Rising fanfare notes on success |
| Spotlight Hum Glyph | Sheet 6 (80, 416) | 24x24 | Wave rings while the spot is live |
| Dramatic Sting Flash | Sheet 6 (272, 352) | 64x64 | Gold flash on every verdict sting |
| Bell Ring Glyph | Sheet 6 (104, 416) | 24x24 | Chime arcs for the Intermission bell |
| Stamp Applause Glyph | Sheet 6 (272, 416) | 24x24 | Clap burst on stamp contact frame |
| Opener Applause-Click Glyph | Sheet 5 (80, 64) | 24x24 | Tiny clap burst on opener use |
| Boo Cloud / Silence Dots | Sheet 6 (0, 416) / (48, 416) | 48x32 / 32x16 | Jeer and dead-silence states visualized |
| Glass Clink Sparkle | Sheet 6 (296, 416) | 16x16 | Toast contact sound made visible |
| Applause Spill Glyph (exterior) | Sheet 1 (672, 288) | 32x32 | Interior applause audible from the street, shown at the doors |

### Colorblind Considerations:
- Applause meter carries triple redundancy: needle position + shape-coded zone icons + fill length (HC variant adds pattern density)
- Lighting gels per beer differ in brightness value, not hue alone (Understudy dim ↔ Encore flood)
- Encore! (laurel) and Booed Off (cracked mask) icons use distinct silhouettes, never tint-only
- Critics' score placards use numerals and mask pips, not colored cards
- Touch zones minimum 44px for taps, toast choices, stamp podium, curtain exit, and retry button

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) marquee and stamp sheets kept uncompressed — letter tiles and stamp detail must stay legible
- **Fallback:** PNG high quality for `the_standing_ovation_items.png` (stamp and opener are screenshot- and inventory-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| standing_ovation_environment | exterior, taproom tileset | 2048x2048 |
| standing_ovation_characters | Herr Dramatisch, critics/stagehands/patrons | 1024x1024 |
| standing_ovation_effects_ui | items, effects, UI | 1024x1024 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full spotlight sweep + dust, confetti burst + fall loop, foam cascade, curtain sway, bulb chase, 10 animated patrons |
| Medium | Spotlight sweep without dust, confetti burst only (no fall loop), 6 animated patrons, static curtain |
| Low | Static spotlight pool, static confetti scatter, palette-swap lighting only, crowd blocks fully static, bulb chase held |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 40 per frame (proposed range 35–45)
- **Memory Footprint:** 35 MB maximum
- **Particle Limit:** 40 (spotlight dust 12 + ambient 8 baseline; confetti burst 40 REPLACES ambient systems, never stacks)

> **Note:** The source location profile (`the_standing_ovation.md`) states no performance budget. The figures above are proposed defaults against the project-standard 60 FPS mobile target and should be ratified (or adjusted) by the tech art lead before asset production locks.

### Performance Notes:
- Confetti replaces ambient particles (spotlight dust, fall loop) rather than stacking — hard swap at burst trigger
- Per-beer lighting shifts are palette/CanvasModulate swaps, not shaders, on low-end devices
- Green Room sprites load on-demand (brewery tour and stamp ceremony only)
- Crowd applause animates nearest 6–10 patrons; silhouette blocks and balcony rows are static
- House Dim Overlay is a single multiply quad, not a lighting pass

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for Herr Dramatisch, stagehands, and patron escalation tiers
- CPUParticles2D (not GPU) for confetti, spotlight dust, foam
- CanvasModulate + gel swatches for per-beer lighting states; PointLight2D only on High LOD for the follow spot
- CanvasLayer for applause meter, toast UI, and results cards
- Location state machine: `house_neutral → spotlight_active → judging → ovation | booed → stamp_ceremony` drives sprite set swaps
- Marquee letter board is a TileMap strip fed by the current `now_pouring` beer string

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Spotlight lock (sweep F3) | Spotlight hum begins | On lock frame; hum glyph appears same frame |
| Applause escalation tiers | Applause scaled to performance | Loop start per tier; glyph burst size matches |
| Herr Dramatisch verdict F2 | Dramatic sting | On F2; sting flash same frame |
| Booed Off trigger | Sad trombone | At results card display; trombone glyph for full 1.5s |
| Confetti burst F1 | Triumphant brass | On F1; brass glyph same frame |
| Stamp anim F4 | Applause sound | Exactly on stamp contact; stamp applause glyph same frame |
| Bottle opener use | Tiny applause click | On glyph pop |
| Intermission bell pulses | Chime x3 | Per swing; ring glyph mirrors each |
| Pour flourish F3 | Dramatic sting | At apex hold |
| Curtain exit F1 | Fabric whoosh + applause swell | Whoosh F1, swell F2 |
| Applause meter zone change | Soft tick | On zone boundary; zone icon pulses |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Bravo Challenge (stamp unlock) | Spotlight system, toast UI, applause meter, crowd escalation, stamp ceremony set | Order signature beer → spotlight finds player → toast choice → judgment → ceremonial drink → bow → stamp at Green Room podium |
| The Standing Ovation Challenge (free opener) | Monologue timer bar, spotlight narrow cone, Herr Dramatisch judging set, opener + free Curtain Call Copper presentation | 60-second beer-themed monologue; success grants opener sprite + Free Copper Presentation pose |
| Encore Performance | Toast UI with Charm check icon, enthusiastic/ovation tiers | Return visit with higher Charm re-runs judgment at improved odds |
| The Critics' Favorite | Critics' full set: assessing, scribbling, slow clap, won over, score placards | Perfect scores from all House Critics; placards display PERFECTION |
| Achievements (First Bow / Standing Ovation / Booed Off [hidden] / Regular Performer / Critics' Darling) | Results cards, Encore! icon, Booed Off icon, selfie variants | Achievement toasts reuse results-card art; "Booed Off" hidden achievement uses the "Tough Crowd" selfie variant |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bassline Opera House | Opera-goer patron sprites (gown/tails) shared; post-show queue silhouettes | Post-performance crowd influx at 22:00; standard street transition |
| The Moderato Pub | Moderato Pub Researcher patron (tempo-faction "research" visits) | Standard door transition; researcher notes pour tempo |
| Baroness' Ballroom | Performance-culture overlap — applause escalation frames reusable for ballroom reactions | None (shared atlas region) |
| Brewery Tour (Sinfonia) | Stamp progress pip #2, passport page, Bravissimo stamp | Persistent passport UI CanvasLayer |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "An opera house that happens to serve beer — and refuses to acknowledge the difference"
- **Color Mood:** Theater Black swallowing everything except what the gold light chooses to bless; Curtain Red as constant velvet pressure
- **Lighting:** The location's true protagonist — follow spots, footlights, per-beer gel washes; Green Room's flat fluorescence is the deliberate anti-punchline
- **Texture:** Worn velvet, scuffed stage boards, polished brass and copper; backstage honesty in raw concrete and steel

### Environmental Storytelling:
- Front of house is pure theater; the Green Room reveals the trick — competent, unglamorous brewing with one gilded podium shipped in for stamps
- Self-written five-star reviews framed in gold; the trophy for commitment to the bit
- Applause signs installed ironically, now obeyed sincerely — the satire's thesis on one wall
- Red carpet worn thin down the center: everyone walks the same dramatic path to a beer
- "TEARS (ALLEGEDLY)" chalked on the understudy barrels — the house legend, half-disowned

### Character Integration Notes:
- **Herr Dramatisch:** Cape and mustache must read in silhouette at 48px; only two emotional poles exist and the sprite set enforces it
- **Stagehands:** Black on black by design — rim-light every edge; their stillness makes the pour flourish land
- **Critics:** Always elevated, always framed by the balcony rail; the slow clap is their entire character arc
- **Patrons:** The applause escalation set is the mini-game's true UI — the crowd is the meter

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Spotlight hitting the player mid-sip** — the universal "oh no, I'm the show now" moment
2. **Confetti burst + standing ovation** for a toast about beer — maximum ceremony, minimum stakes
3. **The "Tough Crowd" selfie** — slinking out of the spotlight past disappointed patrons (hidden achievement bait)
4. **Marquee reading "NOW POURING: THE UNDERSTUDY"** — the changeable letters doing quiet comedy
5. **Herr Dramatisch at maximum flourish apex**, one leg raised, stamping a beer passport like a declaration of war

### TikTok Potential:
- "POV: you ordered a beer and now there's a spotlight on you"
- "Rating my toast: the critics gave it a slow clap that turned real"
- "He said there's a DIFFERENCE between drinking and PERFORMING drinking"

### Quote Potential:
- "Welcome to The Standing Ovation! Here, we do not merely DRINK — we PERFORM drinking!" — Herr Dramatisch
- "For PERFORMING drinking a beer! There is a DIFFERENCE!" — Herr Dramatisch
- "A toast to statistical probability and fermentation science." — Bradley / "UNCONVENTIONAL! I LOVE IT!" — Herr Dramatisch
- "Derivative toast. We've heard that one before." — The House Critics
- "Your Curtain Call Copper, served precisely at the moment of maximum dramatic impact." — Stagehand

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | the_standing_ovation_exterior.png | 1024x512 |
| 2 | the_standing_ovation_tileset.png | 1024x1024 |
| 3 | herr_dramatisch.png | 512x512 |
| 4 | the_standing_ovation_npcs.png | 512x512 |
| 5 | the_standing_ovation_items.png | 512x256 |
| 6 | the_standing_ovation_effects.png | 512x512 |
| 7 | the_standing_ovation_ui.png | 512x256 |

**Total Estimated Memory:** ~10 MB uncompressed RGBA (2 + 4 + 1 + 1 + 0.5 + 1 + 0.5 MB at 4 bytes/pixel)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `the_standing_ovation_exterior.png` (1024x512)
- [ ] `the_standing_ovation_tileset.png` (1024x1024)
- [ ] `herr_dramatisch.png` (512x512)
- [ ] `the_standing_ovation_npcs.png` (512x512)
- [ ] `the_standing_ovation_items.png` (512x256)
- [ ] `the_standing_ovation_effects.png` (512x512)
- [ ] `the_standing_ovation_ui.png` (512x256)

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
- **Documentation:** Animation timing reference sheet + marquee letter-tile spacing guide + lighting gel state chart

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] Marquee letter tiles legible at game resolution; longest beer name fits the board
- [ ] Applause meter readable one-handed on a 5.5" mobile screen (needle + zone icons + fill all distinct)
- [ ] Herr Dramatisch's cape reads in silhouette at 48px — HC silhouette confirms
- [ ] Stagehands never disappear against Theater Black walls (rim-light pass verified)
- [ ] Applause escalation tiers distinguishable from each other at crowd distance
- [ ] Per-beer lighting gels distinct in brightness value, not hue alone
- [ ] Curtain-rise stamp animation frames sync to Herr Dramatisch stamp poses
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets — total theatrical commitment to an ordinary pint
- [ ] Green Room's deliberate flatness contrasts front-of-house drama
- [ ] Hidden areas/interactions have discoverable visual cues (Wings booth, tasting nook, stamp podium mark)
- [ ] Performance optimized (CPU particles, atlas limits respected, confetti replaces ambient)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices (spotlight moments frame the player center-stage)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Viennese opera culture evoked, never named |
| Cultural Specificity | ✅ | Viennese opera tradition, standing-ovation etiquette, critic culture applied to beer |
| Satirical Targets Appropriate | ✅ | Performance culture, applause addiction, craft-beer ceremony — punches at pretension, not people |
| Seedy Underbelly Present | ❌ | Honest gap: vice is soft here — self-written five-star reviews, self-appointed critics, and the buy-a-round Booed Off redemption are gag-level puffery, not a genuine exploitation economy. Acceptable as a lighter-shade location, but flagged per validation standard |
| Gameplay Value Established | ✅ | Toast mini-game, brewery stamp #2, six-beer shop with buffs, achievements, selfie spot |
| Technical Feasibility | ✅ | Seven sheets, atlas plan, LOD tiers, palette-swap lighting documented |
| Performance Budget | ✅ | 60 FPS, 40 draw calls, 35 MB, 40-particle cap — proposed defaults; source profile stated no budget (flagged in Performance & Assets) |
| Accessibility Features | ✅ | Visual cues for every audio event; static spotlight/confetti variants; HC silhouettes; pattern-coded meter |
| No Crypto Elements | ✅ | None present — pure theatrical satire |
| Social Media Integration | ✅ | Spotlight, ovation, and Booed Off moments identified; selfie variants specced |

**The Standing Ovation: where the player orders a beer and receives a starring role — and by the final bow, the applause they were mocking is the applause they came back for.**
