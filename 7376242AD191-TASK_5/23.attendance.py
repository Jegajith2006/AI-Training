class Attendance:
    def __init__(self):
        self.present = []

    def mark(self, name):
        self.present.append(name)

    def show(self):
        print(self.present)

a = Attendance()
a.mark(input())
a.show()
