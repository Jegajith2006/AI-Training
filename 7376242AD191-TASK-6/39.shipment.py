class Shipment:
    def delivery_time(self):
        pass

class Air(Shipment):
    def delivery_time(self):
        print("2 Days")

s = Air()
s.delivery_time()
