class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

a1 = BankAccount(1001, "Rahul", 10000)
a2 = BankAccount(1002, "Amit", 15000)

print(a1.acc_no, a1.name, a1.balance)
print(a2.acc_no, a2.name, a2.balance)