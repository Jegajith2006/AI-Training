n = int(input())

if n < 10000:
    r = 3
elif n <= 50000:
    r = 5
else:
    r = 7

i = (n * r) / 100 / 12
print(i)
