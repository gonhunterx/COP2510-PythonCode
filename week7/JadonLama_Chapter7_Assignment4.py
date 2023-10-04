# Number Analysis Program
# Ask the user to enter a series of 10 numbers
# Store the numbers in a list
# Display the following:
# Lowest number in list, highest number in list, total of list, average of list
# max min sum avg
import statistics
import sys


def displaying_data(main_list):
    # converting the values in the list to integers
    # I do this by creating a new variable (x) and x becomes the value in main_list at each instance read.
    # then it is converted into an int and now the new main_list variable has a list of integers.
    main_list = [int(x) for x in main_list]

    # calculations for the lowest, highest, total, and average values.
    lowest_value = min(main_list)
    highest_value = max(main_list)
    total_value = sum(main_list)
    # using the import statistics functions to calculate the mean
    average_value = statistics.mean(main_list)
    # printing the values with formatted strings.
    print(f"The lowest value is: {lowest_value}")
    print(f"The highest value is: {highest_value}")
    print(f"The total value is: {total_value}")
    print(f"The average value is: {average_value}")
    # creating a choice for the user to return to the main function and enter more data.
    choice = input("Do you want to go again?(yes or no): ")
    # logic for the choice
    if choice == "yes":
        main()
    else:
        sys.exit()


# main function to handle the program
def main():
    # creating a list of 7 values that will be stored in the main_list variable
    main_list = [0] * 7
    # using a for loop to create the 7 values entered by the user.
    for index in range(0, 7):
        main_list[index] = input("Please enter a number: ")
    # printing the main list after the user has entered the values.
    print(main_list)
    # bar for clearity in the program
    print("===============================")
    # calling the displaying_data function and passing main_list as a parameter.
    displaying_data(main_list)


# calling the main function.
main()
