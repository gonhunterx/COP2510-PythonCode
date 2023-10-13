import sys

# Classes


class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.inventory = []

    def display_stats(self):
        print("-----------------------")
        print(f"🙂‍↔️ User: {self.name}")
        print(f"💰 Coins: {self.coins}")
        print("🎒 Inventory:")
        for item in self.inventory:
            print(f"{item.name}: {item.value} coins")
        print("-----------------------")


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# items for inventory

# defining items to be collected with names and values to pass through class
wood_log = Item("Wood Log", 4)
wheat = Item("Wheat", 2)
# first passed is name second is coin value


# functions
def intro_menu(player):
    print("welcome to Nomata")
    print("1. Start")
    print("2. Quit")
    intro_choice = input("Make a choice: ")
    if intro_choice == "1":
        main_menu(player)
    elif intro_choice == "2":
        sys.exit()
    else:
        print("Invalid input.")


def main_menu(player):
    print("main menu:")
    print("1. Go to farm")
    print("2. Go to woods")
    print("3. Go to the market")
    print("4. Display stats/inv")
    print("5. Quit")
    choice = input("Input 1 - 5: ")
    if choice == "1":
        farm(player)
    elif choice == "2":
        woods(player)
    elif choice == "3":
        market(player)
    elif choice == "4":
        player.display_stats()
        main_menu(player)
    elif choice == "5":
        sys.exit()
    else:
        print("invalid input.")


def main():
    player_name = input("What is your name?: ")
    player = Player(player_name)
    # adding items to lyers inv
    intro_menu(player)

    main_menu(player)


# Zones


def farm(player):
    print("you walk to the farm...")
    choice = input("do you want to farm or leave?: ")
    if choice.lower() == "farm":
        print("You farm some wheat. +1 wheat")
        player.inventory.append(wheat)
    elif choice.lower() == "leave":
        main_menu(player)
    else:
        print("invalid input. farm or leave.")


def woods(player):
    print("you walk into the woods...")
    choice = input("do you want to chop or leave?: ")
    if choice.lower() == "chop":
        print("You chop some wood. +1 wood log")
        player.inventory.append(wood_log)
    elif choice.lower() == "leave":
        main(player)
    main_menu()


def market():
    print("you enter the market...")
    # if player says yes to sell item
    # then remove item from inventory and give value to player in coins.


if __name__ == "__main__":
    main()
