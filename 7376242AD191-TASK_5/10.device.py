class Device:
    def __init__(self, id):
        self.id = id
        self.status = "OFF"

    def on(self):
        self.status = "ON"
        print("Turned ON")

d = Device(input())
d.on()
