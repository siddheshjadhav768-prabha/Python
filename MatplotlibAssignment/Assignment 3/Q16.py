import matplotlib.pyplot as plt

sales=[20,30,25,40]

for style in ["default","ggplot","dark_background"]:
    plt.style.use(style)
    plt.figure()
    plt.plot(sales)
    plt.title(style)

plt.show()
