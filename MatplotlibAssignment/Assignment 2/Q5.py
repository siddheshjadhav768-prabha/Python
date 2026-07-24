import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
expenses = [15000,18000,16000,20000,19000,21000]

plt.figure(figsize=(8,5))

plt.bar(months, expenses, color="orange")

plt.grid(axis="y")

plt.title("Monthly Expenses")
plt.xlabel("Months")
plt.ylabel("Expenses")

plt.show()
