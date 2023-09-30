# Sum of numbers program
import sys


# creating a repeating menu for user ease.
def menu():
    print("==============")
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
    # try except statements for error handling
    try:
        # opening the file and assigning it as numbers_file
        with open("numbers.txt", "r") as numbers_file:
            # for loop to go through the file lines
            for line in numbers_file:
                print(line)
            menu()
    except Exception as e:
        print(f"Error: {e}")


def total_of_numbers():
    # try except statements for error handling
    try:
        # opening the file and assigning it as numbers_file
        with open("numbers.txt", "r") as numbers_file:
            # iterating for each line in the file
            accumulator = 0
            # for loop to go through the file
            for line in numbers_file:
                # convert the lines values to intigers
                number = int(line)
                # add the numbers to the accumulator
                accumulator += number
            # print the accumulators value after the loop completes
            print(f"The total is: {accumulator}")
            # return to the menu
            menu()
    except Exception as e:
        print(f"Error: {e}")


def main():
    menu()


main()
