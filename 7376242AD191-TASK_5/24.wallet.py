class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Payment Done")
        else:
            print("Insufficient Balance")

w = Wallet(float(input()))
w.pay(float(input()))
