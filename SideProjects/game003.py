import sys


class Folder:
    def __init__(self, name):
        self.name = name
        self.contained_files = []

    def display_contents(self):
        print(f"Folder name: {self.name}")
        print(f"Files: {self.contained_files}")

    def create_folder(self):
        folder_name = input("What do you want to name your folder: ")
        folder = Folder(folder_name)
        return folder


def main_menu():
    print("Main Menu:")
    print("1. ")


def main():
    print("Welcome to Lama Mage the folder manipulation application")
    print("Selection an option: ")
    print("1. Go to main menu and create a folder")
    print("2. Quit")
    main_choice = input("Input: ")
    if main_choice == "1":
        main_menu()
    elif main_choice == "2":
        sys.exit()
    else:
        print("Incorrect input.")


if __name__ == "__main__":
    main()
