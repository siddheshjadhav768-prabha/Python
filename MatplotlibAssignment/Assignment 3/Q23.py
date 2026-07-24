import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(df["Month"],df["Sales"])
plt.grid(True)

plt.subplot(2,2,2)
plt.bar(df["Month"],df["Sales"])
plt.grid(True)

plt.subplot(2,2,3)
plt.scatter(df["Quantity"],df["Sales"])
plt.grid(True)

plt.subplot(2,2,4)
plt.pie(df["Sales"],labels=df["Month"],autopct="%1.1f%%")

plt.suptitle("Dashboard")
plt.tight_layout()
plt.show()
