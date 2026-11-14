extends GutTest
## ArcadeHallLines + ArcadeBarkZones + quest objectives: the approved completion lines verbatim
## (final.md sections 2-5, 7a; Desk Eurobound-3ho-q4) and their gating.


func test_first_entry_plays_the_three_bro_lines_once() -> void:
	var flags := {}
	var beats := ArcadeHallLines.take_first_entry(flags)
	assert_eq(beats.size(), 3)
	assert_eq(beats[0], {"who": "PILSNER", "line": "Okay. THIS is the Europe I flew six hours for."})
	assert_eq(beats[1]["who"], "BRADLEY")
	assert_eq(beats[1]["line"], "They got a bidet for a bar stool. That's culture, bro. That's, like, history.")
	assert_eq(beats[2], {"who": "CHADWICK", "line": "Chat. We found the mothership."})
	assert_eq(ArcadeHallLines.take_first_entry(flags), [], "second entry is silent")


func test_vip_arrows_and_bidet_text() -> void:
	var v := ArcadeHallLines.vip_arrows()
	assert_eq(v[0]["line"], "VIP's this way. I knew it. I can smell exclusivity.")
	assert_eq(v[1]["line"], "It's a private entrance. Opens right onto the bar. Very exclusive. Nobody else is using it.")
	assert_eq(ArcadeHallLines.bidet_examine(), "A porcelain bidet bolted to a brass bar-stool base. The menu calls it \"reclaimed European seating.\" It is the last stool anyone chooses.")


func test_exterior_examines_and_flyer_gating() -> void:
	assert_eq(ArcadeHallLines.exterior_examine("street_cabinet", {}), "A sticker-bombed arcade cabinet left out on the cobblestones, rain-warped and dead. Its screen reads OUT OF ORDER. It still costs 1 SOV.")
	assert_eq(ArcadeHallLines.exterior_examine("chalkboard", {}), "The chalkboard promises a REAL ARCADE, REAL ABSINTHE and REAL BAD DECISIONS. The first two are technically true.")
	assert_eq(ArcadeHallLines.exterior_examine("window_cat", {}), "A black cat sits on the open first-floor sill, motionless, watching the street like it pays rent. It does not acknowledge you.")
	assert_eq(ArcadeHallLines.exterior_examine("flyer_panel", {}), "A corkboard strangled under six layers of club flyers, each one promising the most exclusive night of your life. None of them are.")
	assert_eq(ArcadeHallLines.exterior_examine("flyer_panel", {"club_flyer_placed": true}), "Your DJ Beatdrop flyer now covers a flyer for a night that also claimed to be unmissable. Yours is the one with the rainbow WordArt.")


func test_four_bark_groups_of_six() -> void:
	var g := ArcadeHallLines.bark_groups()
	assert_eq(g.keys().size(), 4)
	for k in g.keys():
		assert_eq(g[k]["lines"].size(), 6, k)
	assert_eq(g["edm_ghosts"]["lines"][5], "We've been dancing to this song since before your divorce.")
	assert_eq(g["twitchy_hackers"]["lines"][3], "Stop trying to be early. Be late on purpose. In this building, late is the only honest render.")
	assert_eq(g["bathroom_route_speedrunners"]["nodes"], ["aa_node_broken_ddr", "aa_node_maintenance_door", "aa_node_main_cabinet_loop"])


func test_next_bark_walks_the_lines_in_order_and_loops() -> void:
	var c := {}
	var first := ArcadeHallLines.next_bark("edm_ghosts", c)
	assert_eq(first, "You found the curtain. Everyone finds the curtain. The curtain finds you first, honestly.")
	for i in 5:
		ArcadeHallLines.next_bark("edm_ghosts", c)
	assert_eq(ArcadeHallLines.next_bark("edm_ghosts", c), first)


func test_bark_zone_is_one_shot_per_proximity() -> void:
	var z := ArcadeBarkZones.new()
	add_child_autofree(z)
	z.add_zone("rogue_backpackers", "aa_node_bottle_bar", Vector3.ZERO)
	var lines: Array = ArcadeHallLines.bark_groups()["rogue_backpackers"]["lines"]
	assert_eq(z.tick(0.1, Vector3(0.5, 0, 0)), lines[0])
	assert_eq(z.tick(10.0, Vector3(0.5, 0, 0)), "", "standing in the zone does not repeat")
	assert_eq(z.tick(10.0, Vector3(9, 0, 0)), "", "walked away: re-arms")
	assert_eq(z.tick(0.1, Vector3(0.5, 0, 0)), lines[1])


func test_sea_monkeys_win_and_loss_vo() -> void:
	assert_eq(ArcadeHallLines.jakub_sea_monkeys_win(), "You won! The big one! Nobody wins the big one. I have to tell the machine. She will be devastated.")
	assert_eq(ArcadeHallLines.loss_vo(), "Service charge.")
	assert_eq(ArcadeHallLines.loss_staging(), "(The two men crack their knuckles. The screen goes black. The bros wake face-down on the cobblestones outside the Arcade.)")


func test_quest_log_objectives_are_the_approved_lines() -> void:
	var q: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/quest_log/quest_log.json"))["quests"][0]
	var got := {}
	for st in q["steps"]:
		got[st["id"]] = st["objective"]
	for o in q["outcomes"]:
		got[o["id"]] = o["objective"]
	assert_eq(got["the_tip"], "Tip Tomáš at the prize counter.")
	assert_eq(got["the_girls_round"], "Buy the birthday girls a round at the bar.")
	assert_eq(got["the_unsettled_tab"], "Settle the tab with Tomáš, or leave without paying.")
	assert_eq(got["tab_paid"], "The tab is paid. Tomáš appreciates the tip.")
	assert_eq(got["tab_open"], "The tab is still open. It now includes a service charge.")
	assert_eq(got["tab_stolen"], "The tab and service charge were taken from your wallet — or whatever was in it.")
	for id in got.keys():
		assert_eq(got[id], ArcadeHallLines.objective(id))
