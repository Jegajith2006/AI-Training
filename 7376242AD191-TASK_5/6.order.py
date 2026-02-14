class Order:
    def __init__(self, id, name, amt):
        self.id = id
        self.name = name
        self.amt = amt

    def pay(self, mode):
        print("Paid using", mode)

o = Order(input(), input(), float(input()))
o.pay(input())
