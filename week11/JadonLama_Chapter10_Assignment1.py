# pet class with attributes


# pet class
class Pet:
    # initalizing the Pet class with 3 parameters.
    def __init__(self, name, animal_type, age):
        # creating private attributes for the pet class that can be set and retrieved.
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # method for setting the attributes
    def set_pet_attributes(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # method for getting the attributes
    def get_pet_attributes(self):
        return self.__name, self.__animal_type, self.__age

    # a return method that will make the object a formatted string.
    def __str__(self):
        return f"Name: {self.__name}, Type: {self.__animal_type}, Age: {self.__age}"


# main function for running the program
def main():
    # intro to application
    print("Welcome to the pet manager application!")
    # while loop for
    while True:
        # try except statement for error handling and testing
        try:
            print("Enter your pet's attributes")
            # creating variables to pass to the class and create an object
            pet_name = input("Enter your pet's name: ")
            pet_type = input("Enter your pet's type: ")
            pet_age = input("Enter your pet's age: ")
            # giving a way out of the loop
            compile_or_not = input("'q' to quit or 1 to continue: ")
            # checking if the input is q
            if compile_or_not.lower() == "q":
                # breaking the loop and exiting the program
                break
            else:
                # if not we create the new pet object and print it as a string
                new_pet = Pet(pet_name, pet_type, pet_age)
                # using the __str__ method to decode the object in a formatted manner
                print("=" * 20)
                print(str(new_pet))
                print("=" * 20)
        # exception handling to check for errors
        except Exception as e:
            print(f"Error at {e}")


# calling the main function only
if __name__ == "__main__":
    main()
