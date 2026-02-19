class Employee:
    def salary(self):
        pass

class FullTime(Employee):
    def salary(self):
        print("Full-Time Salary")

class Contract(Employee):
    def salary(self):
        print("Contract Salary")

e = FullTime()
e.salary()
