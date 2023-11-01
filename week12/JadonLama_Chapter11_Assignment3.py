class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        # __ makes the attribute private

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number


class Customer(Person):
    def __init__(self, name, address, phone_number, customer_number, mailing_list):
        # call the superclass __init__ method and pass the arguments from it
        Person.__init__(self, name, address, phone_number)
        # initalize its own attributes
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    # Mutator methods
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    # Accessor methods
    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list

    # def __str__(self):
    #     return f"Name: {self.get_name()}\nAddress: {self.get_address()}\nPhone Number: {self.get_phone_number()}\nCustomer Number: {self.get_customer_number()}\nMailing List: {self.get_mailing_list()}"


def main():
    # get customer information.
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    customer_number = input("Enter your customer number: ")
    mailing_list = input("Include in mailing list? (y/n): ")

    if mailing_list.lower() == "y":
        mailing_list = True
    else:
        mailing_list = False
    # create an instance of the Customer class
    my_customer = Customer(name, address, phone_number, customer_number, mailing_list)

    # display the data
    print("Customer Information")
    print("----------------------")
    print("Name:", my_customer.get_name())
    print("Address:", my_customer.get_address())
    print("Phone:", my_customer.get_phone_number())
    print("Customer Number:", my_customer.get_customer_number())
    print("Mailing list:", my_customer.get_mailing_list())


main()
