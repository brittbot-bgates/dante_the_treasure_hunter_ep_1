#!/usr/bin/env python3
from modules.player_class import Player

dante = Player()


def text_hud():
    """
    Shows Dante's current vitals on the screen to the player. 
    return: The current status of Dante's `hp`, `weapon`, `weapon_dmg`, `armor`, `armor_rating`, and treasure in his `backpack`.
    """
    print("*" * 50)
    print(f"\nDante's HP: {dante.hp}\nCurrent Weapon: {dante.weapon} | Dmg: {dante.weapon_dmg}\nCurrent Armor: {dante.armor} | Rating: -{dante.armor_rating} Dmg\nDante's Loot: {dante.backpack}\n")
    print("*" * 50)
