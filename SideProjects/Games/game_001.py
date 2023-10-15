# game where have an inventory thta you can take items in and out of
import sys
import random


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# function to create items
def create_item(name, value):
    return Item(name, value)


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.gold = 0

    def display_stats(self):
        print("================")
        print(f"User: {self.name}")
        print(f"Gold: {self.gold}")
        print(f"Inventory:")
        if not self.inventory:
            print("[Empty]")
        else:
            for item in self.inventory:
                print(f"- {item.name}")


# function for adding item to players inv
def add_item_to_inventory(player, item):
    player.inventory.append(item)


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
            tavern(player)
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


# Tavern
def tavern(player):
    print("You enter the tavern...")
    while True:
        # accessing the returned value
        tavern_option = tavern_options()
        if tavern_option == "1":
            # creating first item object
            beer_item = create_item("beer", 1)
            add_item_to_inventory(player, beer_item)
            print("You order a beer... +1 beer")
            another_beer = input("'You want another?' yes or no: ")
            if another_beer == "yes":
                add_item_to_inventory(player, beer_item)
                print("You order a beer... +1 beer")
                print("'Alright, you've had enough get out of here!'")
                castle_courtyard(player)
            else:
                castle_courtyard(player)
        elif tavern_option == "2":
            print("You take a seat.")
            print("You get up and leave...")
            castle_courtyard(player)
        else:
            print("Invalid input.")


def tavern_options():
    print(
        """
===================
1. Order drink 
2. Take a seat
3. Leave 
            """
    )
    tavern_selection = input("Input: ")
    # doing this allows us to access the returned value
    return tavern_selection


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


# Auction House
# for this we should create a database of some sort maybe sqlite
# we can have items that rotate in and out of avalability depending on maybe
# some kind of experience

# Items for auction
items_for_auction = [
    Item("Cube", 100),
    Item("Short Sword", 55),
    Item("Shiny Stone", 250),
]


def display_auction_items(auction_items):
    print("Auction House Items:")
    for i, item in enumerate(auction_items):
        print(f"{i + 1}. {item.name} - Value: {item.value}g")


def rotate_auction_items(auction_items):
    # simulate roating items
    random.shuffle(auction_items)


def auction(player):
    while True:
        print("\nWelcome to the Auction House!")
        display_auction_items(items_for_auction)
        choice = input("Enter the item number to bit on (or 'exit' to leave)")
        if choice.lower() == "exit":
            break
        try:
            item_index = int(choice) - 1
            if 0 <= item_index < len(items_for_auction):
                item = items_for_auction[item_index]
                bid = int(input(f"Enter your bid for the {item.name}:"))
                if bid >= item.value:
                    print(f"Congratz! You won {item.name} for {bid}g")
                    player.inventory.append(item)
                    # remove item at the index of bought item
                    items_for_auction.pop(item_index)
                else:
                    print("Sorry, your bid was unsuccessful.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input. Please enter a valid item or 'exit'.")


if __name__ == "__main__":
    main()
