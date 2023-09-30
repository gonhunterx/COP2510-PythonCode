# Sum of numbers program
import sys


# creating a repeating menu for user ease.
def menu():
    print("Main menu")
    # 3 options for the user.
    print("1. Calculate total of numbers.txt file.")
    print("2. Read all values in numbers.txt file.")
    print("3. Quit Program")
    # choice logic for the menu
    choice = input("1, 2, or 3: ")
    if choice == "1":
        # calling the total of numbers function
        total_of_numbers()
    elif choice == "2":
        # calling the read all numbers function
        read_all_numbers()
    elif choice == "3":
        # exit program function
        sys.exit()
    else:
        print("Invalid choice")
        # go back to menu if invalid entry
        menu()


# reading all numbers in the file function
def read_all_numbers():
    # opening the file and assigning it as numbers_file
    with open("numbers.txt", "r") as numbers_file:
        # for loop to go through
        for line in numbers_file:
            print(line)
        menu()


def total_of_numbers():
    with open("numbers.txt", "r") as numbers_file:
        # itterating for each line in the file
        accumulator = 0
        for line in numbers_file:
            number = int(line)
            accumulator += number

        print(f"The total is: {accumulator}")
        menu()


def main():
    menu()


main()
