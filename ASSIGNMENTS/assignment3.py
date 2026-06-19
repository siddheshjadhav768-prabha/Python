"""print("Q.1 Answer")
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:-",self.name)
        print("Age:-",self.age)
s1=Student("Sidd",18)
s1.display()
s2=Student("raju",19)
s2.display()
s3=Student("amit",20)
s3.display()

print("Q.2 Answer")
class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee ID:-",self.emp_id)
        print("Name:-",self.name)
        print("Salary:-",self.salary)
e1=Employee(1,"Siddhesh",20000)
e2=Employee(2,"Ramesh",18000)
e1.display()
e2.display()

print("Q.3 Answer")
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("Brand:-",self.brand)
        print("Model:-",self.model)
c1=Car("TATA","Swfit")
c1.display()

print("Q.4 Answer")
class Bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def check_balance(self):
        print("Balance:-",self.balance)
b1=Bankaccount(5000)
b1.deposit(5000)
b1.check_balance()
b1.withdraw(5000)
b1.check_balance()

print("Q.5 Answer")
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title:-",self.title)
        print("Author:-",self.author)
book1=Book("Gen AI","XYZ author")
book1.display()

print("Q.6 Answer")
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:-",self.brand)
        print("Price:-",self.price)
m1=Mobile("Apple",150000)
m1.display

print("Q.7 Answer")
class Company:
    def __init__(self,emp_name):
        self.emp_name=emp_name
    company_name="Prabha Technology"
    def display(self):
        print("Employee:-",self.emp_name)
        print("Company:-",Company.company_name)
emp=Company("Siddhesh")
emp.display()

print("Q.8 Answer")
class Product:
    def __init__(self,price):
        self.price=price
    tax_rate=0.18
    def final_price(self):
        return self.price+self.price*Product.tax_rate
p1=Product(10000)
print("Final Price:-",p1.final_price())

print("Q.9 Answer")
class Student:
    school_name = "ABC School"
    def __init__(self, name):
        self.name = name
    @classmethod
    def update_school(cls, new_name):
        cls.school_name = new_name
    def show(self):
        print(f"{self.name} studies at {Student.school_name}")

st = Student("Siddhesh")
st.show()
Student.update_school("XYZ School")
st.show()

print("Q.10 Answer")
class Vehicle:
    vehicle_count = 0
    def __init__(self, name):
        self.name = name
        Vehicle.vehicle_count += 1
v1 = Vehicle("Car")
v2 = Vehicle("Bike")
print("Total Vehicles:", Vehicle.vehicle_count)

print("Q.11 Answer")
class Calculator:
    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def sub(a, b): return a - b
    @staticmethod
    def mul(a, b): return a * b
    @staticmethod
    def div(a, b): return a / b
print(Calculator.add(5, 3))
print(Calculator.mul(4, 2))

print("Q.12 Answer")
class TempConverter:
    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32
print("Celsius 37 =", TempConverter.c_to_f(37), "F")

print("Q.13 Answer")
class Utility:
    @staticmethod
    def check(num):
        return "Even" if num % 2 == 0 else "Odd"
print(Utility.check(11))

print("Q.14 Answer")
class Person:
    def __init__(self, name):
        self.name = name
class Student3(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name: {self.name}, Roll: {self.roll}")
s = Student3("Pranvi", 101)
s.show()

print("Q.15 Answer")
class Vehicle2:
    def __init__(self, brand):
        self.brand = brand
class Bike(Vehicle2):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc
    def show(self):
        print(f"Bike: {self.brand}, CC: {self.cc}")
b = Bike("Hero", 150)
b.show()

print("Q.16 Answer")
class Shape:
    def area(self): pass
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r
class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
print("Circle Area:", Circle(5).area())
print("Rectangle Area:", Rectangle(4, 6).area())

print("Q.17 Answer")
class Animal:
    def sound(self): pass
class Dog(Animal):
    def sound(self): print("Woof!")
class Cat(Animal):
    def sound(self): print("Meow!")
Dog().sound()
Cat().sound()

print("Q.18 Answer")
class Person2:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def get_salary(self): return self.__salary
    def set_salary(self, s): self.__salary = s
p = Person2("Ravi", 20000)
print(p.get_salary())
p.set_salary(25000)
print(p.get_salary())

print("Q.19 Answer")
class BankAccount2:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amt): self.__balance += amt
    def get_balance(self): return self.__balance
acc2 = BankAccount2()
acc2.deposit(500)
print("Balance:", acc2.get_balance())

print("Q.20 Answer")
class Employee2:
    def __init__(self, name):
        self.__name = name
    def set_name(self, new_name): self.__name = new_name
    def get_name(self): return self.__name
e = Employee2("Raj")
print(e.get_name())
e.set_name("Ravi")
print(e.get_name())
print("Q.21 Answer")
class Book2:
    def __init__(self, title): self.title = title
class Library:
    def __init__(self): self.books = []
    def add_book(self, book): self.books.append(book)
    def show_books(self):
        for b in self.books: print(b.title)
lib = Library()
lib.add_book(Book2("Python"))
lib.add_book(Book2("AI"))
lib.show_books()

print("Q.22 Answer")
class Person3:
    def __init__(self, name): self.name = name
class Patient(Person3):
    def __init__(self, name, disease):
        super().__init__(name)
        self.disease = disease
    def show(self): print(f"{self.name} has {self.disease}")
pat = Patient("Siddhesh", "Flu")
pat.show()

print("Q.23 Answer")
class School:
    school_name = "ABC School"
    def __init__(self, student):
        self.student = student
    @classmethod
    def change_school(cls, new): cls.school_name = new
    def show(self):
        print(f"{self.student} studies at {School.school_name}")
s = School("Siddhesh")
s.show()
School.change_school("XYZ School")
s.show()"""
print("Q.24 Answer")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show(self):
        print(f"Product: {self.name}, Price: {self.price}")
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
    def show(self):
        print(f"Electronics: {self.name}, Price: {self.price}, Warranty: {self.warranty} years")
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    def show(self):
        print(f"Clothing: {self.name}, Price: {self.price}, Size: {self.size}")
e1 = Electronics("Laptop", 50000, 2)
c1 = Clothing("T-Shirt", 500, "M")
e1.show()
c1.show()
print("Q.25 Answer")
class ATM:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds")
    def check_balance(self):
        print("Balance:", self.__balance)
atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)
atm.check_balance()
