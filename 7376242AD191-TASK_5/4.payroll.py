class Employee:
    def __init__(self, name, des, sal):
        self.name = name
        self.des = des
        self.sal = sal

    def final(self):
        if self.des == "Manager":
            print(self.sal + 5000)
        else:
            print(self.sal + 2000)

e = Employee(input(), input(), float(input()))
e.final()
