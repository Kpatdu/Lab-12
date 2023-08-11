
class Account:
    """"

    """
    def __init__(self):
        """

        """
        self.__account_name = 0
        self.__account_balance = 0

    def deposit(self, amount):
        tf = False
        if amount > 0:
            tf = True
            self.__account_balance += amount
        return tf

    def withdraw(self, amount):
        tf = False
        if 0 < amount < self.__account_balance:
            tf = True
            self.__account_balance -= amount
        return tf

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
