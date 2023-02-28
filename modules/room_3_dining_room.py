#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.room_4_kitchen import kitchen


def dining_room():
    """
    This is the third room in the game.
    return: The player goes into the `Kitchen`.
    """

    with open("python/dante_the_treasure_hunter/script/dining_room_intro.txt", "r") as dining_room_intro:
            for line in dining_room_intro.readlines():
                print(line)
                sleep_print()

    kitchen()
