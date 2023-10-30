# Chapter 9 Assignment 1
# using temporary storage for a user instance


class 


# user class and its methods
class User:
    def __init__(self, username):
        # creating a username to pass for the User class. Along with a list to store added classes
        self.username = username
        self.added_classes = []

    # Method to append chosen classes to the added_classes list
    def add_class(self, data):
        self.added_classes.append(data)
        print("Class added to schedule")

    # Method to view classes you have added.
    def view_added_classes(self):
        # if the added_classes returns true execute the if statement
        if self.added_classes:
            print("=========================")
            print(f"Registered Classes for {self.username}:")
            # printing the added classes
            print(self.added_classes)
        # else print that the classes list is empty
        else:
            print("[Empty]")

    # Method to remove classes from the list
    def remove_classes(self, data_to_delete):
        # removing the input data from the list
        self.added_classes.remove(data_to_delete)


# dictionary for avaliable classes
classes_dict = {
    "CS101": {"Number": 3004, "Professor": "Haynes", "Time": "8:00 a.m."},
    "CS102": {"Number": 4501, "Professor": "Alvarado", "Time": "9:00 a.m."},
    "CS103": {"Number": 6755, "Professor": "Rich", "Time": "10:00 a.m."},
    "NT110": {"Number": 1244, "Professor": "Burke", "Time": "11:00 a.m."},
    "CM241": {"Number": 1411, "Professor": "Lee", "Time": "1:00 p.m."},
}
# main menu options
# creating an object from a choice of the items in classes_dict


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


# main menu that returns a choice taken from an input the user enters
def options_menu():
    print(
        """
=========================
1. View avaliable classes 
2. Register for classes
3. View registered schedule
4. Remove classes from schedule 
'q' to exit
          """
    )
    # getting the input from user
    choice = input("Input: ")
    return choice


def create_user():
    username = input("Please enter a username: ")
    # create an object that represents the User class and allows access to its methods.
    global user
    user = User(username)
    return user


def main(user_created=False):
    # Printing inital message
    print("Computer Science Class Organizer")
    print("=========================")
    if not user_created:
        create_user()
        user_created = True
    # getting the username from the user to pass through the User class
    # if not user_created:
    #     username = input("Please enter a username: ")
    #     # create an object that represents the User class and allows access to its methods.
    #     global user
    #     user = User(username)
    # print(user.add_class("CS101"))


def main_menu():
    # while loop so keep manipulating the user object
    while True:
        # creating a variable that contains the returned value of the main menu function
        choice = options_menu()
        if choice == "1":
            # call the view classes function
            view_avaliable_classes()
        elif choice == "2":
            # get the data to pass into the add class method from the User class
            data = input("Input class name: ")
            print(data)
            user = user.add_class(data)
        elif choice == "3":
            # call the user objects view added classes method
            user = user.view_added_classes()
        elif choice == "4":
            # call the user objects remove classes method
            user = user.remove_classes()
        elif choice.lower() == "q":
            # allow the user to break out of the loop
            break
        else:
            print("Invalid input.")


# calling only the main function.
if __name__ == "__main__":
    main()
