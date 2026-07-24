import matplotlib.pyplot as plt

marks = [55,60,65,70,75,80,85,90,95]

plt.hist(marks,
         bins=5,
         color="purple",
         edgecolor="black")

plt.title("Student Marks Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.grid(True)

plt.show()
