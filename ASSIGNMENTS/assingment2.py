"""print("ASSIGNMENT 2 ")
print("Q.1,3,4,5,6 answer")
print("Q.1")
student={
    "name":"Sidd",
    "age":18,
    "course":"AIML",
    "city":"Pune"
}
print(student)
print("Q.3")
student["Email"]="Sid@gmail.com"
print("After adding email:-",student)
print("Q.4")
student["city"]="Mumbai"
print("After changing city:-",student)
print("Q.5")
student.pop("Email")
print("After poping email:-",student)
del student["city"]
print(student)
print("Q.6")
print("Keys:-")
for key in student.keys():
    print(key)
print("Values:-")
for value in student.values():
    print(value)
print("In Pair:-")
for k,v in student.items():
    print(k,":",v)

print("Q.2 answer")
emp={
    "Name":"Ramu",
    "Salary":50000,
    "Department":"IT"
}
print("Name:-",emp["Name"])
print("Salary:-",emp["Salary"])
print("Department:-",emp["Department"])

print("Q.7,8,9 answer")
print("Q.7")
marks={"math":80,"science":73,"english":56,"history":48,"geography":75}
print(marks)
print("total subject:-",len(marks))
print("Q.8")
total=sum(marks.values())
print("Total Marks:-",total)
print("Q.9")
if "math" in marks:
    print("Key exists")
else:
    print("Key not exists")

print("Q.10 answer")
products={"pen":10,"water bottle":40,"bag":700,"shoes":1200}
for p,price in products.items():
    if price>500:
        print(p,price)

print("Q11,12,13 answer")
print("Q.11")
numbers = {10, 20, 30, 40, 50}
for num in numbers:
    print(num)
print("Q.12")
numbers.add(60)
numbers.add(70)
print(numbers)
print("Q13")
numbers.remove(20)
numbers.discard(30)
print(numbers)

print("Q14,15,16 answer")
print("Q.14")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Q15")
print("Common Elements:", A.intersection(B))
print("Q16")
value = 4
if value in A:
    print("Value exists")
else:
    print("Value does not exist")

print("Q17 answer")
lst = [10, 20, 20, 30, 40, 40, 50]
unique_set = set(lst)
print(unique_set)

print("Q18 answer")
students = {"Rohit", "Amit", "Priya", "Rohit", "Amit"}
print("Unique Students:", students)
print("Total Unique Students:", len(students))

print("Q19 answer")
set1 = {1, 2, 3}
set2 = {3, 2, 1}
if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")

print("Q20 answer")
temp_set = {1, 2, 3, 4}
temp_set.clear()
print(temp_set)

print("Q21 answer")
def welcome():
    print("Welcome to Python Programming")
welcome()

print("Q22 answer")
def add(a, b):
    print("Sum =", a + b)
add(10, 20)

print("Q23 answer")
def greet(name):
    print("Hello,", name)
greet("Rohit")

print("Q24 answer")
def square(num):
    return num * num
print("Square =", square(5))

print("Q25 answer")
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_odd(7)

print("Q26 answer")
def rectangle_area(length, width):
    return length * width
print("Area =", rectangle_area(10, 5))

print("Q27 answer")
def greater(a, b):
    return a if a > b else b
print("Greater =", greater(25, 15))

print("Q28 answer")
def print_numbers():
    for i in range(1, 11):
        print(i, end=" ")
    print()
print_numbers()

print("Q29 answer")
def list_sum(numbers):
    return sum(numbers)
print("Sum =", list_sum([10, 20, 30, 40]))

print("Q30 answer")
def result(marks):
    if marks >= 35:
        print("Pass")
    else:
        print("Fail")
result(50)
result(25)

print("Q31 answer")
def student(name, city="Pune"):
    print("Name:", name)
    print("City:", city)
student("Rohit")
student("Amit", "Mumbai")

print("Q32 answer")
def details(name, age):
    print("Name:", name)
    print("Age:", age)
details(age=21, name="Rohit")"""

print("Q33 answer")
def display_numbers(*args):
    print("Numbers:", args)
display_numbers(10, 20, 30, 40, 50)

print("Q34 answer")
def max_min(numbers):
    return max(numbers), min(numbers)
maximum, minimum = max_min([10, 50, 20, 80, 30])
print("Maximum =", maximum)
print("Minimum =", minimum)

print("Q35 answer")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print("Vowel Count =", count_vowels("Python Programming"))
