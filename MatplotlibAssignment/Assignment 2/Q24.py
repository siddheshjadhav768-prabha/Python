import matplotlib.pyplot as plt

products = ["Laptop","Mobile","Tablet","Watch"]
sales = [60,90,40,50]

explode = [0,0.1,0,0]

plt.pie(sales,
        labels=products,
        autopct="%1.1f%%",
        shadow=True,
        explode=explode,
        startangle=90)

plt.title("Product Sales")

plt.show()
