class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print("Studying")

class Teacher(Person):
    def teach(self):
        print("Teaching")

s = Student(input())
s.study()
