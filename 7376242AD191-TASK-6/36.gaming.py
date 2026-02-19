class Enemy:
    def action(self):
        pass

class Zombie(Enemy):
    def action(self):
        print("Zombie Attacks")

e = Zombie()
e.action()
