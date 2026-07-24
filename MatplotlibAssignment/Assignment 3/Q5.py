import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
sales = [20,30,25,40]
products = ["A","B","C","D"]
payment = [40,30,20,10]
ratings = [3,4,5,4,5,3,4,5]

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(months,sales)
plt.title("Monthly Sales")

plt.subplot(2,2,2)
plt.bar(products,sales)
plt.title("Product Sales")

plt.subplot(2,2,3)
plt.pie(payment,labels=["Cash","UPI","Card","NB"],autopct="%1.1f%%")
plt.title("Payment")

plt.subplot(2,2,4)
plt.hist(ratings)
plt.title("Ratings")

plt.tight_layout()
plt.show()
