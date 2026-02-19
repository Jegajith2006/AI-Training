class Workout:
    def calories(self):
        pass

class Running(Workout):
    def calories(self):
        print("Calories Burned: 300")

w = Running()
w.calories()
