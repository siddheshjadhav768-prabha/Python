import matplotlib.pyplot as plt

temperature = [30,31,29,32,33,35,34,31,30,32,
               33,36,37,34,32,31,30,29,28,30,
               31,33,34,35,36,37,38,34,32,31]

plt.hist(temperature, bins=7)

plt.title("Daily Temperature")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

plt.grid(True)

plt.show()
