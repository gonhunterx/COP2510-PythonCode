# Quit the user for 5 states
# controls the number of times the user is quizzed
import random

NUM_STATES = 5


def main():
    # initalize the state_caps dictionary
    state_caps = state_cap_dictionary()

    # initalize variables to keep count of
    # correct and incorrect responses
    correct = 0
    incorrect = 0

    # turning the dictionary into a list then shuffling it
    # for a truly random list
    # .keys() retrieves a list of keys from the dict
    states = list(state_caps.keys())
    random.shuffle(states)

    # create a loop that will go off the value of NUM_STATES times
    for count in range(NUM_STATES):
        # this will pop the last key value from the newly shuffled dict
        state = states.pop()
        # we are then assigning capital to the dictionary value and
        # using [state] to access the key's popped/associated values
        capital = state_caps[state]
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


if __name__ == "__main__":
    main()
