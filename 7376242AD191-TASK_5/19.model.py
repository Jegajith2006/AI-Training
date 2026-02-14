class Model:
    def predict(self, x):
        print(x*2)

m = Model()
m.predict(int(input()))
