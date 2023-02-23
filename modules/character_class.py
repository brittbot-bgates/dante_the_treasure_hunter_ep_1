#!/usr/bin/env python3
import random
from modules.sleep_print import sleep_print


class Dante:
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
        print(f"Dante's HP: {self.hp}\nCurrent Weapon: {self.weapon} | Dmg: {self.weapon_dmg}\nCurrent Armor: {self.armor} | Rating: {self.armor_rating} Dmg\nDante's Loot: {self.backpack}")
        print("-" * 50)

    def sword_attack(self):
        while dante.hp > 0:

            num = random.randint(0, 2)

            if num == 0:
                print(
                    f"\n~ {self.name} slices the {bat.name} with his {self.weapon}!")
                sleep_print()
                remaining_bat_hp = bat.hp - dante.weapon_dmg
                bat.hp = remaining_bat_hp

                if bat.hp <= 0:
                    print(
                        f"\n!! {bat.name} drops onto the floor in two pieces. !!")
                    break
                else:
                    bat.multiple_bites()
            else:
                print(
                    f"\n~ {self.name} swings his {self.weapon} toward the {bat.name} but the {bat.name} dodges the attack.")
                sleep_print()
                bat.multiple_bites()


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
        print(f"{self.name}'s HP: {self.hp}\nCurrent Weapon: {self.weapon} | Dmg: {self.weapon_dmg}\nArmor Rating: {self.armor_rating} Dmg")
        print("-" * 50)


class Bat(Enemy):
    def __init__(self):
        super().__init__(name="Large Bat", hp=5,
                         weapon="Multiple Bites", weapon_dmg=2, armor_rating=0)

    def multiple_bites(self):
        while bat.hp > 0:

            num = random.randint(0, 2)

            if num == 0:
                print(
                    f"\n~ The {bat.name} swoops down toward {dante.name} and sinks its fangs into him with {bat.weapon}.")
                sleep_print()
                remaining_player_hp = dante.hp - bat.weapon_dmg
                dante.hp = remaining_player_hp

                if dante.hp <= 0:
                    print(
                        f"\n!! {dante.name} succumbs to the {bat.weapon} of the {bat.name} and collaspes onto the floor dead.")
                    break
                else:
                    dante.sword_attack()
            else:
                print(
                    f"\n~ The {bat.name} swoops down to bite with {bat.weapon} but {dante.name} dodges the attack.")
                sleep_print()
                dante.sword_attack()


class Rat(Enemy):
    def __init__(self):
        super().__init__(name="Massive Rat", hp=10,
                         weapon="Furious Nibbling", weapon_dmg=3, armor_rating=0)

    def furious_nibbling(self):
        print(f"The {self.name} nibbled you!")


class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Enormous Spider", hp=5,
                         weapon="Poison Fang", weapon_dmg=2, armor_rating=0)

    def pison_fang(self):
        print(f"The {self.name} sank its fangs into you!")


class Guard(Enemy):
    def __init__(self):
        super().__init__(name="Cursed Guard", hp=20,
                         weapon="A Good Pummeling", weapon_dmg=4, armor_rating=3)

    def a_good_pummeling(self):
        print(f"The {self.name} hits you several times!")


class Guard_Captain(Enemy):
    def __init__(self):
        super().__init__(name="Cursed Guard Captain", hp=30,
                         weapon="A Baton Strike", weapon_dmg=5, armor_rating=3)

    def a_knife_strike(self):
        print(f"The {self.name} hits you with a baton!")


class Mansion_Owner(Enemy):
    def __init__(self):
        super().__init__(name="Cursed Mansion Owner", hp=50,
                         weapon="A Sword Strike", weapon_dmg=7, armor_rating=5)

    def an_axe_strike(self):
        print(f"The {self.name} slashes you with a sword!")


dante = Dante()
bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()
