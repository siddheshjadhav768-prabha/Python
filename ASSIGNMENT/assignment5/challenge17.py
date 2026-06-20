class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print(self.name)
        print(self.color)

a1 = Animal("Tiger", "Orange")

a1.show()