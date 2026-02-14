class Update:
    def apply(self, version):
        print("Updated to version", version)

u = Update()
u.apply(input())
