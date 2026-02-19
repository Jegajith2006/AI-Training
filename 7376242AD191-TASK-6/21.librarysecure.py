class Book:
    def __init__(self, price):
        self.__price = price

    def update_price(self, amount):
        self.__price = amount

    def show(self):
        print("Price:", self.__price)

b = Book(float(input()))
b.update_price(float(input()))
b.show()
