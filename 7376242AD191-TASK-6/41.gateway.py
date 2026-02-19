class Gateway:
    def process(self):
        pass

class PayPal(Gateway):
    def process(self):
        print("Processed via PayPal")

g = PayPal()
g.process()
