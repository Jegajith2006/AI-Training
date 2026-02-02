n = int(input())

min_time = int(input())

for i in range(n - 1):
    t = int(input())
    if t < min_time:
        min_time = t

print(min_time)
