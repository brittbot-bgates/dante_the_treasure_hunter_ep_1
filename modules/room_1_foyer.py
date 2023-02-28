#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.loot import generate_basic_loot
from modules.character_class import Dante, Bat, Rat, Spider, Guard, Guard_Captain, Mansion_Owner
from modules.room_2_great_room import great_room

dante = Dante()
bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()


def starting_room():
    """
    This is the starting room in the game.
    return: If the player goes into the `Study`or searches the `Closet`.
    """

    def study_choice_function():
        print()

        with open("python/dante_the_treasure_hunter/script/starting_room_study_choice.txt", "r") as study_choice:
            for line in study_choice.readlines():
                print(line)
                sleep_print()

        print("~ A " + bat.name + ". And it's ready to attack!\n")
        sleep_print()
        print("~ Dante's unsheathes his sword and prepares to fight!")
        clear_screen()
        bat.enemy_hud()
        sleep_print()
        dante.sword_attack_bat()
        sleep_print()
        print()

        with open("python/dante_the_treasure_hunter/script/starting_room_study_loot.txt", "r") as study_choice_loot:
            for line in study_choice_loot.readlines():
                print(line)
                sleep_print()

        generate_basic_loot()
        sleep_print()

    def closet_choice_function():
        print()

        with open("python/dante_the_treasure_hunter/script/starting_room_closet_choice.txt", "r") as closet_choice:
            for line in closet_choice.readlines():
                print(line)
                sleep_print()

        generate_basic_loot()
        sleep_print()
        print("\n~ Dante stands up and closes the closet door.\n")
        sleep_print()

    Dante.player_hud(dante)

    print("Current Location: Foyer.\n\nTo your left is a Study and to your right is a closet. What do you do?\n")

    try:
        starting_room_choice = int(input(
            "1) Go into the Study\n2) Open the closet\n\nYour Choice: "))

        if starting_room_choice == 0:
            print("\nQuitting the game as requested.")
            exit()
        elif starting_room_choice == 1:
            study_choice_function()
            print(
                "\n~ Dante leaves the Study and walks into the Great Room.\n")
            great_room()
        elif starting_room_choice == 2:
            closet_choice_function()
            print(
                "\n~ Dante leaves the Study and walks into the Great Room.\n")
            great_room()
        else:
            print(
                "\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
            sleep_print()
            clear_screen()
            starting_room()
    except ValueError:
        print("\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
        sleep_print()
        clear_screen()
        starting_room()
    except (KeyboardInterrupt, EOFError):
        print("\n!! You can always quit the game by typing \"0\" !!")
