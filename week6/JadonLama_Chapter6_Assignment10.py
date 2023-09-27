# Golf Scores and player names organization program
# importing sys for easy exit inside or outside of loops
import sys

gulf_data = []


# main menu function
def menu():
    print("1. Enter Data")
    print("2. Read Data")
    print("3. Clear Data")
    print("4. Quit")
    choice = input("Please select an option: ")
    if choice == "1":
        edit_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        clear_data()
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid choice.")


# function to clear the data.
def clear_data():
    # confrimation before actually just clearning all data
    confrimation = input("Are you sure you want to delete all data?: (yes or no): ")
    # if statement for result of confrimation
    if confrimation.lower() == "yes":
        # try opening and writing over it (when the file is opened in "w" then closed
        # it truncates the existing content)
        try:
            open("gulf.txt", "w").close()
            print("Cleared")
        # error handling while trying to truncate the file.
        except Exception as e:
            print(f"An error occured: {e}")
    else:
        print("Data not cleared.")


def edit_file():
    while True:
        # using 'a' to append data to the file
        with open("gulf.txt", "a") as gulfscoresFile:
            player_name = input("What is the player's name?: ")
            gulf_score = input("What is the associated score?: ")
            # write the data in columns with commas
            gulfscoresFile.write(f"{player_name}, {gulf_score}\n")
            print("Saved.")

        again = input("Do you want to enter more data? (yes or no): ")
        if again.lower() == "yes":
            edit_file()
        else:
            menu()


def read_file():
    print("Gulf Score Data:")
    try:
        # 'with' automatically handles opening and closing files so we use that
        with open("gulf.txt", "r") as gulfscoresFile:
            # iterating over each line in the gulf.txt file renamed as gulfscoresFile for ease of use
            # and creating the line var to represent each line in the txt
            for line in gulfscoresFile:
                # line.strip().split(", ") is for formatting the return for each line
                # strip removes any extra characters form the beginning and end
                # split creates two columns seperated by the ", "
                player_name, gulf_score = line.strip().split(", ")
                # printing each line
                print(f"Player: {player_name}, Score: {gulf_score}")
    # creating a catch incase there is not a file already created
    except FileNotFoundError:
        print("No file found.")
    return menu()


# main function
def main():
    menu()


# call the main function
main()
