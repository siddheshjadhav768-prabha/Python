class Animal:
    pass


class Dog(Animal):
    def sound(self):
        print("Dog: Bark")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


Dog().sound()
Cat().sound()
Cow().sound()