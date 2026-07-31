# Opera House Plaza - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Opera House Plaza location in Sinfonia. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this grand baroque plaza featuring the Fiaker Fiasco quest.

---

## 🎨 Sprite Sheet 1: Plaza Tileset
**File:** `opera_house_plaza_tileset.png`  
**Dimensions:** 1024x1024 pixels  
**Color Palette:** 
- Cobblestone Grey: #808080
- Cobblestone Dark: #696969
- Imperial Gold: #DAA520
- Baroque Cream: #F5F5DC
- Opera White: #FFFAFA
- Fountain Green (aged): #2F4F4F

### Cobblestone Tiles (32x32 each):
- **Cobble Standard** (0, 0, 32x32) - Base plaza cobblestone
- **Cobble Worn** (32, 0, 32x32) - Worn variant with subtle cracks
- **Cobble Wet** (64, 0, 32x32) - Rain-soaked cobblestone with reflections
- **Cobble Performer Circle** (96, 0, 32x32) - Decorative pattern marking performance area
- **Cobble Edge** (0, 32, 32x32) - Transition tile to grass/other surfaces
- **Cobble Corner** (32, 32, 32x32) - Corner piece for plaza boundaries

### Fountain Tiles:
- **Fountain Base NW** (256, 0, 64x64) - Northwest section of fountain base
- **Fountain Base NE** (320, 0, 64x64) - Northeast section
- **Fountain Base SW** (256, 64, 64x64) - Southwest section
- **Fountain Base SE** (320, 64, 64x64) - Southeast section
- **Neptune Statue** (384, 0, 96x128) - Central Neptune figure, baroque style, slightly green patina
- **Water Surface** (256, 128, 128x64) - Animated water surface

### Building Facade Tiles:
- **Opera Facade Section** (512, 0, 256x256) - Main opera house facade with columns
- **Opera Columns** (768, 0, 64x256) - Repeatable column element
- **Opera Entrance** (832, 0, 128x192) - Grand entrance doorway with steps
- **Baroque Building 1** (512, 256, 128x192) - Generic baroque facade left
- **Baroque Building 2** (640, 256, 128x192) - Generic baroque facade right
- **Café Facade** (768, 256, 192x160) - Coffeehouse storefront with awning

### Props:
- **Bench Ornate** (0, 128, 64x32) - Habsburg-style ironwork bench
- **Lamppost Gas** (64, 128, 32x96) - Ornate gas lamp (lit state)
- **Signpost Gilded** (96, 128, 32x64) - Directional sign with German text
- **Queue Post** (128, 128, 16x48) - Numbered Fiaker queue marker
- **Café Table** (0, 192, 32x32) - White-clothed table (intact)
- **Café Chair** (32, 192, 24x32) - Matching café chair
- **Performer Hat** (56, 192, 24x16) - Velvet-lined violin case open
- **Opera Poster** (80, 192, 48x64) - "The Magic Flute" performance poster

---

## 🎭 Sprite Sheet 2: Character Sprites
**File:** `opera_plaza_characters.png`  
**Dimensions:** 2048x1024 pixels  
**Color Palette:**
- Fiaker Black: #1C1C1C
- Hans-Jürgen Red Face: #8B0000
- Gustav Bay: #964B00
- Opera Cape Red: #8B0000
- Formal White: #FFFFFF
- Brass Buttons: #B5A642

### Hans-Jürgen (64x96 base size):

**Idle Drunk** (6 frames, 2 FPS):
- (0-320, 96, 64x96 each) - Pronounced sway with flask sipping

**Panic** (8 frames, 8 FPS):
- (0-448, 192, 64x96 each) - Running in place, wild arm gestures, hat bouncing

**Relief Hug** (6 frames, 4 FPS):
- (0-480, 288, 96x96 each) - Bear hug animation with Gustav

**Confession** (4 frames, 1 FPS):
- (0-192, 384, 64x96 each) - Slumped against carriage

**Details:**
- Bowler Hat Askew (512, 0, 32x24)
- Schnapps Flask (544, 0, 16x32)
- Gustav Photo (560, 0, 24x32)

### Gustav Horse (128x96 base size):

**Eating** (6 frames, 2 FPS):
- (640-1280, 96, 128x96 each) - Munching stolen food

**Judgmental Stare** (2 frames, hold frame 1 for 3 seconds):
- (640-768, 192, 128x96 each) - Direct stare, ears back

**Escape Trot** (8 frames, 8 FPS):
- (640-1536, 288, 128x96 each) - Full trot cycle

**Considering Skittles** (4 frames, 1 FPS):
- (640-1024, 384, 128x96 each) - Head tilt, taking one Skittle

**Resigned Return** (6 frames, 2 FPS):
- (640-1280, 480, 128x96 each) - Heavy sigh, reluctant walk

**Accessories:**
- Opera Cape (1408, 0, 64x96) - Red cape overlay
- Harness Broken (1472, 0, 48x64) - Remnant pieces
- Sachertorte Crumbs (1520, 0, 24x16) - Muzzle overlay

### Supporting NPCs (48-64x80):
- Opera Usher states (0-96, 576)
- Café Maître D' states (144-240, 576)
- Street Performer playing (288-432, 576, 4 frames)
- Ticket Scalper states (480-528, 576)
- Pigeon Lady states (576-640, 576)
- Fiaker Driver Variants (704-848, 576)
- Opera Patrons (896-992, 576)

---

## ✨ Sprite Sheet 3: Environmental Effects
**File:** `opera_plaza_effects.png`  
**Dimensions:** 512x512 pixels  

### Fountain Water:
- **Spray** (0-448, 0, 64x64 each) - 8 frames, 8 FPS
- **Ripples** (0-144, 64, 48x48 each) - 4 frames, 4 FPS

### Pigeons:
- **Pecking** (0-120, 128, 24x24 each) - 6 frames, 6 FPS
- **Flying** (0-224, 152, 32x32 each) - 8 frames, 12 FPS

### Gas Lamp Glow:
- (0-144, 200, 48x48 each) - 4 frames, 2 FPS

### Table Destruction:
- (0-320, 256, 64x64 each) - 6 frames, 12 FPS, no loop

---

## 🐴 Sprite Sheet 4: Fiaker Carriage
**File:** `fiaker_carriage.png`  
**Dimensions:** 512x256 pixels  

- **Idle** (0, 0, 192x128) - Empty carriage at rest
- **Horse Attached** (192, 0, 256x128) - Carriage with horse
- **Empty No Horse** (0, 128, 192x128) - Abandoned, harness dangling

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Gustav in Opera Cape** - Horse wearing stolen red cape, judging the viewer
2. **Hans-Jürgen's Panic Face** - Red-faced, hat flying, arms flailing
3. **Table Destruction Mid-Frame** - Sachertorte flying through air
4. **Judgmental Stare Close-Up** - Gustav's expression is internet gold

---

## 📦 File Delivery Checklist

### Required PNG Files (4 Total):
- [ ] `opera_house_plaza_tileset.png` (1024x1024)
- [ ] `opera_plaza_characters.png` (2048x1024)
- [ ] `opera_plaza_effects.png` (512x512)
- [ ] `fiaker_carriage.png` (512x256)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG
- **Naming Convention:** snake_case, all lowercase

**Opera House Plaza brings the refined chaos of high culture colliding with American tourist energy—where a drunk Fiaker driver's worst day becomes the bros' most memorable adventure.**
