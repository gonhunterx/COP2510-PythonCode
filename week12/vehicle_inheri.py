class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def car_info(self):
        return f"{self.display_info()}, {self.num_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def bike_info(self):
        return f"{self.display_info()}, {self.engine_size} engine"


def main():
    # Gathering input for Car
    car_make = input("Enter car make: ")
    car_model = input("Enter car model: ")
    car_year = input("Enter car year: ")
    # Extra parameter for Car subclass
    car_doors = input("Enter number of doors: ")

    # Creating instance of Car
    my_car = Car(car_make, car_model, car_year, car_doors)

    # Gathering input for Motorcycle
    bike_make = input("Enter motorcycle make: ")
    bike_model = input("Enter motorcycle model: ")
    bike_year = input("Enter motorcycle year: ")
    # Extra parameter for Motercycle subclass
    bike_engine = input("Enter engine size: ")

    # Creating instance of Motorcycle (storing it)
    my_bike = Motorcycle(bike_make, bike_model, bike_year, bike_engine)

    # Displaying information
    print("Car Information:", my_car.car_info())
    print("Motorcycle Information:", my_bike.bike_info())


if __name__ == "__main__":
    main()
