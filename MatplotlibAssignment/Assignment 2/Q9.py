import matplotlib.pyplot as plt

cities = ["Delhi","Mumbai","Pune","Chennai"]
population = [45,35,15,20]

explode = [0.1,0,0,0]

plt.pie(population,
        labels=cities,
        explode=explode,
        autopct="%1.1f%%",
        shadow=True)

plt.title("City Population")
plt.show()
