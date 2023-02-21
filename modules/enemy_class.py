#!/usr/bin/env python3
class Enemy:
    def __init__(self, name, hp, weapon, weapon_dmg, armor_rating):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.weapon_dmg = weapon_dmg
        self.armor_rating = armor_rating

    def enemy_hud(self):
        """
        Shows the current enemy's vitals on the screen to the player. 
        return: The current status of enemy's `hp`, `weapon`, `weapon_dmg`, and `armor_rating`.
        """
        print("-" * 50)
        print(f"{self}'s HP: {self.hp}\nCurrent Weapon: {self.weapon} | Dmg: {self.weapon_dmg}\nArmor Rating: -{self.armor_rating} Dmg")
        print("-" * 50)

    # The method to attack the player goes below

    def attack_player(self):
        pass

    # The method to receive player damage goes below

    def player_damage_taken(self):
        pass

    def take_damage(self, damage):
        remaining_hp = self.hp - damage
        if remaining_hp >= 0:
            self.hp = remaining_hp
            print(f"{self} took {damage} points of damage and have {self.hp} left")
