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
        print(f"{self.name}'s HP: {self.hp}\nCurrent Weapon: {self.weapon} | Dmg: {self.weapon_dmg}\nArmor Rating: {self.armor_rating} Dmg")
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


class Bat(Enemy):
    def __init__(self):
        super().__init__(name="Large Bat", hp=5, weapon="Multiple Bites", weapon_dmg=2, armor_rating=0)

    def multiple_bites(self):
        print(f"The {self.name} bit you!")


class Rat(Enemy):
    def __init__(self):
        super().__init__(name="Massive Rat", hp=10, weapon="Furious Nibbling", weapon_dmg=3, armor_rating=0)

    def furious_nibbling(self):
        print(f"The {self.name} nibbled you!")


class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Enormous Spider", hp=5, weapon="Poison Fang", weapon_dmg=2, armor_rating=0)

    def pison_fang(self):
        print(f"The {self.name} sank its fangs into you!")


class Guard(Enemy):
    def __init__(self):
        super().__init__(name="Cursed Guard", hp=20, weapon="A Good Pummeling", weapon_dmg=4, armor_rating=3)

    def a_good_pummeling(self):
        print(f"The {self.name} hits you several times!")


class Guard_Captain(Enemy):
    def __init__(self):
        super().__init__(name="Cursed Guard Captain", hp=30, weapon="A Baton Strike", weapon_dmg=5, armor_rating=3)

    def a_knife_strike(self):
        print(f"The {self.name} hits you with a baton!")


class Mansion_Owner(Enemy):
    def __init__(self):
        super().__init__(name="Cursed Mansion Owner", hp=50, weapon="A Sword Strike", weapon_dmg=7, armor_rating=5)

    def an_axe_strike(self):
        print(f"The {self.name} slashes you with a sword!")


bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()
