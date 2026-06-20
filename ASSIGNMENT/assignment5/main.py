import calculator
import employee
import area
import math
import random

print("Addition =", calculator.add(10, 5))
print("Subtraction =", calculator.subtract(10, 5))
print("Multiplication =", calculator.multiply(10, 5))
print("Division =", calculator.divide(10, 5))

employee.display_employee()

print("Square Root =", math.sqrt(144))
print("Pi =", math.pi)
print("Factorial =", math.factorial(6))

languages = ["Python", "Java", "React", "Django"]

print("Random Number =", random.randint(1, 100))
print("Random Choice =", random.choice(languages))

print("Circle Area =", area.area_circle(5))
print("Rectangle Area =", area.area_rectangle(10, 4))