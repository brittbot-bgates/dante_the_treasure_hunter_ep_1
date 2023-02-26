#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.room_1_foyer import starting_room


def start_game():
    """
    Starts the game and provides the story's introduction.
    :return: None
    """
    print("\nSetting up the scene leading up to The Maledictus Mansion...\n")
    sleep_print()

    with open("python/dante_the_treasure_hunter/script/game_intro.txt", "r") as game_intro_script:
        for line in game_intro_script.readlines():
            print(line)
            sleep_print()

    starting_room()
