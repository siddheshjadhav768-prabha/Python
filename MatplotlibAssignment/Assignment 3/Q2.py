import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.figure(figsize=(8,8))

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Line")

plt.subplot(2,2,2)
plt.bar(x,y)
plt.title("Bar")

plt.subplot(2,2,3)
plt.pie(y, labels=["A","B","C","D"], autopct="%1.1f%%")
plt.title("Pie")

plt.subplot(2,2,4)
plt.scatter(x,y)
plt.title("Scatter")

plt.tight_layout()
plt.show()
