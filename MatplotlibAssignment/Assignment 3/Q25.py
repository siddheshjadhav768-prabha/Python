import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv("sales.csv")

plt.figure(figsize=(15,10))

# Monthly Sales
plt.subplot(3,2,1)
plt.plot(df["Month"], df["Sales"])
plt.title("Monthly Sales")

# Product Sales
plt.subplot(3,2,2)
plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales")

# Payment Methods
plt.subplot(3,2,3)
payment = df.groupby("Payment")["Sales"].sum()
plt.pie(payment, labels=payment.index, autopct="%1.1f%%")
plt.title("Payment Method Distribution")

# Customer Ratings
plt.subplot(3,2,4)
plt.hist(df["Rating"])
plt.title("Customer Rating Distribution")

# Quantity vs Total Amount
plt.subplot(3,2,5)
plt.scatter(df["Quantity"], df["Sales"])
plt.title("Quantity vs Total Amount")

plt.suptitle("Supermarket Sales Dashboard")
plt.tight_layout()

plt.savefig("sales_dashboard.png", dpi=300)

plt.show()
