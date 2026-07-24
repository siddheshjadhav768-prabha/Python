import matplotlib.pyplot as plt

dept = ["HR","Sales","IT","Finance"]
employees = [20,35,30,15]

colors = ["red","blue","green","orange"]

plt.pie(employees,
        labels=dept,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90)

plt.title("Department Employees")
plt.show()
