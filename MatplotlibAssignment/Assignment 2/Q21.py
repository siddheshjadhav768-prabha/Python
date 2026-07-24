import matplotlib.pyplot as plt

products = ["Laptop","Mobile","Tablet","Watch"]
sales = [60,90,50,70]

plt.figure(figsize=(10,5))

plt.bar(products, sales,
        color="green",
        edgecolor="black")

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.grid(axis="y")

plt.show()
