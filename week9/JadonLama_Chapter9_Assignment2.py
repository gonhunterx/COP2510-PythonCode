# Quit the user for 5 states
# controls the number of times the user is quizzed
NUM_STATES = 5


def main():
    # initalize the state_caps dictionary
    state_caps = state_cap_dictionary()

    # initalize variables to keep count of
    # correct and incorrect responses
    correct = 0
    incorrect = 0

    # create a loop that will go off the value of NUM_STATES times
    for count in range(NUM_STATES):
        # get random entry from dictionary
        # here we are just naming state and capital
        # in regards to the way they are entered in the dictionary
        state, capital = state_caps.popitem()
        # quiz the user
        print("What is the capital of ", state, "? ", end="")
        response = input("Enter capital: ").strip()

        # is the users response correct?
        if response.lower() == capital.lower():
            correct += 1
            print("Correct!")
        else:
            print("Incorrect...")
            incorrect += 1
    # display results after NUM_STATES amount of tests
    print(f"You had {correct} correct responses")
    print(f"You had {incorrect} incorrect responses.")


# function containing the dictionary 'sc' which stands for state capitals
def state_cap_dictionary():
    sc = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "St. Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne",
    }
    return sc


# calling just the main function
if __name__ == "__main__":
    main()
