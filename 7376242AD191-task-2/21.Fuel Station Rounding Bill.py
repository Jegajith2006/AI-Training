l = float(input())
p = float(input())

n = int(l * p)
d = n % 10

if d <= 4:
    n = n - d
else:
    n = n + (10 - d)

print(n)
