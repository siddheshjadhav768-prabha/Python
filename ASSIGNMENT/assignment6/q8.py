class Shape:
    pass


class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r


class Rectangle(Shape):
    def area(self, l, b):
        return l * b


class Square(Shape):
    def area(self, side):
        return side * side


print("Circle Area:", Circle().area(5))
print("Rectangle Area:", Rectangle().area(4, 6))
print("Square Area:", Square().area(4))