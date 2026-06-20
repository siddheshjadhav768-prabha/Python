class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5


class Rectangle(Shape):
    def area(self):
        return 4 * 6


class Triangle(Shape):
    def area(self):
        return 0.5 * 4 * 6


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    print("Area:", shape.area())