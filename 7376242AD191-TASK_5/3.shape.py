class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        print(3.14*self.r*self.r)

r = float(input())
c = Circle(r)
c.area()
