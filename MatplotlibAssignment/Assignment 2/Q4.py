import matplotlib.pyplot as plt

products = ["Laptop","Mobile","Tablet","Watch"]
sales = [60,90,45,70]

colors = ["red","blue","green","orange"]

plt.bar(products, sales, color=colors)

plt.title("Product Sales")
plt.show()
