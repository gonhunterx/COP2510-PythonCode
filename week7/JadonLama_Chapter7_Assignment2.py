# importing random for random.randint
import random


def main():
    # this means we will repeat this list element 7 times
    numbers = [0] * 7
    # using a for loop to itterate through the list
    for index in range(7):
        # passing in the random numbers we generate at each index of the list.
        numbers[index] = random.randint(0, 60)
    print(sum(numbers))


main()
