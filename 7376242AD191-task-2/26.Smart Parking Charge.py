n = int(input())

if n <= 2:
    c = n * 20
elif n <= 5:
    c = 40 + (n - 2) * 15
else:
    c = 85 + (n - 5) * 10

print(c)
