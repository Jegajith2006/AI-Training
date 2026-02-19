class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Starting")

class Bike(Vehicle):
    def start(self):
        print("Bike Starting")

v = Car()
v.start()
