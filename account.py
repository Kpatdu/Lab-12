
class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        tf = False
        try:
            if amount > 0:
                tf = True
                self.__account_balance += amount
        except TypeError:
            tf = False
        finally:
            return tf

    def withdraw(self, amount):
        tf = False
        try:
            if 0 < amount < self.__account_balance:
                tf = True
                self.__account_balance -= amount
        except TypeError:
            tf = False
        finally:
            return tf

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
