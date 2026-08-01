extends Node

func _ready():
    if BreweryTracker.progress["brewery_progress"]["debaucheryville"]["absinthium_taproom"]:
        print("Already visited The Absinthium Taproom")
    else:
        BreweryTracker.progress["brewery_progress"]["debaucheryville"]["absinthium_taproom"] = true
        BreweryTracker.save_progress()
        print("Visited The Absinthium Taproom for the first time!")
