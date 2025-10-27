# 2. Bank Account System •
# Base class: Account (account number, balance) • 
# o Derived class: SavingsAccount  Add method withdraw(amount) 
#  Raise a custom exception InsufficientBalanceError if withdrawal exceeds balance.
# o Also include a deposit() method and test with valid/invalid cases.

class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print("Deposited:", amount)

class SavingsAccount(Account):
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientBalanceError("Not enough balance!")
            self.balance -= amount
            print("Withdrawn:", amount)
        except InsufficientBalanceError as e:
            print("Error:", e)

# Test
s1 = SavingsAccount(1234, 1000)
s1.deposit(500)
s1.withdraw(200)
s1.withdraw(2000)  # Error
