import matplotlib.pyplot as plt

months = ["Rent","Food","Travel","Shopping"]
expense = [40,25,20,15]

plt.pie(expense,
        labels=months,
        autopct="%1.1f%%",
        shadow=True)

plt.title("Monthly Expenses")
plt.show()
