import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch"]
sales = [50, 80, 40, 60]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()
