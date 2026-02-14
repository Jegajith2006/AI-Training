class Exam:
    def __init__(self, sub, maxm):
        self.sub = sub
        self.maxm = maxm

    def result(self, mark):
        print(mark, "/", self.maxm)

e = Exam(input(), int(input()))
e.result(int(input()))
