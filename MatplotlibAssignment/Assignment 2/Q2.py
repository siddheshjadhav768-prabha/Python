import matplotlib.pyplot as plt

employees = ["A", "B", "C", "D", "E"]
salary = [25000, 30000, 28000, 35000, 32000]

plt.barh(employees, salary)

plt.title("Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Employees")

plt.show()
