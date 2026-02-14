class Subscription:
    def __init__(self, user, plan):
        self.user = user
        self.plan = plan

    def bill(self):
        if self.plan == "Basic":
            print("Amount: 500")
        else:
            print("Amount: 1000")

s = Subscription(input(), input())
s.bill()
