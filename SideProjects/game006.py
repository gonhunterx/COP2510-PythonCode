# List of objectives:
# Create a nice menu screen maybe one that is always there and if you are in a menu that is not
# create some sort of function that will estimate the price of a generated computer
import sys


class User:
    def __init__(self, name):
        self.name = name
        self.storage = []
        self.user_created = False


class Computer:
    def __init__(self, os, software, hardware, price):
        self.os = os
        self.software = software
        self.hardware = hardware
        self.price = price

    def display_comp_info(self):
        print("==========================")
        print(f"Installed OS: {self.os}")
        print(f"Installed Software: {self.software}")
        print(f"Specs: {self.hardware}")
        print(f"Price: ${self.price}")


def main_menu():
    create_user()

    print("Computer Creator")
    print("1. Create Computer")
    print("2. Generate Random Computer")
    print("3. Exit Program")
    choice = input("Input: ")
    if choice == "1":
        create_your_own_computer()
    elif choice == "2":
        pass
    elif choice == "3":
        sys.exit()
    else:
        print("invalid input.")


def create_user():
    user_name = input("Enter a username: ")
    user = User(user_name)
    user.user_created == True
    return user


def create_your_own_computer():
    # need to get the os, software, hardware, and price

    print("==========================")
    new_os = input("What is the operating system?: ")
    new_software = input("Select one from {list of software}: ")
    new_hardware = input("Select a Micro-processor(i3, i5, i7, i9): ")
    new_price = int(input("What price is the computer?: "))
    print(
        "Eventually there will be a generated value for price for now please add it. "
    )
    new_computer = Computer(new_os, new_software, new_hardware, new_price)
    new_computer.display_comp_info()
    main_menu()


# a_computer = Computer("Linux", "Google Chrome", "i9", 3000)
main_menu()
# a_computer.display_comp_info()
