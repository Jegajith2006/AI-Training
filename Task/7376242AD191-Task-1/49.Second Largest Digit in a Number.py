n = int(input())

l = -1
s = -1

while n > 0:
    d = n % 10

    if d > l :
        s = l
        l = d
    elif d < l and d > s:
        s = d

    n //= 10

print(s)
