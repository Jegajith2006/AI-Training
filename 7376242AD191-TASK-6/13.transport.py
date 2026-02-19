class Vehicle:
    def start(self):
        pass

class Bus(Vehicle):
    def start(self):
        print("Bus Engine Started")

class Train(Vehicle):
    def start(self):
        print("Train Engine Started")

v = Bus()
v.start()
