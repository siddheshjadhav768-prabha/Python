import matplotlib.pyplot as plt

plt.pie([40,30,20,10],labels=["Cash","UPI","Card","NB"],autopct="%1.1f%%")
plt.savefig("payment_report.pdf")
plt.show()
