class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Borrowed")

b = Book(input())
b.borrow()
