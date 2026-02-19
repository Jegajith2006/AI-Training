import random
import datetime

data = input("Enter data: ").split()
random.shuffle(data)

print("Shuffled Data:", data)
print("Training Time:", datetime.datetime.now())
