import matplotlib.pyplot as plt

salary=[25000,30000,35000,40000]
exp=[1,2,3,4]

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(salary)

plt.subplot(2,2,2)
plt.bar(["HR","IT","Sales"],[20,30,25])

plt.subplot(2,2,3)
plt.hist(salary)

plt.subplot(2,2,4)
plt.scatter(exp,salary)

plt.tight_layout()

plt.savefig("employee_dashboard.png", dpi=300)

plt.show()
