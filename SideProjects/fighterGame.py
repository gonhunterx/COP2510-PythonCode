# create player function

# def player(name, health, gold):
#     name = input("What is your username?: ")
#     health = 10
#     gold = 0

enemies_defeated = {}


def main():
    player_name = input("What is your name sir?: ")
    player_health = 10
    player_coins = 0
    print(
        f"~~~~~~~~~~~~~~ \n Health: {player_health} \n Player: {player_name} \n Coins: {player_coins} \n ~~~~~~~~~~~~~~"
    )
    while player_health >= 0:
        choice = input("Choose your battle (1, 2, 3) or 'q' to quit: ")
        if choice == "q":
            print("Byeee")
            break
        elif choice == "1":
            print("Choice 1 selected")
            if "1" not in enemies_defeated:
                enemies_defeated["1"] = True
                player_coins, player_health = encounter_1(
                    player_coins, player_health, player_name
                )
        else:
            print("Thanks for playing")


def encounter_1(player_health, player_name, player_coins):
    print(
        f"~~~~~~~~~~~~~~ \n Health: {player_health} \n Player: {player_name} \n Coins: {player_coins} \n ~~~~~~~~~~~~~~"
    )


# def enemy():
#     enemy_name = "Zommet"
#     enemy_health = 8


if __name__ == "__main__":
    main()
