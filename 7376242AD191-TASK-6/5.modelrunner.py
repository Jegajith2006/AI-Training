class Model:
    def predict(self):
        pass

class LinearModel(Model):
    def predict(self):
        print("Linear Prediction")

m = LinearModel()
m.predict()
