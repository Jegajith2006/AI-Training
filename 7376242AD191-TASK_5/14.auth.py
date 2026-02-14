class Login:
    def check(self, user, pwd):
        if user == "admin" and pwd == "123":
            print("Success")
        else:
            print("Fail")

l = Login()
l.check(input(), input())
