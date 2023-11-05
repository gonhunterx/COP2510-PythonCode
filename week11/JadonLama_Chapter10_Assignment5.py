# Retail item class for item creation
class Retail_item:
    # setting the constructor and its parameters
    def __init__(self, item_desc, units_in_inv, price):
        # setting the private attributes
        self.__item_desc = item_desc
        self.__units_in_inv = units_in_inv
        self.__price = price

    # Mutator methods for setting values
    def set_item_desc(self, description):
        self.__item_desc = description

    def set_units_in_inv(self, units):
        self.__units_in_inv = units

    def set_price(self, price):
        self.__price = price

    # Retrieval of the set values for the item.
    def get_item_desc(self):
        return f"{self.__item_desc},"

    def get_units_in_inv(self):
        return f"{self.__units_in_inv},"

    def get_price(self):
        return f"${self.__price}"


# hard coding some items
def base_items():
    item1 = Retail_item("Jacket", 12, 59.95)
    item2 = Retail_item("Designer Jeans", 40, 34.95)
    item3 = Retail_item("Shirt", 20, 24.95)

    return item1, item2, item3


# something like this function could possibly be used to create new items then
# append them into a list, dictionary, database, or files
# def create_new_item():
#     new_item_name = input("Name for new item: ")
#     new_item_units = input("Enter the number of units: ")
#     new_item_price = input("Enter the price of the item: ")

#     new_item = Retail_item(new_item_name, new_item_units, new_item_price)
#     return new_item


def main():
    while True:
        try:
            print("Welcome to the Retail Item Manager")
            print("==================================")
            print("The following items are currently in stock:")
            # setting values to the function that returns retail item objects
            item1, item2, item3 = base_items()
            # logic for breaking out of the loop
            choice = input("'q' to quit '1' to continue. ")
            if choice != "q":
                # printing the objects with their methods to get information
                print(
                    item1.get_item_desc(), item1.get_units_in_inv(), item1.get_price()
                )
                print(
                    item2.get_item_desc(), item2.get_units_in_inv(), item2.get_price()
                )
                print(
                    item3.get_item_desc(), item3.get_units_in_inv(), item3.get_price()
                )
                print("==================================")
            else:
                # allow the user to break out of the loop
                break
        # error handling
        except Exception as e:
            return f"Error at {e}"


# calling the main function only
if __name__ == "__main__":
    main()
