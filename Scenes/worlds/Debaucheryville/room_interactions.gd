# GDScript for interacting with exhibits
func on_geocities_kiosk_interact():
    if GameTime.get_hour() == 3 and GameTime.get_minute() == 33:
        ICQController.trigger_popup("memelord.exe", "i got what ur soul needs lol")
