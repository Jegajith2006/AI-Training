class Payment:
    def pay(self):
        pass

class Card(Payment):
    def pay(self):
        print("Paid using Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

p = Card()
p.pay()
