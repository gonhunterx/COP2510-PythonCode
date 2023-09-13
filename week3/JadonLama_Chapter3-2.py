# Program for comparing the area of two rectangles


# calculating the area
# passing r1w, r1h, r2w, r2h in place of rectangle width and height values with
# associated numbers corresponding to the inital rectangle's dimensions.
def calculate_area(r1w, r1h, r2w, r2h):
    area_rectangle_one = r1w * r1h
    area_rectangle_two = r2w * r2h
    # creating the if statement to handle comparison logic
    if area_rectangle_one > area_rectangle_two:
        print("The first rectangle's area is greater.")
    elif area_rectangle_one < area_rectangle_two:
        print("The second rectangle's area is greater.")
    # assume that the dimensions are equal since the above checks for every other
    # possible value.
    else:
        print("They have the same area.")


while True:
    # ask for the rectangles width and height
    rectangle_one_width = int(input("What is the first rectangles width?: "))
    rectangle_one_height = int(input("What is the first rectangles height?: "))
    rectangle_two_width = int(input("What is the second rectangles width?: "))
    rectangle_two_height = int(input("What is the second rectangles hight?: "))
    # calling the calculate_area function with the values given by the inputs
    # called above
    calculate_area(
        rectangle_one_width,
        rectangle_one_height,
        rectangle_two_width,
        rectangle_two_height,
    )
    # creating an option for the user to continue or quit the program
    choice = input("Do you want to go again? yes or no: ")
    # using .lower() function to change input to all lowercase for checking input
    if choice.lower() != "yes":
        break
