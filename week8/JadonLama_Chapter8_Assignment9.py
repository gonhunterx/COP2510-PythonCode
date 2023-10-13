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
    # returning to the main function after the results function completes.
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


# main function for the program.
def main():
    # menu features
    print("Main menu")
    print("1. Vowel and Consonant Counter")
    print("2. Exit Program")
    # choice for the user to make concerning the menu
    choice = input("Enter a choice: ")
    if choice == "1":
        results()
    elif choice == "2":
        # exit the program
        sys.exit()
    # catching incorrect inputs
    else:
        print("Invalid Input.")
        main()


# calling the main function
if __name__ == "__main__":
    main()
