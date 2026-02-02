n = int(input())
t = n
has0 = False
while t > 0:
    if t % 10 == 0:
        has0 = True
    t //= 10
print("OPEN" if has0 and n%10==5 else "LOCKED")
