class Config:
    def __init__(self, key):
        self.__key = key

    def show(self):
        print("Protected")

c = Config("123")
c.show()
