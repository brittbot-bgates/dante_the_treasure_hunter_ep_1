#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.loot import generate_basic_loot
from modules.character_class import Dante, Bat, Rat, Spider, Guard, Guard_Captain, Mansion_Owner
from modules.room_6_garage import garage

dante = Dante()
bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()


def mud_laundry_room():
    """
    This is the fifth room in the game.
    return: The fight between `Dante` and the `Cursed Guard`.
    """

    with open("python/dante_the_treasure_hunter/script/mud_laundry_room_intro.txt", "r") as mud_laundry_room_intro:
        for line in mud_laundry_room_intro.readlines():
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

    with open("python/dante_the_treasure_hunter/script/mud_laundry_room_loot.txt", "r") as mud_laundry_room_loot:
        for line in mud_laundry_room_loot.readlines():
            print(line)
            sleep_print()

    generate_basic_loot()
    sleep_print()
    garage()
