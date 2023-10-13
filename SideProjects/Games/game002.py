class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.coins = 0
        self.experience = 0

        print(f"Name: {self.name}")

    def displayStats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Coins: {self.coins}")
        print(f"Exp: {self.experience}")

    def resetStats(self):
        self.health = 10
        self.coins = 0

    def resetName(self, name):
        self.name = name


class Enemy:
    def __init__(self, name, health, experienceUponDeath, damage):
        self.name = name
        self.health = health
        self.experienceUponDeath = experienceUponDeath
        self.damage = damage

    def attack(self, player):
        player.takeDamage(self.damage)

    def takeDamage(self, damage):
        self.health -= damage


class Shop:
    def __init__(self, player):
        self.player = player

    def shopMenu(self):
        while True:
            shopKeeperQuestion = input("Hey, do you want a drink? (yes, no): ")
            if shopKeeperQuestion.lower() == "yes":
                self.player.coins += 4
                if self.player.coins >= 3:
                    self.player.coins -= 3
                    print("Here's your drink...")
                    print(
                        "You look tough, head to the Tavern. My friend may need some help."
                    )
                    self.player.health += 2
                elif self.player.coins <= 2:
                    print("I doubt you have enough. Come back another time.")
            elif shopKeeperQuestion.lower() == "no":
                print("Alright, have yourself a good day")
                break
            else:
                print("What did you say??")


def townOne(player):
    while True:
        locationChoice = input(
            "Where do you want to go? (Tavern, Shop, Weapon Shop, Exit): "
        )
        if locationChoice.lower() == "tavern":
            print("There does not seem to be anything of interest in there...")
        elif locationChoice.lower() == "shop":
            shop = Shop(player)
            shop.shopMenu()
        elif locationChoice.lower() == "weapon shop":
            pass
        elif locationChoice.lower() == "exit":
            return player
        else:
            print("What do you mean?")


def main():
    print("Welcome to Greed Island")
    player_name = input("What is your name traveler?: ")
    # this creates a new value for the variable player_name
    # it is then passed as a parameter to the Player class and we reassign that entire
    # value as 'player' for ease of use when calling specific
    player = Player(player_name)

    while True:
        print("\nOptions:")
        print("1. Display Player Stats")
        print("2. Quit")
        print(
            f"================\n[🛡️  {player.name}]\n ❤️  : {player.health}\n Exp: {player.experience}\n================"
        )
        print("3. Continue...")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.displayStats()
        elif choice == "2":
            print("Goodbye")
            break
        elif choice == "3":
            print("A wise choice...")
            player = townOne(player)
        else:
            print("That's not a choice...")


if __name__ == "__main__":
    main()


# create game kinda like runescape
# so implement some sort of attack exp mining ect..
#
#
#
# #
