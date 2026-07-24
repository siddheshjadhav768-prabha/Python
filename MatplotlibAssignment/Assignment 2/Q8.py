import matplotlib.pyplot as plt

products = ["Laptop","Mobile","Tablet","Watch"]
sales = [40,30,20,10]

colors = ["red","blue","green","orange"]

plt.pie(sales,
        labels=products,
        colors=colors,
        startangle=90)

plt.title("Product Sales")
plt.show()
