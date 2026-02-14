class Ticket:
    def __init__(self, s, d, f):
        self.s = s
        self.d = d
        self.f = f

    def fare(self):
        print(self.f)

t = Ticket(input(), input(), float(input()))
t.fare()
