def main():
    player_name = input("Enter your username: ")
    player_coins = 0 
    print(f"Welcome to Greed Island, {player_name}")
    print(f"Coins: {player_coins}")
    
    cities = [
        {"name": "city_one", "function": city_one}
        {"name": "city_two", "function": city_two}
        {"name": "city_three", "function": city_three} 
    ]
    
    visited_cities = {}
    
    while True:
        choice = input("Choose a city (1, 2, 3) or 'q' to quit: ")
        if choice == "q":
            print("Goodbyeee")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(cities):
            city_index = int(choice) - 1
            city = cities[city_index]
            city_name = city["name"]
            city_function = city["function"]
            if city_name not in visited_cities:
                visited_cities[city_name] = True
                player_coins = city_function(player_name, player_coins)
            else:
                print("You have already visited this location...")
        else:
            print("Invalid choice. Select another option")
            
def city_one():
    