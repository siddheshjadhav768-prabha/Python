import matplotlib.pyplot as plt

subjects = ["English", "Math", "Science", "Computer", "History"]
marks = [72, 80, 76, 90, 95]

plt.plot(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
