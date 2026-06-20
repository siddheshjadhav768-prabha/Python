class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print("Area =", area)

c1 = Circle(5)

c1.calculate_area()