# even though it does not matter the names I chose to keep them the same for clearity
# function that calculates the monthly expenses which we then use to also calculate annual expenses.
def calcMonthlyExpenses(
    loan_payment,
    insurance_payment,
    gas_payment,
    oil_payment,
    tire_payment,
    maintenance_payment,
):
    # creating a variable that represents the total of all the input payments as taken from the main function.
    monthly_expenses = (
        loan_payment
        + insurance_payment
        + gas_payment
        + oil_payment
        + tire_payment
        + maintenance_payment
    )
    # return the updated value of monthly_expenses.
    return monthly_expenses


# creating main function to encapsulate the start and update features of the program.
def main():
    # while loop to make the program reusable without it breaking on its own.
    while True:
        # taking inputs for the variables so we can send them to the monthly expenses calculation function
        loan_payment = float(input("What is your monthly loan payment?: "))
        insurance_payment = float(input("What is your monthly insurance payment?: "))
        gas_payment = float(input("What is your monthly gas payment?: "))
        oil_payment = float(input("What is your monthly oil payment?: "))
        tire_payment = float(input("What is your monthly tire payment?: "))
        maintenance_payment = float(
            input("What is your monthly maintenance  payment?: ")
        )
        # creating the variable that calls the calcMonthlyExpenses function and passes
        # in the values from the inputs and preforms the function on those values
        monthly_costs = calcMonthlyExpenses(
            loan_payment,
            insurance_payment,
            gas_payment,
            oil_payment,
            tire_payment,
            maintenance_payment,
        )
        # creating a new variable for the annual costs using the monthly_costs total
        annual_payment = monthly_costs * 12
        # displaying the totals.
        print(f"Your monthly payment is: ${monthly_costs}")
        print(f"Your annual payment is: ${annual_payment}")

        # create choice to break out of loop and end program
        choice = input("Do you want to go again? yes or any key to quit: ")
        if choice.lower() != "yes":
            break


main()
