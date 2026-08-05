# Café NORA - Complete PNG Asset Requirements

## 📋 Overview
Café NORA is Publandia's most literary internet café — a Georgian shopfront named for James Joyce's muse and used almost exclusively for uploading selfies and answering ICQ pings from the Sauce Apostates. This document specifies every PNG required to render the collision between Dublin literary heritage and dial-up-era digital narcissism: the counter where Nora Fitzgerald judges your order, the eight vintage terminals, the contested power outlet, the bookshelf that exists to be photographed, and the one fake Joyce quote nobody has ever noticed.

**Location ID:** `publandia_services_cafe_nora_01`
**Theme:** Literary tourism as performance — high-culture aesthetic, low-culture usage
**Zone:** Cobblestone Market Street (cultural corner), Publandia
**Hours:** 8 AM - 2 AM (extended hours for "digital nomads")
**Primary Function:** Service hub — ICQ communication hub, selfie upload station, rumor ping receiver, coffee/pastry shop, terminal rental, "Regular" status progression

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Coffee Brown | #6F4E37 | Wood surfaces, counter, bookshelf, exterior trim |
| Literary Green | #2E5A1C | Signage script, awning, Celtic knot accents |
| Cream Paper | #FFFDD0 | Walls, menu boards, book pages, framed quotes |
| Tech Blue | #4169E1 | Screen glow, ICQ window, UI chrome, terminal desktops |
| Chalk White | #F8F8F0 | Chalkboard lettering, Wi-Fi password board |
| Rain Gray | #9FB4C7 | Misty street, rain-streaked windows, overcast light |
| Espresso Black | #2B1B12 | Coffee liquid, keyboard keys, night-mode shadows |
| Selfie Flash Gold | #FFD966 | Camera flash, viral stamps, Influencer status glow |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/cafe_nora/
├── environment/
│   ├── cafe_nora_exterior.png
│   ├── cafe_nora_interior.png
│   ├── terminal_section.png
│   └── literary_corner.png
├── npcs/
│   ├── nora_fitzgerald.png
│   └── cafe_regulars.png
├── objects/
│   └── cafe_items_effects.png
├── effects/
│   └── (shared regions inside cafe_items_effects.png)
└── ui/
    ├── cafe_nora_ui.png
    └── cafe_nora_accessibility.png
```

---

## 🏪 Sprite Sheet 1: Exterior & Signage
**File:** `cafe_nora_exterior.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Coffee Brown brick warmth against Rain Gray mist; Literary Green script signage

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Georgian Shopfront | (0, 0) | 256x256 | Narrow brick facade, large sash windows, literary aesthetic with tech awkwardly bolted on |
| Cornice & Roofline | (256, 0) | 128x64 | Georgian cornice detail, chimney pot, damp slate |
| Chalkboard Special | (384, 0) | 64x96 | "Today's Special: Ulysses Blend & 1 Hour Free Browsing" — hand-chalked, slightly smudged |
| Small Print Plaque | (448, 0) | 64x96 | "Named for Nora Barnacle, Joyce's Muse (Ask Us About Her)" — brass, polished by no one |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign | (256, 64) | 128x48 | "CAFÉ NORA" in elegant Literary Green script |
| Subtitle Sign | (256, 112) | 128x32 | "Est. 2003 — Literary Tradition, Digital Future" |
| Window Decal Strip | (256, 144) | 128x32 | "FREE WI-FI • ESPRESSO • INTERNET TERMINALS" |
| Wi-Fi Symbol Decal | (256, 176) | 32x16 | Peeling vinyl Wi-Fi fan icon |
| Espresso Cup Decal | (288, 176) | 32x16 | Steaming cup silhouette |
| Celtic Knot Trim | (320, 176) | 64x16 | Repeating knotwork border strip |
| Awning | (256, 192) | 128x64 | Literary Green canvas, rain-darkened at the edges |
| Hanging Sign | (384, 96) | 64x64 | Wrought-iron bracket, swinging "Caife Nóra" board |
| Night Window Glow | (448, 96) | 64x64 | Warm interior light + Tech Blue screen glow for the 1 AM crowd |
| Rain-Streaked Window Overlay | (384, 160) | 128x96 | Streak texture laid over the shopfront glass in wet weather |

### Street Level:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Closed | (0, 256) | 64x96 | Painted Georgian door, brass letterbox |
| Door Open | (64, 256) | 64x96 | Same door, open — coffee smell implied |
| Cobblestone Street Tile | (128, 256) | 128x64 | Market Street cobbles, tileable |
| Misty Street Backdrop | (256, 256) | 256x128 | Rain Gray mist, neighboring shopfronts softened to silhouettes |
| Puddle Reflection | (128, 320) | 64x64 | Puddle catching the sign's green glow |
| Street Lamp | (192, 320) | 64x64 | Cast-iron lamp, halo in the mist |
| Window Box Flowers | (0, 352) | 128x32 | Defiantly cheerful against the drizzle |

### Technical Notes:
- Rain-Streaked Window Overlay is a separate alpha layer — toggled by weather state, static texture (no particle cost)
- Night Window Glow swaps in after 20:00 game time; simple sprite swap, no shader
- Hanging Sign gets a 2-frame sway only on high LOD

---

## ☕ Sprite Sheet 2: Interior — Counter & Laptop Lounge
**File:** `cafe_nora_interior.png`
**Dimensions:** 512x512 pixels

### Room Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wood Floor | (0, 0) | 256x128 | Warm boards, worn path from door to counter to terminals |
| Back Wall & Shelving | (0, 128) | 256x128 | Cream Paper walls, framed prints, cup shelves |
| Counter Front | (0, 256) | 256x64 | Coffee Brown wood panel, brass foot rail |
| Counter Top Detail | (0, 320) | 256x48 | Ring stains, tip jar, "ASK FOR THE PASSWORD" card stand |

### The Counter (The Gateway):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Espresso Machine | (256, 0) | 128x96 | Professional, chrome, LOUD — the room's true engine |
| Pastry Display Case | (384, 0) | 128x96 | Imported, overpriced — scones, brown bread, "Joyce's Favorite" cake |
| Coffee Grinder | (256, 96) | 64x64 | Hopper full of Ulysses Blend beans |
| Cash Register | (320, 96) | 64x64 | Modern till in a room pretending it's 1904 |
| Wi-Fi Password Chalkboard | (384, 96) | 128x64 | Current password (always a Joyce reference), erased hourly |
| Cup Pyramid | (256, 160) | 64x48 | Stacked cups, one chipped |
| Milk Jugs & Tamper | (256, 208) | 64x48 | Barista tools, steam-scalded |
| Coffee Menu Board | (320, 160) | 96x96 | All six drinks, chalk-lettered with literary flourishes |
| Headphone Rack | (416, 160) | 96x48 | Loaner headphones, "2 Sovs DEPOSIT" tag |
| Terminal Time Price Sign | (416, 208) | 96x48 | "3 Sovs / 30 MIN — DAY PASS 15 Sovs" |

### The Back Alcove (The Privacy):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Back Alcove Nook | (256, 256) | 256x112 | Slightly hidden seating where ICQ chats get personal and "work" happens (definition varies) |

### The Laptop Lounge (The Pretension):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Laptop Lounge Armchairs | (0, 368) | 256x96 | Comfortable mismatched seating for personal devices |
| The Contested Power Outlet | (256, 368) | 64x48 | Single wall outlet, faint scuff halo from years of territorial disputes |
| Outlet Claimed State | (320, 368) | 64x48 | Same outlet buried under the Digital Nomad's three chargers |
| Power Strip Spaghetti | (384, 368) | 128x48 | Extension lead chaos, fire-code adjacent |
| Lounge Low Table | (256, 416) | 128x96 | Coffee-ringed table with abandoned notebook (blank) |
| Reading Lamp Lit | (384, 416) | 64x48 | Warm pool of light |
| Reading Lamp Off | (384, 464) | 64x48 | Off state for day scenes |
| Framed Celtic Print | (448, 416) | 64x48 | Knotwork print, purchased at an airport |
| Rain-Streaked Interior Window | (448, 464) | 64x48 | The street from inside, blurred by rain |
| Skirting & Trim Tiles | (0, 464) | 256x48 | Baseboard strips, cable-gnawed corner |

### Technical Notes:
- Wi-Fi Password Chalkboard text is drawn at runtime over the blank board region — the sprite ships with chalk smudge history only
- Outlet Claimed State is a direct swap keyed to Digital Nomad presence
- Espresso Machine pairs with steam burst effect (Sheet 7) and the hiss audio cue

---

## 💻 Sprite Sheet 3: Terminal Section & Back Alcove Fittings
**File:** `terminal_section.png`
**Dimensions:** 512x256 pixels

### Terminal States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terminal Off | (0, 0) | 64x64 | Dead CRT, dusty beige tower |
| Terminal Booting | (64, 0) | 64x64 | BIOS text crawl, vintage aesthetic |
| Terminal Desktop Live | (128, 0) | 64x64 | Functional hardware, teal desktop wallpaper |
| Terminal ICQ Open | (192, 0) | 64x64 | Green flower icon blooming on screen |
| Terminal Screensaver | (256, 0) | 64x64 | Flying books screensaver (Nora's touch) |
| Terminal Frozen | (320, 0) | 64x64 | Hourglass cursor, eternal |
| Privacy Screen | (384, 0) | 64x64 | Clip-on divider providing theoretical privacy |
| Headphones on Hook | (448, 0) | 64x64 | Deposit-secured loaner pair, desk-side |

### The Terminal Row:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terminal Row Bank | (0, 64) | 512x96 | All 8 desktops in a row, privacy screens between, cable loom behind |

### Alcove & Desk Fittings:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Desk Chair | (0, 160) | 64x96 | Squeaky swivel chair, one arm missing |
| Alcove Bench Seat | (64, 160) | 96x96 | Tucked-away cushioned bench for private pings |
| Alcove Curtain | (160, 160) | 64x96 | Half-drawn velvet curtain — "privacy" |
| Dial-Up Modem | (224, 160) | 64x48 | External modem, status LEDs, museum piece that still runs the hourly nostalgia tone |
| Mouse & Pad | (224, 208) | 64x48 | Ball mouse on a Publandia-map mousepad |
| CRT Glow Overlay | (288, 160) | 64x96 | Tech Blue screen light cast onto user and wall |
| Beige Keyboard | (352, 160) | 96x48 | Loud keys, shiny WASD from something unliterary |
| Cable Run | (352, 208) | 96x48 | Ethernet and power snaking along the skirting |
| Alcove Table & Candle | (448, 160) | 64x96 | Small table, one candle — atmosphere on a budget |

### Technical Notes:
- Terminal Row Bank renders once as background; individual 64x64 terminal states are stamped over each of the 8 desk positions per machine state
- CRT Glow Overlay uses additive blend at 40% opacity; disabled on Low LOD
- Dial-Up Modem LEDs animate only during the hourly dial-up moment

---

## 📚 Sprite Sheet 4: Literary Corner
**File:** `literary_corner.png`
**Dimensions:** 256x256 pixels

### The Aesthetic:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bookshelf | (0, 0) | 128x192 | Irish literature floor-to-shoulder — for photos, rarely read; spines pristine |
| Joyce Quotes Wall | (128, 0) | 128x96 | Framed quote gallery, 70% accurate, 100% photographed |
| The Fake Quote Frame | (128, 96) | 64x48 | The one quote Nora made up to see if anyone notices — no one has |
| Nora Barnacle Photo | (192, 96) | 64x96 | Real photo of the real Nora Barnacle; tourists ask "who's that?" |
| Fake Joyce Letter | (128, 144) | 64x48 | Handwritten "Joyce letter" — definitely fake, completely convincing |

### The Relics:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| First Edition Ulysses | (0, 192) | 64x64 | Reproduction under glass; tourists impressed anyway |
| Literary Map of Publandia | (64, 192) | 96x64 | Accurate, annotated, never once consulted |
| Reading Armchair | (160, 192) | 64x64 | Where people sit to look intellectual |
| Celtic Bookends & Bunting | (224, 192) | 32x64 | Knotwork bookends, faded Bloomsday bunting scrap |

### Technical Notes:
- The Fake Quote Frame is pixel-identical in style to the real frames — the gag only lands on examine (Area2D reveals Nora's confession dialogue)
- Nora Barnacle Photo doubles as the "Literary Publandia" quest trigger examine point
- Bookshelf spines must read as decorative from gameplay zoom; individual titles legible only in the selfie backdrop close-up

---

## 👩 Sprite Sheet 5: Nora Fitzgerald
**File:** `nora_fitzgerald.png`
**Dimensions:** 384x384 pixels

### Nora States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle Behind Counter | (0, 0) | 96x128 | Practical elegance, perpetual slight disappointment |
| Pouring Espresso | (96, 0) | 96x128 | Precise, unhurried, quietly excellent |
| Judging the Order | (192, 0) | 96x128 | One eyebrow, entire literature degree behind it |
| Handing Over Password | (288, 0) | 96x128 | Card extended — "It's a Joyce reference. Always is." |
| Recommending a Book | (0, 128) | 96x128 | Book offered, hope against evidence |
| Watching the Photographers | (96, 128) | 96x128 | Arms folded, watching someone shoot the bookshelf for ten minutes |
| Marking the Calendar | (192, 128) | 96x128 | Someone actually read a book today — first this week |
| 1 AM Real Talk | (288, 128) | 96x128 | Leaning on counter, guard down, night-shift honesty |

### Nora Expressions:
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Weary Warmth | (0, 256) | 48x48 | Default — warm but weary, hopeful but realistic |
| Slight Disappointment | (48, 256) | 48x48 | The house special |
| Flicker of Hope | (96, 256) | 48x48 | Someone touched a book |
| Deadpan | (144, 256) | 48x48 | For "what's Ulysses about" |
| Genuine Respect | (192, 256) | 48x48 | Reserved for honesty and actual readers |
| "He'd Definitely Judge" | (240, 256) | 48x48 | Wry, sideways, Joycean |

### Nora Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cardigan & Apron Texture | (288, 256) | 96x48 | Practical knitwear over barista apron |
| Name Tag & Pen | (0, 304) | 64x32 | "NORA" — yes, really |
| Password Card | (64, 304) | 64x32 | Hourly Wi-Fi card, chalk-dusted |
| Portafilter Hands | (128, 304) | 64x32 | Close-up for the pour animation |
| Framed Literature Degree | (192, 304) | 96x32 | Hung low, behind the register, where she can see it |
| Marked Calendar | (288, 304) | 96x32 | One red circle: "SOMEONE READ" |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Default | (0, 336) | 64x48 | Weary warmth for dialogue boxes |
| Portrait Weary | (64, 336) | 64x48 | For selfie hours |
| Portrait Hopeful | (128, 336) | 64x48 | For book recommendations |
| Portrait Respect | (192, 336) | 64x48 | For the Literary Achievement |
| Portrait Judging | (256, 336) | 64x48 | For Ulysses Blend orders from non-readers |
| Portrait Night Shift | (320, 336) | 64x48 | 1 AM, only the real ones left |

### Technical Notes:
- Nora carries the location's satire: every state must read "provides the aesthetic, accepts the reality" — no cartoon exasperation
- Marking the Calendar state pairs with the rare "someone actually reads" sound cue
- Portrait swaps driven by dialogue category (Welcome / Coffee Orders / Observations / Literary Moments / Digital Reality)

---

## 👥 Sprite Sheet 6: Café Regulars
**File:** `cafe_regulars.png`
**Dimensions:** 512x384 pixels

### Regular States (Row 1):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Struggling Writer Typing | (0, 0) | 64x96 | Furious typing, one 4-hour coffee, corner seat |
| Struggling Writer Deleting | (64, 0) | 64x96 | Holding backspace, soul leaving body |
| Digital Nomad On Call | (128, 0) | 64x96 | Three devices, video call, unclear profession |
| Digital Nomad Guarding Outlet | (192, 0) | 64x96 | Physically between you and the power |
| Joyce Enthusiast Waiting | (256, 0) | 64x96 | Literary corner, primed, scanning for eye contact |
| Joyce Enthusiast Explaining | (320, 0) | 64x96 | Mid-Penelope-episode, hands wide, audience leaving |
| Selfie Addict Posing | (384, 0) | 64x96 | Book held backwards, angle-hunting |
| Selfie Addict Rearranging Props | (448, 0) | 64x96 | Moving Nora's décor for the shot |

### Regular States (Row 2):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Scammer Response Haunted | (0, 96) | 64x96 | Fell for an ICQ scam, eyes that have seen the invoice |
| Scammer Response Warning | (64, 96) | 64x96 | Gripping a stranger's shoulder near the terminals |
| Generic Typing NPC A | (128, 96) | 64x96 | Background terminal user, hunched |
| Generic Typing NPC B | (192, 96) | 64x96 | Background terminal user, upright, two-finger typist |
| Generic Typing NPC C | (256, 96) | 64x96 | Background laptop user, headphones in |
| Silent Local Writer | (320, 96) | 64x96 | Actually working, silently judging everyone |
| Tourist With Book Prop | (384, 96) | 64x96 | Holding Ulysses like a clutch purse |
| Bro Uploading | (448, 96) | 64x96 | Mid-upload, feeling connected to Irish literature |

### Portraits & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Portrait Struggling Writer | (0, 192) | 64x48 | "200 pages written, 180 deleted. Progress." |
| Portrait Digital Nomad | (64, 192) | 64x48 | Disrupting the intersection of blockchain and the outlet |
| Portrait Joyce Enthusiast | (128, 192) | 64x48 | Wants to talk about it. All of it. |
| Portrait Selfie Addict | (192, 192) | 64x48 | Here for content, not coffee |
| Portrait Scammer Response | (256, 192) | 64x48 | "I know this VERY WELL now." |
| Laptop Sticker Detail | (320, 192) | 64x48 | Sticker-armored lid for the nomad's rig |
| Phone-in-Hand Detail | (384, 192) | 64x48 | Selfie grip close-up |
| Coffee Cup Nursing Detail | (448, 192) | 64x48 | The writer's single, sacred, cold americano |

### Animation Frames:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Typing Frame 1 | (0, 240) | 64x48 | Hands down |
| Typing Frame 2 | (64, 240) | 64x48 | Hands up |
| Typing Frame 3 | (128, 240) | 64x48 | Flourish keystroke |
| Typing Frame 4 | (192, 240) | 64x48 | Pause, stare, despair |
| Selfie Pose Frame 1 | (256, 240) | 64x48 | Casual |
| Selfie Pose Frame 2 | (320, 240) | 64x48 | Artistic |
| Selfie Pose Frame 3 | (384, 240) | 64x48 | Ironic |
| Delete-Everything Frame | (448, 240) | 64x48 | Backspace held, screen emptying |

### Group Clusters:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seated Silhouette Cluster | (0, 288) | 256x96 | Low-LOD crowd fill for busy hours |
| Video Call Gesture Cycle | (256, 288) | 128x96 | Two 64x96 frames of nomad gesticulation |
| Counter Queue Cluster | (384, 288) | 128x96 | Two-tourist queue, phones out |

### Technical Notes:
- Struggling Writer never leaves the corner seat — position is fixed, states swap in place
- Generic typing NPCs share the 4-frame typing hand cycle to keep animation memory flat
- Mobile builds cap ambient regulars at 4 visible (profile: reduced NPC count)

---

## 🥐 Sprite Sheet 7: Menu Items & Effects
**File:** `cafe_items_effects.png`
**Dimensions:** 256x256 pixels

### Coffee Menu Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Ulysses Blend (Espresso) | (0, 0) | 48x48 | 4 Sovs — +10 SP, +Focus; bold, like the book nobody's read |
| Dubliners Drip (Filter) | (48, 0) | 48x48 | 3 Sovs — +5 SP, +Stamina; honest filter coffee |
| Portrait of the Artist (Latte) | (96, 0) | 48x48 | 5 Sovs — +10 SP, +Creativity; foam art attempted |
| Finnegans Wake (Triple Shot) | (144, 0) | 48x48 | 6 Sovs — +20 SP, ++Speed, -Sleep later; enlightenment or palpitations |
| Nora's House Blend | (192, 0) | 48x48 | 4 Sovs — +8 SP, staff approval; her grandmother's recipe |

### Tea & Pastries:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Literary Tea Selection | (0, 48) | 48x48 | 3 Sovs — +5 SP, +Calm; leaves, not bags, obviously |
| Scone (Plain) | (48, 48) | 48x48 | 3 Sovs — +10 HP |
| Scone (With Jam) | (96, 48) | 48x48 | 4 Sovs — +15 HP |
| Brown Bread Toast | (144, 48) | 48x48 | 3 Sovs — +12 HP |
| "Joyce's Favorite" Cake | (192, 48) | 48x48 | 5 Sovs — +20 HP (Joyce never ate this) |

### Effect Icons:
| Icon | Position | Size | Description |
|------|----------|------|-------------|
| +SP Icon | (0, 96) | 32x32 | Coffee cup burst |
| +HP Icon | (32, 96) | 32x32 | Pastry heart |
| +Focus Icon | (64, 96) | 32x32 | Narrowed-eye glyph |
| +Creativity Icon | (96, 96) | 32x32 | Quill spark |
| ++Speed Icon | (128, 96) | 32x32 | Triple chevron, vibrating |
| Staff Approval Shamrock | (160, 96) | 32x32 | Nora-approved mark |
| +Calm Icon | (192, 96) | 32x32 | Steam spiral, serene |
| -Sleep Icon | (224, 96) | 32x32 | Crossed-out moon (Finnegans Wake debt) |

### Ambient Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Coffee Steam Frame 1 | (0, 128) | 16x32 | Wisp rising |
| Coffee Steam Frame 2 | (16, 128) | 16x32 | Wisp curling |
| Coffee Steam Frame 3 | (32, 128) | 16x32 | Wisp dispersing |
| Cup Steam Large | (48, 128) | 32x32 | Counter-scale steam plume |
| Dust Motes | (80, 128) | 32x32 | Floating particles in window light |
| Screen Glow Wash | (112, 128) | 64x32 | Tech Blue ambient cast for the terminal row |
| Keyboard Clack Burst | (176, 128) | 32x32 | Tiny impact tick above busy keys |
| Notification Spark | (208, 128) | 32x32 | ICQ ping glint |
| Camera Flash Sliver | (240, 128) | 16x32 | Edge flash for selfie captures |

### The Dial-Up Moment:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Dial-Up Moment Overlay | (0, 160) | 128x64 | Full-screen retro handshake visual — scan bars, connection meter, 1998 in sprite form |
| Modem Blink Frame 1 | (128, 160) | 32x32 | LEDs: RD on |
| Modem Blink Frame 2 | (160, 160) | 32x32 | LEDs: SD on |
| Modem Blink Frame 3 | (192, 160) | 32x32 | LEDs: all on, connected |
| Reading Lamp Glow | (224, 160) | 32x32 | Warm halo overlay |
| Window Rain Streak Loop | (128, 192) | 64x32 | Two-frame trickle for interior windows |
| Espresso Steam Burst | (192, 192) | 64x32 | Machine hiss plume, synced to grind-and-hiss audio |

### Rare & Social Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| "Someone Actually Reads" Sparkle | (0, 224) | 32x32 | Soft golden shimmer over an opened book — the rarest effect in Publandia |
| Page Turn Glint | (32, 224) | 32x32 | Companion glint for the reading moment |
| Selfie Flash Burst | (64, 224) | 32x32 | Selfie Flash Gold pop |
| Upload Success Ping | (96, 224) | 32x32 | Rising checkmark twinkle |
| ICQ Note Pop | (128, 224) | 32x32 | Green flower petal burst |
| Judgment Aura | (160, 224) | 32x32 | Faint gray shimmer around Nora during Judging state |
| Mist Drift Overlay | (192, 224) | 64x32 | Slow street-mist band for exterior scenes |

### Technical Notes:
- All effects run through CPUParticles2D or 2-3 frame sprite cycles — nothing requires GPU particles
- Dial-Up Moment Overlay plays hourly as the café's "feature"; it is an overlay animation, not a shader
- "Someone Actually Reads" Sparkle is quest-gated (The Ulysses Challenge) — treat as premium polish

---

## 🖥️ Sprite Sheet 8: UI Elements
**File:** `cafe_nora_ui.png`
**Dimensions:** 512x512 pixels

### Terminal & Chat:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Computer Terminal Desktop | (0, 0) | 256x192 | Full desktop interface — teal wallpaper, ICQ shortcut, browser, recycle bin |
| ICQ Chat Window | (256, 0) | 192x256 | Message interface, contact list (Sauce Apostates pinned), flower logo |
| ICQ Flower Online | (448, 0) | 64x64 | Green flower status bloom |
| ICQ Uh-Oh Burst | (448, 64) | 64x64 | The notification moment, visualized |

### Status Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Liked Status Icon | (448, 128) | 32x32 | Minor fame — NPCs occasionally recognize you |
| Influencer Status Icon | (480, 128) | 32x32 | Temporary fame, Selfie Flash Gold ring, insufferable |
| Wi-Fi Signal Icon | (448, 160) | 32x32 | "Literary pace" bars |
| New Mail Icon | (480, 160) | 32x32 | Rumor ping carrier |
| Hourglass Cursor | (448, 192) | 32x32 | For frozen terminals |
| Dial-Up Handshake Icon | (480, 192) | 32x32 | Connection-in-progress glyph |
| Scam Alert Flag | (448, 224) | 32x32 | Experienced-traveler warning marker |
| Nigerian Prince Crown | (480, 224) | 32x32 | Obviously fake; can play along |

### Menus & Passes:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Coffee Menu UI | (0, 192) | 192x256 | Order screen — six drinks, four pastries, prices, effects |
| Regular Status Stamp Card | (192, 192) | 64x64 | Five-visit punch card; fifth stamp unlocks the staff bathroom |
| Hourly Password Ticket | (192, 256) | 64x96 | Printed Wi-Fi ticket, Joyce reference of the hour |
| Bravado +N Popup | (192, 352) | 64x48 | Floating Bravado gain number |
| Upload Progress Bar | (192, 400) | 64x48 | Tileable segment, agonizingly slow fill |

### Selfie System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Selfie Upload UI | (256, 256) | 256x192 | Upload screen — backdrop, pose, filter, caption fields |
| Quality Stamp: Poor | (0, 448) | 48x64 | +5 Bravado, 1 hour |
| Quality Stamp: Average | (48, 448) | 48x64 | +10 Bravado, 2 hours |
| Quality Stamp: Good | (96, 448) | 48x64 | +15 Bravado, "Liked" status |
| Quality Stamp: Viral | (144, 448) | 48x64 | +25 Bravado, gold burst, "Influencer" status |
| Rumor Ping Popup | (192, 448) | 160x64 | Quest hint window — Street Intel / Rival Watch / Hot Tips / Scam Alerts / Literary Secrets |
| Wi-Fi Password Board (UI) | (352, 448) | 96x64 | Readable close-up of the hourly password board |
| Selfie Caption Input | (448, 448) | 64x64 | Caption field with engagement meter tick |

### Technical Notes:
- ICQ Chat Window and Rumor Ping Popup are 9-slice friendly — keep 8px uniform borders
- Quality Stamps slam onto the Selfie Quality Result with a 0.2s scale bounce
- All tappable UI regions ship at or above 44px minimum touch dimension at render scale

---

## 🎬 Animation Specifications

### Nora Idle Cycle:
- **Duration:** 12 seconds loop
- **Frames:** 5 states (Idle 5s → Wipe counter 2s → Glance at bookshelf 2s → Slight Disappointment 1s → Idle 2s)
- **Pattern:** Idle → wipe → glance → expression → return, loop
- **Trigger:** Constant while Nora is at the counter
- **Purpose:** Sells "warm but weary" without a word of dialogue
- **Audio Sync:** Soft cup placement on the wipe beat
- **Performance Optimization:** Drop glance/expression beats on Low LOD; 2-state loop

### Espresso Pour:
- **Duration:** 2.5 seconds
- **Frames:** 6 (grind → tamp → lock → pour → steam → serve)
- **Pattern:** Linear one-shot, no loop
- **Trigger:** Any coffee purchase
- **Purpose:** The one genuinely excellent craft in the room
- **Audio Sync:** Grinder growl on frame 1, machine hiss on frames 4-5, cup clink on frame 6
- **Performance Optimization:** 3-frame version (grind → pour → serve)

### Coffee Steam:
- **Duration:** 1.2 seconds loop
- **Frames:** 3 (rise → curl → disperse)
- **Pattern:** 1 → 2 → 3 → loop with slight x-drift
- **Trigger:** Constant on any served cup; despawns after 60s
- **Purpose:** Warmth and café atmosphere
- **Audio Sync:** None
- **Performance Optimization:** Static Cup Steam Large sprite on Low LOD

### Typing NPCs:
- **Duration:** 0.8 seconds loop per cycle
- **Frames:** 4 (hands down → up → flourish → despair pause)
- **Pattern:** 1 → 2 → 3 → 1 → 2 → 4, loop; Struggling Writer inserts Delete-Everything Frame every 5th cycle
- **Trigger:** Constant for seated terminal/laptop NPCs
- **Purpose:** Vigorous typing producing nothing — the café's heartbeat
- **Audio Sync:** Keyboard clicking layer volume scales with visible typist count
- **Performance Optimization:** Only 2 NPCs animate simultaneously; others hold Frame 1

### Screen Flicker:
- **Duration:** 0.3 seconds, random intervals 20-45 seconds
- **Frames:** 3 (normal → dim → normal)
- **Pattern:** Quick single dip via alpha toggle
- **Trigger:** Timer per powered terminal
- **Purpose:** Vintage hardware authenticity
- **Audio Sync:** None
- **Performance Optimization:** Disabled below Medium LOD; disabled entirely in reduced-motion mode

### The Dial-Up Moment:
- **Duration:** 6 seconds
- **Frames:** 8 overlay frames + 3 modem LED frames
- **Pattern:** Overlay scan bars fill left to right; modem LEDs cycle 1 → 2 → 3 and hold
- **Trigger:** Hourly timer (the café's advertised "nostalgia feature")
- **Purpose:** The location's signature gag — everyone pauses reverently for a sound from 1998
- **Audio Sync:** Full dial-up tone; connection meter completes exactly on the final screech
- **Performance Optimization:** 3-frame reduced overlay, LEDs static on frame 3

### ICQ Notification Popup:
- **Duration:** 1.0 second
- **Frames:** 4 (pop → bloom → settle → idle)
- **Pattern:** Scale bounce then hold until dismissed
- **Trigger:** ICQ event roll (Sauce Apostates ping, scammer contact, rival sighting, hot tip)
- **Purpose:** Comedy delivery vehicle and quest hook
- **Audio Sync:** ICQ "uh-oh" on frame 1
- **Performance Optimization:** 2-frame pop, no bloom

### Selfie Pose & Capture:
- **Duration:** 3 seconds
- **Frames:** 3 pose frames + 1 flash frame
- **Pattern:** Casual → Artistic → Ironic (player choice locks a frame) → flash
- **Trigger:** Player uses Selfie Upload at any backdrop (literary corner grants quality bonus)
- **Purpose:** The core delusion loop — culture as backdrop
- **Audio Sync:** Shutter click on flash frame
- **Performance Optimization:** Flash burst reduced to single sprite, no screen-wide white

### Upload Progress & Success:
- **Duration:** 2-4 seconds (varies by "literary pace" connection)
- **Frames:** Progress bar fill + 2-frame success ping
- **Pattern:** Fill (stutters at 80% for comedic beat) → ping
- **Trigger:** Selfie upload confirm
- **Purpose:** Tension → validation → Bravado
- **Audio Sync:** Upload success chime on ping frame 1
- **Performance Optimization:** Fixed 2-second fill, no stutter beat

### Dust Motes:
- **Duration:** 8 seconds drift loop
- **Frames:** 1 (particle sprite, CPU-driven drift)
- **Pattern:** Slow diagonal drift through window light volume
- **Trigger:** Constant during daylight hours
- **Purpose:** "Intellectual atmosphere" in particle form
- **Audio Sync:** None
- **Performance Optimization:** 6 motes max on Medium, off on Low

### Rumor Ping Arrival:
- **Duration:** 1.5 seconds
- **Frames:** 3 (New Mail icon shake → popup slide → settle)
- **Pattern:** Shake ×2 → slide up → hold
- **Trigger:** Rumor system event while player is in the back alcove or at a terminal
- **Purpose:** Quest hint delivery with tabloid energy
- **Audio Sync:** Soft mail chime on shake
- **Performance Optimization:** Slide replaced with instant show

### "Someone Actually Reads":
- **Duration:** 2 seconds
- **Frames:** 4 (book opens → sparkle → page glint → fade)
- **Pattern:** One-shot, never loops — that would be unrealistic
- **Trigger:** The Ulysses Challenge read action; also fires on the Silent Local Writer once per real-time hour
- **Purpose:** The rarest, most sacred event in Café NORA
- **Audio Sync:** The rare "someone actually reads" chime, exactly once
- **Performance Optimization:** None needed (event is too rare to budget for)

---

## ♿ Accessibility Sprite Requirements
**File:** `cafe_nora_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Order Outline | (0, 0) | 64x64 | White-on-dark outline for Nora's order hotspot |
| Terminal Rental Outline | (64, 0) | 64x64 | Bold outline over the terminal-time purchase point |
| Bookshelf Examine Outline | (128, 0) | 64x64 | High-visibility literary corner hotspot (includes fake quote frame) |
| Power Outlet Outline | (192, 0) | 64x64 | The contested outlet, finally visible to everyone |
| ICQ Window Bold | (0, 64) | 96x64 | Thick-bordered chat window with enlarged message text |
| Selfie Upload Button Bold | (96, 64) | 96x64 | Oversized upload confirm with heavy outline |
| Rumor Ping Bold | (192, 64) | 64x64 | High-contrast popup variant with icon-coded rumor category |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Screen Flicker, Steady | (0, 128) | 48x48 | Constant-brightness terminal screens — flicker timer disabled |
| Steam, Static | (48, 128) | 48x48 | Fixed steam wisp replacing the 3-frame cycle and CPU drift |
| Dial-Up Moment, Reduced | (96, 128) | 96x48 | Static "CONNECTING…" card replacing the 6-second scan-bar overlay — audio still plays, screen holds still |
| Dust Motes, Off | (192, 128) | 64x48 | Clean window-light beam with particles removed |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Espresso Hiss Lines | (0, 176) | 32x32 | Steam-line burst over the machine (replaces hissing/grinding audio) |
| ICQ Uh-Oh Flash | (32, 176) | 32x32 | Green flower double-pulse for the notification sound |
| Dial-Up Handshake Bars | (64, 176) | 32x32 | Rising signal bars tracking the full dial-up tone |
| Selfie Shutter Icon | (96, 176) | 32x32 | Aperture snap glyph on capture |
| Upload Success Check | (128, 176) | 32x32 | Checkmark bloom for the upload success chime |
| Keyboard Ripple | (160, 176) | 32x32 | Soft concentric ticks above active typists (replaces constant clicking) |
| Reading Chime Sparkle | (192, 176) | 32x32 | Gold book glyph for the rare "someone actually reads" sound |
| Cup Placement Tick | (224, 176) | 32x32 | Small ring pulse when coffee lands on the counter |

### Caption & Touch Support:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ambient Caption Bar | (0, 208) | 256x32 | Strip for soft-jazz / murmur / busy-hour ambience captions |
| 44px Touch Grid Ruler | (0, 240) | 256x16 | QA reference strip verifying minimum touch target sizing |

### Colorblind Considerations:
- Selfie quality tiers (Poor/Average/Good/Viral) never rely on color alone — each stamp has a distinct shape (dash / circle / star / burst)
- Coffee effect icons pair every color with a unique glyph silhouette (chevrons, heart, quill, moon)
- ICQ status and rumor categories are icon-coded (flower, flag, crown, mail), not color-coded
- All interactive elements — order hotspot, terminal rental, selfie upload, ICQ window, rumor popups, menu rows — meet the 44px minimum touch target

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) `cafe_nora_ui.png` kept uncompressed — chat text and password board must stay legible with alpha across all sheets
- **Fallback:** Lossless PNG for `literary_corner.png` and `cafe_nora_ui.png` — the fake quote gag and ICQ text are detail-critical

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cafe_nora_environment | exterior, interior, terminal_section, literary_corner | 2048x2048 |
| cafe_nora_characters | nora_fitzgerald, cafe_regulars | 1024x1024 |
| cafe_nora_ui_fx | cafe_nora_ui, cafe_items_effects, cafe_nora_accessibility | 1024x1024 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full steam/dust/flicker, all 8 terminals animated, 6+ ambient NPCs, full dial-up overlay |
| Medium | Steam 3-frame only, 6 dust motes, flicker off, 4 ambient NPCs, 2 simultaneous typists |
| Low | Static steam sprite, no dust, no flicker, seated silhouette clusters replace individual NPCs, reduced dial-up card |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 12 per frame (per the location's performance budget)
- **Memory Footprint:** 30 MB maximum
- **Particle Limit:** 20 (steam + dust + notification sparks combined)

### Performance Notes:
- Simplified terminal section on mobile: Terminal Row Bank renders as one sprite, individual screen states stamped only for the 3 nearest machines
- Ambient NPC count reduced per platform considerations; typing audio layer scales with visible typists so audio and animation never desync
- ICQ window, selfie UI, and rumor popups are 9-slice — one texture each regardless of screen size
- Dial-up overlay preloads with the scene; it fires hourly and must never hitch

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap for cobblestone street and interior floor; ParallaxBackground for the misty Market Street backdrop
- CPUParticles2D (not GPU) for coffee steam, dust motes, and notification sparks — 20-particle combined cap; screen flicker via alpha toggle timers, disabled in reduced-motion mode
- Area2D examine points: bookshelf, Joyce quotes wall (fake quote reveal), Nora Barnacle photo, fake Joyce letter, first edition Ulysses, literary map, contested power outlet, dial-up modem
- Terminal state machine per machine (off → booting → desktop → ICQ/screensaver/frozen); hourly timers drive the Wi-Fi password change and the dial-up moment
- State tracking per `cafe_nora_state` (visits_count, regular_status, selfies_uploaded, viral_achieved, icq_scam_answered, read_something, rumor_pings_found, current_wifi_password_index)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Espresso Pour (2.5s) | Machine hissing + grinding | Grinder on frame 1, hiss on frames 4-5, cup clink on serve |
| ICQ Notification Popup | ICQ "uh-oh" notification sound | On pop frame 1, every ping |
| Dial-Up Moment Overlay (6s) | Full dial-up tone (hourly "feature") | Tone spans the overlay; meter completes on the final screech |
| Selfie flash frame | Selfie capture shutter click | On flash frame |
| Upload Success Ping | Upload success chime | On ping frame 1, after the 80% stutter beat |
| Typing NPC cycles | Keyboard clicking (constant ambient) | Layer volume tracks visible typist count |
| "Someone Actually Reads" (2s) | The rare literary moment chime | On sparkle frame — once, reverently |
| Cup on counter | Coffee cup placement | On Nora's serve/wipe beats |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Ulysses Challenge | Bookshelf, First Edition Ulysses, "Someone Actually Reads" sparkle, Page Turn Glint, Nora Marking the Calendar state, Portrait Respect | Actually read something Joyce wrote (harder than it sounds); success fires the rarest effect and +20 Bravado with Nora's genuine respect |
| Scammer Showdown | ICQ Chat Window, Nigerian Prince Crown, Scam Alert Flag, Scammer Response NPC states, ICQ Uh-Oh Burst | Navigate an ICQ scam for comedy or profit; the Scammer Response NPC hovers as living warning |
| Viral Moment | Selfie Upload UI, Selfie Pose Frames, Quality Stamp: Viral, Influencer Status Icon, Selfie Flash Burst | Achieve viral selfie status; literary corner backdrop grants the quality bonus |
| Literary Publandia | Literary Map of Publandia, Nora Barnacle Photo, Joyce Quotes Wall, Rumor Ping Popup (Literary Secrets) | Visit all Joyce-related spots — triggered from the literary corner examine; Nora's rare Literary Secrets pings mark the map |
| Regular Status | Regular Status Stamp Card, Portrait Night Shift, Hourly Password Ticket | 5 visits with purchases: 10% off terminals, free 15 minutes, Nora remembers your name, staff bathroom access (significant upgrade) |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Blarney Trap | Rumor Ping Popup cross-references both locations' rumors | Shared rumor UI skin; ping arrival chime identical in both venues |
| Craic Broker Network | Hot Tips category in Rumor Ping Popup, New Mail Icon | Rumor network overlap — broker tips route through the café's inbox |
| Sauce Apostates ICQ Hub | ICQ Chat Window, ICQ Flower Online, pinned contact list | Café NORA is the primary Publandia ICQ hub; global network messages land here |
| All Publandia Locations | Selfie Upload UI + Quality Stamps | Selfies taken anywhere in Publandia upload here; backdrop metadata feeds the quality roll |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Digital culture in literary drag — a Georgian shopfront where Joyce's ghost watches selfie uploads"
- **Color Mood:** Coffee Brown and Cream Paper warmth undercut by Tech Blue screen glow; Rain Gray mist pressing at the windows; Selfie Flash Gold as the vulgar accent
- **Lighting:** Warm café lamps and reading lights against cold CRT glow; night scenes lit almost entirely by screens and one candle in the alcove
- **Texture:** Polished wood and pristine book spines (unread) against yellowed keyboards, thumb-worn phones, and chalk dust

### Environmental Storytelling:
- The bookshelf spines are perfect because no hand has ever disturbed them — the wear is on the floor in front of it, where photographers stand
- The fake Joyce quote hangs in plain sight among the real ones; the fake handwritten letter fools everyone; the real Nora Barnacle photo goes unrecognized — authenticity and forgery swapped values at the door
- The contested power outlet's scuff halo, the writer's single cold coffee, the modem kept alive as a shrine — every prop is the gap between what people think they're doing and what they're doing
- The literary map of Publandia: accurate, framed, never consulted

### Character Integration Notes:
- Nora Fitzgerald is the room's conscience: practical elegance, perpetual slight disappointment, never cartoon contempt — she provides the aesthetic and accepts the reality
- The regulars are a taxonomy of café delusion: the writer who works, the nomad who "works," the enthusiast who read everything, the addict who reads nothing — render each with equal dignity; the satire is in the behavior, not the drawing
- Generic typists share silhouettes and the 4-frame hand cycle; the Silent Local Writer alone gets the once-hourly reading sparkle

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Fake Quote Frame** - One made-up Joyce quote hiding among the real ones, unnoticed since 2003
2. **The Dial-Up Moment** - The whole café pausing reverently for the hourly 1998 handshake screech
3. **Selfie With Unread Books** - The Selfie Addict holding Ulysses backwards in perfect literary-corner light
4. **The Contested Power Outlet** - One outlet, three chargers, zero mercy
5. **Nora Marking the Calendar** - "Someone actually read a book today" gets a red circle
6. **The Viral Stamp** - Gold burst, Influencer status, insufferable dialogue options unlocked

### Quote Potential:
- "Ulysses Blend? Bold choice. Like the book. Have you read it? ...no one has."
- "The Joyce quotes on the wall? Mostly accurate. I made up one to see if anyone notices. No one has."
- "I opened this café to promote literature. Now I provide Wi-Fi for selfies. Joyce would appreciate the irony. He loved irony."
- "You've been photographing the bookshelf for ten minutes. Feel free to actually take one down."
- "The Nigerian prince isn't real. I know this now. I know this VERY WELL now."
- "I've written 200 pages. Deleted 180. That's progress. I think."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | cafe_nora_exterior.png | 512x384 |
| 2 | cafe_nora_interior.png | 512x512 |
| 3 | terminal_section.png | 512x256 |
| 4 | literary_corner.png | 256x256 |
| 5 | nora_fitzgerald.png | 384x384 |
| 6 | cafe_regulars.png | 512x384 |
| 7 | cafe_items_effects.png | 256x256 |
| 8 | cafe_nora_ui.png | 512x512 |

**Total Estimated Memory:** ~16 MB (in-atlas, mipmapped, before platform compression)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `cafe_nora_exterior.png` (512x384)
- [ ] `cafe_nora_interior.png` (512x512)
- [ ] `terminal_section.png` (512x256)
- [ ] `literary_corner.png` (256x256)
- [ ] `nora_fitzgerald.png` (384x384)
- [ ] `cafe_regulars.png` (512x384)
- [ ] `cafe_items_effects.png` (256x256)
- [ ] `cafe_nora_ui.png` (512x512)
- [ ] `cafe_nora_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (Joyce quote frames on separate layers — the fake quote must remain swappable; Wi-Fi chalkboard text on its own layer for runtime replacement)
- **Documentation:** Animation timing reference sheet (Nora idle cycle, 2.5s espresso pour, 6s dial-up moment, hourly timers)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Coffee Brown #6F4E37, Literary Green #2E5A1C, Cream Paper #FFFDD0, Tech Blue #4169E1)
- [ ] The fake Joyce quote frame is stylistically indistinguishable from the real frames — the gag only works if artists can't tell either
- [ ] The real Nora Barnacle photo reads as a genuine period photograph, not a game prop
- [ ] Dial-Up Moment overlay lands the 1998 nostalgia at full and reduced-motion fidelity
- [ ] Selfie-with-unread-books composition works: bookshelf spines pristine, floor wear in front of it, Ulysses holdable backwards
- [ ] Accessibility visual alternatives included for all audio cues (espresso hiss, ICQ uh-oh, dial-up tone, shutter/upload chime, keyboard clicking, reading chime)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (literary tourism as performance, pretension without substance) is clear throughout all assets
- [ ] Easter eggs discoverable: fake quote, fake Joyce letter, reproduction Ulysses, never-consulted literary map, the marked calendar
- [ ] Performance optimized (CPU particles capped at 20, 12 draw calls, silhouette crowd clusters, 9-slice UI)
- [ ] Touch zone sizing considered (44px minimum — order hotspot, terminal rental, selfie upload, ICQ window, rumor popups)
- [ ] Colorblind-friendly alternatives available where color codes meaning (shape-coded quality stamps, glyph-coded effect icons, icon-coded rumor categories)
- [ ] Social media viral potential maximized (fake quote framing, dial-up moment composition, contested outlet tableau)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only — "Dublin literary brand" satirized via Publandia's cultural corner, no real city named in-world assets |
| Cultural Specificity | ✅ | Joyce worship without Joyce reading; Nora Barnacle heritage; Irish literary tourism culture |
| Satirical Targets Appropriate | ✅ | Tourists, bros, digital nomads, and selfie culture — never Irish literature or locals; actual writers are treated with dignity |
| Seedy Underbelly Present | ✅ | Pretension without substance — exploiting literary heritage for Wi-Fi fees; ICQ scam ecosystem in the back alcove |
| Gameplay Value Established | ✅ | ICQ hub, selfie/Bravado system, rumor pings, consumables, Regular progression, five quest hooks |
| Technical Feasibility | ✅ | Godot 4.x, top-left origin, CPUParticles2D, alpha-toggle flicker, 9-slice UI, state machines documented |
| Performance Budget | ✅ | 60 FPS target, 12 draw calls, 30 MB memory, 20-particle cap per the location's performance budget |
| Accessibility Features | ✅ | Visual cues for all six critical sounds, steady/static/reduced motion variants, 44px targets, shape-coded stamps |
| No Crypto Elements | ✅ | Passes — the Digital Nomad's "blockchain" line is satirical dialogue established in the source profile, not a game mechanic |
| Social Media Integration | ✅ | Six viral moments identified; selfie system is itself the satirical social-media loop |

---

**Café NORA delivers Eurobound's sharpest cultural gap in a single room: a Georgian shopfront consecrated to James Joyce and used to upload selfies over hourly-rotating Wi-Fi. Every asset serves the same joke from a different angle — the pristine unread spines, the fake quote nobody notices, the real muse nobody recognizes, the modem kept alive as a beloved relic, the one writer actually writing while everyone else photographs the idea of writing. When these PNGs land, the player enters seeking culture, photographs the bookshelf, uploads forty-seven selfies, and leaves feeling literary — having read nothing. Nora watches it all, marks her calendar on the rare day someone opens a book, and pours another Ulysses Blend for someone who thinks it's a movie.**

**"I opened this café to promote literature. Now I provide Wi-Fi for selfies. Joyce would appreciate the irony. He loved irony."**
