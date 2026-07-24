import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
marks = [50,60,70,80,90]

plt.scatter(hours, marks,
            color="red",
            marker="o",
            s=100)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
