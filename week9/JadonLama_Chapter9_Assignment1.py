# dictionary for avaliable classes
classes_dict = {
    "CS101": {"Number": 3004, "Professor": "Haynes", "Time": "8:00 a.m."},
    "CS102": {"Number": 4501, "Professor": "Alvarado", "Time": "9:00 a.m."},
    "CS103": {"Number": 6755, "Professor": "Rich", "Time": "10:00 a.m."},
    "NT110": {"Number": 1244, "Professor": "Burke", "Time": "11:00 a.m."},
    "CM241": {"Number": 1411, "Professor": "Lee", "Time": "1:00 p.m."},
}


# function to view the classes
def view_avaliable_classes():
    # try for error handling
    try:
        while True:
            print("Classes:")
            for key in classes_dict.keys():
                # print each key in the dictionary
                print(key)
            print("=========================")
            print("'q' to quit")
            print(
                "Please input a class number from the list above for more information."
            )
            choice = input("Input: ").upper()
            # checking if the choice input is in the classes dict.
            if choice in classes_dict:
                # printing the input class and printing it out of the dictionary
                print(classes_dict[choice])
            elif choice.lower() == "q":
                break
            else:
                print("Invalid class number. ")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # creating an object from a choice of the items in classes_dict
    classes = view_avaliable_classes()
    # printing the object
    print(classes)


if __name__ == "__main__":
    main()
