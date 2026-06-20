class Employee:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

e1 = Employee(101, "Ravi", "HR")
e2 = Employee(102, "Karan", "IT")

print(e1.id, e1.name, e1.department)
print(e2.id, e2.name, e2.department)