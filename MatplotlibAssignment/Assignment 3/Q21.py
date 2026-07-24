import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.plot(df["Month"], df["Sales"])
plt.title("Line")

plt.subplot(1,2,2)
plt.bar(df["Month"], df["Sales"])
plt.title("Bar")

plt.tight_layout()
plt.show()
