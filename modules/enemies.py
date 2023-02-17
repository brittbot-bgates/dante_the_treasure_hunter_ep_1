#!/usr/bin/env python3
import random
from modules.enemy_class import Enemy

bat = Enemy("bat", 5, "bite", 2, 0)

basic_enemies = [
    bat,
]


def random_basic_enemy():
    """
    Generates a random enemy for the player to fight.
    return: The enemy from `basic_enemies`.
    """
    chosen_basic_enemy = random.choice(basic_enemies)
    print(chosen_basic_enemy.name)
