class Employee:
    def work(self):
        print("Employee works")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Tester(Employee):
    def work(self):
        print("Tester tests software")


class Designer(Employee):
    def work(self):
        print("Designer designs UI")


Developer().work()
Tester().work()
Designer().work()