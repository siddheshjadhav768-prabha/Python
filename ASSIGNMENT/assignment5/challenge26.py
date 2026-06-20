class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area =", area)

r1 = Rectangle(10, 5)

r1.calculate_area()