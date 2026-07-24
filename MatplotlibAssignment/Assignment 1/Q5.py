import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 31, 35, 36, 34, 33]

plt.plot(days, temperature,
         color="red",
         marker="*")

plt.title("Weekly Temperature")

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.show()
