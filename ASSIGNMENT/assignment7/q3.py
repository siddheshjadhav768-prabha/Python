class Shape:

    def draw(self):
        print("Drawing Shape")

class Circle(Shape):

    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):

    def draw(self):
        print("Drawing Rectangle")

c = Circle()
r = Rectangle()

c.draw()
r.draw()