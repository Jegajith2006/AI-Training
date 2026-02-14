class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def bill(self):
        print(self.price)

f = Food(input(), float(input()))
f.bill()
