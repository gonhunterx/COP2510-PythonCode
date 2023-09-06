# Distance traveled calculator
# distance = speed * time

# accumulators
miles_traveled = 0
# Variables

vehicle_speed = int(input("What is the vehicles speed(MPH)?: "))
hours_traveled = int(input("How many hours did you travel?: "))


def distanceTraveled():
    for inital_hour in range(hours_traveled):
        distance = vehicle_speed / hours_traveled
        print(f"Hour {inital_hour+1}: Traveling at {distance} MPH")


distanceTraveled()
