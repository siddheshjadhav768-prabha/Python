class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

p1 = Person("Suraj", 18)

p1.show()