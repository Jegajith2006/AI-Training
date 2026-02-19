import random

data = input().split()
sample = random.sample(data, 2)

print("Sample:", sample)
print("Count:", len(sample))
