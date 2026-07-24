import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

# 1. Bar Chart
plt.subplot(2,2,1)
products = ["Laptop","Mobile","Tablet","Watch"]
sales = [60,90,40,70]
plt.bar(products, sales, color="green")
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True)

# 2. Pie Chart
plt.subplot(2,2,2)
methods = ["Cash","UPI","Card","Net Banking"]
values = [30,40,20,10]
plt.pie(values,
        labels=methods,
        autopct="%1.1f%%")
plt.title("Payment Methods")

# 3. Histogram
plt.subplot(2,2,3)
marks = [50,60,65,70,75,80,85,90,95]
plt.hist(marks,
         bins=5,
         color="purple",
         edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)

# 4. Scatter Plot
plt.subplot(2,2,4)
hours = [1,2,3,4,5]
marks = [50,60,70,80,90]
plt.scatter(hours,
            marks,
            color="red")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

plt.suptitle("Sales Analysis Dashboard")

plt.tight_layout()

plt.show()
