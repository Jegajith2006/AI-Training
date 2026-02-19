class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def update_salary(self, amount):
        self.__salary += amount

    def show(self):
        print(self.__salary)

e = Employee(float(input()))
e.update_salary(float(input()))
e.show()
