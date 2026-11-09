
extends Node

signal item_purchased(item_name, effect_description)

var menu = {
    "Doner of Illusions™": {
        "price": 7,
        "effect": "+10 SP, -5 Intelligence, 25% Confused for 2 battles"
    },
    "Sausage of Suspicion": {
        "price": 6,
        "effect": "-2 Defense, +3 Agility, 50% chance of 'Itchy' status"
    },
    "Clown Dog Deluxe™": {
        "price": 9,
        "effect": "Heals 15 HP, adds 'Sticky' debuff to all enemies next round"
    },
    "Meatball on a Lollipop Stick": {
        "price": 5,
        "effect": "+5 Accuracy, 25% chance of attracting sewer NPCs"
    },
    "Glizzénstein’s Brain Brat": {
        "price": 12,
        "effect": "+2 Intelligence, -1 Charisma, +5% critical chance vs. humanoids"
    },
    "Sauce of Unknowing™": {
        "price": 2,
        "effect": "50% chance to randomly re-roll the item’s effects"
    }
}

func interact():
    for item_name in menu:
        var item = menu[item_name]
        emit_signal("item_purchased", item_name, item["effect"])
