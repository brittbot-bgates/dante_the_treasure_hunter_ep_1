#!/usr/bin/env python3
"""
Title: Dante, The Treasure Hunter
Creator: Brittany Gates (https://github.com/brittbot-bgates)
About: You are Dante, a world-famous treasure hunter who travels to exotic locations around the world to search dangerous building for its famed loot.
Episode #1: The Famed Loot of The Maledictus Mansion
"""
from modules.sleep_print import sleep_print
from modules.clear_screen import clear_screen
from modules.start_game import start_game


def main():
    """
    The menu for the game.
    :return: A new game or quits the game depending on the player's choice.
    """
    print("*" * 60)
    print("\nDante, The Treasure Hunter")
    print("\n\x1B[3mEpisode #1: The Famed Loot of The Maledictus Mansion\x1B[0m")
    print("\nEnter \"0\" to quit or \"1\" to start the game.\n")
    print("*" * 60)

    try:
        player_choice = int(input("\nYour Choice: "))

        if player_choice == 0:
            print("\nWe'll see you next time!")
            exit()
        elif player_choice == 1:
            start_game()
        else:
            print(
                "\n!! Invalid choice. Please enter either \"0\" or \"1\" as your choice. Restarting the game. !!")
            sleep_print()
            clear_screen()
            main()
    except ValueError:
        print("\n!! Invalid choice. Please enter either \"0\" or \"1\" as your choice. Restarting the game. !!")
        sleep_print()
        clear_screen()
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n!! You can always quit the game by typing \"0\" !!")


if __name__ == "__main__":
    main()
