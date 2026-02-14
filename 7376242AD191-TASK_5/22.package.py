class Package:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.status = "Pending"

    def update(self):
        self.status = "Delivered"
        print("Status:", self.status)

p = Package(input(), input())
p.update()
