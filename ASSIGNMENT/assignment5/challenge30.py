class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance =", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Balance =", self.balance)

b1 = BankAccount(10000)

b1.deposit(5000)
b1.withdraw(2000)