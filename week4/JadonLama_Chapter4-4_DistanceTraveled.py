# Distance traveled calculator
# distance = speed * time


# function for calculating distance per hour based on speed * time traveled
def distanceCalculator(vehicle_speed, hours_traveled):
    # creating an accumulator for total distance storage
    # this will store each instance of the
    total_distance = 0
    # displaying the header for the function when called
    print("Hours   Distance Traveled")
    # creating the for loop to get all values between 1 and the input value
    for hour in range(hours_traveled):
        # creating a distance per hour to break up the total distance
        distance_per_hour = vehicle_speed * (hour + 1)
        # adding the distance per hour to the
        total_distance += distance_per_hour
        # using the .format method I apply maximum widths to the responses
        # space length. This makes it so that numbers will not push each other
        # when a number gains a digit.
        print("{:<7} {:<15}".format((hour + 1), distance_per_hour))
    return total_distance


def main():
    # creating a while loop to keep the program running until a break is initiated
    while True:
        # Variables
        vehicle_speed = int(input("What is the vehicles speed(MPH)?: "))
        hours_traveled = int(input("How many hours did you travel?: "))
        # calling the distanceCalculator function and passing parameters to it for the calculation with the given inputs as their values.
        distanceCalculator(vehicle_speed, hours_traveled)

        # adding a choice to continue. this makes it so once the main program has
        # run the string below will appear and it assumes that if you type anything
        # besides yes that you are done.
        choice = input("Do you want to go again? yes or no: ")
        if choice.lower() != "yes":
            break


# calling the main function
if __name__ == "__main__":
    main()
