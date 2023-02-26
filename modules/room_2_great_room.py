#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.loot import generate_basic_loot
from modules.character_class import Dante, Bat, Rat, Spider, Guard, Guard_Captain, Mansion_Owner

dante = Dante()
bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()


def great_room():
    """
    This is the second room in the game.
    return: If the player goes into the `Main Bedroom` or `Backyard Porch`.
    """

    def backyard_porch_function():
        print()

        with open("python/dante_the_treasure_hunter/script/great_room_backyard_porch_choice.txt", "r") as backyard_porch_choice:
            for line in backyard_porch_choice.readlines():
                print(line)
                sleep_print()

        print("~ " + spider.name + "...and it's ready to attack!\n")
        sleep_print()
        print("~ Dante's unsheathes his sword and prepares to fight!")
        clear_screen()
        spider.enemy_hud()
        sleep_print()
        dante.sword_attack_spider()
        sleep_print()
        print()

    def main_bedroom_function():
        print()

        with open("python/dante_the_treasure_hunter/script/great_room_main_bedroom_choice.txt", "r") as main_bedroom_choice:
            for line in main_bedroom_choice.readlines():
                print(line)
                sleep_print()

        print("~ " + rat.name + "...and it's ready to attack!\n")
        sleep_print()
        print("~ Dante's unsheathes his sword and prepares to fight!")
        clear_screen()
        rat.enemy_hud()
        sleep_print()
        dante.sword_attack_rat()
        sleep_print()
        print()

        with open("python/dante_the_treasure_hunter/script/great_room_main_bedroom_loot.txt", "r") as main_bedroom_loot:
            for line in main_bedroom_loot.readlines():
                print(line)
                sleep_print()

        generate_basic_loot()
        sleep_print()


    with open("python/dante_the_treasure_hunter/script/great_room_intro.txt", "r") as great_room_intro:
            for line in great_room_intro.readlines():
                print(line)
                sleep_print()

    Dante.player_hud(dante)

    print("Current Location: Great Room.\n\nStraight ahead is the door to the Backyard Porch and to your right is the Main Bedroom. What do you do?\n")

    try:
        great_room_choice = int(input(
            "1) Walk through the Main Hallway\n2) Go outside on the Porch\n3) Enter the Main Bedroom\n\nYour Choice: "))
        if great_room_choice == 0:
            print("\nQuitting the game as requested.")
            exit()
        elif great_room_choice == 1:
            backyard_porch_function()
            print(
                "\n~ Dante reenters the house through the Great Room.\n")
            # place the Dining Room function here
        elif great_room_choice == 2:
            main_bedroom_function()
            print(
                "\n~ Dante exits the Main Bedroom through the door leading onto the Backyard Porch.\n")
            backyard_porch_function()
        else:
            print(
                "\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
            sleep_print()
            clear_screen()
            great_room()
    except ValueError:
        print("\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
        sleep_print()
        clear_screen()
        great_room()
    except (KeyboardInterrupt, EOFError):
        print("\n!! You can always quit the game by typing \"0\" !!")
