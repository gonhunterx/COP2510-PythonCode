#
import sys


def main_menu():
    print("MAIN MENU")
    print("1. Add to note card")
    print("2. View note card")
    print("3. Quit")
    choice = input("1, 2, or 3: ")
    if choice == "1":
        add_to_notecard()
    elif choice == "2":
        pass
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid entry.")


# so lets say its like you create a 'notecard' and these
# notecards can store a string of data.
# 3 total note cards
notecard2 = input("Note card 2 entry: ")
notecard3 = input("Note card 3 entry: ")


class Notecard:
    def __init__(self, note_card_number, note_card_data):
        self.note_card_number = note_card_number
        self.note_card_data = note_card_data

    def display_notecard(self):
        print(self.note_card_number)


added_notecards = {}


def add_to_notecard():
    notecard1 = input("Note card 1 entry: ")
    added_notecards.append(notecard1)


main_menu()
