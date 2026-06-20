class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

c1 = Course("Python", "3 Months", 15000)

print(c1.course_name)
print(c1.duration)
print(c1.fees)