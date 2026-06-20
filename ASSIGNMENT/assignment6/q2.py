class Vehicle:
    def show_vehicle(self):
        print("This is a Vehicle")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class ElectricCar(Car):
    def battery(self):
        print("Electric Battery Enabled")


class SportsElectricCar(ElectricCar):
    def speed(self):
        print("High Speed Sports Electric Car")


car = SportsElectricCar()
car.show_vehicle()
car.battery()
car.speed()