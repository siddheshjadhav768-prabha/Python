class Vehicle:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def show(self):
        print(self.company)
        print(self.model)

v1 = Vehicle("Honda", "City")

v1.show()