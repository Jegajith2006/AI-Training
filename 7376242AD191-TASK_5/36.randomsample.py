import random

data = input("Enter values: ").split()
k = int(input("How many samples: "))

print("Random Sample:", random.sample(data, k))
