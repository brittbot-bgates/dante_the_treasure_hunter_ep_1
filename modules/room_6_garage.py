#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.loot import generate_basic_loot
from modules.character_class import Dante, Bat, Rat, Spider, Guard, Guard_Captain, Mansion_Owner
from modules.room_7_bedrooms_bathroom import bedrooms_bathroom

dante = Dante()
bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()


def garage():
    """
    This is the sixth room in the game.
    return: The fight between `Dante` and the `Cursed Guard`.
    """

    with open("python/dante_the_treasure_hunter/script/garage_room_intro.txt", "r") as garage_room_intro:
        for line in garage_room_intro.readlines():
            print(line)
            sleep_print()

    print("~ The " + guard_captain.name + " is ready to attack!\n")
    sleep_print()
    print("~ Dante's unsheathes his sword and prepares to fight!")
    clear_screen()
    guard_captain.enemy_hud()
    sleep_print()
    dante.sword_attack_guard_captain()
    sleep_print()

    with open("python/dante_the_treasure_hunter/script/garage_room_outro.txt", "r") as garage_room_outro:
        for line in garage_room_outro.readlines():
            print(line)
            sleep_print()

    bedrooms_bathroom()
