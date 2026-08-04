
extends Node

var progress = {}
var tracker_path := "user://saves/brewery_tracker_full.json"

func load_progress():
    if FileAccess.file_exists(tracker_path):
        var file = FileAccess.open(tracker_path, FileAccess.READ)
        progress = JSON.parse_string(file.get_as_text())
    else:
        # fallback to default
        progress = {
            "brewery_progress": {
                "debaucheryville": {
                    "absinthium_taproom": false,
                    "tap_dat_vault": false,
                    "three_crown_keg_haus": false,
                    "ye_olde_brew_lab": false
                },
                "publandia": {
                    "blarney_trap": false,
                    "stoutworks_brewery": false,
                    "trinity_of_pints": false,
                    "shenanigans": false
                },
                "sinfonia": {
                    "moderato_pub": false,
                    "standing_ovation": false,
                    "crown_and_cask": false,
                    "dancing_stein": false
                }
            },
            "brewery_global_total": 0
        }

func save_progress():
    var file = FileAccess.open(tracker_path, FileAccess.WRITE)
    file.store_string(JSON.stringify(progress, "\t"))
    file.close()
