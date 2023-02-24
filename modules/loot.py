#!/usr/bin/env python3
import random
from modules.sleep_print import sleep_print
from modules.character_class import Dante

basic_loot = [
    "A few gold coins",
    "A rare coin",
    "A gold ring",
    "A pair of gold earrings",
    "A rare stamp",
    "A silver ring",
    "A pair of silver earrings",
]

premium_loot = [
    "Falchion Sword",
    "Gold bar",
    "A pouch of precious gemstones",
    "A full jewelry box",
    "Pristine Silver Certificates",
]

dante = Dante()


def generate_basic_loot():
    """
    Generates basic loot when the player searches a room.
    return: A random piece of loot from `basic_loot`.
    """
    num = random.randint(0, 3)

    if num >= 2:
        basic_found_loot = random.choice(basic_loot)
        print(f"{basic_found_loot}!")
        sleep_print()
        dante.backpack.append(basic_found_loot)
        print(f"\nCurrent treasure inventory:\n")
        Dante.player_hud(dante)
    else:
        print("Nothing.")


def generate_premium_loot():
    """
    Generates premium loot when the player searches a room.
    return: A random piece of loot from `premium_loot`.
    """
    num = random.randint(0, 6)

    if num >= 3:
        premium_found_loot = random.choice(premium_loot)
        print(f"{premium_found_loot}!")
        sleep_print()
        dante.backpack.append(premium_found_loot)
        print(f"\nCurrent treasure inventory:\n")
        Dante.player_hud(dante)
    else:
        print("Nothing.")
