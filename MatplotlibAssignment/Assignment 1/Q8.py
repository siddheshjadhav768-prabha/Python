import matplotlib.pyplot as plt

products = ["P1", "P2", "P3", "P4", "P5"]
sales = [120, 180, 160, 220, 250]

plt.plot(products, sales,
         color="orange",
         linestyle=":",
         marker="o")

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.grid(True)

plt.show()
