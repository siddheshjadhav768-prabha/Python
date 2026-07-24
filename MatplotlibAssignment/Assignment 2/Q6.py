import matplotlib.pyplot as plt

methods = ["Cash","UPI","Card","Net Banking"]
values = [30,40,20,10]

plt.pie(values, labels=methods)

plt.title("Payment Methods")
plt.show()
