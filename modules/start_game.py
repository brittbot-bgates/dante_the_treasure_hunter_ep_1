#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.first_move_decision import first_move_decision


def start_game() -> None:
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

    first_move_decision()
