class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def display_info():
        pass


def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")
    User.set_username(username)
    User.set_password(password)


def inital_menu():
    print(
        """
1. Continue 
2. Register
3. Login           
          
          """
    )


def main():
    print("Welcome to LFPWM")
    print("=" * 25)

    while True:
        try:
            pass

        except Exception as e:
            print(f"Error at {e}")
