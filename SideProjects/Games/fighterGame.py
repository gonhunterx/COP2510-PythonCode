# CLI Adventure mini-game ^-^
# by jadon L
enemies_defeated = {}


def main():
    player_name = input("What is your name sir?: ")
    player_health = 10
    player_coins = 0
    print(
        f"~~~~~~~~~~~~~~ \n Health: {player_health} \n Player: {player_name} \n Coins: {player_coins} \n~~~~~~~~~~~~~~"
    )
    while player_health > 0:
        choice = input("Choose your battle (1, 2, 3) or 'q' to quit: ")
        if choice == "q":
            print("Byeee")
            break
        elif choice == "1":
            print("Choice 1 selected")
            if "1" not in enemies_defeated:
                enemies_defeated["1"] = True
                player_coins, player_health = encounter_one(
                    player_health, player_name, player_coins
                )
            else:
                print("you have already defeated the boss of this town.")
        elif choice == "2":
            print("Choice 2 selected")
            if "1" not in enemies_defeated:
                enemies_defeated["2"] = True
                player_coins, player_health = encounter_two(
                    player_health, player_name, player_coins
                )
        elif choice == "3":
            print("Choice 3 selected")
            if "1" not in enemies_defeated:
                enemies_defeated["3"] = True
                player_coins, player_health = encounter_three(
                    player_health, player_name, player_coins
                )
        else:
            print("Thanks for playing")
        return player_coins, player_health


# enemy one : fire type takes damage from water type abilities
# name : dotto health: 10 damage: 2
def player():
    damage = 2
    return damage


def fireEnemy():
    enemy_health = 10
    enemy_name = "dotto"
    enemy_damge = 2
    return enemy_health, enemy_name, enemy_damge


# once the function is called with the vars you have to have them in order
# or else it will switch the order in the cli interface.
def encounter_one(player_health, player_name, player_coins):
    # playerHealth = player_health

    print(
        f"~~~~~~~~~~~~~~ \n Health: {player_health} \n Player: {player_name} \n Coins: {player_coins} \n~~~~~~~~~~~~~~"
    )

    return player_health, player_coins


def encounter_two(player_health, player_name, player_coins):
    print(
        f"~~~~~~~~~~~~~~ \n Health: {player_health} \n Player: {player_name} \n Coins: {player_coins} \n~~~~~~~~~~~~~~"
    )
    return player_coins, player_health


def encounter_three(player_health, player_name, player_coins):
    print(
        f"~~~~~~~~~~~~~~ \n Health: {player_health} \n Player: {player_name} \n Coins: {player_coins} \n~~~~~~~~~~~~~~"
    )
    return player_coins, player_health


# def enemy():
#     enemy_name = "Zommet"
#     enemy_health = 8


# add in tier sets?
# make it so you can build a house and upgrade it?
# make it so that you can choose to fight the same boss again, but you get less exp
# keep coins add exp
#
#
# #

if __name__ == "__main__":
    main()
