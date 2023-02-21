#!/usr/bin/env python3
import random
from modules.enemy_class import Enemy

bat = Enemy("Large Bat", 5, "Multiple Bite", 2, 0)
rat = Enemy("Massive Rat", 10, "Furious Nibbling", 3, 0)
spider = Enemy("Enormous Spider", 5, "Poison Fang", 2, 0)
guard = Enemy("Cursed Guard", 20, "A Good Pummeling", 5, 3)
guard_captain = Enemy("Cursed Guard Captain", 30, "A Knife Strike", 7, 3)
mansion_owner = Enemy("Cursed Mansion Owner", 80, "Axe Strike", 8, 5)

easy_enemies = [
    bat,
    rat,
    spider,
]

hard_enemies = [
    guard,
    guard_captain,
    mansion_owner,
]


def random_easy_enemy():
    """
    Generates a random easy enemy for the player to fight.
    return: The enemy from `easy_enemies`.
    """
    chosen_easy_enemy = random.choice(easy_enemies)
    print(chosen_easy_enemy.name)


def random_hard_enemy():
    """
    Generates a random hard enemy for the player to fight.
    return: The enemy from `hard_enemies`.
    """
    chosen_hard_enemy = random.choice(hard_enemies)
    print(chosen_hard_enemy.name)
