class Employee:
    def role(self):
        pass


class Developer(Employee):
    def role(self):
        print("Developer")


class Tester(Employee):
    def role(self):
        print("Tester")


class Manager(Employee):
    def role(self):
        print("Manager")


employees = [
    Developer(),
    Tester(),
    Manager()
]

for employee in employees:
    employee.role()