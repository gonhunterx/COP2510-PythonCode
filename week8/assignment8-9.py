# word = input("Enter a string: ")
import sys


def results():
    # creating var for the functions to process
    answer = input("What is the word: ")
    print("===================")
    # calling functions and printing their outputs
    print(f"Vowels: {vowel_counter(answer)}")
    print(f"Consonants: {consonant_counter(answer)}")
    print("===================")
    main()


def vowel_counter(word):
    # vowel list
    vowels = "aeiou"
    # accumulator
    v_total = 0
    # looping through each letter in the word
    for ch in word:
        # if letter is a vowel add to counter
        # adding .lower() so it takes more input options
        if ch.lower() in vowels and ch.isalpha():
            v_total += 1
    # returning the updated total value
    return v_total


def consonant_counter(word):
    # vowel list
    vowels = "aeiou"
    # accumulator
    c_total = 0
    # looping through each letter in the word
    for ch in word:
        # if letter is a consonant add to counter
        # adding .lower() so it takes more input options
        # isalpha means is alphabet
        if ch.lower() not in vowels and ch.isalpha():
            c_total += 1
    # returning the updated total value
    return c_total


def main():
    print("Main menu")
    print("1. Vowel and Consonant Counter")
    print("2. Exit Program")
    choice = input("Enter a choice: ")
    if choice == "1":
        results()
    elif choice == "2":
        sys.exit()
    else:
        print("Invalid Input.")
        main()


# calling the main function
if __name__ == "__main__":
    main()


# could be like this with arguments
# if you did not use an input for word
# print(vowel_counter("banana"))


# NOTES
# I think that what is in the main function should be its own function and the results should
# just be in the main function.
