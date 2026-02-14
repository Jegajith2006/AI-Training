class Student:
    def __init__(self, name, dept, cgpa, year):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        self.year = year

    def check(self):
        if self.cgpa >= 7 and self.year >= 3:
            print("Eligible")
        else:
            print("Not Eligible")

name = input()
dept = input()
cgpa = float(input())
year = int(input())

s = Student(name, dept, cgpa, year)
s.check()
