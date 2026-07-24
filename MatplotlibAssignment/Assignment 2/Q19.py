import matplotlib.pyplot as plt

quantity = [10,20,30,40,50]
sales = [1000,2000,3500,4500,6000]

plt.scatter(quantity, sales,
            color="purple",
            marker="*")

plt.grid(True)

plt.title("Quantity vs Sales")
plt.show()
