import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [150, 180, 170, 200, 230, 210, 250]

plt.figure(figsize=(10,5))

plt.plot(days, visitors,
         color="black",
         marker="+",
         label="Visitors")

plt.title("Website Visitors")

plt.xlabel("Days")
plt.ylabel("Visitors")

plt.legend()
plt.grid(True)

plt.show()
