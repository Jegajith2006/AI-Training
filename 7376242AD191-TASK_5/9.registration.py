class Course:
    def __init__(self):
        self.students = []

    def register(self, name):
        if name not in self.students:
            self.students.append(name)

c = Course()
c.register(input())
print(c.students)
