class Vehicle:
    def drive(self):
        print("Driving")

class Car(Vehicle):
    def drive(self):
        print("Car driving")

c = Car()
c.drive()
