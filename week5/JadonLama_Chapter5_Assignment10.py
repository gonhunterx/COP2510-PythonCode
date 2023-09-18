# Feet to inches calculator


# creating the feet to inches function
def feet_to_inches(total_feet):
    total_inches = total_feet * 12
    return total_inches


def main():
    while True:
        total_feet = int(input("How many feet would you like to convert?: "))
        converted_to_inches = feet_to_inches(total_feet)
        print(f"The total in inches is: {converted_to_inches}")

        choice = input("Do you want to go again? (yes or no): ")
        if choice.lower() != "yes":
            break


main()
