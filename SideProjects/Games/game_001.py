# game where have an inventory thta you can take items in and out of
import sys


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def display_stats(self):
        print(f"User: {self.name}")
        print(f"Inventory:")
        for item in self.inventory:
            print(f"- {item}")


def main():
    player_name = input("Enter a username: ")
    player = Player(player_name)
    print(
        """
Welcome to Nagamitashima
1. Continue.
2. Display Stats
3. Exit Program  
  """
    )
    choice = input("Input: ")
    if choice == "1":
        pass
    elif choice == "2":
        player.display_stats()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid input.asd")


main()
