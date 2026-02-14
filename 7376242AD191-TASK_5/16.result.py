class Result:
    def grade(self, m):
        if m >= 90:
            print("A")
        else:
            print("B")

r = Result()
r.grade(int(input()))
