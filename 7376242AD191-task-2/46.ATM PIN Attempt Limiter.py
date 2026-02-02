
p = int(input())
f = 0

for i in range(3):
    a = int(input())
    if a == p:
        f = 1
        break

if f == 1:
    print("ACCESS GRANTED")
else:
    print("CARD BLOCKED")
