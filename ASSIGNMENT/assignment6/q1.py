class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_no, subject):
        Student.__init__(self, name, age, roll_no)
        self.subject = subject

    def display(self):
        print("Teaching Assistant Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Siddhesh", 22, 101, "Python")
ta.display()