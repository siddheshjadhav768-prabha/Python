print("ASSIGNMENT 1 ")
print("Q.1 answer")
print("name:- Siddhesh Jadhav")
print("college:- Zeal polytechnic college ")
print("favorite language:- python")

print("Q.2 answer")
str=input("Enter your name:")
age=int(input("enter your age:"))
print("Hello",str,",you are",age,"years old")

print("Q.3 answer")
stud_name="siddhesh jadhav"
roll_no=18
percentage=82.80
passed="Yes"
print("Name:-",stud_name,
    "\nRoll number:-",roll_no,
    "\nPercentage:-",percentage,
    "\npassed:-",passed)

#Q.4 answer
#1name -> name1
#student-name -> student_name
#class -> class_name
#total marks -> total_marks
#user_name -> correct already

print("Q.5 answer")
a=18
b=12.4
c="hello"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("Q.6 answer")
num1=int(input("Enter your first number:-"))
num2=int(input("Enter your second number:-"))
print("addition of 2 number is",num1+num2)

print("Q.7 answer")
number=float(input("Enter your number:-"))
print("Integer number is",int(number))
print("String  number is",str(number))

print("Q.8 answer")
age=input("Enter your age:-")
print("Type is",type(age))

print("Q.9,10 answer")
num1=float(input("Enter your first number:-"))
num2=float(input("Enter your second number:-"))
print("Q.9")
print("Addition:",num1+num2)
print("Substraction:",num1-num2)
print("Multiplication:",num1*num2)
print("Division:",num1/num2)
print("modulas:",num1%num2)
print("Q.10")
print(num1>num2)
print(num1<num2)
print(num1==num2)
print(num1!=num2)

print("Q.11 answer")
username=input("Enter Username:- ")
password=input("Enter password:- ")
if username=="admin" and password=="1234":
    print("login success")
else:
    print("login failure")

print("Q.12 answer")
n=float(input("Enter your number:-"))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("Entered number is 0")

print("Q.13 answer")
marks=float(input("Enter your marks:-"))
if marks>=90:
    print("a grade")
elif marks>=75:
    print("B grade")
elif marks>=50:
    print("C grade")
else:
    print("fail")

print("Q.14 answer")
n=int(input("Enter your number:-"))
if n%2==0:
    print("Even")
else:
    print("Odd")

print("Q.15")
age=int(input("Enter your age:-"))
if age<10:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior Citizen")

print("Q.16 answer")
number1=float(input("Enter your first number:-"))
number2=float(input("Enter your second number:-"))
op=input("Choose operation(+,-,*,/):- ")
if op=="+":
    print("addition",number1+number2)
elif op=="-":
    print("subtraction",number1-number2)
elif op=="*":
    print("multiplication",number1*number2)
else:
    print("Division",number1/number2)

print("Q.17 answer")
for i in range(1,21):
    print(i)

print("Q.18 answer")
for i in range(1,50):
    if i%2==0:
        print(i)

print("Q.19 answer")
num=int(input("Enter your number:-"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

print("Q.20 answer")
i=10
while(i>0):
    print(i)
    i-=1

print("Q.21 answer")
s=0
for i in range(1,101):
    s= s+i
print("sum of numbers from 1 to 100 is",s)

print("Q.22 answer")
num=int(input("enter a number:-"))
digit_count=0
while num>0:
    num=num//10
    digit_count+=1
print("the number of digits is:-",digit_count)

print("Q.23 answer")
for i in range(1,21):
    if i==15:
        break
    print(i)

print("Q.24 answer")
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

print("Q.25 answer")
correct_password="Sidd786"
while True:
    password=input("Enter the password:-")
    if password==correct_password:
        print("Access granted")
        break
    else:
        print("Fail, try again! ")

print("Q.26 answer")
for i in range(1,6):
    print("*"*i)

print("Q.27 answer")
for i in range(1,6):
    print("Multiplication Table of",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

print("Q.28 answer")
for i in range(1,5):
    for j in range(4):
        print(i,end="")
    print()

print("Q.29 answer")
list1=["sidd","raju","krish","bala","ramu"]
print(list1)
print("first name:-",list1[0])
print("last name:-",list1[4])
print("total students names is",len(list1))

print("Q.30,31,32 answer")
print("Q.30")
numbers=[]
for i in range(1,6):
    num=float(input("enter your number:-"))
    numbers.append(num)
print(numbers)
print("Q.31")
numbers.append(6)
print("after appending 6 number:-")
print(numbers)
numbers.remove(6)
print("after removing 6 number:-")
print(numbers)
numbers.pop()
print("after poping list:-")
print(numbers)
numbers.sort()
print("after sorting list:-")
print(numbers)
print("Q.32")
for i in numbers:
    print(i)

print("Q.33,34 answer")
print("Q.33")
list2=[1,2,3,4,5,6,7,8,9,10]
print(list2)
print("maximum value from list2:-",max(list2))
print("minimum value from list2:-",min(list2))
print("sum of all element from list2:-",sum(list2))
print("Q.34")
print("First 5 numbers:-",list2[0:5])
print("last 3 numbers:-",list2[7:10])
print("Alternate elements using slicing",list2[3:8])

print("Q.35 answer")
person = ("sidd", 18, "Pune")
print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])

#print("Q.36 answer")
#t=(1,2,3)
#t[0]=5  (Error happens because tuple is immutable)

print("Q.37 answer")
t1=(10,20,30,40,50)
print(t1)
print("Maximum value:-",max(t1))
print("Minimum value:-",min(t1))
print("Sum of all elements of tuple:-",sum(t1))

print("Q.38 answer")
student=("Siddhesh",18,"Pune")
name,age,city=student
print(name,age,city)

print("Q.39 answer")
balance=10000
while True:
    print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    choice=int(input("Enter Your Choice(1,2,3,4):-"))
    if choice==1:
        print("Balance:-",balance)
    elif choice==2:
        amount=int(input("Deposit amount:-"))
        balance+=amount
        print("Deposit Successfully")
    elif choice==3:
        amount=int(input("Withdraw amount:-"))
        if amount<=balance:
            balance-=amount
            print("Withdrawal Successfully")
        else:
            print("Insufficient Balance")
    elif choice==4:
        break
    else:
        print("Invalid Choice, Try again!!")

print("Q.40 answer")
marks=[int(input("enter marks:-"))for i in range(5)]
print("Enter Your 5 Subject Marks:-",marks)
avg=sum(marks)/len(marks)
print("Average marks:-",avg)
if avg>=90:
    print("Grade A")
elif avg>=75:
    print("Grade B")
elif avg>=50:
    print("Grade C")
else:
    print("Fail")
print("Highest Marks:-",max(marks))
