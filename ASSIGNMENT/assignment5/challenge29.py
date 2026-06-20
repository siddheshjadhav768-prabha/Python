class Student:
    def __init__(self, marks):
        self.marks = marks

    def calculate_percentage(self):
        per = (self.marks / 500) * 100
        print("Percentage =", per)

s1 = Student(450)

s1.calculate_percentage()