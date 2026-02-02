n = int(input())
t = n
c = 0
f = 0

while t > 0:
    d = t % 10
    c = c + 1
    if d == 7:
        f = 1
    t //= 10

if c >= 6 and f == 1:
    print("STRONG")
else:
    print("WEAK")
