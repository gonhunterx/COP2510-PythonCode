import sys


# Creating a class for what the Initials objects can contain and adjust.
class Initials:
    # initalizing the class with first, middle, and last name arguments.
    def __init__(self, first, middle, last):
        # stating that if the class is called the inputs can be changed.
        # attributes created, but not listed as arguments can be appended and manipulated, but are
        # not usually directly called with a given value from what I understand.
        self.first = first
        self.middle = middle
        self.last = last

    # creating a method within the Initials class to call for calculating the initials.
    def calculate_initials(self):
        # declaing the variable names and using values given to the method for return value.
        # using first[0] grabs the item at the first index of the string.
        first_initial = self.first[0].upper()
        middle_initial = self.middle[0].upper()
        last_initial = self.last[0].upper()
        return f"Initials: {first_initial}. {middle_initial}. {last_initial}."


# main menu function for ease of use.
def main_menu():
    print(
        """
=====================
1. Calculate initials
2. View generated initials
3. Exit program
          """
    )
    # storing the main_menu_choice and returning it so we can use that value for if statement logic.
    main_menu_choice = input("Input: ")
    return main_menu_choice


def generate_initials():
    # creating a while loop so if you enter invalid inputs it takes you back to the beginning.
    while True:
        # using a try except statement for better error handling.
        try:
            first_name = input("Enter first name: ").strip()
            middle_name = input("Enter middle name: ").strip()
            last_name = input("Enter last name: ").strip()
        # used for exiting the program when commands like ^C are used.
        except KeyboardInterrupt:
            print("\nExiting the program.")
            # importing system to use the exit function from its library.
            sys.exit()
            # creating a general exception statement to catch general errors
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        # if statement to make sure the values entered are alphabetical for initials.
        if first_name.isalpha() and middle_name.isalpha() and last_name.isalpha():
            # passing the new variables tp the Initials class so we can use them.
            return Initials(first_name, middle_name, last_name)
        # handling more invalid inputs
        else:
            print(
                "Please enter valid alphabetical names without numbers or special characters."
            )


# Main function
def main():
    print("=====================")
    print("Welcome to the Initial Calculator")
    # creating a list to store initials that have been generated during current session.
    generated_initials_list = []  # Initialize a list to store generated initials
    while True:
        # taking the selection from the main_menu function.
        main_menu_selection = main_menu()
        # logic for return value from main_menu()
        if main_menu_selection == "1":
            # creating a variable to represent the generate_initials function.
            generated_initials = generate_initials()
            # appending the results from generate_initials() to the genereated_initials_list for viewing later
            generated_initials_list.append(generated_initials)  # Add to the list
            print("=====================")
            print(generated_initials.calculate_initials())
        # logic for displaying the list of initials stored in the generated_initials_list
        elif main_menu_selection == "2":
            # checking to see if the list is empty an if statement with
            # nothing besides the name checks if it has values
            if generated_initials_list:
                print("=====================")
                # for loop to go through each item in the generated_initials_list.
                for initials in generated_initials_list:
                    print(initials.calculate_initials())
            # if generated_initials_list is empty.
            else:
                print("No initials have been calculated yet.")
        # leaving the while loop.
        elif main_menu_selection == "3":
            break


# Calling the main function.
if __name__ == "__main__":
    main()
