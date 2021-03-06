class InsufficientBalanceError(Exception):
    def __init__(self):
        self.message = "Insufficient Balance!"


class Account:
    # Class attributes
    minbal = 10000

    @staticmethod
    def set_minbal(newminbal):
        Account.minbal = newminbal

    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno  # Private member
        self.ahname = ahname
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientBalanceError()

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.acno} - {self.ahname} - {self.balance}"

    def __eq__(self, other):
        print("__eq__")
        return self.acno == other.acno

    def __gt__(self, other):
        return self.balance > other.balance


a1 = Account(1, "Mr. Bill")
Account.set_minbal(5000)
a2 = Account(2, "Mr. Mark", 50000)
try:
    a2.withdraw(100000)
    print("Withdrew amount!")
except InsufficientBalanceError as ex:
    print("Error : ", ex.message)
