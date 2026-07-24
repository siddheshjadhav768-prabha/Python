import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 35000, 40000, 45000, 50000]

plt.plot(months, sales,
         color="green",
         linestyle="--",
         linewidth=3)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
