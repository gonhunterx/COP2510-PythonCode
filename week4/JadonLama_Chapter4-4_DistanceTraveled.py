# Distance traveled calculator
# distance = speed * time


# function for calculating average distance per hour based on speed * time traveled
def distanceCalculator(hours_traveled, vehicle_speed):
    for inital_hour in range(hours_traveled):
        distance = vehicle_speed / hours_traveled
        print(f"Hour  Distance Traveled\n{inital_hour+1}     {distance} miles")


def main():
    # creating a while loop to keep the program running until a break is initiated
    while True:
        # Variables
        vehicle_speed = int(input("What is the vehicles speed(MPH)?: "))
        hours_traveled = int(input("How many hours did you travel?: "))
        # calling the speedCalculator function and passing parameters to it for the calculation with the given inputs as their values.
        distanceCalculator(hours_traveled, vehicle_speed)
        # adding a choice to continue. this makes it so once the main program has
        # run the string below will appear and it assumes that if you type anything
        # besides yes that you are done.
        choice = input("Do you want to go again? yes or no: ")
        if choice.lower() != "yes":
            break


# calling the main function
if __name__ == "__main__":
    main()
