import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot([100,120,140,160])
plt.title("Revenue")

plt.subplot(2,2,2)
plt.pie([40,30,20,10],autopct="%1.1f%%")
plt.title("Employees")

plt.subplot(2,2,3)
plt.bar(["HR","IT","Sales"],[20,40,30])
plt.title("Budget")

plt.subplot(2,2,4)
plt.hist([3,4,5,4,3,5,4])
plt.title("Ratings")

plt.tight_layout()
plt.show()
