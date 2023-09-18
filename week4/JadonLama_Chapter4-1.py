def bugs_per_day(day_num):
    bugs_each_day = input("How many bugs did you catch on day {}: ".format(day_num))
    return int(bugs_each_day)


def main():
    while True:
        total_bugs = 0
        for num in range(5):
            bugs = bugs_per_day(num + 1)
            total_bugs += bugs
        print("Total bugs caught in a week:", total_bugs)

        choice = input("Do you want to go again? (yes or no): ")
        if choice.lower() != "yes":
            break


main()
