
class Account:
    """"
    A class representing the details for an Account subject
    """
    def __init__(self, name: str):
        """
        Method to set default values and parameters of Account objects
        """
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float):
        """
        Increments the account balance by a specified amount if Boolean value returns True, otherwise,
        the function does not increment and returns False.
        """
        tf = False
        try:
            if amount > 0:
                tf = True
                self.__account_balance += amount
        except TypeError:
            tf = False
        finally:
            return tf

    def withdraw(self, amount: float):
        """
        Decrements the account balance by a specified amount if Boolean value returns True, otherwise,
        the function does not decrement returns False.
        """
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
        """
        Returns the account balance.
        """
        return self.__account_balance

    def get_name(self):
        """
        Returns the account name.
        """
        return self.__account_name
