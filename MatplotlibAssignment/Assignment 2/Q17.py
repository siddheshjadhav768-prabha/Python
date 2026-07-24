import matplotlib.pyplot as plt

height = [150,155,160,165,170]
weight = [45,50,55,60,65]

plt.scatter(height, weight,
            color="blue",
            marker="D")

plt.grid(True)

plt.title("Height vs Weight")
plt.show()
