# pet class with attributes

added_pets = []


class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_pet_attributes(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_pet_attributes(self):
        return self.__name, self.__animal_type, self.__age

    def __str__(self):
        return f"Name: {self.__name}, Type: {self.__animal_type}, Age: {self.__age}"


def add_pet(new_pet):
    updated_pets_list = added_pets.append(new_pet)
    return updated_pets_list


def display_added_pets():
    print(str(added_pets))


def main():
    print("Welcome to the pet manager application!")
    print("Enter your pet's attributes:")
    while True:
        try:
            pet_name = input("Enter your pet's name: ")
            pet_type = input("Enter your pet's type: ")
            pet_age = input("Enter your pet's age: ")

            new_pet = Pet(pet_name, pet_type, pet_age)

            print(str(new_pet))

        except Exception as e:
            print(f"Error at {e}")


main()
