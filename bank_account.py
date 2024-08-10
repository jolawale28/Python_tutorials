# Description: Define a class BankAccount with attributes account_number and balance.
# Include methods deposit(amount) and withdraw(amount) to update the balance.
# Task: Create an instance of the BankAccount class, perform some deposits and
# withdrawals, and display the final balance.

class BankAccount:

    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

vicky = BankAccount("026789167")

vicky.deposit(10_000_000)
vicky.withdraw(2_000_000)

print(f"Account Number: {vicky.account_number}, Balance: {vicky.balance}")