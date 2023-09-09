visited_cities = {}


def main():
    player_coins = 0
    player_name = input("Enter your username: ")
    print(f"Welcome to Greed Island, {player_name}!")
    print(f"Coins: {player_coins}")
    while True:
        choice = input("Choose a city (1, 2, 3) or 'q' to quit: ")
        if choice == "q":
            print("Goodbyeee")
            break
        elif choice == "1":
            if "city_one" not in visited_cities:
                visited_cities["city_one"] = True
                player_coins = city_one(player_name, player_coins)
            else:
                print("you have already visited this location")
        elif choice == "2":
            if "city_two" not in visited_cities:
                visited_cities["city_two"] = True
                player_coins = city_two(player_name, player_coins)
            else:
                print("you have already visited this location")
        elif choice == "3":
            if "city_three" not in visited_cities:
                visited_cities["city_three"] = True
                player_coins = city_three(player_name, player_coins)
            else:
                print("you have already visited this location")
        else:
            print("Invalid choice. Please select a valid option.")


def city_one(player_name, player_coins):
    # city logic
    print(
        f"Listen here {player_name}... I've been waiting.. hoping.. \n in search of the new light.. banished by the city titans.. left to live my eternal life in solitude.. but you.. you.. found me? Answer me {player_name}"
    )

    whatIsMyNameGuesser = input("What do you think my name is?: ")
    if whatIsMyNameGuesser == {player_name}:
        print("now you see.. here.. *tosses coin*")
        player_coins += 1
    else:
        print("you failed me.. move on...")
        pass

    EnteredNumber = int(input("Number: "))
    # print(f"Welcome to Lot22...\n enter a number {EnteredNumber}")
    if EnteredNumber < 50:
        player_coins += 1
        print("On to the next...")
        print(
            f" ~~~~~~~~~~~~~~~~~ \n Username: {player_name}\n Coins: {player_coins} \n ~~~~~~~~~~~~~~~~~"
        )
        # print(f"Username: {player_name}")
        # print(f"Coins: {player_coins}")
    else:
        print("you failed...")

    return player_coins  # returning updated player_coins


def city_two(player_name, player_coins):
    # city logic
    EnteredNumber = int(input("Number: "))
    print(f"Welcome to Lot23...\n enter a number {EnteredNumber}")
    if EnteredNumber < 50:
        player_coins += 1
        print("On to the next...")
        print(
            f" ~~~~~~~~~~~~~~~~~ \n Username: {player_name}\n Coins: {player_coins} \n ~~~~~~~~~~~~~~~~~"
        )
    else:
        print("you failed...")
    return player_coins


def city_three(player_name, player_coins):
    # city logic
    EnteredNumber = int(input("Number: "))
    print(f"Welcome to Lot24...\n enter a number {EnteredNumber}")
    if EnteredNumber < 50:
        player_coins += 1
        print("On to the next...")
        print(
            f" ~~~~~~~~~~~~~~~~~ \n Username: {player_name}\n Coins: {player_coins} \n ~~~~~~~~~~~~~~~~~"
        )
    else:
        print("you failed...")
    return player_coins


if __name__ == "__main__":
    main()

    # villages on the island have vendors.
    # one for bread and one for wine.
    # you can choose which village to enter then choose a vendor
    # CityOne = ["Hozen", "FarReach", "TumbleTown"]
    # CityTwo = ["BuckleBur", "SownCove", "Decelace"]
    # CityThree = ["Kyoni", "Lot22", "FarrowsEnclave"]

    # once you choose one of the cities you then pick a town
    # once you've selected a town you then will meet various vendors which you can buy itsms
    # you will have a small list of items you've collected
    # you have to collect 3 of them for the game to end.
    # each vendor will have a little dialog
