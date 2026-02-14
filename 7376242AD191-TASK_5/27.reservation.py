class Reservation:
    def __init__(self):
        self.slots = []

    def book(self, time):
        if time not in self.slots:
            self.slots.append(time)
            print("Booked")
        else:
            print("Already Reserved")

r = Reservation()
r.book(input())
