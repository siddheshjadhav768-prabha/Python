import matplotlib.pyplot as plt

age = [20,25,30,35,40]
income = [20000,30000,45000,55000,70000]

plt.scatter(age, income,
            color="orange",
            marker="s",
            s=120)

plt.title("Age vs Income")
plt.show()
