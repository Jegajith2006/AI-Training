class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)

b = BankAccount(float(input()))
b.deposit(float(input()))
b.withdraw(float(input()))
b.show_balance()
