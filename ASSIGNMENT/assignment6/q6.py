class BankAccount:
    def __init__(self, balance):
        self.balance = balance


class SavingsAccount(BankAccount):
    pass


class CurrentAccount(BankAccount):
    pass


class FixedDepositAccount(BankAccount):
    pass


savings = SavingsAccount(10000)
current = CurrentAccount(20000)
fd = FixedDepositAccount(50000)

print("Savings Balance:", savings.balance)
print("Current Balance:", current.balance)
print("FD Balance:", fd.balance)