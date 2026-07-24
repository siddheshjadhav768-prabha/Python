import matplotlib.pyplot as plt

plt.style.use("ggplot")

salary=[25000,30000,35000,40000]

plt.bar(["A","B","C","D"],salary)

plt.title("Employee Salary")
plt.xlabel("Employees")
plt.ylabel("Salary")

plt.grid(True)

plt.show()
