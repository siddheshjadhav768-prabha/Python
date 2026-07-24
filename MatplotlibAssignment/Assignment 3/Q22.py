import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%")

plt.subplot(1,2,2)
plt.hist(df["Sales"])

plt.tight_layout()
plt.show()
