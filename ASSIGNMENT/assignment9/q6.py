file = open("students.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()

file = open("students.txt", "r")
print(file.read())
file.close()