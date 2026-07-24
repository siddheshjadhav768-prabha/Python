import matplotlib.pyplot as plt

marks=[70,75,80,90]

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(marks)
plt.title("Line")

plt.subplot(2,2,2)
plt.bar(range(4),marks)
plt.title("Bar")

plt.subplot(2,2,3)
plt.pie(marks,autopct="%1.1f%%")
plt.title("Pie")

plt.subplot(2,2,4)
plt.hist(marks)
plt.title("Histogram")

plt.tight_layout()
plt.show()
