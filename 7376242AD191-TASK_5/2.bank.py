class Account:
    def __init__(self, no, name, bal):
        self.no = no
        self.name = name
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt

    def withdraw(self, amt):
        if amt <= self.bal:
            self.bal -= amt

    def show(self):
        print(self.bal)

no = input()
name = input()
bal = float(input())

a = Account(no, name, bal)
a.deposit(float(input()))
a.withdraw(float(input()))
a.show()
