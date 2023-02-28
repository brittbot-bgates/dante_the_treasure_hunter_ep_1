#!/usr/bin/env python3
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.character_class import Dante, Bat, Rat, Spider, Guard, Guard_Captain, Mansion_Owner
from modules.room_5_mud_laundry_room import mud_laundry_room
from modules.room_6_bedrooms_bathroom import bedrooms_bathroom

dante = Dante()
bat = Bat()
rat = Rat()
spider = Spider()
guard = Guard()
guard_captain = Guard_Captain()
mansion_owner = Mansion_Owner()


def kitchen():
    """
    This is the fourth room in the game.
    return: If the player goes into the `Mud & Laundry Room` or the `Bedrooms & Bathroom` after entering the `Main Hallway`.
    """

    with open("python/dante_the_treasure_hunter/script/kitchen_intro.txt", "r") as kitchen_intro:
        for line in kitchen_intro.readlines():
            print(line)
            sleep_print()

    print("~ The " + guard.name + " is ready to attack!\n")
    sleep_print()
    print("~ Dante's unsheathes his sword and prepares to fight!")
    clear_screen()
    guard.enemy_hud()
    sleep_print()
    dante.sword_attack_guard()
    sleep_print()
    print("\nCurrent Location: Main Hallway.\n\nTo your left leads to the Mud & Laundry Room and to your right is Bedrooms & Bathroom. What do you do?\n")

    try:
        main_hallway_choice = int(input(
            "1) Walk to the Mud & Laundry Room\n2) Walk toward the Bedrooms & Bathroom\n\nYour Choice: "))
        if main_hallway_choice == 0:
            print("\nQuitting the game as requested.")
            exit()
        elif main_hallway_choice == 1:
            print(
                "\n~ Dante takes a left and enters the Mud & Laundry Room.\n")
            mud_laundry_room()
        elif main_hallway_choice == 2:
            print(
                "\n~ Dante takes a right and stops before the Bedrooms & Bathroom.\n")
            bedrooms_bathroom()
        else:
            print(
                "\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
            sleep_print()
            clear_screen()
            kitchen()
    except ValueError:
        print("\n!! Invalid choice. Please enter either \"1\" or \"2\" or \"3\" as your choice. !!")
        sleep_print()
        clear_screen()
        kitchen()
    except (KeyboardInterrupt, EOFError):
        print("\n!! You can always quit the game by typing \"0\" !!")
