# Item Definition: Clock Energy Wine

*"Infused with temporal energy. Very popular with ladies."*

## 📦 Item Identity
- **Item ID**: `item_clock_energy_wine`
- **Display Name**: Clock Energy Wine
- **Internal Name**: Boxed Wine in Fancy Bottle
- **Item Type**: Consumable / Scam Product
- **Rarity**: Common (despite vendor claims)
- **Stack Size**: 6 max

---

## 🎭 Core Concept

### What It Actually Is
€3 boxed wine (generic Franzia-equivalent) poured into fancy glass bottles with handmade "vintage" labels. The vendor claims it's infused with "temporal energy" from the 600-year-old astronomical clock.

### What Bros Believe
A mystical European wine vintage infused with clock energy that makes the drinker irresistible to women. The kind of authentic cultural experience you can't find in Napa Valley.

### The Scam Economics
| Metric | Value |
|--------|-------|
| Actual Cost (Boxed Wine) | €3 |
| Sale Price | €60/bottle |
| Profit Margin | 1,900% |
| "Temporal Energy" Content | 0% |
| Magnetism to Ladies | 0% |

---

## 📊 Item Statistics

### Base Stats
```json
{
  "item_id": "item_clock_energy_wine",
  "display_name": "Clock Energy Wine",
  "type": "consumable",
  "subtype": "alcohol",
  "purchase_price": 60,
  "sell_price": 3,
  "actual_value": 3,
  "stack_size": 6,
  "consumable": true,
  "effect_on_use": "blessed_drunk_status"
}
```

### Effect When Consumed
| Effect | Value | Duration | Notes |
|--------|-------|----------|-------|
| Status Applied | "Blessed Drunk" | 60 min | Identical to regular Drunk |
| Accuracy | -15% | 60 min | Standard alcohol effect |
| Bravado | +10% | 60 min | Standard alcohol effect |
| Magnetism to Ladies | +0% | N/A | Despite vendor claims |
| Temporal Energy | +0% | N/A | Not a real thing |

### "Blessed Drunk" vs Regular Drunk
| Attribute | Blessed Drunk | Regular Drunk |
|-----------|---------------|---------------|
| Accuracy Penalty | -15% | -15% |
| Bravado Boost | +10% | +10% |
| Duration | 60 min | 60 min |
| Icon | Wine glass with sparkles | Beer mug |
| Bros' Interpretation | "Clock energy" | "Just drunk" |
| Actual Difference | None | None |

---

## 🎨 Visual Design

### Item Sprite
- **Dimensions**: 16x32px (standard consumable)
- **Design**: Fancy wine bottle shape
- **Label**: "Temporal Vintage" in ornate script
- **Color**: Dark green glass, gold label accents
- **Cork**: Visible, suggests "quality"

### Bottle Details (Examination)
- Label text: "Temporal Vintage - Est. [current year minus random]"
- Small text: "Product of Wherever"
- Back label: Fake tasting notes ("Notes of time, hints of clock")
- No actual vineyard name
- Suspiciously uniform for "vintage" bottles

### Inventory Icon States
| State | Appearance |
|-------|------------|
| Full | Complete bottle |
| Empty | Grayed out, "consumed" |
| Stack | Number indicator |

---

## 🛒 Acquisition

### Primary Source
- **Vendor**: Clock Wine Vendor (Václav)
- **Location**: Astronomical Cock-Up Square, Debaucheryville
- **Quest**: The Astronomical Cock-Up (Stage 2)

### Purchase Options
| Option | Price | Quantity | "Discount" |
|--------|-------|----------|------------|
| Single Bottle | €60 | 1 | None |
| Three Bottles | €150 | 3 | "Save €30" |
| Six Bottles | €300 | 6 | "Lifestyle Package" |

### Vendor Dialogue on Purchase
> "Very popular with ladies at clubs. The clock energy, it makes you... magnetic."

> "This vintage? 2019. Very good year. For boxes."

---

## 🎯 Quest Integration

### The Astronomical Cock-Up
- **Stage**: Scam Gauntlet (Stage 2)
- **Trigger**: Post-clock vulnerability active
- **Minimum Purchase**: 1 bottle (bros typically buy 3-6)
- **Total Spending**: €60-300

### State Flags
```
clock_wine_purchased: true
clock_wine_quantity: [number]
total_wine_spending: [amount]
blessed_drunk_status_available: true
```

### Running Gag
Throughout the game, bros reference the wine's "effects":
- "I can feel the temporal energy working"
- "The ladies are definitely noticing"
- "This wine hits different. It's the clock energy."

---

## 🔄 Environmental Integration

### Hostel Room Appearance
After purchase, wine bottles appear in bros' hostel room:
- On nightstand
- In bathroom (bad idea)
- Being used as candle holders (empty)
- Label visible for screenshot opportunities

### Other NPCs React
| NPC Type | Reaction |
|----------|----------|
| Club Staff | "Is that... boxed wine in a fancy bottle?" |
| Other Tourists | "Where did you get that?" (wanting to be scammed) |
| Locals | Suppressed laughter |
| Actual Sommelier | Visible pain |

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. Purchase moment with vendor
2. Bros proudly holding bottles
3. Wine bottles in hostel room
4. "Blessed Drunk" status icon with sparkles
5. Close-up of fake "Temporal Vintage" label

### Meme Potential
- "The clock energy, it makes you... magnetic"
- "Very good year. For boxes."
- Blessed Drunk status as ironic achievement
- Wine bottles appearing everywhere in hostel

---

## 🔊 Audio

### Sound Effects
| Action | Sound |
|--------|-------|
| Purchase | Cash register + "satisfied vendor ahh" |
| Consume | Cork pop + drinking sound |
| Status Applied | Subtle sparkle (ironic) |

---

## 📱 Technical Implementation

### Item Data Structure
```json
{
  "item_id": "item_clock_energy_wine",
  "display_name": "Clock Energy Wine",
  "description": "Wine 'infused with temporal energy' from the astronomical clock. Very popular with ladies. (It's boxed wine in a fancy bottle.)",
  "description_bros_see": "Mystical European wine infused with 600 years of clock energy. The vendor said it makes you magnetic.",
  "type": "consumable",
  "subtype": "alcohol",
  "icon": "clock_wine_bottle.png",
  "purchase_price": 60,
  "sell_price": 3,
  "stack_max": 6,
  "use_effect": {
    "status": "blessed_drunk",
    "duration_minutes": 60
  },
  "flavor_text": "Temporal energy not actually included.",
  "examine_text": "The label says 'Temporal Vintage' but the back says 'Product of Wherever.' The bottle seems mass-produced despite the 'vintage' claim.",
  "quest_flags_on_acquire": ["clock_wine_purchased"],
  "tags": ["alcohol", "scam", "consumable", "comedy"]
}
```

### Status Effect Data
```json
{
  "status_id": "blessed_drunk",
  "display_name": "Blessed Drunk",
  "description": "Feeling the 'temporal energy' (actually just drunk)",
  "icon": "blessed_drunk.png",
  "duration_minutes": 60,
  "effects": {
    "accuracy_modifier": -0.15,
    "bravado_modifier": 0.10,
    "magnetism_modifier": 0.00
  },
  "visual_effect": "slight_sparkle_overlay",
  "functionally_identical_to": "regular_drunk"
}
```

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item stats defined | ✅ |
| Visual design specified | ✅ |
| Acquisition source documented | ✅ |
| Quest integration clear | ✅ |
| Status effect defined | ✅ |
| Environmental integration planned | ✅ |
| Comedy value preserved | ✅ |
| Bros never realize it's boxed wine | ✅ |

---

## 📝 Development Notes

- "Blessed Drunk" MUST be functionally identical to regular drunk
- The sparkle visual is purely ironic
- Wine bottles should persist in hostel room environment
- Vendor's "For boxes" slip should be in audio too
- Consider: Achievement for drinking all 6 bottles in one session
- Bros' ongoing references to "clock energy" should feel natural

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **NO crypto elements** - Traditional wine scam
- [x] **Focus on city-specific satire** - Tourist wine exploitation
