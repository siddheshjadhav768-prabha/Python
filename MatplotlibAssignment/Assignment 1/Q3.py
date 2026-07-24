import matplotlib.pyplot as plt

employees = ["E1", "E2", "E3", "E4", "E5"]
salary = [25000, 32000, 40000, 38000, 45000]

plt.plot(employees, salary, color="blue", marker="o")

plt.grid(True)

plt.title("Employee Salary")
plt.xlabel("Employees")
plt.ylabel("Salary")

plt.show()
