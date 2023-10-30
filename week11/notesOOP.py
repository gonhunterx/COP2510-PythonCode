# Classes and OOP


class Insect:
    def __init__(self, name, flight_speed):
        self.name = name
        self.flight_speed = flight_speed


housefly = Insect("Housefly", 12)
misquito = Insect("Misquito", 4)
print(f"{housefly.name}, has a flight speed of {housefly.flight_speed} MPH")

# to make an attribute private use __ before it.

# methods are accessors or mutators. Which makes sense.


class MyRectangle1:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return 2 * (self.width + self.height)
