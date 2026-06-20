class Employee:
    def __init__(self, salary):
        self.salary = salary

    def annual_salary(self):
        annual = self.salary * 12
        print("Annual Salary =", annual)

e1 = Employee(50000)

e1.annual_salary()