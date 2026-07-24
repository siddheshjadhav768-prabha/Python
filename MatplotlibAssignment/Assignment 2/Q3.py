import matplotlib.pyplot as plt

students = ["S1","S2","S3","S4","S5","S6"]
marks = [70,75,80,65,90,85]

plt.bar(students, marks, color="green", edgecolor="black")

plt.grid(True)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
