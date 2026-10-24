
# icq_great_doner_debate_dialogue.gd
extends Node

var dialogue_tree = {
    "start": {
        "speaker": "Tony420",
        "text": "yo\nheard u tried the publandia wrap, the clownbox, n the crypto cube\n🧐 respect\nwhich one wins the grease war?",
        "options": ["Publandia OG.", "Debaucheryville Chaos Box.", "They all taste like shame."]
    },
    "Publandia OG.": {
        "Tony420": "lol clown just rage quit\nanyway ur kebab karma just got spicier",
        "ChefChuckles": "HOW DARE U\nthat wrap had *lettuce.*\nu insulted the circus and the sacred mystery meat spiral",
        "effects": {
            "Bravado": +5,
            "MrChadzDiscount": -0.05
        }
    },
    "Debaucheryville Chaos Box.": {
        "Tony420": "ok but like\nu just gave a vending machine diarrhea box the W\nbold move. markets are crashing",
        "ChefChuckles": "yesssss\nONE OF US\nwe ride the greasewave to glory",
        "effects": {
            "Bravado": +5,
            "NewMenuTier": true
        }
    },
    "They all taste like shame.": {
        "Tony420": "damn\nmost honest thing i heard all week\nu get the badge of shame\nand the gut of steel",
        "ChefChuckles": "betrayal. but… respected",
        "System": "[NEW TITLE UNLOCKED] 🏅 World’s Pickiest Drunk",
        "effects": {
            "UnlockTitle": "World’s Pickiest Drunk",
            "ICQGroup": "Sauce Apostates 2.0"
        }
    }
}
