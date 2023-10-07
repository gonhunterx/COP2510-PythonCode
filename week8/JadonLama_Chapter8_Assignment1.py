# def get_users_full_name():
#     first_name = input("What is your first name?: ")
#     middle_name = input("What is your middle name?: ")
#     last_name = input("What is your last name?: ")


def main():
    print("Inital Calculator")
    first_name = [input("Enter first name: ")]
    middle_name = [input("Enter middle name: ")]
    last_name = [input("Enter last name: ")]
    for i in first_name:
        for j in i:
            first_inital = j
            break
    for i in middle_name:
        for j in i:
            middle_inital = j
            break
    for i in last_name:
        for j in i:
            last_inital = j
            break
    print(f"{first_inital.upper()}. {middle_inital.upper()}. {last_inital.upper()}")


main()
