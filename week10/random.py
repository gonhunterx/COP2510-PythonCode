class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.inventory = []

    def display_stats(self):
        print(
            f"""
User: {self.name}          
Gold: {self.gold}
              """
        )
        if self.inventory:
            for item in self.inventory:
                print({item.name})
        else:
            print("[Empty]")


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


def avaliable_items():
    items = {
        "Sword": 20,
        "Hammer": 45,
        "Dagger": 20,
    }
    return items


def main_menu():
    print(
        """
1. Go to shinata's hut
2. View Inventory
3. Exit    
          """
    )
    main_menu_choice = input("Input: ")
    return main_menu_choice


def shinatas_hut():
    while True:
        pass


def main():
    print("Welcome to Tomanishi no Sekai")
    player_name = input("What is your name?: ")
    player = Player(player_name)
    while True:
        menu_choice = main_menu()
        if menu_choice == "1":
            print("You enter Shinata's hut...")
            shinatas_hut()
        elif menu_choice == "2":
            player.display_stats()
        elif menu_choice == "3":
            break
        else:
            print("Invalid Input.")


main()
