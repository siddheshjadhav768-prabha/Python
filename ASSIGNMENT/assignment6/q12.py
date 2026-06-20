class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class Lion(Animal):
    def make_sound(self):
        print("Roar")


animals = [Dog(), Cat(), Lion()]

for animal in animals:
    animal.make_sound()