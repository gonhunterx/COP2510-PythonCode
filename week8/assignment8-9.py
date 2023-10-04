# word = input("Enter a string: ")
import sys


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


def menu():
    print("Main Menu")
    print("1. Go again")
    print("2. Quit")
    choice = input("Enter a choice: ")
    if choice == "1":
        main()
    elif choice == "2":
        sys.exit()
    else:
        menu()


def consonant_counter(word):
    # vowel list
    vowels = "aeiou"
    # accumulator
    c_total = 0
    # looping through each letter in the word
    for ch in word:
        # if letter is a consonant add to counter
        # adding .lower() so it takes more input options
        if ch.lower() not in vowels and ch.isalpha():
            c_total += 1
    # returning the updated total value
    return c_total


def main():
    # creating var for the functions to process
    answer = input("What is the word: ")
    # calling functions and printing their outputs
    print(f"Vowels: {vowel_counter(answer)}")
    print(f"Consonants: {consonant_counter(answer)}")
    menu()


menu()


# could be like this with arguments
# if you did not use an input for word
# print(vowel_counter("banana"))
