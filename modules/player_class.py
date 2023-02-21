#!/usr/bin/env python3
class Player:
    def __init__(self):
        self.name = "Dante"
        self.hp = 100
        self.weapon = "Sword"
        self.armor = "Basic Armor"
        self.backpack = []
        self.weapon_dmg = 5
        self.armor_rating = 3

    def player_hud(self):
        """
        Shows Dante's current vitals on the screen to the player. 
        return: The current status of Dante's `hp`, `weapon`, `weapon_dmg`, `armor`, `armor_rating`, and treasure in his `backpack`.
        """
        print("-" * 50)
        print(f"Dante's HP: {self.hp}\nCurrent Weapon: {self.weapon} | Dmg: {self.weapon_dmg}\nCurrent Armor: {self.armor} | Rating: -{self.armor_rating} Dmg\nDante's Loot: {self.backpack}")
        print("-" * 50)

    # The method to attack the enemy goes below
    """
    Fighting enemies works as so:
    1) Once a player encounters an enemy the fight starts
    2) Use a random number to determine if the enemy catches the player by surprise.
    3) If the enemy doesn't catch the player by surprise then the player attacks first.
    4) The attack goes back and forth between the player and the enemy until one of them dies.
    5) The attack uses random numbers to determine if the attack is successful.
    6) A successful attack displays with "attack hit" or something on screen and shows the damage done.
    7) A missed attacks displays with "miss" or something on the screen.
    8) Damage done reduces the HP of the player and the enemy
    9) If the player dies show a game over screen.
    10) If the enemy dies the player gets to continue the game.
    """

    def attack_enemy(self):
        pass

    # The method to receive enemy damage goes below

    def enemy_damage_taken(self):
        pass
