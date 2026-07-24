import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 28000, 40000, 45000, 50000]

plt.figure(figsize=(10,5))

plt.plot(months, sales,
         color="green",
         marker="o",
         linestyle="--",
         linewidth=3,
         label="Monthly Sales")

plt.title("Monthly Sales Report")

plt.xlabel("Months")
plt.ylabel("Sales (₹)")

plt.grid(True)
plt.legend()

plt.show()
