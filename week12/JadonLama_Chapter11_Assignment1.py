# Create an employee main class which can be used to create specific types of employees
class Employee:
    def __init__(self, name, e_number):
        self.name = name
        self.e_number = e_number

    # methods for setting the values of the employee class
    def set_name(self, name):
        self.name = name

    def set_pay(self, e_number):
        self.e_number = e_number

    # getting the information from the set values
    def get_name(self):
        return self.name

    def get_e_number(self):
        return self.e_number


# child class (subclass)
class ProductionWorker(Employee):
    # initalize the production worker class with new values.
    def __init__(self, name, e_number, shift_num, hourly_pay):
        # this is a constructor for the ProductionWorker subclass of the Employee class
        # Employee is passed as a parameter to the Production worker so you are able to do this.
        Employee.__init__(self, name, e_number)
        # initiate shift num and hourly pay attributes for the subclass
        self.shift_num = shift_num
        self.hourly_pay = hourly_pay

    # methods for setting the shit num and hourly pay
    def set_shift_num(self, shift_num):
        self.shift_num = shift_num

    def set_hourly_pay(self, hourly_pay):
        self.hourly_pay = hourly_pay

    # get the shift num and hourly pay
    def get_shift_num(self):
        return self.shift_num

    def get_hourly_pay(self):
        return self.hourly_pay

    # method for displaying the information
    def display_info(self):
        # here we create an info variable to store the individual lines of the display info method
        info = "-" * 20 + "\n"
        info += "Employee Information:\n"
        info += f"Name: {self.get_name()}\n"
        info += f"Employee Number: {self.get_e_number()}\n"
        info += f"Shift Time: {self.get_shift_num()}\n"
        info += f"Hourly Pay: ${self.get_hourly_pay()}\n"
        # return the info variable with all of the retrieved information
        return info


def main():
    try:
        name = input("Input name: ")
        e_number = input("Input employee number: ")
        # create a shift choice variable
        shift_num_choice = input("Input shift number (1 or 2): ")
        # check the input of the choice
        if shift_num_choice == "1":
            # set shift num value to "day or night"
            shift_num = "Day"
        elif shift_num_choice == "2":
            shift_num = "Night"
        else:
            # return user if they enter an invalid input.
            print("Invalid entry.")
            return
        # continue on and get the next value
        hourly_pay = input("Input hourly pay: ")
        # create the employee object
        employee = ProductionWorker(name, e_number, shift_num, hourly_pay)
        # create a variable that will return the info entered int the subclass
        display = employee.display_info()
        # display it
        print(display)
    # catch errors
    except Exception as e:
        print(f"Error at {e}")


# call the main function.
if __name__ == "__main__":
    main()
