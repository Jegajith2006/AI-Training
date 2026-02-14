class Character:
    def __init__(self, h, p):
        self.h = h
        self.p = p

    def attack(self):
        print("Damage:", self.p)

c = Character(int(input()), int(input()))
c.attack()
