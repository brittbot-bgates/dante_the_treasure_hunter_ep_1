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


def first_move_decision():
    """
    The player's first move in the game.
    return: If the player goes into the `Study`, `Great Room`, or searches the `Closet`.
    """
    Dante.player_hud(dante)

    print("Current Location: Front Door.\n\nTo your left is a Study, straight ahead is a Great Room, and to your right is a closet. What do you do?\n")

    try:
        move_choice = int(input(
            "1) Go into the Study\n2) Walk into the Great Room\n3) Open the closet\n\nYour Choice: "))

        if move_choice == 0:
            print("\nQuitting the game as requested.")
            exit()
        elif move_choice == 1:
            print("")

            with open("python/dante_the_treasure_hunter/script/first_move_decision_study.txt", "r") as choice_1:
                for line in choice_1.readlines():
                    print(line)
                    sleep_print()

            print("~ " + bat.name + "...and it's ready to attack!\n")
            sleep_print()
            print("~ Dante's unsheathes his sword and prepares to fight!")
            clear_screen()
            bat.enemy_hud()
            sleep_print()
            dante.sword_attack()
            sleep_print()

        elif move_choice == 2:
            print("")

            with open("python/dante_the_treasure_hunter/script/first_move_decision_great_room.txt", "r") as choice_2:
                for line in choice_2.readlines():
                    print(line)
                    sleep_print()

            print("~ " + rat.name + "...and it's ready to attack!\n")
            sleep_print()
            rat.enemy_hud()

        # TODO: Add the enemy function here.

        elif move_choice == 3:
            print("")

            with open("python/dante_the_treasure_hunter/script/first_move_decision_closet.txt", "r") as choice_3:
                for line in choice_3.readlines():
                    print(line)
                    sleep_print()

            generate_basic_loot()

            sleep_print()
            print("\n~ Dante stands up and closes the closet door.\n")
            sleep_print()

            # TODO: Add second move choice function here
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
