b = int(input())
d = int(input())
c = 0

if b < 20:
    print(0)
else:
    while b >= 20:
        b = b - d
        c = c + 1
    print(c)
