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


def second_move_decision():
    """
    The player's second move in the game.
    return: If the player goes into the `Main Bedroom`, `Porch`, or walk through the `Main Hallway`.
    """    

    def move_choice_1_function():
        pass

    def move_choice_2_function():
        pass

    def move_choice_3_function():
        pass

    Dante.player_hud(dante)

    print("Current Location: Great Room.\n\nTo your left is the Main Hallway, straight ahead is the door leading to the Porch facing the backyard, and to your right is the Main Bedroom. What do you do?\n")

    try:
        move_choice_1 = int(input(
            "1) Walk through the Main Hallway\n2) Go outside on the Porch\n3) Enter the Main Bedroom\n\nYour Choice: "))
        if move_choice_1 == 1:
            move_choice_1_function()
        elif move_choice_1 == 2:
            move_choice_2_function()
        elif move_choice_1 == 3:
            move_choice_3_function()
        else:
            print(
                "\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
            sleep_print()
            clear_screen()
            second_move_decision()
    except ValueError:
        print("\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
        sleep_print()
        clear_screen()
        second_move_decision()
    except (KeyboardInterrupt, EOFError):
        print("\n!! You can always quit the game by typing \"0\" !!")
