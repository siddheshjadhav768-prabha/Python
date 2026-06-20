class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

e1 = Employee(101, "Siddhesh", 50000)

print(e1.id)
print(e1.name)
print(e1.salary)