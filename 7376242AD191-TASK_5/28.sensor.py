class Sensor:
    def read(self, value):
        print("Sensor Data:", value)

s = Sensor()
s.read(input())
