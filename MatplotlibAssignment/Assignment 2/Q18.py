import matplotlib.pyplot as plt

experience = [1,2,3,4,5]
salary = [25000,30000,40000,50000,60000]

plt.scatter(experience, salary,
            color="green",
            s=150,
            alpha=0.7)

plt.title("Experience vs Salary")
plt.show()
