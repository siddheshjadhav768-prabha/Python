import matplotlib.pyplot as plt

marks = [55,60,62,65,68,70,72,75,78,80,82,85,88,90,95]

plt.hist(marks,
         bins=5,
         color="green",
         edgecolor="black")

plt.title("Student Marks Histogram")
plt.show()
