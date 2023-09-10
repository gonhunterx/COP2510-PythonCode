# Distance traveled calculator
# distance = speed * time


# Variables
vehicle_speed = int(input("What is the vehicles speed(MPH)?: "))
hours_traveled = int(input("How many hours did you travel?: "))


# function for calculating average speed per hour based on speed * time traveled
def speedCalculator():
    for inital_hour in range(hours_traveled):
        speedPerHour = vehicle_speed / hours_traveled
        print(f"Hour {inital_hour+1}: Traveling at {speedPerHour} MPH")


speedCalculator()
