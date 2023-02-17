#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.text_hud import text_hud
from modules.loot import generate_basic_loot
from modules.player_class import Player


dante = Player()


def first_move_decision():
    """
    The player's first move in the game.
    return: If the player goes into the `Study`, `Great Room`, or searches the `Closet`.
    """
    text_hud()

    # TODO: create the first move options for the player.
    print("Current Location: Front Door.\n\nTo your left is a Study, straight ahead is a Great Room, and to your right is a closet. What do you do?\n")

    try:
        move_choice = int(input(
            "1) Go into the Study\n2) Walk into the Great Room\n3) Open the closet\n\nYour Choice: "))

        if move_choice == 0:
            print("\nQuitting the game as requested.")
            exit()
        elif move_choice == 1:
            pass
        elif move_choice == 2:
            pass
        elif move_choice == 3:            
            print("\nYou open the closet door and a musty smell hits you. You wave it away and turn on the headlamp attached to your head.")
            sleep_print()
            print("\nThe light illuminates the closet and you see at a small metal box sitting on the floor.")
            sleep_print()
            print("\nYou open it and find...\n")
            sleep_print()
            generate_basic_loot()
        else:
            print(
                "\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
            sleep_print()
            clear_screen()
            first_move_decision()
    except ValueError:
        print("\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
        sleep_print()
        clear_screen()
        first_move_decision()
    except (KeyboardInterrupt, EOFError):
        print("\n!! You can always quit the game by typing \"0\" !!")
