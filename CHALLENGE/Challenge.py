print("Challenge 1:- Student management System")
class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    school_name="ABC College"
    def display(self):
        print("Name:-",self.name)
        print("age:-",self.age)
        print("course:-",self.course)
        print("School:-",Student.school_name)
    @classmethod
    def change_school_name(cls,new_name):
        cls.school_name=new_name
s1=Student("Sidd",18,"AIMl")
s1.display()
print("After changing School name:=")
s1.change_school_name("Zeal college")
s1.display()

print("Chanenge 2:- Employee Counter")
class Employee:
    employee_count=0
    def __init__(self,emp_id,emp_name,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.salary=salary
        Employee.employee_count +=1
    def display(self):
        print("Employee ID:-",self.emp_id)
        print("Employee Name:-",self,self.emp_name)
        print("Salary:-",self.salary)
    @classmethod
    def total_employee(cls):
        print("Total Employees:-",Employee.employee_count)
e1=Employee(1,"Sidd",15000)
e2=Employee(2,"Raju",18000)
e3=Employee(3,"Amit",20000)
e1.display()
e2.display()
e3.display()
Employee.total_employee()

print("Challenge 3:-Bank Account System")
class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    bank_name="State Bank Of India"
    def display(self):
        print("Account Number:-",self.account_number)
        print("Holder Name:-",self.holder_name)
        print("Balance:-",self.balance)
        print("Bank Name:-",BankAccount.bank_name)
    def depoist(self,amount):
        self.balance += amount
        print(amount,"Depoisted Successfully")
    def withdraw(self,amount):
        self.balance -= amount
        print(amount,"Withdraw successfully")
    def check_balance(self):
        print("Balance:-",self.balance)
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
b1=BankAccount(1,"Sidd",15000)
b1.display()
b1.depoist(5000)
b1.withdraw(8000)
b1.check_balance()
BankAccount.change_bank_name("Axis Bank")
b2=BankAccount(2,"Raju",20000)
b2.display()
b2.depoist(7000)
b2.withdraw(13000)
b2.check_balance()

print("Challenge 4:- Mobile Store Inventory")
class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    discount_percentage=10
    def display(self):
        print("Brand:-",self.brand)
        print("Model:-",self.model)
        print("Price:-",self.price)
    def calculate_discount_price(self):
        discount=(self.price*Mobile.discount_percentage)/100
        print("Price After Discount:-",self.price-discount)
    @classmethod
    def change_discount_percentage(cls,new_percentage):
        cls.discount_percentage=new_percentage
m1=Mobile("Apple","16 PRO",150000)
m1.display()
m1.calculate_discount_price()
Mobile.change_discount_percentage(20)
m2=Mobile("Samsung","S25",150000)
m2.display()
m2.calculate_discount_price()

print("Challenge 5:-Library Book Management")
class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
    library_name="City Library"
    def display(self):
        print("Book ID:-",self.book_id)
        print("Title:-",self.title)
        print("author:-",self.author)
        print("Library Name:-",Book.library_name)
    @classmethod
    def change_library_name(cls,new_name):
        cls.library_name=new_name
book1=Book(1,"Basic Python","Author A")
book2=Book(2,"Basic AIML","Author B")
book3=Book(3,"Advanced AIML","Author C")
book1.display()
book2.display()
book3.display()
Book.change_library_name("Private Library")
print("\nAfter Changing Library Name:-")
