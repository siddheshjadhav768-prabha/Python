import matplotlib.pyplot as plt

salary = [25000,30000,32000,35000,40000,45000,38000,42000]

plt.hist(salary,
         bins=6,
         color="orange")

plt.grid(True)

plt.title("Employee Salary")
plt.show()
