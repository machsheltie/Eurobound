extends Node

func _ready():
    if BreweryTracker.progress["brewery_progress"]["deboucheryville"]["absynthium_taproom"]:
        print("Already visited Absynthium Taproom")
    else:
        BreweryTracker.progress["brewery_progress"]["deboucheryville"]["absynthium_taproom"] = true
        BreweryTracker.save_progress()
        print("Visited Absynthium Taproom for the first time!")
