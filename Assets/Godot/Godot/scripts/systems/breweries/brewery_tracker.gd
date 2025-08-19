
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
                "deboucheryville": {
                    "absynthium_taproom": false,
                    "three_crown_keg_haus": false,
                    "tap_dat_vault": false,
                    "ye_olde_brew_lab": false
                },
                "publandia": {
                    "bogmans_brewery": false,
                    "flatcap_ferments": false,
                    "liffy_lager_house": false,
                    "tattie_porter_crafthouse": false
                },
                "sinfonia": {
                    "opernhaus_ale_stube": false,
                    "sachercraft_barrelworks": false,
                    "vienna_noir_fermentarium": false,
                    "schnitzelbier_innovation_lab": false
                }
            },
            "brewery_global_total": 0
        }

func save_progress():
    var file = FileAccess.open(tracker_path, FileAccess.WRITE)
    file.store_string(JSON.stringify(progress, "\t"))
    file.close()
