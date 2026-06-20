class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car Started")


class Bike(Vehicle):
    def start(self):
        print("Bike Started")


class Bus(Vehicle):
    def start(self):
        print("Bus Started")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()