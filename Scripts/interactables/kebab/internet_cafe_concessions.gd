
extends Node2D

func _ready():
    print("Welcome to the 24-Hour Internet Café – Back Room Concessions!")

func interact(player):
    # Sample interaction logic
    player.show_menu("internet_cafe_concessions_dialogue.json")
