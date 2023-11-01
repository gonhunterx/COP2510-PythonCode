class Employee:
    def __init__(self, name, e_number):
        self.__name = name
        self.__e_number = e_number

    def set_name(self, name):
        self.__name = name

    def set_pay(self, e_number):
        self.__e_number = e_number

    def get_name(self):
        return self.__name

    def get_e_number(self):
        return self.__e_number


# child class (subclass)
class ProductionWorker(Employee):
    def __init__(self, name, e_number, shift_num, hourly_pay):
        Employee.__init__(self, name, e_number)
        self.__shift_num = shift_num
        self.__hourly_pay = hourly_pay

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_pay(self):
        return self.__hourly_pay


def main():
    name = input("Input name: ")
    e_number = input("Input employee number: ")
    shift_num = input("Input shift number: ")
    hourly_pay = input("Input hourly pay: ")

    emplpoyee = ProductionWorker(name, e_number, shift_num, hourly_pay)

    if shift_num == 1:
        shift_num = "Day"
    elif shift_num == 2:
        shift_num == "Night"
    else:
        return "Invalid input. "

    print("Employee Information:")
    print("-" * 20)
    print("Name:", emplpoyee.get_name())
    print("Employee Number:", emplpoyee.get_e_number())
    print("Shift Number:", emplpoyee.get_shift_num())
    print("Hourly Pay:", emplpoyee.get_hourly_pay())


if __name__ == "__main__":
    main()
