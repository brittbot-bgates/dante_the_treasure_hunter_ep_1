#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.player_class import Player


def start_game():
    print("\nSetting up the scene leading up to The Maledictus Mansion...\n")
    sleep_print()

    with open("python/dante_the_treasure_hunter/script/game_intro.txt", "r") as game_intro_script:
        for line in game_intro_script.readlines():
            print(line)
            sleep_print()

# TODO: create a text hud showing Dante's health and treasure in the backpack
# TODO: create a module for the "first move decision" and add that here and its function call.

    dante = Player()
