class Mobile:
    company = ""
    model = ""
    storage = ""

m1 = Mobile()
m1.company = "Samsung"
m1.model = "S24"

m1.storage = "256GB"

m2 = Mobile()
m2.company = "Apple"
m2.model = "iPhone 15"
m2.storage = "128GB"

print(m1.company, m1.model, m1.storage)
print(m2.company, m2.model, m2.storage)