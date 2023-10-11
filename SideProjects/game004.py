import sys
import random

# starting with making the first decision based on whether they are younger or older than 5 assigned randomly.
# when you go into scineros you can gain or lose health, you always gain age after tasks or questions
# you can gain money and add items to your storage.


class Item:
    def __init__(self, name):
        self.name = name


ball = Item("ball")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.money = 0
        self.popularity = 0
        self.storage = []

    def display_stats(self):
        print("=========Stats=========")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Bank Value: {self.money}")
        print(f"Popularity: {self.popularity}")
        print("Inventory:")
        for item in self.storage:
            if self.storage == [""]:
                print("[empty]")
            else:
                print(f"- {item.name}")


# is there a way i could make a rolling system to help determine outcomes of perticular situations to make ther emore variance.
def main_menu(person):
    print("========Main Menu========")
    print("1. Continue")
    print("2. Exit Game")
    print("3. View Stats")
    main_menu_choice = input("Input:")
    if main_menu_choice == "1":
        if person.age in range(1, 5):
            one_to_four(person)
        elif person.age in range(5, 10):
            five_to_ten(person)
        elif person.age in range(10, 15):
            pass

    elif main_menu_choice == "2":
        sys.exit()
    elif main_menu_choice == "3":
        person.display_stats()
        main_menu(person)


def main():
    print("Welcome to Ichinasai Nedomi")
    print("What is your name traveler?")
    person_name = input("Input: ")
    starting_age = random.randint(2, 10)
    person = Person(person_name, starting_age)
    print("1. Continue...")
    print("2. Quit")
    first_choice = input("Input: ")
    if first_choice == "1":
        main_menu(person)
    elif first_choice == "2":
        sys.exit()
    else:
        print("Invalid input.")


def years_old(person):
    print("=================")
    print(f"[You are {person.age} years old]")


# best to do in while loops? idk probably or there is some other way todo something like this
def one_to_four(person):
    years_old(person)
    print(f"Well... you're {person.age} years old..")
    print("your mother holds you as you both watch television...")
    very_first_decision = input("You want to get up but do you? yes or no: ")
    if very_first_decision.lower() == "yes":
        person.age += 3
        person.health += 2
        print("You stand up and round around infront of the television.")
        main_menu(person)

    else:
        person.age += 3
        person.health -= 1
        print("You doze off on your mothers lap...")
        main_menu(person)


def five_to_ten(person):
    years_old(person)
    print(f"So... {person.age} years old..")
    print(
        f"you see another kid in the park who was mean to you eariler at school.. do you approach him or not? "
    )
    five_choice = input("Input(yes or no): ")
    if five_choice.lower() == "yes":
        print("You walk over to him and he looks sad...")
        print("Your presence makes him happier and he gives you a little ball!")
        person.storage.append(ball)
        person.age += 3
        person.health += 2
        main_menu(person)
    elif five_choice.lower() == "no":
        print("You walk past...")
        person.age += 3
        person.popularity -= 1
        main_menu(person)
    else:
        print("invalid input.")
        main_menu(person)


def eleven_to_fourteen():
    pass


def fifteen_to_twenty():
    pass


def twentyone_to_24():
    pass


def twentyfive_to_30():
    pass


main()


# could create places around town that age with the players age
def mall(person):
    if person.age > 50:
        print("The mall is being torn down...")


# do the increments needs to be lower? can there just be a fucntion full of questions?
# one to organize and then just call once a certain age is hit?
