# game where have an inventory thta you can take items in and out of
import sys
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.gold = 0

    def display_stats(self):
        print(f"User: {self.name}")
        print(f"Gold: {self.gold}")
        print(f"Inventory:")
        if self.inventory == []:
            print("[Empty]")
        else:
            for item in self.inventory:
                print(f"- {item}")


def main_menu(player):
    print(
        """
=======================
Welcome to Nagamitashima
1. Continue.
2. Display Stats
3. Exit Program  
  """
    )
    choice = input("Input: ")
    if choice == "1":
        castle_courtyard(player)
    elif choice == "2":
        player.display_stats()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid input.asd")


def main():
    player_name = input("Enter a username: ")
    player = Player(player_name)
    main_menu(player)


def courtyard_options():
    print(
        """
=======================
1. Go to the Tavern
2. Go to the Gamblers
3. Go to the Auction House
4. Exit Castle
5. Exit Game
"""
    )
    player_cy_choice = input("Input: ")
    return player_cy_choice


def castle_courtyard(player):
    print("You enter the castle's courtyard...")
    while True:
        player_cy_choice = courtyard_options()
        if player_cy_choice == "1":
            print("You enter the tavern...")
            main_menu(player)
        elif player_cy_choice == "2":
            gambling_section(player)
        elif player_cy_choice == "3":
            pass
        elif player_cy_choice == "4":
            print("You exit the courtyard.")
            main_menu(player)
        elif player_cy_choice == "5":
            sys.exit()
        else:
            print("Invalid input.")


# gambling functions


def gambling_menu():
    print(
        """
=======================
1. Gamble (50/50)
2. Russian Roulette
3. Exit
          """
    )
    gambling_menu_input = input("Input: ")
    print(gambling_menu_input)
    return gambling_menu_input


def gambling_section(player):
    menu_input = gambling_menu()
    if menu_input == "1":
        gamble_50_50(player)
    elif menu_input == "2":
        # russian_roulette()
        pass
    elif menu_input == "3":
        main_menu(player)
    else:
        print("Invalid input. ")


def gamble_50_50(player):
    print("You roll...")
    roll = random.randint(1, 101)
    print(roll)
    if roll >= 50:
        print("You win! +1 gold")
        player.gold += 1
        return player
    else:
        print("Better luck next time...")
        return player


main()
