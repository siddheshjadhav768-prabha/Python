import matplotlib.pyplot as plt

ratings = [2,3,4,5,5,4,3,2,1,5,4,4,5,3,2,5]

plt.hist(ratings,
         bins=8,
         color="blue",
         edgecolor="black")

plt.title("Customer Ratings")
plt.show()
