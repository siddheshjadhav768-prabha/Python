import matplotlib.pyplot as plt

plt.style.use("dark_background")

plt.pie([30,40,20,10],
labels=["A","B","C","D"],
autopct="%1.1f%%")

plt.show()
