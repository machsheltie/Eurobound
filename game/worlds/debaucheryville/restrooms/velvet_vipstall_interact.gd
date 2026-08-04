
extends Node

func _on_graffiti_interacted(graffiti_id: String) -> void:
    if graffiti_id == "graffiti_dont_look_baby" and Player.status.has("Hungover"):
        if not GameState.quest_flags.has("meme_black_market_hint_seen"):
            GameState.quest_flags["meme_black_market_hint_seen"] = true
            ICQController.trigger_popup("memelord.exe", "i got what ur soul needs lol")
            MemeMastery.increment("graffiti")  # Optional if using MemeMastery system

        # Optional lore
        show_tooltip("Etched below in sharpie: ‘LOOKED AT THE BABY IN ‘03. NEVER RECOVERED.’")
