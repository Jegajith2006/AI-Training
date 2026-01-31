n = int(input())
s = 0

while n > 0:
    d = n % 10
    if d == 2 or d == 3 or d == 5 or d == 7:
        s += d
    n //= 10

print(s)

