import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]

plt.figure(figsize=(10,8))

plt.subplot(3,2,1)
plt.plot(x,y)

plt.subplot(3,2,2)
plt.bar(x,y)

plt.subplot(3,2,3)
plt.scatter(x,y)

plt.subplot(3,2,4)
plt.hist(y)

plt.subplot(3,2,5)
plt.pie(y)

plt.subplot(3,2,6)
plt.barh(x,y)

plt.tight_layout()
plt.show()
