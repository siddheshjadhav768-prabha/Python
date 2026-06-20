class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

p1 = Product(1, "Laptop", 70000)
p2 = Product(2, "Mouse", 1000)

print(p1.id, p1.name, p1.price)
print(p2.id, p2.name, p2.price)