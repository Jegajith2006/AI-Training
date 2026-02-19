class Delivery:
    def dispatch(self):
        pass

class AirDelivery(Delivery):
    def dispatch(self):
        print("Air Delivery Dispatched")

d = AirDelivery()
d.dispatch()
