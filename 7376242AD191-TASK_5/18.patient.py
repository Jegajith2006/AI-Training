class Patient:
    def cost(self, cat):
        if cat == "General":
            print(500)
        else:
            print(1000)

p = Patient()
p.cost(input())
