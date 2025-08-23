
extends Node

signal dialogue_complete

var dialogue_lines = [
    "Warning: I run on LimeWire and vengeance.",
    "Hamster Dance is eternal, peasant.",
    "YOLO’d into GeoCitiesCoin, AMA.",
    "I got diamond hands and zero liquidity, baby.",
    "Wanna buy a rage comic that got me banned from Habbo Hotel?",
    "Funcoland offered me $1.10 for my soul and two PS2 controllers."
]

func start_dialogue():
    for line in dialogue_lines:
        print(line)
    emit_signal("dialogue_complete")
