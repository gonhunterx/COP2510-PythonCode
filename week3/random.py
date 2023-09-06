def get_float_input(prompt_message):
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("That's not a valid number. Please try again.")

def calculate_area(height, width):
    return height * width

def main():
    print("Let's compare the areas of two rectangles!")

    # Ask for the dimensions of the first rectangle
    rectangleHeight1 = get_float_input('What is the first rectangles height? ')
    rectangleWidth1 = get_float_input('What is the first rectangles width? ')

    # Ask for the dimensions of the second rectangle
    rectangleHeight2 = get_float_input('What is the second rectangles height? ')
    rectangleWidth2 = get_float_input('What is the second rectangles width? ')

    # Calculate the area of the rectangles
    area1 = calculate_area(rectangleHeight1, rectangleWidth1)
    area2 = calculate_area(rectangleHeight2, rectangleWidth2)

    # Compare the areas
    if(area1 > area2):
        print('Rectangle 1 has the greater area.')
    elif(area2 > area1):
        print('Rectangle 2 has the greater area.')
    else:
        print('Both rectangles have the same area.')

if __name__ == "__main__":
    main()
