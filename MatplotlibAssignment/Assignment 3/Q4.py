import matplotlib.pyplot as plt

salary = [25000,30000,35000,40000,45000]
exp = [1,2,3,4,5]
dept = ["HR","IT","Sales","Finance"]
emp = [20,30,25,15]

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(salary)
plt.title("Salary Trend")

plt.subplot(2,2,2)
plt.bar(dept, emp)
plt.title("Department Employees")

plt.subplot(2,2,3)
plt.hist(salary)
plt.title("Salary Distribution")

plt.subplot(2,2,4)
plt.scatter(exp, salary)
plt.title("Experience vs Salary")

plt.tight_layout()
plt.show()
