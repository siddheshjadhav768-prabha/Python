import matplotlib.pyplot as plt

subjects = ["Sub1", "Sub2", "Sub3", "Sub4", "Sub5"]

student_A = [75, 80, 78, 90, 88]
student_B = [70, 85, 80, 86, 92]

plt.plot(subjects, student_A,
         color="blue",
         marker="o",
         label="Student A")

plt.plot(subjects, student_B,
         color="red",
         marker="s",
         label="Student B")

plt.title("Student Marks Comparison")

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.legend()
plt.grid(True)

plt.show()
