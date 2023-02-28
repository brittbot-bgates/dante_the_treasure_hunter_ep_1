#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.loot import generate_basic_loot
from modules.character_class import Dante, Bat, Rat, Spider, Guard, Guard_Captain, Mansion_Owner

dante = Dante()
bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()


def kitchen():
    """
    This is the fourth room in the game.
    return: If the player goes into the `Main Hallway`.
    """

    with open("python/dante_the_treasure_hunter/script/kitchen_intro.txt", "r") as kitchen_intro:
        for line in kitchen_intro.readlines():
            print(line)
            sleep_print()

    print("~ The " + guard.name + " is ready to attack!\n")
    sleep_print()
    print("~ Dante's unsheathes his sword and prepares to fight!")
    clear_screen()
    guard.enemy_hud()
    sleep_print()
    dante.sword_attack_guard()
    sleep_print()
    print("\nCurrent Location: Main Hallway.\n\nTo your left leads to the Mud & Laundry Room and to your right is Bedrooms & Bathroom. What do you do?\n")
    # TODO: Add the rest of the room 5 choices below
