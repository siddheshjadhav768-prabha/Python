import matplotlib.pyplot as plt

height = [150,155,160,165,170]
weight = [45,50,55,60,65]

plt.scatter(height, weight,
            marker="D",
            s=150,
            color="blue",
            alpha=0.8)

plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.grid(True)

plt.show()
