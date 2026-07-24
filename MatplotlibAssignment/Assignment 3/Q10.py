import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))

for i in range(1,5):
    plt.subplot(2,2,i)
    plt.plot([1,2,3],[2,4,6])

plt.tight_layout()
plt.show()
