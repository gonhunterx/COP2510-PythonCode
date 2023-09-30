# Golf Scores and player names organization program
# importing sys for easy exit inside or outside of loops
import sys


# main menu function
def menu():
    # styling for the menu :)
    print("================")
    # list of options to select from
    print("1. Enter Data")
    print("2. Read Data")
    print("3. Clear Data")
    # creating an exit from the program
    print("4. Quit")
    # creating the variable for the main menu choice.
    choice = input("Please select an option [1-4]: ")
    # if statement for the logic behind the menu by entering numbers in the form of strings then just reading them
    # this will determine which function to call based on user input.
    if choice == "1":
        edit_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        clear_data()
    elif choice == "4":
        # exits program.
        sys.exit()
    # catching if anything else is entered.
    else:
        print("Invalid choice.")
        menu()


# function to clear the data.
def clear_data():
    # confrimation before actually just clearning all data
    confrimation = input("Are you sure you want to delete all data?: (yes or no): ")
    # if statement for result of confrimation
    if confrimation.lower() == "yes":
        # try opening and writing over it (when the file is opened in "w" then closed
        # it truncates the existing content)
        try:
            # this line opens and closes the file in write mode which will clear it.
            open("gulf.txt", "w").close()
            print("Cleared.")
            menu()
        # error handling while trying to truncate the file.
        except Exception as e:
            # using Exception and naming it 'e' to easily print it rather than typing Exception again.
            print(f"An error occured: {e}")
    else:
        # if no is selected we are going back the the main menu
        print("Data not cleared.")
        # right now once this else statement executes you are sent directly into adding a new player name and score.
        # Fixed by adding the menu function here it sends you back
        menu()
        # using menu() in else statements works well because then you can essentially default back to the menu


def edit_file():
    # using 'a' to append data to the file
    with open("gulf.txt", "a") as gulfscoresFile:
        # CREATING the player_name and gulf_score variables.
        player_name = input("What is the player's name?: ")
        gulf_score = input("What is the associated score?: ")
        # trying to create the logic for if someone enters no data.
        # if player_name != "" and gulf_score != "":
        # write the data in columns with commas
        gulfscoresFile.write(f"{player_name}, {gulf_score}\n")
        print("Saved.")
    # again variable is created to store the input of the user to determine if they want to go again.
    # must take this part of the function outside of the with statement. So it will go to the second part AFTER already closing the file.
    again = input("Do you want to enter more data? (yes or no): ")
    # checking if the user wants to enter more data.
    if again.lower() == "yes":
        # going to the edit_file() function to enter more data.
        edit_file()
    else:
        # returning to menu() with the function call
        menu()
        # else:
        #     print("Player name and score can not be empty.")


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
