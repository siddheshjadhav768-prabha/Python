class College:
    def __init__(self, name, city, students):
        self.name = name
        self.city = city
        self.students = students

c1 = College("XYZ College", "Mumbai", 5000)

print(c1.name)
print(c1.city)
print(c1.students)