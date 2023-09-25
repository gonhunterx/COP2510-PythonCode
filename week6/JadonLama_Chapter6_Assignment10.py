# Golf Scores and player names organization program

gulf_data = []


def menu():
    print("1. Enter Data")
    print("2. Read Data")
    print("3. Quit")
    choice = input("Please select an option: ")
    if choice == "1":
        edit_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        return
    else:
        print("Invalid choice.")


def edit_file():
    while True:
        gulfscoresFile = open("gulf.txt", "w")
        player_name = input("What is the players name you want to add?: ")
        gulf_score = input("What is the score you would like to add?: ")
        gulfscoresFile.write(str(player_name + ", " + gulf_score) + "\n")

        gulfscoresFile.close()
        print("Saved")
        again = input("Do you want to enter more data?(yes or no): ")
        if again.lower() == "yes":
            return
        else:
            break


def read_file():
    print("Gulf Score Data:")
    for player_name, gulf_score in gulf_data:
        print(f"Player: {player_name}, Score: {gulf_score}")


def main():
    menu()


main()
